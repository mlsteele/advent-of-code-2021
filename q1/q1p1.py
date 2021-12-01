import fileinput

entries = list(map(int, fileinput.input()))
x = zip(entries, entries[1:])
x = map(lambda (a, b): b > a, x)
x = sum(x)
print(x)
