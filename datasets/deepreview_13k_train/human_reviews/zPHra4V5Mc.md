# Feature Averaging: An Implicit Bias of Gradient Descent Leading to Non-Robustness in Neural Networks

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
In this work, we investigate a particular implicit bias in the gradient descent training process, which we term “Feature Averaging”, and argue that it is one of the principal factors contributing to non-robustness of deep neural networks. Despite the existence of multiple discriminative features capable of classifying data, neural networks trained by gradient descent exhibit a tendency to learn the average (or certain combination) of these features, rather than distinguishing and leveraging each feature individually. In particular, we provide a detailed theoretical analysis of the training dynamics of gradient descent in a two-layer ReLU network for a binary classification task, where the data distribution consists of multiple clusters with orthogonal cluster center vectors. We rigorously prove that gradient descent converges to the regime of feature averaging, wherein the weights associated with each hidden-layer neuron represent an average of the cluster centers (each center corresponding to a distinct feature). It leads the network classifier to be non-robust due to an attack that aligns with the negative direction of the averaged features. Furthermore, we prove that, with the provision of more granular supervised information, a two-layer multi-class neural network is capable of learning individual features, from which one can derive a binary classifier with the optimal robustness under our setting. Besides, we also conduct extensive experiments using synthetic datasets, MNIST and CIFAR-10 to substantiate the phenomenon of feature averaging and its role in adversarial robustness of neural networks. We hope the theoretical and empirical insights can provide a deeper understanding of the impact of the gradient descent training on feature learning process, which in turn influences the robustness of the network, and how more detailed supervision may enhance model robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper provides a theoretical analysis of the relation between feature dependency and adversarial robustness. The authors studied a two-layer ReLU network on the simulated data and derived that the gradient descent tends to learn averaged features instead of isolated/robust ones. The results were proved thoroughly. Then, the paper provides a test on the derived theory on real-world datasets, showing that by incorporating more precise training labels, the model can learn isolated features rather than mixed ones, therefore achieving better adversarial robustness.

### Strengths
The paper gives very thorough theoretical study of the problem. The hypothesis, assumptions and derivation are reasonable and sound. The results matched with the intuition well.

### Weaknesses
The theory developed in this paper is phenomenological. It can be further improved if systematic and quantifying criteria can be built to design an optimization method that can help improve the robustness. The current analysis, while thorough, primarily describes the observed behavior of gradient descent rather than providing a prescriptive approach for enhancing adversarial robustness. The theory lacks a clear mechanism for translating the understanding of feature averaging into actionable strategies for training more robust models. Specifically, the paper does not offer a concrete method for identifying or preventing the formation of these averaged features during training, which limits its practical applicability. The empirical validation, while supporting the theory, is confined to relatively simple scenarios and does not fully address the complexities of real-world, high-dimensional data.

### Questions
1. The feature average is clearly defined in two-layer networks - the linear input combinations. However, in the deeper layer, such a definition does not seem reasonable. How do we analyse features in this case? Can the authors provide one or more examples, conceptually or mathematically, about how features are averaged in deeper neural networks?

2. In image tasks, reasonable and robust features are often local and isolated. However, there are other scenarios where the features are required to have global or long-term dependency. Such as time series, and natural language. In those cases, it seems like the real interpretable and robust features are some "mixing" of the original data. Therefore:
 a) How should we define the feature mixing in those cases?
 b) Would the theory developed in the paper be effective in those circumstances? If so, how to measure or validate? If not, should there be possible modification can improve the adaptability of the theory?

3. There are researches that have out that, the neural network tends to learn low-frequency features (which are nonlocal and varied smoothly) more effectively than high-frequency features. Some connect such behaviour to the generalization capacity of over-parameterized neural networks. Do you think there is any relation between this theory and the ones developed in this paper? I want to hear about the comments of the authors. 
I list a few papers for reference:
Xu, Zhi-Qin John, et al. "Frequency principle: Fourier analysis sheds light on deep neural networks." arXiv preprint arXiv:1901.06523 (2019).
Xu, Zhi-Qin John, Yaoyu Zhang, and Tao Luo. "Overview frequency principle/spectral bias in deep learning." Communications on Applied Mathematics and Computation (2024): 1-38.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper analyzed the training dynamics of gradient descent on a simplified two-layer ReLU networks in a binary supervised classification task, where the feature vector is sample from a gaussian mixture model with equal probability for K>2 components and the label are masked as 2 categories. The main result in section 4 showed that, under some regulatory assumptions and choices of hyper-parameters, the learned network turns to a feature averaging network, which has low generalization error but is not robust to perturbation of dataset.

