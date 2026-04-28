# Deep Learning Algorithms for Mean Field Optimal Stopping in Finite Space and Discrete Time

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 6, 5

## Abstract
Optimal stopping is a fundamental problem in optimization that has found applications in risk management, finance, economics, and recently in the fields of computer science. We extend the standard framework to a multi-agent setting, named multi-agent optimal stopping (MAOS), where a group of agents cooperatively solves finite-space, discrete-time optimal stopping problems. Solving the finite-agent case is computationally prohibitive when the number of agents is very large, so this work studies the mean field optimal stopping (MFOS) problem, obtained as the number of agents approaches infinity. We prove that MFOS provides a good approximate solution to MAOS. 
We also prove a dynamic programming principle (DPP), based on the theory of mean field control.
We then propose two deep learning methods: one simulates full trajectories to learn optimal decisions, whereas the other leverages DPP with backward induction; both methods train neural networks for the optimal stopping decisions. We demonstrate the effectiveness of these approaches through numerical experiments on 6 different problems in spatial dimension up to 300.
To the best of our knowledge, this is the first work to study MFOS in finite space and discrete time, and to propose efficient and scalable computational methods for this type of problem.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work focuses on optimal stopping of stochastic processes in the multi-agent setting. 
Prior work on optimal stopping: 
1. provided deep learning approaches in the single-agent case, 
2. extended the optimal stopping problem in the multi-agent case, referred to as multi-agent optimal stopping (MAOS).

Furthermore, as the MAOS problem complexity increases with the number of agents $N$, prior work:

3. has combined MAOS with mean-field approximation where $N\to\infty$ in the continuous time and continuous space setting.


This work builds on these approaches in that it considers a mean-field approximation for MAOS as in (2,3), but aims to develop computational methods as in (1).

It introduces two deep learning methods to efficiently find solutions, proving the approach efficient with experiments on high-dimensional problems.

### Strengths
- Proposes two deep learning methods that leverage trajectory simulation and backward induction for optimal stopping.
- Empirical validation: demonstrates the effectiveness of the methods through experiments on high-dimensional problems

### Weaknesses
## Lacking explanation of the motivation
The introduction does not give a motivating multi-agent example or explain examples of what kind of problems this work will allow to solve. 
I also did not understand by reading the introduction why the results (and deep learning approaches) from the single-agent setting do not extend to the multi-agent setting. The introduction should emphasize the main challenges for the extension.

## Writing

*Title*. This paper is about a multi-agent setting extension, and the title does not even mention that.

*Abstract*.
- starting with "optimal stopping of stoch. processes" would be clearer, because there are other studied stopping criteria
- I couldn't tell what the DPP proof implies. Perhaps describe what it implies for MFOS without assuming the reader knows DPP and its implications.

*Introduction*. The problem of the paper is very vague while reading the introduction. It would be helpful to provide a simple multi-agent optimal stopping motivating example so that ML readers can understand for which type of problems this problem is relevant.


*Other.*
- In the listed contributions it is unclear if (1) is for the discrete or the continuous case.

### Structure
The results are not in a separate section, making it hard to understand the contributions vs. the background. Section 2 contains existing models and subsection 2.4 gives one of the main theorems.

### Minor
- line 100: the text in brackets is unclear, do you mean the net's input can be up to 300? How was this determined?
- lines 108-109. At this point, only $N$ is introduced, but you use $\delta, X, k, \alpha$, etc. Moreover, this notation cannot be found later in the paper. 
- lines 116-118: It is weird that you first define  $P(\mathcal{X})$ and later $\mathcal{X}$.
- line 125: $\delta$ is not defined.
- line 126: typo mathds-$N$ should be $N$?
- line 133: missing 'is' (which is)
- line 139: write what is the expectation over in eq. (2)

### Questions
1. Regarding prior MAOS work, precisely how does the problem complexity increase with N? 
2. From the two proposed Deep Learning approaches, which one is better (or in which case which one is better)?
3. Could you elaborate on how the deep learning approaches for discrete-time single-agent case OS problems (listed in line 84) differ from the approach taken here on a per-agent basis? 
4. I do not understand what you mean by "this makes the problem time inconsistent" in line 170. I understand that Markovian is comp. efficient, but do not understand why otherwise is "time inconsistent".
5. How does the extended state in Eq. (5) differ from Talbi et al. (2023)?
6. Since Eq. (5) is for a representative player, how does it differ from the singe-agent setting? Why is the most complex step in extending the single-agent results to the multi-agent setting? (with mean field)

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This papers designs a mean field approximation method for solving multi-agent optimal stopping (MAOS). Theoretical justifications are provided establishing that the mean field approximation error is relatively small as number of agents goes to infinity. A dynamic programming principle is also established. Two algorithms are designed with neural networks modeling the policy functions. Adequate numerical experiments are provided.

