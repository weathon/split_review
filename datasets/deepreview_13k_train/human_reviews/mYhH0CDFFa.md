# Rethinking CNN’s Generalization to Backdoor Attack from Frequency Domain

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Convolutional  neural network  (CNN) is easily affected by backdoor injections, whose models perform normally on clean samples but produce specific outputs on poisoned ones. Most of the existing studies have focused on the effect of trigger feature changes of poisoned samples on model generalization in spatial domain. We focus on the mechanism of CNN memorize poisoned samples in frequency domain, and find that CNN generate generalization to poisoned samples by memorizing the frequency domain distribution of trigger changes. We also explore the influence of trigger perturbations in different frequency domain components on the generalization of poisoned models from visible and invisible backdoor attacks, and prove that high-frequency components are more susceptible to perturbations than low-frequency components. Based on the above fundings, we propose a universal invisible strategy for visible triggers, which can achieve trigger invisibility while maintaining raw attack performance. We also design a novel frequency domain backdoor attack method based on low-frequency semantic information, which can achieve 100\% attack accuracy on multiple models and multiple datasets, and can bypass multiple defenses.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper propose to study the backdoor attack on CNN in frequency domain. It shows that high frequency component are more susceptible to perturbations. It further proposes a strategy for rendering visible backdoor attack invisible and proposes a backdoor attack algorithm based on low-frequency component from target class.

### Strengths
1). It is interesting and novel to study the backdoor attack on CNN in frequency domain. The proposed algorithm utilizing low-frequency component from target class is also interesting. 

2). Overall, the paper is clear and well-written.

### Weaknesses
1). The experiments is not enough to show the effectiveness of the proposed method against defense. For backdoor attacks, it is easy to achieve high ASR with no defense. Though empirical evidences have been provided in Fig.6, I still have doubts on the effectiveness of the propsoed method against defense. It would be more convincing to report the result against some defense methods e.g. the defense methods supported by backdoorbench [1].

2). For the strategy rendering visible backdoor attack invisible, it lacks comparison with other invisible backdoor attacks. Since invisible backdoor attacks mainly rely on the perturbation on high frequency components, what is the relation or difference between visible backdoor attack and invisible backdoor attack after masking the low-frequency perturbation?

3). Fig.4 shows that it requires smaller perturbation on high frequency than on low frequency to achieve high attack success rate. However, when comparing to the original image, since most mass concentrate in low-frequency components, the small perturbation on high frequency might be relatively large comparing to the original image. It might require more results to show that high frequency components are more susceptible to backdoor attack

Overall, I think the experiments in this paper is not sufficient to support the analysis in this paper and verify the effectiveness of the proposed method.

### Questions
As mentioned in the weakness section, I have several questions regarding the experiments in this paper.

1). When rendering visible backdoor attack invisible, what is the relation between the visible backdoor attacks and invisible backdoor attacks?

2). For both the rendering strategy and the proposed backdoor attack algorithm, are they still be effective facing conventional defence methods?

3). It has already been observed that high frequency components are more susceptible to attacks such as adversarial attacks. Is there any new takeaways regarding the backdoor attack?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The study examines how triggers affect CNNs by looking at the frequency domain. The authors found that these triggers change the way images are distributed in this domain, which in turn affects CNN performance. They noted that higher frequencies are more vulnerable to attacks than lower ones. Based on these insights, they developed strategies to hide visible triggers and introduced a new backdoor attack method using low-frequency information. This method was effective against many defenses. The authors also provided ideas for future work, like using different triggers during training and testing. They hope their research encourages more exploration in the area of backdoor attacks and defenses.

### Strengths
1.  This paper adopt a novel perspective of learning the backdoor effect through the lens of frequency domain. Specifically, it is interesting to see how different frequency component affect the attack success rate of in current backdoor attack methods. This research provides an insightful understanding into the intricate dynamics between frequency components and the effectiveness of backdoor attacks.
2. The paper provides detailed experiments that comes with insightful conclusion, which is considered a good contribution to the backdoor community.

### Weaknesses
Two important works on frequency-based backdoor attack are missed:
[1] Zeng, Y., Park, W., Mao, Z.M. and Jia, R., 2021. Rethinking the backdoor attacks' triggers: A frequency perspective. In Proceedings of the IEEE/CVF international conference on computer vision (pp. 16473-16481).
[2] Feng, Y., Ma, B., Zhang, J., Zhao, S., Xia, Y. and Tao, D., FIBA: Frequency-Injection based Backdoor Attack in Medical Image Analysis Supplementary Material.
The paper should clearly state the differences between the current work and these previous works.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigate CNN's generalization to backdoor attack in the frequency domain. Based on the fact that high frequencies are more easily perturbed and have higher attack efficiency. They designed an algorithm to convert visible triggers into invisible triggers and also a backdoor attack in the frequency domain.

