# Optimistic Games for Combinatorial Bayesian Optimization with Application to Protein Design

- Decision: Accept
- Scores: 8, 8, 3, 3

## Abstract
Bayesian optimization (BO) is a powerful framework to optimize black-box expensive-to-evaluate functions via sequential interactions. 
In several important problems (e.g. drug discovery, circuit design, neural architecture search, etc.), though, such functions are defined over large \emph{combinatorial and unstructured} spaces. This makes existing BO algorithms not feasible due to the intractable maximization of the acquisition function over these domains. 
To address this issue, we propose \textsc{GameOpt}, a novel game-theoretical approach to combinatorial BO.
\textsc{GameOpt} establishes a cooperative game between the different optimization variables, and selects points that are game \emph{equilibria} of an upper confidence bound acquisition function. These are stable configurations from which no variable has an incentive to deviate -- analog to local optima in continuous domains. Crucially, this allows us to efficiently break down the complexity of the combinatorial domain into individual decision sets, making \textsc{GameOpt} scalable to large combinatorial spaces. %
We demonstrate the application of \textsc{GameOpt} to the challenging \emph{protein design} problem and validate its performance on four real-world protein datasets. Each protein can take up to $20^{X}$ possible configurations, where $X$ is the length of a protein, making standard BO methods infeasible.
Instead, our approach iteratively selects informative protein configurations and very quickly discovers highly active protein variants compared to other baselines.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a novel method that frames the protein design task as an optimization problem of finding a Nash Equilibrium (NE) with unknown utility functions. It provides sample efficiency guarantees, and empirical results using multiple NE solvers suggest promising improvements over existing baselines.

### Strengths
- ***Innovative Formulation***: The paper introduces an interesting formulation by shifting the focus from kernel design for protein structures to an objective that reflects the insight that multiple separate contributing factors exist within protein design tasks.

- ***Sample Efficiency Guarantee***: The algorithm comes with a sample efficiency guarantee, which is valuable for practical scientific experimental design tasks where data collection can be costly and demand a principled optimization solution.

### Weaknesses
 - ***Limited Novelty in BO Guarantees***: The Bayesian Optimization (BO) component naturally inherits the guarantees of the Upper Confidence Bound (UCB) algorithm. There doesn't appear to be a significant difference or improvement, especially considering that the method does not address specific challenges unique to protein design. The theoretical guarantees, while present, do not seem to offer a substantial advantage over standard BO methods, particularly in the context of high-dimensional protein sequence spaces where the assumptions of UCB might not hold. The paper should more clearly articulate how the NE formulation provides a practical benefit beyond what can be achieved with standard BO techniques.
- ***Lack of Comparison with High-Dimensional BO Methods***: BO methods tackling protein design typically involve specific treatments for high-dimensional spaces. Including comparisons against these methods would strengthen the paper, especially when ESM embedding allows the direct application of such methods. The absence of comparisons with methods that explicitly address high-dimensional discrete search spaces, such as those using trust region approaches or variable selection techniques, is a notable gap. This makes it difficult to assess the true practical value of the proposed method in the context of state-of-the-art BO for protein design.

- ***Challenges in Finding Nash Equilibrium***: Given that finding a Nash Equilibrium is PPAD-complete and challenging even with state-of-the-art solvers, could the authors provide more insight and detailed discussion on optimizing the equilibrium for protein applications, especially in high-dimensional cases? The paper could better illustrate why the benefits of introducing the equilibrium outweigh the additional challenges rather than implying that solvers are guaranteed to find the NE. This clarification would prevent confusion among readers not familiar with the literature, especially since multiple NE solvers are discussed while claiming guarantees of finding local optima. The paper needs to address the practical limitations of finding a true Nash Equilibrium in high-dimensional protein sequence spaces, where convergence to a meaningful equilibrium is not guaranteed and the computational cost can be prohibitive. The discussion should include a more nuanced analysis of the trade-offs between the theoretical benefits of the NE formulation and the practical challenges of its implementation.
- ***Price of Anarchy Discussion***: The discussion of the price of anarchy briefly addresses the motivation for the problem formulation but is not sufficiently convincing. Providing more details and insights specific to protein design tasks could improve the presentation and strengthen the argument. The current discussion lacks a concrete explanation of how the price of anarchy relates to the specific challenges of protein design. The paper should provide a more detailed analysis of the potential suboptimality introduced by the NE formulation and how this relates to the overall goal of finding high-fitness protein sequences.

