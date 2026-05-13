# Value-Incentivized Preference Optimization: A Unified Approach to Online and Offline RLHF

- Decision: Accept
- Scores: 5, 5, 6, 6

## Abstract
Reinforcement learning from human feedback (RLHF) has demonstrated great promise in aligning large language models (LLMs) with human preference. Depending on the availability of preference data, both online and offline RLHF are active areas of investigation. A key bottleneck is understanding how to incorporate uncertainty estimation in the reward function learned from the preference data for RLHF, regardless of how the preference data is collected. While the principles of optimism or pessimism under uncertainty are well-established in standard reinforcement learning (RL), a practically-implementable and theoretically-grounded form amenable to large language models is not yet available, as standard techniques for constructing confidence intervals become  intractable under arbitrary policy parameterizations. 

In this paper, we introduce a unified approach to online and offline RLHF --- value-incentivized preference optimization (\algabb) --- which regularizes the maximum-likelihood estimate of the reward function with the corresponding value function, modulated by a {\em sign} to indicate whether the optimism or pessimism is chosen. \algabb also directly optimizes the policy with implicit reward modeling, and therefore shares a simpler RLHF pipeline similar to direct preference optimization. Theoretical guarantees of \algabb are provided for both online and offline settings, matching the rates of their standard RL counterparts. Moreover, experiments on text summarization and dialog verify the practicality
and effectiveness of \algabb.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes VPO which can either optimistically or pessimistically compute the reward function so that it can be used for both online and offline settings. Interestingly, ignoring the prompt-dependent baseline reward value due to the BT model, there is a computationally efficient algorithm to compute the resulting policy. In fact the formulation results in adding a KL regularization to DPO.
The paper proved a regret bound for online setting and a PAC bound for offline setting.
The experimental results have several evidence to claim that VPO outperforms DPO.

### Strengths
The paper gives a new view of online/offline learning for RL research.

- Solving online and offline learning problems using the same algorithm with (theoretically) just an adjustment of one hyperparameter is very interesting.
- The method is simple and easy to implement.
- The assumption and the optimization criteria of the method is clearly stated so that what the method intended to optimize is clearly stated in the paper, which makes the understanding of the algorithm much better. It is connected to the body of RL research.
- The analytical results are nice to have, yet its practical implication is difficult to verify in experiments.

### Weaknesses
The impact of the paper to the field of natural language processing and large language model is not clear to me.

- In terms of practical benefit to the LLM development, the experimental results are not decisive to conclude that VPO is better than DPO. I believe that the number of runs is not reported. The standard deviation/error is also not reported (sorry if I missed it).
- From what I understand, ARC-challenge is not a benchmark for alignment. It is a multiple-question answering task just to evaluate the knowledge of the LLM. It is difficult to judge if VPO has an advantage over IPO/DPO for online learning settings given that aside from the format, ARC is mostly just a collection of discrete knowledge that shares little among each instance. I would like to take a look at the generation examples. Or, I would guess using the standard benchmarks for alignment algorithms like AlpacaFarm or HH-RLHF makes more sense.


----------------------------------
I believe my concern was clearly stated in my very first reviewer comment as above.

Why ARC.

The authors decided not to answer this question. So, there is no reason for me to consider improving my score.
They decided to separate my questions into multiple discrete questions so that it looked like I was just randomly asking for generation examples.

> > (Q2) I'm curious about why ARC-Challenge is chosen as the task for the offline learning task. ARC is a collection of questions evaluating the knowledge of the LLM. It is mostly used to evaluate the non-instruction tuned pretrained LLMs but not the result of the alignment process. Isn't the *POs just learning the format of the multiple question answering format?
>
> We would like to remark that Arc-challenge has been widely used in previous RLHF works including DPOP[1], and Iterative RPO [2]. We follow the protocol in [2], and side-by-side comparison to offline DPO and IPO demonstrates that pessimism is necessary.
>
> > I would like to take a look at the generation examples. Or, I would guess using the standard benchmarks for alignment algorithms like AlpacaFarm or HH-RLHF makes more sense.


