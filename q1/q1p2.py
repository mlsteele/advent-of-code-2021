import fileinput

entries = list(map(int, fileinput.input()))
x = zip(entries, entries[1:], entries[2:])
x = map(sum, x)
x = zip(x, x[1:])
x = map(lambda (a, b): b > a, x)
x = sum(x)
print(x)
