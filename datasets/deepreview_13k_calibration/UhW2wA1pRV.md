# Robust Deep Reinforcement Learning against ADVERSARIAL BEHAVIOR MANIPULATION

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
This study investigates the robustness of deep reinforcement learning agents against targeted attacks that aim to manipulate the victim's behavior through adversarial interventions in state observations. While several methods for such targeted manipulation attacks have been proposed, they all require white-box access to the victim's policy, and some rely on environment-specific heuristics. Furthermore, no defense method has been proposed to counter these attacks. To address this, we propose a novel targeted attack method for manipulating the victim, which does not depend on environmental heuristics and applies in black-box and no-box settings. Additionally, we introduce a defense strategy against these attacks. Our theoretical analysis proves that the sensitivity of a policy's action output to state changes affects the defense performance and that the earlier in the trajectory, the greater the effect. Based on this insight, we introduce a time-discounted regularization as a countermeasure for such behavior targeted attacks, which helps to improve robustness against attacks while maintaining task performance in the absence of attacks. Empirical evaluations demonstrate that our proposed attack method outperforms baseline attack methods. Furthermore, our defense strategy shows superior robustness against existing defense methods designed for untargeted attacks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the problem of deep RL under poisoning attack. It considers an adversary to manipulate the behavior of a policy used by the learning agent during testing time. It develops an efficient attack and defense in this setting and provides the theoretical insight behind its methods. The performance of its methods is verified with abundant experiments, and the experiment results seem promising.

### Strengths
1. This paper studies an interesting and important problem: adversarial attacks in DRL and their defense

2. This paper provides a complete story that gives both an attack and a defense. In addition, for the attack part, they are the first black-box attack in their targeted testing time attack setting.

3. The selection of the baselines is reasonable, and the experiment results look very strong. Both the attack and defense perform significantly better than their baselines.

4. Considering the promising results, their methods seem simple and easy to implement, which makes them more practical.

### Weaknesses
1. The explanation of the motivation is not enough. This work only explains an example of autonomous driving. It should also explain why the attack is realistic: how this attack happens in the real world and what bad things will happen under the attack. It is even better to find evidence showing that behavior manipulation attacks already threaten our world.

2. An explanation of the challenges is missing. The problem studied in this problem should not be easy, but it is beneficial to explicitly clarify exactly why the problem is hard to solve and what the challenges are.

3. This work's theoretical analysis is weak in that it doesn't provide any guarantees on their defense algorithm. Is there a chance that some guarantees can be provided under certain assumptions?

4. It is difficult to digest the result that the PGD attack performs almost identically to the random attack. I want to see more details on how the PGD attack is implemented and how much effort has been spent on tuning it. This baseline ought to be strong, but now it seems trivial. I think a more detailed investigation is necessary rather than a simple explanation.

5. It took me a while to find that the attack works during the testing time (no training happens during the attack). I think this needs to be clarified. It is also beneficial to discuss the related works on the training time DRL attacks to make the related work section complete, such as [1] and [2].

### Questions
See Weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces BIA (Behavior Imitation Attack), a novel attack method that forces a victim RL agent to imitate a specified target policy without requiring environment-specific heuristics or full access to the victim's policy. Rather than attempting to match actions at each individual step, BIA aims to achieve overall behavioral alignment, making it effective even when perfect action matching is impossible due to limited adversarial intervention capabilities. Additionally, the paper presents TDRT (Time-Discounted Regularization Training), the first defense framework specifically designed for behavior-targeted attacks, which applies stronger regularization in early trajectory stages and demonstrates improved robustness-performance trade-offs compared to existing untargeted defense methods.

### Strengths
1. Shifts from action matching to behavioral imitation, enabling effective attacks under limited intervention.
2. Identifies the critical role of early-trajectory stability and action-state sensitivity in defense against behavior targeted attack
3. Provides theoretical analysis in both attack and defense methods.

