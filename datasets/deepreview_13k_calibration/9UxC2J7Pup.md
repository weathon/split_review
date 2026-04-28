# Understanding Nonlinear Implicit Bias via Region Counts in Input Space

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 3, 6

## Abstract
One explanation for the strong generalization ability of neural networks is implicit bias. Yet, the definition and mechanism of implicit bias in non-linear contexts remains little understood. In this work, we propose to characterize implicit bias by the count of connected regions in the input space with the same predicted label. Compared with parameter-dependent metrics (e.g., norm or normalized margin), region count can be better adapted to nonlinear, overparameterized models, because it is determined by the function mapping and is invariant to reparametrization. Empirically, we found that small region counts align with geometrically simple decision boundaries and correlate well with good generalization performance. We also observe that good hyper-parameter choices such as larger learning rates and smaller batch sizes can induce small region counts. We further establish the theoretical connections and explain how larger learning rate can induce small region counts in neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper motivates and studies a novel generalization measure for neural networks: the number of connected regions in the input space. The paper first describes current challenges in connecting generalization to geometric properties of neural networks, and then introduces the proposed generalization measure. Extensive experiments assess the correlation between a small number of connected regions and generalization. Finally, the paper concludes by providing a theoretical link between the region count (in the training data) and the learning rate of (S)GD used during training.

Update: changed my score to 6.

### Strengths
This is an interesting paper to read. I would like to highlight the following strengths:

- Novel (empirical) measure for generalization: To the best of my knowledge, the proposed measure (input space connected region count) has not been studied theoretically or experimentally before, and the experimental findings are interesting. Namely, the paper finds that, for various configurations, the proposed measure (or, better, an estimate of it) seems to correlate well with the generalization gap.
- Extensive experiments: The experimental analysis is very thorough, including many datasets, models and hyperparameter choices.
- Theoretical result on the relation between region count and learning rate: Theorem 1 (partially) explains the empirical finding that a larger learning rate is associated with a smaller region count (and, as a result, smaller generalization gap). I found the result simple yet creative.

### Weaknesses
I believe that the community will find the findings and observations of this paper interesting. However, I identified a few areas where the paper could improve substantially:

- Omission of important details from introduction: The paper almost exclusively studies a specific approximation of the input space region count, which measures the number of prediction changes along *a line that connects two points from the training data*. However, this detail is not mentioned in the introduction, but only much later. Furthermore, many readers, while going through the paper for the first time, might confuse the introduced measure with the number of linear regions of the neural network. While this is clarified later in the paper (pg. 3), a short explanation in the introduction would be helpful.

- Weak/misleading section on "Motivation" (Section 3): I found Section 3 to be entirely misleading. The norm and margin quantities considered have **no reason** to be correlated with generalization for a ResNet18. First, they are not properly normalised, which is acknowledged later, so I do not see the reason for considering them in the first place. Second, there is no clear understanding that SGD on a ResNet will necessarily increase a specific notion of margin or minimise a specific norm. If someone wants to assess such connections, they should probably focus on simpler models (such as homogeneous neural networks) and control for many confounders. I understand and agree with the general point of this section (i.e., that accurate generalization measures based on the parameters of a "practical" network may be challenging to find in practice), but I found the motivating experiments problematic. I insist on this, since this section is the starting point of the paper and might mislead many readers. I would suggest being more precise in this section. Further concrete comments on this section: 1) Equation in line 172 is missing the distribution with respect to the expectation is taken. This is crucial, as it is not clear whether it applies to train or test data (it should be train). 2) It would be good to define the input-space margin which you mention in line 188 for the first time.

- Insufficient theoretical link to generalization: While I understand this is mainly an experimental paper, I was disappointed that there is no discussion on how the proposed measure can perhaps be related to improved generalization. For example, there is no mention of the self-evident property that a very small region count is undesirable (for region count equal to 1, we obtain a trivial predictor). An example of a satisfying result would be that (S)GD biases the model to implicitly minimise $R(\theta)$ under the constraint that all the train points are classified correctly together with perhaps more constraints from the hyperparameters (akin to results that exists for gradient descent on homogeneous neural networks and margin maximization). Should we hope to prove such a result? Do you believe that such result could be true? While this point alone is not brought up to dissuade acceptance of the paper, I would appreciate any thoughts the authors have on this.

