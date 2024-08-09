# HM_TPshop_Test

#### 介绍
HM_TPshop_Test: 自动化测试

#### 软件架构
软件架构说明

LNMP

#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明
自动化测试
Python+pytest+allure

#### 完成进度

前台部分
1.  完成登录模块的参数化自动测试
2.  完成下单模块的参数化自动测试
3.  完成注册模块的参数化自动测试

后台部分
1.   完成登录模块的单项自动测试
2.   完成商品模块的单项添加自动测试



### 文件结构

```
project_root/
│
├── runner.py             # 运行测试并生成报告
├── pytest.ini            # pytest配置文件
├── README.md             # 项目说明文件
│
├── src/                  # 源代码和测试代码
│   ├── test_data_json/   # 测试数据文件（可选，视用途）
│   ├── tests/            # 测试文件
│   │   ├── test_login_assert.py
│   │   ├── test_pytest_login.py
│   │   └── ...           # 其他测试文件
│   └── ...               # 其他源代码
│
├── reports/              # 报告文件夹
│   └── ...               # 测试生成的报告和HTML文件
│
└── tools/                # 工具文件夹
    └── ...
