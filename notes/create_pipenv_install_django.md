# Create `pipenv` Virtual Environment and Install Django

1. Start in project root (the directory which houses all our code)

    When discussing the concept of a "root directory" in the context of coding and specifically within Django applications, it's important to provide a clear and accessible explanation. Here's a way you might describe it:

    The "root directory" in coding, especially within the framework of Django applications, is the top-most folder in the hierarchy of files that make up your project. Think of it as the starting point or base camp for your project's file structure. Just like the root of a tree anchors it into the ground and supports all the branches above, the root directory serves as the foundational base for all the project files, directories, and subdirectories.

    In a Django application, the root directory typically contains the manage.py file, which is a command-line utility that lets you interact with your Django project in various ways, such as starting a new app, running the development server, or applying migrations. It also houses the project's main configuration directory (often named after the project itself), which includes settings.py, urls.py, and wsgi.py, among others. These files are crucial for setting up the application's settings, URL patterns, and deployment configurations, respectively.

    Understanding the root directory's role is essential for navigating and managing your Django project efficiently. It's where you'll often start when running commands, adding new applications, or organizing your project's overall structure. It sets the stage for how your Django project is organized and operates, making it a fundamental concept for both beginners and seasoned developers alike.

1. Verify current position in directory structure

    - `Get-Location`
        ```powershell
        PS C:\Users\FlynntKnapp\Programming\view-function-based> Get-Location 

        Path
        ----
        C:\Users\FlynntKnapp\Programming\view-function-based

        PS C:\Users\FlynntKnapp\Programming\view-function-based>
        ```
1. Check current installed Python packages

    - `pip list`

        ```powershell
        PS C:\Users\FlynntKnapp\Programming\view-function-based> pip list   
        Package      Version
        ------------ ----------
        certifi      2023.11.17
        distlib      0.3.8
        filelock     3.13.1
        pip          24.0
        pipenv       2023.11.15
        platformdirs 4.1.0
        setuptools   69.0.3
        virtualenv   20.25.0
        PS C:\Users\FlynntKnapp\Programming\view-function-based>
        ```

1. Investigate current Python executable location

    - `Get-Command python | Format-List`

        ```powershell
        PS C:\Users\FlynntKnapp\Programming\view-function-based> Get-Command python | Format-List

        Name            : python.exe
        CommandType     : Application
        Definition      : C:\Users\FlynntKnapp\AppData\Local\Programs\Python\Python312\python.exe
        Extension       : .exe
        Path            : C:\Users\FlynntKnapp\AppData\Local\Programs\Python\Python312\python.exe
        FileVersionInfo : File:             C:\Users\FlynntKnapp\AppData\Local\Programs\Python\Python312\python.exe
                        InternalName:     Python Console
                        OriginalFilename: python.exe
                        FileVersion:      3.12.1
                        FileDescription:  Python
                        Product:          Python
                        ProductVersion:   3.12.1
                        Debug:            False
                        Patched:          False
                        PreRelease:       False
                        PrivateBuild:     False
                        SpecialBuild:     False
                        Language:         Language Neutral


        PS C:\Users\FlynntKnapp\Programming\view-function-based>
        ```

1. Create `pipenv` virtual environment

    - `pipenv install`
        ```text
        PS C:\Users\FlynntKnapp\Programming\view-function-based> pipenv install
        Creating a virtualenv for this project...
        Pipfile: C:\Users\FlynntKnapp\Programming\view-function-based\Pipfile
        Using default python from C:\Users\FlynntKnapp\AppData\Local\Programs\Python\Python312\python.exe (3.12.1) to create virtualenv...
        [  ==] Creating virtual environment...created virtual environment CPython3.12.1.final.0-64 in 416ms
        creator CPython3Windows(dest=C:\Users\FlynntKnapp\.virtualenvs\view-function-based-8Nuan46G, clear=False, no_vcs_ignore=False, global=False)
        seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=C:\Users\FlynntKnapp\AppData\Local\pypa\virtualenv)
            added seed packages: pip==23.3.2
        activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

        Successfully created virtual environment!
        Virtualenv location: C:\Users\FlynntKnapp\.virtualenvs\view-function-based-8Nuan46G
        Creating a Pipfile for this project...
        Pipfile.lock not found, creating...
        Locking [packages] dependencies...
        Locking [dev-packages] dependencies...
        Updated Pipfile.lock (702ad05de9bc9de99a4807c8dde1686f31e0041d7b5f6f6b74861195a52110f5)!
        Installing dependencies from Pipfile.lock (2110f5)...
        To activate this project's virtualenv, run pipenv shell.
        Alternatively, run a command inside the virtualenv with pipenv run.
        PS C:\Users\FlynntKnapp\Programming\view-function-based>
        ```

1. Investigate current Python executable location

    - `Get-Command python | Format-List`

        ```powerhsell
        PS C:\Users\FlynntKnapp\Programming\view-function-based> Get-Command python | Format-List

        Name            : python.exe
        CommandType     : Application
        Definition      : C:\Users\FlynntKnapp\AppData\Local\Programs\Python\Python312\python.exe
        Extension       : .exe
        Path            : C:\Users\FlynntKnapp\AppData\Local\Programs\Python\Python312\python.exe
        FileVersionInfo : File:             C:\Users\FlynntKnapp\AppData\Local\Programs\Python\Python312\python.exe
                        InternalName:     Python Console
                        OriginalFilename: python.exe
                        FileVersion:      3.12.1
                        FileDescription:  Python
                        Product:          Python
                        ProductVersion:   3.12.1
                        Debug:            False
                        Patched:          False
                        PreRelease:       False
                        PrivateBuild:     False
                        SpecialBuild:     False
                        Language:         Language Neutral


        PS C:\Users\FlynntKnapp\Programming\view-function-based>
        ```

