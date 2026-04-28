# Dual RL: Unification and New Methods for Reinforcement and Imitation Learning

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 8, 6, 1

## Abstract
The goal of reinforcement learning (RL) is to find a policy that maximizes the expected cumulative return. It has been shown that this objective can be represented as an optimization problem of state-action visitation distribution under linear constraints. The dual problem of this formulation, which we refer to as \textit{dual RL}, is unconstrained and easier to optimize. In this work, we first cast several state-of-the-art offline RL and offline imitation learning (IL) algorithms as instances of dual RL approaches with shared structures. Such unification allows us to identify the root cause of the shortcomings of prior methods. For offline IL, our analysis shows that prior methods are based on a restrictive coverage assumption that greatly limits their performance in practice. To fix this limitation, we propose a new discriminator-free method ReCOIL that learns to imitate from arbitrary off-policy data to obtain near-expert performance. For offline RL, our analysis frames a recent offline RL method XQL in the dual framework, and we further propose a new method $f$-DVL that provides alternative choices to the Gumbel regression loss that fixes the known training instability issue of XQL. The performance improvements by both of our proposed methods, ReCOIL and $f$-DVL, in IL and RL are validated on an extensive suite of simulated robot locomotion and manipulation tasks.\\

\centering{\textbf{Project page (Code and Videos):} \href{https://hari-sikchi.io/dual-rl/}{\color{myredorange}hari-sikchi.io/dual-rl/}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a unified dual RL framework that connects several recent offline RL and IL methods. New algorithms called ReCOIL (for IL) and f-DVL (for RL) are presented that aim to address limitations of prior approaches. Experiments across locomotion, manipulation and navigation tasks generally demonstrate improved or comparable performance to baselines.

### Strengths
- The theoretical dual RL formulation provides a common lens to view recent offline RL/IL methods. This is a useful conceptual contribution.
- The methods are evaluated extensively on a diverse set of tasks using standardized benchmarks. Implementation details are clearly described.
- For offline IL, ReCOIL relaxes assumptions like coverage and avoids instability of density ratio estimation. The results showcase strong performance on imitation tasks.
- The modifications in f-DVL seem to improve training stability compared to XQL, a prior state-of-the-art in offline RL.

### Weaknesses
 - While f-DVL outperforms XQL, its gains over other offline RL methods like IQL are marginal. The gains are not as significant as claimed over the full spectrum of baselines.
- The presentation of empirical results could be improved by using standardized metrics, showing confidence intervals, and increasing clarity around performance highlights.
- There are open questions around design choices, estimation procedures, and other technical details that warrant clarification.

### Questions
Overall, I am moderately positive about this submission. The theoretical framework is clean and impactful. The empirical results are reasonably strong but could use tighter presentation and analysis. 

I have the following specific questions:

- In Eq. 10, is the reward assumed to be zero in the Bellman consistency term?
- Can you expand on how ReCOIL estimates the policy visitation and reward for the results in Sec 7.1? Also clarify if Fig 1 and Fig 10 use OPOLO or SMODICE for comparison.
- What do the distributions D and d^O refer to in Eq. 12 and 13? Are they both d_{mix}^{E,S}?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a new approach in offline IL, adopting the f-MAX objective function instead of the commonly utilized SMODICE objective. Unlike f-MAX, which employs GAIL for optimization, this work leverages the DICE technique to derive a dual form and subsequently applies an IQL-style algorithm for resolution. Additionally, the framework exhibits versatility, with potential applications in both the online and offline RL settings.

### Strengths
1. The paper offers a thorough and insightful analysis of recent developments within the dual-RL paradigm.
2. The proposed framework demonstrates adaptability across IL, offline RL, and online RL settings.
3. By eliminating the discriminator in offline IL, the paper potentially enhances stability and reliability in this domain.

### Weaknesses
1. XQL's instability and heavy reliance on hyperparameters are noticeable, with subpar performance in both online and offline RL under unsuitable conditions. As an alternative example, it might be more suitable to reference a more general and effective implicit policy improvement algorithm, like IQL[1]. I suggest you use a more general and effective implicit policy improvement algorithm, IQL, as an example.

2. In the last paragraph of Section 4.1, it is not suitable to say, "This insight also allows us to cast IL method OPOLO ....." as the objective function here originates from SMODICE. Referencing "this objective function" or similar expressions would be more appropriate.

3. In the first paragraph of Section 4.2, it is strange to use "Unfortunately" just because XQL is not the policy regularization style.

4. Figure 1 (a) is quite hard to follow. Please refine the caption to explain what the floats and the colors mean.

5. The first paragraph of Section 7.1 lacks supportive evidence for this claim. Incorporating illustrative figures and evaluations would substantiate this statement.

6. On page 36, typo in "We base the implementation of SAC off pytorch_sac ..."

7. On page 37, I disagree with your claim that "Our experiments with the popular off-policy method SAC [Haarnoja et al., 2018] reveal its brittleness to off-policy data". SAC is not brittle to off-policy data. Filling the replay buffer arbitrarily with expert data at the beginning is not fair for an ADP-style algorithm. Please rewrite this paragraph.

8. On page 40, the statement "f-DVL leads to noticeable improvements even in the online RL benchmarks" appears overstated:

   * The baselines are too few.

   * The performance improvement is not noticeable in 75% tasks you conducted experiments in.

   If you would like to claim noticeable,  please include more baselines (PPO[2], TD3[3], AlgeaDICE[4], and some other more recent algorithms, e.g., RRS[5], BAC[6], REDQ[7]) and more benchmark tasks. And please broaden the discussion of related works in the online RL setting beyond SAC.

9. Some crucial experimental outcomes, currently in Appendix H, should be integrated into the main paper for better accessibility and coherence, especially those results referenced and analyzed within the main paper.

10. Better not to claim "New" in the title directly. Just saying "A unified framework" is ok.

### Questions
Your work is commendable, but improvements in presentation and accuracy are needed. My specific questions and suggestions are as follows:

1. XQL's instability and heavy reliance on hyperparameters are noticeable, with subpar performance in both online and offline RL under unsuitable conditions. As an alternative example, it might be more suitable to reference a more general and effective implicit policy improvement algorithm, like IQL[1]. I suggest you use a more general and effective implicit policy improvement algorithm, IQL, as an example.

2. In the last paragraph of Section 4.1, it is not suitable to say, "This insight also allows us to cast IL method OPOLO ....." as the objective function here originates from SMODICE. Referencing "this objective function" or similar expressions would be more appropriate.

3. In the first paragraph of Section 4.2, it is strange to use "Unfortunately" just because XQL is not the policy regularization style. 

4. Figure 1 (a) is quite hard to follow. Please refine the caption to explain what the floats and the colors mean.

5. The first paragraph of Section 7.1 lacks supportive evidence for this claim. Incorporating illustrative figures and evaluations would substantiate this statement.

6. On page 36, typo in "We base the implementation of SAC off pytorch_sac ..."

7. On page 37, I disagree with your claim that "Our experiments with the popular off-policy method SAC [Haarnoja et al., 2018] reveal its brittleness to off-policy data". SAC is not brittle to off-policy data. Filling the replay buffer arbitrarily with expert data at the beginning is not fair for an ADP-style algorithm. Please rewrite this paragraph.

8. On page 40, the statement "f-DVL leads to noticeable improvements even in the online RL benchmarks" appears overstated:

   * The baselines are too few.

   * The performance improvement is not noticeable in 75% tasks you conducted experiments in.

   If you would like to claim noticeable,  please include more baselines (PPO[2], TD3[3], AlgeaDICE[4], and some other more recent algorithms, e.g., RRS[5], BAC[6], REDQ[7]) and more benchmark tasks. And please broaden the discussion of related works in the online RL setting beyond SAC.

9. Some crucial experimental outcomes, currently in Appendix H, should be integrated into the main paper for better accessibility and coherence, especially those results referenced and analyzed within the main paper.

10. Better not to claim "New" in the title directly. Just saying "A unified framework" is ok.

By addressing these points, your work could gain greater clarity and impact. And then, I would like to raise the score.

[1] Kostrikov I, Nair A, Levine S. Offline Reinforcement Learning with Implicit Q-Learning[C]//International Conference on Learning Representations. 2021.

[2] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347, 2017.

[3] S Fujimoto, H van Hoof, and D Meger. Addressing function approximation error in actor-critic methods. Proceedings of Machine Learning Research, 80:1587–1596, 2018.

[4] Nachum O, Dai B, Kostrikov I, et al. Algaedice: Policy gradient from arbitrary experience[J]. arXiv preprint arXiv:1912.02074, 2019.

[5] Hao Sun, Lei Han, Rui Yang, Xiaoteng Ma, Jian Guo, and Bolei Zhou. Optimistic curiosity exploration and conservative exploitation with linear reward shaping. In Advances in Neural Information Processing Systems, 2022.

[6] Ji T, Luo Y, Sun F, et al. Seizing Serendipity: Exploiting the Value of Past Success in Off-Policy Actor-Critic[J]. arXiv preprint arXiv:2306.02865, 2023.

[7] Chen X, Wang C, Zhou Z, et al. Randomized Ensembled Double Q-Learning: Learning Fast Without a Model[C]//International Conference on Learning Representations. 2021.

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
The paper proposes a framework called dual RL based on the LP formulation of RL. The author shows dual RL can be used to derive offline RL and offline IL algorithms, providing a unification of existing approaches. Based on this insight, they propose new offline IL and RL algorithms (ReCOIL and f-DVL), which remove existing assumptions. These algorithms are tested in the D4RL benchmarks empirically and achieve competent performance compared with other baselines.

### Strengths
The proposed dual RL framework based on the duality of a regularized RL problem is quite clean. The authors provide good background information and detailed derivations, which makes the paper self-contained and easy to follow. The dual RL framework makes some connections of existing works and suggests potential generalization (which the authors adopt) to design new algorithms. The empirical results are promising. Overall, this is an insightful paper.

### Weaknesses
There are some technical parts, which I think are not fully correct (see below). If they're indeed wrong, then the contribution of this paper would be compromised. The current writing is also quite dense as well, though the details are provided in the appendix. It would be better if the main paper is more readable. Lastly, in some sense, this paper lacks novelty. The unifying perspective and connection are interesting, but at the end the resulting algorithms can be viewed as minor tweaks from existing ones. Nonetheless, I think this last point on novelty is minor.

1. Proposition 4: The authors write that CQL can be cast as a dual-Q problem with a right choice of f-divergence (Pearson). However, in the proof of Proposition 4 in Appendix D.1, Eq (70) actually corresponds to the objective of ATAC [Cheng et al. 2022], not CQL. See Eq (1) in [Cheng et al. 2022], which is exactly the same Eq (70) here. To my understanding, the main difference between CQL and ATAC is that ATAC takes a maxmin formulation, whereas CQL doesn't, though they have a similar objective for learning Q. The dual-Q formulation here is a maxmin problem. The authors should update Proposition 4 to make the connection to ATAC, which would be more appropriate and precise.

2. Bug in the proof of Theorem 1. There is a minor bug in the proof of Theorem 1. In the block starting "Imitation from Arbitrary data (dualQ)" after Eq (108), max_d is moved inside min_Q, whereas max_d is outside min_Q in Eq (108). So Eq (109) is not just a summary, and that "we summarize the result of the derivation so far" can be misleading. But this can be easily fixed though, by applying strong duality before moving forward. Another minor suggestion: I think it would be good to write out the proof Eq (112) for completeness.

3. Validity Eq (10). In the proof, the author assume d_0 = d_E. I think that this is a fairly strong assumption, as it implies that the initial state at the test time would be drawn from the same distribution of the expert. This is rarely the case in practice, and in my experience it's not a common assumption in offline or off-policy RL. The authors should highlight this assumption in the main paper, or the authors should present Eq (140) as the main result. A minor bug in the proof is the derivation misses a 1/4 factor in front of the square loss.

4. Bug in Proof of Proposition 3. There're a few issues in the derivation, and one is major.
    a. f', (f')^-1 are not strictly increasing. it's only non-decreasing. e.g. see f(t) = | t-1|.
    b. why is f*(x) = -f(0) for x<0?
    c. why is f(0+)>0?
    d. You write (f')^{-1}(t) >0 when t>0 and 0 otherwise. What does "0 otherwise" mean?
    e. (Major issue). From Eq (79) to Eq (80), it doesn't use "(f')^{-1}(t) >0 when t>0" (though the paper writes so). It uses the other way (f')^{-1}(t) >0  --> t>0 and likewise (f')^{-1}(t) <0  --> t<0. But they are not true. See e.g. f(t) = | t-1| again. This error step prevents me from validating the remaining part.

5. The experiment design of offline IL can be a bit confusing. It says the agent is given 1 expert demonstration. But the suboptimal transition dataset actually contains 200 expert demonstrations, though I understand they're not marked as expert demonstrations to the algorithm. I think a more convincing experiment is to completely remove the expert demonstrations in the suboptimal data. Table 2 writes 1000 expert transitions. Is that the same as one expert trajectory?

6. I don't know how to interpret Fig 1. Can you explain more?

Minor:

1. This sentence is confusing to read. "Unfortunately, one of the most successful classes of offline RL methods .. has evaded connections to regularized policy optimization. Proposition 2 shows, perhaps surprisingly, that XQL can be cast as a dual of regularized policy learning, concretely as a dual-V problem."

2. I don't understand the connection between the sentence "To prevent extrapolation error in the offline setting, we rely on an implicit maximizer [Garg et al., 2023] that estimates the maximum over the Q-function conservatively with in-distribution samples." and Eq (12)

### Questions
1. Proposition 4: The authors write that CQL can be cast as a dual-Q problem with a right choice of f-divergence (Pearson). However, in the proof of Proposition 4 in Appendix D.1, Eq (70) actually corresponds to the objective of ATAC [Cheng et al. 2022], not CQL. See Eq (1) in [Cheng et al. 2022], which is exactly the same Eq (70) here. To my understanding, the main difference between CQL and ATAC is that ATAC takes a maxmin formulation, whereas CQL doesn't, though they have a similar objective for learning Q. The dual-Q formulation here is a maxmin problem. The authors should update Proposition 4 to make the connection to ATAC, which would be more appropriate and precise.

2. Bug in the proof of Theorem 1. There is a minor bug in the proof of Theorem 1. In the block starting "Imitation from Arbitrary data (dualQ)" after Eq (108), max_d is moved inside min_Q, whereas max_d is outside min_Q in Eq (108). So Eq (109) is not just a summary, and that "we summarize the result of the derivation so far" can be misleading. But this can be easily fixed though, by applying strong duality before moving forward. Another minor suggestion: I think it would be good to write out the proof Eq (112) for completeness.

3. Validity Eq (10). In the proof, the author assume d_0 = d_E. I think that this is a fairly strong assumption, as it implies that the initial state at the test time would be drawn from the same distribution of the expert. This is rarely the case in practice, and in my experience it's not a common assumption in offline or off-policy RL. The authors should highlight this assumption in the main paper, or the authors should present Eq (140) as the main result. A minor bug in the proof is the derivation misses a 1/4 factor in front of the square loss.

4. Bug in Proof of Proposition 3. There're a few issues in the derivation, and one is major. 
    a. f', (f')^-1 are not strictly increasing. it's only non-decreasing. e.g. see f(t) = | t-1|. 
    b. why is f*(x) = -f(0) for x<0? 
    c. why is f(0+)>0?
    d. You write (f')^{-1}(t) >0 when t>0 and 0 otherwise. What does "0 otherwise" mean?
    e. (Major issue). From Eq (79) to Eq (80), it doesn't use "(f')^{-1}(t) >0 when t>0" (though the paper writes so). It uses the other way (f')^{-1}(t) >0  --> t>0 and likewise (f')^{-1}(t) <0  --> t<0. But they are not true. See e.g. f(t) = | t-1| again. This error step prevents me from validating the remaining part. 

