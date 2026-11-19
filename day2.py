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
    ## **Control de versiones** con _git_

    ### ¿Qué es git?

    - git es un **sistema de control de versiones**: registra los cambios de nuestro código (y de cualquier archivo de texto)
    - Permite volver a cualquier estado anterior y comparar dos estados dados

    - Pro Git https://git-scm.com/book/es/v2
    - Changing history, or How to Git pretty http://justinhileman.info/article/changing-history/
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Glosario

    - **Repositorio**: directorio rastreado por git; contiene una carpeta `.git` y se crea con `git init`
    - **Commit**: estado o instantánea del repositorio; se crea con `git commit`
    - **Rama** (_branch_): línea de desarrollo paralela o separada; la predeterminada es `main` y se crea con `git branch` o `git switch -c`

    ![Ramas de git](public/git-branches.png)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Línea de comandos 101

    - `whoami`: ¿quién soy?
    - `pwd`: muestra el directorio actual
    - `ls`: lista el contenido del directorio
      - `ls --color`: muestra colores
      - `ls -a`: muestra también los archivos ocultos (los que empiezan por `.`)
    - `cd`: cambia de directorio (`.` es el actual y `..` el padre)
    - `touch`: crea un archivo vacío
    - `nano`: edita un archivo desde la terminal (alternativa avanzada: `vim`)
    - `cat`: muestra el contenido de un archivo
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Flujo de trabajo básico

    1. Crea un directorio y entra en él: `mkdir test_project` y `cd test_project`
    2. Inicializa un repositorio: `git init`
    3. Comprueba el estado: `git status`
    4. Crea algún archivo: `nano README.txt`
    5. Prepara los cambios (_stage_): `git add README.txt`
    6. Haz el commit: `git commit -m "Primer commit"`

    ![Ciclo de vida de los archivos](public/git-lifecycle.png)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ⚠️ No ejecutes `git init` en tu home

    > No ejecutes `git init` en tu directorio personal, ya que puede provocar confusión y pérdida de datos. Si `git status` muestra muchos archivos sin rastrear que no tienen que ver con tu proyecto, quizá quieras hacer `rm -rf .git` y empezar en otro directorio. Ten en cuenta que este comando elimina todo el historial de git.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Ramas (_branching_)

    1. Crea **y** cámbiate a una rama nueva: `git switch -c nueva-rama`
    2. Haz commits ahí (ver arriba)
    3. Vuelve a la rama principal: `git switch main`
    4. Fusiona los cambios: `git merge nueva-rama`
    5. Borra la rama: `git branch -d nueva-rama` (¡no olvides este paso!)

    Normalmente la fusión ocurre en línea mediante _pull requests_ o _merge requests_, que **no** son conceptos de git, sino de GitHub/GitLab.

    > Si `git switch` no funciona, puede que tengas una versión antigua de Git: usa `git checkout -b` en su lugar.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Fusiones (_merging_)

    Dos tipos de fusión:

    - **_Fast-forward_**: no hay historia divergente y git solo "avanza el puntero" de la rama actual
      - `git merge nueva-rama --ff-only` falla si no es posible una fusión _fast-forward_
    - **_Non fast-forward_**: la historia ha divergido y git crea un commit de fusión (con dos padres) que combina ambas ramas
      - `git merge nueva-rama --no-ff` crea siempre un commit de fusión, aunque sea posible una _fast-forward_
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Conflictos

    Las fusiones _non fast-forward_ pueden acabar en conflictos: git detiene la operación y deja marcas en los archivos afectados:

    ```
    If you have questions, please
    <<<<<<< HEAD
    open an issue
    =======
    ask your question in IRC.
    >>>>>>> branch-a
    ```

    - Abortar la fusión: `git merge --abort`
    - Quedarte con la rama que llega: `git merge nueva-rama --strategy-option theirs`
    - Quedarte con la rama actual: `git merge nueva-rama --strategy-option ours`

    **Ten cuidado** al editar archivos en conflicto y usa tu editor para resolverlos.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Otros comandos útiles

    - Ignorar archivos: `nano .gitignore` (este archivo también se debe commitear)
    - Enmendar el último commit: `git commit --amend`
    - Ver el historial de forma bonita: `git log --graph --oneline --decorate --all`
    - Configurar alias: `git config --global alias.lg "log --graph --oneline --decorate"` y ahora tienes `git lg`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Flujos de trabajo triangulares

    - Lo más habitual al colaborar en GitHub es tener un repositorio central, un _fork_ remoto por persona y clones locales
    - Convención de nombres: `origin` / `<usuario>` / local

    ![Flujo de trabajo triangular](public/triangular-workflow.png)

    https://www.asmeurer.com/git-workflow/
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ⚠️ Después de crear un pull request

    Tras mezclar tu pull request, tu `main` local y el de tu _fork_ se quedan desactualizados respecto a `origin/main`. Recuerda: las ramas deben ser efímeras y de corta vida.

    Para volver a un estado limpio:

    1. Pulsa "Delete branch" en el pull request (¡no "Delete fork"!)
    2. `git switch main`
    3. `git fetch origin` (**nunca** uses `git pull` salvo que sepas exactamente lo que haces)
    4. `git merge --ff-only origin/main`
    5. `git fetch -p <usuario>`
    6. `git branch -d rama-antigua`
    7. `git push <usuario> main`
    8. `git switch -c rama-nueva`

    Este proceso **se repite después de cada pull request**. 🌈
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
