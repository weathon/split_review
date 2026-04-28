# Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
While language models (LMs) have shown potential across a range of decision-making tasks, their reliance on simple acting processes limits their broad deployment as autonomous agents. In this paper, we introduce Language Agent Tree Search (LATS) -- \emph{the first general} framework that \emph{synergizes} the capabilities of LMs in reasoning, acting, and planning. By leveraging the in-context learning ability of LMs, we integrate Monte Carlo Tree Search into LATS to enable LMs as agents, along with LM-powered value functions and self-reflections for proficient exploration and enhanced decision-making. A key feature of our approach is the incorporation of an environment for external feedback, which offers a more deliberate and adaptive problem-solving mechanism that surpasses the constraints of existing techniques. Our experimental evaluation across diverse domains, including programming, interactive question-answering (QA), web navigation, and math, validates the effectiveness and generality of LATS in decision-making while maintaining competitive or improved reasoning performance. Notably, LATS achieves state-of-the-art pass@1 accuracy (92.7\%) for programming on HumanEval with GPT-4 and demonstrates gradient-free performance (average score of 75.9) comparable to gradient-based fine-tuning for web navigation on WebShop with GPT-3.5.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new framework called Language Agent Tree Search (LATS) to improve the reasoning and decision-making abilities of large language models (LLMs). Specifically, LATS is a framework that incorporates self-reflection and tree-of-thoughts into LLM-based agent problems. Evaluations across diverse tasks like programming, HotPotQA, and WebShop show LATS effectively harnesses LLM capabilities for reasoning and decision-making.

### Strengths
1. The writing is overall clear and easy to follow.
2. The author provides sufficient technical details to understand the LATS framework and reproduce results.
3. The authors evaluate LATS extensively across diverse tasks like programming, HotPotQA, and webshop to demonstrate generality and superiority.

### Weaknesses
1. The idea is overall not that novel considering previous work like RAP and Reflextion.

2.  As far as I can see, LATS definitely has much more token consumption compared with other baselines when sampling the same amount of trajectories. I think the author should try to increase the token consumption used in other baselines. For example, report the overall token consumption and try to increase the K set in CoT-SC so it may consume tokens on a similar scale to LATS.

3. The author should try to at least incorporate one baseline with the external environment feedback as the ablation study. 

4. The author could provide more ablation studies to analyze the impact of different components, for example, search depth, exploration factor etc..

4. The limitation of LATS is not fully addressed. For example, it seems the current version LATS cannot scale to large-scale problems.

