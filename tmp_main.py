def createfile(string):
    try:
        file = open('zad1.txt', 'a')
        file.write(string)
        file.close()
    except Exception as e:
        print("error: ", e)

samogloski = ['a','i','o','y','e']

createfile('cos')
file = open('zad1.txt', 'r')
lines = file.readlines()
for line in lines:
    tekst = line
    do_zmiany = []
    for i in range(len(line)):
        for j in range(len(samogloski)):
            if (tekst[i] == samogloski[j]):
                do_zmiany.append(tekst[i])
    for i in range(len(do_zmiany)):
        tekst = tekst.replace(do_zmiany[i], "")
    print(tekst, end="")
file.close()
