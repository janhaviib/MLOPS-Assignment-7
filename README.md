# Assignment 7: Implement CI/CD Pipeline Using GitHub Actions

## Objective
To implement an automated Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions, ensuring that every push or pull request to the main branch is automatically checked out, built, linted (`flake8`), and tested (`pytest`).

---

## Directory Structure
```text
Assignment_7/
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI workflow definition
├── src/
│   ├── __init__.py
│   ├── calc.py                # Core utility functions (add, divide)
│   └── model_utils.py         # ML utility functions (accuracy, normalization)
├── tests/
│   ├── __init__.py
│   ├── test_calc.py           # Unit tests for calc functions
│   └── test_model_utils.py    # Unit tests for ML utilities
├── pytest.ini                 # Pytest configuration with pythonpath
├── requirements.txt           # Testing & linting dependencies
├── Assignment_7.pdf           # Lab report documentation
└── README.md                  # Comprehensive instructions
```

---

## CI/CD Workflow (`.github/workflows/ci.yml`)
The workflow automatically executes the following 5 stages on `ubuntu-latest`:
1. **Checkout:** Checks out repository code via `actions/checkout@v4`.
2. **Environment Setup:** Configures Python 3.11 via `actions/setup-python@v5`.
3. **Dependency Installation:** Upgrades pip and installs packages from `requirements.txt`.
4. **Linting:** Runs static analysis via `flake8 src tests --max-line-length=100`.
5. **Automated Testing:** Runs test suite via `pytest -v`.

---

## How to Test Locally

### 1. Run Unit Tests
```powershell
pytest -v
```

### 2. Run Linting
```powershell
flake8 src tests --max-line-length=100
```

---

## How to Deploy to GitHub Actions

1. Initialize git and commit:
   ```powershell
   git init
   git add .
   git commit -m "Add source code, test suite, and CI/CD workflow"
   ```
2. Link to your GitHub repository:
   ```powershell
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git push -u origin main
   ```
3. Observe the pipeline running under the **Actions** tab on GitHub:
   - Green checkmark (`SUCCESS`) confirms all tests and lint checks passed.
   - To verify failure gating: deliberately modify an assertion in `tests/test_calc.py` (e.g. `assert add(2, 3) == 6`), commit and push. The pipeline will fail with a red cross (`FAILURE`) and halt deployment.
