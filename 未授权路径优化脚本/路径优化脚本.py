
import re

def modify_paths():
    # 提示用户将收集的路径放入 Path.txt
    input("请将收集的路径放入 Path.txt 中，然后按 Enter 键继续...")

    # 打开 Path.txt 文件读取内容
    with open('Path.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 处理每一行
    new_lines = []
    for line in lines:
        # 任务1：将 = 后面添加数字 1
        if '=' in line:
            parts = line.split('=')
            key = parts[0]
            value = parts[1].strip()  # 去掉多余的空白符
            value += '1'
            new_line = f"{key}={value}"
        else:
            new_line = line.strip()  # 去除可能的多余换行符

        # 任务2：处理 /:id/:style/:ip 等格式，将其转换为 /1/1/1
        new_line = re.sub(r'/:[^/]+', '/1', new_line)

        # 添加换行符
        new_lines.append(new_line + '\n')

    # 将处理后的结果写入 result.txt
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

    print("路径修改完成，结果已写入 result.txt")

def add_https_header():
    # 提示用户是否要添加 HTTPS 请求
    add_https = input("是否要为结果添加 HTTPS 请求头？ (y/n): ").strip().lower()

    if add_https == 'y':
        # 提示用户手动添加 HTTPS URL
        https_url = input("请输入 HTTPS URL（如：https://www.example.com）: ").strip()

        # 打开 result.txt 文件，读取所有行
        with open('result.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 在每行开头添加用户提供的 HTTPS URL
        modified_lines = [https_url + line.strip() + '\n' for line in lines]

        # 将修改后的内容写入 result.txt
        with open('result.txt', 'w', encoding='utf-8') as file:
            file.writelines(modified_lines)

        print("HTTPS 请求头添加完成，结果已更新到 result.txt")
    else:
        print("未添加 HTTPS 请求头，程序结束。")

if __name__ == "__main__":
    modify_paths()
    add_https_header()
