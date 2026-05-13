# Less is More: Stealthy and Adaptive Clean-Image Backdoor Attacks with Few Poisoned

- Decision: Reject
- Scores: 5, 5, 8, 5, 6

## Abstract
Deep neural networks are fundamental in security-critical applications such as facial recognition, autonomous driving, and medical diagnostics, yet they are vulnerable to backdoor attacks. Clean-image backdoor attack, a stealthy attack utilizing solely label manipulation to implant backdoors, renders models vulnerable to exploitation by malicious labelers. However, existing clean-image backdoor attacks likely lead to a noticeable drop in Clean Accuracy (CA), decreasing their stealthiness. In this paper, we show that clean-image backdoor attacks can achieve a negligible decrease in CA by poisoning only a few samples while still maintaining a high attack success rate. We introduce **G**enerative Adversarial **C**lean-Image **B**ackdoors (GCB), a novel attack method that minimizes the drop in CA to less than 1\% by optimizing the trigger pattern for easier learning by the victim model. Leveraging a variant of InfoGAN, we ensure that the trigger pattern we used has already been contained in some training images and can be easily separated from those feature patterns used for benign tasks. Our experiments demonstrate that GCB can be adapted to 5 datasets—including MNIST, CIFAR-10, CIFAR-100, GTSRB, and Tiny-ImageNet—5 different architectures, and 4 tasks, including classification, multi-label classification, regression, and segmentation. Furthermore, GCB demonstrates strong resistance to backdoor defenses, successfully evading all detection methods we know. Code: *anonymous.4open.science/r/GCB*.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a mutual information-constrained approach for backdoor pattern generation, to create backdoored samples with similar distribution to the target class. Therefore, the authors can enhance the stealthiness of backdoor samples. The authors demonstrate the strong correlation between the backdoor samples and the backdoor labels, showing that such samples can be easily learned by the model.

### Strengths
The authors propose to generate backdoor samples based on InfoGAN, enhancing stealthy of backdoor attacks. The proposed backdoor is proved to be more undetectable and easy to learn. This work is validated by theoretical analysis and supported by well-designed experiments.

### Weaknesses
1.To my best knowledge, other advanced clean image backdoor methods are strongly related to the proposed approach. Although they are not referred to as ‘clean image backdoors,’ they are also rather ‘invisible backdoors’. From this perspective, the innovation of the proposed approach seems limited. I suggest that the authors compare their method with these state-of-the-art techniques and clarify its advantages.
References:
[1]Li, Yuezun, et al. "Invisible backdoor attack with sample-specific triggers." Proceedings of the IEEE/CVF international conference on computer vision. 2021.
[2]S. Li, M. Xue, B. Z. H. Zhao, H. Zhu and X. Zhang, "Invisible Backdoor Attacks on Deep Neural Networks Via Steganography and Regularization," in IEEE Transactions on Dependable and Secure Computing, vol. 18, no. 5, pp. 2088-2105, 1 Sept.-Oct. 2021, doi: 10.1109/TDSC.2020.3021407.
[3]R. Ning, J. Li, C. Xin and H. Wu, "Invisible Poison: A Blackbox Clean Label Backdoor Attack to Deep Neural Networks," IEEE INFOCOM 2021 - IEEE Conference on Computer Communications, Vancouver, BC, Canada, 2021, pp. 1-10, doi: 10.1109/INFOCOM42981.2021.9488902.
2.The condition ‘irrelevance’ is only briefly explained in the ablation study, where this loss is removed to measure ASR. However, the experiments do not effectively demonstrate why the generated samples are irrelevant to the original-class samples. Specifically, the ablation study only shows the impact on ASR, not how the generated trigger maintains the original classification performance when applied to clean images.

### Questions
1.In Figure 4, the authors analyze the learning rate on backdoor data using the CIFAR-10 dataset. I find it interesting that the learning rate of GCB is higher than that of BadNet and clean image, as this contradicts previous findings suggesting that more ‘out-of-distribution’ backdoor samples are learned faster. To better validate this observation, I recommend the authors to test on additional datasets.

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
The paper proposes a clean-image backdoor attack that achieves low poisoning rates even in the all-to-one setting. The proposed method relies on learning an InfoGAN's generator network to generate images from real and fake classes (this is used to generate the triggered images) and a discriminator network to distinguish samples between real and fake classes (this is used as scoring function to select poisoned samples). This design of InfoGAN's networks ensures that the trigger patterns exist within the real images, while making the poisoned tuples separated from the clean tuples for easier backdoor training. The paper provides extensive empirical results to demonstrate the effectiveness of the proposed method on multiple datasets, architectures, and defenses.