### Questions
- line 362: why is there a norm in the definition of the $\ell_2$ loss? The neural network is defined to have real output.
- line 366: remove the word "the" before "assumption".
- line 381: the term "Hessian $\ell_2$ norm" sounds strange.
- Table 2: what are the reported results? correlation? This is not mentioned.
- There seems to be a typo in line 797 ("Table 4" appears twice).
- proof of Lemma 2, line 988: shouldn't the condition for the inner products be for $i$ and $i+1$, instead of $i$ and $i+2$? 
- line 042, "results from linear regime can be extended to linear neural networks": this sentence is confusing. Similarly in line 037. Linear neural networks are in the linear regime. You can just mention that results can be extended for the deep case.

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
This paper introduces *region count* as a new metric for understanding generalization in neural networks by examining the consistency of predictions across connected regions in the input space. The authors suggest that region count, which reflects the complexity of a model’s decision boundaries, is a more effective generalization indicator than traditional parameter-based metrics. Empirical results across various architectures and hyperparameter settings show that models with lower region counts tend to generalize better. Additionally, the authors' theoretical analysis links large learning rates to simpler decision boundaries, which may enhance generalization.

### Strengths
1. **Innovative Metric**: The introduction of region count to measure implicit bias in non-linear neural networks addresses limitations in parameter-dependent metrics, offering a fresh perspective on generalization.
3. **Hyperparameter Insights**: Findings around learning rate and batch size impacting region count offer practical value, guiding hyperparameter choices for improved generalization.
4. **Theoretical Basis**: Theoretical analysis, albeit in a simplified setup, provides a foundation for understanding the implicit bias induced by large learning rates, which aligns with the empirical findings.

### Weaknesses
### Weaknesses

1. **Limited Scope of Theoretical Analysis**: The theoretical section mainly focuses on a two-layer ReLU model, which limits its generalizability. Extending this analysis to more complex architectures, such as those with skip connections or attention mechanisms, is crucial for demonstrating the broader applicability of the proposed metric. The current theoretical framework does not address how the region count behaves in deeper networks or with different activation functions, which are common in modern architectures.

2. **Scalability Challenges in High Dimensions**: Estimating region count in high-dimensional spaces can be computationally intensive. While the proposed low-dimensional approximation is valuable, further analysis of its scalability is needed. Specifically, the paper should address how the number of random subspaces sampled affects the accuracy of the region count estimation and how this scales with increasing input dimensionality. The computational cost of the slicing method, especially when applied to large models and high-resolution inputs, needs to be more thoroughly investigated.

3. **Narrow Experimental Domain**: The experiments are primarily conducted in the image domain, which restricts the broader applicability of the region count metric. Extending validation to tasks like NLP would enhance the metric’s relevance across varied contexts. The current experiments do not explore the behavior of region count in sequence-based models or with different data modalities, which limits the generalizability of the findings. For example, the notion of a 'region' in text data might be different from that in image data, and this needs to be addressed.

4. **Limited Comparative Analysis with Complexity Metrics**: Although norm-based metrics are discussed, deeper comparisons with other complexity measures—such as sharpness- and margin-based metrics—would offer a more comprehensive view of the advantages and limitations of region count. The work of Andriushchenko et al. (2023) highlights how sharpness correlates positively with ResNet architectures but is less effective on Transformers and ViTs. For example, CIFAR and ResNet benchmarks alone may not sufficiently clarify the relationship between sharpness and generalization. Similarly, flatness measures perform well on CNNs, a setting similar to the one used here. Extending the method to NLP datasets and Transformer architectures, however, could better demonstrate its broader utility.

