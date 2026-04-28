# Backdoor in Seconds: Unlocking Vulnerabilities in Large Pre-trained Models via Model Editing

- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 3, 5

## Abstract
Large pre-trained models have achieved notable success across a range of downstream tasks. However, recent research shows that a type of adversarial attack ($\textit{i.e.,}$ backdoor attack) can manipulate the behavior of machine learning models through contaminating their training dataset, posing significant threat in the real-world application of large pre-trained model, especially for those customized models. Therefore, addressing the unique challenges for exploring vulnerability of pre-trained models is of paramount importance. Through empirical studies on the capability for performing backdoor attack in large pre-trained models ($\textit{e.g.,}$ ViT), we find the following unique challenges of attacking large pre-trained models: 1) the inability to manipulate or even access large training datasets, and 2) the substantial computational resources required for training or fine-tuning these models. To address these challenges, we establish new standards for an effective and feasible backdoor attack in the context of large pre-trained models. In line with these standards, we introduce our EDT model, an \textbf{E}fficient, \textbf{D}ata-free, \textbf{T}raining-free backdoor attack method. Inspired by model editing techniques, EDT injects an editing-based lightweight codebook into the backdoor of large pre-trained models, which replaces the embedding of the poisoned image with the target image without poisoning the training dataset or training the victim model. Our experiments, conducted across various pre-trained models such as ViT, CLIP, BLIP, and stable diffusion, and on downstream tasks including image classification, image captioning, and image generation, demonstrate the effectiveness of our method. Our code is available in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose EDT, a backdoor attack method that injects a codebook in the encoder layers of victim models, enabling efficient attacks on large pre-trained models without requiring dataset poisoning or training of the vctim model. Experimental results indicate that EDT can maintain high clean accuracy and stealthiness across various models.

### Strengths
- The work identifies key challenges of backdoor attacks on large pre-trained models, including attack feasibility and capability. 
- By substituting the embedding of trigger with a codebook, EDT efficiently attacks large pre-trained models without incurring the cost of retraining or dataset poisoning.
- Experimental results show that EDT incurs minimal performance degradation while achieving 100% ASR, demonstrating its effectiveness

### Weaknesses
 - EDT's reliance on a codebook limits its applicability to large pre-trained models that do not have a codebook. Specifically, the method's effectiveness hinges on the existence of a suitable embedding space within the model's architecture where a codebook can be effectively integrated. This raises concerns about the generalizability of the approach to models with different architectural designs or those lacking a clear, separable embedding space.
- Lack of experiments for multi-target backdoor attacks, which would further validate EDT's versatility. The current evaluation focuses primarily on single-target attacks, leaving open questions about the method's performance and scalability when multiple triggers and target outputs are involved. This is a critical aspect to consider for real-world scenarios where attackers might aim to control multiple functionalities of a model.
- Table 1 is missing the results of Fine-tune Baseline on CLIP. It's unclear why multi-modal dataset is intractable to poison. The absence of this baseline makes it difficult to assess the relative performance of EDT against a standard fine-tuning approach, particularly in the context of multi-modal models. The explanation for the intractability of poisoning multi-modal datasets lacks sufficient detail, making it hard to understand the specific challenges involved.

### Questions
- Could you clarify how to EDT would be applied to stable diffusion models? There is no text or figure detailing this.
- Is it feasible to fine-tune only the encoder of large pre-trained models with triggers and corresponding target embeddings? This could be a cost-effective alternative to full model training, potentially enhancing the practicality of backdoor attacks.
- Typo: "PIPLINE" in the title of Section 3.3 and its first paragraph.

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
This paper studies the backdoor injection in large pre-trained models, where the proposed attack is training-free and data-free. The authors discuss the limitations of regular backdoor attacks, focusing on the threat model where training or fine-tuning large models is impractical for adversaries with limited access to computational resources. To this end, the authors propose a claimed training-free and data-free model editing-based backdoor attack where a codebook is injected into a pre-trained large model to inject the backdoor. The injected codebook examines the input and selectively replaces the embedding of the input with the target embedding. The proposed attack is evaluated on benchmark datasets.

### Strengths
This work's motivation is well illustrated. The authors provide a threat model in which the adversaries have limited computational resources, and the proposed backdoor attack is training-free. Previous works did not adequately discuss this threat scenario. The paper is generally well-structured, and most key points are clearly presented. However, several concerns still need to be clarified.

### Weaknesses
 - Important related works. Previous works [a, b] have discussed the model edit-base backdoor, but this work did not include these closely related works. For example, [a] proposes a step-by-step guide to injecting backdoors into pre-trained models by gradually modifying model parameters. It would be great if the authors could include closely related works and articulate the advantages and disadvantages of the proposed attack, especially the connections between different approaches. Also, the authors could revise the claimed threat model novelty regarding the related works. 

- Other baselines. Table 1 provides different backdoor attack baselines in comparison to the proposed attack. The justification behind the choices made is the types of backdoor attacks. One concern is that state-of-the-art backdoor attacks are not included, e.g., [c]. Based on the observation that the proposed attack is not significantly better than classical attacks, it would be great if the authors could clarify or provide analysis on recent backdoors. Another concern is that some baseline attacks are not thoroughly evaluated on CLIP-ViT and CLIP-ResNet. The authors explained that the multi-modal datasets are intractable to poison, but further details are appreciated. In addition, the threat models of the baselines in Table 1 are not the same, which may introduce unfair comparisons. This needs to be explained. 

