# A Policy Gradient Method for Confounded POMDPs

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
In this paper, we propose a policy gradient method for confounded \textit{partially observable Markov decision processes} (POMDPs) with continuous state and observation spaces in the offline setting. We first establish a novel identification result to non-parametrically estimate any history-dependent policy gradient under POMDPs using the offline data. The identification enables us to solve a sequence of conditional moment restrictions and adopt the min-max learning procedure with general function approximation for estimating the policy gradient. 
 We then provide a finite-sample non-asymptotic bound for estimating the gradient uniformly over a pre-specified policy class in terms of the sample size, length of horizon, concentratability coefficient and the measure of ill-posedness in solving the conditional moment restrictions. Lastly, by deploying the proposed gradient estimation in the gradient ascent algorithm, we show the global convergence of the proposed algorithm in finding the history-dependent optimal policy under some technical conditions. To the best of our knowledge, this is the first work studying the policy gradient method for POMDPs under the offline setting.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper introduces a novel policy gradient method for confounded partially observable Markov decision processes (POMDPs), and proves it converges to global optimal under certain assumptions. Their method estimates the policy gradient using bridge functions calculated from offline data, which is adopted from min-max estimator of [Dikkala et al. (2020)]. The paper provides a finite-sample non-asymptotic bound for estimating the gradient uniformly over a pre-specified policy class. Additionally, the authors show the global convergence of the proposed algorithm in finding the history-dependent optimal policy under certain technical conditions. This work is claimed to be the first to study the policy gradient method for POMDPs under the offline setting.

The paper also discusses the challenges in studying policy gradient methods in confounded POMDPs under the offline setting, such as the bias in estimation due to unobserved state variables, the need for function approximation in continuous spaces, and the challenge in achieving global convergence for finding the optimal policy.

The authors contribute by proposing a policy gradient method with both statistical and computational guarantees, establishing a non-asymptotic error bound for estimating the policy gradient, and providing a solution for global convergence in POMDPs.

### Strengths
**Dsiclaimer:** I should first note that the results of this paper are super technical. A proper review of this article needs a full working week of my time, which clearly I couldn't put. I tried going through Appendix A and B, but even then I cannot say I understood completely.

Despite these challenges, it is evident that the results derived in this paper solid. Establishing any form of convergence for the Policy Gradient (PG) algorithms within the context of POMDPs is immensely valuable to the community. Furthermore, their method for gradient estimation in this study presents itself as a potentially advantageous tool in its own right.

### Weaknesses
Given the technical nature of this paper, I am compelled to express my reservations about the suitability of the ICLR conference as the platform for its publication. I believe that this work might find a more fitting home in a scholarly journal, where reviewers are afforded ample time to thoroughly validate the results presented. Additionally, the attempt to condense the material into a 9-page format has significantly hindered its readability. In particular, the contents of Appendix A are critical enough that they warrant inclusion (or partial inclusion) in the main body of the text.

