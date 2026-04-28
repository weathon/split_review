# Bad-PFL: Exploiting Backdoor Attacks against Personalized Federated Learning

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Data heterogeneity and backdoor attacks rank among the most significant challenges facing federated learning (FL). For data heterogeneity, personalized federated learning (PFL) enables each client to maintain a private personalized model to cater to client-specific knowledge. Meanwhile, vanilla FL has proven vulnerable to backdoor attacks. However, recent advancements in PFL community have demonstrated a potential immunity against such attacks. This paper explores this intersection further, revealing that existing federated backdoor attacks fail in PFL because backdoors about manually designed triggers struggle to survive in personalized models. To tackle this, we degisn Bad-PFL, which employs features from natural data as our trigger. As long as the model is trained on natural data, it inevitably embeds the backdoor associated with our trigger, ensuring its longevity in personalized models. Moreover, our trigger undergoes mutual reinforcement training with the model, further solidifying the backdoor's durability and enhancing attack effectiveness. The large-scale experiments across three benchmark datasets demonstrate the superior performance of our attack against various PFL methods, even when equipped with state-of-the-art defense mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors develop Bad-PFL, a new backdoor attack that leverages natural features from the target label as a trigger, enabling backdoor persistence across both global and personalized models. It uses a dual-component trigger, combining natural target features and disruptive noise to deceive the model without being easily detectable. Bad-PFL demonstrates high attack success rates even when state-of-the-art defenses are applied.

### Strengths
It introduces Bad-PFL, a unique attack using natural features as triggers in PFL, and a novel dual-trigger design combining natural features and disruptive noise for stealth and effectiveness. Experiments are thorough, covering multiple datasets and comparing Bad-PFL to six top backdoor attacks, showing its high success rate even with strong defenses. This work highlights vulnerabilities in PFL previously thought resistant to backdoors, encouraging the development of specialized defenses and impacting fields that rely on PFL.

### Weaknesses
1) Some newer or adaptive defenses, such as gradient masking or input filtering, are not covered, leaving questions about Bad-PFL's effectiveness against more dynamic defenses.

2) While Bad-PFL claims high stealthiness, there is limited quantitative analysis on how detectable the trigger is by modern anomaly or intrusion detection systems. Specifically, the evaluation lacks a rigorous analysis of the trigger's detectability using methods that analyze the model's internal representations or activation patterns, which are commonly used in backdoor detection.

3) The experiments are largely conducted on ResNet models, leaving questions about the attack's adaptability to other architectures commonly used in federated learning, such as transformer-based models. The evaluation should include a wider range of architectures to demonstrate the generalizability of the attack.

### Questions
1) Have you tested the detectability of the Bad-PFL trigger with current anomaly or backdoor detection methods? If so, what results did you observe?

2) How does the attack’s success vary with different levels of data heterogeneity among clients? Could more heterogeneous data distributions reduce Bad-PFL’s attack success rate or persistence?

3) How does Bad-PFL perform across different model architectures, such as transformer-based models?

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
In this paper, the authors propose a novel PFL backdoor method that leverages natural features from the data as triggers, rather than manually designed triggers used in previous attacks. Specifically, the proposed method adopt a generator to generate the features that make samples appear similar to the target category and introduces disruptive noise to eliminate features associated with the ground-truth labels.

### Strengths
1. The proposed method is novel in that the trigger is designed to be sample-specific, which is a significant difference with the previous works

2. The paper is well organized and is easy to follow

3. The authors provide a thorough discussion about the challenges of backdoor attack under the PFL setting.

4. The authors conduct the experiment on three benchmark datasets. Besides, the effectiveness of the propsoed backdoor methods are also evaluated under the state-of-the-art defense mechanisms

### Weaknesses
1. In this paper, the authors lack the in-depth discussion about why the propose method can overcome the challenges metioned in section 2.2.
	
	a. It is suggested that the authors give more intuitive or theoretical discussion about why it works. 

	b. Specifically, the authors may give more experimental analysis about the inherent mechanism about the proposed method. For example, the authors can visualize the representation of different classes under clean and backdoored data.  


