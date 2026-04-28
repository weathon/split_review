# Multi-level Certified Defense Against Poisoning Attacks in Offline Reinforcement Learning

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 3, 8

## Abstract
Similar to other machine learning frameworks, Offline Reinforcement Learning (RL) is shown to be vulnerable to poisoning attacks, due to its reliance on externally sourced datasets, a vulnerability that is exacerbated by its sequential nature. To mitigate the risks posed by RL poisoning, we extend certified defenses to provide larger guarantees against adversarial manipulation, ensuring robustness for both per-state actions, and the overall expected cumulative reward. Our approach leverages properties of Differential Privacy, in a manner that allows this work to span both continuous and discrete spaces, as well as stochastic and deterministic environments---significantly expanding the scope and applicability of achievable guarantees. Empirical evaluations demonstrate that our approach ensures the performance drops to no more than 50% with up to 7% of the training data poisoned, significantly improving over the 0.008% in prior work (Wu et al., 2022), while producing certified radii that is 5 times larger as well. This highlights the potential of our framework to enhance safety and reliability in offline RL.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors investigate certified poisoning defenses in offline RL. The authors employ DP approaches to achieve both action and policy level robustness guarantees.

### Strengths
* The paper is very well presented. As someone who is not very familiar with RL poisoning, or certified defenses to poisoning, I think the exposition and organization in the paper was great. The flow was logical and the writing, definitions, and lemmas/theorems were all clear. 
* The experimentation is thorough and provides reasonable empirical justification for the proposed method.

### Weaknesses
 * Although the proposed method does offer transition-level certified robustness, it seems like the trajectory level results presented in Table 1 do not always show an improvement from the proposed method. I'm specifically looking at the Breakout results. I do acknowledge that the proposed method also works for continuous action spaces, and has other flexibility advantages, so I do not consider the previously mentioned results to be of great concern.
 * The need to train multiple policies could prove cumbersome in certain settings, and may dissuade practitioners from adopting this approach.
 * The paper lacks a thorough discussion of the practical relevance of the threat model. While the authors cite a survey, it's unclear how these attacks manifest in real-world offline RL systems. The paper would benefit from a more detailed explanation of the specific attack vectors and their potential impact, beyond the theoretical framework.

