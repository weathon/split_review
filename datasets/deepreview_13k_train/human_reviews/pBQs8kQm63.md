# Finite Sample Analyses for Continuous-time Linear Systems: System Identification and Online Control

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Real world evolves in continuous time but computations are done from finite samples. Therefore, we study algorithms using finite observations in continuous-time linear dynamical systems. 
We first study the system identification problem, and propose a first non-asymptotic error analysis with finite observations. Our algorithm identifies system parameters without needing integrated observations over certain time intervals, making it more practical for real-world applications. Further we propose a lower bound result that shows our estimator is provably optimal up to constant factors.
Moreover, we apply the above algorithm to online control regret analysis for continuous-time linear system. Our system identification method allows us explore more efficiently, enabling the swift detection of ineffective policies. We achieve a regret of $\mathcal{O}(\sqrt{T})$ over a single $T$-time horizon in a controllable system, requiring only $\mathcal{O}(T)$ observations of the system.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper considers a continuous time linear control system and proposes a system identification method with a convergence rate guarantee. A lower bound is also developed to demonstrate the optimality of the upper bound. The system identification method is then applied to an online control method to obtain a regret bound.

### Strengths
1. The identification of continuous time linear system is not fully studied in the statistical learning setting, especially the convergence rate analysis.
2. The paper uses two approximation of A, B to construct the estimator, which is quite novel. 
3. The paper is well written.

### Weaknesses
1. My major concern is the novelty and significance. The system ID of linear systems is very well studied for discrete-time systems. The extension to continuous time systems is interesting, but I don't see significant technical difficulty. Besides, most classical control literature considers continuous time linear systems already in the past, e.g. [W1]. The authors should provide a better summary of the technical novelty for their convergence rate analysis.

2. The lower bound and the regret analysis also seem to be straightforward extensions of the existing results for the discrete time systems in [W2]. The authors should provide a better summary of the technical novelty for their lower bound analysis.

### Questions
1. This paper mentions that the one major motivation is practicability: most linear systems in practice are continuous time. But does this paper consider other practical issues, such as uneven time sampling? Does the algorithm still work if the time discretization is also noisy and uneven?

2. Another practical issue is the imperfect state observation, i.e. the observation is $x_t+\epsilon_t$. This is easier than output feedback but this is also a common issue in real-world applications. How can the proposed algorithm be generalized to handle imperfect state observations?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper studies the problem of control in a continuous time setting, where the state/environment varies by a stochastic process. The authors suggest a method of discrete sampling that involves a mixture of system identification and discarding non-stable controllers, allowing a regret of O(sqrt(T)), matching the best-known bounds in the literature.

### Strengths
1) Addresses a weakness in the literature of approximating $X_{t+\epsilon}$, (could add references for readers, line 227), but then proposes a solution that involves preserving bijections between matrix exponentials.
2) Nice ideas in section 4.2 involving system identification,
3) Makes progress towards a challenging problem in the literature

### Weaknesses
1) Firstly, it is hard to trust the regret bounds presented in the paper without any numerical simulations, and it is also hard to accept the paper in good faith without a limitations section.
2) The assumption of having H>1 could be justified further in line 349. For instance, it is a significant weakening to run the system of multiple trajectories, instead of a single, purely online, trajectory.
3) The paper only studies the model of the LQR cost function (the main focus is more on stability, granted); but how does this extend to more general costs?
4) The exact technical novelty of the paper seems to be unclear. For instance, optimizing while estimating system parameters is not new (The Nonstochastic Control Problem, Hazan et. al., Online Policy Optimization in Unknown Nonlinear Systems, et. al.). Maybe the authors can comment on why this result doesn't follow from the literature?
5) Why aren’t the time intervals $h$ chosen in a dynamic fashion? Surely, this would lead to better bounds? Right now, it seems $h=\frac{1}{15\kappa}$, where $\kappa$ is assumed to be known in advance (this is potentially a very significant assumption since the entire point of the system identification is to estimate A and B).
6) Line 162, would be good to clarify somewhere that $\mathbb{S}_+$ represents the set of symmetric PSD matrices,
7) Line 169, how do we know that the optimal mapping is unique? If it is not unique, then the convergence described in Line 176 is not guaranteed, right?
8) Line 1456 - why is the determinant never 0?
9) Line 283. How small should h be for the estimation to hold?
10) Line 190. There are many notions of regret. It would be good for the authors to clarify that this is the expected regret of the system. In this sense, it seems that the paper overclaims a little at the start.
11) Grammatical issues: line 483. $U^*$ should “minimize” cost, not minimizes. Line 502 - “analyze”, not “analysis”. Line 241. Missing an “in” between “relationship” and “equation"
12) Missing references: Line 100 seems to be missing a reference for Simchowitz et. al, Line 293, 304, 306. Missing reference for Algorithm (hard to tell which algorithm the paper is referring to)

