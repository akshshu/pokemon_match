import json


def check(i, j, data):
    if(j in data["super effective"][i]):
        return 2
    elif(j in data["normal effective"][i]):
        return 1
    elif(j in data["not very effective"][i]):
        return 0.5
    elif(j in data["no effect"][i]):
        return 0


n1 = int(input("no_of_pokemon in team1"))
n2 = int(input("no_of_pokemon in team2"))
n1_list = []
n2_list = []
arr_main = []
arr_main2 = []
sec_final = []
sums = 0
print("\nenter the type of pokemon for team1 :(max type can be 2 for each pokemon")
for i in range(n1):
    n1_list.append(input())
print("\nenter the type of pokemon for team2:(max type can be 2 for each pokemon")
for i in range(n2):
    n2_list.append(input())
with open("pok.json", 'r') as f:
    data = json.load(f)
for i in range(n1):
    temp_arr = n1_list[i].split(" ")
    arr_main.append(temp_arr)
for i in range(n2):
    temp_arr2 = n2_list[i].split(" ")
    arr_main2.append(temp_arr2)
for x in arr_main:
    final = []
    for x2 in arr_main2:
        pi = []
        for i in range(len(x)):
            p = 1
            for j in range(len(x2)):
                p *= check(x[i], x2[j], data)
            pi.append(p)
        final.append(max(pi))
    sec_final.append(final)
for item in sec_final:
    sums += sum(item)

sec_final = []
sums2 = 0
for x2 in arr_main2:
    final = []
    for x in arr_main:
        pi = []
        for i in range(len(x2)):
            p = 1
            for j in range(len(x)):
                p *= check(x2[i], x[j], data)
            pi.append(p)
        final.append(max(pi))
    sec_final.append(final)
for item in sec_final:
    sums2 += sum(item)
print("team me", sums)
print("team foe", sums2)
if(sums > sums2):
    print("ME")
elif(sums < sums2):
    print("Foe")
else:
    print("equal")
