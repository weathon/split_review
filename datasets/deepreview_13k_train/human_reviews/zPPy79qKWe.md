# RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
Large language models (LLMs) deployed as agents solve user-specified tasks over multiple steps while keeping the required manual engagement to a minimum.
Crucially, such LLMs need to ground their generations in any feedback obtained to reliably achieve desired outcomes.
We propose an end-to-end reinforcement learning method for teaching models to leverage execution feedback in the realm of code synthesis, where state-of-the-art LLMs struggle to improve code iteratively compared to independent sampling.
We benchmark on competitive programming tasks, where we achieve new start-of-the art results with both small (8B parameters) and large (70B) models while reducing the amount of samples required by an order of magnitude.
Our analysis of inference-time behavior demonstrates that our method produces LLMs that effectively leverage automatic feedback over multiple steps.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel approach aimed at enhancing the performance of Large Language Models (LLMs) in multi-turn code generation tasks. The primary challenge addressed is the difficulty LLMs face in leveraging execution feedback for iterative code improvement, a crucial aspect of achieving reliable outcomes in multi-step code generation. The authors propose an end-to-end reinforcement learning method designed to teach LLMs to effectively use execution feedback. The paper makes three key contributions: (1) the development of a reinforcement learning framework that grounds LLMs in execution feedback, (2) demonstrated improvements in performance on code synthesis tasks, and (3) practical benefits including significant sample reduction and enhanced utilization of multi-step feedback.

### Strengths
- The method effectively incorporates self-correction and self-refinement techniques into the RLHF framework, leading to significant sample reduction.
- It demonstrates enhanced utilization of multi-step feedback, contributing to improved performance and efficiency in iterative code generation tasks.
- The approach addresses a critical limitation of current LLMs by successfully leveraging execution feedback, providing a practical and innovative solution for complex code synthesis problems.

### Weaknesses
1. The method's novelty is limited, as it mainly adapts self-correction and self-refinement techniques to the RLHF framework. Similar approaches have already been explored, such as Anthropic's work on iterative code correction[1] and DeepMind's adaptation of self-correction in RLHF for improved training and inference efficiency[2]. Additionally, the core idea of using compiler feedback as a reward signal for RLHF lacks sufficient comparative analysis with contemporary methods that integrate RLHF with compiler feedback, such as RLTF, Execution-based Code Generation using Deep Reinforcement Learning, CodeRL, StepCoder, and $\mathcal{B}$-Coder.
2. The experiments are limited to the CodeContest dataset, with a relatively small number of validation and test samples. The paper should validate its effectiveness on more datasets, such as APPS, which is commonly used for training in RLHF+compiler feedback research.
3. The paper claims that the multi-turn iterative approach of SFT performs significantly worse than RL (as mentioned in the appendix). However, self-improvement methods like critic+SFT have proven effective in code tasks. Providing the SFT and RL code as open-source could help validate this experimental conclusion.

### Questions
In the proposed method, when an incorrect solution is generated, the model immediately moves on to the next iteration. Could the authors explore the effect of incorporating feedback on the incorrect code before proceeding to the next iteration? How would this impact the experimental results?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces RLEF, a reinforcement learning framework that enhances code synthesis for large language models (LLMs) by utilizing execution feedback during training. RLEF allows models to iteratively refine code solutions based on execution feedback from test cases, significantly improving solve rates on competitive programming tasks and reducing sample requirements. The authors benchmark RLEF with Llama 3 models on CodeContests and demonstrate state-of-the-art performance, with generalizability to HumanEval+ and MBPP+ benchmarks.

### Strengths
1. The experimental results show general improvement when applying RLEF with Llama 3 series models on the CodeContests dataset, demonstrating the effectiveness of the proposed method.

2. The authors demonstrate that Llama 3.1 models trained on CodeContests with RLEF can generalize to other datasets like HumanEval+ and MBPP+, especially the 70B model. This generalization capability makes the proposed method more appealing and suggests broader potential applications.

3. The behavioral analysis post-RLEF training provides valuable insights into how the model learns to handle feedback differently. The detailed error analysis (e.g., fewer repetitions, more targeted edits, reduced reliance on random sampling) gives empirical weight to claims about the improved robustness of RLEF-trained models in multi-turn setup.

### Weaknesses
1. The scientific novelty of RLEF is somewhat limited. Although it extends previous work by introducing a multi-turn setup, the core concept of using unit test feedback as a reward signal has already been proposed in the literature, such as in RLTF [1], which uses unit test feedback within an online RL framework for code generation. The primary advancement in RLEF lies in iterating on this approach by incorporating execution feedback as input text across turns, making this more of an empirical extension than a conceptual breakthrough. 
To clarify the novel contributions, the authors could explicitly outline how RLEF builds upon and differs from RLTF and related works. Including a citation to RLTF would also better contextualize RLEF within the existing literature, helping to position its contributions more clearly.

