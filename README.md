# **Midterm Lab Exam Question: Working With GitHub and CI/CD**

## **Instructions**

### **Objective**  
The goal of this lab exam is to **install a Python library**, **write basic code**, and **fix a failing test** in your project. You will also use **GitHub** to track your progress and complete the quiz.

---

## **Step-by-Step Instructions**

### **1. Create a New GitHub Repository** (4 pts)

1. Log in to your GitHub account.
2. Create a **new private repository** named `PythonQuiz`.
3. Add a **README** to the repository.
4. Invite me (`delveccj`) as a collaborator.

---

### **2. Clone the Repository Locally**

1. Open your terminal and clone the repository:
   ```bash
   git clone <your-repo-url>
   cd PythonQuiz
   ```

---

### **3. Install Required Library** (4 pts)

1. You will use the **`requests` library** for this quiz.
2. Install the library:
   ```bash
   pip install requests
   ```
3. Create a `requirements.txt` file with the following content:
   ```
   requests
   ```

---

### **4. Write a Simple Script to Fetch a Web Page**

Create a Python file named `fetch_page.py` with the following content:

```python
import requests

def fetch_website_content(url):
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "https://example.com"
    content = fetch_website_content(url)
    print(content[:100])  # Print only the first 100 characters
```

---

### **5. Write a Failing Unit Test**

Create a file named `test_fetch_page.py` with the following content:

```python
import unittest
from fetch_page import fetch_website_content

class TestFetchPage(unittest.TestCase):
    def test_fetch_website_content(self):
        content = fetch_website_content("https://example.com")
        self.assertIn("<h1>Example Domain</h1>", content)  # This will fail initially

if __name__ == "__main__":
    unittest.main()
```

---

### **6. Fix the Failing Test** (4 pts)

1. **Run the unit test** to confirm it fails:
   ```bash
   python3 -m unittest test_fetch_page.py
   ```
2. The test fails because the **assertion text is slightly incorrect**. Update the `test_fetch_page.py` file with the correct string:

```python
self.assertIn("<title>Example Domain</title>", content)
```

3. **Run the test again** to make sure it passes: 
   ```bash
   python3 -m unittest test_fetch_page.py
   ```

---

### **7. Create a GitHub Actions Workflow** (4 pts)

1. Create the `.github/workflows` directory:
   ```bash
   mkdir -p .github/workflows
   ```

2. Create a file named `python-app.yml` inside `.github/workflows`:

```yaml
name: Python Tests

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run unit tests
      run: |
        python -m unittest discover
```

---

### **8. Add, Commit, and Push Your Changes** (4 pts)

1. Add all your files:
   ```bash
   git add .
   ```

2. Commit your changes with the following message:
   ```bash
   git commit -m "Quiz complete"
   ```

3. Push your changes to GitHub:
   ```bash
   git push
   ```

---

### **9. Verify the GitHub Actions Workflow** (4 pts)

1. Go to your **GitHub repository** and click on the **Actions** tab.
2. Make sure your **tests run successfully** on push.

---

## **Submission Instructions**

1. Ensure your repository contains the following files:
   - `fetch_page.py`
   - `test_fetch_page.py`
   - `requirements.txt`
   - `.github/workflows/python-app.yml`
2. Confirm that **all tests pass** in the GitHub Actions workflow.
3. Notify me (via GitHub or email) once you have completed the quiz.

---

### **Key Learning Outcomes**
- Use of **GitHub** for version control and collaboration.
- Install and manage **Python libraries** with `pip`.
- Write, run, and fix **unit tests**.
- Create **GitHub Actions workflows** for CI/CD.

---

This version keeps the focus on essential tasks—**writing simple code, fixing tests, using GitHub, and CI/CD workflows**—with **less complexity**. The students will have a straightforward example to follow while learning key skills.
