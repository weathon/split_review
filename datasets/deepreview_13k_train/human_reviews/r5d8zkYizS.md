# Adversarial Attacks as Near-Zero Eigenvalues in the Empirical Kernel of Neural Networks

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
Adversarial examples ---imperceptibly modified data inputs designed to mislead machine learning models--- have raised concerns about the robustness of modern neural architectures in safety-critical applications. 
In this paper, we propose a unified mathematical 
framework for understanding adversarial examples in neural networks, corroborating Szegedy et al.'s original conjecture that 
such examples are exceedingly rare, despite their presence in the proximity of nearly every test case. By exploiting Mercer's decomposition theorem, we characterise adversarial examples as those producing near-zero Mercer's eigenvalues in the empirical kernel associated to a trained neural network. 
Consequently, the generation of adversarial attacks, using any known technique, can be conceptualised as a progression towards the eigenvalue space's zero point within the empirical kernel.
We rigorously prove this characterisation for trained neural networks that achieve interpolation and under mild assumptions on the architecture, thus
providing a mathematical explanation for the apparent contradiction of neural networks excelling at generalisation while remaining vulnerable to adversarial attacks. 
We have empirically verified that adversarial examples generated for both fully-connected and convolutional architectures through the widely-known DeepFool algorithm and through the more recent Fast Adaptive Boundary (FAB) method consistently lead to a shift in the distribution of Mercer's eigenvalues toward zero. These results are in strong agreement with predictions of our theory.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new theory explaining the nature of adversarial examples. Using Mercer’s theorem from kernel theory, the authors try to explain the adversarial examples’ contradictory nature; even a neural network with good generalization performance suffers from the existence of adversarial examples. First, the authors provide a theorem that adversarial examples shift Mercer’s spectrum to have near-zero eigenvalues. Then, the authors prove another theorem that explains why it is unlikely to sample an adversarial example in a test set. Finally, the authors validate their theory with a set of experiments.

### Strengths
1. The theoretical finding is non-trivial. The proofs look to be correct.
2. The paper proposes a new theoretical analysis of adversarial examples. To the best of my knowledge, this is the first application of kernel theory, and the authors make a novel contribution to the theoretical understanding of adversarial examples.
3. The theoretical finding does not depend on a specific data point being attacked.
4. The authors tried validating the theory on a more complex neural network architecture, i.e., VGG.

### Weaknesses
1. The significance of the theoretical findings is unclear. The authors should have demonstrated more potential application of the theoretical findings, e.g., how to apply the findings to design a new defense. It is not sufficient to simply state that the findings are novel; the authors need to show how this novelty translates to practical impact or a deeper understanding of existing methods. For example, do the near-zero eigenvalues correlate with any known properties of adversarial examples that are already used in detection methods? If so, this would strengthen the significance of the theoretical findings.
2. The theoretical finding is a limit behavior that only holds for extremely small perturbation sizes. The authors’ argument that such an assumption on small perturbation size is needed is not sufficient because we don’t even have a proper definition of how small is “small enough”. As the authors describe in Section 7, a formal convergence rate analysis is required. The lack of a concrete bound on the perturbation size makes the practical relevance of the theoretical results questionable. The theory needs to be extended to provide insights into the behavior of adversarial examples with more realistic perturbation sizes.
3. The experiments should be improved further.
   * The number of adversarial examples is too small to demonstrate some distribution. The experiments need to include a significantly larger number of adversarial examples to provide a reliable empirical validation of the theory. The current sample size is insufficient to draw any meaningful conclusions about the distribution of eigenvalues.
   * The experiment setup is quite arbitrary. Different architectures and attacks are used for different datasets. This makes it difficult to compare the results across datasets and to generalize the findings. A more systematic experimental design is needed, where the same architectures and attacks are used across different datasets, or at least a clear justification for the choice of different setups.
   * The choice of attack algorithms (DeepFool and FAB) also seems uncommon. It is better to use simpler and common attack algorithms. While DeepFool and FAB are valid attack methods, they are not as widely used as FGSM or PGD. Using more common attacks would make the results more accessible and comparable to existing literature.

### Questions
1. Can the authors provide more evidence about the significance of the theoretical findings? You may refer to more existing papers that reflect the findings, or you can provide a more detailed impact statement.
   * I can see that the authors mentioned (Tramer, 2022) as a detection method that the theoretical findings could inspire. Can the authors provide more details about how this detection method relates to your findings?
2. In my opinion, characterization of the convergence rate is a necessary part that completes the paper. Statements that hold only at the limit are too weak to be accepted.
3. Comments regarding the experiments.
   * I understand that the experiments require enormous computation, but the number of adversarial examples is too small to say anything about the distribution.
   * Do you have some specific reason for using DeepFool or FAB to generate adversarial examples? If the experiments take a long time, why don’t you try simpler attacks, such as FGSM or PGD with a small number of iterations?
   * Why do you use different network architectures and attack methods for each dataset? If you have experimental results for all the other combinations (e.g., VGG architecture on MNIST, DeepFool attack on CIFAR-10, etc.), you may put them in the Appendix and refer to the Appendix. If you don’t provide those results, it looks like you are cherry-picking the best combinations and hiding some negative results.

### Soundness
3

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
This paper provides one theoretical result that substantiate the original hypothesis raised in Szegedy's 2014 paper. This research paper is based on the formulation of NN as specific instances of kernel machines, and it adopts the perspective that the introduction of an adversarial example can be regarded as a modification of the empirical data distribution derived from the training set, expanded to incorporate the adversarial example.

The results include a mathematical explanation for that while NN demonstrate strong generalisation to novel test examples, they are still susceptible to attacks, because adversarial examples have measure zero in the limit where they become infinitely close to any test example sampled from the original data distribution. There also numerical experiments conducted that align with the theory.

### Strengths
This paper provides a relatively new perspective on explaining adversarial examples in NNs.
There is an explainable math framework.

### Weaknesses
The paper made a strong assumption that the adversarial examples are close to the data points.

Experiments are relatively insufficient, for example, there are only experiments over two specific classes of both MNIST and CIFAR-10 datasets.

### Questions
Is there any numerical/theoretical comparison between this theory and other explanations of the frangibility of NN networks? Why do you think this paper has a better interpretation?

### Soundness
3

### Presentation
2

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
This article mainly uses Mercer theorem to provide two theorems about the adversarial samples. The Theorem 3.1 shows that $x'$ is an adversarial exampls if and only if the density of Mercer’s eigenvalues which based on the network and $x'$ is not integrable near zero. The Theorem 4.1  shows that adversarial examples are zero measure. And last, author gives some experiments.

### Strengths
1, This article attempts to understand adversarial samples from the perspective of Kernel functions, and demonstrates the characteristics (Th3.1) and density (Th4.1) of adversarial samples. These two research questions are undoubtedly important.

2, The proof of the theorem is clear.

3, Nice write and easy to follow.

### Weaknesses
1, In my opinion, Theorem 3.1 seems to provide a method for determining whether a new sample is an adversarial sample by using the feature vectors of the samples in the training set and the new sample. Moreover, this method seems quite cumbersome, I couldn't see the importance of it.

2, Th4.1 seems obvious. The author's definition of adversarial samples is a sample that is misclassified near a correctly classified sample (line 161), and the network is Lip continuous, so there should be a small neighborhood around each correctly classified samples so that the points in the neighborhood are naturally correct. From this perspective, theorem 4.1 is clearly established.

### Questions
My biggest question about this article is the importance of the results given by the two theorems.

### Soundness
3

### Presentation
3

### Contribution
2
