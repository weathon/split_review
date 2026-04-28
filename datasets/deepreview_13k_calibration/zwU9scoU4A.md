# Learning Mean Field Games on Sparse Graphs: A Hybrid Graphex Approach

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Learning the behavior of large agent populations is an important task for numerous research areas. Although the field of multi-agent reinforcement learning (MARL) has made significant progress towards solving these systems, solutions for many agents often remain computationally infeasible and lack theoretical guarantees. Mean Field Games (MFGs) address both of these issues and can be extended to Graphon MFGs (GMFGs) to include network structures between agents. Despite their merits, the real world applicability of GMFGs is limited by the fact that graphons only capture dense graphs. Since most empirically observed networks show some degree of sparsity, such as power law graphs, the GMFG framework is insufficient for capturing these network topologies. Thus, we introduce the novel concept of Graphex MFGs (GXMFGs) which builds on the graph theoretical concept of graphexes. Graphexes are the limiting objects to sparse graph sequences that also have other desirable features such as the small world property. Learning equilibria in these games is challenging due to the rich and sparse structure of the underlying graphs. To tackle these challenges, we design a new learning algorithm tailored to the GXMFG setup. This hybrid graphex learning approach leverages that the system mainly consists of a highly connected core and a sparse periphery. After defining the system and providing a theoretical analysis, we state our learning approach and demonstrate its learning capabilities on both synthetic graphs and real-world networks. This comparison shows that our GXMFG learning algorithm successfully extends MFGs to a highly relevant class of hard, realistic learning problems that are not accurately addressed by current MARL and MFG methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors study a class of games with many players who are interacting through a sparse graph structure. More specifically, they are interested in the regime where the number of players tend to infinity. The main solution concept is an extension of the notion of Nash equilibrium. The authors propose a learning algorithm based on online mirror descent. They conclude the paper with examples and numerical simulations.

### Strengths
Overall, the paper studies an interesting problem and is relatively clearly written. As far as I know, this is a new extension of MFG to sparse graphs. The algorithm is very inspired from existing ones but there is an adaptation to the problem under consideration (core vs periphery).

### Weaknesses
The model is quite abstract at some places. For the theoretical results, they are mostly about the analysis of the game and I am not sure how relevant they are for this conference (although they are certainly interesting for a certain community). It might have been more interesting to focus more on the learning algorithm.

There are some typos which make it hard to check the correctness of some parts (see questions).

1. I am wondering if some assumptions are missing. For example below Lemma 1, should $f$ be at least measurable (and perhaps more?) with respect to $\alpha$ for the integral to make sense?

2. Assumption 2 as used for instance in Lemma 1 does not seem to make much sense (unless I missed something): What is $\boldsymbol{\pi}$? We do not know in advance the equilibrium policy and even if we did, we would still need to define the set of admissible deviations for the Nash equilibrium. Could you please clarify?

3. Algorithm 1, line 14: Could you please explain or recall what is $Q^{k, \mu^{\tau_{\mathrm{max}}}}$?

Some typos: Should the state space be either $\mathcal{X}$ or $X$ (see section 3 for instance)? Does $\mathbb{G}^\infty_{\alpha,t}$ depend on $\boldsymbol{\mu}$ or not (see bottom of page 4)? Etc.

### Questions
1. I am wondering if some assumptions are missing. For example below Lemma 1, should $f$ be at least measurable (and perhaps more?) with respect to $\alpha$ for the integral to make sense?

2. Assumption 2 as used for instance in Lemma 1 does not seem to make much sense (unless I missed something): What is $\boldsymbol{\pi}$? We do not know in advance the equilibrium policy and even if we did, we would still need to define the set of admissible deviations for the Nash equilibrium. Could you please clarify?

3. Algorithm 1, line 14: Could you please explain or recall what is $Q^{k, \mu^{\tau_{\mathrm{max}}}}$?

Some typos: Should the state space be either $\mathcal{X}$ or $X$ (see section 3 for instance)? Does $\mathbb{G}^\infty_{\alpha,t}$ depend on $\boldsymbol{\mu}$ or not (see bottom of page 4)? Etc.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces Graphex Mean Field Games (GXMFGs), a framework for addressing the challenge of learning agent behavior in large populations. GXMFGs leverage graphon theory and graphexes, which represent limiting objects in sparse graph sequences. This approach suits real-world networks with both dense cores and sparse peripheries. The paper presents a specialized learning algorithm for GXMFGs. 

Key contributions include:

1. Introduction of GXMFGs, extending the scope of Mean Field Games.
2. Provides theoretical guarantees to show that GXMFGs accurately approximates finite systems.
3. Development of a learning algorithm tailored to GXMFGs.
4. Empirical validation on synthetic and real-world networks, demonstrating GXMFGs' ability to model agent interactions and determine equilibria effectively.

### Strengths
- Well-Written and Organized: The paper demonstrates strong writing and organization, enhancing its overall readability and accessibility.

- Clear Motivation: The paper effectively conveys a clear and compelling motivation for addressing the problem it tackles.

- Thorough Discussion of Prior Works: The paper provides a comprehensive and well-structured overview of prior works related to the research area.

- The paper provides solid theoretical contributions complimented with supporting empirical studies strengthens the paper's arguments and findings.

### Weaknesses
As the current paper falls outside the scope of my research interests, I am unable to identify any significant weaknesses in the paper. Consequently, my confidence in assessing the paper is limited.

### Questions
- Providing an intuitive explanation for assumptions 1(b) and 1(c) would greatly enhance the paper's overall readability and accessibility.

- While the paper assumes finite state and action spaces, it may be beneficial to explore whether the proposed approach can be extended to scenarios with infinite action spaces. 
- Including the code for the simulations, would enhance reproducibility.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces Graphex Mean Field Games (GXMFGs) which build on the graph theoretical concept of graphexes to include sparse network structures between agents. This improves over prior work on Graphon Mean Field Games which only allows for modelling with dense graphs. The authors derive convergence properties for the finite game. In addition, a learning algorithm based on online mirror descent is provided for a particular class of GXMFGs that follow a core-periphery network structure. Finally, the theoretical claims are empirically validated over both synthetic and real-world networks.

### Strengths
- This paper has a clear motivation to extend Graphon Mean Field Games to deal with sparse graphs which are frequently seen in practice. The hybrid graphex approach proposed in this work looks like a natural and intuitive solution.
- The technical development is principled and the analysis is nontrivial.
- The overall presentation and clarity is good.

### Weaknesses
 - Even though the authors explained in the paper, I didn't like the fact that the proposed GXMFGs have no baseline competitors to compare against. While I agree that one could argue on the contrary that the ability to work with sparse graphs is precisely the unique advantage of GXMGFs, I think that the authors should at least spend some efforts to discuss (if empirical comparison with LPGMFG is indeed unsuitable) how GXMFGs would compare with LPGMFG and GMFG in practice.


### Questions
In Figure 3a, it looks like the curves are diverging rather than converging as k increases? Are the curves coloured correctly?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
