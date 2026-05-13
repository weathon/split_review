# Conformal Structured Prediction

- Decision: Accept
- Scores: 6, 5, 6

## Abstract
Conformal prediction has recently emerged as a promising strategy for quantifying the uncertainty of a predictive model; these algorithms modify the model to output sets of labels that are guaranteed to contain the true label with high probability. However, existing conformal prediction algorithms have largely targeted classification and regression settings, where the structure of the prediction set has a simple form as a level set of the scoring function. However, for complex structured outputs such as text generation, these prediction sets might include a large number of labels and therefore be hard for users to interpret. In this paper, we propose a general framework for conformal prediction in the structured prediction setting, that modifies existing conformal prediction algorithms to output structured prediction sets that implicitly represent sets of labels. In addition, we demonstrate how our approach can be applied in domains where the prediction sets can be represented as a set of nodes in a directed acyclic graph; for instance, for hierarchical labels such as image classification, a prediction set might be a small subset of coarse labels implicitly representing the prediction set of all their more fine-descendants. We demonstrate how our algorithm can be used to construct prediction sets that satisfy a desired coverage guarantee in several domains.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a framework for conformal structured prediction i.e., conformal prediction in the structured prediction setting. The proposed framework outputs structured prediction sets that achieve marginal or PAC coverage guarantees while minimizing prediction set size. In the context of a set of nodes in a directed acyclic graph, the prediction set as a small subset of coarse labels corresponds to the prediction set of fine-grained descendants of the coarse labels. The paper presents empirical analysis of the approach in three domains to demonstrate the performance of their approach.

### Strengths
1. The paper is well-organized for the most part.
2. The paper is technically sound in its description of problem formulation and the marginal and PAC guarantees.
3. Construction of prediction sets in the structured prediction setting and in the context of nodes in a directed acyclic graph is an important problem.

### Weaknesses
1. Missing discussion of important related work [1, 2]: I believe the paper misses citing and comparison with important related work on conformal risk control [1]. [1] considers hierarchical image classification in ImageNet similar to the paper and controls the graph distance between nodes. Additionally, RAPS method in [2] is a conformal prediction method that introduces regularization to encourage smaller and stable sets, and is worth comparing to given the focus of the paper on reducing average set size.
2. The empirical evaluation can certainly benefit from more analysis. In the current form, the contribution and significance of the method are not demonstrated very clearly:
    - It is hard to understand the utility of the method without comparison with more baselines. I believe doing this is especially possible for the marginal guarantees. Qualitative comparison of the prediction sets will also help demonstrate the utility of structured prediction sets. I see the paper discusses one example in the main text, however there is certainly value in adding more examples in this case (also mentioning the error level used for standard conformal prediction and other details for fair comparison).
    - Following from above, I appreciate Table 1 in the paper as it helps understand the influence of hyperparameters better. I would suggest adding similar examples for other datasets as well.

3. The motivation of the paper is not very clear in the beginning and only becomes clearer as the method and examples are discussed later in the paper. While the introduction has sufficient details about the method, I would suggest making the motivation for structured prediction sets clearer early on.




**Minor comments:**
1. L60: parameter $\tau$ has not been defined and referenced early I believe without sufficient context here.
2. Similar comment for Figure 2. The caption makes reference to $\tau$, whereas the notation has not been introduced earlier in text or in the caption.
3. L306: typo/incomplete -> (2)
4. L416-417: possibly missing word after ‘values’; “ in contrast, for the PAC guarantee, coverage for all values within one standard deviation...”

[1] Anastasios Nikolas Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, and Tal Schuster. Conformal Risk Control. International Conference on Learning Representations, 2024.

[2] Anastasios Nikolas Angelopoulos, Stephen Bates, Michael Jordan, and Jitendra Malik. Uncertainty Sets for Image Classifiers using Conformal Prediction. International Conference on Learning Representations, 2021.

### Questions
How should $m$ be selected in practice? From the experiments, this selection appears as an important choice for the quality of prediction sets, however the paper lacks discussion on this aspect.

### Soundness
3

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
The authors propose conformal structured predictions which addresses the interpretability issue of conformal predictions when the output set is complex. Their algorithm also differs from existing algorithms as in conformal structured predictions the search space over $\tau$ is not monotone anymore. This approach can be applied to tasks where the output space can be represented as a directed acyclic graph and has a hierarchical structure. The authors provide formal coverage guarantees using PAC and marginal coverage and evaluate their approach in numbers predictions with MNIST digits, ImageNet classification and temporal Q&A.

### Strengths
* It is an interesting problem, particularly how best to use the external structure of the labels to generate a better 'curve', i.e. recall at given output size.
* The experimental setups were quite interesting, e.g. MNIST with number ranges.
* The proposed method seems to extend well to DAG spaces (beyond trees). Though I suppose it is still restricted to DAG instead of Graphs to sum up the probs of final leaf nodes.

### Weaknesses
* I would love to see a baseline where we dont use the structure at all and instead rely on regular P/R curve characteristics. Does the AUC of this model behave better? It is not clear to me as such.

* Even if we do use the external structure and forced to only predict internal nodes in the DAG (as opposed to arbitrary set of leaf nodes), it would still be useful to understand the P/R curve look significantly different with the proposed models. There are plenty of baselines where we can do prediction on internal nodes in addition to leaf nodes.

