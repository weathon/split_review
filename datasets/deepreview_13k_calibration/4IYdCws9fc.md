# REFINE: Inversion-Free Backdoor Defense via Model Reprogramming

- Decision: Accept
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
Backdoor attacks on deep neural networks (DNNs) have emerged as a significant security threat, allowing adversaries to implant hidden malicious behaviors during the model training phase. Pre-processing-based defense, which is one of the most important defense paradigms, typically focuses on input transformations or backdoor trigger inversion (BTI) to deactivate or eliminate embedded backdoor triggers during the inference process. However, these methods suffer from inherent limitations: transformation-based defenses often struggle to balance the intensity of transformations with preserving the model's accuracy, while BTI-based defenses require accurate reconstruction of the trigger patterns, which is rarely achievable without prior knowledge. In this paper, we propose REFINE, an inversion-free backdoor defense method based on model reprogramming. REFINE consists of two key components: (1) an input transformation module that disrupts both benign and backdoor patterns, generating new benign features; and (2) an output remapping module that redefines the model's output domain to guide the input transformations effectively. By further integrating supervised contrastive loss, REFINE enhances the defense capabilities while maintaining model utility. Extensive experiments on various benchmark datasets demonstrate the effectiveness of our REFINE and its resistance to potential adaptive attacks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper propose an inversion-free backdoor defense method based on model reprogramming, REFINE. REFINE consists of an input transformation module and an output mapping module. The key idea is to transform both input and output domains to break the trade-off between model utility and defense effectiveness faced by existing pre-processing based defenses.

### Strengths
- Extensive experiments demonstrating the effectiveness of REFINE across different datasets.

- Thorough ablation studies validating each component's contribution

### Weaknesses
 - The connection between motivation and the proposed methods is not very close. However, the analysis of BTI-based defenses does not involve this domain-based perspective. The paper didn’t discuss whether and how the purification process in BTI-based defenses alter the image domain.

- The theoretical analysis through Theorem 1 effectively explains the limitations of transformation-based defenses by quantifying how domain transformations affect defense performance.

- Experiments mainly focus on ResNet. Conducting experiments under different network structures is beneficial for verifying the effectiveness of the proposed method, for example, VGG, DenseNet etc.

- Requiring 20% clean data may be impractical in many real-world scenarios.

- The proposed method requires training a U-Net, which involves a significant computational cost.


### Questions
In Figure 3, why did the color of the part of the image outside the trigger also change?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper analyzes existing pre-processing-based backdoor defense methods and their limitations. Then, a simple yet effective method is proposed. This method utilizes model reprogramming techniques rather than model retraining, which not only eliminates backdoor attacks but also maintains the model's performance. The evaluation of different backdoor attacks also demonstrates the effectiveness of the proposed method.

### Strengths
1. A theoretical analysis demonstrates that the effect of backdoor defenses is bounded by the distance of the output features before and after the preprocessing. Therefore, existing methods can not break the trade-off between the model utility and the defense effectiveness.
2. The proposed method is novel and interesting. By integrating model reprogramming techniques, they only need to change the model input without changing the model parameters to achieve backdoor elimination, and it does not affect the original performance of the model.

### Weaknesses
1. The authors discuss the pre-processing defense methods, i.e., input-transformation defenses and BTI-based defenses, and analyze their limitations in details. However, the proposed methods actually belong to the input transformation-based method. This paper also spend a large amount of time to analyze and compare BTI methods with the proposed method, which makes it hard to read.
2. This paper assumes that they have access to an unlabeled dataset that is independent and identically distributed to the training dataset of the pre-trained model. The authors need to clarify how to acquire this dataset. In addition, since the performance of model reprogramming methods is related to the distribution of input data, if the author cannot obtain data with the same distribution, will it affect the performance of the model?
3. The experiment is pretty insufficient. REFINE is only evaluated with the ResNet-18 model. The evaluation under more complex models (such as ResNet-50) or other architecture models (such as InceptionV3 or VGG16) is lack.

### Questions
1. The two sentences (i.e., "by first obtaining ... outcomes" and "the internet ... poisoned samples)") in the Section 1 contradict each other. What is the difference between prior information and prior knowledge?
2. This paper focuses on the dirty-image backdoor attacks. But considering the recent clean-image backdoor attacks that do not have trigger features, can the proposed defense method work?
3. In Section 3.2, the "Pad Size" and "Mask Ratio" are not defined before. it is necessary to clarify.
4. In this paper, there are many long sentences, which makes it hard to understand. Such as "Additionally, we treat ... the transformation" on Page 4.
5. In Section 3.2, the authors did not show the dataset used for limitation analysis. Please clarify it.
6. In Section 4.2.1, the authors present that traditional model reprogramming methods are insufficient to remove triggers. I suggest that the authors explain why traditional methods are insufficient in detail.
7. The discussion about the feature distance changes in the proposed input transformation module is lacking. It is better to add it to highlight the function of this module.

