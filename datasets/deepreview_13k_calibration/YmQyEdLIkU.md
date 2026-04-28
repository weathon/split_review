# Adversarial Attacks as Near-Zero Eigenvalues in The Empirical Kernel of Neural Networks

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Adversarial examples ---imperceptibly modified data inputs designed to mislead machine learning models--- have raised concerns about the robustness of modern neural architectures in safety-critical applications. 
In this paper, we propose a unified mathematical 
framework for understanding adversarial examples in neural networks, corroborating Ian Goodfellow's original conjecture that 
such examples are exceedingly rare, despite their presence in the proximity of nearly every test case. By exploiting results from Kernel Theory, we characterise adversarial examples as those producing near-zero Mercer's eigenvalues in the empirical kernel associated to a trained neural network. 
Consequently, the generation of adversarial attacks, using any known technique, can be conceptualised as a progression towards the eigenvalue space's zero point within the empirical kernel.
We rigorously prove this characterisation for trained fully-connected neural networks under mild assumptions on the nonlinear activation function, thus
providing a mathematical explanation for the apparent contradiction of neural networks excelling at generalisation while remaining vulnerable to adversarial attacks. 
In practical experiments conducted on the MNIST dataset, we have verified that adversarial examples generated through the widely-used Deep Fool algorithm do, indeed, lead to a shift in the distribution of Mercer's eigenvalues toward zero. These results are in strong agreement with predictions of our theoretical framework.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies a novel interpretations of adversarial attacks as points that induce near zero Mercer eigenvalues in the kernel formed via the inner product of empirical feature maps (i.e. the activations at the penultimate network layer). The authors show under strong assumptions of locality that the set of adversarial examples is measure zero under the training data distribution, explaining why such points are practically never observed in the natural world. Preliminary experiments support the theoretical claims.

This reviewer was admittedly unable to check the details of the proofs to ensure correctness.

### Strengths
This paper proposes a new mathematical explanation for the existence of adversarial examples through the application of kernel methods. Most hypotheses to date about this phenomena have lacked formal proofs. A successful mathematical model for adversarial examples could have significant impact by informing techniques to improve adversarial robustness.

The paper explains that neural networks generalize in the real world because the set of adversarial examples is measure zero. This proof supports a decade-old conjecture by Goodfellow et al.

The paper does an excellent job framing the challenge and decade-long history of adversarial examples. Notation is nicely defined, consistent, and clear throughout the paper.

### Weaknesses
The paper is narrow in scope and parts of the paper appear to be hastily written. It is unclear whether the contribution is complete enough to justify a top-tier publication. In particular, the fact that the paper limits its consideration to adversarial points that are infinitesimally close to data points is probably unrealistic. This local limiting assumption significantly restricts the practical relevance of the theoretical results, as adversarial examples are often found at a non-negligible distance from the training data manifold. The paper needs to address the implications of this assumption more thoroughly.

The definition of adversarial examples appears a bit different than the usual definitions, relying on a local limiting assumption. Some work needs to be done to explain the relationship between this paper’s definition and the working definition used of the broader community. The authors should explicitly discuss how their definition relates to the standard notion of adversarial examples, which typically involves a perturbation within a bounded $L_p$ norm. The current definition, based on a limiting process, makes it difficult to directly compare with existing literature and practical attacks.

The figures are poorly presented, and captions could be clarified. The paper says “Our results, however, are currently only directly applicable to FCNs and regression tasks. Nevertheless, we anticipate that the core insights from our research could be extended to encompass classification tasks as well as other neural architectures; this is a clear path for future research.” It is not clear in the experiments that the authors are training regression tasks on MNIST, if this is the case, this needs to be clarified in the paper. The experimental setup lacks sufficient detail, making it hard to reproduce the results and assess the validity of the claims. The choice of using regression on MNIST is unusual and needs further justification, especially given that adversarial attacks are more commonly studied in the context of classification.

Small issues:
* Please check for style, e.g. correct use of \citet and \citep.
* At the end of Section 1, the authors say they “estimated the integral of relevant quantities near zero.” Please make this more specific to outline contributions up front.
* Space before comma 2nd line from the bottom on page 1.
* At the end of Section 6, add a citation for the claim “Researchers have demonstrated that a technique involving the iterative elimination of the dominant eigenvalue direction in the Fisher Information Matrix leads to the generation of adversarial examples.”

### Questions
1. Are there geometric interpretations that your theory provides?
2. Are the authors proposing that this method could serve to identify adversarial examples? If so, is there any contention with [1]?
3. The notation $(x^*, y^*) \sim p$ is strange from a probabilistic perspective. Isn’t there some probability mass on any point $x^*$? It also appears you are assuming no label noise (i.e. the labeling function $y(x)$ is deterministic).
4. Is it really necessary to limit this paper to the consideration of fully-connected layers, or is a Lipschitz assumption sufficient?

