# aph
Automatic Python Help. A CLI tool that generates docstrings for a Python source file using GPT-3 (OpenAI).

## Rationale
Well, I am too lazy to write my own docstrings so I shall let AI do it for me. Whether the results are good or bad - thats up to luck.

## Installation
Clone the repo
```py
git clone https://github.com/recreationx/aph
```
## GPT3 OpenAI API Key
Get an API Key [here](https://openai.com/blog/openai-api/).

## Example usage
An example file will look like this. Docstrings will specifically start with `"""` for it to be processed by the tool.
```py
def delete_folder():
    """A to be replaced, manual string"""
    pass

def open_process_with_pid():
    """"""
    # Empty docstrings works too!
    pass
```

Run the tool
```
aph.py filename output api_key
```

An intended output will look something like
```py
def delete_folder():
    """This function deletes a folder from the current directory."""
    pass

def open_process_with_pid():
    """This function opens a process with a given PID."""
    # Empty docstrings works too!
    pass

```

To ensure more accurate results, use more descriptive and self-explanatory function names!

## Contributing

Open a PR.