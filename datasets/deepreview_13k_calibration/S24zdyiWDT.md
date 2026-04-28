# Is Inverse Reinforcement Learning Harder than Standard Reinforcement Learning?

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8, 6

## Abstract
Inverse Reinforcement Learning (IRL)---the problem of learning reward functions from demonstrations of an \emph{expert policy}---plays a critical role in developing intelligent systems. While widely used in applications, theoretical understandings of IRL present unique challenges and remain less developed compared with standard RL. For example, it remains open how to do IRL efficiently in standard \emph{offline} settings with pre-collected data, where states are obtained from a \emph{behavior policy} (which could be the expert policy itself), and actions are sampled from the expert policy.

This paper provides the first line of results for efficient IRL in vanilla offline and online settings using polynomial samples and runtime. Our algorithms and analyses seamlessly adapt the pessimism principle commonly used in offline RL, and achieve IRL guarantees in stronger metrics than considered in existing work. We provide lower bounds showing that our sample complexities are nearly optimal. As an application, we also show that the learned rewards can \emph{transfer} to another target MDP with suitable guarantees when the target MDP satisfies certain similarity assumptions with the original (source) MDP.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper builds on recent works on Inverse Reinforcement Learning (IRL). It introduces a new metric different from the literature to analyze the distance between the feasible set of reward functions compatible with an expert's demonstrations in the limit of infinite samples and the estimated set. Their metric actually considers the distance between two mappings whose image set coincides with the feasible set. Next, the paper analyzes the sample complexity of estimating this mapping in the offline and online (forward model) settings. They provide algorithms for both the settings (and therefore upper bounds to the sample complexity) as well as lower bounds. Finally, the paper provides a sample complexity analysis on the error obtained when doing transfer learning with the estimated mapping, i.e., when transferring the estimated mapping instead of the true one.

### Strengths
- the main strengths are the sample complexity results for the offline and online (forward model) settings for IRL, which are the first results of this kind for IRL;
- the idea of connecting transferability with concentrability when analyze the transfer learning setting is interesting

### Weaknesses
 - the main strengths are the sample complexity results for the offline and online (forward model) settings for IRL, which are the first results of this kind for IRL;
- the idea of connecting transferability with concentrability when analyze the transfer learning setting is interesting

### weaknesses:
 - no technical novelty in the proofs which are based on (i) previous works on offline RL and (ii) previous works on IRL
- the lower bounds (both for offline and online settings) are definitely not tight, since they do not depend on the confidence $\delta$
- the metric introduced to evaluate the complexity in the offline setting is actually not a metric in the mathematical sense

### questions:
 I am willing to adjust my score if the authors successfully answer my questions.

1) Why do you use $d^\pi$ (Definition 3.1) as a (pre)metric between reward functions? This is not a metric, and therefore the problem that you highlight in Lemma C.4 for the Hausdorff distance between sets sussists also for your (pre)metric $D_\Theta^\pi$ (Definition 3.2). It might be that the proposed (pre)metric $D_\Theta^\pi$ is zero even if the reward sets do not coincide. 

2) What is the rationale behind choosing the (pre)metric in Definition 3.1? In the usual pipeline, the reward recovered by IRL is then used for training RL agents. It does not seem to me that the (pre)metric in Definition 3.1 guarantees anything on how close the performance of the trained RL agent with the learned reward. In "Towards Theoretical Understanding of Inverse Reinforcement Learning" the authors focus on the actual distance between reward functions, not induced value functions. Can the author elaborate?

3) Why do your lower bounds not depend on $\delta$? This is quite significant especially when $\delta$ is small. Inspecting the proofs in comparison with  "Towards Theoretical Understanding of Inverse Reinforcement Learning", it seems that the authors have adapted one construction only (the one that provides the part of the lower bound that does not depend on $\delta$). Why this choice?

4) How did you manage in the proof of the upper bound the fact that rewards defined as in the ground truth reward mapping are not bounded in $[-1,+1]$ even though the parameters $(V,A)\in\mathcal{V}\times\mathcal{A}$? In "Towards Theoretical Understanding of Inverse Reinforcement Learning", Lemma B.1 (appendix), they normalize the reward functions, but you don't. What allows you to avoid this step?

5) The lower bounds do not match the upper bounds, especially for what concerns the dependence on the horizon H. What is the reason for this gap?

