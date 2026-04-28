# Robust Backdoor Attack with Visible, Semantic, Sample-specific and Compatible Triggers

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Deep neural networks (DNNs) can be manipulated to exhibit specific behaviors when exposed to specific trigger patterns, without affecting their performance on benign samples, dubbed \textit{backdoor attack}. Currently, implementing backdoor attacks in physical scenarios still faces significant challenges. Physical attacks are labor-intensive and time-consuming, and the triggers are selected in a manual and heuristic way. Moreover, expanding digital attacks to physical scenarios faces many challenges due to their sensitivity to visual distortions and the absence of counterparts in the real world. To address these challenges, we define a novel trigger called the \textbf{V}isible, \textbf{S}emantic, \textbf{S}ample-specific, and \textbf{C}ompatible (VSSC) trigger, to achieve effective, stealthy and robust simultaneously, which can also be effectively deployed in the physical scenario using corresponding objects. To implement the VSSC trigger, we propose an automated pipeline comprising three modules: a trigger selection module that systematically identifies suitable triggers leveraging large language models, a trigger insertion module that employs generative models to seamlessly integrate triggers into images, and a quality assessment module that ensures the natural and successful insertion of triggers through vision-language models. Extensive experimental results and analysis validate the effectiveness, stealthiness, and robustness of the VSSC trigger. It can not only maintain robustness under visual distortions but also demonstrates strong practicality in the physical scenario. We hope the proposed VSSC trigger and implementation approach could inspire future studies on designing more practical triggers in backdoor attacks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors observe that existing backdoor attacks are not robust to visual distortions like Gaussian blurring or changes in environmental conditions, which could hinder their practical application. 

To mitigate this issue, the paper introduces the concept of a Visible, Semantic, Sample-Specific, and Compatible (VSSC) trigger. The development of the VSSC trigger leverages large language models to select an appropriate trigger, and harnesses text-guided image editing methods to embed the trigger into the poisoned image seamlessly.

The authors demonstrate the VSSC trigger’s performance through rigorous experimentation, showing that it not only retains the stealth required for a successful backdoor attack but also exhibits an enhanced resistance to visual distortions, surpassing the robustness of most existing digital backdoor attacks. Furthermore, the VSSC trigger offers a more effective and adaptable integration approach compared to traditional physical backdoor attacks.

### Strengths
- I think the proposed attack is interesting and inspiring. It might makes backdoor detection more challenging.
- The presentation is motivating and easy to follow.

### Weaknesses
 - The first 5 page writing is great, but the latter evaluation part does not support the claims well. The trigger generation in Design and Evaluation do not match.

 - In Section 4.2 Stage 1, the paper said LLM are used to automatically select text trigger. But this part is not mentioned in the evaluation. Could the author explain it in detail? How are the evaluated triggers selected?

 - For Table 3 and Table 4, I am not clear why the lowest ACC is highlighted. Isn't that an effective backdoor attack should have a high ACC (and a high ASR at the same time)?

 - Also, from Table 3 and Table 4, I am not convinced that the proposed method is better than baselines. Many bold values are from baselines. This does not align with corresponding text explanation in the paper. Could the author explain it in detail?

 - Minor. In Section 4.2, the algorithm will be more clear and precise if the author can use a pseudo-code, rather than natural language. Also, some adopted techniques are just a reference (like image editing and dense caption). It would be better to provide brief description for better reading experience.

### Questions
1. In Section 4.2 Stage 1, the paper said LLM are used to automatically select text trigger. But this part is not mentioned in the evaluation. Could the author explain it in detail? How are the evaluated triggers selected?

2. For Table 3 and Table 4, I am not clear why the lowest ACC is highlighted. Isn't that an effective backdoor attack should have a high ACC (and a high ASR at the same time)?

3. Also, from Table 3 and Table 4, I am not convinced that the proposed method is better than baselines. Many bold values are from baselines. This does not align with corresponding text explanation in the paper. Could the author explain it in detail?

