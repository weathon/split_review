# Improved Finite-Particle Convergence Rates for Stein Variational Gradient Descent

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
We provide finite-particle convergence rates for the Stein Variational Gradient Descent (SVGD) algorithm in the Kernelized Stein Discrepancy ($\KSD$) and Wasserstein-2 metrics. Our key insight is that the time derivative of the relative entropy between the joint density of $N$ particle locations and the $N$-fold product target measure, starting from a regular initial distribution, splits into a dominant `negative part' proportional to $N$ times the expected $\KSD^2$ and a smaller `positive part'. This observation leads to $\KSD$ rates of order $1/\sqrt{N}$, in both continuous and discrete time, providing a near optimal (in the sense of matching the corresponding i.i.d. rates) double exponential improvement over the recent result by~\cite{shi2024finite}. Under mild assumptions on the kernel and potential, these bounds also grow polynomially in the dimension $d$. By adding a bilinear component to the kernel, the above approach is used to further obtain Wasserstein-2 convergence in continuous time. For the case of `bilinear + Mat\'ern' kernels, we derive Wasserstein-2 rates that exhibit a curse-of-dimensionality similar to the i.i.d. setting. We also obtain marginal convergence and long-time propagation of chaos results for the time-averaged particle laws.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work provides a convergence analysis of the Stein Variational Gradient Descent (SVGD) algorithm in its full formulation, i.e., using finitely many particles and in discrete time. Such a quantitative convergence proof was long sought after, ever since the algorithm was first proposed in 2016. (The only previous known result, Shi and Mackey (2024), gave a quite poor convergence rate, and had a much more involved proof.) This paper thus improves upon a long line of work reviewed in the introduction. In particular, the behavior of SVGD in the infinite-particle limit is relatively well-understood, so the main difficulty lies in the finite-particle discretization.

This work's main novel insight is presented in Equation (9) in the proof of Theorem 1, in a continuous-time context: it consists in an identity which cleanly separates the finite-particle error from the infinite-particle behavior of SVGD. The finite-particle error term in this identity can be controlled by making a mild assumption on the kernel and the target distribution (Remark 1). The discrete-time, finite-particle convergence result, Theorem 3, builds upon this insight, as well as on ideas from prior works and on new estimates (Remark 4).

The Theorems 1 and 3 establish convergence in kernelized Stein discrepancy (KSD). They are complemented by convergence results in Wasserstein distance in section 4. A long-time propagation of chaos-type result for SVGD is established in section 5.

### Strengths
This paper establishes quantitative convergence guarantees for finite-particle (and discrete-time) SVGD, with a much better dependency on problem parameters than the only previous known analysis. This is thus arguably the first satisfactory convergence bound, for an algorithm that has attracted considerable attention from theoreticians. So this paper's achievement is highly significant.

The main novel insight used in this paper is remarkably clean. It is also quite satisfying, in that it allows for an intuitive proof strategy. 

The presentation of the paper is clear, although a bit technical from section 4 onwards.

### Weaknesses
Section 5 on propagation of chaos (POC) could benefit from a little bit more motivation: it is not clear why POC would be a desirable property for SVGD.

Possible typos:
- In Assumption 1(b) and Lemma 1, p_0^N needs to be C2 (not C1) for p^N(t,.) to be C2
- in Assumption 2(d), maybe = is meant to be <=
- typos on line 430

- In the proof of Theorem 3, the bounds on the magnitude and the Lipschitz-ness of the update operator (Lemmas 3 and 4) grow with $n$ the iteration count. Is there any way to relate those quantities back to the distance between $\mu_n^N$ and $\pi$ instead? Intuitively, this way, the time-discretization error terms could be bounded uniformly for long times...
- Are there any results on the convergence of SVGD in KL divergence (with infinite particles and/or in continuous time)? If yes, do your results allow to improve upon them? If not, would your proof approach allow to get such a result?
- Does SVGD also exhibit long-time propagation of chaos for the "last-iterate" (as opposed to "time-averaged" in Proposition 1) occupancy measure of particle locations?

