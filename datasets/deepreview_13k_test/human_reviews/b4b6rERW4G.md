# Concealing Backdoors in Federated Learning by Trigger-Optimized Data Poisoning

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
Federated Learning (FL) is a decentralized machine learning method
that enables participants to collaboratively train a model without
sharing their private data. Despite its privacy and scalability
benefits, FL is susceptible to backdoor attacks, where adversaries
poison the local training data of a subset of clients using a backdoor
trigger, aiming to make the aggregated model produce malicious results
when the same backdoor condition is met by an inference-time input.
Existing backdoor attacks in FL suffer from common deficiencies: fixed
trigger patterns and reliance on the assistance of model
poisoning. State-of-the-art defenses based on analyzing clients' model updates exhibit a good defense performance on these attacks
because of the significant divergence between malicious and benign client model updates. To effectively conceal malicious model updates among
benign ones, we propose \ourmodel{}, a backdoor attack strategy in FL
that dynamically constructs backdoor objectives by optimizing a
backdoor trigger, making backdoor data have minimal effect on model
updates. We provide theoretical justifications for \ourmodel{}'s
attacking principle and display experimental results showing that
\ourmodel{}, via only a \textit{data}-poisoning attack, effectively
undermines state-of-the-art defenses and outperforms existing backdoor
attack techniques on various datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces DPOT, a backdoor attack strategy that optimizes the trigger pattern to combine with data instead of using a fixed pattern using multi-object optimization. Unlike previous attacks that relied on fixed patterns or model manipulation, DPOT dynamically adjusts trigger placements and values to blend malicious updates with benign ones, effectively bypassing standard defenses. Experimental results show DPOT’s superior attack success rate across various datasets, demonstrating both high effectiveness and stealthiness in maintaining main-task accuracy​.

### Strengths
- This paper is easy to follow with a good structure. The method is clear and sounds.
- This paper has comprehensive evaluations across diverse datasets and defenses.
- The using of dynamic trigger optimization is interesting.

### Weaknesses
1. The trigger seems to be very noticeable, especially when the trigger size is high, which can not be effective against post-defense such as Neural Cleanse. The suggestion for the trigger size is vague and does not contain specific number ranges (Appendix D.3), which is hard to apply in real settings. Could the author argue more about it?
2. The authors did not well discuss the difference between this method with related works using optimized triggers nor comparing them [1][2]. The idea of optimizing triggers is somewhat similar to adversarial attack methods like the Basic Iterative Method (BIM) and Fast Gradient Sign Method (FGSM) in terms of iterative gradient-based optimization, but the discussion is missing.
3. The results in Table 8 and Table 9 raise suspicion that in existing attack papers, the MA of CIFAR-10 should be > 80% but in those tables, the corresponding number is around 70% [3].
4. The rationale for why using DPOT and its subsequent stealthiness across the defenses is unclear, given that Algo 1 and Algo 2 only focus on optimizing triggers to mislead the classification output of model $W_g$.
5. This method does not include any component to ensure the MA of the model, and the Backdoor attack should consider both ASR and MA. How to show that this method intuitively does not degrade MA. In Algo.2, there is no optimization objective to maintain clean accuracy, and the MA should be reported together with the ASR in the main paper.
6. The related works and introduction should include more works in the literature, now it is not extensive enough.

[1] Fang, Pei, and Jinghui Chen. "On the vulnerability of backdoor defenses for federated learning." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 37. No. 10. 2023.

[2] Nguyen, Thuy Dung, et al. "Iba: Towards irreversible backdoor attacks in federated learning." *Advances in Neural Information Processing Systems* 36 (2024).

[3] Xie, Chulin, et al. "Dba: Distributed backdoor attacks against federated learning." *International conference on learning representations*. 2019.

