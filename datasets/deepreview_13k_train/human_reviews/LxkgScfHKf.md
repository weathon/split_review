# Conformal Training with Reduced Variance

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
Conformal prediction (CP) is a distribution-free framework for achieving probabilistic guarantees on black-box models. {CP} is generally applied to a model post-training. Conformal training is an approach that aims to optimize the CP efficiency during training. In this direction, ConfTr (Stutz et al, 2022) is a technique that seeks to minimize the expected prediction set size of a model by simulating {CP} in-between training updates. Despite its potential, we identify a strong source of sample inefficiency in ConfTr that leads to overly noisy estimated gradients, introducing training instability and limiting practical use. To address this challenge, we propose variance-reduced conformal training (VR-ConfTr), a method that incorporates a variance reduction technique in the gradient estimation of the ConfTr objective function. Through extensive experiments on various benchmark datasets, we demonstrate that VR-ConfTr consistently achieves faster convergence and smaller prediction sets compared to baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this work, authors studies conformal training and proposes variance-reduced conformal training which incorporates a variance reduction technique in the gradient estimation of the ConfTr objective function. In particular, it proposes an $\epsilon$ estimator to estimate quantile gradient. Authors also provide the theoretical results of the variance and bias of the proposed estimator, and some numerical studies on synthetic datasets and MNIST dataset.

### Strengths
1. Authors state the problem clearly and then propose a solution, finally provide numerical studies.
2. The discussion is accompanied with sufficient background introduction
3. Authors tackle the high-variance issue in conformal training  and reduce the variance of quantile estimator relaxing the definition of the gradient and using more available samples in estimation.

### Weaknesses
1. Some of the formulas are not clearly explained. In particular, what does the set ${E_{\theta}(X,Y) =\tau_{\tau}}$ represent? It seems $E_{\theta}(X,Y)$ is a random variable, $\tau_{\tau}$ is a scaler, but how to interpret it in ${E_{\theta}(X,Y) =\tau_{\tau}}$? Furthermore, what expectation you take with respect to in equation 11 and 12? The notation is confusing, as it is not clear whether $E_{\theta}(X,Y)$ represents a function of $(X,Y)$ parameterized by $\theta$, or a random variable. If it is a function, then the set notation is unclear. If it is a random variable, then the equality to a scalar is unclear. The expectation in equations 11 and 12 needs to be explicitly defined, specifying the random variable over which the expectation is taken. It is crucial to define the underlying probability space clearly to avoid confusion.
2. How do you the value of $\epsilon$? Can you include some ablation studies to this hyper-parameter? The choice of $\epsilon$ is critical to the performance of the proposed method, and a principled way to select this value is missing. It is not clear how sensitive the method is to this hyperparameter, and without a proper analysis, it is difficult to assess the robustness of the approach. An ablation study is needed to understand the impact of different values of $\epsilon$ on the performance of the method, including both bias and variance of the quantile gradient estimator.
3. What is the per-step computational cost of your algorithm compared to the ConfTr? The computational cost of the proposed method is not discussed in detail. It is important to understand the overhead introduced by the variance reduction technique. A comparison of the per-step computational cost with the original ConfTr algorithm is needed to assess the practical applicability of the proposed method. This should include a breakdown of the computational steps and their associated costs.
4. Can you test your method over larger scale datasets beyond the toy dataset of MNIST? The experiments are limited to relatively small datasets like MNIST. It is not clear how the proposed method would perform on larger, more complex datasets. Testing on larger datasets is crucial to demonstrate the scalability and effectiveness of the method in real-world scenarios. The current experiments do not provide sufficient evidence of the method's applicability in more challenging settings.

### Questions
Please see the weakness above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The submission proposes VR-ConfTr, a variance-reduced conformal training method that enhances the stability and efficiency of conformal prediction by reducing the variance in gradient estimates, which is a key limitation in previous [1]. VR-ConfTr introduces a novel gradient estimator that achieves faster convergence and smaller prediction sets.

---

[1] Stutz, David, et al. "Learning Optimal Conformal Classifiers." International Conference on Learning Representations.

### Strengths
- The length efficiency in conformal prediction is an important research problem. The proposed novel approach addresses significant sample inefficiency issues present in prior methods and stabilizes gradient estimation.

- This is a plug-in algorithm hence the proposed variance reduction technique could enjoy a broad applicability.

- VR-ConfTr demonstrates superior performance across multiple datasets, including MNIST, Fashion-MNIST, Kuzushiji-MNIST, and OrganAMNIST.

