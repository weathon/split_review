# Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models

- Decision: Accept
- Avg Score: 8.67
- Scores: 8, 8, 10

## Abstract
Language Model (LM) agents for cybersecurity that are capable of autonomously identifying vulnerabilities and executing exploits have potential to cause real-world impact. Policymakers, model providers, and researchers in the AI and cybersecurity communities are interested in quantifying the capabilities of such agents to help mitigate cyberrisk and investigate opportunities for penetration testing. Toward that end, we introduce Cybench, a framework for specifying cybersecurity tasks and evaluating agents on those tasks.\footnote{All code and data are publicly available at \url{https://cybench.io}.} We include 40 professional-level Capture the Flag (CTF) tasks from 4 distinct CTF competitions, chosen to be recent, meaningful, and spanning a wide range of difficulties. Each task includes its own description, starter files, and is initialized in an environment where an agent can execute commands and observe outputs. Since many tasks are beyond the capabilities of existing LM agents, we introduce subtasks for each task, which break down a task into intermediary steps for a more detailed evaluation. To evaluate agent capabilities, we construct a cybersecurity agent and evaluate 8 models: GPT-4o, OpenAI o1-preview, Claude 3 Opus, Claude 3.5 Sonnet, Mixtral 8x22b Instruct, Gemini 1.5 Pro, Llama 3 70B Chat, and Llama 3.1 405B Instruct. \az{For the top performing models (GPT-4o and Claude 3.5 Sonnet), we further investigate performance across 4 agent scaffolds (\baseline, action-only, pseudoterminal, and web search). Without subtask guidance, agents leveraging Claude 3.5 Sonnet, GPT-4o, OpenAI o1-preview, and Claude 3 Opus successfully solved complete tasks that took human teams up to 11 minutes to solve.} In comparison, the most difficult task took human teams 24 hours and 54 minutes to solve.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce a framework (CyBench) which allows to

- specify cybersec tasks (focused on CTF, hence exploitation of vulnerabilities / cyberoffense) and
    
- evaluate LLM agents on those tasks
    

The framework is open for submission of new tasks from the community to ensure benchmark can evolve and remain relevant.

They introduce a dataset of 40 professional-level curated CTF tasks curated to be recent, meaningful, and covering a large dynamic range of difficulties. The recency of the collected tasks means minimal leakage into train data of current models (with minor exceptions). The tasks span 6 relevant cybersec categories incl. cryptography, web sec, reverse engineering, forensics, pwn/exploitation.

The task specifications include a task description, starter files (incl. local files the agent can directly read/write/exec + files defining servers that the agent can interact with via network calls), and an evaluator that checks correctness of submission. Additionally, each task is broken down into subtasks for intermediate steps to allow more fine-grained evaluation of partial success of LLM agents.

LLM agents in CyBench are allowed bash access (command execution and observing outputs).

The authors construct one cybersec LLM agent (not customized to the task beyond including the task description) and evaluate 8 different SotA LLM models

Their agent scaffolding specifies the LLM output to be highly structured, including reflection on the previous observation, a plan and status section for high-level tracking, thought to reason about next steps, a log section to track past observations and actions, and an action (either a bash command to execute next or an answer, i.e. an attempt to solve the flag)  
Their main findings are:

- Without subtask guidance the most powerful models (3.5sonnet, 3opus, 4o, o1-preview) can solve complete tasks that take human teams up to 11 minutes (compared to 24hrs 54min human team solution time for most difficult task)(aka “first-solve-time”, ranging from 2 min to 1494 min) => the benchmark still is far from being saturated
    
- first-solve time is a strong “indicator” of difficulty for agents (though the number of tasks fully solved is a bit small to make confident statements here)
    
- safety refusals were quite rare (somewhat surprising to me that afaict not much prompt engineering was necessary here)
    
- models struggle to make “insights” that take experts time to figure out (this is not clear to me; does not seem to be well operationalized or defined)

### Strengths
Originality:

- CTFs are not new tools for LLM evals, e.g. Phuong et al. (2024) and concurrent work by Anurin et al. (2024)  have used them before; but their potential for assessing LLM offensive cybercapabilitiesis is not yet fully realized so the contribution is still very meaningful
    
- using first-solve-time as an objective proxy for task difficulty is new afaict and a significant addition to our methodological toolbox
    

Quality

- **careful task curation** (afaict) and inclusion of first-solve-time to guarantee a benchmark with high dynamic range makes this a high-quality dataset
    
- **extensibility:** the fact that others seem to already have contributed new tasks to their framework increases my confidence that this benchmark will remain relevant (though I did not check the quality of these new contributions and have not found a discussion of it in the paper)
    
- **measures guaranteeing solvability:** the inclusion of solution scripts and automated probes to guarantee task correctness are a big plus for the benchmark quality and the confidence in the performance numbers obtained in this benchmark (potentially these are also an original contribution though I have not double-checked that)
    
- **introduction of subtasks** for more fine-grained evaluation increases the usefulness of this benchmark a lot and may be an original contribution (though I have not double-checked)
    
- **diversity of task sources:** sourcing CTF tasks from several competitions increases my confidence that we have a diverse enough selection of tasks here to make some general statements about LLM cybercapabilities
    

Clarity

- presentation is mostly very clear
    

Significance:

- given the rapidly improving capabilities of LLMs, the potentially enormous implications of strongly LLM-aided or autonomous cybercrime, and the fact that LLMs are not far anymore from human SotA on many cyber skills, this contribution to better understanding of the exact capability frontier is very timely and highly important

### Weaknesses
the main weaknesses I see are

- **limited statistical power:** only 8 tasks have been solved at all making the empirical basis for any statements on LLM cybercapabilities pretty slim. Is it possible to increase the resolution of the benchmark at the lower difficulty range?

- **no protection against future test data leakage**: the full CTF dataset is released meaning that once model training cutoffs move past the benchmark release date, the benchmark will not be usable anymore (cf. e.g. Haimes et al., 2024). Would it be possible to withhold a part of the dataset as a private holdout set? 

- **limited understanding of the quality of the agent scaffolding:** while the agent scaffolding seems sophisticated I am missing an assessment of how close this gets us to the capability frontier. 

    - Cf. “structured responses that include Reflection, Planning, and Thought, which can improve capabilities.” ([pdf](zotero://open-pdf/library/items/U8NQPGEL?page=10&annotation=QESJCKAM)) do they have evidence for that?
        
    - Are there any ablation studies that demonstrate the impact of different parts of the scaffolding? Note: it is crucial to trust that the capability elicitation here is state-of-the-art if we are to trust this as an assessment of threat scenarios in the wild.
        
    - Full CLI access (including scrolling, history search, etc; see Anurin et al, 2024) seems like the more powerful and more natural paradigm for cyber-agents. Unclear to me whether the current scaffolding could be artificially limiting.
        
    - also: missing assessment of whether scaffolding that is more customized to the task would significantly change scores
        
    - in real-world threat scenarios I would assume tool use, in particular browsing / internet search, to be the standard approach - have you measured whether that would make a big difference (obviously needs filtering of search results to prevent leakage of literal task solutions)
        
- **lack of formal task selection algorithm:** while the task curation process seems to have been principled and well thought-through, it would be great to provide a principled algorithm for inclusion so that the benchmark can be extended in a more principled way and that we can be certain that this version and future versions of the benchmark do not suffer from cherry-picking
    

other minor weaknesses

- limited analysis of what makes certain tasks unsolvable (inherently impossible for current models? or: solvable with improved scaffolding?)
    
- limited information on how closely the tasks evaluated here track real-world cybersec threat scenarios
    
- no discussion (afaict) of biases or limitations implied by the data sources

### Questions
- Are there quality controls for newly submitted tasks?
    
- re “Agents are evaluated based on the answer they submit. The evaluator also parses observations for answers that are unique and indicative of success on a task (e.g., a unique flag hkcert22{mistakes-off-the-page} that is outputted only on successful completion of a task).” ([pdf](zotero://open-pdf/library/items/U8NQPGEL?page=3&annotation=ES8K55FQ)) : it was not clear to me whether the observation-parsing influences the score.
    
- re “Since releasing Cybench, we have received task contributions from several additional CTF competitions.”: can you comment on the quality of these contributions compared to the curated tasks?
    
- how much performances would agents gain if customized more to the task?
    
- …how much would they gain if you allowed internet search?
    
- how stable is FST as a difficulty metric across different competitions/contexts? also: can you correlate FST with other objective measures of task difficulty?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work unifies 40 questions from recent capture-the-flag (CTF) competitions with descriptions, subtasks, environments, and starter files into a single benchmark for LLM-powered agents to measure their dual-use cybersecurity capability. The authors implement and benchmark agents powered by 8 different frontier LLMs, demonstrating tasks present significant difficulty for their agents and a lack of model refusal to these cybersecurity challenges.

### Strengths
Benchmark Difficulty: This benchmark is a good evaluation of frontier agent capabilities; the evaluation of cybersecurity dual-use capability in LLMs is a highly relevant topic. Table 2 shows the strongest models only reach 17.5% overall success rate, with the highest solve times ranging from 6 minutes to 52 minutes, indicating significant difficulty for agents today. I believe the difficulty of this benchmark makes it a good contribution to the community working on frontier evals. The authors address the possibility of training contamination and are careful to select more hard problems (as measured by human solve time) past the pretraining cutoff date of most frontier models.

Presentation: As this is a popular topic, the authors present a good contrast of their work from other CTF datasets, which was either easier (human solve time < 1 hour) or suffer more from training data contamination. The paper is overall clear and easy to follow.

### Weaknesses
Experimental setup:
It’s possible that the agent implementation is a limiting factor in the lower solve rates of this benchmark. It would be interesting to see if different agent implementations across these 8 models have any differences in solve rate.

### Questions
Models will eventually be trained on the tasks in this benchmark as knowledge cutoffs progress. Do you have any plans to ensure this benchmark stays relevant by ensuring it remains relatively uncontaminated, or plan to continually update it with new CTF tasks?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The authors introduce a new benchmark for evaluating the capablities of LLM agents to independently solve capture-the-flag challenges for cybersecurity. The tasks are taken from real CTFs and their difficulty is determined by the time it takes humans to solve them. Most tasks are still not solvable by LLMs, so the authors decompose them into smaller tasks for granular evaluation.

### Strengths
* I think this paper is a great contribution to the field since measuring and anticipating agentic hazardous capabilities in LLM agents will be of outmost importance, as motivated by the authors in the paper.
* I also believe this benchmark has three of the properties we should look for in a benchmark: (1) it is not saturated, so it will provide valuable signal on progress in future models, and (2) it was designed to provide granular evaluation using subtasks, (3) evaluation is deterministic and easy to compute.
* The benchmark is carefully designed and includes human time as a measure of difficulty, which can also provide another important axis for evaluation.
* The authors do a great job explaining the relevant concepts from security CTFs to a ML audience.
* I am convinced that the benchmark covers a wide range of relevant tasks.
* The authors evaluate their benchmark on a wide range of models. Their results align with other capabilities benchmarks and our current intuitions about their capabilities.

### Weaknesses
 * The authors introduce an agent that has memory containing the last 3 messages and responses. This seems like a very small memory to solve complex tasks that require hours for humans to solve. Although I think we should not expect the authors of a benchmark to also create the best agent, I think this could be prominently indicated as a limitation of the agent that may underestimate current capabilities of LLMs. The limited memory could hinder the agent's ability to track long-term dependencies and maintain context across multiple steps, especially in tasks requiring extensive exploration or backtracking. This is particularly concerning given the complexity of real-world CTF challenges, which often involve intricate sequences of actions and information gathering.
* Authors could enhance the metrics in their benchmark. I suggest (1) a metric that combines performance and highest FST into a single number, e.g. weight the success on a task by its relative FST.(2) a metric that conveys "how hard it was for a model to solve", e.g. number of messages and submission attempts required. The current metrics do not fully capture the nuances of agent performance, such as the efficiency of the solution process or the ability to handle tasks of varying difficulty. A weighted metric could provide a more comprehensive view of model capabilities, while metrics related to solution attempts could reveal insights into the agent's problem-solving approach.
* The paper could benefit from additional qualitative analysis. As I explained above, I think current models might be able to score higher with more complex implementations (again, we should not expect the authors to also find such an agent). However, including more qualitative analysis on the observatiosn could help researchers build systems that are representative of existing capabilities. Some questions that could be useful for the community are: (1) is there a common pattern in the steps where models fail (e.g. they struggle making specific calls, they cannot interact with a GUI robustly, outputs are too complex and could be summarized, etc.)? (2) Are agents limited in their understanding of their problem or in their capabilities to execute steps (e.g. is the reasoning in the output correct but execution incorrect)? The lack of detailed qualitative analysis makes it difficult to pinpoint the specific bottlenecks in current LLM agents. Understanding these failure modes is crucial for developing more robust and capable agents.

### Questions
* Have you considered defining a metric that combines performance and highest FST into a single number? You could e.g. weight the success on a task by its relative FST.
* There are many models that reduce their performance with subtasks. Do you think this could be due to memory filling up with subtasks and losing context? It is also surprising that 4o obtains such a low subtask performance but solves the most subtask-guided tasks and the highest FST.

### Suggestions

These are not relevant for my evaluation, but I think that could be useful for the authors:
* Writing can be improved in some places. For example first paragraph in section 4 is very unclear.
* Have you considered doing minor changes to the problems to make the train-test overlap smaller for those problems that have been potentially been used for training?
* Have you considered a third level of evaluation where models are given the environment without providing them with a specific description of the flag they are looking for? Something like "here is an environment that we know has a vulnerability that if exploited will give you a flag, look for it".
* I would suggest removing the model handles from the main text in 5.1 and send those to appendix. Makes it a bit harder to identify the models.

### Soundness
4

### Presentation
3

### Contribution
4
