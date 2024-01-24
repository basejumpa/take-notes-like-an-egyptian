# Take Notes Like An Egyption

- Author personal notebook as code.
- Use Visual Studio Code as your typewriter.
- Use Sphinx ecosystem as "digital printshop".

## Prerequisites

- Operating System: Linux, MacOS or Windows
- Visual Studio Code
- Webbrowser
- draw.io
- git
- Python
- Java

For the installation step a internet connection is necessary.

## Installation

- Open `bash` or on Windows `git-bash`
- Change to the repository's root directory

``` bash
$ ./doc.sh install
```

## Usage

Editing:

- Open `bash` or on Windows `git-bash`
- Change to the repository's root directory
- Open the repository folder with Visual Studio code:

``` bash
$ code .
```

The sources of your notebook are located in folder `doc`.
You edit them with Visual Studio Code.
Sphinx scans for file changes and rebuild automatically the output.
You have a live preview in your browser.

- Start live preview:

``` bash
$ ./doc.sh preview
```

Check the bash window for build success, errors and warnings regularily.
