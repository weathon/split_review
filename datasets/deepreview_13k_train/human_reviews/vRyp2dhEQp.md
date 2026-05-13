# Efficient Backdoor Attacks for Deep Neural Networks in Real-world Scenarios

- Decision: Accept
- Scores: 6, 3, 8, 6

## Abstract
Recent deep neural networks (DNNs) have came to rely on vast amounts of training data, providing an opportunity for malicious attackers to exploit and contaminate the data to carry out backdoor attacks. However, existing backdoor attack methods make unrealistic assumptions, assuming that all training data comes from a single source and that attackers have full access to the training data. In this paper, we introduce a more realistic attack scenario where victims collect data from multiple sources, and attackers cannot access the complete training data. We refer to this scenario as \textbf{data-constrained backdoor attacks}. In such cases, previous attack methods suffer from severe efficiency degradation due to the \textbf{entanglement} between benign and poisoning features during the backdoor injection process. To tackle this problem, we introduce three CLIP-based technologies from two distinct streams: \textit{Clean Feature Suppression} and \textit{Poisoning Feature Augmentation}.
The results demonstrate remarkable improvements, with some settings achieving over $\textbf{100\%}$ improvement compared to existing attacks in data-constrained scenarios. %Our research contributes to addressing the limitations of existing methods and provides a practical and effective solution for data-constrained backdoor attacks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses an important and practical backdoor attack scenario called data-constrained backdoor attacks. The key insight is that in real-world settings, attackers often do not have full access to a victim's entire training dataset, which spans multiple sources. The paper clearly defines three variants of data-constrained attacks based on restrictions on the number of poisoning samples, classes, or domains.
A thorough set of experiments on CIFAR and ImageNet datasets demonstrates that existing backdoor methods like BadNets and Blended attacks fail under data constraints, due to entanglement between benign and poisoning features. The analysis of this entanglement issue is a nice contribution. To address this limitation, the authors cleverly utilize CLIP in two ways: 1. Clean feature suppression via CLIP-CFE to erase benign features.
2. Poisoning feature augmentation via CLIP-UAP and CLIP-CFA to amplify poisoning features.
The introduction of CLIP for backdoor attacks is novel. Results show CLIP-UAP and CLIP-CFA consistently outperform baseline triggers across constraints, architectures, and datasets. CLIP-CFE provides further improvements in attack success rate. The attacks remain stealthy and do not impact benign accuracy.

### Strengths
1.	Addresses a highly practical attack scenario of data-constrained backdoor attacks that reflects real-world training environments where attackers have limited data control.
2.	Provides a clear taxonomy of data-constrained attacks based on restrictions to number of samples, classes, and domains.
3.	Identifies through analysis and experiments that existing attacks fail under data constraints due to entanglement of benign and poisoning features. This is an important insight.

### Weaknesses
1.	While the data-constrained scenario is practical, the specific sub-variants of number, class, and domain constraints may not fully capture all real-world limitations an attacker could face. More complex constraints could be studied. For instance, the interaction between these constraints (e.g., a limited number of samples across a small subset of classes from a specific domain) is not explored, which could reveal further vulnerabilities or limitations of the proposed approach. The current constraints are somewhat orthogonal, and a more realistic attacker might face a combination of these limitations simultaneously.
2.	The computational overhead and time required for the CLIP optimization process is not extensively analyzed. While the paper mentions the use of CLIP, it does not delve into the specific computational resources required for the optimization steps, such as the number of gradient updates or the memory footprint. This is crucial for assessing the practicality of the attack, especially when considering real-world scenarios with limited computational resources. The paper should provide a more detailed analysis of the time complexity and resource requirements of the proposed methods.
3.	The stealthiness metrics mainly rely on signal processing based measures like PSNR and SSIM. While these metrics provide a quantitative measure of pixel-level differences, they do not fully capture the perceptual stealthiness of the attack. More rigorous stealthiness analysis like visualizations and defense evaluations may be beneficial. For example, the paper could include visualizations of the poisoned images to allow for a qualitative assessment of the trigger's visibility. Furthermore, evaluating the attack's resilience against existing backdoor detection and defense methods would provide a more comprehensive understanding of its stealthiness.

