from draw import draw
draw_list = draw.split('\n')
import os

for d in draw_list:
    # print(f'draw/{d.strip()}')
    print(f'handprint -s microsoft draw/{d.strip()} -e')

# os.system(f'handprint -s microsoft draw/{draw_list[0].strip()} -e')
# IMG_9531.jpeg
# handprint -s microsoft draw/IMG_9531.jpeg -e
# print(draw_list[1])