The empirical study’s impact is limited because the evaluated networks belong to the same family, raising questions about scalability to modern architectures like Transformers and ViTs. Andriushchenko’s findings also indicate that other flatness metrics struggle to adapt to these modern settings, suggesting that additional validation on ResNet and Transformer models could yield stronger insights. Though the method is claimed to be effective, the evidence provided lacks sufficient experimental depth. A more robust evaluation could include comparisons with sharpness metrics where they perform well or tests on edge cases, such as out-of-distribution generalization, to better establish the method’s efficacy.

### Questions
1. **Link to Certified Radius and Generalization Measures**: The connection between certified radius, margin, and norm-based measures may not be sufficient. Could metrics such as the ratio of a neural network’s margin to its Lipschitz constant provide additional insight? This ratio is directly related to the certified radius, representing the region where a classifier’s predictions remain unchanged (see Tsuzuku et al., 2018).

2. **Scalability**: How does the computational cost of estimating region count scale with model size and dimensionality, especially in NLP domains?

3. **Extensions to Complex Architectures**: Can the theoretical framework be feasibly extended to deeper or more sophisticated architectures, and would insights about learning rate and region count remain applicable?

4. **Generalization Beyond Classification**: Could region count metrics be adapted to other types of tasks, such as regression or structured prediction?

5. **Impact of Additional Hyperparameters**: Beyond learning rate and batch size, how do other hyperparameters—like weight decay, optimizer choice, and normalization layers such as BatchNorm or LayerNorm—affect region count and generalization?

6. **Comparison with Other Generalization Metrics**: How does the generalization potential of region counts compare with other metrics such as Lipschitz continuity, flatness, etc.? (See Jiang et al., 2020).

7. **Role of Implicit Regularization**: High learning rates (linked to weight decay effects with normalization) and small batch sizes (as noted by Keskar et al., 2017) are already associated with implicit regularization. The paper suggests that this is explained through sharp minima, but a more precise explanation could clarify this link.

8. **Connection to Certified Radius in Adversarial Robustness**: Discuss the relationship between region count and certified radius, particularly regarding Tsuzuku’s work, which uses the ratio of margin and Lipschitz constant as a robustness measure.

9. **Comparison to Sharpness**: Sharpness measures are data-dependent, yet the proposed method is also data-dependent. Would a comparison with sharpness metrics provide valuable insights?

10. **Scalability to Larger Models**: Does the slicing method scale effectively to larger models, and how does it behave as the number of parameters increases? Testing it on MLP layers with an increasing number of features could offer insights.

11. **Effectiveness of Scaling Techniques**: The scaling technique to invalidate the measure does not seem effective for the margin-to-Lipschitz-based ratio. Are there alternative approaches to validate or refine this measure?

12. **Region Count Interpretation**: Could you clarify what is meant by region count when it is not an integer?

### References

- Tsuzuku, Y., Sato, I., & Sugiyama, M. (2018). *Lipschitz-Margin Training: Scalable Certification of Perturbation Invariance for Deep Neural Networks*. In Proceedings of the 32nd Conference on Neural Information Processing Systems (NeurIPS).

- Jiang, Y., Neyshabur, B., Mobahi, H., Krishnan, D., & Bengio, S. (2020). *Fantastic Generalization Measures and Where to Find Them*. In Proceedings of the 8th International Conference on Learning Representations (ICLR).

- Keskar, N. S., Mudigere, D., Nocedal, J., Smelyanskiy, M., & Tang, P. T. P. (2017). *On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima*. In Proceedings of the 34th International Conference on Machine Learning (ICML).

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
5

### Summary
The paper proposes to quantify implicit bias through the lens of linear regions in deep networks. The authors find some empirical relations between the number of linear regions and the ability of the architecture to generalize. Trends with respect to number of regions and hyper parameters are also highlighted.

### Strengths
The paper proposes to study an important problem which is the quantification of implicit bias with deep networks. While numerous measures have emerged, it does seems that using linear regions offers a promising direction. The paper also explores a few different explorative set of experiments showing trends with hyper parameters which can be useful to help decide about optimization or regularization settings to employ.

### Weaknesses
The major weakness of the paper is in failing to cite entire corpus of work that already explored that direction before.

