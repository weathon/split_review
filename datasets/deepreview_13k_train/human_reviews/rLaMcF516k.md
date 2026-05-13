# Make LLMs better zero-shot reasoners: structure-oriented autonomous reasoning

- Decision: Reject
- Scores: 6, 3, 3, 8, 6, 3

## Abstract
Zero-shot reasoning methods with Large Language Models (LLMs) offer significant advantages including great generalization to novel tasks and reduced dependency on human-crafted examples. 
However, the current zero-shot methods still have limitations in complex tasks, e.g., answering questions that require multi-step reasoning.
In this paper, we address this limitation by introducing a novel \analysis method to help LLMs better understand the question and guide the problem-solving process of LLMs.
We first demonstrate how the existing reasoning strategies, Chain-of-Thought and ReAct, can benefit from our \analysis. 
In addition to empirical investigations, we leverage the probabilistic graphical model to theoretically explain why our \analysis can improve the LLM reasoning process. 

To further improve the reliability in complex question-answering tasks, we propose a multi-agent reasoning system, \textbf{S}tructure-oriented \textbf{A}utonomous \textbf{R}easoning \textbf{A}gents (SARA), that can better enforce the reasoning process following our \analysis by refinement techniques and is equipped with external knowledge retrieval capability to reduce factual errors.
Extensive experiments verify the effectiveness of the proposed reasoning system. Surprisingly, in some cases, the system even surpasses few-shot methods.
Finally, the system not only improves reasoning accuracy in complex tasks but also demonstrates robustness against potential attacks that corrupt the reasoning process.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a structure-oriented analysis method and a multi-agent reasoning system to enhance zero-shot reasoning capabilities in LLMs. The authors claim improvements in complex, multi-step tasks by leveraging a structure-based analysis inspired by human cognition, which identifies key syntactic and grammatical components of questions and uses multiple agents to ensure reasoning accuracy and factual reliability.

### Strengths
1. The idea is interesting. It applies syntactic and grammar parsing to guide LLM reasoning paths, mimicking human-like structured analysis. Additionally, the authors use probabilistic graphical models to represent the reasoning process, which provides an interpretable way to understand the model's decision-making.
2. Authors provides a detailed breakdown of each contribution, showing a clear understanding of the effectiveness of proposed methods.
3. Easy to follow the structure of the paper.

### Weaknesses
1. The evaluated LLMs are limited (4 LLMs), which may not be representative of the entire LLM space. The authors should consider evaluating more models (especially the open-sourced LLMs) to ensure the generalizability of their findings.
2. The evaluated datasets are also limited, which may not fully capture the diversity of reasoning tasks. 
3. It could further discuss the computational efficiency of implementing SARA across large datasets, as the proposed method may be computationally expensive.
4. The paper focuses on reasoning capabilities, but only evaluates on QA tasks. It would be beneficial to evaluate on more diverse tasks to demonstrate the generalizability of the proposed method.
5. I recommend expanding the Related Works section to provide a more comprehensive overview of the field. Currently, the section references only a limited number of studies, which might not fully represent the breadth of research in zero-shot reasoning and multi-agent systems in LLMs (you can consider add some works about 'deciphering GPT-4-o1').
6. The analysis lacks depth in discussing the limitations and reasons behind the performance of the proposed method.

### Questions
1. The probabilistic model on Assumption 3.1 assumes independence among hidden variables in exploring reasoning paths. This assumption could be restrictive, as real-world tasks may involve dependencies between steps. How does the model handle such dependencies? Please justify the applicability in complex reasoning tasks. 
2. The structure-oriented analysis relies on syntactic and grammatical patterns, what happens when the questions are ambiguous or lack clear structures? How does the model adapt to such scenarios?
3. What if the Retrieval Agent provides information that conflicts with the Reason Agent’s initial understanding? Could you elaborate more?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper stressed the challenges of zero-shot reasoning ability of LLMs on complex tasks. Inspired by human reasoning behaviros, the authors introduce a method based on the linguistic and logical structures to help LLMs break down complex tasks and give the answer through a iterative reasoning process. The authors develop a multi-agent system SARA based on the method with a reason agent to analyze grammar and syntax, a refinement agent to resolve inconsistencies and logical error, a retrival agent to access external knowledge and a shared memory to store the intermediate states. Compared with few-shot baselines, the authors performed experiments on four models across four different datasets to validates the effectiveness of the method. In addition, the method shows robustness against malicous injections in demonstrations and irrelevant information in problem statements.