COMMENTS:
- a section with the limitations of the results is missing and should be added;
- the title has nothing to do with the paper; the paper concerns a sample complexity analysis in the IRL setting, stop. Nothing in the paper gives novel results on whether IRL is harder than RL, so the title must be changed;
- the proof of the second part of Lemma C.1, although easy, is missing;
- the proof of Proposition C.2 is missing;
- in Section 1, Introduction, when listing the contributions, authors state that this work contributes at "providing an answer to the
longstanding non-uniqueness issue in IRL". This statement is factually false. Indeed, the authors investigate IRL as the reconstruction of the feasible reward set (and this formulation is not introduced in the paper), providing novel analysis for the offline and online (with forward model);
- the use of O-tilde is incorrect for what concerns the dependence on $\delta$. Conventionally, O-tilde does not hide dependences on $\log(1/\delta)$. This is not just a cosmetic comment, but seems to hide an additional term present in the upper bound and not present in the lower bound, spotting an additional term that is not matched;
- you use the same symbol $d$ for both the visit distribution and the metric, and maybe you could change one of the two symbols to improve the presentation;
- the paper contains many typos both in the main paper and in the appendix.





- **[On the use of $d^{pi}$]** While I fully agree on the impossibility of using the $L_\infty$-norm of the difference between rewards, I don't really agree on the fact that the expectation under $d^{\pi}$ is a proper index. Indeed, the authors claim that " $d^{\pi}$ (Definition 3.1) can provide guarantees for performing RL algorithms or doing transfer learning with learned rewards (see Section C.2 and I.3).", but looking at Section C.2, only with $d^{all}$ it is possible to have guarantees when performing RL. It doesn't seem that for the offline setting the authors are able to provide guaranteed w.r.t. $d^{all}$. This makes the argument in favor of $d^{\pi}$ quite weak in my opinion.

- **[On the dependence on $\delta$]** I am not satisfied by the authors' answer about the role of $\delta$ in the bounds. The authors claim that the bounds hold for $\delta \le 1/3$. However, there is no presence of $\delta$ in the sample complexity lower and upper bounds. It is hard to believe that such dependence is really not present since when $\delta \rightarrow 0$ clearly the sample complexity must diverge to infinity. One possibility is that the authors have hidden it in the $\widetilde{O}$. I have already pointed out that the **proper use of $\widetilde{O}$ should not hide the polynomial dependence on $\log(1/\delta)$**. This is indeed the case for the upper bounds reported in the paper. However, looking carefully at the lower bounds proofs, there is no dependence on $\log(1/\delta)$ (but only on $1-\delta$). This spots an important lack of tightness since the lower bound does not diverge to infinity when $\delta\rightarrow 0$. **I want to stress that this in combination with an inappropriate use of $\widetilde{O}$ is severely hiding a suboptimality of the lower bound in comparison with the upper bounds**.

- **[Title]** I remain convinced that the chosen title is inappropriate.

- **[Pessimism]** By re-reading the paper, I realized that the use of pessimism in the reward function has a quite strange effect compared to pessimism in standard off-line RL. Here, pessimism is directly applied to the reward function (eq. 4.4) but it does not seem to have a significant role in the ability to achieve the desired results. From a technical perspective, looking at eq. (E.8), if we do not use pessimism we just obtain the bonus $b^\theta_h(s,a)$ instead of twice the bonus $2 b^\theta_h(s,a)$; but the pessimism has no impact on the computation of $C^*$. This is radically different compared to the case of off-line RL where the pessimism is essential to obtain the desired covering wrt to the optimal policy (instead of the undesirable uniform covering over all the policies). I am aware that I am raising this point by the end of the discussion period, but I think that **if the role of pessimism is so marginal in the paper (as I suspect at this point) and if without using it, it is possible to derive the same results, this is an important concern to report. I would really appreciate it if the authors could say whether without pessimism they can obtain (apart from constants) the same results.**

### Questions
I am willing to adjust my score if the authors successfully answer my questions.

1) Why do you use $d^\pi$ (Definition 3.1) as a (pre)metric between reward functions? This is not a metric, and therefore the problem that you highlight in Lemma C.4 for the Hausdorff distance between sets sussists also for your (pre)metric $D_\Theta^\pi$ (Definition 3.2). It might be that the proposed (pre)metric $D_\Theta^\pi$ is zero even if the reward sets do not coincide. 

2) What is the rationale behind choosing the (pre)metric in Definition 3.1? In the usual pipeline, the reward recovered by IRL is then used for training RL agents. It does not seem to me that the (pre)metric in Definition 3.1 guarantees anything on how close the performance of the trained RL agent with the learned reward. In "Towards Theoretical Understanding of Inverse Reinforcement Learning" the authors focus on the actual distance between reward functions, not induced value functions. Can the author elaborate?

