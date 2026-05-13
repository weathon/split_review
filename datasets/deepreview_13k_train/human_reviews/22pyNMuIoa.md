# PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization

- Decision: Accept
- Scores: 6, 8, 3, 6

## Abstract
Highly effective, task-specific prompts are often heavily engineered by experts to integrate detailed instructions and domain insights based on a deep understanding of both instincts of large language models (LLMs) and the intricacies of the target task. However, automating the generation of such expert-level prompts remains elusive. Existing prompt optimization methods tend to overlook the depth of domain knowledge and struggle to efficiently explore the vast space of expert-level prompts. Addressing this, we present {PromptAgent}, an optimization method that autonomously crafts prompts equivalent in quality to those handcrafted by experts. At its core, PromptAgent views prompt optimization as a strategic planning problem and employs a principled planning algorithm, rooted in Monte Carlo tree search, to strategically navigate the expert-level prompt space. Inspired by human-like trial-and-error exploration, PromptAgent induces precise expert-level insights and in-depth instructions by reflecting on model errors and generating constructive error feedback. Such a novel framework allows the agent to iteratively examine intermediate prompts (states), refine them based on error feedbacks (actions), simulate future rewards, and search for high-reward paths leading to expert prompts. We apply PromptAgent to 12 tasks spanning three practical domains: BIG-Bench Hard (BBH), as well as domain-specific and general NLP tasks, showing it significantly outperforms strong Chain-of-Thought and recent prompt optimization baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The manuscript proposed PromptAgent, a new method using a planning algorithm, i.e., Monte Carlo Tree Search, to navigate and discover high-quality prompts through a process resembling human-like trial-and-error, incorporating feedback from model errors and refining previous prompts based on feedback. This method has been tested across 12 tasks with promising performance compared to existing baselines such as CoT and APE with GPT-3.5. The optimized prompt can be generalized to different LLMs, including GPT-4 and PaLM2.

### Strengths
- The proposed PromptAgent leveraged a Monte Carlo Tree Search framework to utilize errors and feedback identified by LLMs for the iterative refinement of prompts. This approach is theoretically sound and can enhance navigation through the expansive search space of potential prompts.
- PromptAgent showed promising experimental results across 12 tasks, and the optimized prompt can be generalized to different LLMs.
- PromptAgent showed better performance and exploration efficiency than other prompt optimization methods, including Automatic Prompt Engineer (APE).

### Weaknesses
 - PromptAgent relies on a key hypothesis: the optimizer LLM (GPT-4 in this study) possesses adequate domain knowledge to identify the errors in the response from the base LLM and give meaningful feedback. However, this may not be a valid hypothesis, especially in some specialized areas such as medicine [1,2], where the data is relatively sparse due to strict data protection regularization like HIPAA. The reliance on the optimizer's domain knowledge is a significant limitation, as the quality of the optimized prompt is directly tied to the accuracy of the feedback, and the risk of propagating misinformation is high if the optimizer lacks sufficient expertise.
- In order to refine the prompt, PromptAgent needs to concatenate the "error_string", "error_summarization and "trajectory_prompts" as one input. Challenges may arise in tasks demanding the interpretation of extensive contexts, such as the analysis of detailed medical documents, where the "state_transit" could become prohibitively large due to the number of training examples and the depth of the Monte Carlo Tree Search, potentially diminishing the LLMs' performance. The concatenation of error information and past prompts could lead to an unwieldy input, particularly in tasks with long documents or complex reasoning chains, potentially exceeding the context window of the LLM and impacting performance.

### Questions
- If the optimizer LLM misidentifies an error or provides incorrect feedback, will this misinformation be propagated through the optimization process, leading to less effective prompts?
- This study used GPT-3.5 as the base model and a more capable model, such as GPT-4, as the optimizer LLM. Why not use GPT-4 for both base and optimizer LLM?
- The question above also extend to the implications of using fundamentally different LLMs, such as employing PaLM 2 as the base model against GPT-4 as the optimizer, and how this difference might affect the optimization outcome.
- In Fig 3(a), why GPT Agent, an "LLM-powered autonomous agent", was not compared in the exploration efficiency test?

### Soundness
2 fair

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
This paper proposes PromptAgent, which adopts a planning strategy based on MCTS for prompt engineering. Empirically, PromptAgent outperforms prior methods and human prompts. Overall the reviewer thinks the manuscript is well written and solid, and would like to recommend for acceptance.

### Strengths
1. This paper is well-written and easy to follow.
2. The method seems clean, straightforward, and promising.

### Weaknesses
There are several clarity issues in the experimental section regarding human prompts and reward functions. See questions below.

