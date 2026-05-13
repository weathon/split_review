# Learning Nash Equilibria in Rank-1 Games

- Decision: Accept
- Scores: 5, 8, 6, 5

## Abstract
Learning Nash equilibria (NE) in games has garnered significant attention, particularly in the context of training Generative Adversarial Networks (GANs) and multi-agent Reinforcement Learning. The current state-of-the-art in efficiently learning games focuses on landscapes that meet the (weak) Minty property or games characterized by a unique function, often referred to as potential games. A significant challenge in this domain is that computing Nash equilibria is a computationally intractable task [Daskalakis et al. 2009]. 

In this paper we focus on bimatrix games (A,B) called rank-1. These are games in which the sum of the payoff matrices A+B is a rank 1 matrix; note that standard zero-sum games are rank 0. We show that optimistic gradient descent/ascent converges to an \epsilon-approximate NE after 1/\epsilon^2 log(1/\epsilon) iterates in rank-1 games. We achieve this by leveraging structural results about the NE landscape of rank-1 games Adsul et al. 2021. Notably, our approach bypasses the fact that these games do not satisfy the MVI property.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on learning (approximate) Nash Equilibria of rank-1 bimatrix game, which can comprise a potentially large number of disconnected components, and may lack convexity in general.
The rank-1 bimatrix games, which have been shown by Adsul et al., 2021  to have polynomial-time algorithms, are especially interesting, as k>=3 are PPAD-hard, and the complexity of k=2 games are left as an open question.

The authors build upon the reparameterization approach of Adsul et al., 2021, which establishes a link between rank-1 games and parameterized zero-sum games. 

- In Section 3.1, the authors illustrates that naively solving an approximate NE of parameterized zero-sum games does not necessarily results in the approximate NE of the original rank-1 games.
- In Section 3.2, the authors sequentially connects the approximate NE of rank-1 games to (constrained) approximate NE of parameterized zero-sum games, and (constrained) approximate NE of the parameterized zero-sum-games to the approximate stationary points of an energy function.
- Finally, the authors propose an algorithm that combines binary search and OMWU that provably learns the approximate NE of the rank-1 game.

### Strengths
- The related works are well-studied and well-presented
- Theoretical claims are well-backed with easy-to-follow proofs

### Weaknesses
# Technical Novelty 
It seems most of the technical heavy-lifting (the reparameterization approach, Lemma 3.3, and the usage of binary search) builds upon  Adsul et al., 2021 [1], and lacks original technical contribution & viewpoint that could be useful for the other researchers in the future. For instance, while the reparameterization is acknowledged, the paper does not clearly articulate how the proposed algorithm offers a fundamentally different approach to finding approximate Nash Equilibria compared to the methods in [1]. Specifically, the connection between approximate NE of rank-1 games and constrained approximate NE of parameterized zero-sum games, as presented in Section 3.2, appears to follow directly from the reparameterization. A more detailed discussion on the novel aspects of this connection would be beneficial. Furthermore, the transition from constrained approximate NE of parameterized zero-sum games to approximate stationary points of an energy function, while technically sound, does not seem to introduce a new perspective that significantly deviates from established techniques in optimization. The authors should elaborate on the unique challenges posed by rank-1 games that necessitate this specific approach, as opposed to more standard optimization methods.

# Broader Context
I think it would better if the authors could put their theoretical results in a broader context of current literature, and explain why this rank-1 game is an important subclass of differential games. The paper currently lacks a compelling argument for the significance of studying rank-1 games beyond their polynomial-time solvability, as established by [1]. A discussion connecting rank-1 games to broader classes of games, or highlighting their relevance in specific application domains, would significantly strengthen the paper's impact. For example, are there specific real-world scenarios where rank-1 games naturally arise? How does understanding rank-1 games contribute to solving more complex game-theoretic problems?  Addressing these questions would provide a stronger motivation for the research and place it within a more meaningful context.

