# Towards General Certified Robustness of Combinatorial Optimization Solvers

- Decision: Reject
- Avg Score: 3.75
- Scores: 5, 1, 3, 6

## Abstract
Combinatorial optimization (CO), driven by algorithmic advancements, now spans applications like network design and bioinformatics, crucial for optimizing complex systems and tackling NP-hard problems efficiently across various industries.
Nonetheless, the study for robustness, especially certified robustness in the CO domain which ensures optimization consistency among different data distributions, persists as an unexplored domain.
In this study, we explore the certified robustness and robustness enhancement strategy for CO solvers.
Experiments across datasets and solvers illustrate that our proposed certification definition can achieve a solid robustness guarantee and the enhancement method significantly amplifies the model’s immunity to perturbations in practice.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents an approach to addressing robustness in combinatorial optimization solvers by introducing a randomized smoothing framework for certified robustness. The theoretical results are supported by experiments on DAG scheduling and  TSP tasks and lend credibility to the proposed method. However, several assumptions in the robustness definitions, such as the strict reliance on CDF stability and the Wasserstein distance as robustness metrics, could limit the model's applicability to broader CO contexts.

### Strengths
- Novelty in the exploration of certified robustness within CO solvers. 
- Adaptation of randomized smoothing to combinatorial problems (this is nice as CO have constraints and non-categorical outputs). 
- Theoretically grounded method that could apply to several optimization tasks in dynamic environments. 
- The enhancement method for leveraging "easy instances" shows a promising direction for robustness without retraining.

### Weaknesses
- The paper’s approach primarily targets DAG scheduling and TSP tasks, but it is unclear how generalizable the method is to structurally richer CO problems. 
- The use of Wasserstein distance as the primary robustness metric may be too restrictive, especially in CO tasks where cost functions or constraints may differ significantly. 
- The empirical robustness results, while promising, rely on specific perturbation strategies (e.g., random search, simulated annealing). A more comprehensive assessment involving adaptive or adversarial perturbation techniques would provide a more robust evaluation here.
- Some sections of the theoretical framework (particularly the robustness guarantees) are challenging to follow. Consider to at least paraphrase the results in English or adding some illustrative examples.

### Questions
1. Does the model handle adversarial perturbations, or is it only applicable to random perturbations? 

2. How does the proposed enhancement method scale with increased constraint complexity in CO tasks e.g., as the constraint structures and dependencies intensify? 

3. Could the robustness guarantees extend to CO problems with multi-objective cost functions?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper seeks to assess the robustness of combinatorial optimization solvers.
While this is a valid direction, the paper fails to articulate an appropriate theoretical framework, 
and exhibits several limitations in its presentation, methodology, and experiments.

### Strengths
There has been a lot of interest recently in providing formal guarantees on the performance of trained ML models.
Investigating such a direction in the context of combinatorial optimization is relevant, however the paper suffers from multiple limitations, outlined below.

### Weaknesses
It is hard to understand the logic behind the paper, and several notations / symbols / problems are used without being clearly defined.
In addition to these limitations, the paper lacks a principled methodological framework.
Finally, numerical experiments are incompletely stated and only small instances are considered.

## Overall paper

* How robustness of classifier relevant to robustness of combinatorial optimization setting?
* The paper discusses the robustness of combinatorial solvers, but makes no mention of the (vast) literature on robust optimization
* Throughout the paper, multiple concepts/notations are ill-defined or not defined at all. 
	This includes, for instance: 
	* the "strictness" of a constraint
	* the underlying randomness & probability distribution considered in Eq (4)
	* variable $v$ in Eq (5)
	* Matrix $H_{b}$ used throughout the paper
	* $g_{\theta}$ in Eq. (6)

## Methodology

The paper suffers from several fundamental methodological limitations, the first of which is the absence of a clear, relevant definition of "robustness" for combinatorial optimization solvers.
This severe limitation makes it impossible to follow the rest of the paper, and to evaluate the paper's contribution and relevance to the field.

