import os, arguably, yaml

default_allowed_extensions_path = os.path.join((os.path.dirname(os.path.realpath(__file__))),"default_allowed_extensions.txt")
with open(default_allowed_extensions_path,"r") as f:
    default_allowed_extensions = [extension.lower() for extension in f.read().split("\n")]

def count_dir(dir,allowed_extensions,exclude_list,result={}):
    items = os.listdir(dir)
    if result == {}:
        result["lines"] = {}
        result["chars"] = {}
        result["lines"]["TOTAL"] = 0
        result["chars"]["TOTAL"] = 0
    for item in items:
        if item in exclude_list:
            continue
        path = os.path.join(dir,item)
        if os.path.isdir(path):
            count_dir(path, allowed_extensions, exclude_list, result)
        else:
            if not "." in item:
                continue
            extension = item.split(".")[-1].lower()
            if extension in allowed_extensions:
                with open(path, "r") as f:
                    data = f.read()
                    lines = len(data.split("\n"))
                    chars = len(data)
                    if not extension in result["lines"]:
                        result["lines"][extension] = 0
                        result["chars"][extension] = 0
                    result["lines"][extension] += lines
                    result["chars"][extension] += chars
                    result["lines"]["TOTAL"] += lines
                    result["chars"]["TOTAL"] += chars
    return result

@arguably.command
def scan(directory=os.getcwd(),*others,exclude_list:list[str]=[],allowed_extensions:list[str]=None):
    """
    count the number of lines of code in a directory its subdirectories

    Args:
        directory: directory to run scan on, defaults to current dir.
        exclude_list: list of files to ignore.
        allowed_extensions: overrides which extensions to allow. default (None) will use standard set.
    """
    if not allowed_extensions:
        allowed_extensions = default_allowed_extensions
        
    print(yaml.dump(count_dir(directory,allowed_extensions,exclude_list),indent=4),end="",flush=True)
    

if __name__ == "__main__":
    arguably.run()