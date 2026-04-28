# On the Adversarial Vulnerability of Label-Free Test-Time Adaptation

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
Despite the success of Test-time adaptation (TTA), recent work has shown that adding relatively small adversarial perturbations to a limited number of samples leads to significant performance degradation. Therefore, it is crucial to rigorously evaluate existing TTA algorithms against relevant threats and implement appropriate security countermeasures. Importantly, existing threat models assume test-time samples will be labeled, which is impractical in real-world scenarios. To address this gap, we propose a new attack algorithm that does not rely on
access to labeled test samples, thus providing a concrete way to assess the security vulnerabilities of TTA algorithms. Our attack design is grounded in theoretical foundations and can generate strong attacks against different state of the art TTA methods. In addition, we show that existing defense mechanisms are almost ineffective, which emphasizes the need for further research on TTA security. Through extensive experiments on CIFAR10-C, CIFAR100-C, and ImageNet-C, we demonstrate that our proposed approach closely matches the performance of state-of-the-art attack benchmarks, even without access to labeled samples. In certain cases, our approach generates stronger attacks, e.g., more than 4% higher error rate on CIFAR10-C.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a novel label-free adversarial attack against Test-Time Adaptation (TTA) algorithms, called Feature Collapse Attack (FCA). The authors argue that existing TTA attack methods unrealistically assume access to test data labels, making them impractical for real-world scenarios. They address this gap by formulating a new attack that leverages the principles of Neural Collapse (NC) to degrade TTA performance without needing ground truth labels.

### Strengths
1. The paper addresses a significant limitation of existing TTA attack research by introducing a label-free approach. This is crucial for practical security evaluations of TTA, as real-world adversaries are unlikely to have access to test labels.
2. The attack design is well-motivated by the theory of Neural Collapse, providing a clear rationale for the chosen loss functions.
3. FCA achieves competitive performance against state-of-the-art attacks that utilize labels, and even surpasses them in some cases. This demonstrates its effectiveness and potential impact.
4. The authors evaluate their attack across multiple datasets and TTA methods, providing a thorough assessment of its generalizability.

### Weaknesses
1. **Assumption of White-Box Access:** The attack assumes white-box access to the model parameters, which might not always be realistic. Analyzing the attack's performance under more restricted settings, such as black-box or gray-box access, would provide a more complete picture of its capabilities. Specifically, the reliance on gradient information for the optimization process limits its applicability in scenarios where such access is unavailable or restricted. Exploring the use of query-based attacks or transfer-based attacks could broaden the scope and relevance of the proposed method.

2. **Attack Algorithm:** The attack part of the FCA algorithm is almost entirely borrowed from the PGD in the adversarial sample attack, which will affect the contribution of this paper. Furthermore, does this suggest that the method could be well enhanced by using more powerful attacks? The direct application of PGD raises questions about the novelty of the attack mechanism itself. While PGD is a well-established method, the paper does not explore alternative optimization strategies or modifications that could potentially enhance the attack's effectiveness or efficiency. The lack of exploration into more advanced adversarial techniques limits the potential impact of the proposed approach.

3. **The Robustness of Victim Model:** The effectiveness of the proposed attack may be limited when targeting inherently robust models or those with defense mechanisms (adversarial training), since it builds upon adversarial attack principles. How significantly does the attack's performance degrade when faced with robust or defended victim models? The paper should investigate the attack's resilience against models trained with adversarial training or other robustness-enhancing techniques. The current evaluation lacks a comprehensive analysis of the attack's performance in the presence of such defenses, which is critical for understanding its practical limitations.

### Questions
1. **Assumption of White-Box Access:** The attack assumes white-box access to the model parameters, which might not always be realistic. Analyzing the attack's performance under more restricted settings, such as black-box or gray-box access, would provide a more complete picture of its capabilities.
2. **Attack Algorithm:** The attack part of the FCA algorithm is almost entirely borrowed from the PGD in the adversarial sample attack, which will affect the contribution of this paper. Furthermore, does this suggest that the method could be well enhanced by using more powerful attacks?
3. **The Robustness of Victim Model:** The effectiveness of the proposed attack may be limited when targeting inherently robust models **[R]** or those with defense mechanisms (adversarial training), since it builds upon adversarial attack principles. How significantly does the attack's performance degrade when faced with robust or defended victim models?