### Questions
See weaknesses section.

### Soundness
2

### Presentation
2

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
This paper presents the first $\mathcal{O}(\sqrt{T})$ regret LQ continuous control algorithm. Besides, it shows its lower bound ($\sqrt{T}$) matching the upper bound, which means this algorithm nearly optimal (the regret is tight).  The algorithms seems novel.

### Strengths
1. The first continuous LQ algorithm achieving $\mathcal{O}(\sqrt{T})$ regret.
2. This algorithm is nearly optimal (the upper bound matches lower bound).

### Weaknesses
1. There are no empirical results presented in paper. Could you perform the experiment to compare your algorithms with (Thompson sampling efficiently learns to control diffusion processes)?
2. I thought in Algorithm 3 line 435 (for $k=0,....\frac{\sqrt{T}}{h}-1$), the $\frac{\sqrt{T}}{h}-1$ is not an integer in most cases, this should be fixed.
3. In page 6 $\textbf{Summary of Notations}$, there are some typos $\textbf{??}$ in 4 and 5.
4. In Abstract 'Our system identification method allows us explore more efficiently' to 'Our system identification method allows us to explore more efficiently'
5. Can you check the $\textbf{Lemma 12}$ in page 17, you should make your subscript more clear, don not always use $k$ as subscript.



### Questions
Also I confess that I have not checked each mathematical conduction presented in the paper in details since this paper is mathematical heavily.

This algorithm can not be applied in nonstochastic settings or adversarial settings since in exploration stage the action is perturbed by gaussian noises, right?

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
3

### Summary
This paper studies the system identification and control of continuous-time linear systems.  The three main contributions are (i) a system ID method that achieves optimal performance (up to constant factors) when the system is stabilized by a known controller, (ii) an approach for identification via N trajectories in the case when a stable controller is not available, and (iii) an approach that learns to control an unknown system assuming a stabilizing controller is known in advance.   This final contribution is the most exciting result to me, and eliminates an annoying log factor in the current state of the art.

### Strengths
Learning to control an unknown system has been a rich and exciting line of research in recent years.  This paper contributes to it by pushing the theory in the continuous-time setting, whereas most work has considered discrete systems.  This is an important direction for the field and the paper achieves optimal (up to constant factor) results in the context where a stabilizing controller is known.  This is a clear contribution to the literature. 

The key ideas underlying the analysis include a novel discretization of the continuous-time system which allows adaptation of recent tools developed for the analysis of discrete time systems.  I expect that this discretization will allow others to build on the work in the paper, studying more general settings.

### Weaknesses
The paper is closely related to a long line of recent papers and does not differentiate itself clearly to show the size of the technical contribution in the work.  This leads to some questions detailed in the next section.  

Given the discrete time results in the literature, one may hope that the assumption of a known stabilizing controller would not be needed for the online control algorithm.  This assumption has been removed in the discrete-time setting (e.g. in Kargin, Lale, et al Thompson Sampling Achieves $O(\sqrt{T})$ Regret in Linear Quadratic Control and the papers that follow that work.  

Section 5.2 provides a detailed comparison to the line of work of Faradonbeh et al.  There is clearly a difference, however the delta does not seem to be large.  They previous work uses a slightly stronger assumption and the algorithm is different.  Removing the annoying log factor is a clear contribution, but the technical and algorithmic contribution is not as clear. 

The results in the case where a stabilizing controller is not known are weaker than the other two main contributions.  They do not seem to provide a practical algorithm or novel technical tool.  

Empirical evaluation of the proposed algorithms is not provided. Such results would strengthen the impact of the theory.

### Questions
What are the major technical challenges in continuous time (or in your reduction) when transitioning results on control of discrete time systems without an initial stabilizing controller to continuous time? 

Beyond the novel discretization, what technical challenges (and novel technical ideas) where needed when adapting the discrete time tools to continuous time?

### Soundness
3

### Presentation
2

### Contribution
3
