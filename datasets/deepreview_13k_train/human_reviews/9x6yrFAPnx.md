# Provably Efficient CVaR RL in Low-rank MDPs

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
We study risk-sensitive Reinforcement Learning (RL), where we aim to maximize
the Conditional Value at Risk (CVaR) with a fixed risk tolerance $\tau$. 
Prior theoretical work studying risk-sensitive RL focuses on the tabular Markov Decision Processes (MDPs) setting.  
To extend CVaR RL to settings where state space is large, function approximation must be deployed. 
We study CVaR RL in low-rank MDPs with nonlinear function approximation.  Low-rank MDPs assume the underlying transition kernel admits a low-rank decomposition, but unlike prior linear models, low-rank MDPs do not assume the feature or state-action representation is known. 
We propose a novel Upper Confidence Bound (UCB) bonus-driven algorithm to carefully balance the interplay between exploration, exploitation, and representation learning in CVaR RL. 
We prove that our algorithm achieves a sample complexity of $\tilde{O}\left(\frac{H^7 A^2 d^4}{\tau^2 \epsilon^2}\right)$ to yield an $\epsilon$-optimal CVaR, where $H$ is the length of each episode, $A$ is the capacity of action space, and $d$ is the dimension of representations.
Computational-wise, we design a novel discretized Least-Squares Value Iteration (LSVI) algorithm for the CVaR objective as the planning oracle and show that we can find the near-optimal policy in a polynomial running time with a Maximum Likelihood Estimation oracle. 
To our knowledge, this is the first provably efficient CVaR RL algorithm in low-rank MDPs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies risk-sensitive RL in in low-rank MDPs with nonlinear function approximation, where the goals is to maximize the Conditional Value at Risk (CVaR). The authors proposed ELA (REprensentation Learning for CVAR) as shown in Algorithm 1, which contains a MLE oracle and uses UCB-based bonus to do exploration. They proved that the sample complexity of ELA is $\tilde{O}(1/\epsilon^2)$ The authors then proposed ELLA (REprensentation Learning with LSVI for CVAR) algorithm, which leverages least-squares value iteration to improve computationally efficiency.

### Strengths
1. The problem of study is interesting, i.e., risk-sensitive RL in in low-rank MDPs.
2. The presentation is clear and easy to understand.
3. Results seem reasonable and novel to me.

### Weaknesses
1. The proposed and improved algorithms are computationally inefficient in the sense that they still require to call MLE oracles.

### Questions
1. In Algorithm 1, for the part of collecting two transition tuples, could you explain why using different policies to sample the two actions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors propose the Representation Learning for CVaR (ELA) algorithm for maximizing the Conditional Value at Risk (CVaR) in low rank Markov decision processes (MDPs). The authors then propose a modification of the ELA algorithm, called ELLA, that improves upon the computational complexity of the former. The authors then provide probably approximate correct (PAC) guarantees for both ELA and ELLA.

### Strengths
The authors do a good job in introducing both risk sensitive RL and the CVaR objective in Low Rank MDPs. The main result for the ELA algorithm and its ensuing discussion are also well-written. Furthermore the authors partially address one the problems posed in Wang et al, 2023 [1] on whether their minimax CVaR guarantees for tabular MDPs can be extended to low rank MDPs. 

Also the introduction and related works do a nice job of setting up the problem and informing the reader on the current state of CVaR and risk-sensitive RL.

### Weaknesses
The main weakness of this work lies in the tightness of their guarantees. While the authors provide upper bounds for their ELA and ELLA algorithms, they do not provide lower bounds for CVaR in low rank MDPs. Therefore it is hard to see whether the bound the authors propose is reasonable (see questions for further details).

Another weakness is in the writing of section 4.1. This is a very weird policy to me. First the agent follows the policy to state $s_h$ then takes a uniform action $a_h \sim U(\mathcal{A})$ and receives the next state $s_{h-1} \sim P_h(\cdot | s_h,a_h)$. If the agent is taking uniform actions in step $h$ then how is it following policy $\pi_k$. Wasn't $s_h$ the state the resulted in taking a uniform action $a_{h-1}$ in the previous state $s_h$? Anyways maybe I missed something here but this seems very weird?

### Questions
Aside from the questions mentioned in the weaknesses section, I also want to ask where the novelty in this work lies. This work seems like it combines the setting and results of Wang et al, 2023 [1] and Uehara et al, 2021 [2]. What, if anything, needs to change? Does your results nicely follow from adapting the REP-UCB algorithm Uehara et al, 2021 [2] with the CVaR bonus of Wang et al, 2023 [1]? 

Also, if you consider time-homogenous transitions as was done in Uehara et al, 2021[2] do you match their dependency on $H$? Also do you think your dependence on $d$ and $H$ are tight? If yes, then why? If no, then where to do think this looseness arises from and how can it be improved?

