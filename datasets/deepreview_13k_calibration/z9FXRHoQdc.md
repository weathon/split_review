# Best Response Shaping

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3

## Abstract
We investigate the challenge of multi-agent deep reinforcement learning in partially competitive environments, where traditional methods struggle to foster reciprocity-based cooperation. LOLA and POLA agents learn reciprocity-based cooperative policies by differentiation through a few look-ahead optimization steps of their opponent. However, there is a key limitation in these techniques. Because they consider a few optimization steps, a learning opponent that takes many steps to optimize its return may exploit them. In response, we introduce a novel approach, Best Response Shaping (BRS), which differentiates through an opponent approximating the best response, termed the "detective."  To condition the detective on the agent's policy for complex games we propose a state-aware differentiable conditioning mechanism, facilitated by a question answering (QA) method that extracts a representation of the agent based on its behaviour on specific environment states. To empirically validate our method, we showcase its enhanced performance against a Monte Carlo Tree Search (MCTS) opponent, which serves as an approximation to the best response in the Coin Game. This work expands the applicability of multi-agent RL in partially competitive environments and provides a new pathway towards achieving improved social welfare in general sum games.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a new opponent modelling tool which differentiates through a constructed opponent that approximates the
agent's best response policy in a best-response algorithm-like manner. The paper include various empirical evaluations to validate the proposed mechanisms.

### Strengths
The paper introduces a neat method for overcoming some of the weaknesses in current opponent modelling approaches. The paper is both well-written and well structured with good empirical results to support the authors' claims.

### Weaknesses
 **Missing references**

Some important references have been missed such as [1] and [2].
For example [1] introduces a method for incorporating diversity into best-response dynamics leading to a diverse fictitious play/diverse best response dynamics. Since fictitious play is based on a type of best-response method, a discussion on how the authors’ paper compares to [1] is needed to be able to properly evaluate the authors’ current contribution.

**Limitations**
It seems that method requires the agent to have access to the detectives received rewards (and vice-versa) – this seems to limit the application to various non-cooperative multi-agent settings where at least the reward may be privately received.