4. Minor. In Section 4.2, the algorithm will be more clear and precise if the author can use a pseudo-code, rather than natural language. Also, some adopted techniques are just a reference (like image editing and dense caption). It would be better to provide brief description for better reading experience.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an approach to designing backdoor attacks by  leveraging large models (diffusion model and large language model) that are highly effective and robust against visual distortions.
The authors highlight the limitations of existing backdoor attacks, particularly their susceptibility to visual distortions during inference. To address this issue, they propose the use of VSSC triggers that are both effective and resilient to visual distortions. These triggers are designed to have a significant magnitude, increase detection complexity, have semantic meaning, and blend seamlessly with the image content. The authors propose a novel approach to implement VSSC triggers using large language models and text-guided image editing techniques. Extensive experiments validate the effectiveness, stealthiness, and robustness of the VSSC triggers, showcasing their superiority compared to state-of-the-art backdoor attacks. The paper also highlights the advantages of the proposed method in both digital and physical spaces.

### Strengths
1. The paper utilizes a large language model to autonomously determine the objects to be introduced into the images and subsequently employs a diffusion model for inpainting. This approach can be seen as an evolved version of prior physical attacks, such as the one outlined in [1], where the selection of glasses is manually determined by humans.

2. The proposed method is capable of successfully executing an attack with a modest poisoning ratio of 5%.

[1] Chen, Xinyun, et al. "Targeted backdoor attacks on deep learning systems using data poisoning." arXiv preprint arXiv:1712.05526 (2017).

### Weaknesses
1. The performance of the proposed method is not very impressive. For instance, in Table 3,4,9, several baseline methods outperform the proposed approach.

2. The analysis of robustness to distortion is somewhat limited, considering only the impact of blurring, compression, and noise. Other physical attack papers, such as [1], take into account additional distortions like transformations, shrinking, and padding. These should be discussed as well.

3. An ablation study discussing the influence of the poisoning ratio should be included.

### Questions
1. If the trigger objects proposed by the Large Language Model (LLM) belong to another class from the training dataset, it could potentially lead to undesirable outcomes, such as misclassification or confusion in the model's predictions. Should the model avoid letting this happen? How  the model avoid letting this happen?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A robust backdoor attack with a visible, semantic, sample-specific, and compatible (VSSC) trigger is proposed. Extensive evaluations have been conducted to show the effectiveness of VSSC and its resistance to various defenses.

### Strengths
* The proposed trigger has been evaluated on various datasets and compared with many existing works.

### Weaknesses
 * The depth of the work is insufficient and the contribution is limited.

The VSSC trigger proposed in the paper is essentially a 'physical' trigger generated digitally. Similar attacks have been proposed in one of the seminal works of backdoor [1]. It is a well-known fact that poisoning the training data with only tens of images of a face wearing a pair of sunglasses can lead to a high attack success rate. Note that the poisoning in [1] uses a weak blended trigger -- directly using real photos for poisoning should require an even lower poisoning ratio.

Besides, the proposed method for the generation of the trigger seems unnecessary in practice (with other concerns in the sequel). Training a generative model is costly while using open-sourced models will limit the application domain (based on the ASR vs PR curves in Figure 6). For instance, it's unlikely that a general-purpose model like Stable Diffusion could generate a realistic-looking tumor in a medical image or handle hyperspectral imagery (HSI) without specific fine-tuning, which would be very costly. Unfortunately, this work has limited contribution due to a lack of additional intellectual merit.

[1] Chen et al, Targeted backdoor attacks on deep learning systems using data poisoning, 2017.

* The methodology needs more consideration.

The reasoning behind the trigger assessment method lacks clarity. There is no evidence showing that models will outperform humans in recognizing the injected trigger objects. It is also unclear why the trigger will be learned if it is recognizable by an object detector. The entire pipeline appears to be heuristic.

* The performance gain of the proposed method over existing ones is marginal.

Also, the poisoning ratio of the proposed trigger is very large.

* Omission of existing works.

The generative model in the proposed work is not state-of-the-art (see [2]). Visible sample-specific triggers have been studied by an early defense in [3].

[2] Liu et al, Cones: Concept Neurons in Diffusion Models for Customized Generation, 2023.
[3] Xiang et al, Revealing perceptible backdoors in DNNs, without the training set, via the maximum achievable misclassification fraction statistic, 2020.

### Questions
See the weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
