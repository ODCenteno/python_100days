

### API's used for this project
* [NEWS API](https://newsapi.org/docs/endpoints/everything)
* [Stock API - Alpha Vantage](https://www.alphavantage.co/)


### Getting the Environment Variables Keys
`import os`

Using `get()` will return `None` if a key is not present rather than raise a `KeyError`:

* `print(os.environ.get('KEY_THAT_MIGHT_EXIST'))`

`os.getenv` is equivalent, and can also give a default value instead of `None`:
* `print(os.getenv('KEY_THAT_MIGHT_EXIST', default_value))`