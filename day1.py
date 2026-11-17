import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium", layout_file="layouts/day1.slides.json")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Buenas prácticas en ciencia computacional con Python

    Juan Luis Cano Rodríguez ::carbon:email:: <hello@juanlu.space>

    2026-11-17 @ EPSL Universidad de Jaén (online)

    ::octicon:mark-github-16:: https://github.com/astrojuanlu/curso-ciencia-computacional

    ![Fotografía © University of Pennsylvania’s School of Engineering and Applied Science](public/cover.jpg)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Agenda (día 1)

    - **Introducción**
      - ¿Por qué este curso?
      - Presentación
      - Temario y objetivos
    - **Desarrollo colaborativo** en _GitHub_
    - **Entornos de desarrollo efímeros** con _GitHub Codespaces_
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ¿Por qué este curso?

    > Computing workflows need to follow the same practices as lab projects and notebooks, with organized data, documented steps, and the project structured for reproducibility, but researchers new to computing often don't know where to start.

    Wilson, G., et al. 2017. "Good enough practices in scientific computing." PLOS Computational Biology 13 (6). https://doi.org/10.1371/journal.pcbi.1005510.

    > we argue that good software practices create better software, and that better software improves the reproducibility and reusability of research

    The Software Sustainability Institute manifesto https://www.software.ac.uk/about-us/manifesto
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > Every employee becomes an agent boss
    >
    > As agents increasingly join the workforce, we’ll see the rise of the agent boss: someone who builds, delegates to and manages agents to amplify their impact and take control of their career in the age of AI. From the boardroom to the frontline, every worker will need to think like the CEO of an agent-powered startup.

    2025 Annual Work Trend Index, Microsoft https://blogs.microsoft.com/blog/2025/04/23/the-2025-annual-work-trend-index-the-frontier-firm-is-born/

    \*Counterpoint: Guest, O., M. Suarez, B. Müller, et al. “Against the Uncritical Adoption of 'AI' Technologies in Academia”. Digital Culture & Education 16, no. 2 (2026): 85–118. https://doi.org/10.5281/zenodo.20082828.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    En resumen:

    - Las buenas prácticas en ciencia computacional ayudan a mejorar la calidad del software en el que se sustenta la investigación
    - Para exprimir la potencia de las herramientas generativas es necesario estructurar el trabajo en torno a la colaboración
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Presentación

    Juan Luis Cano Rodríguez (he/him/él 🇪🇸)

    - Ingeniero Aeronáutico (MSc) from la Universidad Politécnica de Madrid 🛰️
    - 12+ años como desarrollador y data scientist en las industrias aeroespacial, consultoría, software 🧑‍💻
    - Organizador de la comunidad PyData Madrid, fundador de Python España, ex organizador PyConES 🐍
    - Formador para Boeing Research & Technology, Telefónica, UPM, UA, UC3M, IE, ESADE 🎓
    - Ex contribuidor al ecosistema SciPy y PyData 🧪

    ::octicon:mark-github-16:: [github.com/astrojuanlu](https://github.com/astrojuanlu) | ::simple-icons:linkedin:: [linkedin.com/in/juanluiscanor](https://www.linkedin.com/in/juanluiscanor/) | ::simple-icons:tangled:: [tangled.org/juanlu.space](https://tangled.org/juanlu.space) | ::simple-icons:bluesky:: [mu.social/juanlu.space](https://mu.social/profile/juanlu.space)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Temario

    1. **Desarrollo colaborativo** en _GitHub_
    2. **Entornos de desarrollo efímeros** con _GitHub Codespaces_
    3. **Entornos de desarrollo persistentes** con WSL o Multipass y VS Code
    4. **Control de versiones** con git

    Material y ejercicios: https://github.com/astrojuanlu/curso-ciencia-computacional
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Desarrollo colaborativo** en _GitHub_

    ### ¿Qué es GitHub?

    - GitHub es "una forja (plataforma de desarrollo colaborativo) para alojar proyectos utilizando el sistema de control de versiones Git"
    - Utilizada por más del 80 % de los desarrolladores ([Stack Overflow Developer Survey 2025](https://survey.stackoverflow.co/2025/technology#1-code-documentation-and-collaboration-tools))
    - Actualmente es propiedad de Microsoft

    ![Uso de GitHub en 2025](public/github-usage.png)

    https://survey.stackoverflow.co/2025/technology#1-code-documentation-and-collaboration-tools
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Entornos de desarrollo efímeros** con _GitHub Codespaces_

    ### Flujos de trabajo triangulares

    - Desde los '90 se denomina **_fork_** a una bifurcación de un proyecto de software, no siempre amistosa
    - GitHub elevó el concepto y lo convirtió en una herramienta central para contribuir a cualquier proyecto
    - La contribución se hace desde el _fork_ al proyecto original (_upstream_) a través del **_pull request_**
    - El trabajo ocurre en el entorno de desarrollo, que necesita estar sincronizado con ambos

    ![Flujos de trabajo triangulares](https://github.blog/wp-content/uploads/2015/07/5dcdcae4-354a-11e5-9f82-915914fad4f7.png)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Entornos de desarrollo remotos

    - Durante el ciclo de vida de un proyecto de software puede ser necesario instalar, actualizar, sustituir y probar diferentes componentes y herramientas, especialmente durante las fases exploratorias
    - Por otro lado, el entorno de trabajo principal debe priorizar la estabilidad y la robustez para garantizar su fiabilidad en las tareas cotidianas.
    - Las herramientas generativas añaden riesgos adicionales: pueden ejecutar comandos, instalar dependencias y modificar archivos de configuración, con consecuencias que no siempre son fáciles de anticipar
    - Una manera de resolver esta dicotomía consiste en aislar ambos entornos (_sandbox_) y tratar el entorno de desarrollo como algo desechable: debe poder reconstruirse desde cero en cualquier momento sin comprometer el entorno de trabajo principal
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    GitHub Codespaces es un servicio _freemium_ de GitHub para disponer de entornos de desarrollo efímeros en la nube.

    https://github.com/features/codespaces

    ![Botón para abrir GitHub Codespaces](public/codespaces-button.png)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Buenas prácticas en ciencia computacional con Python

    Juan Luis Cano Rodríguez ::carbon:email:: <hello@juanlu.space>

    2026-11-17 @ EPSL Universidad de Jaén (online)

    ::octicon:mark-github-16:: https://github.com/astrojuanlu/curso-ciencia-computacional

    ![Fotografía © University of Pennsylvania’s School of Engineering and Applied Science](public/cover.jpg)
    """)
    return


if __name__ == "__main__":
    app.run()
