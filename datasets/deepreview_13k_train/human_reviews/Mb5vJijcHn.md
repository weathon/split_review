# Decoupling Backdoors from Main Task: Toward the Effective and Durable Backdoors in Federated Learning

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
Federated learning, as a distributed machine learning method, enables multiple participants to collaboratively train a central model without sharing their private data. However, this decentralized mechanism introduces new privacy and security concerns. Malicious attackers can embed backdoors into local models, which are inherited by the central global model through the federated aggregation process. While previous studies have demonstrated the effectiveness of backdoor attacks, the effectiveness and durability often rely on unrealistic assumptions, such as a large number of attackers and scaled malicious contributions. These assumptions arise because a sufficient number of attackers can neutralize the contributions of honest participants, allowing the backdoor to be successfully inherited by the central model. In this work, we attribute these backdoor limitations to the coupling between the main and backdoor tasks. To address these backdoor limitations, we propose a min-max backdoor attack framework that decouples backdoors from the main task, ensuring that these two tasks do not interfere with each other. The maximization phase employs the principle of universal adversarial perturbation to create triggers that amplify the performance disparity between poisoned and benign samples. These samples are then used to train a backdoor model in the minimization process. We evaluate the proposed framework in both image classification and semantic analysis tasks. Comparisons with four backdoor attack methods under five defense algorithms show that our method achieves good attack performance even if there is a small number of attackers and when the submitted model parameters are not scaled. In addition, even if attackers are completely removed in the training process, the implanted backdoors will not be dramatically weakened by the contributions of other honest participants.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a min-max backdoor attacks for federated learning, with an objective to separate the interference between the main and backdoor tasks. The proposed attack is composed of two phase: the maximization phase amplifies the difference between benign and malicious samples, and then minimize phase then trains the backdoor. It compares three other attacks under five defenses. The evaluation is done on two types of tasks: image classification and emotion analysis.

### Strengths
- Backdoor attacks is still a relevant issue in federated learning

### Weaknesses
 - Representative and unconvincing evaluation results.
The comparison attacks considered here are dated. And, the defense methods are even more outdated, i.e. all published before 2018. Flame is one of the strongest defense. The authors should have at least included that one.  The attacks and defense comparisons are only done in one of the dataset of the image classification task. I would expect an exhaustive evaluation on all the data sets of both tasks. 
- Missing comparison and indepth understanding of the prior art. 
This is very active research field - attacks in FL for both ML and security research comminutes. Authors have unfortunately missed out a large body of prior work.  All the cited baselines and prior work are simply outdated. 
- Unclear methodology.
From the writing, it's not clear why such a min-max method will work and what advantage it actually brings to the backdoor. The stealthiness aspect of backdoor task is not discussed.
- The argument and writing are rather premature. 
There are still a lot of typos and incomplete argument.

### Questions
See my points in the weakness.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Existing works have demonstrated that the effectiveness and durability of backdoor attacks often rely on unrealistic assumptions, such as a large number of attackers and scaled malicious contributions. The authors attribute these backdoor limitations to the coupling between the main and backdoor tasks. Then they propose a min-max backdoor attack method, termed EDBA, which decouples backdoors from the main task. EDBA consists of two phases. In the maximization phase, EDBA generates triggers that maximize the performance disparity between poisoned and benign samples. In the minimization phase, EDBA utilizes both poisoned and benign samples to inject the triggers into the local model. The authors compared EDBA with three attack methods under six defense algorithms to verify the EDBA’s effectiveness.

### Strengths
1. The idea of decoupling the backdoor task from the main task to enhance the effectiveness and durability is novel and less studied in previous works. The proposed EDBA seems to be competitive with related methods.
2. The paper is well-organized in general, well-written and mostly easy to follow.
3. This paper addresses a pertinent problem in Federated learning. The extensive experiments show that EDBA works even if there is only one attacker among 200 clients.

### Weaknesses
1. **Robustness of EDBA.** In section 3.2, the authors state that “within the FL setting, the invisibility of triggers in the local model is not a crucial metric”. However, this is inconsistent with existing works [1,2,3], which emphasize the necessity of ensuring trigger invisibility through smaller norm constraints, fewer perturbed pixels, semantic features, or edge-case samples. I strongly recommend the authors to reconsider this position and provide visualizations of the generated triggers. If these triggers are visually apparent, benign clients could easily detect them through simple inspection, undermining the effectiveness of the approach.

2. **Cost with NLP tasks.** While it is good that the authors have considered NLP datasets, it is concerning that EDBA in NLP tasks appears to exhibit high time complexity. For Eq. 5, the requirement to calculate the importance score for each word position raises significant efficiency concerns. So the complexity should be analysis.

### Questions
1. This paper compares its method to IBA, which includes a norm constraint on trigger size during generation. It is critical to know whether a similar norm constraint has been applied in your method for a fair comparison. If there is no norm constraint on trigger generation, could a clean sample($x^\ast$) from the target class be directly selected as the triggered sample($x + T$)?  If so, why we need the Max optimization phase?

2. The authors generate triggers aimed at maximizing the logit output distance between clean and poisoned data. However, could these triggers be regarded as out-of-distribution (OOD) features? A clear explanation of why EDBA works in this context is essential. Additionally, I strongly recommend including a comparison with the edge-case method [1], which utilizes marginal distribution samples as triggers, where the model misclassifies with higher probability. Clarifying the relationship between EDBA and the edge-case method would greatly enhance the paper's clarity and rigor.

3. Regarding Eq. 5, if the classification of a sentence remains unchanged after adding the trigger at a specific position, does this imply that the backdoor task and the main task are still coupled?

