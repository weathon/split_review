# MindSearch: Mimicking Human Minds Elicits Deep AI Searcher

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Information seeking and integration is a complex cognitive task that consumes enormous time and effort. 
Search engines reshape the way of seeking information but often fail to align with complex human intentions.
Inspired by the remarkable progress of Large Language Models (LLMs), recent works attempt to solve the information-seeking and integration task by combining LLMs and search engines.
However, these methods still obtain unsatisfying performance due to three challenges: (1) complex requests often cannot be accurately and completely retrieved by the search engine once; (2) corresponding information to be integrated is spread over multiple web pages along with massive noise; and (3) a large number of web pages with long contents may quickly exceed the maximum context length of LLMs.
Inspired by the cognitive process when humans solve these problems, we introduce MindSearch (\methodnamechinese) to mimic the human minds in web information seeking and integration, which can be instantiated by a simple yet effective LLM-based multi-agent framework consisting of a WebPlanner and WebSearcher.
The WebPlanner models the human mind of multi-step information seeking as a dynamic graph construction process: it decomposes the user query into atomic sub-questions as nodes in the graph and progressively extends the graph based on the search result from WebSearcher. Tasked with each sub-question, WebSearcher performs hierarchical information retrieval with search engines and collects valuable information for WebPlanner.
The multi-agent design of MindSearch enables the whole framework to seek and integrate information parallelly from larger-scale (\textit{e.g.}, more than 300) web pages in \textbf{3 minute}, which is worth \textbf{3 hours} of human effort.
Based on either GPT-4o or InternLM2.5-7B models, MindSearch demonstrates significant improvement in the response quality in terms of depth and breadth, on both closed-set and open-set QA problems.
Besides, responses from MindSearch based on InternLM2.5-7B are preferable by humans to ChatGPT-Web (by GPT-4o) and Perplexity.ai applications, which implies that MindSearch with open-source models can already deliver a competitive solution to the proprietary AI search engine.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes MindSearch, an LLM-based multi-agent information-seeking framework for complex multi-step information-seeking questions. MindSearch includes a Web Planner which decomposes the user query into atomic sub-questions as nodes in a dynamic graph and progressively extends the graph based on results from the WebSearcher. MindSearch considerably improves in response quality in terms of depth and breadth and also improves over the baseline react-based iterative search system.

### Strengths
1)	The paper demonstrates considerably better output responses for MindSearch, compared to proprietary AI-Search engines like Perplexity Pro and ChatGPT-Web.

2)	MindSearch also works considerably better than the closed-book and ReACT baselines on a variety of multi-hop question-answering datasets. 

3)	Extensive analysis and evaluation provided in terms of the prompting strategy for WebPlanner along with using a graph-based methodology vs JSON-based and code-based.

### Weaknesses
1) While the paper only evaluates for final response quality, it does not consider the attribution quality of the generated response. Popular AI search engines like Perplexity.AI and ChatGPT-web also provide citations as part of the generated output. The authors do not discuss whether MindSearch provides any kind of attribution, and if yes, what does the citation quality look like (based on automatic evaluations like ALCE [1])

2) No analysis was provided with regard to the dynamic graph constructed by the WebPlanner. Does the number of hops in the question match the depth of the tree? How often is an incomplete graph created? Also, it would be interesting to see a cost analysis in terms of the number of search queries that MindSearch generates, in comparison to the baselines (ReACT specifically)


### Questions
1)	The discussion in line 315 is a bit confusing. The authors say “MindSearch does not yield better performance in terms of facticity, but as per Figure 4 in the paper, factuality of MindSearch is preferred 70% of the time.

2)	Please consider showing the example in Figure 5 in English.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents MindSearch, a multi-agent system for complex tasks that uses large language models (LLMs) and search engines for complex web information-seeking tasks. MindSearch addresses complex queries by decomposing them and retrieving information hierarchically, modeling the process as an iterative graph construction to enhance precision and recall. By distributing tasks across specialized agents, the framework manages complex and extended contexts effectively. The authors show that experimental results using GPT-4o and InternLM2.5-7B MindSearch outperforms benchmarks like ChatGPT-Web and Perplexity.ai, with human evaluators preferring its responses.

### Strengths
1. The problem is both interesting and important. Multi-agent systems for complex QA tasks that are robust and effective 

2. Easy to follow and the methods are simple and well explained.

3. Experiments that include inference cost analysis is well considered.

### Weaknesses
1) The work fails to cite and compare to other relevant baselines. For complex QA tasks like HotpotQA or MusiqueQA self-ask[1] with search is a relevant baseline. Similarly Searchain[2] is particularly relevant as it also forms a global reasoning chain or graph where the query is decomposed into subquestions that comprise the nodes of the chain and this planning is similar in philosophy to Mindsearch. I think Assistantbench[3] released in July 2024 is also very relevant and useful to evaluate on. The method SeeplanAct proposed in the paper would serve as a strong baseline. SeeAct[4] is also a relevant baseline. While the authors have cited the same they have not compared to this approach. Other RAG baselines in AssistantBench are also relevant.

