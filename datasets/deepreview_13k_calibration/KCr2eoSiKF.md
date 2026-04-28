# Learning-Augmented Robust Algorithmic Recourse

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
The widespread use of machine learning models in high-stakes domains can have a major negative impact, especially on individuals who receive undesirable outcomes. Algorithmic recourse provides such individuals with suggestions of minimum-cost improvements they can make to achieve a desirable outcome in the future. However, machine learning models often get updated over time and this can cause a recourse to become invalid (i.e., not lead to the desirable outcome). The robust recourse literature aims to choose recourses that are less sensitive, even against adversarial model changes, but this comes at a higher cost. To overcome this obstacle, we initiate the study of algorithmic recourse through the learning-augmented framework and evaluate the extent to which a designer equipped with a prediction regarding future model changes can reduce the cost of recourse when the prediction is accurate (consistency) while also limiting the cost even when the prediction is inaccurate (robustness). We propose a novel algorithm for this problem, study the robustness-consistency trade-off, and analyze how prediction accuracy affects performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors study in this paper the notion of robust recourse. A recourse is defined in the first paragraph: it ``provides each individual who was given an undesirable label with a minimum cost improvement suggestion to achieve the desired label”. The problem studied here is that the classifier may change (for example, it could be updated as new data arrive), which can invalidate the recourse.

The paper subsequently consider a recourse found by solving a min-max problem: the minimization is over the space of input feature, the maximization is over the perturbation set of the model parameter. The authors propose Algorithm 1, which is proved to converge to the global optimal solution under specific condition. The results are supported empirically by the numerical experiments with three real world datasets.

### Strengths
1. The paper proposed Algorithm 1, which can compute the robust recourse to global optimality, despite the non-convexity of the robust recourse problem.

### Weaknesses
1. The guarantee is only for a generalized linear model, a 1-norm cost on $x$ and an $\infty$-norm neighborhood for $\theta$.

2. It is unclear how the insights from the learning-augmented framework has impacted the main contributions of this paper. I feel that I can omit all the sentences discussing learning-augmented framework without changing meaning/results/implications of the paper. 

3. Despite the positive results for the case presented in the paper, it is unclear how the result can be extended to any other settings (different cost, or nonlinear model without linear surrogate, etc.)

### Questions
1. Is there any convergence guarantee for the algorithm in Section C2? If there is no convergence guarantee, then how could we interpret the results in the numerical experiments? Could we attribute the superior performance of the recourse to the algorithm or to the different loss function?

2. Please provide out-of-sample validity results. In the experiment settings of ROAR, the out-of-sample can simulate different shifts of the ML models. The out-of-sample validity computed this way is a more practical criterion to compare different methods. In fact, the set $\Theta_\alpha$ is only a proxy to model our belief about future model perturbation, and it has no real meaning when we compute the worst-case validity.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the author proposes a learning-augmented method for generating algorithmic recourse by accounting for the dynamic behavior of the target model. They assume that the designer has access to an unreliable prediction model, which can be leveraged to improve upon prior robust recourse methods. By identifying an anchor using the unreliable model, they assess the consistency between the generated recourse and this anchor. The problem then shifts to finding an optimal balance between robustness and consistency.

### Strengths
1 The topic is quite interesting. It points out an interesting topic of algorithmic recourse.
2 The algorithm is concise and a theoretical guarantee is provided.
3 Several experiments are implemented.

### Weaknesses
1 The presentation lacks clarity. Although the innovation is highlighted at the beginning, it’s unclear why the learning-augmented framework is proposed as the solution to this issue. There seems to be a logical gap in Section 3 that needs to be addressed. Specifically, the connection between the unreliable prediction model and the need for a learning-augmented approach is not well-established. It's not immediately obvious why leveraging an unreliable model, instead of focusing on improving the robustness of the recourse directly, is the chosen path. The motivation for introducing consistency as a performance metric, given the unreliability of the prediction model, requires further justification.
2 Their method is quite limited, as it only considers the case of linear model. While the authors present an algorithm for the linear case, the applicability of this approach to more complex models is not sufficiently explored. The experiments do not adequately address the limitations of using a linear approximation for non-linear models, and the practical implications of this approximation on the quality of recourse are not clear.
3 In Section 3, they mention that the prediction model is unreliable, yet it is still used to measure the consistency of the algorithmic recourse. However, they do not explain how the uncertainty of the prediction model is measured or the extent to which this uncertainty impacts the solution. The paper lacks a discussion on how the degree of unreliability in the prediction model affects the balance between robustness and consistency. It's unclear how the method would perform under varying levels of prediction model accuracy.

