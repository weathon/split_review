# Seeing Through the Mask: Rethinking Adversarial Examples for CAPTCHAs

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 1, 5

## Abstract
Modern CAPTCHAs rely heavily on vision tasks that are supposedly hard for computers but easy for humans. However, advances in image recognition models pose a significant threat to such CAPTCHAs. These models can easily be fooled by generating some well-hidden "random" noise and adding it to the image, or hiding objects in the image. However, these methods are model-specific and thus can not aid CAPTCHAs in fooling all models. We show in this work that by allowing for more significant changes to the images while preserving the semantic information and keeping it solvable by humans, we can fool many state-of-the-art models. Specifically, we demonstrate that by adding masks of various intensities the Accuracy @ 1 (Acc@1) drops by more than 50\%-points for all models, and supposedly robust models such as vision transformers see an Acc@1 drop of 80\%-points. 
    These masks can therefore effectively fool modern image classifiers, thus showing that machines have not caught up with humans -- yet.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the problem of CAPTCHA fooling all models with adversarial samples. The paper defines four masks including "Circle", "Diamond", "Square" and "Knit", and applies these masks to the images at various intensities. The experiments are conducted on the constructed datasets using four masks, and the drop in Acc@1 and Acc@5 accuracy are calculated.

### Strengths
The paper proposes more aggressive perturbations to apply to images, as the limit is not imperceptibility bu rather semantic preservation for humans in CAPTCHA.

The experiments are conducted using five models including ConvNeXt, EVA02, ResNet, ViT-H-14 and RoBERTa-L. The results show that proposed masks can reduce accuracy of these models.

### Weaknesses
There are no comparison methods in the main results, e.g., Table 1 and 2. It is difficult to understand the advantage of proposed methods compared other adversarial samples.

The novelty is limited. The paper proposes to apply different masks to images for constructing the datasets, and then calculates the accuracy of images in the constructed dataset.

It is better to show some visualizations, e.g., images with masks at various intensities.

### Questions
In line 195-200, the paper says that the method uses a weighted average metric to capture various aspects of image quality. How to select these weights? Is it possible to use only one metric?

### Soundness
2

### Presentation
2

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
This work challenges the traditional constraints of imperceptibility in adversarial attacks by introducing periodic noise into image CAPTCHAs, making them resistant to CAPTCHA recognition attacks. By allowing more substantial modifications to the images while preserving their semantic information and ensuring they remain solvable by humans, this approach is capable of deceiving many state-of-the-art models.

### Strengths
Strengths:

- The method of introducing periodic noise into image CAPTCHAs to challenge the imperceptibility constraints in adversarial attacks is both novel and well-founded.
- The dataset and experimental setup are extensive and well-executed, offering compelling evidence for the conclusions drawn.

### Weaknesses
I have significant concerns about the effectiveness of the periodic noise method. It appears that the authors trained their models on standard images and then evaluated them using masked images, which understandably results in a substantial drop in performance. If an attacker were to learn how to apply this periodic mask technique and train with noisy images, the validity of this approach would be greatly undermined.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper reviews the common imperceptibility assumptions adopted by most adversarial attacks and proposes a new attack against automated image models to recognize CAPTCHA by incorporating filters like repeated patterns and words. The paper shows its effectiveness against different models like ViT and RoBERTa. It also shows the attack performance under various parameter settings like opacity. The paper states that this attack can disrupt automated bypassing while preserving the semantic functionality for human users.

### Strengths
1. The writing is clear and easy to understand.
2. The paper inspects the adversarial examples from a new perspective, which holds an assumption different from traditional ones on stealthiness. Instead, the attack, in this case, preserves "functionality" for human beings. The angle is refreshing.
3. The experiments include some of the largest and most advanced transformer models, which is an outstanding point.

