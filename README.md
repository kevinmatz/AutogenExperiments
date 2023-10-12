# AutogenExperiments
Experiments with Microsoft's Autogen AI code generation tool


## Prerequisites for running these projects locally (using VSCode):

* Install Anaconda (e.g., on Windows, use the installer)

* Install Docker Desktop (and on Windows, WSL) if running any examples that use Docker containers

* Add an environment variable `OAI_CONFIG_LIST` with the choice of model and your OpenAI API key:
  * `[{"model": "gpt-4", "api_key": "sk-..."}]`
  * Models: `gpt-4`, `gpt-3.5-turbo`, `gpt-3.5-turbo-16k`
  * Be sure to restart VSCode and any terminal windows (if adding environment variable through Windows control panel or using multiple terminals)

* Create and activate a conda environment (do this in the project directory)
  * In VSCode, when opening the integrated terminal, it automatically rund:
    * `activate`, which runs `conda.bat activate`, which runs (on my system) `C:\DevTools\anaconda3`
  * `conda create -n my-autogen-env python=3.11.4`
  * `conda activate my-autogen-env`
  * TODO: On Windows, VSCode uses PowerShell by default as the integrated terminal and conda activate does not work in it??? Need to use "cmd", although then the environment does not get picked up in VSCode
    * In left-hand sidebar, select Python icon and select the right entry under Global Environments
    * TODO: Here the new environment has an warning "!" icon and cannot be selected

* `pip install pyautogen~=0.1.0` or if `pip` doesn't work like on my Windows system, use `python -m pip install pyautogen~=0.1.0` (remove version number if latest version is desired)

* `pip install docker` or `python -m pip install docker` for any examples that use Docker containers


## If using Google Colab:

* In Google Colab, click the "Files" icon in the left-hand panel and in the /content/ folder, upload a OAI_CONFIG_LIST.json file that has the OpenAI key in it. Format of this file:
  * `[ { "model": "gpt-4", "api_key": "" } ]`
  
* In the first code block, use:
  * `%pip install pyautogen~=0.1.0`

