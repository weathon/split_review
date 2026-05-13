# Long-Sequence Recommendation Models Need Decoupled Embeddings

- Decision: Accept
- Scores: 5, 6, 3, 8

## Abstract
Lifelong user behavior sequences, comprising up to tens of thousands of history behaviors, are crucial for capturing user interests and predicting user responses in modern recommendation systems. 
A two-stage paradigm is typically adopted to handle these long sequences: a few relevant behaviors are first searched from the original long sequences via an attention mechanism in the first stage and then aggregated with the target item to construct a discriminative representation for prediction in the second stage. 
In this work, we identify and characterize, for the first time, a neglected deficiency in existing long-sequence recommendation models: a single set of embeddings struggles with learning both attention and representation, leading to interference between these two processes. 
Initial attempts to address this issue using linear projections---a technique borrowed from language processing---proved ineffective, shedding light on the unique challenges of recommendation models. 
To overcome this, we propose the Decoupled Attention and Representation Embeddings (DARE) model, where two distinct embedding tables are initialized and learned separately to fully decouple attention and representation. 
Extensive experiments and analysis demonstrate that DARE provides more accurate search of correlated behaviors and outperforms baselines with AUC gains up to 9\textperthousand~on public datasets and notable online system improvements. 
Furthermore, decoupling embedding spaces allows us to reduce the attention embedding dimension and accelerate the search procedure by 50\% without significant performance impact, enabling more efficient, high-performance online serving.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper suggests the inefficiency of using the same embeddings for attention calculation and preference prediction (representations) in lifelong sequence recommendations, where the user behavior history (sequence) is usually very long (more than 10,000). Authors correspondingly propose a decoupling framework, DARE, to boost the recommendation performance by decoupling embeddings. Specifically, DARE sets separate embedding tables for attention calculation and preference prediction. Abundant preliminary studies and experimental evaluation support the effectiveness.

### Strengths
1. Preliminary study is available. Authors provide experimental evidence supporting that using a shared embedding for attention calculation and preference prediction can impair performance due to the varying magnitudes and conflicting gradients. Furthermore, the authors examine the linear projection solutions of current methods, noting that the constrained embedding size may hinder the effectiveness of linear projection for decoupling. 

2. Clarity. The paper presents its ideas with remarkable clarity, making it not only easy to follow but also engaging for the reader.

3. Experiments. Comprehensive experiments demonstrate the effectiveness of DARE. Various behavioral sequence models, including DIN, SDIM, ETA, and TWIN, are compared. A thorough analysis of attention and representation capabilities, as well as efficiency tests, is presented.

### Weaknesses
1. Applicability. This work aims to decouple attention and representation embeddings for sequence modeling. I wonder if the proposed solution in Section 2 can be extended to more scenarios. When the attention mechanism is not used in certain sequential models, the suggested method does not apply and, therefore, cannot benefit these models. The paper does not explore the limitations of the approach when applied to models without an attention mechanism, which is a significant gap in the analysis. For instance, how would this decoupling strategy perform in simpler sequence models like recurrent neural networks (RNNs) or even basic Markov models, where attention is not a component? The lack of investigation into these scenarios limits the generalizability of the proposed method.

2. Inconsistent Solution without Novelty. The proposed solution is too straightforward-setting separate embedding tables for attention and representation. This is not novel and does not align with the findings, although the separate embeddings can resolve the conflicting gradient and are not simply a linear projection. In my view, authors should go beyond linear projection. For instance, a linear projection-based decoupling method that addresses the gradient issue can be applied to small embedding sizes in recommendation systems, rather than reverting to separate embeddings, a very basic solution. The authors should have explored more sophisticated decoupling techniques, such as using different non-linear transformations or adaptive learning rates for the attention and representation embeddings, rather than simply resorting to separate embedding tables. The lack of exploration of more advanced techniques undermines the novelty of the approach.

3. Storage Complexity. Authors only provide the inference efficiency. However, for large-scale recommender systems, a separate embedding table can occupy exceptionally large storage space. The authors should provide a detailed analysis of the memory footprint of their approach, including the additional storage required for the separate embedding tables. This is crucial for evaluating the practical feasibility of the method in real-world large-scale recommendation systems. The paper lacks a quantitative assessment of the increased memory requirements, which is essential for practical deployment.

### Questions
1. What are potential application scenarios other than sequential models with attention and representation?

2. To what extent would DARE increase the storage complexity? I believe it would be doubled.

### Soundness
3

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
3

### Summary
The paper addresses a key limitation in existing long-sequence recommendation models, which struggle to balance the learning of attention and representation with a single set of embeddings. To tackle this, the authors introduce the Decoupled Attention and Representation Embeddings (DARE) model, which separates these two processes with distinct embeddings. Experiments show that DARE not only improves the accuracy of correlated behavior searches but also boosts efficiency, reducing embedding dimensions and accelerating the search by 50% without significant performance loss.

### Strengths
The definition of the problem is very clear.
The research perspective is quite innovative.

### Weaknesses
The definition and explanation of the gradient issue are one-sided, and the motivation and the logic of the method are not clear. For example, why do the impact of different modules on embedding gradients must be ‘equal-magnitude’ and ‘consistent’? How do imbalance-magnitude and inconsistent gradients degrade recommendation performance? Additionally, the connection between the proposed method and the target problem is weak. For example, why does the embedding decoupling approach help mitigate the gradient issues? Overall, the logic and the motivation of the main idea need to be illustrated clearly.

