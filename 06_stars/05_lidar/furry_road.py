with open('furry_road2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    i = 5
    с = 2
    while i <= (len(lines) - 1):
        # line = lines[i].strip().split(' ')

        if i == len(lines):
            break

        if lines[i].strip().split(' ')[с] == "False":
            print("stay")
            i += 1
            print(с)
        elif lines[i].strip().split(' ')[с] == "True" and lines[i].strip().split(' ')[с - 1] == "False" and lines[i - 1].strip().split(' ')[с - 1] == "False":
            print("right")
            с -= 1
            i += 1
            print(с)
        elif lines[i].strip().split(' ')[с] == "True" and lines[i].strip().split(' ')[с - 1] == "True" and lines[i].strip().split(' ')[с + 1] == "False" and lines[i - 1].strip().split(' ')[с + 1] == "False":
            print("left")
            с += 1
            i += 1
            print(с)
        elif lines[i].strip().split(' ')[с] == "True" and lines[i].strip().split(' ')[с - 1] == "True" and lines[i].strip().split(' ')[с + 1] == "True":
            print("stop")
            print(с)

    # print(lines[0])
    # print(lines[0].strip().split(' ')[с - 1])