**[R]** MEMO: Test Time Robustness via Adaptation and Augmentation.

### Soundness
2

### Presentation
2

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
The paper concentrates on the adversarial vulnerability in test-time adaptation (TTA). To explore more practical adversarial attacks, the paper designs a novel attack algorithm, named Feature Collapse Attack (FCA), which can achieve comparable performance without access to labeled test samples. This method consists of three loss designs, which are Nearest Centroid Loss, Feature Collapse Loss and Feature Scattering Loss. Experimental results demonstrate the outstanding performance of the proposed method.

### Strengths
+ **New Scenario**: The paper explores a novel scenario, where the attacker has no access to the true labels.
+ **Simple Implementation**: The proposed method is relatively easy to implement and follow.

### Weaknesses
 + The number of baseline attack methods is limited. More comparison with multiple attacks is expected.
+ In line 134, there is a repeated word "the".

### Questions
The paper considers the worst-case scenario where the attacker has knowledge of the TTA algorithm and has white-box access to the latest updated model parameters provided by some malicious insider. Under this assumption, is it reasonable to hypothesize that the attacker has no access to the true labels?

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
3

### Summary
The authors study the robustness of test-time adaptation (TTA) methods and propose a novel label-free attack. They argue that the assumption of the attacker having true labels on the test set is too strong for the real-life scenarios and without it the existing DIA attack is much less effective. However, the FCA attack proposed in the paper, that uses the idea of neural collapse, remains effective in the label-free scenario which emphasizes the need to further study the TTA robustness.

### Strengths
**Originality**: label-free attacks on test-time adaptation seem to be a novel direction. The paper demonstrates the weaknesses of existing defence mechanisms (Section 7.1)

**Quality**: the results are supported with numerous experiments on different datasets (CIFAR10-Cm CIFAR100-C, ImageNet-C) and have theoretical justification (Theorem 1 with proof in Appendix). Ablation study with respect to different loss components is performed (Table 4). 

**Clarity**: the paper is in general well structured.

**Significance**: robustness of test-time adaptation is important in real life applications.

### Weaknesses
 **Quality:**

1)	The experiments are performed only with the ResNet architecture variants (line 316). Empirical results would benefit from including some other popular architecture e. g. one based on a vision transformer. At least in the Appendix. The lack of experiments on other architectures limits the generalizability of the findings. Specifically, Vision Transformers, with their fundamentally different architecture and reliance on attention mechanisms rather than convolutional layers, might exhibit different vulnerabilities to the proposed attack. It is crucial to investigate whether the observed neural collapse phenomenon, which the attack exploits, is equally present and exploitable in transformer-based models.

**Clarity:**

1)	Figure 1a: the process in the Figure 1a is hard to grasp for an outside reader. The diagram flow is confusing. Consider making it clearer where the flow starts and ends.  The overview figure has to be more intuitive to help the reader better understand the paper idea and not to confuse them. Consider simplifying it or breaking into several Figures. The top dotted line is missing an arrow on its end.

2)	Please elaborate on how the pseudo labels are defined or add a citation (line 364). The definition of pseudo-labels is crucial for understanding the attack's mechanism, and the current explanation lacks sufficient detail. It is unclear whether hard or soft pseudo-labels are used, and how these labels are generated from the model's predictions. This ambiguity makes it difficult to reproduce the results and fully grasp the attack's methodology.

**Typos and minor comments:**

1)	Line 090 - “as” not needed: This makes our proposed attack **as** a prevalent threat that requires countermeasure

2)	Line 134 - additional “the”: and **the** the set

3)	Line 172 - Why is “Nearest Neighbour Classifier” abbreviated as NCC and not NNC?

4)	Line 265 - the sentence is too complex and poorly constructed, it is hard to understand its point. The more the last layer activations collapse to class mean vector, the likelihood of having a region close to it where the actual prediction deviates if the sample is projected into that region decreases

5)	Line 314 - delete one “use”: we use the use the provided data.

6)	It would be good to include “w/o Attack” value (Table 1) in the Table 4 to better the relative improvement of each variant. The L_nc + L_col would also be good to include for completeness. Perhaps there is some synergy between these two terms that make their combination stronger than the sum of each term.

