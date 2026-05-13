# Safe and Robust Watermark Injection with a Single OoD Image

- Decision: Accept
- Scores: 6, 3, 8, 6

## Abstract
Training a high-performance deep neural network requires large amounts of data and computational resources. 
Protecting the intellectual property (IP) and commercial ownership of a deep model is challenging yet increasingly crucial. 
A major stream of watermarking strategies implants verifiable backdoor triggers by poisoning training samples, but these are often unrealistic due to data privacy and safety concerns and are vulnerable to minor model changes such as fine-tuning. 
To overcome these challenges, we propose a safe and robust backdoor-based watermark injection technique that leverages the diverse knowledge from a single out-of-distribution (OoD) image, which serves as a secret key for IP verification. 
The independence of training data makes it agnostic to third-party promises of IP security. 
We induce robustness via random perturbation of model parameters during watermark injection to defend against common watermark removal attacks, including fine-tuning, pruning, and model extraction. 
Our experimental results demonstrate that the proposed watermarking approach is not only time- and sample-efficient without training data, but also robust against the watermark removal attacks above.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel method for watermarking deep neural networks to protect their intellectual property and commercial ownership. Traditional watermarking strategies involve adding backdoor triggers to training samples, but these methods have limitations in terms of data privacy, safety concerns, and vulnerability to model changes. In contrast, the proposed technique leverages the knowledge from a single out-of-distribution image as a secret key for IP verification. The proposed method can immune to third-party promises of IP security. The watermark is injected by perturbing the model parameters randomly, which enhances robustness against common watermark removal attacks such as fine-tuning, pruning, and model extraction. The experimental results show that the proposed watermarking approach works well without requiring additional training data. Furthermore, it demonstrates robustness against the watermark removal attacks.

### Strengths
IP Protection: The paper addresses the challenge of protecting the intellectual property of deep neural networks, which is increasingly crucial in the field. It has attracted increasing attentions in the literature, especially in the era of foundation models. This paper considers an important problem, potentially having large impact to the community. 

Safe and Robust Technique: The proposed technique claims to be safe and robust. It leverages a single out-of-distribution (OoD) image as a secret key for IP verification. This approach avoids privacy and safety concerns associated with poisoning training samples. By inducing random perturbations of model parameters during watermark injection, it aims to defend against common watermark removal attacks such as fine-tuning, pruning, and model extraction.

Agnostic to Third-party Promises: The technique is described as agnostic to third-party promises of IP security. This suggests that the proposed approach does not rely on external entities or services for ensuring IP protection, which can be beneficial in scenarios where trust in third parties is limited.

Time- and Sample-Efficient: The proposed watermarking approach is claimed to be time- and sample-efficient without requiring additional training data. This could be advantageous as it reduces the computational resources needed for watermarking.

### Weaknesses
Training time watermarked data will have some distribution discrepancy over test situations, thus one cannot ensure the performance of watermarking. It seems that such an issue remains an open question in IP protection, so more discussion about "how to handle such a problem" or "is it an important issue in the literature" can be formally discussed.

Do more data points, other than just one point, will lead to more contributions to the watermarking strategy? Experimental verification and heuristic explanation seem to be interesting. More ablation studies, such as number of data points, hyper parameter setting, choice of validation set, and effects of individual modules, can be presented, which can largely improve the solidity of this paper.

For the first equation in Sec 3.1, I am not sure if the first term is contributive. In previous works of watermarking, the first term is used to ensure the original high performance for the original task (I guess). Therefore, from my view, the first term is not important, especially considering the fact that x does not follow the same distribution of original data distribution, and no semantic information should be kept therein.

A related question  is that does the watermarking strategy suffer from catastrophic forgetting? In other words, does learning from tilde D impact the performance for the original task, especially for foundation models. More discussion and empirical justification should be given here. Another related issue is that, it seems that this paper is motivated by the recent progress in foundation models, but it seems that this paper does not provide enough evaluation for the power of watermarking with backbones of foundation models.

In previous works, researchers demonstrate that weight perturbation can lead to data transformation [1]. Therefore, the reason  why the suggested method works may also be explained from the perspective of implicitly introducing more data.  Another related question is that if introducing more data can also mitigate the impact of watermarking removing. More discussion and evaluation should be considered here.

