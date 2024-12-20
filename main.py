import os, arguably

default_allowed_extensions_path = os.path.join((os.path.dirname(os.path.realpath(__file__))),"default_allowed_extensions.txt")
with open(default_allowed_extensions_path,"r") as f:
    default_allowed_extensions = [extension.lower() for extension in f.read().split("\n")]

def count_dir(dir,allowed_extensions,result={}):
    items = os.listdir(dir)
    for item in items:
        if os.path.isdir(item):
            count_dir(os.path.join(dir,item), allowed_extensions, result)
        else:
            if not "." in item:
                continue
            extension = item.split(".")[-1]
            if extension in allowed_extensions:
                with open(os.path.join(dir,item), "r") as f:
                    count = len(f.readlines())
                    if not extension in result:
                        result[extension] = 0
                    result[extension] += count
    return result

@arguably.command
def scan(directory=os.getcwd(),allowed_extensions:list[str]=None):
    """
    count the number of lines of code in a directory its subdirectories

    Args:
        directory: directory to run scan on, defaults to current dir.
        allowed_extensions: overrides which extensions to allow. default (None) will use standard set.
    """
    if not allowed_extensions:
        allowed_extensions = default_allowed_extensions

    print(count_dir(directory,allowed_extensions))
    

if __name__ == "__main__":
    arguably.run()