# On Minimizing Adversarial Counterfactual Error in Adversarial Reinforcement Learning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Deep Reinforcement Learning (DRL) policies are critically vulnerable to adversarial noise in observations, posing severe risks in safety-critical scenarios. For example, a self-driving car receiving manipulated sensory inputs about traffic signs could lead to catastrophic outcomes. Existing strategies to fortify RL algorithms against such adversarial perturbations generally fall into two categories: (a) using regularization methods that enhance robustness by incorporating adversarial loss terms into the value objectives, and (b) adopting "maximin" principles, which focus on maximizing the minimum value to ensure robustness. While regularization methods reduce the likelihood of successful attacks, their effectiveness drops significantly if an attack does succeed. On the other hand, maximin objectives, although robust, tend to be overly conservative. To address this challenge, we introduce a novel objective called Adversarial Counterfactual Error (ACoE), which naturally balances optimizing value and robustness against adversarial attacks. To optimize ACoE in a scalable manner in model-free settings, we propose a theoretically justified surrogate objective known as Cumulative-ACoE (C-ACoE). The core idea of optimizing C-ACoE is utilizing the belief about the underlying true state given the adversarially perturbed observation. Our empirical evaluations demonstrate that our method outperforms current state-of-the-art approaches for addressing adversarial RL problems across all established benchmarks (MuJoCo, Atari, and Highway) used in the literature.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduced a new perspective into adversarial RL problems by viewing the state-perturbing adversary as inducing a POMDP. The authors then proposed the concept of Adversarial Counterfactual Error (ACoE) and developed a surrogate of it for applicability in general RL problems. Extensive experiments in various environments demonstrate the effectiveness of the proposed ACoE objective and the practical algorithms.

### Strengths
1. The newly introduced objective ACoE provides a theoretically grounded approach to handling the POMDP induced by state-perturbing adversaries. This is novel and a valuable contribution to the adversarial RL literature. 
2. The evaluation is comprehensive. The authors experimented with various RL environments and considered different types of attacks, which consistently demonstrated the effectiveness of the proposed approach.
3. The paper is overall well-written and pleasant to read. The authors have done a great job setting up the background, comparing with the literature, motivating the new objective and algorithm on top of that.

### Weaknesses
I overall enjoy reading the paper and only have a few minor questions; see "Questions" section.



### Questions
1. The authors "restrict solutions to the set of policies that depend just on the current observation" (line 302). Can the authors discuss the trade-off here, i.e., how much benefit can there be if we consider using policies that can depend on the history, and what's the downside of the increased complexity (e.g. computational cost).
2. It's encouraging to see that the proposed approach performs well even against long-horizon adversaries, given that the design of the brief construction algorithms only involve the consideration for the myopic adversary. It would be interesting to see whether A3C can be hacked and to which extent--suppose we have a long-horizon adversary who's aware of the A3C heuristic (an adaptive attacker), how robust is the proposed algorithm in this case.
3. The authors focused on the state-perturbing adversary in this work. Can the authors discuss the extension of the framework to other types of RL adversary?

Minor

