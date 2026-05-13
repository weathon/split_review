# CodeChain: Towards Modular Code Generation Through Chain of Self-revisions with Representative Sub-modules

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Large Language Models (LLMs) have already become quite proficient at solving simpler programming tasks like those in HumanEval or MBPP benchmarks. However, solving more complex and competitive programming tasks is still quite challenging for these models - possibly due to their tendency to generate solutions as monolithic code blocks instead of decomposing them into logical sub-tasks and sub-modules. %This lack of modularity is a common deficiency across all SoTA inference frameworks (self-refine, self-debug, reflexion, etc). 
On the other hand, experienced programmers instinctively write modularized code {with abstraction} for solving complex tasks, often reusing previously developed modules. To address this gap, we propose CodeChain, a novel \iffalse iterative \fi framework for inference that elicits modularized code generation through a chain of self-revisions, each being guided by some representative sub-modules generated in previous iterations. 
Concretely, CodeChain first instructs the LLM to generate modularized codes through chain-of-thought prompting. Then it applies a chain of self-revisions by iterating the two steps: 1) extracting and clustering the generated sub-modules and selecting the cluster representatives as the more generic and re-usable implementations, and 2) augmenting the original chain-of-thought prompt with these selected module-implementations %as hints 
and instructing the LLM to re-generate new modularized solutions. We find that by naturally encouraging the LLM to reuse the previously developed and verified sub-modules, CodeChain can significantly boost both modularity as well as correctness of the generated solutions, achieving relative pass@1 improvements of 35\% on APPS and 76\% on CodeContests. It is shown to be effective on both OpenAI LLMs as well as open-sourced LLMs like WizardCoder. We also conduct comprehensive ablation studies with different methods of prompting, number of clusters, model sizes, program qualities, etc.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes the CodeChain approach for code generation in LLM (Large Language Model) sub-modules, aiming to enhance the modularity and accuracy of the resulting code.

### Strengths
The paper is well-structured and presents its arguments in a clear fashion. 

The prompt method described is uncomplicated yet efficacious. 

The experimental evaluation encompasses both closed-source and open-source models, providing a comprehensive analysis.

### Weaknesses
It is unclear whether the method can improve the quality of code generation specifically for Codellama models.

The potential of CodeChain to bolster problem-solving capabilities in other domains, such as mathematics, is not established.

### Questions
See Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes CodeChain a method for prompting LLMs to generate modular code and reuse the generated submodules in subsequent iterations of prompting. The generated submodules are extracted and clustered to find representative and reusable components for iterations of self-revision. Experimental results on the APPS and CodeContests demonstrates that CodeChain significantly improves pass@1 metric when compared to several prior approaches.

### Strengths
* The CodeChain prompting technique proposed in the paper is intuitive and easy to utilize. Designing a prompting strategy for inducing and leverage modular functions seems novel. 
* The experimental results on the selected benchmarks show the effectiveness of the prompting strategy relative to several prior methods.
* Studies on the impact of different clustering strategies, embedding choices and revision sampling are informative.
* Overall CodeChain seems like a good prompting strategy which is simple and effective.

### Weaknesses
 * The clustering strategy seems to add only a small performance improvement to the overall approach. Randomly picking the modules also seems to do reasonably well (Table 3). One experiment that would be helpful is adding all submodules instead of randomly picking the generated modules to include in future revisions. Would this eliminate the need for clustering. 

* It is unclear how much the prompting strategy is sensitive to specific wording of the prompt and alternative formulations. Did the authors try multiple variants of the prompt and if so what was the variance and sensitivity of the results. Is it possible that there are prompts which could instruct the model to do revisions in a single shot? Could this improve direct generation? 

 * The evaluation largely relies on two benchmarks. It would be good to see the evaluation extend to some of the appropriate subsets in https://github.com/bigcode-project/bigcode-evaluation-harness

### Questions
* The authors observe that the training datasets do not filter for modularity. Have the authors tried filtering the training dataset for modular code and do light-weight fine-tuning with parameter efficient tuning methods?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a modular code generation approach for complex programming tasks. CodeChain extracts and clusters generated sub-modules, selects representative implementations and instructs the LLM to generate new solutions using these selected modules. Experimental results show that CodeChain significantly improves modularity and correctness, achieving relative pass@1 improvements of 35% on APPS and 76% on CodeContests. The framework works well with both OpenAI LLMs and open-sourced LLMs like WizardCoder. The paper also includes comprehensive ablation studies that provide insights into CodeChain's performance.

