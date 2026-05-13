# Safe Bayesian Optimization for Complex Control Systems via Additive Gaussian Processes

- Decision: Reject
- Scores: 6, 3, 1, 10

## Abstract
Controller tuning and optimization have been among the most fundamental problems in robotics and mechatronic systems. The traditional methodology is usually model-based, but its performance heavily relies on an accurate mathematical system model. In control applications with complex dynamics, obtaining a precise model is often challenging, leading us towards a data-driven approach. While various researchers have explored the optimization of a single controller, it remains a challenge to obtain the optimal controller parameters safely and efficiently when multiple controllers are involved. In this paper, we propose \textsc{SafeCtrlBO} to optimize multiple controllers simultaneously and safely. We simplify the exploration process in safe Bayesian optimization, reducing computational effort without sacrificing expansion capability. Additionally, we use additive kernels to enhance the efficiency of Gaussian process updates for unknown functions. Hardware experimental results on a permanent magnet synchronous motor (PMSM) demonstrate that compared to existing safe Bayesian optimization algorithms, \textsc{SafeCtrlBO} can obtain optimal parameters more efficiently while ensuring safety.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the authors propose a safe Bayesian optimization framework utilizing Gaussian processes with additive squared exponential functions. The motivation for the new kernel function is the poor performance of the "standard" SE kernel for high-dimensional spaces. The authors argue that using BO for controller tuning often requires operating in high-dimensional spaces due to a large number of parameters of the controllers to be considered. It is experimentally evaluated that the proposed algorithm, SafeCtrlBo, can lead to better results than other safe BO algorithms. Furthermore, the authors present theoretical results on the finite-time convergence of the algorithm.

The main contribution is utilizing additive SE-kernels in a Bayesian optimization framework and proofing the finite-time convergence.

UPDATE: score raised

### Strengths
- The paper addresses an important problem of (safe) BO, which is the limitation to low-dimensional problems. 
- Using additive kernel functions in a safe BO setting to increase its performance in high dimensional problems seems, to the best of my knowledge, a novel idea. The results indicate that this approach can be superior to "standard" safe BO approaches for some systems. 
- To the best of my knowledge, the math seems to be sound and the proofs are correct.

### Weaknesses
1. The main motivation for introducing the new kernel function is its superior in high dimensions. However, all evaluations in the paper are still pretty low-dimensional, with dimensions up to 10. In fact, in the related work it is mentioned that existing safe BO approaches work with systems where "three controller [...] each controller having only two parameters". However, the proposed algorithm is experimentally evaluated on the exact same numbers of parameters.