- Line 362: should be $\pi(s_1)$ instead of $\pi(s_1')$.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel method for adversarial reinforcement learning which balances between natural policy value and adversarial robustness. By revisiting the relation between policy value without perturbation and with perturbation, the paper proposes a new objective that minimizes the controllable difference of the return between attacked policy and unattacked policy. Based on the theoretical insights, the paper introduces a model-free adversarial training method with two algorithms, A2B and A3B, to estimate the belief states. Experiments on variaous environments and attack methods show that the proposed methods are effective, achieveing better balance between clean reward and attacked rewards.

### Strengths
- This paper proposes an interesting idea of balancing policy unperturbed value and perturbed value through the optimization of Adversarial Counterfactual Error. Different from prior work which considers the worst-case performance, the proposed method estimates the attacked value via belief state estimation. 
- The paper is in general well-written and easy to follow. 
- The paper presents experiments in several different scenarios and shows better performance than SOTA baselines. The method can be adapted for both PPO and DQN, both of which achieve good empirical results.

### Weaknesses
Both A2B and A3B rely on some knowledge of the attacker, such as attack radius and attack perference. Can the authors provide more justification on whether this is a realistic assumption? For the experiments, how does the attack radius and surrogate attack set for different attack scenarios? If the surrogate attack radius or attack preference is very different from the actual attack, how will the attack performance drop compared to baselines which consider the worse-case attack?

### Questions
See my questions in the weakness section.

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
3

### Summary
This paper focus on the adversarial defense in the context of Deep Reinforcement Learning (DRL). Specifically, this paper introduces Adversarial Counterfactual Error (ACoE) defined based on the beliefs (uncertainty) about the underlying true state of the target model, thus balancing value optimization for improved robustness. In addition to extensive experimental evaluations, the authors also provide systematic analyses in the theoretical part to justify the effectiveness and generalization ability of the proposed method.

### Strengths
1. The proposed method is novel with a clear motivation. It's also scalable for model-free environments.
2. Extensive experiments and analyses are conducted to demonstrate the efficacy of the proposed method.
3. Theoretical analyses are detailed and solid.

### Weaknesses
1. This paper has limited (experimental) justifications for surrogate belief construction choices. Comparisons with alternative constructions would be better to support the motivation. Specifically, the paper introduces A2B and A3B, but lacks a thorough exploration of why these specific constructions were chosen over other plausible alternatives. The absence of a comparative analysis against other potential belief formulations weakens the justification for the proposed approach.
2. The method's adaptability to diverse or higher-dimensional continuous state spaces is underexplored. Instead of theoretical analyses, further explanations or experimental results would be preferred. While the authors claim the method is applicable to continuous spaces, the experimental validation primarily focuses on relatively low-dimensional environments. The paper would benefit from experiments in more complex, high-dimensional continuous control tasks to demonstrate the practical scalability of the approach. The current theoretical analysis, while detailed, does not fully address the practical challenges of applying the method to such spaces.
3. I feel the performance of the proposed C-ACoE would be likely sensitive to hyper- parameters. Further analyses are required. The paper lacks a comprehensive sensitivity analysis of the key hyperparameters, particularly the robustness-weight factor \lambda and the neighborhood size. The absence of such an analysis raises concerns about the practical robustness of the method and its sensitivity to parameter tuning. The paper needs to explore the impact of different parameter settings on the overall performance.

### Questions
1. Is it possible to provide an analysis of the trade-off between natural performance and adversarial robustness?
2. Is it possible to extend the proposed method to high-dimensional continuous state spaces?
3. The authors can try to run sensitivity analyses on key hyperparameters, such as the
robustness-weight factor \lambda and neighbourhood size

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces the Adversarial Counterfactual Error (ACoE) as a metric for quantifying robustness in adversarial deep reinforcement learning (DRL). Current methods for adversarial robustness often struggle to balance performance and robustness, especially in cases of partial observability due to adversarial noise. The authors hypothesise that explicitly accounting for partial observability in adversarial settings can lead to more balanced results. To address this, they propose Cumulative-ACoE (C-ACoE), a scalable surrogate objective designed to improve model-free DRL methods. C-ACoE allows for simultaneous robustness and performance improvements achieved through adaptations of popular DRL algorithms such as PPO and DQN. Their experimental results on various benchmarks (MuJoCo, Atari, and Highway) show that C-ACoE methods outperform current state-of-the-art approaches in adversarial environments.

### Strengths
The paper proposes an original approach to managing adversarial robustness in DRL by framing it as a partial observability problem. This novel perspective on adversarially-induced partial observability, operationalized by ACoE and its scalable form C-ACoE, is a significant theoretical contribution. With ACoE as the objective, the methods A2B and A3B show superior performance compared to baselines.

### Weaknesses
 - The Abstract is overly long.
- Missing $)$ in Eq. 2.
- It is unclear to me how C-ACoE $delta$-network is learned, and how it's aligned with the theory especially Eq. (2). Specifically, in the paper the authors claim that $delta$ is no longer dependent on $b$, then what's the use of $b(s)$ in A2B and A3B? And if $b$ is not needed then in Eq. (2) RHS the second term still has $b$, then how do you learn C-ACoE correctly? The authors should put more details about C-ACoE in algorithm 1, and omit the common knowledge like GAE and PPO-clipped.

### Questions
1. Do we care about unperturbed performance since basically all real-world applications have states being perturbed. Can you list any applications?
2. Both A2B and A3B require KL divergence between policies, which should be computational costly. Did the authors address this anywhere?
3. Can you provide any intuition about algorithmically, why this method can have such good empirical performance?

### Soundness
2

### Presentation
2

### Contribution
3
