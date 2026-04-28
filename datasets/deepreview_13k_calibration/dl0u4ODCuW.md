# Retro-fallback: retrosynthetic planning in an uncertain world

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Retrosynthesis is the task of planning a series of chemical reactions
to create a desired molecule from simpler, buyable molecules.
While previous works have proposed algorithms to find optimal solutions for a range of metrics
(e.g.\@ shortest, lowest-cost),
these works generally overlook the fact that we have imperfect knowledge of the space
of possible reactions, meaning plans created by algorithms may not work in a laboratory.
In this paper we propose a novel formulation of retrosynthesis in terms of stochastic processes
to account for this uncertainty.
We then propose a novel greedy algorithm called retro-fallback which maximizes
the probability that at least one synthesis plan can be executed in the lab.
Using \textit{in-silico} benchmarks we demonstrate that retro-fallback
generally produces better sets of synthesis plans than the popular MCTS
and retro* algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an algorithm for retrosynthetic planning named Retro-Feedback.
The algorithm is tested on a benchmark problem and achieved improving
performance compared with existing algorithms, including Retro* and MCTS.

### Strengths
- The algorithm is described in detail.

- The improving performance on the benchmark problems.

- Proposed a novel measure of successful synthesis probability (SSP) for retrosynthesis.

### Weaknesses
 - The reviewer has several questions explained in the Questions below.

### questions:
 1. On page 4.
"... while algorithms like breadth-first search or proof-number search (Kishimoto et al., 2019) have no customizable rewards or costs of any kind."
In Section 5.
"In fact, if costs are defined to be negative log probabilities then the updates for ψ and ρ are essentially equivalent to the “reaction number” and “retro* value” updates from (Chen et al., 2020)."
The reviewer could not find the key difference between retro-fallback and the two existing algorithms, DFPN-E [Kishimoto+ 2019] or Retro* [Chen+ 2020].
If we use the negative log probabilities as the proof or disproof number, retro-feedback, Retro*, and DFPN-E seem very similar.
Probably, the reviewer did not understand what this sentence meant.
"The key difference is that retro-fallback performs parallel updates..."
What does "parallel" mean in this case?
Could the authors elaborate on this part?

 2. The reviewer might have misunderstood something, but the problem described in Section   4.1 could easily avoided if the authors used a hash table for implementing the search algorithms.
(Using a hash table is a standard technique for proof-number search.)
If a hash table is used, a cycle could be easily detected, so it is possible to avoid problems caused by the same molecule or reaction appearing multiple times in a path.

 3. P. 1.
"Although existing algorithms may find multiple synthesis plans, they are generally not designed to do so, and there is no reason to expect the plans found will be suitable as backup plans (e.g. they may share steps with the primary plan and thereby fail alongside it)."
The following paper proposes an AND-OR-tree-based search algorithm for retrosynthesis, which keeps enumerating (probably) all the synthetic routes one by one in the order of some preference.
> Shibukawa, R., Ishida, S., Yoshizoe, K. et al. CompRet: a comprehensive recommendation framework for chemical synthesis planning with algorithmic enumeration. J Cheminform 12, 52 (2020). https://doi.org/10.1186/s13321-020-00452-5

Minor comments.
 4. There is an older paper that proposes to use AND-OR tree search for retrosynthesis. Please consider referring to this paper.
> Heifets, A., & Jurisica, I. (2021). Construction of New Medicines via Game Proof Search. Proceedings of the AAAI Conference on Artificial Intelligence, 26(1), 1564-1570. https://doi.org/10.1609/aaai.v26i1.8331
https://ojs.aaai.org/index.php/AAAI/article/view/8331

 5. Is it reasonable to assume there is always only one product?

 6. P. 2. "tip nodes"
  In graph search terminology, I think this is called "frontier nodes".

### Questions
1. On page 4.
"... while algorithms like breadth-first search or proof-number search (Kishimoto et al., 2019) have no customizable rewards or costs of any kind."\
In Section 5.
"In fact, if costs are defined to be negative log probabilities then the updates for ψ and ρ are essentially equivalent to the “reaction number” and “retro* value” updates from (Chen et al., 2020)."\
The reviewer could not find the key difference between retro-fallback and the two existing algorithms, DFPN-E [Kishimoto+ 2019] or Retro* [Chen+ 2020].
If we use the negative log probabilities as the proof or disproof number, retro-feedback, Retro*, and DFPN-E seem very similar.\
Probably, the reviewer did not understand what this sentence meant.
"The key difference is that retro-fallback performs parallel updates..."\
What does "parallel" mean in this case?
Could the authors elaborate on this part?

