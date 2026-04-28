# FLARE: Faithful Logic-Aided Reasoning and Exploration

- Decision: Reject
- Avg Score: 5.75
- Scores: 3, 6, 6, 8

## Abstract
Modern Question Answering (QA) and Reasoning approaches based on Large Language Models (LLMs) commonly use prompting techniques, such as Chain-of-Thought (CoT), assuming the resulting generation will have a more granular exploration and reasoning over the question space and scope.
However, such methods struggle with generating outputs that are faithful to the intermediate chain of reasoning produced by the model.
On the other end of the spectrum, neuro-symbolic methods such as Faithful CoT (F-CoT) propose to combine LLMs with external symbolic solvers.
While such approaches boast a high degree of faithfulness, they usually require a model trained for code generation and struggle with tasks that are ambiguous or hard to formalise strictly. We introduce \textbf{F}aithful \textbf{L}ogic-\textbf{A}ided \textbf{R}easoning and \textbf{E}xploration (\textbf{\ours}), a novel interpretable approach for traversing the problem space using %exact 
task decompositions. We use the LLM to plan a solution, soft-formalise the query into facts and predicates using a logic programming code and simulate that code execution using an exhaustive multi-hop search over the defined space.
Our method allows us to compute the faithfulness of the reasoning process w.r.t. the generated code and analyse the steps of the multi-hop search without relying on external solvers.  Our methods achieve SOTA results on $\mathbf{7}$ out of $\mathbf{9}$ diverse reasoning benchmarks.
We also show that model faithfulness positively correlates with overall performance and further demonstrate that {\textbf{\ours}} allows pinpointing the decisive factors sufficient for and leading to the correct answer with optimal reasoning during the multi-hop search.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Faithful Logic-Aided Reasoning and Exploration (FLARE) to enhance the interpretability and faithfulness for LLM-based reasoning. FLARE uses task decomposition and logic programming to guide LLMs. It combines planning with logical reasoning, where the query is formulated into structured facts and predicates, and then explored through an exhaustive multi-hop search within a defined problem space. At the end, there are some reasoning inconsistencies detection and faithfulness measurement.

### Strengths
Improving LLM-based reasoning with neuro-symbolic integration is a good research problem. Empirical results are given.

### Weaknesses
## Review

### summary:
 This paper introduces Faithful Logic-Aided Reasoning and Exploration (FLARE) to enhance the interpretability and faithfulness for LLM-based reasoning. FLARE uses task decomposition and logic programming to guide LLMs. It combines planning with logical reasoning, where the query is formulated into structured facts and predicates, and then explored through an exhaustive multi-hop search within a defined problem space. At the end, there are some reasoning inconsistencies detection and faithfulness measurement.

### soundness:
 2

### presentation:
 2

### contribution:
 2

### strengths:
 Improving LLM-based reasoning with neuro-symbolic integration is a good research problem. Empirical results are given.

### weaknesses:
 The writing could benefit from adjustments to improve clarity, strengthen notation, and correct typos. The advantages of using LLMs to simulate Prolog execution are ambiguous. Some key design and implementation details are missing. Code and data are not provided for reproducibility.

### questions:
 1) It would be helpful to include the notations for equations (Eq. (1)-(4)) and explanations for figures (e.g., Figure 1) to enhance readability and logical flow. Additionally, there are a few specific points that may benefit from clarification. For example, $T$ as a single token in query $Q$ is misused in Eq. (1)-(4). In Eq. (4), there might be a redundant comma or a missing variable.

2) In Section 3.1, the Simulating Search section might benefit from additional details. Specifically, elaborating on how a problem space traversal trace is formed would be valuable. Including a detailed description, pseudocode, or examples could provide further clarity. It would also be helpful to include a detailed explanation of the backtracking mechanism.

3) The complete process could be further clarified by explaining the steps following inconsistency detection and faithfulness measurement. For example, it would be valuable to know if a best-of-n selection, weighted voting or other strategies are used to decide the final answer. A pseudocode of the entire framework could also enhance understanding here. In addition, it's better to include some full examples for inconsistency detection and faithfulness measurement.

