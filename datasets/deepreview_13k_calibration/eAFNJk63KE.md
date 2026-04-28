# Riemannian Manifold Learning for Stackelberg Games with Neural Flow Representations

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
We present a novel framework for online learning in Stackelberg general-sum games, where two agents, the leader and follower, engage in sequential turn-based interactions. At the core of this approach is a learned diffeomorphism that maps the joint action space to a smooth Riemannian manifold, referred to as the $\textit{Stackelberg manifold}$. This mapping, facilitated by neural normalizing flows, ensures the formation of tractable isoplanar subspaces, enabling efficient techniques for online learning. By assuming linearity between the agents' reward functions on the $\textit{Stackelberg manifold}$, our construct allows the application of standard bandit algorithms. We then provide a rigorous theoretical basis for regret minimization on convex manifolds and establish finite-time bounds on simple regret for learning Stackelberg equilibria. This integration of manifold learning into game theory uncovers a previously unrecognized potential for neural normalizing flows as an effective tool for multi-agent learning. We present empirical results demonstrating the effectiveness of our approach compared to standard baselines, with applications spanning domains such as cybersecurity and economic supply chain optimization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the Stackelberg general-sum games.  They propose a learned diffeomorphism that maps the joint action space to the so-called Stackelber Manifold using neural normalizing flows. This way, they convert the equilibrium learning problem into an online learning problem on manifolds. Applying multi-armed bandit methods, this proposed framework is shown to achieve efficient computation of the equilibrium. Simulation results are provided to validate the proposed methods.

### Strengths
The proposed framework is highly novel to me. It effectively bridges equilibrium learning, manifold learning, and online learning paradigms by establishing theoretical and practical connections. The application of normalizing neural flows shows particular promise for converting equilibrium learning problems into online manifold learning, and optimization problems, opening valuable new research directions.

### Weaknesses
The paper would benefit from a clearer organizational structure, particularly in Section 4. The progression of ideas through Lemmas 4.1-4.4 needs stronger motivation and explicit statements of their individual contributions to the overall narrative. Additionally, the technical foundation could be strengthened by providing clearer connections between consecutive lemmas and their role in building the theoretical framework and by including fundamental definitions from Riemannian geometry, especially the concept of geodesics, which is central to the framework. In summary, I hope the authors make fewer assumptions about the reader's background knowledge in differential geometry.

### Questions
- Could the authors discuss more on the roles of Lemmas 4.1-4.4?
- Could the authors explain what structures of Riemannian manifolds are essential in the proposed framework? Can this framework be applied to space with fewer structures, say a smooth differential manifold?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies Stackelberg games where a leader and follower take actions sequentially. The framework presented in the paper maps the joint actions pace to a smooth Riemannian manifold for efficient methods for online learning. It assumes the agents' rewards function are linear on the Stackelberg manifold and then uses bandit algorithms.

### Strengths
The paper tries to provide a framework to map the Stackelberg games to a bandit problem by using neural normalizing flows and by assuming the reward function is linear on the mapped manifold, allowing the use of the bandit results to study the game. The paper could provide regret analysis and empirical results. 

However, the reviewer is very confused by the motivation of the approach. More details of weakness is shown below.

### Weaknesses
The paper is not very well structured and not very motivated. The contributions are not clear. The problem is statement is not clearly stated. It seems like the paper considers a 2-player Stackelberg game and considers bounding a form of regret as a measure of performance. However, Section 2.2 describes a procedure to obtain an embedding on the D-sphere where the reward functions are linear as in (2.16). First of all, it is unclear why people should do this embedding (motivation is not clear). Secondly, It is not clear how such an embedding is possible. The loss in 2.14 does not reflect that.

There are several lemmas and theoretical results in the paper that do not seem to hold as currently stated and/or the provided proof doesn’t make sense. Examples include:

1) Definition 4.2: it seems like such a manifold does not exist unless it is a singleton, because any two distinct points as a subset is certainly not geodetically convex.
2) Lemma 4.1 where the statement does not make sense for any non-compact domain.
3) Lemma 4.3: the justification of this lemma does not make sense other than restating the Poincare-Hopf Theorem.

In the simulations, the rewards models seem to be linear in \theta parameters automatically, then it is not clear what is the purpose of Section 2.2. regarding the embedding.

### Questions
see comments under the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes an approach to no-regret learning in Stackelberg games that first embeds the original joint actions in a Riemmanian manifold, in particular the sphere. The authors deploy techniques from normalizing flows to learn this invertible mapping using a loss function they designed to approximately satisfy several desiderata (D1-D6) that they argue a *Stackelberg Embedding* should satisfy. They then propose an algorithm that takes advantage of this embedding to estimate optimal *embedding* actions that they then map back to the original action space. Experiments show the regret of their algorithm (GISA) grows more slowly than the baseline UCB algorithm.

