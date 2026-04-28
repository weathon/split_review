# Combining Analytical Smoothing with Surrogate Losses for Improved Decision-Focused Learning

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 3, 5, 8, 3

## Abstract
Many combinatorial optimization problems (COPs) in routing, scheduling, and assignment involve parameters such as price or travel time that must be predicted from data; so-called predict-then-optimize (PtO) problems. Decision-focused learning (DFL) is a family of successful end-to-end techniques for PtO that trains machine learning models to minimize the error of the downstream optimization problems.
This requires solving the COP for each training instance with the predicted parameters and computing the derivative of the solution with respect to the predicted parameters—tasks that become computationally prohibitive for large COPs.
When the COP is an integer linear program (ILP), a recent work, DYS-Net, applies Davis-Yin splitting (DYS) to solve and differentiate through quadratically regularized ILP. While this fully neural approach significantly accelerates training, it has only been evaluated on datasets where true cost parameters are unobserved, limiting its comparability to state-of-the-art techniques. In this work, we experimentally demonstrate that minimizing empirical regret using DYS-Net results in suboptimal regret on test data compared to state-of-the-art DFL methods across three different COPs. 
We attribute this to the plateau effect: regret remains constant over regions of the parameter space, with sharp changes occurring only at transition points resulting in low gradient values over much of the space when regret is minimized.
We illustrate how minimizing a noise contrastive surrogate loss avoids this problem.
% We experimentally demonstrate that minimizing this surrogate loss enables DYS-Net to achieve test regret that is as low as or better than the state-of-the-art. By achieving state-of-the-art regret levels with DYS-Net at significantly reduced training times, this work advances research in DFL and its applicability to large-scale PtO problems.
Through extensive experiments, we show that minimizing this surrogate loss allows DYS-Net to achieve test regret levels that are comparable to or lower than the state-of-the-art methods. Moreover, by achieving state-of-the-art regret levels with significantly reduced training times, our approach represents a substantial advance in DFL research, particularly in improving its scalability towards large-scale PtO problems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper concerns itself with combinatorial optimization (CO) problems, in the predict-then-optimize (PtO) regime.  The authors advocate that two main approaches are used to train ML models to minimize downstream CO error (Decision Focused Learning):

1. Minimizing a differentiable (convex) surrogate function, (instead of the regret).
2. Smoothing the problem to a PQ, and minimizing this proxy instead.

The authors argue that whilst the latter is differentiable, its gradient is zero almost everywhere, except at transition points. The paper suggests that minmizing a surrogate loss even after smoothing, and provides supporting empirical evidence (in the form of toy data sets) in addition to the presented theory.

### Strengths
The paper is well written, with a good structure and presents the mathematics in a clear and coherent way to the reader. The proposed minimization of a surrogate function (Sections 3 & 4) is well reinforced with the experiments section, and the motivations in Section 5 are pertinent for such methods to be deployed at scale in the future.

### Weaknesses
Whilst the paper is well written, and produces a coherent argument, I am reluctant to accept on contribution grounds. From what I can see, the majority of the paper is pulling together prior works, with limited novel contribution; (please note I am new to this exact line of research and could be missing something here, hence my low confidence score). 

More precisely, a large portion of the paper is compiling prior problems / works, the surrogate losses in 3.2.1 and 3.2.2 are from existing works, and the experiments (whilst nice and supporting the argument), are toy-experiments and with little differing the cited literature. This should not detract from the papers clear strengths, and hence I politely suggest further contribution could be added either via i) further experimentation ii) novel theory / mathematics for surrogates  (or novel surrogates), which would render the paper acceptable to the conference upon resubmission.

### Questions
See suggested relevant literature that you may wish to cite in Section 3.1 (lines 136-147):


- [Berthet 2020] *Learning with Differentiable Perturbed Optimizers*.
- [Blondel 2020] *Fast differentiable sorting and ranking*
- [Jang 2016] *Categorical Reparameterization with Gumbel-Softmax*.
- [Peterson 2024] *Generalizing Stochastic Smoothing for Differentiation and Gradient Estimation*
- [Stewart 2023] *Differentiable Clustering with Perturbed Spanning Forests*.
- [Peterson 2024] *Differentiable Top-k Classification Learning*

From my limited understanding, it appears [Berthet 2020] addresses some of the problems discussed in this paper.

### Soundness
4

