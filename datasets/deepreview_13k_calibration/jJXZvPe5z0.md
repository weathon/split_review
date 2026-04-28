# On the Convergence of No-Regret Dynamics in Information Retrieval Games with Proportional Ranking Functions

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Publishers who publish their content on the web act strategically, in a behavior that can be modeled within the online learning framework. 
Regret, a central concept in machine learning, serves as a canonical measure for assessing the performance of learning agents within this framework.
We prove that any proportional content ranking function with a concave activation function induces games in which no-regret learning dynamics converge. 
Moreover, for proportional ranking functions, we prove the equivalence of the concavity of the activation function, the social concavity of the induced games and the concavity of the induced games.
We also study the empirical trade-offs between publishers' and users' welfare, under different choices of the activation function, using a state-of-the-art no-regret dynamics algorithm. Furthermore, we demonstrate how the choice of the ranking function and changes in the ecosystem structure affect these welfare measures, as well as the dynamics' convergence rate.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper examines strategic behavior in recommender systems, focusing on how content providers adapt their strategies to maximize visibility under different ranking principles. WIth a game-theoretic framework, the authors look at no-regret learning dynamics when competing for exposure. The authors then explore how these rankers impact stability (Nash equilibrium) of the resulting dynamics, and the issue of strategy convergence. The contributions of the paper include: 1. modeling SEO as a game: The authors introduce a new class of ranking functions termed proportional ranking functions and formulate the corresponding game-theoretic framework, 2. by employing the concept of socially concave games, the authors show that if the activation function in the ranking mechanism is concave, the no-regret learning dynamics will converge, thus ensuring stability.

### Strengths
The paper models the strategic interactions among content producers as an information retrieval game. By defining key concepts such as no-regret dynamics, concave games, socially concave games, proportional ranking functions (PRF), the authors provide technical proofs and establish conditions under which PRF induces stable equilibrium and guarantees the convergence of any no-regret dynamics. The main theorem and its insight are presented clearly. Overall I think this paper brings an interesting insight, especially the new concept PRF. I'm curious to see the potential of PRF in real-world applications.

### Weaknesses
1. There might be a major technical flaw in Lemma 1. Since the socially concave game is a subclass of concave game, when one tries to verify the social-concavity of $u_i$, one should also verify that $u_i(x_i, x_{-i})$ is concave in $x_i$. However, neither the Definition 1 nor the proof of Lemma 1 considers this criterion. In fact, I think this loophole might not be easy to fix: the concavity of $g$ and convexity of $d$ are not sufficient to guarantee that a function of the form $r(x_i, x_{-i})=\frac{g(d(x_i))}{g(d(x_i))+C}$ is concave in $x_i$ (one can easily come up with counterexamples). One possible fix is to assume that $\lambda_i$ is sufficiently large so that even if we do not know the concavity of $\frac{g(d(x))}{g(d(x))+C}$, $\frac{g(d(x))}{g(d(x))+C}-\lambda_i d(x_i)$ can still be concave due to the convexity of d(x_i). However, the dominance of the cost term in the utility model does not make much sense to me. I hope the authors explain this issue in detail in the response, otherwise, this flaw renders the main theoretical result in Theorem 2 groundless as well. 

2. The stability guarantee offered by the socially concave property is a weak one in my perspective and does not provide sufficient real-world implications. As the authors acknowledged in L. 168, only the average strategy sequence over time converges to the Nash equilibrium. This means it does not guarantee the last-iterate convergence (the most common convergence concept in practice) since it does not preclude the cycling pattern of strategies (which is commonly observed in many game structures, e.g., in [1], gradient dynamics can cycle in minimax zero-sum game). Such a weak notion of convergence makes me skeptical about the significance of the theoretical result.

3. Insufficient related work. This paper tries to study no-regret dynamics running on a proposed SEO game which is socially concave: 
- Socially concave game is not a new concept: it is actually widely known as a criterion to verify monotone games (which is also a subclass of concave games and are extensively studied due to its provided nice convergence properties [2, 7]). The discussion of socially concave games can be found in appendix A.2 of [2], though without explicitly mentioning its name, and also [3]. I'm wondering since there are many works providing alternative dynamics that guarantee stronger last-iterate convergence in monotone (and thus socially concave) games, why the author insisted in establishing a weaker convergence result under no-regret dynamics. 
- Some related studies propose similar game structures modeling competition among content publishers, with a guarantee that the resulting game is monotone (see [4,5] and possibly more). 
- In addition, no-regret dynamics and their convergence in similar content publisher games are studied in [6].

