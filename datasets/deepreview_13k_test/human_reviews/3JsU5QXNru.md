# Group Distributionally Robust Dataset Distillation with Risk Minimization

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Dataset distillation (DD) has emerged as a widely adopted technique for crafting a synthetic dataset that captures the essential information of a training dataset, facilitating the training of accurate neural models. Its applications span various domains, including transfer learning, federated learning, and neural architecture search. The most popular methods for constructing the synthetic data
rely on matching the convergence properties of training the model with the synthetic dataset and the training dataset. However, targeting the training dataset must be thought of as auxiliary in the same sense that the training set is an approximate substitute for the population
distribution, and the latter is the data of interest. Yet despite its popularity, an aspect that remains unexplored is the relationship of DD to its generalization, particularly across uncommon subgroups. That is, how can we ensure that a model trained on the synthetic dataset performs well when faced with samples from regions with low population density? Here, the representativeness and coverage of the dataset become salient over the guaranteed training error at inference. Drawing inspiration from distributionally robust optimization, we introduce an algorithm that combines clustering with the minimization of a risk measure on the loss to conduct DD. We provide a theoretical rationale for our approach and demonstrate its effective generalization and robustness across subgroups through numerical experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes an algorithm for dataset distillation by incorporating distributionally robust optimization into it. There is theoretical justification and empirical validation of the proposed algorithm.

### Strengths
There are both theoretical and experimental demonstrations of the effectiveness of the algorithm.

### Weaknesses
1. There seems to be a mismatch between the motivation and the experiments. The motivation emphasizes regions with low population density, which usually correspond to the worst-group performance in subpopulation shift [1]. However, the main experiments related to distribution shift are conducted on test sets with perturbations or the worst group induced by an additional clustering process. It would be better to conduct more experiments on subpopulation datasets included in [1]. 
2. The introduction has too many paragraphs, which makes the logic of the introduction tedious with poor readability. 

Some minor issues:

- In Line 049, "some technique". 
- In Line 129 and 131, "Algorithm" "Numerical Results" their first letters do not need to be capitalized. 
- In the last paragraph of introduction, Section 3 is not mentioned.

[1] Yang, Yuzhe, et al. "Change is Hard: A Closer Look at Subpopulation Shift." *International Conference on Machine Learning*. PMLR, 2023.

### Questions
In Line 017, what does "targeting the training dataset" mean?

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
3

### Summary
The work proposes a robust dataset distillation approach that incorporates distributional robust optimization (DRO) to enhance generalization and performance across subgroups. This method combines clustering with risk-minimized loss to conduct dataset distillation. By prioritizing representativeness and coverage over training error guarantees, the approach enhances the models trained on synthetic datasets for real-world scenarios. Both theoretical analysis and empirical validation on multiple standard benchmarks are provided, demonstrating the effectiveness of the proposed approach.

### Strengths
1. The paper proposes applying distributional robust optimization to dataset distillation, providing a reasonable approach to enhance generalization.

2. Drawing on distributional robust optimization theory, this work establishes a theoretical foundation to support the proposed approach to dataset distillation.

3. The paper is well-structured, with clear algorithm block and effective visualizations that enhance the presentation of the work.

### Weaknesses
1. The empirical experiments focus primarily on CIFAR-10, ImageNet-10. Extending the evaluation to larger, real-world datasets with a greater number of classes would better demonstrate the effectiveness of proposed approach in generalization and robustness under real-world conditions.

2. Comparing the proposed approach with additional baseline method addressing generalization and robustness would provide a more comprehensive assessment of the proposed approach, including comparisons with baseline methods such as [1, 2, 3].

3. It would be valuable to visualize the robust inference tasks using real-world data rather than illustrative visuals, which could provide more insight and observations in real-world scenarios.

Reference:

[1] Domain generalization with adversarial feature learning. CVPR 2018.

[2] Self-challenging Improves Cross-Domain Generalization. ECCV 2020.

[3] HYPO: Hyperspherical Out-of-Distribution Generalization. ICLR 2024.

### Questions
Please refer to the detailed suggestions provided in the weaknesses section.