I had to write multiple responses until the authors finally showed the result of the ARC at the last second of the discussion period.
I am confident that my question was clearly stated in my first official review and also stated repeatedly, so I believe it is not unfair to point out the following concern.

> {"inputs": {"inputs_pretokenized": "What is the choice to the following Question? Only provide the choice by providing a single letter.\n\nQuestion: Which of the following would you most likely use to study the growth of an insect over time? Choices: (A)a clock that measures seconds (B)a hand lens with a large lens (C)several insects that feed on other insects (D)a glass aquarium with food for the insect\n\nThe answer is:", "targets_pretokenized": "(D)a glass aquarium with food for the insect"}, "prediction": "(C) several insects that feed on other insects"}
>
> {"inputs": {"inputs_pretokenized": "What is the choice to the following Question? Only provide the choice by providing a single letter.\n\nQuestion: A pharmaceutical company published experimental data showing that a new medication improved cholesterol levels in the people who participated in the study. Which professional most likely did not contribute to developing this medication? Choices: (A)a chemist (B)a biologist (C)a geologist (D)a physician\n\nThe answer is:", "targets_pretokenized": "(C)a geologist"}, "prediction": "(B) a biologist"}
>
> {"inputs": {"inputs_pretokenized": "What is the choice to the following Question? Only provide the choice by providing a single letter.\n\nQuestion: Monica grows vegetable plants in her garden. The plants have holes in their leaves and look unhealthy. Which task should Monica do first to solve this problem? Choices: (A)Add fertilizer to the soil. (B)Water the garden more often. (C)Plant different vegetables in the garden. (D)Observe the plants to identify the source of the damage.\n\nThe answer is:", "targets_pretokenized": "(D)Observe the plants to identify the source of the damage."}, "prediction": "(C) Plant different vegetables in the garden."}
>
> {"inputs": {"inputs_pretokenized": "What is the choice to the following Question? Only provide the choice by providing a single letter.\n\nQuestion: The students in a class would like to make 20 paper sailboats for a race. The students will select one design and collect the materials they need to construct the boats. Which of the following is the best way for the students to be sure the paper sailboats will float without tipping over in the water? Choices: (A)construct a prototype of a boat for testing (B)calculate the total mass of all of the finished boats (C)determine the total amount of weight each boat can carry (D)test the strength of each material used to construct the boats\n\nThe answer is:", "targets_pretokenized": "(A)construct a prototype of a boat for testing"}, "prediction": "(D)test the strength of each material used to construct the boats."}
>
> {"inputs": {"inputs_pretokenized": "What is the choice to the following Question? Only provide the choice by providing a single letter.\n\nQuestion: A class tested the amount of vitamin C in fresh orange juice and calculated a different amount than the previous class that conducted the same investigation. What should most likely be done to make sure that their results are accurate? Choices: (A)try a different juice (B)analyze the recorded data (C)ask a scientist what went wrong (D)repeat the investigation two more times\n\nThe answer is:", "targets_pretokenized": "(D)repeat the investigation two more times"}, "prediction": "(B) analyze the recorded data"}.

Given that you are computing the accuracy using the exact match, "(A) XXX" is not a correct answer, even if the answer was "(A)XXX" because of the white space after the (B). 4 out of 5 generation examples insert the white space after the parenthesis in the base model. After the RLHF process, there seems to be no space after the parenthesis. It is likely to be a good reason why it has less accuracy than the RLHFed models.
This raises my concern that the whole RLHF process is just learning not to put a white space after the parenthesis. I don't call it an alignment.

The theory of the paper is interesting enough to make the paper accepted if accompanied by some experimental results to support the idea.
However, I don't think the experiments are conducted to evaluate what the algorithm is supposed to do.

