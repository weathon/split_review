# $\texttt{MirrorCheck}$ : Efficient Adversarial Defense for Vision-Language Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Vision-Language Models (VLMs) are becoming increasingly vulnerable to adversarial attacks as various novel attack strategies are being proposed against these models. While existing defenses excel in unimodal contexts, they currently fall short in safeguarding VLMs against adversarial threats. To mitigate this vulnerability, we propose a novel, yet elegantly simple approach for detecting adversarial samples in VLMs. Our method leverages Text-to-Image (T2I) models to generate images based on captions produced by target VLMs. Subsequently, we calculate the similarities of the embeddings of both input and generated images in the feature space to identify adversarial samples. Empirical evaluations conducted on different datasets validate the efficacy of our approach, outperforming baseline methods adapted from image classification domains. Furthermore, we extend our methodology to classification tasks, showcasing its adaptability and model-agnostic nature. Theoretical analyses and empirical findings also show the resilience of our approach against adaptive attacks, positioning it as an excellent defense mechanism for real-world deployment against adversarial threats.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the problem of adversarial defense for Vision-Language Models (VLMs). The paper proposes a simple and elegant method called MIRRORCHECK to detect adversarial samples. The method utilizes Text-to-Image (T2I) models to generate images based on captions produced by target VLMs. Then, the similarities of the embeddings of both input and generated images in the feature space are leveraged to identify adversarial samples. Extensive experiments are conducted to demonstrate the effectiveness of proposed method.

### Strengths
The proposed method is simple and elegant. It leverages Text-to-Image models to generate images based on captions produced by target VLMs. Then, the similarities of the embeddings of both input and generated images in the feature space are used to identify the adversarial samples.

The paper conducts sufficient experiments to demonstrate the advantages of proposed method. Specifically, the experiments are conducted on five victim models. More Text-to-Image models and pretrained image encoders are tested in the ablation studies.

The paper is well-written. For example, there is a section in Method to describe the threat model.

### Weaknesses
It is better to introduce how to choose hyperparameter \tau (decision threshold in line 217), especially the relation between \tau and text-to-images models (or pretrained image encoders).

The experiments are conducted against targeted attacks. How about untargeted attacks?

In Section 3.1, the paper writes "the attacker's objectives are to execute targeted attacks". If the attack performance of used attack method is low, will the proposed method still work?

There are some typos. For example, "Tables 1 and 3 presents" should be "Tables 1 and 3 present" in line 312.

### Questions
Though the paper conducts ablation study to explore the influence of different Text-to-Image (T2I) models and pretrained image encoders, is it possible to provide some information of T2I models such as classification accuracy and training mechanism to explain the relation between detection results and text-to-image models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes MirrorCheck, a novel method for detecting adversarial samples in Vision-Language Models (VLMs). It leverages a Text-to-Image (T2I) model to generate an image based on the caption produced by the victim model and then compares the embeddings of the input and generated images. The method is evaluated on different datasets and tasks, showing its effectiveness and superiority over baseline methods. It also demonstrates robustness against adaptive attacks and adaptability to different T2I models and image encoders.

### Strengths
- **Originality**: The idea of using a T2I model to generate images for adversarial sample detection in VLMs is novel. It provides a new perspective and approach compared to existing defenses.
- **Quality**: The experiments are well-designed and conducted. The use of multiple datasets, victim models, T2I models, and image encoders shows the robustness and generality of the method. The results are presented clearly and support the claims made in the paper.
- **Clarity**: The paper is well-written and organized. The introduction provides a clear motivation for the work, the method description is detailed and understandable, and the experimental results are presented in a logical manner.
- **Significance**: The proposed method has significant implications for the security and reliability of VLMs. It addresses an important problem of adversarial attacks and provides a practical solution that can be applied in real-world scenarios.

### Weaknesses
 - The effectiveness of MirrorCheck depends on the quality of the pretrained generative model used. Any shortcomings in the generative model can directly impact the performance of the method. This limitation could be further explored and addressed.
- The paper could provide more in-depth analysis of the theoretical aspects of the method. For example, a more detailed explanation of why the image-image similarity approach works better than directly comparing the input image with the generated caption could be beneficial.

### Questions
- How can the method be further improved to handle cases where the pretrained generative model is of poor quality?
- Can the authors provide more insights into the theoretical foundation of the image-image similarity approach?
- Are there any potential limitations or challenges in applying MirrorCheck to other types of multimodal models or tasks?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a simple adversarial sample detection method called MirrorChecker, which detects adversarial samples by comparing the embedding similarity between reconstructed adversarial samples and clean samples. Specifically, given an adversarial sample, the method first uses a pre-trained multimodal model to generate a caption for the image and then employs a diffusion model to reconstruct the image based on that caption. Finally, it assesses the similarity between the reconstructed image and the clean image to detect malicious adversarial samples. The paper validates the effectiveness of the proposed defense method across multiple models.

### Strengths
- The writing is clear.
- Detecting adversarial samples in multimodal models is an interesting research topic.

### Weaknesses
 - **Unclear Threat Model:** In section 3.1, the authors focus on targeted attacks (lines 199-200), but this assumption is unclear. It is recommended that the authors address a broader range of attack scenarios, including patch attacks and untargeted attacks. Specifically, how might untargeted attacks affect the performance of the proposed detection method?

- **Lack of Defender Capability:** The paper does not provide sufficient detail about the defender's capabilities and the practical feasibility of the proposed defense. A key concern is how the defender obtains the clean samples needed for comparison. In other words, if clean images are not required, how does the defense work? The authors should clarify how this affects the real-world applicability of their approach.

