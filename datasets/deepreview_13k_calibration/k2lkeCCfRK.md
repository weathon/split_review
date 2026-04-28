# GFLOWNET TRAINING BY POLICY GRADIENTS

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5, 5

## Abstract
Generative Flow Networks (GFlowNets) have been shown effective to generate combinatorial objects with desired properties. We here propose a new GFlowNet training framework, with policy-dependent rewards, that bridges keeping flow balance of GFlowNets to optimizing the expected accumulated reward in traditional Reinforcement-Learning~(RL). This enables the derivation of new policy-based GFlowNet training methods, in contrast to existing ones resembling value-based RL. It is known that the design of backward policies in GFlowNet training affects efficiency. We further develop a coupled training strategy that jointly solves GFlowNet forward policy training and backward policy design. Performance analysis is provided with a theoretical guarantee of our policy-based GFlowNet training. Experiments on both simulated and real-world datasets verify that our policy-based strategies provide advanced RL perspectives for robust gradient estimation to improve GFlowNet performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces a way to train GFlowNets through policy gradients from the RL literature. The work proposes a coupled training strategy to train the forward and backward policies in GFlowNets.

### Strengths
1. This work discusses an interesting direction of training GFlowNets and using learning from RL policy-based methods to introduce a policy-based GFlowNet.
2. The discussion and perspective around backward trajectories is interesting and a useful way to improve GFlowNet training.
3. The gradient equivalence discussion and analysis is useful to understand the theoretical claims and some of the motivation behind this work.

### Weaknesses
1. The related work section could be made more exhaustive by adding the other GFlowNet losses and their references.
2. It will be useful to expand the number of environment configurations. For hypergrid, N=2 and N=3 are the only options used and using a higher value will help. Specifically, the hypergrid experiments should explore the impact of increasing the dimensionality (N) and the number of steps (H), as these parameters directly influence the complexity of the state space and the length of the trajectories. The current experiments are limited in scope and do not adequately demonstrate the scalability of the proposed method.
3. Previous work has analyzed number of states visited for hypergrid domain, which has not been included here. It is important to analyze the number of unique states visited during training, as this metric provides insights into the exploration capabilities of the algorithm. Comparing this with existing GFlowNet methods would be beneficial.
4. Adding other GFlowNet based baselines, such as Detailed Balance, would be useful as it is an important and commonly used objective. The Detailed Balance objective is a fundamental loss function in GFlowNets, and its inclusion as a baseline is crucial for a comprehensive evaluation. The absence of this baseline makes it difficult to assess the relative performance of the proposed method.
5. Some of the domains that were used in the previous work have been not included here. In order to corroborate that the proposed method can be used over different settings, including them would be helpful. The selection of domains should be more diverse to demonstrate the general applicability of the proposed method. Including domains with different characteristics, such as those with continuous state spaces or more complex reward functions, would be beneficial.
6. For bit sequence domain, including all bits used in the previous work would be beneficial for a fair comparison across methods. The bit sequence experiments should be conducted with a range of sequence lengths to evaluate the method's performance under varying complexity. The current experiments do not provide sufficient evidence to support the method's effectiveness in this domain.
7. Related work could be expanded and made more exhaustive, including the recent improvements in GFlowNets as well.

### Questions
The main concerns are about the coverage of the experiments section. If the authors could address and answer those concerns, stated in the weaknesses section, it will be useful for the contribution of the work.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper reformulates the the GFlowNet training problem as a RL problem over a special MDP. A policy gradient method is proposed to do RL training in this setting. The authors also formulate the design of backward policies in GFlowNets as a RL problem and propose a coupled training strategy. Theoretical and empirical results are provided to validate and help understand the proposed method.

### Strengths
**originality**
- The main novelty of the paper is on formulating the GFlowNet problems as RL problems and allow the use of RL in these problems. The problem formulation and the training strategies proposed can be considered novel results. 
- The theoretical results are interesting and can be considered novel

**quality**
- The paper is overall well-written, with only minor isuses

**clarity**
- The paper is quite clear

**significance**
- The new problem formulation and training strategies discussed in this paper allow RL to be used in GFlowNet training problems, together with theoretical and empirical results, can be a significant contribution.

### Weaknesses
Related work:
- It seems to me the related work can be improved, for example, what is the most relevant standard RL algorithm? And how is your proposed policy gradient method different in design? Additionally, GFlowNet and RL are discussed together in some other papers in the literature, such as the "GFlowNet Foundations" by Bengio et al. How is the analysis in your work related to these previous works?

Additional technical details: 
- Would be nice to have more technical details, for example, how does your method compare to others in terms of computation efficiency? Will formulating into RL problems make training much slower. 

