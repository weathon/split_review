# Almost Sure Convergence of Average Reward Temporal Difference Learning

- Decision: Reject
- Scores: 3, 6, 1, 3

## Abstract
Tabular average reward Temporal Difference (TD) learning
is perhaps the simplest and the most fundamental policy evaluation algorithm in average reward reinforcement learning.
After at least 25 years since its discovery,
we are finally able to provide a long-awaited almost sure convergence analysis.
Namely,
we are the first to prove that, under very mild conditions, 
tabular average reward TD converges almost surely to a sample-path dependent fixed point.
Key to this success is a new general stochastic approximation result concerning nonexpansive mappings with Markovian and additive noise,
built on recent advances in stochastic Krasnoselskii-Mann iterations.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors present an almost sure convergence analysis for finite state-action spaces, infinite horizon average reward in the tabular setting (that is without linear function approximation for the relative value function). There are many prior works in this regime, but the ones which are the most relevant are: (i) Tsitsiklis and Van Roy 1999 and (ii) Zhang et al 2021. The problem formulation addresses data sets obtained through Markovian sampling, with additive noises.

### Strengths
It is theoretically interesting to examine the almost sure convergence of fixed policy evaluation in tabular settings without relying on value function projection to achieve the contraction needed for analysis.

### Weaknesses
The amount of literature in this realm is quite significant. My main issue is the limited scope of this work. For instance, the following have been very well studied:
(i) Tsitsiklis and Van Roy 1999 consider policy evaluation using linear value function approximation, where the feature vectors do not span the constant vector (a mild assumption which doesn't hinder the applicability of their approach in many problems). They provided an asymptotic convergence analysis for this TD learning algorithm. The authors argue that their assumption does not hold when considering tabular cases and that might be true, but for most applications of interest, the state and action spaces are large enough to necessitate the use of function approximations for value function estimation to ensure practicality. Hence, the importance of this work is not well motivated.
(ii) Zhang et al 2021 considered the Tsitsiklis and Van Roy 1999 approach and relaxed the assumption by including a projection step, where the value function vectors are projected onto a subspace where an unique representation for them exists (generally the average reward value functions aren't unique vectors and are unique only upto an additive constant, and this projection eliminates this non uniqueness). They later characterize convergence in L2 space instead of asymptotic convergence and provide finite time bounds in terms of expectations of quantity of interest. The authors argue L2 convergence does not imply almost sure convergence which is true and also claim that the iterates converge to a set instead of a unique point. But if every point in this set is a solution, there is no need to obtain a unique solution since the original value function is not unique anyway.  

Given all these limitations, I feel the work lacks sufficient contribution.

### Questions
Why is the asymptotic analysis for only the tabular case important? Prior results exist for applications with linear function approximations which capture almost all applications of interest. And prior literature also provides finite time bounds (although in the L2 norm sense) which are of more significance in terms of determining sample complexities, etc. The motivation for this work is not compelling in its current form.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studied the convergence temporal difference(TD) algorithm in average reward setting and tabular case. What differs the work from many existing literature is the focus on almost sure (a.s.) convergence. Discussions on limitations of existing approaches on a.s. is provided with clarity. A general a.s. convergence for stochastic system with Markovian noise and additive noise is established, as a result of which TD algorithm in average reward setting is established.

### Strengths
* A long standing a.s. convergence of TD in average reward setting is investigated and convergence result is confirmed.

* A general a.s. general a.s. convergence for stochastic system with Markovian noise and additive noise is established, which might be of an independent interest.

* Discussions on existing approaches are helpful and provide clarity.

### Weaknesses
 * Although an a.s. convergence is characterized, it's not clear as to how the connection of sample path and the resulting fixed point. It would be nice to have further clarification.

* In the sentence of Line 149-151, the authors argued that existing analysis failed to move beyond convergence to a bounded invariant set. However, the main result in Theorem 2 falls into the same category, as it converges to $\mathcal{V}_{*}$, which is an unbounded set.



### Questions
1. The value function defined in Line 65 appears slight different from Page 250 value function definition in [1], are they equivalent? If so how to see this?

[1] Sutton, Richard S. "Reinforcement learning: An introduction." A Bradford Book (2018).

2. In equation (5), why not just cancel out v(t) with the last term in h(v(t))? Is there some consideration for not doing so?

3.  In the sentence of Line 149-151, the authors argued that existing analysis failed to move beyond convergence to a bounded invariant set. Are there any particular references the authors are referring to? If so, please provide them.

4. In Line 168, it mentioned that "it cannot be used once function approximation is introduced". Can you elaborate more on this?

5. Maybe a question concerns future effort, where are the potentially challenges lie in analysis in order to achieve a convergence with rate rather asymptotic convergence?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The present paper studies tabular average rewerd temporal difference and proves it converges almost surely to a sample path dependent fixed point.

### Strengths
The proofs in this paper seem sound, even if the tools used are much more complicated than the problem.

### Weaknesses
In my view, the contributions of this paper are limited, as the problem it addresses is significantly simpler than the authors suggest. At least one-third of the paper is spent attempting to persuade the reader that the problem is more complex than it actually is, taking up considerable space and reducing readability.

Here is a list of concerns:
1. The sections "Hardness in Stability" and "Hardness in Convergence" seem somewhat artificial: (5) and (6) admit explicit solutions, using matrix exponentials and the superposition principle. This approach would make the analysis clearer and directly yield the desired stability property, which is straightforward. It follows simply from the fact that $D(P-I_d)$ admits $A=$ { constant vectors } as its kernel and is Hurwitz on any space complementary to $A$. Similarly, the convergence property mentioned on lines 147–148 is evident using the explicit solution. The authors spend considerable effort on a more complex analysis using tools that are not needed for this specific case. This obscures the underlying simplicity of the problem.
2. I disagree with the interpretations presented in the "Hardness with Linear Function Approximation" section. In fact, the results of this paper can be easily derived using standard results on linear function approximation. It suffices to take $K=|S|-1$, $\Phi(i,i)=1-1/|S|$ and $\Phi(j,i)=-1/|S|$ for $0\leq i\leq |S|-1$ and $j\neq i$. This leads to a new algorithm similar to the one studied in this paper, up to an additive constant vector (constant with respect to the state but not the iterative variable). This approach enables straightforward convergence using the ODE method ($L^2$ and almost surely) and provides a much more precise description of the path-dependent limit in Theorem 5.1. The authors fail to recognize that the tabular updates can be represented in a linear form with a specific choice of basis functions. This linear formulation would simplify the analysis and provide a clearer path to convergence.
3. Several primary definitions are missing, such as sample path-dependent convergence. Some standard definitions are misused: for instance, (3) is not an Euler discretization of (5), nor is the equation on line 188 an Euler discretization of (9). The lack of precision in defining key concepts and the misuse of standard terminology raise serious concerns about the rigor of the analysis. For example, the term 'sample path-dependent convergence' is used without a clear definition, making it difficult to assess the validity of the results. The authors should provide a formal definition of this term and justify its use in the context of their work. The incorrect characterization of the discretizations further undermines the paper's credibility.
4. The main argument in this paper relies on the ODE method, yet I am surprised it is never explicitly cited. Moreover, this method only provides asymptotic convergence results, while the trend is increasingly toward non-asymptotic results. This leads me to think that a thorough discussion of such methods is missing, at least in the "Related Work" section. The authors should explicitly acknowledge the use of the ODE method and discuss its limitations, particularly regarding the lack of non-asymptotic results. A more comprehensive discussion of alternative methods, such as those providing finite-sample guarantees, is necessary to place this work in the proper context.

### Questions
See the weaknesses.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper provides an analysis of tabular average reward TD under the additive noise assumption and assuming a Markov chain. The analysis extends the result of SKM to Markovian noise case.

### Strengths
1. The paper is well-written and provide clear comparison with related works.


2. The authors almost sure convergence of tabular average reward TD under some restricted assumptions. The work may provide some hints on further proving its convergence under milder assumptions.

### Weaknesses
1. My major concern is that as the authors mentioned, the additive noise assumption in Assumption 4.5 is quite strong assumption. For example, in bounding, $\bar{\bar{\epsilon}}^{(1)}_n$, the additive noise assumption plays a key role. At least in the context of RL, this assumption seems to be not a mild assumption, and not commonly use used, as opposed to the argument in the abstract by the authors. With this assumption, I believe many open problems in RL can be solved.


2. The analysis of stochastic approximation with Markovian noise has been well-studied in the literature, in particular using the Poisson equation. Therefore, it is questionable, what is the difficulty of applying such techinque to the anlaysis of SKM.


3. Although the authors claim that combining non-expansive mappings and Markovian noise has not been studied, and I acknowledge that the result itself can be considered a contribution, I am not fully convinced of its originality or significance. This is because both topics have been well-studied in SKM and in literature of stochastic approximation with Markovian noise.


4. Moreover, the authors claim that there are new terms to bound (in paragraph 2 of related works), which authors claim to be novel and challenging. But I think the claim is insufficient because the terms not appearing in the previous literature does not always mean that it is novel or challenging. There should be more supporting claims or explanation why the terms are novel and they are difficult to bound.


5. Lastly, following the discussion with Reviewer PPqC, I have some concerns regarding the choice of feature matrix. While I do not have a specific suggestion nor the literature seems to have one, it is questionable whether we can definitively conclude that the result of Tsitsiklis and Van Roy does not imply the convergence in a tabular setup. Are there any chance that a nice choice of feature matrix other than Reviewer PPqC suggested, can imply the convergence in the tabular setup?

### Questions
1. $e$ in equation (1) has not been defined previously.

### Soundness
4

### Presentation
3

### Contribution
2
