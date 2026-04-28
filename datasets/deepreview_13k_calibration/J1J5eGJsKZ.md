# ToolDial: Multi-turn Dialogue Generation Method for Tool-Augmented Language Models

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Tool-Augmented Language Models (TALMs) leverage external APIs to answer user queries across various domains. However, existing benchmark datasets for TALM research often feature simplistic dialogues that do not reflect real-world scenarios, such as the need for models to ask clarifying questions or proactively call additional APIs when essential information is missing. To address these limitations, we construct and release ToolDial, a dataset comprising 11,111 multi-turn dialogues, with an average of 8.95 turns per dialogue, based on APIs from RapidAPI. ToolDial has two key characteristics. First, the dialogues incorporate 16 user and system actions (e.g., request, clarify, fail inform) to capture the rich dynamics of real-world interactions. Second, we simulate dialogues where the system requests necessary information from the user based on API documentation and seeks additional APIs if the user fails to provide the required information. To facilitate this process, we introduce a method for generating an API graph that represents input and output compatibility between APIs. Using ToolDial, we evaluate a suite of language models on their ability to predict correct actions and extract input parameter values for API calls from the dialogue history. Modern language models achieve accuracy scores below 70\%, indicating substantial room for improvement. We provide a detailed analysis of the areas where these models fall short.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work introduces a new dataset for tool calling in LLMs for a multi-turn setup. It consists of conversations where the API calls are dependent on the context in the previous turns as well as require the system to request/clarify more information from the user. The dataset has been generated. The benchmark is evaluated on three tasks - action prediction, dialogue state tracking, and correctness of the API call. Experiments are conducted on four GPT-based versions and one fine-tuned LLaMA.

Score was updated from 6-> 8. See comments for the updated score

### Strengths
1. Moving to multi-turn use of tool calling is new and timely to the TALM literature.
2. Instead of relying on one task for evaluation, the benchmark supports three smaller tasks to get a better understanding of the model's performance.

### Weaknesses
1. Non-LLM based baselines need to be included for completeness

2. The dataset was constructed using an LLM (GPT4-o-mini) - perhaps some artifacts in generation can lead to undesirable effects . The authors back up the dataset quality through human evaluation as well, but perhaps a blind test prepared by human authors can also be helpful.

