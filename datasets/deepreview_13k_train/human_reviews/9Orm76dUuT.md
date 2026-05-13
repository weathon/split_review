# Test-Time Backdoor Attacks on Multimodal Large Language Models

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
Backdoor attacks typically set up a backdoor by contaminating training data or modifying parameters before the model is deployed, such that a predetermined trigger can activate harmful effects during the test phase. Can we, however, carry out test-time backdoor attacks *after* deploying the model? In this work, we present **AnyDoor**, a test-time backdoor attack against multimodal large language models (MLLMs), without accessing training data or modifying parameters. In AnyDoor, the burden of *setting up* backdoors is assigned to the visual modality (better capacity but worse timeliness), while the textual modality is responsible for *activating* the backdoors (better timeliness but worse capacity). This decomposition takes advantage of the characteristics of different modalities, making attacking timing more controllable compared to directly applying adversarial attacks. We empirically validate the effectiveness of AnyDoor against popular MLLMs such as LLaVA-1.5, MiniGPT-4, InstructBLIP, and BLIP-2, and conduct extensive ablation studies. Notably, AnyDoor can dynamically change its backdoor trigger prompts and/or harmful effects, posing a new challenge for developing backdoor defenses.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores the possibility of implementing a backdoor attack during the testing phase. The paper proposes a type of backdoor attack called ``AnyDoor``, which does not require access to training data or modification of model parameters. In terms of experiments, the article focuses on multimodal language models and conducts extensive experiments on multiple models such as LLaVA, Mini-GPT4, BLIP.

### Strengths
- The experiments in the article are comprehensive, with experiments conducted on multiple multimodal large models. 
- The writing/presentation is good, and some of the visual explanations are quite clear. 
- The test-time backdoor researched in this article is quite interesting.

### Weaknesses
- The method section seems quite vague. After reading, I still do not understand the principle of backdoor injection during the test phrase. It seems that the article dedicates a large portion of its content to introducing the scenario and highlighting the differences from traditional scenarios in the methodology section.

- It seems that the article did not analyze the threat model. Who is the attacker during the testing phase? Who is the victim? What are the capabilities of the attacker? Where do these attacks take place, in which scenarios/platforms?

- The technical contribution of this article is minimal. Could you perhaps emphasize the technical contribution again? I believe that a certain level of technical contribution is necessary for a top-tier conference like this.

### Questions
- I suggest the author provide a detailed explanation of the method's principles and details, and explain why such a method is needed. 
- I also recommend that the author elaborate on the main contributions of the article. In my opinion, it seems that only a new scenario has been proposed. 
- For other suggestions, please refer to the "Limitations" section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a test-time backdoor attack method called AnyDoor, which employs adversarial noise on images alongside static triggers at the text level. Specifically, AnyDoor optimizes adversarial noise for the visual module and uses predefined textual triggers as supervisory signals. During inference, these text backdoor triggers activate the backdoor behavior. The effectiveness of the proposed method is evaluated across multiple model architectures.

### Strengths
- The research motivation is clearly articulated, and the writing is coherent.
- The exploration of backdoor attacks on multimodal large language models represents a novel research area.

### Weaknesses
- **Unclear Definition of Backdoor Attack:** The definition of the attack is ambiguous. The proposed method aligns more with adversarial attacks than with traditional backdoor attacks. Typically, a backdoor attack involves two key components: (1) Backdoor injection (through poisoning or weight/activation manipulation) and (2) Backdoor activation using a predefined trigger to control the model’s output target. The injection phase establishes a mapping between the trigger and a specific target label or response, allowing the attacker to control the model's output during inference. Based on the fundamental concept of backdoor attacks, I believe the proposed AnyDoor attack is more accurately classified as an adversarial attack rather than a backdoor attack. Therefore, the authors should clarify the differences between adversarial and backdoor attacks and explain the rationale for merging these concepts.

- **Limited Technical Innovation:** The core technique of the proposed method combines standard adversarial perturbations (for images) with specific string triggers (for text) to execute the attack. However, universal adversarial perturbations (UAPs) and token-level triggers (e.g., using static words like “sudo”) have already been extensively studied in existing literature [1][2][3]. As a result, the proposed attack does not introduce new insights or techniques for the backdoor research community. One interesting idea would be to explore jointly optimizing image perturbations and text triggers, which may lead to a more effective attack strategy.

