# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: ZF


menu = {
    '水果': {
        "苹果": {"红富士", "嘎啦", "黄元帅"},
        "橙子": {"甜橙", "脐橙", "冰糖橙"},
        "柚子": {"沙田柚", "文旦", "坪山柚"}
    },
    '荤菜': {
        "肉": {"猪肉", "狗肉", "羊肉"},
        "蛋": {"鸡蛋", "鸭蛋", "鸟蛋"}
    },
    '酒': {
        "白酒": {"五粮液", "茅台", "二锅头"},
        "红酒": {"拉菲", "张裕", "干露"},
    }
}

# 将字典menu键取出来转换成list；
menu_list = list(menu.keys())
print(menu_list)
while True:
    print('\033[41;1m一级菜单\033[0m'.center(23, '*'))
    for i in menu_list:
        print(menu_list.index(i)+1, '.', i)   # 将列表索引值加1形成编号，并按格式打印一级菜单
    menu_id = input("请输入菜单编号:")
    if menu_id.isdigit():        # 判断输入的是否是数字；
        menu_id = int(menu_id)   # 将menu_id转换成int型
        if 0 < menu_id <= len(menu_list):
            menu_name = menu_list[menu_id-1]
            print(menu_name)
            menu_list2 = list(menu[menu_name].keys())  # 将字典menu二级字典键取出转换成列表
            while True:
                print("\033[44;1m二级菜单\033[0m".center(20, '*'))
                for j in menu_list2:
                    print(menu_list2.index(j)+1, '.', j)        # 将列表索引值加1形成编号，并按格式打印二级菜单
                menu_id2 = input("请输入种类编号：")
                if menu_id2.isdigit():
                    menu_id2 = int(menu_id2)
                    if 0 < menu_id2 <= len(menu_list2):
                        menu_name2 = menu_list2[menu_id2-1]
                        print(menu_name2)
                        menu_list3 = list(menu[menu_name][menu_name2])
                        while True:
                            print("\033[43;1m三级菜单\033[0m".center(20, '*'))
                            for k in menu_list3:
                                print(menu_list3.index(k)+1, k)
                            menu_id3 = input("请输入食物编号：")
                            if menu_id3.isdigit():
                                menu_id3 = int(menu_id3)
                                if 0 < menu_id3 <= len(menu_list3):
                                    menu_name3 = menu_list3[menu_id3-1]
                                    print(menu_name3)
                                else:
                                    print("请输入存在的编号")
                            elif menu_id3 == 'b':
                                break
                            elif menu_id3 == 'q':
                                exit()
                            else:
                                print("非法输入")
                    else:
                        print("输入不规范，请输入存在的编号")
                elif menu_id2 == 'b':
                    break
                elif menu_id2 == 'q':
                    exit()
                else:
                    print("请输入存在的编号")
        else:
            print("您输入的编号%d不存在" % menu_id)
    elif menu_id == 'q':
        break
    else:
        print("非法输入，请重输")
