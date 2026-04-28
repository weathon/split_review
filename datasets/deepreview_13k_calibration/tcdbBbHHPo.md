# Direct Alignment of Language Models via Quality-Aware Self-Refinement

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
Reinforcement Learning from Human Feedback (RLHF) has been commonly used to align the behaviors of Large Language Models (LLMs) with human preferences. Recently, a popular alternative is Direct Policy Optimization (DPO), which replaces an LLM-based reward model with the policy itself, thus obviating the need for extra memory and training time to learn the reward model. However, DPO does not consider the relative qualities of the positive and negative responses, and can lead to sub-optimal training outcomes. To alleviate this problem, we investigate the use of intrinsic knowledge within the on-the-fly fine-tuning LLM to obtain relative qualities and help to refine the loss function. Specifically, we leverage the knowledge of the LLM to design a refinement function to estimate the quality of both the positive and negative responses. We show that the constructed refinement function can help self-refine the loss function under mild assumptions. The refinement function is integrated into DPO and its variant Identity Policy Optimization (IPO). Experiments across various evaluators indicate that they can improve the performance of the fine-tuned models over DPO and IPO.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Recently, offline preferences-based RL methods have gained popularity for doing RLHF alignment without the need for online exploration or training a reward model. However, DPO methods, fail to take into account the relative qualitative differences between preference pairs since all training preferences are optimized equally. The authors argue that in the presence of the oracle reward model, the sigmoid of reward difference between very distinct preferences should be larger than the sigmoid of reward difference in preferences that are only slightly apart in quality. To enforce this ordering on top of existing DPO (and IPO) objectives, authors recommend a refinement operator that doesn't use any external reward model. Instead uses a prompted version of the same LM. In the case of DPO, their refinement term looks identical to the DPO's objective with the change that it has an additional evaluator prompt prepended to the input
> Please generate a response with a usefulness rating of 100 out of 100 for the following query. Note that the response should be harmless. The term 100 indicates the level of usefulness, where 100 is the maximum and 1 is the minimum. Query:

The authors add a positive weight $\lambda$ along with this refinement term before adding it to the DPO objective. The gradients are not propagated through the refinement term. Overall, this change increases the computational cost of the method with two forward passes for each input (one for DPO gradients and another for prompted refinement term) but also shows consistent improvements over vanilla objective across three different evaluations - MT-Bench, Vicuna Bench and Open LLM Leaderboard.

### Strengths
- Relatively simple modification of DPO (and IPO) objective to incorporate per-preference reweighting using a minor change in the input prompt.

### Weaknesses
- It is unintuitive why a mere prompt would enforce/align with the margins of an oracle reward. In the previous literature, it is well known that language models are poor at assigning numerical feedback like humans. This makes the choice of prompt more unclear in the refinement operator. Moreover, the results from Table 4, also suggest that the wording of the prompt doesn't matter too much on the performance.
- The naive variation of the refinement operator in Table 4, effectively reduces the $\beta$ parameter and the authors claim that it also outperforms DPO in terms of win rate. This suggests, that the DPO baseline is not hyperparameter tuned correctly and makes me question the insights derived from the results.
- The method presentation can be improved further. Both the abstract and intro vaguely hint at a refinement process with LM's internal knowledge, without giving any meaningful intuition of what that is up until section 3.

### Questions
- See weaknesses

### Soundness
2

### Presentation
2

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
This paper proposes a novel approach to align large language models (LLMs) with human preferences by leveraging the intrinsic knowledge within the models themselves. The authors introduce a refinement function that estimates the quality of both positive and negative responses, which is then integrated into Direct Policy Optimization (DPO) and its variant, Identity Policy Optimization (IPO). The goal is to improve the loss function and enhance the performance of fine-tuned models. The experimental results across various datasets show that the proposed methods outperform traditional DPO and IPO.

### Strengths
1. The paper introduces a novel method for refining the loss function using the intrinsic knowledge of LLMs, which is a good contribution to the field of model alignment.

2. The authors provide extensive experimental results that demonstrate the effectiveness of the proposed methods across different datasets, reinforcing the validity of their approach.

3. The paper includes a theoretical analysis that supports the design of the refinement function, providing a solid foundation for the proposed techniques.

### Weaknesses
1. The compared baselines are not enough. Many improvements to DPO introduce a gap between positive and negative samples; I won't list them all here, but the author needs to compare their approach with such methods.

2. Introduce a gap value into the DPO objective is not a very novel idea. The author introduce the gap value by a prompt-augmented query $p+x$, but I argue that the chosen of $p$ has a large influence to the final results.  The relative analysis is not enough.

3. According to my own experimental experience, I found that Zephyr is a model that is quite easy to fine-tune for good results. Some methods are effective on Zephyr, but may not be as significant when applied to other large models, which is also one of the reasons why the Zephyr model is widely used in a large amount of academic research. Has the author tested the proposed methods on other series of large models, such as Llama3.1-8b?

### Questions
1. Is Sr-IPO effective on other LLMs?

2. The author introduces a gap value in the gradient of the DPO objective function, which can change according to positive or negative preference pairs. Could a similar idea be applied to the coefficient $\beta$, meaning $\beta$ could adaptively change based on positive or negative preference pairs? Theoretically, could such an approach be proven effective?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper identifies a limitation in current RLHF methods, that is, they fail to consider the relative quality of chosen and rejected responses. To address this, the paper designs a self-refinement function, which includes the introduction of an additional prompt and modifications to the loss objective. This approach can be integrated into existing optimization methods (e.g., DPO and IPO), and demonstrates performance improvements.

### Strengths
1.	This paper is well-write and easy to follow.
2.	The proposed refinement function can be integrated into existing optimization frameworks like DPO and IPO, making it compatible with current research and practical applications.
3.	The self-refined methods (Sr-DPO and Sr-IPO) show performance improvements compared to traditional DPO and IPO, indicating the potential for future RLHF developments.

### Weaknesses
1. Lack of logical consistency. In the Abstract and Introduction sections, the authors emphasize utilizing the intrinsic knowledge of LLMs for self-refinement. However, in the Method section, they only introduce the addition of an extra prompt and the definition of a $\Delta$ objective based on the prompt, which is not convincing in demonstrating the application of LLMs' intrinsic knowledge.
2. Lack of novelty. As previously stated, the authors' method heavily relies on the introduction of an extra prompt and the definition of a $\Delta$ objective based on the prompt. Additionally, this $\Delta$ objective appears quite similar to the typical optimization objective of DPO, indicating a lack of innovation.

### Questions
1. Can the authors explain more clearly and convincingly how the proposed refinement method utilizes the intrinsic knowledge of LLMs to estimate the quality gap of responses?
2. Can the self-refinement method presented in this paper be combined with other RLHF approaches besides DPO and IPO, and would it lead to improved results?

### Soundness
2

### Presentation
3

### Contribution
2