### Strengths
The main strengths of the paper lie in its clever use of InfoGAN and the extensive empirical results (although I do have some concerns in these aspects as well)
* The use of InfoGAN, while trivial, shows a cleverness in using it for clean-image backdoor attack. 
* The experiments include multiple benchmark datasets. The paper also evaluate against multiple networks and a large number of defenses.

### Weaknesses
While this paper is interesting, I also find several concerns, specifically on its rigorous analysis of why the method works so well:

* The paper proposes to use Wasserstein loss, but the theoretical analysis instead shows the convergence on JS Divergence. This is a crucial mismatch. In fact, I don't even think the proof of convergence is necessary because it is quite well established for InfoGAN (and GAN in general), and the paper does not change anything in the base InfoGAN model, rather than changing the model's input. The analysis should focus on the specific properties of the learned generator and discriminator in the context of the backdoor attack, rather than generic convergence proofs.
* I also find that the statement of converging, especially in the context of GANs, is quite strong. It's been known that GANs' theoretical convergence and what actually happens in practice are two very different things. I suggest that the paper focuses more on analyzing why the scoring function works so well instead, and provide a more rigorous analysis there. Specifically, the paper should analyze how the discriminator's decision boundary evolves during training and how this boundary separates real and fake samples, leading to effective backdoor triggers. The current analysis lacks this crucial connection.
* In fact, I find that the design of the attack is based on several assumptions (such as convergence) that may or may not hold in practice. While the final results show favorable performance for GCB, the paper lacks rigorous connections between these assumptions and the performance, which is a bit disappointing. The paper needs to provide a more detailed analysis of the generator's learned latent space and how the manipulation of this space leads to effective backdoor triggers. The connection between the InfoGAN's latent space and the backdoor trigger's effectiveness is not sufficiently explored.
* For example, the statement that the backdoor can be learned even more easily than BadNets deserves more rigorous analysis. In general, in backdoor attacks, when the backdoor is learned really easily, it also causes several consequences; for example, ABL relies on the fact that the loss of poisoned samples drops abruptly during training, which urges the question of why GCB works so well. As there are so many backdoor attack papers in the last several years, I think that these analyses are much more important than demonstrating that the method "just works very well". The paper should investigate the training dynamics of the poisoned samples and compare them with those of other backdoor attacks to understand why GCB is more effective and stealthy.
* I also find that while several defenses have been tested (which is commendable), a new category of defenses (based on fine-tuning, such as FT-SAM) is not evaluated. I wonder whether the fact that the backdoor is learned very quickly could also mean that fine-tuning defenses could work very well against GCB. The paper should include an evaluation against fine-tuning based defenses to provide a more complete picture of the attack's robustness.
* Another weakness of the paper is that several experiments only include the evaluations on CIFAR10 and CIFAR100, which are essentially the same. I would suggest that the paper to include all datasets. The lack of diversity in datasets limits the generalizability of the findings and should be addressed by including more diverse datasets.
* On line 214, the paper suddenly introduces *c*, a notation that is not explained until a bit later. I find that this part of the paper could be improved quite a lot. In addition, I struggled a bit to understand how the triggered images are created during inference. I think the paper assumes that the reader is very familiar with the backdoor domain, and I hope the paper can make this part clearer and more accessible to new readers. The methodology section needs significant revision to improve clarity and ensure that all notations and processes are clearly explained.
* Some minor grammatical errors/typos: - line 69: "construct trigger", several places the paper mention InforGAN.

### Questions
Please see the concerns in the weaknesses!

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a GAN-based architecture that makes backdoor triggers easier to learn for the victim model and hence achieves high ASR and hinders non-trivial clean accuracy drop. The proposed GCB (Generative adversarial clean image backdoor) combines InfoGAN and Conditional GAN to ensure that the backdoor trigger meet requirements of existence, separability and irrelevancy. The authors perform comprehensive evaluations over various dataset across different model architectures and demonstrate that GCB achieves high ASR and CA with a low poisoning rate. They also conduct a extensive ablation study of their design choices and assess GCB against multiple existing defenses.

