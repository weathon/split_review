# General Framework for Off-Policy Learning with Partially-Observed Reward

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Off-policy learning (OPL) in contextual bandits aims to learn a decision-making policy that maximizes the target rewards by using only historical interaction data collected under previously developed policies. Unfortunately, when rewards are only partially observed, the effectiveness of OPL degrades severely. Well-known examples of such partial rewards include explicit ratings in content recommendations, conversion signals on e-commerce platforms that are partial due to delay, and the issue of censoring in medical problems. One possible solution to deal with such partial rewards is to use secondary rewards, such as dwelling time, clicks, and medical indicators, which are more densely observed. However, relying solely on such secondary rewards can also lead to poor policy learning since they may not align with the target reward. Thus, this work studies a new and general problem of OPL where the goal is to learn a policy that maximizes the expected target reward by leveraging densely observed secondary rewards as supplemental data. We then propose a new method called Hybrid Policy Optimization for Partially-Observed Reward (HyPeR), which effectively uses the secondary rewards in addition to the partially observed target reward to achieve effective OPL despite the challenging scenario. We also discuss a case where we aim to optimize not only the expected target reward but also the expected secondary rewards to some extent; counter-intuitively, we will show that leveraging the two objectives is in fact advantageous also for the optimization of only the target reward. Along with statistical analysis of our proposed methods, empirical evaluations on both synthetic and real-world data show that HyPeR outperforms existing methods in various scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies off-policy learning with partial rewards. In the considered setting, the rewards are partially observed and the authors assume a secondary reward information.  The authors provide a weighted objective for the original and secondary reward functions based on the off-policy policy gradient algorithms. The authors then give an unbiased estimator of the gradient of the policy value and prove that the variance is reduced if the policy learned by the secondary information is better than the policy only based on the partially observed reward.  A strategy to tune the balancing weight is also given. Both synthetic and real-world datasets are provided to validate the performance.

### Strengths
The paper has the following strengths:
+ The paper provides an unbiased estimator for the value based on secondary information and prove that the expected gradient is the same as the one without considering secondary information ($\beta=0$).
+ The authors formally prove the variance reduction due to the introduction of the secondary information and show the reduction exists if the policy learned by the secondary information is better than the policy only based on the partially observed reward.

### Weaknesses
The paper can be improved in the following aspects.
- It is common to consider a weighted combination of the original and secondary information in machine learning algorithms.  Similar strategies are used in few-shot learning [2], informed learning [1], etc. The authors need to compare the proposed algorithm with them and emphasize their uniqueness.
- The paper considers the setting with some types of reinforcement learning settings and secondary information, and the authors only consider policy gradient, so I would not regard the framework as "general".
-  The strategy to tune the weight $\gamma$ is straightforward. Can the authors show the improvement in theory?

### Questions
See the comments in weakness.

### Soundness
3

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
4

### Summary
This work presents an off-policy learning approach to efficiently optimise partially-observed reward. The authors first model the data generation process of this problem, assuming access to dense, secondary rewards that are correlated to the target reward. They introduce HyPer, an unbiased policy gradient method that leverage secondary rewards to better optimise the true target. Experiments validate the approach on synthetic and semi-synthetic problems.

### Strengths
- The paper is well written and is easy to follow.
- The problem of partially observed/delayed reward is of high importance.
- The formulation of the data-generation process is simple and can model diverse problems.

### Weaknesses
 - The contribution of the paper is twofold, first, the introduction of the framework of partially-observed rewards with presence of secondary rewards, that comes with a new data-generation-process (DGP), and secondly, the derivation of an unbiased policy gradient that can efficiently leverage all information to optimise the target. These two main contributions present some weaknesses:
   + The framework's data generation process (DGP) is **restrictive and was not properly tested**: If the DGP models missing, non delayed rewards, the claim that it can model delayed rewards is not supported, as these rewards can be observed after many interactions with the system and attribution of the reward to a certain action becomes the main difficulty [1]. The current formulation treats delayed rewards as simply missing, where $o=0$ and $r=N/A$ if not immediately observed. This approach fails to capture the temporal dependencies inherent in delayed rewards, where the reward is eventually observed and needs to be attributed to past actions. For example, in a video streaming platform, a user might watch several videos (and see multiple ads) before making a purchase on another website. This purchase is a delayed reward, and attributing it to the most recent interaction is suboptimal. The proposed DGP does not account for the temporal sequence of actions and the delayed observation of the reward, thus limiting its applicability to real-world scenarios involving delayed rewards.
   + The policy gradient approach relies on $p(o|x)$ **which is unknown**, thus the PG is never unbiased as we need to model $p(o|x)$. In addition, this quantity can be really hard to model in real life scenarios (For example, we do not know what explains why a user did not purchase an item after he clicked on it).
