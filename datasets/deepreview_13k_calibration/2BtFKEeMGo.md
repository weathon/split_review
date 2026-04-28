# Learning from weak labelers as constraints

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
We study programmatic weak supervision, where in contrast to labeled data, we have access to \emph{weak labelers}, each of which either abstains or provides noisy labels corresponding to any input. Most previous approaches typically employ latent generative models that model the joint distribution of the weak labels and the latent ``true'' label. The caveats are that this relies on assumptions that may not always hold in practice such as conditional independence assumptions over the joint distribution of the weak labelers and the latent true label, and more general implicit inductive biases in the latent generative models. In this work, we consider a more explicit form of side-information that can be leveraged to denoise the weak labeler, namely the bounds on the average error of the weak labelers. We then propose a novel but natural weak supervision objective that minimizes a regularization functional subject to satisfying these bounds. This turns out to be a difficult constrained optimization problem due to discontinuous accuracy bound constraints. We provide a continuous optimization formulation for this objective through an alternating minimization algorithm that iteratively computes soft pseudo labels on the unlabeled data satisfying the constraints while being close to the model, and then updates the model on these labels until all the constraints are satisfied. We follow this with a theoretical analysis of this approach and provide insights into its denoising effects in training discriminative models given multiple weak labelers. Finally, we demonstrate the superior performance and robustness of our method on a popular weak supervision benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper explores programmatic weak supervision by treating weak labelers as constraints in a classification task.The authors propose a constrained optimization approach that integrates weak labeler error bounds directly into the learning objective. This forms a complex optimization problem and is solved with a novel alternating minimization algorithm.

### Strengths
The idea is novel and the theory is rigorous. The proposed algorithms lead to significant improvements in empirical evaluations on some datasets.

### Weaknesses
1. The paper misses a conclusion and future extensions paragraph.
2. On some datasets, the margin of the proposed methods and competing methods are small. Would it be helpful to run some statistical tests to compare their performances?

### Questions
see weaknesses

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
By using accuracy restrictions on weak labelers as learning constraints, this work introduces a novel method for programmatic weak supervision. The paper makes three primary contributions:

1. create a constraint-based method for aggregating weak labelers; 
2. present a scalable optimization problem; and 
3. offer a theoretical analysis of the suggested constrained estimator.

The suggested method is technically sound and well-motivated, and the paper is well-written. The empirical evaluation shows the efficacy of the suggested approach, while the theoretical analysis sheds light on the denoising consequences of several weak labelers.

### Strengths
1. Novel approach: This work presents a novel constraint-based objective that specifically considers accuracy bounds.
2. Scalable: A linear program for classifier constraints and a convex optimization problem for distribution constraints can effectively execute the paper's efficient alternating minimization approach.
3. Thorough theoretical analysis: The paper offers a thorough theoretical examination of the suggested approach. These analyses offer assurances on the trained classifier's inaccuracy and draw attention to the denoising impacts.
4. Excellent empirical performance: According to an experimental evaluation on a well-known weak supervision benchmark, the suggested approach outperforms current baselines, proving its efficacy and resilience.

### Weaknesses
1. The authors admitted that in the case of learning on classifier solving the ILP can still be slow even with LP relaxation. Additionally, because the stochastic gradient descent relies on the population means of the weak labeler accuracies, the method is unable to use a small batch size.

### Questions
1. I suggest the authors use different markers and line styles for different datasets instead of only using color to differentiate different lines.
2. There are several ?? in the paper. For example, on line 1357, 1359, 1418: ??
3. On line 491, the author mentioned that they implemented Algorithm 1 with an L2 regularization. I wonder what are the impacts of other regularization.

### Soundness
4

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
3

### Summary
This paper proposes a method for learning from programmatically generated weak labels by treating weak labelers as constraints rather than relying on traditional generative models. This approach uses side information in the form of bounds on weak labelers’ error rates, which are applied as constraints within a constrained optimization framework. The authors introduce an alternating minimization algorithm to iteratively project model predictions onto the feasible region defined by these constraints. They evaluate the method on multiple weak supervision benchmarks and demonstrate that it improves upon traditional weak supervision techniques, such as Snorkel, by incorporating this constraint-based learning approach.