### Strengths
- This paper tackles the clean accuracy drop issue in clean-image backdoors, which further improves the effectiveness and stealthiness of such an attack.

- The proposed GAN architecture is technically sounded and novel. The authors explicitly explain their motivations of using InfoGAN and conditional GAN, and the GCB design is well-aligned with the objectives of triggers properties (i.e., existence, separability and irrelevancy).

- The authors also provide detailed theoretical proofs and mathematical analysis for the design.

- The experiments are abundant to support the authors claims. They show that the GCB can generalize to different datasets and model architectures including TinyImageNet and ViT.  They also test it on multiple vision tasks such as image regression and segmentation. In addition, GCB is evaluated against prestigious defenses for backdoor attacks.

- The paper is well-written and easy to follow.

### Weaknesses
 - I don't see any major weaknesses/issues in this paper.

### Questions
- In the paper, you show figures of selected training samples and triggered test samples. Can you also provide the figure of generated triggers?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces Generative Adversarial Clean-Image Backdoors (GCB), a backdoor attack technique that minimizes detection in neural networks used for sensitive applications like facial recognition and autonomous driving. Unlike traditional backdoor attacks, GCB only uses clean images with manipulated labels, avoiding noticeable accuracy drops and making the attack stealthier. The technique employs a variant of InfoGAN, called C-InfoGAN, to embed backdoor triggers naturally by manipulating benign features in the dataset. The method maintains high attack success rates (ASR) across multiple tasks, datasets, and architectures, even with low poison rates. Extensive experiments show GCB’s resilience against numerous backdoor defenses, including Neural Cleanse and STRIP, and strong adaptability across diverse visual tasks.

### Strengths
(1)  GCB achieves high attack success rates (ASR) with minimal impact on clean accuracy (CA), which is critical for stealthiness in security-sensitive applications.

(2) With a poison rate as low as 0.1%, GCB still maintains high ASR, showcasing efficiency in terms of resource requirements.

### Weaknesses
 (1) This paper employs GANs to generate the trigger image. However, GANs are known for their limited ability to fit complex data distributions, such as ImageNet, raising concerns about the method's applicability to more complex datasets. Specifically, the high dimensionality and intricate feature relationships within datasets like ImageNet pose a significant challenge for GANs, potentially leading to triggers that are not sufficiently realistic or effective in a real-world scenario. The paper should provide a more thorough analysis of the GAN's capacity to generate triggers that can generalize well across diverse image complexities.

(2) Since the trigger in this study is GAN-generated, there may be a significant distributional gap between the generated trigger and real image data. Consequently, it is essential to analyze the method’s resistance to defense strategies based on abnormal sample detection. The concern is that the GAN-generated triggers, even if visually subtle, might occupy a distinct region in the feature space of the victim model, making them vulnerable to detection methods that identify outliers or anomalies in the feature distributions. A more rigorous evaluation against such defenses is needed to validate the practical stealth of the proposed method.

(3) The theoretical justification in Section 3.2 closely aligns with prior work on InfoGAN, and this overlap should be clarified to better situate the contribution within the existing literature. The paper needs to more clearly delineate the novel aspects of their approach from the existing InfoGAN framework, particularly in the context of backdoor attacks. A more detailed explanation of how their specific adaptation of InfoGAN differs and contributes to the field is necessary.

(4) The paper uses InfoGAN to partition the benign training set into two subsets (A and B), selecting one (B) for poisoning. However, this approach may reduce benign accuracy on the original subset B. Additional experiments and discussion regarding the impact on benign accuracy would strengthen this section. The concern is that by manipulating labels within subset B, the model's performance on the original, unpoisoned data distribution of B might be compromised. The paper should include a more detailed analysis of the trade-off between attack success and the potential degradation of clean accuracy on the manipulated subset.

### Questions
(1) This paper employs GANs to generate the trigger image. However, GANs are known for their limited ability to fit complex data distributions, such as ImageNet, raising concerns about the method's applicability to more complex datasets.

(2) Since the trigger in this study is GAN-generated, there may be a significant distributional gap between the generated trigger and real image data. Consequently, it is essential to analyze the method’s resistance to defense strategies based on abnormal sample detection.

