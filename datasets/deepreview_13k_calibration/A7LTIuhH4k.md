# Approximating Multiple Robust Optimization Solutions in One Pass via Proximal Point Methods

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Robust optimization provides a principled and unified framework to model many problems in modern operations research and computer science applications, such as risk measures minimization and adversarially robust machine learning. To use a robust solution (e.g., to implement an investment portfolio or perform robust machine learning inference), the user has to \emph{a priori} decide the trade-off between efficiency (nominal performance) and robustness (worst-case performance) of the solution by choosing the uncertainty level hyperparameters.  In many applications, this amounts to solving the problem many times and comparing them, each from a different hyperparameter setting.  This makes robust optimization practically cumbersome or even intractable. We present a novel procedure based on the proximal point method (PPM) to efficiently approximate many Pareto efficient robust solutions at once. This effectively reduces the total compute requirement from $N \times T$ to $2 \times T$, where $N$ is the number of robust solutions to be generated, and $T$ is the time to obtain one robust solution. We prove this procedure can produce exact Pareto efficient robust solutions for a class of robust linear optimization problems. For more general problems, we prove that with high probability, our procedure gives a good approximation of the efficiency-robustness trade-off in random robust linear optimization instances. We conduct numerical experiments to demonstrate.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper studies robust optimization with an uncertainty set, and proposes a more efficient way for computing Pareto efficient robust solutions based on proximal point methods.

### Strengths
This paper proposes a novel way for solving robust optimization with an uncertainty set. The idea of applying Proximal point method for computing the Pareto efficient robust solutions seems to be a novel idea that has been explored before. 

Empirical results demonstrate the effectiveness of the proposed methods.

### Weaknesses
A limited setting: The algorithms and theoretical guarantees given by the authors seem to only work on a toy example with linear functions and ellipsoidal uncertainty set. The objective function (e.g., in (3)) has a very particular form, and it seems that the analysis is difficult to be generalized to other cases.

One of the main advantage mentioned by the authors is that the total computational cost is reduced from NT to 2T. I wonder can the authors provide more discussion on this point? To be more specific, which papers are we talking here (Line 054)?

I am not sure how to understand Theorem 1. The algorithm gives a series of x_k, which are PE in terms of  a series of special alpha (i.e., alpha(ω_k)). What are these alpha(ω_k)? how do we know this sequence is good enough? That is, how do we know these alpha covers enough possible alphas, and how does alpha(ω_k) varies with ω_k?

Line 239:  (alpha(ω_k)) is such that the equality holds. How do we know such an alpha exist? How do we compute it?

I have some doubts on how to implement the proposed methods. Specifically: Line 234: when computing x_R, \xi\in\Xi(\infty). So how exactly should we compute x_R? What is \mathcal{U} in Line 253 for the linear problem with ellipsoidal uncertainty set?

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper studies approximating the efficient-robust Pareto solutions through proximal point method. It contributes faster computation requirements compared to the literature.

### Strengths
**Originality:** 
- Their undertaking of efficient identification of Pareto front seems new.  
- The work is a novel combination of well-known techniques.

**Quality:**
- The methods used seem appropriate.
- This is a complete piece of work, with possible future improvements.
- The authors are careful and honest about evaluating both the strengths and weaknesses of their work.

**Clarity:**
- The submission is clearly written.
- It is well organized.

**Significance:**
- The result seems important from a computational efficiency perspective.
- Others (researchers or practitioners) are likely to use the ideas or build on them.
- It provides unique conclusions about existing approaches.

### Weaknesses
 **Originality:** 
- It is not exactly clear how this work differs from previous contributions or if the related work is adequately cited, since there is not substantial comparison.

**Quality:**
- A key point is that the submission has certain issues with technically sound, please see Questions. Similarly, some claims need more support.

**Clarity:**
- It occasionally fails to adequately inform the reader.

**Significance:**
- The difficultness of the task the submission addresses is hard to gauge, considering the rather simple approaches. The comparison with previous work is a bit lacking.
- Thus, it is also not easy to conclude if it advances the state of the art in a demonstrable way.

### Questions
**Questions:**
- Line 239: in Theorem 1, $\alpha(\omega_k)$ seems to depend on $x$. How does this work?
- Line 247: what are the two passes exactly?
- Line 299: in Proposition 3, again, the existence of such $\alpha(\omega_k)$ needs to be explained. Is the equality with respect to a specific choice of $x$?

**Major Suggestions:**
- Line 231: define $e$ from the simplex domain.
- Line 329: in Corollary 1, $m$ cannot be arbitrarily large, which makes the probability upper-bounded, so this is not exactly a high probability bound.

