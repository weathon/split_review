# MGDA Converges under Generalized Smoothness, Provably

- Decision: Accept
- Scores: 8, 6, 5, 5

## Abstract
Multi-objective optimization (MOO) is receiving more attention in various fields such as multi-task learning. Recent works provide some effective algorithms with theoretical analysis but they are limited by the standard $L$-smooth or bounded-gradient assumptions, which typically do not hold for neural networks, such as Long short-term memory (LSTM) models and Transformers. In this paper, we study a more general and realistic class of generalized $\ell$-smooth loss functions, where $\ell$ is a general non-decreasing function of gradient norm. We revisit and analyze the fundamental multiple
gradient descent algorithm (MGDA) and its stochastic version with double sampling for solving the generalized $\ell$-smooth MOO problems,  which approximate the conflict-avoidant (CA) direction that maximizes the minimum improvement among objectives. We provide a comprehensive convergence analysis of these algorithms and show that they converge to an $\epsilon$-accurate Pareto stationary point with a guaranteed $\epsilon$-level average CA distance (i.e., the gap between the updating direction and the CA direction) over all iterations,  
where totally $\mathcal{O}(\epsilon^{-2})$ and $\mathcal{O}(\epsilon^{-4})$ samples are needed for deterministic and stochastic settings, respectively. 
We prove that they can also guarantee a tighter $\epsilon$-level CA distance in each iteration using more samples. Moreover, we analyze an efficient variant of MGDA named MGDA-FA using only $\mathcal{O}(1)$ time and space, while achieving the same performance guarantee as MGDA.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors analyze the problem of multi objective optimization (MOO), 
$$\begin{align*}
F^\star = \min_{x\in \mathbb{R}^d} F(x) = (f_1(x), f_2(x), \ldots f_K(x))
\end{align*}
$$
where each $f_i:\mathbb{R}^m \to \mathbb{R}$ when each $f_i$ has generalized $\ell$-smoothness. Generalized $\ell$-smoothness implies that $\|\nabla^2 f_i(x)\| \leq \ell(\|\nabla f_i(x)\|), \forall x$ for a continuous non-decreasing positive function $\ell$. This subsumes $(L_0, L_1)$-smoothness, where $\ell(a) = L_0 + L_1 a$, (Zhang et al 2019) and standard $L$-smoothness, where $\ell(a) = L$. Further,  NNs do not satisfy stronger notions of $L$-smoothness but satisfy generalized smoothness. 

The goal of MOO is to obtain $\epsilon$-accurate Pareto stationary point, defined as $\min_{w\in \mathcal{W}} \|\nabla F(x) w\|^2 \leq \epsilon^2$. This is referred to as $\epsilon$-CA distance (Conflict avoidant).

First, the authors analyze the existing MGDA algorithm in Algorithm 1 (Desideri 2012) and its stochastic variant in Algorithm 3, to obtain $\epsilon$-CA distance on average. The required sample complexity for these cases is $\mathcal{O}((\alpha\epsilon^2)^{-1}, (\beta\epsilon^2)^{-1})$(Theorem 1)  and $\mathcal{O}((\alpha \epsilon^2)^{-1} + \epsilon^{-4})$ (Theorem 2) respectively, which matches the sample complexity for single objective optimization under $L$-smoothness. Here, $\alpha$ and $\beta$ are step sizes to update  $w$ and $x$ in their algorithms.

Second, the authors consider a stronger metric, the per-iteration $\epsilon$-level CA distance, defined as $\|\nabla F(x_t)w_t - \nabla F(x_t) w_t^\star\| \leq O(\epsilon)$, where $x_t, w_t$ are iterates of the algorithm, and $w_t^\star \in \arg\min_{w\in \mathcal{W}} \|\nabla F(x_t) w\|^2$. To achieve this metric, the authors propose using a  warm-start for $w$ in deterministic setting (Algorithm 1), and warmstart with increasing batch size for stochastic setting (Algorithm 3), yielding sample complexities of $\mathcal{O}(\epsilon^{-11})$ (Theorem 3) and $\mathcal{O}(\epsilon^{-17})$ (Theorem 6) respectively.  Further, the authors propose a zeroth-order method modificiation to warm-start deterministic MGDA in Algorithm 4, which uses only $O(1)$ space and time and achieves per-iteration $\epsilon$-level CA distance with same sample complexity $\mathcal{O}(\epsilon^{-11})$.

A key advantage of their analysis is removing the bounded gradient assumption required by all existing works and they require sufficient effort to show such a bound exists implicitly for their algorithms.