* The paper lacks a principled definition of robustness for CO solvers.
	Authors are invited to review the paper [_Compact Optimality Verification for Optimization Proxies_](https://proceedings.mlr.press/v235/chen24bj.html) and the references therein for relevant literature on performance verification for ML models that output solutions to optimization problems.
* The paper states that "hard" instances have higher optimal value, which is not correct.
	For instance, in TSP, multiplying all the distances by $\gamma > 1$ increases the optimal value by the same factor $\gamma$, but the optimization problem is equivalent.
* The function CDF F(r) in Eq. (4) seems to be defined w.r.t a probability distribution over Q... which is never defined.
* In Theorem 4.1, the right-hand-side integral (used as upper bound on a Wasserstein distance) may be infinite.
	Note that this term is the integral of a CDF function, which makes it likely that it is not finite.

## Experiments

The numerical experiments are hard to understand.
The paper does not state the mathematical formulation of either problem, nor how instances are generated.
This makes it impossible to evaluate the soundedness of the experiments and the validity of the results.

TSP instances
* TSP instances with 100 cities are very small compared to state-of-the-art.
	Instances of that size can be solved exactly to global optimality on a phone using the free Concorde app.
	The authors are encouraged to consider (much larger) instances from the TSPLib, aiming for at least tens of thousands of cities for hard-to-solve instances.
* It is extremely hard to understand how TSP instances are generated, and what the parameters introduced in the paper translate to in the context of TSP instances.

### Questions
* The paper should explain how it differs from the (large) literature on robust optimization
* Please provide a valid, self-contained definition of robustness for combinatorial optimization solvers.
	The change in objective value from instance to instance is not an appropriate metric.
* Numerical experiments should include a clear mathematical formulation of the problem at hand,
	as well as a complete description of the data distribution used to generate instances.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper describes an approach to certifying the robustness of parametrizable combinatorial optimization solvers with respect to certain kinds of perturbations of the solver's input. The perturbations are divided into two categories: binary, where a constraint is add/deleted, and tightness, where the constraint's bound is changed. 

The paper states a definition of robustness certification for combinatorial optimization solvers, quantifying robustness in terms of the closeness of input instances. A randomized smoothing technique is used to robustify solvers. The output of these robust solvers is guaranteed to be close for any inputs that are close. 

The paper presents a "robustness enhancement method" that works by searching for easy instances that are similar to the given instance. 

Finally, experiments are performed demonstrating aspects of the framework.

### Strengths
While previous works have focused on the empirical evaluation of robustness for combinatorial optimization solvers, this paper provides a theoretically sound robustness certification guarantee, which is helpful when, for example, a priori guarantees are required. 

The paper also describes a way of using this guarantee to enhance the robustness of solvers using a randomized smoothing technique. This is arguable the main contribution of the paper, as it gives a way of producing useable, provably robust solvers. 

The paper is well-placed within the existing literature: randomized smoothing applied to make robustness guarantees for combinatorial optimization solvers.

### Weaknesses
- The definition of "certified radius" does not look like a definition to me. It is just an inequality. Is the certified radius the largest $\delta$ that satisfies this inequality? 

- Line 186. "finding the optimal solution $x$ for a given problem instance $Q$ is often NP-hard". As stated, this is not correct. A solver that completely ignores its input and just always outputs $x$ returns the optimal solution for $Q$ in constant time, but of course this does not mean $P = NP$... The problem that is NP-hard is to find the optimal solution *for any* possible input. 

- Line 187: "indicating that no polynomial-time algorithm exists to solve it." Assuming $P \not= NP$... 

- Equation 4 defines the CDF for the cost $c(f_\theta(Q), Q)$. Where is the randomness in the cost coming from? I would have thought it was over the choice of inputs $Q$, but in Theorem 4.1 the input $Q$ is taken as given and the cost still has a CDF? The source of the randomness needs to be made more clear. 

- Equation 5: Should $v$ be $u$?

- The matrix $H_b$. I wonder if the authors could describe more generally how this matrix is built from the set of constraints. It is stated that "1 signifies the presence of a constraint", since this set is inherently linear. In the DAG example, the constraints are between two jobs, so a matrix is implied, but I cannot see how this would be so in general. 

- Equation 6: What part of this is the definition? It seems like $G_{H_b}$ is being defined in terms of $g_\theta$ and/or $F_{H_b \oplus z}$, but what are these? 

- Algorithm 1 and subsequent: $F_{H_b + z^{(j)}}$ should be an $\oplus$? 

- Algorithm 1 is called "Randomized Smoothing..." but it outputs a number that is a distance. What has been smoothed? Shouldn't it output a smoothed/robust solver? 

- Robustness Enhancement Method (Algorithm 2 and Section 4.2): Why are we trying to find an easy instance? How does this enhance the robustness of the solver? This seems important and should be explained better. 

- Theorem 4.1: Is $G_{H_b}$ the smoothed CDF using a vector $z$ of Bernoulli($\beta$) RVs? Why are we interested in bounding the distance between this smoothed distribution and the perturbed distribution $G_{H_b \oplus \delta_b}$? Don't we want to bound the distance with the actual cost distribution $F$? The preamble defines the cost CDF $F$, but then does not use it, so I suspect I am misunderstanding something...

- Both Theorem 4.1 and 4.2 define $F(r)$, but then never use it. Is this intentional? 

- Why are absolute values taken of CDFs? Shouldn't they be non-negative anyway? 

- Experimental details are pushed to the Appendix, in particular results for the enhancement method for certified robustness. 

- In general, I am not sure I would describe the experiments as "Extensive" (line 105)...

- The experiments vary $m$ and $\beta$. If I were to use this robustness certification method in practice, how would I choose values for these parameters? 

- Figure 1: It is not clear to me what the denominator of the ratios is. What is SFT (line 431) and why is this the right normalizing baseline?

Some minor issues not affecting my recommendation:

- In text citation style is used where parenthesis citation style should be used. E.g., "Previous studies Varma & Yoshida (2021); Geisler et al. (2021); Lu et al. (2023) indicate..." -> "Previous studies (Varma & Yoshida, 2021; Geisler et al., 2021; Lu et al., 2023) indicate..."

- Line 205 missing word? "two distinct perturbation types that can..."

- Equation 5: I would use a naming convention that makes the connection between $\mu$ and $C_1$, and between $\nu$ and $C_2$, more clear.

- Figure 1, y-axis label: radio -> ratio

### Questions
See Weaknesses above.

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
3

### Summary
This paper studies the robustness of combinatorial optimization (CO) solvers. As claimed by the authors, previous work has not explored the certified robustness of CO solvers. In this work, they propose a definition of robustness certification for CO solvers, along with a method to improve both certified and empirical robustness. The authors conduct experiments to validate the effectiveness of their certification approach and enhancement method. They claim that their proposed framework addresses gaps in the existing literature regarding the certified robustness of combinatorial optimization solvers.

### Strengths
1. The paper is generally well-written, with clear explanations.

2. This paper focus on framework studying, which is a foundational work in the robustness of combinatorial optimization solvers.

3. Experiments are conducted on the representative problems.

### Weaknesses
1. In Section 5.1, the solver selection criteria for the two representative problems are not consistent. The solver for DAG scheduling does not include SOTA solvers or learning methods.

2. In the work of ROCO, an evaluation was conducted on the MC problem. Why this problem was not selected in this paper?

### Questions
Please reply to my comments in "Weaknesses".

### Soundness
2

### Presentation
3

### Contribution
3
