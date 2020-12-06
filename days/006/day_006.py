def read():
    output = []
    with open('input.txt') as f:
        acc = ""
        for line in f.readlines():
            if line != "\n":
              if len(acc) > 0:
                acc += " "
              acc += line.strip()
            else:
                output.append(acc.strip())
                acc = ""
        else:
            output.append(acc)
    return output
sum = 0

data = read()

for line in data:
    l = "".join(line.split())
    sum += len(set(l))

print(sum)
part_two_sum = 0
print(data[0:10])

for line in data:
    persons = (set(x) for x in line.split(" "))
    part_two_sum += len(set.intersection(*persons))
print(part_two_sum)
