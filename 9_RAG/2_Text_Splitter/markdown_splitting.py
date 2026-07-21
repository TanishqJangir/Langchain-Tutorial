from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
# Introduction to Python

Python is one of the most popular programming languages in the world. It is easy to learn, readable, and widely used for web development, automation, data analysis, artificial intelligence, and scripting.

## Why Learn Python?

Some advantages of Python include:

- Simple syntax
- Large community
- Extensive libraries
- Cross-platform support
- Fast development

## Variables

Variables are used to store data.

```python
name = "Alice"
age = 22
is_student = True
```

Python automatically determines the data type based on the assigned value.

## Functions

Functions help organize reusable code.

```python
def greet(name):
    return f"Hello, {name}!"
```

Functions can take parameters and return values.

## Loops

Python supports both `for` and `while` loops.

```python
for i in range(5):
    print(i)
```

Loops are useful for repeating tasks without writing the same code multiple times.

## Lists

Lists are ordered collections of items.

```python
fruits = ["Apple", "Banana", "Orange"]
```

Common list operations include adding, removing, and accessing elements.

## Dictionaries

A dictionary stores data as key-value pairs.

```python
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A"
}
```

Dictionaries allow fast lookup using keys.

## Conclusion

Python is an excellent language for beginners and professionals alike. Learning its fundamentals provides a strong foundation for exploring advanced topics such as web development, machine learning, and data science.
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.MARKDOWN,
    chunk_size=300,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))

print(chunks[0])