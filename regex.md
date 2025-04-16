## 🔍 What is Regex (Regular Expression)?

**Regex** is a way to describe patterns in text. In Python, it's used to **search**, **match**, or **replace** parts of strings.

To use regex in Python, you need to import the `re` module:

```python
import re
```

---

## 🧱 Basic Structure

A regex pattern is a **string** that defines a rule to match certain characters.

Here’s a super basic example:

```python
pattern = r"cat"
text = "I have a cat."
match = re.search(pattern, text)
print(match)
```

It checks if `"cat"` is in the text.

---

## 🧠 Regex Symbols (The Magic Part)

Here are **important symbols** you’ll use a lot:

| Symbol | Meaning                            | Example      | Matches                         |
|--------|-------------------------------------|--------------|----------------------------------|
| `.`    | Any character except newline        | `c.t`        | `cat`, `cut`, `c9t`              |
| `^`    | Start of string                     | `^Hello`     | `Hello world`                    |
| `$`    | End of string                       | `world$`     | `Hello world`                    |
| `*`    | 0 or more of previous character     | `lo*`        | `l`, `lo`, `loo`, `looo`...      |
| `+`    | 1 or more of previous character     | `lo+`        | `lo`, `loo`, `looo`...           |
| `?`    | 0 or 1 of previous character        | `lo?`        | `l`, `lo`                        |
| `{n}`  | Exactly n times                     | `a{3}`       | `aaa`                            |
| `{n,}` | At least n times                    | `a{2,}`      | `aa`, `aaa`, `aaaa`...           |
| `[]`   | Any one character inside brackets   | `[aeiou]`    | Any vowel                        |
| `|`    | OR                                  | `cat|dog`    | Matches `cat` or `dog`           |
| `()`   | Grouping                           | `(ha)+`      | `ha`, `haha`, `hahaha`...        |
| `\d`   | Any digit (0-9)                     | `\d+`        | `123`, `4567`                    |
| `\w`   | Any word character (a-z, A-Z, 0-9, _) | `\w+`      | `word123`                        |
| `\s`   | Any whitespace (space, tab, etc.)   | `\s+`        | Matches space, tab               |

---

## ✅ Examples

### 1. **Check if a string contains a digit**

```python
import re

text = "My number is 123"
if re.search(r"\d+", text):
    print("Contains a number!")
```

### 2. **Find all words in a sentence**

```python
text = "Hello, I love Python3"
words = re.findall(r"\w+", text)
print(words)  # ['Hello', 'I', 'love', 'Python3']
```

### 3. **Replace all digits with #**

```python
text = "My PIN is 1234"
new_text = re.sub(r"\d", "#", text)
print(new_text)  # My PIN is ####
```

---


## 🧪 1. Regex Functions in Python (`re` module)

| Function        | Description                                     |
|-----------------|-------------------------------------------------|
| `re.search()`   | Searches for the first match                    |
| `re.match()`    | Checks match **only at the beginning**          |
| `re.fullmatch()`| Checks if the **entire string** matches         |
| `re.findall()`  | Returns **all** non-overlapping matches         |
| `re.finditer()` | Returns match objects as an **iterator**        |
| `re.sub()`      | Replaces parts of the string                    |
| `re.compile()`  | Compiles a regex pattern for reuse              |

---

## 🔄 2. Match Object and Groups

When you use `re.search()` or `re.match()`, you get a **match object**, not just a True/False.

```python
match = re.search(r"(\d+)", "User ID: 54321")

if match:
    print("Match:", match.group(0))     # whole match
    print("Group 1:", match.group(1))   # first group (digits)
```

You can also name groups:

```python
text = "Name: John, Age: 25"
match = re.search(r"Name: (?P<name>\w+), Age: (?P<age>\d+)", text)
print(match.group("name"))  # John
print(match.group("age"))   # 25
```

---

## 📦 3. Greedy vs Non-Greedy Matching

Regex is **greedy by default**, meaning it matches as much as possible.

```python
text = "<p>Hello</p><p>World</p>"
re.findall(r"<p>.*</p>", text)  # ['<p>Hello</p><p>World</p>']
```

**Solution: use non-greedy (lazy) quantifier `*?`**

```python
re.findall(r"<p>.*?</p>", text)  # ['<p>Hello</p>', '<p>World</p>']
```

---

## 🧹 4. Lookahead and Lookbehind (Zero-width assertions)

These don’t consume characters, just **assert** if a condition is met.

### ✅ Positive Lookahead `(?=...)`

```python
re.findall(r"\w+(?=@)", "user@example.com")  # ['user']
```

→ Match a word that comes before @

### ❌ Negative Lookahead `(?!...)`

```python
re.findall(r"\b(?!cat)\w+", "cat dog bat")  # ['dog', 'bat']
```

→ Excludes 'cat'

### 🔙 Lookbehind `(?<=...)`

```python
re.findall(r"(?<=\$)\d+", "Price: $100")  # ['100']
```

→ Match number only if preceded by `$`

---

## 🛠 5. `re.compile()` and Flags

Use `re.compile()` when reusing a pattern:

```python
pattern = re.compile(r"\d+")
print(pattern.findall("12 cats and 30 dogs"))
```

### Common Flags

```python
re.IGNORECASE or re.I  → ignore case
re.DOTALL     or re.S  → `.` matches newlines too
re.MULTILINE  or re.M  → `^` and `$` match at every line
```

Example:

```python
pattern = re.compile(r"^hello", re.MULTILINE)
text = "hello\nworld\nhello again"
print(pattern.findall(text))  # ['hello', 'hello']
```

---

## 🧪 6. Practice Challenge (Try this out!)

Here’s a small challenge for you:

```python
text = """
Name: Alice, Email: alice@example.com
Name: Bob, Email: bob@hello.co.uk
"""

pattern = r"Name: (\w+), Email: ([\w.-]+@[\w.-]+\.\w+)"
```

Can you use `re.findall()` to extract a list of tuples like:

```python
[('Alice', 'alice@example.com'), ('Bob', 'bob@hello.co.uk')]
```

---

## 🎁 Pro Tips

1. **Test your regex online:**  
   Try [regex101.com](https://regex101.com) (it explains everything)
   
2. **Break patterns into parts.** Don’t try to write complex ones in one go.

3. **Use raw strings `r""`** to avoid escaping every backslash `\\`.