### Questions
- How many runs are conducted for Figure 1 and Table 1? Figures 4 and 5 show the average but do not show the standard deviation or standard error.
- I'm curious about why ARC-Challenge is chosen as the task for the offline learning task. ARC is a collection of questions evaluating the knowledge of the LLM. It is mostly used to evaluate the non-instruction tuned pretrained LLMs but not the result of the alignment process. Isn't the *POs just learning the format of the multiple question answering format? I also couldn't find how the evaluation is done for ARC. Do you consider only the exact match to be the correct answer?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Reinforcement Learning from Human Feedback (RLHF) is emerged as one of the most powerful approach to finetune the large language model (LLM) and align its performance to the human. However, even with the reward model-less approach like DPO, the uncertainty of the preference label remains as a core challenge. This work, VPO, highly exploits the closed form formulation between the reward function and optimal policy. From the intuition of the policy-invariance against prompt-dependent reward function shifting, they derive a tractable objective function that reflects the pessimism / optimism of the uncertainty. Proposed objective function has a guarantee of the uncertainty bound, and experimental results show an outperforming output than the baseline.

### Strengths
Their formulation and statements, thesis, have solid foundation and concrete derivation. They provide a reasonable error bound that allows one to estimate the difference between the trained policy and the optimal policy. Their base framework is easily applicable to the both online and offline settings with minimal modification and its implementation is quite simple. The language of the paper is tidy and easy to read.

### Weaknesses
Above all, the empirical gap is insufficient. Especially on table 1, the performance gap is around 0.5%p, therefore proper statistical tests are required to verify the effectiveness of the proposed method. Furthermore, Iter 3 setting tends to underperform than Iter 1 and Iter 2, thus it diminishes the intuition of theorem 1. The second concern is the misleading introduction. To my best knowledge, the term 'uncertainty' in the RLHF context usually refers to the ambiguousity and noise of the preference label. However, due to my understanding, this paper mainly focuses on the uncertainty and errors that occurred from the imperfect optimization of the RL framework itself. This part might be rewritten to avoid misleading and highlight their contribution.

### Questions
Is there any statistical result to validate the significance of the performance gap in Table 1? The gap looks marginal without any additional information. Reporting the standard deviation may be helpful, in my opinion. Rewriting your focus will reduce the misleading; the term uncertainty usually sounds like an error from the noisy label. Finally, it may be a subjective comment; the weight of the theory content was relatively high, and it reduced the volume of the experimental contents. I wish some more ablation studies could support your core contribution to the guaranteed confidence boundary.

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
The authors propose a new algorithm for RLHF, value-incentivized preference optimization (VPO), which allows for training an LLM with either optimistic or pessimistic principles in both offline and online settings. Experiments show VPO is more robust to over-optimization in the offline setting and outperforms online DPO in online settings.

### Strengths
- The theoretical motivation is clear and makes sense, and proposing both offline and online variants makes it more applicable in popular LLM training settings.
- The ARC-challenge experiments do seem to show that VPO does avoid over-optimization relative to DPO and IPO.

### Weaknesses
 - The AlpacaEval results seem quite weak, with further iterations of VPO underperforming multiple iterations of DPO, and having a fairly small gap in the one iteration setting (2 points). It would be useful to either run more seeds or try more models (e.g., VPO on top of llama 3 models) to see if the improvement is robust. The current results don't provide strong evidence that VPO consistently outperforms DPO in practical scenarios, especially given the small margin in the single iteration case and the underperformance in multi-iteration settings. The lack of statistical significance testing further weakens the claims of improvement. 
- There has been a lot of work into DPO-like algorithms recently in the field (I think the recent rainbowPO paper [1] has a good discussion of them). It would be useful to discuss how the proposed offline algorithm relates to these other approaches, such as SimPO [2] or WPO [3] (which appear to perform much more strongly on benchmarks like AlpacaEval 2). I see there is some discussion about how the method relates to DPOP, which is good. The absence of a detailed comparison with these methods makes it difficult to assess the novelty and practical advantages of VPO. Specifically, it's unclear if VPO offers unique benefits beyond what these existing methods already provide, or if it simply replicates their performance with a different formulation.
- Following the above, it would be good to see comparisons with these newer, reportedly better-performing DPO variants as well, to see if VPO still can perform better or similarly. Without these comparisons, it's hard to determine if VPO is a genuine advancement or just another method with similar performance characteristics. The lack of direct comparisons with state-of-the-art DPO variants limits the impact of the paper.