### Questions
1.	Why are the gradients from \textbf{attention} significantly smaller than those from \textbf{representation} in Fig. 2? And why is this imbalance undesirable during training (e.g., does it contradict theoretical derivations)? It is necessary to provide a theoretical analysis here.
2.	The definition of conflicts between attention and representation is quite vague. The cancellation of gradients during backpropagation cannot be explained merely by the sign of the angle. Could you supplement this with the merged gradient values or in other ways to illustrate the degradation caused by conflicts to the embeddings?
3.	What are the consequences of these gradient issues? Do they lead to the failure of representation learning or the malfunction of certain modules? Would you add a presentation or explanation of the outcomes of the mentioned problem？
4.	How does DARE solve the aforementioned gradient issues (gradient magnitude imbalance and gradient conflicts)?
5.	The embedding dimension shown in Figure 6 should reach at least 200 to be consistent with the analysis in lines 208-213. Additionally, the analysis here can be summarized as: linear mapping requires a large embedding dimension to be effective, but increasing the embedding dimension leads to the dimensional collapse problem in recommendation systems. How does DARE address this problem? Does it only work effectively in low dimensions, or does it solve the dimensional collapse problem and work under any embedding capacity?
6.	How are the embeddings between the two modules in DARE aligned? Why can the weights used to measure attention embeddings be directly utilized for representation embeddings?
7.	The concept of Mutual Information （MI） is repeatedly mentioned in the experimental section, so it is necessary to introduce its calculation method. Moreover, this concept is already used in Figure 1, but it is not explained there. The connection between MI and the problem analyzed in this paper (Section 2) needs careful and thorough clarification.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper focuses on long-sequence recommendation models. It first identifies a problem in existing models where a single set of embeddings struggles to handle both attention and representation learning, leading to interference. Initial attempts to address this using linear projections from language processing failed. Then it proposes the Decoupled Attention and Representation Embeddings (DARE) model. This model uses two distinct embedding tables for attention and representation, which are initialized and learned separately. Extensive experiments on public datasets and an online system show its effectiveness.

### Strengths
1. The paper clearly identifies a crucial problem in long-sequence recommendation models. The analysis of the interference between attention and representation learning due to shared embeddings is comprehensive.

2. The extensive experiments on public datasets (Taobao and Tmall) and an online advertising platform are a major strength. The comparison with a wide range of baselines, including state-of-the-art models like TWIN and its variants, demonstrates the superiority of the DARE model. The evaluation metrics used, such as AUC, NDCG, and representation discriminability measures, provide a comprehensive assessment of the model's performance.

### Weaknesses
1. The performance on the short-sequence modeling using the Amazon dataset was marginal. This suggests that the DARE model may not be as effective in short-sequence scenarios, and more research is needed to understand its applicability in different sequence lengths. Additionally, the experimental setup for some baselines, like DIN, required adjustments to fit the long-sequence context, which may introduce some biases in the comparison.

2. There are some results that lack a satisfactory explanation. For instance, on the Tmall dataset with embedding dimension = 16, TWIN (w/o TR) outperforms TWIN, which was unexpected. The authors could not convincingly explain this result, leaving a gap in the understanding of the model behavior under different dataset characteristics.

3. In the exploration experiment, although the data is somewhat persuasive, some special cases or edge cases may not be fully covered. For example, it is uncertain whether different gradient relationships will occur under certain combinations of specific categories or user behavior patterns. Moreover, there is no further in-depth analysis of the reasons behind why it is nearly two-thirds of the cases, which may cause readers to have some doubts about the universality of the conclusion.

### Questions
How was the decision made to use two distinct embedding tables for attention and representation? Were there any other alternative architectures considered and why were they rejected?

In the DARE model, how sensitive is the performance to the choice of embedding dimensions for attention and representation? Have different combinations been explored and what are the trade-offs?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper has focused on the interference between search and aggregation stages in the long-sequence recommendation. The authors first conducted some preliminary experiments and found the unbalanced and adverse gradients brought by the two stages. Inspired by such findings, they propose to adopt two individual embedding sets for the two stages, respectively, which may alleviate the conflicts between the two stages. The experiments on two public datasets validate that the proposed method can benefit the previous two-stage method, i.e., TWIN, and achieve SOTA performance.

### Strengths
- S1. This paper is well-written and -structured, which is easy to follow and understand.
- S2. This paper is well-motivated, where the motivation is from an interesting preliminary study.
- S3. The proposed method is simple but effective.

### Weaknesses
 - W1.  I can understand the results and conclusion from the preliminary study, but the detailed process of the preliminary study is not clear. For example, I wonder how to calculate the gradients from the attention and representation to the embeddings. Specifically, it's unclear how the gradients are isolated and measured given that both attention and representation modules likely contribute to the final loss, and how these gradients are then attributed to the respective embedding tables. The process of synchronizing the two embedding tables also needs further clarification.
- W2. Only one metric is revealed in the experiments. GAUC and Logloss are often two common metrics in CTR prediction tasks. Thus, I suggest the authors add more metrics.
- W3. The number of filtered behaviors, i.e., K in this paper, is often important to the two-stage method, but no related hyper-parameter experiment is conducted. It's crucial to understand how the performance of the proposed method varies with different values of K, as this parameter directly controls the amount of information passed from the search stage to the aggregation stage. Without this analysis, it's difficult to assess the robustness of the method.
- W4. It seems that the proposed method can only fit the two-stage method, such as TWIN. However, there still exist many one-stage works [1], which may illustrate that the two-stage method has not been the optimal solution. If so, the value of this paper is limited.

### Questions
- Q1. Why the performance of TWIN-V2 is worse than TWIN, which does not align with the original paper? Are there some differences in experimental settings?

All of my other questions are included in the weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3
