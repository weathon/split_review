# SERA: Sample Efficient Reward Augmentation in offline-to-online Reinforcement Learning

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 3, 5, 5

## Abstract
A prospective application of offline reinforcement learning (RL) involves initializing a pre-trained policy using existing static datasets for subsequent online fine-tuning. However, direct fine-tuning of the offline pre-trained policy often results in sub-optimal performance. A primary reason is that offline conservative methods diminish the agent's capability of exploration, thereby impacting online fine-tuning performance. To enhance exploration during online fine-tuning and thus enhance the overall online fine-tuning performance, we introduce a generalized reward augmentation framework called Sample Efficient Reward Augmentation (SERA). SERA aims to improve the performance of online fine-tuning by designing intrinsic rewards that encourage the agent to explore. Specifically, it implicitly implements State Marginal Matching (SMM) and penalizes out-of-distribution (OOD) state actions, thus encouraging agents to cover the target state density, and achieving better online fine-tuning results. Additionally, SERA can be effortlessly plugged into various RL algorithms to improve online fine-tuning and ensure sustained asymptotic improvement, showing the versatility as well as the effectiveness of SERA. Moreover, extensive experimental results will demonstrate that when conducting offline-to-online problems, SERA consistently and effectively enhances the performance of various offline algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a generalized reward enhancement framework known as SERA, which aims to boost online fine-tuning performance by designing intrinsic rewards, thereby improving the online performance of offline pre-trained policies. SERA achieves this by implicitly enforcing state marginal matching and penalizing out-of-distribution state behaviors, encouraging the agent to cover the target state density, resulting in superior online fine-tuning outcomes. Experimental results consistently demonstrate the effectiveness of SERA in enhancing the performance of various algorithms in offline-to-online settings.

### Strengths
1. The exploration of the offline-to-online problem in this study holds great relevance and is imperative for practical implementations, aligning seamlessly with the demands of real-world situations.
2. The fundamental idea at the core of this study is firmly grounded. While the concept presented in this paper is rather straightforward, involving the introduction of an exploration strategy during the online phase to enhance performance, the specific exploration technique employed is quite novel and has demonstrated favorable results in the experiments.

### Weaknesses
1. In the experimental section, the author conducted experiments solely on the medium dataset in MuJoCo. However, according to the consensus in the field of offline-to-online research, it is generally recommended to perform experiments on at least three types of datasets: medium, medium-replay, and medium-expert, in order to validate the effectiveness of the method.
2. The method proposed in this paper is primarily an extension of CQL and Cal-QL. However, in the context of the offline-to-online field, the actual compared baselines are limited to AWAC and Cal-QL. It is advisable for the authors to consider comparing their method with other more efficient algorithms such as Balanced Replay[1], PEX[2], and ENOTO[3].
3. The SERA algorithm, proposed in this paper, primarily enhances online performance by designing intrinsic rewards to encourage exploration. This concept has been mentioned in previous works such as O3F[4] and ENOTO, although SERA employs different exploration methods. While introducing exploration during the online phase can enhance performance, it may introduce another challenge: instability due to distribution shift, which can lead to performance degradation in the early stages of online learning. This issue has been discussed in many offline-to-online works and is a critical metric in this field. However, it might not be very evident on the medium dataset. Therefore, the authors should consider conducting additional experiments on the medium-replay and medium-expert datasets to verify whether performance degradation occurs.
4. In Figure 4, the experimental results for the Antmaze environment are challenging to discern, as the curves for various algorithms are intertwined and unclear. The author should consider optimizing the representation of these experimental results for better clarity.
5. In Table 1, only the mean values of the algorithm results are presented, with a lack of information regarding the errors or variances associated with these results.

### Questions
See weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on offline-to-online RL and proposes improving the performance by enhancing exploration during online fine-tuning with a reward augmentation framework, SERA. The intrinsic rewards are calculated by implementing State Marginal Matching (SMM) and penalizing out-of-distribution (OOD) state actions.

### Strengths
- The proposed method is easy to understand.
- The technique seems sound.

