# Robustness Guarantees for Adversarial Training on Non-Separable Data

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 3, 6, 6

## Abstract
Adversarial training has emerged as a popular approach for training models that are robust to inference time attacks. However, our theoretical understanding of why and when it works remains limited. Prior work has offered convergence analysis of adversarial training, but they are either restricted to the Neural Tangent Kernel (NTK) regime or make restrictive assumptions about data such as linearly realizability. In this work, we provide convergence and generalization guarantees for adversarial training of two-layer networks of any width on non-separable data. Our analysis goes beyond the NTK regime and holds for both smooth and non-smooth activation functions. We support our theoretical findings with an empirical study on synthetic and real-world data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies convergence and generalization guarantees of adversarial training of two-layer neural networks with arbitrary width on non-separable data. It provides theoretical guarantees on both smooth and non-smooth activation functions. For moderately large networks, the paper shows the robust test error behaves differently on different perturbation budgets. The theoretical findings are supported by experiments on both synthetic and real-world data.

### Strengths
The paper is well-written. References are well cited with detailed comparisons.

### Weaknesses
The additional assumption in Section 3, which states that $\phi'(z)z$ and $\phi(z)$ are close, is hard to grasp. Is it another notion on the Liptshitzness on the activation function? How strong is it to assume that $c_1,c_2=0$ in ReLU network, for example? The connection between this assumption and the homogeneous property is not clearly explained. It's unclear how this assumption is used to derive the convergence results, and whether it is a necessary condition or a sufficient one. The paper would benefit from a more detailed explanation of the role of this assumption in the overall proof strategy. Furthermore, the practical implications of this assumption are not discussed, making it difficult to assess its relevance in real-world scenarios. It would be helpful to see examples of activation functions that satisfy this condition and those that do not, beyond the ReLU case, to better understand its scope and limitations.

### Questions
See discussion in Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper provides a theoretical analysis of adversarial training. Specifically, it establishes the convergence guarantees for adversarial training of a specific two-layer neural network and provides generalization guarantees for both the clean test error and the robust test error. Additionally, the paper conducts experiments to validate the theoretical results.

### Strengths
Compared to previous theoretical work on adversarial training, this paper does not require some strong assumptions such as linear separability or lazy training.

### Weaknesses
1: The setting, proof approach, and techniques in this paper completely follow the previous works [1, 2] for benign overfitting, but this is a high-dimensional data setting that is different from the typical environment of robustness problems.

2: The technical difficulty of this paper is mainly the processing of the adversarial part. However, since the attack intensity $\alpha$ needs to take a very small value, such an expansion does not have great technical difficulty and contribution. Specifically, for smooth activation functions, the perturbation size is constrained to be smaller than the distance from the data center to the decision boundary, while for non-smooth activations, it needs to be significantly smaller. This limitation on perturbation size diminishes the practical relevance of the analysis.

3: While the authors claim that the results in this paper are applicable to any width, for overparameterized networks which $m\gg n, d$, the results presented may lack significance. The theoretical guarantees rely on assumptions B.3 and B.7, which implicitly require both the number of data points $n$ and the data dimensionality $d$ to approach infinity as the network width $m$ increases. This implies that for fixed $n$ and $d$, the results do not hold for arbitrarily large network widths.

4: The discussion of overfitting with adversarial training is unconvincing. Such a discussion can only show that the results of this paper are not inconsistent with the phenomenon in [3], but it still cannot provide a reasonable explanation for the phenomenon in [3].

### Questions
I believe that in the setting of this paper, which is similar to the [1, 2] with a relatively small $\alpha$, one can potentially obtain a similar bound for robust error even without using adversarial training, by using standard SGD. I wonder what the author's perspective on this is.

[1] Spencer Frei, Niladri S Chatterji, and Peter Bartlett. Benign overfitting without linearity: Neural network classifiers trained by gradient descent for noisy linear data. In Conference on Learning Theory, pages 2668–2703. PMLR, 2022.

[2] Xingyu Xu and Yuantao Gu. Benign overfitting of non-smooth neural networks beyond lazy training. International Conference on Artificial Intelligence and Statistics, pages 11094–11117, 2023.

[3] Leslie Rice, Eric Wong, and Zico Kolter. Overfitting in adversarially robust deep learning. In International Conference on Machine Learning, pages 8093–8104. PMLR, 2020.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors consider adversarial training for neural networks of one hidden layer and prove that, under certain assumptions, it converges to an arbitrarily small robust loss. An important aspect of the theoretical results of the paper is that they hold  for NN of finite width. The results are empirically investigated on an example with a synthetic dataset.

### Strengths
- Providing convergence guarantees for adversarial training of neural networks is certainly a problem of interest for the ICLR community

- In contrast with the existing literature, which mostly focus on providing theoretical results in the infinite-width regime, the results of the authors also hold for neural networks of finite width. I see this as an important contribution

- The paper is well written

### Weaknesses
 - My main issue with the submission is that the assumptions made by the authors are quite restrictive for most applications. For instance, the assumption that the number of training data is much lower than the dimension of the input space, but still larger than C log(1/\delta) is restrictive for many applications where neural networks are employed and where the amount of data is generally larger than the input dimension. This assumption limits the applicability of the theoretical results to scenarios where data is scarce relative to the input dimensionality, which is not the typical setting for many deep learning tasks. Furthermore, the constant C, which depends on several other parameters, is not explicitly defined or bounded, making it difficult to assess the practical implications of the assumption. 

- Experimental results are only limited to a synthetic example. The authors also report some experiments on MNIST on the Appendix. Why not reporting them in the main text? The lack of experiments on real-world datasets in the main text makes it difficult to evaluate the practical relevance of the proposed method. The synthetic dataset, while useful for initial validation, does not fully capture the complexities of real-world data distributions and the challenges of adversarial training in such settings.

### Questions
- Where the constant C in Assumption 1 comes from? Can you bound it for some specific applications?

- Why in the experiments in Figure 2 robust accuracy seems to decrease with increasing the dimension d for a fixed perturbation ratio? Is this in line with your theoretical results?

Minor:

- why do you need to overload the notation for the l_2 norm in the first line of Page 3. Can't you simply use always || \cdot || ?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides convergence and generalization guarantees for adversarial training of two-layer neural networks on non-separable data, for both smooth and non-smooth activate functions. The experimental results are consistent with the theory.

### Strengths
- This paper takes a great step toward understanding adversarial training (non-smooth activate functions, non-separable data, and goes beyond the NTK regime)

### Weaknesses
 - The model is a two-layer neural network with the weights for the second layer fixed, which is too simple compared with DNNs. And the assumption about the data is too simple.
- It seems that the paper [1] is very relevant to this work, detailed discussion about the similarities, differences, and the superiority of this paper should be added.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