### Questions
1. At the end of Section 3.1, the manuscript says “PromptAgent straightforwardly defines a reward function $r_t=r(s_t,a_t)$ as the performance on a held-out set separated from the given training samples.” However, the reviewer cannot see how the reward functions are actually defined in the experimental sections (and the appendix). Is it possible that the author can provide a clear definition of how the reward function is defined (or provide an example of how the reward function is generated)?
2. In the paragraph “Baselines” of section 4.1, the descriptions of how Human Prompts are created are a bit vague. Although the authors have provided several examples of the human prompts in Appendix F, the reviewer would suggest the authors provide some extra details on how the human prompts are collected or generated.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces a prompting agent designed to perform few-shot prompting. The seeking of better-prompting policies is based on recursively generation and self-reflection (using a stronger general-purpose LLM). The idea is straightforward, the results show some improvement over single-round prompting methods.
The idea is interesting, but not technically novel, and the results are not insightful enough to add knowledge to the community (please see the weakness section below). I hereby would vote for a rejection.

### Strengths
The idea of this work is clear and easy to follow. The writing is in general clear. This idea can be useful from the engineering/ deployment side.

### Weaknesses
Technical contribution is limited.

Comparing the performance of an average user with LLM in prompting is somewhat unfair. Also, even human experts will be posited under an unfair setting where LLMs can do multiple-round prompting.

Some of the experiment settings are suspicious to be unfair (please see questions below)

### Questions
Can the authors please provide the depth setting used in the Greedy baseline? It is too-sample efficient but performs poorly in Figure 3.(a). I also wonder what would the optimization burden be for each task compared to a DFS search. The beam search baseline implemented in the main text seems to be the BFS search. I would expect DFS to outperform BFS as it can integrate more of the LLMs’ ability of reflection and reasoning.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a strategic prompt engineering method by utilizing Monte Carlo Tree Search where a base model collects errors from the training data set and an optimizer model provides feedback based on the collected errors to further optimize the prompt. Once a new prompt is composed, the hold-out set will be used to gauge its performance based on a given reward function. The method is evaluated on 12 curated tasks from three domains where results show its superior performance compared to a few alternative approaches including human curated prompt, Chain of Thoughts (CoT), and a couple of optimization methods including GPT agent and Automatic Prompt Engineering. Authors study the the effect of strategic planning aspect of their method through a set of ablation studies by considering various alternatives through single Monte Carlo Search, greedy, and Beam search where results show the benefit of considering exploitation vs. exploration trade offs in exploring the search space. Authors study prompt generalization and exploration efficiency as well.

### Strengths
- The paper is well written and easy to follow.
- Related literature is covered.
- Authors have conducted comprehensive experiments to evaluate the performance of their proposed method against a set of alternative methods and ablation studies shed further lights on the effectiveness of the proposed strategic exploration of the search space using MCTS.
- Appendix covers useful details about the hyper parameters and the evaluation data sets and details of the studied methods.

### Weaknesses
 - **Novelty** of the proposed method is arguable. Use of MCTS in prompt engineering is not novel. However, the way authors have incorporated a base and an optimizer model in their implementation and the prompts used to incorporate the error feedback into the existing state (+ the empirical studies) can be considered as the main contributions of this work.
- **Contribution**: Based on the details provided in the Appendix section, it can be seen that the amount of details covered in prompts generated by APE is not comparable with that of the proposed method. The prompts generated by the proposed method are significantly lengthier and cover more details compared which is hard to justify. APE supposedly uses Monte Carlo Search to iteratively propose and select prompts, therefore, it is expected to see more details getting added to the original prompt over each iteration which is not reflected in the samples that I see in the Appendix section. **This makes me conclude that the additional gain from the proposed method by authors come from the way they instruct the optimizer method to incorporate the feedback into the existing state rather than utilization of MCTS** which is the main claim of the paper.
However, 
- Clarity [minor]: It's ok that authors have covered the details of the selection, expansion, simulation, and back-propagation in MCTS and it can be very useful for general audience with less context, however, I was hoping to read more details about how authors have implemented the expansion stage. Appendexi briefly touches base under "Implementation details" sub-section and mentions "We sample 3 batches, and for each batch, we generate multiple new prompts". It would be good if authors can further explain how they generate new prompts for each batch.

### Questions
- Page 2: What does it mean when you say "bad at managing multiple errors"
- It's not clear how the authors have picked the hyper parameters including number of iterations and exploration vs. exploitation related parameter.

Minor:
p 1: prompting engineering => prompt engineering
P 3: without as less as => with as less as

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
