# Near-Optimal Solutions of Constrained Learning Problems

- Decision: Accept
- Avg Score: 5.80
- Scores: 6, 3, 6, 8, 6

## Abstract
With the widespread adoption of machine learning systems, the need to curtail their behavior has become increasingly apparent. This is evidenced by recent advancements towards developing models that satisfy robustness, safety, and fairness requirements. These requirements can be imposed (with generalization guarantees) by formulating constrained learning problems that can then be tackled by dual ascent algorithms. Yet, though these algorithms converge in objective value, even in non-convex settings, they cannot guarantee that their outcome is feasible. Doing so requires randomizing over all iterates, which is impractical in virtually any modern applications. Still, final iterates have been observed to perform well in practice. In this work, we address this gap between theory and practice by characterizing the constraint violation of Lagrangian minimizers associated with optimal dual variables, despite lack of convexity. To do this, we leverage the fact that non-convex, finite-dimensional constrained learning problems can be seen as parametrizations of convex, functional problems. Our results show that rich parametrizations effectively mitigate the issue of feasibility in dual methods, shedding light on prior empirical successes of dual learning. We illustrate our findings in fair learning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the problem of constrained learning using the dual-ascent relaxation framework. The paper attempts to bound the error in the constraints of the relaxed solution using the dual variables. The approach is based on an infinite-dimensional (not parameterized) formulation/relaxation of the dual problem in which the bounds are obtained. This provides a bound on the error in the infinite-dimensional primal problems and the results are used to bound the error in the actual solution to the primal using the actual finite-dimensional dual ascent.

### Strengths
The narrative of the paper is initially quite clear and the approach is relatively novel and intuitive. The problems seems interesting. There are clear theorem statements and clearly stated assumptions. The mathematics is mostly rigorous and quite general.

### Weaknesses
The interpretation of the results are not clearly stated. In an attempt to be perfectly general, it is hard to state exactly how the results apply to any particular learning problem. One would think that algorithms based on neural networks would perform quite differently than a kernel-based approach using a single poorly chosen kernel. And yet the results don't seem to account for such differences in any way. Additionally, this makes it hard to understand if the 7 (mostly regularity) assumptions are valid and what the corresponding parameters are.

Specific concerns and questions are listed as follows.

1 Please more clearly spell out the motivation in the context of fairness of including the constraint vs. just not including data on the protected classes.

2 "$\mathcal{F}_\theta$ can be a neural network" -- First, its a set, not a network. But remind me -- in this case will the hypothesis space be convex? Also, take the extreme case of a single arbitrarily chosen Gaussian kernel. Is there not some problem with fragility/generalizability? Performance on untrained data? How does this approach account for the robustness of the parameterization? Maybe this relates to the question of which topology is being used to characterize Lipschitz continuity.

3 The Lipschitz and convexity are defined using $\ell$ which is a statistical function. Would it not be more suitable to define them using the actual functions, $\tilde{\ell}$?

4 Not much mention of the primal-dual gap and whether it is significant in parameterized or unparameterized problems

5 Generally bothersome to have lots of assumptions unless it can be shown they are satisfied in certain basis and useful cases.

6 I'm not sure exactly the point of Section 3.3.2 -- Are we saying that the bounds can be improved by making the constraints strict?

7 "We will denote by $\hat \ell$ an estimate of $\ell$ using the dataset D...." First, redefining $D$ casuses confusion. Also, how is this now a dataset? Also, this brings up the $\ell$ vs $\tilde{\ell}$ issue again -- Alg 1 is defined using $\ell$ and not $\tilde{\ell}$. What is $D^*_p$ in Lemma 4.1 -- clearly not related to D.... Actually it seems there are lots of $D$-based notation in this paper.

8  "We train this model over T = 400 iterations using a ADAM"  Acronym undefined -- maybe they mean Adam, which is an algorithm. What is $\ell$ here? Are the Assumptions satisfied? What are the obtained bounds?

Minor corrections are as follows

- Page 1 - "In fact, this problem is even hard from" -- which problem?

- Notation $D_{KL}$ on Page 2 is undefined.

- "guarantees usually pertain a probability distribution over"

- Assumption 3.2 is unclear. What is $f_\theta(\lambda)$ here? It becomes more difficult to interpret the results after this.

- "the unparametrized Lagrangian minimizer is unique" -- presumably this is the solution for the unparameterized version, $D_u$?

