## Human Reviewer 1

### Summary
This work presents MIRA, a monitorability measure for neural networks based on feature space analysis. The proposed method works via input perturbations, and the Mahalanobis distance is used to measure the discrepancy between perturbed inputs and the training set in the feature space. Several experiments validate the proposed method.

### Strengths
The provided visualizations are clear and effectively demonstrate the alignment between the MIRA score and the "separability" of trained neural network features. This work also sheds light on the importance of monitorability in the deep neural network literature.

### Weaknesses
The connection between Section 3.2 and Section 3.3 is weak. Section 3.2 gives Definition 1 regarding abstract monitorability, while Section 3.3 provides an empirical metric serving as the main contribution of this paper. However, there is no guarantee nor clear theoretical connection establishing how the method given in Section 3.3 relates to Definition 1.

Furthermore, the data distribution $P_{in}$ in Definition 1 is somewhat ambiguous. Intuitively, what would be an example of $P_{in}$? If $P_{in}$ is the training distribution, then if the model achieves near-zero training loss, the $\ell$-monitorability becomes meaningless. On the other hand, if $P_{in}$ is supposed to be a mixture between training and (out-of-distribution) test distributions, how is this distribution reflected by only the training set (potentially with perturbation)?

### Questions
Please see the weaknesses above. Minor questions:

- The formulation in line 175 is very similar to some kind of adversarial robustness. Are there any links between Equation (2) and other adversarial robustness metrics?
- What is $\tilde{x}$ in line 187?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper proposes the concept of monitorability, whereby the inference maybe assigned a score that showcases whether said inference maybe trusted. The authors claim that existing uncertainty estimates are based on well-trained networks and features. Additionally, OOD estimation generally separates ID from OOD without addressing the correctness of ID sample inference. The authors propose MIRA, a method to monitor neural network predictions.

### Strengths
1. The paper is well written with a clear logical flow.

2. The results are showcased on a variety of datasets.

### Weaknesses
**Incorrect motivation and claims**:

The paper makes some fundamentally incorrect claims:

1. (Line 12) *Although out-of-distribution (OOD) detection and uncertainty estimation have been widely studied, they often rely on the assumption that neural networks learn high-quality features.*: This is false. Early-stopping is a well known method in UQ that explicitly states that network training must stop long before overfitting.

2. (Line 87) *However, it is important to note that misclassifications may also occur for ID inputs, which is a distinct scenario not directly addressed by OoD detection.*: True. But the application that does look at ID classification and OOD detection is Open set recognition [1].

3. (Line 57) *To the best of our knowledge, this is the first work to formally define and quantify monitorability as a distinct property of neural networks.*: True in the sense of using the word monitorability. But there are a large number of simple UQ metrics (margin sampling, entropy), and more complex internal state-based gradient metrics [2, 3] that can monitor the outputs and provide an alternative score.

[1] Recent Advances in Open Set Recognition: A Survey

[2] Probing the Purview of Neural Networks via Gradient Analysis

[3] Counterfactual Gradients-based Quantification of Prediction Trust in Neural Networks

**Paper positioning**: Without referencing and comparing against prediction trust, UQ, open set recognition, it is hard to evaluate the contributions and results in the paper.

### Questions
Please note that my rating is based on the weaknesses above. I would be willing to reevaluate my rating if I have missed something fundamental about the concept of monitoriability that is not covered by UQ, prediction trust, or open set recognition.

### Soundness
1

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
5

---

## Human Reviewer 3

### Summary
This paper attempts to relax the implicit assumption that most black-box OOD and UQ approaches make, which is that models have learned semantically meaningful features. In practice, if this assumption does not hold, it may lead to undetected errors. The authors formalize the concept of monitorability and an associated MIRA score, which is intended to highlight inference errors at the internal model layer level, rather than merely relying on a black-box assessment. The score quantifies this property by applying norm-bounded input perturbations and measuring the separability of resulting feature representations using Mahalanobis distance. MIRA is validated across computer vision, tabular, and NLP tasks by demonstrating correlation with OOD detection performance.

