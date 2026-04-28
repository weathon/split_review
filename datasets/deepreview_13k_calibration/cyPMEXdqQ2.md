# Overcoming Lower-Level Constraints in Bilevel Optimization: A Novel Approach with Regularized Gap Functions

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Constrained bilevel optimization tackles nested structures present in constrained learning tasks like constrained meta-learning, adversarial learning, and distributed bilevel optimization. 
However, existing bilevel optimization methods mostly are typically restricted to specific constraint settings, such as linear lower-level constraints. 
In this work, we overcome this limitation and develop a new single-loop, Hessian-free constrained bilevel algorithm capable of handling more general lower-level constraints. 
We achieve this by employing a doubly regularized gap function tailored to the constrained lower-level problem, transforming constrained bilevel optimization into an equivalent single-level optimization problem with a single smooth constraint. 
We rigorously establish the non-asymptotic convergence analysis of the proposed algorithm under the convexity of lower-level problem, avoiding the need for strong convexity assumptions on the lower-level objective or coupling convexity assumptions on lower-level constraints found in existing literature. 
Additionally, the generality of our method allows for its extension to bilevel optimization with minimax lower-level problem. 
We evaluate the effectiveness and efficiency of our algorithm on various synthetic problems, typical hyperparameter learning tasks, and generative adversarial network.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies a bilevel problem where lower-level problem is convex with coupled constraints. To avoid joint projection onto the coupled constraint set which requires coupling convexity and is costly, this paper introduces a doubly regularized gap function to convert lower-level problem into a smooth constraint. This constrained problem is then solved by penalty method. Convergence analysis is provided and numerical results validate the effectiveness of the proposed method.

### Strengths
1. This work tackles an important bilevel problem which involves coupled constraints at the lower level.
2. The design of the doubly regularized gap function is novel and effective. 
3. The numerical studies are comprehensive and thorough.

### Weaknesses
This paper addresses a relaxation of the original bilevel problem through a penalty reformulation and truncation approach. For the penalty reformulation, it is shown that by selecting a sufficiently large penalty constant $c$, the penalty problem becomes an $\epsilon$-approximate solution to the original problem. At the same time, the truncation parameter $r$ also appears to need a large value to ensure equivalence with the original problem. But in the final convergence theorem, $r$ is chosen as a constant, independent of the target error $\epsilon$. This raises concerns about the practical applicability of the method, as the choice of $r$ is not directly linked to the desired accuracy, potentially leading to suboptimal performance or requiring extensive tuning. Furthermore, the paper does not provide a clear strategy for selecting the penalty parameter $c$ other than it being sufficiently large, which is not practical. The lack of a systematic approach for choosing both $r$ and $c$ makes the algorithm's performance highly dependent on the user's ability to select these parameters appropriately. 

In Proposition 3.1, it is assumed that the optimal solution $(x^*,y^*,z^*)$ to (6) exists with finite $z^*$. How can this be guaranteed? The paper mentions constraint qualification conditions in Remark 2.5, but it does not explicitly state which conditions are required and how they are verified in practice for the specific lower-level problem. Additionally, how should $r$ be chosen in practice? Setting $r$ too large may hinder algorithm convergence, while choosing $r$ too small could exclude the optimal point $z^*$, which is unknown. The paper suggests tuning $r$ based on problem-specific characteristics, but this lacks concrete guidance and may require significant trial and error. 

Additionally, several concurrent related works are missing: [1]--[2].

In Table 3, the term "Required accuracy" could be replaced with a word like "Time" to clarify the values reported. As it stands, it is unclear whether the numbers in this table represent accuracy or computation time.

### Questions
In Proposition 3.1, it is assumed that the optimal solution $(x^*,y^*,z^*)$ to (6) exists with finite $z^*$. How can this be guaranteed? Additionally, how should $r$ be chosen in practice? Setting $r$ too large may hinder algorithm convergence, while choosing $r$ too small could exclude the optimal point $z^*$, which is unknown. 

Additionally, several concurrent related works are missing: [1]--[2]. 

[1] A Primal-Dual-Assisted Penalty Approach to Bilevel Optimization with Coupled Constraints. L Jiang, et. al. arXiv:2406.10148. 

[2] First-Order Methods for Linearly Constrained Bilevel Optimization. G Kornowski, et.al. 	arXiv:2406.12771.