(3) The theoretical justification in Section 3.2 closely aligns with prior work on InfoGAN, and this overlap should be clarified to better situate the contribution within the existing literature.

(4) The paper uses InfoGAN to partition the benign training set into two subsets (A and B), selecting one (B) for poisoning. However, this approach may reduce benign accuracy on the original subset B. Additional experiments and discussion regarding the impact on benign accuracy would strengthen this section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes Generative Adversarial Clean-Image Backdoors (GCB), a novel clean-image backdoor attack method that maintains high ASR with low poison rates and minimal drop in clean accuracy (CA). The key idea is optimizing the trigger pattern to make it easier for the victim model to learn, by using a variant of InfoGAN called C-InfoGAN. Experiments demonstrate GCB's effectiveness across 5 datasets, 5 model architectures, and 4 vision tasks. GCB also shows strong resistance to existing backdoor defenses.

### Strengths
- Achieves outstanding stealthiness, with high ASR (>90%), low poison rate (<=1%), and minimal CA drop (<=1%) across all tested datasets. This significantly advances clean-image backdoor attack capabilities.
- Shows strong adaptivity to 5 datasets, 5 architectures, and 4 vision tasks beyond just classification. Indicates the attack is widely applicable.
- Introduces a novel C-InfoGAN method to optimize triggers for easy learning without interfering with clean task accuracy. The theoretical analysis supports why this works.
- Demonstrates robustness to a wide range of backdoor defenses, revealing gaps in existing mitigation techniques that need to be addressed.
- Extensive experiments and ablations provide good insight into the attack's behavior and validate the approach.

### Weaknesses
 - Scalability concerns: The paper only evaluates on relatively small datasets. The required poison rate increases as dataset complexity grows (e.g. from CIFAR-10 to Tiny ImageNet), suggesting scalability issues. It's unclear if the method would still be effective on large-scale datasets like ImageNet-1K without requiring an impractically high poison rate. Testing on a wider range of dataset sizes would help assess the scalability limits. Specifically, the paper lacks analysis on how the generator's capacity and training dynamics would be affected by the increased dimensionality and complexity of larger datasets. The current experiments do not sufficiently address whether the C-InfoGAN framework can maintain its effectiveness when the feature space and label space grow significantly.
- Limited evaluation against newer defenses: Many of the backdoor defenses tested are relatively dated. The attack's effectiveness against more recent state-of-the-art defenses, particularly those developed in the past 1-2 years, is not demonstrated. Additionally, for the Label Cleaning experiments, only one technique is evaluated. There are several other advanced Label Cleaning approaches that may be more effective but are not considered, such as DivideMix, MentorMix, and Robust Meta-Learning. The paper should include a more comprehensive evaluation against recent defense methods to provide a clearer picture of the attack's robustness. It is also important to analyze the specific mechanisms by which these defenses fail or succeed against GCB, rather than simply reporting aggregate results.
- Relabeling mitigation analysis: The authors' claim that a >95% relabeling rate is needed to keep ASR below 20% seems questionable given advancements in vision-language models. With the increasing popularity and capability of models like CLIP and BLIP, it may be feasible to automatically relabel large portions of the training set accurately and efficiently. This could significantly lower the cost of relabeling and make it a more viable mitigation strategy. The paper's analysis of relabeling as a defense does not sufficiently consider this. The analysis should also explore the impact of relabeling on different types of backdoor triggers, as some triggers might be more resilient to relabeling than others.

### Questions
- Scalability: Have you considered evaluating GCB on larger, more complex datasets beyond Tiny ImageNet, such as ImageNet-1K? How do you expect the attack performance and required poison rate to scale on these large-scale datasets?
- Hyperparameter sensitivity: How sensitive is the attack performance to the choice of hyperparameters, such as the learning rate and weight decay for the C-InfoGAN training? Did you find that careful tuning was necessary to achieve good results, or is the attack relatively robust to hyperparameter choices?
- Transferability to other domains: While the paper demonstrates strong results on vision tasks, do you expect the GCB attack to generalize to other data modalities, such as audio, text, or graphs classification? What challenges might arise in adapting the method to these domains?

### Soundness
4

### Presentation
3

### Contribution
3