### Strengths
1. This work introduce a intuitive method to break down complex tasks through grammar and syntax structure analysis and help LLMs to give answers via iterative reasoning.
2. This work provides theoretical analysis and empirical evidence to validate the effectiveness of the method. The experiments cover both open-source and closed-source models and are performed on both literal and science tasks. All the models show remarkably higher performance than  baselines.

### Weaknesses
1. The authors have conducted ablation studies on each components of the SARA system. However, the experiments are limited to agents that backended by the same model. To enhance the study, it is recommended to perform future experiments including analyses examining the impact of assigning different models to different agent roles within the system and how the models' performance influences each parts.
2. The method is somewhat incremental considering many previous works about multi-agent systems/debate systems and the novelty is limited.

### Questions
1. The performance of Llama3-70B on MMLU-BIO and MMLU-PHY improves significantly using SARA compared to its vanilla results but shows little advantage compared to GPT-4. Why can't this method help open-source LLMs out-performs closed-sourced ones on STEM tasks?
2. I wonder the effectiveness of this method on math reasoning problems.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes using structure-oriented analysis to improve zero-shot reasoning of language models (specifically for knowledge-intensive tasks). The authors motivate how structure-oriented analysis by leaning on the hypothesis that inference with language models emulates a PGM constructed on the pretraining data. The models explore neighboring nodes in the PGM based on key properties of the question, and the knowledge of states on the path of correct reasoning helps reduce reasoning errors. Then the authors get into their method SARA, which comprises three agents performing reasoning, refinement, and retrieval. Their results show that their method improves performance over baselines such as CoT and ReAct (zero-shot) on tasks like hotpotQA, fever, MMLU.

### Strengths
* The paper is well-organized and easy to follow
* Their system SARA achieves reasonable improvements over other prompting baselines
* The PGM analysis is intuitive and could potentially be useful to the larger community

