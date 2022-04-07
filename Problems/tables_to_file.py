#table with file
for a in  range(2,21):
    with open(f"Table of {a}.txt","w") as table:
        for b in range(1,11):
            table.write(f"{a} * {b} = {a*b}\n")