### Questions
see in weakness

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper assumed a threat model for backdoor attacks, so-called as ‘data-constrained backdoor attacks’, where the attacker doesn’t have access to the entire training dataset. Then, the authors claimed that the exiting backdoor attacks are inefficient in this new threat model.

### Strengths
The authors considered an interesting topic on AI security, specifically, how to improve the backdoor efficiency in a data-constrained scenario.

### Weaknesses
First, the authors only provided the empirical results to support the performance decline when the exiting backdoor attack in the new threat model, as shown in Fig.2. I highly recommend that the authors give a possible theoretical analysis to this phenomenon.

Secondly, the new proposed 'clip-guided backdoor attack' method includes two components: clean feature suppression and poisoning feature augmentation. Specifically, the main idea is to exploit adversarial example to generate the noise to suppress the clean feature or amplify the poison feature. Unfortunately, as far as I know this idea has been exploited by many published papers, for instance, as shown as follows. The main difference of this paper is that it is based on a novel pre-trained model CLIP.

[1] Zhao, Shihao, et al. "Clean-label backdoor attacks on video recognition models." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2020.
[2] Turner, D. Tsipras, and A. Madry, “Label-consistent backdoor attacks,” arXiv preprint arXiv:1912.02771, 2019.

In summary, the main idea has been exploited already, which will significantly reduce the contribution of this paper.

### Questions
What is the main difference between the 'clip-guided backdoor attack' with the existing references which have been mentioned in the 'weaknesses'

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new backdoor attack that performs well in data-constraint conditions that are more akin to real-world scenarios. The attack uses the CLIP model as a feature extractor to diminish the entanglement between benign and poison features. The experiment results show significant improvement compared to previous methods in these more realistic conductions.

### Strengths
- A novel approach to backdoor attack
- Comprehensive evaluations

### Weaknesses
 - CLIP limits the application domain
- Defense discussion missing
- Runtime information missing

- The usage of the CLIP model for backdoor attacks is indeed novel. However, this also limits the domains of possible application of the attack. While the method seems to perform well on datasets with natural sceneries, such as CIFAR-100, CIFAR-10, and ImageNet-50, the performance cannot be guaranteed on datasets where the domain drastically differs from CLIP’s training set, such as medical scans, satellite imageries, etc. Additionally, even for similar domains, it would be interesting to see if the feature extraction capabilities transfer onto fine-grained datasets, such as CUB-200-2011, Stanford-Cars, Oxford-Flowers, etc. The authors should consider including results on more diverse datasets.

- The target models used in this paper are all relatively simple/small (experimental settings focused). They also differ drastically from the CLIP model both in terms of architecture and performance. The authors have already pointed out the effect of model architecture in Section 5.1. Evaluating the attack on more advanced and larger architectures, such as ViT, can further prove the author’s claim for applicability in real-world scenarios.

- Discussion regarding potential defenses is also missing. It would be interesting to see how this new attack performs against backdoor detection or defense methods. Since the optimization suppresses the clean features and augments the poison features, defense/detection methods that rely on optimization, such as Neural Cleanse[1] could potentially be more effective (compared to defending against traditional backdoor attacks). Furthermore, a recent work[2] on backdoor defense seems to use similar intuition (detangling benign and poison features). It would be interesting to see how this defense performs against an attack that is intuitively similar.  
[1]Wang et al. Neural cleanse: Identifying and mitigating backdoor attacks in neural networks. 2019. In IEEE Symposium on Security and Privacy (S&P).  
[2]Min et al. Towards Stable Backdoor Purification through Feature Shift Tuning. 2023. arXiv preprint arXiv:2310.01875.

- Considering the optimization process needed to conduct this attack, the authors should consider including relevant runtime information. Since the focus of this paper is on presenting a backdoor attack that is applicable in real-world scenarios, the computing resource required can be another limiting factor. 

Minors:

- Fonts in figures are too small to be legible
- Page 8, VGG-16 datasets? (should be models)