### Strengths
1. This paper is well organized.

2. The both proposed algorithms are well-motivated.

### Weaknesses
1. The authors claimed that "backdoor attack and defense from a frequency domain perspective is
still insufficient", but IMHO, their literature review is insufficient. Recently, there are many researches about backdoor attacks in the frequency domain. The authors only mentioned one work [1], please discuss more related works such as [2,3,4]. By the way, adversarial attack (aka evasion attack) is closely related to backdoor attack, and there are even more adversarial attacks [5,6] in the frequency domain, and I noticed that the proposed algorithms shown in Figure 5(b) share some similarities with f-mixup in [6].

2. [7,8] has already provided comprehensive analyses about CNN's generalization in the frequency domain, I think most conclusions reached in Section 3 may also be derived from the previous work. In other words, this paper does not provide enough new insights as the authors claimed.

3. The proposed attack is motivated by frequency domain analysis for CNNs , but ViT has different bias in the frequency domain [9], which means that the proposed method may not generalize to ViT. IMHO, this is a great limitation.

4. The authors conducted experiments on MNIST, CIFAR-10 and Celeba, it is necessary to validate the proposed algorithms on ImageNet. In my experience, CNNs trained on ImageNet is far less sensitive to high frequencies than CNNs trained on the above datasets.

Overall, although I think this work is interesting, the current manuscript seems to not achieve the bar of ICLR in 2024.

### Questions
Please see weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the mechanism of CNN memorize poisoned samples in the frequency domain, and finds that CNN generate generalization to poisoned samples by memorizing the frequency domain distribution of trigger changes. It proposes a universal invisible strategy for visible triggers, which can achieve trigger invisibility while maintaining raw attack performance. It also designs a novel frequency domain backdoor attack method based on low-frequency semantic information. The main contributions of this paper are:
- It explores the mechanism of CNN memorization for poisoned images from a frequency domain perspective, investigating the generalization of CNN with respect to perturbations in different frequency domains. 
- It explores the generalization of CNN for visible and invisible triggers, demonstrating that high-frequency features are more susceptible to perturbations than low-frequency features. 
- It proposes a generalized strategy for rendering visible backdoor attacks invisible while maintaining algorithmic performance. 
- It proposes a backdoor attack algorithm based on low-frequency semantic information for target classes, achieving high success rates across diverse datasets and models.

### Strengths
The main strengths of the paper are:
- The paper is well-organized and clearly written, which is easy to follow.
- This paper provides novel perspectives for backdoor attacks on CNN.
- Experimental results are promising and can validate the effectiveness of the proposed method.

### Weaknesses
The weaknesses of the paper are:
- The motivation of this paper is unclear. The authors mention some related work about CNN and backdoor attacks, and they put forward their findings and the proposed methods. However, the necessity and urgency of the proposed method are still unclear. The authors should further clarify the motivation of the paper. Specifically, while the paper touches on the frequency domain analysis of CNNs, it does not adequately explain why analyzing backdoor attacks in the frequency domain is a crucial next step. The connection between frequency domain characteristics and the practical implications for backdoor attacks needs to be more explicitly established. The paper needs to articulate what limitations of existing spatial domain methods are overcome by this frequency domain approach, and why those limitations are significant.
- The dataset used in the paper is relatively small, which is not sufficient to reflect the generalization of the experiment. The author should conduct experimental observations on more generalized datasets such as ImageNet. The current experiments are limited to relatively simple datasets and do not provide sufficient evidence that the proposed method will generalize well to more complex, real-world scenarios. The lack of experiments on larger, more diverse datasets like ImageNet raises concerns about the practical applicability of the proposed method.

### Questions
- Q1. The motivation of this paper is unclear. The authors mention some related work about CNN and backdoor attacks, and they put forward their findings and the proposed methods. However, the necessity and urgency of the proposed method are still unclear. The authors should further clarify the motivation of the paper.
- Q2. The dataset used in the paper is relatively small, which is not sufficient to reflect the generalization of the experiment. The author should conduct experimental observations on more generalized datasets such as ImageNet.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