[1] Tramer, Florian. “Detecting adversarial examples is (nearly) as hard as classifying them." In International Conference on Machine Learning. 2022.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies adversarial examples in the context of deep supervised learning and aims to show that adversarial examples are of low probability. The paper introduces a kernel-based framework to analyze adversarial examples, connecting adversarial examples to minor Mercer’s eigenvalues in the empirical kernel matrix of the neural net. Based on a definition of adversarial examples in section 2, the paper proves Theorem 1 showing that when the attack radius $\epsilon$ is approaching $0$ the existence of an adversarial example means the density function of the kernel eigenvalues divided by $\lambda^2$ is not integrable and uses this result to show in the limit case $\epsilon\rightarrow 0$ the adversarial examples have zero probability. Some numerical results on MNIST data and DeepFool attacks are presented in the paper.

### Strengths
1- The paper applies a kernel-based framework to analyze adversarial examples which I find interesting. I appreciate the authors' idea of connecting the Mercer eigenvalues to adversarial examples.

### Weaknesses
1- The paper's presentation should be improved. The theory sections are abstract and hard to follow in their current form. I think this is because the authors present the results in the most general and abstract way possible and also include the theorem proofs in the text, which makes the paper difficult to read for an average machine learning researcher. 

2- Theorem 1 is an asymptotic result and holds when the attack radius $\epsilon\rightarrow 0$. This could limit the implications of the theorem. Furthermore, the statement of Theorem 1 indicates an implicit dependence on the choice of adversarial example $\mathbf{x}'$. The theorem states "In the limit $\epsilon \rightarrow 0$, there exists an $\epsilon_0$ such that for all $\epsilon \leq \epsilon_0$, ...", but the choice of $\epsilon_0$ seems to depend on the specific $\mathbf{x}'$ considered. This implies that the asymptotic guarantee might not hold uniformly for all $\epsilon \leq \epsilon_0$ where $\epsilon_0$ is independent of the adversarial example.

3- The definitions and notations in sections 2 and 3 are in some cases vague and raise questions: a) In the definition of adversarial examples, the role and determination of the function $f(\epsilon)$ is unclear. The definition only states the condition $\lim_{\epsilon\rightarrow 0}f(\epsilon) = \infty$, which is insufficient. For any fixed $\epsilon > 0$, one could construct a function $f$ that satisfies this condition for an observed dataset, leading to a trivial satisfaction of the adversarial example definition for a perturbed $\mathbf{x}'$. It is crucial to clarify whether $f$ is determined based on the dataset $\mathbf{X}, \mathbf{y}$ or if it is chosen independently. b) In Theorem 1, the definition of $P_{\mathbf{X}'}$ (with the prime) is ambiguous. Is it a Dirac delta function concentrated at $\mathbf{x}'$, or a continuous density function related to the data distribution $P_\mathbf{X}$? c) The phrase "In the limit $\epsilon\rightarrow 0$, .... " in Theorems 1 and 2 needs further clarification. Does it mean there exists an $\epsilon_0 > 0$, independent of the choice of $\mathbf{x}'$, such that the statement holds for every $\epsilon \leq \epsilon_0$? d) The statement "such that $|| \mathbf{x}- \mathbf{x}'||\le \epsilon$ for some example $(\mathbf{x}^*,y)\sim p$" requires a precise mathematical definition. If $p$ is a continuous distribution, each point in its sample space has zero probability. Therefore, whether $(\mathbf{x}^*,y)$ belongs to the support set of $p$ or not does not affect its zero likelihood of being sampled from $p$. The theorem needs to elaborate on the meaning of this statement within the context of continuous probability distributions.

### Questions
Please see the questions in the previous part.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a possible explanation for the existence of adversarial examples which allows for the emergence of the property that adversarial examples are hard to find (or does not occur naturally in test time).

As for existence, the paper proposes that an adversarial example is a point $x'$ in an $\epsilon$-neighborhood of a natural sample $x^*$ for which the squared error $(y(x^*)-y(x'))^2$ diverges as $\epsilon\to 0$. The paper then proves that, for this definition of an adversarial example, the eigenvalues of the eigenfunctions of the Mercer's kernel vanish. Equivalently, $\lim_{t\to0}\int_t^\infty\frac{1}{\lambda^2}\mathrm{d}\mu(\lambda)=\infty$. Next, the previous theorem is utilized to show that the measure of adversarial examples vanishes as $\epsilon\to0$.

Given the computational constraints, the predictions of the theorems are verified empirically by considering a binary classification of 0 and 1 digits in the MNIST dataset.

### Strengths
### Originality:
Even though some aspects of the proposal appear in the literature, the paper adds an original perspective on the existence of adversarial examples from the point of view of kernels.

