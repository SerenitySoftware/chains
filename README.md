# Chains
Chains is a Python library that provides easy, safe navigation for complex objects.

```python

from chains import Chain

raw = {
    "never": {
        "gonna": {
            "give": {
                "you": {
                    "up": "never gonna let you down"
                }
            }
        }
    },
    "artists": [
        {
            "name": "Rick Astley",
            "genre": "Pop"
        },
        {
            "name": "Michael Jackson",
            "genre": "Pop"
        }
    ]
}
data = Chain(raw)


# Accessing nested dict keys that may or may not exist
print(data.never.gonna.give.you.up)  # "never gonna let you down"
print(data.let.you.down)  # None

# Navigating through lists
print(data.artists[0].name)  # "Rick Astley"
print(data.artists[1].name)  # "Michael Jackson"
print(data.artists[2].name)  # None
```


## Installation and Support
Chains is available on PyPI, so you can install it like any other Python package, using the packager of your choice.

```bash
pip install chains
```

Chains is [automatically tested with 100% coverage](https://github.com/SerenitySoftware/chains/blob/master/.github/workflows/verify.yml) on Python 3.8 and above for Ubuntu, macOS, and Windows.


## Why Chains?

Chains makes data navigation easy and safe so you don't have to constantly null-check, coalesce, try/except, and if/else.

You want data? Just go get it.

Simply wrap your raw data in a `Chain` object, which allows you to access its attributes using the dot notation.
If a key, attribute, or list index does not exist, the Chain object will return `None` instead of raising an exception.

This is particularly useful when dealing with complex data structures, such as JSON responses from APIs, where you can't always guarantee the presence of every key or index.

## Usage
Chains aims to be as simple and intuitive as possible, so you can use it without having to write tons of code for null-checking and type validation.

For the most part, you can just use Chains and pretend that you're working with the raw data directly.
However, there are some important differences to be aware of, especially when working with scalar values, arithmetic operations, and identity comparisons.

### Usage: Scalar values
Chains allows you to seamlessly work with scalar values, such as strings, integers, and Booleans.
This allows you to operate on your data naturally.

```python
data = Chain({
    "name": "John Doe",
    "age": 30,
    "is_active": True
})

print(data.name)  # "John Doe"
print(data.age)  # 30
print(data.is_active)  # True
```

You can operate at any point on the Chain object, and it will return the expected result.

```python
data = Chain({
    "name": "John Doe",
    "age": 30,
    "is_active": True
})

print(data.name.upper())  # "JOHN DOE"
print(data.age + 10)  # 40
```


### Usage: Numeric values and arithmetic operations
Chains allows you to work with numeric values and perform arithmetic operations on them,
but certain operations work differently from usual to ensure that you don't raise errors,
such as coercing `None` values to zero.

```python
data = Chain({
    "price": 100,
    "quantity": 5
})

print(data.price * data.quantity)  # 500
print(data.missing + 10)  # 10
print(data.quantity ** 3)  # 125

# Chains even allows division by zero, returning None instead.
# Not even Stephen Hawking could do that.
print(data.missing / 0)  # None
```

### Usage: Lists and other iterables
Chains allows you to work with lists, sets, and other iterables in a natural way.
You can access items by index and iterate over them. If they don't exist, Chains will return `None`.


```python
data = Chain({
    "names": ["Alice", "Bob", "Charlie"]
})

print(data.names[0])  # "Alice"
print(data.names[50])  # None

for index, name in enumerate(data.names):
    print(name)
```

### Working with dicts and nested data
Chains allows you to work with nested data structures quickly and easily. No more null-checking or catching KeyErrors.

```python
data = Chain({
    "user": {
        "name": "Alice",
        "address": {
            "city": "Wonderland",
            "country": "Fairyland"
        }
    }
})

print(data.user.name)  # "Alice"
print(data.user.address.city)  # "Wonderland"
print(data.this.is.missing)  # None
```


### Usage: Special values and identity comparisons
When you access items in a chain, it's not directly returning the value, it's returning a `Chain` wrapping the value.
A `Chain` is a very powerful and dynamic object that allows all sorts of operations on it, but it's not the same as the raw value.

This means there are a few special cases to be aware of. Because values are wrapped in a `Chain`, you can't use the identity operator `is` to check if a value is `None`, `True`, or `False` like usual.

But good news! If you want to compare identity, you can call the key like it's a function, and it'll return the raw value.

```python

data = Chain({
    "name": "John Doe",
    "age": 30,
    "is_active": True
})
print(data.is_active is True)  # False :(
print(data.missing.key is None)  # False :(
print(data.is_active() is True)  # True :)
print(data.missing.key() is None)  # True :)
```

### Usage: Navigating reserved words and invalid keys
Certain names are reserved in Python, so if your data contains keys that are reserved words or against the Python grammar,
you can still access them by using the square bracket notation. In fact, you never have to use the dot notation if you hate it! Either way Chains will make sure it's safe navigation.

```python
data = Chain({
    "123": "Hello World!",
    "jeffrey-epstein": "Didn't kill himself"
})

print(data.123)  # SyntaxError :(
print(data["123"])  # "Hello World!"

print(data.jeffrey-epstein)  # SyntaxError :(
print(data["jeffrey-epstein"])  # "Didn't kill himself"
```


## Contributing
Feel free to report bugs and suggest features through GitHub Issues, or open a PR for improvements.
