from edalize import *
from sys import argv
import os
import re
import shutil


def getFullPath(relPath):
    return "{0}/{1}".format(os.getcwd(), relPath)


def getFilesInDirectory(dirPath):
    fileEntries = []

    try:
        for i in os.scandir(getFullPath(dirPath)):
            if i.is_file(follow_symlinks=True):
                fileEntries.append(i.path)

    except FileNotFoundError:
        pass

    return fileEntries


def getBoardFiles():
    return getFilesInDirectory("board")


def getSourceFiles():
    return getFilesInDirectory("src")


def main():
    if len(argv) < 2:
        print("Usage: q2.py any of [clean] [configure] [build] [run]")
        exit(0)

    projectSources = []

    extensionMapping = {
        ".v": "verilogSource",
        ".tcl": "tclSource",
        ".sdc": "SDC"
    }

    for i in getSourceFiles() + getBoardFiles():
        fileType = None
        extensionMatch = re.search(r"\..*$", i)

        try:
            if extensionMatch is not None:
                fileType = extensionMapping[extensionMatch.group()]
        except KeyError:
            pass

        if fileType is not None:
            projectSources.append({
                "name": i,
                "file_type": fileType
            })

    edam = {
        "files": projectSources,
        "name": os.path.basename(os.getcwd()),
        "toplevel": "top",
        "tool_options": {
            "quartus": {
                "family": "Cyclone II",
                "device": "EP2C20F484C7"
            }
        }
    }

    backend = get_edatool("quartus")(edam=edam, work_root="build")

    if "clean" in argv:
        try:
            shutil.rmtree(getFullPath("build"))
        except FileNotFoundError:
            pass

    if "configure" in argv:
        if os.path.exists(getFullPath("build")) is False:
            os.mkdir(getFullPath("build"))

        backend.configure()

    if "build" in argv:
        backend.build()

    if "run" in argv:
        backend.run()


if __name__ == "__main__":
    main()
