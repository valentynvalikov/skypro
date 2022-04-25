def file_read(filename) -> set:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.readlines()
        lines = []
        for item in content:
            item = item.strip()
            lines.append(item)
    return set(lines)


hat = file_read('hat.txt')
walk = file_read('walk.txt')
sing = file_read('sing.txt')
dream = file_read('dream.txt')

all_fish = hat | walk | sing | dream

hat_walk = hat & walk
hat_sing = hat & sing
hat_dream = hat & dream
walk_sing = walk & sing
walk_dream = walk & dream
sing_dream = sing & dream

not_hat = all_fish - hat
not_walk = all_fish - walk
not_sing = all_fish - sing
not_dream = all_fish - dream

if len(hat_walk) > 0:
    print("Носят шапочку и любят гулять: \n" + '\n'.join(hat_walk))
if len(hat_sing) > 0:
    print("\nНосят шапочку и поют: \n" + '\n'.join(hat_sing))
if len(hat_dream) > 0:
    print("\nНосят шапочку и задумчивые: \n" + '\n'.join(hat_dream))
if len(walk_sing) > 0:
    print("\nЛюбят гулять и поют: \n" + '\n'.join(walk_sing))
if len(walk_dream) > 0:
    print("\nЛюбят гулять и задумчивые: \n" + '\n'.join(walk_dream))
if len(sing_dream) > 0:
    print("\nЛюбят петь и задумчивые: \n" + '\n'.join(sing_dream))

print("\nНе носят шапочку: \n" + '\n'.join(not_hat))
print("\nНе любят гулять: \n" + '\n'.join(not_walk))
print("\nНе поют: \n" + '\n'.join(not_sing))
print("\nНе задумчивые: \n" + '\n'.join(not_dream))
