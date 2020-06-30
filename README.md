# zhengrr 所知的 Python

官网 <https://python.org/>，Python 始于 1991 年，最初由 Guido van Rossum（吉多·范·罗苏姆）创作。

## 参考

[*Python 3 Docs*](https://docs.python.org/3/ "Python 3 documentation") <sub>
    [*lang*](https://docs.python.org/3/reference "The Python Language Reference"),
    [*lib*](https://docs.python.org/3/library "The Python Standard Library"),
    [*doc*](https://docs.python.org/3.1/documenting/ "Documenting Python") </sub>

[*Sphinx*](https://www.sphinx-doc.org/) <sub>
    [*Sphinx and RST syntax guide*](https://thomas-cokelaer.info/tutorials/sphinx/) </sub>

[*reStructuredText*](http://docutils.sourceforge.net/rst.html)

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

*   [*Jupyter*](https://jupyter.org/)
*   [*Matplotlib*](https://matplotlib.org/) <sub>
        [*cmn-Hans*](https://matplotlib.org.cn/) </sub>
*   [*NumPy*](https://numpy.org/) <sub>
        [*cmn-Hans*](https://numpy.org.cn/) </sub>
*   [*pandas*](https://pandas.pydata.org/) <sub>
        [*cmn-Hans*](https://pypandas.cn/) </sub>
*   [*pipenv*](https://pypi.org/project/pipenv/)
*   [*PyCharm*](https://jetbrains.com/pycharm "一款集成开发环境") <sub>
        [*zh_CN*](https://github.com/pingfangx/jetbrains-in-chinese/tree/master/PyCharm) </sub>
*   [*pytest*](https://pytest.org/)
*   [*PyTorch*](https://pytorch.org/) <sub>
        [*cmn-Hans*](https://pytorch.apachecn.org/),
        [*man cmn-Hans*](https://github.com/zergtant/pytorch-handbook),
        [*doc cmn-Hans*](https://pytorch-cn.readthedocs.io/zh/latest/) </sub>
*   [*SciPy*](https://scipy.org/)
*   [*SymPy*](https://sympy.org/)
*   [*TensorFlow*](https://tensorflow.google.cn) <sub>
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

```
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
