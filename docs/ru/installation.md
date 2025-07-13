# Installation Guide

## Environment Setup

Before installing project dependencies, it is best practice to create a virtual environment. This is an isolated space where all the necessary libraries for this project will be installed, without affecting your main system.

```bash
cd /path/to/project/folder
python3 -m venv venv
source venv/bin/activate
```

After activation, you will notice that `(venv)` appears at the beginning of your terminal prompt. This means you have successfully entered the virtual environment. Now, all `pip` commands will install packages here.

## Installing Dependencies

Now that the environment is active, you need to install all the libraries the project depends on. The list is in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

This command will read the `requirements.txt` file and automatically download and install all the listed libraries (such as click, sqlalchemy, etc.) into your virtual environment.

## Installing the Project in "Editable Mode"

This is a key step. To make your system "aware" of the `chat` command and link it to the project's code, you need to install the project using pip. We will use the special `-e` flag, which means "editable" mode.

This mode creates a symbolic link to your source code. This means that any changes you make to the project files will be immediately reflected in the `chat` command's behavior without needing to reinstall it.

Make sure you are still in the project's root folder and the virtual environment is active. Run the installation command:

```bash
pip install -e .
```

(Note the dot `.` at the end—it indicates that the project should be installed from the current directory).

## Running and Verifying

If all the previous steps were successful, you can now use the application!

1.  Check that the command is available. The easiest way is to request help:

```bash
chat --help
```

2.  Start the interactive mode (REPL). This is the main command to get started:

```bash
chat run
```

You will see a `chat>` prompt where you can enter other commands (`add`, `log`, etc.) without the `chat` prefix.