3) Why do your lower bounds not depend on $\delta$? This is quite significant especially when $\delta$ is small. Inspecting the proofs in comparison with  "Towards Theoretical Understanding of Inverse Reinforcement Learning", it seems that the authors have adapted one construction only (the one that provides the part of the lower bound that does not depend on $\delta$). Why this choice?

4) How did you manage in the proof of the upper bound the fact that rewards defined as in the ground truth reward mapping are not bounded in $[-1,+1]$ even though the parameters $(V,A)\in\mathcal{V}\times\mathcal{A}$? In "Towards Theoretical Understanding of Inverse Reinforcement Learning", Lemma B.1 (appendix), they normalize the reward functions, but you don't. What allows you to avoid this step?

5) The lower bounds do not match the upper bounds, especially for what concerns the dependence on the horizon H. What is the reason for this gap?

COMMENTS:
- a section with the limitations of the results is missing and should be added;
- the title has nothing to do with the paper; the paper concerns a sample complexity analysis in the IRL setting, stop. Nothing in the paper gives novel results on whether IRL is harder than RL, so the title must be changed;
- the proof of the second part of Lemma C.1, although easy, is missing;
- the proof of Proposition C.2 is missing;
- in Section 1, Introduction, when listing the contributions, authors state that this work contributes at "providing an answer to the
longstanding non-uniqueness issue in IRL". This statement is factually false. Indeed, the authors investigate IRL as the reconstruction of the feasible reward set (and this formulation is not introduced in the paper), providing novel analysis for the offline and online (with forward model);
- the use of O-tilde is incorrect for what concerns the dependence on $\delta$. Conventionally, O-tilde does not hide dependences on $\log(1/\delta)$. This is not just a cosmetic comment, but seems to hide an additional term present in the upper bound and not present in the lower bound, spotting an additional term that is not matched;
- you use the same symbol $d$ for both the visit distribution and the metric, and maybe you could change one of the two symbols to improve the presentation;
- the paper contains many typos both in the main paper and in the appendix.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper gives theoretical guarantees for both online and offline setting in the inverse reinforcement problem.

### Strengths
I think this work really pushes the inverse RL community research efforts further by answering:

> can we give theoretical guarantees for the inverse RL algorithm enforced by pessimism for offline and exploration for online settings?

This is a really nice idea worthy for publication. My score reflect the weaknesses.

### Weaknesses
Firstly note that this is an emergency review. I will rely on discussion with authors and reviewers, and other reviews, to decide on the score.

I have only a few weaknesses for this work as follows:

- The main paper writing needs to be improved. Yes, the soundness of this paper maybe good, considering similar pessimism and exploration ideas from past works. But this submission looks like a hurried submission with many typos like `Theoretical low bound in offline setting.`, ` $\pi_b = \pi_E ().,$`, `RLP utilizes empirical MDP and Pessimism frameworks`, `for all offline IRL problems with probability at least $1 − \delta$, has to take at least ... samples in expectation.` (both h.p. and in expectation?!), and so on. In addition to typos, the out-of-margin equation formatting makes a strenuous reading experience. To be honest, I am not sure if the authors can fix this writing issue of 56 pages during the rebuttal period, but I will welcome some attempts since proceedings require good quality.

- The closest work I can think of is [1] that provides theoretical guarantees for imitation learning ($\approx$ reward-free IRL+RL) in both online and offline data setting. The current work stops at reward learning, that is, the IRL problem. But without the extra RL step using the learned reward, is an incomplete story. The paper talks about similarities with RLHF; yes, there is a connection but one needs to eventually learn the optimal policy. Yes, one can just do planning with the learned reward and learned transition model, but equipping it with traditional model-based guarantees is important for making connections with other relevant works. _Model based guarantee_ will be unsatisfactory since [1] gives results for general function approximation. 

- Moreover, this manuscript subsumes many results from (Li et al., 2023) which is a non-peer reviewed work. This makes it hard to check soundness since one needs to evaluate both (at least the relevant parts required for this submission). I am mentioning this due to my emergency review. My score reflects the fact that generative model setting (samples from every state-action pairs $\approx$ uniform concentrability) in Lindner et al. (2023), is equipped with pessimism and optimism terms to account for partial concentrability using the usual techniques in offline RL (Rashidinejad, et al. 2021) and thereafter.

### Questions
-na-

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes RIP and RLE method which opterates in offline and online IRL settings respectively. These methods do have some theoretical guarantees.

### Strengths
1. This paper builds metrics for both online and offline IRL settings. 
2. Informed by the pessimism principle, RLP is proposed for offline IRL setting with theoretical guarantees. 
3. RLE achieves great sample complexity compared to other online IRL methods.

### Weaknesses
Lack of some experiment results.

