import tkinter as tk
from collections import defaultdict
import csv

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, value):
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.words.append(value)

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect_words(node)

    def _collect_words(self, node):
        results = []
        if node.is_end_of_word:
            results.extend(node.words)
        for child in node.children.values():
            results.extend(self._collect_words(child))
        return results

class AutoCompleteApp:
    def __init__(self, root, title_trie, author_trie):
        self.root = root
        self.title_trie = title_trie
        self.author_trie = author_trie

        self.root.title("Auto-Complete by Title and Author")

        self.label = tk.Label(root, text="Enter title or author:")
        self.label.pack()

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()
        self.entry.bind("<KeyRelease>", self.on_key_release)

        self.listbox = tk.Listbox(root, width=60, height=20)
        self.listbox.pack()

    def on_key_release(self, event):
        self.listbox.delete(0, tk.END)
        user_input = self.entry.get().strip().lower()
        if not user_input:
            return

        # Search by title
        title_matches = self.title_trie.search_prefix(user_input)
        for title, author in sorted(set(title_matches))[:50]:
            self.listbox.insert(tk.END, f"{title}, {author}")

        # Search by author
        author_matches = self.author_trie.search_prefix(user_input)
        for author, title in sorted(set(author_matches))[:50]:
            self.listbox.insert(tk.END, f"{title}, {author}")

# Tries
title_trie = Trie()
author_trie = Trie()

# Load data
file = "GoodReads_100k_books_test_1.txt"

# Zmienic w zaleznosci od kodowania pliku
# with open(file, newline='', encoding='utf-8-sig') as f:
# with open(file, newline='', encoding='utf-8') as f:
# with open(file, newline='', encoding='windows-1252') as f:
# with open(file, newline='', encoding='iso-8859-1') as f:
with open(file, newline='', encoding='iso-8859-1') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 2:
            continue
        authors_raw, title = row[0].strip(), row[1].strip()
        title_lower = title.lower()

        # Rozdziel wielu autorów
        authors = [a.strip() for a in authors_raw.split(",") if a.strip()]
        for author in authors:
            author_lower = author.lower()

            # Wstaw dane do obu Trie
            title_trie.insert(title_lower, (title, author))
            author_trie.insert(author_lower, (author, title))

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = AutoCompleteApp(root, title_trie, author_trie)
    root.mainloop()