### Strengths
* SoTA performance on code generation benchmarks
* CodeChain works well across LLMs (GPT-3.5, GPT-4 and WizardCoder)
* The paper is well-written and is easy to understand.
* The authors provided extensive ablation.

### Weaknesses
 * Correctness/Soundness: 
(1) Programs generated by CodeChain are with high levels of modality and reusability on Likert scale judging by GPT-4 prompt. It is unclear how this evaluation align with human preference.
(2) The effectiveness of sub-module generation is unclear. 
(3) The analysis on the chain of self-revisions sees a slight performance drop in the 5th iteration, which hints at the limitation of self-revise prompting.

* Novelty/Originality: 
1. Using CoT to generate demonstrations and choosing representative demonstrations has been explored in [1]. The novelty of this work lies in employing this idea for code generation, which is incremental.
2. Missing citation: [2] explores a similar idea of decomposing source code into components. 
3. The idea of utilizing LLMs' ability to self-revise has been studied in [3,4] and more. 

* Writing could be improved: There are multiple references to an Appendix section (e.g., Appendix F) without clarifying which figure/prompt is being referred to.  

### Questions
In section 3.2, the author mentioned, "We append the instruction with a one-shot demonstration.", which part of the referenced figure (Figure 3) or the appendix (Appendix F) is the one-shot demonstration? How is this demonstration being constructed?



=== Post-rebuttal ====
Thanks for the detailed clarification and the additional evaluation. While I still have concerns regarding the novelty and the proper evaluation with GPT-4 (in terms of human evaluation), I think this paper is a good contribution to the community. I increased my score.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new inference framework for modularised code generation using a large language model. Existing LLM tends to generate monolithic code blocks while a complex coding task usually needs to be broken down into multiple sub-tasks with each addressed by a sub-module. Motivated by the modular programming discipline, this paper proposes to iteratively ask LLM to generate code solutions with sub-modules and add the potentially valid sub-modules to the prompts for LLM’s generation at the next round. The sub-module selection is conducted by test case filtering and clustering.  The proposed framework yielded nontrivial improvements over the direct generation baselines.

### Strengths
In general, this paper follows the self-revision practice to improve the quality of code generated by LLM in a trial-and-error manner. However, instead of solely focusing on the functional correctness of the code, this paper raises the concern about LLM’s ability to decompose a complex coding task into multiple sub-tasks so as to generate reliable and reusable sub-modules. Although both task decomposition and chain-of-thoughts have been widely studied in different NLP applications, they are delicately adapted to fit the modular programming discipline in order to benefit code generation. Empowering LLM to produce modular code is not only helpful in improving the code’s reliability but also important for reducing the cost of subsequent manual maintenance. So this work’s originality and significance are considerable to me.

### Weaknesses
+ Sub-module filtering by public tests: given that the objects to be filtered are sub-modules generated by LLMs but we actually have no idea how the LLMs will decompose the target task/module into what sub-tasks/sub-modules. Then how can we compose the tests for the unknown sub-modules?

+ Four schemes for deciding the number of clusters are investigated. However, different tasks are of different complexity and it is difficult to decompose them into a fixed number of sub-tasks. Then is it possible that LLMs may generate some sub-modules which are never used in the task-level solution? If yes, then what are the effects of those sub-modules?

+ Kmeans are selected for clustering by why? Will density-based clustering like DBSCAN work better given it doesn’t need to specify the number of clusters as a prior?

+ As shown in Figure 5 and Figure 7, I failed to observe a consistent pattern to help me decide the optimal round of self-revision for CodeChain. The authors explained that the performance degradation at the 5th round is because of overfitting to the public test sets but this claim lacks support.

+ The title of the y-axis is missing in charts like Figures, 6, 7

### Questions
In table 2, why is the result of GPT4 (All: 34.75) is even bettrer than Self-repair+GPT4 with GPT4 as the feedback source (33.30)?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