### Questions
The authors present a novel backdoor attack that utilizes the pre-trained CLIP model as a feature extractor to suppress benign features and accentuate poison features. The attack also relaxes previous assumptions that having knowledge of the training datasets and the target models trained on datasets from one distribution. The authors show previous methods do not perform well in these more realistic scenarios but their new method is consistently effective and the trigger is hard to detect visually. Overall, the paper is well-written and the evaluation is comprehensive. However, there are a few points I would like to see the authors to further address.

- The usage of the CLIP model for backdoor attacks is indeed novel. However, this also limits the domains of possible application of the attack. While the method seems to perform well on datasets with natural sceneries, such as CIFAR-100, CIFAR-10, and ImageNet-50, the performance cannot be guaranteed on datasets where the domain drastically differs from CLIP’s training set, such as medical scans, satellite imageries, etc. Additionally, even for similar domains, it would be interesting to see if the feature extraction capabilities transfer onto fine-grained datasets, such as CUB-200-2011, Stanford-Cars, Oxford-Flowers, etc. The authors should consider including results on more diverse datasets.

- The target models used in this paper are all relatively simple/small (experimental settings focused). They also differ drastically from the CLIP model both in terms of architecture and performance. The authors have already pointed out the effect of model architecture in Section 5.1. Evaluating the attack on more advanced and larger architectures, such as ViT, can further prove the author’s claim for applicability in real-world scenarios.

- Discussion regarding potential defenses is also missing. It would be interesting to see how this new attack performs against backdoor detection or defense methods. Since the optimization suppresses the clean features and augments the poison features, defense/detection methods that rely on optimization, such as Neural Cleanse[1] could potentially be more effective (compared to defending against traditional backdoor attacks). Furthermore, a recent work[2] on backdoor defense seems to use similar intuition (detangling benign and poison features). It would be interesting to see how this defense performs against an attack that is intuitively similar.  
[1]Wang et al. Neural cleanse: Identifying and mitigating backdoor attacks in neural networks. 2019. In IEEE Symposium on Security and Privacy (S&P).  
[2]Min et al. Towards Stable Backdoor Purification through Feature Shift Tuning. 2023. arXiv preprint arXiv:2310.01875.

- Considering the optimization process needed to conduct this attack, the authors should consider including relevant runtime information. Since the focus of this paper is on presenting a backdoor attack that is applicable in real-world scenarios, the computing resource required can be another limiting factor. 

Minors:

- Fonts in figures are too small to be legible
- Page 8, VGG-16 datasets? (should be models)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The submission focuses on the backdoor attacks in data-constrained scenarios. By leveraging CLIP-based technologies, the proposed CLIP-CFE (CLIP for Clean Feature Erasing) suppresses clean features while amplifying poisoning features to achieve more efficient attack with limited poisoning samples.

### Strengths
+ The submission presents a novel method, which introduces the optimized feature erasing noise to effectively suppress benign features. Besides, it enhances the poisoning features through contrastive learning and amplifies the existing backdoor attacks efficiently in data-constrained scenarios.

+ The experimental results demonstrate the effectiveness of the CLIP-based attacks in data-constrained scenarios. Across various real-world constraints such as *number-constrained, class-constrained*, and *domain-constrained* conditions, the proposed backdoor attack consistently achieves a high attack success rate while maintaining the benign accuracy.

### Weaknesses
 + **Insufficient experimental results**

The submission should take more recent backdoor attack and defense mechanisms into consideration while discussing the adaptive defenses more thoroughly, e.g., the noise used for erasing benign features might be unlearned [1, 2]. Besides, it is necessary to compare the effectiveness of utilizing different proxy extractors other than CLIP.


+ **Ambiguous expressions**

Several points in the submission need further explanation, e.g., the reason and effect of choosing the overall attack process relying on the style of CLIP within the feature space, and the analysis of erasing benign features compared to the semantic-agnostic out-of-domain samples.

### Questions
Given that the submission's motivation is related to data-constrained scenarios, the author may provide more empirical evidence regarding to the occurrence of these backdoor attacks in real-world scenarios.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
