# Causal Graph Transformer for Treatment Effect Estimation Under Unknown Interference

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Networked interference, also known as the peer effect in social science and spillover effect in economics, has drawn increasing interest across various domains. This phenomenon arises when a unit’s treatment and outcome are influenced by the actions of its peers, posing significant challenges to causal inference, particularly in treatment assignment and effect estimation in real applications, due to the violation of the SUTVA assumption. While extensive graph models have been developed to identify treatment effects, these models often rely on structural assumptions about networked interference, assuming it to be identical to the social network, which can lead to misspecification issues in real applications. To address these challenges, we propose an Interference-Agnostic Causal Graph Transformer (CauGramer), which aggregates peers information via $L$-order Graph Transformer and employs cross-attention to infer aggregation function for learning interference representations. By integrating confounder balancing and minimax moment constraints, CauGramer fully incorporates peer information, enabling robust treatment effect estimation. Extensive experiments on two widely-used benchmarks demonstrate the effectiveness and superiority of CauGramer.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses causal inference in situations involving interference, where both the interference graph and the summary function are unknown (note that the interference graph is distinct from a social network). The authors assume that interference occurs within an 
L-order neighbor network, where peer information can be aggregated using a graph transformer. They utilize a cross-attention mechanism to capture complex sequential interference representations. Additionally, they apply techniques such as regularization to balance the distribution of confounders across control and treatment groups, and they leverage moment conditions to account for confounding and mitigate model misspecification.

### Strengths
The paper has a well-defined research focus on causal inference under interference with unknown interference structures.

The experiments conducted are engaging and effectively demonstrate the proposed methods.

 Overall, the paper is well-organized and presented.

A few sections lack clarity, as noted in my specific questions.

### Weaknesses
The paper’s primary contribution—clearly distinguishing the interference graph from the social network—is highly valuable. However, if the approach is limited to neighboring nodes only, it risks undermining this motivation. Specifically, restricting the interference to L-order neighbors, while computationally convenient, may not capture the full complexity of real-world interference patterns, where influence can propagate beyond immediate connections. On the other hand, if this limitation is not imposed, the computational complexity becomes quadratic in the number of nodes when using transformers, which poses feasibility issues for large graphs, making the method impractical for many real-world networks. 

Additionally, a category of related work on non-iid data, particularly doubly robust estimators, IPW, and representation-based methods, appears to be missing from the review. Including this literature could provide a more comprehensive view of the field. Specifically, methods that explicitly address network interference, such as those using doubly robust estimation or targeted maximum likelihood estimation, should be discussed [1, 2, 3].

Since doubly robust estimators represent the state-of-the-art for causal parameter inference and have advantages over IPW-based methods, adding at least one of these approaches as a baseline would further strengthen the comparisons [1, 2, 3]. The lack of comparison with these methods makes it difficult to assess the relative performance of the proposed approach.

### Questions
Could you provide some additional justification or intuition for how the bridge function makes the residual independent of x?
	Line 377: You mention, “If the model is correctly specified and properly optimized…” Could you elaborate on how you ensure the model is both correctly specified and optimized?

Also, why is it necessary for the residual to be independent of t?	Section 4.3 could benefit from a bit more clarity in its presentation.

Many of the baselines, as far as I’m aware, assume a fixed and known exposure mapping. In your experiments where the interference graph is unknown, or the graph is known but the summary function is not, could you clarify how comparisons are made with these baselines that assume the exposure map is already known?

line 414 and 415: In the presence of unmeasured confounders, we will collect negative control variables and embed them into the Eqs. (11) and (12)

Could you elaborate on this aspect of your technique? line 481: We conduct 10 replications to report (mean±std) results. Given that this is a relatively small number of trials, could you provide some reasoning behind this choice?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
CauGramer leverages a Graph Transformer architecture with cross-attention to aggregate peer information within an L-order neighborhood.  This approach addresses the limited receptive field of traditional GCNs.  The model learns interference representations for both features and treatments, using cross-attention to capture complex interactions between units.  To mitigate confounding bias, the model incorporates confounder balancing and minimax moment constraints, further enhancing the robustness of the treatment effect estimation.  The authors extend the model to handle unmeasured confounders by incorporating negative control variables.