5. The experiment design of offline IL can be a bit confusing. It says the agent is given 1 expert demonstration. But the suboptimal transition dataset actually contains 200 expert demonstrations, though I understand they're not marked as expert demonstrations to the algorithm. I think a more convincing experiment is to completely remove the expert demonstrations in the suboptimal data. Table 2 writes 1000 expert transitions. Is that the same as one expert trajectory?

6. I don't know how to interpret Fig 1. Can you explain more?

Minor: 

1. This sentence is confusing to read. "Unfortunately, one of the most successful classes of offline RL methods .. has evaded connections to regularized policy optimization. Proposition 2 shows, perhaps surprisingly, that XQL can be cast as a dual of regularized policy learning, concretely as a dual-V problem."

2. I don't understand the connection between the sentence "To prevent extrapolation error in the offline setting, we rely on an implicit maximizer [Garg et al., 2023] that estimates the maximum over the Q-function conservatively with in-distribution samples." and Eq (12)

Reference: 
Cheng, Ching-An, et al. "Adversarially trained actor critic for offline reinforcement learning." International Conference on Machine Learning. PMLR, 2022.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper unifies a number of recent methods in offline RL and IL through the lens of regularized policy learning and Lagrange duality. Specifically, the paper views the regularized policy learning problem as a convex optimization problem with equality constraints on the state-action visitation distribution. Then, deriving the dual version of two equivalent primal problems, each named dual-Q and dual-V, the authors show that many recent offline IL and RL methods such as IQLearn and XQL, are specific instance of those problems with a particular choice of the f-divergence as the regularizer. Based on this analysis, the authors propose two algorithms for fixing shortcomings of previous algorithms. For offline IL, ReCOIL is presented as a new dual-Q algorithm that can leverage suboptimal demonstration data and that does not require the coverage assumption needed in prior work. For offline RL, f-DVL is proposed as a new dual-V algorithm as an extension of XQL, which results in more stable training by choosing a different f-divergence. The proposed methods are evaluated on the locomotion and manipulation tasks from the D4RL benchmark, and baseline comparisons show superior performance of ReCOIL and f-DVL on various tasks.