### Weaknesses
==Major concerns==
- The paper requires careful revision due to numerous typographical errors that hinder comprehension.
- The practical calculation of Equation (3) for high-dimensional continuous state variables is unclear. A detailed analysis of its implementation, particularly concerning the approximation of state entropy in a continuous, high-dimensional space using a finite batch of samples, is needed.
- The relationship between Equation (2) and Equation (4) when calculating the critic-conditioned intrinsic reward is not adequately explained. The paper should clarify how these equations are connected, especially regarding the implementation details of calculating Q-conditioned state entropy.
- The reliance on KNN for intrinsic reward calculation raises concerns about computational efficiency, especially regarding time consumption. An evaluation or discussion of the computational overhead compared to alternative methods would be beneficial.
- The appendix is not included, making it difficult to fully assess the paper's claims and derivations.
- The paper lacks comprehensive comparisons across the full suite of D4RL datasets. Providing results for all datasets, or at least a more representative subset, would strengthen the experimental validation.
- Several citations are incorrectly formatted.
- The experimental setup lacks information about the random seeds used, making it difficult to assess the reproducibility of the results.

==Minor concerns==
- The paper fails to define all symbols used. For example, in Section 3.1, $d_D(.|s)$ and $\mathcal{G}_{\mathcal{M}}$ are not introduced. A clear definition of all symbols is necessary for clarity.
- In Definition 1, the absence of a negative sign in the critic-conditioned entropy formula is unconventional and requires justification. Additionally, if N states are used for calculating the critic-conditioned entropy, this should be clearly stated and explained in the context of the formula.
- There is an inconsistency in the notation for the initial state distribution. In Equation (3), it is denoted as $\rho_0(S)$, while in Section 3.1, it is defined as $p(s_0)$. This discrepancy should be resolved.
- The significant difference in the symbols used on the left and right sides of Equation (4) is confusing. A detailed derivation or explanation of how these terms are related would enhance understanding.
- The paper claims that maximizing $E_{s\sim\rho(s)}[H_{\pi}[s]]$ is equivalent to minimizing $D_{KL}(\rho_{\pi}(s)||p^*(s))$, but it does not provide a derivation or sufficient explanation for this equivalence. This should be clarified.
- The paper uses inconsistent expressions when referring to figures.

==Typos==
- Section 3.1 “Model-free Offline RL”: “In particular, Model-free”-> “In particular, model-free”
- Section 3.1 “Model-free Offline RL”: “Specifically, Model-free” -> “Specifically, model-free”
- Section 3.1 “Model-free Offline RL”: “one step bellman equation i.e. …. which” -> “one step bellman equation, i.e. xxxx, which”
- Section 3.1 “Model-free Offline RL”: “Previous studies have extensively studied such a problem, such that CQL was proposed to penalty the OOD state actions by conservative term (Equation 1), and IQL implicitly learns Q function with expected regression without explicit access to the value estimation of OOD state-actions.”
- Section 3.1: “state entropy(Seo et al., 2021)” -> “state entropy (Seo et al., 2021)”
- Section 3.1: “i.i.d”-> ““i.i.d.””
- Section 3.2: grammatical mistake: “Specifically, we first use the offline methods to …..”
- Section 3.2: “\pi_{beta}” -> “\pi_{\beta}”
- Section 3.2: “Equation. 4” -> “Equation (4)”
- Section 3.2: “SMM,i.e.” -> “SMM, i.e.”
- Section 3.2: “Only maximize” -> “Only maximizing”
- Section 4.1: “… are the params of double Q Networks” -> “… are the parameters of double Q Networks”
- Section 4.1: “in addition to testing SERA” -> “in addition to test SERA”
There are so many typos, so I suggest the authors check this paper carefully.

### Questions
==Major concerns==
- The authors are strongly advised to revise this paper carefully. There are so many typos in this paper, which affects the normal comprehension of this paper.
- I do not understand how to calculate Equation (3) in practice when the state is high dimensional continuous variables. Can the authors provide the analysis?
- What is the relation between Equation (2) and Equation (4) when calculating the critic-conditioned intrinsic reward?
- Every intrinsic reward calculation must be calculated by KNN, so the efficiency of physic time consumption may be a little poor.
- I can not find the appendix mentioned in this paper.
- Can the author provide the whole comparisons about D4RL datasets?
- The format of some citations is wrong.
- What about the random seed in the experiments?

==Minor concerns==
- The authors should explain all symbols that appear in this paper, e.g., in Section 3.1, the authors do not introduce $d_D(.|s)$ and $\mathcal{G}_{\mathcal{M}}$.
- In Definition 1, why the critic-conditioned entropy does not contain “-”. Besides, if there are N states that are used for calculating the critic conditioned entropy, 
- In Equation (3), the initial state distribution is $\rho_0(S)$, but in Section 3.1, the initial state distribution is defined as $p(s_0)$. Besides, 
- In Equation (4), the symbols of the left side and the right side are very different. Can the authors provide a detailed derivation?
- The authors should provide the derivation about “Another reason is that maximizing Es∼ρ(s)[Hπ[s]] is equivalent to minimize DKL(ρπ(s)||p∗(s)) thus has the mathematical guarantee.”
- Different reference expressions about figures.



