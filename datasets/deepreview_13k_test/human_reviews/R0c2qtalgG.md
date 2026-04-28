# MetaTool Benchmark for Large Language Models: Deciding Whether to Use Tools and Which to Use

- Decision: Accept
- Scores: 5, 8, 6, 6

## Abstract
Large language models (LLMs) have garnered significant attention due to their impressive natural language processing (NLP) capabilities. Recently, many studies have focused on the tool utilization ability of LLMs. They primarily investigated how LLMs effectively collaborate with given specific tools. However, in scenarios where LLMs serve as intelligent agents, as seen in applications like AutoGPT and MetaGPT, LLMs are expected to engage in intricate decision-making processes that involve deciding whether to employ a tool and selecting the most suitable tool(s) from a collection of available tools to fulfill user requests. Therefore, in this paper, we introduce \textsc{MetaTool}, a benchmark designed to evaluate whether LLMs have tool usage awareness and can correctly choose tools. Specifically, we create a dataset called \textsc{ToolE} within the benchmark. This dataset contains various types of user queries in the form of prompts that trigger LLMs to use tools, including both single-tool and multi-tool scenarios. Subsequently, we set the tasks for both tool usage awareness and tool selection. We define four subtasks from different perspectives in tool selection, including \emph{tool selection with similar choices}, \emph{tool selection in specific scenarios }, \emph{tool selection with possible reliability issues}, and \emph{multi-tool selection}. We conduct experiments involving eight popular LLMs and find that the majority of them still struggle to effectively select tools, highlighting the existing gaps between LLMs and genuine intelligent agents. However, through the error analysis, we found there is still significant room for improvement. Finally, we conclude with insights for tool developers -- we strongly recommend that tool developers choose an appropriate rewrite model for generating new descriptions based on the downstream LLM the tool will apply to. Our \textsc{ToolE} dataset is available at \href{https://atlas.nomic.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Summary: The paper presents a dataset and a set of tasks that help evaluate Tool calling ability of LLMs. While the work differentiates the abilities into four tasks (A) whether to employ tools (b) Which tools to employ (c) handle the results from the tool (d) return the outcomes to the use, the paper tries to focus on (a) and (b) motivating that the existing works focus on (c) and (d). ToolE dataset with 21,127 user queries, with both single-tool and multi-tool queries. They compare multiple different LLMs on four different tasks based on the dataset and show that ChatGPT performs the best in comparison to others. 

Concerns: 
1. One of the things mentioned is that other works lack diverse user inputs whereas this work does have diverse user inputs. Experiments or evidence for this is missing in this paper?

2.  Keyword Generation and Details Generation: What’s the exact difference between the two?

3.  Multi-tool selection: We select top-15 popular tools — for each pair generate 5 queries
            1. How do you select the popular tools? Manual? 
            2. What do you think of the quality of multi-tool queries?
            3. Multi-tool queries seems to have been created with no semantics associated to the queries or there are no specific details on it. It Is important of have multi-tool queries where the tool combinations are commonly used rather than random tool combinations. Are there any human validations on the percentage of tool combinations that are useful in the dataset?
            4. The results are also pointing in this direction where it seems to be very evident for ChatGPT, Llama2 and Vicena-13B that the queries are multi tool queries — Seems unnatural queries where the patterns are evident? 

 4. Awareness dataset: positive examples from ToolE dataset and negative examples from other datasets
            1. Tt’s unclear how this dataset can be useful. The negative examples will be starkly different from that of the positive examples. Furthermore, it’s unclear if the negative examples truly does not require any tools. There might be setting specifically in commonsense QA where tool use can be useful such as entity extraction and relation extraction from the text that can inform answers. The aspect of tools is probably too domain specific to make such assumptions

5. Tool selection with possible reliability issue: There are concerns how this experiment is setup or the motivation behind this experiment. If the tool is not available and a similar tool is available (Overlapping tool) and if the LLM is able to detect that then shouldn’t the LLM be given those points. This experiments seems non-realistic and would need more investigation on the reliability of LLMs (hallucinations)

6. No Related work: How does this work compare to ToolLLM, toolAlpaca, API-Bank, etc etc. Can those datasets be transformed to Meta-Tool in which case how would that work and what are the drawbacks. The motivation of this work is not very concrete because of the existence of these datasets and no comparison to those. 

7. While at a meta-level these tasks make sense, the aspect of arguments for each of the tools and execution is not focused in this work. A good explanation for this would be useful and makes it easier for the reader to understand. Specifically because when discussing tools, the arguments and executions plays a very important role.

### Strengths
1. The paper states an important problem for using Tools in LLMs
2. The experiments are well done and proves or concludes some hypothesis in the paper regarding LLMs abilities with tools.

### Weaknesses
1. The paper needs to be self sustained -- There are aspects that are unclear in the paper
2. Related work is very important given the number of papers in this domain
3. The experimental setup for some of the tasks does seem unnatural

### Questions
In the summary

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This works studies the ability of LLMs to (1) decide whether to use tools and (2) which tools to use. They introduce a benchmark with over 20,000 prompts that trigger single- or multi-tool usage. Unlike recent related benchmarks, they study the reliability of nine LLMs at tool selection between similar choices, across challenging and diverse scenarios, and when multiple tools are needed. To generate diverse scenario prompts, the authors use algorithms that apply prompting and tool merging & decomposition. Through multiple studies and error analyses, the authors characterize ways in which most LLMs are inconsistent and poorly calibrated at tool usage.

The authors emphasize tool usage as a concrete way to test hallucination (does the LM know when it needs help from a tool? does the LM know which tool to use?) and sycophancy (does the LM know when to defer to tools despite context in the prompt?). The work also makes interesting connections between recommendation (or retrieval) and tool usage from an evaluation standpoint.

### Strengths
1. This benchmark tackles an area with much hype, and offers a much-needed challenging "agent" benchmark.

2. The authors thoughtfully construct MetaTool, following an extensive consideration of the desiderata (Sec 2). This work could be part of making "LLM general-purpose agents" a more systematic and empirical area. 

3. The construction of the dataset is relatively novel. The authors collect 390 tools from OpenAI plugins. They merge (or decompose) tools to reduce benchmark ambiguity.  To construct the queries for evaluation, they prompt OpenAI models in a set of four pipelines. They also generate multi-tool queries from pairs of tools. All queries in the dataset were checked by a human.

4. The definition of the four tasks and the evaluation analyses conducted (3.2, 3.3) are quite rich.

### Weaknesses
1. Section 2 is rich in substance but the presentation is disorderly. There's probably at least 2 different sections that should be there, like "Task Formulation & Desiderata" first then "Dataset Generation" second, but these two considerations are mixed up repeatedly in the current presentation. I'm happy to change my mind on this if the authors would like to defend the current organization.
   
2. It's unclear (and seemingly undiscussed) how fundamentally the generation of the test queries with LLMs biases the evaluation for/against particular models, or reduce the true diversity of these queries.

### Questions
Questions and comments:

1. What kind of dev vs. test guidance do you recommend for this benchmark? Is it meant to be a truly "blind zero-shot, no tuning" dataset? What did the authors do for tuning? Did they use the prompt unchanged for each LLM? (Having no dev set is completely reasonable in principle, but practical considerations tell us that much of the community will, in effect, reuse the test set so often it becomes a dev set. I recommend having at least a few examples explicitly for tuning.)

2. Which Llama2 models were used, vanilla or chat? I presume it's chat. It may be good to include more explicit information in the main text. You find that "the worst-performing model, Llama2-13b, has an F1 Score of only 11.53%". This is surprisingly low. Is this some kind of unintended interaction between the chat format or some other minor detail and the task?

3. Is the word "task" is overloaded in Sec 2.3, where it refers both to the two major tasks "2.3.1" and "2.3.2", and to the four sub-tasks of "2"? Maybe rename the four tool selection tests to "sub-tasks".

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The METATOOL Benchmark paper introduces a new benchmark designed to evaluate the tool usage awareness and selection abilities of large language models (LLMs). The TOOLE dataset contains various user queries that prompt LLMs to use tools, and the benchmark includes tasks for both tool usage awareness and tool selection. The paper presents the results of experiments with several LLMs on the benchmark, and analyzes the performance of the models on different subtasks. The authors also provide insights into the factors that influence tool selection, and discuss potential real-world applications for LLMs with strong tool usage awareness and selection abilities. Overall, the paper's contributions include the development of a new benchmark for evaluating LLMs, insights into the factors that influence tool selection, and a framework for analyzing the performance of LLMs on tool usage tasks.

### Strengths
- The paper is well-written and easy-to-follow. The visualizations are clear and can help readers easily understand the task definitions, model performances, and framework.
- The paper is highly original in its approach to evaluating the tool usage awareness and selection abilities of large language models. The authors introduce a new benchmark, the TOOLE dataset, which includes a wide range of user queries generated using various prompting methods.
- The authors provide detailed descriptions of the TOOLE dataset and the four subtasks in tool selection, and they analyze the performance of several LLMs on the benchmark. The paper's results are presented clearly and are supported by statistical analysis. 
- The conclusions are very insightful: the more detailed the description, the more efficient tool selection.

### Weaknesses
- I think the comparison with existing benchmarks still needs polishing. To the best of my knowledge, I have found these places to be potentially incorrect: (1) API-Bank (https://arxiv.org/pdf/2304.08244v1.pdf) has included the task ① of determining whether LLMs need to leverage external tools or not (level-1 description in Section 1 Page 2. Thus, it might be incorrect to describe API-Bank as only focusing on tasks ③④; (2) ToolBench (https://arxiv.org/abs/2305.16504) also involves the task ②, requiring the retriever to retrieve the most relevant tools. Thus, it is also incorrect to describe the ToolBench as a benchmark that only focuses on tasks ③④; (3) There are also some benchmarks that are missing in the table, like ToolQA (https://arxiv.org/pdf/2306.13304.pdf). In summary, the authors better clarify the differences compared with these existing benchmarks more clearly.
- Most statements in the experiments are not well explained. I think the authors should focus more on the potential reasons and analysis behind these observations.
- I am a little bit confused about the second conclusion you have obtained in Section 3.3. Can you provide more details about the comparison between generated tool descriptions and those provided by tool developers. Like, if we rewrite all the tool descriptions by tool developers with ChatGPT, will we observe a performance gain?

### Questions
See Weaknesses

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper investigates whether models know when to use tools, and whether they know what tools to use. 

The first task is “awareness of tool usage” and it’s a binary classification task. The authors construct the ToolE dataset for this task; the queries are generated using various prompting methods (“emotional generation,” “keyword generation,” “direct diverse generation,” “detailed generation).

The second task is “tool selection.” Four subtasks are proposed to evaluate tool selection: (1) Tool selection with similar choices: select the correct tool from a list containing similar tools. (2) Tool selection in specific scenarios (specialized scenarios). (3) Tool selection with possible reliability issues: given query and tool t, construct tool list such that the t is not in the tool list; assess if LLMs can avoid choosing tools that do not exist in the list. (4) Multi-tool selection. 

The tasks seem to be done in a zero-shot manner based on the prompts in the appendix. For the first task, most models achieve ~random accuracy (except for ChatGPT and Vicuna which are better than the others – also potentially because these models are largest in the batch). Performance on the second task is unsatisfactory too.

### Strengths
Tool use is one of the most powerful ways to improve LLM performance, and there has been lots of recent interest (Toolformer, or even generating new tools).

It’s good that many of the examples shown in this paper are actually how humans may use an assistant in the future. So although the benchmark is artificial, the queries are often relevant to the real world.

### Weaknesses
The “awareness of tool usage” dataset contains positive and negative examples. Positive examples are the ones that require tools, and negative examples are the ones that can be directly solved by LLMs. For negative examples, the authors use three instruction tuning datasets like Commonsense QA and instruction datasets in LIMA. I’m a bit confused because a lot of those questions are quite difficult, and intuitively would definitely benefit from retrieval, for example. The reason LLMs can solve them may be because they appeared in the pretraining/fine-tuning datasets already, so LLMs remember the examples. So why are those instruction tuning datasets in the negative subset (if it wouldn’t harm if they search for info on the internet)? 

Some answers (on whether LLMs need tools for a Q) in Table 12 and Table 13 are debatable in my opinion. I wonder how the authors define a reference answer (on whether LLMs need to use a tool) if with or without the tool, LLM can both solve the question. Similar issue for the second task (tool selection). What would be the human performance on these tasks? 

Relevant to the above two: would it be more prudent to measure “whether LLMs know when to use tools / whether they can use tools” by actually performing tool use experiments – the metric would be the accuracy on the downstream task (e.g., whether the weather actually matches internet search, or whether some calculation actually equals the correct answer, or whether a 2-hour reminder is created in some simulator)?

The experiments are done zero-shot. I wonder if few-shot prompting (with chain of thought reasoning) can improve the performance (on both tasks) by a lot. 
 
I wonder what the tool descriptions are. I don’t see detailed tool descriptions in the paper. I also don’t see any supplementary materials in the submission. In the tool description, is there info on *when* a *language model* should use the tool? If not, then I naturally don’t expect LLMs to do well on the tasks in this paper.

### Questions
Did you use the SFT-tuned & RLHF-tuned llama (which should be llama2-chat) or the plain pretrained llama (without SFT/RLHF finetuning)?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
