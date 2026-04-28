# Three ways that non-differentiability affects neural network training

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
This paper investigates how non-differentiability affects three different aspects of the neural network training process. We first analyze fully connected neural networks with ReLU activations, for which we show that the rate of convergence results derived using continuously differentiable functions grossly under-estimate the actual rate of convergence. Next, we analyze the problem of $L_{1}$ regularization and show that the solutions produced by deep learning solvers are unreliable even for the $L_{1}$ penalized linear model. Finally, we analyze the edge of a stability problem, where we show that all convex non-smooth functions display unstable convergence, and provide an example of a result derived using differentiable functions which fails in the non-differentiable setting. More generally, our results suggest that accounting for the non-linearity of neural networks in the training process is essential for us to develop better algorithms, and to get a better understanding of the training process in general.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on ways that non-differentiability may affect the training of neural networks. Specifically, the paper considers one layer fully-connected networks with ReLU activation functions, lasso and ridge regression. The paper shows three settings under which the training of neural network may have undesirable behavior. Specifically, the convergence rate of non-asymptotic NGD (non-gradient descent, as opposed to GD, gradient descnet), the lasso problem and the edge-of-stability problem.

### Strengths
The paper is mostly well-written, both in terms of language and, flow and literature review. It is also sound. The paper may motivate research towards the training of non-differentiable neural networks.

### Weaknesses
The main motivation for the work is that the theoretical results for gradient-descent methods on smooth functions may not hold in the case of non-smooth functions (second paragraph of the introduction), even though GD methods are used in non-differentiable cases in practice. This motivation, while true, is not too strong. As the authors acknowledge, it is a common violation in practical machine learning, and its success is undeniable. Therefore, I think the work would benefit significantly from having more significant, large-scale examples, where we see the non-differentiability as a clear problem. Considering in the examples non-asymptotic and constant learning rate settings is also distracting, as this way we can not distinguish if it the asymptotic and diminishing learning rate settings would hold the same problems.

The three specific arguments for drawbacks of non-differentiability are too disconnected and the paper also does not go too deep into each of these problems, and the results are too superficial and lacking a significant novelty. However, I do think each of the problems could be interested on its own, and could deserve more exploration from the authors. Specifically, while the authors point out problems, they do not investigate the impact of obvious solutions: if the problem is the constant learning rate, we can just make it diminishing; if the problem is non-differentiability, for instance from the ReLU layer or the lasso penalty, we can smoothen the function at points.

Finally, even though the work calls attention for three problems within the training of non-differential neural networks, investigating specific solutions, or at least directions for solving the problems raised, would make the paper much stronger. It could also allow for more specific and interesting conclusions than the one presented (which is that attention to the problem is required).

Minor and detailed comments:
- in the abstract, "under-estimate" is ambiguous;
- in the abstract, "unreliable" is also not clear;
- in the preliminaries, the learning rate $\alpha$ should be defined when it appears. the vectors $z_i$ are also not defined, even though we can understad their dimensions for the dimensions of the matrix $\mathbf{Z}$. The response vector is defined bold but appears un-bolded in the expression. Its dimension should also be $N \times 1$, not $P \times 1$.
- in the preliminaries, if it is argued that the differences between subgradient and standard gradient play a key role in the analysis, subgradient must be introduced, defined and discussed.
- the results in section 3 may be too unsurprising, as the authors acknowledge after discussing the experiments whose results appear in figure 1.
- the results in section 4 are more interesting. Nevertheless, the constant learning rate plays a key role in the contributions, and even in the differentiable case, non-convergence can happen with non-diminishing learning rates.
- the results in section 5 are too disconnected from the previous and makes the reading not transition smoothly.
- in section 5, the result cited in the proof holds for decreasing learning rates.