Finally, on two multi-task learning datasets (Cityscapes and NYU-v2), their warm start method obtains best average performance across all tasks.


**References** --
- (Zhang et al 2019) Why gradient clipping accelerates training: A theoretical justification for adaptivity. Arxiv.
- (Desideri 2012) Multiple-gradient descent algorithm (mgda) for multiobjective optimization. CRM.

### Strengths
- **Presentation**: The paper is easy to follow, even for readers without expertise in MOO. The MOO problem under generalized smoothness, the MGDA algorithm, and the warm-start procedure are well-motivated. Further, the proof sketch also provides a good overview of key ideas, atleast for average CA distance.


- **Novel algorithms**: A warm-start procedure appears in (Xiao et al 2023), however, it requires running two-loops, one of warm start of $w$ and other for $x$. In contrast, the proposed warm-start algorithm is run only once at initialization for $w$, and then the simple MGDA algorithm takes over. Even with this "weaker" warm-start, the authors can achieve stronger per-iteration $\epsilon$-CA distance. Algorithm 4, MGDA-FA, seems novel, and utilizes zeroth-order optimization intelligently, without worsening theoretical guarantees in the deterministic case.


- **Weak assumptions**: All existing works require $L$-smoothness and bounded gradients, while this paper requires only generalized smoothness. For their proofs, they show that gradients are indeed bounded by initial suboptimality, $\max_{i\in [K]} (f_i(x_0) - f_i^\star)$ for MGDA updates in the deterministic case. In the stochastic case, their proof is more complicated, wherein they take  a union bound over all iterations until a stopping time to show that gradient noise is also bounded.


- **Best sample complexity**: Even under weaker conditions, the obtained sample complexities for average CA distance, $\mathcal{O}(\epsilon^{-2})$ and $\mathcal{O}(\epsilon^{-4})$ for deterministic and stochastic cases respectively, match the lower bounds for single-objective optimization under $L$-smoothness. For iteration level CA distance, it seems that the best sample complexity of existing methods with stronger assumptions is $\mathcal{O}(\epsilon^{-12})$ while their analysis obtains $\mathcal{O}(\epsilon^{-17})$.

### Weaknesses
- **Theory**:
    - **Definition of $\mathcal{W}$:** The authors have not defined the set $\mathcal{W}$, however across the proof(Line 809, Eq 11), they use $\max_{w\in \mathcal{W}}\|w\| \leq 1$. It seems to be the unit sphere in $K$ dimensions. 
    - **Choice of step size does not work in Theorem 2:** The parameters $\alpha,\beta,\rho = \mathcal{O}(\epsilon^2)$ do not work out for Theorem 2 as each of $\alpha, \beta$ and $\rho$ depend on other two. Consider $\rho \leq \frac{1}{\sqrt{\alpha T}}$ in Theorem 2, which for $T = \epsilon^{-4}$ and $\alpha  = \epsilon^{2}$ implies, $\rho \leq \epsilon$. For $\epsilon << 1$, $\rho=\epsilon^2$ does not satisfy this condition. Ideally, the authors should provide the condition for parameters in a sequential manner, for instance, $\rho$ depends on $\beta$ and $\alpha$, $\beta$ depends on $\alpha$ not $\rho$ and $\alpha$ doesn't depend on either $\beta$ or $\rho$. This would ensure that such inconsistent parameter values do not arise. Also, I am no longer sure that $T = \mathcal{O}(\epsilon^{-4})$ can be obtained for choice of $\alpha,\beta,\rho$ satisfying all constraints in Theorem 2. 
    - **Value of $M$:**  For the deterministic case (Theorems 1, 3, 4 and 5), the value of step sizes depend on $M$ defined in Line 357, which is a function of $\ell$ and initial function suboptimality. Therefore, while the bounds in these theorems scale well with  $\epsilon$, they might not do so with $M$. If the scaling with $M$ in these theorems matches that of single-objective generalized $\ell$-smooth optimization from (Li et al 2024), or if is small under certain conditions on $\ell$, then it should not be an issue.
    - **Dependence on high probability error $\delta$ in stochastic variants (Theorem 2 and 6):** The authors do not provide the dependence on the high probability error $\delta$ in Theorems 2 and 6. For high probability guarantees, we would want to know if we can make $\delta$ extremely small, for instance $\mathcal{O}(\epsilon)$, or if it works only for a constant $\delta$. From Theorem 8, it seems that a constant $\delta \in (0,\frac{1}{2})$ might work, but the authors should provide more details on this. The union bound  over all iterations should force $\delta$ to not be very small.
    
    
 
