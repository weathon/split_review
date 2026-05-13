# fairret: a Framework for Differentiable Fairness Regularization Terms

- Decision: Accept
- Scores: 8, 5, 8, 3

## Abstract
Current fairness toolkits in machine learning only admit a limited range of fairness definitions and have seen little integration with automatic differentiation libraries, despite the central role these libraries play in modern machine learning pipelines.

    We introduce a framework of fairness regularization terms (\textsc{fairret}s) which quantify bias as modular, flexible objectives that are easily integrated in automatic differentiation pipelines. By employing a general definition of fairness in terms of linear-fractional statistics, a wide class of \textsc{fairret}s can be computed efficiently. Experiments show the behavior of their gradients and their utility in enforcing fairness with minimal loss of predictive power compared to baselines. Our contribution includes a PyTorch implementation of the \textsc{fairret} framework.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a tool that implemented generalized group fairness metrics that can be used in automatic differentiation libraries. The fairness metrics are expressed as a linear-fractional statistic, which can be further represented as a smoothed regularization term. The authors also present an alternative projection method that penalize the divergence between models. Through extensive experiments, the authors shows the framework is lucrative for the optimization of fairness constraints.

### Strengths
- The presented SmoothMax regularization terms are elegant and provide expressive representations for widely applied group fairness metrics.
- The methods can be combined with automatic differentiation tools, such as PyTorch.
- The methods can be naturally applied with multiple axes of sensitive attributes, allowing wider applications.

### Weaknesses
 - The method still applies relaxed fairness metrics, rather than the exact metrics as the regularization terms. Specifically, the use of probabilistic classifiers and the smoothing of the max operator in the linear-fractional statistic inherently approximate the true fairness constraints. This relaxation, while enabling differentiability, may lead to solutions that do not strictly satisfy the desired fairness criteria, especially in scenarios where the probabilistic outputs are not well-calibrated or when the decision boundary is sharp.
- A superior learning objective should be a minimax game with the optimization of the $\lambda$-player. As far as my understanding, the authors use fixed $\lambda$ values as a hyper-parameter and run grid search to get the optimal results. This approach is suboptimal because it does not adapt the regularization strength based on the current state of the model's fairness. A fixed $\lambda$ might either over-regularize early in training, hindering convergence, or under-regularize later, failing to achieve the desired fairness level. The lack of an adaptive mechanism for $\lambda$ limits the framework's ability to dynamically balance accuracy and fairness during the optimization process.

### Questions
1. If the model $h$ is not a probabilistic classifier, then Equation (4) is no longer differentiable. Can the framework still be useful? 
2. How is the projection $f^\star$ initialized in the constrained optimization problem of Equation (5)?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a general framework for formulating fairness regularization terms which are differentiable. Their framework encompasses a wide range of group fairness notions. The authors then propose a series of regularizers for enforcing the fairness definitions. Finally, an experimental evaluation is given.

### Strengths
I think the authors propose a valuable contribution to the fairness community. Specifically, I appreciate the effort the authors make on combining multiple fairness notions into a general framework. I also think that providing a python package can be valuable for research and adaptation of fairness in ML.

### Weaknesses
The theoretical contribution of this work is in my opinion quite limited. While combining different fairness notions is valuable, I do not think that this is in itself a theoretical contribution. For instance, if in (3) you fix $\overline{\gamma}(h)=c$, then a norm based regularizer would be convex in $f(X)$. Thus if the model is linear, you would get a convex regularizer. Combine this with a convex $\mathcal{L}_Y$ and your problem is convex in the model parameters. This would allow you to get fast convergence rates.

Furthermore, the paper's focus on linear-fractional statistics, while encompassing common fairness metrics, inherently limits its ability to capture complex, non-linear relationships between sensitive attributes and model outputs. The use of a fixed \(\overline{\gamma}(h)=c\) to achieve convexity, while simplifying optimization, may also restrict the expressiveness of the fairness constraints, potentially leading to suboptimal solutions in scenarios where more nuanced fairness adjustments are needed. The framework, while general, does not seem to offer any novel theoretical insights into the trade-offs between fairness and accuracy, or the convergence properties of the proposed regularizers beyond the simple convex case.

### Questions
Some minor questions:
- Why do you call your method "Partition Fairness" and not "Group Fairness" as is common in the literature?
- Regarding continuous sensitive variables. It seems that this approach only captures linear correlation between the sensitive variables and the score. Is this correct?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors study the problem of fairness in ML. To be specific, they introduce a formal framework which facilitates defining regularization terms for fairness which can be minimized using auto-differentiation tools. The authors report significant improvements over baselines.

### Strengths
+ The paper provides a good formal coverage of the fundamental concepts.

### Weaknesses
1. I have concerns about the novelty. It appears that the paper's novelty is a formal fairness regularization framework. The paper criticizes existing frameworks for not being formal and limited in terms of fairness definitions. However, the paper does not showcase what the benefit of this formal framework is. Specifically, it is not clear how this framework enables the definition of novel fairness measures that are not already possible with existing tools. Moreover, it is not clear why FFB or FairTorch cannot be extended to include more fairness definitions through modular design or other software engineering techniques. The paper needs to demonstrate a concrete advantage of the proposed formalism beyond simply stating that existing methods are less formal.

2. I find "fairness tools" misleading. This term is used inconsistently, sometimes referring to fairness measures themselves, sometimes to their approximations as regularization terms, and sometimes to the specific implementations of these approximations. This lack of clarity makes it difficult to follow the technical arguments and understand the precise contributions of the paper.

### Questions
Please see Weaknesses.

**After Rebuttal**

I've read the comments provided by other reviewers and the responses by the authors. I find that the authors have sufficiently addressed my concerns. Looking at the sample code in Appendix E and the implementations in FFB, I see the contribution of the paper better. I think it will be beneficial for the community. Therefore, I've changed my recommendation.

### Soundness
3 good

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Paper claims that current tools for machine learning fairness only admit a limited range of fairness definitions and have seen little integration with automatic differentiation libraries.
For this reason they introduce a framework of fairness regularization terms which quantify bias as modular objectives that are easily integrated in automatic differentiation pipelines.

### Strengths
The overview, FAIRRET, and results are interesting and valuable.

### Weaknesses
Authors claim is an overstatement in fact there are plenty of work that proposes differentiable (and in some case even convex) regularisers.
State of the art is largely incomplete.

Regarding comparison with baselines i think that  (Adel et al. 2019) is not enough nether a state-of-the-art baseline given the large amount of more recent works.
Regarding the comment on the fact that just demographic parity is tested, i think is not accurate. Most group fairness definitions (e.g., equal odds, equal opportunity, uncorellation) can be defined under the same hat bus simply constraining the distribution of the representation to be close for a subset of the data distribution (e.g., for equal opportunity the distribution of the representation of the male labeled with +1 and the distribution of the representation of the female labeled with +1).
Regarding the claim of differentiability, there is a number of works which propose both differentiable or even convex relaxation of the fairness definitions with theoretical properties so the statement for me is still too much.
All these comments led me to my low rank: paper novelty, in my opinion, is limited since large amount of related works are not properly compared to the proposal neither theoretically nor empirically.

### Questions
There are plenty of work that proposes differentiable (and in some case even convex) regularisers (e.g. [1] but in ICML, NeurIPS, etc. you can find plenty of work on this). Paper should elaborate on that.

[1] Exploiting MMD and Sinkhorn Divergences for Fair and Transferable Representation Learning, NeurIPS 2020.
[2] Deep Fair Models for Complex Data: Graphs Labeling and Explainable Face Recognition, Neurocomputing 2021.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
