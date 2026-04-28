# Divide and Conquer: Provably Unveiling the Pareto Front with Multi-Objective Reinforcement Learning

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3

## Abstract
We introduce a novel algorithm for learning the Pareto front in multi-objective Markov decision processes. Our algorithm decomposes learning the Pareto front into a sequence of single-objective problems, each of which is solved by an oracle and leads to a non-dominated solution. We propose a procedure to select the single-objective problems such that each iteration monotonically decreases the objective space that possibly still contains Pareto optimal solutions. The final algorithm is proven to converge to the Pareto front and provides an upper bound on the distance to undiscovered non-dominated policies in each iteration. We introduce several practical designs of the required oracle by extending single-objective reinforcement learning algorithms. When evaluating our algorithm with these oracles on benchmark environments, we find that it leads to a close approximation of the true Pareto front. By leveraging problem-specific single-objective solvers, our approach holds promise for applications beyond multi-objective reinforcement learning, such as in pathfinding and optimisation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes IRPO, which transforms multi-objective optimization problems into a series of single-objective optimization problems. It iteratively selects reference points and simplifies the search space based on the solutions optimized by RL. The effectiveness of the method is demonstrated both experimentally and theoretically in this paper.

### Strengths
1, The idea presented in this paper, as far as I know, is innovative. The approach of decomposing the problem from the perspective of hypervolume and solving it gradually is inspiring to me. I believe this paper has the potential to become a work with long-term impact.

### Weaknesses
1. Despite the novelty of the idea, the major concern is that the experimental evidence in the paper is not sufficient to demonstrate the advantages of the method compared to other MORL algorithms. First, the benchmarks used are relatively simple, and there are no experiments on complex multi-objective tasks, such as the classic MO-MuJoCo tasks. Additionally, there is a lack of comparisons with relevant MORL baselines, such as Envelope [1], PGMORL [2], and Q-Pensieve [3]. The absence of experiments on more complex, continuous control tasks, and the lack of comparison to state-of-the-art MORL algorithms, significantly limits the impact of the empirical results.
2. Further improvements are needed in the presentation of the paper. For instance,  the definitions in Chapter 4 could be introduced in Chapters 2 and 3, rather than gradually unfolding them within later sections. The current structure makes it difficult to follow the core concepts and their relationships. The delayed introduction of key definitions hinders the reader's understanding of the method's mechanics.
3. I strongly recommend the authors to include pseudocode in the main text. The lack of pseudocode makes it difficult to understand the precise implementation details and to reproduce the results. The absence of a clear algorithmic description is a significant barrier to the adoption and further development of this method.

### Questions
1. What are the advantages of IRPO compared to directly using RL for multi-objective optimization? For example, I could scalarize the multi-objective rewards directly and optimize them. I could use Envelope [1] to train one policy to solve all tasks, or get a set of policies through PGMORL [2].
2. Could the authors provide a performance comparison between IRPO and other MORL algorithms on MO-MuJoCo?
3. What do "occupancy measure" and "occupancies" mean in Section 3.2.1? An introduction is lacking.
4. How long does the RL optimization process before pruning take? More detailed training specifics are needed.

If the authors can address my concerns, I am willing to increase my score.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a way to discover the Pareto front of Multi-objective RL (MORL) problems. The authors use the augmented Chebyshev scalarisation function as the achievement scalarising function (ASF), converting a multi-objective problem into a single-objective one. They introduced the Pareto oracles (the weak and the approximate ones) into MORL. With the Pareto oracles in hand, they propose Iterated Pareto Referent Optimization (IPRO), which learns the Pareto front in 3 phases: (i) The main loop consists of iteratively updating the Pareto front by interacting with the Pareto oracle. (ii) The return value from the Pareto oracle can be used to update the Pareto front while maintaining the lower set L and upper set U. Finally, they theoretically give an upper bound on the approximation error and a guarantee to converge to a \tau-Pareto front. The proposed algorithm is then evaluated on multiple benchmark MORL environments, including DST, Minecraft and MO-Reacher.