### Strengths
The idea of learning an embedding of a Stackelberg game such that the game can be reasoned about and solved in that space more easily is novel and interesting. To accomplish this, the authors leverage normalizing flows; in general, this work requires aggregating ideas and techniques from several typically disparate research areas which makes it original. While the paper focuses on the spherical manifold, the proposed loss function in equation 2.14 provides a way of learning the embedding, not just for spherical manifolds.

### Weaknesses
### weaknesses:
 As the paper is currently presented, there was little discussion or motivation early on for why a spherical embedding (or any embedding) would be helpful for constructing an improved no-regret algorithm. The learned mapping is invertible so there's no dimensionality reduction, which is a typical motivation in other work making similar assumptions. Section 2.3 is introduced eventually, but it would seem the assumption of reward functions that are linear in the embedding space is critical for this approach to be strong. For example, in the linear MDP literature, this reward assumption is stated early on as part of the problem definition [1]. A more thorough discussion of the benefits of the spherical embedding, particularly its geometric properties that facilitate equilibrium computation, should be included early in the paper. It is also unclear whether the linearity assumption of the reward function in the embedding space is a strict requirement or an assumption that, when met, enhances performance. If it is the latter, this should be clarified, and a discussion of the algorithm's behavior when this assumption is violated would be beneficial.

It's unclear how the precise experimental settings illustrate the importance of the embeddings. Do the reward functions in this game satisfy the linearity assumption in the chosen embedding space? The experimental section should explicitly address this question. Furthermore, an ablation study comparing the performance of the proposed method using the learned normalizing flow versus using the closed-form mappings in Appendix G.1 would provide valuable insights into the importance of the normalizing flow. If the normalizing flow is indeed crucial, experiments should demonstrate its impact on the uniformity of data distribution across the manifold and the resulting performance improvements.

There are several areas where the writing and presentation could be improved. The paragraph on Problem Setting mentions optimal transport and causal game theory, but these concepts are not discussed further in the paper. Their inclusion is confusing and should be either elaborated upon or removed. Additionally, the use of five different versions of  $\theta$ ($\theta$, $\theta’$, $\hat{\theta}$, $\tilde{\theta}$, $\theta^*$) is excessive and makes the paper difficult to follow. A more streamlined notation, with clear definitions for each symbol, would greatly improve readability. For example, it is not immediately clear what the difference is between $Q$ and $\phi$, and whether separate symbols are necessary. The algorithm pseudocode also needs significant clarification. It currently only accounts for a subset of the components of the algorithmic pipeline (action embedding, objective parameter estimation, strategy learning) and relies on "global" variables that are not properly defined within the algorithm's scope. For instance, the estimation of $\hat{\theta}_A$ and $\hat{\theta}_B$ is not represented in Algorithm 1, nor are they inputs to the algorithm.

### questions:
 In general, I like the idea of the paper but I feel the writing needs to be substantially improved (e.g., motivation and layout of paper mentioned in weaknesses above). I also feel the experimental domains could be supplemented with a few toy domains that are tailored to the specific reward assumption for a given embedding. Including additional manifolds beyond the sphere manifold would strengthen the paper as well if you can construct meaningful motivations for them.

- Figure 1: I originally found Figure 1 to be saying something contradictory to Lemmas 4.3 and 4.4. The red arrow corresponding to $\Phi_a$ appeared to be suggesting that $\Phi_a$ runs horizontally. Similarly, $\Phi_b$ points to a horizontal surface. Can you change $\Phi_a$ to simply point to a single longitudinal line? Also, maybe make $\Phi_b$'s arrow blue to be consistent?
- Algorithm 1: line 12 shows the algorithm returning an action before the for-loop completes. Is there an indent typo here? Do you mean *yield* rather than *return*? Also, line 12 states "return $a^*$" whereas I assume you mean $\hat{a}^*$.
- Figure 2 / Algorithm 1: Presumably, these two can help the reader better understand the algorithm. Figure 2 uses $\theta'\_B$ while Algorithm 1 uses $\hat{\theta}\_B$. Can these be made consistent? Also, if the green circle represents $\mathcal{B}(\theta, \hat{\theta}\_B)$, can you point out $\tilde{\theta}\_A$ specifically in Figure 2?
- Theorem 1: Is there a typo? "and Eq. (2.15) and Eq. (2.16)" is repeated. I'm not sure the sentence currently makes sense either. Do you mean to say "and the linear relationship to the reward function.... holds"?
- Section 4.1, near end of first paragraph: "In the Stackelberg game, since the follower moves first...". You mean the leader moves first.
- Paragraph "Mapping to a Spherical Manifold": The sentence "The transformation from spherical coordinates to Cartesian coordinates is used to map input features onto a $D$-dimensional spherical manifold" seems to read backwards. It should be "transformation from Cartesian to spherical..." or the "inverse of the transformation from...".
- How might you handle Stackelberg games with discrete action spaces?