### Weaknesses
 - The proposed VR-ConfTr gradient estimation method uses sample splitting, where batch data are divided into calibration and prediction subsets. This approach might introduce sampling instability, particularly with smaller datasets or non-i.i.d. data. The paper does not sufficiently analyze the impact of this splitting on the variance of the gradient estimates, especially in scenarios where the calibration set is small, potentially leading to unreliable quantile estimates and, consequently, unstable training. Furthermore, the authors do not explore alternative sampling strategies, such as using overlapping subsets or adaptive splitting ratios, which could potentially mitigate these issues and improve the robustness of the method.

- Although the paper claims innovation in integrating variance reduction into conformal training, similar variance reduction techniques have already been proposed in gradient estimation contexts (e.g. well-known SVRG in optimization community). The authors fail to convincingly differentiate their work from these established methods, nor do they address why VR-ConfTr is distinct beyond the context of conformal prediction. Specifically, the paper lacks a detailed comparison with existing variance reduction techniques in terms of computational complexity, memory requirements, and convergence properties. A rigorous analysis demonstrating the advantages of VR-ConfTr over these methods, especially in the context of conformal prediction, is missing.

- The empirical results, while presented across multiple datasets, appear selective and limited to low-complexity, classical datasets (e.g., MNIST variants). Conformal prediction applications span far more complex domains, yet there is no evidence here that VR-ConfTr scales or performs effectively on realistic, large-scale datasets. The paper does not provide any analysis of the computational cost and memory usage of VR-ConfTr on larger datasets, nor does it discuss the potential challenges in applying the method to high-dimensional data or complex model architectures. The absence of experiments on more challenging datasets limits the practical relevance of the proposed method.


- The theoretical section of this paper appears hastily constructed (see Questions), which risks undermining the reader's confidence in the proposed methodology and suggests that this submission is not yet ready for formal publication.

### Questions
- The mathematical notation in Theorem 3.1 lacks standardization. Are you intending to use $q_{\epsilon}(\theta)^n$ from (i) and $
[q\_{\epsilon}(\theta)]^n$ from (ii) to both represent the $n$-th power of $q(\cdot)$?

- line 323: the definition of $K(t)$ lacks a right parenthesis

- line 716, the asymptotic equivalence is defined by $a_n \asymp b_n: \lim_{n \to \infty} \frac{a_n}{b_n} = 1$ (in your sense), so we should have $b_n \neq 0$, which is in contrast to your usage like line 719, 745. Besides, "Let"

- line 852: missing a proper definition

- if you let $a_n=nf_n$, shouldn't your (45) turns into $a_{n+1}=(n+1)q f_n+(1-q^n)$ instead of your (46)?

- In my view, the notation in the second line of (50) should begin with $ \preceq$. Also the = in the final line seems unclear to me. While I understand your intention to retain the $\frac{2 - p}{pn} \Sigma_\epsilon$, the remaining terms are somehow ambiguous—how exactly does it equate to your final conclusion?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a new training objective for optimizing for conformal predictive set size, based on the work of (Stutz et al., 2022). By focusing on the computation of the gradients of the loss rather than the loss itself, the authors identify an alternative estimator of the conformal threshold to be incorporated in the loss that is more sample efficient, leading to less noisy gradients, and thus more stable training, faster convergence and better models.

### Strengths
The problem of building models that optimize for conformal predictive set size is a natural one, and yet often left to the sides. Indeed, there are still few works that tackle this problem, and more work on the topic is certainly welcome. The proposed solution is novel and can be of use to a wide audience.

### Weaknesses
I have two major issues with the paper:
1. The mathematical reasoning in the paper does not seem sound
2. Even if they were, the theoretical analysis seems lacking.
Given these two points, the paper could still be held up by a comprehensive empirical analysis. However, while there is some empirical analysis, it is hardly comprehensive, and could be improved on (especially if it is needed in order to compensate for (1.) and (2.)).

On the soundness of the mathematical reasoning:
- The derivatives in equation (5) do not exist. As currently written, the chain rule cannot be applied. Perhaps it can be salvaged with subgradients, though.
- I was unable to understand why (8) holds, or where it comes from.

Lacking theoretical analysis: the authors only prove their reduced variance with one particular estimator, which does not even match the estimator used in the experiments; moreover, this was done under significant simplifying assumptions. If these assumptions were so light as the authors imply, then it should be easy to prove a relaxed version of the theorem that incorporates them. (Change-of-measure inequalities may be useful here.)
This is to the point that I barely consider the paper to have any theoretical analysis.

On the experiments:
- The current visualizations are almost exclusively learning curves. While their presence is welcome, there are probably better ways to visualize, e.g., the variance of the gradients over the course of the training, which the authors claim to have reduced. From the learning curves, it is not entirely clear that these have really been reduced.
- It would be nice to also investigate the conditional coverage of the models. Does using your training objective lead to better conditional coverage? (Even if the answer is 'no', it would still be nice to have this in the supplementary material, and would not count negatively, in my view.)
- The authors should consider more datasets and models -- currently only CNNs on MNIST-like datasets. I suggest the authors also consider:
  - ViTs, still on image data
  - Transformers (e.g., BERT-style) on text classification tasks
  - GNNs for graph-based tasks, e.g., node prediction