### Questions
- why is the loss function in equation (12) not differentiable ? or is it differentiable once but not twice ?
- where do the authors "demonstrate that the widely-used assumption of L-smoothness tends to significantly overestimate convergence rates"? Is this not shown in Tibshirani (2015)?
- in the second paragraph of section 3, why is the reference for saying "the learning rate (is) reduced three of four times during training" ?
- in the third paragraph of section 3, "optimal" is in the local or global sense ?
- do the authors believe the solution for the problem raised should be more directed to the function (smoothen the function to differentiability) or the algorithm (develop specific algorithms for non-differential functions) ? Can this discussion be added ?
- in section 5, the result cited in the proof holds for decreasing learning rates. is that not contradictory to the constant learning rate setting considered ?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tries to investigate how non-differentiability affects machine learning algorithms. Several issues are raised when non-differentiability is present, including convergence rate under smooth conditions, convergence for LASSO, and reason for the edge of stability. Dozens of existing works are used to explain these issues.

### Strengths
This paper studies non-differentiability in deep learning, which is an important issue.

### Weaknesses
1. I am really confused about what the algorithm "NGD" is. The authors say it is "Non-differentiable gradient descents" without providing any concrete definition (how is $\tilde{\nabla}$ defined? Is it subgradient? If it depends on the problem, what is the concrete definition of it in Figure 1?). This makes it hard to evaluate this paper, as I do not know if it is the version of gradient applied to deep learning practice. Also, I would like to remind the authors that "NGD" is usually referred to as "Natural Gradient Descent", and I suggest the authors change the name.

2. The presentation of this paper needs to be polished. As an example, it is quite weird that the left subfigure of Figure 1 is not in a log scale, since there are only two or three points in the figure much above 0. Also, the subfigure even appears to be a screenshot with inconsistent color with the background. Also, on page 5, I do not think it is a proper way to use discussions in a forum to support claims.

3. Is Prop 1 correct? I do not check the reference, but at first glance, this appears to be strange, as intuitively it is possible that at $\theta_0$ the gradient is quite large and the iterations jump outside the unit ball.

4. This paper extensively cites conclusions from other papers without any further explanation. For example,
> Since the loss function described in equation (6) satisfies the Lipschitz condition (see equation (5)) with L = \lambda1, we have from Boyd et al. (2003) (Section 2 on the Constant Step Size) that...

5. Many connections are drawn based on imprecise observations/statements. For example, in the texts below,
> we know from Figure 2 that the optimal weights lies close to points of non-differentiability
How "close" is needed to make the Taylor expansion invalid?


**Typos**

1. The first line under Eq. (3): y is a $N\times 1$ ...?

2. Proof of Proposition 1: missing "."

### Questions
See the Weaknesses above.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies how non-differentiability affects the optimization trajectory of convex non-smooth minimization problems. The analysis comes from three perspectives: the convergence behavior, the algorithm’s ability to reach the optimal point, and the effect of non-differentiability on the phenomenon of the edge of stability. In general, the paper argues that non-differentiability introduces a different dynamic of optimization, and calls for a more fine-grained analysis to deal with non-differentiability.

### Strengths
1. The topic considered in this paper is interesting. Indeed, non-differentiability deviates from traditional regulatory conditions in convex optimization, and it is a mystery why blindly applying SGD on e.g. ReLU neural network can achieve a good performance.

2. The paper is well-written. The topics of the paper are decoupled nicely into three different sections, and each section is written clearly.

### Weaknesses
1. Objectives are too simple and not representative of neural networks. The paper considers a one-layer linear model with an added ReLU activation at the end, which is an extremely simple version of neural networks. It further assumes that the labels $\mathbf{y}$ contain only non-positive entries, which is almost never the case in real neural network training. In particular, the two conditions combined enforces the neural network to almost never fit all training labels. This setup deviates significantly from practical neural network architectures, where ReLU activations are typically interspersed throughout the network, not just at the output layer. The constraint of non-positive labels further limits the applicability of the analysis, as real-world datasets rarely exhibit this property. The combination of these simplifications raises concerns about the generalizability of the findings to more complex and realistic neural network scenarios.

2. The argument that the GD dynamic differs on differentiable and non-differentiable objectives is not strong. In particular, the contradiction is constructed by running experiments on the simple objectives discussed above, and no rigorous of the whole claim is provided. The paper lacks a formal mathematical proof demonstrating the divergence in behavior between gradient descent on differentiable and non-differentiable objectives. The reliance on empirical observations from the simplified model weakens the claim, as it does not provide a theoretical basis for the observed differences. A more rigorous analysis would involve establishing theoretical conditions under which the optimization trajectories diverge, rather than relying solely on experimental evidence.