2. Some related attacks are missing, such as: 
	a. Lurking in the shadows: Unveiling Stealthy Backdoor Attacks against Personalized Federated Learning (https://arxiv.org/html/2406.06207v1)


3. Missing defense method. 
	a. Simple-Tuning: Clients reinitialize their classifiers and then retrain them using their local clean datasets while keeping the feature encoder fixed. (https://dl.acm.org/doi/10.1145/3580305.3599898)

### Questions
See weekness 1, 2, 3

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper investigates backdoor attacks in FPL and introduces a new method to conduct attacks with PFL, named Bad-PFL. This method trains a sample-specific generator to generate a mask for input. Another mask is learned for the main task; the final poisoned sample combines the original one and these two masks. Experiments show that this method can work with different settings and bypass existing defenses.

### Strengths
- It provides an interesting insight into why existing backdoor attacks are ineffective in PFL, offering a foundation for advancing attack strategies.
- The proposed Bad-PFL approach achieves high stealth and persistence in personalized models under various settings.

### Weaknesses
1. This method shows degradation when the data is highly heterogeneous, which is more practical in cases in FPL.
2. The use of a generator for mask optimization is not novel. Previous works such as IBA [1] and Perdoor [2] use the same method. However, this paper lacks comparison and discussion with these papers.
3. The use of two masks is not totally convincing and lacks theoretical analysis to support this mechanism. What is exactly the role of each mask in the overall method, and what is the relationship between these two masks? The paper does not fully justify why two separate masks are essential rather than using a single mask that can adaptively balance target and non-target features. How can we ensure that the two masks—the target feature enhancement mask ($\delta$) and the disruptive noise mask ($\xi$)—do not interfere with each other, either by collapsing into a single effect or by unintentionally complementing each other? Table 4 is not enough to support this point. A more detailed analysis, potentially visualizing the interplay between $\delta$ and $\xi$ or providing quantitative metrics on their interaction, would strengthen the justification.
4. It is unclear how Bad-PFL can address the limitations mentioned in Section 2.2. Though the authors mentioned using features of the target label as the trigger for a more effective backdoor attack, the benign mask $\eta$ is learned as a noise mask instead of the true features in the images. The paper should provide a more explicit connection between the proposed method and the limitations outlined, demonstrating how the use of a learned noise mask overcomes the challenges of existing methods in the context of personalized federated learning.

### Questions
1. In the threat model (Line 236-237), the attack can be colluded or non-colluded but the paper did not explicitly discuss or show this attack can work with both cases.
2. Can the authors explain more detail about the phenomenon mentioned in L263-264, and why the model should focus on the backdoor mask $\delta$?
3. Could the authors discuss the computational overhead of this method? Will it raise suspicion when it takes too long for the malicious to complete a training iteration?
4. In Line 294, what is the intuition of setting \eta by the reversed sign of the input?
Why does it ensure to return of an approximate solution?
5. Will another factor such as the number of clients affect the performance of this method, since it will affect the global model in each training round?
6. Some close related papers are missing such as [3][4]. The authors can discuss the key difference in terms of the methodology of this work.
7. Can the authors elaborate more on the sharp difference in ASR among different datasets such as CIFAR100 and SVHN under FedREP in Tables 15 and 16?

[3] Ye, Tiandi, et al. "BapFL: You can Backdoor Personalized Federated Learning." *ACM Transactions on Knowledge Discovery from Data* (2024).

[4] Lyu, Xiaoting, et al. "Lurking in the shadows: Unveiling Stealthy Backdoor Attacks against Personalized Federated Learning." *arXiv preprint arXiv:2406.06207* (2024).

### Soundness
2

### Presentation
3

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
The authors investigate the potential of backdoor attacks targeting personalized federated learning (PFL) and intuitively outline why such attacks often fail in PFL. They propose using natural features rather than manually designed triggers to execute backdoor attacks in PFL, which improves both the attack's success rate and robustness across various test cases, with or without defenses.

### Strengths
1. Clear and well-structured presentation
2. Comprehensive experimental test cases covering various attacks, defenses, and PFL mechanisms
3. Novel reinforcement techniques, including generating target features

### Weaknesses
1. Fundamentally, I feel like the traditional backdoor objective may be insufficient for effectively attacking personalized federated learning (PFL), especially in scenarios with a high degree of non-i.i.d. data where each client has its own unique "target." Therefore, a personalized or adaptive backdoor attack approach may be necessary. Specifically, the current approach seems to assume a single global backdoor target, which may not be realistic in PFL where clients have diverse data distributions and potentially different objectives. The attack's effectiveness could be significantly reduced when the backdoor target conflicts with a client's local learning objective.
2. The current attack mechanism is based on empirical intuitions. Strengthening this work could involve a deeper exploration of the model’s internal dynamics, such as identifying which layers or neurons are critical for shared vs. unshared parameters and examining the influence of regularization on the model. For instance, analyzing the gradient flow during the backdoor training process could reveal which parts of the model are most susceptible to the attack. Furthermore, a more rigorous analysis of how different regularization techniques impact the backdoor's success would be beneficial. Alternatively, providing a fundamental analysis of why traditional backdoor attacks fail and why Bad-PFL succeeds would also add significant value.
3. As this is the first study on backdoor attacks in PFL, rather than focusing on more practical backdoor scenarios, it’s recommended to compare white-box and black-box attacks. This comparison can help illustrate the limitations of current attacks, especially when the attacker has knowledge of clients' data and the full model structure, thus providing justification for the authors' three hypotheses on why the backdoor was ineffective in PFL. Specifically, a white-box attack where the attacker has full access to the model architecture, parameters, and client data distributions would provide a strong baseline. Comparing this to a black-box scenario where the attacker has limited information would highlight the attack's robustness and limitations.

### Questions
1. The authors consider using natural features as triggers, termed an edge-case attack in [1]. I wonder if the main distinction of the proposed attack is that it generates target features rather than manually selecting them. However, it seems that different clients—or at least different client groups—may require distinct natural features for effectiveness.
2. Other than training-stage defenses (i.e., robust aggregation), have the authors considered post-training defenses (e.g., pruning, CRFL [2]) or unlearning as defenses? I feel those defenses may be more effective on backdoor attacks.
3. For different clients, does the effectiveness of the backdoor vary significantly? And is this variation caused by data heterogeneity or differences in shared model parameters?
4. What happens when attackers target different labels and clients have multiple objectives? Detailed experiments may not be necessary, but insights and intuitions would be helpful.

[1] Wang, Hongyi, et al. "Attack of the tails: Yes, you really can backdoor federated learning." Advances in Neural Information Processing Systems 33 (2020): 16070-16084.
[2] Xie, Chulin, et al. "Crfl: Certifiably robust federated learning against backdoor attacks." International Conference on Machine Learning. PMLR, 2021.

### Soundness
3

### Presentation
3

### Contribution
2