Ablations:
- I think more ablation on the proposed method with different hyperparameters can help us understand better how it can be applied/tuned to different problems. 

Other issues: 
- End of page 5, a figure reference seems to be broken. Is this figure in the paper?

### Questions
- Can you elaborate on why is RL a good strategy to use for these problems and what unique advantages it can bring? Are there concrete problems where they have to be solved with RL and not other strategies?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new approach for improving the training of GFlowNets from the perspective of policy-based rewards and guided backward policy. The proposed method includes a coupled training strategy that jointly solves GFlowNet training and backward policy design, which aims to improve training efficiency. The method is tested a few benchmark including hypergrid, bit sequence generation and bayesian structure learing.

### Strengths
This paper tries to connect the field of RL and GFlowNets, which forms an interesting problem. The experimental part is well-explained.

### Weaknesses
The main concern for the paper is that the experimental evaluation part is too toy -- which focuses on some synthetic problems including hypergrid and bit sequence generation only, and the evaluation metric does not follow previous paper, and some of the claims are not well supported. The hypergrid and bit sequence experiments, while useful for initial validation, do not adequately demonstrate the method's applicability to more complex, real-world scenarios. Specifically, the lack of experiments on tasks such as molecule generation or biological sequence design limits the impact of the work. Furthermore, the use of non-standard evaluation metrics, such as not reporting L1 error or the number of modes, makes it difficult to compare the performance of the proposed approach with existing methods. The claims of improved training efficiency are not fully substantiated by the provided experimental results, as the performance gains are not clearly demonstrated against established baselines using standard metrics.

### Questions
> Our theoretical results are also accompanied by performing experiments in three application domains, hyper-grid modeling, Bit sequence modeling, and Bayesian Network (BN) structure learning.

Could the authors also consider molecule generation and biological sequence design, which are more practical and larger-scale tasks for validating the effectiveness of the approach?

> Definition 1 (Policy-dependent Rewards).

If the rewards are dependent on the policy, will it change during the course of training? Doesn't this introduce additional instability? 

Regarding the experiments, why not following the standard metric for evaluating the algorithms, e.g., L1 error, the number of modes?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work shows that there is an equivalence (in expectation) between training GFlowNets (GFN) with the Trajectory Balance objective, and a special form of non-stationary-reward policy gradient (PG) method. This is derived through the equivalence (in expectation) between TB and a forward KL-Divergence shown in prior work. This enables the algorithm to be treated as a PG method, onto which one can apply methods like TRPO.

The authors perform some empirical evaluations of their method on grids, bit sequences, and Bayesian networks.

### Strengths
This paper continues the work of relating GFlowNets and other frameworks, here RL, and of building novel methods upon that. In that sense the work here is a novel and interesting contribution.

### Weaknesses
The two main weaknesses of this paper are presentation and strength of empirical results.

Presentation: what the authors are trying to do isn't incomprehensible, I kind of get it and staring at the appendix helps, but I honestly think  section 3 could be heavily reworked to be more concise and tell a story, e.g. make it clear at every step what the symbols are, where they come from and how they make us progress in going from TB to RL with a non-stationary reward.

Results:
- Hypergrids and bit sequences are not very hard nor interesting problems, they were meant to be toy examples in the papers in which they were introduced. Learning to produce Bayesian nets is interesting, but I don't think the authors properly compare to Deleu et al.
- There isn't much in terms of "why does this work [better]?" which is usually a good thing to have in a paper.

Now I realize this paper may be more "theory" than experiment, but it does feel unfortunate that there's a mismatch between the "we're doing PG therefore we can bring in the whole RL arsenal" and the lack of big results.

This may be tangential, and just a semantics argument, but I find it slightly far-fetched to call this a policy gradient algorithm, or maybe even RL. The reason: the reward changes at every state, _and_ in a self-referential manner. The closest we have is maybe methods like Random Network Distillation, but even then the update of $R$ is decoupled from the update of $\pi$. Just because the update equation "looks like" PG, doesn't mean it's the most "scientifically useful" way to describe it. Methods like TRPO certainly assume a fixed reward, so I don't even know if what's being done here is correct.

- > "Value-based methods, however, face the difficulties of designing a powerful sampler that
can balance the exploration and exploitation trade-off, especially when the combinatorial space is
enormous with well-isolated modes."   
  
  I really don't see what this challenge has to do with a method being value-based or not. Soft-Q-Learning is very powerful and handles this trade-off. SubTB-GFlowNets seem to work very well and handle this trade-off through means like temperature conditioning.
