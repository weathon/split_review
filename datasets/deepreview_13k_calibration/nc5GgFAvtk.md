# An Image Is Worth 1000 Lies: Transferability of Adversarial Images across Prompts on Vision-Language Models

- Decision: Accept
- Avg Score: 6.80
- Scores: 6, 8, 6, 8, 6

## Abstract
Different from traditional task-specific vision models, recent large VLMs can readily adapt to different vision tasks by simply using different textual instructions, i.e., prompts. However, a well-known concern about traditional task-specific vision models is that they can be misled by imperceptible adversarial perturbations. Furthermore, the concern is exacerbated by the phenomenon that the same adversarial perturbations can fool different task-specific models. Given that VLMs rely on prompts to adapt to different tasks, an intriguing question emerges: Can a single adversarial image mislead all predictions of VLMs when a thousand different prompts are given? This question essentially introduces a novel perspective on adversarial transferability: cross-prompt adversarial transferability. In this work, we propose the Cross-Prompt Attack (CroPA). This proposed method updates the visual adversarial perturbation with learnable textual prompts, which are designed to counteract the misleading effects of the adversarial image. By doing this, CroPA significantly improves the transferability of adversarial examples across prompts. Extensive experiments are conducted to verify the strong cross-prompt adversarial transferability of CroPA with prevalent VLMs including Flamingo, BLIP-2, and InstructBLIP in various different tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a method called Cross-Prompt Attack (CroPA) that creates adversarial images, destined for vision-language models (VLMs), that transfer across prompts.  They train on multiple prompts using a variant of projected gradient descent to learn both the image perturbation and the text embedding perturbation. They consider both the targeted and non-targeted scenarios. CroPA achieves better coss-prompt transferability compared to baseline methods when evaluated with OpenFlamingo-9B, BLIP-2, and InstructBLIP on different tasks.

### Strengths
- The paper introduces an aspect of adversarial transferability that was not emphasized before. The problem that the paper tries to address is clearly formulated and is worth investigating.  
- The experimental setup covers a wide range of scenarios: targeted and non-targeted attacks, multiple VLMs (OpenFlamingo-9B, BLIP-2,InstructBLIP) and different multi-modal tasks (VQA, classification, captioning). The baselines are strong.

### Weaknesses
 - The method does not achieve transferability across models or images in addition to cross-prompt transferability. This might limit  its practical applicability.  

- Clarifications are required in some parts of the paper. Certain statements about the “textual prompts” are misleading. For example, in the abstract, the method is described as follows:  “This proposed method updates the visual adversarial perturbation with learnable textual prompts”. This might suggest that the method directly modifies the textual prompts or discrete prompt tokens whereas it is actually modifying the embedding of these textual prompts. Moreover, the authors should explicitly state the underlying optimization algorithm (is it projected gradient descent?) , the norm (is it L-infinity ?) and the selected value of the perturbation size for easier comparison with related work.

Minor issues: there are some typos in the paper (for example in the conclusion “baseline approaches only archive” -> “achieve”).

### Questions
- This is a clarification question. Do you only add the prompt perturbations during the optimization phase or do you also add them during evaluation?

- What is the ASR of Multi-P when transferred across models or images?

- Do you have a conjecture regarding the inability of CroPA to achieve transferability across models or images?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies a novel perspective on adversarial transferability in the context of Vision and Language Models (VLM). In particular, it explores the problem of learning for adversarial visual patterns that can seamlessly traverse various textual prompts. The author introduces the method of a cross-prompt attack, akin to the principles of Generative Adversarial Networks (GANs), where the goal is to simultaneously learn visual perturbations and prompt perturbations with opposing objectives. Through compelling demonstrations, the study reveals that this competitive process significantly enhances the visual perturbation's ability to traverse different prompts effectively.

### Strengths
The problem being studied (cross-prompt adversarial transferability) and the proposed method seems very novel to me, and the author performed extensive experiments to validate the strength of the proposed method. I am convinced that this paper will provide valuable insights and knowledge to the research community.