Since the paper proposes a new training objective, in the absence of a better theoretical understanding of it (possibly including on its interactions with gradient descent methods), it is important to test it on a wider variety of architectures.

There are also some minor issues:
- The use of $\min_{\theta \in \Theta} L(\theta) := [\cdots]$ can be a bit confusing, as it seems at a first glance that the equality is claimed with regards to the minimum. A better way to write this is $\min_{\theta \in \Theta} L(\theta) \quad \text{where}\ L(\theta) := [\cdots]$.
- In line 317, I suggest avoiding the use of the term 'gradient-boosting estimators'; gradient boosting estimators are an established class of ML models (e.g., XGBoost, LightGBM, etc.). These have little to do with the estimators being constructed in the paper, and caused a fair amount of head-scratching on my end. How about just calling these 'estimators for $\eta(\theta)$'?
- The writing in the proof of lemma 3.1 is rather unorthodox in the context of a paper. Consider avoiding long chains of {in,}equalities, especially, when you feel the need to follow it up with explanations for why the steps of the chain hold (e.g., line 682).
- On tables 1, 2 and 5, use the standard $\mu \pm \sigma$ notation in a single column for average and standard deviation, rather than separating into multiple columns.
- The notation is overall very heavy, probably unnecessarily so. This makes the paper a bit hard to parse.

Finally, it is worth noting that over half of the paper is spent effectively describing the work of (Stutz et al., 2022). Perhaps this can be trimmed somewhat, or better streamlined.

### Questions
My main questions:

- Some clarification on (8) would be appreciated. Why does it hold? The text claims that it comes from differentiating $\ell$, but that does not make sense. Is there a typo?
- How does the derivation of the loss fare in the face of the non-existant derivatives in (5)? (Or do they actually exist and I've missed something?)
- How does the proposed method fare when using the estimator in equation (13) rather than the ranking estimator?

**Score:** the weaknesses (particularly those relating to soundness and the theoretical analysis) seem rather significant to me, making me lean towards rejection. Given their severity, I do not think the rejection is borderline, even if the experimental results seem somewhat positive. Should the reviewers improve their presentation and soundness of their theoretical results, I would be willing to increase my score.

### Soundness
1

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new approach, Variance-Reduced Conformal Training, which adds a variance reduction in the estimation of gradients to improve the efficiency of conformal prediction during training. It is an attempt to sort out the inefficiency problems that appear with other methods like ConfTr, for which the estimation of gradients is problematic because of noise in the data batches. These improvements in the proposal have brought both an increase in the speed of convergence and the efficiency in the size of the sets of predictions, as confirmed by experiments using different benchmark datasets. This effectively preserves probabilistic guarantees to obtain much more compact and reliable prediction sets when compared to baseline models.

### Strengths
1. VR-ConfTr consistently generates smaller prediction sets with better length efficiency than its predecessor, ConfTr, and baseline models.

2. The paper provides a solid theoretical analysis to support the variance reduction claims, offering insights into the bias-variance trade-off involved.

3. The paper is well-written and clearly structured.

### Weaknesses
1. VR-ConfTr relies on a large calibration set to accurately estimate the quantile estimator $\hat{\tau}$ and its gradient $\hat{\frac{\partial \tau}{\partial \theta}}$, which are critical for variance reduction. The accuracy of the quantile estimator and its gradient is directly tied to the size and representativeness of the calibration set. If the calibration set is not sufficiently large, the estimated quantile may not accurately reflect the true underlying distribution, leading to unreliable prediction sets. Furthermore, if the calibration set does not adequately cover the input space, the estimated gradient may be biased, which could negatively impact the performance of the variance reduction technique.

2. While VR-ConfTr improves prediction set efficiency, it introduces additional computational steps, which may slow down training in scenarios with limited computational resources. Specifically, the computation of the $m$-ranking estimator, while claimed to have similar complexity to the gradient of the sample quantile, still involves averaging $m$ derivatives of conformity scores. This additional computation, even if not drastically higher, might become a bottleneck in resource-constrained environments or when dealing with very large models or datasets. The practical impact of this computational overhead needs to be carefully evaluated, especially in comparison to the gains in prediction set efficiency.

### Questions
1. How does VR-ConfTr handle situations with limited/imbalanced calibration data, and how does this affect coverage guarantees?

2. The paper mainly focuses on MNIST-type datasets, which restricts the demonstration of generality and robustness. How would VR-ConfTr perform on high-resolution images?

### Soundness
3

### Presentation
3

### Contribution
3