### Questions
1. In DPOT, the $W_g$ is used as the starting point model to optimize the trigger, however, at the original rounds, this model has not been converged, does it affect the performance of this method?
2. In Algo.1., why is not CE loss used here, given this is a classification problem?
3. How is the data poison rate set for the baselines? Since the high DPR may relate to higher suspicion, the original DPR in the DBA paper is much lower than 0.5. An experiment with a smaller DPR with all baselines can ensure fairness across baselines.
4. In Figure 3 and Table I, was it the non-IID or IID setting? It is important that the proposed method can work with both scenarios.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, the authors propose DPOT, a novel backdoor attack method relying solely on data poisoning in federated learning (FL). DPOT dynamically adjusts the backdoor objective to conceal malicious clients' model updates among benign ones, allowing the global model to aggregate them even when protected by state-of-the-art defenses.

### Strengths
1.	This paper tackles a challenging FL backdoor attack scenario, where the FL system employs a trusted execution environment to restrict clients from freely modifying the objective function, limiting attackers to data poisoning as their only option for inserting backdoors.
2.	The authors validate DPOT’s effectiveness through extensive experiments and offer theoretical insights to explain its success.
3.	The paper is well-written, clearly conveying both the workings of the proposed method and the reasoning behind it.In this work, the authors propose DPOT, a novel backdoor attack method relying solely on data poisoning in federated learning (FL). DPOT dynamically adjusts the backdoor objective to conceal malicious clients' model updates among benign ones, allowing the global model to aggregate them even when protected by state-of-the-art defenses.

### Weaknesses
1.	DPOT’s core concept of using a UAP as a trigger (even though the UAP changes dynamically each round) lacks novelty; similar approaches have already been explored in methods like A3FL and IBA.
2.	Could the authors clarify why A3FL shows a performance far below the values reported in the original paper, even underperforming compared to FT and DFT? This result appears counterintuitive. Also, A3FL should be given more emphasis in the main experiment, rather than being placed in the Appendix.
3.	In Table 5, why is the trigger size for Fashion MNIST set larger than for CIFAR-10 and even equal to Tiny ImageNet?
4.	A comparison between DPOT and IBA (IBA: Towards Irreversible Backdoor Attacks in Federated Learning) would be beneficial, as IBA optimizes the trigger generator, which intuitively offers greater room for enhancement and may outperform all baselines considered here.
5.	In terms of defenses, it would be useful to include more recent approaches, such as BackdoorIndicator (Usenix Security ‘24).
6.	Would optimizing only the Trigger-Pixel Values without limiting Trigger-Pixel Placements lead to better attack performance?
7.	Can DPOT withstand adaptive defenses, where defenders anticipate the use of DPOT and design customized countermeasures?
8.	The impact of different levels of Non-IID on DPOT’s attack performance is not evaluated.

### Questions
My questions are included in Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper addresses a critical issue in federated learning: the threat of backdoor attacks. It proposes a novel attack method called DPOT (Data Poisoning with Optimized Trigger), which leverages trigger optimization to effectively conceal malicious model updates. Specifically, DPOT dynamically adjusts the trigger pattern by identifying the optimal locations and values of the trigger using gradient scores for each pixel. An extensive evaluation on four datasets: Fashion-MNIST, CIFAR-10, FEMNIST, and Tiny ImageNet along with a comprehensive analysis of backdoor defense mechanisms, demonstrates the effectiveness of DPOT.

### Strengths
- The evaluation metrics (Final ASR, Average ASR, Main-task Accuracy) are well-defined and provide a thorough assessment of the attack’s effectiveness.
- The analysis of various hyperparameter impacts on attack performance offers valuable insights into DPOT’s behavior.
- A detailed analysis of DPOT’s working principle is provided, distinguishing between the aggregation of backdoored model updates and benign updates.

### Weaknesses
- While DPOT effectively hides malicious model updates, the backdoor images still display a visible trigger, which could limit the attack's practicality in real-world applications. Have the authors considered techniques such as IBA [1] or similar methods to make the trigger less detectable? An analysis comparing DPOT's trigger visibility with other state-of-the-art methods, including a discussion on the trade-off between trigger visibility and attack effectiveness, would be valuable.
- DPOT’s use of an adversarial-style trigger is likely a significant factor in its success, which may explain its improved performance over fixed-pixel triggers. However, it would strengthen the paper by providing a detailed comparison with other adversarial trigger methods, such as A3FL, in terms of both attack effectiveness and computational overhead. Conducting experiments that directly compare DPOT with A3FL under the same settings could help clarify DPOT’s unique advantages.
- The paper does not specify the number of pixels in Algorithm 1, which is crucial for the optimization process. How is this pixel count determined in practice?
- The paper lacks a discussion on the potential limitations of DPOT and possible future directions to address them. For instance, the authors could suggest strategies to defend against DPOT, propose enhancements to strengthen existing defense mechanisms, or explore applying the technique to other domains (e.g., text or time-series data) and FL tasks (e.g., regression or reinforcement learning).

