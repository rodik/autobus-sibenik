# Contributing to This Project

Thank you for considering contributing! Here are some guidelines to get you started:

## Getting Started

1. **Fork** the repository.
2. **Clone** your fork:
``` sh
git clone https://github.com/your-username/autobus-sibenik.git 
```
3. (optional) **Create python virtual env**
``` sh
# create vitual env if you want to modify and/or run the obrada.py script locally
python3 -m venv .venv
``` 
4. **Create a new branch** for your changes:
``` sh
git checkout -b your-branch-name
```

## Izmjene voznog reda

U odgovarajućem json-u napraviti izmjenu:

### Primjer izmjene polazaka
```diff
"polasci": {
    "ponedjeljak-subota": [
        ...
        "12:50",
        "14:15",
-       "15:15",
+       "15:20", # bus u 15:15 pomaknut na 15:20
        "16:15",
        "17:15",
        ...
    ],
    "nedjelja": [
+       "06:50", # novi polazak
        "07:40",
        "08:40",
        "09:40",
        "10:40",
-       "11:40", # ukinut polazak
        "12:40",
        ...
    ]
}
```
### Primjer izmjena stanica i udaljenosti
```diff
"stanice": {
    "AK": 0,
    "Tržnica": 2,
    "Baldekin B": 3,
-   "Križ B": 1, # ukinuta stanica
    "Bioci B": 1,
-   "Put Egera B": 4,
+   "Put Egera B": 3, # skraćen razmak između stanica
    "TLM B": 1,
    "Rezalište B": 5,
    "Maratuša B": 3,
    "Rešačka": 4,
    "Brodarica": 1
}
```

## Coding Guidelines

- Please follow our coding standards (include links to any style guides).
- Ensure all new features and changes are well-documented.

## Pull Requests

1. Ensure your changes are committed with clear, descriptive messages.
2. Push your changes:
``` sh
git push origin your-branch-name
```

3. Open a **pull request** to the main branch. Provide a detailed description of your changes.

Thank you for contributing!
