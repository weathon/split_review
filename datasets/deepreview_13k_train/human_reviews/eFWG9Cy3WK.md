# Merge, Then Compress: Demystify Efficient SMoE with Hints from Its Routing Policy

- Decision: Accept
- Scores: 3, 8, 8

## Abstract
Sparsely activated Mixture-of-Experts (SMoE) has shown promise to scale up the learning capacity of neural networks, however, they have issues like: ($a$) \textit{High Memory Usage,} due to duplication of the network layers into multiple copies as experts; and ($b$) \textit{Redundancy in Experts,} as common learning-based routing policies suffer from representational collapse. Therefore, vanilla SMoE models are memory inefficient and non-scalable, especially for resource-constrained downstream scenarios. In this paper, we ask: \textit{Can we craft a compact SMoE model by consolidating expert information?} \textit{What is the best recipe to merge multiple experts into fewer but more knowledgeable experts?} Our pilot investigation reveals that conventional model merging methods fail to be effective in such expert merging for SMoE. The potential reasons are: ($1$) redundant information overshadows critical experts; ($2$) appropriate neuron permutation for each expert is missing to bring all of them in alignment. To address these challenges, we propose a novel merging algorithm for SMoE, \textit{i.e.}, \texttt{M-SMoE}, which leverages routing statistics to guide expert merging. Specifically, it \uline{starts} with neuron permutation alignment for experts; \uline{then}, dominant experts and their ``group members" are formed based on routing policies; \uline{lastly}, every expert group is merged into a single expert by utilizing each expert's activation frequency as their weight for merging, thus diminishing the impact of insignificant experts. Moreover, we draw an interesting observation that our proposed merging promotes a low dimensionality in the merged expert's weight space, naturally paving the way for additional compression. Hence, our final method, \texttt{MC-SMoE} (\textit{i.e.}, Merge, then Compress SMoE), further decomposes the merged experts into low-rank and structural sparse alternatives. Extensive experiments across $8$ benchmarks validate the effectiveness of our proposals. For instance, our \texttt{MC-SMoE} achieves up to $80\%$ memory and a $20\%$ FLOPs reduction, with virtually no loss in performance.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes MC-SMoE, which is a compression method for Mixture-of-Experts models. The idea is to split experts into several groups, where only the most important expert is kept in each group. The authors further propose an algorithm to compress the merged experts. Experiments are provided to demonstrate the effectiveness of the proposed method.

### Strengths
* In this work, the authors study how to consolidate experts in MoE models. This is a very important topic since one of the major bottlenecks of deploying MoE models is the memory usage.

* The problem studied in the paper is well-motivated. It is well-known that there are redundancies in MoE models. This paper leverages this finding and propose algorithms to compress MoE models.

### Weaknesses
Concerns and questions about presentation:

* What is the intuition behind experts permutation alignment? Specifically, how is “alignment” defined? I can understand from performance-wise (Table 6) that alignment is needed. However, I do not understand how two experts are “aligned” using the proposed alignment method. To make the paper self-contained, please include the detailed algorithm used for this. It is unclear how the permutation is computed and what objective function is being optimized to achieve this alignment. The paper should clarify whether this is a one-time operation or if it is performed iteratively during training.

* How are the results in Figure 3 computed? From my understanding, a Switch-base-32 model is first fine-tuned on each individual task, and then the activation frequencies are computed. Are the models fine-tuned with the load balancing loss [1]? It seems in Figure 3, loads of different experts are extremely unbalanced. The paper should clarify if the observed imbalance is a result of the fine-tuning process or an inherent property of the model architecture. Furthermore, the impact of this imbalance on the compression method should be discussed.

* How is the stable-rank computed? For example, in a specific layer, the 32 experts are compressed into 6 experts. Do you compute the average stable-rank of the 32 experts as “before” in Figure 4, and the average stable-rank of the 6 experts as “after”? It is important to specify whether the stable rank is computed for individual experts and then averaged, or if it is computed on the merged experts directly. The paper should also clarify if the stable rank is computed on the weight matrices directly or on the activations.

* I do not fully understand how experts are grouped. It is mentioned that “each non-dominant expert gravitates toward and joins the group led by its most similar dominant expert“. For example, suppose we have two dominant experts $E_1$ and $E_2$, then for a non-dominant expert $E$, do you calculate the similarity of $E$ with $E_1$ and $E_2$, and then assign $E$ to the more similar one? If this is true, is it possible that nearly all non-dominant experts are assigned to the same group? The paper should provide a more detailed explanation of the similarity metric used for grouping and discuss the potential implications of having imbalanced group sizes.