### Weaknesses
1. **The experiments are only conducted on a portion of ImageNet, up to 5000**. This makes all the insights gained less convincing.
2. **Many contributions or claims are not validated**. 
- *"The simplicity and ease of execution of the proposed attacks make them readily available to large-scale CAPTCHA systems."*: While the attack might seem "too easy," have you tried to deploy it in a large-scale CAPTCHA system? If not, how much resources will the attack consume? Is it memory-efficient and time-efficient?
- *"Our research aims to understand and leverage the difference in human and machine perception."*: I do not see any insights from understanding the difference except the trade-off between quality and ASR. The stronger the attack is visually, the stronger it will be functionally. Not surprising or interesting enough.
- "We challenge the constraint of imperceptibility in adversarial attacks.": The constraint is naturally relaxed due to this specific problem. You are not challenging the imperceptibility generally for adversarial attacks.
- "thus showing that machines have not caught up with humans–yet.": Showing that adding patterns fails ViT in CAPTCHA cannot act as proof of the sweet victory of humanity.
3. **The evaluation against robust models is insufficient.** Firstly, the paper does not reference the "robustness" of RoBERTa. Secondly, the paper does not show the attack can bypass certified robust models, smoothed models, or adversarially trained models.
4. While the paper claims that **the attack does not negatively influence human beings in recognition, there is no validation at all**. A user study might be helpful. 
5. While I appreciate enhancing the resistance of CAPTCHA against deep-learning image models, it is unclear whether this problem is significant considering CAPTCHA in the real world. According to my experiences, most of the CAPTCHA I encounter nowadays are all different kinds of fancy and weird puzzles. The simplest one might be the one to identify the regions containing the target object. I wonder how significant the problem is considering the scope. Maybe providing some statistics about adopting the "classification-based" CAPTCHA might be helpful. 
6. The claim that "CAPTCHA does not need imperceptibility" is unclear and not convincing. I have two guesses for the authors' intended meaning: (1) The background of CAPTCHA is naturally complex, so the attack looks natural. In this case, the attack's stealthiness still needs to be evaluated. (2) The attacker does not need to make the manipulation invisible as long as the human user can still recognize the object. Now, it seems quite easy to find the attack since they are perceptible. What if the model holder finds out the added patterns and gets them removed? How hard is it to nullify the attack (a.k.a, how robust is the attack itself)? 
7. The paper's writing quality is insufficient, at least for a top conference like ICLR. The paper's language is casual, making the paper read like a technical blog or a homework report. There are many freewheeling claims, as mentioned above. Also, in my perspective, it would be more appropriate to position the paper's contributions in a battle game or "protection" against automated scrapping bots rather than "advancing and understanding robust computer vision systems".

### Questions
1. What is the attack performance in other datasets?
2. How robust is the attack if the image model owner finds the attack pattern? Can he remove the attack?
3. Why is it easy to deploy in large-scale CAPTCHA systems? How much resources will the attack consume? Is it memory-efficient and time-efficient?
4. How do you understand the difference between human and machine perception?
5. Why is RoBERTa robust against AEs?
6. Why are the manipulated images still semantically useful for human users? How do you find that?
7. What about other types of CAPTCHA?

### Soundness
1

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
3

### Summary
This paper introduces a new approach to CAPTCHA design leveraging insights from geometric adversarial perturbations by adding visible geometric patterns (like circles, squares, diamonds, and knit patterns) to images while preserving the semantic information. This makes them difficult for computer vision models to interpret but still easy for humans to interpret. The authors found that these patterns significantly lowered model accuracy, even with robust vision transformers.

### Strengths
1. The paper introduces a new approach by using visibly perturbed images for CAPTCHAs, potentially enhancing security mechanisms.
   
2. It aims to leverage the discrepancies in human and machine perception and the existence of AI-hard tasks where humans surpass machines, which could provide new insights into CAPTCHA design.

4. The detailed description of the method and results is useful and easy to follow, making the findings accessible to readers.

### Weaknesses
1. While the paper mentions leveraging differences in perception, it lacks a thorough analysis of how vision models interpret adversarial examples. This is particularly relevant given their stated contribution of understanding the difference in human and machine perception.

2. The authors do not consider existing literature that demonstrates vulnerabilities in hCaptcha and successful large-scale attacks, such as "A Low-Cost Attack Against the hCaptcha System" by Hossen and Hei. The authors need to check if their CAPTCHAs can withstand these attacks.

3. The paper feels more like a technical report rather than a comprehensive research study, lacking depth in certain areas that would typically be expected in a research paper.

4. The choice of datasets, while practical, may not fully represent the diverse real-world images and contexts CAPTCHAs encounter. Relying solely on ImageNet-based datasets could limit the generalizability of findings across different CAPTCHA scenarios.

6. The paper focuses heavily on machine performance but does not provide a comprehensive assessment of human performance on images with the applied masks. This omission raises questions about how human users actually experience these modified CAPTCHAs and how intuitive they are for practical use.

### Questions
1. Given your aim to leverage the differences in perception between humans and machines, could you elaborate on why there was no thorough examination of how vision models interpret adversarial examples?

2. Why did you not consider existing literature that discusses vulnerabilities in Captcha? How do you believe your CAPTCHAs would perform against the attacks presented in that study?

3. The paper appears to have a technical report-like structure rather than a comprehensive research study. Could you clarify your rationale for this approach and discuss whether you plan to expand on any sections in future work?

4.  Have you considered conducting studies to assess how diverse groups of users interact with and perceive your CAPTCHAs? What plans do you have for including this type of analysis?

5. The choice of datasets used for your experiments seems limited. Can you explain your reasoning behind using only ImageNet-based datasets, and how do you plan to address the generalizability of your findings to different CAPTCHA contexts?

### Soundness
2

### Presentation
3

### Contribution
2