The paper addresses an important problem for safety-critical applications and makes a valuable theoretical contribution, however, the work has limitations: (1) MIRA's layer-dependency lacks principled aggregation to provide an overall monitorability estimate, the perturbation range selection requires domain-specific threshold choices, and the validation has some circularity.

### Strengths
This paper has the following strengths:

Formalizing monitorability as a distinct property of networks is valuable and contributes to trustworthiness and explanability that is sought from today's models (I think integrating formal methods and verification, as pointed out as extensions, is an interesting direction too).

The use of Mahalanobis distance with the surprisal score normalization (Eq 3) appropriately handles dimensionality differences, which would have been a concern if not addressed.

Experiments span three data modalities: vision, tabular data, and NLP with diverse architectures, demonstrating consistent correlation with OOD detection performance.

MIRA captures monitoring of internal model semantics which has a  potential to be applied independently of any specific detection method.

### Weaknesses
There are two primary weaknesses of the approach:

The primary weakness of the proposed score is that it is layer l dependent and there is a lack of aggregation of this score at the layer level to provide an overall aggregate estimate of how the effect of cascading layers affects overall monitorability of the network as a whole. Specifically, the missing multi-layer analysis has huge architectural dependence and implications. The experimental results show comparisons for the monitoring methods across different classes, but not across different layers. The authors should: (1) provide empirical evidence and theoretical justification for selecting a specific layer (e.g., final layer) as representative or (2) develop a principled aggregation scheme that accounts for the cascading effects of these networks. Investigating how MIRA scores vary across different layers within the same network would be a valuable insight.

The claim of not requiring external OOD is a lucrative one, however, it is undermined by the requirement for a user-defined distribution for perturbation magnitudes p(epsilon) in definition 2 on page 4. While Appendix B.6 proposes a threshold-based heuristic (selecting epsilon to reduce accuracy below pre-determined thresholds), this approach introduces domain-dependent choices (50% for some datasets, 15% for CIFAR-100, and 75% for NLP) without principled guidance on how this should be selected in practice. Since perturbation magnitudes may vary significantly across test domains, the lack of a principled selection strategy for p(epsilon) represents a critical gap. The authors should provide: (1) a theoretical or empirical justification for p(epsilon) choices and/or (2) an adaptive method for automatically determining p(epsilon) across datasets.

### Questions
On page 2, the alignment of the Mahalanobis distance with the softmax classifier remains specific to this type of classifier. Does this assumption hold for other types of classifiers? The broader question is about the generalization of the method to other model architectures.

On page 4, the perturbation delta(x,epsilon) needs to move x toward the decision boundary -> how is this perturbation selected in practice? Taking this further, in definition 2 on the same page, p(epsilon) is a user-defined probability distribution over perturbation magnitudes. It is not clear as to how the user should select this probability distribution. Are there any insights here that can be leveraged? 

In practice, the magnitude of perturbations is not known and hence this is a critical assumption. So, while no external OOD data is required, the perturbation magnitude distribution, which is assumed to be user-specified, is unknown and a principled method to obtain this should be explored further and formalized. While section 4.2 on page 5 provides details on the use of FGSM to obtain perturbations, it is not clear as to why the authors "consider this as a better choice."

The authors state on page 4 that MIRA is not intended for runtime detection, but rather as a pre-deployment evaluation metric. It is not clear, then, how this is used downstream at runtime. Can models be explicitly trained to improve their MIRA scores?

The evaluation creates a somewhat circular argument: the MIRA metric is validated by showing it correlates with detection performance, but monitorability is itself defined as detectability. I understand there is a lack of baselines in the space, however, is there a theoretical justification that can be provided here to back up the results? Addressing the multi-layer analysis would help.

No error bars or confidence intervals are provided for MIRA scores or OOD detection performance. Given the sensitivity shown in Table 8, understanding variance is important.

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4