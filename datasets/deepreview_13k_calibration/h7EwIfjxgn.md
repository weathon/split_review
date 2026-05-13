# Sharpness-Aware Black-Box Optimization

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 10, 6, 5

## Abstract
Black-box optimization algorithms have been widely used in various machine learning problems, including reinforcement learning and prompt fine-tuning. However, directly optimizing the training loss value, as commonly done in existing black-box optimization methods, could lead to suboptimal model quality and generalization performance.
To address those problems in black-box optimization, we propose a novel Sharpness-Aware Black-box Optimization (SABO) algorithm, which applies a sharpness-aware minimization strategy to improve the model generalization. Specifically, the proposed SABO method first reparameterizes the objective function by its expectation over a Gaussian distribution. 
Then it iteratively updates the parameterized distribution by approximated stochastic gradients of the maximum objective value within a small neighborhood around the current solution in the Gaussian distribution space. 
Theoretically, we prove the convergence rate and generalization bound of the proposed SABO algorithm. 
Empirically, extensive experiments on the black-box prompt fine-tuning tasks demonstrate the effectiveness of the proposed SABO method in improving model generalization performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors strive to introduce SAM to the black-box optimization algorithm, and propose a new algorithm called Sharpness-Aware Black-box Optimization (SABO). SABO reparameterizes the objective function using its expectation over a Gaussian distribution and iteratively updates the parameterized distribution based on approximated stochastic gradients of the maximum objective value within a small neighborhood. The authors provide theoretical guarantees for SABO's convergence rate and generalization bounds. Also, they give empirical experiments to validate its effectiveness in improving model generalization performance on black-box prompt fine-tuning tasks and synthetic numerical problems.

### Strengths
1. The paper is clearly written, well organized and easy to follow.
2. I think the whole topic is intriguing and worthy to probe, and the authors give some interesting insights.
3. It is valuable to find that the proposed method could be effective in prompt tuning.

### Weaknesses
1. My primary concern is the motivation regarding the introduction of SAM in black-box optimization. In other words, can we safely use the proposed method in black-box optimization? The implicit premise of SAM relies on the smoothness of the mapping function. However, black-box optimization may deal with highly complex, non-smooth, or potentially noisy objective landscapes, scenarios much more complicated than optimizing neural networks. In my opinion, it is crucial for the authors to clarify the scope of which minimizing the maximization of the neighborhood region is appropriate for black-box optimization.

2. I noticed that in the algorithm, the authors use two different samples to separately calculate the ascent and descent gradients. Could the authors give some explanations here given that we always keep the same batch in SAM?

3. The essence of SAM involves two main steps: first, a maximization step using gradient ascent based on the current parameters with a step size of rho/||g||; and second, a minimization step using gradient descent based on the maximized parameters with a step size equal to the learning rate. What are the results of applying this procedure in the current black-box optimization?

4. The convergence analysis mostly relies on the assumption of convexity of F(x), which I think could be less useful.

5. Some minor mistakes: (1) Line 121, SAM is proposed by [Foretet al., 2021] not [Kwon et al., 2021].
(2) Eq 6. nabla_F(x + epsilon_t) should be rewrite as nabla_F(x)|x = epsilon_t

### Questions
See Weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
2

### Summary
This paper combines ideas from sharpness aware minimization (SAM) in machine learning with black-box optimization problems to propose a new algorithm called Sharpness-Aware Black-box Optimization (SABO). The goal of SABO is to improve the generalization performance of models by finding flat minima in the loss landscape, which are believed to lead to better generalization. The authors provide theoretical analysis of SABO's convergence rate and generalization bound, and they demonstrate its effectiveness through experiments on synthetic problems and black-box prompt fine-tuning tasks.

### Strengths
This is an interesting paper that combines ideas from sharpness aware minimization (SAM) with black box optimization. SAM has already proven to be a very useful technique to improve generalization in training ML models and the authors present an intuitive motivation for applying these ideas to BBO. SABO is a creative combination of SAM techniques and black box optimization methods. 

This paper has a strong theoretical analysis of SABO, including convergence rate and generalization error bounds. These theoretical results are then empirically validated on synthetic and real-worl black-box prompt fine-tuning models. 

The paper is very well-written and logically structured. The authors do a good job motivating their approach and everything is presented in a clear understandable manner.

### Weaknesses
Overall, I see no major weaknesses for this paper and some of these points raised here are covered in the questions below which might clear up these apparent weaknesses. For example, in eqn (8) there is a dependence on the parameter $\rho$. The performance of SABO would be sensitive to the neighborhood size $\rho$ in (8) and tuning this parameter would be critical for successful application of this technique. It would be nice to see methods which can automatically adapt this parameter in a useful way to reduce dependence on manual tuning. 

The authors do not mention in detail the increased computational cost of the sharpness-aware updates in SABO. One way to decrease computational cost, the authors assume the covariance matrix $\Sigma$ is diagonal. This seems like a fairly naive assumption and one I would assume is too simplistic in general. To address this problem in SAM for traditional ML settings, variants of SAM have been introduced. Could similar techniques be applied here?

The authors focus on Gaussian distributions for the search distribution. Is that a fair simplification? How effective or sensitive is SABO with other types of distributions that are likely to occur for parameters; e.g. heavy-tail distributions, or other posteriors that are more informative.