2) Some claims are unsupported. For instance the claim made in abstract and section 2.3 regarding the utility of Mindsearch : “Mindsearch performs in 3 minutes tasks worth 3 hours of human effort” has no related evidence cited in the paper. Was there any qualitative evaluation on the benchmark where several human subjects were involved in performing the task with corresponding measurement of time taken ? to compare to mindsearch ?.

3) The work also misses on some important ablations. What happens when Webplanner and code style interaction is not employed ? Is query decomposition required for all queries in web-searcher ? There is also a lack of qualitative analysis of failure scenarios. What happens when response at one node of the chain is wrong ? Does it result in cascading failures. Is there ayn mechanism for the Webplanner to detect such mistakes with feedback from websearcher ? The current approach is a simple tool use based approach which has been well explored in existing WebAgent based works. The additional analysis and error handling mentioned above may help strengthen and understand the core contributions of MindSearch

### Questions
1. What happens when Webplanner and code style interaction is not employed ? Is query decomposition required for all queries in web-searcher ? There is also a lack of qualitative analysis of failure scenarios. What happens when response at one node of the chain is wrong ? Does it result in cascading failures. Is there ayn mechanism for the Webplanner to detect such mistakes with feedback from websearcher ? 

2. Was there any qualitative evaluation on the benchmark where several human subjects were involved in performing the task with corresponding measurement of time taken ? to compare to mindsearch ?


3. how do you respond to the first point in the weakness 1.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel tool agent, MindSearch, which decomposes user queries into atomic sub-questions represented as graph nodes and progressively extends the graph based on the search results from WebSearcher. For each sub-question, WebSearcher performs hierarchical information retrieval using search engines to gather relevant information for WebPlanner. Extensive experiments are conducted, including both open-set and closed-set datasets, and using open-source models alongside close-sourced LLMs, demonstrating the its effectiveness.

### Strengths
S1: The writing and framework of this paper are clear and easy to follow.

S2: The method is novel, utilizing the agents WebPlanner and WebSearcher to perform web search tasks.

S3: Extensive experiments are conducted, demonstrating both the effectiveness and efficiency of this approach.

### Weaknesses
W1: In Figure 5, the words should also be accompanied by English translations.

W2: For WebSearcher, how does the LLM select the most valuable pages from all the retrieved web content? More details should be provided. Additionally, regarding answer generation, the statement, "After reading these results, the LLM generates a response to answer the original question based on the search results," requires further elaboration, such as information on input design or specific prompt construction.

W3: For the open-set evaluation, five experts are chosen. The author should provide more details, including whether these experts had prior exposure to the answers generated by MindSearch. Furthermore, examples should be included to intuitively demonstrate the differences between the responses generated by MindSearch, ChatGPT-Web, and Perplexity.ai.

W4: The author could provide information on token consumption to help the community manage the budget when using MindSearch in their projects.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a system called MindSearch, designed to emulate human cognitive processes to enhance web information retrieval and integration tasks. By combining large language models (LLMs) with search engines, the system addresses limitations in handling complex queries, fragmented information, and lengthy content through an LLM-based multi-agent framework.
* WebPlanner: Simulates the cognitive process of multi-step information seeking by breaking down user queries into atomic subproblems, represented as nodes in a graph. The graph is then progressively expanded based on search results from WebSearcher.
* WebSearcher: Conducts hierarchical information retrieval for each subproblem, using a search engine to gather valuable information for WebPlanner.

This multi-agent design enables MindSearch to search and integrate information from vast web sources within three minutes, equivalent to saving three hours of manual effort. MindSearch demonstrates significant response quality improvements in both closed-set and open-set QA tasks.

### Strengths
- The paper presents a clear and logical approach to the problem, with a well-organized visual format that is easy to understand and read. 
- This method provides a novel question-answering retrieval method based on directed acyclic graphs, which makes the RAG more reasonable.

### Weaknesses
 - The method part is not detailed enough to show the technical details. For instance, the design of DAG and the use of DAG is not clear.
- Few baseline methods from the same category are included, and many RAG-based question-answering approaches are left unexamined, such as ChatKBQA, AutoReAct, etc. 
- The backbone was only tested on GPT-4 (close sourced) and InternLM2.5 (open sourced). Under this setting, it is hard to tell if the MindSearch will work for all (at least most) LLMs.

### Questions
- When constructing the DAG, how does MindSearch automatically create graph nodes? What are some tips for structuring question as graph nodes?
- When large amounts of content are retrieved, how does WebSearcher reduce noise? And, as the rapid growth of web content can easily exceed the maximum context length of the LLM, how does WebSearcher effectively limit content length?
- Additionally, could the experiment include more closed-source and open-source LLMs to further validate the effectiveness of the method?

### Soundness
3

### Presentation
3

### Contribution
3