- I don't understand if the authors mean something specific (or different) when they talk about absorbing MDPs; GFlowNets already operate on absorbing DAGs through the definition of $s_f$.
- In section 3.2, the authors write "It is clear that...", I beg to differ, it would be helpful to explain where this equation is pulled from. Why can $V_F$ be substituted for (4)?
- The authors carry on to write that the gradients of TB can be written something like $(Q(s,a) -C)\nabla \log P_F$, which sounds cool but at this point in the paper $Q$ (nor $V$) hasn't been fully defined. It appears to be the action-value function of policy $P_F$, but for which reward? For which MDP?
- "Following the pipeline by Shen et al. (2023), we must solve the optimization of LT B−G to find the desired PB at first". I'm not 100% sure but fairly confident that in Shen et al. $P_B$ and $P_F$ are "trained" simultaneously, it's just that $P_B$ is non-parametric, thus it evolves in time as more states are visited.
- Hypergrid:
    - Gridworlds, in GFNs and in RL, are useful to _sanity check_ an idea, but I really wouldn't use it as a strong base of comparison between algorithms
    -  "[P] can be estimated empirically by sampling" in a hypergrid it can be computed exactly as well through dynamic programming.
- BN: Deleu et al. use detailed balance, not TB, to train their model. It would be good to compare performance to their setup exactly rather than a possibly suboptimal one.
- After Eq (12), I'm not sure what Lemma 1 has to do with the fact that the expected value of a score is 0.


- There are lots of typos and some citation formatting mistakes throughout, I'd recommend another round of proofreading.

### Questions
- > "Value-based methods, however, face the difficulties of designing a powerful sampler that
can balance the exploration and exploitation trade-off, especially when the combinatorial space is
enormous with well-isolated modes."   
  
  I really don't see what this challenge has to do with a method being value-based or not. Soft-Q-Learning is very powerful and handles this trade-off. SubTB-GFlowNets seem to work very well and handle this trade-off through means like temperature conditioning.
- I don't understand if the authors mean something specific (or different) when they talk about absorbing MDPs; GFlowNets already operate on absorbing DAGs through the definition of $s_f$.
- In section 3.2, the authors write "It is clear that...", I beg to differ, it would be helpful to explain where this equation is pulled from. Why can $V_F$ be substituted for (4)?
- The authors carry on to write that the gradients of TB can be written something like $(Q(s,a) -C)\nabla \log P_F$, which sounds cool but at this point in the paper $Q$ (nor $V$) hasn't been fully defined. It appears to be the action-value function of policy $P_F$, but for which reward? For which MDP?
- "Following the pipeline by Shen et al. (2023), we must solve the optimization of LT B−G to find the desired PB at first". I'm not 100% sure but fairly confident that in Shen et al. $P_B$ and $P_F$ are "trained" simultaneously, it's just that $P_B$ is non-parametric, thus it evolves in time as more states are visited.
- Hypergrid:
    - Gridworlds, in GFNs and in RL, are useful to _sanity check_ an idea, but I really wouldn't use it as a strong base of comparison between algorithms
    -  "[P] can be estimated empirically by sampling" in a hypergrid it can be computed exactly as well through dynamic programming.
- BN: Deleu et al. use detailed balance, not TB, to train their model. It would be good to compare performance to their setup exactly rather than a possibly suboptimal one.
- After Eq (12), I'm not sure what Lemma 1 has to do with the fact that the expected value of a score is 0.


- There are lots of typos and some citation formatting mistakes throughout, I'd recommend another round of proofreading.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper derives a connection between generative flow networks (GFlowNets) and policy gradient methods. An equivalence of gradients between GFlowNet objectives and gradients of variational objective is (re)derived, and from this emerges an equivalence with a reinforcement learning problem that can be solved using policy-based RL methods such as TRPO. Experiments are performed on three amortized sampling problems from past work and the algorithm is claimed to deliver improved samplers on two of them.

### Strengths
- The connection between GFlowNets and policy-based RL is stated for the first time, which can be valuable if it can produce improved training algorithms for GFlowNets.
- New result extending the SubTB gradient analysis from [Malkin et al., 2022b] to state flows.
- Experiments on diverse problems, representing a nontrivial engineering effort by the authors.