### Strengths
1. The paper is overall clear and well-written.
2. The idea is innovative.
3. Solid theoretical results are shown with practical interpretations.
4. Adequate numerical experiments are conducted for the proposed algorithms.

### Weaknesses
I agree with the limitations discussed by the authors in Sec 6. Other than that, having some specific problem as an example in the first few sections could further improve readibility.

### Questions
1. Is the intuition of Theorem 2.2 similar to Law of Large Numbers, in the sense that averaging the stop/continue of N agents starts to loose randomness as N gets larger? And the rate of 1 / \sqrt{n} could roughly be related to the rate of concentration for the average?
2. What is the structure of neural networks for the applications? I.e. some shallow fully connected layers, or are some specific architectures prefered?

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
This paper studies a special form of mean field reinforcement learning (RL), the mean-field optimal stopping problem (MFOS), where each agent can only choose to continue or stop. The authors prove that MFOS is a good approximation of the multi-agent optimal stopping problem (MAOS) and characterize the convergence rate as the number of agents tends to infinity. They also propose two algorithms for optimizing the policy in MFOS. The authors verify the effectiveness of their proposed algorithms in several numerical simulations.

### Strengths
The paper is well-structured and easy to follow because the authors provide sufficient background and motivations for the MFOS. The convergence rate concerning the number of agents (Theorem 2.2) should be a good contribution if it is the first theoretical result that characterizes the gap between multi-agent RL and mean field RL. However, I’m unsure if similar results exist in the literature on mean field RL. The proposed algorithms are natural and show a good empirical performance.

### Weaknesses
Problem setting: MFOS is a special class of mean field RL. The readers may wonder why this work's theoretical guarantees and algorithms cannot directly apply to general transition kernels and action sets.

Theoretical results: The $1/\sqrt{N}$ convergence rate in Theorem 2.2 is not fast enough if we consider the practical number of agents in target applications (e.g., the number of drones in a fleet in Example 6). But it is good to see that this convergence rate is tight.

Algorithms: A major limitation is that both algorithms, Direct Approach (DA) and Dynamic Programming (DP), need to know the exact mean-field dynamics $\bar{F}$ and take derivatives of this function.

Besides, the authors mention that DP is "A more ideal treatment" than DA in Line 325. However, I do not see any rigorous reasoning through time/memory complexity. The only practical reason might be the training memory size mentioned in Line 374. But even when T is large, it may be better to have a single time-dependent neural network (as required by DA) rather than training T in different neural networks (as needed by DP).

Experiments: The examples are all about synthetic environments with known transition probabilities.
Despite the above limitations, I still feel this work makes contributions that should be interesting to the audience in the field of multi-agent RL.

### Questions
I hope the authors can clarify whether similar convergence results like Theorem 2.2 exist in the literature of mean-field RL. If not, does the proof of Theorem 2.2 rely on the special structures of MAOS compared with general multi-agent RL?

Is the mean-field dynamics easy to learn/differentiate in real-world applications with a finite number of agents? Are the proposed algorithms robust to any estimation errors in the mean-field dynamics?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the mean field optimal stopping problem in finite space and discrete time. Theoretically, the authors show that as the number of agents N goes to infinity, the optimal cost converges to its mean field limit at a rate of $N^{-1/2}$. They also show the dynamic programming principle in this setting. Numerically, the authors propose two algorithms, one directly optimizes the objective, and the other leverages the maximum principle. The authors apply the algorithms on 6 examples to test the efficacy.

### Strengths
The numerical experiments are comprehensive, showing the effectiveness of the algorithm.

### Weaknesses
Part of the article is not clear enough. I have put details in Questions.
The notations in the paper are complicated and hard to track. For example, stopping corresponds to $\alpha=1$ and $A=0$, while $\alpha=0$ and $A=1$ refer to continuing the dynamic. This causes some confusion.

Page 3 line 156. You mention that “randomized stopping times for individual agents differ from the randomization of the central planner on policies”. Why are they different? What should a central planner be like?

Page 4. What is the space for a stopping probability p? Is it a sequence of T functions in x, with values in [0,1]?

In assumption 2.1, you assume the Lipschitz condition of $\bar{F}$ and $\Psi$. However, you did not specify the metric in the input domain, which makes the assumption ambiguous.

### Questions
Page 3 line 156. You mention that “randomized stopping times for individual agents differ from the randomization of the central planner on policies”. Why are they different? What should a central planner be like?

Page 4. What is the space for a stopping probability p? Is it a sequence of T functions in x, with values in [0,1]?

In assumption 2.1, you assume the Lipschitz condition of $\bar{F}$ and $\Psi$. However, you did not specify the metric in the input domain, which makes the assumption ambiguous.

### Soundness
2

### Presentation
3

### Contribution
2