### Questions
# Technical Novelty
I would appreciate if the authors could clarify the the main technical novelties of this work over Adsul et al., 2021 that could contribute (either directly or indirectly) to the future work in this field (differential games, robust optimization, multi-agent RL, etc).

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study the problem of finding Nash equilibria for bimatrix rank-1 games. They propose a novel decentralized algorithm for finding approximate Nash equilibria of rank-1 games. Their approach works by reducing the problem to a sequence of parametric zero sum games where the parameter changes for each step of the sequence. Approximately solving the zero sum game and then adapting the game parameter repeatedly leads to an approximate Nash equilibrium for the original game. This decomposition allows the authors to bypass the fact that the original game does not satisfy the Minty variational inequality.

### Strengths
To the best of my knowledge, this work is the first to propose gradient based decentralized algorithms for approximate Nash equilibria of rank one games. Even though the general solution framework is the same as in Adsul et al. 2021, as they both reduce the problem to a sequence of parametric zero sum games, the way each zero sum game is tackled in this work is different and novel. Handling the additional constraint to the zero sum game was non-trivial. In addition, showcasing new  decentralized learning algorithms for games that go beyond the MVI property may be of independent interest.

### Weaknesses
The algorithm proposed is decentralized in a somewhat limited sense. For example, the two players need to coordinate to solve the same parametric game zero sum in each iteration.

### Questions
I think some more explanation about how we computed the bound on K would help. I guess I am missing the argument about why we only need to know $\lambda$ up to $O(\epsilon)$ accuracy or at least some similar argument for the binary search termination.

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
This paper studies the problem of learning Nash equilibrium in two-player rank-1 games, which does not satisfies the Minty condition. The main contribution of the paper is an efficient algorithm for learning Nash equilibrium in two-player zero-sum games. The main technical insights that enables the result are structural results of rank-1 games. Specifically, it is shown that the set of Nash equilibria of a rank-1 game is equivalent to the set of Nash equilibria of a two-player zero-sum game (with additional constraints, so can be seen as a saddle-point problem). The proposed algorithm is double-loop in the sense that the inner loop runs OWMU on the parameterized zero-sum, finds an approximate Nash equilibrium and the outer loop updates the parameter.

### Strengths
This paper is fairly well-written and easy-to-follow. I really appreciate the authors for providing very detailed high-level iades and proofs for every technical results, which makes the paper very clear.

### Weaknesses
Several concerns about the technical contributions.

1. There is no lower bound results and it is not know if the provided convergence rate is optimal. 
2. The authors show that there exists a rank-1 game that does not satisfies the Minty condition, so previous results on efficient convergence does not apply directly to rank-1 games. However, recent results have shown efficient convergence under a weaker condition than the Minty condition, called *weak Minty* [1, 2, 3].  [1] proposed the notion of weak MVI, while [2,3] generalized the notion to the constrained setting.
3. I am not sure whether Algorithm 1 is a decentralized algorithm since it is a double-loop algorithm and requires some coordination between the two players. Thus Algorithm 1 is more like an algorithm that computes the Nash equilibrium, not a decentralized learning dynmics that converges to Nash equilibrium

### Questions
1. Does rank-1 games satisfy the weak Minty condition?
2. Can the authors comment more on Algorithm 1? Is it possible to get a single-loop and decentralized algorithm?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors consider the problem of approximating the Nash equilibrium (NE) of a rank-one two-player game where the sum of the payoff matrices is of rank one. They prove that a modification of the optimistic mirror descent converges, used to learn a NE in zeros-sum (rank-0) games, to an \epsilon-approximate NE after O(1/\epsilon^2\log(1/\epsilon)) iterations. They achieves this by leveraging a reduction of rank-1 games to rank-0 games building on the results by Adsul et al. (2021).

### Strengths
I think the proposed algorithm and associated analysis is a natural and valuable contribution. The proofs seem correct and are easy to read as far as I checked.

