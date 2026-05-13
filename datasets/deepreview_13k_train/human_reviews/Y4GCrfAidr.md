# Multiway Multislice PHATE: Visualizing Hidden Dynamics of RNNs through Training

- Decision: Reject
- Scores: 6, 5, 3, 5, 6

## Abstract
Recurrent neural networks (RNNs) are a widely used tool for sequential data analysis, however, they are still often seen as black boxes of computation. Understanding the functional principles of these networks is critical to developing ideal model architectures and optimization strategies. Previous studies typically only emphasize the network representation post-training, overlooking their evolution process throughout training. Here, we present Multiway Multislice PHATE (MM-PHATE), a novel method for visualizing the evolution of RNNs' hidden states. MM-PHATE is a graph-based embedding using structured kernels across the multiple dimensions spanned by RNNs: time, training epoch, and units. We demonstrate on various datasets that MM-PHATE uniquely preserves hidden representation community structure among units and identifies information processing and compression phases during training. The embedding allows users to look under the hood of RNNs across training and provides an intuitive and comprehensive strategy to understanding the network's internal dynamics and draw conclusions, e.g., on why and how one model outperforms another or how a specific architecture might impact an RNN's learning ability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
## Summary
This paper aims to visualize the internal dynamics of RNNs. The authors claim that the previous papers merely achieve it via post-training, overlooking their evolution process. To this end, they proposed MM-PHATE, which is a graph-based embedding using structured kernels across the multiple dimensions spanned by RNNs: time, training epoch, and units. Experiments show that the proposed method helps users to understand RNNs.

### Strengths
## Strength
1. The visualization results look cool.

2. The motivation is clear and the understanding of RNN is meaningful.

3. The analyses are comprehensive.

### Weaknesses
## Weakness
1. The codes and datasets are missing, limiting the reproducibility. 

2. Recommend generalizing the proposed method to more recent sequential models like transformers. 

3. The statistical information of the datasets are missing.

### Questions
see weakness

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
3

### Summary
This paper proposes a technique to visualize the hidden states of RNNs while training and across units. They extend PHATE and M-PHATE to account for within sequence time-steps, in addition to epoch-level time steps. They compute kernels over a 4-way tensor that creates two types of edges: (1) edges that look at the same unit evolving over the course of a sequence and epochs, and (2) edges that look at how different units are related to each other for a fixed timestep/epoch. The intrastep edges form block-diagonal matrices and the interstep edges create off diagonal diagonal matrices. The utility of the proposed representation is evaluated on two datasets (Area2Bump, Human Activity Recognition dataset). They demonstrate that looking at the inter and intra-step entropy provides insights into the loss and when models may begin to overfit. They also show that visualizations obtained are better than TSNE/PCA/etc.

UPDATE: I thank the authors for their feedback. I have read the other reviews and responses as well. While some of my concerns were addressed, I do not feel this paper is quite read for acceptance and thus will maintain my score. I encourage the authors to take into account some of the suggestions made by reviewers for expanding their analyses.

### Strengths
- *Interesting Problem.* Understanding the learning dynamics of RNN representations is an interesting problem. It will enable additional insights into improving their architectures. Though transformers are certainly more popular these days, I think that RNNs are still useful in some areas, so this is a useful task.

- *Some Nice Insights.* The author's demonstration of the relationship between the entropy of the representation and loss/over-fitting and related experiments are interesting observations, especially considering existing hypotheses for what happens when learning RNN representations.

### Weaknesses
 -  *Novelty.*  This paper builds off of PHATE and MMPhate to introduce a visualization model specifically for RNNs, which accounts for the sequential nature of the data. This involves some changes to the tensor and kernel to include additional edges amongst the sequence steps, in addition to the epoch steps. I do not see this as significant novelty.

- *Weak baselines/Limited Datasets.* The authors limit their analysis to one tasks (classification), on two datasets. The visualizations compared are to tsne/pca/isomap, which are known to be insufficient for neural network representations. I would have liked to seen more recently comparisons as well. I feel that the authors are missing some citations and recent work. 

