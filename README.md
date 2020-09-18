# zhengrr 所知的 Python

官网 <https://python.org/>，Python 始于 1991 年，最初由 Guido van Rossum（吉多·范·罗苏姆）创作。

## 参考

[*Python 3 Docs*](https://docs.python.org/3/ "Python 3 documentation") <sub>
    [*lang*](https://docs.python.org/3/reference "The Python Language Reference"),
    [*lib*](https://docs.python.org/3/library "The Python Standard Library"),
    [*doc*](https://docs.python.org/3.1/documenting/ "Documenting Python") </sub>

[*Sphinx*](https://www.sphinx-doc.org/) <sub>
    [*reStructuredText Style*](https://www.sphinx-doc.org/en/master/usage/restructuredtext),
    [*Google Style*](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html),
    [*NumPy Style*](https://www.sphinx-doc.org/en/master/usage/extensions/example_numpy.html) </sub>
*   [*reStructuredText*](http://docutils.sourceforge.net/rst.html)
*   [*numpydoc docstring guide*](https://numpydoc.readthedocs.io/en/latest/format.html)

## 风格

*   [*PEP 8 -- Style Guide for Python Code*](https://python.org/dev/peps/pep-0008/)
*   [*PEP 224 -- Attribute Docstrings*](https://python.org/dev/peps/pep-0224/)
*   [*PEP 257 -- Docstring Conventions*](https://python.org/dev/peps/pep-0257/)

## 指南

*   廖雪峰的官方网站上的 [*Python 教程*](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
*   [*床长人工智能教程*](https://captainbed.net/)
*   [“机器学习速成课程”](https://developers.google.cn/machine-learning/crash-course/). *Google Developers*.

## Awesome

[*Awesome Python*](https://awesome-python.com/) <sub>
    [*cmn-Hans*](http://python.jobbole.com/84464) </sub>

*   [*docopt*](http://docopt.org/) 命令行参数
*   [*Jupyter*](https://jupyter.org/) 交互式计算
*   [*Loguru*](https://github.com/Delgan/loguru) 日志
*   [*Matplotlib*](https://matplotlib.org/) 数据可视化 <sub>
        [*cmn-Hans*](https://matplotlib.org.cn/) </sub>
*   [*NumPy*](https://numpy.org/) 科学计算 <sub>
        [*cmn-Hans*](https://numpy.org.cn/) </sub>
*   [*Orator*](https://github.com/sdispater/orator) 对象关系映射
*   [*pandas*](https://pandas.pydata.org/) 数据分析和处理 <sub>
        [*cmn-Hans*](https://pypandas.cn/) </sub>
*   [*Pipenv*](https://pypi.org/project/pipenv/) 开发工作流
*   [*profig*](https://github.com/dhagrow/profig) 配置
*   [*PyCharm*](https://jetbrains.com/pycharm) 集成开发环境 <sub>
        [*zh_CN*](https://github.com/pingfangx/jetbrains-in-chinese/tree/master/PyCharm) </sub>
*   [*pytest*](https://pytest.org/) 测试框架
*   [*PyTorch*](https://pytorch.org/) 机器学习框架 <sub>
        [*cmn-Hans*](https://pytorch.apachecn.org/),
        [*man cmn-Hans*](https://github.com/zergtant/pytorch-handbook),
        [*doc cmn-Hans*](https://pytorch-cn.readthedocs.io/zh/latest/) </sub>
*   [*sandman2*](https://github.com/jeffknupp/sandman2) 为数据库提供 RESTful 接口
*   [*schedule*](https://github.com/dbader/schedule) 计划任务
*   [*Schematics*](https://github.com/schematics/schematics) 数据验证 
*   [*SciPy*](https://scipy.org/) 用于数学、科学和工程的开源软件生态
*   [*sh*](https://github.com/amoffat/sh) 子进程
*   [*SymPy*](https://sympy.org/) 符号数学
*   [*TensorFlow*](https://tensorflow.google.cn) 机器学习框架 <sub>
        [*cmn-Hans*](http://tensorfly.cn/) </sub>

### Python 运行时 CPython

```cmder
:: 使用 Scoop 安装 CPython
%USERPROFILE% λ scoop install python

:: 交互式 Python 壳层
%USERPROFILE% λ pip install ipython
%USERPROFILE% λ ipython

:: 运行 Python 脚本
%USERPROFILE% λ python <script.py>
```

### Python 包管理器 pip

[*PyPI 官网*](https://pypi.org/)。

```cmder
:: 列出配置
%USERPROFILE% λ pip config list

:: 列出系统配置
%USERPROFILE% λ pip config --global list

:: 列出用户配置
%USERPROFILE% λ pip config --user list

:: 列出项目配置
%USERPROFILE% λ pip config --site list

:: 编辑配置
%USERPROFILE% λ pip config --editor=notepad edit

:: 配置豆瓣镜像
%USERPROFILE% λ pip config set global.index-url https://pypi.doubanio.com/simple

:: 升级 pip
%USERPROFILE% λ python -m pip install --upgrade pip
:: abbr.        python -m pip install -U pip

:: 列出已安装的包
%USERPROFILE% λ pip list

:: 搜索 PyPI
%USERPROFILE% λ pip search <package>

:: 安装包
%USERPROFILE% λ pip install <package>

:: 升级包
%USERPROFILE% λ pip install --upgrade <package>
:: abbr.        pip install -U <package>

:: 卸载包
%USERPROFILE% λ pip uninstall <package>
```

### Python 环境管理器 Pipenv

```cmder
%USERPROFILE% λ pip install pipenv

%USERPROFILE% λ pipenv {--three | --two}

%USERPROFILE% λ pipenv install [--dev] <package>
:: abbr.        pipenv install [-d] <package>

%USERPROFILE% λ pipenv uninstall <package>

%USERPROFILE% λ pipenv lock

%USERPROFILE% λ pipenv sync

%USERPROFILE% λ pipenv run python <script.py>
```

### Jupyter Notebook

```cmder
%USERPROFILE% λ pip install jupyter notebook

%USERPROFILE% λ jupyter notebook [script.ipynb]
```

## 许可

项目采用 Unlicense 许可，文档采用 CC0-1.0 许可：

<p xmlns:dct="https://purl.org/dc/terms/">
  <a rel="license"
     href="https://creativecommons.org/publicdomain/zero/1.0/">
    <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <span resource="[_:publisher]" rel="dct:publisher">
    <span property="dct:title">zhengrr</span></span>
  has waived all copyright and related or neighboring rights to this work.
</p>
