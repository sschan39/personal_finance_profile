# Personal Finance Monitor

This project is a web application designed to monitor and save personal finance profiles using the Yahoo Finance API. It is built with FastAPI and provides a simple interface for users to manage their financial data.

## Project Structure

```
personal-finance-monitor
├── app
│   ├── main.py               # Entry point of the application
│   ├── routers
│   │   └── finance.py        # API routes for finance-related operations
│   ├── models
│   │   └── profile.py        # Data model for personal finance profiles
│   ├── services
│   │   └── yahoo_finance.py  # Functions to interact with Yahoo Finance API
│   └── database.py           # Database connection and operations
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables for configuration
├── README.md                 # Project documentation
└── .gitignore                # Files and directories to ignore in version control
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/personal-finance-monitor.git
   cd personal-finance-monitor
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables in the `.env` file. You will need to provide your Yahoo Finance API key and database connection string.

## Usage

To run the application, execute the following command:
```
uvicorn app.main:app --reload
```

You can access the API documentation at `http://127.0.0.1:8000/docs` after starting the server.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.