- **Poor empirical Performance of MGDA-FA**: While MGDA-FA achieves the same performance as warm-start MGDA theoretically(Theorems 3 and 4), it performs much worse in experiments (Table 4). Its performance is better than only $2$ of the $8$ baselines in Table 3, while warm-start MGDA outperforms all $8$ baselines. The authors do not discuss possible causes for this. Even though MGDA-FA is fast in practice, as its error is very large, its usefulness is limited.




- **Typos**: $f_i^\star$ in the definition of $\Delta$ in Line 357 and "optional stopping theorem" in Line 407-408.

### Questions
- **References for Optimal rates for deterministic variants of per-iteration CA distance** : Can the authors provide any references for deterministic iteration-level CA distance to compare Theorems 3 and 4. Further, can the authors compare the performance of their warm-start procedure to existing baselines? Do warm-start procedures achieve optimal sample complexity for these cases? It might be helpful to include the sample complexity results in Table 1 for a quick comparison to baselines.

- **Independent samples for each $f_i$ for stochastic variants**: For 
stochastic variants (Line 387) at each iteration $t$, $F(x_t;s_{t,i})$ requires a different sample $s_{t,i,j}$ to evaluate $f_j$ for $j\in [K]$. Is this necessary for the analysis? Does using the same sample for all $f_j$ change the analysis, as in practice, one might take a single minibatch to evaluate all $f_j$ at each iteration. Further, in Eq 16 and 17, using the same sample can remove the terms of $K$ from the union bound while still obtaining similar results.

- **Stochastic MGDA-FA** : If there is a bound the variance of $F(x;s)$ for instance $\mathbb{E}[\|F(x;s) - F(x)\|^2]\leq \sigma_F^2, \forall x$ or for each function $f_j(x;s)$, then would it be possible to analyze a stochastic variant of MGDA-FA by combining the analysis of the deterministic MGDA-FA and stochastic MGDA? Are there any reasons why the authors believe this shouldn't be possible or straightforward?

- **Warm-start procedure for general bi-level optimization**: MOO is bi-level optimization problem, where the inner optimization problem solves for best $w$ and the outer optimization solves for $x$. The warm-start procedure here implies that for single loop solutions to bilevel optimization, the inner problem is already very accurate, $\mathcal{O}(\epsilon)$ to be precise. This makes solving the bi-level optimization easier, as the inner problem is already almost solved.
Can this technique be applied to ohter bi-level optimization problems, where a single warm-start conveniently solves the inner problem accurately? Or is this an artifact of the MOO problem's simple structure?

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
2

### Summary
This paper studies the multi-objective optimization (MOO) problem under generalized $ell$-smoothness, where $\ell$ is a general non-decreasing function of gradient norm. The authors provide the first convergence analysis of multiple gradient descent algorithm (MGDA) (and its variant with fast approximation) under this setting, in terms of $\epsilon$-Pareto stationarity and $\epsilon$-level conflict-avoidant (CA) distance. The resulting complexities with respect to $\epsilon$-Pareto stationarity and $\epsilon$-level average CA distance match the best known results.

### Strengths
- The analysis of MGDA under generalized smoothness is new. Their analysis further relax the assumptions such as bounded function values or bounded gradients assumed in prior work. 
- The authors use a general notion of generalized smoothness, i.e., in terms of a non-decreasing function $\ell$ instead of the original one with $ell(a) = L_0 + L_1 a$.
- The authors further study a variant of MGDA, which approximates the gradient in each iteration to save memory and time.

### Weaknesses
- The notation of this paper is a bit unclear. In multiple places, the authors introduce something before they define the notation, so the write-up should be refined. For example, the authors should define $\mathcal{W}$ in Definition 3.
- The preliminaries on generalized smoothness from Section 2.1 is redundant, as those are not proposed by this work and not the main contribution here. 
- All the complexity results of this paper are only stated in terms of $\epsilon$. A more clear statements with dependencies on other problem parameters would be better.

### Questions
- What is the meaning of minimizing a vector as in Eq. (1)? I suggest that the authors may make it clearer, in the context of multi-objectives.
- Could the authors elaborate how they computed the local smoothness for Figure 1?
- What is $f_*$ in the definition of $\Delta$ in Line 357?
- Take Theorem 1 as an example. Could the authors provide a more detailed discussion on the constants $c$, $F$ and $M$, like how tight they can be in some special case? I found the current convergence result is hard to parse.
- Would generalized smoothness bring any benefits in practice, like providing guidance on how to choose the step sizes?

### Soundness
3

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
2

