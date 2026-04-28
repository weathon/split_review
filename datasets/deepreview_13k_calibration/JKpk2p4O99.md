# Towards robust unlearnable examples via deep hiding

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Ensuring data privacy and protection has become paramount in the era of deep learning. Unlearnable examples are proposed to mislead the deep learning models and prevent data from unauthorized exploration by adding small perturbations to data. However, such perturbations (e.g., noise, texture, color change) predominantly impact low-level features, making them vulnerable to countermeasures like adversarial training, data augmentations, and preprocessing. In contrast, semantic images with intricate shapes have a wealth of high-level features, making them more resilient to countermeasures and potential for producing robust unlearnable examples. In this paper, we propose a Deep Hiding (DH) scheme that adaptively hides semantic images enriched with high-level features. We employ an Invertible Neural Network (INN) to invisibly integrate predefined images, inherently hiding them with deceptive perturbations. To enhance data unlearnability, we introduce a Latent Feature Concentration module, designed to work with the INN, regularizing the intra-class variance of these perturbations. To further boost the robustness of unlearnable examples, we design a Semantic Images Generation module that produces hidden semantic images. By utilizing similar semantic information, this module generates similar semantic images for samples within the same classes, thereby enlarging the inter-class distance and narrowing the intra-class distance. Extensive experiments on CIFAR-10, CIFAR-100, and ImageNet-subset, against 12 countermeasures, reveal that our proposed method exhibits state-of-the-art ro- bustness for unlearnable examples, demonstrating its efficacy in data protection.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents an approach to generate unlearnable examples by hiding the semantic images in the natural images. To hide the semantic images, DWT along with INN has been used. The loss functions are combined to ensure a frequency image is close to the natural image and only high-frequency features are disturbed. The experiments are performed on multiple datasets and the resiliency of the proposed approach is also demonstrated.

### Strengths
The paper presents straightforward unlearnable examples generation algorithms.
The generated examples are robust to several defense strategies.

### Weaknesses
### weaknesses:
*   The paper could improve the clarity of the hiding process description by integrating it into the main text instead of relegating it to the supplementary file. This would improve the flow and readability of the paper.
*   The experimental section lacks sufficient depth, particularly in the ablation studies. A more thorough investigation into the impact of various parameters is needed. For instance, an ablation study concerning the role of individual loss items ($\{w_i\}$) would provide valuable insights into their relative importance. Specifically, how do different weight values affect the trade-off between imperceptibility and unlearnability? What is the sensitivity of the model to these weights? The paper mentions using 100 semantic images for hiding; however, it is unclear how these images are selected and utilized during the hiding process. Are all 100 images used for each sample, or is there a selection mechanism? Clarifying this process is crucial.
*   The rationale behind re-implementing existing algorithms needs further justification. While the authors mention using parameters from the original papers, it is unclear whether these implementations were rigorously fine-tuned and validated against the original codebases. Could the authors not use the original implementations or established evaluation protocols from prior work to ensure direct comparability? This would strengthen the validity of the comparisons.
*   The observation that *JPEG10* yields significantly higher robustness across each unlearnable example warrants further investigation. Is there a theoretical explanation for this phenomenon? Have the authors experimented with lower *JPEG* quality factors to understand the relationship between compression level and robustness? Providing a more detailed analysis of this aspect would enhance the paper's contribution. Additionally, have the authors studied the transferability of the proposed examples to different model architectures when these models are trained with defenses? This would provide a more comprehensive understanding of the method's robustness.
*   The sharp drop in test accuracy from 84.40% at 80% unlearnable examples to 10.00% at 100% is intriguing. While the authors hypothesize that the 20% clean data provides useful features, a more in-depth analysis is needed. Is this a gradual decline, or is there a critical threshold? Investigating the relationship between the percentage of unlearnable examples and test accuracy would be beneficial. Furthermore, what is the transferability of unlearnable examples generated using a limited number of samples? Does the effectiveness of the method degrade significantly when fewer unlearnable examples are used during training?
*   The paper should include a more comprehensive discussion of contemporary image-hiding works that are effective in generating adversarial examples, such as those proposed by Din et al. [1] and Agarwal et al. [2]. A detailed comparison highlighting the differences between these methods and the proposed approach would better position the current work within the existing literature. Why can these methods not be used or adapted for generating unlearnable examples, as compared to the proposed DH?

### Questions
Please check the weakness section.

---------------------------------- Post Rebuttal ----------------