- **Lack of a Defined Threat Model:** The paper does not clearly delineate the attack scenario or the attacker's capabilities. Without a defined threat model, readers may struggle to assess the relevance of the proposed attack in real-world situations and whether the attacker can successfully execute it under practical constraints.

- **Concerns about Attack’s Robustness:** The attack may be easily mitigated through preprocessing techniques at the image or text level. For example, defenders could use diffusion-based models to purify adversarial perturbations in images [4] or filter out special characters in text [5], effectively neutralizing the attack. The authors need to clarify the practical implications of their method and how it would withstand these potential defenses.

In summary, the proposed AnyDoor attack is more accurately classified as an adversarial attack rather than a backdoor attack, as it primarily relies on optimizing adversarial noise in images. In terms of methodology, the technical novelty is limited, and the attack could be easily countered by purification techniques such as diffusion models at the image level. Most critically, achieving target-specific attacks during test-time may not be transferable or universal, as adversarial noise needs to be optimized for specific targets, thereby limiting the method’s applicability in real-world scenarios.

[1] Adversarial Illusions in Multi-Modal Embeddings, USENIX Security, 2024  
[2] Towards adversarial attack on vision-language pre-training models, MM, 2022  
[3] Badnl: Backdoor attacks against nlp models with semantic-preserving improvements, ACSAC, 2021  
[4] Diffusion models for adversarial purification, ICML, 2022  
[5]  STRIP: a defence against trojan attacks on deep neural networks, ACSAC, 2019

### Questions
See weakness.

### Soundness
2

### Presentation
3

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
This paper presents AnyDoor, a test-time backdoor attack method targeting multimodal large language models (MLLMs). AnyDoor uses universal adversarial perturbations in the vision domain, combined with a text prompt, to activate harmful backdoor responses. The approach leverages the higher capacity of the vision modality to generate perturbations, while a short phrase in the language domain triggers the backdoor response in MLLMs. Unlike traditional data poisoning backdoor attacks, AnyDoor optimizes the backdoor trigger at test time, making it feasible for real-world applications. This novel approach reveals a new adversarial threat to MLLMs, with comprehensive evaluations demonstrating AnyDoor’s effectiveness.

### Strengths
- Optimizing the backdoor perturbation/trigger at test time is both novel and practical for MLLMs. Unlike data poisoning—which may be impractical in some settings—test-time optimization of the backdoor perturbation/trigger is a more realistic approach for real-world scenarios. This introduces a new form of adversarial threat for many MLLMs.

- In this threat model, the backdoor trigger is embedded in the text domain, while the image is also perturbed. The harmful backdoor response is activated only when both the image perturbation and text trigger are present, representing a unique and innovative threat model for MLLMs. The motivation behind this model is well illustrated in Figure 1.

- The thorough evaluations are appreciated, and the empirical results clearly demonstrate the proposed method’s effectiveness.

### Weaknesses
- Although not explicitly stated, AnyDoor appears to require gradient access for perturbation optimization, implying a white-box setting. This requirement could limit its practical applicability, as many MLLMs are deployed as services without granting gradient access to users. This restriction makes the attack challenging to execute in real-world.
- The results in Table 9 indicate limited black-box transferability. When using LLaVA-1.5 as the source model, it would be helpful to know if the attack transfers effectively to other models such as InstructBLIP or BLIP2. Further exploration of cross-model transferability could offer more insights into AnyDoor’s robustness in black-box scenarios.
- The paper lacks evaluations with adversarially trained models. It would be great to assess AnyDoor’s effectiveness on MLLMs that incorporate adversarial training, such as a LLaVA model with an adversarially trained image encoder, as discussed in RobustCLIP by Schlarmann et al. (2024) [1]. Such analysis would shed light on whether adversarial training enhances model resilience to AnyDoor.
- The current perturbations, such as Border and Corner attacks, are visually apparent and might be easily detected by human observers. Defenders could employ simple countermeasures, like cropping, to neutralize these fixed-location perturbations. It would be great to test if randomizing the perturbation locations retains the attack’s effectiveness. Additionally, the high perturbation budget of 32/255 for $L_\infty$ attack is noticeable. Including an ablation study with smaller perturbation budgets, such as 4/255, 8/255, and 16/255, could provide a better understanding of the trade-off between stealthiness and attack success.
- The paper has a few potentially misleading areas that would benefit from further clarification. Please refer to the questions section.

