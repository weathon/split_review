# Understanding Constraint Inference in Safety-Critical Inverse Reinforcement Learning

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
In practical applications, the underlying constraint knowledge is often unknown and difficult to specify. To address this issue, recent advances in Inverse Constrained Reinforcement Learning (ICRL) have focused on inferring these constraints from expert demonstrations. However, the ICRL approach typically characterizes constraint learning as a tri-level optimization problem, which is inherently complex due to its interdependent variables and multiple layers of optimization.
Considering these challenges, a critical question arises: *Can we implicitly embed constraint signals into reward functions and effectively solve this problem using a classic reward inference algorithm?* The resulting method, known as Inverse Reward Correction (IRC), merits investigation. In this work, we conduct a theoretical analysis comparing the sample complexities of both solvers. Our findings confirm that the IRC solver achieves lower sample complexity than its ICRL counterpart.
Nevertheless, this reduction in complexity comes at the expense of generalizability. Specifically, in the target environment, the reward correction terms may fail to guarantee the safety of the resulting policy, whereas this issue can be effectively mitigated by transferring the constraints via the ICRL solver. 
Advancing our inquiry, we investigate conditions under which the ICRL solver ensures $\epsilon$-optimality when transferring to new environments. Empirical results across various environments validate our theoretical findings, underscoring the nuanced trade-offs between complexity reduction and generalizability in safety-critical applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces the IRC solver to overcome the limitation of the IRL solver, which generally lacks a mechanism to leverage existing reward signals and may not be compatible with different rewards. The authors also give theoretical analysis and achieve a lower sample complexity. Besides, they also study and extend the transferability. The results of the experiments demonstrate its efficiency.

### Strengths
1. This paper is well-written and easy to follow.
2. The related work is well organized.
3. The authors give a strong theoretical. analysis of the advantages and shortcomings between IRC and ICRL solvers, i.e., convergence, and sample complexity. Besides, the authors clearly presented their theory contributions.

### Weaknesses
1. What are the wall-clock running times of your method and the other baselines in the experiments?
2. In Theorem 3.2, Can we have such that directly maximizing the cumulative rewards and considering the constrained optimization objective?
3. In B.8.2 subsection, Can we provide experimental results to evaluate the soft constraint scenario?

### Questions
Please see the weaknesses.

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
5

### Summary
The paper addresses the task of inferring safety constraints from expert demonstrations where the expert maximizes a known reward subject to unknown constraints. Although inverse constrained reinforcement learning (ICRL) has developed specialized methods for this task, recent work has shown that casting the problem into the framework of inverse reinforcement learning (IRL) via "inverse reward correction" (IRC) could offer advantages. This paper provides a deeper analysis of these claims, showing that:
1) Inverse reward correction can achieve better sample efficiency than ICRL for constraint inference;
2) The implicit constraints inferred through IRC, however, may transfer poorly across environments with different dynamics or reward structures compared to constraints explicitly modeled by ICRL; and
3) ICRL’s explicit constraint modeling offers conditions under which its inferred constraints allow for approximately optimal and safe policies when transferred to new environments, even under varied dynamics.

### Strengths
- the task of inferring unknown safety constraints is important
- the recent challenge that the field of ICLR with its growing literature may be redundant deserves further scrutiny, and the results in this paper add important nuance to this challenge, showing that such redundancy is not clear cut
- the paper shows potentially useful results relating inverse reward correction and ICRL that deserve a place in the literature

