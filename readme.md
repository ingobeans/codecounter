# codecounter
python cli tool to count the number of lines and characters of code in a directory and its subdirectories

because fun statistics!

example usage:
```
> cd my_cool_project
> python <path_to_script>
chars:
    py: 1990
lines:
    py: 51
>
```
```
> python <path_to_script> "my_cool_project"
chars:
    py: 1990
lines:
    py: 51
>
```
```
> cd soysoupOS
> python <path_to_script> --blacklist="programs.js",".git"
chars:
    html: 1059
    js: 28365
    py: 857
    soup: 23392
    soy: 324
lines:
    html: 27
    js: 1068
    py: 24
    soup: 857
    soy: 7
>
```