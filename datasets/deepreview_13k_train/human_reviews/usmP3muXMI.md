# Minimizing Chebyshev Risk Magically Mitigates the Perils of Overfitting

- Decision: Reject
- Scores: 5, 6, 3

## Abstract
Overparameterized deep neural networks (DNNs), if not sufficiently regularized, are susceptible to overfitting their training examples and not generalizing well to test data.  To discourage overfitting, researchers have developed multicomponent loss functions that reduce intra-class feature correlation and maximize inter-class feature distance in one or more layers of the network.  By analyzing the penultimate feature layer activations output by a DNN's feature extraction section prior to the linear classifier, we find that modified forms of the intra-class feature covariance and inter-class prototype separation are key components of a fundamental Chebyshev upper bound on the probability of misclassification, which we designate the Chebyshev Prototype Risk (CPR).  While previous approaches' covariance loss terms scale quadratically with the number of network features, our CPR bound indicates that an approximate covariance loss in log-linear time is sufficient to reduce the bound and is scalable to large architectures.  We implement the terms of the CPR bound into our Explicit CPR (\emph{exCPR}) loss function and observe from empirical results on multiple datasets and network architectures that our training algorithm reduces overfitting and improves upon previous approaches in many settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents an approach to reduce overfitting and improve the test performance of DNNs. It considers the existence of an optimal prototype (featurizer) and uses Chebyshev's inequality to bound the misclassification probability, which depends on (low) intra-class variance and (high) inter-class distances in the prototype. Based on this, the authors present a new loss function and showcase its effectiveness in reducing overfitting on some image classification benchmarks.

### Strengths
1. The idea to use Chebyshev prototype risk is novel, interesting and theoretically grounded. The authors also present a way to make their approach scalable with number of classes and it seems effective across several settings.

1. Overall, the paper is well-written and easy to follow.

### Weaknesses
1. ****Discussion on a set of related works seems missing.****
- The concept of minimizing intra-class variance while encouraging larger inter-class distances seems very similar to the well-observed phenomenon of neural collapse [1]. In [1], it was observed that after training for a sufficiently long time, the final layer feature embeddings collapse to class means and form a simplex ETF structure. The classifier of top also coincides with these. It was also shown to improve test performance. How does the proposed approach relate to this? I suggest including some discussion on the connection/comparisons with this. Specifically, the authors should discuss whether their method achieves similar feature collapse and how their loss function compares to simply training until convergence where neural collapse is observed. A more detailed comparison, perhaps by measuring the intra-class variance and inter-class distances during training, would be beneficial.
- It seems that the section on related work on methods aimed to reduce overfitting only contains relatively older papers. For instance, [2] is a recent work that is not discussed. Furthermore, the authors should consider discussing other regularization techniques such as mixup or label smoothing, and how their approach compares or complements these methods.

2. ****Limited evaluation.****
- The proposed approach seems promising but it would be helpful to see more evidence that it is effective, e.g. by evaluating this approach on other datasets such as ImageNet. The current evaluation is limited to relatively small datasets, and it is unclear how the method would scale to larger and more complex datasets. The authors should also provide results on datasets with varying levels of difficulty to better understand the strengths and weaknesses of their approach.
- I would also suggest comparing with some other methods. For instance, the recently proposed squentropy loss [3] is shown to improve test performance. It is important to compare with state-of-the-art methods to properly contextualize the performance of the proposed approach. The authors should also consider comparing with other methods that explicitly aim to reduce overfitting, such as dropout or batch normalization, to see how their method compares in terms of effectiveness and computational cost.

### Questions
(See weaknesses above)

Can the authors verify whether the baseline numbers used for comparison are computed in the terminal phase of training where neural collapse happens (please refer to [1])? Since the proposed approach seems to have a similar motivation as this phenomenon, it would be interesting to see how much incorporating the loss helps compared to just training for a large enough time.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work subscribes itself within methods for improving generalization such as Cogswell et al.'15, Rodriguez et al. '16 and Haresh et al. '18, that seek to limit the hypothesis space by reducing the variance in either covariates or among members of a class. They agree to use an idea borrowed from the group that produced a distance-based classification and nearest-class means to use as anchors, and much in the same manner as anchors in a siamese setup. Thereby global loss components that enforce distance among these class prototypes, and locals ones that enforce class-cluster compactness, are derived. As an extension almost, the authors derive bounds on the variances around class prototypes.

### Strengths
The paper makes clear and persuasive arguments and the motivation leads naturally to the presented solution. It provides theoretic grounds for tailoring the loss for exploiting the two classicalideas of intra- and inter- class-cluster (for the lack of better terminology). The presented theorems and proofs check out for correctness. Benchmarks are sufficiently provided.

### Weaknesses
I would have liked to see a theoretical understanding of why prefer your method over the competition, beyond the simple benchmark over two usual datasets.

### Questions
None.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel regularization for deep neural networks (DNNs) based on Chebyshev's inequality, where Chebyshev's inequality is used to derive the upper bound of the probability of an embedding feature for an example deviating from class-wise prototypes.
Losses for estimating prototypes as the class-wise embedding average, reducing intra-class feature covariances, and making prototypes orthogonal to each other are proposed.
Experiments are conducted to compare the proposed regularization with existing methods that try to minimize covariances between activations or weights.

### Strengths
- The use of Chebyshev's inequality to derive the regularization for DNNs is novel.

### Weaknesses
 - I could not figure out the theoretical justification for using DS in Lemma 3.1 or Corollary 3.1.1.
    - If I understand correctly, the DS part in Eq.(6) can be any positive variable. Then what is the reason for using DS here?
    - Moreover, the authors claim to regularize DNN training by increasing DS (which is established by decreasing $\mathcal{L}_{CS}$), because it leads to a smaller value of the right part of Eq.(6). However, the larger DS value leads to the looser condition from the point of view of the left part of Eq.(6).
- Discussion and empirical comparison with related work is insufficient.
    - There are several other existing papers that discuss the orthogonality of weights, such as [1].
    - It is also preferable to qualitatively or qualitatively compare the proposed method with other methods using class-wise prototypes, such as [2].
    - Formatting in references is incomplete. For example, some papers do not have a place of publication.
- Experiments are performed with CIFAR-100 and STL-10 only.

### Questions
- In Lemma 3.1, is there an assumption that the class label of $v$ is $k$?

- In Section 5.4, I could not understand how the hyperparameters are determined in the proposed method.

- In Section 4.3, Eq.11 -> Eq.9?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