4) The framework may benefit from adaptive capabilities. Currently, the plan generation is done in one pass without a feedback loop. Introducing a mechanism to refine the generated code if errors are detected during subsequent simulation could also improve adaptability.

5) For simulating Prolog execution, the choice to use LLMs over an external solver might benefit from further clarification. Understanding the reasoning behind using an LLM-based simulation instead of an external solver, particularly in terms of handling the self-bias of LLMs, would be insightful.

6) Since Prolog is tailored for rule-based logical reasoning, the specific adaptations for solving math word problems need to be clarified. Further implementation details and example outputs could illustrate the achieved improvements and highlight the framework's effectiveness.

7) It would be valuable to expand the evaluation to include other general methods, such as Tree of Thought, Program of Thought, and Self-Consistency, alongside comparisons to similar methods [1-3]. Additionally, for Llama-3.1-8B, CmDR, and CMDR+, the F-CoT results are zero. Could the authors provide more context on this outcome?

8) Code and data are not provided for reproducibility.

Reference:

[1] Pan, Liangming, et al. "Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning." The 2023 Conference on Empirical Methods in Natural Language Processing.

[2] Yang, Sen, et al. "Neuro-symbolic integration brings causal and reliable reasoning proofs." arXiv preprint arXiv:2311.09802 (2023).

[3] Xu, Fangzhi, et al. "Symbol-LLM: Towards foundational symbol-centric interface for large language models." arXiv preprint arXiv:2311.09278 (2023).

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 3

### confidence:
 4

### code_of_conduct:
 Yes

### role:
 Review

### Questions
1) It would be helpful to include the notations for equations (Eq. (1)-(4)) and explanations for figures (e.g., Figure 1) to enhance readability and logical flow. Additionally, there are a few specific points that may benefit from clarification. For example, $T$ as a single token in query $Q$ is misused in Eq. (1)-(4). In Eq. (4), there might be a redundant comma or a missing variable.

2) In Section 3.1, the Simulating Search section might benefit from additional details. Specifically, elaborating on how a problem space traversal trace is formed would be valuable. Including a detailed description, pseudocode, or examples could provide further clarity. It would also be helpful to include a detailed explanation of the backtracking mechanism.

3) The complete process could be further clarified by explaining the steps following inconsistency detection and faithfulness measurement. For example, it would be valuable to know if a best-of-n selection, weighted voting or other strategies are used to decide the final answer. A pseudocode of the entire framework could also enhance understanding here. In addition, it's better to include some full examples for inconsistency detection and faithfulness measurement.

4) The framework may benefit from adaptive capabilities. Currently, the plan generation is done in one pass without a feedback loop. Introducing a mechanism to refine the generated code if errors are detected during subsequent simulation could also improve adaptability.

5) For simulating Prolog execution, the choice to use LLMs over an external solver might benefit from further clarification. Understanding the reasoning behind using an LLM-based simulation instead of an external solver, particularly in terms of handling the self-bias of LLMs, would be insightful.

6) Since Prolog is tailored for rule-based logical reasoning, the specific adaptations for solving math word problems need to be clarified. Further implementation details and example outputs could illustrate the achieved improvements and highlight the framework's effectiveness.

7) It would be valuable to expand the evaluation to include other general methods, such as Tree of Thought, Program of Thought, and Self-Consistency, alongside comparisons to similar methods [1-3]. Additionally, for Llama-3.1-8B, CmDR, and CMDR+, the F-CoT results are zero. Could the authors provide more context on this outcome?

8) Code and data are not provided for reproducibility.

Reference:

[1] Pan, Liangming, et al. "Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning." The 2023 Conference on Empirical Methods in Natural Language Processing.

[2] Yang, Sen, et al. "Neuro-symbolic integration brings causal and reliable reasoning proofs." arXiv preprint arXiv:2311.09802 (2023).

