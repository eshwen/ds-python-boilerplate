# Development Container

This project can be configured to be developed in a Docker container. This allows for a consistent development
environment to be used across different machines and operating systems.

=== ":material-microsoft-visual-studio-code: Visual Studio Code"

    1. Install the **Remote - Containers** extension (`ms-vscode-remote.remote-containers`)
    2. Open this project as a folder
    3. A prompt should appear to open it in a container. Ensure Docker is installed and running so the container can be
       built.

    The devcontainer encompasses the following:

    - Building the Docker container that contains a recent Python image
    - Installing the project dependencies
    - Installing VS Code workspace extensions
    - Applying custom settings to aforementioned extensions

=== ":simple-pycharm: PyCharm"

    1. Under the interpreters tab on the bottom row, hit **Add New Interpreter** -> **On Docker...**
        1. If the **Docker server** is blank, in the dropdown menu click **Create new...** -> **Ok**
        2. Select the correct Dockerfile
        3. Set the **Context folder** to `.`
        3. Uncheck the box **Rebuild image automatically every time before running code**
        4. Optionally, add an image tag to identify it later
    2. Hit **Next** and let the container build
    3. On the final page, the default interpreter should be sufficient
