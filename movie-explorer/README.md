# Movie Explorer

Movie Explorer is a simple Python project for exploring movies, managing favorites, and running tests.

## Project Structure

```
movie-explorer/
├── movie_explorer/
│   ├── __init__.py
│   ├── api.py
│   ├── favorites.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_favorites.py
│   └── test_utils.py
├── main.py
├── requirements.txt
└── README.md
```

## Features

- Search for movies using an API (to be implemented in `api.py`)
- Manage favorite movies (`favorites.py`)
- Utility functions (`utils.py`)
- Unit tests for all modules (`tests/`)

## Getting Started

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```
   python main.py
   ```

3. **Run tests:**
   ```
   pytest
   ```

## Contributing

Feel free to fork this repository and submit pull requests.

## License

This project is licensed under the MIT License.