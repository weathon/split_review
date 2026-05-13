# Distribution-Dependent Rates for Multi-Distribution Learning

- Decision: Reject
- Scores: 3, 6, 6, 5

## Abstract
To address the needs of modeling uncertainty in sensitive machine learning applications, the setup of distributionally robust optimization (DRO) seeks good performance uniformly across a variety of tasks. The recent multi-distribution learning (MDL) framework \cite{pmlr-v195-awasthi23a-open-prob} tackles this objective in a dynamic interaction with the environment, where the learner has sampling access to each target distribution. Drawing inspiration from the field of pure-exploration multi-armed bandits, we provide \textit{distribution-dependent} guarantees in the MDL regime, that scale with suboptimality gaps and result in superior dependence on the sample size when compared to the existing distribution-independent analyses. We investigate two non-adaptive strategies, uniform and non-uniform exploration, and present non-asymptotic regret bounds using novel tools from empirical process theory. Furthermore, we devise an adaptive optimistic algorithm, LCB-DR, that showcases enhanced dependence on the gaps, mirroring the contrast between uniform and optimistic allocation in the multi-armed bandit literature.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses the multi-distribution learning problem, where the learner aims to optimize the model's worst-case performance across a set of distributions. The main contribution is a reformulation of this problem as a pure exploration multi-armed bandit task and obtain simple regret bounds that depend on the sub-optimal gap of actions. The first part of the paper studies the non-adaptive case, where the learner cannot interact with the environments. Here, the authors provide simple regret bounds for both uniform exploration (UE) and non-uniform exploration (NUE). The second part explores the interactive case, where environment interaction is permitted, and proposes an LCB-based algorithm that better a lower simple regret than UE.

### Strengths
- This paper offers a new perspective by formulating multi-distribution learning as a pure exploration problem in multi-armed bandits.
- Based on this view, gap-dependent bounds are derived for both adaptive and non-adaptive cases for the multi-distribution learning problem.

### Weaknesses
 - **On the Significance of the Results:** One of my main concerns is the significance of the results achieved in this paper, as they rely on strong assumptions, and their implications are not rigorously discussed.  
   - **Assumptions:** The paper appears to address a simplified case where the action space $ \mathcal{A} $ is discrete and finite, and the data space is restricted to 1-dimension in the analysis. In contrast, continuous decision sets are more commonly studied in the literature, such as Blum et al. (2017), Sagawa et al. (2020), and Soma et al. (2022). Although Section 5 discusses an extension to infinite decision sets, the proposed approach using an $ \epsilon/k $-cover would result in a method with prohibitive computational costs. This is particularly concerning as the complexity of constructing such a cover scales exponentially with the dimension of the action space and the data, making it impractical for many real-world scenarios. The paper does not adequately address the computational implications of this exponential scaling.
   - **Results for the Non-Adaptive Case:** It is not entirely clear to me why the results for Non-Uniform Exploration (NUE) would be better than Uniform Exploration (UE), as the NUE outcomes depend on $\min_Q{n_Q}$, which could potentially be very small. The arguments in Section 3.3 are too intuitive to me, with several approximations made that require further justification. For instance, I am confused by the statement "considers a case $\Delta_{DR}(a) \approx B_n$"  in line 321. It is uncertain whether we can disregard the term $\Delta_{DR}(a) - B_n$ in the comparison, as this term varies across arms, and the value of $B_n$ differs between UE and NUE cases. The analysis lacks a clear condition on when NUE strictly outperforms UE, relying on asymptotic arguments that are not sufficiently rigorous. Specifically, a more detailed analysis is required to understand how the interplay between $\min_Q n_Q$ and the variance of each distribution impacts the overall regret bounds.

- **On the Proposed Method in Section 4:** The proposed method for adaptive cases requires knowledge of $H_j$, which depends on the suboptimal gap $\Delta_{a,\min}$ and is generally unknown in practice. Although the authors provide some discussion in Remark 4, it remains unclear how this issue would be addressed. Additionally, the setting of $\epsilon_t$ is also confusing. While this quantity appears to only require to be lower bounded, it is still unclear how to set this value to ensure that Condition Eq. (1) is not violated.
- **About literature review**:  The discussion of the convergence rate for related work in lines 139-152 is inaccurate. Although Soma et al. (2022) claim a result of $O(\frac{\sqrt{B^2 + k}}{T})$, their analysis overlooks the non-oblivious property of the learning process, rendering the result invalid. This issue was identified by Zhang et al. (2023), and the currently best-known result remains $O(\frac{\sqrt{B^2 + k \log k }}{T})$ in this line of research. One may check Section 2.3 in Zhang et al 2023 for a discussion.

### Questions
- Is it possible to extend the results to continuous spaces without a significant increase in computational complexity? For example, could pure exploration in linear bandit settings be considered?
- Could you provide more detailed explanations on the comparison between UE and NUE? (Please refer to the first point under weaknesses for a more detailed discussion.)
- How can the parameter $T_j$ be set in practice to ensure the theoretical guarantees?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies multiple distribution learning (MDL) from bandit optimization point of view. By connecting pure-exploration setting in bandits to MDL, it develops instance-dependent sharp regret rates, thereby improving the current instance-agnostic rates in the MDL literature.

### Strengths
The paper uses techniques from pure-exploration bandits to develop instance-dependent simple regret rates, which serves as less-conservative complements to the current instance-agnostic MDL error bounds.