### Questions
- In the proof of Theorem 3, the bounds on the magnitude and the Lipschitz-ness of the update operator (Lemmas 3 and 4) grow with $n$ the iteration count. Is there any way to relate those quantities back to the distance between $\mu_n^N$ and $\pi$ instead? Intuitively, this way, the time-discretization error terms could be bounded uniformly for long times...
- Are there any results on the convergence of SVGD in KL divergence (with infinite particles and/or in continuous time)? If yes, do your results allow to improve upon them? If not, would your proof approach allow to get such a result?
- Does SVGD also exhibit long-time propagation of chaos for the "last-iterate" (as opposed to "time-averaged" in Proposition 1) occupancy measure of particle locations?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper studies the finite-particle SVGD in both discrete and continuous settings. Their results include convergence results in averaged Kernel Stein Discrepancy and Wasserstein distance.

### Strengths
The SVGD algorithm was well studied in practice for several years already. However, its theoretical understanding was rather limited. As well discussed by the authors, past work only tackled particular (simpler) cases discretization mechanisms of the continuous SVGD, leaving the most interesting case open. That is the finite-particle discrete-time setting. In this setting they solve this problem and obtain polynomial convergence guarantees for different types of metrics, under certain conditions.  
The paper is generally well-written, although certain mathematical details are omitted.

### Weaknesses
### General comments

- Some of the conditions in the main results are not easy to verify. See the Questions section. 
- The paper is generally well-written, although certain mathematical details are omitted. 

### Mathematical comments 

- The derivations starting from *line 281* are not well-explained. Why does the first term on the right-hand side vanish on second line? How is the third line derived?
- In order to obtain (17), the term $(\sum_j V(x_j)/N)^{2\alpha}$ is upper bounded  by $\sum_j V(x_j)/N$. This does not seem to be correct, even with the assumption $2\alpha < 1$. The inequality only holds if $\sum_j V(x_j)/N$ is less than 1, which is not guaranteed.
- *line 927*. "Routine computations give...". More details on this part would ease the reading. 

### Notation
- *Theorem 2*  $P(x_1(t) \in dx)$ is slightly vague from a mathematical point of view. Perhaps explicitly stating what is meant by this notation, would make the theorem clearer. 
-  $p^N (t,\underline{z})$ is defined in Lemma 1, but later in the paper the notation is changed to $p(t,\underline{z})$. 
- *notation in the proof of theorem 1* To keep notation self-explanatory I would suggest to use the number of particles in the notation for $H(0)$ in the proof of Theorem 2. That is to use $H^N(0)$, as later in the proof of the last claim you use $\sup_L H^L(0)/L$.

### typos

* *line 271* equation equation -> equation.
* *line 291* missing a period at the end of the equation.
* *line 674* Extra square bracket in the equation. 
* *line 747,749* There is a $\sum$ sign missing in the first term of the right side and in the definition of $f(n)$. 
* *page 8* literature literature -> literature

### Questions
- *Theorems 1 and 2*. Is it easy to choose an initial distribution, such that $\lim\sup_{N \to \infty} \frac{1}{N} \mathrm{KL}\left(p^{N}(0) \,\big\|\, \pi^{\otimes N}\right) < \infty$? If yes, is there a general scheme for it?
- How easy would it be to replace the averaged KSD error with the 'last iterate' KSD error. In the paper you have this type of results for some time-averaged distributions. But is it possible to avoid averaging completely as in the case of LMC?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper performs a new analysis for Stein variational gradient descent (SVGD), achieving double exponential improvement of #particle for the continuous-time and discrete-time convergence rates in Kernel Stein discrepancy (KSD) over the best known previous result. This paper also establishes the convergence in Wasserstein distance using the bilinear Matern kernel and establishes marginal convergence and long-time propagation of chaos results for the time-averaged particle laws.

### Strengths
* In KSD, this paper significantly improves the particle dependence over Shi & Mackey (2024) (which is known to be the previous best result) by considering the evolution of the joint distribution of N particles.
* In Wassertein-2 distance, this is the first convergence rate, albeit showing curse of dimension.
* The discussion on related works is extensive and informative.

### Weaknesses
 * Some notations should be further clarified, and there is not a subsection collecting all the notations which makes certain parts not that readable.