### Questions
1. Since the author utilizes LLM itself as the evaluation metric, how do you think of recent works that indicate LLM may not be good at self-critique, for example, Huang et al. 2023 mention that in the experiment of reflection (section 3.1.3 in Huang's paper), they use the correct answer as the criteria to stop the self-correction loop, which is not fair as I think. How do you handle this question during the evaluation of value function in LATS?

2. I understand that LATS leverages the final environment feedback to guide the MCTS search (especially in the backward process). The final result of programming and Webshop is accessible (since you have the simulator), but how can you get the feedback on HotpotQA? Will the HotpotQA environment tell you whether your answer is right or not? If so, it means that you are using a ground-truth answer during the MCTS search process which is completely not reasonable (tbh, this is also related to the phenomenon of using the correct answer as the criteria in my question 1). Could the author elaborate more on what the environment feedback looks like in the HotpotQA environment?

Reference
Huang, Jie, et al. "Large language models cannot self-correct reasoning yet." arXiv preprint arXiv:2310.01798 (2023).

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a MCTS framework which uses LLM as the basic functioning component to perform sequential decision-making tasks. 
It achieves strong performance across multiple important benchmarks.

### Strengths
The proposed framework is intuitive and easy-to-understand. 
It combines modern LLM with classical MCTS algorithm, which is a neat idea. 

The empirical results are strong.

### Weaknesses
There are some key weaknesses that prevent me from giving an acceptance score. 

First, some key technical designs of the proposed framework are not well motivated and seem to be problematic. 

E.g., the Abstract says that this method is inspired by model-based RL but the proposed method is model-free. The authors argue that "we can conveniently backup to any state by setting the input..." but, without an environment model, one needs to actually interact with the environment to roll out future steps in order to compute values for possible actions at an earlier step; see Fig-2 and 3. How is that possible in a real application that you could go back up to an earlier step after execution? More importantly, in deployment/inference, using future states of actual interactions does not seem to be a fair comparison with other model-free approaches such as ReAct which doesn't roll out, because it is like an undo move, right? 

Second, presentation has major issues. It is easy-to-follow, which is good, but it leaves out much important information so I find it hard to gauge its overall soundness. 

E.g., the LATS section is confusing even to a reader familiar with both LLM and MCTS. This section needs a high-level review about MCTS and how it is reshaped with LLM for this framework. Important technical details need to be added: e.g., I didn't find any math formula about backpropagation even after checking within appendices and algorithm boxes.

### Questions
Why model-free and why you can still take a previous action after actual roll-out?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Language Agent Tree Search (LATS), which hierarchically expands the reasoning path and employs Monte-Calro Tree Search (MCTS) to find the correct reasoning path. Also, to deal with decision making problems, Reflexion mechanism (reflecting past failure episodes and leveraging it in the future rollout) is incorporated. LATS empirically achieves the strong performance in HotpotQA, HumanEval, MBPP, and WebShop, as done in original Reflexion paper.

### Strengths
### quality and clarity
- This paper is well-written and easy to follow.

### significance
- The empirical results are strong. 94.4 Pass@1 in HumanEval would be notable results.

### Weaknesses
- LATS seems to be the naive combination of existing methods, MTCS from RAP [1] (or ToT [2]) and Reflexion [3], to leverage past (failure) experience. I cannot find a clear difference among those. The originality and significance could be limited from this perspective. 
- Evaluation is biased to decision making (HotPotQA \& WebShop). Some reasoning benchmark should be included, such as Game 24, Crossword as done in ToT [2] or GSM8K in RAP [1] to clarify the difference between LATS and ToT/RAP.
- Related to Table 1, I think ToT [2] also incorporates self-refinement process.
- The results of ReAct in Table 5 (WebShop) are lower than the one reported in original paper (Score: 66.6 / SR: 40.0).
- In WebShop, WebGUM [4], a finetuned language model agent, achieves the best performance in SR (Score: 67.5 / SR: 45.0).
- The intention in Figure 4 is ambiguous. Is this a conceptual description of Tree Search?

[1] https://arxiv.org/abs/2305.14992

[2] https://arxiv.org/abs/2305.10601

[3] https://arxiv.org/abs/2303.11366

[4] https://arxiv.org/abs/2305.11854

(Minor Issue)
- In Section 4.2, the definition of $M$ in UCT algorithm is missing.

### Questions
- RAP applies at most 20 reasoning iterations for MCTS. This is smaller than LATS (50 iters). Is there any reason for this?
- What is the difference between decision-making and planning in Table 1? I guess both are the same concept.
- What "Memory" means in Table 1?
- How did you measure each metric? Reporting aggregated best among $k=50$ reasoning iterations for MCTS (I guess "best of k" in Table 2)? or reporting the result after $k=50$ reasoning iterations for MCTS? I'm curious about its "learning curve".
- In Table 2 (right), what "CoT+ReAct" means?  In my understanding, ReAct is "CoT" in decision making problem. Also, are there LATS (w/ CoT) in Table 2 (left)?
- On WebShop, it is reported that Reflexion cannot improve the performance as done in ALFWorld. Could you explain what could be the source of improvement of LATS (because LATS employs Reflexion process, too)?

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes LATS, a general framework that unifies the capabilities of LLMs in planning, acting, and reasoning by deliberately constructing trajectories with MCTS and incorporating external feedback. The experiments demonstrate the superiority of LATS by achieving new sota on HumanEval and HotPotQA.

### Strengths
- The paper proposes a general framework unifying the capabilities of LLMs in planning, acting, and reasoning

- The paper is well-written and presented clearly.

- The results look promising, achieving new sota on HumanEval and HotPotQA

- The ablation provides some insights into the importance of various strategies when harnessing the power of LLMs.

### Weaknesses
- LATS uses a higher computational cost to achieve a better performance, it would be better to add some table or figure explicitly discussing about the tradeoff here.

- It would be clearer to add the exact number of API calls and tokens used etc. for each baseline in the results table since the inference time is not directly comparable to other methods.

- Not much novelty compared to existing LLM prompting techniques.

- It would be interesting to see how LATS performs in real complex planning environments, such as ALFWorld and Minecraft.

### Questions
Please address the concerns raised in the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