### Weaknesses
 - The paper claims one of its contribution being developing problem-dependent rates for MDL, because “Oftentimes, it is more intuitive to analyze the learner’s performance in a fixed setting, as opposed to considering a worst-case instance for each sample size. When domain knowledge is available, a “one-size-fits-all” rate does not provide any insight on how to take advantage of this information”. However, the upper bound rates developed in this paper depend on the knowledge of the unknown optimality gap; how would this be integrated into domain knowledge remains unclear. Specifically, the practical utility of instance-dependent bounds is diminished if they rely on parameters that are as difficult to estimate as the optimal solution itself. The paper should clarify how these bounds offer a practical advantage over instance-agnostic bounds, given this dependency on the unknown optimality gap.
- The problem setting seems very similar to Kirschner et al for distributionally robust online contextual bandit problem, but no discussion is provided on the differences and connections. The absence of a discussion on the relationship to this line of work is a significant oversight, as it leaves the reader questioning the novelty and positioning of the proposed approach within the broader landscape of distributionally robust learning. A more thorough comparison is needed to establish the unique contribution of this paper.


### Questions
- Following up the first point in the weaknesses, Would the story of the paper rather be, given the knowledge that the uncertainty set $\mathcal{U}$ is fixed, one can develop exponential rates that scale with an unknown but fixed sub-optimality gap of each arm? 
- The paragraph in the introduction states “The current literature is populated with distribution-independent rates”, but there were not any relevant literature cited in this paragraph.
- How would the proof be adjust to accommodate the case where the learner interacts with the environment but the optimal arm is non-unique?
- Typo on Line 223: a fixed number times -> a fixed number of times

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors study distribution-dependent guarantees in the multi-distribution learning framework. They prove that distribution-dependent bounds are tighter than distribution-independent bounds. Specifically, they derive finite sample bounds under uniform and non-uniform exploration and propose an algorithm that improves over non-adaptive counterparts.

### Strengths
The authors clearly compared the finite sample bounds under uniform exploration against that under non-uniform exploration, and they highlighted where non-uniform exploration could have gains.

### Weaknesses
The authors clearly compared the finite sample bounds under uniform exploration against that under non-uniform exploration, and they highlighted where non-uniform exploration could have gains.

The authors compared their proposed algorithm against uniform sampling, but not non-uniform sampling. Non-uniform sampling benefits from varied sampled sizes and would be a stronger baseline to compare against. 

It would be nice to provide experimental results, even in very simple set ups, to showcase the strength of their proposed algorithm. The main results of this work are in theoretical results and there are substantial theoretical contributions, and thus I understand the experimental results may not be necessary.

### Questions
How does this work relates to active learning, where one would also take an adaptive strategy? What are the barriers that prevent active learning algorithm from being applied to the problem setting studied in this work? 

Are there relevant lower bounds available? If so, how do the upper bounds proven in this work compare to the lower bounds?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents innovative strategies within the framework of Multi-Distribution Learning (MDL), with the primary objective of identifying the best-performed distribution. It is informed by principles from Distributionally Robust Optimization (DRO) and multi-armed bandit theory, proposing both non-adaptive and adaptive methodologies. The non-adaptive techniques, namely Uniform Exploration (UE) and Non-Uniform Exploration (NUE), yield both distribution-independent and distribution-dependent bounds. Furthermore, the paper introduces an adaptive method in the interactive environment, LCB-DR, which further optimizes performance by employing optimistic sampling strategies analogous to the Upper Confidence Bound for Exploration (UCB-E) utilized in multi-armed bandit scenarios.

### Strengths
The paper is well-written and clearly conveys the problem setting and the conclusion to the reader. This work provides a distribution-dependent bound with analysis, which has not been reported in the literature. The distribution-dependent bound enjoys an exponential decay which can be compared to the probability of identification failure in the Best-arm Identification. Furthermore, this paper does not limit itself to non-adaptive exploring but extends to an adaptive exploring strategy, which is the UCB-E algorithm.

### Weaknesses
Since the author mentions that MDL draws inspiration from multi-armed bandits, I have found that identifying the best-performed distribution can be viewed as an analogy to identifying the best arm (BAI) in MAB. In lines 199-203, the author also mentions a connection between this work and BAI, which is a $H_a$ term; It would be better if the author could draw more comparisons between MDL and BAI. Specifically, the structural similarities between the Uniform Exploration (UE) strategy in this paper and the UE approach in the BAI literature could be further elaborated. In the BAI context, UE typically involves sampling each arm a fixed number of times and selecting the arm with the highest empirical reward. How does this translate to the MDL setting, where the objective function involves a minimization over distributions? Furthermore, the paper's LCB-DR algorithm appears to employ the Upper Confidence Bound for Exploration (UCB-E) strategy to identify the worst-performing distribution for each decision. A more detailed comparison of how UCB-E is adapted to the MDL framework would be beneficial. Since several works in BAI can achieve instance-independent bound [1,2], how does the objective upper bound guarantee relate to the existing bound shown in the BAI literature? I believe it is important to show whether the given bound is tight when reducing the problem setting to the existing work. Specifically, does the derived bound in this paper match or improve upon known bounds in the BAI literature when specialized to the simpler setting of identifying the best arm? This would help establish the tightness of the bound and provide a clearer connection to existing work.

### Questions
- What is the definition of $a^\star$ in lines 199-203.

- What is $l$ appearing in the RHS of Eq in lines 263-266?

- Is $M$ a known parameter or an unknown parameter to the agent?

- In lines 320-321, why $\Delta_{\text{DR}}(a) \approx B_n$ induces the comparison to be $\tfrac{M^2}{n}$ v.s. $\sigma^2_T + \Sigma^2_T + V_T$? Both exponential terms should be $1$ when the exponential factor becomes $0$.

### Soundness
3

### Presentation
4

### Contribution
2
