# Online Preference Alignment for Language Models via Count-based Exploration

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Reinforcement Learning from Human Feedback (RLHF) has shown great potential in fine-tuning Large Language Models (LLMs) to align with human preferences. Existing methods perform preference alignment from a fixed dataset, which can be limited in data coverage and the resulting reward model is hard to generalize in out-of-distribution responses. Thus, online RLHF is more desirable to empower the LLM to explore outside the support of the initial dataset by iteratively collecting the prompt-response pairs. In this paper, we study the fundamental problem in online RLHF, i.e., how to explore for LLM. We give a theoretical motivation in linear reward assumption to show that an optimistic reward with an upper confidence bound (UCB) term leads to a provably efficient RLHF policy. Then, we reformulate our objective to direct preference optimization with an exploration term, where the UCB-term can be converted to a count-based exploration bonus. We further propose a practical algorithm, named Count-based Online Preference Optimization (COPO), which leverages a simple coin-flip counting module to estimate the pseudo-count of a prompt-response pair in previously collected data. COPO encourages LLMs to balance exploration and preference optimization in an iterative manner, which enlarges the exploration space and the entire data coverage of iterative LLM policies. We conduct online RLHF experiments on Zephyr and Llama-3 models. The results on instruction-following and standard academic benchmarks show that COPO significantly increases performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces the COPO algorithm for better exploration of online RLHF formulation. The authors provide a theoretical background of the proposed method and explain the practical implementation of it. To be specific, it assumes that the reward function could be expressed as a dot product between a parameter vector and a feature vector. Based on it, the model incorporates a USB term for exploration. Also, they employ a lightweight Config Flipping Network (CFN) to obtain pseudo-visit counts for the large state space of language generation. Experimental results show the efficacy of the proposed COPO algorithm. It performs better than the other exploration-aware online RLHF baseline, SELM, in several benchmarks. When they adjust the coefficient for the exploration term, it supports the importance of the exploration term in their experiments.

### Strengths
It tackles the important problem innate in RLHF-based alignment learning, i.e., exploration, with formal theoretical motivation and practical algorithm.

### Weaknesses
 * Their explanation and selection of baseline methods are not enough. Especially, I think other iterative/online methods should have been 
considered in addition to the SELM. There are many variants to implement online DPO. For example, [1], [2], and [3].

* The improvements seem marginal despite the complexity of the proposed method. The performance gaps among the baselines could be changed with different random seeds, especially for the LLM-as-a-Judge tasks.

* It would be good if more benefits of the exploration were suggested. For example, it might be more robust in some adversarial cases.

### Questions
* How do we measure/believe the CFN works properly? (before testing the model on the final benchmarks.)
  * (Declaimer) I do not have any idea about the original CFN work. However, the model (CFN module) seems too small to represent the hidden state of the modern LLM.
  * If we can improve the performance of the module, will the final alignment performances be also improved?

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
4

### Summary
This paper identifies a central problem in current online RLHF methods, that is, efficiently exploring the prompt-response space in each iteration. To address this, the paper designs a novel RLHF algorithm named Count-based Online Preference Optimization (COPO), which re-formulates the original DPO objective to balance space exploration and preference optimization. The authors adopt a simple coin-flip counting network approach to support COPO's pseudo-count, achieving promising experimental results.

### Strengths
1. Solid theoretical analysis. This work is built upon a solid theoretical foundation, starting from a relatively reasonable linear reward assumption and ultimately analyzing the regret upper bound of the optimization objective, providing a more credible motivation.

2. The authors demonstrate good insights into the existing problems in online RLHF, specifically the focus on preference optimization while lacking effective space exploration. Around this issue, they propose an algorithm suitable for LLMs with vast token sequence spaces.

3. The proposed COPO algorithm shows notable improvements after multiple iterations.

### Weaknesses
1. The proposed COPO algorithm is only implemented based on the DPO optimization objective, without verification of its adaptability to improve other online RLHF algorithms.

2. The visit count item in the COPO algorithm relies solely on a pseudo-count mechanism implemented by a coin flipping network (CFN) with accompanying random labels, which seems too simplistic. More convincing visit count algorithms need to be explored.

3. As mentioned by the authors in the experimental section, a better reward model could improve COPO's performance. However, this point wasn't explored in the experiments. In fact, the choice of different scoring RMs has a significant impact on the experiment and should be given more attention.

### Questions
1. What would be the experimental results if COPO's main ideas were applied to other online RLHF algorithms?

2. Are there other alternative or explorable counting algorithms?

3. How would choosing a stronger Reward model (or Judge model) affect algorithm performance, and can this be demonstrated with specific experimental results?

### Soundness
3

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
This paper introduces an online RLHF approach via the Count-based Online Preference Optimization (COPO) algorithm, which integrates count-based exploration and direct preference optimization to improve performance. Experiments on Zephyr and Llama-3 models demonstrate COPO’s effectiveness in boosting instruction-following capabilities and general academic benchmarks.

### Strengths
The paper rigorously establishes the theoretical underpinnings of COPO, providing a regret-bound analysis that demonstrates the efficiency of the UCB-based exploration strategy.

### Weaknesses
It seems there’s no notable improvement over SELM for the Llama-3-8B Instruct model in Table 1, especially when considering the potential variance from using GPT-4 as the evaluator. And can authors provide more baselines, for example comparison with Best-of-N and PPO?

### Questions
Please see the weakness.

### Soundness
2

### Presentation
2

### Contribution
2
