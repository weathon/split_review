# Common Pitfalls of Margin-based Preference Optimization in Language Model Alignment

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 6, 5, 5

## Abstract
Reinforcement Learning from Human Feedback (RLHF) has become the predominant approach for aligning language models (LMs) to be more helpful and less harmful. At its core, RLHF uses a margin-based loss for preference optimization, which specifies the ideal LM behavior only in terms of the difference between preferred and dispreferred responses. 
This under-specification of ideal behavior for each response individually leads to two unintended consequences as the margin increases:
(1) The probability of dispreferred (e.g., unsafe) responses may increase, resulting in potential safety alignment failures.
(2) When the probability of dispreferred responses is reduced, this often coincides with a decrease in the probability of preferred responses, even when these responses are ideal.
In this paper, we identify the fundamental issue: margin-based preference optimization loss under-specifies ideal LM behaviors. 
We derive key conditions under which the probabilities of both preferred and dispreferred responses increase or decrease together. 
These conditions occur when the inner products between the gradients of the log-probabilities of preferred and dispreferred responses are large. 
We theoretically analyze when such inner products are large and empirically validate our findings. 
Our framework also reveals important differences in the training dynamics of various preference optimization algorithms and suggests new directions for developing better algorithms for language model alignment.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper considers a common failure mode of RLHF algorithms like DPO, in which, although the difference between preferred and dispreferred outputs is guaranteed to increase, there is no guarantee that the log likelihood of the preferred option will increase, or that the log likelihood of the dispreferred option will decrease.  This paper derives a general criterion that can be used to identify pairs in which either both will increase, or both will decrease.

### Strengths
The theoretical analysis was enjoyable to read. The examples demonstrate the proposed criterion quite clearly.

### Weaknesses
The provided examples are tremendously simplified, which is useful to demonstrate the applicability of the theoretical analysis, but which reduces confidence that the analysis will have much impact on real LLM practice.

The analysis in the submitted manuscript clearly demonstrates the high-correlation problem in response pairs that closely match, but does not clearly demonstrate that the high correlation is still a problem in distinguishing response pairs that are very different. I'm thinking in particular of toxic responses, e.g., one response in a pair expresses a negative stereotype, and the other does not; there may be little lexical overlap between the two. For simple academic exercises, it is important to analyze cases when the responses being discriminated are quite similar. In real-world deployments, however, I think the responses may be very different.  The paper's analysis does not sufficiently address the practical relevance of the identified issue in scenarios with significant dissimilarity between responses.

### Questions
Is there any strong argument that the problematic behavior addressed by this paper (both go up, or both go down) is important in real-world settings?

I was intrigued by the claim that the log likelihood of a dispreferred output can go up, but this seems to not be a problem that has concerned any previous authors.  The alternative approaches discussed in the paper all address the problem that the log probability of the preferred option might go down, and that outcome is the outcome suggested by the last example analyzed in the paper.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates issues in margin-based preference optimization for language model alignment, with a focus on the Direct Preference Optimization (DPO) algorithm. It highlights that margin-based loss specifies only the ideal margin behavior, overlooking individual term behaviors, which often results in synchronized log probability changes between chosen and rejected responses. The authors theoretically derive conditions for this phenomenon starting with DPO, and extend their insights to other margin-based algorithms. They examine cases where the derived condition holds, noting that higher token similarity between chosen and rejected responses can intensify synchronized movement, and validate these findings empirically.

### Strengths
This paper stands out in its originality by addressing the under-explored limitations of margin-based preference optimization in RLHF, offering fresh insights into its impact on language model alignment. The theoretical contributions, specifically the gradient inner product conditions, demonstrate high quality, providing a clear, mathematically grounded framework that identifies when alignment failures may occur under existing loss structures. 
In addition to an in-depth focus on the DPO algorithm, the paper comprehensively reviews existing methods in Table 2 and extends its findings in Section 3.2, which gives additional quality to the paper.
The suggested condition in DPO is further substantiated with its practical implication, with experimental validation in Section 4.

### Weaknesses
The paper centers primarily on DPO in Sections 3.1 and 4, with limited coverage of other margin-based optimization algorithms. To better align with reader expectations, it would be beneficial to introduce their main focus of DPO explicitly in the introduction and outline how subsequent sections will compare DPO against alternative approaches. Alternatively, devoting more space to a detailed examination of other algorithms could create a more balanced narrative.

The experimental results in Section 3.3 primarily observe phenomena regarding preferred and dispreferred response probabilities increasing or decreasing together—findings that have already been discussed in previous work, such as Pal et al. (2024), and does not fully investigate the conditions under which these probability trends occur. Furthermore, the experiment relies on a single dataset, limiting the depth of empirical validation. 

