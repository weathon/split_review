# Watch Out!! Your Confidence Might be a Reason for Vulnerability

- Decision: Reject
- Scores: 3, 3, 5, 6

## Abstract
The tremendous success of deep neural networks (DNNs) in solving `any' complex computer vision task leaves no stone unturned for their deployment in the physical world. However, the concerns arise when natural adversarial corruptions might perturb the physical world in unconstrained images. It is widely known that these corruptions are inherently present in the environment and can fool DNNs. While the literature aims to provide safety to DNNs against these natural corruptions they have developed two forms of defenses: (i) detection of corrupted images and (ii) mitigation of corruptions. So far, very little work has been done to understand the reason behind the vulnerabilities of DNNs against such corruption. We assert that network confidence is an essential component and ask whether the higher it is, the better the decision of a network is or not. Moreover, we ask the question of whether this confidence itself is a reason for their vulnerability against corruption. We extensively study the correlation between the confidence of a model and its robustness in handling corruption. Through extensive experimental evaluation using multiple datasets and models, we found a significant connection between the confidence and robustness of a network.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes using Stochastic Weight Averaging Gaussian (SWAG) as a method for calibrating neural networks, aiming to improve their performance and robustness against natural corruptions. The approach leverages SWAG's capacity to model uncertainty and enhance prediction reliability, asserting that better-calibrated confidence scores contribute to robustness in challenging real-world conditions.

### Strengths
The paper presents a detailed investigation into the impact of calibration on model robustness, especially under naturally occurring corruptions. By systematically exploring the role of confidence in model predictions, the authors contribute to understanding the relationship between calibration and robustness, reinforcing SWAG’s potential in addressing natural corruption without introducing additional computational burden associated with adversarial training.

### Weaknesses
1. Limited Novelty: The paper largely relies on the established SWAG technique without introducing new calibration methods or adaptations specific to the architecture or the problem of natural corruption.

2. Experimental Scope: The experimental evaluations are confined to small datasets (CIFAR-10 and CIFAR-100) and convolutional architectures like VGG and ResNet, lacking analysis on larger-scale datasets and modern architectures like Transformers.

### Questions
1. Applicability Across Architectures: The proposed method seems tailored primarily for convolutional neural networks (CNNs). A major gap lies in assessing how well SWAG might generalize to other architectures, such as Transformers, which have become prevalent in vision tasks. Expanding the discussion on generalizability or including Transformers in the experimental setup could enhance the study's relevance and adaptability to current deep learning trends.

2. Novelty in Approach: While the study reinforces known concepts around calibration and robustness, these insights are not novel, particularly within the Bayesian deep learning community, where calibration’s role in improving robustness under adversarial scenarios is well-understood [refA, refB]. This limits the paper's contribution, as it primarily confirms existing knowledge rather than pushing the boundaries with a novel calibration approach. Introducing an innovative calibration technique, or a modified variant of SWAG tailored for robustness, would provide a more substantial contribution.

3. Experimental Limitations: The experiments focus on CIFAR datasets and CNNs, which are both limited in size and scope. A broader evaluation involving larger datasets like ImageNet, and a wider range of architectures, including Transformer-based models, would offer a stronger validation of SWAG's effectiveness. This could also strengthen the paper’s generalizability claims and its relevance for real-world deployment.

References

[refA] Wicker, Matthew, et al. "Bayesian inference with certifiable adversarial robustness." International Conference on Artificial Intelligence and Statistics. PMLR, 2021.

[refB] Stutz, David, Matthias Hein, and Bernt Schiele. "Confidence-calibrated adversarial training: Generalizing to unseen attacks." International Conference on Machine Learning. PMLR, 2020.

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
The paper explores the challenges DNNs face from natural adversarial corruptions, which can undermine their robustness. While past work has focused on detecting and mitigating these corruptions, this study examines whether a model’s confidence may contribute to its vulnerability.

### Strengths
1. It explores the vulnerability of DNNs from the perspective of model overconfidence.
2. The article is well-structured and relatively clear in its presentation.

### Weaknesses
1. What exactly is the novelty of this paper? SWAG is not your contribution; merely using it to derive some results for analysis does not suffice.
2. The phenomenon of model overconfidence appears to be only a description in your paper. Do you have specific examples or experimental results to substantiate this claim?
3. Is your method limited to CNN architectures? Given the prevalence of transformer-based models, a method solely applicable to CNNs may have limited relevance, and it appears you tested on a very small set of CNN models.
4. Based solely on the text, I cannot appreciate the superiority of your method. Please provide comparative experiments with adversarial training methods, covering dimensions such as effectiveness and cost. Furthermore, does your method apply only to natural corruptions? How would it perform against adversarial samples?
5. The experiments lack depth: (1) In terms of models, this paper tests only on VGG-16 and ResNet, which seems rather limited. Where are the tests on more advanced models? (2) In terms of datasets, you only used CIFAR-10 and CIFAR-100, yet experiments on ImageNet are also necessary.

### Questions
Please refer to the weakness.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper investigates the vulnerability of deep neural networks (DNNs) when facing natural corruptions (such as noise, blur, etc.) and proposes that the model's confidence could be an important factor contributing to this vulnerability. Experiments demonstrate a significant correlation between a model’s confidence and its robustness in handling corruption. The study primarily focuses on calibrating model confidence and employs the Stochastic Weight Averaging Gaussian (SWAG) method to enhance model robustness.

### Strengths
Proposing that high confidence might lead to model vulnerability in naturally corrupted environments is a novel perspective, differing from traditional defense methods.

### Weaknesses
1. This paper only conducts experiments on convolutional neural networks (CNNs), lacking tests on other network architectures such as ViT-B/16 or DeiT, to validate the conclusions about confidence and robustness across different model types. This would provide a more comprehensive demonstration of the method's applicability and effectiveness.

2. This paper validates the robustness of the model to natural corruptions and its relationship with confidence using CIFAR-10 and CIFAR-100 datasets. However, the complexity of these datasets is relatively low, making it difficult to fully reflect the model's performance in real-world complex scenarios. It is recommended to conduct further experiments on more challenging datasets such as ImageNet-C or ImageNet-A, which include a broader range of corruptions (e.g., Gaussian noise, motion blur, weather-induced degradation, digital transformations) and better reflect the diversity and complexity of real-world applications. 

3. The paper mainly focuses on confidence calibration without an in-depth comparison with other advanced defense methods (such as adversarial training), which may weaken the practical applicability of this approach.

### Questions
Although the proposed method addresses natural corruption, its effectiveness against gradient-based adversarial attacks remains unclear. It is recommended that the authors conduct experiments involving FGSM, PGD, and C&W attacks to evaluate the method's performance under adversarial attacks. For example, performance under different noise magnitudes and different numbers of attack iterations could be assessed.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the correlation between the confidence of deep neural networks and their vulnerability to natural corruptions. Specifically, the authors leverage the model calibration method SWAG to construct a smoothed model. The parameter of this model is sampled and averaged from the estimated Gaussian distribution of several versions of model parameters recorded during training. The evaluation on the widely used natural corruption benchmark CIFAR-10-C for VGGNet and PreActResNet has shown the robustness of the smoothed model against natural corruptions.

### Strengths
- **Novel insight**: this paper is the first to leverage model calibration method to mitigate natural corruptions. 
- **Promising experiment results**: the leveraged SWAG method substantially improves the robustness of CNNs against natural corruptions. 
- **Well-written paper**: the paper is well-organized and easy to follow.

### Weaknesses
 - **Limited technical contribution**: the methodology in Section 3 is originally proposed in SWA and SWAG. This paper has not introduced further adjustment or improvement when applying the method to mitigating natural corruptions. 
- **Lacking theoretical analysis**: the experiments have shown the effectiveness of SWAG in improving the robustness against corruptions. However, no theoretical analysis is provided to help better understand the source of the robustness. The explanation of why SWAG helps is more conceptual, rather than a rigorous mathematical analysis. The paper does not delve into the properties of the loss landscape that SWAG might be exploiting, such as the flatness of the minima or the curvature of the loss surface, to provide a more concrete understanding of the observed robustness. The connection between the Gaussian approximation of the posterior and the robustness is not rigorously established.


### Questions
- For Figure 1, how is the reliability plot plotted? Specifically, which hyper-parameter is adjusted to control the confidence of the model, and how is it adjusted? 
- How does the proposed method perform on larger datasets like ImageNet-C? Can this method survive different set of natural corruptions other than those in CIFAR-10-C, e.g., ImageNet-P, ImageNet-$\bar{C}$ [1]? 



[1] On interaction between augmentations and corruptions in natural corruption robustness. NeurIPS 2021.

### Soundness
2

### Presentation
3

### Contribution
2