- *Utility/Practicality*. While the visualizations are interesting, I am not persuaded that they are particularly useful or would generalize across different datasets, sizes, or variations in architecture. Nor am I convinced the additional computational time/memory to compute these visualizations would be useful if I did.

### Questions
Please see weaknesses.

- Can the authors please expand upon the utility of the visualizations and entropy based plots? I found them visually interesting but I could not see myself utilizing them when training or comparing amongst models? 

- Can the authors clarify a bit how different length sequences are represented in T. My understanding is that T is n×s×m×p, so is there padding for the different length s, or is this a non-issue for the formulation of K? 

- The two datasets evaluated on appear to be classification datasets. Is the author's formulation useful for other tasks? Please describe what insights could be derived from the MMPhate visualizations there. 

- I noticed that the authors did not compare to [1], which has been used in the past to analyze the dynamics of neural networks. I bring it up because it may be a stronger baseline to the TSNE/PCA. 

[1] SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics and Interpretability

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
2

### Summary
This work introduces Multiway Multislice PHATE (MM-PHATE), an innovative visualization method designed to explore the internal dynamics of recurrent neural networks (RNNs). This method employs a graph-based embedding with structured kernels to capture the multiple dimensions of RNNs, including time, training epochs, and units. Through experiments on various datasets, the authors demonstrate that MM-PHATE effectively preserves the community structure of hidden representations and highlights distinct phases of information processing and compression during training.

### Strengths
- This paper is clearly written, well organized. 
- Experiments can effectively reflect the intended objectives of the model.

### Weaknesses
 - The technical contribution is incremental. The authors merely add the time step dimension to the M-PHATE and do not make any additional adaptation for RNN. 
- MM-PHATE is closely related to M-PHATE, but the experiment lacks analysis of M-PHATE.

### Questions
What is the relationship between the visualization of MM-PHATE and the visualization of M-PHATE at each time step?

### Soundness
2

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
- This paper introduces MM-PHATE, a novel visualization method designed to analyze hidden dynamics of RNNs during training by capturing both temporal and epoch-wise changes. 
- The method extends PHATE by incorporating a multiway multislice graph representation that preserves community structure among hidden units while tracking their evolution across time steps and training epochs. 
- Through extensive experiments on neurological and human activity recognition datasets, the authors demonstrate that MM-PHATE can identify distinct phases of information processing and compression.

### Strengths
- The paper presents a comprehensive approach to visualizing RNN dynamics that simultaneously captures both temporal and training evolution, addressing a significant gap in existing visualization methods. 
- The authors provide thorough empirical validation through entropy analysis that reveals meaningful patterns in model behavior, particularly in identifying different learning phases and community structures among hidden units. 
- The method demonstrates practical utility by successfully differentiating between different RNN architectures (LSTM, GRU, Vanilla RNN) and providing insights into their learning behaviors without requiring additional validation data.

### Weaknesses
 - The authors fail to provide rigorous mathematical foundations, particularly in connecting entropy changes to information bottleneck theory and distinguishing between meaningful compression and information loss. 
- The method suffers from significant scalability issues due to its $O(n^2sm^2)$ complexity, and the necessary sampling of temporal data may compromise the analysis of RNN dynamics. 
- The validation of their method lacks quantitative metrics for evaluating preserved structures and performance correlations, while experimental evidence is limited to small-scale networks and only two datasets. 
- Claims of superiority over baseline methods (PCA, t-SNE) are not sufficiently supported by objective metrics or theoretical guarantees.

### Questions
1. The authors claim that MM-PHATE identifies information processing and compression phases. However, this appears to be based only on entropy change observations. Could you provide mathematical/theoretical proof of how this relates to information bottleneck theory?

2. How do you differentiate between useful information compression and mere information loss in your entropy analysis?

3. Regarding the claimed correlation between MM-PHATE visualization and model performance, what specific visualization characteristics quantitatively correlate with which performance metrics?

