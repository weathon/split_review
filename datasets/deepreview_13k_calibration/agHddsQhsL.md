# Targeted Attack Improves Protection against Unauthorized Diffusion Customization

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
Diffusion models build a new milestone for image generation yet raising public concerns, for they can be fine-tuned on unauthorized images for customization. Protection based on adversarial attacks rises to encounter this unauthorized diffusion customization, by adding protective watermarks to images and poisoning diffusion models. However, current protection, leveraging untargeted attacks, does not appear to be effective enough. In this paper, we propose a simple yet effective improvement for the protection against unauthorized diffusion customization by introducing targeted attacks. We show that by carefully selecting the target, targeted attacks significantly outperform untargeted attacks in poisoning diffusion models and degrading the customization image quality. Extensive experiments validate the superiority of our method on two mainstream customization methods of diffusion models, compared to existing protections. To explain the surprising success of targeted attacks, we delve into the mechanism of attack-based protections and propose a hypothesis based on our observation, which enhances the comprehension of attack-based protections. To the best of our knowledge, we are the first to both reveal the vulnerability of diffusion models to targeted attacks and leverage targeted attacks to enhance protection against unauthorized diffusion customization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a targeted attack method for the protection against unauthorized diffusion customization. Extensive experiments validate the effectiveness of the targeted attack compared to other baselines. The paper also proposes an explanation for the effectiveness of targeted attacks.

### Strengths
1. The paper first proposes the targeted attacks for the protection against diffusion customization, and validates the effectiveness of targeted attacks.

2. The paper proposes an explanation for the superiority of targeted attacks, which may help understand attack-based protection.

3. The experiments on transferability and robustness also validate the effectiveness.

### Weaknesses
There are two main concerns.

1. Did the authors try some specifically purification methods for the protection? e.g., the method in [1]. Can the method purify the perturbations?

2. The authors may need to compare the added loss term alone in the ACE+ loss with the proposed ACE loss. The added loss in ACE+ is also targeted attack. Experimental comparisons are needed between it and the ACE loss.

### Questions
Please see the Weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes using targeted adversarial attacks to prevent unauthorized customized fine-tuning of LDM. The motivation is straightforward with a clear method design. The proposed ACE and ACE+ demonstrate a significant reduction in generation quality compared to baseline methods while maintaining an acceptable computational cost. The authors also conducted experiments to assess the robustness and transferability of ACE.

### Strengths
1. This is a well-written paper with solid experiments and analysis. The proposed ACE and ACE+ demonstrate superior performance against baseline methods.
2. The proposed method is straightforward and effective, with clear explanations for each step.

### Weaknesses
Given the detailed and solid experiments presented in this paper, I have no queries regarding the need for more ablation experiments. However, I do have concerns regarding the technical contributions and practical settings.

1. While this paper employs targeted adversarial attacks to prevent unauthorized customized fine-tuning, it is noted that this approach resembles Glaze [1], which also utilizes targeted style transfer to safeguard against style mimicry. Can you discuss the core difference between your technical contributions?

2. It is intriguing to investigate whether we should adopt ACE to all the protected images to achieve such protection results. What would be the impact on protection performance if the attacked ratio (the proportion of protected images) is reduced?

### Questions
My questions have been listed above. I'm willing to increase my score if my concerns are addressed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper discusses the use of targeted adversarial attacks to improve protection against unauthorized diffusion customization in image generation models. Traditional protections using untargeted attacks are not effective enough, so the authors propose a method called Attacking with Consistent score-function Errors (ACE). ACE significantly degrades the quality of customized images by introducing targeted errors, making unauthorized customization less viable. The paper validates ACE's effectiveness through extensive experiments and provides insights into the mechanisms of attack-based protections, setting a new benchmark in the field.

### Strengths
1. Relevant and timely topic  
2. Clear presentation of ideas  
3. Thorough evaluation

The authors address the important and timely topic of protecting diffusion models from unauthorized fine-tuning on specific images. To overcome limitations in existing approaches, they shift the focus from untargeted to targeted attacks, introducing a novel protection method called ACE. The authors provide a clear explanation of the design and rationale behind their method, which is commendable. Additionally, they conduct extensive evaluations that demonstrate the method's effectiveness. Overall, this paper is well-written and easy to follow.

### Weaknesses
 1. **Limited Technical Contribution**: The proposed method primarily relies on existing adversarial attacks, such as PGD, to mislead the model toward a predefined target. However, all of the techniques applied are directly taken from prior works, with minimal novel adaptation or extension.

