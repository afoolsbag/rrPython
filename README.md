# zhengrr 所知的 Python

[Python](https://python.org/) 始于 1991 年，最初由 Guido van Rossum（吉多·范·罗苏姆）创作。

## 参考

*   [Python 3 文档](https://docs.python.org/zh-cn/3/)
    *   [语言参考](https://docs.python.org/zh-cn/3/reference/index.html)
    *   [标准库参考](https://docs.python.org/zh-cn/3/library/index.html)

<br>

*   [Sphinx](https://www.sphinx-doc.org/zh_CN/master/)
    *   [reStructuredText 风格](https://www.sphinx-doc.org/zh_CN/master/usage/restructuredtext/index.html)  
        [reStructuredText](http://docutils.sourceforge.net/rst.html)
    *   [Markdown 风格](https://www.sphinx-doc.org/zh_CN/master/usage/markdown.html)
    *   [Google 风格](https://www.sphinx-doc.org/zh_CN/master/usage/extensions/example_google.html)
    *   [NumPy 风格](https://www.sphinx-doc.org/zh_CN/master/usage/extensions/example_numpy.html)  
        [numpydoc docstring guide](https://numpydoc.readthedocs.io/en/latest/format.html)

## 风格

*   [PEP 8 -- Style Guide for Python Code](https://python.org/dev/peps/pep-0008/)
*   [PEP 224 -- Attribute Docstrings](https://python.org/dev/peps/pep-0224/)
*   [PEP 257 -- Docstring Conventions](https://python.org/dev/peps/pep-0257/)

## 指南

*   [Python教程 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)
*   [机器学习速成课程 &nbsp;|&nbsp; Google Developers](https://developers.google.cn/machine-learning/crash-course/)
*   [床长人工智能教程](https://captainbed.net/)

## Awesome

[Awesome Python](https://awesome-python.com/)

*   [docopt](http://docopt.org/) 命令行参数
*   [Jupyter](https://jupyter.org/) 交互式计算
*   [Loguru](https://github.com/Delgan/loguru) 日志
*   [Matplotlib](https://matplotlib.org/) ([cmn-Hans](https://matplotlib.org.cn/)) 数据可视化
*   [NumPy](https://numpy.org/) ([cmn-Hans](https://numpy.org.cn/)) 科学计算
*   [Orator](https://github.com/sdispater/orator) 对象关系映射
*   [pandas](https://pandas.pydata.org/) ([cmn-Hans](https://pypandas.cn/)) 数据分析和处理
*   [Pipenv](https://pypi.org/project/pipenv/) 开发工作流
*   [profig](https://github.com/dhagrow/profig) 配置
*   [PyCharm](https://jetbrains.com/pycharm) ([~~zh_CN~~](https://github.com/pingfangx/jetbrains-in-chinese/tree/master/PyCharm "已有官译插件")) 集成开发环境
*   [pytest](https://pytest.org/) 测试框架
*   [PyTorch](https://pytorch.org/) ([cmn-Hans](https://pytorch.apachecn.org/)) 机器学习框架
    *   [man cmn-Hans](https://github.com/zergtant/pytorch-handbook)
    *   [doc cmn-Hans](https://pytorch-cn.readthedocs.io/zh/latest/)
*   [sandman2](https://github.com/jeffknupp/sandman2) 为数据库提供 RESTful 接口
*   [schedule](https://github.com/dbader/schedule) 计划任务
*   [Schematics](https://github.com/schematics/schematics) 数据验证 
*   [SciPy](https://scipy.org/) 用于数学、科学和工程的开源软件生态
*   [sh](https://github.com/amoffat/sh) 子进程
*   [SymPy](https://sympy.org/) 符号数学
*   [TensorFlow](https://tensorflow.google.cn) ([cmn-Hans](http://tensorfly.cn/)) 机器学习框架

### CPython 版本管理器 pyenv

``` batch
:: 更新元数据
%USERPROFILE%> pyenv update

:: 列出可用版本
%USERPROFILE%> pyenv install --list

:: 下载某版本
%USERPROFILE%> pyenv install <version>

:: 列出已知版本
%USERPROFILE%> pyenv versions

:: 选择全局版本
%USERPROFILE%> pyenv global <version>

:: 同步垫片
%USERPROFILE%> pyenv rehash
```

参见：

*   [pyenv: Simple Python version management](https://github.com/pyenv/pyenv)
*   [pyenv for Windows | pyenv-win](https://pyenv-win.github.io/pyenv-win/)

### Python 运行时 CPython

``` batch
:: 使用 Scoop 安装 CPython
%USERPROFILE%> scoop install python

:: 交互式 Python 壳层
%USERPROFILE%> pip install ipython
%USERPROFILE%> ipython

:: 运行 Python 脚本
%USERPROFILE%> python <script.py>
```

参见 [CPython](https://github.com/python/cpython)。

### Python 包管理器 pip

``` batch
:: 列出配置
%USERPROFILE%> pip config list

:: 列出系统配置
%USERPROFILE%> pip config --global list

:: 列出用户配置
%USERPROFILE%> pip config --user list

:: 列出项目配置
%USERPROFILE%> pip config --site list

:: 编辑配置
%USERPROFILE%> pip config --editor=notepad edit

:: 配置豆瓣镜像
%USERPROFILE%> pip config set global.index-url https://pypi.doubanio.com/simple

:: 升级 pip
%USERPROFILE%> python -m pip install --upgrade pip
:: abbr.       python -m pip install -U pip

:: 列出已安装的包
%USERPROFILE%> pip list

:: 搜索 PyPI
%USERPROFILE%> pip search <package>

:: 安装包
%USERPROFILE%> pip install <package>

:: 升级包
%USERPROFILE%> pip install --upgrade <package>
:: abbr.       pip install -U <package>

:: 卸载包
%USERPROFILE%> pip uninstall <package>
```

参见：

*   [pip - The Python Package Installer](https://pip.pypa.io/en/stable/)
*   [PyPI · The Python Package Index](https://pypi.org/)
*   [Python Packaging Authority](https://www.pypa.io/en/latest/)

### Python 环境管理器 Pipenv

``` batch
%USERPROFILE%> pip install pipenv

%USERPROFILE%> pipenv {--three | --two}

%USERPROFILE%> pipenv install [--dev] <package>
:: abbr.       pipenv install [-d] <package>

%USERPROFILE%> pipenv uninstall <package>

%USERPROFILE%> pipenv lock

%USERPROFILE%> pipenv sync

%USERPROFILE%> pipenv run python <script.py>
```

参见 [Pipenv: Python Dev Workflow for Humans](https://pipenv.pypa.io/en/latest/)。

### Jupyter Notebook

```batch
%USERPROFILE%> pip install jupyter notebook

%USERPROFILE%> jupyter notebook [script.ipynb]
```

参见 [Project Jupyter](https://jupyter.org/)。

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
