import tkinter as tk
from collections import defaultdict

# TrieNode and Trie classes
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        node.is_end_of_word = True

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect_all_words(node, prefix)

    def _collect_all_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, next_node in node.children.items():
            words.extend(self._collect_all_words(next_node, prefix + char))
        return words

# GUI
class AutoCompleteApp:
    def __init__(self, root, title_trie, author_trie, title_to_author, author_to_titles):
        self.root = root
        self.title_trie = title_trie
        self.author_trie = author_trie
        self.title_to_author = title_to_author
        self.author_to_titles = author_to_titles
        self.search_by = "title"  # domyślnie

        self.root.title("Auto-Complete (Title & Author)")

        self.label = tk.Label(root, text="Enter title or author:")
        self.label.pack()

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()
        self.entry.bind("<KeyRelease>", self.on_key_release)

        self.switch_button = tk.Button(root, text="Search by: Title", command=self.switch_mode)
        self.switch_button.pack(pady=5)

        self.listbox = tk.Listbox(root, width=60, height=15)
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

    def switch_mode(self):
        self.search_by = "author" if self.search_by == "title" else "title"
        self.switch_button.config(text=f"Search by: {'Author' if self.search_by == 'author' else 'Title'}")
        self.on_key_release(None)

    def on_key_release(self, event):
        self.listbox.delete(0, tk.END)
        user_input = self.entry.get().strip().lower()

        if not user_input:
            return

        if self.search_by == "title":
            suggestions = self.title_trie.search_prefix(user_input)
            for title in suggestions[:100]:
                author = self.title_to_author.get(title, "Unknown")
                self.listbox.insert(tk.END, f"{title.title()}, {author.title()}")
        else:  # search by author
            suggestions = self.author_trie.search_prefix(user_input)
            for author in suggestions[:50]:
                titles = self.author_to_titles.get(author, [])
                for title in titles[:3]:  # max 3 tytuły na autora
                    self.listbox.insert(tk.END, f"{title.title()}, {author.title()}")

    def on_select(self, event):
        # Możesz dodać reakcję po kliknięciu
        pass

# Przygotowanie struktur
title_trie = Trie()
author_trie = Trie()
title_to_author = {}
author_to_titles = defaultdict(list)

# Wczytywanie danych z pliku
with open("book_titles_sorted.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or ',' not in line:
            continue
        title, author = map(str.strip, line.split(',', 1))
        title_lower = title.lower()
        author_lower = author.lower()

        title_trie.insert(title_lower)
        author_trie.insert(author_lower)

        title_to_author[title_lower] = author
        author_to_titles[author_lower].append(title)

# Uruchomienie aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    app = AutoCompleteApp(root, title_trie, author_trie, title_to_author, author_to_titles)
    root.mainloop()