4. Has the correlation between visualization patterns and model performance been validated across different architectures and datasets? If so, how consistent are these correlations?

5. The paper claims to preserve community structure well. How do you define and measure "well-preserved community structure"? What metrics validate this preservation?

6. The authors emphasize the analysis of RNN temporal dynamics as a key objective yet use sampling (e.g., reducing 600-time steps to 100 in the Area2Bump dataset) due to memory constraints. How do you moderate this substantial temporal sampling with the goal of preserving temporal dynamics, particularly given RNNs' inherent purpose of capturing sequential dependencies? Could you analyze information loss at different sampling rates, empirical validation that your chosen sampling strategy is optimal, and quantitative metrics demonstrating that temporal patterns are preserved?

7. Concerning the visualizations across LSTM, GRU, and Vanilla RNN, how can you verify that visualization differences genuinely reflect internal model behavior differences rather than artifacts of the visualization method?

8. Specifically in Appendix D.3, how do you distinguish whether the observed 'chaotic pattern' in Vanilla RNN represents actual learning instability rather than limitations of the visualization approach?

9. The paper claims that PCA and t-SNE "failed to capture" certain aspects. How do you verify that the uncaptured information is indeed significant? What evidence supports that MM-PHATE's additional patterns reflect meaningful model dynamics?

10. How does the diffusion kernel accurately capture RNN temporal dependencies? What theoretical guarantees can you provide for this?

11. What is the theoretical justification for using different methods (α-decay vs. Gaussian) for intrastep and interstep affinity calculations in the multiway multislice kernel design?

12. What assumptions are made about the geometric/topological properties of the manifold formed by RNN hidden state dynamics?

13. The authors claim that "changes in entropy coincided with shifts in model performance" (line 323, p.6). However, this claim requires rigorous validation. Could you provide correlation coefficients between entropy changes and performance metrics at each time step, along with statistical tests validating their significance?  Furthermore, can you explain why these entropy changes should reflect performance shifts? 

14. Can you derive statistical bounds for the sampling effects? What convergence guarantees can you provide in the finite sample regime?

15. Given the $O(n^2 s m^2)$ memory complexity, what theoretical approaches could improve this computational burden while maintaining the method's effectiveness?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper extends the M-PHATE framework for visualization of the inner time-dependent dynamics of RNNs across training epochs. Example visualizations are provided for two datasets, while also providing insights gained through these visualizations.

### Strengths
- Well detailed presentation of the proposed method as well as prior work.
- Application to two datasets and presentation of gained insights.
- The ability of this method to detect "important" neural units in RNNs (Fig 4c,d).

### Weaknesses
The method itself is lacking in novelty as it simply extends the kernel-matrix slicing framework set up in M-PHATE by adding another slicing dimension in the kernel matrix. One could argue that once the slicing framework is established, users could choose to slice across any number of dimensions - epochs, RNN time index, network depth, etc. 

In light of the above, I evaluate the scientific contribution of this paper only in terms of the insights gained through visualizations of RNN dynamics. While insights were presented from the generated visualizations on two datasets, many times these were post-hoc explainations. Some phenomena was only observed in one of the two datasets. Rigorous testing for the generality of these insights is missing.

### Questions
1. Line 461-469: This paragraph attempts to address the mismatch in the insight mentioned the previous paragraph (information compression). It presents a hypothesis that the Area2Bump dataset is too complex for the size of LSTMs considered. I believe, it is important to test this hypothesis by training wider/deeper LSTMs. This insight is only valid if you're able to see a similar information compression stage when training with Area2Bump dataset with a sufficiently large model.
2. I find the ability of the presented methods to find "high-information" neural units that are "important" for the task, as presented in figure 4, to be very good for gaining confidence in this method's ability. Repeating this analysis and showing the same for the HAR dataset would be helpful in estabilishing that this phenomena is valid across datasets.

### Soundness
3

### Presentation
3

### Contribution
2
