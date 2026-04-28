# Do Stochastic, Feel Noiseless: Stable Stochastic Optimization via a Double Momentum Mechanism

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Optimization methods are crucial to the success of machine learning, with Stochastic Gradient Descent (SGD) serving as a foundational algorithm for training models. However, SGD is often sensitive to the choice of the learning rate, which necessitates extensive hyperparameter tuning. In this work, we introduce a new variant of SGD that brings enhanced stability in two key aspects. First, our method allows the use of the same fixed learning rate to attain optimal convergence rates regardless of the noise magnitude, eliminating the need to adjust learning rates between noiseless and noisy settings. Second, our approach achieves these optimal rates over a wide range of learning rates, significantly reducing sensitivity compared to standard SGD, which requires precise learning rate selection.
Our key innovation is a novel gradient estimator based on a double-momentum mechanism that combines two recent momentum-based techniques. Utilizing this estimator, we design both standard and accelerated algorithms that are robust to the choice of learning rate. Specifically, our methods attain optimal convergence rates in both noiseless and noisy stochastic convex optimization scenarios without the need for learning rate decay or fine-tuning. We also prove that our approach maintains optimal performance across a wide spectrum of learning rates, underscoring its stability and practicality.  Empirical studies further validate the robustness and enhanced stability of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents two methods for stochastic optimization that achieve similar guarantees as standard gradient descent and accelerated gradient descent while being robust to the choice of learning rate involved.

### Strengths
This is a well written paper that presents two interesting algorithms with strong theoretical guarantees. The algorithms definitely appear novel to my knowledge but I do not know of the latest developments in this area.

### Weaknesses
The empirical section seems to be fairly underbaked in my opinion.

### Questions
1. Have the authors tested out the proposed algorithms (or their adaptive gradient variants) on problems that appropriately reflect problems/setups that are of realistic practical interest? For instance, training transformer based architectures on standard pre-training tasks?
2. Can the authors clarify how this algorithm's guarantees look like with (a) strong convexity, (b) non-convex but say with a PL style condition?

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
3

### Summary
The paper introduces the $\mu^2$ (Momentum$^2$) gradient estimator, designed to manage gradient noise in stochastic optimization, particularly in convex and smooth loss scenarios using single-sample batch sizes. This estimator integrates two momentum techniques:

1. **Anytime Averaging**, which averages the query points for the gradient oracle.
2. **STORM**, a corrected momentum method that averages gradient estimates with bias correction.

By combining these techniques, $\mu^2$ achieves a progressively shrinking square error of the gradient estimates ($\|\epsilon_t\|^2 \propto 1/t$), contrasting with the fixed gradient error in standard stochastic optimization ($\|\epsilon_t\|^2 = O(1)$). This property enables the use of a fixed step-size for convergence, removing the necessity of step-size decay in stochastic settings. Additionally, $\mu^2$ allows the norm of the gradient estimate to serve as a stopping criterion.

The paper implements $\mu^2$ in two algorithms:

1. **$\mu^2$-SGD**: This combines $\mu^2$ with SGD. Although $\mu^2$ could work with other first-order methods, the authors focus on SGD to derive theoretical guarantees. Theorem 4.2 shows that $\mu^2$-SGD achieves optimal convergence rates for noiseless ($O(L/T)$) and noisy ($O(L/T + \tilde{\sigma}/\sqrt{T})$) settings using a fixed learning rate $\eta_{\text{Offline}} = 1/8LT$. Remarkably, this rate does not need to change between noiseless and noisy conditions.

2. **$\mu^2$-ExtraSGD**: This accelerated variant of $\mu^2$-SGD uses the ExtraGradient framework to achieve optimal convergence rates of $O(L/T^2)$ (noiseless) and $O(L/T^2 + \tilde{\sigma}/\sqrt{T})$ (noisy) with a fixed learning rate $\eta_{\text{Offline}} = 1/2L$.

Experiments on MNIST and CIFAR-10 datasets, using convex (logistic regression) and non-convex (deep learning) models, demonstrate $\mu^2$-SGD's stability and performance over a range of learning rates compared to various baseline optimizers, including SGD, Polyak momentum, and individual applications of Anytime Averaging and STORM.

### Strengths
- The paper is well-organized, with clear explanations of each momentum component and its integration into $\mu^2$. A convergence guarantee for stochastic optimization with a fixed step-size addresses a significant challenge in optimization.

- The theoretical results are rigorously supported. Extending Theorem 4.2 to the accelerated version in Theorem 5.1 provides a pleasing completeness to the theory. In the former, the learning rate has a dependency on $T$, which prevents it from achieving the accelerated rate. This dependency is eliminated by introduction of the $\mu^2$-ExtraSGD.

- The theoretical results carry over nicely in the convex experiment, logistic regression on MNIST. $\mu^2$SGD consistently achieves the best performance across a very wide range of learning rates ($10^{-3}$ to $10^3$). Unfortunately, I am unable to tell where each method lies in the last plot in Figure 1 ($10^{-4}$).

