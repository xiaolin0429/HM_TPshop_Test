import os
import shutil

import pytest

# 设置报告生成路径
report_path = "./reports"
json_path = "./reports/json"  # 创建一个专门存放JSON文件的文件夹


def run_tests():
    # 清除之前的测试报告和JSON文件夹
    if os.path.exists(report_path):
        shutil.rmtree(report_path)  # 使用shutil来递归删除目录

    # 创建一个新的JSON文件夹
    os.makedirs(json_path, exist_ok=True)

    # 运行测试并生成Allure结果
    pytest.main([
        "--alluredir", json_path,  # 将Allure结果输出到JSON文件夹
        "--reruns", "3",  # 设置失败测试用例的重试次数为3
        "--maxfail", "1",  # 可以设置为1以便在第一次失败后停止，也可以根据需要调整
        "-s",  # 实时输出测试结果
        "./src/tests"  # 根据项目结构更新测试文件夹路径
    ])

    # 检查Allure命令是否存在
    if shutil.which("allure") is None:
        raise EnvironmentError(
            "Allure command is not found in the system path. \
            Please ensure Allure is installed and added to the system PATH.")

    # 生成Allure HTML报告
    os.system(f"allure generate {json_path} -o {report_path}/html --clean")


if __name__ == "__main__":
    run_tests()
