# Enhancing Robust Fairness via Confusional Spectral Regularization

- Decision: Accept
- Scores: 8, 6, 6, 8, 6, 8

## Abstract
Recent research has highlighted a critical issue known as ``robust fairness", where robust accuracy varies significantly across different classes, undermining the reliability of deep neural networks (DNNs). 
A common approach to address this has been to dynamically reweight classes during training, giving more weight to those with lower empirical robust performance. 
However, we find there is a divergence of class-wise robust performance between training set and testing set, which limits the effectiveness of these explicit reweighting methods, indicating the need for a principled alternative.
In this work, we derive a robust generalization bound for the worst-class robust error within the PAC-Bayesian framework, accounting for unknown data distributions. 
Our analysis shows that the worst-class robust error is influenced by two main factors: the spectral norm of the empirical robust confusion matrix and the information embedded in the model and training set. 
While the latter has been extensively studied, we propose a novel regularization technique targeting the spectral norm of the robust confusion matrix to improve worst-class robust accuracy and enhance robust fairness.
We validate our approach through comprehensive experiments on various datasets and models, demonstrating its effectiveness in enhancing robust fairness.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies the robust fairness of deep neural networks. The authors first derive a robust generalization bound for the worst-class robust error within the PAC-Bayesian framework. The bound comprises two key components: the spectral norm of the empirical robust confusion matrix and a model-dependent and training data-dependent term. Based on this, the authors further develop a novel regularization technique to optimize the spectral norm of the robust confusion matrix to improve the robust fairness. Extensive experiments are conducted to show the effectiveness of the method.

### Strengths
- The paper is well-written and easy to follow. It gives adequate background on the topics of fairness, adversarial robustness, and PAC-bound, which can be very helpful for readers who are not familiar with the field to understand the gist of the paper.
- The contribution is quite significant because:
1. this is the first PAC-Bayesian framework to characterize the worst-class robust error across different classes.
2. the proposed regularization term is novel because it aims to improve the robust fairness from the spectral norm of the robust confusion matrix, which is ignored by previous methods.
3. during evaluation, the method shows improved results in terms of robust fairness across all settings.

### Weaknesses
 - The motivation from the intro feels disconnected from the method. In Figure 2, the authors argue that the class exhibiting the worst robust performance on the training set may not be the same as the one on the test set. However, how would the proposed method in Section 4 address this issue? It would be great if the authors could provide some discussion about the connection between this motivation and the proposed method. Specifically, the paper highlights a potential divergence between training and test set performance for worst-case classes, but it's not clear how regularizing the spectral norm of the confusion matrix directly mitigates this divergence. A more explicit link between the observed training-test discrepancy and the proposed regularization would strengthen the motivation.

- It would be great to also see some analysis for the hyper-parameters $\alpha$ and $\gamma$ for a better understanding of the method. How optimal is 0.3 for $\alpha$? What is the effect of changing it? Does it trade off the average accuracy vs the worst class robustness? I would appreciate if the authors can provide some intuition behind the effect of these two hyper-parameters and also some experimental results showing how AA & Worst changes with respect of different values. The current analysis lacks a systematic exploration of how these parameters influence the trade-off between average and worst-case performance. For instance, it's unclear how the magnitude of $\alpha$ affects the emphasis on worst-class robustness versus overall accuracy, and how $\gamma$ interacts with this balance.

