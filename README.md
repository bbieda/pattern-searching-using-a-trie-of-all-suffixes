# 🇬🇧📚 Auto-complete System for Book Titles and Authors Using Trie Tree

This is a simple graphical application written in Python using the Tkinter library. It allows users to search for books by title or author. The search feature is powered by the Trie (prefix tree) data structure, which enables fast matching of typed fragments.

The dataset used in this application comes from Kaggle: https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k

## 🔍 Features

- Auto-completion of typed prefixes.
- Two search modes – by title or by author.
- A button to toggle between search modes.
- Real-time display of results as the user types.
- Proper handling of authors listed in quotes, even if they contain commas in their names.

## 🗂 Input Data Format

The program reads data from a `.txt` file, where each line has the format:
author, title

The file may include multiple authors separated by commas. The program handles this correctly by using a CSV parser with the proper encoding (`Windows-1252`).

## 🚀 Running the Application

1. Place the data file (e.g. `GoodReads_100k_books.txt`) in the same folder as the script `prefix_trie.py`.
2. Run the application:
   python prefix_trie.py

## ⚙️ Requirements

- Python 3.x  
- Built-in libraries: `tkinter`, `collections`, `csv`

No external dependencies required.

## 🧠 Technologies Used

- Trie (prefix tree) – for efficient prefix matching.
- Tkinter – for the graphical user interface.
- CSV with Windows-1252 encoding – to properly handle special characters like ©.

---

# 🇵🇱📚 System auto-uzupełniania tytułów książek i autorów z wykorzystaniem drzewa Trie

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

Program czyta dane z pliku `.txt`, w którym każda linia ma format:
autor, tytuł


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
