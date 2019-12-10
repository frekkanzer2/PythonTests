import os


def buildFileName(savepath, filename, ext) -> str:
    return savepath + filename + ext


def createDirectory(savepath, dirname=None):
    try:
        if dirname is not None:
            os.mkdir(savepath + dirname)
        else:
            os.mkdir(savepath)
    except Exception:
        return False
    return True


def checkDirectory(savepath, dirname=None):
    if dirname is not None:
        if os.path.exists(savepath + dirname):
            return True
        else:
            return False
    else:
        if os.path.exists(savepath):
            return True
        else:
            return False


def checkFile(complete_filename):
    if os.path.exists(complete_filename):
        return True
    else:
        return False


def checkFile_more(savepath, filename, ext):
    complete_filename = buildFileName(savepath, filename, ext)
    return checkFile(complete_filename)