- "unparametrtized"

- Assumption 3.4 seems difficult to verify...

- Thm 3.5. This is difference between the constraint functions, not their violations since $\ell_i$ are not non-negative.

- Page 12, after Defn A.1. Some conflation of operator $B \in \mathcal{B}$ and its representor, $g$.

- Defn A.3 -- what does it mean for $h(x)>-\infty$?

- "Linear independence constraint qualification (LICQ)" -- capitalization issue...

- "Thus, it can be thought of as the baseline effect" --  define "it"... What is the third component -- I see only two.

- " Combining the bound in equation in equation 6 with"

- numerous problems with bibliography entries.

- Proofs in appendix need better organization. No explanation or connecting verbiage is given. For example, Appendix A.6

### Questions
Specific concerns and questions are listed as follows.

1 Please more clearly spell out the motivation in the context of fairness of including the constraint vs. just not including data on the protected classes.

2 "$\mathcal{F}_\theta$ can be a neural network" -- First, its a set, not a network. But remind me -- in this case will the hypothesis space be convex? Also, take the extreme case of a single arbitrarily chosen Gaussian kernel. Is there not some problem with fragility/generalizability? Performance on untrained data? How does this approach account for the robustness of the parameterization? Maybe this relates to the question of which topology is being used to characterize Lipschitz continuity.

3 The Lipschitz and convexity are defined using $\ell$ which is a statistical function. Would it not be more suitable to define them using the actual functions, $\tilde{\ell}$?

4 Not much mention of the primal-dual gap and whether it is significant in parameterized or unparameterized problems

5 Generally bothersome to have lots of assumptions unless it can be shown they are satisfied in certain basis and useful cases.

6 I'm not sure exactly the point of Section 3.3.2 -- Are we saying that the bounds can be improved by making the constraints strict?

7 "We will denote by $\hat \ell$ an estimate of $\ell$ using the dataset D...." First, redefining $D$ casuses confusion. Also, how is this now a dataset? Also, this brings up the $\ell$ vs $\tilde{\ell}$ issue again -- Alg 1 is defined using $\ell$ and not $\tilde{\ell}$. What is $D^*_p$ in Lemma 4.1 -- clearly not related to D.... Actually it seems there are lots of $D$-based notation in this paper.

8  "We train this model over T = 400 iterations using a ADAM"  Acronym undefined -- maybe they mean Adam, which is an algorithm. What is $\ell$ here? Are the Assumptions satisfied? What are the obtained bounds?

Minor corrections are as follows

- Page 1 - "In fact, this problem is even hard from" -- which problem?

- Notation $D_{KL}$ on Page 2 is undefined.

- "guarantees usually pertain a probability distribution over"

- Assumption 3.2 is unclear. What is $f_\theta(\lambda)$ here? It becomes more difficult to interpret the results after this.

- "the unparametrized Lagrangian minimizer is unique" -- presumably this is the solution for the unparameterized version, $D_u$?

- "unparametrtized"

- Assumption 3.4 seems difficult to verify...

- Thm 3.5. This is difference between the constraint functions, not their violations since $\ell_i$ are not non-negative.

- Page 12, after Defn A.1. Some conflation of operator $B \in \mathcal{B}$ and its representor, $g$.

- Defn A.3 -- what does it mean for $h(x)>-\infty$? 

- "Linear independence constraint qualification (LICQ)" -- capitalization issue...

- "Thus, it can be thought of as the baseline effect" --  define "it"... What is the third component -- I see only two.

- " Combining the bound in equation in equation 6 with"

- numerous problems with bibliography entries.

- Proofs in appendix need better organization. No explanation or connecting verbiage is given. For example, Appendix A.6

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the problem of contrained learning problems using the dual learning algorithm. The authors provide feasiblity gap (for both the primal and dual variables) between the parameterized/unparameterized problems under certain regularity conditions. The authors then provide optimality gap for the dual learning algorithm, and numerical validations for the hypothesis that the feature space size impacts optimality gap according to the theory.

### Strengths
The paper is clearly written and easy to read. The authors make the assumptions clear and define the problem well. The theory for the parts I checked is sound.

