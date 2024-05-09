from pathlib import Path
def get_cats_info(path):
    with open(path, "r") as cats_file:
        list_cats_dict = []
        for line in cats_file.readlines():
            cats_line = line.split(',')
            cats_line[-1] = cats_line[-1].strip()
            keys= ["id", "name", "age"]
            cats_dic = dict(zip(keys,cats_line))
            print(cats_dic)
            list_cats_dict.append(cats_dic)
            print(list_cats_dict)
            return list_cats_dict

cats_path = Path("task_2/cats_file.txt")
if cats_path.is_file():
    cats_info = get_cats_info(cats_path)
    print(cats_info)