### Weaknesses
1. The nearly identical performance between BIA-ILfD and BIA-ILfO contradicts the established understanding that ILfO is generally more challenging than ILfD. This observation in very easy MetaWorld tasks significantly weakens the paper's empirical validation. The lack of a clear performance gap raises concerns about the method's ability to capture the nuances of different imitation learning paradigms, particularly in more complex environments where the distinction between state-only and state-action observations becomes crucial.
2. The paper fails to analyze how the quantity and quality of demonstrations affect attack performance. The use of 20 demonstrations for these MetaWorld tasks seems excessive. The absence of a systematic study on the impact of demonstration quality and quantity limits the practical insights that can be drawn from the experiments. It is unclear whether the attack's effectiveness is robust across varying demonstration sets.
3. No discussion on whether expert-level demonstrations are necessary. The assumption of having access to expert demonstrations may severely limit practical applicability. The requirement for expert demonstrations is a significant constraint that needs to be thoroughly addressed, as it may not be feasible in many real-world scenarios where obtaining such demonstrations is difficult or costly.
4. Lack of limitation and efficiency analysis for the proposed attack and defences. The paper does not provide a thorough analysis of the computational cost and scalability of the proposed attack and defense methods. This is a critical omission, as it is important to understand the practical limitations of the proposed techniques.
5. Overlooks recent related work [1] about RL defences

### Questions
1. The nearly identical performance between BIA-ILfD and BIA-ILfO contradicts the established understanding that ILfO is generally more challenging than ILfD. This observation in very easy MetaWorld tasks significantly weakens the paper's empirical validation.
2. The paper fails to analyze how the quantity and quality of demonstrations affect attack performance. The use of 20 demonstrations for these MetaWorld tasks seems excessive.
3. No discussion on whether expert-level demonstrations are necessary. The assumption of having access to expert demonstrations may severely limit practical applicability.
4. Lack of limitation and efficiency analysis for the proposed attack and defences
5. Overlooks recent related work [1] about RL defences

[1] Game-Theoretic Robust Reinforcement Learning Handles Temporally-Coupled Perturbations, Liang et al, ICLR 2024

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper provides formalizations for a previously uncovered adversarial RL scenario in which an adversary is directing the victim toward some specific target behavior. Under this formulation, the paper proposes a robust policy regularizer based on the F-divergence between the policy and the composite policy+adversary. Empirical results demonstrate the effectiveness of the attacks and defenses provided.

### Strengths
The attention to behavior-manipulating attacks is very novel. Although the concept has been mentioned before, this work is the first to provide formalizations and a solution. 

The problem setup and theoretical contributions are clear.

The attention to both adversarial and robust angles of the problem makes a thorough contribution.

### Weaknesses
A few baselines are missing which should be compared to. For defenses, there are methods [1] and [2]  and [3] that should be considered versus TDRT. For attacks, the PA-AD component of [3] should be compared to BIA-ILfD/O.

The empirical setup is unclear, as is the presentation of the results in Table 1. The information in Table 1 is confusing, for instance, the attack rewards appear to be higher-is-better (assuming boldface = best), but the boldface scores are lower than the target reward. This is more confusing when compared to Table 2, which is clearly lower-is-better for the attacks.

The description of experimental tasks is lacking--from section 7.1, it is unclear how rewards are distributed for each goal, and how they correlate to agent performance.



### Questions
1) How do the opposing goals in the tasks distribute rewards? Is one of the states (i.e. window-open) a positive reward, and the opposite negative? If that is the case, this seems identical to classic reward-min attacks, unless a formalization can be provided to differentiate the two scenarios.

2) Related to question 1, is there a way to formalize the selection process for $\pi_{tgt}$? I understand the novelty of the attack type in isolation, however, the only well-defined $\pi_{tgt}$ would be min-reward, which is the existing attack paradigm.

3) In equations 8 and 11, my understanding is that the optimization only depends on $\nu$ unless D interacts with $\pi$ in some way. Since $\pi$ is a fixed policy, why can't equation 8 be solved directly? The problem seems easier than if $\pi$ was dynamic.

4) The authors mention that there are no defense methods currently for behavior-targeted attacks, so untargeted defense methods are used. What considerations are made to adapt these methods to this setting? For instance, is the target reward used as the learning objective for PA-ATLA, or a different notion of reward?

Minor comments:\
-$\hat{p}$ is defined in eq 10 but unused in eq 9.\
-Some misspellings throughout, like the "Notaion" header in Section 3.

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper first proposes a method to mount a targeted black-box attack to adversarially manipulate a victim RL policy towards a target policy. Unlike previous works, the proposed method, leverages imitation learning and is extendable to the no-box setting and does not require environment heuristics or the creation of a target policy, but only the trajectories of the target policy is required. Additionally, the authors also developed a defense framework that is specific towards behavioral manipulation by introducing a time-discounted regularization to induce robustness of the victim policy towards adversarial manipulation while maintaining nominal performance. Experiments were shown on MuJoCo and MetaWorld environments.

