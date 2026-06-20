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

14-6-2026

1. Change of plan instead of dealing with API URL and Web Scraping URL separately try to merge them together in a single workflow, like 3 nodes, but have a type to determine what type of data the node is dealing with if its json it will ignore mid node, else will do the whole workflow, in that sense instead of having 6 nodes + 1 anlaysis nodes, we will have 3 nodes with 1 analysis node

2. implement analysis node better than this in a way that make sense, make it print out tokens, time taken, also error messages, and what tasks in each node took most of the time in this subgraph, and whether we need to visit one of nodes again because we failed

18-6-2026

1. instead of writing a track variable to track time, tokens in each node manually i can use langsmith , that is the industry practice, note that langsmith for google gen needs to be installed, there is different langsmith installation for each different llm
2. clear description to LLM is important
3. what if text file or dataset is locked being processed, shouldn't agent have ability to visit again after some time
4. different encoding issues to be handled
5. what if text file is too large to be processed? what is a better way of processing it without consuming all tokens that are available