### Questions
Please see the weaknesses above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new method to inject watermarks into the DNN models by leveraging only one out-of-distribution image. It first crops some patches from the selected image, augments, and adds trigger patterns on some of them as the trigger images. The rest of the patches are also augmented but not injected with the trigger patterns, and used as the data to retain the main functionality of the target model. Then, it jointly fine-tunes the target model using the two parts of augmented data. Meanwhile, in order to improve the watermark robustness under the watermark removal attacks, the authors propose to randomly add perturbations to the model weights during fine-tuning. The authors claim they can achieve a better performance compared with that implemented using basic backdoor-based methods.

### Strengths
The proposed approach is interesting, and the paper is easy to follow.

### Weaknesses
1. The authors do not give a comprehensive discussion of previous work on this topic. 

2. The experimental justification of this work is not sufficient, only compared to the basic backdoor-based strategy.

3. On page 5. The statement of ‘the anomalies of the parameter distribution could be easily detected by an IP infringer’ may be conflict with the experimental results of Ref. [1]. The authors of Ref. [1] conduct experiments to check whether the distributions of model weights or model representations could be used as indicators to detect backdoors or anomalies in a DNN model. 

4. Experimental settings are not clear enough: 1) How many patches are used for training? 2) Comparison experiments are not well organized. There are many previous methods with similar strategies, e.g., BadNets, 10-invisible, smooth, Trojan Square, and Trojan watermark, and it's essential to compare with them. 

5. In Table 2, we observe that the OoDWSR may increase after fine-tuning and pruning. Could you give some explanations? It seems the IDWSR may also increase after such two attacks. Why? It seems to be contradicted by your previous claim.

6. How did you implement the model extraction attack? According to the experimental results in Table 4, we still have a high OoDWSR after model extraction. Could you explain why the model extraction methods using i.i.d data can also extract the watermarks that are generated using the OoD data?

### Questions
The questions are listed based on the organization order of the paper:

1. On page 2. ‘…, which fills in the gap of IP protection of deep models without training data’. Most of the white-box watermarking methods do not need the training data, you should make it clear that you target the backdoor-based methods.

2. On page 5. ‘If the protected model shares a similar parameter distribution with the pre-trained model, the injected watermark could be easily erased by fine-tuning using clean i.i.d. data or adding random noise to parameters’. What is the pre-trained model? Does it mean that fine-tuning with the i.i.d data can introduce more perturbations on the watermarks than fine-tuning with OoD data? What’s the intuition behind such an claim? 

3. On page 5. The statement of ‘the anomalies of the parameter distribution could be easily detected by an IP infringer’ may be conflict with the experimental results of Ref. [1]. The authors of Ref. [1] conduct experiments to check whether the distributions of model weights or model representations could be used as indicators to detect backdoors or anomalies in a DNN model. 

4. Experimental settings are not clear enough: 1) How many patches are used for training? 2) Comparison experiments are not well organized. There are many previous methods with similar strategies, e.g., BadNets, 10-invisible, smooth, Trojan Square, and Trojan watermark, and it's essential to compare with them. 

5. In Table 2, we observe that the OoDWSR may increase after fine-tuning and pruning. Could you give some explanations? It seems the IDWSR may also increase after such two attacks. Why? It seems to be contradicted by your previous claim.

6. How did you implement the model extraction attack? According to the experimental results in Table 4, we still have a high OoDWSR after model extraction. Could you explain why the model extraction methods using i.i.d data can also extract the watermarks that are generated using the OoD data?

[1] Ji, Y., Liu, Z., Hu, X., Wang, P., & Zhang, Y. (2019). Programmable neural network trojan for pre-trained feature extractor. *arXiv preprint arXiv:1901.07766*.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel technique for protecting the intellectual property of deep models using a single out-of-distribution image as a secret key. The proposed technique is safe and robust against watermark removal attacks and does not require poisoning training samples.

### Strengths
The main strength of this paper is the proposal of a novel technique for protecting the intellectual property of deep models using a single out-of-distribution (OoD) image as a secret key. The proposed technique is robust against watermark removal attacks and does not require poisoning training samples. The paper has great clarity and is easy to follow. The proposed technique looks promising for protecting the commercial ownership of deep models, which require large amounts of data and computational resources to train.