==Typos==
- Section 3.1 “Model-free Offline RL”: “In particular, Model-free”-> “In particular, model-free”
- Section 3.1 “Model-free Offline RL”: “Specifically, Model-free” -> “Specifically, model-free”
- Section 3.1 “Model-free Offline RL”: “one step bellman equation i.e. …. which” -> “one step bellman equation, i.e. xxxx, which”
- Section 3.1 “Model-free Offline RL”: “Previous studies have extensively studied such a problem, such that CQL was proposed to penalty the OOD state actions by conservative term (Equation 1), and IQL implicitly learns Q function with expected regression without explicit access to the value estimation of OOD state-actions.”
- Section 3.1: “state entropy(Seo et al., 2021)” -> “state entropy (Seo et al., 2021)”
- Section 3.1: “i.i.d”-> ““i.i.d.””
- Section 3.2: grammatical mistake: “Specifically, we first use the offline methods to …..”
- Section 3.2: “\pi_{beta}” -> “\pi_{\beta}”
- Section 3.2: “Equation. 4” -> “Equation (4)”
- Section 3.2: “SMM,i.e.” -> “SMM, i.e.”
- Section 3.2: “Only maximize” -> “Only maximizing”
- Section 4.1: “… are the params of double Q Networks” -> “… are the parameters of double Q Networks”
- Section 4.1: “in addition to testing SERA” -> “in addition to test SERA”
There are so many typos, so I suggest the authors check this paper carefully.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of fine-tuning pre-trained offline RL agents. Specifically, it proposed a reward augmentation framework, named Sample Efficient Reward Augmentation (SERA), to encourage exploration in the fine-tuning stage with Q conditional state entropy. SERA further uses state marginal matching (SMM) and penalizes OOD state actions. Experiments on the D4RL benchmark tasks showed the proposed SERA outperformed other baselines.

### Strengths
- This paper investigates an important question in offline RL.
- The proposed method outperformed other baseline in the D4RL benchmark task.

### Weaknesses
 - Firstly, the writing is not good enough. Many sentences are not rigorous or confusing. For example:
    - In the first paragraph, "such paradigm can only learn similar or slightly better performance than behavioural policy" is not true. Because model-based offline RL methods can sometimes significantly improve the performance w.r.t. the behavioural policy.
    - In the third paragraph, "The second approach employs offline RL with policy regression". What does the "policy regression" mean? Or it's a typo of "policy regularization".
    - "underestimate the value of the offline buffer in comparison to the ground truth returns" => should be "underestimate the value of OOD samples in the offline buffer"

- There are too many typos and grammar errors: 
    1. "some researches penalty the Q values" ==> penalize
    2. Missing period after "or implicitly regularize the bellman equation"
    3. "It similarly train agent" ==> trains
    4. "high sampling efficiency" ==> sample
    5. extra period "on both offline and online RL., we "
    6. "as a Markov decision Process" ==> Decision
    7. "A denotes the actions space" ==> action
    8. missing comma in "tau = {s0, a0, r0, ..., st, at rt}"
    9. missing "the" in "in offline-to-online RL problem setting"
    10. "Bellman equation iteration"  ==> "Bellman iteratio equation"
    11. "it always suffer from" ==> suffers
    12. missing norm notation in the one step Bellman equation
    13. missing right bracket in "if (s', pi(\cdot | s') \notin D"
    14. "to penalty the OOD state actions" ==> penalize
    15. "expected regression" ==> expectile regression
    16. "by rollout behavioural policy" ==> unrolling
    17. "thus has the" ==> having
    18. "only maximize" ==> maximizing
    19. "rather E[H[s]]" ==> rather than
    20. "where Tanhs see" ==> sees

- There are some missing SOTA baselines for offline-to-online fine-tuning in the experiments: Reincarnating RL [1], PEX [2], InAC [3]

### Questions
- "which is unbiased in the early online process" => why it's unbiased?

- Since the main argument of this work is a new exploration method for fine-tuning offline RL agents. I think it should compare to other  intrinsic reward baselines, i.e, state entropy, RND, ICM.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates sample-efficient offline-to-online reinforcement learning with reward augmentation technique. Specifically, this paper enhances VCSE with Q conditioned state entropy, deriving initially successful empirical findings on D4RL benchmark.