### Quality:
The paper is exceptionally well-written. The assumptions and definitions are formally expressed, and claims of the paper is presented in concise steps and a rigorous manner.

### Clarity:
The paper is clear in its goals and provides enough background for the average reader to understand the logic behind the claims.

### Significance:
The proposed theorems could prove to be consequential in interpretation and mitigation of adversarial examples phenomenon.

### Weaknesses
### Minor:
- The axis of the figures does not bear any labels, and the captions are also a little encrypted.

- The low-probability pockets perspective is credited to Goodfellow in the abstract, which is wrong. The main text however correctly credits Szegedy.

### Major:
- My main objection with the presented argument is that I am not sold on the definition of an adversarial example in the paper. Specifically, I think that the limiting process of $\epsilon\to0$ in the definition is flawed. This limiting process effectively adds two equal samples to the training set with two different targets. I am under the impression that the vanishing of the eigenvalues is a consequence of this construction ($K(X,X)$ wouldn't be invertible) and is not associated with the robustness of the network.

- Assuming that my understanding of the limiting process is correct, the paper has rediscovered the robustness-accuracy trade-off as depicted in [A] (this is not a critique exactly). Zhang et al. in [A] propose that adversarial examples and natural samples overlap in the input space and that is why we observe a trade-off between robustness and accuracy in adversarial training. I think the paper should at the very least mention [A]. An alternative to the proposal of Zhang et al. that might be relevant is [B].

In the proof of theorem 1, the paper assumes that $(\Phi(X)\Phi(X)^T)^{-1}$ is bounded, but my understanding is that the assumption of $\epsilon\to0$ and $(y-N(x'))^2\to\infty$ is the same as assuming $\Phi(x'\cup X)\Phi(x'\cup X)^T$ is not invertible (because there is some $x$ in the dataset that has been added to the set twice, but with different targets). Consequently, generalization error is not the source of the error that is being analyzed in the paper.

### Questions
- The limiting process that constructs $\int_t^\infty\frac{1}{\lambda^2}\mathrm{d}\mu(\lambda)$ appear to be a Riemannian sum. However, I am curious to know if $M\to\infty$ is the same as asserting that the size of the training set approaches infinity.

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
This paper makes contributions to the theoretical understanding of the adversarial examples. The authors use kernel theory, Mercer’s theorem in particular, to explain the adversarial examples. Specifically, the authors first prove that adversarial examples shift the Mercer’s spectrum of the empirical kernel so that the near-zero density of the Mercer eigenvalues is high. Extending the first theorem, the authors also explain the reason for the denseness of adversarial examples, i.e., adversarial examples are unlikely to appear in the test set, but they exist near every test sample. Lastly, the authors demonstrate their findings with small experiments.

### Strengths
1. I briefly checked the proofs and the proofs look to be correct to me.
2. To the best of my knowledge, this is an original work that makes theoretical progress in the field of adversarial machine learning. Considering that such theoretical works are rare in this field, the authors’ findings are valuable.

### Weaknesses
1. As mentioned in Section 7, the theoretical result only covers limited neural network architecture, i.e., fully connected layers. This significantly restricts the applicability of the findings to modern deep learning architectures, which often incorporate convolutional, recurrent, or attention-based layers. The theoretical framework should be extended to encompass these architectures to increase its practical relevance.
2. This work is a theory-intensive paper, however, experiments can be improved further.
    - For example, the authors can run more experiments on artificial data to reduce the heavy computation of diagonalization and then validate the theory more thoroughly. The current experiments are limited in scope and do not fully explore the parameter space or different data distributions. More extensive experimentation, including varying the dimensionality of the input data and the size of the neural networks, is needed to validate the theoretical claims more robustly.
    - DeepFool algorithm is an old attack algorithm and cannot represent all the existing attacks (that are likely to be more powerful than DeepFool). The authors should perform similar experiments with other attack methods. The choice of DeepFool limits the generalizability of the experimental results. It would be beneficial to include experiments with more recent and powerful attack algorithms, such as Projected Gradient Descent (PGD) or Carlini & Wagner (C&W) attacks, to ensure the findings hold under stronger adversarial perturbations.

### Questions
1. I cannot understand the reason for the assumption on the layer widths, i.e., all layers except the last layer have the same width $N$, because the proof mainly uses the empirical feature map that does not involve the intermediate layer output. Is this assumption necessary for the theorem? If so, how do you justify the assumption on the layer width?
2. Minor comments
    - According to the [formatting instruction](https://github.com/ICLR/Master-Template/raw/master/iclr2024.zip), in-text citations (`\citet`) and citations in parentheses (`\citep`) should be used differently, but I see only in-text citations in the paper writing. Please fix the citation style.
    - I don’t think that Figure 1 is the best way to show the eigenvalue distributions. Why do you waste space by having a y-axis ranging from 0 to 1?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
