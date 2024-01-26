# Take Notes Like An Egyption

- Author personal notebook as code.
- Use Visual Studio Code as your typewriter.
- Use Sphinx ecosystem as "digital printshop".

- Works on Operating System: Linux, MacOS or Windows
- Works in Github Workspaces

## Prerequisites

- Visual Studio Code
- git
- Python
- Java
- Webbrowser

## Optional Prerequisites

- draw.io (recommended),
- Inkscape (recommended)

The prerequisites need to be in the path, so callable from any directory.

For the installation step a internet connection is necessary.

## Installation

- Open `bash` or on Windows `git-bash`
- Change to the repository's root directory

``` bash
$ ./doc.sh install
```

When you open the directory in Visual Studio Code the very first time
you get prompted for installation of recommended extensions. 

Install those extensions.

## Basic Usage

### Editing

- Open `bash` or on Windows `git-bash`
- Change to the repository's root directory
- Open the repository folder with Visual Studio code:

``` bash
$ code .
```

The sources of your notebook are located in folder `doc`.
You edit them with Visual Studio Code.

### Editing with live preview

Sphinx scans for file changes and rebuild automatically the output.
You have a live preview in your browser.

- Start live preview:

``` bash
$ ./doc.sh preview
```

Check the bash window for build success, errors and warnings regularily.

### Make your day

Right before you begin your work you add a new day to the sources.

- You change to the repository's root folder and call:

``` bash
$ ./doc.sh make-my-day
```

## Authoring as code you'll love

### Working with screenshots

TODO: Describe it.

### Working with  draw.io diagrams

TODO: Describe it.

### Working with PlantUML diagrams

TODO: Describe it.

### Working with Ticket-System

TODO: Describe the slick ticket browsing