I think the theoretical analysis for IRL is important. However, the title of this paper is a little confusing. The sample complexity analysis seems not relevant to this title.

### Questions
None

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of inverse reinforcement learning: given observations of an expert policy deployed in a (tabular) MDP, what reward function can one learn which is consistent with the actions of the expert policy? They consider both the offline (batch) setting as well as the online setting. They propose a metric for inverse reinforcement learning, defined in terms of the difference between the learned and ground truth rewards.

For the offline setting, they propose a pessimistic algorithm and show it achieves poly(S, A, H) sample complexity, as well as some dependence on the concentrability coefficient. For the online setting, they propose an algorithm which also achieves poly(S, A, H) sample complexity (and uses the offline algorithm as a subroutine). There is also an extension to a "transfer learning" setting.

### Strengths
- The paper is thorough, detailed, and mathematically rigorous. (As a disclaimer, I only checked in detail the proofs and associated lemmas for Thm 4.2, their main result on the sample complexity of the offline algorithm; but I am familiar with most of the literature and techniques used for online/offline tabular RL, so the results seemed correct to me.)
- To me, the most interesting contribution is the new notion of "performance", which is measured in terms of a uniform distance for a set of "reward mappings" (Defn 2.1). I think this notion of metric merits future discussion and is a valuable contribution to this area. However, I have some comments/questions about it - see below.
- On the algorithmic side, this paper also shows how several existing techniques (i.e., pessimism, reachable state identification / reward free exploration) can also be adapted to the IRL problem. While the algorithms and analysis themselves are not particularly novel, it is nice that we can use well-studied techniques in RL for the IRL problem.

### Weaknesses
 - Given that this paper proposes new metrics for IRL, I found the discussion / comparison with previous work a bit vague. At times, the language and writing was a bit informal, and sometimes confusing to interpret.
    - For example, in the appendix you write that "our method that considers is greater than theirs". What does it mean for a method to be greater than another method? Did you mean your metric?
    - You write in C.3 that the "metric can't capture transitions". What does this actually mean? Specifically, does this mean that the metric is invariant to changes in the transition dynamics, and if so, is this a desirable property?
- I would urge the authors to rewrite their comparison with prior work in Appendix C, focusing on cases where one subsumes the other, and giving concrete examples when your algorithm(s) can achieve guarantees while previous algorithms cannot. What is currently lacking is a distinction in the writing between (1) comparing the quantities $d^{\pi}$ and $d^{\mathrm{all}}$ themselves to prior work; (2) comparing guarantees that your algorithms can achieve to guarantees that algorithms from prior work can achieve. For example, it would be helpful to see a concrete example of an MDP and expert policy where prior methods fail, but the proposed method succeeds, and vice versa.
- (minor) weakness: the upper/lower bounds seem to be loose. In particular, it would be good if the authors commented on the fact that the lower bound has a $\min \{S, A\}$ term - where does this come from? can it be improved? In general, the regime that we care about is when $S \ge A$, so the fact that the rate is only sharp when $S \le A$ is not very meaningful. Furthermore, the dependence on $H$ in the lower bound seems to be $H^2$, while the upper bound is linear in $H$, which is a significant gap.

Minor comments:
- Many typos throughout, especially in the appendix. Some examples:
    - "Broaderly" in the first paragraph.
    - e.g., at bottom of page 4, "Given a policy $\pi$, We" -> lower case the "we".
    - a missing citation before Corollary 4.3? I see an "()".
    - "week transferability" should be "weak transferability"?
    - some typo in the equation (C.6).
    - At the beginning of page 23, in the first display equation, should it be $a \in \mathrm{supp}$ instead of $a \notin \mathrm{supp}$?
- For lower bounds, use $\Omega$, not $O$.
- In the algorithm pseudocode, a quantifier over the set $\Theta$ is missing: The algorithm needs to be run separately for every $\theta \in \Theta$.

### Questions
1. I'm a bit confused about the discussion of the Hausdorff metric used by Metelli et al. The quantity that they propose seems to be some notion of diameter. I'm not sure why it should go to zero as you collect more samples, as even when $\mathcal{R} = \widehat{\mathcal{R}}$ the quantity doesn't seem like it should be zero since the set of possible rewards could be large. But your results imply that an upper bound on this quantity goes to zero, so what am I missing here?
2. While the definition of the metric seems mathematically well defined, it seems a bit weird: to define the reward mapping, you need a value and advantage function (V,A) (e.g., Eq. 3.2). However, inside the definition of the metric, you define a new value function of a particular policy and reward function (e.g., in Eq. 3.1). How do these two value functions relate?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