### Questions
- in the setup on line 177, you claim that for computational consideration you can assume the search distribution to be Gaussian. Is that a fair simplification? How sensitive is SABO to this choice of distribution and would it make more sense to sample the local parameter space in some way that captures the nature of the posterior rather than with a naive Gaussian?
 - related to above (line 180), is it fair to assume that the covariance matrix is diagonal. This seems optimistic and is essentially assuming no correlation between parameters, correct? And then your perturbations $\delta$ also have diagonal covariance. I understand that, as you point out in line 195, removing this assumption would make the problem computationally substantially more difficult.  Theoretically, how much of a sacrifice does this assumption make? and are there any other means you can use to not lose this amount of information?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces the Sharpness-Aware Black-Box Optimization (SABO) algorithm, enhancing model generalization in black-box optimization tasks by incorporating sharpness-aware minimization principles. Unlike traditional methods that may lead to poor generalization by focusing solely on training loss, SABO optimizes a Gaussian parameter distribution, finding "flat" minima that improve robustness. Through reparameterization and stochastic gradient approximation, SABO adapts Sharpness-Aware Minimization (SAM) for use without gradient information, making it suitable for black-box settings. Theoretical results demonstrate SABO's convergence and generalization bounds, and empirical evaluations on synthetic problems and prompt fine-tuning tasks show that SABO outperforms existing methods in high-dimensional settings, positioning it as a powerful tool for black-box optimization in machine learning.

### Strengths
- This paper is novel in that it extends sharpness-aware minimization (SAM) principles, typically used in gradient-based settings, to black-box optimization where gradients are unavailable.
- This paper is supported by rigorous theoretical analysis, including convergence rates and generalization bounds in both full-batch and mini-batch settings. 
- The empirical results highlight SABO’s practical value and potential to improve generalization in real-world applications where direct gradient access is unavailable.

### Weaknesses
 - Due to its reliance on iterative updates to a Gaussian distribution, along with stochastic gradient approximations and KL divergence constraints, this method may incur higher computational costs per iteration compared to some existing black-box optimization methods, especially in high-dimensional settings. A discussion of the time complexity for various black-box optimization algorithms would strengthen the paper.

- This paper introduces additional hyperparameters (e.g., neighborhood size for KL divergence) that require careful tuning to achieve optimal performance. Discussing the sensitivity of these hyperparameters would improve the analysis.

- Although the proposed method is evaluated on prompt fine-tuning tasks, the backbone model used in the experiments may not be sufficiently representative. Evaluating it on a larger model, such as LLaMA-7B, would provide a stronger assessment of its effectiveness.

### Questions
Please see weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies Sharpness-Aware Minimization in the context of black-box optimization. It introduces Sharpness-Aware Black-Box Optimization (SABO), which is the first to design a sharpness-aware minimization strategy specifically for black-box optimization. The key contributions include the formulation of the SABO algorithm, convergence results, generalization bounds, and extensive empirical validation through experiments on both synthetic benchmark functions and black-box prompt fine-tuning tasks.

### Strengths
- The paper is well-written and easy to follow.
- The proposal of integrating SAM techniques into black-box optimization is interesting. They show clearly how to achieve the update algorithm. The paper provides proofs for the convergence rate and generalization bounds.
- Comprehensive experiments are conducted on synthetic benchmarks and real-world tasks (black-box prompt fine-tuning for large language models). Results show that SABO outperforms other methods.

### Weaknesses
 - The paper lacks evidence that SABO can find flat minima, even though this is their motivation for improving model generalization. The connection between the proposed method and the actual flatness of the minima found is not clearly established. While the method is inspired by SAM, it's not clear if the optimization in the distribution space directly translates to finding flatter minima in the parameter space, which is the typical goal of sharpness-aware methods.
- The paper lacks a strong motivation for why we need Sharpness-Aware Minimization for black-box optimization, aside from the fact that it may help improve generalization. Could the authors identify the problems that existing black-box optimization methods encounter and demonstrate how SABO addresses these issues? The paper should provide a more detailed analysis of the limitations of current black-box optimization techniques, particularly in the context of model generalization, and how SABO specifically overcomes these limitations. It's not sufficient to simply state that SAM is successful in white-box settings; a clear argument for its necessity in black-box optimization is needed.
- Assumption 4.1 is narrow because it includes both L-smoothness and H-Lipschitz conditions; typically, we only assume one of them. For example, the simple function $f(x) = x^2$ satisfies L-smoothness but does not satisfy H-Lipschitz. The assumption should be relaxed to be more applicable to a wider range of functions. The current assumption limits the theoretical scope of the paper.
- In Theorem 4.3, the assumption is too strong for real applications in neural networks. The result in Lin et al. [2022] is more general. The theoretical results should be compared more directly to existing work, and the limitations of the current assumptions should be clearly stated.
- Theorem 4.6 is not strong because the assumptions are overly restrictive, which limits the practical applicability of this theorem. The assumptions for the generalization bound are too strong and not realistic for practical applications, limiting the impact of the theoretical results.
- The empirical convergence results of SABO in synthetic problems do not show much improvement over INGO. The convergence plots do not demonstrate a significant advantage of SABO over existing methods in the synthetic benchmarks, which raises questions about its practical value in these settings.
- The empirical results in Table 1 are not very significant, showing only around a 0-1% improvement, even for datasets with low accuracy such as RTE and SNLI. The improvements in the empirical results are marginal, particularly on datasets with low accuracy, which does not strongly support the effectiveness of the proposed method.

### Questions
- Could you provide a table showing how selecting the neighborhood size $\rho$ affects both convergence and performance?
- What specific $\rho$ would you recommend to ensure stability?
- Could the authors include a comparison of computational usage against other methods in Table 1?
- Could the authors provide a comparison of your theoretical and empirical results with the paper Lin et al. [2022]?
- See the Weakness part.

Tianyi Lin, Zeyu Zheng, and Michael Jordan. Gradient-free methods for deterministic and stochastic nonsmooth nonconvex optimization. Advances in Neural Information Processing Systems, 35:26160–26175, 2022.

### Soundness
2

### Presentation
3

### Contribution
2
