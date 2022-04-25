def s():
  s = "ddddddd"
  return s

s()


"""""""""""""""""""""""""""""""""""""""""""     Урбанизация    """""""""""""""""""""""""""""""""""""""""""""""""""""""""

# # по количеству скамеечек на человека
# top_by_benches = ['Auckland', 'Osaka', 'Adelaide', 'Geneva', 'Melbourne']
#
# # по количеству фонтанчиков на человека
# top_by_fountains = ['Adelaide', 'Geneva', 'Osaka', 'Melbourne', 'Auckland']
#
# # по количеству качелек на человека
# top_by_swings = ['Osaka', 'Adelaide', 'Geneva', 'Melbourne', 'Auckland']
#
# city = input("Введите город\n").capitalize()
#
#
# print(f"По количеству скамеечек: #{top_by_benches.index(city) + 1}\n"
#       f"По количеству фонтанчиков: #{top_by_fountains.index(city) + 1}\n"
#       f"По количеству качелек: #{top_by_swings.index(city) + 1}\n"
#       f"В среднем занимает позицию: \n"
#       f"{round((top_by_benches.index(city) + 1 + top_by_fountains.index(city) + 1 + top_by_swings.index(city) + 1) / 3)}")


""""""""""""""""""""""""""""""""""""""""     Уникализация списка     """""""""""""""""""""""""""""""""""""""""""""""""""

# songs = ["DRIVERS LICENSE", "DON'T PLAY", "AFTERGLOW", "SWEET MELODY", "AFTERGLOW", "STREETS", "AFTERGLOW",
#          "YOU BROKE ME FIRST", "SWEET MELODY"]
#
# played_songs = []
#
# i = 1
# for song in songs:
#     if song in played_songs:
#         print(f"X {song} уже пели")
#     else:
#         print(f"{i} {song}")
#         played_songs.append(song)
#         i += 1