In the abstract, the authors state the focus of the paper is in partially-competitive games, however the study of the cooperation regularization method does not shed any light on games that may be of mixed character (for example games in which $r^1(s,\cdot)=-r^2(s,\cdot)$ and $r^1(s',\cdot)=r^2(s',\cdot)+k$ for $s\neq s'$).

In the conclusion, the authors state that one of the aims is improving the scalability and non-exploitability of agents. However, it is unclear about the practicalities of such a method in larger scale games as well as how it could ever be adapted beyond two-player games.

### Questions
Q1: How does the method compare to other approaches that introduce diversity into opponent modelling such as [1] and [2]?

Q2: Can the authors comment on whether or not (and how) this could be applied in games where the opponent’s rewards are unobserved?

Q3: Although the cooperation regularization method yields a useful tool that does not produce cooperative effects in zero-sum games, its effect in games in which some game states the players ought to behave adversarially and other game states cooperatively (for example the weakest link) is unclear to me. Can the authors shed any light on this?

[1] Perez-Nieves, Nicolas, et al. "Modelling behavioural diversity for learning in open-ended games." International conference on machine learning. PMLR, 2021.
[2] Yang, Yaodong, et al. "Multi-agent determinantal q-learning." International Conference on Machine Learning. PMLR, 2020.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce a new scalable method to tackle general-sum games called Best Response Shaping (BRS). BRS works by differentiating through an opponent that is approximating a best response. They introduce a way for the detective to condition on the agent's policy through question answering. They show promising results in the IPD and Coin Game.

### Strengths
Originality:

The author's proposed method is original and builds and contributes on top of prior work. The "detective" mechanism is an interesting approach to approximating the best response that I have not seen in previous literature.

Quality:

The author's evaluate in the challenging Coin Game environment and the IPD and run a large number of relevant ablatoins. 

Clarity:

The authors describe the IPD, Coin Game, and related literature in depth.

Significance:

AI systems that perform well in general-sum scenarios are becoming increasingly important as AI systems become more widely-deployed.

### Weaknesses
Originality:

The author's proposed method is original and builds and contributes on top of prior work. The "detective" mechanism is an interesting approach to approximating the best response that I have not seen in previous literature.

- The training paradigm described here is closely related to [PSRO](https://arxiv.org/pdf/1711.00832.pdf), which is not mentioned in the paper. The core idea of iteratively adding a best response to a policy set and retraining is very similar. While the authors differentiate through the best response, the high-level training loop is very similar to PSRO, and the lack of discussion is a significant oversight.

Quality:

The author's evaluate in the challenging Coin Game environment and the IPD and run a large number of relevant ablatoins.

Clarity:

The authors describe the IPD, Coin Game, and related literature in depth.

- The writing does not make it clear that the detective and agent take turns during optimization. The title of Algorithm 1 (that it says "a single iteration") is the *only* way I knew that this is how the training is done. Otherwise, it seems as though the detective is first trained on a pre-selected buffer B, which *significantly changes the reader's understanding of the method*.

- Section 4.1 and 4.2 really make it seem like the detective is pre-trained when it is not.

- BRS-NOSP is an important part of Figure 2, but is not defined until significantly later.

- It's still not clear which player is $\theta_1$ and which is $\theta_2$. Presumably the agent would be $\theta_1$ and the detective would be $\theta_2$, but that is flipped in Equation 4 where $\theta_r$ takes the place of $\theta_1$ but actually represents the detective and the agent is now $\theta_2$ (?)

- The whole description of "Simulation-Based Question Answering" makes the setup far more confusing than it needs to be. Here is my understanding: The conditioning vector consists of the Q-Values of each action of a random opponent policy in that state. The Q-Values are estimated by sampling trajectories. It is not described in the paper like this, and is instead treated as a complicated "Question-Answering" scheme.

- Describing and defining $\delta_A$ before describing or motivating what $Q^\text{simulation}$ was confusing as a reader, as it is uncertain how $\delta_A$ is related to anything.

- It's unclear why the authors have a paragraph about Diplomacy in the related work and a paragraph about self-play from human data. It's fine to include it, but the authors should explain, *in the paper*, why they include it.

- The authors do not write out the bi-level optimization in Equation 12, making it seem like a single-level optimization. Writing it out would make this significantly more clear that it's a bi-level process.

Significance:

AI systems that perform well in general-sum scenarios are becoming increasingly important as AI systems become more widely-deployed.

Quality:

- The analysis is only done on three seeds (stated in the Appendix). This is  small, considering the high variance we observe from POLA. Using more seeds for POLA because the authors "observed higher variance" is problematic from a statistical point of view. (See: Stopping rules in statistics).

- The authors state that "in this paper, [they] advocate that a reasonable point of comparison is the agent’s outcome when facing a best response opponent, which we approximate by Monte Carlo Tree Search (MCTS)." I cannot find where in the paper the authors advocate for this. This is a significant claim, since arguably POLA and LOLA are not interested in this setting as much and seem to be far more interested in learning *online* against opponents that are also *learning online*. This is rather important, as it makes head-to-head comparisons with POLA a bit more questionable, seeing as it was designed for a different setting.

Significance:

- BRS is *more exploitable than POLA* in Figure 3 against AD, seemingly contradicting the purpose of the paper. BRS-NOSP performs better, but at the cost of social welfare. However, I understand that you can't get the best of everything in general-sum games (See Q4 below).

- The authors collected head-to-head results of POLA and BRS (in the Appendix Figure 7), but have elected not to show them in the main text. It seems as though POLA outperforms BRS in the head-to-head, further indicating that BRS is exploitable.

- The authors write that the Good Shepherd is not scalable; however, their approach also seems similarly difficult to scale. (See Q3: below). What is the sample efficiency in terms of simulated environment steps?

### Questions
1. Why not just train directly against the MCTS opponent?

2. BRS-NORB performs near-identically to BRS in Figure 4 and is *significantly simpler*. Why not just make the method BRS-NORB?

3. Isn't calculating $\delta_A$ at every single timestep extremely expensive and not very scalable? What is the sample efficiency of BRS in terms of the total number of simulator steps? 

4. Why did you run head-to-head results for the BRS variants and POLA in the Appendix, but not include them in the main text? I understand that evaluations in general-sum games can be odd, since the ultimate objective is not well-defined. I would be more convinced that BRS is valuable if there was a more explicit metric demonstrating reciprocity.

5. What is the intuition for the choice of conditioning? Why is an estimate of Q-Values of a random policy in the current state a good metric?

6. Misc: What is the reasoning for the separate optimizers? (Equation 8). Have you ablated this?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel opponent-aware framework to improve cooperation. The framework involves training a detective to approximate the opponent, training the agent based on the interaction between the detective and agent, and conducting self-play to learn to cooperate. The experiments demonstrate that the proposed method can improve social welfare.

### Strengths
1) The proposed method that involves training a detective to help training the agent is interesting.

### Weaknesses
1) My major concern is that the explanation why BRS outperforms POLA is not very clear. The authors mention that "When the opponent is specifically trained to maximize its own return against a fixed policy trained by POLA, the first exploits the former." However, it is not clear whether this issue would be avoided when POLA is replaced by the proposed BRS. Specifically, the paper lacks a detailed analysis of how the detective network in BRS prevents exploitation by a learning opponent, and whether the detective's approximation of the opponent is sufficiently accurate to guarantee this. Additionally, the paper claims that "POLA can't differentiate through all opponent optimization steps," but more experiments are needed to support this claim, such as ablating the number of opponent optimization steps used by POLA and showing the impact on performance. Besides, the authors also state that "the interactions between the agent and the detective mirror the foundational Stackelberg setup," but it is still not clear whether convergence to Stackelberg equilibrium helps to improve social welfare. The paper needs to provide a more rigorous argument or empirical evidence that the Stackelberg equilibrium induced by the detective-agent interaction leads to better cooperation than other equilibrium concepts. More detailed analysis is needed to clarify these points.