**Minor Suggestions:**
- Line 34: need cites in this first paragraph.
- Line 46: also need more cites in the second paragraph.
- Line 91: $E$ is not empty but only includes the zero vector.
- Line 173: explain the connection of this central path to the robust optimization problem earlier on.

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
2

### Summary
This paper presents a proximal point method based procedure to approximate many Pareto efficient robust solutions. This procedure reduces the computational requirement  by a multiplicity of the number of robust solutions to be generated. They go on to show that this procedure can produce exact Pareto efficient robust solutions for a class of optimization problems.

### Strengths
S1 - The paper is generally well written and well presented.

S2 - The technical claims in the paper are generally well explained.

S3 - Experiments are a plus.

S4 - The idea is interesting

### Weaknesses
W1 - The literature review is a bit lacking. The comparisons to previous art are inadequate.

W2 - The main novelty is ambiguous. 

W3 - The method seems to be limited in its generation of robust solutions where the radius of the uncertainty sets are not freely selectable.

### Questions
Q1 - Although the computational efficiency claim somewhat makes sense. I am not sure how this is equivalent to generating multiple robust solutions and comparing their results. While your proximal point method generates pareto efficient intermediate solutions, how many of them does it generate? Why is the new computational complexity $2\times T$ and does not include $N$ at all. 

Q2 - How comprehensive is the robust solutions generated by your proximal point based procedure?

Q3 - How to read figure 1 and 2, why are not one-to-one? Are these supposed to be the trajectories followed with the gradient steps?

### Soundness
3

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
4

### Summary
The paper proves that for robust LPs with uncertain objective functions under the simplex decision domain and ellipsoidal uncertainty sets, the proximal point trajectory are exactly Pareto efficient robust solutions. For robust LPs with a random polyhedron domain, the paper proves that with high probability, the performances of the Pareto efficient robust solutions are bounded by the performances of two proximal point trajectories. Numerical experiments on portfolio optimization and adversarially robust deep learning are provided.

### Strengths
The paper raises the interesting question of computing the efficient frontier that balances robustness and efficiency, and proposes a novel approach to finding this frontier. The paper provides an original proof that with high probability, the performances of the Pareto efficient robust solutions are bounded by the performances of two proximal point trajectories. The paper demonstrates clear structural organization. The visualizations are informative, and both the core ideas and theorems are presented with clarity.

### Weaknesses
The paper claims that the computational cost is reduced from N*T to 2*T. However, in each iteration of the proposed proximal point method for portfolio optimization, a quadratic optimization problem needs to be solved. Thus, the total computational cost is not reduced compared to the brute-force method of solving the problem for multiple alphas. The core argument for computational efficiency hinges on the claim that the proximal point method (PPM) provides a more efficient way to generate multiple robust solutions compared to solving individual robust optimization problems. However, for linear programs, each iteration of the PPM requires solving a problem of comparable complexity to the original robust problem, thus negating the claimed computational advantage. The paper also lacks a rigorous analysis of the approximation quality of the proposed method. While the paper demonstrates a connection between proximal point trajectories and Pareto efficient robust solutions, it does not provide theoretical guarantees on how well the approximate solutions generated by the PPM approach the true Pareto frontier, especially when using approximate PPM updates. The numerical experiments, particularly in the portfolio optimization section, do not provide a compelling case for the practical benefits of the proposed approach. The portfolio optimization section feels somewhat disconnected from the core theoretical contributions, and the results do not clearly demonstrate the advantages of the proposed method over existing techniques. The substantial discrepancy between the out-of-sample performance of robust Markowitz++ portfolios, despite their similar in-sample performance, requires further explanation. It is not clear why the distribution shift impacts the two out-of-sample performances differently. The paper would benefit from a more thorough discussion of the limitations of the proposed method, particularly in the context of non-linear objective functions and non-ellipsoidal uncertainty sets. The current discussion focuses primarily on linear objectives with ellipsoidal uncertainty, which limits the generalizability of the results. 

Typos: 
Line 157 bracket is misplaced
Line 180 by -> be
Figure 1: Porfolio -> Portfolio

### Questions
The paper would benefit from numerical experiments comparing the running time of the proposed method against the brute-force approach. The abstract should explicitly state that mean-variance optimization is the paper's primary focus. Additionally, it would be helpful to acknowledge the existence of a closed-form solution to the Markowitz optimization problem. Regarding Figure 1, the substantial discrepancy between the out-of-sample performance of robust Markowitz++ portfolios, despite their similar in-sample performance, requires further explanation.

Typos: 
Line 157 bracket is misplaced
Line 180 by -> be
Figure 1: Porfolio -> Portfolio

### Soundness
3

### Presentation
3

### Contribution
1