2. While the experiments on CodeContests show the effectiveness of RLEF, high-quality unit tests like those provided in CodeContests are hard to obtain in practice or from other data sources. The authors didn't study how the quality of the unit tests (beyond just random feedback) would affect the effectiveness of RLEF. For example, if the public unit tests only cover simple input cases, the execution feedback might struggle to find bugs, imperfections, or inefficiencies in the code, thus providing less useful feedback. This limitation might hinder the application range of this method. 
It would strengthen the paper to include an analysis on RLEF's sensitivity to unit test quality. The authors could consider testing the method with varying qualities of unit tests, or provide a discussion on approaches to generate high-quality tests in real-world environments where comprehensive unit tests are scarce. Specific experiments that address this limitation would add valuable depth to the study.

3. The paper’s presentation, particularly in the Method section, needs improvement. (a) The organization is overly condensed, and crucial methodological details are packed into dense paragraphs, making it challenging for readers unfamiliar with PPO or RL for code generation. Key adjustments in the RL setup are mentioned briefly without adequate justification, making reproduction difficult and potentially deterring readers from fully engaging with the methodology. Expanding on crucial areas, particularly the PPO implementation details and any task-specific adjustments, could improve clarity. Breaking down dense sections into distinct, digestible subsections would also enhance readability. (b) Additionally, the primary results section compares models across different n@k metrics with varying n and k values, which may not be intuitive for readers unfamiliar with this metric. A more consistent comparison framework or additional explanation of these metrics would improve clarity.

### Questions
1. How robust is RLEF to feedback of varying quality beyond random feedback? For instance, how does the model perform if unit tests are incomplete or only cover trivial cases? How does the performance of RLEF change with different types or amounts of execution feedback? Is there an optimal amount or type of feedback for maximizing performance improvements?

2. The paper sets a fixed turn limit in the multi-turn setup. How does this choice affect model performance, and could RLEF benefit from a dynamic turn limit based on feedback content or problem complexity? How sensitive is the model to the number of feedback turns, particularly with respect to diminishing returns after a certain number of turns?

3. The paper mentions using a hybrid approach for value estimation (response-level) and policy optimization (token-level). Can you elaborate on why this approach works better than optimizing both at either the turn or token level?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors introduce a new approach for LLMs coding abilities that utilizes execution feedback from generated code through reinforcement learning to enhance performance in code synthesis tasks. The core insight is that LLMs can effectively follow user instructions while leveraging execution feedback to identify and correct errors in the generated code. The authors conceptualize the code generation process as an interactive task, proposing an environment where LLM-based agents generate code and receive real-time execution feedback. Their reinforcement learning-based method, termed RLEF, optimizes the performance of LLMs through this interactive framework. The results demonstrate that RLEF improves the correctness of the generated code compared to existing methodologies.

### Strengths
- This method is very intuitive, and modeling reinforcement learning as an interactive task is reasonable.
- The experimental results are good in training language models for coding.

### Weaknesses
 - Considering previous methods for training LLM coding and reasoning capabilities with reinforcement learning [1][2], the innovation is limited, as they also used some specially designed reward functions.
- There is no ablation on the reward function, which is important for the paper.
- There is a lack of experiments on more models to verify the generality of the method.
- It lacks some related work on training LLMs for reasoning and coding with reinforcement learning [1][2].

### Questions
See above weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a novel method to enhance LLM code synthesis through the use of execution feedback. In contrast to existing works that use unit test feedback as binary indicators or fractions of unit test pass rates to improve code generation, the feedback in this work is provided as language descriptions, including error messages and unit test results. Additionally, the proposed method is iterative, with the model trained to self-correct its previous responses based on received execution feedback. Experimental results indicate that this approach significantly improves LLM code synthesis capabilities.

### Strengths
1. The paper is well-written and clearly presented. I appreciate the clarity and organization in the presentation of the results.
2. The proposed method appears to be effective, substantially enhancing code generation performance.

### Weaknesses
 1. **Limited Practical Application:**
   While effective, the proposed method seems highly constrained in its practical application. The reliance on unit tests for feedback is a significant limitation, as generating accurate unit tests for arbitrary user prompts is often as challenging as solving the problems themselves. This confines the method to specific OJ style problems, where unit tests are readily available, and cannot be trivially extended to more general user scenarios where unit tests are not available.

2. **Advantage Computation:**
   The way how the authors compute the advantages seems to be weird. The authors claim the action space is defined on the token level, but the advantages for every token in the same turn is the same. In that sense, how does the critic be updated? Can the authors intuitively / empirically explain why they do this?

3. **Effectiveness of Multi-turn Feedback:**
   The empirical success of multi-turn feedback is intriguing. It is unclear whether the iterative nature of the algorithm or the unit tests' guidance contributes more to this success. An ablation study could clarify this by training RLEF iteratively while providing intermediate/final feedback with only numerical values, avoiding specific details on failed unit tests and expected outputs. For example, assigning smaller reward signals at the end of each turn and a larger signal at the end of the episode based on whether the generated code is correct or the fraction of unit tests passed could yield insights.

### Questions
N/A

### Soundness
3

### Presentation
4

### Contribution
3