2. I agree that controller tuning including many parameters can be tricky. However, cascaded controllers are a bad example of that. In practice, these structures can be tuned very efficiently as you start with the inner loop until a specific performance is reached, then the next loop, and so on. All parameters are very meaningful, and the process is quite transparent. Furthermore, 
motor controllers are a bad example for safe BO. As long as no load is attached to the motor (something you don't do for tuning the controllers), it is almost impossible to destroy the system. Typical amplifiers do have a "max current" setting, or it is simply defined in the software. Therefore, I cannot understand the safety concerns that the authors mentioned for the experiment.

Long story short: Although the adapted safe BO method sounds interesting, the motivation with cascade controllers and the experimental evaluation are not a good choices.

### Questions
1: Can you include an experiment with a truly high-dimensional system? 

2: As mentioned in the weakness section, I think cascade controllers are not a good example. I suggest something like distributed controllers in large water/power networks. Could you test the algorithms on more complex systems?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propse a novel algorithm for safe Bayesian optimization that exploits purported properties of the squared-exponential kernel to facilitate the expansion of the safe set. The proposed idea is interesting and the authors report good theoretical results. However, the theoretical exposition is poor and the corresponding proofs are either incomplete or incorrect. Though I recommend rejection for this reason, I am open to changing my score if the authors improve the paper accordingly.

### Strengths
The paper is well-motivated and written in a very clear form. It also provides an adequate review of related works. The proposed algorithm is an interesting contribution and shows good empirical results.

### Weaknesses
The theoretical results are mostly stated usinng plain text instead of mathematical formulas, which makes them somewhat ambiguous and hard to understand at times.

The proofs of the theoretical results are incomplete and potentially wrong.

The statement "Srinivas et al. (2010) demonstrated that BO methods can converge to the global optimum of unknown performance functions in fewer steps compared to genetic algorithm." is incorrect. Nothing in the paper compares their approach to a genetic algorithm, and there is no discussion on this.

Similarly, the statement "However, SAFEOPT uses Gaussian kernels as the covariance function of the Gaussian processes, which is effective mainly for low-dimensional problems (Bengio et al., 2005)" is inaccurate. Berrkenkamp et al. (2016) use a Matern kernel and there is nothing in Sui et al. (2015) that indicates that a squared-exponential kernel is necessary.

Is equation (1) correct? Shouldn't the last term have t in the subscript instead of k? The same holds for equation 2.

I feel that theorems 4.1 and 4.2 are mostly trivial and should be placed in the appendix.

Does line 5 in the pseudocode simply mean that the algorithm picks the point with maximal variance in B_n? If so, why not just write sigma insteadl of un-ln?

The presentation of outermost evaluated safe points is somewhat confusing. Is a_{oes} in the dataset? Would it help to introduce the data set \mathcal{D}_n and to write a_{oes} \in \mathcal{D}_n?

Theorems 5.1 and 5.2 are unclear to me. What do the authors mean by the "maximum allowable uncertainty for the exploration to converge to an ( \epsilon )-reachable safe region." and "Maximum allowable uncertainty for the performance function to converge to a ( \zeta )-optimal function value."?

In the proof of Lemma C.1, the step from line 878 to 880 is incomplete. To show that the posterior variance is indeed increasing, the authors also need to show that [K_t^{-1} k_t(x)]_i is positive, which the authors do not do.

I might have missed something, but I am not sure if the statement in line 894 holds. Take, for example, the points x_sb =1, x_oes = 0 and x_i = 10. For \lambda=0, we have || x(\\) - x_i ||_2 = 10 > || x_sb - x_oes||_2 = 1, yet the inner product (x(\\) - x_i ) (x_sb-x_oes)  = (0-10 ) (1-0) <0 is negative.

### Questions
The statement "Srinivas et al. (2010) demonstrated that BO methods can converge to the global optimum of unknown performance functions in fewer steps compared to genetic algorithm." is incorrect. Nothing in the paper compares their approach to a genetic algorithm, and there is no discussion on this.

Similarly, the statement "However, SAFEOPT uses Gaussian kernels as the covariance function of the Gaussian processes, which is effective mainly for low-dimensional problems (Bengio et al., 2005)" is inaccurate. Berrkenkamp et al. (2016) use a Matern kernel and there is nothing in Sui et al. (2015) that indicates that a squared-exponential kernel is necessary.

Is equation (1) correct? Shouldn't the last term have t in the subscript instead of k? The same holds for equation 2.

I feel that theorems 4.1 and 4.2 are mostly trivial and should be placed in the appendix.

Does line 5 in the pseudocode simply mean that the algorithm picks the point with maximal variance in B_n? If so, why not just write sigma insteadl of un-ln?

The presentation of outermost evaluated safe points is somewhat confusing. Is a_{oes} in the dataset? Would it help to introduce the data set \mathcal{D}_n and to write a_{oes} \in \mathcal{D}_n?

Theorems 5.1 and 5.2 are unclear to me. What do the authors mean by the "maximum allowable uncertainty for the exploration to converge to an ( \epsilon )-reachable safe region." and "Maximum allowable uncertainty for the performance function to converge to a ( \zeta )-optimal function value."?

In the proof of Lemma C.1, the step from line 878 to 880 is incomplete. To show that the posterior variance is indeed increasing, the authors also need to show that [K_t^{-1} k_t(x)]_i is positive, which the authors do not do.

I might have missed something, but I am not sure if the statement in line 894 holds. Take, for example, the points x_sb =1, x_oes = 0 and x_i = 10. For \lambda=0, we have || x(\lambda) - x_i ||_2 = 10 > || x_sb - x_oes||_2 = 1, yet the inner product (x(\lambda) - x_i ) (x_sb-x_oes)  = (0-10 ) (1-0) <0 is negative.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper addresses safe Bayesian optimization (BO) to optimize the parameters of cascaded control systems. To make safe BO more suitable for this task, additive kernels are used as a model, and a new definition of expander sets is introduced, which makes the BO optimization more compute efficient. The method is benchmarked on synthetic functions and a hardware setup, tuning parameters for a field-oriented control algorithm in a permanent magnet synchronous motor. Although the proposed method outperforms other benchmarks, all tested safe BO methods result in safety constraint violations.

### Strengths
(S1) Clear motivation and objective 

(S2) Demonstration and benchmarking of  different safe BO algorithms on synthetic function and in a real-world use case. The application of multiple algorithms as baselines makes the results significant for the BO community. 

(S3) The provided implementation gives clear insights into the method and the experiments. 

In general, the contribution is reasonable. Focusing on the border of the safe set to reduce computational effort is a logical approach. Additive kernels seem to be able to enhance the performance of safe BO algorithms for high-dimensional systems. However, it remains unclear how to choose kernel hyperparameters in practice.

### Weaknesses
I see the following main weaknesses:

(W1) The embedding of related work is insufficient. There are lines of work, which seem closely related, but are not cited appropriately.

(W2) Theoretical results are partially imprecise. Some of the results have been known before and build on previous results, yet these are not cited.

(W3) In the empirical study, information is missing on how to apply the algorithm and how hyperparameters are chosen. The choice of heuristics is not sufficiently documented and discussed.

(W4) Safety violations in hardware experiments are not adequately discussed.

Below, I provide a more detailed discussion of these weaknesses, ordered by sections.


## Related work:

* In related work, Bottero et al. 2022 is missing. It would make sense to compare against this, as this work explicitly focuses on safe BO without expander sets. 
* Furthermore, studies on safe/constrained BO for cascaded control systems, such as Khosravi et al. 2022, seem directly related but are not mentioned. 


## Theoretical Results: 

* Lemma 4.1 is a known result that can be found in e.g., Berlinet and Agnan-Thomas 2004 Theorem 5
* Theorem 4.2 is imprecise; further information on this can be found in Fiedler 2023 (Section 4) 
* The theoretical results section clearly builds on Chowdhury and Gopalan 2017, Theorem 2, using their results for confidence bounds without referencing this paper.  
* There are more recent results on confidence bounds in GP Regression, which lead to more conservative bounds and do not rely on the information gain. Information on this can be found in Whitehouse et al. 2024
* Theorem 5.1: The RKHS norm of the safety functions is bounded by $B$ , not the safety functions themselves

## Empirical Study 

For the stage-wise approach it is unclear, when to go to the next stage. This can only be chosen through a heuristic. In the paper it remains unclear, how to choose this in a practical application. 

In the synthetic experiments, only a noise free setting is evaluated. The results would be more relevant and would underline the contribution of the method more, if function evaluations would be noisy. In addition, this setting would also better represent real-world settings. 

In the experimental evaluation, the choice of hyperparameters of the GP and the choice of $\beta$ is unclear. While in the theoretical derivations, the RKHS-norm bound and the information gain are used, in the experiments, $\beta = 2$ is used as a heuristic. This choice is common in other safe BO works; however, it is not made transparent in the paper and can only be found in the implementation. The use of this heuristic invalidates all proven safety guarantees. A detailed discussion on this can be found in Fiedler et al. 2024.

The choice and the long lengthscales in the kernel lead to safety violations. Typically, shorter lengthscales compared to the domain size are applied in safe BO applications. This limits performance while exploring but can lead to fewer safety violations. 
It would be interesting to know when safety violations occurred in the hardware experiments. I assume this is mostly in the first exploration stage.

For the hardware experiments, it is unclear what $T_0$ is and if there is even a switch in the exploitation stage. 

## Discussion

The safety violations that occur in the empirical results need to be more thoroughly discussed. In light of these, the claim in the conclusion that it "can be seamlessly integrated into real-world complex control applications." is too confident, having observed 39 safety violations in the hardware experiments. 


## Minor comments: 

Line 191 and 194: Definitions of safe set and expander sets in Sui 2015 and Sui 2018 are different
Line 206-207: This statement is wrong. Berkenkamp 2016 uses a Matern kernel; generally, in many SafeBO applications Matern kernels with $\nu = 3/2$ are used.
Line 333: Typo: Lipschitz continuous
Line 317-318: Grammar in Theorem 5.1 and Theorem 5.2 "with R-sub-Gaussian"

### Questions
Please address the mentioned weaknesses. 

Additional questions on the hardware experiments: 
- When does the exploration phase stop, when does the exploitation phase start?
- How were the GP hyperparameters chosen? 
- Why and when do safety violations occur?
- How can $T_0$ be chosen in real-world applications?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
2

### Summary
The paper describes a method for safe Bayesian optimization suitable for control applications where safety concerns limit the set of parameters that can be tried. The main contribution is the use of additive kernels in safe BO, resulting in faster optimization. This contribution is of major significance when applying BO to physical systems, where control trials are slow and costly to perform. A second contribution is the speedup of the computation of the expander set, affecting the computational time of the algorithm. The proposed method has been verified on benchmark functions in simulation, as well as on a challenging control problem involving a physical set-up consisting of nested controllers regulating the velocity of a permanent magnet synchronous motor under field-oriented control.

### Strengths
The proposed method for using additive kernels in safety-aware BO leads to optimization in fewer trials, which is of great practical significance for physical control systems with safety limitations. The paper is written clearly, references prior work in the field, and explains very well the connections of the proposed method to that work. Although safe BO and additive functions are not novel ideas individually, their combination is original and based on significant technical insight. Properties of the proposed additive kernels are analyzed well theoretically. A novel acquisition function is proposed that is faster to compute than previously proposed ones. 

Furthermore, the method is tested on a physical control system set-up that is of real practical use. Because the optimized parameters of the controllers are their proportional and integral gains, the proposed method could potentially find widespread use in industrial practice, where the use of PI controllers is very common and their tuning is known to be notoriously tricky and laborious.

### Weaknesses
The paper is somewhat incremental in the line of research on applying BO to safety-constrained control systems, and combines known ideas. Nevertheless, this combination required a significant technical insight, so it is far from obvious or trivial.

The experimental results on the physical system resulted in a significant number of constraint violations (39 for the method proposed by the authors). It is not clear what the consequences of these violations are in practice.

### Questions
What are the consequences of violations of constraints in this test application? Do they make the algorithm unsafe for use in practice? Is there a parameter that can be changed to reduce the number of violations? Does that result in a trade-off between performance and number of constraint violations, and if yes, how can this trade-off be handled?

### Soundness
4

### Presentation
4

### Contribution
4