[3] Xu, Fangzhi, et al. "Symbol-LLM: Towards foundational symbol-centric interface for large language models." arXiv preprint arXiv:2311.09278 (2023).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents a reasoning framework capable of answering fuzzy and multi-hop questions while ensuring transparency in its reasoning steps. The framework achieves this through three key phases: task decomposition, soft formalization, and simulated search. In the first phase, the LLM is prompted to analyze the question and generate a structured plan for subsequent formalization. Following this, the LLM translates the question into ProLog programs according to the provided plan, called "soft formalization." Finally, the framework searches for answers by simulating a depth-first search over the problem space, essentially emulating Prolog execution within the LLM. This structured pipeline allows the framework to detect inconsistencies in reasoning by examining the facts and relationships used during inference. Additionally, it assesses the faithfulness of the reasoning process by comparing the actual execution paths to simulated paths generated by the LLM. Their methods achieved SOTA performance on 7 out of 9 common reasoning benchmarks.

### Strengths
1. The authors address limitations in current methods, which either struggle to maintain faithful, consistent reasoning steps or fail to handle fuzzy reasoning for difficult-to-formalize problems. They tackle these issues with a soft-formalization approach and a simulated search mechanism.
2. Unlike F-CoT, their approach doesn’t require programming expertise or additional fine-tuning for the LLMs. The LLMs aren’t required to generate perfectly accurate code but instead simulate Prolog execution internally, bypassing the need for an external interpreter.
3. The use of Prolog encourages the LLM to explicitly outline facts and relations in its reasoning, enhancing control and enabling verification of correct fact and relation usage, which helps reduce hallucinations.
4. Prolog’s DFS feature ensures thorough exploration of the problem space, increasing the likelihood of finding the correct answer.
5. The experiments are well-designed and thorough, demonstrating the method’s effectiveness with results that surpass or match those of CoT and F-CoT. The ablation study results for simulated search align well with expectations.
6. The correlation between faithfulness and reasoning performance is effectively highlighted through experimental results, supporting the model’s interpretability and reliability.

### Weaknesses
1. The paper would benefit from more detailed examples to illustrate how the simulated search operates and how it benefits intermediate reasoning steps.
2. There is no theoretical analysis of search complexit. If complexity analysis isn’t feasible for certain fuzzy problems, a time cost comparison between FLARE and baseline methods (e.g., CoT and F-CoT) would be a useful alternative.

### Questions
1. Considering that DFS can become computationally intensive as search depth increases, and that appending search traces to prompts may risk exceeding the LLMs' context length, how do you manage the generated Prolog program to avoid an unacceptable search space?
2. Would it be possible to set a faithfulness threshold and continue the simulated search only until this threshold is met (i.e., early stopping)? Testing this approach could make the way to faithfulness calculation more convincing.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new method named FLARE for logic-aided reasoning of LLMs using a semi-formal language that is not necessarily executable to allow flexibility. The model is given a problem and proceeds in 3 steps:

1. Generate a natural language plan given few-show examples. 
2. Model is prompted to generate a Prolog code given few-shot examples. In this step, the problem is decomposed into set of facts $F$, relations $R$, and a goal $G$.
3. The model is prompted to $\textbf{simulate}$ the execution of the code generated in stage 2 via prompting. This simulation is later used to detect reasoning inconsistencies and measuring faithfulness (to the intermediate reasoning steps) of the model. 

There are 2 failure modes in reasoning inconsistencies. First is when a fact or a relation that was not in the Prolog code from step 2 is used in step 3. Second is when a fact or a relation in the code is $\textbf{not}$ used in the reasoning steps, which authors classify as "sub-optimal reasoning."

Authors demonstrate that such prompting with language models such as CmDR and GPT-3.5 results in stronger accuracies on various Q&A and mathematical reasoning benchmarks. The paper has extensive evaluation demonstrating that simulating search and writing code is actually necessary for the performance increase and faithfulness of the generated text/code correlates with the accuracy of the results.

