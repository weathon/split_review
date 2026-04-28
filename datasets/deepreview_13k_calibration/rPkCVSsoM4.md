# A Causal Lens for Learning Long-term Fair Policies

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
Fairness-aware learning studies the development of algorithms that avoid discriminatory decision outcomes despite biased training data. While most studies have concentrated on immediate bias in static contexts, this paper highlights the importance of investigating long-term fairness in dynamic decision-making systems while simultaneously considering instantaneous fairness requirements. In the context of reinforcement learning, we propose a general framework where long-term fairness is measured by the difference in the average expected qualification gain that individuals from different groups could obtain. Then, through a causal lens, we decompose this metric into three components that represent the direct impact, the delayed impact, as well as the spurious effect the policy has on the qualification gain. We analyze the intrinsic connection between these components and an emerging fairness notion called benefit fairness that aims to control the equity of outcomes in decision-making. Finally, we develop a simple yet effective approach for balancing various fairness notions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies long-term fairness through a causal decomposition framework. In particular, the authors first show that the total causal effect can be decomposed into a direct impact, delayed impact, and spurious impact. Moreover, a connection between benefit fairness and the causal effect of switching from a baseline policy to a virtual policy is established. In order to promote long-term fairness, the authors propose to update the PPO objective by introducing a fairness regularizer. Then the experiment section compares various methods on a simulated environment and the proposed method attains improved benefit fairness compared to the other methods.

### Strengths
1. The decomposition of long-term fairness into direct and delayed impact is interesting, although it is not surprising. The connection between benefit fairness and the proposed measure of fairness (through policy intervention in an MDP) is quite interesting.

2. The experimental section shows that the proposed modification of the PPO objective works, and in particular it can achieve approximate benefit fairness.

### Weaknesses
1. The authors claim that they introduce a general framework to study long-term fairness. However, the proposed framework is based on MDP which has been extensively studied in dynamic fairness. The use of an MDP framework, while common, does not inherently provide a general solution to long-term fairness, as many real-world scenarios may not fit neatly into the Markovian assumption. Furthermore, the specific structure of the MDP, such as the state and action spaces, can significantly influence the results, limiting the generalizability of the findings.

2. The causal decomposition result is very similar to existing decomposition results of causal fairness for static settings. In fact, the proof is very similar and the only difference seems to be that the indirect effect is replaced with the delayed impact. The core idea of separating direct and indirect effects is well-established in causal inference. The adaptation to a temporal setting by introducing a 'delayed impact' does not represent a substantial theoretical leap. The authors should more clearly articulate the novelty of this decomposition in the context of MDPs, especially considering the existing literature on causal inference in sequential decision-making.

3. Finally, the main drawback of the work is that there is no provable guarantee that the proposed method achieves long-term fairness. Since the result is not evaluated across a large class of benchmarks/simulation studies it is difficult to tell whether the method attains long-term fairness in different types of MDPS. The lack of theoretical guarantees is a significant limitation. The empirical evaluation, while demonstrating some improvement, is not sufficient to establish the robustness and reliability of the proposed method across diverse MDP environments. The authors should consider a more rigorous evaluation protocol, including a wider range of MDPs with varying characteristics.

### Questions
1. Is there a typo in Proposition 1 (main result)? The inner sum already marginalizes the feature $x'$.

2. You have expressed DPE in terms of benefit fairness. Can the same be done for the delayed impact effect?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies long-term fairness in causal reinforcement learning. The paper proposes the difference between the average qualification gain achieved by each group as their notion of long-term fairness and uses a PPO-type optimization objective to enforce fairness. Through a casual decomposition, the authors break down the qualification gain difference into 3 terms: direct impact, delayed impact, and spurious effects. Empirically, the paper studies how to lower the disparity in average qualification gains across groups and study the effect of each of the three terms.

### Strengths
-- The paper studies long-term fairness which is an important, yet understudied problem.

-- The paper proposes a novel fairness metric for long-term fairness in causal reinforcement learning.

### Weaknesses
 -- There are no technical algorithmic novelties in the paper as the optimization problem is inspired by PPO. This is not a major weakness as the paper introduces novel elements like the qualification gain function and proposes a causal decomposition of the qualification gain.

-- The experimental setup does not clearly show the advantage of the approach over prior baselines. For example, the difference between the worst and best approach is a mere 0.2% in all experiments in Figure 2. Are there other settings where this difference is more significant? The qualification gain disparity in Figure 3, does not go to 0 for each of the proposed metrics and seems to increase with increasing horizon. Can the authors provide why this is the case? Are there other settings where the qualification gain disparity goes to 0?