In Table 3, the term "Required accuracy" could be replaced with a word like "Time" to clarify the values reported. As it stands, it is unclear whether the numbers in this table represent accuracy or computation time.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces a method for transforming constrained bilevel optimization problems with coupled lower-level constraints into a single-level problem with a smooth constraint, employing a doubly regularized gap function. Based on this reformulation, the authors propose a first-order single-loop penalty-based algorithm called BiC-GAFFA. Theoretically, they establish non-asymptotic convergence results under general assumptions. Additionally, they investigate the extension of the proposed algorithm to bilevel optimization problems featuring minimax lower-level problems, a topic that has received limited attention in the existing literature. Extensive experiments are conducted to validate the practicality, robustness and efficiency of BiC-GAFFA, encompassing multiple complex problem models within the learning problems.

### Strengths
1.The paper introduces a smooth constrained reformulation for bilevel optimization with a constrained lower-level problem. This reformulation avoids the use of any implicit functions associated with the lower-level problem, which are typically known to necessitate additional iterations or inexact solutions.

2. The authors present the first-order single-loop algorithm BiC-GAFFA, which exhibits overall complexity that is lower than that of many existing first-order algorithms requiring double-loop iterations. Notably, it does not rely on the assumption of full convexity of the lower-level constraints.

3. When updating the proximal variable $\lambda$ associated with the multipliers $z$, there is no need to compute the gradient of the gap function. Instead, the update can be effectively executed solely by applying the first-order optimality conditions of the maximization problem.

4. BiC-GAFFA possesses a broader range of potential applications, making it suitable for solving bilevel optimization problems where the lower-level problem is a minimax problem. Existing bilevel optimization algorithms are unable to achieve this simultaneously.

### Weaknesses
1. From Section 6.2 and A.2.2., we observe that when dealing with nonsmooth problems, such as sparse group lasso and SVM, it is necessary to reformulate them into a smooth form for effective resolution. This reliance on smoothing techniques, while common, introduces approximations that may not accurately reflect the original problem's characteristics, potentially impacting the solution quality and limiting the applicability of the algorithms to problems where such smoothing is not straightforward or introduces significant error. The practical implications of this smoothing, especially in terms of solution accuracy and convergence speed, are not thoroughly explored.

2. By introducing the gap function, the authors have designed a single-loop algorithm. However, the dimensionality of the introduced variables remains the same as that of the original problem, resulting in an increased iteration scale. Compared to LV-HBA proposed in [1], there is no significant improvement in mathematical representation or convergence results. The computational overhead of this increased dimensionality, particularly in large-scale problems, is a concern that warrants further investigation. The paper does not provide a detailed analysis of the computational cost associated with the increased variable space, nor does it offer a comparison of the practical runtime performance against existing methods.

3. The necessity to control multiple iteration step sizes within the algorithm significantly affects the convergence theory and empirical performance, making them highly dependent on the adjustment of these step size parameters. The paper lacks a systematic approach for selecting these step sizes, and the convergence analysis does not provide clear guidance on how to choose them optimally. This sensitivity to step size parameters makes the algorithm less robust and requires careful tuning for each specific problem, which is a significant practical limitation.

### Questions
1. The convergence results for extending the proposed algorithm to bilevel optimization problems with minimax lower-level problems are lacking, which leads to that Section 5 feels somewhat abrupt overall.

2. In the experimental settings, we observe that the step sizes $\alpha_k$ and $\eta_k$ are fixed or vary in a specific form. Are the step sizes related to the specific formulations of different problems?

Some more detailed questions:

1. Can the conclusion of Lemma 2.1 be stated as "$\mathcal{G}_\gamma(x,y,z)=0$ if and only if $y\in S(x)$ and $z\in \mathcal{M}(x, y)$"?

2. In line 845, the loss function in lower-level problem should be $\mathcal{L}_{tr}$.

3. In line 1007, can you provide the specific mathematical format of the functions $\mathcal{L}_{gen/det}$

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
The paper introduces a novel algorithm for constrained bilevel optimization (BiO) using a regularized gap function to transform bilevel problems with lower-level (LL) constraints into a single-level optimization problem with a smooth inequality constraint. The authors propose a first-order, single-loop algorithm, BiC-GAFFA, that operates without requiring Hessian evaluations or projections onto the LL constraint set, offering both theoretical convergence results and empirical validation on synthetic and real-world tasks, such as hyperparameter optimization and generative adversarial networks (GANs). The paper also presents an extension of the method to minimax lower level problems, which broadens its applicability.