### Strengths
1. Overall, the paper is relatively well written, clear and easy to follow. 

2. The problem of adversarial manipulation towards a targeted behavior and the corresponding need to defend against such attacks are not necessarily new, but I believe the way the authors formulate the adversarial problem and derive corresponding algorithm and the formulation of the time-discounted regularization is original, to the best of my knowledge. 

3. In terms of significance, I believe that this area of research (adversarial manipulation and defense for RL) is a niche (more on that below) but important area of study. More importantly, I believe any advancement in this area could also lead to advancement in other areas of RL robustness.

### Weaknesses
1. The main motivation for behavior manipulation and claim that it is different from reward minimization from adversarial point of view is a little challenging to imagine in the real world. Specifically, while the authors argue that an adversary might want to manipulate behavior without significantly reducing reward, it's unclear how this differs practically from a reward-minimization attack in most realistic scenarios. In many real-world systems, behaviors are often implicitly or explicitly tied to reward structures, making a clean separation difficult to conceptualize. For example, in a navigation task, a manipulated route that doesn't significantly reduce reward (i.e., still reaches the destination) would likely still incur some cost, which would be reflected in the reward, making it a form of reward minimization. 

2. Similarly, I'm not convinced that the idea of time-discounted regularization is a generalizable method of defense. The effectiveness of this regularization seems highly dependent on the specific task and reward structure, particularly if the critical actions for the task are not concentrated at the beginning of the episode. If crucial actions occur later in the episode, the time-discounted regularization might not provide sufficient protection against adversarial manipulation. Furthermore, the method's applicability to non-episodic or infinite-horizon problems is unclear, as the concept of time-discounting might not translate directly to such scenarios.

3. The results shown in the main paper are convincing but somewhat limited and the results in MuJoCo shown in the Appendix are somewhat mixed, which further weakens the paper's claims. The lack of consistent performance across different environments and tasks raises concerns about the robustness and generalizability of the proposed method. The mixed results in MuJoCo, in particular, suggest that the method's effectiveness might be highly sensitive to the specific characteristics of the environment and task, which limits its practical applicability.

### Questions
1. One of the main differentiation of this paper from existing works that the authors claimed are that behavioral manipulation is different from naive adversarial attacks that seeks to minimize rewards. While I understand this conceptually, I find it hard to imagine a situation in a real world where adversarial behavior manipulation does not somehow lead to the same scenario as reward minimization. Could the authors provide some concrete examples?

2. Related to the question above, in the contributions, the authors wrote: "TDRT is robust against attacks that do not significantly reduce rewards but greatly alter behavior". Does this assume that there are environments where rewards are not strongly correlated with sub-optimal behavior? In other words, is there an assumption that the reward function still returns a relatively high reward when the policy is suboptimal?

3. On the topic of time-discounted regularization, could the authors comment on what happens in scenarios where the RL is non-episodic or is facing an infinite horizon problem? I can understand if the authors claim that this method works for situations where the initial time steps are critical, but there are also many problems where the actions and state are equally critical in the later stages of the episode.

4. For the attack algorithm, the authors mentioned that a target policy is not needed, only access to the trajectory of the target policy is needed. In such cases when target policy is not available, is there a specific amount of trajectory that is needed for the attack to be mounted successfully?

5. In Equation 12. the formulation suggest that the loss function minimizes the victim's behavior even under the worse-case adversarial policy. How is the worse-case adversarial policy defined here?  Isn't the premise of the attack a policy that doesn't necessarily minimizes the reward but rather pushes the victim towards a target behavior?

6. In the results section for Defense, could the authors explain why the clean rewards represent rewards when the victim is trained to achieve the adversarial task without attacks? Shouldn't the clean rewards represent the victim's performance for the nominal task without any attack and wouldn't a comparison showing how the naive and adversarially trained victim policy performs in the a normal and attacks setting makes more sense? Please let me know if I misunderstand this section.

7. As mentioned in the section above, additional results on more task in the MetaWorld / MuJoCo showing the effectiveness of the proposed attack and defense method would definitely make the results more convincing.

### Soundness
3

### Presentation
3

### Contribution
3