### Questions
-- Can the authors specify how I should interpret the results of Figures 2 and 3 in light of the weaknesses mentioned above?

-- What is the relationship of this notion of fairness, with the ones aiming to equalize rewards across all groups? See https://proceedings.mlr.press/v130/wen21a.html and references within.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper uses the causal perspective to study the long-term fairness problem where decisions can

### Strengths
1. The long-term fairness under causal inference perspective seems novel
2. The fairness penalty decomposition is useful in practice

### Weaknesses
1. Theoretical guarantee not sufficient:
(1). Convergence of the algorithm
(2). How the penalty coefficients \beta^{KL} and \beta^{\Lambda} quantitatively impact fairness and model performance (e.g., precision/recall per round)

2. Despite fairness metrics improvement, it is difficult to tell if the model performance improved and if the fairness-aware optimization can result in a Pareto superior result for every group or every individual, there should be more theoretical and numerical evidence on the utilities instead of just utility gaps

3. References:
(1). The long-term fairness problems are studied in a previous line of work related to repeated distributionally robust optimizations, e.g., "Fairness Without Demographics in Repeated Loss Minimization"
(2). The performative predictions and the strategic classification/regression problems are other research areas closely related to model decision having causal effect on data distribution, please compare with them

4. Similarities and differences between the new metrics and the conventional fairness metrics:
It will be more helpful to build connections between the fairness terms in the long-term causal formulation with metrics like demographic parity, equal opportunity, equalized odds in the conventional settings like single shot classification and regression problems, which I think equalized odds (both TPR and FPR being the same) as well as loss disparities do not have counterparts in the causal formulation, and I encourage authors to provide explanations on why not.

### Questions
1. Why fairness penalty instead of re-weighting in the optimization problem?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposed a general causal framework to characterize long-term fairness in reinforcement learning (RL) settings, where the unfairness is represented by "qualification gain disparity" between the advantaged group and the disadvantaged group ($C_{\pi}$). The authors decomposed the unfairness into three different parts (DPE, IPE, SPE) and used Proximal Policy Optimization (PPO) to optimize the decision policy. Particularly, DPE is closely related to benefit fairness (i.e., individuals from different groups who gain similar qualification improvement should have similar opportunities to get the treatment), and if the benefits are independent of the group attribute, then benefit fairness means with 0 DPE, demonstrating some kind of alignment between the long-term fairness proposed by the authors and benefit fairness. Motivated by this, the authors also added fairness as a separate term to the fair objective function. Thus, there are 2 fairness mechanisms ($PPO-C$, $PPO-Cb$) proposed, and the authors did simulation studies on real datasets to verify their findings.

### Strengths
1. Studying Long-term fairness as qualification gain disparity is well-motivated and of social importance.
2. I like the idea of the causal decomposition using $\pi_{PS}$.
3. The experiments demonstrate the effectiveness of the fairness mechanisms.

### Weaknesses
Overall, I think the paper is interesting, but so far it does not situate well in previous literature. I am willing to increase my score if the authors clarify their contribution.

1. Though I appreciate the efforts the authors made to compare their work to previous literature, I still feel the novelty of the paper is not clear enough. Firstly, just as the authors stated, [Hu et al., 2023, Hu & Zhang, 2022, Yu et al., 2022] considered long-term fairness in a causal framework. Especially for the framework proposed by [Hu & Zhang, 2022], the main difference seemed to be: (i) they considered the disparity of qualification rate (not the gain of qualification) as the fairness notion; (ii) they did not consider RL settings. Could the authors try making the comparison clearer?

2. There are other recent papers on strategic classification and performative prediction considering long-term fairness in terms of qualification rate improvement (also known as social welfare) when population distribution can be shaped by the decision policy (e.g., [Jia et al., 2024, Jin et al., 2024]). Moreover, there are at least two fairness notions related to qualification gain: (i) equal improvement [Guldogan et al., 2022]; (ii) bounded effort [Heidari et al., 2019]. It is necessary to review these papers.

3. The fairness mechanisms just stack all terms together and I am not sure about the novelty. Plus, in Figure 5, it seems that IPE and SPE are rarely influenced by the proposed fairness mechanisms. Could you explain why?

4. Why not provide error bars for Figure 4?

### Questions
1. Could you make your contribution clearer and review previous work more comprehensively? (weakness 1, 2)

2. Why are IPE and SPE not influenced by the fairness mechanisms? (weakness 3)

3. Could you justify why it helps by directly adding benefit fairness as another regularization term? (weakness 3)

4. Could you provide error bars for Figure 4, or am I missing something? (weakness 4)

### Soundness
3

### Presentation
3

### Contribution
2