2) Recently, [1] proposed a method for reasoning about players' future strategy through multiple lookahead steps. This suggests that scalability issues for POLA (or other related works) may not be a serious problem. It would be helpful if the authors could discuss some details about [1], specifically addressing how the proposed method compares in terms of computational complexity and performance when considering multiple lookahead steps. The discussion should also include whether the proposed method can be extended to incorporate similar lookahead mechanisms.

3) The training curves for baselines and proposed methods are missing. Also it would be helpful to test the proposed method in more complicated social dilemma environments, such as those presented in [2]. The current experiments are limited to relatively simple environments, and it is not clear how the proposed method would perform in more complex scenarios with larger state and action spaces, and more nuanced social dynamics. It would be beneficial to include experiments in environments with varying degrees of difficulty and different types of social dilemmas to assess the robustness and generalizability of the proposed method.

4) Some typos need to be fixed, including Alg 1., $\theta_1' \leftarrow \theta_1+z$ should be $\theta_1 \leftarrow \theta_1+z$.

### Questions
1) In Corollary D.3, the paper uses $r^1\left(s_t, a_t, b_t\right)+r^2\left(s_t, b_t, a_t\right)=0$ which implies $R^1(\tau)=-R^2(\tau)$. However, in proposition D.2, the authors use Lemma D.1 which assumes $r^1\left(s_t, a_t, b_t\right)=r^2\left(o_t, b_t, a_t\right)$ so as to imply  ${\mathbb{E}}\left[R^1(\tau)\right]={\mathbb{E}}\left[R^2(\tau)\right]$. Since Corollary D.3. also involves proposition D.2,This creates a potential inconsistency, and the proof of Corollary D.3 may not be correct. The authors are requested to provide clarification on this matter.