### Questions
In general, I like the idea of the paper but I feel the writing needs to be substantially improved (e.g., motivation and layout of paper mentioned in weaknesses above). I also feel the experimental domains could be supplemented with a few toy domains that are tailored to the specific reward assumption for a given embedding. Including additional manifolds beyond the sphere manifold would strengthen the paper as well if you can construct meaningful motivations for them.

- Figure 1: I originally found Figure 1 to be saying something contradictory to Lemmas 4.3 and 4.4. The red arrow corresponding to $\\Phi_a$ appeared to be suggesting that $\\Phi_a$ runs horizontally. Similarly, $\\Phi_b$ points to a horizontal surface. Can you change $\\Phi_a$ to simply point to a single longitudinal line? Also, maybe make $\\Phi_b$'s arrow blue to be consistent?
- Algorithm 1: line 12 shows the algorithm returning an action before the for-loop completes. Is there an indent typo here? Do you mean *yield* rather than *return*? Also, line 12 states "return $a^*$" whereas I assume you mean $\\hat{a}^*$.
- Figure 2 / Algorithm 1: Presumably, these two can help the reader better understand the algorithm. Figure 2 uses $\\theta'\_B$ while Algorithm 1 uses $\\hat{\\theta}\_B$. Can these be made consistent? Also, if the green circle represents $\\mathcal{B}(\\theta, \\hat{\\theta}\_B)$, can you point out $\\tilde{\\theta}\_A$ specifically in Figure 2?
- Theorem 1: Is there a typo? "and Eq. (2.15) and Eq. (2.16)" is repeated. I'm not sure the sentence currently makes sense either. Do you mean to say "and the linear relationship to the reward function.... holds"?
- Section 4.1, near end of first paragraph: "In the Stackelberg game, since the follower moves first...". You mean the leader moves first.
- Paragraph "Mapping to a Spherical Manifold": The sentence "The transformation from spherical coordinates to Cartesian coordinates is used to map input features onto a $D$-dimensional spherical manifold" seems to read backwards. It should be "transformation from Cartesian to spherical..." or the "inverse of the transformation from...".
- How might you handle Stackelberg games with discrete action spaces?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
1. **Summary:** This paper presents a novel framework for online learning in Stackelberg general-sum games, which involves two agents: a leader and a follower. The key innovation is the use of a learned diffeomorphism that maps the joint action space to a smooth Riemannian manifold, termed the Stackelberg manifold. This approach, facilitated by neural normalizing flows, creates isoplanar subspaces that simplify the application of standard bandit algorithms for online learning. The authors assume linearity of the agents' reward functions on the Stackelberg manifold, providing a theoretical foundation for regret minimization on convex manifolds and establishing finite-time bounds on simple regret for learning Stackelberg equilibria. The paper demonstrates the effectiveness of this manifold learning integration into game theory, showing its potential for neural normalizing flows as a tool for multi-agent learning. Empirical results are presented, comparing the approach to standard baselines and showing improvements in computational efficiency and regret minimization across applications in cybersecurity and economic supply chain optimization.

2. **Contribution:** The paper's contributions are significant in advancing the understanding of Stackelberg learning under imperfect information and providing a rigorous framework for optimizing Stackelberg games on spherical manifolds.

### Strengths
The primary strengths of this paper can be summarized in the following two aspects:

1. The paper presents a novel approach of mapping actions to a Riemannian manifold to solve the Stackelberg equilibrium.
2. The paper provides both rigorous theoretical analysis and comprehensive empirical validation.

### Weaknesses
Here are the major weaknesses from my perspective:

1. The authors have not compared their method to many current state-of-the-art approaches for solving Stackelberg equilibrium. The only comparison provided is in the experimental section, where they benchmark their algorithm against the dual-UCB method. The lack of broader comparisons with other recent algorithms, both from an empirical and theoretical standpoint, limits the contribution.

2. As a minor suggestion, the author should provide additional background information on Riemannian manifolds, as the concept may not be familiar to the broader deep learning community.


Additionally, I have a minor suggestion: I recommend that the authors switch to the official template for the conference to ensure a more formal presentation.

### Questions
Based on the discussion of the paper's strengths and weaknesses, I have the following questions for the authors:

1. What is the intuition behind mapping the action space to a Riemannian manifold? Does this approach stem from leveraging methods such as Riemannian gradient descent?
2. Is it necessary to consider a general Riemannian manifold, or is it sufficient to focus only on the unit sphere?
3. Can the authors provide a theoretical explanation of why their algorithm has advantages over previously proposed methods?

### Soundness
3

### Presentation
3

### Contribution
3