### Strengths
1. The paper presents an interesting alternative to traditional generative models for weak supervision. By viewing weak labelers as error-bound constraints, the approach avoids common assumptions about label independence or probabilistic structure, which may not hold always. 

2. The authors provide an upper bound on error (in the union of covered region by all weak labelers) of any predictor satisfying all the constraints. The upper bound is summation of upper bounds on the errors in each weak labelers and the probability of region where weak labelers have a conflict. Implying better bound with more conflict.

3. The method is evaluated on weak supervision benchmarks, where it demonstrates improved accuracy over other weak supervision methods.

### Weaknesses
1. The model relies on accurate estimates of weak labelers’ error bounds to define constraints. However, obtaining these estimates is challenging, and inaccurate bounds could lead to suboptimal model performance. In the experiments these are estimated using validation data, which could also be hard to obtain. In contrast several baselines in weak supervision (those based on generative modeling) estimate 'labelers quality' using only the unlabeled samples. 

2. Assumptions made on the weak labelers are not clear. In particular, what are the assumptions that the labelers have to satisfy to ensure the method will work as expected and the theoretical results will hold. Naively putting an upper bound of $\eta_j$ on each labeler could lead to several scenarios e.g. all could have $\eta_j$ error in different parts of the input space (~independence) or highly overlapping parts (~highly correlated). Could you explain how the method and results will turn out in these two extremes? 

3.  Theoretical results do not explain how learning in the proposed setup leads to a classifier with good generalization error. It naively depends on the summation of errors of individual labelers. On the other hand several of the baselines provide results showing how the labelers cancel their noises and eventually lead to a classifier with comparable generalization error to a model trained on clean labels. They do make certain assumptions on labelers to get there. What can be said more specifically in this setup with similar assumptions? Even a naive majority vote with labelers with random noise of $\eta_j$ could be shown to give good generalization error going down with the number of samples and the number of weak labelers.



### Questions
Please see the weaknesses above. And,
1. I do not find the empirical results convincing. Ours(C) and Ours(V) rely on either hand tuning $\eta_j$ or estimating from validation data. Did you estimate source quality in other WS setups using the same validation data? 

2. Can you provide some simulations with different $\eta_j$ and labeling sources outputs, clearly showing how the method works in different scenarios?

### Soundness
2

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
This paper introduces a novel approach for learning from weak labelers by framing the problem as a constrained optimization task. Instead of relying on generative models or conditional independence assumptions, the paper proposes using known upper bounds on the error rates of weak labelers to guide the learning process. The paper develops an alternating minimization algorithm to iteratively generate soft pseudo-labels that satisfy the constraints and train the model accordingly. Theoretical analysis is provided to explain the denoising effects of the method, and experiments on benchmark datasets demonstrate its effectiveness.

### Strengths
1. The paper moves away from traditional generative models, avoiding the often unrealistic assumption of conditional independence between weak labelers, making it more flexible for real-world applications.

2. The theoretical analysis is quite thorough, especially with the introduction of projection techniques and alternating minimization, showing how to effectively build a classifier without labeled data.

3. Good writting.

### Weaknesses
The problem addressed in this paper is certainly interesting, but as the authors themselves mention, it has strong connections to areas like crowdsourcing, noisy label learning, semi-supervised learning, and ensemble learning. Each of these fields already has well-established techniques that could be adapted, with only minor modifications, to solve the problem presented here. However, the paper dismisses these connections too quickly, with phrases like "not directly applicable to our setting" and "relies on the implicit inductive bias." I find this explanation insufficient, as it limits the paper's significance and impact. A deeper exploration of these connections, along with additional comparative experiments, would have been much more convincing.

The authors propose two objectives and frame the problem as a constrained optimization task, introducing corresponding optimization methods. While the paper's main contribution is centered on optimization through projection, I have to admit that I'm not an expert in optimization, this approach feels somewhat intuitive. It doesn't strike me as a particularly novel or non-intuitive solution.

Additionally, regarding the problem setup and experiments, I would like to see more details about the coverage rate and noisy rate of each weak labeler and the collective coverage of all labelers. This seems crucial to the model’s performance and yet isn’t discussed in enough detail.

### Questions
Please see above

### Soundness
3

### Presentation
3

### Contribution
2