2. **Lack of Evaluation on SD3**: The evaluations are conducted exclusively on SD versions 1.4, 1.5, and 2.1, which are somewhat outdated. Although testing on SD3 could provide valuable insights, it’s worth noting that SD3 is not open-source and lacks support for customization pipelines like LoRA or DreamBooth, which are central to this paper’s focus on protecting against unauthorized customization. Including a discussion of this limitation and potential future directions for adapting the method to newer models could strengthen the paper.

3. **Potential Bias in Selected Evaluation Images**: The authors selected images from two datasets to evaluate the performance of various customization and protection methods. However, it's unclear if these images were part of the original SD models’ training set, which could introduce bias. It would be helpful if the authors could clarify whether they verified that the selected images were not in the SD models’ training data. If verification wasn’t conducted, acknowledging this limitation would be beneficial.

4. **Additional Baseline for Comparison**: While the authors include several baselines, an important reference—**"Adversarial Perturbations Cannot Reliably Protect Artists from Generative AI"**—is missing. Including this work would allow for a more comprehensive comparison. Specifically, a discussion on how the proposed method compares to or improves upon the reliability and effectiveness of the techniques discussed in this paper would provide valuable context.

### Questions
1. Did the authors verify that the selected evaluation images were not part of the original SD models' training datasets to minimize potential bias? 

2. Please consider including the suggested work as an additional baseline for evaluating the proposed method.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper focuses on protecting images from being exploited by sota T2I diffusion models via adversarial perturbation. Different from previous works that mainly utilize untargeted attacks, this work points out an interesting and novel perspective that targeted attacks works better. The experimental results prove the method's effectiveness. The author also provides an insight to explain the success of targted attack: the attack can lead to model to learn more consistent chaotic patterns, and mitigate the neutralization effect of untargeted perturbation from multiple samples.

### Strengths
- The idea is simple and interesting, and the proposed method is easy to implement.

- The discovery that targeted attacks on diffusion-based mimicry works better than untargeted ones is novel and interesting.

- This paper is written in a clear way, and the logic of this paper is easy to follow.

- The performance reported in the paper demonstrates the effectiveness of the proposed technique.

- This paper tries to provide some insights to explain the underlying reason of why targeted attacks works better than untargeted attacks. The reasons and explanations are intuitive and reasonable.

### Weaknesses
My concerns mainly lie in the experimental evaluation part of the paper. The authors seem to be not closely following the recent advances in adversarial attacks & defenses for protection against diffusion-driven mimicry/editting.

- Lack of recent attack baselines (in 2024) for comparison in the experiments, such as SDS, MetaCloak, Influence Watermarks, etc. Specifically, the absence of a comparison against SDS, which leverages score distillation for efficient protection, is a notable gap. Furthermore, MetaCloak's focus on robustness against transformations, particularly Gaussian noise, makes it a relevant baseline that should be considered. The lack of comparison against Influence Watermarks, which directly targets the personalization process, is also a significant omission.

- The paper only focuses on latent diffusion models, while other models such as diffusion transformers are not evaluated. I suggest to conduct more experiments on state-of-the-art DiT models. Although they might not be tailored for personalization, some of them can be easily adopted for image editting tasks. The evaluation should include a range of DiT architectures to assess the generalizability of the proposed method across different diffusion model families.

- The purification experiments does not include any purification methods specifically designed for diffusion mimicry, such as IMPRESS [1], GrIDPure [2], etc. The evaluation should include a more comprehensive set of purification techniques, especially those designed to counteract adversarial perturbations in diffusion models, to provide a more robust assessment of the proposed method's resilience. The absence of these specific purification methods raises concerns about the practical applicability of the proposed approach in real-world scenarios.

- I also have a concern on the superiority of targeted attacks claimed in this paper. In the analyses part (Section 5), the main idea is that as targeted attacks can lead to model to learn more consistent chaotic patterns, they mitigate the neutralization effect of untargeted perturbation from multiple samples. However, for image editting tasks and some state-of-the-art personalization methods, only one reference image is involved, and the above "neutralization effect" will not neccessarily happen. How can the hypotheses in Section 5 explain the empirical success of targeted attacks in these settings?

Minor Points:

- The claim in L144 that all existing protection are untargeted attacks is not accurate. For example, Glaze should be classified as a targeted attack. ASPL also proposes a targeted attack version.

- The description in L500 seems wrong. $\theta^{\prime}$ should be the customized diffusion model.

### Questions
- In algorithm 1 Line 5-7, why are you optimizing the diffusion model parameters as well? Seems that these details are not included in Eq. (4)-(5).

- In table 1, what are the budgets of the baselines? Are they 4/255 or aligned with their own settings?

### Soundness
3

### Presentation
3

### Contribution
3
