from pico2d import *
import map_data
import grass
map_choice = None
map_mapping = []
Pos_x = None
Pos_y = None
i = None
import flagpos
def map_read():
    global map_choice, map_mapping, Pos_x, Pos_y, i
    if flagpos.stage_number == 1:
        map_choice = map_data.map_stage1_data
    elif flagpos.stage_number == 2:
        map_choice = map_data.map_stage2_data

    for y in range(16):
        for x in range(240):
            Pos_x = x * 40
            Pos_y = 600 - y * 40

            if map_choice[y][x] == 0:
                pass
            elif map_choice[y][x] == 1:
                i = grass.Grass(Pos_x, Pos_y)
                # map_mapping.append = grass.Grass(Pos_x, Pos_y)
                map_mapping.append(i)

            elif map_choice[y][x] == 2:
                i = grass.Block_QM(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Block_QM(Pos_x, Pos_y)

            elif map_choice[y][x] == 3:
                i = grass.Block_Shadow(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Block_Shadow(Pos_x, Pos_y)

            elif map_choice[y][x] == 4:
                i = grass.Mountain(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Mountain(Pos_x, Pos_y)

            elif map_choice[y][x] == 5:
                i = grass.Cloud(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Cloud(Pos_x, Pos_y)

            elif map_choice[y][x] == 6:
                i = grass.Cloudsmall(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Cloudsmall(Pos_x, Pos_y)

            elif map_choice[y][x] == 66:
                i = grass.Cloud_enemy(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Cloudsmall(Pos_x, Pos_y)

            elif map_choice[y][x] == 7:
                i = grass.Flag(Pos_x, Pos_y)
                map_mapping.append(i)

                # map_mapping.append = grass.Flag(Pos_x, Pos_y)

            elif map_choice[y][x] == 8:
                i = grass.JUMP_Bar(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.JUMP_Bar(Pos_x, Pos_y)

            elif map_choice[y][x] == 9:
                i = grass.Block_Drop(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Block_Drop(Pos_x, Pos_y)

            elif map_choice[y][x] == 21:
                i = grass.Block_RM(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Block_Drop(Pos_x, Pos_y)

            elif map_choice[y][x] == 44:
                i = grass.Block_PM(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Block_Drop(Pos_x, Pos_y)

            elif map_choice[y][x] == 88:
                i = grass.TREE(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.TREE(Pos_x, Pos_y)

            elif map_choice[y][x] == 10:
                i = grass.SWITCH(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.SWITCH(Pos_x, Pos_y)

            elif map_choice[y][x] == 11:
                i = grass.Roof(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Roof(Pos_x, Pos_y)

            elif map_choice[y][x] == 33:
                i = grass.Leaf(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Leaf(Pos_x, Pos_y)

            elif map_choice[y][x] == 55:
                i = grass.Bong(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Bong(Pos_x, Pos_y)

            elif map_choice[y][x] == 22:
                i = grass.Bong_Enemy(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Bong(Pos_x, Pos_y)

            elif map_choice[y][x] == 56:
                i = grass.Clear_Door(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Clear_Door(Pos_x, Pos_y)

            elif map_choice[y][x] == 99:
                i = grass.Block_UP(Pos_x, Pos_y)
                map_mapping.append(i)
                # map_mapping.append = grass.Clear_Door(Pos_x, Pos_y)

            elif map_choice[y][x] == 51:
                i = grass.Grass_Ver2(Pos_x, Pos_y)
                # map_mapping.append = grass.Grass(Pos_x, Pos_y)
                map_mapping.append(i)

            elif map_choice[y][x] == 19:
                i = grass.Block_UP_DOWN(Pos_x, Pos_y)
                # map_mapping.append = grass.Grass(Pos_x, Pos_y)
                map_mapping.append(i)

            elif map_choice[y][x] == 77:
                i = grass.Block_STAR(Pos_x, Pos_y)
                # map_mapping.append = grass.Grass(Pos_x, Pos_y)
                map_mapping.append(i)

            elif map_choice[y][x] == 12:
                i = grass.Block_Switch(Pos_x, Pos_y)
                # map_mapping.append = grass.Grass(Pos_x, Pos_y)
                map_mapping.append(i)

            elif map_choice[y][x] == 17:
                i = grass.SWITCH_COIN(Pos_x, Pos_y)
                # map_mapping.append = grass.Grass(Pos_x, Pos_y)
                map_mapping.append(i)