### Questions
I'm curious to know how much of a threat existing attacks against offline RL systems actually pose. I know this isn't the focus of this work, but it would be nice to have a bit of explanation about attack specifics/provide more grounding as to why practitioners should be concerned beyond the cited Kumar et al. survey (which I'm not sure is specific to RL poisoning.)

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper studies the problem of robust DRL algorithms against data poisoning attacks. Based on the idea from differential privacy, it provides a provably robust framework such that by combining an RL algorithm with the framework, one can get a new learning algorithm with a high-probability guarantee on the lower bound of the performance of the learned policy under the attack with a certain level. Compared to the previous work COPA, the performance of the method in this work increases significantly: the performance drops to no more than 50%, with up to 7% of the training data poisoned. At the same time, the percentage COPA can guarantee is only 0.008%. In some sense, this paper develops the first practical and provably robust DRL framework.

### Strengths
1. This paper studies an important problem. The threat of poisoning attacks in the real world should not be underestimated. It is crucial to develop methods that are robust against such attacks.

2. This paper provides a framework that can make a class of RL algorithms robust, which is much more powerful than providing a single robust algorithm

3. This paper provides strong theoretical guarantees on its learning framework instead of empirical evaluation, which is especially important for developing trustworthy algorithms. 

4. It is interesting to see how ideas from differential privacy help develop a provably robust algorithm in the DRL setting.

5. This paper provides the first practical DRL algorithm/framework against poisoning attacks. The previous work, COPA, had poor performance, which is hard to be realistic about. The experiments result show that the method in this work has a much better performance.

### Weaknesses
1. This work does not investigate the lower bound of the guarantee one can get for a robust DRL algorithm under the poisoning attack. So, it is unknown if the method in this work is optimal and the gap between them. It would be beneficial to explore if the current framework's performance is close to the theoretical limits of what's achievable with a differentially private approach, or if there's a significant gap that could be closed by future research. This would involve analyzing the tightness of the privacy bounds and their impact on the performance guarantee.

2. The attack's power is too great and unrealistic. The learning algorithm assumes that the attacker can modify some trajectories arbitrarily without any constraint, which may not be realistic for the attack. Currently, the method expects a 50% drop in performance for robustness against 7% of data corruption, which costs too much and can be a consequence of the attack being unrealistic. The assumption that an attacker can arbitrarily modify trajectories, without any constraints on the magnitude or frequency of changes, is a strong one. In practice, attackers might be limited in their ability to make such drastic changes, and it's important to consider more realistic attack models that reflect these constraints. For example, attackers might only be able to modify a limited number of transitions or introduce small perturbations to the existing data.

3. It is unclear exactly what will happen to the robust algorithm under some practical attacks. The bound provided in the theoretical analysis might not be tight, especially for the practical attacks that do not lead to the worst case. It will be great to see what is the performance and behavior of your robust algorithms under actual attacks. The theoretical guarantees are valuable, but it's crucial to understand how the algorithm behaves under practical attacks that might not align with the worst-case assumptions. For instance, an attacker might introduce subtle but consistent biases in the data, which could have a different impact than the arbitrary modifications considered in the theoretical analysis. It would be helpful to evaluate the algorithm's performance under a range of practical attack scenarios and compare it with the theoretical bounds.

4. The discussion on the application of differential privacy in RL is missing in the related works

### Questions
1. The legends in the figures are missing. They are only explained in the caption.

2. It is important to give a good method a good name. However, it is unclear to me what we should call the method in this work. Could you consider an official name for your method?

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a certified defense framework for certifying offline reinforcement learning algorithms against two levels of poisoning attacks, transition-level and trajectory-level. The proposed algorithm leverages differential privacy (DP) techniques; the derived theoretical guarantees regarding per-state action and expected cumulative reward arises from the properties of DP. Compared to prior works, the proposed work can handle continuous action space and stochastic transition. Empirical evaluations demonstrated the effectiveness of the proposed approach.

### Strengths
1. The proposed framework extends beyond the previous work and can handle several important variations including continuous action space, stochastic transition, as well as a transition-level poisoning adversary.
2. The authors conducted extensive evaluations and offered concrete discussions and comparisons.

### Weaknesses
1) One major issue with the current status of the draft is the lack of clarity. Important technical details are missing, e.g., the authors didn't clarify how DP is used in the framework; I assume it is through applying DP-SGD when training each sub-policy to ensure each of the obtained set of policies is DP, but this is definitely important technical detail that shouldn't be omitted. Moreover, it's confusing when the authors mentioned in line 240 "depending on whether the DP training algorithm provides transition- or trajectory-level guarantees" while not providing any detail re. what exact algorithm offers what guarantee. An outline of the training/aggregation/certification algorithm will significantly improve the readability. 
2) Discussion and comparison with prior works are insufficient, which makes it hard to assess the contribution of the proposed work. The paper didn't make it clear re. what's new in this work & what's different from prior works. 1) The notion of policy-level robustness and action-level robustness was already proposed in Wu et al., 2022, then what is new in Sec 3.2; why the highlight of "multi-level" if it's already covered in the prior work? 2) The authors pointed out the limitation of the prior work being restricted to deterministic environment and discrete action space. Algorithmically, what difference in the proposed approach enables it to address these challenges? The comparisons are particularly important but are missing in the draft. 
3) In the experiments, the authors compared with the PARL algorithm in Wu et al., 2022, but the prior work proposed two other algorithms TPARL and DPARL which were reported to achieve better results than PARL on some datasets. It is unclear how the proposed algorithm compares with the two stronger algorithms in the prior work. 

Minors:

- Lack of mathematical rigor & typos in various places.
- Line 317: a value network wasn't introduced in the previous context.
- Line 373: a brief description of SimuEM method would help.
- Line 377: it's unclear how "a binary search over the domain of $\mathcal{K}$" Is conducted.

### Questions
I have listed in the "Weaknesses" section some major questions re. clarifications of algorithmic details and comparisons with prior works on specific aspects. Below are some additional questions.

1. Why did the authors choose to consider ADP and RDP? How do different versions of DP impact your methods? Is it through the DP accountant used in training the model + the certification results? -- this needs clarification. There exist other advanced and tighter DP accountants, e.g., Gopi et al., 2021, Doroshenko et al., 2022. Can the authors discuss the applicability of these techniques in your work, and whether this will likely strengthen your results? 
2. From the experimental results, it seems that RDP almost dominates ADP everywhere. Can the authors provide some insights re. why this happens? 