- The introduction of the combined policy value overloads the paper, and the story would have been simpler by defining a clear goal, which is to optimise the target reward, considered the north start in the majority of applications. 
- There is a problem in Equation (10), which is the core result of the paper. The gradient boils down to a doubly robust gradient that does not use any secondary reward. This is a major typo that needs fixing.
- The paper does not discuss important, theoretical contributions to OPL, even in the extended related work. These contributions are based on the pessimism principle and were proven to be optimal, contrary to using naive policy gradients. The following lines of work should be incorporated to the extended related work and discussed:
   + Counterfactual Risk Minimization: Learning from Logged Bandit Feedback. Adith Swaminathan, Thorsten Joachims
   + Bayesian Counterfactual Risk Minimization. Ben London, Ted Sandler Proceedings of the 36th International Conference on Machine Learning, PMLR 97:4125-4133, 2019.
   + PAC-Bayesian Offline Contextual Bandits With Guarantees. Otmane Sakhi, Pierre Alquier, Nicolas Chopin Proceedings of the 40th International Conference on Machine Learning, PMLR 202:29777-29799, 2023.
   + Importance-Weighted Offline Learning Done Right. Germano Gabbianelli, Gergely Neu, Matteo Papini Proceedings of The 35th International Conference on Algorithmic Learning Theory, PMLR 237:614-634, 2024.
   + Logarithmic Smoothing for Pessimistic Off-Policy Evaluation, Selection and Learning. Otmane Sakhi, Imad Aouali, Pierre Alquier, Nicolas Chopin.



### Questions
In addition to the weaknesses, I have the following questions:
- How can we test if the DGP hold in real world problems? The real world experiment section in your paper is still a synthetic experiment simulated (with the DGP you suggest) on real world data.
- In real world scenarios, we never have access to the observation probability $p(o|x)$. How do you estimate it in the real world? And what is the impact of its estimation in the efficiency of your algorithm?
- Why did you need to introduce the combined policy value? And why did you define it with the sum of secondary rewards? In addition, It is better to change the name to "policy combined value", "policy secondary value" as it reflects more the quantities defined.
- The baselines s-IPS and s-DR use aggregation function $F(s)$ over the secondary rewards, why they do not use also the primary reward when available, giving $F(s, r)$?
- If it is difficult to derive the theoretical value of $\gamma^*$ as defined in your paper, one can derive the theoretical value of $\gamma^{**}$ to minimise the MSE of the gradient, did you explore this path? 
- There is a new line of work [2] that optimises for long term reward, using dense, secondary/surrogate reward, is there a reason why you did not compare to it?
- Is there a reason why you did not include the large spectrum of pessimistic OPL? 

[2] Long-term Off-Policy Evaluation and Learning. Yuta Saito, Himan Abdollahpouri, Jesse Anderton, Ben Carterette, Mounia Lalmas

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the problem of off-policy learning in contextual bandits where rewards are only partially observable. In this setting, the authors propose using an auxiliary variable to reduce the variance of the double-robust inverse propensity weighted (IPW) estimator for the reward. They introduce a Hybrid Policy Optimization for Partially-Observed Reward (HyPeR) estimator, which incorporates an auxiliary-conditioned reward estimator to refine average reward predictions. Theoretical and empirical results demonstrate that when the auxiliary variable is highly correlated with the target reward, the HyPeR method surpasses baseline approaches in performance.

### Strengths
Incorporating auxiliary variables for variance reduction is a well-established idea in the ML community. However, the authors innovatively integrate this concept with the doubly robust estimator to tackle the challenge of limited data coverage under partially observable rewards—a contribution that appears novel. The experiments further support the theoretical insights, and the paper is generally clear and easy to follow, aside from a few errors and typos.

### Weaknesses
I noticed several potential technical issues (or possibly typos) that may impact the rigor of the results:

1. In eqn (6), you write down the distribution in a way that allow $r_i$ to also depend on $o_i$. This will cause the problem of confounding bias, which does not give rise to an unbiased estimator of $q(x, a)$. See Kato et al. 2021 or Pearl, 2009 for details. Is this a typo or is there something missing? I found in the proof of Theorem 1 that you indeed assume $r$ to be independent of $o$ when conditioned on other observable variables $(x, a, s)$. If this is an assumption, you should clearly state it.

2. In Eqn (10), you perhaps miss out a $o_i / p(o_i\,|\, x_i)$ term in the second line, as you cannot evaluate this term when $o_i = 0$ and $r_i$ is missing from the observational data. The absence of this term would lead to a biased estimator, particularly when $p(o_i | x_i)$ is small for some $x_i$.