### Questions
- Could an $L_\infty$ norm be used to constrain the trigger pattern, and how would this impact attack performance?
- How does the optimization process in DPOT compare to other optimization-based attacks like A3FL in terms of training time and convergence?
- How does model performance compare when optimization for trigger-pixel values is omitted (i.e. when selected positions are set to 1)?
- Do all attack scenarios require attackers to participate in only one training round?
- In Figure 6 (page 23), global accuracy on the main task drops between rounds 0 and 40, so the server might not need the contribution from clients and can detect the poisoned model early. How can this be prevented?
- The FEMNIST dataset lacks a dedicated test set. How was a test set generated for this dataset?
- How is the non-iid data distribution considered in attack scenarios?

**References:**

[1] Nguyen, Thuy Dung, et al. "IBA: Towards irreversible backdoor attacks in federated learning." Advances in Neural Information Processing Systems 36 (2024).

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
4

### Summary
This work proposes a data-poisoning backdoor method with dynamic malicious training objective. Authors argue that current backdoor training algorithms either adopt fixed trigger pattern, or highly relies on model-poisoning assumption. These attacks could fail to escape from current defenses as backdoor updates deviate much from benign ones. Methods based on model poisoning are unrealistic under TEEs. This work thus proposes DPOT to dynamically search for optimal trigger patterns to avoid the detection of defenses mechanisms. Authors further provide empirical results to demonstrate the effectiveness of the method against several defense mechanisms in comparison with other backdoor training algorithms.

### Strengths
1. This paper identify a novel scenario, where the existence of TEEs eliminates the possibility of model-poisoning attacks.
2. well-written with clear structure.

### Weaknesses
1. This paper claims that the static optimization objective makes current backdoor training algorithms generate updates with distinct difference with benign ones. This could result in the rejection of many backdoor detection methods. However, a recent work [1] finds that adversaries could simply adopt smaller learning rates to train backdoored models. This could craft malicious updates which are statistically close to benign ones, bypassing most defense methods. This raises concern about the necessity about the proposed method. Authors could further conduct experiments under different adversarial settings (different learning rates), and also against the recent work [1].
2. The newly proposed method, DPOT, involves trigger optimization for every global round. And since optimized triggers are different for every global round, will the malicious training for early rounds (with different triggers) helps the training for the last round (the final evaluated trigger)? Otherwise, i cant find reasons for continuously poisoning the FL systems with different triggers.
3. As DPOT introduces extra operations after receiving the global model, time consumed by the optimization procedure could be important. This is because extra processing time could may cause the drop out of malicious clients. I suggest that authors could further discuss on this part.
4. Carefully manipulating the pixel location and pixel value for triggers is not realistic for adversaries to deploy. I dont see a practical setting where adversaries could such precisely control the backdoor pixel location and value. Authors may consider specify this point in the threat model part, otherwise it is inconvincible that the described method is dangerous.
5. The abstract part claims this work provides theoretical justification about the methods. However, i could only find this part in the appendix. I suggest authors could put some of the main results in the main paper.

[1] Li, Songze, and Yanbo Dai. "BackdoorIndicator: Leveraging OOD Data for Proactive Backdoor Detection in Federated Learning." USENIX Security 2024.

### Questions
1. could DPOT still outperform other methods under different malicious settings? will it bypass the mentioned work?
2. could the malicious training for early rounds (with different triggers) helps the training for the last round (the final evaluated trigger)?
3. is DPOT practical at least for some settings?

### Soundness
3

### Presentation
2

### Contribution
2