### Strengths
- This paper introduces a new concept called Pareto oracle into MORL, which can be implemented with modifications of single-objective RL algorithms, and thereby proposes IPRO, a new MORL framework that iteratively finds the Pareto optimal policies with the help of Pareto oracles. 

- This paper then provides upper bounds on the true approximation error at each time step and gives a convergence guarantee of their proposed algorithm IPRO.

### Weaknesses
 - My main concern is that the proposed IPRO framework completely ignores one core problem of RL (and hence MORL) -- sample efficiency. Specifically, IPRO completely abstracts away the "learning from online interactions" aspect of RL through the use of Pareto oracles, which are assumed to be capable of directly returning a Pareto optimal policy given any reference point. However, this is actually the fundamental challenge of RL (and surely MORL as well). If the complexity of "learning from online interactions" is completely encapsulated into an oracle, then the problem would simply degenerate to a typical Multi-Objective Optimization (MOO) problem and then there is no need for reinforcement learning (That also manifests why the experimental results are all shown in terms of iterations, not in number of samples). With that said, the IPRO appears more like just an MOO algorithm rather than an MORL method (as it is agnostic to the specific problem structure of RL).

- Several algorithmic components are stated without much explanation and hence rather confusing. For example:
    - Regarding the practical implementation of a Pareto oracle, a Pareto oracle could be achieved by taking the augmented Chebyshev scalarisation function as the objective under any off-the-shelf RL algorithm (e.g., DQN, A2C, etc). Notably, the augmented Chebyshev function depends not only on the reference point but also  $\lambda$ and $\rho$, which are the weight vector and the augmentation coefficient that determine the required improvement of each dimension. The choices of $\lambda$ and $\rho$ are critical in determining which Pareto optimal solution we are looking for (similar to the preference vector in linear scalarization). However, in IPRO, it is not explained (either in the main text of the pseudo code in Appendix) how these parameters are determined in each iteration. 
    - IPRO, how shall we construct the sets $L$ and $U$?
    - What has been done in the Pruning phase? And how does Pruning uncover additional Pareto optimal solutions?
    - How is the memory-based policy implemented? Is there any special neural network architecture involved?

- The experimental results do not appear strong enough to demonstrate the performance of IPRO. Several MORL benchmark methods are missing in the experiments. Just to name a few:
    - PGMORL (Xu et al., ICML 2020) uses an evolutionary approach to search for the Pareto front and shall be a good baseline for IPRO.
    - Envelope Q-learning (Yang et al., NeurIPS 2019) and (Abels et al., ICML 2019) provide single-network solutions to approach the convex coverage set.
    - More recently, (Basaklar et al., ICLR 2023) and (Hung et al., ICLR 2023) also provide single-network solutions to MORL.

Moreover, the experimental results are all reported in terms of iteration, which does not reflect the actual sample efficiency of the algorithms.

- The presentation could be improved in several places. For example, in Section 2 and Section 3, while the preliminaries and definitions are mostly fairly standard definitions and concepts in MORL, I do find the description to be somewhat lengthy and hence a bit hard to read.

### Questions
Some additional detailed questions:

- What are the definitions of “nadir” $v^n$ and “ideal” vector $v^i$ in Figures 1 and 2? (They seem to be some uniform lower bound and upper bound of all possible return vectors?)

- What is the reason behind the design of a* in eq (3)? Is this design theoretically grounded?

- I notice that in Fig 3(e), the coverage of DQN as Pareto oracle is generally higher than the other two while the hypervolume of DQN as Pareto oracle is the lowest in Fig 3(b). Why is that the case?

