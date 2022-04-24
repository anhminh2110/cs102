# steamvalley
Python game for CS 102

# Structure

* Dung 1 repo cho nhieu games trong qua trinh thu nghiem, cac ban bat dau viet thu game thi hay tao moi game 1 folder roi thoai mai push code len `master` branch.
* Version chinh thuc nam rieng trong `steamvalley/`. Doi voi folder nay, ko push code len `master` branch ma phai thong qua PR va code review process.

# Setup Development Env

* Clone repo
* Create python virtualenv with python3: `python3 -m venv venv`
* Activate virtualenv: `source venv/bin/activate`
* Go to main game folder and run:
 
```
cd steamvalley
python main.py
```

# Development History

* Use GameManager class to manage game loop
* Move collected item state into player class
* Move config values into @dataclass classes
* Implement World