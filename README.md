# selenium-test-automation-bank

## Summary
Perform test automation against [ParaBank](https://parabank.parasoft.com/parabank/login.htm) using Python tools such as [Selenium](https://www.selenium.dev/) and [PyTest](https://docs.pytest.org/en/stable/).

## Goal
Reinforce my existing web browser test automation skills by assembling a test plan. These test cases will verify that the target website meets performance expectations.

## How to run the test plan
1. Clone this Git repository.
2. Change into the repository directory.
3. Set up a Python virtual environment:
    ### Windows/MacOS/Linux
    ```
    python -m venv <directory_name>
    ```
    ##### Example
    ```
    python -m venv venv
    ```
4. Activate the Python virtual environment:
    ### Windows
    #### cmd.exe
    ```
    <venv_directory>/Scripts/activate.bat
    ```
    ##### Example
    ```
    venv/Scripts/activate.bat
    ```
    Skip to step 4
    #### PowerShell
    ```
    <venv_directory>/Scripts/Activate.ps1
    ```
    ##### Example
    ```
    venv/Scripts/Activate.ps1
    ```
    Skip to step 4
    ### MacOS/Linux
    ```
    source <venv_directory>/bin/activate
    ```
    ##### Example
    ```
    source venv/bin/activate
    ```
    Move on to step 4
5. Install the required dependencies:
    ### Windows
    ```
    pip install -r requirements.txt
    ```
    ### MacOS/Linux
    ```
    pip3 install -r requirements.txt
    ```
6. Run the tests:
    ### Run all tests
    ```
    pytest
    ```
    ### Run all tests present within a directory
    ```
    pytest <directory_name>/
    ```
    ### Run an individual test
    ```
    pytest test_<name>.py
    ```

## Resources
- [ParaBank (target website)](https://parabank.parasoft.com/parabank/login.htm)
- [Selenium](https://www.selenium.dev/)
- [PyTest](https://docs.pytest.org/en/stable/)