The empirical observations are concise but lack important methodological details. For instance, it would be valuable to clarify how log probabilities are computed in Figure 1 (e.g., whether they are averaged over the training samples), and to include additional measures such as standard deviations or confidence intervals to improve the figure's reliability. Since Figure 1 is intended as a motivating visualization, providing a additional figure for dedicated to empirical results (Section 3.3) would allow for a more thorough presentation of the experimental findings without cluttering the introductory material.

For minor clarification, it would be better to change the interval of the grid to clearly show the trend of margin in Figure2.

### Questions
1. The paper presents a clear delineation between preferred and dispreferred samples. 
However, some papers focus on distributional framework. This approaches insists the model to encounter a broader range of sample types to cover the distribution's full support, supporting the original RLHF sampling method.
- Go, Dongyoung, et al. "Aligning language models with preferences through f-divergence minimization." arXiv preprint arXiv:2302.08215 (2023).
- Korbak, Tomasz, et al. "On reinforcement learning and distribution matching for fine-tuning language models with no catastrophic forgetting." Advances in Neural Information Processing Systems 35 (2022): 16203-16220.

 Could the authors discuss the potential impacts of their idealized setup compared to a distributional approach? This clarification would help assess the implications of choosing one framework over the other in alignment training.

2. Training with both high- and moderate-quality responses, where one is better but another may serve as a hard negative example, can push the model to better distinguish between fine-grained preference levels. The ideal condition that assume clear difference of the quality  between preferred and dispreferred samples, seems to take a different approach. Does this work incorporate hard negative samples, or is it constrained to cases with explicit distinctions?

3. The findings on token-level gradients provide an intriguing direction for refining preference optimization. Could the authors elaborate on any potential methods to leverage token-level distinctions more effectively within their model, perhaps as a future research direction or via fine-grained adjustments?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper identifies and analyzes a fundamental problem with margin-based preference optimization in language model alignment (like RLHF): these methods only specify how much better preferred responses should be compared to dispreferred ones, without specifying how the individual probabilities should behave. This leads to two unintended consequences: (1) sometimes the probability of dispreferred (e.g., unsafe) responses increases, and (2) when reducing dispreferred response probabilities, the probability of preferred responses often decreases too, even when they are ideal.

### Strengths
The paper addresses a fundamental issue in language model alignment through RLHF by analyzing the under-specification problem in margin-based preference optimization - this is an important contribution given how widely RLHF is used.

### Weaknesses
1  Presentation Issues:
The notation becomes dense and potentially confusing in Section 3.2, particularly around the general form analysis
Some figures (like Figure 4b) would benefit from more detailed explanations of their implications
The connection between the theoretical results and practical implications could be more clearly articulated

2  Limited Experimental Validation:  
Experiments are conducted on only one main dataset (TL;DR) and a simple sentiment classification task
Only tested on two main models (Mistral 7B and Llama-3 8B)
Lacks validation across diverse preference optimization scenarios and task types
More extensive empirical validation across different datasets and model architectures would strengthen the claims

3  Theoretical Assumptions:
The theoretical analysis in Section 4.1 relies on somewhat simplified model settings (learnable last linear layer, learnable logits)
Some assumptions about token probability relationships between chosen/rejected responses may not hold in practice
The extension of single-token results to multi-token cases could be more rigorously justified

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper criticizes margin-based preference optimization for LM alignment, which is a core method in RLHF. While increasing preference margins can reduce unsafe responses, it also often reduces preferred response probabilities, due to synchronized probability shifts between chosen and rejected responses. The authors reveal when these shifts occur and suggest that the under-specification of behaviour in current margin-based methods limits model safety and effectiveness. The work proposes fine-grained, token-level approaches as potential improvements, though this is not really pursued very deeply in this work.

### Strengths
- The paper provides a fairly nuanced and theoretically grounded critique of margin-based preference optimization, which is an increasingly relevant task (especially  in RL). Identifying conditions under which preference optimization can backfire is important for real-world use and may provide a relatively underdeveloped area of research
- The proposal to address preference optimization problems at the token level is interesting (though perhaps not surprising).

### Weaknesses
 - this is not meant to be a primarily empirical paper (apparently, it leans more on its theoretical aspects) but this work of course calls for broader empirical validation than it has. The proposed method may be evaluated across diverse tasks such as summarization, dialogue, and instruction-following. Other variants of the given LLMs (e.g., LLaMa) could have been explored, to demonstrate generalizability. 
- The analysis of Sec 4 focuses on synthetic, controlled scenarios. The kinds of complexities exist that in actual, diverse language data should be addressed.

### Questions
- While the theoretical analysis of gradient inner products and synchronized probability shifts is fairly rigorous, what actionable insights for real-world RLHF applications are achievable?
- How would you evaluate the ‘safety-critical alignment tasks’ you mention in Sec 5 as being particularly ill-suited for margin-based preference optimization?
- Can you clarify more directly how token-level gradient inner products between chosen and rejected responses provide a reliable indicator for alignment behaviour?

### Soundness
3

### Presentation
3

### Contribution
2