References:

[1] Recursive Reasoning in Minimax Games: A Level k Gradient Play Method

[2] Multi-agent Reinforcement Learning in Sequential Social Dilemmas

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a learning method to discover an NE solution that discovers maximum social welfare. The idea extends the LOLA and POLA works by directly applying MARL with backpropagation through the entire opponent policy. The experiments are conducted on the IPD game and the coin game.

### Strengths
In general, I appreciate the attempt to extend the existing works further, from a few RL steps to the policy change via policy conditioning. However, the paper has significant technique issues.

### Weaknesses
### Fundamental Issue

The fundamental issue of this work is that the paper directly assumes **symmetric NEs** throughout the entire paper. If we know **in advance** that the desire NE **must** be symmetric, then all the technical derivations in this paper are correct. However, although IPD falls into this category, this remains an extremely strong assumption and you cannot really leverage this assumption during algorithmic design, which, to some extent, is a cheating strategy. 

I want to remark that LOLA does not adopt parameter sharing during learning. 

I also want to mention that a symmetric game does not mean that the NE is symmetric. Let's consider a particular symmetric 2-player matrix game with a payoff matrix as
```
(0, 0), (1,1)
(1,1), (0,0)
```
This is an XOR game where the NE should be two agents taking different actions, which cannot represented by policies with shared parameters. You may refer to [this paper](https://arxiv.org/abs/2206.07505) for a discussion on the XOR game.

Another example would be a modified chicken game as shown below. 
```
(0, 0), (0,1)
(1,0), (-1,-1)
```
The NE solution is the same as the XOR game. 

I also want to point out that the claims in Section 4.3.2 are particularly problematic. 
1. "_this is equivalent to training an agent with self-play with reward sharing_". This claim is **wrong**. Equation (7) is only equivalent to **reward sharing _with parameter sharing_**. "Self-play with reward sharing'' should refer to the case where "you learn two different policies with different parameters while the game reward is shared across agents". So, self-play with reward sharing should be able to learn an NE in the XOR game while equation 7 can never due to parameter sharing
2. "_In zero-sum games, this update will have no effect as the gradient would be zero_". To be frank, I was deeply shocked by such a conclusion at the very beginning when I read this sentence. Then I find it correct but meaningless: in a symmetric and zero-sum game, the expected reward is always 0 when the players use identical policies, which means you have zero gradient everywhere. 

Finally, the concept of _symmetric game_ only applies to two-player games. For general $N$-player games, you are essentially assuming the game is cooperative. 

### Minor Issues

1. Section 2.1 presents a $N$-player game formulation. However, the entire paper adopts a two-player setting. 
2. At the end of section 4.1, it is stated that "_Note that ($	heta^{∗∗1}$, $	heta^{∗2}$) is a nash equilibrium by definition._" This sounds wrong to me. An NE should be defined over a minimax operator rather than two separate equations. A simple counter-example here is the rock-paper-scissor game. Suppose initially you have $	heta^1$ to be rock. Then $	heta^{*2}$ will be paper, and $	heta^{∗∗1}$ becomes scissor, which is clearly not an NE. 
3. The presentation of Section 4.2 is hard to follow. A few examples. What do you mean by "detective’s conditioning"? I would be better to have a formulation of what you want to present. It is also mentioned "the behavior of the agent against a random agent" in Section 4.2.2. Here the word "agent" is mentioned twice. So which is agent 1 and which is agent 2? I guess you are using agent to refer to agent 1 while the detective to agent 2 but it is not always consistent. 
4. There are also notation issues. I'm always confused by which agent an action refers to. Moreover, in Equation 6, $b$ is used to denote the action from agent 2. However, the notation of $b$ is never introduced before.

### Questions
First of all, I think the paper should be substantially rewritten.

Besides, I would be also curious about how your algorithm will perform on cases where (1) the NE is asymmetric and (2) the parameter sharing is turned off, i.e., two agents have two separate policies.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
