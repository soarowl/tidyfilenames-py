from os import path
import os
import pandas as pd


def main():
    # 请修改下面参数
    tidynames("data.xlsx", "源码")


def nametidy(data, root, filename):
    """
    目录或文件名标准化处理
    """
    dir = path.dirname(filename)
    base = path.basename(filename)
    name, ext = path.splitext(base)
    if "-" in name:
        parts = name.split("-")
        if len(parts) == 2:
            if parts[0] in data["学号"].values and parts[1] in data["姓名"].values:
                return

    for i, row in data.iterrows():
        if str(row["学号"]) in name or row["姓名"] in name:
            newname = f"{row['学号']}-{row['姓名']}{ext}"
            newfilename = path.join(root, dir, newname)
            os.rename(path.join(root, filename), newfilename)


def tidynames(datafilename, top):
    """
    从datafilename excel文件中导入学号、姓名，然后在top目录下遍历所有的文件或目录，只要文件名或目录名包含学号或姓名，统一修改成“学号-姓名”或“学号-姓名.ext”格式。
    datefilename: xlsx文件，有两列，包含“学号、姓名”
    top: 从指定的目录开始处理
    """
    data = pd.read_excel(datafilename)
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            nametidy(data, root, name)
        for name in dirs:
            nametidy(data, root, name)


if __name__ == "__main__":
    main()