1. Investigate global installed Python packages
    - `pip list`

        ```
        PS C:\Users\FlynntKnapp\Programming\view-function-based> pip list      
        Package      Version
        ------------ ----------
        certifi      2023.11.17
        distlib      0.3.8
        filelock     3.13.1
        pip          24.0
        pipenv       2023.11.15
        platformdirs 4.1.0
        setuptools   69.0.3
        virtualenv   20.25.0
        PS C:\Users\FlynntKnapp\Programming\view-function-based>
        ```

1. Activate `pipenv` virtual environment

    - `pipenv shell`

        ```powershell
        PS C:\Users\FlynntKnapp\Programming\view-function-based> pipenv shell
        Launching subshell in virtual environment...
        PowerShell 7.4.1
        PS C:\Users\FlynntKnapp\Programming\view-function-based>
        ```

1. Investigate virtual environment installed packages

    - `pip list`

        ```powershell
        PS C:\Users\FlynntKnapp\Programming\view-function-based> pip list
        Package    Version
        ---------- -------
        pip        23.3.2
        PS C:\Users\FlynntKnapp\Programming\view-function-based>
        ```

1. Investigate current Python executable location

    - `Get-Command python | Format-List`

        ```powershell
        PS C:\Users\FlynntKnapp\Programming\view-function-based> Get-Command python | Format-List

        Name            : python.exe
        CommandType     : Application
        Definition      : C:\Users\FlynntKnapp\.virtualenvs\view-function-based-8Nuan46G\Scripts\python.exe
        Extension       : .exe
        Path            : C:\Users\FlynntKnapp\.virtualenvs\view-function-based-8Nuan46G\Scripts\python.exe
        FileVersionInfo : File:             C:\Users\FlynntKnapp\.virtualenvs\view-function-based-8Nuan46G\Scripts\python.exe
                        InternalName:     Python Launcher
                        OriginalFilename: py.exe
                        FileVersion:      3.12.1
                        FileDescription:  Python
                        Product:          Python
                        ProductVersion:   3.12.1
                        Debug:            False
                        Patched:          False
                        PreRelease:       False
                        PrivateBuild:     False
                        SpecialBuild:     False
                        Language:         Language Neutral


        PS C:\Users\FlynntKnapp\Programming\view-function-based>
        ```

1. Install Django

    - `pipenv install django`

        ```
        PS C:\Users\FlynntKnapp\Programming\view-function-based> pipenv install django
        Installing django...
        Resolving django...
        Added django to Pipfile's [packages] ...
        Installation Succeeded
        Pipfile.lock (2110f5) out of date, updating to (e35515)...                                                                                                                                                                                
        Locking [packages] dependencies...
        Building requirements...
        Resolving dependencies...
        Success!
        Locking [dev-packages] dependencies...                                                                                                                                                                                                    
        Updated Pipfile.lock (0b5823de65ff0f5100b8f0fd7642f5000e8f2788c925cc51afe587d419e35515)!
        Installing dependencies from Pipfile.lock (e35515)...
        PS C:\Users\FlynntKnapp\Programming\view-function-based>
        ```

1. Investigate virtual environment installed packages

    - `pip list`

        ```powershell
        PS C:\Users\FlynntKnapp\Programming\view-function-based> pip list
        Package  Version
        -------- -------
        asgiref  3.7.2
        Django   5.0.1
        pip      23.3.2
        sqlparse 0.4.4
        tzdata   2023.4
        PS C:\Users\FlynntKnapp\Programming\view-function-based>
        ```

1. Exit `pipenv` virtual environment
    
    - `exit`
    
        ```
        PS C:\Users\FlynntKnapp\Programming\view-function-based> exit
        PS C:\Users\FlynntKnapp\Programming\view-function-based>
        ```

1. See that we are again using the global-installed Python

    - `Get-Command python | Format-List`

        ```
        PS C:\Users\FlynntKnapp\Programming\view-function-based> get-Command python | Format-List

        Name            : python.exe
        CommandType     : Application
        Definition      : C:\Users\FlynntKnapp\AppData\Local\Programs\Python\Python312\python.exe
        Extension       : .exe
        Path            : C:\Users\FlynntKnapp\AppData\Local\Programs\Python\Python312\python.exe
        FileVersionInfo : File:             C:\Users\FlynntKnapp\AppData\Local\Programs\Python\Python312\python.exe
                        InternalName:     Python Console
                        OriginalFilename: python.exe
                        FileVersion:      3.12.1
                        FileDescription:  Python
                        Product:          Python
                        ProductVersion:   3.12.1
                        Debug:            False
                        Patched:          False
                        PreRelease:       False
                        PrivateBuild:     False
                        SpecialBuild:     False
                        Language:         Language Neutral


        PS C:\Users\FlynntKnapp\Programming\view-function-based>
        ```
