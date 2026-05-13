# Grond: A Stealthy Backdoor Attack in Model Parameter Space

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
Recent research on backdoor attacks mainly focuses on invisible triggers in input space and inseparable backdoor representations in feature space
to increase the backdoor stealthiness against defenses.
We examine common backdoor attack practices that look at input-space or feature-space stealthiness and show that state-of-the-art stealthy input-space and feature-space backdoor attacks can be easily spotted by examining the parameter space of the backdoored model. 
Leveraging our observations on the behavior of the defenses in the parameter space, we propose a novel clean-label backdoor attack called Grond. 
We present extensive experiments showing that Grond outperforms state-of-the-art backdoor attacks on CIFAR-10, GTSRB, and a subset of ImageNet. 
Our attack limits the parameter changes through Adversarial Backdoor Injection, adaptively increasing the parameter-space stealthiness.
Finally, we show how combining Grond's Adversarial Backdoor Injection with commonly used attacks can consistently improve their effectiveness.
Our code is available at \url{https://anonymous.4open.science/r/grond-557F}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose a backdoor attack against image classification models that improves robustness and stealthiness. Current backdoor attacks are "easily spotted by examining the parameter space". The authors propose an Adversarial Backdoor Injection method that prunes weights of the backdoored network after each training epoch whenever they deviate too strongly from the mean weight within each layer. The authors evaluate their attack on relatively small-scale image datasets, such as CIFAR-10 and a 200-class subset of ImageNet, which includes nine backdoor removal and seven backdoor detection methods. The results show their attack is robust and undetectable against all surveyed defences.

### Strengths
- Effectiveness: The paper's results are promising and show improvement over other attacks in all dimensions. 
- Ablation studies: The authors conducted extensive experiments across multiple datasets (CIFAR-10, GTSRB, ImageNet200) and architectures to analyse their attack’s effectiveness. 
- Presentation: The methodology and results are presented clearly, making the paper easy to follow.

### Weaknesses
 - Lack of Novelty: The approach of pruning weights to enhance stealth is not particularly original and provides only limited new insights into defending against these types of attacks. This limits the novelty of the proposed method.

- Assumption of a Strong Attacker: The paper assumes a white-box threat model with complete control over the training process. This setting, also known as a ‘supply chain attack’ [A], is extremely challenging (hopeless?) to defend against. It may not represent more realistic attacks or limited-access scenarios. This was stated in previous works [A] and others even show that provably undetectable backdoors can be implanted into models in this setting [B].

- Lack of theoretical insights: There are no clear reasons why Grond should perform better than existing attacks, and the authors do not provide insights on the 'why' question. 

- Lack of adaptive defenders: From a security perspective, it appears that Grond does not evaluate an adaptive defender who knows the attack strategy used by Grond. For instance, pruning weights in the way the authors proposed could make the attack detectable.

### Questions
- Why does Grond work better than any other method?

- Why is the white-box setting significant?

- Do adaptive defenders exist that can detect or remove Grond?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a new clean-label backdoor attack that achieves stealthiness in both the input space and the parameter space. Specifically, to achieve the stealthiness in the input space, the paper utilizes the targeted universal adversarial perturbation as the backdoor trigger. For the parameter-space stealthiness, the paper restricts the magnitude of model weight parameters by setting particularly large weights to the mean value of the corresponding layer. The evaluation is conducted on three standard benchmarks. Comparing to existing backdoor attacks, the proposed attack is more resilient to existing defense and detection methods.

### Strengths
1. The studied topic is important as backdoor attacks can exploit the integrity of deployed deep learning models and cause unexpected consequences.
2. The paper is overall easy to understand.

### Weaknesses
1. The proposed attack utilizes the targeted universal adversarial perturbation as the backdoor trigger, which is the same as an existing work [1]. To increase the stealthiness of the attack in the parameter space, the paper uses backdoor defenses to help reduce backdoor-related neurons. This technique has already been proposed in the literature [2]. The proposed attack is just a collection of existing techniques. The novelty is very limited.
2. The paper assumes that the attacker has white-box access to the training processes, meaning that the attacker has whole control over the training. And yet, the paper chooses a clean-label attack, which is quite strange. The introduction of clean-label attacks is to simulate the scenario where adversaries have no control over the labeling and training procedures. The attacker can only modify a subset of the training images, making it a realistic threat model. Since this paper assumes white-box access to the training processes, there is no need to use the clean-label setting. Can the authors explain why such a setting is needed for a successful attack?
3. According to Figure 2, the mask loss for the proposed backdoor attack is much lower than benign cases. Cannot one design a defense method by measuring the outliers of the mask loss? Clearly the mask loss for the proposed attack is much smaller, which can be easily detected.
4. Following the above point, there is no evaluation on adaptive defenses, where the defender has the knowledge of the proposed attack. Since the proposed attack uses a small-size trigger with epsilon equal to 8, simple defenses can be existing adversarial detection methods and/or (universal) adversarial training. Another defense approach could be randomly perturbing the weight parameters. As the proposed attack reduces backdoor weights, the backdoor effect may be quite brittle when weights are perturbed.

### Questions
Please see above comments.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents Grond, a backdoor attack that achieves enhanced stealth across input, feature, and parameter spaces to avoid detection. Through Adversarial Backdoor Injection, Grond disperses backdoor effects across multiple neurons, making it harder to identify using parameter-space defenses. Extensive experiments on datasets like CIFAR-10, GTSRB, and ImageNet200 show that Grond outperforms other attacks in evading both pruning and fine-tuning-based defenses, highlighting its robustness and adaptability.

### Strengths
This paper introduces Grond, a novel backdoor attack with comprehensive stealth across input, feature, and parameter spaces. Using Adversarial Backdoor Injection, Grond disperses backdoor effects across neurons, enhancing its stealth and evading parameter-space defenses. Extensive testing on multiple datasets (CIFAR-10, GTSRB, ImageNet200) and defenses demonstrates Grond's effectiveness and adaptability across diverse scenarios and model architectures.

### Weaknesses
1. Limited Threat Model in Terms of Defender Capabilities: The paper's threat model lacks a thorough consideration of the defender’s capabilities, particularly regarding proactive measures they could take to identify and mitigate backdoors prior to deployment. This omission may limit the applicability of the model to real-world scenarios where defenders could leverage more advanced tools and strategies. Specifically, the threat model does not account for defenders employing techniques such as analyzing activation patterns or performing statistical analysis on model weights to detect anomalies indicative of backdoors before the model is deployed. This limits the practical relevance of the proposed attack in scenarios where such proactive defenses are in place.
2. Lack of Comparison with Stealthy Clean-Label Backdoor Attacks: The paper does not include a comparison with other existing stealthy clean-label backdoor attacks, such as Hidden Trigger Backdoor Attacks (HTBA). This omission makes it difficult to assess the relative stealthiness of the proposed attack compared to state-of-the-art methods that also aim to minimize the detectability of backdoors in the input space. Without such a comparison, it is unclear whether the proposed method offers a significant advantage in terms of stealth.
3. Limited Range of Defense Methods Evaluated: The paper tests Grond against a small selection of defense methods, primarily focusing on pruning and fine-tuning-based defenses. The evaluation does not include sample-level detection methods, which are crucial for identifying backdoored inputs. This narrow focus limits the evaluation of the attack's robustness against a broader range of defense strategies, particularly those that target the input space directly. The absence of such evaluations raises concerns about the practical resilience of the attack in real-world scenarios where defenders may employ diverse detection mechanisms.

### Questions
Can this type of backdoor attack be detected by sample-based detection defenses?

### Soundness
3

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
In this paper, the researchers propose a new backdoor attack scheme to combat existing defense strategies based on model repairing. The core idea of this scheme is very simple and easy to understand. Specifically, this scheme first generates a trigger using TUAP, and then uses this trigger to poison the model. During the process of implanting the backdoor, it modifies parameters with higher activation values, thereby enhancing the stealth of the backdoor attack in the parameter space. Additionally, experimental results demonstrate the effectiveness of this scheme. However, both trigger generation and adversarial backdoor injection are based on existing works, so the innovation of this research is limited.

### Strengths
The experimental results of this approach are convincing. The results indicate that the approach can bypass existing defense mechanisms while maintaining a high attack success rate.

### Weaknesses
This work lacks novelty because two key steps—trigger generation and adversarial backdoor injection—are based on existing studies [1], [2]. Furthermore, while the authors claim stealthiness in input, feature, and parameter spaces, a closer look at the provided ImageNet200 backdoor samples reveals perceptible perturbations. The authors should provide a more rigorous evaluation of the backdoor image quality, especially when compared to imperceptible backdoor attacks, such as those presented in [3]. The paper also lacks a clear specification of the number of clean samples used in the pruning-based and fine-tuning-based defense experiments, making it difficult to assess the validity of the experimental results.

### Questions
1. The experimental section should clearly specify the number of clean samples used in the pruning-based and fine-tuning-based approaches, which is not clearly stated in the paper. 
2. The authors list some ImageNet200 backdoor samples; however, despite the authors claiming that this backdoor attack is stealthy in input space, feature space, and parameter space, a close examination of these backdoor samples reveals obvious perturbations. The authors should evaluate the quality of the backdoor images, especially in comparison with some imperceptible backdoor attacks, such as [3].
3. It would be more convincing if the authors could provide Grad-CAM images of the backdoor samples and visualise their distribution in feature space.


[1] Moosavi-Dezfooli, Seyed-Mohsen, et al. "Universal adversarial perturbations." Proceedings of the IEEE conference on computer vision and pattern recognition. 2017.
[2] Zheng, Runkai, et al. "Data-free backdoor removal based on channel lipschitzness." European Conference on Computer Vision. Cham: Springer Nature Switzerland, 2022.
[3] Doan, Khoa, et al. "Lira: Learnable, imperceptible and robust backdoor attacks." Proceedings of the IEEE/CVF international conference on computer vision. 2021.

### Soundness
3

### Presentation
3

### Contribution
2