* This paper is short of some discussion on assumptions. Specifically, the growth condition in Assumption 2, while presented as a generalization, lacks sufficient explanation regarding its implications and relation to more standard conditions used in sampling analysis. The paper would benefit from a more thorough discussion on the necessity and implications of this growth condition, especially in the context of practical applications.
* Comparison with previous analysis including assumptions and rates is not that clear. While the authors claim improvement over Shi & Mackey (2024), a direct comparison of the assumptions and convergence rates in a table would greatly enhance clarity and allow for a more rigorous assessment of the contribution.
* The discussion on the convergence in Wasserstein-2 distance is weak. The paper mentions a curse of dimensionality but does not provide sufficient intuition or analysis of why this occurs, especially given the dimension-independent results for KSD. The practical implications of this curse of dimensionality for the Wasserstein distance are not sufficiently explored, leaving the reader with an incomplete understanding of the limitations of the method in high-dimensional settings.

### Questions
* For time-average distribution $\frac{1}{N}\int_0^N\mu^N(t, \mathrm{d}x)\ \mathrm{d}t$, why do you integrate it from $0$ to $N$ instead of from $0$ to $T$? Since $N$ is the number of particle, the time integration range is confusing to me.
* What is $\mathcal{L}$ in Assumption 4?
* The Growth condition in Assumption 2 is essential for Theorem 3. Can you discuss some relation between this condition with some other common conditions in sampling such as log Sobolev inequality, Poincare inequality and Talagrand inequality (which is also used in some previous works on SVGD)? What kind of distributions satisfy Assumption 2?
* Also, it would be helpful to collect all related results and their corresponding assumptions in a table for a clear comparison.
* The smoothness constant in condition (c) could be interesting to the convergence rate. Why don't you include that constant in Thm 3?
* What is the relation between Wasserstein distance and KSD? Since Thm 1 doesn't exhibit any curse of dimension (CoD), it would be interesting to provide some intuition about where the CoD comes from for Wasserstein distance. Is that due to the relation between Wasserstein distance and KSD? I think the convergence in Wasserstein distance is more interesting than KSD to sampling community, and thus there should be more discussion on this result. Does Matern kernel in SVGD show better performance than some bounded kernels (Gaussian RBF) in practice (maybe do some simulation)?
* If we choose $\alpha=1/2$, as remark 3 claims, the distribution will approach Gaussian. According to Thm 3, in order to achieve the averaged $\mathrm{KSD}^2\leq\varepsilon^2$, we need to choose $N\asymp 1/\varepsilon^2$, and thus $T=O(N^4)=O(1/\epsilon^8)$. Is this terrible mixing time comparable to other sampling algorithm for Gaussian targets?

I am happy to raise my score if the authors can answer some of the questions.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies finite-particle convergence rates for the Stein Variational Gradient Descent (SVGD) algorithm in the Kernelized Stein Discrepancy (KSD), deriving results in both continuous and discrete times. It also provides convergence rates for the continuous-time SVGD in the L2-Wasserstein metric for a specific class of kernels.

Minor typo: in line 430, either refer to Assumption 3 in the singular or the conditions in the plural.

### Strengths
The paper is extremely well written, and while I have not checked all the proofs in detail, the results appear to be formally correct. The authors also do a good job explaining the literature.

The authors bypass the challenges faced by previous attempts at deriving convergence rates for SVGD in the KSD metric by working with the joint density of particle locations and the N-fold product target measure, exploiting a simple and elegant relationship related to the evolution of their KL divergence.

### Weaknesses
A key element in the development is the N-fold product target measure $\pi^{\bigotimes N}$. Although it's definition can arguably be derived from its name, I think it would be nice to formally define it too; pressumably, $\pi^{\bigotimes N}(x_1,\cdots,x_N) := \pi(x_1)\times\cdots\times\pi(x_N)$.

Theorem 5 is derived for the Matérn-family of kernels (defined by eq. (12)) since it needs Theorem 3.5 in Kanagawa et al. (2022). However, the authors claim in the main text that the restriction to such kernels is only done for "computational clarity." This justification is somewhat vague. It is not clear if the restriction is due to a limitation in the proof technique or if it is a choice made for simplicity. The authors should clarify whether the result extends to the broader class of kernels defined in eq. (11), and if not, why the proof strategy cannot be generalized.

### Questions
Theorem 5 is derived for the Matérn-family of kernels (defined by eq. (12)) since it needs Theorem 3.5 in Kanagawa et al. (2022). However, the authors claim in the main text that the restriction to such kernels is only done for "computational clarity." Could the authors add a remark further clarifying if this means that Theorem 5 extends to the broader class of kernels defined in eq. (11)?

### Soundness
4

### Presentation
4

### Contribution
4