- Typos:
1. In Equation 10, (x, y) -> (x', y)
2. Line 425, W -> We

### Questions
- This question relates to the motivation in Fig. 2. What is the correlation between the class-wise robust accuracy of the training and the test set? I understand the robust confusion matrix over the training set does not always align with that of the test set. But if they are aligned most of the time, should it still be an important concern?

- It seems that $\gamma=0$ always has slightly better AA and worse Worst compared to $\gamma=0.1$. Why is this the case?

- The derivation from Eq. 9 to Eq. 11 is a bit confusing. Why is the middle term approximated by the sign? How good/bad is this approximation? It would be great if the authors could provide a bit detailed explanation for lines 354-358.

- Why is the best result in the 5th column of Tab. 1 the original TRADES-AWP? It seems that all the fine-tuning methods fail to improve the average accuracy?

### Soundness
3

### Presentation
4

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
This work derives a robust generalization bound for the worst-case (i.e. adversarial) robust error using a PAC-Bayesian analysis. This is the worst-margin violation in an epsilon-perturbed adversarial input setup, which can be represented as L1 norm on a perturbed confusion matrix. Through a link to the L2 norm (with an unknown empirically tight ratio), the bound further splits to (1) spectral norm of the empirical margined confusion matrix and (2) a component that depends on the information content of the input data and the specifics of the hypothesis space.

The paper focuses on the spectral norm component as much of the recent literature has focused on the other component. The work argues that this spectral norm can be used as a regularization term during training, and provides an approximation of it with a feasible implementation path.

The proposed method is evaluated on the worst-case accuracy (test) metric under both clean-data and AutoAttack (Groce & Hein, 2020b) settings, and is compared to a number of common adversarial training methods. Experiments on image datasets show that the proposed method has comparable results to SOTA on average metrics while outperforming most methods on worst-case robust error. Transfer learning experiments (CIFAR to ImageNet) show that the regularized fine-tuning outperforms the baseline on the worst-case robust error metric.

### Strengths
- The approximation in section 4.1 makes it possible to implement an adversarial spectral-norm regularizer effectively.

- Based on limited empirical analysis, the method looks robust to the choice of hyperparameters.

- The method performs well against SOTA attack methods (AutoAttack), and not just the limited setting considered in the theoretical analysis.

### Weaknesses
 - Empirical analysis is somewhat limited both in domain and the datasets used. It’s hard to argue only based on the provided analysis that the results will extend to larger models, other vision datasets, or non-vision classification tasks. Adding experiments with much larger datasets (e.g. larger ImageNet) or non-vision tasks would greatly improve the empirical analysis in the paper.

 - The assumption on the norm of U (i.e. restricting f_{w+u}(x) - f_w(x), instead of bounding the input perturbation) seems crucial to the derivation of Lemma 3.2. Have you looked at the value of this norm in your experiments? An analysis of the norm of U for some of the experiments conducted for the work could help establish how tightly this assumption is satisfied in practice.

### Questions
- The assumption on the norm of U (i.e. restricting f_{w+u}(x) - f_w(x), instead of bounding the input perturbation) seems crucial to the derivation of Lemma 3.2. Have you looked at the value of this norm in your experiments? An analysis of the norm of U for some of the experiments conducted for the work could help establish how tightly this assumption is satisfied in practice.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper endeavors to address the robust fairness problem and derives a robust generalization bound for the worst-class robust error within the PAC-bayesian framework, accounting for unknown data distributions.
Leveraging the insights gleaned from our theoretical results, they propose an effective and principled method to enhance robust fairness by introducing a spectral regularization term on the confusion matrix.

### Strengths
1. This work represents the first endeavor to develop a PAC-Bayesian framework to characterize the worst-class robust error across different classes. This is an important problem.
2. This paper is theoretically solid.
2. The improvement brought by this method is obvious in the experiment.

### Weaknesses
 1. The fairness improvement method in this article seems to be designed only for adversarial training, so is there any improvement for the unfairness brought by other settings (such as long-tail training distribution)?
2. In the experiment, the author targeted AutoAttack. Does it have any effect on other attack methods?

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Recent studies have identified "robust fairness" as a significant challenge in deep learning, where the robust accuracy of DNNs can differ widely across various classes, affecting their reliability. Traditional methods attempt to tackle this issue by adjusting class weights during training, yet these methods often fail to predict which class will have the poorest robust accuracy in testing. To address this, researchers have developed a new theoretical framework within the PAC-Bayesian paradigm to better understand and control the worst-case robust error. This framework introduces a regularization technique aimed at reducing the spectral norm of the robust confusion matrix, thereby improving the robust accuracy of the most vulnerable class and promoting fairer outcomes across all classes.

### Strengths
1. The paper is well written and organized for readers' easy understanding.

2. The work is well motivated.

3. The performance is good.

### Weaknesses
1. The spectral norm should be denoted by another symbol rather than ||*||_2. It is rather confused between spectral norm and l_2 norm. Specifically, in Line 311 ~ Line 315, the authors mention the relationship of l_1 and l_2 norm, but the norm in Eqn. (8) should be spectral norm? So I not sure whether it is correct for the derivation.

### Questions
Please see Weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the issue of fairness in adversarial robustness. The authors leverage PAC-based bounds to analyze the worst-class error. They first provide a bound for deterministic classifiers based on the PAC framework. Next, using techniques proposed by Neyshabur et al., they bound the KL divergence, which is challenging to compute. Finally, they apply the analysis from Xiao et al. to obtain Lemma 3.4. Empirically, based on their analysis of the confusion matrix, they propose the addition of an approximated regularization term. Empirical results support the effectiveness of the proposed method.

### Strengths
This paper is well-motivated, clearly written, and easy to follow. 

The theoretical results are novel and offer an interesting perspective on the problem of robustness fairness. 

Empirically, the proposed method enhances worst-class performance.

### Weaknesses
Concerns regarding this paper primarily focus on practical implications. From a methodological perspective, the authors apply a regularization term to the confusion matrix. Intuitively, calculating the KL divergence between misclassified examples is akin to re-examining those examples or, in other words, assigning greater weight to misclassified instances. Since only the empirical confusion matrix is used for optimization during training, this method may not effectively address their motivation, which is to resolve the mismatch between training and testing worst-class performance.

As a result, the proposed method may encounter issues such as sacrificing the performance of the best class and an increased likelihood of robust overfitting, both of which are evident in the empirical results presented in this paper.

Regarding the experimental setup, the authors overlook important evaluations under PGD attacks. Each experimental condition should be assessed across all three datasets rather than just one or two, and both $L_2$ and $L_\infty$ attacks should be included.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper aims to enhance the worst-class accuracy under adversarial attacks. The authors first establish a robust generalization bound within the PAC-Bayesian framework, demonstrating that the worst-class error is constrained by the spectral norm of the empirical robust confusion matrix. Based on this theoretical insight, they propose a regularization loss to minimize the spectral norm of the confusion matrix. Extensive experiments on CIFAR-10, CIFAR-100, and TinyImageNet validate the effectiveness of the proposed method in improving worst-class accuracy under adversarial attacks.

### Strengths
(1) The paper is well-written and easy to follow. Although I am not an expert in the PAC-Bayesian framework, the authors clearly explain the flow of their proof, enabling me to understand how the main results are derived. 

(2) To address the problem of non-differentiable confusion matrix, the authors propose a novel approximation method — using KL divergence to replace binary errors. This approach is conceptually sound and interesting.

(3) Improving worst-class accuracy is important but often overlooked. The authors make a meaningful contribution by providing both theoretical insights and practical methods to address this issue effectively.

### Weaknesses
 (1) I find Paragraph 3 (Lines 51 to 66) unclear in its intended message. First, the authors state that “our findings indicate that the robust confusion matrix over the training set does not always align with that of the test set. In other words, as shown in Fig. 2.” However, Figure 2 illustrates a strong correlation between training and testing accuracy, with the worst-performing class in training being the second-worst in testing. Additionally, the performance gap between the two worst-performing classes in testing is small, which could be attributed to estimation variance. Second, the authors assert that their findings “motivate the need for a principled approach to mitigate the disparities in robust performance.” However, Proposition 3.1 suggests that the discrepancies between the training and testing confusion matrices arise from a second term, which depends on the model and training set. Minimizing this term is not a contribution of the paper and is not explicitly addressed in the work. I recommend that the authors explain more explicitly how their findings motivate their approach.

(2) Lines 182–184: It is not immediately clear why the worst-class robust error can be represented as the L_1 norm of the confusion matrix. Could the authors provide a detailed derivation to clarify this relationship?

(3) There is an inconsistency between the confusion matrix in Figure 3 and the one in Eq. (1). In Eq. (1), the diagonal entries are defined as 0, whereas in Figure 3, the diagonal contains non-zero values. I suggest that the authors clarify this discrepancy and modify either Figure 3 or Equation 1 to be consistent, if appropriate.


(4) The experiments in this paper focus solely on adversarial training and evaluate both clean and robust worst-class accuracy. According to Lemma 3.3, the proposed method is also applicable to improving worst-class accuracy under clean training (e.g., using standard cross-entropy loss). I am curious whether the proposed method can enhance worst-class accuracy under clean training setting (CIFAR100 and ImageNet results), as demonstrated in [1]. For example, conduct additional experiments on CIFAR100 and ImageNet using standard cross-entropy loss.

(5) Why is the sign() function required in Eq. (11)? Why can’t the average KL divergence be used directly? Are there any ablation studies to justify this operation? I suggest that authors include ablation studies comparing performance with and without the sign() function or
discuss any potential drawbacks or limitations of using the average KL divergence directly.

minor typos: Line 470, Tab. 2 should be Tab. 3.

### Questions
See weaknesses. I am open to increasing my score if the identified weaknesses are adequately addressed.

### Soundness
3

### Presentation
4

### Contribution
4
