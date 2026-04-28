# Improving Branching in Neural Network Verification with Bound Implication Graph

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 5, 6

## Abstract
Many state-of-the-art neural network verifiers for ReLU networks rely on Branch and Bound (BaB)-based methods. They branch ReLUs into positive (active) and negative (inactive) parts, and bound each subproblem independently. Since the cost of verification heavily depends on the number of subproblems, reducing the total number of branches is the key to verifying neural networks efficiently. In this paper, we consider \emph{bound implications} during branching - i.e., when one or more ReLU neurons are branched into the active (or inactive) case, they may imply that a set of other neurons from any layers become active or inactive, or have their bounds tightened. These implications can eliminate subproblems and improve bounds. We propose a scalable method to find implications among all neurons within tens of seconds even for large ResNets, by reusing pre-computed variables in popular bound-propagation-based verification methods such as $\alpha$-CROWN, and solving a cheap linear programming problem. Then, we build the bound implication graph (BIG) which connects neurons with bound implications, and it can be used by any BaB-based verifier to reduce the number of branching needed. When evaluated on a set of popular verification benchmarks and a new benchmark consisting of harder verification problems, BIG consistently reduces the verification time and verifies more problems than state-of-the-art verification tools.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel method named bound implication graph (BIG) to efficiently reduce the number of subproblems when verifying neural networks with the bound-and-branch techniques. The bound implication graph is constructed to capture the neuron dependencies with pre-computed estimated bound on each neuron and track the active/inactive status of the neuron given the branch status of the other neuron. The experiments demonstrate a significant reduction in verification time and an improvement in the tightness of bounds.

### Strengths
- The paper is sound and the topic of the paper is of high interest to the research community.
- The paper does a good job at introducing technical details and makes the paper easy to follow.
- As far as I know, the paper is the first to provide ways to efficiently reduce the branches for verifying neural networks by explicitly tracking the neuron dependencies as active/inactive states.
- The empirical study shows great improvement of the proposed method over existing verification algorithms in both verification time and verification results.
- Comprehensive ablation studies on the studied problems.
- The paper also provides a new dataset as VeriHard which contains instances that can only be solved using state-of-the-art verifiers with a long timeout.

### Weaknesses
 - More discussions on the bottleneck of the proposed method would further strengthen the paper.

### Questions
- Could you comment on how would the BIG can be used to discover hard adversarial examples or train the model to be robust against those examples?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes to leverage "bound implications" during neural network verification to reduce the number of explored branches in a BaB procedure. To this end, they construct a bound implication graph where each node corresponds to a positive or negative split of a formerly unstable neuron/ReLU and edges correspond to a split of the outgoing node implying a stabilization of the incoming node. They find these implications by evaluating the linear bounds on the implicated neuron, as computed during LiRPA, over the part of the specification compatible with a linear relaxation of the split of the implicating neuron. Enforcing these implied splits during BaB, improves verification performance on a wide range of tasks.

### Strengths
* The tackled issue of (certified) adversarial robustness is of high importance.
* To the best of my knowledge, this paper is the first to propose bound implications between arbitrary layers and among more than two neurons.
* Combining (sub)BIG with established BaB-based verification methods consistently improves their performance, in some cases significantly so.
* The novel VeriHard benchmark is not only useful for this work but also to benchmark further novel certification methods.
* The two-stage check for the potential of bound implication (Theorem 3.2) is elegant and helps to significantly reduce the computational cost for finding bound implications.

### Weaknesses
 * An important baseline, GCP (Zhang et al. 2022), the most recent version of $\alpha\beta$-CROWN, is missing from all comparisons. However the MILP constraints leveraged by this approach might be highly correlated to the bound implications described in this work. Thus, a direct comparison or even better combination with GCP would be essential to judge the marginal contribution of this work over state-of-the-art methods.  The lack of comparison to GCP is particularly concerning because the method builds upon $\alpha\beta$-CROWN, and it is unclear if the improvements stem from the bound implications or from a more efficient implementation of the underlying $\alpha\beta$-CROWN framework. Furthermore, without a direct comparison, it is difficult to assess whether the proposed bound implications offer a unique advantage over the cutting planes generated by GCP's MILP solver, which could potentially capture similar relationships between neurons. The experimental results should include a comparison of the number of branches explored by the proposed method and GCP, as well as the certified accuracy achieved by each approach, to properly evaluate the effectiveness of the bound implications.
* Clarity of presentation including copy writing (see some examples below) could be improved significantly.
* Significance of improvements on established benchmarks (less than $1\%$ is unclear). The improvements on established benchmarks are marginal, and it's unclear if these small gains are practically significant. The paper should provide a more detailed analysis of the cases where the proposed method shows improvement and the cases where it does not.  It is also important to consider whether the small improvements are due to the benchmark design itself, given that many instances in these benchmarks are already solved by existing methods. The authors should also discuss the limitations of the proposed approach and under which conditions it is expected to perform well or poorly.