### Weaknesses
 * The paper is missing a lot of related works that focus on sub-task or sub-question decomposition to improve reasoning or LLM agent performance, see the list below:
    * [Socratic CoT](https://arxiv.org/abs/2212.00193)
    * [Least to Most Prompting](https://arxiv.org/abs/2205.10625)
    * [Decomposed Prompting](https://arxiv.org/abs/2210.02406)
    * [Adapt](https://arxiv.org/abs/2311.05772)
    * [Screws](https://arxiv.org/abs/2309.13075)
    * [ART](https://arxiv.org/abs/2311.07961)
    * [Self-Discover](https://arxiv.org/abs/2402.03620)

*  The primary assumption in this work (corroborated by ablations) is that *syntactic structures are useful to guide the reasoning process*, which seems very specific to knowledge-intensive multi-hop QA and not just any reasoning dataset. For e.g., I don't see a reason why this setup should work for math or logical reasoning datasets (GSM8K, MATH, ARC, BigBench, etc.) To that end, I found the title and abstract overly generic or a bit misleading since the scope of the work does not cover all forms of reasoning.  

* Are the main improvements coming from the fact that instead of one environment (retrieval) in ReAct, which is already quite expensive, we are increasing the computational budget of each step (reason, retrieve, verify/refine)? I would like to see how SARA fairs against self-consistency, ReAct with multiple trials, or step-wise self-consistency for agentic tasks as in [this paper](https://arxiv.org/abs/2402.13212)

* On a related note,  the paper lacks a cost (token budget) vs. performance tradeoff. SARA generates far more tokens than any of the baselines; comparison with just a few-shot CoT/ReAct may not suffice since additional tokens are on the input side. Why not have zero-shot SC as a baseline, or sample multiple responses and ask the model to decide which one is best / [Meta-reasoning](https://arxiv.org/abs/2304.13007)

* The paper does not include 0-shot Chain-of-Thought (CoT) as a baseline, which is a standard zero-shot prompting technique. This omission makes it difficult to assess the true contribution of the proposed method compared to a simple, yet effective, zero-shot baseline.

* The reported results for CoT with self-consistency (CoT-SC@10) show only marginal improvements over the greedy zero-shot baseline, which is inconsistent with existing literature and common experience. Typically, self-consistency with multiple samples yields a more significant performance boost. This raises concerns about the implementation and evaluation of the CoT-SC@10 baseline.

### Questions
1. Are there any more datasets where this method would find application?
2. The paper hinges on the model discovering and generating "structures." Is it fair to rely on the model's ability to do so without any training?  How will this generalize to other tasks where finding such structures is harder, like for math reasoning?
3. What is the role of the memory in the agent? Is the memory instance specific, if so how is it different from just keeping history around in ReAct trajectory?
4.  Why not use EM (exact match) for HotpotQA like the ReAct paper, what is the justification for this choice, and what do the results look like with EM metric for HotpotQA?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce a structure-oriented analysis method that enhances LLMs’ ability to understand question structure by systematically identifying and reasoning through key components before addressing a problem. This structured approach, applicable to most standard LLM prompting methods, is validated with CoT and ReAct, using syntactic and grammatical analysis to identify crucial components, relationships, and sub-questions within a problem statement.
To implement this structure-oriented analysis, the authors uses four components—Reason, Refine, Retrieve, and Shared Memory—that collectively enforce structured reasoning, improve accuracy through iterative refinement and retrieval of external knowledge.

The theoretical foundation for this approach is grounded in probabilistic graphical models (PGMs), which the authors use to illustrate how structure-oriented analysis can guide LLMs along correct reasoning paths. By capturing the relationships between observed knowledge components and latent variables, PGMs demonstrate how this structured approach minimizes reasoning errors by identifying critical intermediate variables along the optimal reasoning path.

Experiments show that SARA effectively enhances performance across diverse natural language tasks, with results sometimes surpassing few-shot methods. Additionally, SARA exhibits robustness against attacks aimed at disrupting the reasoning process.

### Strengths
- Interesting theory motivation
- Really good experimental protocol:
    - Ablations on the contributions of each part of the structure, retrieval and refinement are complete to 
    - Showed the versatility to multiple base models

### Weaknesses
 - Only evaluated the application of the method to natural language tasks. Would have liked to see how that applies to other tasks that required reasoning, e.g. math. There’s probably not a 1:1 mapping with grammar/syntax, but task decomposition seems quite close, and I see your method general enough to do that. Have you already tried this?
- The correctness/soundness structured analysis is only captured by the downstream performance on the task. Have you thought about investigating the analysis in a more direct way? Would the use of structured outputs (e.g. parsing the string into 1.,2.,3.,4. enable you to create evaluation metrics?)
- Robustness on attacks is interesting theoretically but i) I am not sure how important that is to the story, ii) attacks on few-shot: you also show that the method is applicable to few-shots prompting. 
- I don’t see a limitation paragraph, what are those? Can you add a paragraph?

### Questions
- The structured oriented analysis seems to be quite close to [1], but not grounded on reasoning modules (which is nice).
- In practice, I am curious how such attacks could happen as they would be happening on backend side, whereas easier prompts attacks could happen on client side.
- “However, these approaches either rely on task-specific examples (few-shot) or suffer from ineffectiveness on complex tasks (zero-shot).” —> you mentioned ToT and GoT. How do they compare in accuracy on the benchmarks you ran (not asking for running this baseline, but reporting if there are numbers in their paper) but to have an idea on their ‘ineffectiveness’ 

[1] 'Self-Discover: Large Language Models Self-Compose Reasoning Structures', Pei Zhou et al.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Structure-oriented Autonomous Reasoning Agents to improve reasoning in LLMs. 
It proposes a structure-oriented analysis, utilizing probabilistic graphical models.
They also prove that identifying the important reasoning steps is crucial in exploring the correct reasoning path.
The results show the effectiveness and robustness of SARA.

### Strengths
1. This paper proposes to use probabilistic graphical model to interpret the reasoning process.
2. The authors test the robustness against backdoor attacks in reasoning to prove its robustness.
3. The ablation study demonstrates the effectiveness of each component.

### Weaknesses
 1. The evaluation is not comprehensive. They do not include common reasoning tasks, such as arithmatic reasoning, commonsense reasoning, and symbolic reasoning. Since the authors did not claim the scope of the reasoning problems they are about to address in the introduction, we, the readers, should assume this is a solution towards general reasoning. And the general reasoning should evaluate a wide range of domains, not just HotpotQA, Fever, and two subsets of MMLU. So this is either an overclaim or a relatively weak evaluation. The lack of evaluation on tasks like GSM8K, MATH, and StrategyQA, which are standard benchmarks for assessing mathematical, symbolic, and commonsense reasoning respectively, makes it difficult to gauge the true scope and limitations of SARA. The current evaluation is heavily skewed towards knowledge-intensive tasks, leaving a significant gap in understanding its performance on other critical reasoning domains.
2.  Lack of analysis of computing time and consumed tokens. Decomposing is a commonly-used approach in improving reasoning ability in LLMs. While it is effective, it also introduces extra computation. Based on the description of SARA, both the input tokens and the output tokens will grow dramatically and the authors should report that and compare it to other methods. The absence of a detailed analysis of computational cost, including both time and token consumption, is a significant oversight. Given that SARA involves a decomposition process, it is crucial to understand the overhead it introduces compared to other methods. Without this information, it is difficult to assess the practical applicability of SARA, especially in resource-constrained environments.
3.  While using probabilistic graphical models to interpret the reasoning process is valuable, the insights it provides are rather limited. It proves a somewhat intuitive point that identifying the important reasoning steps is crucial in exploring the correct reasoning path. This is also well-aligned with existing knowledge. The theoretical analysis using probabilistic graphical models, while interesting, does not yield substantial new insights. The conclusion that identifying critical reasoning steps is important is already well-established, and the PGM framework does not offer a significant advancement beyond this existing understanding. The analysis feels more like a formal justification of an intuitive idea rather than a novel theoretical contribution.

### Questions
1. Can you add more evaluations of common reasoning tasks, like GSM8K[1], MATH[2], StrategyQA[3]? Without these benchmarks, the readers are unable to compare SARA to other methods.

2. Can you clarify the scope of SARA? From what I see, this is an approach towards only knowledge-intensive tasks, which is also revealed by the datasets you choose and the examples in your paper.

3. Can you report computing time and consumed tokens and compare them to other methods? This can provide insights to the correlation between consumed tokens and improved accuracy.

4. Can you explain the novelty of your proposed agents compared to others, for example, the one used in Minecraft [4] and the general architecture defined in [5]? It also consists of a decomposer (your Reason Agent), a planner (can be viewed as both reasoning and refining), a knowledge part and a memory part, which can also solve complex reasoning and planning tasks. I don't see much difference here with other agents that were proposed more than a year ago. And using "agents" to improve reasoning is already a common practice [6][7].







[1] Cobbe, Karl, et al. "Training verifiers to solve math word problems." arXiv preprint arXiv:2110.14168 (2021).

[2] Hendrycks, Dan, et al. "Measuring mathematical problem solving with the math dataset." arXiv preprint arXiv:2103.03874 (2021).

[3] Geva, Mor, et al. "Did aristotle use a laptop? a question answering benchmark with implicit reasoning strategies." Transactions of the Association for Computational Linguistics 9 (2021): 346-361.

[4] Zhu, Xizhou, et al. "Ghost in the minecraft: Generally capable agents for open-world environments via large language models with text-based knowledge and memory." arXiv preprint arXiv:2305.17144 (2023).

[5] Sumers, Theodore R., et al. "Cognitive architectures for language agents." arXiv preprint arXiv:2309.02427 (2023).

[6] Gou, Zhibin, et al. "Tora: A tool-integrated reasoning agent for mathematical problem solving." arXiv preprint arXiv:2309.17452 (2023).

[7] Zhou, Andy, et al. "Language agent tree search unifies reasoning acting and planning in language models." arXiv preprint arXiv:2310.04406 (2023).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces an LLM-based multi-agent reasoning system called SARA, which employs a novel prompting method known as structure-oriented analysis. This approach guides LLMs to explicitly identify key elements in the query, detect relationships between these elements, and break down the question into a series of sub-questions. The final answer is then generated based on the information gathered for each sub-question. This method enhances the base model's performance and can be applied in both zero-shot and few-shot settings.

### Strengths
The idea of preforming zero-shot prompting through structuring and decomposing the query seems sound.

### Weaknesses
- The PGM-based theoretical analysis of the proposed method does not align well with the primary focus of this paper, which is enhancing the zero-shot reasoning capability of LLMs. This section occupies a significant portion of the content (~3 pages) and is difficult to follow. While its stated motivation in line 178 is "to quantify the benefits of our structure-oriented analysis," I am unable to identify any findings or conclusions from this analysis that directly relate to the proposed method
- Experimental evaluation is insufficient and unfair.
  - The generalizability of the proposed method should be evaluated on a broader range of tasks and datasets, such as other datasets for commonsense reasoning (e.g., CSQA, StrategyQA, Date, SocialQA, etc.) and math reasoning (e.g., GSM8K, MATH, etc.). The current paper only evaluates the proposed method on three datasets, which is too limited.
  - Comparing SARA, which has access to external knowledge sources (such as Wikipedia and Google Search), with other prompting methods that rely solely on internal knowledge is unfair. The ablated version of SARA without the retrieval agent, i.e., SARA (no retrieval), should be a more appropriate method under the current comparison setup. From Figure 5 and Table 1, SARA (no retrieval) performs worse than ReAct (6-shot) and CoK (6-shot) on the HotPotQA dataset. Additionally, the paper does not report experimental results for SARA (no retrieval) on the MMLU-BIO and MMLU-PHY datasets, and several other datasets as mentioned before.

### Questions
Could you please elaborate on the findings or key insights presented in the PGM-based theoretical analysis section?

### Soundness
2

### Presentation
2

### Contribution
2