### Weaknesses
 - My main critique of this paper goes back to its main promise: with $\mu^2$SGD, convergence using a fixed step-size is achievable in a stochastic setting. However, although the step-size is fixed, varying momentum parameters, $\alpha$ and $\beta$, are required to prove convergence in Theorem 4.2. The decreasing step-size nature necessary for convergence in a stochastic setting seems to be delegated to the momentum parameter here. That being said, I appreciate the theoretical results and the simplicity of the schedule for $\alpha$. This same schedule was also used in the experiments, and it seems to work well.
- There is no experiment on $\mu^2$-ExtraSGD. Observing the accelerated rate in experiments could have potentially highlighted the strength of this method. I would also be curious to see how this acceleration performs compared to the Nesterov accelerated method. 
- Although the paper shows $\mu^2$’s stability across learning rates, there is little analysis on how sensitive the algorithm might be to momentum parameter choices, especially in non-convex settings where fixed parameters are used.

### Questions
I am curious to know about your choice of  single sample per iterate setting. I understand that this choice might be more convenient to work in theory, but could you still carry the same theory using batch size b?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Combining two existing methods, the authors propose an accelerated SGD mechanism that is stable w.r.t. learning rate. The authors provide rigorous justifications for their claims and supporting experiments.

### Strengths
1. By combining two existing methods--Anytime-SGD (Cutkosky, 2019) and STORM (STochastic Recursive Momentum) (Cutkosky & Orabona, 2019), the authors propose $\mu^2$-SGD.

2. The authors show the error term is upper bounded by $\frac{1}{t}$ with $\mu^2$-SGD. Moreover, they obtain an upper bound for the excess loss that gives a noise independent optimal learning rate, which results in a wider range of optimal choice for learning rate compared to SGD. 

3. By adding Optimistic-OGD, the authors propse an accelerated version of $\mu^2$-SGD--$\mu^2$-ExtraSGD. The optimal learning rate in this case is constant in time so the optimal rate can be obtained without doing time-varying learning rate. 

4. The authors have experiments in both convex and non-convex setting to verify their results. Experiments show $\mu^2$-SGD and $\mu^2$-ExtraSGD are stable w.r.t different learning rates while other methods don't. Experiments are done thoroughly with details given in the appendix.

### Weaknesses
1. The main contribution of this work--$\mu^2$-SGD and $\mu^2$-ExtraSGD--comes by combining two existing works. The proofs for main theorems are quite traditional. One could argue this lacks novelty, although I personally found the results interesting.

2. In the numerical experiments (non-convex setting), It seems $\mu^2$-SGD and $\mu^2$-ExtraSGD only make a difference when the learning rate is far away from normal choices. More precisely, Figure 2 shows all methods are quite similar for $\eta\leq1$. $\mu^2$-SGD and $\mu^2$-ExtraSGD are better only when $\eta >1$, which is not a typical choice for learning rate anyway. I am not sure how learning rate stability is appreciated by the community. 

3. By allowing a wider range of learning rates, one could argue that with this method, we don’t need to tune the learning rate anymore, like we could set it to be 1. However, $\mu^2$-SGD and $\mu^2$-ExtraSGD are not hyperparameter free, i.e. they introduce weights $\alpha_t$ and Corrected Momentum weights $\beta_t$, which are chosen to be $t$ and $\frac{1}{t}$ in the experiments. I wish the authors could give more insights into this topic. If the cost of reducing one hyperparameter is introducing two hyperparameters, I am not sure it’s worth it. 

4. The experiments are done for different learning rates, but I found the plots were hard to read when the accuracies/losses got too close. Presenting results with an additional table could help in these cases.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel gradient estimator for stochastic convex optimization, combining momentum-based techniques. Using this estimator, the authors develop robust SGD-style algorithms that achieve optimal convergence rates in both noiseless and noisy settings, maintaining stable performance over a wide range of learning rates.

### Strengths
Considering algorithms that work in both noisy and noise-free conditions helps improve the robustness of the algorithm.

### Weaknesses
1.	The structure of this paper makes it difficult to follow, especially in terms of understanding the novelty of the algorithms.
2.	The experimental results presented do not convincingly demonstrate the superiority of the proposed algorithm. The choice of learning rates between 10 and 1000 is unconventional and the hyperparameter settings for STORM are not clearly defined. Furthermore, the generalization benefits mentioned by the author in line 52 has no experimental support.
3.	The novelty of this paper appears to be limited. For example, STORM was originally designed for a non-convex setting, and one of the main contributions of this paper seems to be the redesign of STORM's parameters for a convex setting.
4.	Many fully parameter-free algorithms[1,2] have appeared recently, which do not require knowledge of the smoothing constant $L$ and can achieve the same convergence rate. In contrast, this paper still relies on smoothing constants to determine the learning rate. Under fully parameter-free conditions, even a wide range of learning rate options appears to lose its significance.

### Questions
1.	Could the author provide more comparisons between the proposed algorithm and parameter-free algorithms?
2.	Could the author include additional experiments on the impact of noise on the algorithm?

### Soundness
3

### Presentation
3

### Contribution
2
