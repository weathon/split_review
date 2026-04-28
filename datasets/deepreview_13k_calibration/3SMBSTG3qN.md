# Beyond CVaR: Leveraging Static Spectral Risk Measures for Enhanced Decision-Making in Distributional Reinforcement Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
In domains such as finance, healthcare, and robotics, managing worst-case scenarios is critical, as failure to do so can lead to catastrophic outcomes. Distributional Reinforcement Learning (DRL) provides a natural framework to incorporate risk sensitivity into decision-making processes. However, existing approaches face two key limitations: (1) the use of fixed risk measures at each decision step often results in overly conservative policies, and (2) the interpretation and theoretical properties of the learned policies remain unclear. While optimizing a static risk measure addresses these issues, its use in the DRL framework has been limited to the simple static CVaR risk measure. In this paper, we present a novel DRL algorithm with convergence guarantees that optimizes for a broader class of static Spectral Risk Measures (SRM). Additionally, we provide a clear interpretation of the learned policy by leveraging the distribution of returns in DRL and the decomposition of static coherent risk measures. Extensive experiments demonstrate that our model learns policies aligned with the SRM objective, and outperforms existing risk-neutral and risk-sensitive DRL models in various settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work studies the problem of incorporating static spectral risk measures (SRM into Distributional Reinforcement Learning (DRL) to enable more flexible and interpretable risk-sensitive decision-making. Unlike conventional Conditional Value-at-Risk (CVaR), SRMs offer a spectrum of risk preferences, allowing for more flexible risk-sensitive policies. The authors argue that using SRMs in DRL enables more flexible and interpretable policies, as SRMs allow for a spectrum of risk preferences rather than a fixed measure like CVaR. The authors propose an iterative DRL algorithm that utilizes a two-stage optimization process to optimize SRMs. They provide theoretical guarantees, proving convergence and characterizing the temporal decomposition of SRMs within the DRL framework. This decomposition enhances interpretability, as it captures how risk preferences evolve over time. The algorithm’s effectiveness is demonstrated through extensive numerical studies across four example environments, where it outperforms several baseline models, highlighting its potential for real-world applications.

### Strengths
1.	This paper is easy to follow and well-organized. 
2.	The theoretical analyses throughout the paper are technically sound and comprehensive, providing strong support for the proposed method.
3.	The authors preform thorough numerical studies across four examples. The proposed algorithm outperforms several baselines, highlighting its potential for real-world applications.

### Weaknesses
See Question section

### Questions
1.	In Table 1, when the objective is CVaR(0.1), why does QR-SRM with $\alpha=0.1$ not achieve the highest value? Could the authors clarify the reasons  influencing this outcome?
2.	The authors introduce the decomposition theorem for SRMs (Theorem 2). Could they use one of the four examples to illustrate how this theorem applies in a practical scenario? This would help readers better understand these concepts.

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
This paper addresses limitations in current risk-sensitive Distributional Reinforcement Learning  by introducing an algorithm that optimizes for a broader class of static SRM, moving beyond the commonly used CVaR. The proposed QR-SRM algorithm utilizes SRMs to adjust the agent's risk sensitivity dynamically, improving policy interpretability and adaptability. Extensive experiments on environments demonstrate that QR-SRM achieves superior performance and consistency with SRM objectives.

### Strengths
- The application of SRM to DRL for more interpretable risk-sensitive policies is innovative, introducing valuable theoretical insights and practical tools for risk-sensitive control.
- Theoretical grounding and comprehensive experimental evaluations
- The problem formulation, motivation, and results are well-articulated, though some technical details could be simplified.

### Weaknesses
 - Certain theoretical sections, especially around SRM decomposition, may challenge readers due to dense terminology and complex proofs. More illustrative examples or simplified explanations could improve accessibility.
- The paper assumes specific properties of SRMs and fixed initial preferences, which may limit the algorithm's flexibility in dynamic environments.
- The authors use an extended state space to solve the inner optimization problem. Can you provide rigorous justification
- The proposed algorithm's computational complexity is not thoroughly analyzed. Given the bilevel optimization algorithmic framework, and the added complexity of optimizing SRM in a distributional RL framework, the computational complexity of the proposed algorithm may be a concern.

some missing references about DRL for RSRL
- Keramati, R., Dann, C., Tamkin, A. and Brunskill, E., 2020, April. Being optimistic to be conservative: Quickly learning a CVaR policy. In Proceedings of the AAAI conference on artificial intelligence (Vol. 34, No. 04, pp. 4436-4443).
- Liang, H. and Luo, Z.Q., 2024. Bridging distributional and risk-sensitive reinforcement learning with provable regret bounds. Journal of Machine Learning Research, 25(221), pp.1-56.
- Chen, Y., Zhang, X., Wang, S. and Huang, L., Provable Risk-Sensitive Distributional Reinforcement Learning with General Function Approximation. In Forty-first International Conference on Machine Learning.

### Questions
- The authors use an extended state space to solve the inner optimization problem. Can you provide rigorous justification
- The proposed algorithm's computational complexity is not thoroughly analyzed. Given the bilevel optimization algorithmic framework, and the added complexity of optimizing SRM in a distributional RL framework, the computational complexity of the proposed algorithm may be a concern.

some missing references about DRL for RSRL
- Keramati, R., Dann, C., Tamkin, A. and Brunskill, E., 2020, April. Being optimistic to be conservative: Quickly learning a CVaR policy. In Proceedings of the AAAI conference on artificial intelligence (Vol. 34, No. 04, pp. 4436-4443).
- Liang, H. and Luo, Z.Q., 2024. Bridging distributional and risk-sensitive reinforcement learning with provable regret bounds. Journal of Machine Learning Research, 25(221), pp.1-56.
- Chen, Y., Zhang, X., Wang, S. and Huang, L., Provable Risk-Sensitive Distributional Reinforcement Learning with General Function Approximation. In Forty-first International Conference on Machine Learning.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel distributional reinforcement learning algorithm called QR-SRM, which extends beyond expected return by incorporating spectral risk measures. 
The authors provide convergence guarantees and enhance interpretability of policies by decomposing coherent risk measures.

### Strengths
- The paper addresses a well-motivated problem by proposing an algorithm with asymptotically optimal regret bounds for scenarios involving trajectory-level feedback. 

- Up to Section 4, the authors clearly outline the motivations, objectives, and proof sketches, making it easier for readers to grasp the core concepts.

- The authors included code for reproducibility and conducted experiments across diverse environments, adding practical value and robustness to the study.

### Weaknesses
 - A minor weakness is the need for improved visualization in the experimental results. The vertical lines are not immediately distinguishable, so adjusting the dash spacing, line thickness, or adding markers would enhance clarity. Additionally, using consistent labels for the same algorithm in the legend would help reduce reader fatigue.

- My main concern is that the low performance of the experimental results makes it difficult to be confident that the algorithm was correctly reproduced. According to [1], QR-DQN performs at least 100 points on LunarLander-v2 after 0.1M steps. However, Table 3 of this paper shows much lower scores, suggesting the results may not be fully reproducible. Can the authors clarify?

- Although the experiments were conducted in various environments, the aforementioned concerns about reproducibility make fair comparison with other baselines challenging. Reporting performance on some Atari environments, commonly used by algorithms that assume discrete action spaces, would provide a more reliable basis for apple-to-apple comparison.


Typos

- Line 197: "Coheret" should be "Coherent"

- Line 230: $[h_l (G^{\pi})]$ should be $\mathbb{E}[h_l (G^{\pi})]$

- Line 286: "Output" should be in bold.

### Questions
- In Line 232, shouldn't it be $h_{l+1} = \arg \max _h \mathbb{E}[h(G^{\pi^*_l})] + \int_0^1 \hat{h}(\phi(u)) du$? 
I'm wondering if $ \int_0^1 \hat{h}(\phi(u)) du=0$ is inherently guaranteed within the algorithm, or if there is a condition that ensures this which I may have missed.

- In Line 383, $\alpha=0.6$ seems to be maximized at $CVaR_{0.8}$, and $\alpha=0.4$ at $CVaR_{0.6}$. Although the small vertical line intervals may be minor, the lack of alignment with targeted risk levels raises concerns.

- In Table 2, aren't the cases with $\alpha=1.0$ essentially QR-DQN?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper aims to extend the work of Bauerle and Glauner [1] on static spectral risk measures (convex combinations of CVaR) in Markov Decision Processes (MDPs) to the context of distributional reinforcement learning (RL). Sections 4 and Appendices A and B reformulate the approach from [1] using distributional value functions. Theorem 1 provides a bound on the performance of the policy derived from greedy action selection over an augmented state space (x, s, c). Algorithm 2 proposes the TD error computation for distributional value function, contrasting with methods like QR-DQN and IQN, by directly addressing for static spectral risk measures. Theorem 2 extends the decomposition from coherent risk measures [2] to a broader class of spectral risks, increasing the generalizability of the approach to a wider array of risk-sensitive applications. Finally, the experiments validate the proposed algorithm, offering evidence of its efficacy and robustness within this distributional risk-sensitive framework.

References:

[1] Nicole Bauerle and Alexander Glauner. Minimizing spectral risk measures applied to Markov decision processes. Mathematical Methods of Operations Research, 94(1):35–69, 2021.

[2] Georg Ch. Pflug and Alois Pichler. Time-Consistent Decisions and Temporal Decomposition of Coherent Risk Functional. Mathematics of Operations Research, 41(2):682–699, 2016.

### Strengths
The strengths of this paper lie in its deep understanding of the current state of research in risk-averse reinforcement learning (RL) and the limitations of recent work in risk-averse distributional RL (DRL). Specifically, the paper identifies key challenges: (1) dynamic and fixed risk DRL approaches often lack interpretability, and (2) the dual representation of coherent risk measures encounters issues during policy optimization. The authors’ solid grasp of the mathematical foundations behind risk measures enables them to combine and present a concise and theoretically sound introduction.

### Weaknesses
Despite the authors’ strong grasp of the limitations in risk-averse distributional RL research, this paper has several notable weaknesses:

(I) The primary weakness lies in the limited originality of the contributions. Much of the content in Theorems and Lemmas in Appendix A, B, and Section 4 is directly adapted from [1], with only minor modifications to distribution value function representation. This reliance raises questions about the novelty and depth of the contributions, compared to [1].

(II) While the Introduction and Preliminaries are well-articulated, Sections 4 and 5 suffer from clarity issues. Section 5 appears disconnected from previous sections. Spectral risk measures can be represented as convex combinations of CVaR, Theorem 2 in Section 5 leverages this property to extend the dual decomposition from coherent risk to general spectral risk measures. However this dual decomposition is unrelated to algorithm 1 and 2 in the earlier sections.

(III) Did not discuss the main limitation of extending static spectral risk MDP to model-free/distributional RL. Specifically:
- (a) There is no analysis of the convergence properties of the algorithm 2 TD loss update  (a static risk variant similar to [2]).
- (b) Missing analysis for approximation errors and guarantees arising from quantile discretization $\tau_i$.
- (c) Contraction analysis is missing, considering that the minimizer of the Huber loss may not be unique (see [3]).

### Questions
(I) What are the contribution of section 4 compared to [1]? Please clearly indicate which methods are re-written from [1] and what is new in this paper, in the main body and also appendix A and B. 

(II) Please address the limitation pointed out in Weaknesses section (III):Did not discuss the main limitation of extending static spectral risk MDP to model-free/distributional RL. Specifically:
- (a) There is no analysis of the convergence properties of the algorithm 2 TD loss update  (a static risk variant similar to [2]).
- (b) Missing analysis for approximation errors and guarantees arising from quantile discretization $\tau_i$.
- (c) Contraction analysis is missing, considering that the minimizer of the Huber loss may not be unique (see [3]).


References:

[1] Nicole Bauerle and Alexander Glauner. Minimizing spectral risk measures applied to Markov decision processes. Mathematical Methods of Operations Research, 94(1):35–69, 2021.

### Soundness
3

### Presentation
2

### Contribution
2
