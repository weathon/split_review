# Learn2Mix: Training Neural Networks Using Adaptive Data Integration

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
Accelerating model convergence in resource-constrained environments is essential for fast and efficient neural network training. This work presents learn2mix, a new training strategy that adaptively adjusts class proportions within batches, focusing on classes with higher error rates. Unlike classical training methods that use static class proportions, learn2mix continually adapts class proportions during training, leading to faster convergence. Empirical evaluations on benchmark datasets show that neural networks trained with learn2mix converge faster than those trained with classical approaches, achieving improved results for classification, regression, and reconstruction tasks under limited training resources and with imbalanced classes. Our empirical findings are supported by theoretical analysis.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the limitation of classical training paradigms that maintain fixed class proportions within batches, which fails to account for varying levels of difficulty across different classes and can hinder optimal convergence rates. The authors propose Learn2Mix, a training strategy that dynamically adjusts the proportion of classes within batches based on real-time class-wise error rates, directing more training emphasis towards challenging or underperforming classes, thereby accelerating model convergence and improving performance across classification, regression, and reconstruction tasks.

### Strengths
1. The paper is well-structured and highly readable. Its motivation stems from a key observation: different classes have varying learning difficulties, an aspect that traditional class imbalance algorithms have largely overlooked.
3. The paper proposes a novel approach where class proportions are dynamically adjusted based on training loss. The idea is both innovative and intuitive.
3. The experimental validation is comprehensive and convincing, encompassing six datasets including CIFAR-100 with its 100 classes, and spanning three different tasks: classification, regression, and image reconstruction.
4. While I haven't thoroughly examined the convergence analysis proofs, the paper provides theoretical guarantees for its approach.

### Weaknesses
The class imbalance setup for CIFAR-100 appears oversimplified, where the first 50 classes each comprise 0.1% of the data while the latter 50 classes each comprise 1.9%. A more rigorous evaluation should explore diverse imbalance patterns, such as exponentially decreasing ratios, step-wise distributions, or even real-world imbalance scenarios, to better validate the algorithm's robustness under complex class distributions. The current evaluation does not sufficiently explore the impact of varying degrees of imbalance within the CIFAR-100 dataset. Specifically, the chosen imbalance, while demonstrating a difference in class representation, does not fully capture the challenges posed by more nuanced or severe imbalance scenarios. This limits the generalizability of the findings to real-world situations where class distributions can be highly skewed and follow more complex patterns.

### Questions
Could the evaluation be strengthened by testing more complex class imbalance patterns on CIFAR-100, rather than simply assigning 0.1% to the first 50 classes and 1.9% to the remaining ones?

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
The authors present learn2mix, a training method which dynamically adapts the proportion of classes during training using class-wise error rates. They provide theoretical justifications for the performance of learn2mix and also empirically demonstrate accelerated convergence on balanced and imbalanced datasets.

### Strengths
- The method is presented in a clear manner and ensures each example within the class-specific dataset will be chosen uniformly at random through training, even with the reweighting.  
- The experiment details are presented clearly between the main text and the appendix, and each experiment seems replicable. 
- learn2mix outperforms classical training across various classification and regression tasks.

### Weaknesses
 - The empirical results for both classical and learn2mix are concerningly underwhelming. For example, the performance of both methods are cut off at only <40% accuracy on CIFAR-10, even though most image classification models can easily achieve 90% accuracy, with modern models reporting >99% test accuracy. Even when considering the LeNet-5 architecture which the authors benchmarked, the original LeNet-5 and MNIST paper [1] achieves 99% accuracy in 20 epochs, while this paper reports <80% accuracy in 60 epochs. This significant gap in performance makes it unclear if the faster convergence of learn2mix holds in practice with more careful training setups and realistic models.
- The method was only compared against classical empirical risk minimization. Classical training is known to be ineffective for class imbalance, so it would be helpful to see how this method compares to other methods which adjust the training data such as oversampling. 
- The theoretical results require that the class-wise loss is strongly convex in $\theta$; however, the loss landscape for neural networks is known to be highly non-convex [2], which challenges the relevance of their findings.

### Questions
- How does learn2mix, which modifies the composition of the training data, compare with other regimes such as [3], which modify the loss function? This method seems slightly more expensive because it involves the extra step of dynamically composing the training data.

[3] Sagawa et al, Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces "learn2mix", a training strategy for neural networks that dynamically adjust the weight of each class during training according to the class-wise error, which is different from the traditional methods that use a static class proportion. Using a dynamic class proportion accelerate the converge rate and improve the performance, especially when the class is imbalanced.

### Strengths
1. The paper is well-written and easy to follow. The topic is related to class-imbalance and neural network training which matches ICLR well. The proposed approach is simple and effective.

2. The paper provides both theoritical and emperical justification.

### Weaknesses
1. My biggest concern about this paper is the evaluation. The only baseline that the authors compared is the standard training mechanisms, although curriculum learning has already been widely studied in the literature. The contribution would be much more convincing by having stronger baselines, such as using Focal loss or any curriculum learning methods.

2. The results shown in Figures 1 and 2 don't seem to be fully converged.

### Questions
1. How does the proposed method perform compared with stronger baselines for class imbalance, such as using the Focal loss?

2. How should a user choose the mixing rate? Is the proposed method sensitive to the hyper-parameter?

3. Since the proposed method doesn't use a fixed class weight. I wondered if this approach is more robust to distributional shifts regarding the class imbalance levels.

### Soundness
2

### Presentation
3

### Contribution
2
