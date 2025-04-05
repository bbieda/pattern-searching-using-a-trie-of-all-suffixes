import tkinter as tk
from collections import defaultdict

# TrieNode definition
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        node.is_end_of_word = True

    # Search for words that start with a given prefix
    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect_all_words(node, prefix)

    # Collect all words that start from the given node
    def _collect_all_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, next_node in node.children.items():
            words.extend(self._collect_all_words(next_node, prefix + char))
        return words

# Graph definition to store relationships and weights between titles
class TitleGraph:
    def __init__(self):
        # Dictionary to hold connections and weights
        self.graph = defaultdict(dict)

    # Add a connection between two titles with a given weight
    def add_connection(self, title1, title2, weight=1):
        self.graph[title1][title2] = weight
        self.graph[title2][title1] = weight

    # Get related titles sorted by the weight of their connections
    def get_related_titles(self, title):
        if title not in self.graph:
            return []
        # Sort the related titles by their weight (in descending order)
        return sorted(self.graph[title].items(), key=lambda x: x[1], reverse=True)

# Simple GUI using Tkinter
class AutoCompleteApp:
    def __init__(self, root, trie, graph):
        self.root = root
        self.trie = trie
        self.graph = graph
        self.root.title("Auto-Complete and Recommendation System")

        # Creating a label and entry for user input
        self.label = tk.Label(root, text="Enter text:")
        self.label.pack()

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()
        self.entry.bind("<KeyRelease>", self.on_key_release)

        # Creating a listbox to show suggestions
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        # Creating a label and listbox to show recommendations
        self.rec_label = tk.Label(root, text="Recommendations:")
        self.rec_label.pack()
        self.recommendations = tk.Listbox(root, width=50, height=5)
        self.recommendations.pack()

    # Function called on key release to update suggestions
    def on_key_release(self, event):
        # Clear current suggestions
        self.listbox.delete(0, tk.END)
        self.recommendations.delete(0, tk.END)  # Clear previous recommendations

        # Get the current text from the entry
        user_input = self.entry.get()

        if user_input:
            # Get suggestions from the Trie
            suggestions = self.trie.search_prefix(user_input)

            # Add suggestions to the listbox
            for suggestion in suggestions:
                self.listbox.insert(tk.END, suggestion)

    # Function called when a title is selected
    def on_select(self, event):
        # Get the selected title from the listbox
        try:
            selected_index = self.listbox.curselection()[0]
            selected_title = self.listbox.get(selected_index)
        except IndexError:
            return

        # Clear previous recommendations
        self.recommendations.delete(0, tk.END)

        # Get the related titles from the graph based on weights
        related_titles = self.graph.get_related_titles(selected_title)

        # Add related titles to the recommendations listbox
        for title, weight in related_titles:
            self.recommendations.insert(tk.END, f"{title} (Weight: {weight})")

# Sample data: tytuły z powiązaniami i wagami
queries = [
    "Harry Potter", "Haruki Murakami", "Harper Lee", "Hobbit", "Narnia", "Władca Pierścieni"
]

# Create the Trie and insert sample queries
trie = Trie()
for query in queries:
    trie.insert(query)

# Create the graph and add connections (title1, title2, weight)
graph = TitleGraph()
graph.add_connection("Harry Potter", "Hobbit", 5)
graph.add_connection("Harry Potter", "Władca Pierścieni", 3)
graph.add_connection("Hobbit", "Władca Pierścieni", 4)
graph.add_connection("Haruki Murakami", "Kafka on the Shore", 7)
graph.add_connection("Harper Lee", "To Kill a Mockingbird", 6)
graph.add_connection("Władca Pierścieni", "Narnia", 2)

# Create the application window and run the app
root = tk.Tk()
app = AutoCompleteApp(root, trie, graph)
root.mainloop()
