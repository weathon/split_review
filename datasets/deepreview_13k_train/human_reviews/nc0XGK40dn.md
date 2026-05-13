# Never Forget the Basics: In-distribution Knowledge Retention for Continual Test-time Adaptation in Human Motion Prediction

- Decision: Reject
- Scores: 6, 5, 3

## Abstract
This paper presents a novel approach to addressing the underexplored challenge of human pose prediction in dynamic target domains that simultaneously contain in-distribution (ID) and out-of-distribution (OOD) data. Existing test-time adaptation (TTA) techniques predominantly focus on OOD data, neglecting the fact that ID data, which closely resembles the training distribution, is often encountered during real-world deployment, leading to significant degradation in ID performance. To address this, we introduce In-Distribution Knowledge Retention (IDKR), a continual TTA framework designed to preserve critical knowledge about ID data while adapting to unseen OOD sequences. Our method introduces an ID-informative subgraph learning strategy that leverages the structural characteristics of human skeletal data to compute a structural graph Fisher Information Matrix (SG-FIM). Unlike prior work, IDKR simultaneously considers both node and edge features in the skeletal graph, with edge features, representing the invariant bone lengths between parent-child joint pairs, being essential for maintaining structural consistency across poses. These edge features are key to extracting reliable SG-FIM parameters, enabling the model to retain parameters critical for ID performance while selectively updating those needed for OOD adaptation. Extensive experiments on multiple benchmark datasets demonstrate that IDKR consistently outperforms state-of-the-art methods, particularly in scenarios involving mixed ID and OOD data, setting a new standard for robust human pose prediction in dynamic environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel approach to Test-Time Adaptation (TTA) for human pose prediction that addresses real-world scenarios where both in-distribution (ID) and out-of-distribution (OOD) motion data appear in the deployment domain. To manage this dual data presence, the authors propose an In-Distribution Knowledge Retention (IDKR) mechanism, designed to retain crucial ID information while adapting to OOD sequences. The method leverages the Graph Information Bottleneck framework to extract the most informative subgraph for ID data, filtering out irrelevant elements and enhancing focus on essential structures. A Structural Graph Fisher Information Matrix (SG-FIM) is then employed to identify key model parameters that contribute to ID sequence prediction. These parameters are selectively preserved during adaptation through a regularization term integrated into the TTA optimization, ensuring robust ID performance amidst OOD adaptation. Experimental results indicate that IDKR outperforms existing methods in diverse real-world scenarios, underscoring its effectiveness and applicability.

### Strengths
1. Novel Framework for Mixed ID and OOD Data in Human Pose Prediction (HPP): The paper introduces a pioneering framework that explicitly addresses the coexistence of in-distribution (ID) and out-of-distribution (OOD) data in human pose prediction tasks, a novel scenario largely overlooked by existing test-time adaptation (TTA) methods. 
2. Innovative In-Distribution Knowledge Retention (IDKR) Mechanism: The proposed IDKR mechanism is a standout contribution, using ID-informative subgraph learning combined with a Structural Graph Fisher Information Matrix (SG-FIM). This approach identifies and retains key ID-specific parameters while adapting to OOD data, ensuring that critical ID information is preserved during adaptation. This dual capability of adaptation and retention is a novel approach that improves robustness and accuracy in complex, mixed-domain scenarios.
3. Extensive and Competitive Evaluation: The paper provides thorough experimental evaluations, demonstrating that IDKR significantly outperforms state-of-the-art HPP models, particularly in non-stationary environments with both ID and OOD data. This strong empirical performance indicates the method’s effectiveness and potential for future HPP tasks that encounter dynamic and evolving domain shifts.

### Weaknesses
The authors propose a TTA approach that aims to address a “realistic” scenario where both ID and OOD data coexist in dynamic target domains. However, the paper could benefit from more concrete real-world examples and specific use cases to demonstrate the relevance and feasibility of this framework. Adding examples of real-world applications where dynamically shifting ID and OOD data are common, would strengthen the justification for this method and better highlight its practical impact.

The concept of domain shifts is also somewhat underdeveloped in the context of skeletal data, where inputs are limited to pose estimates. The paper would be clearer with a more explicit definition of domain shifts, including measurable criteria for detecting these changes within skeletal data and an explanation of how these shifts affect model performance. Clarifying how the model differentiates ID and OOD data based solely on skeletal data, or whether additional information sources (like RGB image) would be beneficial, would help reinforce the proposed approach’s robustness in real-world scenarios.