1. The reviewer might have misunderstood something, but the problem described in Section   4.1 could easily avoided if the authors used a hash table for implementing the search algorithms.
(Using a hash table is a standard technique for proof-number search.)
If a hash table is used, a cycle could be easily detected, so it is possible to avoid problems caused by the same molecule or reaction appearing multiple times in a path.

1. P. 1.
"Although existing algorithms may find multiple synthesis plans, they are generally not designed to do so, and there is no reason to expect the plans found will be suitable as backup plans (e.g. they may share steps with the primary plan and thereby fail alongside it)."\
The following paper proposes an AND-OR-tree-based search algorithm for retrosynthesis, which keeps enumerating (probably) all the synthetic routes one by one in the order of some preference.
> Shibukawa, R., Ishida, S., Yoshizoe, K. et al. CompRet: a comprehensive recommendation framework for chemical synthesis planning with algorithmic enumeration. J Cheminform 12, 52 (2020). https://doi.org/10.1186/s13321-020-00452-5

Minor comments.
1. There is an older paper that proposes to use AND-OR tree search for retrosynthesis. Please consider referring to this paper.
> Heifets, A., & Jurisica, I. (2021). Construction of New Medicines via Game Proof Search. Proceedings of the AAAI Conference on Artificial Intelligence, 26(1), 1564-1570. https://doi.org/10.1609/aaai.v26i1.8331
https://ojs.aaai.org/index.php/AAAI/article/view/8331

1. Is it reasonable to assume there is always only one product?

1. P. 2. "tip nodes"
  In graph search terminology, I think this is called "frontier nodes".

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to find multiple retrosynthesis plans to cope with the uncertainty of infeasible reactions or non-buyable molecules. To achieve this goal, the paper first presents a evaluation metric SSP to quantify the probability of at least one synthesis plan can work (judged by a feasibility and buyability model), and further designs a retrosynthetic planning algorithm retro-fallback that can greedily expand molecules to maximizes SSP, specially when all existing synthesis plans currently fail.

### Strengths
1. The objective for addressing the uncertainty of infeasible reactions or non-buyable molecules is well-motivated and important in practice, and the paper laid out a clear and general formalism for this objective (e.g., feasibility, buyability, SSP);
2. The path from motivation to solution is well-paved, from trivial/straightforward solution to the proposed one, and discussed the connection to related work systematically;
3. The evaluation directly answers questions about the claims made by the paper.

### Weaknesses
1. While I appreciate the general formulation and systematic discussion about planning algorithms, given the existence of retro*, the novelty and advantage of this work (e.g., performing parallel updates using multiple samples) is not that obvious to me. I would encourage adding more discussion when talking about detailed method. Specifically, the paper should clarify how the parallel updates in retro-fallback lead to a different search behavior compared to the single cost function optimization in retro*. The advantage of optimizing SSP, which is a probability, over a scalar cost needs more elaboration, especially in the context of multi-step retrosynthesis where the interplay of reaction feasibility and buyability is complex.
2. Since this work focuses on multi-step retrosynthesis, related works [1] working on this should be discussed.

### Questions
1. How does Algorithm 1 generate multiple possible reaction graph for a target molecule? 
2. Algorithm 1 could generate plan that is not a valid plan, e.g., when the algorithm terminates, there are still tip nodes in G'. To take such cases into consideration, can the authors also evaluate performance using two other metrics: the success rate as in Retro*, and the set-wise exact match accuracy as in FusionRetro?
3. How sensitive the method is to the number of samples when computing line 4-6 in Algorithm 1?
4. It is interesting to see retro-fallback with transformer can be more computational efficient, and the authors elaborate more on that (e.g., how to combine both for improvement)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The submission has a clear description and clarifies that low-feasibility of retrosynthetic routes limit the real-world practicability in lab. The quantitative results and the comparison to prior methods may need to be clarified to support the statement of enhancing the generated route practicability.

### Strengths
1. This paper draws an insight to the unperfect reactions by the one-step prediction model and redefined the buyability of real-world molecules.

2. This paper uses a novel approach based on stochastic processes to solve the retrosynthetic problem.

### Weaknesses
1. More quantitative experimental results and baseline comparisons need to be clarified.

2. This paper has a solid motivation and a novel solution to perform the route planning but is limited by the proposed SSP metric. SSP attempts to calibrate the feasibility of chemical reactions. However, it will not perform better than a forward one-step prediction model since they are trained on the similar reaction dataset. Besides, SAScore is a trivial metric as it prefers unrealistic large carbon rings.

### Questions
The quantitative results seem not adequate enough to support the findings, could the author present more quantitative results?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
