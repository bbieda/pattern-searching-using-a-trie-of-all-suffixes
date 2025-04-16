## Zadanie 1: Implementacja Trie i najdłuższego wspólnego prefiksu

**Opis:**

Zaimplementuj strukturę Trie, która pozwala na wstawianie słów oraz znalezienie najdłuższego wspólnego prefiksu dla wszystkich wstawionych słów.

**Napisz klasę `Trie` z metodami:**

- `insert(word: str)` – dodaje słowo do drzewa
- `longest_common_prefix(total_words: int)` – zwraca najdłuższy wspólny prefiks, który zawierają wszystkie wstawione słowa

Następnie napisz funkcję `longestCommonPrefix(strs: List[str])`, która korzysta z powyższej klasy, aby znaleźć najdłuższy wspólny prefiks w liście słów.

**Przykład:**

```python
words = ["flower", "flow", "flight"]
print(longestCommonPrefix(words))  # "fl"

words = ["dog", "racecar", "car"]
print(longestCommonPrefix(words))  # ""
```
---

## Zadanie 2: Czy dane słowo jest prefiksem innego słowa w Trie?

**Opis:**

Zaimplementuj metodę `is_prefix_of_other(word: str) -> bool` w klasie Trie.  
Funkcja ma zwrócić `True`, jeśli dane słowo jest prefiksem innego słowa znajdującego się w Trie, ale samo nie jest końcem słowa (lub jeśli są słowa dłuższe z tym samym początkiem).

**Przykład:**

```python
trie = Trie()
trie.insert("car")
trie.insert("cart")
trie.insert("carbon")

trie.is_prefix_of_other("car")     # True  ("car" jest prefiksem "cart", "carbon")
trie.is_prefix_of_other("cart")    # False (nie ma dłuższego słowa zaczynającego się od "cart")
trie.is_prefix_of_other("carbon")  # False (nie ma innego słowa z tym prefiksem)
```

---

## Zadanie 3: Czy dane słowo istnieje w Trie?

**Opis:**

Dodaj metodę `search(word: str) -> bool`, która sprawdza, czy dane słowo zostało wcześniej wstawione do Trie.

**Przykład:**

```python
trie = Trie()
trie.insert("banana")
trie.search("ban")      # False
trie.search("banana")   # True
```

