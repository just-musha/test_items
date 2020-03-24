### What is it
Task from Stepic.org course ["Test Automation with Python and Selenium"](https://stepik.org/course/575/)

Step 3.6 Task: Run test for different interface languages

#### Test example
Test checks if button is present on page.
Accepts ```language``` parameter. Languages: ```ru, en, fr, es```

#### How to run

```
$ pipenv install
$ pipenv shell
$ pytest --language=es test_items.py
```