### Weaknesses
I don’t see a major weakness, but have some suggestions for the naming. The term "prompt perturbation" initially appears a bit confusing, as it implies an intention to deceive the model (as it’s commonly used for adversarial “attach” rather than “defense”), which is not the case in this paper. Instead, it’s used in an opposite direction other than image perturbation to encourage stronger cross-prompt transferability during this competitive update process. I would recommend that the author consider selecting a more fitting name.

### Questions
How does the proposed method work for the longer prompt? Does the transferability still hold?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper aims to generate a single adversarial image capable of misleading all predictions made by VLMs, regardless of the input prompts. To accomplish this objective, it introduces a Cross-Prompt Attack, characterized by a minimax optimization process involving image perturbations and learnable textual prompts. Extensive experiments have validated that, in a white-box setting, the proposed attack scheme can outperform other attack methods.

### Strengths
1. The proposed method intuitively makes sense and consistently outperforms other baseline attack schemes in extensive experiments.

2. The paper is well-written and easy to follow.

### Weaknesses
1. The primary concern for this paper is whether the proposed attack can indeed raise significant security issues. For instance, when considering the exemplary target prompts in Table 1, they have the potential to disrupt the functionality of VLMs, but it remains unclear how they may pose security risks in real-world applications. This security concern would be more valid if the attack successfully tricks VLMs into producing contradictory predictions or harmful instructions. Otherwise, the objective of this study appears to be more like a pioneering exploration of VLMs' adversarial robustness.

2. The author mentions another potential use case for the proposed framework, which is to "prevent malicious usage of large VLMs for unauthorized extraction of sensitive information from personal images." If this is indeed the case, the proposed method should also be assessed in a black-box setting, as users' VLMs cannot be known in advance. However, this set of experiments is absent from the paper. Previous jailbreaking attacks aimed at emerging large language models have shown substantial transferability across models [1]. I am curious whether this holds true for various VLMs as well.

3. I am curious whether some straightforward defense techniques can defeat the proposed attack, such as incorporating data augmentation on the input images [2]. This could provide insights into whether the optimized adversarial perturbation converges to an unstable local minimum and can be easily defended against.

### Questions
In addition to the concerns in the weakness section, I also have the following question:

Is the improvement achieved by the proposed Cross-Prompt Attack over Multi-P due to the increased number of textual prompts generated through perturbations during minimax optimization? One approach to achieve a similar effect is to utilize another language model to rephrase the text prompts into new ones, thus serving as data augmentation.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes the Cross-Prompt Attack (CroPA) that generalizes the pixel-space image perturbation for multiple prompts. The authors propose to optimize learnable textual prompts in the opposite direction of the pixel-space adversarial perturbation for transferability. Evaluations on small-scale VLMs showed that CroPA was effective in fooling the target model, and the pixel-space perturbations are transferable across multiple types of prompts.

### Strengths
1. The paper is well-written and well-presented. The motivations are sufficiently reasonable to motivate the framework.

2. The idea of jointly optimizing pixel-space perturbation and text-space perturbation is novel.

3. The evaluations include multiple kinds of VLM paradigms with several major language tasks, which are comprehensive.

### Weaknesses
1. The paper assumes the white-box access for VLMs, which enables the framework to have backward gradients to update in multimodal input space. However, this assumption may not be generalized to all mainstream VLMs as they are fast scaling up. For instance, the authors evaluated the effectiveness of OpenFlamingo-9B and InstructBLIP, whose LLM component is not of large-scale. The applicability of CroPA on large-scale VLMs (e.g., those embedded with LLaMA-65B) or black-box VLMs (e.g., GPT4-V) remains challenging. Specifically, the computational cost of backpropagating through large language models for adversarial attacks is substantial, and the paper does not adequately address this scalability issue. The reliance on white-box access also limits its practical relevance, as many state-of-the-art VLMs are deployed as black-box APIs.