[1] Wang, Kaiwen, Nathan Kallus, and Wen Sun. "Near-Minimax-Optimal Risk-Sensitive Reinforcement Learning with CVaR." arXiv preprint arXiv:2302.03201 (2023).

[2] Uehara, Masatoshi, Xuezhou Zhang, and Wen Sun. "Representation learning for online and offline rl in low-rank mdps." arXiv preprint arXiv:2110.04652 (2021).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies risk-sensitive Reinforcement Learning (RL) in the context of low-rank Markov Decision Processes (MDPs), employing the Conditional Value at Risk (CVaR) risk metric. The proposed algorithm bears resemblance to value iteration techniques, incorporating exploration bonuses based on the Upper Confidence Bound (UCB) principle, a well-established concept within the field of RL. Furthermore, the authors introduce a discretized variant of the least-squares value iteration approach and demonstrate its capacity to approach near-optimal policy solutions within a polynomial computational time framework, given access to a Maximum Likelihood Estimation (MLE) oracle. This novel contribution enhances the body of knowledge in this area of research, delivering valuable insights to the academic community.

### Strengths
(+) The paper is generally well-written and the technical exposition is overall sound.  

(+) I personally find the computationally efficient algorithm a nice addition to the paper. I do not see any citations in Section 5 so I assume that these are novel contributions of the authors.

### Weaknesses
(-) In Section 4.1, it is mentioned that the algorithm requires two sets of trajectories. Is it true that a *simulator is required* to obtain these two sets? By simulator, I meant the ability to draw samples from the *true* transition probability $P^*_h$. If this is indeed required, it is a major assumption that the authors fail to disclose in the abstract or in a formal statement. I strongly encourage the authors to highlight this fact.

(-) Again, suppose my understanding of the above is correct. In that case, the result becomes fairly trivial: combining the realizability assumptions with a finite model class (assumption 3.2) with access to a simulator, it is easy to see that given enough samples, any algorithm is no-regret. Nevertheless, there is still credit in proving finite-sample regret bounds in Theorem 4.1.

(-) The claim that this is the first provably efficient CVaR RL algorithm is incorrect. There have been regret bounds for CVaR RL in function approximation settings in the literature. 

(-) I also encourage the author to at least discuss the difference between dynamic and static CVaR, as this has non-trivial implications in algorithm design and theoretical analysis.

### Questions
Please see the above section and correct me if I misunderstood some results. I am happy to increase my score if that is the case.

### Soundness
3 good

### Presentation
3 good

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
This paper study risk-sensitive Reinforcement Learning under low-rank MDPs, where the transitions of MDPs admit a low-rank decomposition into two unknown low-dimension embedding functions and the goal is to maximize the conditional value at risk (CVaR) with certain risk $\tau$. This paper first propose an efficient upper confidence bound type algorithm and then provide regret bound $\tilde{\mathcal{O}}(\frac{H^7A^2d^4}{\tau^2\epsilon^2})$. In addition, this paper disigns a computational efficient LSVI algorithm for planning.

### Strengths
1. This paper propose an agorithm with theoretical regret bound, which is new for CVaR RL under low-rank MDPs.

2. This paper propose an computational efficient algorithm for planning.

3. The presentation of this paper is easy to follow and clear notations tables are provided.

### Weaknesses
1. My main concern is that the algorithm 1 is quite close to [1]. It seems that algorithm 1 is just an application of REP-UCB in Augmented MDPs. The analysis of regret bound is also similar to [1], with only difference to convert CVaR into value function (as Eq. (13) in Page 17), which makes the result not so surprising and significant. It is likely that I miss some novel analysis techniques, so please bring it out and I think it is also important to stress the novelty in the paper.

2. The authors claim the worse dependency of regret bound on $H^7$ is due to the non-stationary transitions in Page 7. I want to point out it may be wrong. Another previous work considers regular low-rank MDPs with finite horizons and time-dependent transition kernels [2], which is the same as this paper, even has better dependence on $H^3$. It is likely that the worse dependency on $H$ of this paper is due that [1,2] assume that the accumulative discounted reward is in $[0,1]$ and this paper only assumes $[0,H]$. I guess that applying similar assumptions and techniques to clip value functions in [2], the regret bound may acheive the same dependence on $H^3$.

3. Based on the two points above, I think the authors can try to enhence this paper by buliding a lower bound of CVaR RL under low-rank MDPs with better dependence on $	au$, or try to improve the algorithm to better regret bound.

### Questions
Could the authors also provide some motivation examples of CVaR RL under low-rank MDPs? It will help the readers to understand the significance of this setting and how this formulation is related to real-world applications.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