- **No Support for Theoretical Analyses:** The authors claim to provide theoretical analyses in the abstract (line 22); however, a review of the paper reveals no such analyses. If these analyses are not present, the authors should explain why this claim is made.

- **Insufficient Robustness Against Adaptive Attacks:** The robustness of the proposed defense method against adaptive attacks needs further analysis. For example, if attackers are aware of this defense mechanism, they may modify the adversarial images to minimize the distance to the clean images. Would this enable them to evade the proposed detection? The authors should consider stronger adaptive attacks and provide corresponding defense results.

- **Defense Results on Out-of-Distribution Data:** It is unclear how the proposed method detects adversarial samples when applied to out-of-distribution (OOD) data, particularly across multiple domains. The authors should provide either experimental results or a theoretical discussion on the performance of their method when dealing with OOD samples from various domains.

- **Lack of Comparison with Advanced Defense Baselines:** A comparison with advanced baselines, such as DiffPure [1], would strengthen the paper. DiffPure uses a diffusion model to remove adversarial noise and detects adversarial samples by assessing the prediction differences between cleaned samples and the original adversarial samples. The detection process of DiffPure seems more straightforward and efficient than the proposed method. The authors should provide a quantitative comparison on a common dataset, focusing on both detection accuracy and computational efficiency. This would help highlight the strengths of their method over existing baselines.

### Questions
see weakness.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on detecting adversarial examples targeting Vision-Language Models (VLMs) by introducing a method called MirrorCheck. MirrorCheck uses an additional Text-to-Image (T2I) model and a CLIP image encoder to identify adversarial inputs. For any input to a VLM, the T2I model generates an image based on the VLM's output, and the CLIP image encoder extracts embeddings to compute a similarity score between the generated and original images. A significant difference in similarity indicates a potential adversarial example. The method is simple yet technically sound, and experiments with various VLMs, T2I models, and CLIP encoders confirm its effectiveness.

### Strengths
- Although the idea behind the method is simple, it is technically sound. The core concept is that adversarial examples tend to cause VLMs to generate text that deviates from the content of the original image. As a result, the T2I model's generated image will also deviate, leading to large differences in similarity scores between the generated and original images.
- While adversarial training is a popular defense method, it is costly, difficult to scale for large models, and faces trade-offs between robustness and accuracy. In contrast, detecting adversarial examples offers a cost-effective defense by rejecting malicious queries. MirrorCheck, the proposed detection method, is specifically designed for VLMs.
- The method is evaluated under a realistic black-box threat model, where the adversary can only query the victim model without access to gradient information, making it practical for real-world scenarios. Additionally, experiments were conducted using a white-box threat model to push the method to its limits. The evaluation setup and findings are well-appreciated.

### Weaknesses
 - The core motivation behind MirrorCheck is that adversarial examples typically cause VLMs to generate content that deviates from the main image. However, adversaries could potentially manipulate the VLM to produce content that is aligned, or at least partially aligned, with the image. In such cases, MirrorCheck might fail to detect the adversarial example. For instance, consider Figure 2, where the adversary's target text is "A leopard laying down on a rock next to a field ...", followed by harmful or misleading texts. If the adversary uses a targeted attack to craft an adversarial example that closely aligns with the original image (except for the harmful text), how would the similarity scores behave? To what extent could this reduce MirrorCheck's detection effectiveness? This scenario raises concerns about MirrorCheck's robustness when handling adversarial attacks that maintain a degree of semantic consistency with the image. This type of targeted attack is examined in this work [1].

- The Average Similarity Scores in Table 1 alone do not fully capture MirrorCheck’s detection performance. While they show a general pattern of deviation between clean and adversarial examples, they do not clearly demonstrate whether MirrorCheck can reliably differentiate between them. In Table 3, the minimum similarity score for clean versus adversarial examples is on the same level, and a similar pattern is observed for the maximum scores, further obscuring the distinction. I recommend that the authors plot the distribution of similarity scores to better illustrate the detection performance.

- The detection accuracy, TPR, and FPR presented in Tables 2 and 4 are influenced by the ratio of adversarial and clean examples. However, this ratio is not explicitly mentioned in the paper. In real-world scenarios, adversarial queries are typically rare. I suggest conducting an ablation study that examines detection performance under varying ratios of adversarial examples. Starting with a balanced 50%-50% to 99.9%-0.1%

- Line 371 stated that the threshold $\tau$ is based on optimized performance. In practical settings, it is very unlikely that the optimal hyperparameters can be found. The similarity scores could vary depending on the validation set, attack used, and CLIP image encoder. I suggest also including the area under the ROC curve and Precision-Recall curve.

- Following the setting in the adaptive attack study, line 485, the adversarial examples can still be detected by other encoders. This could be the result of the adversarial example not transferable to other encoders. What if the adversary improves the transferability by using an ensemble of other encoders?

- There are relevant detection baselines [2-4] and related adversarial attacks [1, 5, 6] that are not examined in the paper.

- Line 098 claims that MirrorCheck does not require training. This could be misleading. T2I models and CLIP encoders are part of the defense that does require training.

- Lines 177 - 182 suggest that existing defenses do not consider multi-modal settings. However, several works [7-9] have proposed adversarial training for the multi-modal setting.

### Questions
- Line 158-160, the certified defense methods can guarantee robustness. What does it mean by the struggle to generalize to novel attack strategies? 
- Line 253, experiments are conducted with 100 or 1000 randomly selected images; why not use the full dataset for evaluation? And which experiments are using 100 and which are using 1000? 
- Line 258-260, I believe the PGD requires a gradient for optimization of the attack vector; how is this used for 100 queries and 8-step PGD with an estimated gradient?

### Soundness
3

### Presentation
2

### Contribution
2
