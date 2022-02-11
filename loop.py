import os


def is_file_accepted(file):
    filename, file_extension = os.path.splitext(file)
    return file_extension in [".ma", ".mb"]


def find_latest(path):
    files = filter(is_file_accepted, os.listdir(path))
    if (len(files) > 0):
        full_paths = map(lambda file: os.path.join(path, file), files)
        full_paths.sort(reverse=True, key=lambda file: os.path.getmtime(file))
        return full_paths[0]
    else:
        return None


def find_best(path):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for (dir) in filter(lambda d: d in ["Animation", "Layout", "Posing"], dirnames):
            publish_path = os.path.join(dirpath, dir, "publish")
            if (os.path.isdir(publish_path)):
                print("-------- " + publish_path + " --------")
                found = find_latest(publish_path)
                if (found != None):
                    print(found)
                    break


find_best("./test-fs/scenario-1")
find_best("./test-fs/scenario-2")
find_best("./test-fs/scenario-3")
