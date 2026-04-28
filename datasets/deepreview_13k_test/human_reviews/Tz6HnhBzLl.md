# Zero-Sum Positional Differential Games as a Framework for Robust Reinforcement Learning: Deep Q-Learning Approach

- Decision: Reject
- Scores: 5, 8, 3, 6

## Abstract
Robust Reinforcement Learning (RRL) is a promising Reinforcement Learning (RL) paradigm aimed at training robust to uncertainty or disturbances models, making them more efficient for real-world applications. Following this paradigm, uncertainty or disturbances are interpreted as actions of a second adversarial agent, and thus, the problem is reduced to seeking the agents' policies robust to any opponent's actions. This paper is the first to propose considering the RRL problems within the positional differential game theory, which helps us to obtain theoretically justified intuition to develop a centralized Q-learning approach. Namely, we prove that under Isaacs's condition (sufficiently general for real-world dynamical systems), the same Q-function can be utilized as an approximate solution of both minimax and maximin Bellman equations. Based on these results, we present the Isaacs Deep Q-Network algorithms and demonstrate their superiority  compared to other baseline RRL and Multi-Agent RL algorithms in various environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper discusses RRL, Robust reinforcement learning, a recent method to incorporate physics and other constraints into the RL paradigm, such as disturbances and perturbations. Finding algorithms for RRL (modeled as an extra adversary in an multi-agent RL setting) is difficult due to non-stationarity. 

The paper introduces a shared-Q-function to compute policies, and compares their new algorithm (IDQN) to other algorithms, on a range of suitable games.

The contribution/text of the paper is mostly theoretical, proving theorems on why such an algorithm may work.

### Strengths
Robust RL is a new and under-studied problem, mostly due to the non-stationary state space. It is nice to see the problem being studied. Also nice is the part on the Isaac condition, and the derivation of the shared Q function algorithm. The experimental results comapring the performance to other algorithms is also nice

### Weaknesses
A shared-Q function algorithm is compared against non-shared Q MARL algorihtms, or to standard single agent RL algorithms such as DDQN and PPO. This is comparing apples and oranges. Of course  shared Q function algorithms outperforms the other options. As such the experimental results are not very meaningful.
Sharing the Q function is not really addressing the MARL problem of non-stationarity, it is a kind of cheating.

### Questions
I find the paper sympathetic in that it addresses Robust RL. Using a shared Q function transforms the MARL problem into a single agent problem. The pages of proofs do not contribute much to deeper understanding of the problem.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Robust Reinforcement Learning (RRL) treats uncertainty as actions of an adversarial agent, and in this paper, the authors propose a novel approach by applying positional differential game theory to develop a centralized Q-learning method. The authors demonstrate that this method can approximate solutions to both minimax and maximin Bellman equations, and they introduce two algorithms, Isaacs Deep Q-Networks (IDQN) and Decomposed Isaacs Deep Q-Networks (DIDQN). The algorithms are tested in various environments and outperform other baseline RRL and Multi-Agent RL algorithms in the experiments.

### Strengths
The paper is well-organized and involving RRL in potential differential games is a neat idea. The ideas for the experiments all seem very natural to me. The paper is also nicely organized.

### Weaknesses
I think the authors address the limitations of their own work as is.

### Questions
Q1) In Section 5, when the environments is described, what is the difference between $R$ and $\mathbb{R}$?

Q2) What are the specifications of the system used to run the experiments?

Minor comments:

I think you should name your main theorem. At the moment, you referred to it as "Theorem" and I think it would help if you name it. Either Thereom 1, Main Theorem, or some other name. Similarly, I would enumerate the remark on page 5 and maybe call it a corollary. 

I was unfamiliar with some of your notation, but if it is common in the field then you should keep it, of course. In particular, $\overline{a,b}$  to refer to the integers $a,a+1,\ldots, b$ was new to me. Similarly, I had to look up $\lim_{\delta\downarrow0}$. I merely wanted to point out that I wasn't familiar with the notation, though I guess it is not so hard to figure out from context.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper explores robust adversarial reinforcement learning (RARL) through the lens of positional differential game theory, ensuring the worst-case deterministic payoff. Leveraging the positional differential game theory, the authors formulated multi-agent reinforcement learning (MARL) to solve the RARL problem. These techniques were then benchmarked against multiple MARL baseline methods. Finally, the authors analyze the learned policies, highlighting the superior performance of the introduced algorithms.

### Strengths
This paper provides a novel perspective of RARL in the context of positional differential games.

### Weaknesses
* There is substantial room for improvement in terms of writing. There is a lack of overall organization of sections and smooth transitions between paragraphs. Some examples are:
    * In section 2, the authors could provide more insights into what is the difference between the standard formulation and differential game and why it is important to have a deterministic payoff. How the fact of the PDG is important to this paper and when the Isaacs's condition is met or not met.
    * In the experiment section, the metric of 'stability' appears without proper definition and explanation. For example, is 'stability' equivalent to 'deterministic payoff'? If so, why not just stick to the latter? 
    * In the experiment section again, some analysis seems to be out of place and is unclear how it is related to the topic. For example, "it is more efficient for agents..." What is efficiency exactly, and how is it compared across CounterDQN and MADQN?
* The reasoning and motivation for using positional differential games instead of Markov games as the framework are unclear. Markov games can be deterministic.
* The discretization of action space makes it unclear under what conditions the main theorem still holds.
* The effects of time discretization are unclear. How does it affect the estimation error or the convergence?

### Questions
* In Equ. 3, should it be $t_{m+1}$ instead of $\tau_{m+1}$?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies Robust Reinforcement Learning (RRL) within the framework of positional differential game theory, presenting a novel approach to understanding agents' robust policies and deterministic payoff values. This paper introduces two algorithms: Isaacs Deep Q-Networks (IDQN) and Decomposed Isaacs Deep Q-Networks (DIDQN). Through theoretical proofs, under the Isaacs’s condition, it shows that a centralized Q-learning approach can be developed for these problems. Empirical results underscore the effectiveness of these algorithms against other RRL and Multi-Agent RL baselines, also proposing a new framework for evaluating the robustness of trained policies.

### Strengths
Firstly, it offers an exhaustive literature review, meticulously drawing contrasts between the current work and existing literature. Moreover, the clarity of writing facilitates comprehension, making the paper accessible to a broad spectrum of readers. Lastly, the experimental results provided is convincing, adding weight to the authors' arguments and hypotheses.

### Weaknesses
1. While the authors adeptly show the significance of considering robustness in RL in the introduction, they do not clearly state why there's a pressing need to study robustness in the framework of positional differential game theory. This oversight makes the paper's motivation less pronounced and leaves readers questioning the specific choice of this framework.

2. One point of confusion for me is in Section 3 where the authors state that "to solve differential games by RL algorithms, it is necessary to discretize them in time，we describe such a discretization...". If employing RL to address differential games still necessitates discretization, then why consider robust RL problems within the framework of differential games? Wouldn't it be more straightforward to tackle the issue directly within the framework of discrete robust MDPs? What additional advantages does considering robustness in differential games provide? Furthermore, how does the efficacy of using discretization to address differential games compare with directly solving a discrete robust MDP?

### Questions
Please see the Weaknesses, I will finalize my rating after rebuttal.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