### Strengths
- The prompting technique proposed in the paper is very interesting for tasks that are hard to fully formalize yet it can benefit from a semi-formalized approach for logical reasoning. 
- The framework seems to reliably improve accuracy on multi-hop QA and MathWord tasks and it is relatively easy to adapt to new problems with just writing few shot examples.
-  The faithfulness metric proposed by the paper seems to correlate well with accuracy which can be used to "weigh" after multiple samples from the model to get more reliable results. This metric also provides a proxy for how reliable the answer is in a very simple way. 
- The paper is very well written and easy to read.

### Weaknesses
 - Although the method seems powerful for QA tasks, its adaptability to harder algorithmic and reasoning tasks seem difficult.
- The authors run experiments with GPT3.5 rather than GPT4o or GPT4o-mini which makes applicability to SoTA models questionable.
- Although the framework increases performance, it does not have the benefits a fully formal system that has guarantees. However, I believe this is okay as they target problems for which it's difficult if not impossible to have guarantees.


### Questions
- Could FLARE’s framework extend to other tasks that require complex reasoning? Insights on its limitations in such settings would be helpful.
- The method seems to work more reliably on LLaMa 8b and CmDR rather than on GPT3.5. Is there a reason why? 
- The framework seems to fail on sports and date Q&A - some insight into why that happens would be useful. 
- Is it true that if the model outputs a Prolog code that is not executable (or wrong syntax), it's not possible do any error detection or faithfulness measure? 
- Can you please summarize the 'characteristic' of problems for which the method is applicable and for which kind of problems it is not applicable?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Authors introduce a new logic aided interpretable formalization search propmting mechanism namely FLARE, where given a query a plan is generated by the LLM following which a logical prolog code is generated given the plan which is simulated with multihop search.

### Strengths
1) The paper is generally is well written with crisply defined mathematical notations and easy to follow presentation of authors works
2) Experimentation section of the paper is sound demonstrating the effectiveness of the proposed method

### Weaknesses
1) Expensive: Given that the LLMs have been used for planning, code generation and the execution of code via multi-hop search, instead of relying on symbolic solvers, this might increase the cost for computation. Specifically, the computational overhead of generating plans, code, and execution traces through multi-hop search, all within the LLM, is a concern. The paper needs to provide a more detailed analysis of the computational cost compared to methods that leverage external symbolic solvers, including a breakdown of the time and resources used for each stage of the proposed method.
2) Weak baselines: Experiments have been performed with relatively simpler datasets. Authors should experiment with more complex datasets that are already present in the literature for question answering such as LogiQA [1], PrOntoQA [2],  ProofWriter [3]. The current evaluation lacks a rigorous comparison with state-of-the-art methods on challenging logical reasoning benchmarks. The paper should demonstrate the method's performance on datasets that require deeper logical inference and have established benchmarks, such as those used in the Logic-LM paper, to properly assess its capabilities.
3) Figures: Figure 1 present in the paper is too cluttered and hard to read. Please break it down so that it is easy to read or please add a more detailed explanation in the appendix. The current figure does not clearly illustrate the different components of the proposed method and their interactions. A clearer visualization, possibly with separate figures for each stage, is needed to improve understanding. Alternatively, a more detailed explanation of the figure in the appendix would be beneficial.
4) Prompt Templates: Ideally since the proposed method is a prompting method, prompt templates are necessary to evaluate the performance of the proposed method in detail but Appending A2 does not include and since there is no supplementary material provided with paper, it is hard to effectively judge the paper in total. The absence of detailed prompt templates makes it difficult to reproduce the results and assess the sensitivity of the method to different prompt designs. The paper should include the exact prompts used for each stage of the method, either in the appendix or supplementary material, to ensure transparency and reproducibility.

### Questions
1) How cost effective is the proposed method over baselines methods since a lot of search is needed?
2) How effective is the proposed method over the methods like LLM + external symbolic solver such as LogicLM [1] ?
3) As mentioned in the cons section, can you please show the effectiveness of proposed method on more complex logical reasoning datasets?

[1] Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning

### Soundness
3

### Presentation
3

### Contribution
3