- Evaluation against different backdoor defenses. Two defenses have been discussed in the paper. But, still, the selection of the defenses needs to be justified. In particular, why were these two defenses selected? Will state-of-the-art backdoor defenses, e.g., [d], be effective against the proposed backdoor attack? Another concern is that defenses may easily spot the introduction of the codebook. It would be great if the authors could explain how to conceal the new block to make it less suspicious to the users. One potential possibility is that when the trained models are translated into some executable inference modules, the codebook will be harder to figure out. Please clarify. 

Minor:

- In Table 4, the time of EDT is 0.00. Does it mean that the time consumed is less than 0.01? 
- The authors claimed that training BadNets exceeds the attack budget. If possible, the exact budget and justification need to be clarified. 
- The zero-shot classification would also be interesting to be evaluated

### Questions
1. Clarify the missing important related works.
2. Clarify and justify the selection of baselines. 
3. Clarify the evaluation against defenses and potential mitigations.

### Soundness
2

### Presentation
2

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
This paper proposes a new threat model for backdoor attacks in large pre-trained models, stressing that training time attacks (backdoors) are impossible due to the lack of compute and training data. Therefore, they propose a new type of backdoor attack based on a training-free model editing technique (GRACE). Instead of adding an adaptor, as in GRACE, they directly manipulate patch embedding with a codebook with a backdoor functionality. They validate the proposed method on three tasks: image classification, image generation, and image captioning. The experiment results show that they have a good performance on four datasets: CIFAR-10, GTSRB, ImageNet-1k, MSCOCO (for captioning), and ImageNet-Sketch (for OOD generalization).

### Strengths
- The paper pointed out that existing training-time attack methods are impossible in the era of pre-trained large models as training data and significant computing are not available for most users.
- The paper exploits patch embedding, which is commonly used in image classification, image generation, and image captioning models. Therefore, the proposed method can work for three tasks.
- The paper contains educational values highlighting the need for new methods in adversarial machine learning research as modern machine learning is towards foundation models.

### Weaknesses
 - Although a new threat model (backdoor attack in large pre-trained models) is valid, the proposed method is not evidently an actual threat because there are assumptions that are not explicitly stated.
- This attack does not modify the model; the victim must use the model and backdoor logic hardcoded in the code. The paper assumes the victims do not read the code and use the backdoored model as it is to make the backdoor work.
- Usually, open models are used as base models, and most of the time, they are fine-tuned and customized according to the intended applications. In Appendix I, the fine-tuning defeats the proposed method to a 0% attack success rate.
- The paper does not propose the model editing technique. It is basically a specific version for GRACE. Therefore, contribution 2 seems a bit over-claimed. In addition, contributions 2, 3, and 4 are overlapped. Multiple triggers are a by-product of the GRACE editing technique using a codebook. I am not sure it stands as a new finding (contribution).

### Questions
- The definition of the backdoor should be re-defined. The traditional backdoors embed a hidden functionality in the model. The backdoor cannot be seen from the model or the code. If you put some additional rules in the code, this will be clearly seen by a user. Will it still be called backdoors? Please explicitly compare the proposed approach to traditional backdoors in terms of detectability and stealthiness. Given differences, please discuss whether the proposed attack is still qualified as backdoor or not.
- I recognize that the paper is a new application of GRACE for a backdoor functionality. However, it should be clearly distinguished between GRACE and this patch embedding manipulation with a codebook. Please provide a detailed comparison between the proposed approach and GRACE, highlighting the key differences and innovations in the proposed method.

### Minor Comments
- Figure 4 is a central figure and is referenced multiple times. But it is not easy to understand. I read GRACE (the previous model editing paper) to understand this paper. In Fig. 4 (Model Pipeline), the inputs and outputs are not clear, it looks like 3 inputs and 4 outputs. I do not understand what do you want to convey in the Code Book figure.
- Appendix I, I do not consider fine-tuning as adaptive attacks. The victims will fine-tune the model without knowing there is a backdoor in any way to adapt to downstream tasks.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper focuses on backdoor attacks against large pre-trained models. Specifically, the authors explore an efficient and data/training-free method to inject an editing-based codebook into the backdoor, thus altering the embeddings. Experiments across diverse architectures (like CLIP, BLIP, and ViT) and several downstream tasks are conducted.

### Strengths
1. This paper is generally well-written, with impressive illustrations to show the whole pipeline and motivations.
2. The motivation is clear, and the method design is also aligned with the motivation.
3. The experiments and analyses are comprehensive to demonstrate the effectiveness of the proposed method.

### Weaknesses
1. This paper merely discusses the possibility of the image-level backdoor attacks, leaving a blank for the text-level backdoor attacks.

2. More recent backdoor attack approaches [a, b] are not discussed and compared.

[a] BadCLIP: Trigger-Aware Prompt Learning for Backdoor Attacks on CLIP
[b] IMTM: Invisible Multi-trigger Multimodal Backdoor Attack

3. The setting for evaluation with defense mechanisms is vague.

### Questions
1. Can authors provide more explanations regarding the evaluation with defense mechanisms like the detailed setups?
2. Can the authors provide comparisons regarding the computational cost to conduct backdoor attacks with comparisons with previous methods?

### Soundness
3

### Presentation
3

### Contribution
2