* The pruning of $S$ needs more justification. It is mentioned that “the weight columns with the lowest cumulative scores will be removed”. Why are weights pruned according to cumulative importance scores instead of importance scores? The pruning procedure in Appendix A2 also seems ad-hoc. How is this particular pruning schedule chosen? The paper should justify the use of cumulative scores over individual scores and provide a rationale for the specific pruning schedule, including its impact on model performance and convergence.


Concerns about experiments:

* I would like to further understand the role of knowledge distillation. The authors mention that all the models (including the baselines) in Table 2 use knowledge distillation. Could the authors provide some results of the dense and full-SMoE models without distillation? It is crucial to understand the individual contribution of knowledge distillation to the final performance of the compressed models. The paper should clarify if the distillation is performed from the full-SMoE model or from a different teacher model.

* From Table 2, it seems performance of the model considerably drops after applying the compression technique (M-SMoE vs. MC-SMoE). The authors should provide more detailed analysis on the design of the compression method. For example, will different pruning strategies/schedules work better? The paper should explore alternative pruning strategies and schedules and provide a comparative analysis of their impact on model performance. This analysis should include a discussion of the trade-offs between compression ratio and performance degradation.

* The authors mention “further memory and parameter efficiency” in the paragraph above Algorithm 1. However, no experiments are conducted to evaluate the speed and memory of the MC-SMoE models. The latency results in Table A10 indicate that there is only marginal speed gain of M-SMoE compared with full-SMoE. The authors should benchmark the inference speed (throughput) and memory usage of M-SMoE and MC-MoE, and compare the metrics with the dense and the full MoE models. The paper should provide a comprehensive analysis of the computational cost and memory footprint of the proposed compression method, including a breakdown of the time spent on different operations.

### Questions
See above

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a mechanism for merging multiple experts by merging redundant experts while preserving as much as knowledge as possible. It is achieved by:
1. Aligning the weights of any two given experts at a time using a permutation matrix since two models that are merely weight permutations of each other are equivalent. 
2. The router policy is used to group experts into groups of similar experts. Based on activation frequency, weight permutation-corrected experts in a group are merged together.  
3. The final merged expert is further compressed by a low-rank decomposition and pruning of the incoherent part.

### Strengths
The authors perform an extensive experimental analysis of each of their design decisions for:
1. Their averaging strategy (Tab. 8)
2. Need for permutation alignment (Tab. 6)
3. Similarity function and the superiority of use of router logits (Tab. 4)

The authors also provide comparisons on multiple text datasets

### Weaknesses
A theoretical proof of either 1. Optimality of their expert merging algorithm or 2. An error bound on either the information loss/performance degradation based on their proposed algorithm would have significantly helped this work.
An analysis of the computational cost as the number of SMoE layers increases would be helpful.

### Questions
1. Could you provide some theoretical insights into why the merging of experts should be done before compression since compression might be able to get rid of irrelevant information and make it more convenient to compare experts later for merging?
2. Could you provide some theoretical background for your claim that similar experts would show similar router logits?
3. An interesting line of investigation is the long-term scalability of how one could add more experts later during the life-cycle after applying M-SMoE.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper distills a large body of experts (in a mixture-of-experts model) into a few experts. This saves memory and improves fine-tunability of the final model. The core idea is to repermute neurons, group based on neuron "routes", then merge models. The authors show memory and FLOP reductions with negligible quality loss.

### Strengths
- The figures are clear, the motivation is well-written, and the paper is overall well put together. 
- The paper presents a large array of experimental results and ablations; the results are convincing.
- Figure 1: Impressive results. (A tradeoff curve might be nice? e.g., lines connect your points. also nit: The legend kinda blends in. Maybe give it a strong border or clearer background?)
- Figure 2 is likewise well done. The lighted dotted lines are and spacing clearly separate the three parts, and the illustration of "highly frequent" to "cluster center" is helpful. (nit: I wish the fonts and sketch-esque style was applied to everything)
- Figure 3's insight and accompanying visualizations are clear and insightful. Is this used later on anywhere? e.g., model can be compressed more aggressively for SST2 than for COPA.

### Weaknesses
 - Experts permutation alignment (then computing similarity based on routes) is a big part of the paper, but the details are a bit lost on me. It could be worth adding more to 3.1, covering the basics of how the different possible permutations are searched. Specifically, it's unclear how the search space of possible permutations is explored. Is it exhaustive, or is some heuristic or approximation used? The computational cost of this search, and how it scales with the number of experts, should also be discussed.
- In 3.1, it *seems like there's a chicken and egg problem -- we need alignment to know which experts are more similar *but we need to know which expert is the "reference" to re-align. How is that resolved?

### Questions
- nit: the changing underline baseline is visually unappealing. not sure if there's a way to glue underlines to the bottoms of letters. this is a super-nit of course, doesn't really matter at all

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
