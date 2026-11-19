# Ejercicios, día 2

## 1. Primeros pasos con git

- Genera una llave SSH dentro de tu máquina Multipass o WSL, para ello utiliza el comando `ssh-keygen -t ed25519`
- Agrega esa llave SSH a tu cuenta, para ello ve a https://github.com/settings/ssh/new y pega el contenido del archivo `.pub` generado
- Clona tu README personal dentro de tu máquina utilizando la URL SSH (tiene que ser parecida a `git@github.com:USUARIO/USUARIO.git`)
- Abre el directorio en VS Code ("Open Folder...")
- Haz algún cambio en el `README.md` y sincroniza los cambios, bien usando la interfaz gráfica o bien usando comandos de git:

```bash
git fetch
git status
git add README.md
git commit -m 'Edita archivo README.md'
git push
git status
```

**Completado cuando**: Los cambios aparecen en GitHub.

## 2. Proyecto conjunto

En grupos de 4-5 personas, tomad algún dataset público de tamaño pequeño-mediano
y haced un pequeño análisis exploratorio.
No es necesario que sea muy exhaustivo,
pero como mínimo debe dar algunos números sobre los datos analizados
(número de filas, número de columnas,
valores promedio, mínimos o máximos de las variables cualitativas,
valores más frecuentes de las variables cuantitativas).
Por ejemplo https://datos.civio.es/dataset/viviendas-protegidas-desde-1991-por-comunidad-autonoma/

El proyecto debe
- Estar en GitHub en un repositorio público
- Tener un `README.md` con los nombres de los participantes y una breve descripción del dataset analizado
- Código y figuras que sustenten el análisis

**Requisitos**:
- Todas las personas del grupo deben haber contribuido al análisis (de manera conjunta o por separado)
- Todas las personas del grupo deben haber mandado al menos 1 pull request desde su fork
- Cada pull request debe estar aprobado por al menos 1 persona antes de ser mezclado
- (Opcional) Los pull requests deben partir de ramas que no sean `main`
- (Opcional) No deben quedar pull requests abiertos o ramas desactualizadas
