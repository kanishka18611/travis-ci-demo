# Travis CI Continuous Integration Demo

## Objective
Demonstrate Continuous Integration by automatically building and testing a Python project whenever code is pushed to GitHub.

## Files
- `calculator.py`: application functions.
- `test_calculator.py`: automated unit tests using pytest.
- `requirements.txt`: test dependency.
- `.travis.yml`: Travis CI build configuration.

## Run locally (Windows)
Open PowerShell in this folder and run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m compileall -q calculator.py
pytest -v
```

If PowerShell blocks activation, use Command Prompt and run:
```bat
.venv\Scripts\activate.bat
```

## Connect to Travis CI
1. Create a GitHub repository named `travis-ci-demo`.
2. Upload/push all five project files, including the hidden `.travis.yml`.
3. Sign in at https://app.travis-ci.com/ using GitHub.
4. Activate the repository in Travis CI and select an appropriate plan if prompted.
5. Push a new commit after activation. Travis should start a build automatically.
6. Open the repository/build page in Travis CI and inspect the log.

## Demonstrate a passing build
Keep `divide()` raising `ValueError` for division by zero. Push the code and confirm all tests pass.

## Demonstrate a failing build
Temporarily change `return a + b` in `add()` to `return a - b`, commit and push. The `test_add_positive_numbers` test should fail and Travis should mark the build failed. Revert the change, commit and push again; the build should pass.

## Expected result
A successful run compiles the Python file and passes all six tests. A failed test makes the CI job fail, giving immediate feedback on the code change.