### Strengths
-This paper focuses on explaining the adversarial robustness of neural networks in classification problem, which of course is an important topic in ML/DL community.

-This paper is generally well-written and logically organized with clear notations, assumptions, and detailed references to prior works with comparisons

-This paper’s idea is intuitive: this paper characterizes the “approximate linearity” in networks under NTK assumptions as adversarial non-robustness in terms of Feature averaging.

### Weaknesses
 - Too many strong and unrealistic assumptions are used. First, the number of neurons $M=2m$ assumed to be finite as the number of clusters of features in assumption 4.3. It is against the purpose of using the neural tangent kernel (NTK) theory to approximate infinite wide neural networks. Thus, the result in this paper is limited since “training deep neural network is a highly non-convex and over-parametrized optimization problem”. The analysis would benefit from a discussion of how the finite width assumption impacts the applicability of the results to more realistic, overparameterized networks. Second, as the solution to adversarial robustness, “fine-grained supervision” suggests including the original cluster labels for all data points, which is extremely unrealistic, because the response is simply assigned from the cluster labels. It is not surprising that there is an improvement in adverbial robustness as the exact latent information is provided. Feature decoupling is a simple result as the network can learn each cluster’s mean given the cluster labels.

- The evidence of feature averaging is shown Figure 2 as the strong correlations/cosine value between cluster’s mean and network weights, but the scale of correlations is not consistent. In particular, the results from CIFAR-10 are not convincing, where the average cosine value can be lower than 0.1.

### Questions
-Minor issues in notations: Big $O$ notation on line 185 is different from the others; $Theta$ notation is not defined.

-Why does strong correlations indicate the existence of feature averaging? Is there a rigorous proof? How do you define the threshold of having a strong correlation?

-Proposition 4.8 is used as an example of “adding more fine-grained supervision signals does not trivially lead to decoupled features and robustness”, but it does not follow the setup of your analysis, since $h=1$. How is this multi-class network obtained? Why is its parameter assumed to be the combination of $mu_s$?

### Soundness
3

### Presentation
4

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
This paper studies the implicit bias of gradient descent, which the authors call 'Feature Averaging' by theoretically analyzing two layer ReLU network with only a learnable first layer, under a specific data distribution - binary data having multiple clusters with orthogonal cluster centers. 
Under gradient descent, weights of neurons in the hidden layer converge to an average of the cluster centers, resulting in a non-robust network. Additionally, they also prove that with more fine-grained cluster information, the network can learn a robust solution for the binary classification problem.

### Strengths
* The theoretical analysis of the finite time gradient descent dynamics is thorough in the feature learning regime. 
* This paper is an interesting contribution in understanding the robustness of neural networks from optimization perspective. The analysis also aided in proving a conjecture. 
* The paper is well written and the presentation is clear.

### Weaknesses
 * The assumptions on the data (orthonormal equinorm and multi-cluster) is restrictive. Specifically, the requirement that cluster centers are exactly orthonormal is a strong constraint that is unlikely to hold in real-world datasets. While the multi-cluster assumption is plausible, the strict orthogonality and equal norm conditions limit the applicability of the theoretical results. This raises concerns about how well the 'feature averaging' phenomenon generalizes to more realistic scenarios with non-orthogonal and varying norm cluster structures.
* The proof is detailed and thorough for two layer ReLU with only one learnable hidden layer. Extending to deeper networks seems challenging. The analysis focuses on a simplified architecture where only the first layer is trained. This is a significant limitation, as many practical neural networks involve training multiple layers. The dynamics of gradient descent in deeper networks can be significantly more complex, and it is unclear if the feature averaging phenomenon would still be the dominant behavior. The analysis also does not address the impact of different activation functions or network architectures.

### Questions
1. In the fine-grained supervision case of the multi-cluster data, I understand that the binary classification using the multi-class network results in a robust solution. But, I wonder if the learned network would still be non-robust for the multi-class classification. 
2. It is not an ask to prove the following. I am only curious to understand and know the authors thought. The fine-grained supervision setting can also be seen as learning a more expressive/complex classifier (learn k classes to do binary classification). Then, can the authors comment on the adversarial min-max training? Would similar feature decoupling, ie the weight of each neuron is aligned with one cluster feature, happen naturally if one does adversarial training of the binary class data?

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
5

