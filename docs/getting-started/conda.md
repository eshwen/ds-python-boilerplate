##Conda

1. For a lightweight experience, install `miniconda`. This can be done through

    === "Homebrew (on :material-apple:)"

        ```shell
        brew install --cask miniconda
        ```

    === "Other"

        Figure it out :material-emoticon-wink-outline:

2. Then initialise conda:

    ```shell
    conda init "$(basename "${SHELL}")"
    <exit and reopen terminal>
    ```

3. Create your environment:

    ```shell
    conda create -y -n my_project
    conda activate my_project
    conda config --set auto_activate_base false  # (1)
    conda install -y python=3.10  # (2)
    pip install --upgrade pip
    ```

    1. Stops automatically activating the `base` env when opening the terminal.
    2. This project also supports 3.11 and 3.12 if you want to use those instead.

4. And finally, install the requirements:

    ```shell
    cd <root dir of project>
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    ```
