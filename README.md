# web3

my-hedera-app/
├── smart-contracts/
│   └── deploy.js
|   └── contracts/
│       └── TokenCounter.sol
├── static/
│   ├── css/
│   │   └── custom.css
│   └── js/
│       └── hashconnect.js
├── templates/
│   ├── base.html
│   ├── home/
│   │   └── index.html
│   ├── hedera/
│   │   ├── connect.html
│   │   └── counter.html
│   └── auth/
│       └── dashboard.html  # No login page needed, just dashboard
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── db.py             # Database setup
│   ├── home/
│   │   └── routes.py
│   ├── hedera/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── blockchain.py
│   └── auth/
│       ├── __init__.py
│       └── routes.py
├── instance/             # SQLite database location
│   └── app.db
├── requirements.txt
└── flask_app.py


## Old one just for reference to know how to deploy solidity from code which is mentioned in only below formate, may be search on grok how to do.
hedera-flask-dapp/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   └── main.py
│   ├── static/
│   │   ├── hashconnect.js
│   │   └── app.js
│   └── templates/
│       ├── index.html
│       └── dashboard.html
├── smart-contracts/
│   ├── contracts/
│   │   └── Counter.sol
│   └── deploy.js
├── .env
├── requirements.txt
└── run.py