### Strengths
- The perspective of improving sample efficiency for offline-to-online RL seems interesting.

### Weaknesses
Overall, I think this paper does not meet the basic bar of ICLR, especially in terms of writing and experiments. I strongly suggest the authors proof-reading the paper thoroughly to make it a stronger submission. See detailed comments below.
- From Fig. 1, it seems that CQL-SERA > Cal-QL-SERA > Cal-QL baseline > CQL baseline, which contradicts to the empirical findings in Fig. 4.
- Is the unbiasedness of SERA theoretically guaranteed by replacing V function by Q function? If not, it is kind of over-claiming in Introduction.
- Please conduct sufficient research investigation on offline-to-online RL. A lot of related works are not appropriately referenced:

[1] Offline-to-online reinforcement learning via balanced replay and pessimistic q-ensemble, CoRL’22.

[2] Adaptive policy learning for offline-to-online reinforcement learning, AAAI’23.

[3] Policy Expansion for Bridging Offline-to-Online Reinforcement Learning, ICLR’23.

[4] Sample Efficient Offline-to-Online Reinforcement Learning, TKDE’23.

[5] Actor-Critic Alignment for Offline-to-Online Reinforcement Learning, ICML’23.

[6] Fine-tuning offline policies with optimistic action selection, NeurIPS workshop.

[7] A Simple Unified Uncertainty-Guided Framework for Offline-to-Online Reinforcement Learning, arXiv preprint.

[8] PROTO: Iterative Policy Regularized Offline-to-Online Reinforcement Learning, arXiv preprint.

[9] Ensemble-based Offline-to-Online Reinforcement Learning: From Pessimistic Learning to Optimistic Exploration, arXiv preprint.

[10] Towards Robust Offline-to-Online Reinforcement Learning via Uncertainty and Smoothness, arXiv preprint.

- Exploration has been discussed a lot by previous works on offline-to-online RL [3,4,6,7]. Please discuss advantages of SERA over them.
- In Section 3.1:

(1) $d_\mathcal{D}$ is not defined.

(2) Should not J(Q) be a MSE loss?

(3) In $\mathcal{B}_{\mathcal{M}}^{\pi}Q(s,a)$, the condition of the expectation is $s \sim \mathcal{D}$?

(4) Eq.(1) seems incorrect. Check Eq. (3.1) in Cal-QL paper.

(5) what is $s_i^{knn}$ in Eq.(2)?
- In Section 3.2:

(1) Eq.(4) seems incorrect. Please double-check.

(2) Overall, I cannot follow details in Section 3.2. Please provide step-by-step instructions in Appendix to make it more clear.
- In Section 4.1, Isn’t SERA a generic offline-to-online RL algorithm? Why the training objective is constrained to the framework of CQL and Cal-QL?
- Moreover, this paper claims to have an appendix pdf, but I cannot find the appendix in openreview.
- Why experiments are only conducted on 8 selected tasks. In general, MuJoCo has random/medium/medium-replay/medium-expert/etc. datasets. Consider these settings.
- It seems that there are only one random seed throughout the paper. Please repeat all the experiments with at least three different random seeds to control the randomness. Also, please report the mean and std value.
- Please consider more sufficient comparison in Fig. 5. Besides, in ant-medium, where is TD3+BC? In ant, halfcheetah, and walker2d, IQL seems performs better than IQL-SERA. Could you provide more explanations?
- Why only two tasks are selected in Fig. 6 (a)?
- Why only IQL is selected in Fig. 6 (b) on only two tasks?
- There are no sufficient ablation studies on each component of SERA. For example, you claim that condition on Q is better than V, thus, please derive some empirical findings to support this claim.
- Some typos:

(1) Reference format is not well-handled throughout the paper. In ICLR template: xxx (Author, et al., Year)

(2) In page 2: by maximizing no-conditioned -> non-conditioned; Anther reason -> Another.

(3) In page 3: some researches penalty the -> penalize; both offline and online RL., we -> delete the comma; improving Model-free offline-to-online RL -> model-free; 

(4) In page 4: given N i.i.d samples -> $N$; consists of samples -> revise this sentence; Add , in Eq.(4); Equation. 4 -> Equation 4;

(5) In page 5: params -> parameters;

(6) In page 6: Differing -> Different;

### Questions
See weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
