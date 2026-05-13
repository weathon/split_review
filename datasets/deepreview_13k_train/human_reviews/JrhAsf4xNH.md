# EM-DARTS: Preventing Performance Collapse in Differentiable Architecture Search with The Edge Mutation Mechanism

- Decision: Reject
- Scores: 5, 6, 3, 6

## Abstract
Differentiable Architecture Search (DARTS) relaxes the discrete search space into a continuous form, significantly improving architecture search efficiency through gradient-based optimization. However, DARTS often suffers from performance collapse, where the performance of discovered architectures degrades during the search process, and the final architectures tend to be dominated by excessive skip-connections. In this work, we analyze how continuous relaxation impacts architecture optimization, identifying two main causes for performance collapse. First, the continuous relaxation framework introduces coupling between parametric operation weights and architecture parameters. This coupling leads to insufficient training of parametric operations, resulting in smaller architecture parameters for these operations. Second, DARTS's unrolled estimation property leads to larger architecture parameters for skip-connections. To attack this issue, we propose Edge Mutation Differentiable Architecture Search (EM-DARTS), where during network weight updates, edges have a probability of mutating from a weighted sum of candidate operations to a specific parametric operation.
    EM-DARTS reduces the impact of architecture parameters on parametric operations, allowing for better training of the parametric operations, thereby increasing their architecture parameters and preventing performance collapse. Theoretical results and experimental studies across diverse search spaces and datasets validate the effectiveness of the proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces Edge Mutation Differentiable Architecture Search (EM-DARTS), an approach designed to address the performance collapse issue in Differentiable Architecture Search (DARTS).  The authors identify the main causes for collapse performance in DARTS: the coupling between network weights and architecture parameters in the continuous relaxation framework. EM-DARTS introduces a mutation mechanism that alters the DARTS supernet edges during network weight updates, allowing parametric operations to better align with the optimal feature map and reducing the impact of architecture parameters on these operations.

### Strengths
1. This paper is overall well-written.

2. Extensive experiments demonstrate that EM-DARTS outperforms some existing methods, including variants of DARTS, across different datasets and search spaces.

3. The edge mutation mechanism introduces negligible computational overhead, preserving the efficiency of DARTS.

### Weaknesses
1. I wonder why we need this  edge mutation rather than a simple EM algorithm to decouple the network optimaztion and architecture search. 

2. The performance of the proposed approach is not outstanding even compared to methods [R1] [R2] that were proposed three years ago.  Besides, the most recent article cited by the authors is published in 2023. And considering that it was September 2024 at the time of submission, I am curious as to why there was no comparison to the most recent methods, especially those published in 2024.

3.  The effectiveness of EM-DARTS heavily relies on the setting of the mutation probability, which may require careful tuning for different search spaces and datasets.

4. While the paper provides theoretical analysis, the validation largely relies on empirical results. More theoretical insights into the long-term behavior and stability of EM-DARTS could strengthen the paper's contributions.

### Questions
Please see the weaknesses.

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
4

### Summary
This paper focuses on mitigating the failure mode of the DARTS method which causes it to select architectures which are dominated by parameterless skip connection operations. The authors argue that while several explanations for this failure mode have been posited, ranging from overfitting during the search phase of DARTS to the unfair advantage of skip-connections in the optimization process, they all overlook the effect of the continuous relaxation of the search space on the parametric operations. They prove, theoretically, that the continuous relaxation framework causes the parametric operations to learn not the optimal features for themselves, but features that contribute to the overall performance of the edge. This finding intuitively explains the discretization gap to some degree. The authors suggest modifying the method used to combine the feature maps from operations on a given edge to generate the output feature map for that edge. Typically, the output feature map of an edge is produced by summing the feature maps of the operations on that edge, each weighted by their softmax-normalized architectural weights. The authors suggest a new approach: sample either this output feature map or the output of a randomly sampled parametrized operation as the output of the edge. This strategy encourages the parametrized operations to train more robustly on their own, rather than simply complementing the other operations on the edge.

### Strengths
### Originality

The proposed method can be seen as a hybrid of DARTS and other methods such as GDAS [1] which trains the supernet along one randomly sampled path at a time. However, the motivation for this approach is theoretically justified.

### Quality
The paper provides a decent ablation study of the main components of their method, albeit on a small tabular benchmark (NAS-Bench-201). These ablations show that (1) randomly sampling either the mixed feature map or the output feature map of a parametrized operation can induce stability to the training phase of DARTS and (2) this stability holds for an extended period of training the supernet (up to 400 epochs).

### Clarity
The writing is mostly clear and follows a neat narrative structure. The method is well-motivated and easy to understand.

### Significance
The main significance of the paper lies in its contribution to the theoretical understanding of the failure mode of DARTS.
Specifically, it shows that the continuous relaxation scheme of the supernet in DARTS does not allow the parametrized operations to learn the representations which are as close as possible to the optimal representations for a given edge.