### Weaknesses
1. The paper's title is near-optimal solutions which is misleading. The main results compare the stationary points of constrained/unconstrained problems as well as using the dual learning algorithm. I'd expect optimality in statistical sense where a lower bound is provided for rates of convergence/estimation error, instead of studying the limiting points error, which is less interesting to me.
2. Following the previous point, bounding the error of stationary points is often less interesting in terms of optimality, and lacks of theoretical contributions to the community. Perhaps the authors can provide why such analyses is nontrivial/fundamentally harder than other problems and why it is important to understand this first.
3. The numerical experiments seem weak. It is not suprising that there will be a gap and as the number of features grow the model approximation error is smaller. I'm not seeing how this directly corrobates the theory. Ideally I would like to see (i) a hypothesis emerged from the theory (ii) an experiment that validates the hypothesis.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considered the problem of providing a theoretical guarantee on the feasibility of the last-iteration solution of a Dual Constrained Learning Algorithm (i.e., dual ascent algorithm applied to the constrained learning model parameterized by $\theta$). Typically, to get a feasible output of the dual acsent algorithm applied to the constrained learning models, one need to perform averaging or randomization over the whole output sequence, which is impractical in reality. Let $P_p$ denote the parameterized constrained learning problem where the candidate functional solutions satisfy $f_\theta\in F_\Theta$, $\theta\in\Theta$. In addition, let $P_u$ be the unparameterized constrained learning problem where the candidate functional solutions come from the set $F\supseteq F_\theta$. The main contribution of this paper is that authors showed that the optimal lagrangian minimizers of problem $P_p$, denoted by $f_\theta(\lambda^*_p)$, are close to the optimal lagrangian minimzer of problem $P_u$, $\phi(\lambda_u^*)$.

### Strengths
1. Let $\ell(f_\theta)\leq 0$ be the constraints that are required for the output $f_\theta$ to satisfy. The author showed for the first time that under some assumptions on the constraints $\ell$, it holds $||\ell(f_\theta(\lambda_p^*))- \ell(\phi)||$ is bounded by some constants, where $f_\theta(\lambda^*_p)$ is the optimal lagrangian min of $P_p$ and $\phi^*$ is the optimal lagrangian min of $P_u$ such that $\ell(\phi^*)\leq 0$.
2. The authors provided high level explanation and intuition which helps the reader to understand the paper better.

### Weaknesses
1. the bound on $|\ell(f_\theta(\lambda_p^*))- \ell(\phi)||$ contains $|\lambda_p^*||_1$, which could be large when the number of coinstraints $m$ is large. When $|\lambda_p^*||$ is large, we cannot assert that $f_\theta(\lambda^*_p)$ is almost feasible. Is there any way to show that $|\lambda_p^*||_1$ is small under some assumptions? Specifically, the dependence on the number of constraints $m$ is concerning, as a large number of constraints could lead to a loose bound, making the feasibility guarantee less meaningful in practice. It would be beneficial to explore conditions under which the norm of the optimal dual variable $|\lambda_p^*||_1$ remains bounded, independent of the number of constraints.
2. The authors considered $f_\theta(\lambda_p^*)$, the optimal lagrangian minimzer of $P_p$. However, one can only get $f_\theta(\lambda_p^*)$ after infinite iterations. It would be more interesting if the authors can provide some information on the feasibility of $f_\theta(\lambda(T))$. In particular, how close can $f_\theta(\lambda(T))$ and $f_\theta(\lambda_p^*)$ be? The lack of finite-time analysis makes it difficult to assess the practical applicability of the proposed method. A bound on the suboptimality of the primal iterates after a finite number of iterations would be crucial for practical use.
3. The author measured the distance between $\ell(f_\theta(\lambda_p^*))$ and $\ell(\phi^*)$. However, $\phi^*$ doesnot necessarily belong to $F_\theta$. It seems a feasible solution from $F_\theta$ should be a better option and perhaps will bring us better bounds. Comparing against a solution that is not in the parameterized family $F_\theta$ makes the bound less relevant for practical scenarios where we are interested in the feasibility of solutions within $F_\theta$. It would be more insightful to compare against the best feasible solution within $F_\theta$, which would provide a more direct measure of the suboptimality introduced by the parameterization.

### Questions
1. Can the authors provide some information about the convergence property of the dual-ascent algorithm applied to a problem with non-convex constraints?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discusses the primal dual algorithm for training a neural network. Since the constraint is difficult to handle, one typical alternative solution is to use Lagrange multiplier to penalize the constraint violation in the objective function and calculates its minimum. This paper specifically calculates and bounds the violation of the constraint to demonstrate that the primal dual algorithm is still good for training NN. Experiments also verify the theoretical conclusion.

