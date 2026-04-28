# Fewer is More: Trojan Attacks on Parameter-Efficient Fine-Tuning

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Parameter-efficient fine-tuning (PEFT) enables efficient adaptation of pre-trained language models (PLMs) to specific tasks. By tuning only a minimal set of (extra) parameters, PEFT achieves performance comparable to full fine-tuning. However, despite its prevalent use, the security implications of PEFT remain largely unexplored. In this paper, we conduct a pilot study revealing that PEFT exhibits unique vulnerability to trojan attacks. Specifically, we present PETA, a novel attack that accounts for downstream adaptation through bilevel optimization: the upper-level objective embeds the backdoor into a PLM while the lower-level objective simulates PEFT to retain the PLM's task-specific performance. With extensive evaluation across a variety of downstream tasks and trigger designs, we demonstrate PETA's effectiveness in terms of both attack success rate and unaffected clean accuracy, even after the victim user performs PEFT over the backdoored PLM using untainted data. Moreover, we empirically provide possible explanations for PETA's efficacy: the bilevel optimization inherently 'orthogonalizes' the backdoor and PEFT modules, thereby retaining the backdoor throughout PEFT. Based on this insight, we explore a simple defense that omits PEFT in selected layers of the backdoored PLM and unfreezes a subset of these layers' parameters, which is shown to effectively neutralize PETA.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work reveals that Parameter-efficient fine-tuning (PEFT) exhibits unique vulnerability to trojan attacks. A novel attack called PETA was presented that accounts for downstream adaptation through bilevel optimization: the upper-level objective embeds the backdoor into a PLM while the lower-level objective simulates PEFT to retain the PLM’s task-specific performance. Extensive evaluation across a variety of downstream tasks and trigger designs demonstrate PETA’s effectiveness in terms of both attack success rate and unaffected clean accuracy, even after the victim user performs PEFT over the backdoored PLM using untainted data.

### Strengths
1. The proposed trojan attack under Parameter-efficient fine-tuning (PEFT) setting is interesting and practical.
2. the experimental results seems promising.
3. The paper is generally well motivated and written.

### Weaknesses
1. How complex is the bilevel optimization?
2. Baselines are all old ones back to 2-5 years before.
3. The defense part is bit weak, just considered a simple one.
4. Some highly relevant works on backdoors are missing:
Fine-mixing: Mitigating Backdoors in Fine-tuned Language Models
Backdoor attacks on self-supervised learning
ASSET: Robust Backdoor Data Detection Across a Multiplicity of Deep Learning Paradigms
Reconstructive Neuron Pruning for Backdoor Defense
Anti-Backdoor Learning: Training Clean Models on Poisoned Data
Neural Attention Distillation: Erasing Backdoor Triggers from Deep Neural Networks

### Questions
see the Weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on trojan/backdoor attacks in the parameter efficient fine-tuning (PEFT) setting, which is an important research topic. The authors propose PETA, a novel attack to inject the backdoor into the PLM using bilevel optimization. Extensive experiments demonstrate the effectiveness of PETA. The authors also discuss potential countermeasures.

### Strengths
- important topic
- well-written paper
- effective attacks and countermeasures

### Weaknesses
 - technical novelty is limited
- unclear attack description
- more evaluations are needed

### Questions
- My main concern is that the proposed attack leverages existing backdoor attack methodology in the scenario of PEFT, making the technical novelty limited. Please correct me if I am wrong. In both Eq. 2 and Eq. 3, the whole model's parameters seem to be updated (including $\theta$ and $\delta$), which is the same as the backdoor attack in the fine-tuning stage. After the attack, $\delta$ will be discard and a new $\delta$ will be trained (with $\theta$ being fixed) by the victim user to perform the downstream task. I appreciate it if the authors could better clarify the advantage of the proposed attack compared to previous attacks and discuss the attack process more clearly.

- Regarding the evaluation, it seems that BadNet can also achieve both high ACC and high LFR. Would it be the case if we discard the classifier $\delta$ backdoored by BadNet and train a new $\delta$?  

- During the backdoor process, the dataset is from the same distribution as the testing data, which is a relatively strong assumption. I would suggest the authors also evaluate the attack performance when the downstream dataset is from a different distribution than the attack dataset.

- I like the authors' idea regarding the defense. As shown in Fig. 3, the LFR can be largely reduced if we could select the optimal layer. However, it would be hard to select the optimal one. Previous work[a] also suggests that fine-tuning the whole model could be an effective defense. Would it be possible to make a trade-off by fine-tuning the last few layers?

[a] https://arxiv.org/abs/2212.09067

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work concerns trojan attack in PLM and present PETA. It contains two stages: (1) bilevel optimization, which inserts the backdoor into a general-purpose pre-trained language model and is conducted by attacker and (2) parameter-efficient fine-tuning on a clean dataset, which is conducted by user.

### Strengths
1. This work is the first to study backdoor attack for PEFT.

2. The experiments are sufficient and convincing.

3. This work also investigates how to solve the backdoor attack from PETA.

### Weaknesses
1. The most important is that the motivation of the studied problem is unclear. I doubt if there are any scenarios in reality where exists corrupted PLM trained with so much (25%) poisoned data and it needs PEFT. I suggest the authors focus on discussing the motivation in introduction.

2. I suggest the author add explanations of poisoned data to improve readability.

### Questions
1. The learning rate of DP is 10x of other baselines from Appendix. Besides, more epochs are used. Is there any explanation?

2. I wonder how would the poisoned rate affects the results?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explore the secure risk of parameter-efficient fine-tuning (PEFT) of pre-trained language models (PLMs) toward trojan attacks. Specifically, the authors present a novel attack PETA that accounts for downstream adaptation through bilevel optimization: the upper-level objective embeds the backdoor into a PLM while the lower-level objective simulates PEFT to retain the PLM’s task-specific performance. Bedise, the authors also propose a fine-tuning method to defense the PETA attack. Emperically, the authors show the effectiveness of the proposed attack method and the defense method.

### Strengths
- Exploring the risk of PEFT toward trojan attacks is valuable.
- The authors propose the paired attack-defense method to promote the exploration of PEFT toward backdoored security.
- The authors run numerous experiments across a variety of downstream tasks and trigger designs to empirically verify the effectiveness of the proposed attack method.

### Weaknesses
My major concern is that the proposed method in this paper needs strong assumptions:
- The authors assume that the attacker is equipped with knowledge about (i) the downstream task and (ii) the PEFT method used by the user. Based on these strong assumptions, the authors design the attack method through bilevel optimization, where the upper-level objective embeds the backdoor into a PLM and the lower-level objective simulates PEFT to retain the PLM's task-specific performance. The feasibility of the bilevel-optimization-based attack is heavily targeted and relies on the assumed downstream task and the PEFT method. 
- However, in practice, the attackers are hard to know (or limit) both the downstream task and the PEFT method used by the users/defenders in advance. Thus, the assumption is too strong and impractical. If the users/defenders choose a novel PEFT method or change the downstream task, I believe the proposed attack method is hard to work.
- The authors could run experiments to explore the effectiveness of the proposed method toward unseen downstream task/PEFT methods. I'm interested in the transferability of the proposed trojan attack method.

### Questions
Please see the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
