# ImplementacionCU-DDS

[DjangoDocs]: https://www.djangoproject.com/
[PythonDocs]: https://www.python.org/doc/

This section is used for setting up the backend [Django][DjangoDocs] server, using [Python][PythonDocs].


#### Setting up the backend for Development

- Tools needed:
  - Shell (bash, zsh, PowerShell, etc.)
  - Python 3.10 or higher
    - pip (Python package manager)
  - Visual Studio Code (optional - recommended)

Steps to set up the backend environment:

1. Install Python 3.10 or higher using the package manager from you OS:

   1. if macOS run using zsh:

      ```bash
      brew install python
      ```

   2. if Ubuntu/Debian run using bash:

      ```bash
      sudo apt-get install python3
      ```

   3. if Windows run using PowerShell or PowerShell Core:

      ```bash
      winget install python
      ```

      **Note:** _If you are using a different OS, or prefer a manual installation, please refer to the official Python [download page](https://www.python.org/downloads/)_

2. Install pip (Python package manager):

   ```bash
   python -m ensurepip
   ```

   to get the latest version of pip:

   ```bash
   python -m pip install --upgrade pip
   ```

3. At the root of the project, create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment using:

   1. On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

   2. On Windows:

      ```bash
      .\venv\Scripts\Activate
      ```

5. Run the server using:

   ```bash
      python manage.py runserver
      ```
