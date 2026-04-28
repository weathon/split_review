# Dense Backpropagation Improves Routing for Sparsely-Gated Mixture-of-Experts

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 5, 3, 6

## Abstract
Mixture of Experts (MoE) pretraining is more scalable than dense Transformer pretraining, because MoEs learn to route inputs to a sparse set of their feedforward parameters. However, this means that MoEs only receive a sparse backward update, leading to problems such as router load imbalance where some experts receive more tokens than others. We present a lightweight approximation method that gives the MoE a dense gradient while only sparsely activating its parameters. A key insight into the design of our method is that at scale, many tokens not routed to a given expert may nonetheless lie in the span of tokens that were routed to that expert, allowing us to create an approximation for the expert output of that token from existing expert outputs. Our dense backpropagation outperforms standard TopK routing across multiple settings without significantly increasing runtime.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper provides an improved back propagation method for MoE routing where the back propagation flows through the outputs of the experts that are not among these sparsely activated ones. This is done by approximating the outputs  of non-executed experts as the average output of other similar tokens executed by the expert. Similar tokens may be defined by those routed to a similar set of experts, or those that have a high attention score with the given token. Experiments show that this method gives improved metrics without increasing training compute.

### Strengths
Gives a simple method to approximately estimate outputs of each expert for each input to improve the backprop gradients to the router. It is nice to see in Figure 9 that quality of approximation of the router gradient is fairly high.

Does not increase the computation required for the backprop

Experiments show improved metrics.

The method provides better load balance.

The paper is fairly well written.

### Weaknesses
Expert may be highly non-linear so averaging in this way need not be a good approximation always. Is there a possibility of a better "higher order" approximation?

The perplexity drop in Table 4 seems small.

### Questions
Is there an implicit assumption that the experts are "linear'?

You don’t pass gradients through the expert parameters and are only focused on the router gradients. Could something be done to approximate the expert gradients too?

### Soundness
3

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
4

### Summary
This paper introduces a novel method to enhance the performance of MoE models, which are crucial for large-scale language model pretraining due to their scalability advantages over dense Transformers. MoEs route input tokens to a sparse set of experts, leading to sparse backward updates and potential load imbalance issues. The proposed method addresses this by providing a dense gradient to the MoE router while maintaining sparse activation.    

The key idea is that at scale, many tokens not routed to a specific expert might still be similar to those routed to that expert. This allows for approximating the expert output for unrouted tokens based on existing expert outputs. The authors propose three approximation methods: Expert Group Approximation, Attention Approximation, and Attention Approximation with LSH. Their experimental results demonstrate that Dense Backpropagation, particularly the Expert Group Approximation method, outperforms standard Top-K routing in both performance and load balance across various MoE configurations without increasing runtime.

### Strengths
The paper presents a novel approach to address the limitations of sparse backpropagation in MoEs. While previous work has focused on auxiliary loss functions or alternative routing methods, this work introduces the concept of approximating expert activations to provide a dense gradient signal. This is a creative solution that hasn't been explored in prior work.  

The paper is well-written and easy to follow. The authors provide a clear explanation of their method, including visualizations and detailed descriptions. The notation is consistent, and the overall structure of the paper is logical and coherent.

By improving the load balancing and performance of MoEs, Dense Backpropagation can lead to more efficient training and resource utilization. This is particularly important as language models continue to grow in size and complexity.

### Weaknesses
The evaluation has been primarily focusing on perplexity evaluation. The review feel a more thorough evaluation on scoring and sampling tasks could significantly improve paper's quality. The authors acknowledge that their evaluation is limited in terms of the number of benchmark results, training tokens, and the size of the MoEs. Expanding the evaluation to include more diverse and challenging tasks, as well as larger models and datasets, would further strengthen the paper's conclusions. 

While the paper focuses on the training benefits of Dense Backpropagation, it doesn't analyze its impact on inference workloads. Evaluating the method's efficiency and performance during inference would provide a more complete picture of its practical implications. 

