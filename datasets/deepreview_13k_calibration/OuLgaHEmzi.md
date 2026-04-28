# Endowing Visual Reprogramming with Adversarial Robustness

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Visual reprogramming (VR) leverages well-developed pre-trained models (e.g., a pre-trained classifier on ImageNet) to tackle target tasks (e.g., a traffic sign recognition task), without the need for training from scratch. Despite the effectiveness of previous VR methods, all of them did not consider the adversarial robustness of reprogrammed models against adversarial attacks, which could lead to unpredictable problems in safety-crucial target tasks. In this paper, we empirically find that reprogramming pre-trained models with adversarial robustness and incorporating adversarial samples from the target task during reprogramming can both improve the adversarial robustness of reprogrammed models. Furthermore, we propose a theoretically guaranteed adversarial robustness risk upper bound for VR, which validates our empirical findings and could provide a theoretical foundation for future research. Extensive experiments demonstrate that by adopting the strategies revealed in our empirical findings, the adversarial robustness of reprogrammed models can be enhanced.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper delves into the adversarial robustness of visual reprogramming. It first highlights the adversarial vulnerability of existing VR methods and proposes to alleviate this issue with two strategies, adopting adversarial trained models and adversarial training in VR. A theoretical analysis is also provided to support the practices.

### Strengths
1. The adversarial robustness of visual reprogramming is a critical issue.
2. The proposed methods significantly improve the adversarial robustness.
3. The theoretical upper bound of adversarial risks is straightforward yet valuable, validating the empricial findings.
4. Multiple strategies of VR are considered in experiments.

### Weaknesses
1. The two proposed strategies are mature techniques in the field. Technically, it's simply an extension to visual reprogramming and there are no surprising results. Meanwhile, as the number of learnable parameters in visual reprogramming is limited, adversarial training may not be an ideal solution to improve the robustness.
2. Although the theoretical analysis correponds to the proposed strategies, the AMDD-VRA part, which takes up the most context, is not reflected or applied in practice. This term seems to be the most important factor in VR, which is neither taken into consideration in methods nor discussed based on experimental results. For instance, the performance-robustness trade-off on GT-SRB is more noticeable than that on CIFAR. Does it has anything to do with the gap between the source domain and the target domain?
3. There can be more discussions on the recent advancements in Visual Reprogramming and Visual Prompting. For instance, [1] has studied VP with adversarial robustness, what's the difference between your work and theirs. Also, [2] has extended VP to visual foundation models, is your work applicable to more significant scenarios like MLLMs?

Minor: There are some typos in submission, e.g., 'iss' in line 191.

### Questions
1. Why $f_{out}$ is concatenated to $f_\mathcal{S}$ in the last term of the equation in Definition 1 ? Is there any intuitive explanation on why the source domain $\mathcal{S}$ should also be mapped to the $\mathbb{R}^\mathcal{T}$ ?

I will raise my rating if the authors can properly addressed my concerns.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper focuses on the adversarial robustness of visual reprogramming (VR) against adversarial attacks. To this end, it first empirically finds that reprogramming pre-trained models with adversarial robustness and incorporating adversarial samples from the target task during reprogramming can both improve the adversarial robustness of reprogrammed models. Furthermore, it also presents a theoretically guaranteed adversarial robustness risk upper bound for VR. Experiments on several benchmarks validate the effectiveness of the proposed method.

### Strengths
1. The proposed method is interesting. The paper is well-written, and easy to understand.
2. The authors introduced an upper bound for the adversarial robustness risk in visual reprogramming, theoretically proving the effectiveness of the proposed method.
3. Extensive comparative experiments were conducted on multiple datasets, showcasing the performance of the proposed method across different attack iteration numbers and perturbation sizes.

