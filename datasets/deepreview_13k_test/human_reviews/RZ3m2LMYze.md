# Representation Confusion: Towards Representation Backdoor on CLIP via Concept Activation

- Decision: Reject
- Scores: 5, 5, 3, 5

## Abstract
Backdoor attacks pose a significant threat to deep learning models, allowing attackers to stealthily embed hidden triggers that can be exploited during inference. Traditional backdoor attacks typically rely on inserting external patches or perturbations into input data as triggers. However, two key challenges remain, i.e., how to evade detection by defense mechanisms and reduce the computational cost of trigger insertion. To address these challenges and design more advanced backdoor techniques, we first explore the underlying mechanisms of backdoor attacks through the lens of cognitive neuroscience, drawing parallels between model decision-making and human cognitive processes. We conceptualize the decision process elicited by the backdoor-triggering as movement between representation spaces (i.e., learned concepts). Thus, existing methods can be seen as implicit manipulations of these stored concepts. This raises a key question: \textit{Why not manipulate the concept explicitly? Could the inherent concepts in the model's reasoning serve as an ``internal trigger'' for the backdoor?} Motivated by this, we propose a novel backdoor attack framework, namely Representation Confusion (RepConfAttack), which explicitly manipulates concepts within the model's representation spaces. This approach eliminates the need for backdoor triggers and enhances stealthness by making the attack harder to detect with traditional defenses. Experimental results demonstrate the effectiveness of our method, achieving high attack success rates even against robust defense mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes an interesting "concept-based" backdoor attack where backdoor poisoning images are labeled following the concept score from explainable AI tools. In particular, if the concept vector or a given image is larger than a pre-defined threshold, the label of the given image will be changed to the target label. After training on the poisoned data set, images with an "internal trigger" (i.e., concept vector larger than the threshold) will be wrongly classified as the target class. The authors also motivate the design choice with the cognitive neuroscience theory. The proposed attack is claimed to be stealthy against existing baseline defenses.

### Strengths
This paper is well-structured, with detailed explanations and a background provided to support each step of the attack design. The authors share an interesting observation that the "concept activation" is the driving force behind the backdoor attacks. Extensive experiments are also provided to validate the proposed attack's effectiveness, where the attack is especially effective against backdoor defenses.

### Weaknesses
- This attack jumps out of the regular threat model where an adversary puts the trigger on test samples during inference to manipulate the predictions. This change makes the backdoor attack more stealthy since there is no need to add external triggers during the test. However, it also brings a question about how to implement it in practice when the adversary needs to change the prediction on a certain target images. For example, the concept vector threshold of the target image is indeed lower than the pre-defined value. Is there a feasible way to increase the value to trigger the backdoored model? One possible solution is to deliberately change the concept vector score of the target image. It would be great if the authors could clarify this point.  

- Related to the question above, if the adversary manages to change the concept vector score, the proposed method is similar to a regular backdoor-triggered sample. In this case, how reliable is the concept score? Taking the results of table 2 also into consideration, when does the proposed attack fail, and is it caused by the concept score calculation? In addition, can the same strategy be used in feature space for random statistics instead of calculating the concept vector score?

- Adaptive defenses. One major advantage of the proposed attack is that it can resist backdoor defense. Regarding the working mechanism of the previous defense, it is non-surprise that previous defenses do not work for the proposed attack. For example, ShrinkPad must inspect the difference between clean and triggered images. The proposed attack is somehow unrelated to ShrinkPad since the triggered inputs do not include substantial patterns. Given the existing defenses, would an adaptive defense that considers the proposed attack mechanism easily filter the proposed backdoor attack? It would be great if the authors could clarify this point.

Minor: 
Line 219, bold -> green.
The font size in Figure 4 is too small.

### Questions
Please clarify about triggering on a randomly selected test image, the reliability of the concept score, and adaptive defenses.

### Soundness
2

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
5

### Summary
This paper presents RepConfAttack, a backdoor attack framework that exploits internal concept representations within CLIP models instead of traditional external triggers, drawing inspiration from cognitive neuroscience. The method achieves high attack success rates while maintaining clean performance across multiple datasets.

### Strengths
- First to apply the Hopfieldian view from cognitive neuroscience to explain backdoor attack mechanisms.
- Proposes a novel concept representation-based backdoor attack method (RepConfAttack) without requiring external triggers

### Weaknesses
- Only validated on image classification tasks downstream of CLIP, leaving other potential tasks unexplored
- Claims to target CLIP but lacks comparison with representative CLIP-specific attacks like BadCLIP, which weakens the comparative analysis
- Insufficient justification for concept selection threshold (σ) choice
- Limited sensitivity analysis on poisoning rate
- No validation on larger-scale datasets, such as ImageNet

### Questions
- How to select optimal trigger concepts? Are certain concepts inherently more suitable as triggers?
- Have you considered using combinations of multiple concepts as triggers?
- Can this method be extended to other types of multimodal models?
- How does the method perform on larger-scale datasets?

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
3

### Summary
This paper addresses the evolving threat of backdoor attacks in deep learning models, where hidden triggers can be covertly embedded to control model behavior at inference. Traditional attacks use external patches or perturbations as triggers, but they often face two challenges: detection by defense mechanisms and high computational costs. To overcome these, the authors draw inspiration from cognitive neuroscience, comparing model decision-making to human cognition and proposing a new approach that manipulates internal representations directly. The proposed framework, called Representation Confusion Attack (RepConfAttack), bypasses the need for external triggers by modifying inherent concepts within the model’s representation spaces. This approach enhances stealth, making the attack less detectable by standard defenses. Experimental results show that RepConfAttack is effective, achieving high success rates even against strong defenses, suggesting a novel and advanced method for conducting undetectable backdoor attacks.

### Strengths
1. The paper addresses a timely and important topic, focusing the security of self-supervised learning (SSL) models against backdoor attacks. The proposed RepConfAttack introduces a novel approach that leverages cognitive science to manipulate internal representations, enhancing stealth and evading detection.

2. The findings are inspiring, and the perspective using cognitive science adds an interesting dimension.

### Weaknesses
1. The novelty of the proposed attack lies in leveraging naturally existing concepts in the dataset, which seems similar to the existing work by Wenger et al. (NeurIPS '22). Could the authors clarify the specific technical differences from [1]?

2. While the use of cognitive science to explain the backdoor attack is intriguing, the connection feels tenuous and lacks strong motivation. First, the cognitive science aspects are described mostly in natural language without much technical depth or formalization. Second, the cognitive science section seems unnecessary, as the proposed Confusion Attack can be fully understood by reading Section 4.3 alone.

3. The practicality of the proposed attack raises some concerns. For example, if "water" is chosen as the target concept, does the attack only succeed when "water" is present in the image? How does the attack perform when this concept is absent? Traditional backdoor attacks can always succeed by injecting a trigger, ensuring consistent success.

4. Concept set size: What is the typical size of the concept set in the experiments? Additionally, how does the size of the concept set affect the performance of the proposed method?

5. Determination of threshold $\sigma$: How is $\sigma$ determined in the experiments, and how sensitive is the performance of the proposed method to variations in $\sigma$

6. The paper misses some backdoor defense strategies specifically designed for SSL, such as SSL-Cleanse[2] and DECREE[3]. 
Discussing how RepConfAttack could potentially evade these defenses would strengthen the paper's security analysis.


[1] Wenger et al., Finding Naturally-Occurring Physical Backdoors in Image Datasets, NeurIPS '22.

[2] Zheng et al., SSL-Cleanse: Trojan Detection and Mitigation in Self-Supervised Learning, ECCV '24.

[3] Feng et al., Detecting Backdoors in Pre-trained Encoders, CVPR '23.

### Questions
Please respond to each weakness mentioned above.

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
4

### Summary
The paper proposes a novel backdoor attack framework called Representation Confusion Attack (RepConfAttack), which explicitly manipulate the concepts and eliminates the need for backdoor triggers.

### Strengths
1. **Novel Motivation**: The motivation behind using cognitive neuroscience, particularly the Hopfieldian perspective, to conceptualize backdoor attacks is innovative. This unique view allows the paper to frame backdoor manipulation in a new and insightful way.
2. **Comprehensive Experiments**: The authors conducted extensive experiments on different datasets and multiple CLIP variants. The results demonstrate the effectiveness of the proposed attack in terms of high attack success rate and high clean accuracy.

### Weaknesses
1. **Motivation Complexity**: The motivation for relating backdoor attacks to cognitive neuroscience is somewhat complex and could be difficult for readers unfamiliar with the field. While the Hopfieldian view provides an interesting perspective, its necessity in the context of backdoor attacks on neural networks is not entirely clear. More emphasis could have been given to explain why this specific perspective is crucial for the proposed attack mechanism.

2. **Novelty of the method**: While this work provides a novel perspective on the success of backdoor attacks, the method itself is not entirely new. It closely resembles traditional backdoor attacks, specifically those categorized as physical attacks [1]. From this standpoint, the contribution of this work remains unclear.

3. **Method Generality**: The paper specifically targets image classification tasks on CLIP models, and it is unclear whether the proposed method can be effectively extended to other tasks, such as multimodal contrastive models. Additionally, it is not evident why the authors chose to use the CLIP visual encoder without utilizing the CLIP text encoder. Could the authors clarify the reasoning behind this choice?

4. **Experiment Limitations**:  I find the experimental setup to be inadequate, particularly regarding the choice of dataset and attack method. When utilizing CLIP models, why not employ datasets specifically designed for them, such as CC3M, ImageNet, or Caltech-101? Furthermore, the attack methods compared are primarily intended for smaller models and are somewhat outdated. It would be more appropriate to compare against state-of-the-art attacks specifically developed for CLIP models.

5. **Defense Limitations**: The defense methods examined in this paper are also outdated, largely stemming from 2021. The only detection method from 2023 relies on image-based techniques, which are insufficient against the proposed attack. It would be advantageous to investigate more advanced defense strategies. Additionally, I believe the method presented in this article may not withstand the most sophisticated defense and detection techniques that assess whether the modalities are aligned [2][3].

[1] Backdoor Attacks Against Deep Learning Systems in the Physical World.

[2] VDC: Versatile Data Cleanser based on Visual-Linguistic Inconsistency by Multimodal Large Language Models.

[3] Robust contrastive language-image pretraining against data poisoning and backdoor attacks.

### Questions
1. What is the differrence between this work and physical backdoor attacks?
2. why the authors chose to use the CLIP visual encoder without utilizing the CLIP text encoder, while "CLIP" appears in the title of the paper?

### Soundness
2

### Presentation
2

### Contribution
2
