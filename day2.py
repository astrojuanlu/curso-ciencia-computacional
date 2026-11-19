import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Buenas prácticas en ciencia computacional con Python

    Juan Luis Cano Rodríguez ::carbon:email:: <hello@juanlu.space>

    2026-11-18 @ EPSL Universidad de Jaén (online)

    ::octicon:mark-github-16:: https://github.com/astrojuanlu/curso-ciencia-computacional

    ![Fotografía © University of Pennsylvania’s School of Engineering and Applied Science](public/cover.jpg)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Agenda (día 2)

    - **Recapitulación**
    - **Entornos de desarrollo persistentes** con _WSL o Multipass y VS Code_
    - **Control de versiones** con _git_
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Entornos de desarrollo persistentes** con _WSL o Multipass y VS Code_

    ### WSL

    - [WSL](https://learn.microsoft.com/es-es/windows/wsl/) (Windows Subsystem for Linux) es una tecnología que permite utilizar sistemas Linux dentro de Windows de una manera sencilla
    - La versión 2 fue introducida en 2019
    - Utiliza virtualización estándar, pero incluye mejores integraciones con Windows que una máquina virtual normal
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Una vez instalado con `wsl --install`, requiere instalar al menos una distribución. Estas se pueden listar con `wsl --list --online`. Por ejemplo, para instalar Ubuntu 24.04, se puede usar

    ```
    wsl --install -d Ubuntu-24.04
    ```

    ![Primeros pasos con WSL2](./public/wsl-first-run.png)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La integración con VS Code la proporciona la extensión [WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl). Una vez instalada, se debe abrir una conexión WSL, y utilizar VS Code normalmente.

    ![WSL en VS Code](./public/wsl-vs-code.png)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Multipass

    - [Multipass](https://canonical.com/multipass) es un software de Canonical que permite crear máquinas virtuales, principalmente de Ubuntu
    - Es más genérica que WSL y funciona en cualquier sistema operativo (Windows, macOS, Linux), y por eso mismo no tiene integración tan fuerte con Windows como WSL
    - Es más similar a productos como VirtualBox
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Tras instalar la aplicación, es necesario lanzar una máquina virtual usando los selectores, o desde la línea de comandos con `multipass launch 24.04`. A partir de ese momento, la interfaz gráfica de Multipass permite conectarse a la máquina.

    ![Primeros pasos con Multipass](./public/multipass-first-launch.png)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La integración con VS Code requiere poder conectarse por SSH. Hoy en día la mayoría de sistemas Windows tienen clientes SSH preinstalados.

    En primer lugar hay que generar un par de claves público-privadas **desde la terminal de Windows**:

    ```
    ssh-keygen -t ed25519
    ```

    Presionando `<Enter>` para aceptar todos los valores por defecto, debería generarse un archivo `id_ed25519.pub` en un directorio `.ssh`. Su contenido debe pegarse en el archivo `~/.ssh/authorized_keys` **dentro de la máquina de Multipass**, por ejemplo ejecutando desde Windows

    ```
    multipass exec NOMBRE_VM -- bash -c "echo '$(Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub)' >> ~/.ssh/authorized_keys"
    ```

    ![Generación de claves SSH en Multipass](./public/multipass-ssh.png)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A continuación, se debe instalar la extensión [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) en VS Code, y crear una nueva conexión SSH, introduciendo

    ```
    ssh ubuntu@IP_VM
    ```

    La IP de la máquina virtual se puede obtener con el comando `multipass info NOMBRE_VM`.

    ![VS Code conectado a una máquina Multipass](./public/multipass-vs-code.png)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Buenas prácticas en ciencia computacional con Python

    Juan Luis Cano Rodríguez ::carbon:email:: <hello@juanlu.space>

    2026-11-18 @ EPSL Universidad de Jaén (online)

    ::octicon:mark-github-16:: https://github.com/astrojuanlu/curso-ciencia-computacional

    ![Fotografía © University of Pennsylvania’s School of Engineering and Applied Science](public/cover.jpg)
    """)
    return


if __name__ == "__main__":
    app.run()