The responses posted addressed my concerns.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel method to generate robust unlearnable examples by hiding semantic images within clean images using invertible neural networks (INNs). This introduces perturbations to mislead classifiers while leveraging semantic features that are robust to countermeasures. A Latent Feature Concentration (LFC) module regularizes the intra-class variance of perturbations. A Semantic Images Generation module creates hidden images with consistent semantics within a class to maximize inter-class separation. Experiments on CIFAR and ImageNet datasets demonstrate state-of-the-art unlearnability and robustness against data augmentations and preprocessing.

### Strengths
1. Novel deep hiding scheme to generate unlearnable examples by hiding semantic images using INNs. 

2. Introduces LFC module to regularize intra-class variance of perturbations.  

3. Introduces Semantic Image Generation module to maximize inter-class separation. 

4. State-of-the-art results on CIFAR and ImageNet datasets against various countermeasures.

### Weaknesses
1. Additional Requirements of generating a large dataset of semantic images using paired text prompts and canny edge maps. This process introduces a significant overhead, requiring careful alignment of text prompts with corresponding edge maps, and may not generalize well to datasets where such pairings are not readily available. Furthermore, the quality of the generated semantic images is highly dependent on the performance of the Stable Diffusion and ControlNet models, which are themselves complex and may introduce artifacts or biases.

2. The sample-wise setting may leak information about hidden images. If some hackers know an image is protected in this way, they may find a countermeasure for the unlearnable examples based on the proposed hidden semantic generations. The adaptive nature of the perturbations, while designed to be robust, could still be reverse-engineered if the underlying hiding mechanism is sufficiently understood, especially given the use of a fixed INN architecture.

3. A pre-trained ResNet-18 is used as the feature extractor, all text prompts are clustered using K-means with the semantic features from the CLIP model, and Stable Diffusion model and ControlNet to generate semantic images. It's hard to analyze the effectiveness of each component. The reliance on these pre-trained models makes it difficult to isolate the contribution of the proposed method itself. The performance may be heavily influenced by the specific pre-trained models chosen, rather than the core idea of semantic image hiding. The clustering of text prompts using K-means may also introduce suboptimal groupings, affecting the quality of the generated semantic images.

4. From the above, the connection between the hidden image and the unlearnable example is unclear. The hidden semantic image may not directly contribute to unlearnability. It is not clear whether the unlearnability is a direct consequence of the semantic content of the hidden image, or simply an artifact of the complex perturbation introduced by the INN. The lack of a clear mechanistic explanation weakens the claims of the paper.

5. The robustness and effectiveness may come from the pre-trained ResNet-18, CLIP, Stable Diffusion, or ControlNet. Therefore, the effectiveness and robustness may not come from the architecture and the idea; instead, these may only come from the extra information from the four pre-trained models. The paper does not provide sufficient evidence that the unlearnability is a result of the proposed architecture and hiding scheme, rather than the pre-existing knowledge encoded in these models. The degree to which each component contributes to the final performance is not well-defined.

6. Although an LFC (a pretrained ResNet18) is used to regularize intra-class variance, and the CLIP, Stable Diffusion, and ControlNet are used to maximize inter-class separation, the author should consider the alignment between these pretrained models. The feature spaces of ResNet-18, CLIP, Stable Diffusion, and ControlNet are not necessarily aligned, and any inconsistencies could lead to suboptimal results. The paper lacks a discussion on how these different feature spaces interact and whether any steps are taken to ensure their compatibility.

7. Although Grad-CAM is used to visualize the attention of DNNs, the intra-class and inter-class relationship with the classification and semantic generation should be more fully exploited. Evaluating the inter-class and intra-class statistics directly could also substantiate the claims around controlled semantics, see questions.

### Questions
On page 4, the paper mentions the previous work lacks semantic high-level features and redundancy. However, I don’t know how redundancy is solved in this work.  

There are some ablation experiments that remove each major component would indeed provide better insights into their individual contributions: 

1. Using clean images from different classes as hidden semantic images, or using random natural images as hidden semantic images, rather than generated ones. As you noted, this removes the control over the consistency of semantics within a class. The drop in unlearnability can show the importance of controlled generation. 

2. Removing the Latent Feature Concentration (LFC) module. This would demonstrate the impact of the proposed module in regularizing intra-class perturbations. 

3. Removing the CLIP-based clustering of text prompts. Using random prompts for generation removes controlled inter-class differences. 

4. Evaluating inter-class and intra-class separation quantitatively using metrics like mean intra-class distance and mean inter-class distance. This can formally validate the claims.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on methods for generating unlearnable samples. The paper takes the unique perspective of deep hiding and improves based on existing deep hiding methods, which consequently proposes new methods for generating unlearnable samples. Experiments demonstrate the effectiveness and robustness of the proposed method.

### Strengths
1. The paper is well written and has clear figures.

