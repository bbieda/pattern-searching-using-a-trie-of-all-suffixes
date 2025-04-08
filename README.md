# 📚 Auto-uzupełnianie tytułów książek i autorów (Trie + Tkinter)

To prosta aplikacja graficzna napisana w Pythonie z użyciem biblioteki Tkinter, która umożliwia wyszukiwanie książek po tytule lub autorze. Do realizacji wyszukiwania wykorzystano strukturę danych Trie (drzewo prefiksowe), co pozwala na szybkie dopasowywanie wpisywanych fragmentów.

Dane wykorzystane w aplikacji pochodzą z serwisu Kaggle: https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k

---

## 🔍 Funkcje

- Automatyczne uzupełnianie wpisywanych prefiksów.
- Obsługa dwóch trybów wyszukiwania – po tytule lub po autorze.
- Przycisk do przełączania trybu wyszukiwania.
- Wyświetlanie wyników w czasie rzeczywistym podczas wpisywania.
- Obsługa autorów zapisanych w cudzysłowie, nawet jeśli zawierają przecinki w imieniu i nazwisku.

---

## 🗂 Format danych wejściowych

Program czyta dane z pliku `.txt`, w którym każda linia ma format: autor,tytuł książki

Przykład:

Plik może zawierać wielu autorów rozdzielonych przecinkami. Program poprawnie to obsługuje dzięki użyciu parsera CSV z odpowiednim kodowaniem (`Windows-1252`).

---

## 🚀 Uruchamianie aplikacji

1. Umieść plik danych (np. `GoodReads_100k_books.txt`) w tym samym folderze co skrypt `prefix_trie.py`.
2. Uruchom program:
```bash
python prefix_tree.py
```

---

## ⚙️ Wymagania
Python 3.x

Wbudowane biblioteki: tkinter, collections, csv

Nie są wymagane żadne zewnętrzne zależności.

## 🧠 Wykorzystane technologie
Trie (drzewo prefiksowe) – do szybkiego dopasowywania wpisywanych fraz.

Tkinter – graficzny interfejs użytkownika.

CSV z kodowaniem Windows-1252 – poprawna obsługa znaków specjalnych, np. ©.

## ✍️ Autorzy
Bartłomiej Bieda, Bartosz Śnieg
