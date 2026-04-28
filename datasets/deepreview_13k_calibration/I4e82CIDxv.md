# Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
We introduce methods for discovering and applying \textbf{sparse feature circuits}. These are causally implicated subnetworks of human-interpretable features for explaining language model behaviors. Circuits identified in prior work consist of polysemantic and difficult-to-interpret units like attention heads or neurons, rendering them unsuitable for many downstream applications. In contrast, sparse feature circuits enable detailed understanding of unanticipated mechanisms. Because they are based on fine-grained units, sparse feature circuits are useful for downstream tasks: We introduce \shift{}, where we improve the generalization of a classifier by ablating features that a human judges to be task-irrelevant. Finally, we demonstrate an entirely unsupervised and scalable interpretability pipeline by discovering thousands of sparse feature circuits for automatically discovered model behaviors.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces sparse feature circuits as a causal network built from human-interpretable features, rather than neurons. The author discuss how to quantify the Indirect Effects (IE) of steering or patching individual neurons on model behaviors and propose approximations to extend this approach to models with many components. 

Through experiments on the Gemme2-2B and Pythia-128M models, they demonstrate that a relatively low number of sparse features, compared to neurons, can interpret model behaviors with high fidelity. Building on these findings, the authors present the SHIFT framework, which enables the surgical removal of unintended features to prevent them from affecting model classification performance. While the framework involves some human judgment, it highlights that these Sparse Auto-Encoder (SAE) features are effective representations of concepts that can be manipulated to control model behaviors. Finally, the authors propose an unsupervised circuit discovery pipeline, moving from next-token clustering to zero-ablating features, to identify the most important feature circuits.

### Strengths
* This paper is well-motivated and articulated;
* The studied subject is of good importance to the NN interpretability domain;
* The experiment setup is clear and the results are promising;
* The idea has sound novelty.

### Weaknesses
 * SAE features are vast, and identifying specific circuits among those formulated by these features can be challenging.
* SAE errors cannot be fully interpreted, while they play an important role in making sparse feature circuits. This is ongoing work to train more proficient SAEs, but it should be discussed more in the paper regarding how to perform surgical edits on such errors.
* I suspect that the circuits may only correlate with certain features. Simply removing gender-related features and observing a drop in classification performance is not universally convincing as a causal intervention approach; additional experiments on other features are needed to support this claim;
* Trivial concerns: 1) several typos: 283: fair; 201: produce; 492: succession; 2) citation formatting errorsat line 95-96; 3) line 454-457 needs more clarity.

### Questions
* Can you add explanations regarding the efficiency of the sparse feature circuit finding with the vast amount of possible feature circuits with respect to neurons'?
* Can you help better understand how to interpret SAE errors at part of the sparse feature circuits?
* Can you share your thoughts on extended experiments on more feature ablating studies and how would the results be?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents Sparse Feature Circuits, a method to discover interpretable causal graphs within language models (LMs) based on sparse, human-interpretable features. Leveraging sparse autoencoders (SAEs), the authors identify feature circuits that reveal causally implicated components in model behaviors, contrasting with prior work focused on more complex components like attention heads and neurons. The technique allows for targeted interventions to refine model predictions by eliminating task-irrelevant features, as demonstrated in a new method called SHIFT. SHIFT enables selective feature removal, improving classifier generalization without requiring disambiguating labels. The paper’s contributions include a scalable pipeline for automatic discovery of interpretable circuits, and applications in improving model behavior by editing these circuits.

### Strengths
- By focusing on sparse feature circuits instead of larger, polysemantic components, this approach introduces a new level of granularity in LM interpretability. The use of SAEs is particularly innovative, as it allows for fine-grained, interpretable features that are scalable and can be applied across thousands of discovered behaviors, improving previous interpretability efforts that were limited by reliance on human-defined hypotheses. 

- The SHIFT technique, designed to improve model generalization by removing unintended signals, offers a practical, actionable method for handling spurious features. The fact that SHIFT can operate without disambiguating labels and apply human judgment to identify spurious features highlights its practical utility for real-world model refinement, especially in settings where unintended biases are a concern. 