3. The paper argues on Page 4 that ”it is consistently observed that the optimal parameter values ... non-differentiability for ReLU activations”. This argument is wrong since zeros of the parameters in the neural networks are not necessarily points at non-differentiability, which depends both on the neural network inputs and the bias.

4. The argument in the last paragraph on Page 4 is also not strong since Tibshirani 2015 only proves the upper bound on the number of steps for subgradient methods. Saying the upper bound of one algorithm is different than the upper bound of the other algorithm is not sufficient to say that the two algorithms have different convergent behavior since the slower convergence rate might be an artifact of proof. The paper fails to demonstrate that the subgradient method's upper bound is tight, thus the comparison is not conclusive. The difference in upper bounds does not necessarily imply a difference in the actual convergence behavior of the algorithms. A more rigorous analysis would involve showing that the subgradient method's convergence rate is indeed slower in practice and not just an artifact of the theoretical bound.

5. The conclusion in Section 4 of the paper does not significantly deviate from previous viewpoints. In summary, the paper shows that the subgradient gradient method does not give sparse solutions for LASSO, which is a known fact. The paper also does not theoretically extend this argument to more complicated objectives such as neural networks. The analysis in this section does not provide any new insights into the behavior of subgradient methods on LASSO problems. The lack of theoretical extension to more complex objectives further limits the impact of this section, as it fails to address the core question of how non-differentiability affects optimization in neural networks.

6. In Section 5, the author argues that EoS have different behavior under non-differentiability, and uses Proposition 4 as a support. This is insufficient since the boundedness of the gradients is not related to either the progressive sharpening or the stabilization of the sharpness right above $2/\alpha$. The paper's argument relies on a definition of stability that is not directly applicable to non-smooth functions. The connection between the boundedness of gradients and the observed behavior of the edge of stability is not clearly established. A more rigorous analysis would require a definition of stability that is suitable for non-smooth functions and a clear explanation of how this definition relates to the observed phenomena.

7. In the first paragraph of Page 8, the paper tries to use the setting in Eq. 12 to experimentally contradict Ma et al. (2022). However, Eq. 12 deviates a lot from the practical neural network setup and conclusions on Eq. 12 may not directly apply to neural networks. The counterexample provided is based on a simplified model that does not reflect the complexity of neural networks. The conclusions drawn from this counterexample may not be generalizable to the scenarios considered by Ma et al., which involve more complex architectures such as VGG and ResNet.

### Questions
Please see "Weaknesses".

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper discusses three ways that non-differentiability impacts network training: by affecting the convergence rate, causing unreliable LASSO solutions, and breaking results from edge-of-stability analysis.

### Strengths
1. The paper is clearly structured.
2. Non differentiability is an interesting and important component of modern neural networks.

### Weaknesses
1. The authors imply that small VGG16 network weights are close to the "domain of non-differentiability." This is flawed, as weights and activations are not the same -- if for example the bias of the linear layer is a very large constant vector, then we have differentiability even from small weights.
2. The authors generally frame their analysis as "practical networks do not satisfy theoretical ssumption (e.g., L-smooth loss functions), therefore they don't apply." This is a fundamental misunderstanding of the importance of theory. Theory tends to study a "toy" scenario, and derive results that are insightful even if they don't directly apply. The authors fail to acknowledge that theoretical assumptions are often simplifications to make the analysis tractable, and the goal is to gain insights that generalize beyond the specific assumptions.
3. Generally, the paper consists of a few loosely connected ideas, and does not provide sufficient analysis for a conference at ICLR's level. The connections between the convergence rate, LASSO solutions, and edge-of-stability analysis are not well-established, and the paper feels like a collection of observations rather than a cohesive study.
4. Presented theoretical results are very simple. The analysis of the non-differentiable case is not sufficiently rigorous, and the results are not novel. The paper lacks depth in its theoretical contributions.

### Questions
1. The authors imply that edge of stability training doesn't hold for non-smooth networks. Does this not contradict with the cited Cohen paper, which uses standard networks with ReLU nonlinearities?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
