# `pyright-type-completeness`

Composite action to verify type completeness of Python packages with [pyright](https://pypi.org/project/pyright/).

## Why should I check type completeness?

Packages that include a PEP 561 compliant `py.typed` file should ensure the library is actually fully typed to ensure a smooth experience for the user.
As Python's dynamic typing system can make it unclear which symbols should be explicitly typed, using a type checker like Pyright can help ensure that all necessary types are clearly defined. 
Using Pyright type checker to assess a Python package's type completeness is beneficial for at least reasons.
Firstly, Pyright adheres to the official guidelines on Python typing, as outlined at [typing.readthedocs.io](https://typing.readthedocs.io/en/latest/source/libraries.html#how-much-of-my-library-needs-types), ensuring that its recommendations are aligned with best practices in the Python community.
Additionally, Pyright is prominently used by [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) in [Visual Studio Code](https://code.visualstudio.com/), a popular development environment, and as such has been established as a reliable and widely-used tool for type checking in Python.

## Usage

This action must be used in workflows that run on pull requests.
It compares the type coverage of the package in the pull request with the type coverage of the package in the base branch.
If the type coverage of the package in the pull request is lower than the type coverage of the package in the base branch, the action will fail.

### Basic

```yml
steps:
  - uses: Bibo-Joshi/pyright-type-completeness@v1.0.0
    with:
        package-name: 'your-package-name'
```

### Optional

```yml
steps:
  - uses: Bibo-Joshi/pyright-type-completeness@v1.0.0
    with:
      package-name: 'your-package-name'
      python-version: '3.8'
      pyright-version: '~=1.1.160' 
      install-command: 'pip install src/your-package-name'
```

## Inputs

| Name              | Description                                                                                                                                                                                  | Required | Default                  |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|--------------------------|
| `package-name`    | The name of the package to check                                                                                                                                                             | Yes      |                          |
| `install-command` | The command to install the package. This command should install the package in the current directory.                                                                                        | No       | `pip install . -U`       |
| `python-version`  | Python version to use. See [actions/setup-python](https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md#using-the-python-version-input) for more information              | No       | `3.x`                    |
| `pyright-version` | Pyright version to use. Must be a valid version specifier for pip install, see [`pip` user guide](https://packaging.python.org/en/latest/specifications/version-specifiers/#id5) for details | No       | latest available version |

## Outputs

| Name                      | Description                                     |
|---------------------------|-------------------------------------------------|
| `base-completeness-score` | The type completeness score of the base branch. |
| `pr-completeness-score`   | The type completeness score of the PR branch.   |

## Status & Contributions

This action was created as abstraction of the usages of similar workflows in [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot) and [`aiorem`](https://github.com/Bibo-Joshi/aiorem).
It currently only supports the main use cases.
Contributions for further customization and additional features are welcome!
Kindly open an issue or a pull request if you have any suggestions or improvements.