### Questions
Please address my comments and concerns raised in the weakness.

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
4

### Summary
This paper considers the game among strategic content publishers in information retrieval systems (like search engines and recommender systems), where each publisher strategically chooses a document to maximize exposure minus the distance of the chosen document and their initial document. 
The authors theoretically prove that: if the content ranking function (recommendation policy) is a proportional function with concave activation, then the game is a concave game, thus admitting a pure Nash equilibrium that can be reached by no-regret learning dynamics of the publishers. Simulations with different concave ranking functions validate the equilibrium convergence result, and demonstrate a tradeoff between the publisher welfare and the user welfare.

### Strengths
(S1) I really like the big question/motivation of this work: how to design a content ranking function to induce a publisher game that admit a stable/learnable equilibrium. While previous work like (Yao et al (2024)) considered how to induce stable equilibrium using payment to the publishers, this paper takes a different and novel approach of using content ranking function, which seems to be very useful in applications where payments are not allowed. 

(S2) The theoretical results are solid and not very straightforward. 

(S3) Writing is very clear.

### Weaknesses
However, I think there are some theoretical and experimental limitations in this work.

Theoretical:

(W1) The main result shown by the authors (a concave ranking function can induce a publisher game with a learnable/stable equilibrium), although is not very straightforward, largely follows from the classical concave game theory.  Another practically relevant and technically interesting question is the welfare property of the learned equilibrium.  Unfortunately, the authors didn't provide any welfare characterization theoretically.  For example, can you prove a "price of anarchy" bound for the equilibrium? Can you characterize the publisher-user welfare tradeoff? Specifically, it would be valuable to understand how the equilibrium outcome compares to a socially optimal outcome, and whether the decentralized nature of the game leads to significant inefficiencies. A formal analysis of the price of anarchy, or similar welfare bounds, would provide a more complete understanding of the implications of the proposed approach. Furthermore, exploring the impact of different concave activation functions on the welfare properties would be beneficial.


Experimental: 

(W2) Some parts of the simulation setup feel unnatural:

(W2.1) First, why do you first sample a small number $s$ of information needs and then consider the discrete uniform distribution on those $s$ points?  This does not seem to capture the real world where the demand distribution spans across a large range, with $s$ being millions (if I interpret each point as an Internet user).  Why don't you just let the demand distribution be a continuous distribution with support being the full unit cube $[0, 1]^k$?  Using a discrete uniform distribution over a small number of sampled points artificially limits the diversity of user preferences and may not accurately reflect the complex, high-dimensional nature of real-world information needs. This simplification could lead to results that do not generalize well to more realistic scenarios. A continuous distribution, such as a Gaussian mixture model or a uniform distribution over the unit cube, would provide a more robust and representative evaluation.

(W2.2) Second, the number of publishers $n$ is too small (<=10). You observed that the user welfare decreases with $n$ because "publishers adhere to their initial documents more when $n$ increases".  However, if $n$ becomes much larger, the $n$ publishers can cover a large space in the unit cube $[0, 1]^k$, which means that the information needs of different users should be more easily satisfied.  So we might see a "U" curve for user welfare.  I'm afraid that your observation of "user welfare decreasing with $n$" is an artifact of too-small $n$ or the choice of discrete demand distribution as I said in (W2.1). The current experimental setup does not explore the potential for increased user welfare as the number of publishers grows and the coverage of the space of information needs becomes more comprehensive. The observed trend might be specific to the limited number of publishers considered and not a generalizable property of the system. It would be crucial to investigate the behavior of the system with a significantly larger number of publishers to determine if the user welfare exhibits a different trend, such as the hypothesized U-shaped curve.

### Questions
**Questions:**

(Q1) See (W1).

(Q2) See (W2).

(Q3) How do you choose publishers' initial document $x_0^i$ in simulations? 