Update:
I read the rebuttal. I found the contribution that this paper bounds the optimality gap which is not generally known in convex case, and the way it handles constraint and shows that the primal convergence, which does not in nonconvex case in general, is important. I raise the score to 8 while not having checked all details.

But I still wonder how good the approximation of the functional class is, i.e., how big is the distance from any function to a function in the parameterized family that the training algorithm is in, and how training error indicates the test error when one has finite samples but a parameterized family to train on being very large. With that, I do not raise confidence and do not raise score to 10.

### Strengths
I think this paper is mathematically correct, detailed, and self consistent. The writing is clear, which gives a lot of discussion, and the logic and the structure that goes to the final conclusion step by step is reader friendly. The analysis of different scenarios under the big primordial framework is comprehensive and detailed.

### Weaknesses
Besides finding the extent of violation of the constraints, it is also very important to bound the objective function’s suboptimality of the final iterates. Especially, since this paper is positioned in NN scenario, the objective function is typically highly nonconvex, and there might be some optimality gap when introducing the dual function, which is relevant to the convex hull of the primal function rather than the primal function itself. This gap, which arises from the non-convexity of the primal problem, needs to be explicitly addressed and bounded to ensure the practical relevance of the proposed algorithm. The analysis should clarify how the algorithm's iterates approach the true optimum of the original non-convex problem, not just its convex relaxation. Furthermore, the paper does not clearly discuss the implications of using an approximate oracle in Line 4, and how this approximation affects the final convergence bounds. The analysis should consider the impact of this approximation on the overall performance of the algorithm, especially in the context of non-convex optimization.

### Questions
This paper introduces an algorithm which has two inner oracles the first optimizes the Lagrangian function by an argmin expression, while the dual variable part is easy to understand. Is this a typical method when we train your networks under constraints, or one typically use the gradient projection? I guess there is a large difference between the sub optimality gap of these two algorithms, so that the authors prefer Algorithm 1. What is the calculation of complexity of the oracle Line 4, and what is the total convergence rate and complexity of algorithm 1?

How to solve Line 4? If you solve it multiple times, what is the total complexity?

How to choose $\eta$?

Page 3, "... $P_p$ is convex" maybe use "... eq$(P_p)$ is convex" to differentiate $P_p$ and $P_p^*$.

I think people in ML area are not familiar with functional optimization so it would be great to explain more. For example, Assumption 3.1, it can be "$M$-Lipschitz \emph{with respect to functional $\ell_2$ norm}" with a footnote about the norm. Also explain strong convexity and smoothness in functional space.

Is there an interpretation of Assumption 3, or for common parameterized classes of functions, can you give an example how large the gap is? 

Thm. 3.5, I think the $\ell_2$ norm on left hand side is a two norm on scalar right? Can you just use $(l(...) - l(...))^2$ or $|l(...) - l(...)|$? Typically we only write norm for vectors.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies a parameterized constrained learning problem and proves that the infeasibility of the Lagrangian minimizer as well as that of the best iterate of dual ascent algorithms is close to that of the corresponding unparameterized convex constrained learning problem. Such a gap is proportional to the parameterization error, which means the Lagrangian minimizer of the parameterized constrained learning problem is nearly feasible under rich parameterization. Compared with the randomized or averaged sequence of primal iterates studied in the existing theoretical results, the best primal iterate studied in this theoretical work is more practical.

### Strengths
Originality: This work provides original theoretical results as explained in my summary above. In addition, the proof techniques in Section 3.3 look novel. 

Quality: The theoretical error bound proportional to the parameterization error is reasonable by intuition. 

Clarity: The general structure of this paper is clear. 

Significance: The best iterate is more practical than the commonly used randomized or averaged sequence of primal iterates, so it is meaningful to provide the first convergence analysis of the best iterate.

### Weaknesses
(1) The theory could be improved in the following aspects: 