Starting with the seminal work of Montufar (On the Number of Linear Regions of Deep Neural Networks) which also studies the impact of number of linear regions on performances and its tie with the architecture. Many follow up works by the same authors delve deeper into that exact research problem as well: Sharp bounds for the number of regions of maxout networks and vertices of minkowski sums. A convolutional network specific study also comes form (On the Number of Linear Regions of Convolutional Neural Networks).

In parallel a whole set of studies from Baraniuk also look at that exact problem:
- A Spline Theory of Deep Networks
- SplineCam: Exact Visualization and Characterization of Deep Network Geometry and Decision Boundaries
- Deep Networks Always Grok and Here is Why
all involving counting regions and relating that to test performance and generalization, as well as depicting comparisons with optimizers and architectures, as provided by the current submissions.

### Questions
Without citing prior work that look at the exact same problem studied here, and thus without any discussion or comparisons, it is hard to assess the novelty of the current submission. A priori, it seems that the proposed findings and methods have already been studied before hence making the current submission fall below acceptance level. However I encourage the authors to precisely cite and compare those references to their submissions and specifically demonstrate how/where do they provide novelty.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors introduce new insights of understanding implicit bias of non-linear neural networks. They find that region count, a measure of the complexity of decision boundaries, is well correlated with generalization gap, defined as the difference between training and test errors. Their empirical and theoretical analysis show that the phenomenon of appropriate hyper-parameters leading to better generalization can be explained in terms of region counts. This work encourages future work for expanding their finding on more general and practical environments, further revealing the underlying implicit bias of neural networks.

### Strengths
- This paper introduces a novel and useful metric for understanding implicit bias of neural network’s generalization.
- Region count shows not only a high correlation with the generalization gap but also robustness across diverse architectures, datasets, and optimizers.
- This paper is well structured and well written. The authors’ claims are strongly supported by both theoretical analysis and empirical results on practical datasets.

### Weaknesses
 - Proposed region count method assumes low-dimensional subspace of the training data. Although robustness to different dimension choices is shown in Section 7, it still relies on a substantial number of sampling trials (100 runs). However, Table 5 in Appendix B contains an ablation study on the impact of the number of experiment runs, which never been discussed in the main paper. Including these results in the main text would strengthen the method's validity.
- The proposed method provides an interesting explanation for the implicit bias whereby a large learning rate or small batch size facilitates superior generalization. While the authors state that this is 'typically deemed as beneficial for generalization’, but it is necessary to show that a large learning rate or small batch size leads to better generalization in terms of both generalization gap, and top-1 accuracy. Specifically, the paper should demonstrate that the observed correlation between region count and generalization gap is not merely a byproduct of these hyperparameter choices but a genuine phenomenon.
- Figure 4 and Table 8 report the correlation between generalization gap and region count on CIFAR-10 across different architectures. However, the range of generalization gap (y-axis) appears large compared to typical CIFAR-10 performance. For example, [1] reported that ResNet20 achieves an error rate of 8.75% on CIFAR-10, and [2] shows that ResNet18 achieves 93.02% accuracy, while in Table 8, ResNet18’s generalization gap is shown to be at least 15% (maximum 85% accuracy). Providing the top-1 accuracy for each architecture (under different hyper-parameters) would help prevent reader confusion and allow for a more direct comparison with existing benchmarks. The absence of these accuracy values makes it difficult to assess the practical relevance of the reported generalization gaps.

### Questions
- Does region count maintain a consistent correlation after dimensionality reduction (e.g., PCA)?
- Dose the variation in the dimensionality $\mathbb{R}^{d}$ affects the results of sampled subspace in region count?
- Is this paper first to understand the correlation between generalization gap and hyper-parameters?
- In Definition 1, how is 'Connectedness' validated in practice for any $f(\gamma(t))=c$ where$\ t \in [0,1]$? For example, is it achieved through a grid search?
- In Figure 7, it is unclear how to interpret the results of the random flip. Is the results missing?
- In Appendix B, the third paragraph mentions Table 4 twice.

### Soundness
3

### Presentation
3

### Contribution
2
