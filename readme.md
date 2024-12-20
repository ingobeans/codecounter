# codecounter

python cli tool to count the number of lines and characters of code in a directory and its subdirectories

because fun statistics!

example usage:
```
> cd my_cool_project
> python <path_to_script>
chars:
    TOTAL: 2172
    py: 2172
lines:
    TOTAL: 55
    py: 55
```
```
> python <path_to_script> "my_cool_project"
chars:
    TOTAL: 2172
    py: 2172
lines:
    TOTAL: 55
    py: 55
```
```
> cd soysoupOS
> python <path_to_script> --blacklist="programs.js",".git"
chars:
    TOTAL: 53997
    html: 1059
    js: 28365
    py: 857
    soup: 23392
    soy: 324
lines:
    TOTAL: 1983
    html: 27
    js: 1068
    py: 24
    soup: 857
    soy: 7
>
```