### Weaknesses
 - There are many instances of unclear and incorrect mathematical language and notation in section 2 and 3.
  - Section 2.1:
    - "Assume there are $T+1$ topological orderings" -- that is not what "topological ordering" means; a topological ordering is a partial order homomorphism from a given partial order to a total order (i.e., a list of the states where no state is preceded by its descendant). Is it meant that the DAG is graded (as stated in the following paragraph) and that the layers are indexed by $0,\dots,T$?
    - Similarly, an instance of two elements being in a binary relation is not a "partial order". A partial order is a set with a binary relation (satisfying some properties), equivalent to a DAG.
    - It is incorrect to **define** ${\cal S}_0:=\{s_0\}$ and similar for ${\cal S}_T$, if the stratification into ${\cal S}_t$ already comes with the data of a graded DAG. That $s^0$ is the only state in the first graded component ${\cal S}_0$ is an **assumption/requirement**.
  - Section 2.2:
    - The second sentence of 2.2 is self-contradictory. "Probability measure" means the measure of the entire $\cal T$ is 1. In fact $F$ is just a measure, and $P$, its normalization, is a probability measure.
    - Equation (2) is missing a condition that this should hold only for $s\neq s^0$.
    - In equation (3), backward policy was not introduced/defined.
    - I did not understand this: "$\hat Z$ is a constant whose value is clamped to $Z$".
  - Section 3 start: I don't believe [Madan et al., 2023] discusses the relationship between TB and KL divergence. However, that relationship is discussed in [Malkin et al., 2022b] and in [Zimmermann et al., "A variational perspective on generative flow networks", TMLR].
  - Section 3.1:
    - "Expectation over $P_B$ is intractable due to unknown $Z^*$" -- even with known $Z^*$, sampling $P_B$ is not necessarily tractable. The issue is that $P_B$ is defined as a function of the reward, which is only known at the terminal states. The backward distribution is not directly accessible for sampling.
    - "This forward gradient equivalence [in [Malkin et al., 2022b]] does not take the total flow estimator into account" -- in fact, that paper shows that the equivalence on $P_F$ parameter gradients holds independently of $Z$ and *also* states the equivalence for the $\log Z$ gradient (after equation (12) in that paper). Thus there is **nothing original in Proposition 1**. The authors should clarify what aspect of the gradient equivalence they are extending, as the core result is already present in prior work.
    - In Proposition 1, it should be made clear that we do not propagate gradients to the distribution $P_F$ over which the expectation is taken. Otherwise, the proposition is not true. (This remark is made in Appendix A but not pointed to.)
- The paragraphs following Definition 1 are extremely difficult to understand, switching between GFlowNets and regular RL settings. 
  - I object to the statement that in "regular RL" the Markov chain determined by the policy and transition environment is ergodic (many RL settings feature "irreversible" actions). The authors should clarify the specific type of RL setting they are referring to, as the ergodicity assumption does not hold in general.
  - It should be noted that the math following Definition 1 is related to that in max-ent RL, which effectively places negative log-policy into the reward. The connection to maximum entropy RL should be explicitly stated and discussed.
    - Most importantly, how can the policy gradient methods described here work off policy (which is the important advantage of GFlowNets, and important for preventing mode collapse)? The authors need to clarify how they address the off-policy nature of GFlowNets within their policy gradient framework.
- The second sentence of section 3.3 seems key but does not make sense to me. The backward policy is a distribution over parents of each state and induces a distribution over subtrajectories. How can the $P_B$ be higher/lower for trajectories that precede a high-reward state $x$ if it is a distribution conditioned on $x$? The relationship between the backward policy and the reward needs further clarification, especially in the context of sub-trajectories.
  - Also, please check grammar in that sentence.
- The experiment results are not very convincing for a few reasons:
  - On the hypergrid, the policy-based methods effectively learn from partial trajectory information, so a fairer comparison may be to subtrajectory balance (which actually performs better on large hypergrids [Madan et al.]). The authors should justify why they are not comparing against sub-trajectory balance, which is a more relevant baseline for this setting.
  - Why is RL-G not tested in sections 4.2 and 4.3?
  - How were training hyperparameters selected? The lack of details regarding hyperparameter selection makes it difficult to assess the validity of the experimental results.
  - I am not convinced by the evaluation of total variation in 4.2 and 4.3 if it is performed by sampling, which can induce high variance in the estimate. It should be possible to compute the true terminating distribution, at least for the structure learning problem. JSD between the full distributions would allow comparison with past work; right now, there is no way to validate that TB faithfully reproduces results from [Deleu et al.] and [Malkin et al., 2022b]. The authors should provide a more robust evaluation of the learned distributions, such as JSD, and compare against existing results.
  - The same concerns apply to the bit sequence problem (4.2).
- Miscellaneous: 
  - Please check your citation type (`\citet`/`\citep`) and consistent capitalization in "GFlowNet", which is wrong in multiple places.
  - Broken ref at the bottom of p.5.

### Questions
Please see above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