### Questions
(see above)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper "Conformal Structured Prediction" introduces a novel framework to extend conformal prediction methods to complex, structured output spaces. Conformal prediction typically provides sets of labels with a high probability of containing the true label, giving a quantified uncertainty. However, for tasks involving structured or hierarchical outputs—such as text generation, image classification with hierarchical categories, or question answering with date ranges—traditional conformal methods produce prediction sets that can be large and hard to interpret.

The authors propose a method to generate interpretable structured prediction sets using a conformal predictor that works within a directed acyclic graph (DAG) representing the label hierarchy. This approach maintains coverage guarantees while reducing prediction set complexity. The paper introduces algorithms for efficiently determining the smallest structured prediction set that meets a specified confidence level, and it adapts these methods to provide both marginal and Probably Approximately Correct (PAC) guarantees.

The authors demonstrate the utility of their approach through experiments on MNIST digits, hierarchical ImageNet classification, and a question answering dataset focused on years as answers. The results show that their framework achieves desired coverage rates while keeping prediction sets concise and interpretable.

### Strengths
1. Extension of conformal prediction to structured outputs using DAGs, combining conformal prediction with hierarchical representations.
2. Rigorous theoretical development with both marginal and PAC coverage guarantees, validated through experiments in diverse domains.
3. Generally well-organized with clear explanations and helpful visual aids, making complex concepts accessible.
4. Addresses an important gap, potentially impacting applications that require structu

### Weaknesses
1. While the paper’s application of conformal prediction to structured outputs is valuable, similar approaches have been explored in hierarchical classification and structured prediction. For instance, previous works have used hierarchical structures (e.g., DAGs or trees) to improve interpretability in label prediction. The paper could benefit from a more thorough comparison to these existing methods, as well as a deeper explanation of what sets its approach apart. Highlighting any unique technical advancements in how the proposed framework constructs prediction sets in hierarchical settings (e.g., advantages of the DAG-based approach) would further clarify its contributions.

Set-Valued Prediction in Hierarchical Classification with Constrained
Representation Complexity. Mortier et al. (2022): This work focuses on hierarchical classification with constrained set-valued predictions, utilizing hierarchical label spaces in which classes are structured in a directed acyclic graph (DAG) or tree. It emphasizes creating interpretable predictions that adhere to hierarchical constraints, much like structured conformal prediction but without formal coverage guarantees.


2. The experiments are limited to specific domains (MNIST digits, ImageNet, and SQuAD). Although these domains represent a variety of structured prediction tasks, they are relatively controlled environments and may not fully reflect the challenges of deploying conformal structured prediction in more complex real-world applications. For instance, the framework’s performance on prediction sets for multi-label classification or in contexts with high label ambiguity (e.g., complex multi-class categorization in medical or legal documents) remains untested.

Deploying conformal structured prediction in a healthcare setting, particularly for diagnostic tasks with hierarchical or multi-label structures (e.g., identifying conditions or diseases from imaging data or lab results), would offer insights into the model's reliability and interpretability under more variable, high-stakes conditions. This field often requires nuanced coverage guarantees and interpretability to support clinical decision-making.

Real-world document classification often involves hierarchical categories (e.g., legal documents, financial reports) and multi-label classifications. Testing in this setting could reveal how well the model scales with complex, unbalanced label hierarchies, providing additional insights into its generalizability to larger, noisy datasets that are typical in business and legal contexts.

3. The paper assumes that the label hierarchy can be represented by a DAG, which works well for hierarchical classification but may be restrictive for tasks with overlapping or cyclical dependencies. In complex scenarios where relationships between classes are non-hierarchical or not acyclic, this assumption may not hold, potentially limiting the framework’s applicability to structured outputs with more intricate dependencies.

4. The inclusion of PAC guarantees is a strong point, but the differences between the marginal and PAC guarantees could be better explored. The PAC guarantee is inherently conservative, and the experiments demonstrate that it leads to larger prediction sets in some cases. However, there is little analysis of scenarios where a PAC guarantee might be more beneficial than a marginal guarantee, or vice versa, depending on the task or risk tolerance.

### Questions
1. How does the proposed method for conformal structured prediction fundamentally differ from or improve upon prior hierarchical prediction approaches? 

2. The framework assumes that the label space is represented by a DAG. How does this assumption impact generalizability to label structures that are non-hierarchical, cyclical, or have overlapping dependencies?

3.  Integer programming (IP) can be computationally intensive, particularly for large DAGs. Have you measured or benchmarked the runtime performance and scalability of the IP formulation, especially in tasks with larger label hierarchies?

4. Could you elaborate on practical scenarios or domains where marginal coverage versus PAC coverage would be preferable? How should a practitioner decide between the two guarantees in real-world settings?

5. Have you considered comparing this approach to other recent extensions of conformal prediction tailored to structured outputs or complex tasks (e.g., those applied to natural language or image data)?

6. How sensitive is the framework to the hyperparameter  m
(the maximum number of nodes in the prediction set)? Is there a recommended method for tuning 
m based on the domain or task?

### Soundness
3

### Presentation
3

### Contribution
2