### Questions
- How does the proposed approach differ to and work with other *PO approaches? (as mentioned in weaknesses)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Value-Incentivized Preference Optimization (VPO), a novel method designed to unify online and offline Reinforcement Learning from Human Feedback (RLHF). The primary goal of VPO is to address the challenge of incorporating uncertainty estimation into the reward function, a key issue in both online and offline RLHF. VPO regularizes the maximum likelihood estimate of the reward function using the value function, modulated by a sign to indicate whether optimism or pessimism is chosen. The method also directly optimizes the policy with implicit reward modeling, simplifying the RLHF pipeline. Theoretical guarantees for VPO are provided, showing that it matches the performance rates of standard RL algorithms in both online and offline settings. Experimental results on text summarization, dialogue, and standard benchmarks verify the practicality and effectiveness of VPO.

### Strengths
1. VPO provides a unified approach to both online and offline RLHF, addressing a significant gap in the literature. This makes it applicable to a wide range of scenarios where preference data is either abundant or scarce.

2. The paper offers strong theoretical guarantees, demonstrating that VPO matches the performance rates of standard RL algorithms. This theoretical foundation adds credibility to the practical applicability of VPO.

3. VPO is designed to be practically implementable and theoretically grounded, making it suitable for large language models (LLMs). The regularization technique using the value function is straightforward and computationally feasible.

4. By directly optimizing the policy with implicit reward modeling, VPO simplifies the RLHF pipeline. This reduces the complexity and computational cost of training LLMs, making the method more accessible and efficient.

5. The paper includes comprehensive experiments on various tasks such as text summarization, dialogue, and standard benchmarks. These experiments demonstrate that VPO is effective and practical, outperforming or matching existing methods in different scenarios.

6. The work suggests a broader methodology for designing practical algorithms with principled optimism or pessimism under more general RL setups, opening avenues for future research and applications.

### Weaknesses
1. Although the paper covers several tasks, the scope of the experiments might be limited. More diverse and challenging tasks, particularly those involving real-world applications, could further validate the robustness and generalizability of VPO. While the paper claims that VPO matches or outperforms existing methods, a more detailed comparison with state-of-the-art techniques, including recent advancements in RLHF, would strengthen the claims and provide a clearer picture of VPO's advantages. Specifically, the paper lacks a rigorous ablation study to demonstrate the impact of different components of VPO, such as the value-based regularization term, on overall performance. It would be beneficial to see how performance changes with varying degrees of regularization, and whether the method is sensitive to the choice of the value function used for regularization.

2. The theoretical guarantees provided are based on certain assumptions, such as well-behaved reward functions and policies. These assumptions may not always hold in real-world scenarios, limiting the applicability of VPO in more complex environments. The paper does not fully address the potential impact of these assumptions on the practical performance of VPO. For example, the assumption of a linear reward function is a strong one, and it is unclear how the theoretical guarantees would be affected if this assumption is relaxed. Furthermore, the paper does not discuss the sensitivity of the theoretical results to the choice of hyperparameters used in the VPO algorithm.

3. The paper does not extensively discuss the scalability of VPO to extremely large datasets or models. Addressing these scalability issues would be crucial for deploying VPO in industrial-scale applications. While the paper mentions that VPO is computationally efficient, it lacks a detailed analysis of the computational complexity of the algorithm, particularly when applied to large language models. It would be useful to see a breakdown of the computational cost of each step in the VPO algorithm, and how this cost scales with the size of the dataset and the model.

### Questions
Is VPO equal to the DPO+KL penalty?

### Soundness
3

### Presentation
3

### Contribution
3