3. The experiments in this work are still preliminary (see suggestions). Addition of more experimental details, clearly signifying the type of prompting baselines, inclusion of another open source LLM, experimenting with chain-of-thought like prompting (https://arxiv.org/abs/2403.04656) can also be useful.

### Questions
Questions:
1. What was the setting for the GPT-based experiments - zero-shot or in-context learning? Please add these details in the next version of the draft
2. Could you explain why does GPT-4o-mini perform better without ground truth in Table 4?
What are the domains of the examples in the dataset?


Suggestions:

1. Please mention the language of the dataset in the paper 
2. Please include qualitative examples from the dataset describing (i) examples after the data collection is complete and (ii) failures of respective LLMs
3. Please report at least three significant digits when reporting the results
4. As it is a multi-turn dataset, inclusion of task completion metric - when the model performs all the correct api calls at every turn it is marked as a complete task. See goal accuracy under https://aclanthology.org/2022.acl-short.35 
5. Please include vanilla LLaMa results in Table 5. 
6. While GPT based results are not reproducible (based on API changes), it may be useful to release the predictions from those runs for future work to be built on this work.
7. While it is exciting to benchmark the models on, non LLM based baselines such as BERT based/T5 based dialogue state tracking/action recognition should also be evaluated for completeness
8. The dataset construction section is a little hard to understand. Perhaps a running example may make the section clear.
9. [Future work] As API calls are similar to function calling in Python, it would be useful to also benchmark CodeLLaMa/finet-uned CodeLLaMa for the given benchmark

Missing References:

Léo Jacqmin, Lina M. Rojas Barahona, and Benoit Favre. 2022. “Do you follow me?”: A Survey of Recent Approaches in Dialogue State Tracking. In Proceedings of the 23rd Annual Meeting of the Special Interest Group on Discourse and Dialogue, pages 336–350, Edinburgh, UK. Association for Computational Linguistics.

Schick, Timo, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda and Thomas Scialom. “Toolformer: Language Models Can Teach Themselves to Use Tools.” ArXiv abs/2302.04761 (2023): n. pag.


Nikita Moghe, Patrick Xia, Jacob Andreas, Jason Eisner, Benjamin Van Durme, and Harsh Jhamtani. 2024. Interpreting User Requests in the Context of Natural Language Standing Instructions. In Findings of the Association for Computational Linguistics: NAACL 2024, pages 4043–4060, Mexico City, Mexico. Association for Computational Linguistics.

Please see the related work of: 


Qin, Yujia, Shi Liang, Yining Ye, Kunlun Zhu, Lan Yan, Ya-Ting Lu, Yankai Lin, Xin Cong, Xiangru Tang, Bill Qian, Sihan Zhao, Runchu Tian, Ruobing Xie, Jie Zhou, Marc H. Gerstein, Dahai Li, Zhiyuan Liu and Maosong Sun. “ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs.” ArXiv abs/2307.16789 (2023): n. pag.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper addresses the limitations of existing benchmarks for Tool-Augmented Language Models (TALMs), which often feature simplistic, single-turn dialogues that don't reflect real-world complexities. To bridge this gap, the authors introduce ToolDial, a dataset comprising 11,111 multi-turn dialogues with an average of 8.95 turns per dialogue, based on APIs from RapidAPI. ToolDial is designed to simulate rich user-system interactions by incorporating 16 types of user and system actions. The dataset also includes scenarios where the TALM must proactively seek additional APIs when the user fails to provide necessary information. To create ToolDial, the authors develop a method for generating an API graph that represents input and output compatibility between APIs, enabling sequential API calls. They then evaluate various language models on tasks like predicting correct actions, selecting appropriate APIs, and extracting input parameters from dialogue history. The results indicate that modern language models still have significant room for improvements.

### Strengths
1. The authors make appropriate citations and discussions to position their work and justify their contributions. 

2. This paper makes solid contributions to the dialogue community. Two of the most popular dialogue state tracking (user intent extractions) are MWOZ and SGD. Both of them are created over 4 years ago. This is a timely work to establish a new benchmark. It also highlights many-turn interactions which differentiates itself from other API benchmark (e.g. API bank)

### Weaknesses
1. Although I recognize the contributions this paper makes to advance the development of dialogue systems, I am not sure the proposed methodologies for creating the dataset are adequately novel or aligned with the values of ICLR. Maybe the authors can provide more evidence and arguments in the rebuttal.

2. Lack of details about the dialogues and APIs: I would like to (1) see more descriptions of how complex the conversations are, as this is something the authors claim as a novelty, and (2) have a clear view of the APIs—what domains are you using and what types of arguments are you employing? Is there any fundamental difference between yours and the SGD?

### Questions
In Figure 2, the agent response contains symbolic terms from the API (seasonId and tournamentId). I am curious about the reasons for this design. Does this mean you are also showing the APIs to the users at the same time? This will make the interactions less natural. 

I also have a writing suggestion for the authors. Try to condense the paper and move some essential information from Appendix to the main paper. I am constantly scrolling to Appendix section when reading the paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces ToolDial, a dataset specifically designed for Tool-Augmented Language Models (TALMs), focusing on simulating complex, real-world, multi-turn dialogues that involve external API usage. ToolDial consists of 11,111 dialogues, each structured to mirror realistic, multi-step user-system interactions where the model may need to request additional information or call relevant APIs in response to the user’s needs. The authors also propose a approach to dataset creation by using an API graph, which maps input-output compatibility between APIs. This structure enables TALMs to manage the sequence and dependencies of API calls within dialogues more effectively. 

The paper evaluates various language models on ToolDial, providing valuable insights into their performance, particularly in handling multi-turn interactions requiring tool usage. This assessment highlights critical areas where TALMs could improve, notably in maintaining coherence and accuracy over extended dialogues.

### Strengths
(1) The ToolDial dataset addresses a gap in resources for TALMs, providing extensive and nuanced multi-turn dialogue interactions that are more reflective of real-world use cases.

(2) Dataset generation leverages an API graph with GPT models, reducing the reliance on human-curated data and offering a scalable approach that may inspire similar future methodologies.

(3) By evaluating multiple language models on ToolDial, the paper provides actionable insights into model performance, helping to identify specific challenges TALMs face in multi-turn, tool-augmented interactions.

### Weaknesses
1. Heavy reliance on GPT-generated dialogues introduces the risk of bias and synthetic errors inherent to the model, which could undermine the dataset’s realism.

2. The paper lacks a detailed error analysis, missing an opportunity to discuss specific areas where TALMs underperform and how ToolDial might be used to address these issues. Specifically, the analysis should include a breakdown of error types in dialogue state tracking (DST), action prediction, and response generation, going beyond overall accuracy metrics. For example, examining errors in slot filling, value extraction, and API parameter selection would be useful.

3. The evaluation process has potential reliability issues:
(1) There are concerns that the upper bound results (when using ground truth) are lower than expected, especially with the TD-Llama model, which performed worse than anticipated.
(2) TD-Llama (finetuned on Llama3-8b) scores lower than GPT-3.5-turbo in many aspect, a result that appears counterintuitive.

### Questions
1. The concept of "correctness" is unclear. Clearer definitions and criteria for correctness could improve result interpretability. It is calculated at the session level, right?

2. It is unclear how many test samples were used in Tables 4 and 5. The presence of integer scores is unusual, given that the test set consists of 1,166 samples. Including precise sample counts and calculation methods could enhance transparency.

3. It remains uncertain if DST or action prediction are essential to achieving high correctness scores. It seems models could achieve high correctness even with low DST or action prediction accuracy. The authors are encouraged to conduct an ablation study to determine the necessity and impact of DST and action prediction on overall performance.

4. The paper would benefit from a comparison with other works that utilize Tool graphs, such as “Taskbench: Benchmarking Large Language Models for Task Automation.”

### Soundness
2

### Presentation
2

### Contribution
2
