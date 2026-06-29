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

21-6-2026
1. need to change json to api in subgraph one
2. need to organise subgraph one, and have state name productState, and organise it more
3. need to write description for subgraph one for each function
4. need to write overall description for subgraph one
5. subgraph two, needs to clarify objective of search, how to merge it with url,
6. do i really need articles category list per country?, i will only focus on global and china together? should all be in one bag or two bags
7. what is some fast llm for classifying articles, should i get whole articles from state[message] right into filter? what are better faster less token consuming techniques
8. i need to change the plan later right? but clarify task subgraph 1 and then subgraph 2 later


24-6-2026

1. need to create subgraph used for dealing with different resources txt,json,api,and handle different error messages
2. that subgraph can be used for all agents whether use api or txt locally to speed up and make development faster
3. in the meantime explore playing with wikipedia agent goal is given a large text file it should be able to fetch required data with minimum resources
4. i noticed llm system prompt sometimes is similar to field of schema
5. is better to have multiple schemas or a single schema which one is faster for a single graph
6. what are some better ways of merging subgraph with other agentic graph workflow without exploding graph is there way to compact it