### Weaknesses
 - unfortunately, the presentation is bad, making deciphering the paper a painful challenge even to a motivated reader closely familiar with the work this paper builds on:
    - for me, this point alone currently warrants rejection, but I may be swayed if the authors manage to upload a substantial revision
    - here is a non-exhaustive list of issues:
    	- for $Q^{r,\pi}_{\mathcal{M}\cup r'}$ (and similarly V), it's never made clear how the value depends on $r$ in the superscript, which remains confusing throughout, especially as other values including the cost c get swapped into that place and this value is quite central in the paper and used frequently throughout the text
    	- the paper initially introduces a soft-constraint setting (allowing for costs up to $\epsilon\geq 0$, with the hard-constraint case $\epsilon=0$ as a special case) but then, in places, assumes the hard-constraint setting without alerting the reader to the fact adding further confusion
    	- several pieces of notation are not defined in the main text (e.g. $N^+_{k+1}$) on page 5
    	- l.219 mentions advantage, followed by a definition of what appears to be a state-value function instead with advantage never defined
    	
	- regarding minor issues:
		- I'd advise using similar notation for different concepts: e.g. depending on sub/superscript, $\mathcal{C}$ is sometimes a set of feasible cost functions, sometimes a (not directly related) scalar value in the sample complexity bound, or $\Delta$ is once a set of measures, another time a reward correction term. I'd advise using at least a different font in the two cases. 
		- several times, the main text refers to numbered Tables or Figures, which are in the appendix but this is not pointed out - by default, a reader will search in the main text
		- there is also a fair amount of typos

- the theoretical results very closely follow similar prior results on the sample complexity of IRL and the transferrability of the recovered rewards (Metelli 2021, Schlaginhaufen 2024). Per se, I don't see that as a huge problem - clearly porting these results to the context of constraint inference still has value. However, if the main contribution of the paper is translating the results into another context, presentation would seem to be one of the main possible contributions, so doing a poor job at that takes away most of the value

### Questions
- what role does the superscript $r$ play in  $Q^{r,\pi}_{\mathcal{M}\cup r'}$  ?
- in Definition 3.3 of an IRC solver, you introduce $\mathcal{C}_{\text{IRL}}$, "the set of feasible reward correction terms derived by [the solver]", which seems to imply that the IRC solver at least *may* recover a whole set of feasible reward correction terms. Then, having this set, one may try to produce a policy that is as robust as possible with respect to that set. Using your own example from Fig. 3, you write that the solver learns a error correction term $-1-\beta,\beta>0$, If understood as a set of feasible correction terms, a robust policy would avoid this state. Instead, you seem to force a choice of one particular reward correction. What do you think of using the full set of feasible error correction terms? Would this eliminate the advantage you point out? Alternatively, Bayesian IRL methods would give a posterior over the different feasible error correction terms, again allowing for producing robust policies.
- could you please point out which results and proofs mostly just follow prior work on related concepts, and which parts (e.g. giving line ranges) are indeed novel and specific to this context?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper explores inverse reward correction (IRC) that, instead of solving a three-level optimization in inverse constrained RL (ICRL), tries to combine the constraints as part of the reward function so as to solve only a reward optimization problem. The paper proves IRC has lower sample complexity but worse generalizability than ICRL solvers. The work investigates conditions in the transition laws, cost/reward functions, and Lagrangian multipliers that guarantee epsilon-optimality of IRC when transferring to a different environment.

### Strengths
- well-written and clear
- problem and questions are well-motivated
- interesting theoretical guarantees and analysis of IRC

### Weaknesses
 - could benefit from comparison on more complex environments than grid-world
- it would be nice to have a comparison of the pseudocode of the IRC and ICRL algorithms used in experiment
- consider adding hyperparameters of the algorithms in the experiments

### Questions
- what are the implications of this in few-shot learning after transferring an IRC/ICRL policy?
- What would these bounds on the sample complexity/generalizability of IRC and ICRL mean in real world tasks where S and A are continuous spaces? 
- Furthermore, do these bounds consider any measure (like complexity) of the dynamics/transition function? Why or why not?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper focuses on two approaches for safety-critical inverse RL: Inverse Constrained Reinforcement Learning (ICRL) and Inverse Reward Correction (IRC). It derives the upper bounds of these two methods and concludes the advantage of IRC in terms of sample efficiency. The paper also discusses potential constraint violations when learning a reward correction term or cost in source environments and transferring them to new environments. Theoretical analysis demonstrates that ICRL is more robust to these issues compared to IRC and examines the optimality of ICRL in target environments. Finally, empirical studies on gridworlds validate the theoretical findings for both methods.

### Strengths
- The paper provides a comprehensive comparison of ICRL and IRC approaches from multiple perspectives, including sample complexity and transferability. This reveals a tradeoff between the methods, offering interesting insights into their applications.
- The theoretical formulations and derivations are detailed and well-defined.
- The empirical evaluations are convincing and consistent with theoretical results.

### Weaknesses
 - The paper compares sample efficiency using theoretical upper bounds. I haven’t fully examined the details, but I am curious about the tightness of these estimations and whether they reliably represent real sample efficiency in practice.
- Although the experiments are conducted in gridworlds to validate the theoretical findings, I wonder if the results hold true for more complex, scalable tasks. Discussing potential challenges in such contexts could offer guidance and inspiration for the practical application of ICRL and IRC.
- I am a little confused about $\min_{\triangle r}$ in Eq. (2), which seems to minimize the expert's returns. Should it be $\max$ instead?
- The term 'iteration' appears in several theorems. It would be helpful to briefly explain what ICRL and IRC do in each iteration, such as taking a fixed number of gradient steps based on Eq. (1) and (2) ?

### Questions
- The paper compares sample efficiency using theoretical upper bounds. I haven’t fully examined the details, but I am curious about the tightness of these estimations and whether they reliably represent real sample efficiency in practice.
- Although the experiments are conducted in gridworlds to validate the theoretical findings, I wonder if the results hold true for more complex, scalable tasks. Discussing potential challenges in such contexts could offer guidance and inspiration for the practical application of ICRL and IRC.
- I am a little confused about $\min_{\triangle r}$ in Eq. (2), which seems to minimize the expert's returns. Should it be $\max$ instead?
- The term 'iteration' appears in several theorems. It would be helpful to briefly explain what ICRL and IRC do in each iteration, such as taking a fixed number of gradient steps based on Eq. (1) and (2) ?

### Soundness
3

### Presentation
3

### Contribution
3