(Q4) I thought the goal of the "Equilibrium strategy learning" paragraph is to show that the strategies of the publishers not only time-average converge to equilibrium, but also last-iterate converge.  But I don't see how this goal is achieved by Proposition 1.  The $x^{eq}_i$ in Proposition 1 is still a time-average strategy, not last-iterate strategy.  An alternative argument to achieve this goal might be the following: Suppose the game has a unique NE $x$ (which is guaranteed under some conditions in Corollary 1). If the publishers' average strategies converge to $x$, then the last iteration strategies must converge to the same limit point $x$ as well. 



**Suggestions:**

- Equation (4): is $d_i^0(x_i)$ equal to $d(x_i, x^i_0)$? 

- As the authors mentioned, a limitation of this work is that the demand distribution $P^*$ if stationary.  Another future direction could be what if the demand distribution can change in response to the strategies played by the publishers. In recommender systems, for example, users' preferences (demand) can change due to the recommended content they see [1, 2].

[1] Dean & Morgenstern. Preference Dynamics under Personalized Recommendations. EC 2022.

[2] Lin et al. User-Creator Feature Polarization in Recommender Systems with Dual Influence. 2024.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the strategic behavior of content creators in an independently mediated recommendation platform from a game theoretic lens. In this setting, the goal of the any content creators is to maximize their exposure to an arriving user by the recommendation platform which uses a ranking function to map the creators’ contents to a distribution over all the creators (which becomes the exposure of their content to the arriving user). The content creators strategies (i.e. the content they produce), as well as the information needs of the arriving user are modeled as vectors in the same embedding space (a common assumption in dense retrieval) endowed with some semi-metric for measuring the distance (relevance) between a creators content and the users requirement. It is further assumed that each content creator has an initial piece of content (a base vector) that they can modify to increase the exposure of this document to the arriving user by the ranking algorithm. However, it is further assumed that the creators want to maintain the integrity of their initial document - i.e. the modified document should not be too far away (in terms of the semi-metric distance) from their initial document. This is modeled by assuming that the utility of the content creator which is their exposure of their (modified) content to the user by the ranking algorithm, is further penalized (linearly) by the distance of the modified document from the original document. In this general setting, the authors aim to understand the learning dynamics of the content creators if the creators were to employ a no-regret learning algorithm for minimizing their regret (defined over their utility). 

In this setting, the authors show that if the recommendation platform were to use a particular kind of a ranking function, which they term “proportional ranking function”, then the resultant game has several desirable properties. This proportional ranking function is a function that loosely converts the vector of distances of the content creators documents from the users information requirement into a distribution, and has a form that structurally looks like the softmax, but is more general as it allows for more general activation functions. In particular, the authors show that if the activation function within this proportional ranking function is concave, then the resultant game has a nash equilibrium, and moreover, the learning dynamics will converge to it if every player employs any regret minimization algorithm that achieves sublinear regret. 

The authors validate their theoretical guarantees with simulations, experimenting with proportional ranking functions with different activation functions. They experimentally analyze the effect of several parameters within their model, such as the dimensionality of the embedding space, the penalty factor (that penalizes the distance of the modified documents from the initial document in the creators utility functions), and the number of publishers.

### Strengths
I really enjoyed reading this paper. The exposition is very clear and it was very easy for me to follow, despite me having relatively little exposure to algorithmic game theory. I do believe this work is impactful, as it is important to understand how the content providers are going to strategize on search platforms. The way I see it, this provides some guidelines for what kind of ranking functions may be used for search ranking. That being said, this is not my primary area of research, and I will leave the judgement of novelty to other more knowledgeable reviewers.

### Weaknesses
That biggest limitation I see with this work is the form the utility function takes: it is a linear function that is the expected exposure of the document penalized by the distance from the initial document with some penalty factor. In practice, I assume the utilities of the content creators would be some more complicated payoff structure that may not necessarily increase linearly with exposure. Do the authors have any ideas as to what the learning dynamics would look like for more general utilities that are monotone, but not necessarily linear in the exposure, or what technical barriers might be faced that might make studying this difficult?

### Questions
None

### Soundness
4

### Presentation
4

### Contribution
3