### Questions
- ***Challenges in Finding Nash Equilibrium***: Given that finding a Nash Equilibrium is PPAD-complete and challenging even with state-of-the-art solvers, could the authors provide more insight and detailed discussion on optimizing the equilibrium for protein applications, especially in high-dimensional cases? The paper could better illustrate why the benefits of introducing the equilibrium outweigh the additional challenges rather than implying that solvers are guaranteed to find the NE. This clarification would prevent confusion among readers not familiar with the literature, especially since multiple NE solvers are discussed while claiming guarantees of finding local optima.

- ***Price of Anarchy Discussion***: The discussion of the price of anarchy briefly addresses the motivation for the problem formulation but is not sufficiently convincing. Providing more details and insights specific to protein design tasks could improve the presentation and strengthen the argument.

p.s. Due to my limited domain expertise, I am not confident in assessing the novelty of the problem formulation in this specific application.

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
4

### Summary
This paper studies how to solve the combinatorial Bayesian optimization problem, which has many important potential applications like protein design. The key idea of this work is introducing the Nash equilibrium to Bayesian optimization, where a game is carefully designed for domain variables to play and the decision making is driven by equilibrium finding algorithms. It’s good to see substantial experiments in protein design in the end.

### Strengths
1.	Combinatorial Bayesian optimization (CBO) is a very important subfield in Bayesian optimization. While Bayesian optimization has been successfully applied to many areas, studying CBO helps us solve even more practical application problems, like protein design.
2.	Sample complexity guarantees are provided to show the algorithm’s ability to achieve approximate Nash equilibrium.
3.	Experiments on protein design are comprehensive and ablation studies are provided.

### Weaknesses
1.	To be honest, as a ML researcher, I have limited background in Nash equilibrium and I think it could be beneficial for this paper to provide more information on introducing Nash equilibrium since this is an ICLR submission. Although locally optimal, why and how does Nah equilibrium help in CBO setting? Could you provide a brief comparison between the local optimality of Nash equilibria and global optimality in the context of CBO. Can we design some globally optimal CBO algorithms or are the authors aware of such algorithms? Also, it might be hard to theoretically investigate the performance difference between GameOPT and the global optimal solution, it is feasible to investigate it in experiments where a small finite decision space is used. That would greatly provide valuable insights into the method's effectiveness.
2.	I have concerns on the computational efficiency of Step 5 of Algorithm 1. Because the GP is assumed on function f which is now defined on the combinatorial space, how do you find the top B equilibria according to UCB? Could you provide more details on how to implement this step efficiently, discuss the computational complexity of this step compared to the overall algorithm, and explain any approximations or heuristics that may be used if an exact solution is computationally infeasible?

### Questions
1.	Does this algorithm work without assumption $|\mathcal{X}^{(i)}|=d$? It means that in this case the numbers of possible decision variables are different.
2.	What is the v function in Algorithm 2? Is that the r function defined in Definition 3.1?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper studied the combinatorial Bayesian optimization in the discrete search space. Based on the theory of cooperative games and upper confidence bound of Gaussian processes (GPs), a new acquisition function that seeks to find the local equilibria of players was proposed. Based on batch and parallel computation, the proposed method achieved better scalability. The effectiveness and competitiveness were demonstrated in the application of computational protein design.

### Strengths
1. The discrete black-box optimization problems are important, and the proposed game-theoretical solution seems novel.
2. The protein design is vital in drug discovery and healthcare.
3. The presentation is clear and the idea is easy-to-follow.