Another area for enhancement is in addressing the inherent variability of future pose predictions. Predicting future skeletal positions involves multiple potential outcomes, but the paper approaches predictions deterministically. To provide a fuller picture of the model’s capabilities, discussing how the method might handle multiple plausible future paths could improve its applicability. Additionally, exploring the model’s predictive accuracy over extended time frames and including a graph showing MPJPE across longer intervals would clarify the scope and limitations of the predictions. This would offer more insight into how effectively the model sustains accuracy over time, adding depth to the performance analysis.

The statements on Line 49 and Line 52 reference prior research developments but lack specific citations to support the claims. Adding relevant citations here would provide necessary context.

### Questions
1. Real-World Use Cases: Could you provide specific real-world scenarios where the coexistence of ID and OOD data is encountered in dynamic target domains for HPP? Clear examples would help solidify the relevance of the approach.
2. Domain Shift Criteria: How are domain shifts defined and detected solely from skeletal pose data? Could you clarify measurable criteria used for distinguishing domain changes and explain if additional data sources would improve domain differentiation?
3 . Handling Prediction Ambiguity: How does the model manage multiple plausible future poses from skeletal data, given the non-deterministic nature of human motion? Would incorporating probabilistic or multi-path prediction improve the model’s robustness?
4. Long-Term Predictive Accuracy: Could you provide a temporal analysis showing how MPJPE error evolves over extended adaptation periods? A graph of MPJPE over time would clarify the model’s performance in long-term deployments.

# UPDATE (After Discussion Period)

I would like to thank the authors for providing such a detailed response. However there are few points that still remains a matter of concern for me.

- Lack of Explicit Validation for Real-World Relevance (A1): While the authors provide compelling real-world examples, these are largely anecdotal. A stronger case would involve showcasing datasets or use cases where such scenarios are observed, along with empirical validation of the method’s performance in those contexts.

- Scope and Limitations of Deterministic Prediction (A3.1): Although the authors justify focusing on deterministic prediction as the standard for TTA-based HPP, this limits the broader appeal of the paper. Probabilistic approaches, which capture the inherent variability of human motion, are gaining traction in the field. While extending the model to support probabilistic predictions may be beyond the scope of this paper, a discussion of how the proposed framework could adapt to such paradigms in future work would strengthen its contribution.

- Empirical Performance and Long-Term Predictions (A3.2): The inclusion of long-term prediction results is a positive step, but the reported increase in MPJPE over time highlights limitations in handling motion variability for extended horizons. This suggests that while the method outperforms baselines, it may not generalize as effectively for long-term predictions in real-world applications.

While the paper presents a novel and valuable contribution to HPP and the authors have addressed many concerns effectively, **the work does not fully meet the standards of a Strong Accept hence I would like to retain the original rating**.

### Soundness
3

### Presentation
4

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
This paper frames the Human Pose Prediction (HPP) task in a continual-Test Time Adaptation (C-TTA) scenario where it accounts for maintaining the performance on both ID and OOD data, which it argues matches the target distribution and  to prevent model degradation on ID sequences while selectively adapting to OOD data. It employs a subgraph learning strategy and a Structural Graph Fisher Information Matrix (SG-FIM) to preserve essential parameters for ID data by leveraging the structural consistency in human skeletons. Experiments are shown on the Humans 3.6m, CMU-Mocap and GRAB datasets and showed improvement when compared to 3 other TTA and C-TTA methods.

### Strengths
1. Using Fischer Information as a regularizing technique is an interesting way of approaching the problem of HPP under Continual Test Time Adaptation. 
2. The experiments conducted are comprehensive and covers a wide set of works not just related to HPP but also from traditional TTA literature like TENT, CoTTA etc.

### Weaknesses
 1. The paper looks incremental in nature: there is limited novelty in the proposed HPP setting. The motivation of the paper seems to come from that fact that there is continuous change in the target domain. When a person performs some activity, it is fair to assume that the environment does not change drastically which may bring in significant domain shift (rain, fog etc.). Some plots in Figure 3 (S+- and C+-) seems to illustrate this.

 2. The fischer information matrix designed here is essentially able to act as a regularizer since it serves as a prior of human anatomy (ex: invariant bone lengths). Several previous works exist in Human Pose Estimation literature which propose strong priors to capture a plausible set of human poses. It seems FIM was chosen as a straight-forward choice - there is a possibility this method may fail in scenarios where there are significant pose variations/self-occlusons due to heavy reliance on just invariant features. In scenarios where poses vary significantly even within the ID distribution (e.g., differing postures or activities within the same subject), SG-FIM’s reliance on just invariant features may lead to suboptimal adaptation as it overemphasizes preserving parameters linked to structural constraints rather than flexible, adaptive knowledge which is the main motivation behind any C-TTA setting.

 3. The loss terms in 9 and 10 don't particularly seem novel: test-time alignment of human poses based on spatial and temporal features is a well-known technique. I would like to see if this was introduced based on some specific enhancement in mind to complement the GIL Learning approach or just as additional regularizers between frames.

 4. The authors introduce specific setups like Setup-C+− and Setup-S+− to simulate mixed ID and OOD domains by including only 10% of the source domain data as ID in the target domain. However, these ratios look somewhat arbitrary - testing with different ID-to-OOD ratios would provide more insight.

 4. Typos present: 800.9 PCK@150 in Table 3.