### Questions
1) Why is the perturbation initialized with 0.5 and not e. g. as random noise? (Algorithm 1, step 2) Wouldn’t the optimization benefit from this?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
To address the distribution shift of deep neural networks (DNNS), test-time adaptation (TTA) updates the model parameters using test samples. However, recent work reveals that TTA algorithms are vulnerable to adversarial attacks. This paper proposes a novel attack named Feature Collapse Attack (FCA). To be specific, the adversarial generated through FCA can be mixed with benign samples, thereby degrading the performance of the target model. A main feature of FCA is that it does not need the label of the test samples.

### Strengths
- This paper is well-written and easy-to-follow
- TTA algorithms are the key developing trend of AI, and the evaluation of the adversarial robustness of TTA algorithms is timely and necessary.

### Weaknesses
 - The threat model of this paper is impractical.

     - One of the main claims of this article is the practicability of the attacks. The paper pointed out that previous attacks like DIA need the label of the test sample. The reviewer agrees that it is very valuable to design a label-free attack. However, in Section 4, the authors claimed that the attacker has white-box access to the latest updated model parameters provided by some malicious insider. In my opinion, this assumption is impractical. First, who is the malicious insider? Can the authors provide a real-world example? 
     - In the threat model of (Cong et al., 2024), they proposed a black-box attack named TePA. TePA does not need access to the parameters of the updated model, which is more practical.
     - The authors also claimed that "existing threat models assume test-time samples will be labeled", and TePA (Cong et al., 2024) relies on access to the entire source dataset to train a substitute model. Actually, TePA also is a label-free attack, and it does not need access to the entire source dataset. It only needs a surrogate dataset that has a similar distribution of the source dataset. I suggest that the authors reorganize the introduction of related work.

- In experiments like Table 1, this paper does not compare the attack success rate with TePA (Cong et al., 2024).
- This paper considers five target TTA methods, which all need the test samples to be fed in a batch-by-batch manner. However, some TTA methods like TTT [R1] can accept only one sample to adjust the model. I am curious if FCA can attack such kinds of TTA methods.
- The proposed attack seems not to be stealthy. In other words, FCA needs a high poisoning rate (Table 3).
- How many batches does FCA need to effectively decrease the target model's performance?
- In (Cong et al., 2024). they also proposed several defenses, which are not discussed in this paper.

### Questions
Thanks for submitting the paper to ICLR 2025!

This paper aims to address a timely and important problem, i.e., evaluating the adversarial robustness of TTA algorithms. As the authors claimed, launching adversarial attacks against TTA algorithms is not a novel question, but at an early stage. Meanwhile, mounting adversarial attacks against TTA algorithms is not trivial, as the capability of the attacker is limited. The authors demonstrate the effectiveness of their proposed FCA attack. However, I have the following questions.

- My biggest concern is the threat model of this paper.

     - One of the main claims of this article is the practicability of the attacks. The paper pointed out that previous attacks like DIA need the label of the test sample. The reviewer agrees that it is very valuable to design a label-free attack. However, in Section 4, the authors claimed that the attacker has white-box access to the latest updated model parameters provided by some malicious insider. In my opinion, this assumption is impractical. First, who is the malicious insider? Can the authors provide a real-world example? 
     - In the threat model of (Cong et al., 2024), they proposed a black-box attack named TePA. TePA does not need access to the parameters of the updated model, which is more practical.
     - The authors also claimed that "existing threat models assume test-time samples will be labeled", and TePA (Cong et al., 2024) relies on access to the entire source dataset to train a substitute model. Actually, TePA also is a label-free attack, and it does not need access to the entire source dataset. It only needs a surrogate dataset that has a similar distribution of the source dataset. I suggest that the authors reorganize the introduction of related work.

- In experiments like Table 1, this paper does not compare the attack success rate with TePA (Cong et al., 2024). 
- This paper considers five target TTA methods, which all need the test samples to be fed in a batch-by-batch manner. However, some TTA methods like TTT [R1] can accept only one sample to adjust the model. I am curious if FCA can attack such kinds of TTA methods.
- The proposed attack seems not to be stealthy. In other words, FCA needs a high poisoning rate (Table 3).
- How many batches does FCA need to effectively decrease the target model's performance?
- In (Cong et al., 2024). they also proposed several defenses, which are not discussed in this paper.

Reference

[R1] Test-Time Training with Self-Supervision for Generalization under Distribution Shifts. ICML 2020.

### Soundness
3

### Presentation
3

### Contribution
3