### Presentation
4

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studies decision-focused learning (DFL) for combinatorial optimization problems. The authors summarize the previous methods of DFL for combinatorial optimization.  To overcome the challenges, previous works either employ a differentiable surrogate loss or tuning the combinatorial optimization to a differentiable mapping. However, the authors point out that the derivative remains nearly zero for a large region by existing methods. To address this issue, the authors combine both approaches of smoothing the cost function and using a surrogate loss. The authors verified the performance of the proposed method by four DFL benchmarks.

### Strengths
The paper has the following strengths:
+ The paper provides a good summary on the existing works of DFL for combinatorial optimization.
+ The paper propose to combine the methods of smoothing the cost and using a surrogate loss and apply DYS-Net to solve the scalability issue.
+ Numerical results on common DFL benchmarks are given.

### Weaknesses
The paper can be improved in the following aspects.
- The paper argues that the derivative remains nearly zero for a lot of combinatorial problems but this argument is not verified. It would be better if the authors can give some illustrations based on some examples.
- The authors propose to combine the two existing methods of DFL for combinatorial optimization. However, the combination looks straightforward. Can the authors present if there are some technical challenges to combine the two methods?
- The authors apply DYS-Net in [D. McKenzie 2024] to address the scalability of DFL. However, it is unclear about the novelty about applying DYS-Net here. Is it just an application?
- The empirical results will be more convincing if more ablation empirical studies are given.

### Questions
Please see the questions in weakness.

### Soundness
2

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
5

### Summary
The paper studies decision-focused learning (DFL) for tasks where the parameters appear linearly in the objective. Specifically, the paper proposes applying QP smoothing to existing decision-focused learning surrogate losses such as SPO+ and the self-contrastive estimation (SCE) loss. They motivate this application by pointing out that the typical approach of applying smoothing directly to the non-convex task loss may still have vanishing gradients, which makes optimizing the decision-focus loss challenging. In addition to smoothing, the paper also studies recently proposed approaches to making DFL more scalable. For both approaches, the paper provides numerical experiments demonstrating the efficacy of applying more heuristic approaches.

### Strengths
The paper highlights two popular decision-focused learning approaches, smoothing and surrogate losses, and points out reasonable drawbacks of learning with both approaches. It then shows how combining the two approaches may potentially help address weaknesses found in the two approaches. They also show how recently proposed approaches for making DFL more scalable can be combined with surrogate losses to improve scalability and the quality of the learned decisions. They then justify their claims with numerical experiments of a popular set of benchmarks found in PyEPO which highlights some robustness.

### Weaknesses
The paper's weaknesses can be broken down into two categories: i) issues related to theoretical justification and ii) issues with the numerical experiments.

Theoretical Issues
- The theoretical justification issues stem from the main argument of the paper--that smoothing task loss directly may not solve a zero-gradient issue which hampers gradient-based optimization techniques. The paper seems to claim that the benefit of combining smoothing and surrogate losses addresses this problem and produces losses with "better" gradients. However, the surrogate losses the paper proposes combining with smoothing are inherently convex, so it is unclear why smoothing would be beneficial. The authors could address this issue by analyzing the newly proposed surrogate loss directly. Perhaps they can verify whether the new surrogate loss formed by combining QP smoothing is convex or non-convex. In the latter case, it may make sense why "better" gradients may be beneficial for the surrogate loss. For the former, perhaps it suggests that QP smoothing adds some form of regularization instead providing better gradients. It may also be helpful to then compare the approach with combining surrogate losses directly with regularizers instead of replacing non-smooth components with smoothed components.

- On page 5 there is a proof, but no formal statement. Adding a formal statement that is proved as a lemma or proposition would improve the presentation and precision of the section.

Numerical Experiment Issues
- The overall more extensive numerical experiments could be performed. The recently accepted work to NeurIPS [1] has proposed a new smoothing approach that outperforms surrogates such as SPO+ and SCE for misspecified settings. Their numerics show this is true especially for settings where a zero regret policy can be learned. For example, in their experiments they propose a simple weighted classification problem and a shortest path problem where the optimal decision can always be learned from the context using a linear plug-in model. Including these experiments would be helpful since it could be implied that directly applying QP smoothing to the task loss would also perform well in these settings. This would further highlight the benefits or drawbacks of combining smoothing with the surrogate losses.

-The numerical experiments could also be expanded to include other methods such as the proposed surrogate loss in [1] and other approaches such as combining regularizers with the surrogate losses and the QP smoothed task loss. The latter approach would also help eliminate zero-gradient issues since the gradient of the regularizer may be non-zero almost everywhere.

# Update to Review
Based on the discussion it seemed the authors primarily decided to pursue answering Reviewer HVPw’s comments, so I decided to just follow along their discussion. I appreciate the additions as the authors clearly worked hard to produce the new results, which helped me better understand what the authors are trying to propose.