### Weaknesses
1. There is no mechanism to avoid or mitigate stucking in local optimality. At the same time, as a Bayesian optimization method, the exploration-exploitation balance is not considered. As a preliminary solution, random restarts can be introduced into the search process, similar to what the trust-region Bayesian optimization algorithm does [1], to ensure exploration and global search ability. 
2. As local optima, the regret bound is not insightful enough to show the superiority. Currently, the regret is similar to what the original GP-UCB is, but only local optima are guarenteed. While the GP-UCB ensures global search and convergence. In my opinion, assuming convexity in the local region containing equilibria may help improve the theoretical results [2].
3. The testing benchmark problems are not diverse enough. Some well-known synthetic problems are required for fair comparison, espectially that employed in the state-of-the-art work.
4. The influence of hyper-parameters, especially the batch size B, is not clear. The baseline algorithms, especially the GP-UCB, are not tailored for batch optimization. It is recommended to consider smaller B, such as B=1, first. 
5. The literature review is insufficient. More baseline algorithms in combinatorial Bayesian optimization and general optimizers should be considered.

### Questions
1. Is there any consideration of balance of exploration and exploitation? How is the data-efficiency guaranteed?
2. What is the influence of batch size B? In what case may the algorithm perform worse?
3. Why not compared baselines using tree-based surrogate models. As far as I know, the tree model is a suitable choice for protein design.
4. How to prove that solving equation (2) is more tractable than solving other acquisition functions?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper tackles scalability challenges in combinatorial black-box optimization tasks, specifically when each dimension contains the same number of discrete points. While this assumption is not universally applicable in combinatorial Bayesian optimization, it is relevant in specific domains, such as protein engineering. The authors introduce GameOpt, a novel approach that leverages the uniform structure of the discrete search space. By reframing the combinatorial optimization problem as an $n$-player cooperative game, the method aims to identify an $\epsilon$-Nash equilibrium at each iteration. This transformation enables the application of scalable solvers and polynomial-time equilibrium-finding techniques from game theory, offering a computationally efficient strategy for optimizing the acquisition function, particularly GP-UCB.

### Strengths
- Large-scale combinatorial optimization is an important challenge, though Bayesian optimization (BO) may not be the most typical approach for tackling it.
- While theoretical analysis is provided for the convergence rate to an $\epsilon$-Nash equilibrium. However, it does not necessarily equate to finding the global optimum of the objective function, and the results are not significantly different from known results for existing game-theoretic BO literature.

### Weaknesses
 - **Clarity**
The weakest part of this paper is definitely the clarity, particularly in math. There are so many uncommon, unexplained, and undefined symbols, that make me frustrated. Detailed below:

**Problem Statement**.  What exactly is $x$? I initially understood it as a $d \times n$-dimensional variable. However, in Line 107, the statement "f(x) corresponds to --- the amino acid sequence $x$, and each $x$ can take $20^n$". I've lost. Is $x$ meant to be a $d$-dimensional variable or a  $d \times n$-dimensional variable? I also can’t interpret the meaning of "each $x$ can take $20^n$". Shouldn't $d = 20$ in this case? Additionally, the definition of the fitness function $f(x)$ is unclear. Is $f(x)$ defined for each discrete variable, or is it applied to the entire variable set? For example, if $x$ is assumed to be $d$-dimensional, does our objective function take the form $\prod_{i=1}^n f(x^{(i)})$? Or is $x$ actually $d \times n$-dimensional, and thus $f(x)$ refers to something else? I’ll proceed under the assumption that $x$ is $d \times n$-dimensional.