### Summary
This paper offers a rigorous convergence analysis for both deterministic and stochastic variants of the Multiple Gradient Descent Algorithm (MGDA) under a generalized $\ell$-smoothness assumption. The authors demonstrate that these methods converge to an $\epsilon$-accurate Pareto stationary point while maintaining an $\epsilon$-level average conflict-avoidant (CA) distance over all iterations. The sample complexity is shown to be $\mathcal{O}(\epsilon^{-2})$ in the deterministic setting and $\mathcal{O}(\epsilon^{-4})$ in the stochastic setting. Additionally, the authors introduce a warm start strategy to enable more precise control over iteration-wise CA distance. They also analyze MGDA-FA, a variant that reduces the computational complexity to $\mathcal{O}(1)$ in both time and space, making it notably efficient.

### Strengths
1. The theoretical analysis is comprehensive and robust.
2. The paper is clearly written and well-organized, making the concepts easy to follow.

### Weaknesses
1. Assumption 2, which posits that $\phi(a) = \frac{a^2}{2\ell(2a)}$ is monotonically increasing, restricts $\ell(a) \leq \mathcal{O}(a^2)$. This places a strict limitation on the class of generalized $\ell$-smooth functions considered.
2. The paper's novelty is somewhat limited. From an algorithmic standpoint, MGDA was introduced several years ago, and the fast approximation presented here constitutes a relatively minor modification.
3. The novelty of the analytical techniques is also limited, as the approach used closely resembles that of [1].
4. The experimental results would benefit from the addition of confidence intervals to clarify statistical significance, particularly given the small differences in performance observed.
5. In the main theorems, the authors use big-O notation without specifying constants. Providing explicit constants would enhance clarity and interpretability.

**Reference**:

[1] Li, Haochuan, et al. "Convex and non-convex optimization under generalized smoothness." Advances in Neural Information Processing Systems 36 (2024).

### Questions
1. In lines 389 and 393, why are $i \in [3]$ and $j \in [3]$ specified? What is the rationale behind selecting only the first three sample collections?
2. In Section 5.2, the analysis involves mini-batch algorithms, yet the effect of batch size on the results is not discussed. How would adjusting the batch size impact the findings?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates a broader class of generalized $\ell$-smooth loss functions, where $\ell$ is a non-decreasing function of the gradient norm. We analyze the multiple gradient descent algorithm (MGDA) and its stochastic variant for addressing generalized ℓ\ellℓ-smooth multi-objective optimization (MOO) problems. Its comprehensive convergence analysis demonstrates that these algorithms converge to an $\epsilon$-accurate Pareto stationary point, ensuring guaranteed average conflict-avoidant distances.

### Strengths
1.Writing: This work is presented with good writing style, where the summarized problems with detailed explanations make it easy for readers to understand the problem addressed in this article. 

2.Novelty: The paper investigates a more general and realistic class of generalized $\ell$-smooth loss functions, which has been rarely considered in previous work. Additionally, a warm start strategy is proposed in the algorithm design to initialize the parameter $\omega$ for enhanced performance.

3.Experiments: Several scenarios and recent baselines are considered, implying improvements in accuracy and robustness under various distributional shifts.

### Weaknesses
1.Unreliable theoretical analysis: The theoretical work in this paper appears to lack reliability. A simple review of the proofs in the appendix reveals that the proof of Corollary 1 is entirely incorrect. 

The inequality
$$
\left\|\nabla F\left(x_t\right) w_t-\nabla F\left(x_t\right) w_t^*\right\|^2 \leq\left\|\nabla F\left(x_t\right) w_t\right\|^2-\left\|\nabla F\left(x_t\right) w_t^*\right\|^2,
$$ 
does not hold.

2.Originality of the algorithm. Could you clarify the differences between the algorithm presented in this paper and MGDA [1]?  Could you elaborate on how the algorithm mentioned in this paper improves the performance of MGDA?

[1]Jean-Antoine Désidéri. Multiple-gradient descent algorithm (mgda) for multiobjective optimization.  Comptes Rendus Mathematique, 350(5-6):313–318, 2012.

3.Warm start. Can the warm start strategy be applied to other multi-objective optimization algorithms? Would incorporating this strategy significantly improve algorithm performance?

4.Computational complexity. 
The paper may not provide a comprehensive assessment of the computational efficiency and practicality of the proposed method in real-world applications. Like the computational complexity analysis or empirical time/memory cost.

### Questions
For specific questions, please refer to the "Weakness" section.
I would be willing to raise my score if these  questions concerned are well addressed.

### Soundness
2

### Presentation
3

### Contribution
2