(1.1) In line 4 of Algorithm 1, the **exact** minimizer of this unconstrained **nonconvex** optimization problem cannot be obtained. This minimization error should be considered which I envision will involve the parameterization error $\nu$ plus the error rate of the corresponding convex unconstrained optimization. Specifically, the analysis should account for the fact that the obtained $f_\theta(t)$ is only an approximate minimizer, i.e., $L(f_{\theta}(t), \lambda(t)) \leq \min_{\theta} L(f_{\theta}, \lambda(t)) + \rho_t$ for some error $\rho_t$. This error $\rho_t$ will propagate through the analysis and affect the final bounds. In addition, for the stochastic version of Algorithm 1, the error of $\widetilde{\ell}_i\approx \ell_i$ should also be considered in line 4, not just in the dual update step in line 5. The stochasticity in the gradient calculation will introduce additional variance that needs to be properly bounded, and this is not addressed in the current analysis.

(1.2) The error of $f_{\theta}(t)$ as well as $\widetilde{\ell} _ i\approx \ell _ i$ will also cause the approximation error of $g_p(\lambda(t))\approx\widetilde{\ell} _ 0[f _ {\theta}(t)]+\lambda(t)^{\top}\widetilde{\ell}[f _ {\theta}(t)]$ for selecting the best prima iterate. This should also be considered. The current analysis assumes that $g_p(\lambda(t))$ can be computed exactly, which is not realistic in practice. The approximation error in $g_p(\lambda(t))$ will affect the selection of the best primal iterate and needs to be accounted for in the theoretical results.

**The above two are the most important problems I think. I would like to increase my score once they are addressed.**

(1.3) You could also obtain the difference of $\ell_0$ between parameterized and convex problems in both Theorem 3.5 and Proposition 4.2 so that the solution of the unparameterized problem is not only nearly feasible but also nearly optimal. The current results only focus on the feasibility of the parameterized solution, but it would be more complete to also analyze its optimality in terms of the objective function $\ell_0$.

(1.4) You could obtain finite time convergence result, i.e. when replacing $\lambda^{\rm best}$ in Proposition 4.2 with $\lambda _ T^{\rm best}$, the best iterate up to a fixed iteration $T$, what is the convergence rate involving $T$? I think this is possible by using the existing convergence rates on the convex constrained optimization problems in terms of the constraint violation (like $\sum _ {i=1}^m \alpha _ i\max(\ell _ i, 0)$ for some constants $\alpha _ i>0$) as well as optimality. Then we upper bound difference of the convergence rates between the convex and parameterized versions. The analysis should explicitly show how the convergence rate depends on the number of iterations $T$ and the parameterization error $\nu$.

(2) A few points are to be clarified as listed in the questions below.

### Questions
(1) About the example of Counterfactual Fairness Constraints

(1.1) Is this example proposed by you? If not, cite the sources of the model and data. Otherwise, say that this example is proposed by you. 

(1.2) What do the constraints mean in this example? You could add an explanation to the paper. 

(1.3) Should we use $\mathbb{E} _ {x,y}$ in both objective and constraints, with the same distribution of $(x,y)$?

(1.4) Why are some $x$ bolded and some are not? Are they the same $x$?

(1.5) $f _ {\theta}(x)$ and $f_{\theta}(x,z)$ have inputs of different dimensionality. How can you make that happen, for example, in a certain neural network with a certain fixed parameter $\theta$?

(2) At the end of Section 2, you mentioned that Lagrangian minimizers are not unique and some of them could contain infeasible optimal primal variables. Is this found by you or previous literature? If it is found you, you could provide examples to support your claim and emphasize this claim as one of your novelty. Otherwise, you could cite the papers that prove this claim. 

(3) Right after the problem $(P_u)$ at the beginning of Section 3.1, you could mention $\phi\in\mathcal{F}$. 

(4) It seems that $\phi(\lambda_u)$ (in Assumption 3.2) and $\Phi^*(\lambda_u)$ are the same, right? If yes, you could unify the notations. If not, you could explain the meaning of $\phi(\lambda_p^*)$ in the paper. 

(5) In paragraph 2 of Section 3.2, it may be clearer to change ''We will first provide a result assuming this curvature is known'' to something like ''We will first provide a result with the following assumption on the knowledge of this curvature'', so readers can relate to Assumption 3.4.

(6) After ''The second one captures the effect of parametrizing the hypothesis class for a fixed dual variable.'', you could add something like ''We will elaborate these perturbations in Section 3.3.1 and Section 3.3.2 respectively.''

(7) In the experiment, 

(7.1) What negative likelihood function $\ell _ 0$ do you use (or the distribution of $x, y$)? What function $f _ {\theta}$ do you use? 

(7.2) What is the math expression of the counterfactual fairness in the middle of Figure 2?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