### Questions
### Questions
1) Have you experimented with considering the bound implication as part of the split heuristic? E.g. adding the scores of implicated neurons to the implicating one.
2) Did you investigate the interaction of these bound implications with the general cutting planes from GCP (also based on beta-CROWN)? It seems like similar implications might be captured by the MILP solver used there.
3) Did you investigate the effect of how many implicating neurons $K$ you consider?
4) In Theorem 3.2, it seems like the two enumerated points add an additional (exhaustive) case distinction if Equation (7) holds, where the first one can be checked independently of the implicated neuron. I would consider moving them to a separate Corollary. What exactly does it mean for its “linear bounds to not have an intersection with C”? Is the first constraint (functionally) equivalent to $a x_0 + c + \epsilon ||a|| < 0 $, i.e. the lower bound will remain negative for any $x \in \mathcal{C}$? I believe the presentation of Theorem 3.2 could be improved significantly. In particular, it is not initially clear, that either of the two cases follows from Equation (7) rather than being additional constraints.

### Comments
* The scaling of the y-axis in Figure 2 is unclear making it hard to interpret. I would consider a linear scale instead.
* I believe it should be "(inputs $\leq$ 0)" for the "inactive" case in Section 1 paragraph 3.
* An illustration of Theorem 3.2 could help communicate the underlying intuition.

#### Typos
- Mn-BaB instead of MN-BaB in Section 1 paragraph 2
- Extra “the” in the third line of Section 2
- The second sentence after Equation (3) is broken and missing a full-stop.
- “Activate and inactive” third last line in Section 2

### Conclusion
The proposed idea of using a (sub)BIG to reduce the number of to be considered branches in BaB-based neural network verification is novel and seems effective. Further, the novel VeriHard benchmark might prove valuable for evaluating novel certification methods beyond this work. However, the lacking comparison to the important baseline GCP makes both its complementarity with and performance compared to current state-of-the-art methods unclear, preventing me from recommending (strong) acceptance

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper incorporates implication constraints for the states of the ReLUs into
branching mechanisms for branch-and-bound-based neural network verification. An
implication constraint between two ReLUs expresses that if one them is stable
in a state then the other one has to be stable in a state as well. The
constraints are computed from the  bound equations of the ReLUs  and are then
exploited in branch-and-bound frameworks to reduce the total number of
branches that need to be explored.

### Strengths
The paper adapts notions from previously developed notions [1, 2] to
branch-and-bound frameworks and shows that they help improve verification
times.

### Weaknesses
1. The paper highly incremental to [1, 2].

2. It often presents several ideas as novel when they were first discussed in
[1, 2]. The following comments illustrate this weakness.
        
    a. While the experimental results from [1] clearly  show that implication
    constraints help with verification times,  the paper says "they were
    handled as constraints to a black-box MIP solver without validating their
    usefulness". 

    b. Bound implication graphs were previously constructed in [2], where they
    were precisely used to reduce the total number of branches. The paper
    however presents the implication graph as a novel aspect of the paper and
    does not reference [2].

    c. While the procedures computing the implication constraints in [1] are
    GPU-friendly the paper claims the opposite. Although they were used as MILP
    constraints in [1] and as a branching heuristic in [2], their
    identification relies only on matrix operations.  [2] discusses that they
    can be incorporated into any verifier with  a branching mechanism.

    d. The paper does not clarify with the introduction of the implication
    constraints that they were first introduced in [1].

3. The main novelty of the paper is the computation of the implication
constraints using bound equations (which are computed using previously
established methods) instead of the concrete bounds. The delta is small in my
opinion for an ICLR paper.

4. The implication constraint identification procedures are not compared with
the ones from [1]. It is not clear that they perform better. For instance [1,
2] show similar gains. Also, the procedures from [1] should be faster because
they deal with concrete bounds instead of bound equations.

### Questions
See comments above.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a procedure for eliminating infeasible sub-problems in branch-and-bound-based neural network verification procedures.

### Strengths
- The paper considers an important problem, verifying neural networks. 
- The paper introduces a new procedure that heuristically select a subset of neurons and keep track of their dependencies during the search, which can be used to remove sub-problems and tighten bounds. 
- The paper implemented the idea in $\alpha$-$\beta$-CROWN and obtained consistent performance gain on a set of robustness verification tasks. 
- The paper is well-written.

### Weaknesses
 - The paper only considers certifying adversarial robustness on perception networks.
- The general idea of removing sub-problems during case-analysis-based search by recording the dependencies between case splits has been considered in the past in the neural network verification setting, such as Planet. Therefore, the technical contribution of this paper is rather incremental and specific to $\alpha$-$\beta$-CROWN.

### Questions
- What is the actual perturbation bounds and perturbation dimensions on the VeriHard benchmark sets?
- Are the techniques described in the paper applicable beyond $\alpha$-$\beta$-CROWN, such as in NNV and Marabou?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