**Section 3**. I understand the reward $r^{(i)}$ here is the UCB defined for $x$ as a $d \times n$-dimensional input, and each player $i$ corresponds to one of the discrete variables. However, since UCB is defined on the entire $d \times n$-dimensional space, how can we apply UCB as $r^{(i)}$ then? How do you select the other $n-1$ variables? Or does $r^{(i)}: \mathcal{X} \rightarrow \mathbb{R}$ imply that each player takes a $d \times n$-dimensional input and $r^{(i)}$ = UCB for all $i$? If that is the case, and all players share the same utility function, why do equilibria arise? Wouldn't this reduce to the same optimal points for all players? Additionally, in Definition 3.1, $r^{(i)}$ takes two arguments, but this is supposed to be UCB. Why does UCB take two arguments? What is arg eq? What exactly does Eq (2) represent? I'm also confused by the explanation on Lines 172-173: "Intuitively, equilibria are computed by breaking down the complex decision space into individual decision sets." Could you precisely explain this process before jumping into the intuition? How is finding a Nash equilibrium equivalent to maximizing UCB? What is the payoff $v$ in Algorithms 2 and 3? I've lost again. 

I’ll stop pointing out specific issues here, but I want to note that the same level of confusion persists throughout the remaining sections (although the introduction was quite smooth).

- **Lack of Critical Guarantee**
Is finding a Nash equilibrium mathematically equivalent to maximizing the objective function $f$? If I understand correctly, this process is more akin to constructing a Pareto frontier, which contains the global maximum, making it more aligned with finding the set of local maxima. How, then, does this algorithm guarantee global convergence? If the goal of this work is local optimization or a heuristic approach, this should be clearly stated in the title or assumptions. Approximations can be valuable, but only if they provide some guarantee that they can recover the original problem under some conditions. Existing work, such as [1], provides such guarantees. I am not surprised that a local optimization algorithm finds local optima (as this work does) faster than a global optimizer (like [1]) in certain experiments, as they target different objectives. Even with these results, I wouldn’t choose this method for global optimization. When the function query is highly expensive, the computational overhead of the acquisition function becomes comparable. Moreover, [1] is not exactly state-of-the-art as it dates to 2022. There are likely more recent studies, such as [2], though performing a literature search is not my role here.
- **Limited Evaluation to Assess Practicality**
Heuristic approaches are completely acceptable if they prove useful in real-world applications. However, in that case, we expect the algorithm to be genuinely practical and perform best among existing heuristics. In the context of protein optimization, chemists would most likely start with deep learning-based approaches, especially diffusion-based methods, which are already well-established. There is a plethora of scalable and sample-efficient work in this area, such as [3, 4]. These methods seem like a more natural choice than using deep learning embeddings as features, as done in this work. Even with embeddings, the GP has no prior data on the objective function, meaning BO must start without a pretrained dataset. Alternatively, why not reduce the dimensionality of the embedding features to make them more tractable for the naïve GP-UCB? This could be achieved by adding just one additional layer to the transformer. In doing so, standard GP-UCB would likely perform just fine like popular latent BO doing. Since this paper does not compare its method against these popular alternatives or simpler alternatives, I cannot properly evaluate whether it represents a good heuristic. What I gather from this work is that it performs better than outdated methods on the limited tasks provided, but that alone does not demonstrate its superiority or practicality compared to modern approaches.
- **Limited Novelty**
The equation on line 295 appears nearly identical to the existing optimistic game-theoretic approach presented in [5], but it is not cited. Additionally, the idea of treating each discrete variable as a player is not particularly novel. For instance, Shapley value GP [6] and additive kernels [7] can be seen as variants of this concept (although they treat dimensions as players). While the specific combination of game theory, combinatorial optimization, and Bayesian optimization may be novel, it ultimately feels like a straightforward combination of existing approaches.
- **Missing Limitation**
I understand that this method leverages the problem structure where each dimension contains the same number of discrete variables, $n$. However, in typical combinatorial Bayesian Optimization, the goal is hyperparameter optimization, where each dimension may have a different number of categorical values, and the space can sometimes be a mixture of continuous and discrete variables. This method is not applicable to such cases. In mixed-variable scenarios, the existence of a Nash equilibrium cannot be guaranteed.


### Questions
See the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2