### Soundness
3

### Presentation
2

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
This paper  proposes REFINE, an inversion-free backdoor defense method based on model reprogramming. Based on the research, the authors revisit existing pre-processing-based backdoor defenses and reveal their limitations. The proposed defense, REFINE, introduces trainable input transformation and output mapping modules for reprogramming and incorporates cross-entropy and supervised contrastive losses to enhance defense performance. Extensive experiments are conducted to validate the effectiveness of REFINE.

### Strengths
1. Revisit the pre-processing defenses against backdoor attacks and reveal their limitations. The pre-processing-based defense is important to protect model security while not changing model structure or weights.
2. Propose a pre-processing defense against backdoor attacks, which seems to be simple but effective.
3. Conduct extensive experiments to demonstrate the effectiveness of the proposed defense.

### Weaknesses
1. The claim of the limitations of prior works are subjective and confusing. For the first limitation, the authors think "transformation-based backdoor defenses methods face a trade-off between utility and effectiveness". So, can the proposed defense overcome this limitation? From the design and experimental results, REFINE also suffer from the same problem. Otherwise, the BA with REFINE should be same with  original model. Moreover, the authors try to utilize experiments to validate their claims. However, the experimental setting is not fair enough. For example, the authors mention ShrinkPad as the baseline. However, in that paper, ShrinkPad is not the best defense method. Also, for the second limitation, the authors do not analyse the SOTA work, and the shown experimental results are different from the original paper, e.g., the experiments with BADNET shown in Fig.3.
2. The categories of the mentioned defenses are not sound enough. According to the manuscript, the BTI-based defense (e.g., NC) reverses the backdoor trigger to eliminate the trigger in the inputs. However, such a kind of defense does not only work in this way. Thus, the comparison seems to be not fair enough.
3. The experiments do not involve some SOTA works. e.g, [1, 2]. Moreover, the experimental results differ from the original paper a lot, e.g., BTI-DBF. Please explain why.

### Questions
1. Please improve the soundness of the limitation study.
2. Please discuss the reasonability of the categories of the mentioned defenses.
3. Please explain the different experimental results.

### Soundness
2

### Presentation
3

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
This paper addresses the challenge of backdoor attacks in deep neural networks, where current defenses struggle to balance accuracy and trigger removal. The proposed REFINE method combines input transformation and output remapping to effectively neutralize backdoors without relying on trigger inversion. Experiments show REFINE's strong defense capabilities while maintaining model performance.

### Strengths
1. The idea may seem bold and imaginative, but it is worth exploring in depth. I believe both the threat model setup and the proposed solution are good.
2. Overall, the paper is well-written, making it relatively easy for someone unfamiliar with model reprogramming, like myself, to grasp the design concepts.
3. The method operates effectively with a small amount of unlabeled data, which not only cleverly avoids direct comparison with fine-tuning-based defenses but also demonstrates its practicality through ablation experiments that confirm its minimal data requirements.

### Weaknesses
1.Regarding the theoretical explanation in the paper (Formula 1), I feel it’s missing a key component and has only achieved about 50% of its purpose. It aims to explain how amplifying the distributional differences in output features changes the variation in prediction results. As the authors emphasize, model reprogramming significantly amplifies these distributional differences, and trigger patterns can be randomized. I agree with this point, but at this stage, the performance guarantee for clean samples doesn’t tie back to this theory; I see it as being empirically supported by the two losses. In fact, even with model reprogramming, Formula 1 still holds, so it may not fundamentally support the authors’ viewpoint (since Formula 1 is a rule that must be met across the overall distribution; I believe focusing on local distributions could be a potential solution).

2.The whole experiments are only conducted on a ResNet-18 model. Furthermore, the discussion of the black-box part in the experiments seems counterproductive to me; I don’t understand the rationale behind setting up absurdly similar black-box and substitute models for exploration.

3.The adaptive attack setup is unreasonable. Based on the general consensus in the community, in adaptive attacks, the attacker is assumed to know the defender’s hard-coded choices. Disallowing the defender from making real-time adjustments (which is a strategy directly aimed at adaptive attacks) is therefore a logical error. Additionally, the authors haven’t clearly explained why a conflict exists between adaptive loss and backdoor loss, resulting in a decrease in BA, and I don’t clearly see a trade-off here.

4.Why is BTI-DBF unable to reverse even the most basic BadNet trigger? I seriously question the validity of this experiment. In the original BTI-DBF paper, it’s evident that it can reconstruct the triggers of certain fixed samples quite effectively.

5.Additionally, I would like to see more examples of transformed samples. Do transformed samples from the same class still share some visual similarities, or do they contain almost no human-recognizable information? What is the underlying significance of these transformations? I am curious if the authors could offer some more unique, high-level insights.

### Questions
See weakness part.

### Soundness
2

### Presentation
4

### Contribution
3