The paper primarily focuses on the Expert Group Approximation method due to its efficiency and ease of implementation. A more in-depth exploration of the other two approximation methods, Attention Approximation and Attention Approximation with LSH, could reveal further potential for improvement. If the other two methods are not useful at all. It is better to not mention the other two methods. 

The paper lacks a comparison with more recent work in MoE routing. A few related work that can be compared:
- "Mixture-of-Experts with Expert Choice Routing" by Zhou et al. (2022)
- "DeepSeek-MoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models" by Dai et al. (2024)
- Gradient-Informed MoE (GRIN)
- SparseMixer

### Questions
1. The paper consistently uses K=2 for Top-K routing. Have you experimented with different values of K, and how does Dense Backpropagation perform with larger or smaller K values?

2. The paper acknowledges that it doesn't analyze the impact of Dense Backpropagation on fine-tuning MoEs. Do you have any insights or plans to investigate whether the method improves the stability or performance of MoEs during fine-tuning?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes a dense approximation of the top K's gradient in SMoE. The method centralizes around the assumption that the output of an inactivated expert can be approximated by the outputs of other tokens routed to that expert. From there, the authors propose an expert group approximation to identify the relevant tokens given the current token and the inactivated experts. The experiments on a DeepSeek MoE and a conventional MoE show that the proposed method can perform better than the standard top K routing.

### Strengths
- Find a dense approximation of the top K routing is an important research topic.
- The proposed method show encouraging performances on some benchmarks.

### Weaknesses
 - **The motivation of this work is not empirically validated** - It is unclear if the key motivation that an inactivated expert output can be reliably approximated by the activations of some other tokens. Specifically, the paper lacks a direct analysis of how well the proposed approximation matches the true gradient of an inactivated expert. The authors should provide a quantitative analysis, such as cosine similarity or mean squared error, between the approximated gradient and the actual gradient on a held-out set of tokens and experts. This analysis should be performed across different layers and training stages to understand the approximation's behavior.
- **Poor presentation of the experimental results** - The authors implemented two SMoE models: a DeepSeek MoE and a conventional MoE. However, in many of the results, it is unclear which model is being reported, e.g. Figure 1, 7, 11, and Table 3,4. Overall, Section 4 is very confusing because of the inconsistent presentation of the results of the two models considered (e.g. validation perplexity for DeepSeek MoE as a plot in Figure 6 while it is a table for the conventional MoE in Table 4), some figures (7, 8) and tables (2, 3, 4) do not mention which model is being reported, and are not placed immediately where they are first mentioned. The lack of clear labeling and consistent reporting makes it difficult to interpret the results and draw meaningful conclusions.
- **Lack of baselines** - Dense approximations for the Top K operator is extensively studied in the literature, even the authors mentioned several relevant strategies (L140-146). Yet, the proposed method is only compared with the standard Top K baseline, ignoring all other baselines. It is important to show that the proposed method can show some advantages over state-of-the-art strategies such as SparseMixer. The authors should include a comparison with at least one or two established dense approximation techniques to properly contextualize the performance of their method.
- **Significance of the results** - Nowadays large scale LLMs, especially MoEs, are interested in the zero-shot evaluation settings. Yet these results are only briefly showed in Figure 1 and 11. What are the numbers on these benchmarks and are the improvements significant over strong baselines. The authors need to provide the exact numerical results on these zero-shot benchmarks, along with statistical significance tests, to demonstrate the practical impact of their method. A qualitative analysis of the types of tasks where the method excels or fails would also be beneficial.
-  **Some claims are incorrect** - In L20, the authors claimed that the propose method does not "increase runtime", which is not entirely correct given that in L66-67 the authors stated that the method incurs "minimal overhead", and the throughput reported in Table 4. Moreover, the attention approximation clearly introduces more overhead. The authors need to be more precise about the computational cost of their method. The use of terms like "minimal overhead" is vague and should be replaced with concrete measurements of latency and throughput.
- **Expert group approximation** - The experiment present in L479-496 may contradict the proposed method. The proposed "more accurate" approximation performs worse than the original method, suggesting that either the original idea may not be rigorous, or the proposed approximation is not more accurate. The authors didn't fully investigate this result, making this work seems incomplete and lack rigorousness. The authors should provide a more detailed analysis of why the more accurate approximation performs worse. This could involve examining the variance of the approximations, the sensitivity to different hyperparameters, or the impact on different parts of the model.