2. The framework learns adversarial prompts to enhance the attack's effectiveness. However, very few text prompt instances are shown in the paper, and the quality of the result text prompts is not sufficiently evaluated. The paper only mentions that the prompt embeddings are optimized, but it does not provide any analysis of the semantic coherence or the syntactic structure of these optimized prompts. Without a qualitative analysis of the generated prompts, it is difficult to assess the validity of the approach and whether the learned prompts are actually meaningful or just random noise in the embedding space.

3. Existing adversarial attacks on VLM [1] have adopted query-based techniques to enhance the attack effectiveness. What's more, this baseline only assumes the black-box access to the VLMs, which more are generalizable. The paper should show sufficient validity or advantages (e.g., ASR, Convergence, etc.) of CroPA over existing baselines. The paper needs to provide a more comprehensive comparison with query-based black-box attacks, particularly in terms of query efficiency and attack success rate. A direct comparison of the performance of CroPA against established black-box methods is necessary to demonstrate the practical advantage of the proposed approach. The lack of such a comparison makes it difficult to assess the true contribution of CroPA.

4. Please fix the typo "leanable" in the introduction (page 2).

### Questions
1. Please address my concerns stated in the weakness section. Given the current status of the paper, I appreciate the problem novelty to rate it as borderline acceptance. However, the authors' responses shall address the weakness mentioned above. I look forward to further discussion and I will consider revising the rating based on the soundness of the response.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes the Cross-Prompt Attack (CroPA). This proposed method updates the visual adversarial perturbation with learnable textual prompts, which are designed to counteract the misleading effects of the adversarial image. By doing this, CroPA improves the transferability of adversarial examples across prompts.

### Strengths
The experiments have shown the cross-prompt transferability created with a single prompt is highly limited. An intuitive approach to increase the cross-prompt transferability is to use multiple prompts during its creation stage. However, the improvement in cross-prompt transferability of these baseline approaches converges quickly with the increase in prompts. CroPA further improve the cross-prompt transferability. 

It creates more transferable adversarial images by utilising the learnable textual prompts. The learnable textual prompts are optimised
in the opposite direction of the adversarial image to cover more prompt embedding space. 

To explore the underlying reasons for the better performance of CroPA compared to the baseline approach, it visualises the sentence embedding of the original prompt and perturbated prompts by CroPA, which is obtained by the averaging embedding of each token. The visualisation of difference in the prompt embedding coverage explains the reason why the CroPA methods can outperform the baseline approach even if the number of prompts used in optimisation is less than the baseline approach.

It experiments with different settings or policies. For example, it explores the effect of different update strategies. It tests the ASRs of the image adversarial examples with the number of in-context learning examples.

### Weaknesses
The technical contribution may be limited. The optimization method is general to use gradients for updating the adversarial perturbations. This optimization method is widely adopted in adversarial attacks.  It is very similar to adversarial training. To achieve cross prompt transferability, it perturbs the prompts without limitations to maximize the loss and obtain the worst prompt, then it trains the image perturbations based on the worst prompts and the final obtained perturbation can fool the model for different prompts because it already deals with the worst prompts. The novelty may be limited.

I am still not very clear about some experiment settings. For example, what is the value of perturbation size $\epsilon$? Larger $\epsilon$ usually means stronger attacks. So what is the performance with a different $\epsilon$?

It seems that the generated perturbations are used to test for the same model that it was trained. Can the generated perturbations be transferred to other VLMs and what are the performance? It is better to discuss the transferability to demonstrate the generalization of the method.

For the non-targeted attack after equation (2), the optimisation is expressed to maximize over token and minimize over image. It is almost the same as the targeted attack. I am wondering if there is a mistake here and it should be to maximize over image to make the results of adversarial examples different from the original one. Minimizing over images and the final image perturbation would make the outputs of adversarial examples similar to clean images. It is better to provide more details about this non-targeted attack. I agree that by maximizing the tokens, the generated tokens can mislead the VLM, but here we focus on image perturbations and use the image perturbation to test the VLM, right?

### Questions
see the weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