### Strengths
1. The introduction of the doubly regularized gap function is a novel (as far as I am aware in the context of bilevel optimization) solution to deal with constraints at the lower level in bilevel optimization. This regularization allows the transformation of the bilevel problem into a smooth optimization problem, which simplifies the numerical implementation and analysis. 

2. The proposed BiC-GAFFA algorithm avoids costly second-order computations, which is usually the case for methods based on constrained optimization reformulation. The single-loop nature of the algorithm is also computationally efficient, as supported by the non-asymptotic convergence analysis. 

3. The extension to minimax inner level problems provides flexibility in dealing with a broader class of problems beyond the traditional settings.

### Weaknesses
1. Some theoretical assumptions are insufficiently justified (i.e. very weak statement), particularly in Remark 2.5, where it’s stated that the existence of a multiplier in Theorem 2.3 “can be guaranteed” under certain constraints qualification conditions like MFCQ. Is the assumption in fact guaranteed when the constraints qualification conditions are satisfied? Or does those conditions directly imply that the assumption is satisfied? Please clarify. 

2. The update steps in BiC-GAFFA are quite similar to existing constrained optimization reformulation methods, such as primal-dual [1] and dynamic barrier [2] methods. While these approaches have been applied successfully in other constrained settings, the paper does not explain why they are inadequate for the additional lower-level constraint here, suggesting a need for BiC-GAFFA. A discussion on this distinction would help clarify the necessity of more complex methods such as the proposed BiC-GAFFA. Specifically, the paper should discuss the limitations of applying primal-dual or dynamic barrier methods directly to the bilevel problem with lower-level constraints, and why the proposed doubly regularized gap function is necessary to circumvent these limitations.

3. The algorithm requires additional sequences (e.g.,  $\theta_k$  and  $\lambda_k$), adding to the computational and memory load, which may challenge its feasibility for large-scale applications. The paper does not provide a detailed analysis of the computational overhead introduced by these additional sequences, nor does it explore strategies to mitigate this overhead. A more thorough discussion of the practical implications of these additional sequences is needed, particularly regarding memory usage and computational time for large-scale problems.

4. The experimental results focus on toy numerical problems and small-scale real-world problems. While these results are encouraging, a broader evaluation on large-scale or diverse domains would better demonstrate BiC-GAFFA’s practical applicability and scalability. The current experiments do not sufficiently demonstrate the method's performance on complex, high-dimensional problems, which are common in real-world applications of bilevel optimization. The paper should include experiments on more challenging datasets and models to provide a more comprehensive evaluation of the proposed method.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work studies bilevel problems where the LL problem is constrained. 

The key contributions are:

1. The equivalence between main problem and the smoothed problem (6) under convexity.

2. The relation between (6) and the sequence of problems in Thm 3.3

3. A gradient based algorithm with nonasymptotic grad-norm rate for an instance of problem 3.3

Strength:

1.The paper is technically sound. 

2.The comparison against known results are clear, and hence the main contributions are clear.

3. I like the discussions on reformulations and the experiments.

Weakness:
I hope the authors could address my concerns below.

1. When and why would constraints in the LL be necessary? 

a. GAN would not require constraints.

b. SVM has uncontrained versions.

c. Hyperparameter tuning / data selection can be solved with more naive approach without bilevel problems.

2. There are more than one way to smoothen/regularize the lower level so that the limit is the original problem.

For example: one can add positive coefficients c1, c2, so that the bilevel is now F +  c1 f + c2 max(g, 0) . Then by sending c1, c2/c1 to infinity, one could also get an approximate solution. Why would one formulation better than another?


Minors: 
1. The notation N_Y(y) and other similar ones are not defined.

### Strengths
See summary

### Weaknesses
1. When and why would constraints in the LL be necessary?

a. GAN would not require constraints.

b. SVM has uncontrained versions.

c. Hyperparameter tuning / data selection can be solved with more naive approach without bilevel problems.

2. There are more than one way to smoothen/regularize the lower level so that the limit is the original problem.

For example: one can add positive coefficients c1, c2, so that the bilevel is now F +  c1 f + c2 max(g, 0) . Then by sending c1, c2/c1 to infinity, one could also get an approximate solution. Why would one formulation better than another?


Minors: 
1. The notation N_Y(y) and other similar ones are not defined.

### Questions
See summary

### Soundness
3

### Presentation
2

### Contribution
2