3. In the proof of Theorem 2, what are $s_\theta^{(j)}(x, a)$, $\sigma^2(x, a, s, o)$? Are they also typos? You also miss out a variance symbol in the first line of the proof. The lack of clarity on these terms makes it difficult to verify the correctness of the proof. Specifically, the use of $s_\theta^{(j)}(x, a)$ is confusing since the policy is not parameterized by $\theta$ in the main paper, and the variance term should be conditioned on $(x,a,s)$ only, not $o$. 

Despite these concerns, I believe the variance reduction claim remains valid, as the paper’s approach can be interpreted as an application of the well-known Rao-Blackwell theorem.

### Questions
No further questions. My score reflects my current concerns about the technical soundness of this paper. I'm open to further discussions.

### Soundness
2

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
4

### Summary
The paper deals with the problem of Off-Policy Learning (OPL) in the contextual bandit domain. They focus, in particular, on the case where a secondary reward is fully observed while the target reward is, in general, partially observed. This is the case in many real-world applications, such as recommendation systems. The paper introduces Hybrid Policy Optimization for partially observed Reward (HyPeR), a method for improving off-policy learning (OPL) when target rewards are partially observed. By utilizing secondary rewards, the method aims to reduce variance in policy gradient estimation, thus improving learning efficiency. An empirical analysis (on synthetic and real data) is presented to support theoretical findings.

### Strengths
- Addresses a relevant issue in OPL with partially observed rewards: the issue is very relevant, since there are many real-world application domains where the target reward may be partially observed, but there are a lot of secondary reward signals available. This paper makes good use of those signals and practitioners may be interested in this

- New estimator with theoretical properties: the HyPeR estimator for the policy gradient is still unbiased and provably reduces (as long as \hat{q}(x,a,s) is more accurate than \hat{q}(x,a)) the variance of the estimation by introducing a sort of "control variate" using the secondary rewards. This is an important contribution.

- Empirical analysis on two datasets: I like the fact that the empirical analysis is done on both synthetic and real data, and also with a lot of different settings (e.g., varying data size, secondary-target reward correlation, etc.).

### Weaknesses
 - Section on the tuning procedure: in my opinion, this section may be a bit misleading (not intentionally, of course). This is because the authors claim that we can simply apply a cross-validation procedure to tune a hyperparameter as we do in the supervised setting. However, this is not so trivial as they claim: the fact that we are dealing with an Off-Policy problem means that the data is not iid with the target data. Hence, performing a cross-validation on such data will not give an unbiased estimation of the performance of the target policy. Nevertheless, it may be a heuristic way of performing hyperparameter tuning (I've seen papers in the OPE/OPL domain doing it), but it must be acknowledged that it is a biased way of performing hyperparameter tuning.

- I am not convinced of the design choices for the secondary targets in the experimental setting: let us consider the real data experiment. The authors say that the target reward is the watch ratio r. We would like however to provide a good PG estimate even when we do not observe this reward. They decide that they will do it with secondary rewards that they design to be *very* correlated with r. In particular, with s_1 and s_2, you can almost reconstruct r. Hence I am wondering if this experiment is really meaningful, since we would like to see what happens when we do not observe r, but we almost exactly observe it (albeit quantized: if s_2 = -1, then r < 0.5, if s_2 = 0 and s_1 = 0, then r \in [0.5, 2), if s_1=1, then r>= 2).

A very minor issue that did not impact the score:
- If I recall correctly, you never mention the fact that you focus only on contextual bandits in the introduction. Perhaps it is better to mention it somewhere in the intro, otherwise readers may be confused and think you are focusing on full RL.

### Questions
- Do you agree that the cross-validation procedure that you proposed is biased by design? In my opinion (if I am correct), you can still leave the section as is, but just acknowledge this caveat. Indeed, empirically, this procedure seems to work despite being biased, so it is not a big deal.

- Can you elaborate a bit on the design choices for the secondary rewards in your experimental settings?

- Can you provide ablation studies on the secondary reward dimensions? I would like to see which dimensions are responsible for the HyPeR good performance. My intuition would say that, in the real data case for example, it is because of s_1 and s_2, since you can almost construct the target reward r based on those. 

- Can you provide an ablation study on what happens when you perform cross-validation with sampling without replacement? You claim that it is important to have sampling with replacement. Do you have empirical data to support this claim? It can be useful for researchers in the future


Finally, it is not a question but more of a comment:
Your estimator of the policy gradient also seems robust to missing secondary rewards: if you set \hat{q}(x,a,s) to resort to \hat{q}(x,a) when there are missing s (for any reason), your estimator reduces to Doubly Robust, which is still an unbiased estimator.

### Soundness
2

### Presentation
3

### Contribution
3