### Questions
- Does the main motivation of the proposed method actually hold in practice?
- Can you present a more rigorous investigation of the results in L479-496?
- Can the propose method outperform some state-of-the-art strategies on zero-shot benchmarks?
- Please carefully revise Section 4 and make the claims regarding the complexity more accurate.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a novel method to improve routing in Mixture of Experts (MoE) by approximating the oracle dense gradient to update the entire router for each token. The authors introduce a lightweight group averaging method, allowing MoEs to receive dense gradient updates during backpropagation without activating more experts in the forward pass. The proposed method outperforms standard Top-K routing across multiple benchmarks, reduces load imbalance, and maintains runtime efficiency. Alternative approximation methods like attention and LSH attention are also explored.

### Strengths
1. *Improved Performance*: The proposed Expert Group Approximation method achieves better results than standard Top-K routing in terms of training loss, validation perplexity, and downstream accuracy.
2. *Lightweight*: The method is computationally efficient, introducing minimal overhead while maintaining strong performance.
3. *Enhanced Load Balancing*: The method approximates the dense gradient well, leading to better load balancing than standard Top-K routing.
4. The method is verified on a relatively large model of 2B total parameters (470M active), and a relatively large training tokens of 200B. Ablations on various approximation heuristics are also presented, providing insight into the design choices.

### Weaknesses
1. *Motivation Clarification*: The authors propose using Expert Group Approximation to estimate the straight-through estimator (STE), suggesting that the dense gradient is superior. However, it is not clearly established that the sparsely activated MoEs trained with this STE-based dense gradient will perform better than those trained with sparse gradients. A direct experiment validating this assumption is needed to strengthen the motivation. Specifically, the paper lacks a baseline where the same sparse activation pattern is used in the forward pass, but the backward pass uses the STE-estimated dense gradient. This baseline is crucial to isolate the effect of the proposed approximation method.
2. *Unclear Methodology Presentation*: The method is initially presented as focusing on approximating the router gradient during backpropagation, but in Section 4.2, it is revealed that applying the method only in the backward pass results in poor performance. Both the forward and backward passes need modification for the method to work effectively, which is fundamentally different. Introducing this crucial detail earlier would prevent confusion and improve clarity. The paper needs to clearly specify how the forward pass is modified, and why this modification is necessary for the method to work effectively.
3. *Modest improvement*: The improvement in validation perplexity (from 18.92 to 18.55, approximately 2%) is relatively small. Considering the slight drop in efficiency (97.7% speed) and the limited experimentation on only two settings, the practical significance of this improvement could be questioned. The paper should include more experiments across different model sizes, datasets, and training regimes to demonstrate the robustness of the method.
4. *Dependence on large micro batch size*: The methods need a large micro batch size to achieve good approximations, which is a limitation when training large-scale models with limited VRAM. The paper should provide a detailed analysis of how the micro batch size affects the approximation quality and the overall performance of the method. It should also explore techniques to mitigate this dependence on large micro batch sizes.

### Questions
1. The proposed Expert Group Approximation seems to be carefully designed for $K=2$. How does it perform with $K=1$ or $K>2$?
2. Does the method scale effectively with an increasing number of experts? Would it perform better in more sparse configurations with a higher number of experts?
3. The approximation of each token seems to involve activations or activation gradients of future tokens. Does this preserve causality in autoregressive models?

### Soundness
3

### Presentation
2

### Contribution
3