Based on these additions I still will keep my score the same. The primary reason is that the work still feels somewhat incremental to me. The authors seem to center their contribution around the SCE surrogate loss, with the main innovation being a combination of incorporating smoothing and DYS-Net into the surrogate loss. These additions don’t seem to greatly complicate the implementation of the SCE surrogate loss and thus feel like small upgrades. Additionally, these techniques are not novel by themselves, so it feels similar to heuristically adding a regularizer or a penalty term.

Below highlights more specific details:

1. From a computational point of view, the smoothed SCE loss with DYS-Net is indeed faster, which is expected. It performs comparably with other methods, but it is not uniformly or clearly the best in any setting. SPO+ with various computational tricks and CaVE do similar or better though not uniformly across all experiments.
2. Theoretically, it is hard to claim that SCE loss is more attractive as Proposition 1 only holds when the original problem Regret and SCE loss are zero. This is often not the case as seen in the experiments. Thus, it’s hard to rigorously argue that low SCE loss corresponds to low regret. This is evident in the generalization section of the appendix as the authors fail to show that the SCE loss bounds the expected regret.

### Questions
1. The proof on page 5 assumes that there exists choices of $\hat{\mathbf{y}}$ such that $\mathcal{L}\_{SCE}(\mathbf{v}^*(\hat{\mathbf{y}}), \mathbf{y})$ is 0 (such as $\hat{\mathbf{y}} = \mathbf{y}$). However, in most cases this is not true if your hypothesis class is misspecified or  if $\mathbf{y} = \mathbb{E}[\mathbf{y}] + \epsilon$ where $\epsilon$ is independent noise. Thus, how important is this result practically? Is often the case your surrogate loss equal or below 0? Also, in general, the surrogate loss is summed over samples, i.e. $\sum_{i=1}^n \mathcal{L}_{SCE}(\mathbf{v}^*(\hat{\mathbf{y}}_i), \mathbf{y}_i)$. It maybe beneficial to present the result relative to the empirical task-based loss.

2. What is the motivation for applying the QP smoothing to SPO+? SPO+ is already convex so it doesn't have any vanishing gradient issues. This seems to also be confirmed numerically since the QP smoothing does not provide significant performance gains when applied to SPO+

3. How does QP smoothing tune $\mu$ in the quadratic term? Presumably larger $\mu$ has more smoothing, but is more different from the solution of the original problem. Does this affect performance and how does affect the computation time?

4. Is there a reason DYS-net is only applied to SCE? Can DYS-net be applied to SPO+ as well or other surrogate losses that require solving an LP?

5. Is there a reason why you don't consider other approaches for eliminating zero gradients issues such as adding a regularizer directly to the surrogate loss or combining MSE loss with the surrogate loss? Both solutions would seem to produce "better" gradients.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In the predict-then-optimize framework, this paper introduces an approach that combines smooth optimization, which transforms the solver into a smooth and differentiable form, with a surrogate loss that approximates regret. This combination allows the learning model to maintain meaningful gradient flow even in flat regions, enhancing stability during training. Additionally, the paper leverages DYS-Net, a fast differentiable solver, to significantly reduce training time while preserving decision quality.

### Strengths
1. **Novelty:** This paper first introduces a combination of smoothing techniques and a surrogate loss function within the predict-then-optimize framework for combinatorial optimization.
2. **Efficiency:** Solving the optimization problem is often the computational bottleneck in PtO. This paper demonstrates the advantages of using DYS-Net, a differentiable solver significantly reducing training time without compromising decision quality.
3. **Clarity:** The paper is well-organized and provides clear and thorough explanations. Additionally, visualizations and examples clarify the results and effectively support the theoretical insights.

