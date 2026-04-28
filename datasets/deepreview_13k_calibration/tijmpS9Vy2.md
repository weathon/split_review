# BAMDP Shaping: a Unified Theoretical Framework for Intrinsic Motivation and Reward Shaping

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Intrinsic motivation (IM) and reward shaping are common methods for guiding the exploration of reinforcement learning (RL) agents by adding pseudo-rewards. Designing these rewards is challenging, however, and they can counter-intuitively harm performance. To address this, we characterize them as reward shaping in Bayes-Adaptive Markov Decision Processes (BAMDPs), which formalizes the value of exploration by formulating the RL process as updating a prior over possible MDPs through experience. RL algorithms can be viewed as BAMDP policies; instead of attempting to find optimal algorithms by solving BAMDPs directly, we use it at a theoretical framework for understanding how pseudo-rewards guide suboptimal algorithms. By decomposing BAMDP state value into the value of the information collected plus the prior value of the physical state, we show how psuedo-rewards can help by compensating for RL algorithms' misestimation of these two terms, yielding a new typology of IM and reward shaping approaches. We carefully extend the potential-based shaping theorem~\citep{ng1999policy} to BAMDPs to prove that when pseudo-rewards are BAMDP Potential-based shaping Functions~(BAMPFs), they preserve optimal, or approximately optimal, behavior of RL algorithms; otherwise, they can corrupt even optimal learners. We finally give guidance on how to design or convert existing pseudo-rewards to BAMPFs by expressing assumptions about the environment as potential functions on BAMDP states.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a theoretical framework that allows us to study both intrinsic motivation and reward shaping together in a unified way. This affords us the analysis of well-known intrinsic motivation and reward shaping methods, and their pathologies. They show that both intrinsic motivation and standard reward shaping can be lifted onto the Bayes-adaptive MDP level, where they together form different ways to do reward shaping for the BAMDP. Then prove that any standard IM and reward shaping method that corresponds to a potential-based shaping in the BAMDP should lead to Bayes-optimality in the underlying problem.

### Strengths
- The BAMDP value decomposition in Lemma 3.2 is to my knowledge novel. It is deceptively simple, yet seems to afford important results.

- Table 1 presents a great overview of how different IM and reward shaping methods fit together under the decomposition.

- The proposed framework of BAMPFs improve our mathematical understanding of IM and reward shaping in RL, and their known pathologies.

- Theoretical results appear novel and of high quality.

- Paper is written clearly and it is easy to read.

### Weaknesses
 - The empirical result is illustrative, more than demonstrative. A bigger-scale experiment would have been better. Specifically, I would appreciate a longer-horizon example. It can be tabular. 

- The theoretical results are heavy on definitions, to the point of sounding circular. Specifically, the Theorem 4.3. is not really surprising, and follows from applying the definition of potential-based shaping to BAMDPs. Although I agree that it is more complicated than the standard MDP case.

- Plots in Figure 3 are very low resolution to the point of being blurry.

### Questions
Overall, I think this is a good paper, providing good insights into IM and reward shaping. However, I think it would have benefitted from showing its impact with studying more examples of different IM and reward shaping terms, demonstrating how we can study their pathologies. 
Can you present more examples demonstrating the impact of your results?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the problem of reward modeling based on intrinsic motivation (IM) and reward shaping. Although IM generalizes reward-shaping functions in the standard MDP setting, it can still be expressed as reward-shaping in the BAMDP setting. Leveraging the fact that potential-based reward shaping functions (PBSFs) preserve optimal policies under any shaping, an extension to BAMDPs is proposed. This leads the authors to introduce BAMPFs, which are potential functions at the level of BAMDP: there, the state becomes the MDP history or a learning algorithm. A result shows that asymptotically stationary potential functions preserve optimal policies. This hints at how one should model the reward function in complex tasks such that the learned policy does not exhibit undesirable side-effects.

### Strengths
The paper is well-motivated: previous literature is introduced properly, and the positioning of this work is clear. 

The interpretation of IM as reward shaping in BAMDPs is novel, to the best of my knowledge. 
Also, it serves a practical objective, namely, reward modeling for complex RL tasks, a critical problem that is particularly challenging.

### Weaknesses
The paper is sometimes hard to follow:
-  too long sentences
-  technical words are used already from the abstract without being introduced or explained. It took me several readings to understand what is going on in this paper. 

I am unfamiliar with most of the related work (just the BAMDP part) so I cannot fully assess the quality of this submission. I know that BAMDPs are hard to work with, in terms of interpretability and tractability, but proposing experiments on a bandit problem seems insufficient for a mature publication.

### Questions
- The "RL algorithms" paragraph in Sec. 2.1 should appear together with BAMDPs from Sec. 2.3

- Did the authors consider extensions of their method to "realistic" environments? Do they already have an algorithm that leverages this BAMPF idea in deep RL?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a unifying decision-making framework that incorporates the concepts of intrinsic motivation, reward shaping, and potential functions. In particular, they propose a Bayes-adaptive MDP (BAMDP) framework that can reformulate intrinsic motivation and reward shaping as BAMDP potential-based shaping functions, thereby avoiding some of the known pitfalls of these methods. They show that this MDP framework satisfies important theoretical properties that make it possible to find an optimal policy, and provide an empirical experiment in support of this.