4. The description of Fig. 6 is somewhat unclear and lacks sufficient detail. Specifically, in Fig. 6(b) and (d), does this suggest that the poisoned samples are clustered based on their original categories? I strongly recommend that the authors provide a more thorough explanation of Fig. 6 to improve understanding.

5. I have also noted several typos in the paper. For instance, in Fig. 6(a) and (c), "benigh" should be corrected to "benign."

[1]. Wang H, Sreenivasan K, Rajput S, et al. Attack of the tails: Yes, you really can backdoor federated learning[J]. Advances in Neural Information Processing Systems, 2020, 33: 16070-16084.

[2]. Bagdasaryan E, Veit A, Hua Y, et al. How to backdoor federated learning[C]. International conference on artificial intelligence and statistics. PMLR, 2020: 2938-2948.

[3]. Nguyen T D, Nguyen T A, Tran A, et al. Iba: Towards irreversible backdoor attacks in federated learning[J]. Advances in Neural Information Processing Systems, 2024, 36.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new backdoor injection algorithm against federated learning systems. It formulates backdoor training as a min-max framework. The framework first designs triggers to amplify the performance disparity between poisoned and benign samples. Crafted backdoor samples are then applied to train the backdoor model to achieve both effectiveness and durability. Authors further conduct experiments to verify the performance of the proposed method against various defense mechanisms.

### Strengths
1. This paper is well-written with clear structure.
2. This paper propose a novel backdoor training algorithm which could achieve effectiveness and durability simultaneously.
3. This paper list detailed configuration of training parameters.

### Weaknesses
1. The claimed unrealistic assumptions of existing backdoor attacks is not accurate. Recent backdoor attack algorithms [1,2] only require controlling a single client for every global round, and does not need scaled malicious contributions. Furthermore, the argument that existing methods require amplified perturbations is not universally true, as some methods achieve success with subtle triggers. The paper should more clearly define the specific limitations of existing methods that this work addresses, rather than making broad generalizations.
2. What is the final trigger for the adversary to evaluate? Is the final evaluated trigger generated from the last global round which the adversary participate? If so, will the injection of previously generated triggers before the last participated round helps the injection at the last round? (as the injected triggers are different for every global rounds). The paper needs to clarify how the triggers evolve across rounds and whether earlier triggers contribute to the final attack success, or if each round's trigger is independent. The lack of clarity on this point makes it difficult to assess the method's overall effectiveness and practical relevance.
3. Please specify a specific scenario/setting where the adversary could attach such fine-grained triggers, with unlimited range in the image space (same size to the whole image) and detailed pixel values. Otherwise, the practicality of the method is limited. The paper should address the feasibility of implementing such triggers in real-world scenarios, especially considering the constraints of physical systems and data acquisition methods.
4. Could the proposed method bypass the recent SOTA backdoor detection mechanism, BackdoorIndicator[3]? The decoupling process, which aims to maximize the difference between benign and poisoned updates, could make poisoned samples as out-of-distribution samples with respect to benign samples. And this aligns with the defense rationale proposed by the BackdoorIndicator. The paper should include an evaluation against BackdoorIndicator to validate its robustness against state-of-the-art detection methods. The current evaluation is incomplete without this analysis.
5. Some minor mistake in line 231, "participantsaAz".

### Questions
1. What is the final trigger for the adversary to evaluate? Is the final evaluated trigger generated from the last global round which the adversary participate? If so, will the injection of previously generated triggers before the last participated round helps the injection at the last round? (as the injected triggers are different for every global rounds). Please further specify this part.
2. Could the proposed method bypass BackdoorIndicator?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the authors attribute the indurability and ineffectiveness of FL backdoor attacks to the coupling of the main and backdoor tasks. They propose a unified FL backdoor framework called EDBA, which employs the principle of universal adversarial perturbation to craft triggers that effectively separate the main and backdoor tasks. Their method is compared with three state-of-the-art backdoor attack methods under six defense methods. The experimental results demonstrate that the proposed method performs well in both computer vision and natural language processing tasks.

### Strengths
1.	This paper attempts to address the important issue of backdoor durability in the field of FL.
2.	In terms of experimental evaluation, the authors not only consider computer vision tasks but also extend their evaluation to natural language processing tasks. Besides, the Tiny-ImageNet dataset is included.

### Weaknesses
1. It is difficult to argue that this paper presents any technical innovation, as the authors merely use UAP as a trigger for backdoor insertion. Notably, a similar idea has already been proposed in IBA.
2. The authors have not conducted a thorough enough survey of related work. In terms of attacks, several studies that are closely related to the paper’s emphasis on durability have been overlooked, such as A3FL (NeurIPS 2023), Chameleon (ICML 2023), and CerP (AAAI 2023). As for defenses, all the methods mentioned are from before 2022.
3. Several important experiments are missing, such as evaluating the impact of the attacker proportion, the degree of Non-IID, and adaptive defenses on the results.
4. The defenses considered by the authors are insufficient to demonstrate the effectiveness of EDBA. They only evaluated four outdated defenses: NDC (2019), Krum/Multi-Krum (2017), Median (2018), and RLR (2021). More recent and advanced backdoor defenses should be considered, such as FLAME, BayBFed, DeepSight, and FreqFed.
5. When evaluating durability, the authors did not deploy any defenses or compare their method with existing durable backdoor approaches (such as the IBA mentioned in the paper), let alone more advanced methods like A3FL or Chameleon. Therefore, the durability of EDBA is not convincingly demonstrated.
6. The authors have not designed any specific evasion modules for existing defenses, yet the results suggest that EDBA can bypass certain defenses. I believe it is necessary to explain this phenomenon.

### Questions
My questions are included in Weaknesses.

### Soundness
1

### Presentation
2

### Contribution
1