**References**

Gopi, Sivakanth, Yin Tat Lee, and Lukas Wutschitz. "Numerical composition of differential privacy." *Advances in Neural Information Processing Systems* 34 (2021): 11631-11642.

Doroshenko, Vadym, et al. "Connect the Dots: Tighter Discrete Approximations of Privacy Loss Distributions." Proceedings on Privacy Enhancing Technologies (2022).

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a new certified defense technique against poisoning attacks in offline reinforcement learning using differential privacy. The goal of their defense is to certifiably minimize the trained agent's drop in episodic return (policy level robustness), and minimize the probability that one of the agent's actions are changed (action level robustness) when trained on a poisoned dataset $\tilde{\mathcal{D}}$. They further want to extend these certifications to both attackers that modify whole trajectories (trajectory-level poisoning) or individual transitions (transition-level poisoning). They model the strength of the attacker as the total number of alterations they make to the dataset.

Their method, in line with common practice in differential privacy, adds additional random noise to the training of an RL agent given the (potentially poisoned) training data $\tilde{\mathcal{D}}$. They show how their particular construction, given established properties of differential privacy, is able to put a lower bound on the agent's drop in episodic return and an upper bound on how many of the agent's actions are changed. The paper's main contributions are theoretical.

They evaluate their defense against trajectory and transition level attackers of varying strength given discrete and continuous offline datasets. They compare their results against the prior COPA defense, displaying increased episodic return and a larger certified radius.

### Strengths
* Defense is well motivated within the scope of prior work.
* Theoretical results are strong and proofs provided in the appendix are convincing.
* The proposed defense improves over prior defenses.
* The writing and presentation is organized and easy to follow.

### Weaknesses
My main complaint with this paper is the lack of clarity in the experimental results section. The authors evaluate each defense against different thresholds of $\bar{r}$, but it's very unclear to me what this means. Under the authors definitions of $\mathcal{B}$ the value of $\bar{r}$ is the number of "changes" to trajectories or transitions. Given this definition I could have $\bar{r} = |\mathcal{D}|$ by simply shaping the rewards with some function $F(s,a,s') = \gamma \Phi(s') - \Phi(s)$, which does not alter the optimal policy in an MDP [1]. This would be a "full strength" attack, which manipulates every timestep in the dataset, but it would not actually impact the optimal policy. On the other hand I could invert each reward as $\hat{r}_t = -r_t$, which would have the same "strength" $\bar{r} = |\mathcal{D}|$, but would be a much more impactful attack.

In short, I think the authors need to be more clear about how they're evaluating their defense so readers can have a better understanding of their empirical results. It's also possible that I'm missing some details here, but it seems that $\bar{r}$ is not well defined. I request that the authors:

* Provide a precise definition of how $\bar{r}$ is measured in practice for both trajectory and transition-level poisoning.
* Clarify whether they are actually poisoning the datasets or just evaluating the certifications at different theoretical poisoning levels.
* If actual poisoning is performed, describe the specific attack method used.

I also think the authors should have some discussion on why they do not explicitly consider backdoor attacks. One paper they cite frequently is [2], which is one of the first backdoor poisoning attacks in deep reinforcement learning. The goal of backdoor attacks is to maintain benign episodic return of the agent while inducing adversarial behavior in the agent upon observing a predetermined trigger [3, 4]. I'm not certain, but I believe stronger backdoor attacks like [3] may break your action level robustness without a very large $\sigma$. Therefore, I think motivating why the authors don't explicitly consider backdoor attacks is important (perhaps leave such analysis to a future work?). In summary, I ask that the authors:

* Explicitly discuss why backdoor attacks are not considered in the current work.
* Address whether their certification framework could potentially be extended to cover backdoor attacks, or explain why it may not be applicable.
* Consider adding a discussion on the limitations of their current approach with respect to more sophisticated attacks like backdoors, potentially as part of the future work section.

### Questions
* How do you measure attack performance with respect to $\bar{r}$ do you directly poison datasets with some attack and evaluate the relevant metrics or is it something else? If you are performing an attack, which attack are you using or how is it formulated?
* How do you think your defense would work in the presence of backdoor attacks? Do these attacks fit within your certifications?

### Soundness
3

### Presentation
3

### Contribution
3