### Weaknesses
The general presentation could be improved, see specific and general comments. The literature review could also be improved in particular it is not clear what is the exact contribution of this work   in comparison to the one by Adsul et al. (2021).

#General comments:

- Do you have a concrete/practical example of a rank-one game?

- It would be interesting to provide some preliminary experiments on some toy games to compare the proposed algorithm to vanilla OMWU.

- The intuition at the end of Section 1 is not very clear in particular about the fundamental connections between rank-one and rank-zero games.

- It would be clearer to introduce  definitions on the equivalence of games since many technical points rely on jumping from on formulation to another.

- How do your algorithm compare with the one of Adsul et al. (2021) in terms of rates, complexity; since both algorithms seem to solve the same problems with similar techniques.

- What can we say about rank-two games?

#Specific comments:

- P1, introduction: it is not clear what is the MVI property. And "games, We".

- P2, top: It is still not clear what is the Minty property. Maybe you can compare the rate you obtain with the rate one can obtain in a rank-0 game. Is \lambda a real parameter or also a vector? Do we really have that extra gradient and optimistic mirror descent fails to converge if the Minty property is not verified or we can just say we cannot provide any guaranties in this case?

- P3, Lemma 2.6:  what do you mean exactly by a game "can be written" in a certain form ?

- P3, end: "In the what follows"

- P5, end of Section 2.3.1: It is still not clear what is the Minty criterion.  The link between (MVI) and (VI) and when it is possible to solve (VI) with extra-gradient of optimistic mirror descent is also not clear, e.g. what do you mean by "the Minty variational inequality is satisfied'. You also talk at some point about saddle point in the context of VI. Maybe you could specialized the results for saddle point without introducing the setting of variationnal inequalities.

- P7, Algorithm 1: How do you initialize \lambda?

- P9, before Lemma 3.6: How do you initialize  \lambda, and maybe you should precise in
which interval \lambda lies.

- P13, before (8): Can you detail the second inequality. I think  you should work with the difference \lambda-xa and upper bound this difference after applying Cauchy-Schwartz inequality.

### Questions
#General comments:

- Do you have a concrete/practical example of a rank-one game?

- It would be interesting to provide some preliminary experiments on some toy games to compare the proposed algorithm to vanilla OMWU.

- The intuition at the end of Section 1 is not very clear in particular about the fundamental connections between rank-one and rank-zero games.

- It would be clearer to introduce  definitions on the equivalence of games since many technical points rely on jumping from on formulation to another.

- How do your algorithm compare with the one of Adsul et al. (2021) in terms of rates, complexity; since both algorithms seem to solve the same problems with similar techniques.

- What can we say about rank-two games?

#Specific comments:

- P1, introduction: it is not clear what is the MVI property. And "games, We".

- P2, top: It is still not clear what is the Minty property. Maybe you can compare the rate you obtain with the rate one can obtain in a rank-0 game. Is \lambda a real parameter or also a vector? Do we really have that extra gradient and optimistic mirror descent fails to converge if the Minty property is not verified or we can just say we cannot provide any guaranties in this case?

- P3, Lemma 2.6:  what do you mean exactly by a game "can be written" in a certain form ?

- P3, end: "In the what follows"

- P5, end of Section 2.3.1: It is still not clear what is the Minty criterion.  The link between (MVI) and (VI) and when it is possible to solve (VI) with extra-gradient of optimistic mirror descent is also not clear, e.g. what do you mean by "the Minty variational inequality is satisfied'. You also talk at some point about saddle point in the context of VI. Maybe you could specialized the results for saddle point without introducing the setting of variationnal inequalities.

- P7, Algorithm 1: How do you initialize \lambda?

- P9, before Lemma 3.6: How do you initialize  \lambda, and maybe you should precise in
which interval \lambda lies.

- P13, before (8): Can you detail the second inequality. I think  you should work with the difference \lambda-xa and upper bound this difference after applying Cauchy-Schwartz inequality.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