### Summary
This paper theoretically studies the robustness of two layer neural networks under a specific data distribution that consists of $k$ clusters in $\mathbb{R}^d$ and the target consists of deciding on which group of clusters the input belongs to (binary classification). The authors show that these networks tend to learn an "averaging" solution (i.e., the first-layer weights encode the averages of the clusters), making the networks susceptible to $\Omega(\sqrt{d / k})$ perturbations of the input (despite the existence of networks capable of tolerating $O(\sqrt{d})$ perturbations). Motivated by this observation, they propose modifying the training process by using each example's cluster vector as the label, and they prove that this approach indeed yields optimally robust networks. Finally, the paper presents experiments with both synthetic data and image classification benchmarks that contextualize the theoretical findings.

### Strengths
This is a good paper, and it was a pleasure to read and review. I would like to highlight the following contributions:

- Important topic: The interplay between the implicit bias of optimization and robustness is, in my opinion, an important area of study.
- Finite time theoretical analysis of neural networks trained in the various settings: The paper rigorously analyzes the training trajectory of the networks. I enjoyed reading and learning about interesting techniques, such as the ones outlined in Section C.2. In general, the Appendix of the paper is exceptionally polished and the results are easy to follow and verify (to the extent that this was possible during the review process - the paper is 67pages long).
- Interesting suggestion on providing additional supervision during training for improved robustness: I found this observation interesting and the experimental results seem to suggest that these ideas may generalize beyond the toy distribution considered in the paper's analysis.

### Weaknesses
1) The main conceptual observation does not appear to be new. To my understanding, Frei et al. (2022) showed that neural networks trained with gradient descent on this distribution are not robust to $\ell_2$ perturbations of the input due to the implicit bias of optimization. In lines 153-171, the authors argue that their work differs from prior work because they do not explicitly analyze the properties of the KKT point of the max-margin problem and instead perform a finite-time analysis. Furthermore, they argue that convergence to the KKT points might be slow. However, we know from Liu & Li (2020) that these conditions are approximately satisfied as long as there is a positive margin. Thus, approximate results are conceptually consistent with the KKT analysis. Additionally, I believe that the fact that the network reaches an "averaging" solution can be deduced from the KKT equations in Frei et al. (2022)—see also (Q1).

2) The paper argues that "feature averaging is a principal factor contributing to non-robustness of neural networks" (line 014). However, it focuses on one type of perturbations. While the authors provide evidence in this direction for $\ell_2$ perturbations in a simple distribution (& experimental results in more complicated settings),  it is not clear that this holds more broadly. Note that the model’s solution is exceptionally contrived, as all neurons (within each group) converge to the same solution. See also (Q2, Q3).

2) While the paper is well-written, I found the discussion on prior work somewhat insufficient. I would appreciate a bit more clarity on what is novel about the first part of the contributions (i.e., the proof that networks reach feature-averaging solutions). Furthermore, in line 110, the authors mention the work of Min & Vidal (2024) and their conjecture for the first time. It would be more appropriate to introduce this work and its conjecture earlier in the introduction, making it easier for readers to appreciate the contribution.

4) A list of non-significant typos/grammatical errors I spotted:
- line 091: features-> feature
- line 107: exists-> exist
- line 167: analyze -> analysis
- line 261: neural -> neuron
- line 893: echos -> echoes
- line 1098: We -> we
- line 1100: margin -> margins
- lines 1307-1310 require rephrasing (they do not make sense),

### Questions
Q1: Can the fact that the network reaches an "averaging" solution be deduced from the KKT equations in Frei et al. (2022)?

Q2: The implicit bias of GD for this problem in 2-layer neural networks is undesirable for $\ell_2$ robustness. What about $\ell_\infty$ perturbations? It seems that this bias would help for $\ell_\infty$ perturbations, in contrast to the feature decoupling solution $NN_{FD}$. I would appreciate your thoughts on this.

Q3: Relatedly, would it be possible to measure robustness in the experiments on CIFAR10/MNIST against $\ell_\infty$ perturbations? If there is evidence for larger $\ell_\infty$ robustness when training with additional supervision, then this would make the authors' claims much stronger.

Q4: Figure 3: How do you measure perturbation radius? If, for example, you normalise MNIST images to be between 0 and 1, then a perturbation radius of 2.0 does not make any sense. Can you mention the ranges of the input for MNIST and CIFAR10?

Q5: In line 882, you mention that "In image classification tasks, Ilyas et al. (2019) visualized both robust and nonrobust features.". However, this is not true to the best of my knowledge. I believe there are 2 works that have provided such visualizations [1, 2].

[1]. G. Goh. A discussion of ’adversarial examples are not bugs, they are features’: Two examples of useful, non-robust features. Distill, 2019.
[2] Tsilivis, N. and Kempe, J. (2022). What can the neural tangent kernel tell us about adversarial robustness? Advances in Neural Information Processing Systems 35.

### Soundness
4

### Presentation
3

### Contribution
3