---

[1] Schlarmann, C., Singh, N. D., Croce, F., & Hein, M. Robust CLIP: Unsupervised Adversarial Fine-Tuning of Vision Embeddings for Robust Large Vision-Language Models. In Forty-first International Conference on Machine Learning.

### Questions
- Is AnyDoor assuming white-box access to the model? 
- Without the image perturbation, can the trigger text alone activate the harmful response?
- In lines 176 - 183, the explanation of greater capacity in the vision domain is clear. Regarding timeliness, the reviewer is confused by the statement in line 178, "attacking activation necessitates a modality with greater manipulating timeliness." Can authors further explain where is the trade-off? Planting the backdoor using data poisoning does not seem to incur any overheads, but AnyDoor requires optimization. 
- It is not clear what loss function $\mathcal{L}$ is used in Eq (2). It would be great if the author could further clarify. 
- For the "Contain" metric, does it only count all the target strings present in the response?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this study, the authors extend visual universal adversarial attacks, initially designed for image classification tasks, to large multi-modal models (MLLMs). Their method involves optimizing adversarial perturbations in conjunction with a predefined trigger token to elicit specific harmful responses from the models. The approach is tested on MLLMs including LLaVA-1.5, MiniGPT-4, InstructBLIP, and BLIP-2, demonstrating a notable success rate in the attacks. Additionally, the authors conduct several ablation studies to further analyze the method's effectiveness.

### Strengths
First, to the best of my knowledge, no prior work has explored attacks in this particular setting, combining adversarial perturbations on images with a triggering token.

Second, the draft is generally clear and easy to follow.

Third, the experimental evaluation includes a robust selection of state-of-the-art MLLMs.

### Weaknesses
First, given that existing approaches, such as Dong et al. (2023b), have already demonstrated that visual universal adversarial perturbations (UAPs) can be applied to MLLMs (potentially in a black-box setting as well), the technical novelty of this work appears somewhat limited, especially so given the limited transferability (see below).

Second, a critical area that requires substantial expansion is the study of the transferability of the proposed attack. While a paragraph on page 10 touches on this, much remains unexplored. For example, how effective is the attack in generating text that is semantically similar to the target response? If it is not effective, what do you believe could be the underlying reasons, and how would you propose to investigate this further? From a practical perspective, the lack of cross-model transferability significantly reduces the attack's relevance.

Third, aspects of the experimental evaluation could be improved. For instance, the rationale behind selecting certain types of adversarial attacks and the criteria for choosing and applying mitigation methods are not clearly explained (see below for specific examples).

The following are some detailed comments. 

Page 2: “It is important to note that adversarial attacks require tset = tact, which may be quite strict as it necessitates both manipulating capacity and timeliness.”

Comment: Do you mean it is more challenging to do or that it is not desirable for some reason? If it is the latter, kindly clarify why it is the case.

Table 5: “Table 5: Attack under common corruptions. The universal adversarial perturbations are generated using the border attack with b = 6.”

Commen: I found the experimental configuration rather under-specified here. Details are how the corruptions are applied are missing, which could greatly impact what the results are saying here. For instance, how do you crop? In the case of border attack, is the border retained somehow or it could be cropped? Furthermore, what about the effect on other types of attacks?

Page 10: “ For cross-model transfer attacks, manipulating the model’s output to align with a predetermined lengthy target string is unfeasible.”

Comment: What do you mean by “unfeasible”? Does it mean that you observed a low success rate? Kindly discuss the original results.

Page 10: “Therefore, we utilize caption evaluation metrics to assess the discrepancy between the model’s output with the introduction of a trigger into the input and the output of the original clean sample. This comparison reveals the sustained transfer attack potential of our AnyDoor attack, resulting in diminished model outputs.”

Comment: It is not unclear to me how to read these numbers in such a setting. In fact, I would say that it is hardly meaningful to make such a measurement.

### Questions
(1): What is your technical contribution that is in addition to existing approaches?

(2): How transferable are your attacks, across different models (models with different architecture or models that have gone through diferent finetuning).

### Soundness
3

### Presentation
3

### Contribution
2