### Weaknesses
1. **Lack of Theoretical Supports:** While the QP-based relaxation for ILP has shown promise in experimental results, the paper lacks a theory supporting the effectiveness of this relaxation approach. (I acknowledge that providing such theoretical support is challenging.)
2. **Lack of Comparison with Related Speed-Up Techniques:** While one of the main contributions of this paper is its focus on enhancing solver speed, it does not compare its approach with other established methods that also aim to accelerate predict-then-optimize (PtO) processes by leveraging ILP relaxations and caching strategies. For instance, 'Differentiation of Blackbox Combinatorial Solvers' and 'Pyepo: A PyTorch-Based End-to-End Predict-Then-Optimize Library for Linear and Integer Programming' utilize LP relaxations of ILP problems as an oracle to speed up solution times. Additionally, 'Contrastive Losses and Solution Caching for Predict-and-Optimize' introduces solution caching to improve efficiency. Comparing this paper’s approach with these alternative acceleration methods, rather than just focusing on ILP solvers, would provide a more comprehensive evaluation of the proposed method’s effectiveness in reducing computation time.
3. **Insufficient Scalability Demonstration:** Although the paper emphasizes computational efficiency, the experiments are conducted on relatively small instances (e.g., 11-node TSP). This may limit the understanding of the scalability for larger combinatorial problems. 
4. **Missing Hyperparameter Details:** The paper does not provide explicit details on specific hyperparameters used for training, such as learning rate, batch size, or optimizer configurations. Thus, it is difficult for readers to reproduce the results. Most critically, there is a lack of information on the smoothing parameter $\mu$, which directly influences gradient flow and solution quality.

### Questions
1. Given that current exact solvers like Gurobi are highly efficient for solving QP problems, have you considered or conducted any comparisons between DYS-Net and other exact QP solvers in the forward pass?
2. Could the authors offer more insights or practical guidelines on choosing $\mu$?
3. Does DYS-Net need to be pre-trained before starting the main PtO training process? If so, could the authors provide some description and training time?
4. To improve reader comprehension, providing more details on DYS-Net would be highly beneficial.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper considers a new training method for decision-focused learning, also known as end-to-end learning or joint predict-then-optimize. They explain two existing methods to approach these problems: surrogate loss approaches such as the smart predict the optimize (SPO) and contrastive loss as well as smoothing methods. The authors propose to combine the two methods, minimizing a surrogate loss with a smoothed solver. They run experiments on some optimization tasks like shortest path, knapsack and TSP.

### Strengths
The ideas are simple and can be easily implemented by practitioners. You present a good outline of past work and background on existing methods. The experimental results are promising as well and show improvements of your proposed method against some of the main existing literature.

### Weaknesses
The exposition and contribution is not very clearly expressed in the paper. As a starting point, it is difficult to find where your proposed method is written. I'm guessing your proposed approach is to solve an empirical version of problem (2). The actual empirical problem is never introduced. I also assume that, given features $x$, you would construct a model to make predictions $f(x)$ of $y$. This is also not explained well. Finally, you solve the empirical problem by gradient descent using (12). All of this needs to be made clear and cohesive. I would suggest a section to explain the full problem and proposed method.

For example, the statement "smoothing addresses the non-differentiability at the transition points, but the derivative dv⋆( ˆy)
d ˆy still remains zero far from these points" is not well-supported. The illustration in Figure 1b that the authors point to does not give adequate support for these claims as a single low-dimensional example does not generalize. Similarly, your subsection "A deep dive into the gradient landscape" does not adequately explain the behavior of your approach. Why should it generalize to more complex problems? Please provide some theoretical analysis on the gradient behavior in higher dimension. Alternatively, you can also provide computational results on gradient behavior for various optimization tasks and higher dimension.

I'm a little confused why section 5 exists. This is only explaining the methods used in a different paper to implement your proposed method. It is not a contribution of your work, as far as I can tell. It may be better to place this discussion in the appendix, if at all. Moreover, the work in [1] may be a good additional reference as it seems to be a more generalized version of the work you cite.

Finally, for the experiments, please give more details on the problems addressed. For example, provide information about:
    1. Problem sizes for each experiment
    2. Exact mathematical formulations of the optimization problems
    3. Architecture details of the neural networks used
    4. Hyperparameters for both the models and optimization algorithms
    5. Data generation process and dataset statistics

### Questions
1. The paper would benefit greatly from a thorough revision to enhance clarity and readability. Please see my first comment in the weaknesses section. 

2. Can you provide more theoretical grounds for your claims? Specifically around the issues of the gradients for the smoothed solvers. And why does your method resolve these issues? 

3. Please provide more details on the experimental results. Again, please see my comments in the weakenesses section. 

4. Can we see some experiments about the behavior of the gradients? Especially if you cannot provide theoretical results. For example, how does the magnitude of the gradients for your proposed approach compare with those of existing methods. Can we also see results on accuracy/regret as a function of the number of training epochs used. 

5. Ideally, the same base model is used across all experiments and only the training method changes. That is, use the same base neural network and optimization solver for each dataset. Then, use each training method (smoothed, surrogate loss, your proposed combination). This way, everything is even across experiments for the same dataset, instead of using for instance both CVXPYlayers and DYS-Net etc.

### Soundness
2

### Presentation
2

### Contribution
2
