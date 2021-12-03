import fileinput
import numpy as np

entries = [list(map(int, line.strip())) for line in fileinput.input()]
entries = np.array(entries)
γ = [round(sum(entries[:, i]) / len(entries)) for i in range(entries.shape[1])]
ε = [1-x for x in γ]
print('γ', γ, '    ε', ε)
(γ, ε) = (int(''.join(map(str, x)), base=2) for x in (γ, ε))
print('γ', γ, '    ε', ε)
print(γ * ε)