### Questions
1  Could you further strenthen the intuition of your method? I suggest that the author provide a clear reason for adopting the learning-augmented framework for this task and include more information in the related work section.
2 Coud you add a case study to demonstrate the advantages of the proposed method?
3 If possible, could you consider a more general case of the target model, e.g. MLP?

### Soundness
2

### Presentation
1

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
The paper studies the problem of robustness of algorithmic recourse in the context of model shifts. The authors propose an algorithm to optimize a well-established adversarial min-max objective in the context of generalized linear models. Additionally, they consider the setting in which we have access to an estimate of the model change $\hat{\theta}$ and show there is a trade-off between robustness and consistency in several experiments. They also perform some validation considering two baselines (ROAR and RBR).

### Strengths
The paper tackles a relevant problem of the recourse literature, namely, the robustness of counterfactual explanations to model shifts. The paper is relatively easy to follow, and it focuses on studying a simple yet potentially important phenomenon arising from the trade-off between consistency and robustness (or regret).

### Weaknesses
I have some concerns about the novelty and experimental analysis of the proposed approach. In general, some design choices (e.g., assuming to know the model shift), are interesting, but they could be better explored.

**[Contributions]**  In Section 1, the statement “the first optimal algorithm for any robust recourse problem” is misleading. There are other settings in which recourse robustness is required in which your method might **not** achieve the optimal (see [1] for an exhaustive list). Moreover, one could argue that in practice most models are deep neural networks, thus making the paper’s approach lose any guarantees. 

**[Learning-Augmented Framework]** The authors consider a setting in which they have access to a prediction over the new model parameters $\hat{\theta}$. In practice, one could simply compute solutions for robust recourse using standard methods (e.g., ROAR, RBR) by considering the updated model $f_{\hat{\theta}}$. This consideration undermines the overall contribution to the approach (since both objective (3) and metrics (5), (6) are very similar to related cited literature). I recommend that the authors discuss the limitations/issues arising from obtaining a prediction of the model update and/or propose a computational model to describe them better. 

**[Algorithm 1]** Section 3.1 would benefit a computational complexity analysis of Algorithm 1. It might as well achieve the global optimum, but if it is exponential in the number of features we could settle for approximate solutions. Lastly, in the case of a local approximation, Algorithm 1 might not be optimal anymore, and the authors should discuss the limitations of their approach in such a scenario.

**[Experimental Analysis with $\hat{\theta}$]** 
- Following the [**Learning-Augmented Framework**] comment, it is not clear if the analysis in Section 4 considers competitors (ROAR and RBR) using the predicted model $f_{\hat{\theta}}$ or the original $f_{\theta}$. The latter case would penalize the competitors and it would result in an unfair comparison between the approaches. 
- In Section 4 (Figure 2), the authors consider a simple setting in which the $\alpha$ parameter in Algorithm 1 is the same used to perturb the model. I believe it is a simplifying assumption since in practice we might have access to a noisy estimator of $\alpha$. 
- The experiments could benefit from additional baselines using adversarial min-max objectives (e.g., Dominguez-Olmedo et al., 2022 can be run without the causal structure, by only considering the $\epsilon$-ball) or other forms of robustness (see Section 4 of [1] for a fairly large list).

### Questions
- Could you provide a computational complexity analysis for Algorithm 1?
- What if the $\alpha$ you consider as perturbation in the experiments (Figure 2) is different from the actual $\alpha$ used by Algorithm 1?
- Do you compute recourses with ROAR and RBR by considering the model with parameters $\hat{\theta}$ or the original $\theta_0$?
- How do you evaluate the recourses computed on the LIME surrogate? Do you consider the validity of the original non-linear model $f_\theta$?

### Soundness
2

### Presentation
3

### Contribution
2
