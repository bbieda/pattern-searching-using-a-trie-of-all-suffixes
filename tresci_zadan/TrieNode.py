# Definicja klasy TrieNode

class TrieNode:
    def __init__(self):
        self.children = {}         # słownik: klucz to litera, wartość to kolejny TrieNode
        self.is_end = False        # True, jeśli w tym węźle kończy się słowo
        self.count = 0             # liczba słów przechodzących przez ten węzeł
