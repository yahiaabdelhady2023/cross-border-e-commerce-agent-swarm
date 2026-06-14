## Progress

1-6-2026

1. you use WSL on terminal instead of powershell
2. if you type python and get the following error

`
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
`
<br> Solution:  `use alias python ='python3'`

3. uv is faster than pip install 100x times!

4. using venv for linux is different than window's venv, if you are using WSL terminal and windows venv you wouldnt be able to activate it, you have to move whole project into WSL or use powershell or CMD for windows


13-6-2026

1. langchain_hyperbrowser need paid API key, they do heavy lifting for you when it comes to extracting information from webpage rapidly
2. I will use Beautiful Soap instead, to finish this job and ask Agentic AI model 1, to adhere to a specific pydantic schema when it coems to producing output I want to have a list of items in json like format
3. failed to use Soap for AliExpress, must look for a workaround