### Weaknesses
1. The technical novelty of this paper is limited. The modules for visual programming, such as input transformation and label mapping, are similar to (Chen, 2022; Cai et al. 2024). And those modules for adversarial robustness also have been proposed by previous literature (Madry et al. 2018; Zhang et al., 2019a)
2. I'm a little confused about the task setting, especially in the availability of adversarially pre-trained models. For the source domain, it may not be practical to have both a pre-trained model and an adversarially pre-trained model. Obviously, we can’t temporarily train a source model via adversarial training. if we can, why don't we train a target model directly with clean and adversarial data, because both datasets are also available?
3. Experiments in Sec. 5 are more like ablation studies, to discuss the effectiveness of different designs for the proposed framework. However, it lacks comparisons with kinds of baselines or SOTA methods. Moreover, it would be more significant to evaluate the proposed method with more complex models on more large datasets, because that is the point of visual reprogramming to reduce the training and storage costs for target domains.
4. In Eq. 10, $\Phi_{\rho}$ has two input variables (i.e., $x$ and $y$), but in the definition of Eq. 11, it only has one.

### Questions
Please see the Weaknesses for details.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The goal of Visual reprogramming is re-purposing pre-trained models for new tasks without retraining the model itself, and only learning a lightweight visual input transformation and label remapping of the output. Prior works have used different kinds of input transforms, remapping functions, losses etc, while this work focuses on the adversarial robustness aspect. The authors find that reprogramming naturally trained models results in almost zero robustness against adversarial attacks. Empirically, the paper demonstrates that using adversarially pre-trained models as the backbone for reprogramming and using adversarial training during the reprogramming both improve robustness. Combining both strategies (adversarially pre-trained backbones + adversarial training) yields the best results. The paper also provides some theoretical lemmas and proofs to establish an upper bound for adversarial risk of visual reprogramming.

### Strengths
+ The paper is easy to follow 

+ The work explores different combinations of input transformations and label remapping techniques, which strengthens confidence in the results.

### Weaknesses
 - Limited novelty, the main component of the method is using adversarially pre-trained backbones, and using adversarial training during visual re-programming, which is a direct application of prior work.

- The theoretical portion of the paper tries to tackle an interesting question, however the relevance to the method is limited ? The method itself is very empirical and intuitive, and the theory seems like an afterthought.

- Though the authors demonstrate results on various input transform/label mapping techniques, in terms of backbones only ResNet18 is used, and only on CIFAR-10/100 and GTSRB datasets, which consist of small images, which is qualitatively different from practical image recognition tasks.

### Questions
1. The authors could clarify more on how their theoretical work on guaranteed adversarial robustness risk upper bound affects their method and potentially what are the implications of their proof for this task

2. Would these results generalize to more practical datasets such as ImageNet and recent models such as VisionTransformers, which have very different robustness characteristics than CNNs ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the adversarial robustness of visual reprogramming (VR), a method that adapts pre-trained models for new tasks without fine-tuning. The authors find that existing VR methods are vulnerable to adversarial attacks, but can be significantly improved by using adversarially robust pre-trained models and incorporating adversarial examples from the target task during reprogramming. The paper presents a theoretical analysis that bounds the adversarial risk of VR and provides a foundation for future research. Experiments demonstrate the effectiveness of the proposed strategies in enhancing the robustness of reprogrammed models.

### Strengths
- Pioneering exploration of VR's adversarial robustness: This paper is the first to focus on the vulnerability of VR models when facing adversarial attacks and proposes corresponding solutions, filling a gap in this field.
- The article not only experimentally verifies that using adversarial pre-trained models and adversarial samples can improve the adversarial robustness of VR models but also proposes a theoretical guarantee of an adversarial robustness risk upper bound, providing a theoretical foundation for future research.

### Weaknesses
 - I am concerned about the application scenarios of the proposed method. Visual reprogramming aims to leverage less data and computational resource overhead to stimulate the base model's capabilities on target tasks, which means that timeliness and performance are more important than adversarial robustness. The methods proposed in the article hinder these two aspects to some extent.
- The paper primarily uses the projected gradient descent (PGD) method to generate adversarial samples. However, different generation methods may have different impacts on the model's robustness, and there is a lack of discussion on more adversarial sample generation methods.
- This work focuses on classification accuracy on adversarial samples, but adversarial robustness is a multidimensional concept that requires more comprehensive evaluation metrics. Adversarial training has some limitations, such as high computational costs and the risk of overfitting, which require more discussion.

### Questions
The paper focuses on image classification tasks. VR can be applied to a wider range of tasks, such as object detection and semantic segmentation. Can the methods in this article be extended to other downstream tasks?

### Soundness
3

### Presentation
3

### Contribution
2