The main technical difference between this work and prior work is the use of a single OoD image as a secret key for watermark injection. Prior work on watermarking strategies often implants verifiable backdoor triggers by poisoning training samples, which are often unrealistic due to data privacy and safety concerns and are vulnerable to minor model changes such as fine-tuning. In contrast, the proposed technique leverages the diverse knowledge from a single OoD image to inject backdoor-based watermarks efficiently to different parts of the pre-trained representation space. Additionally, the proposed technique is safe and robust against watermark removal attacks and does not require poisoning training samples. Since the training data is independent, it is also not necessary to trust third-party providers with sensitive data. 

Experimental findings demonstrate that the proposed watermarking approach is effective in protecting IP of deep models. The authors show that their technique is robust against common watermark removal attacks, including fine-tuning, pruning, and model extraction. The proposed technique is also time- and sample-efficient without requiring any training data. The authors demonstrate the effectiveness of their approach on several popular models including VGG16, ResNet50, and MobileNetV2. The experimental results show that the proposed technique achieves high watermark detection accuracy while maintaining the performance of the original model on the original task.

### Weaknesses
Relying on a single OoD image as a secret key might introduce vulnerabilities. If an adversary gains access to this single image, the watermarking scheme could be compromised. Specifically, if the adversary can obtain the OoD image, they could potentially reverse-engineer the watermark injection process or create a model that is not susceptible to the watermark. The paper does not explore the implications of such a scenario, including the potential for an attacker to generate adversarial examples that bypass the watermark. Using multiple OoD images or a combination of techniques might enhance security?

It is unclear why specific trigger patterns are well suited for specific dataset. The paper lacks a detailed analysis of the relationship between trigger patterns and dataset characteristics. Further, it would be interesting to see how the watermarking technique performs when models are transferred across different tasks or domains. The watermark might lose its effectiveness in such scenarios. For example, if a model trained on ImageNet is fine-tuned for a medical imaging task, it's unclear if the injected watermark would remain detectable or if the fine-tuning process would effectively remove or alter the watermark.

### Questions
How many verification samples are needed for each successful verification?

In experiments the authors tried many different triggers. which trigger should an IP protector choose in practice?

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
The submission proposes a backdoor-based model watermarking scheme with a single OOD image. The work approaches a new scenario that the verifier of the model has no access to the original training data (e.g., as a third party or model-sharing platform), and demonstrates the robustness and efficiency of the watermark injection method.

### Strengths
+ The submission focuses on a new task that the watermark injection is performed after the training phrase, which allows the IP protection in more real-world scenarios. 
+ The proposed watermark injection method only requires a single OOD image to insert the copyright information, reducing the cost of sampling trigger datasets whilst maintaining the confidentiality.

### Weaknesses
 + **About the *Model Extraction* attack**: It is mentioned in section 4 that *the behavior of a victim model is cloned by fine-tuning it with the queried image-prediction pairs*, then what's the difference between the fine-tuning attack and model extraction? As retraining-based extraction attacks are generally considered in previous works [1-2], the robustness against such an attack should be further demonstrated. Specifically, the fine-tuning process described seems to be a simplified version of a model extraction attack, and it is unclear how the proposed method defends against a more sophisticated retraining-based extraction attack where the adversary might use a larger dataset or more advanced fine-tuning techniques. The evaluation should include a comparison with state-of-the-art model extraction methods, demonstrating the resilience of the watermark under such attacks.
+ **Possible OOD detection**: As the verification process is conducted with the augmentation of a single OOD image, the adversary may simply reject the query of OOD samples to reject the ownership verification process, as illustrated in [2]. Since OOD detection is entirely possible in the realistic scenarios proposed by the submission, the adpative defenses shoule be discussed in further detail. The concern is that if the verification process relies on a single, easily identifiable OOD image, it becomes vulnerable to simple filtering techniques. The adversary could employ basic OOD detection methods to identify and discard these verification samples, thereby circumventing the watermark verification. The paper needs to address how the proposed method can be made robust against such adaptive attacks, possibly by exploring more complex OOD samples or verification strategies.

### Questions
As the submission highlights the use of a single OOD image for watermark injection, the author may provide more comparison between the "pachify" of a single image and sampling several OOD images as the verification dataset, as to enhance the persuasiveness. Besides, more adaptive defenses such as OOD detection and Neural Cleanse [3] should be considered in addition to the traditional watermark removal attacks. 

Reference:

[3] Wang B, Yao Y, Shan S, et al. Neural cleanse: Identifying and mitigating backdoor attacks in neural networks. 2019 IEEE Symposium on Security and Privacy (SP). IEEE, 2019: 707-723.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