### Questions
Please refer to the weaknesses section.

### Soundness
3

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
The paper introduces a framework called In-Distribution Knowledge Retention (IDKR) to tackle test-time adaptation (TTA) for human pose prediction (HPP) in dynamic environments. Typically, TTA methods adapt models to out-of-distribution (OOD) data but fail to maintain performance on in-distribution (ID) data, leading to issues when ID and OOD data coexist during inference. In order to address this issue, the key idea of the IDKR framework is to preserve ID-specific knowledge while adapting to OOD data. 

The authors propose representing human pose sequences as a graph, where the IDKR framework identifies and retains ID-relevant information through an ID-informative subgraph learning technique. IDKR then computes a Structural Graph Fisher Information Matrix (SG-FIM) based on both node and edge features within this subgraph, to identify the model parameters which are essential for ID data. Two self-supervised losses are finally introduced, allowing the model to adapt effectively to new data while minimizing deviation in ID-specific parameters.

Experiments are conducted on 3 datasets: Humans3.6M, CMU MoCap, and GRAB. Results are shown across multiple scenarios (different subjects/motion/datasets) including cases where ID data is present during testing.

### Strengths
1. By specifically addressing the coexistence of ID and OOD data during adaptation, the paper tackles a practical gap in current TTA methods for HPP, which often focus solely on OOD adaptation.

2. Experiments demonstrate the method's effectiveness across multiple settings, showing clear performance improvements over state-of-the-art methods.

### Weaknesses
 **Method**

1. The exact details of ID-subgraph extraction is unclear. The authors mention that it is implemented by learning binary masks which are then used to mask the over the node and adjacency matrices. There is no mention of how binary constraints are imposed on these masks. Specifically, it is unclear how the method ensures that the learned masks result in a valid subgraph, i.e., that the selected nodes and edges form a connected component or a meaningful subset of the original graph. The lack of explicit constraints on the mask could lead to disconnected or fragmented subgraphs, which might not be informative for retaining ID knowledge.
2. In equation 3 the masks are learned by minimizing a binary classification loss where all instances have the same label - why will the masks be incentivized to learn anything? The loss function seems to lack a mechanism to differentiate between different parts of the graph, making it unclear how the model identifies and retains ID-relevant information. The use of a single label for all instances suggests that the model might not be learning a meaningful representation of the subgraph, but instead converging to a trivial solution.
3. In relation to equation 3, the posterior of the subgraph $q(\mathcal{Z}|\mathcal{G})$ is not defined. The paper does not specify the form of this distribution, making it difficult to understand how the subgraph is sampled or optimized during training. Without a clear definition of the posterior, it is challenging to evaluate the validity of the proposed approach.
4. Section 3.3 discusses Fisher information, but equation 4/5 calculate it w.r.t the inputs (node and edge features) and not the parameters. How do the dimensions match up? How exactly are these node and edge features calculated? The paper does not provide sufficient detail on how the Fisher information is computed with respect to the model parameters, given that the equations are defined in terms of input features. This discrepancy raises concerns about the validity of the approach and its ability to identify parameters essential for ID data. Furthermore, the calculation of node and edge features is not sufficiently detailed, making it difficult to reproduce the results.
5. The authors introduce two self-supervised losses which are weighted according to an exponential function, with higher weights for larger timestamps (or more recent frames). Equation 9 defines the time-weighted spatial loss which calculates the consistency of predicted bone lengths across frames - why does the timestamp play a role here given that bone length should remain consistent across time? Similar argument holds for equation 10. Overall the impact is unclear.


**Clarity**

I found the paper to be lacking in clarity.


**Experiments**

Going from the setup $S^+$ to $S^{+-}$ and from $C^+$ to $C^{+-}$ the difference in performance is consistent for both the baseline H/P-TTP and IDKR. This implies that both methods are handling ID data similarly - is the claim that IDKR is better at mixed TTA valid?

### Questions
1. Please make the learning process clearer. 
- What are the masks? 
- How do you define the distribution over graphs?
- How is the Fisher Information computed, especially, what are the node and edge features?

2. Ablation study having no weights in the losses.

### Soundness
2

### Presentation
2

### Contribution
2