### Strengths
The major novel contribution of the paper is the theory which shows that various existing offline IL and RL methods can be derived from a Lagrange dual formulation of a single regularized policy learning problem. This itself has a huge consequence. For instance, showing that pessimistic value learning such as CQL is essentially a dual RL problem brings about a new insight into analyzing their properties and deficiencies. The self-contained review as well as derivations of key theoretical results in Appendix C has a core value in the paper, where the math is relatively easy to follow with the basic knowledge of convex optimization. This analysis itself paves a new way to developing many practical algorithms for both offline IL and RL, and has a significant potential impact on future research in this domain.

### Weaknesses
On the other hand, I have found a handful of math errors throughout the paper, especially in Appendix C, which critically degrades the quality of such a theory-driven paper. While many of them can be simple typos, some may actually require careful consideration. I will list them below.

 * There is a typo in equation (35). The second term inside $f^*$ should be $\gamma \sum_{s', a'} p(s' \mid s, a) \pi(a' \mid s') Q(s', a')$, not $\gamma \sum_{s'} p(s' \mid s, a) \pi(a \mid s') Q(s', a')$.

Regarding the empirical results in Section 7, the quality of presentation has much room for improvement, as described below.
* It is unclear what the left-most figure in Figure 1(a) represents and how it is related to the squared distribution gap plot right next to it. The connection between the policy visualization and the distribution gap needs to be clarified. Furthermore, the axes and labels in the policy visualization are not clearly defined, making it difficult to interpret.

* In Table 2, it is unclear how the authors determined to highlight some of the entries with blue bold texts as an indication of the most-performant policy. For instance, In the hopper task with the medium few-expert dataset, the RCE seems to have the highest mean but not highlighted in blue.

* In Table 3, the highlighting logic is inconsistent. The authors should clearly define the criteria for highlighting entries in blue and apply it consistently throughout the table. The current highlighting creates confusion rather than providing clarity.

### Questions
* ~~I do not see how one can directly derive equation (14) from equation (5), as a rewriting of dual-V with the temperature parameter $\lambda$. Can you elaborate on the derivation? I believe that the discount factor $\gamma$ is determined by the problem specification and is not a hyperparameter that can be tuned arbitrarily.~~

* ~~In equations (32) to (34), can you elaborate on why the interchangeability principle holds in this specific case? In other words, can you explain why $\max$ and $\mathbb{E}$ can be exchanged?~~

* ~~All the analysis presented in the paper implicitly assumes discrete state and action spaces (which I think is good for readers in the RL community to follow the math). Do the results naturally extend to continuous spaces? I would be surprised if they did not, but I bet we need more sophisticated tools from real-analysis and probability theory to prove the same results.~~

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