2. The paper proposed methods for generating unlearnable samples from such an interesting perspective as deep hiding.

3. The experiments demonstrate the high effectiveness and robustness of the method proposed in the paper.

### Weaknesses
1. The comparison experiments do not show the relationship between the scale of the perturbations generated by the proposed method and the comparison method, and the size of the generated perturbations cannot be fully controlled by $L_{hide}$ alone, because there are other losses included in the total loss. Specifically, the paper lacks a direct comparison of perturbation magnitudes (e.g., measured by metrics such as L2 norm or PSNR) between the proposed method and existing unlearnable example generation techniques. This makes it difficult to assess whether the proposed method achieves unlearnability through comparable perturbation magnitudes or by other means. Furthermore, while $L_{hide}$ aims to control the perturbation, the presence of other loss terms in the total loss function makes it unclear how much influence $L_{hide}$ has on the final perturbation size. This lack of control over the perturbation scale is a significant limitation.

2. An ablation experiment on the semantic image generation module is missing to demonstrate its advantages compared with randomly selected hidden images. The paper does not provide sufficient evidence to justify the use of a complex semantic image generation module. It remains unclear whether the semantic content of the hidden image is essential for the effectiveness of the unlearnable examples, or if randomly generated noise or other simpler hidden patterns would achieve similar results. An ablation study comparing the proposed semantic image generation module with simpler alternatives is necessary to validate its contribution.

### Questions
1. There is a backward revealing process for the INN-based hiding model used in the paper, but what is the significance of the existence of this process?

2. The paper proposed a concentration loss (Eq. 7), and how are sample i and sample j selected in the specific implementation?


======================After rebuttal===================

The authors' response address most of my concerns. Thus I am willing to increase the rating score to 6.


======================Update after discussion===================

After discussion, I agree with reviewer Naq4. For data with larger resolution, while it contains more information that needs to be protected, there are also more features that can be used to hide critical content. However, the proposed method seems to be limited on more complex datasets (e.g., ImageNet-subset). Thus, I think the current work needs further improvements to meet the acceptance criteria.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The majority of existing methods for generating Unlearnable Examples primarily focus on investigating the robustness against adversarial training, while overlooking the resilience to other attack strategies such as data augmentation and preprocessing. Previous research has found that images containing semantic information are robust against common attacks. In this paper, the authors propose a novel defense mechanism that is effective under various prevalent attack methods. The authors first generate multiple image samples corresponding to the number of categories using ControlNet, and then employ Image Hiding techniques to conceal the generated image samples within the dataset to be protected, utilizing Invertible Neural Networks (INN). This process disrupts the original semantic information of the images, thereby achieving the goal of protecting the data.

### Strengths
- The authors introduce Image Hiding techniques into Data Unlearning, providing a new reference direction for the field of Data Unlearning.
- The authors employ a Latent Feature Concentration module during the image hiding process to achieve consistency in semantic features within the same class, thus allowing the features of similar data to become more concentrated.
- The selection of attack methods for the experiments in this paper is fairly comprehensive.

### Weaknesses
 - The method consists of three modules: The Deep Hiding Scheme, which introduces the concept of Image Hiding, an existing work; the Semantic Image Generation Module, which utilizes the existing ControlNet; and the Latent Feature Concentration Module, which is very similar to the idea of EntF mentioned in the related work. In summary, the ideas presented in this paper are intriguing, but the innovation is insufficient.
- Previous research has shown that some Unlearnable Examples possess an inherent resistance to data augmentation, which contradicts the paper's claim that prior methods have overlooked these issues. Specifically, while some methods might be vulnerable to simple processing like grayscaling or JPEG compression, many have demonstrated robustness against common augmentations like cutout, mixup, and blurring, which are also included in the experimental evaluation of this paper.
- In the experimental settings of the paper, the perturbation for adversarial training is set to $8/255$, and the perturbation for protection noise also appears to be set to $8/255$ according to the experimental table. Under this setting, which is consistent with EntF, the paper's experiments lack a comparison with this method. Furthermore, the choice of $8/255$ for both adversarial and protection perturbations raises questions about the method's ability to defend against stronger attacks or if the protection mechanism is simply adding noise at the same magnitude as the adversarial perturbation.
- The paper doesn't explain why it's also effective under adversarial training.

Although the introduction of Image hiding in the paper is interesting, the three important parts of the article are existing work and lack innovation. In addition, there is a lack of comparison of EntF methods, a lack of inquiry about defense against training, and a lack of inquiry about the effect of the generated hiding image on protection. All in all, at this point in time, I would recommend this paper as weak reject.

### Questions
see weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