### Weaknesses
The main weakness of the paper is the evaluation pipeline chosen for the DARTS architectures. It is mentioned in Section A.5.2 that "due to introducing more parametrized operations, the training is extended from 600 to 800 epochs". This significant deviation from the DARTS evaluation pipeline makes the results of the experiments unreliable. In my experience, the test performance of DARTS models do not plateau at 600 epochs of training. It is conceivable that the performance of the models could simply be an artifact of training the models 33% longer. The argument that the model is trained longer due to a higher number of parameters is also not strong, considering that DrNAS, which discovers models with 4M parameters (compared to EM-DARTS with an average of 4.3M), also evaluates the model with 600 epochs of training. Regrettably, this renders the comparisons in Table 2 both unfair and invalid.

The paper does not explicitly state the number of epochs used in training the Reduced DARTS models. It simply mentions that it is the same as DARTS in Section 4.2. If these models have also been trained for longer, then the comparisons in Table 3 are not fair either.

The experiments on NAS-Bench-201 look robust and fair, since they are all evaluated with a tabular benchmark. However, the results on this benchmark alone do not adequately defend the proposed method.

A few other minor issues are:
1. Grammatical errors in the text. E.g., "we analyzes" in the abstract in L017.
2. The text in Figure 1 is not clearly legible.
3. Incorrect style of citation in L196.

### Questions
1. Can the authors provide the results of EM-DARTS models trained for 600 epochs? 
2. What is the motivation for picking 800 epochs, specifically? Why not 700, for example, or 900?
3. Have you tracked the trajectories of the number of parameterless operations in the discretized models as the training of the supernet progresses? Empirically, is it not possible that the method simply biases the optimization in favour of architectures with more parametrized operations? As seen in Figure 5, the normal cells have no parameterless operations, while the reduction cell has only one parameterless operation (a skip connection) in its eight edges.
4. How does EM-DARTS perform against a random sampling baseline, where only parameterized operations are included in the search space?

### Soundness
2

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
This paper proposes an edge mutation approach to improve the robustness of DARTS.

### Strengths
+ The motivation of the paper is clear. It is well-known that DARTS has many robustness issues and there have been various ways to address that. 
+ The observation that insufficient training may be the cause for some of the issues of DARTS makes sense.

### Weaknesses
 - The technical contributions seem to be incremental. Essentially it is a form of doing DARTS and SPOS together. 
- The theoretical analysis is a bit misleading, and it seems to be very close to what has been discussed in existing work like DARTS-PT.
- The results are also less convincing. For instance, on DARTS space, the discovered models are significantly larger than the competing approaches, which probably is the main reason of performance increase. Also the search cost reported is the same with DARTS, but why?

### Questions
* What if you only do the mutation at different stages of training? Would that make major differences? 
* Why your search cost is the same with DARTS when you have to do extra work of mutation?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces EM-DARTS that alleviate the phenomenon of the dominance of skip connections during training of DARTS and the following works. First of all, this study attributes the dominance to two major reasons: 1) the less optimized network parameters due to the coupling of architecture and parametric weights, and 2) the unrolled estimation that all operations attempt to estimate the same feature map leads to a bias towards the choice of skip-connections. An edge mutation differentiable architecture search (EM-DARTS) method is proposed that randomly allows the output of each edge to adopt the one-hot operation. The mutation ratio follows an increasing trend through training to encourage exploitation at an early stage and finally lead to an unbiased estimation. Experimental results show strong performance results on various benchmarks.

### Strengths
1. This study is well-motivated as it explains the edge-operation dominance phenomenon well. I find the inverse relationship between the weight of each parametric operation and the variance of the output from its optimal value interesting, and the theoretical derivation is sound to me. 
2. The derivation of the biased nature of the unrolled estimation of each operation is also attractive and solid.
3. The experimental performance is competitive when compared with other state-of-the-art neural network search methods.

### Weaknesses
1. Although the two convincing reasons for the bias toward skip connection are presented, the solution is still intuitive. The paper does not discuss how mutation can reduce the coupling between parameter optimization and operation search. 
2. Given that the mutation can de-bias the optimization target of DARTS, previous studies like DS-NAS that introduced sparsity during DARTS training should also function similarly, despite their different motivations. This paper fails to discuss in detail the comparison with such studies. Furthermore, the authors' claim that the mutation is only applied to parametric operations is not clearly justified, as the impact of edge mutation on non-parametric operations is not shown in the paper. If the edge mutation on all operations does not significantly influence, what explains the performance gain over methods that have introduced sparsity?

### Questions
The reviewer appreciates the clear motivation and theoretical analysis, which outweighs the drawbacks. Therefore, a "weak accept" is voted for now.

### Soundness
3

### Presentation
3

### Contribution
3