### Strengths
Addresses a significant limitation: The paper directly tackles the crucial challenge of estimating treatment effects in networked data with unknown interference structures and aggregation functions, a problem neglected by many existing methods.

Novel architecture: CauGramer's architecture is innovative, combining the strengths of graph neural networks and transformers to capture complex interference patterns. The use of cross-attention is particularly insightful for broadening the receptive field.

Robustness: The incorporation of confounder balancing and minimax moment constraints significantly improves the robustness of the model. The extension to handle unmeasured confounders further enhances its practical applicability.

Comprehensive evaluation: The empirical evaluation is thorough, covering various scenarios and comparing against multiple strong baselines.

### Weaknesses
NA, see the questions

### Questions
Can you elaborate on the computational complexity of CauGramer, especially compared to other graph neural network and transformer-based methods? Are there any specific strategies employed to mitigate the computational burden, such as approximation algorithms or distributed training?

How sensitive are the results to the choice of the L-order neighborhood parameter in CauGramer? What is the impact of choosing too small or too large an L value? Is there an optimal way to select this parameter?

The paper employs the Wasserstein distance (IPM) to measure the discrepancy between treatment and control group representations. Have you considered other divergence measures (e.g., Jensen-Shannon divergence, Kullback-Leibler divergence)? How would the results change with different choices of divergence measures?

You address the issue of unmeasured confounders by using negative controls. What is the impact on the performance of CauGramer if the negative control variables are not perfectly valid or are missing? How robust is the model to misspecification in the negative control variables?

What are the current study's limitations, and what are your plans for future work? Specifically, are there any plans to explore alternative architectures, different attention mechanisms, or more sophisticated methods for handling unmeasured confounders?

In some sense, I think this paper's theoretical is somehow a bit thin. I am curious whether we could give your method some theoretical guarantee.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper "Causal Graph Transformer for Treatment Effect Estimation under Unknown Interference" introduces an innovative Interference-Agnostic Causal Graph Transformer (CauGramer) framework for causal effect estimation under unknown network interference. This approach captures complex interference information across nodes through an L-order graph attention mechanism combined with cross-attention, without relying on a known interference graph. The model incorporates confounder balancing and minimax moment constraints to achieve robust causal effect estimation.

### Strengths
1.The study introduces a novel approach by addressing causal inference from the perspective of an unknown interference graph. The combination of L-order graph attention with cross-attention for modeling interference information.
2.The paper is well-structured.
3.Causal inference under unknown interference graphs is a significant challenge in network data analysis, and the outcomes of this study provide a reference for future research.

### Weaknesses
1.In Table 1, which includes i.i.d. data, the title "Causal Networked Data" may not be fully accurate. Perhaps "Observational Data" would be more accurate.
2.On line 129, "Representation" could be more accurate formatted in lowercase as "representation."
3.The method appears to rely on an unconfoundedness assumption, yet latent confounders are mentioned later, violating this assumption.
4.In Section 4.1, Ma & Tresp’s work is not necessarily limited to first-order interference.
5.There are multiple instances of quotation mark formatting errors in lines 375, 449, 487, and 516, among others.
6.How did you address latent confounders in their approach?
7.When network interference is unknown, how does the proposed method differ from existing work (e.g., Rf1-Rf3)?
8.The work lacks a description of the number of layers (L) and attention heads (M) used.
9.While the paper compares CauGramer with several mainstream methods, it lacks a detailed discussion of specific methods for unknown interference graphs (e.g., Rf1-Rf3).
Rf1: Sävje, Fredrik, Peter Aronow, and Michael Hudgens. "Average treatment effects in the presence of unknown interference." Annals of Statistics 49.2 (2021): 673.
Rf2: Hoshino, Tadao, and Takahide Yanagi. "Causal inference with noncompliance and unknown interference." Journal of the American Statistical Association (2023): 1-12.
Rf3: Lin, Xiaofeng, et al. "Treatment Effect Estimation Under Unknown Interference." Pacific-Asia Conference on Knowledge Discovery and Data Mining. Springer Nature Singapore, 2024.