- The unsupervised interpretability pipeline for discovering feature circuits across various model behaviors (including grammatical tasks like subject-verb agreement) is impressive. It enables scalable, automatic generation of feature circuits, addressing the labor-intensive nature of previous interpretability work. This unsupervised aspect expands the approach’s applicability across domains and data types, making it a versatile contribution. 

- The paper presents quantitative evaluations on interpretability metrics such as faithfulness and completeness for both feature and neuron circuits, providing objective assessments of the interpretability advantage of sparse features.

### Weaknesses
 - The method relies on human judgment to determine which features are spurious, which may lead to inconsistencies across applications or datasets. The framework lacks a clear evaluation on the repeatability and consistency of human-selected spurious features in SHIFT, especially when applied by different users or in different contexts. Including a quantitative study or qualitative analysis on the consistency of feature selection across different users or scenarios would strengthen the reliability of SHIFT’s results and enhance confidence in its practical application. For instance, assessing inter-annotator agreement or providing a standardized checklist could help mitigate inconsistencies. 

- Although SHIFT leverages human judgment for feature interpretation, this reliance could hinder scalability in complex or high-dimensional models, as manual inspection becomes increasingly challenging. The paper does not provide clear guidelines on how to efficiently scale this process for larger models or more diverse tasks. Specifically, the paper lacks details on how the number of features to be inspected scales with model size and task complexity, and whether the manual inspection process can be parallelized or automated in any way. The absence of a clear protocol for feature selection makes it difficult to assess the practical applicability of SHIFT in real-world scenarios.

- The method’s success is heavily tied to the availability and quality of sparse autoencoders (SAEs). If the SAEs are suboptimal, the interpretability and causal circuit discovery might suffer, particularly if they fail to capture meaningful latent structures. This dependency on pretrained SAE quality raises questions about the method’s consistency and applicability across different model architectures or under domain shifts. The paper does not explore the sensitivity of the results to different SAE training parameters or architectures, which could impact the reliability of the discovered feature circuits. A more thorough analysis of the impact of SAE quality on the overall method is needed.

- The faithfulness and completeness metrics for feature circuits are assessed primarily on grammatical tasks like subject-verb agreement, which may not generalize to more complex language tasks that involve nuanced semantic understanding or context-sensitive behaviors. This limited evaluation could affect confidence in the generalizability of the results. Expanding evaluations to include complex, semantically challenging tasks (e.g., multi-turn dialogue or reasoning tasks) would provide stronger evidence of the method’s robustness. The paper should also consider evaluating the method on tasks that require more sophisticated reasoning and contextual understanding, such as question answering or text summarization, to demonstrate its broad applicability.

### Questions
1. How do the authors ensure consistency in identifying spurious features across different annotators or applications? Are there any plans to standardize the interpretation criteria?

2. Could the authors clarify how the performance of SAEs affects the interpretability and effectiveness of feature circuits? Have they tested their approach on varying SAE architectures to assess robustness? 

3. For large-scale models with complex circuits, what optimizations or techniques do the authors recommend to maintain interpretability while managing the increased number of features?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a method for discovering interpretable sparse feature circuits in LLMs using sparse autoencoders (SAEs). While previous mechanistic interpretability work focused on polysemantic neurons, MLP attention heads, this paper shows how to decompose model behaviors into monosemantic, human-interpretable features. The authors validate their approach through three key contributions: (1) a circuit discovery method combining SAEs with linear approximations of indirect effects, (2) a debiasing application called SHIFT that ablates task-irrelevant features, and (3) demonstration of scalable, automated circuit discovery for large sets of model behaviors.

### Strengths
Strengths:

Successfully addresses a core challenge in MI: finding and scaling interpretable units of analysis. 


- Empirical Results:

Comprehensive subject-verb agreement circuits reveal clear compositional structure (e.g., distinct pathways for handling relative clauses vs. prepositional phrases)
Human evaluation shows significantly better feature interpretability (81.5 for BiB circuit features vs 36.0 for neurons)
SHIFT achieves 93.1% profession accuracy while reducing gender bias to near chance (52.0%)

- Validation & Reproducibility:

Thorough ablation studies on all key parameters (SAE width, layer selection, manipulation coefficients). Clear comparison against neuron-based approaches showing consistent advantages.

### Weaknesses
Weaknesses:

- No code and data released yet. 

- Theoretical Analysis:

In terms of theoretical weaknesses, some formal characterization of when SAE features capture meaningful concepts vs memorized patterns would strength the paper. 


Most of these are noted in the paper but it's worth mentioning it here, SAE training requires significant compute (2 billion tokens) with potential instability (dead features). The current implementation limited to decoder-only models (Pythia-70M and Gemma-2-2B). 

- Evaluation Scope:

Subject-verb agreement circuits focus on relatively simple grammatical phenomena and this might not be an issue with scale but no mention of anything more complex in the paper.

### Questions
- The paper shows strong results with linear approximations of indirect effects. Have you checked when/why these approximations break down? This seems especially relevant for early layers where you note integrated gradients improves accuracy.

- For the automated circuit discovery, how robust are the discovered clusters to different choices of projection dimension and clustering hyperparameters?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a method that automatically discovers "sparse feature circuit", defined as subgraphs of a large language model that satisfy two desiderata: (1) responsible for implementing a model behavior, and (2) human-interpretable. As a by-product, the authors propose SHIFT, a method that removes non-causal features (e.g. gender bias) from a classifier. Finally, the authors scale their method to thousands of automatically discovered behaviors from SAEs, hinting at the possibility of automated interpretability.

### Strengths
- This paper is very well written, and provides enough background on SAEs to motivate their approach. Each component of the method is also presented very clearly.
- This contribution is very timely. Most prior works on mechanistic interpretability suffers from two pitfalls: (1) Inability to understand / interpret dense MLP layers [1], and (2) what's next after interpretability. This work provides satisfactory answers to both, by (1) using more recent approaches of SAEs to disentangle polysemanticity and (2) using interpretable features to debias a classifier / remove non-causal relationships from it.
- Owning to the scalability of SAEs, this method can be scaled to automatically discover thousands of behaviors to billion scale parameters. The authors also supplement this ability with an interactive website, which offers many interesting insights and improves accessibility of this research.

[1] How does GPT-2 compute greater-than?: Interpreting mathematical abilities in a pre-trained language model, https://arxiv.org/abs/2305.00586

### Weaknesses
 - While this approach is scalable with respect to model size and a broad range of behaviors, using this approach would still require contrastive sample pairs that is hard to get and / or define for tasks such as long-form generation and algorithmic reasoning. Specifically, for long-form generation, defining what constitutes a 'positive' or 'negative' example for a specific behavior is non-trivial. For instance, if the behavior is 'generating creative metaphors', it's difficult to automatically create pairs where one has a metaphor and the other doesn't, without human intervention. Similarly, for algorithmic reasoning, creating contrastive pairs that isolate specific reasoning steps is challenging, as the space of possible reasoning paths is vast and complex. Nevertheless, I believe this work represents a step in the right direction, but it'd be great for the authors to discuss this type of dataset limitations and future directions to automatically construct contrastive pairs for more challenging tasks.
- As the authors have mentioned, most of these results are qualitative, and it would be great to establish a more quantitative benchmark to supplement the other interesting behaviors that the authors were able to mine from their unsupervised approach. The current qualitative analysis, while insightful, lacks a systematic way to compare the discovered circuits across different behaviors or models. A quantitative benchmark could involve metrics that measure the 'sparsity' of the discovered circuits, their 'causal influence' on the target behavior, or their 'robustness' to adversarial perturbations. Without such metrics, it's difficult to objectively assess the effectiveness of the proposed method and compare it to alternative approaches.

### Questions
See weaknesses

### Soundness
3

### Presentation
4

### Contribution
4