### Strengths
This paper provides a theoretically-sound framework that is able to incorporate the essence and advantages of intrinsic motivation and/or reward shaping while avoiding some of the known pitfalls of these methods. The decomposition of the value function into two components is insightful and interesting. The paper is generally well-written, and the technical concepts are explained in a relatively clear manner.

### Weaknesses
My biggest concern with this paper is the lack of empirical experiments. While it is reasonable to expect that a theoretical paper such as this one will not have as many experiments, having a single experiment with only a single state is a bit underwhelming. In particular, it would be useful if the authors included at least one other, more complicated experiment that further illustrates the usefulness of their framework. Ideally, the additional experiment(s) would show and contrast how the BAMDP avoids the reward-hacking (or similar) behavior that can occur with intrinsic motivation and/or reward shaping.

Similarly, it would be useful if the authors could provide a case study showing how a well-known, problematic instance of intrinsic motivation or reward shaping can be converted into a BAMDP potential-based shaping function. I understand that the authors provided a generic, brief overview of this process in lines 315-320, however having a specific example of a well-known, documented instance of reward-hacking (or similar) that would be alleviated by their framework would greatly solidify the arguments presented in this paper.

Finally, the limitations of the framework could use more discussion. In particular, it would be useful to have an example of intrinsic motivation and/or reward shaping (if any) that cannot be converted into a BAMDP potential-based shaping function. This would better characterize the usefulness and applicability of the framework. Ultimately, any potential user of the framework needs to be able to infer from this paper under what conditions the framework should or should not be used.

Some minor comments:
1) Figure 1 is hard to read. In particular, the caption should be more descriptive, it is not clear which individual plots belong to ‘a)’ vs ‘b)’, and the color scale should have a title.
2) Figure 2 is overcrowded (making it hard to read) and needs to be simplified.
3) Each item in Table 1 should have a reference/citation attached to it, especially since some of the items are not mentioned in the main text.

### Questions
Is there a type of intrinsic motivation and/or reward shaping that cannot be converted into a BAMDP potential-based shaping function? In other words, do these items have to conform to some sort of form or adhere to a certain set of assumptions?

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
This paper investigates the design of pseudo-rewards (e.g., intrinsic motivation, reward shaping) and when it can lead to unwanted side effects. To achieve this, the authors first cast the problem into a meta-learning problem by considering the effect of pseudo-rewards at the scale of RL algorithms using the BAMDP framework. 
By decomposing value functions into value of information/opportunity (VOI/ VOO), the authors developed a new way to classify different 
The authors also showed that the optimality of an RL algorithm is preserved if and only if the pseudo-rewards belong to the class of potential-based reward shaping in the corresponding BAMDP.

### Strengths
The idea of studying pseudo-rewards in the meta-learning setting is very original and interesting. The main theoretical result which says that pseudo-rewards can preserve optimality of an RL algorithm if and only if they are potential-based is very insightful and might be useful for designing new generations of exploration methods.

### Weaknesses
My main concern is that most of the performance guarantee results are proven at the scale of meta-learning, and it is not clear to me whether this actually solves the “reward-hacking” problem at the scale of individual MDPs, which is the main motivation of the paper. For example, if only 1 out of 100 of the MDPs suffers from the noisy TV problem, then the optimal RL algorithm in this case might simply “sacrifice” that MDP by using a novelty-based approach to explore more efficiently in the rest of the MDPs if the rewards from these MDPs far outweigh the ones from the noisy TV MDP.
Another minor weakness is that the paper mostly focuses on the invariance properties of the class of BAMPFs, and it remains unclear what are the advantages/disadvantages of choosing a specific BAMPF, which limits the practical relevance of the paper.

Also, as this paper is more theory focused, I feel like some parts of the paper are not clearly/rigorously written (see questions).

My question is that whether we can guarantee the performance of the optimal BAMDP policy $\bar{\pi}^{\ast}$ for an individual MDP (i.e., what can we say about $\mathbb{E}_{\bar{\pi}^{\ast}}[G|\mathcal{M}]$?) In contrast, the theorem relates optimal policies with or without BAMPF shaping within a given MDP.

Now, if we cannot guarantee the individual performance $\mathbb{E}_{\bar{\pi}^{\ast}}[G|\mathcal{M}]$, is it not the case that there might exist a BAMPF that makes the performance arbitrarily bad for some environments (i.e., misleading the agent into learning suboptimal policies)?

Note that this does not contradict with Theorem 4.3, as the theorem only states that the performance is preserved for the *optimal* policies (with/without shaping) of a given environment. The problem here is that the Bayes-optimal RL algorithm might not find the optimal policies for some environments.

### Questions
1. In section 3.2, the authors draw connections between IM, VOI, and VOO. However, it’s not clear to me how IM is related to VOI or VOO quantitatively. Also, what are the definition of attractive/repulsive signals?

2. On line 323, “In environments containing finite information…”, what is the definition of information for an environment?

3. I’m not sure if Def 4.2 is well-defined. Consider the same single-state MDP/potential function defined on line 364, except that now there are infinitely many levers. In this case, whether the potential function is settling is going to depend on the policy, that is, the potential function is settling if the policy has non-zero probabilities on finitely many levers (independent of time), and will not be settling otherwise.

4. In figure 3, what is None? Does it make use of any exploration method?

### Soundness
2

### Presentation
2

### Contribution
3
