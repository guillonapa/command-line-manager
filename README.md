# Command Line Manager

The **Command Line Manager** is an utility to easily manage personal scripts. Through the cli, you can add, edit, remove, and explore your commands (the entry point to your scripts). This is an easy way to keep things organized and boost productivity.

![command line manager preview](lib/usage.gif)

## How it Works

There are two parts for the manager: metadata and content. When adding a new command, two files will be created:

1. All the command's metadata will be stored in `your_command.yml`.
2. The contents of the `your_command.sh` file will be copied inside of a shell function (by the same name as `your_command`) and called everytime you use the command from your terminal.

You will need to modify the shell file to write your own command or script, but you are encoraged to only modify the metadata file using the Command Line Manager's `add`, `edit`, and `rm` sub-commands.

After you have generated commands, you can run the `load` sub-command to generate a file called `__functions__.sh`. Source this file and that's it!

If you need to add further files, feel free to place them (or any directories) under `~/.clmanager/public`, and reference them in your scripts as needed.

## Getting Started

Clone the repository and run the `setup.py` file.

```
$ git clone https://github.com/guillonapa/command-line-manager.git
$ cd command-line-manager
$ python setup.py
```

At this point you can call the manager directly.

```
$ python manager/manager.py
```

However, you can add a snippet like this to your `.bash_profile`, `.zshrc`, or similar:

```sh
function clmanager() {
    # call the manager and pass along all the arguments
    python ~/path/to/git/clone/manager/manager.py "$@"
}
```

You will also need to add to your `.bash_profile` or `.zshrc` the following:

```sh
source ~/.clmanager/internal/__functions__.sh
```

If you do this, you will be able to call `clmanager` directly in your terminal without having to worry about the path to the manger script.