- What is the main usage of Section 3.2.1? Is the stochastic stationary policy used in the implementation?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides a framework for learning the Pareto front in multi-objective MDPs. The framework decomposes the learning problem into a series of single-objective problems, where each problem is solved by a Pareto oracle. Specifically, the IPRO algorithm iteratively proposes reference points to a Pareto oracle and gets new Pareto optimal points which trim sections from the search space. The algorithm is shown to converge to the Pareto front asymptotically. The paper also contains experiments that validate that the algorithm leads to a close approximation to the true Pareto front.

### Strengths
- The problem of learning the Pareto front in MOMDPs is general and is important in practice.

- The proposed algorithm is natural and novel.

- The theoretical guarantee looks sound.

### Weaknesses
 - The presentation is not good enough. The major contribution of this paper is the algorithmic framework IPRO and the guarantee Theorem 4.2. However, the paper introduces IRPO on page 6 while stating Theorem 4.2 on page 8. For example, Section 3.2.1 - 3.2.2 is irrelevant to the main result and should be presented later. Moreover, the absence of the algorithm box of IPRO hinders my understanding.

- See the question part.

### Questions
1. How do you select the reference point $l$ from the set of lower points $L$ if there are many candidates?

2. Since the convergence is only asymptotic, how do you show the advantage of your method theoretically? For example, one can optimize a weighted sum utility each time, and the weights are sampled uniformly. This method can also converge to the Pareto front asymptotically.

3. Following 2, is it possible to characterize the convergence rate?

4. What is the big difference between a weak Pareto oracle and an approximate Pareto oracle in practice? Is it only for theoretical rigorousness?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a new algorithm for multi-objective reinforcement learning. The main idea is to construct a Pareto oracle which can be queried iteratively to shrink the search space of Pareto optimal points. The authors provide theoretical analyses of the convergence properties of the proposed algorithm and experiment with three standard multi-objective optimization environments.

### Strengths
1. Multi-objective reinforcement learning is an important problem to study. This paper adds a new method to the collection of MORL algorithms. The proposed Iterated pareto Referent Optimization (IPRO) algorithm is interesting in its three phases and is relevant to the community.

2. I appreciate the authors providing theoretical analyses of IPRO, though I have some questions about their presentations. Please see my questions in the Questions section.

### Weaknesses
1. There are some important baselines that need to be included, for example [1] and [2]. Furthermore, comparisons with GPI-LS did not demonstrate any improvements. I think that the authors should provide more discussion on this. It is hard to see why one would want to use IPRO over an existing method.

[1]: Yang, Runzhe, Xingyuan Sun, and Karthik Narasimhan. "A generalized algorithm for multi-objective reinforcement learning and policy adaptation." Advances in neural information processing systems 32 (2019).

[2]: Abels, Axel, et al. "Dynamic weights in multi-objective deep reinforcement learning." International conference on machine learning. PMLR, 2019.

2. The presentation of the paper could use a major improvement. There are several places where definitions are either missing or unclear, making the paper hard to understand. The IPRO algorithm is described in words only in the main paper. I think Algorithms 1 and 2 in the Appendix should be included in the main paper to improve the clarity. Please see my comments in the next sections about other places for clarification.

3. This may be a point I did not understand entirely due to the presentation issue. In Section 3.2, in describing the design of a Pareto oracle, the authors mentioned using GGF-DQN to optimize the objective function in Equation (1). My question is: what is the benefit of utilizing another multi-objective algorithm as a subroutine in IPRO compared to directly using it to optimize the multi-objective function?

### Questions
1. In Theorem 4.1, does one need to place some assumptions on the Pareto oracle to claim this result?

2. IPRO needs to find the ideal and nadir vectors for initialization. In practice, even the reduced single-objective RL problem might not be solved to optimality. How does this fact impact the performance of IPRO?

3. In the definition of Achievement scalarizing functions (Section 2), please explain how $s$ becomes $s_r$ depending on $r$.

4. Please define what a target region is. It is first mentioned in the paragraph about Achievement scalarizing functions in Section 2.

5. In the Problem setup (Section 2), please define the expected return value $v^{\pi}$ rigorously.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