### Questions
1.In the COVID case study, where transmission primarily occurs through contact, how can interference occur in the absence of a direct link? Could you clarify potential mechanisms of transmission under such conditions?
2.Could you clarify why the final output \( r_x^{(L)} \) is used as the input to the first layer of the peer-treatment representation network, specifically \( r_t^{(1)} = r_x^{(L)} \)?
3. Please explain the statement: "we simulate unmeasured confounding by removing features."
4. The paper states that the relationship between peer-treatment \( t_{Pi} \) and outcome \( y_i \) remains confounded by the common causes \( r_i \), leading to biased estimates of peer and total effects. Moreover, the peer-treatment \( t_{Pi} \) is unknown. In the main text, it is mentioned that \( r = r_x \oplus r_t \). Could you clarify why \( r_i \) acts as a confounder for both \( t_{Pi} \) and \( y_i \)?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study aims to estimate treatment effects in the presence of unknown interference (including unknown network and summary mechanism). To achieve this goal, it proposes a method named CauGramer, which uses the transformer to address unknown interference.
However, some important studies and baseline methods for unknown interference are ignored.

### Strengths
1. The presentation is clear.
2. A new method is proposed.
3. Identifiability of total effect is given, which provides insight for studying unknown interference.
4. Experiments are conducted to verify the proposed method.

### Weaknesses
# Weakness
1. Some important studies are ignored. Unknown interference has been addressed in many existing works [R1-R4]. These works have excellent contributions for unknown interference, but they are ignored by authors. Authors should introduce the difference between their work and these works. Specifically, the authors add a paragraph in the related work section comparing their approach to [R1-R4], highlighting key differences in methodology, assumptions, and capabilities. It is concerning that all of these relevant studies were overlooked, suggesting a significant gap in the authors' understanding of the existing literature on unknown interference.

2. As introduced in Weaknesses 1, unknown interference is not a new challenge in causal inference, because there are some existing methods [R1~R4] that focus on this issue. 
The novelty of this study might be limited. It might be helpful if the authors could introduce the limitations of these existing methods and how this study addresses them. Specifically, what limitations of prior methods does CauGramer address? What new capabilities does it enable? The authors should clarify how their approach goes beyond simply combining existing techniques and demonstrate a clear advancement in the field.

3. In addition, existing methods [R1-R4] have a more relaxed assumption for unknown interference. They do not require any network information, whereas the proposed method requires network information, i.e., $A$. This reliance on network information is a significant limitation, as it restricts the applicability of the method in scenarios where such information is not available or unreliable. The authors need to justify this requirement and discuss its implications.

4. For experiments, authors need to compare with the existing methods for unknown interference. In the current version, authors did not compare with [R1-R4]. The authors can add [R1], [R3] and [R4] as baselines in their experiments, following the implementation details.  [R1] can create a network (you can only take the edges among different nodes) when the input graph is a complete graph or an initial graph, i.e., $A$ in the authors' setting. Then, you can apply G-HSIC on the network created by [R1] as a baseline. [R3] and [R4] can directly work when you give or not give an input graph. [R2] can be ignored, as it is not a learning method. The lack of comparison with these established methods makes it difficult to assess the true performance and contribution of the proposed approach.

5. In definitions 1 and 3, as well as equations (1) and (2), should the $t$ in the right of '=' be 1, as the treatment is a binary value, i.e., 1 or 0.

### Questions
# Questions:
1. Why do you not introduce the existing works [R1-R4], which have excellent contributions for unknown interference? Can you introduce the difference between your works and these works?  What limitations of prior methods does CauGramer address? What new capabilities does your method enable?

2. [R1-R4] can work when the network information is totally unknown. Can the proposed method work when the network information is totally unknown? How does the performance change in this case?

3. In definitions 1 and 3, as well as equations (1) and (2), should the $t$ in the right of '=' be 1 instead of $t$?

4. For more details, please see Weakness.



# Reference
[R1] Bhattacharya, et al.  Causal inference under interference and network uncertainty.  UAI 2019

[R2] Sävje, et al. Average treatment effects in the presence of unknown interference. The Annals of Statistics 2021

[R3] Mayleen, et al. Staggered rollout designs enable causal inference under interference without network knowledge. NeurIPS 2022.

[R4] Lin, et al. Treatment effect estimation under unknown interference. PAKDD 2024.

### Soundness
2

### Presentation
3

### Contribution
2