[Vlassis et. al., 2012] have proved that finding a stochastic controller of polynomial size that achieves a certain target, is an NP-hard problem. Optimizing policy for confounded POMDPs is even more challenging. While [Vlassis et al., 2012] does not directly contradict this paper, it does raise questions about the real-world applicability of the assumptions made herein. Is there a possibility to provide examples that provide lower bounds? [Agrawal et. al.] provided an example demonstrating the necessity of distribution mismatch coefficient (which I presume it isn't very difficult to have a similar one for POMDPs). With this work, I also love to see more about computational complexity (and polynomial / NP-hardness / ...) of specific classes of POMDPs.

I must note that I am unable to specifically identify any of the assumptions as unreasonable, but I guess Assumption 2 is the most critical assumption.

### Questions
[Vlassis et. al., 2012] have proved that finding a stochastic controller of polynomial size that achieves a certain target, is an NP-hard problem. Optimizing policy for confounded POMDPs is even more challenging. While [Vlassis et al., 2012] does not directly contradict this paper, it does raise questions about the real-world applicability of the assumptions made herein. Is there a possibility to provide examples that provide lower bounds? [Agrawal et. al.] provided an example demonstrating the necessity of distribution mismatch coefficient (which I presume it isn't very difficult to have a similar one for POMDPs). With this work, I also love to see more about computational complexity (and polynomial / NP-hardness / ...) of specific classes of POMDPs.

I must note that I am unable to specifically identify any of the assumptions as unreasonable, but I guess Assumption 2 is the most critical assumption. 

References:
- Alekh Agarwal, Sham M Kakade, Jason D Lee, and Gaurav Mahajan. On the theory of policy
gradient methods: Optimality, approximation, and distribution shift. The Journal of Machine Learning Research, 22(1):4431–4506, 2021.
- Vlassis, Nikos, Michael L. Littman, and David Barber. "On the computational complexity of stochastic controller optimization in POMDPs." ACM Transactions on Computation Theory (TOCT) 4.4 (2012): 1-8.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a policy gradient method for confounded partially observable Markov decision processes (POMDPs) in the offline setting with novel gradient identification and estimation. Also, a theoretical analysis of the suboptimality of the proposed method is provided. Finally, numerical experiments are conducted to evaluate the performance of the algorithm.

### Strengths
The gradient identification proposed is new to confounded POMDPs, and the policy gradient based on that is complimented by strong theoretical guarantees. The statistical error of the gradient estimation and the suboptimal of the obtained policy are both discussed with a comprehensive analysis. Also, The theoretical results are also complimented by experimental results.

### Weaknesses
While I typically do not complain about the empirical results of a theory paper, I do expect that the authors could show how to implement such estimation and algorithm on real practical RL problems.



### Questions
1. In the third paragraph of Section 3, does the definition of history $\mathcal{H}_{t}$ lack the subscript on $\mathcal{O}$ and $\mathcal{A}$?
2. The notation $Z_{t}$ has already been defined in Section 3; however, another $\mathcal{z}$ is used in Section 5 as additional notation. Are they the same things?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a policy gradient method tailored for confounded POMDPs with continuous state and observation spaces in the offline learning context. The authors present a novel method for non-parametrically estimating any history-dependent policy gradient in POMDPs using offline data. They employ a min-max learning procedure with general function approximation to estimate the policy gradient through solving a sequence of conditional moment restrictions.

The authors provide a finite-sample, non-asymptotic bound for the gradient estimation. Using the proposed gradient estimation method within a gradient ascent algorithm, the paper demonstrates the global convergence of the algorithm.

### Strengths
- The paper addresses a challenging problem on policy gradient methods for POMDPs in the offline setting with continuous state and observation spaces. This is a novel contribution to the best of my knowledge; most existing work on policy gradient methods has been centered around fully observable environments. 

- The paper’s contributions seem to be significant with the global convergence result of the algorithm to find the history-dependent optimal policy. Additionally, the identification result for non-parametrically estimating any history-dependent policy gradient under POMDPs using offline data is a unique contribution.

### Weaknesses
 - The paper introduces a significant number of symbols and notations, which might overwhelm readers, especially those who are less familiar with the topic. To improve clarity, the authors could consider providing a table or appendix that lists all the symbols used along with their definitions. Additionally, they might simplify the notation where possible and ensure that each symbol is clearly defined upon its first use. For example, the notation seems to be quite heavy at the end of Page 5 where $\mathcal{Z_t}$ and $\mathcal{W_t}$ are introduced.

- The full coverage assumptions stated in Assumption 4(a) and Assumption 5(a) are indeed common in offline RL literature, but they bring about challenges and potential limitations to the proposed method in the paper.

1.  **Full Coverage Assumption (Assumption 4(a))**: This assumption, which requires that the offline distribution $P_{\pi_b}$ can calibrate the distribution $P_{\pi_\theta}$ induced by $\pi_\theta$ for all $\theta$, is strong and might not always be satisfied in practical scenarios. In real-world applications, especially in domains like healthcare or finance, obtaining an offline dataset that sufficiently covers all possible actions and states can be impractical due to ethical, logistical, or financial constraints. The paper could improve by discussing the potential implications of this assumption, providing guidance on how to assess whether this assumption is reasonable in a given setting, or suggesting alternative approaches if the assumption is not met.

2.  **Optimal Policy Coverage (Assumption 5(a))**: This assumption requires that the optimal policy $\pi^*$ is covered by all the policies in the class. While this condition ensures that the policy class is rich enough to contain the optimal policy, it might be too restrictive in practice.

### Questions
How might the proposed method be adapted or extended to accommodate partial coverage assumptions, and what would be the technical challenges associated with such an adaptation? Could you provide insights or discuss potential ways for relaxing the full coverage assumptions while maintaining the theoretical guarantees of the method?


================================================

**After Rebuttal:**

Thank you for the detailed response. I feel like my concerns have been addressed by the authors' response, and I would like to raise my score to 8.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper theoretically studies the problem of offline policy optimization in POMDPs from a confounded offline data dataset, following the line of previous works on confounded POMDPs and policy gradient in MDPs. The core contribution is a deconfounded policy gradient ascent algorithm (Algorithm 1) based on proximal causal inference with theoretical guarantees. There are also numerical demonstrations to show the effectiveness of the proposed method.

### Strengths
1. The confounded offline POMDP setting itself is a well-motivated problem, and based on existing works it is natural to ask how to learn the optimal history dependent policy with computational efficiency. The authors answer this question by looking into the policy gradient style method which has not been explored in this literature.
2. The idea of using bridge functions (originated from proximal causal inference) to identify not only the policy value $\mathcal{V}(\pi_{\theta})$ but also the policy gradient $\nabla_{\theta}\mathcal{V}(\pi_{\theta})$ is new.
3. The theoretical derivations of the policy gradient identification is novel and is of independent interest to future research in confounded offline RL area.
4. The theoretical results are self-content and sound.

### Weaknesses
1. From my viewpoint, by looking into the previous line of works, the main theory (Sections 6.1 & 6.2) of this work is mostly based on **(i)** the theoretical understanding of statistical analysis for using minimax estimator to solve bridge functions in confounded offline POMDP settings, e.g., [1, 2, 3]; **(ii)** the analysis of global convergence of policy gradient ascent methods in standard MDP settings, e.g., [4, 5]. So the technical contributions of the main theory part are somehow weakened given these prior works.
2. As stated in 1., a consequence is that the theoretical assumptions regarding the policy gradient analysis (Section 6.2) are mostly adapted directly from those for MDP setups. How to understand these assumptions in POMDP settings with a history dependent policy class is less discussed. Specifically, the smoothness and positive definiteness assumptions on the policy gradient and Fisher information matrix, respectively, are not clearly justified in the context of POMDPs with history-dependent policies. Furthermore, the impact of the history length on these assumptions and the resulting convergence rates is not addressed, which is a crucial consideration when dealing with POMDPs.

### Questions
1. Continued from Weakness 1., I would appreciate it if the authors could highlight more on the technical contributions behind the main theory, especially when compared with the previous line of works listed.
2. Continued from Weakness 2., it seems that the paper does not contain any discussion of a concrete policy class example. I think this is important since we are now dealing with history-dependent policy class which is different from previous MDP policy gradient problems. How does the dependence on history change (or not change) the difficulty of doing policy gradient and why? It would be great if such discussions can be included.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