### Soundness
3

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
4

### Summary
This paper proposes a new data distillation approach emphasizing the subgroup coverage and generalization ability of the models trained on the synthetic dataset. This paper provides a theoretical analysis rooted in Distributionally Robust Optimization (DRO) and verifies the effectiveness of the proposed method with various experiments.

### Strengths
* This paper considers the group coverage and generalization ability of the synthetic dataset in Data Distillation(DD), which is interesting and novel.

* The introduced algorithm is clear and the theoretical analysis seems solid.

* The numerical results do show the effectiveness of the proposed algorithm. Meanwhile, the figures (Fig.3, 4) seem to indicate that the proposed method improves group coverage.

### Weaknesses
* While the paper emphasizes group coverage and generalization in data distillation, the experiments are mainly conducted on IID datasets. More experimental results in scenarios with distribution shift between training and testing sets (such as long-tail classification, subpopulation shift, domain adaptation, domain generalization, etc) can further validate the improvement in group coverage and generalization ability,

* According to Algorithm 1, the initialization of the synthetic dataset seems very important because it involves how the training data samples are clustered into subgroups. It may require further ablation study to verify the stability of the proposed algorithm.

* The proposed method seems like a plug-in as it only modifies the objective for data distillation and could be combined with any data distillation methods. A more sophisticated comparison between the proposed method with other objectives regarding training gradients, feature distributions, and training trajectory could help readers better understand the improvement of the proposed method.

### Questions
I have stated many of my suggestions and concerns in the weaknesses section. Below, I have further questions with some minor issues.

* While theoretical analyses have been provided, I wonder whether the proposed method would affect the convergence rate and make it more difficult to find an optimal solution for the proposed objective. I would appreciate an empirical time complexity analysis regarding the proposed method.

* In Eq.10, what does the *N* represent? I did not see any introduction of the *N*.

### Soundness
3

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
This paper proposes a robust dataset distillation method that enhances generalization across underrepresented subgroups by using a double-layer distributionally robust optimization (DRO) approach. Traditional dataset distillation often compresses training data into synthetic sets by matching training characteristics but may struggle with subgroup generalization. To improve this, the authors cluster the training data around synthetic data points and apply a Conditional Value at Risk (CVaR) loss to minimize worst-case subgroup errors, making the synthetic dataset more representative of diverse data distributions. Experimental results show that this method significantly improves robustness under domain shifts, outperforming baseline methods on benchmarks like CIFAR-10 and ImageNet-10, particularly in challenging conditions like noise and blurring.

### Strengths
- As far as I know, this paper firstly addresses a major limitation in standard dataset distillation (underrepresented or rare subgroups) by applying a double-layer distributionally robust optimization (DRO) framework. This approach ensures the synthetic dataset better represents the full diversity of the data, reducing performance drops across different data subgroups. 

- This paper provides not only empirical evidence of the proposed method's robustness against domain shifts such as noise, blur, and inversion, but also a theoretical analysis of the effectiveness of CVaR in the loss function to enhance robustness.

- The proposed method is designed to be adaptable and can integrate with various existing distillation techniques, such as gradient or distribution matching. This modularity makes it compatible with a range of distillation methods, which are still actively developing and evolving.

### Weaknesses
- The proposed DRO approach, particularly with clustering and CVaR, may introduce significant computational overhead. This added complexity could be amplified for large-scale datasets due to the clustering of training (real) data. However, the paper does not discuss the computational overhead of the proposed method.

- Although the method shows promising results on benchmarks like CIFAR-10 and ImageNet-10, the experiments are limited to controlled domain shifts (e.g., noise, blur). Testing under more realistic settings, such as in transfer learning, would further validate its robustness and practical relevance. For example, one could (1) train neural networks on a synthetic dataset distilled from a coarse-grained dataset (e.g., ImageNet) and (2) fine-tune and evaluate them on a fine-grained dataset (e.g., Birds 200). This setup would better illustrate the method's effectiveness in addressing the challenges posed by rare subgroups.

### Questions
Please see weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3
