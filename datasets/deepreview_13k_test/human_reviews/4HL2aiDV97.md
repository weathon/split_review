# GAD-VLP: Geometric Adversarial Detection for Vision-Language Pre-Trained Models

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
Vision-language pre-trained models (VLPs) have been deployed in numerous real-world applications; however, these models are vulnerable to adversarial attacks. Existing adversarial detection methods have shown their efficacy in single-modality settings (either vision or language), while their performance on VLPs, as multimodal models, remains uncertain. In this work, we propose a novel aspect of adversarial detection called GAD-VLP, which detects adversarial examples by exploiting vision and joint vision-language embeddings within VLP architectures. We leverage the geometry of the embedding space and demonstrate the unique characteristics of adversarial regions within these models. We explore the embedding space of the vision modality or the combined vision-language modalities, depending on the type of VLP, to identify adversarial examples. Some of the geometric methods do not require explicit knowledge of the adversary's targets in downstream tasks (e.g., zero-shot classification or image-text retrieval), offering a model-agnostic detection framework applicable across VLPs. Despite its simplicity, we demonstrate that these methods deliver a nearly perfect detection rate on state-of-the-art adversarial attacks against VLPs, including both separate and combined attacks on the vision and joint modalities.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper benchmarks the effectiveness of several methods for detecting adversarial input images in multi-modal models. In particular, these techniques exploit the geometry of the features extracted by the vision and multi-modal encoders to distinguish between clean and adversarial images, and are agnostic of the downstream task. In the experimental evaluation, the different methods are compared on several datasets for both classification and retrieval tasks.

### Strengths
- The paper extends the use of several detection techniques to vision-language models, which might be interesting as making these models robust is a relevant challenge. The question of whether detection in multi-modal models is easier than with classifier is also interesting.

- The experimental evaluation includes several datasets and tasks, and different architectures.

### Weaknesses
- Detection methods for image classification have often been shown ineffective against adaptive attacks: for example, LID was bypassed in [A], Mahalanobis distance was shown non-robust to adversarial perturbations in [B], and several detection methods are bypassed in [C]. Thus, the proposed methods should be tested against attacks targeting the detection mechanism, e.g. as discussed in [C]. Moreover, the ablation study in Sec. 5.3 about generalization to different attacks only uses methods which are very close to the PGD attack (with only 10 steps) used for tuning the detection methods, and optimize the same loss function: then the generalization to them is not surprising.

- The techniques used for detection are from prior works, which limits the technical novelty of the paper.

- I think it'd be useful to report the success rate of the attack before detection.

[A] https://arxiv.org/abs/1802.00420 \
[B] https://arxiv.org/abs/2201.07012 \
[C] https://openreview.net/forum?id=af1eUDdUVz

### Questions
I think it'd be important to test adaptive attacks, especially considering that the same techniques used in this paper have been shown ineffective with standard classifiers.

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
4

### Summary
This paper proposes GAD-VLP, a geometric adversarial detection framework for vision-language pre-trained models. The method leverages geometric approaches including local intrinsic dimensionality, k-nearest neighbors distance, Mahalanobis distance, and kernel density estimation to identify adversarial examples in VLPs.

### Strengths
This paper is easy to follow, and the structure is well-claimed.

### Weaknesses
1. The paper lacks rigorous theoretical analysis of why geometric methods work better for VLPs compared to traditional models. While empirical results are shown, there's no formal proof or theoretical guarantees about the method's effectiveness, especially claiming why their approach is fundamentally sound for VLPs.

2. The paper doesn't adequately address the computational costs of calculating geometric metrics, especially for large-scale deployments. Computing k-NN, Mahalanobis distances, and KDE for high-dimensional embeddings can be computationally expensive. 

3. The paper doesn't consider sophisticated adaptive attacks that might specifically target the geometric detection mechanism. Adversarial methods often adapt to known defense mechanisms, and the lack of evaluation against such adaptive attacks raises questions about the method's robustness in real-world scenarios. 

4. The authors don't thoroughly examine the false positive rates and their impact on model usability. In real-world applications, high false positive rates could lead to unnecessary rejection of legitimate inputs.

### Questions
This paper should consider further feedback regarding the lack of rigorous mathematical proof, computational scalability concerns, and vulnerability to adaptive attacks.

### Soundness
2

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
3

### Summary
The paper looks at detection of adversarial examples for multi-modal models (CLIP, ALBEF). They extend uni-modal detection methods to vision-language based models. Experiments are conducted on classification and Image-retrieval tasks using different 'geometry of sample' based approaches to show GAD-VLP (proposed framework) works well when using different methods for detection.

### Strengths
- The problem being studied is important - Detecting adversarial inputs in multi-modal setup.
- The related work exploration seems sufficient.
- Diversity of evaluation tasks (classification, retrieval) and models is reasonable

### Weaknesses
- Overall the paper lacks technical novelty as previously used methods (MMD, KDE etc) for uni-modal detection methods are just transferred to multi-modal setup.

- The evaluation/testing setup in re to adversarial setup is not sufficient.

- The adversarial attacks do not seem strong, looking at Fig. 2 a naturally strong attack would be to add a regularizer term that enforces the image embedding (under perturbation) to stay close to the clean embedding. Testing method on such strong attacks would be nice.

- The attacks are based on10-step PGD, and versions of FGSM all at eps=8/255 (other values should have been looked at). A lot of new attacks (see the ones in [1, 2]) for CLIP like models have been proposed - testing which would have been also a valuable addition to the submission.

- For the binary classifier using LID, attacking the classifier (detector) would also be a reasonably strong attack.

[1] Schlarmann, Christian, and Matthias Hein. "On the adversarial robustness of multi-modal foundation models." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

[2] Mao, Chengzhi, et al. "Understanding Zero-shot Adversarial Robustness for Large-Scale Models." The Eleventh International Conference on Learning Representations.

### Questions
- What is the setup for retrieval is it top-1, top-5?  
No other questions, some questions on choice of experiments can be inferred from Weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper propose the GAD-VLP, a method for detecting adversarial attacks in VLP Models. It uses geometric metrics like Local Intrinsic Dimensionality (LID), k-Nearest Neighbors (k-NN), Mahalanobis distance, and Kernel Density Estimation (KDE) to distinguish adversarial examples. GAD-VLP works across various VLP architectures, whether they use separate or combined embeddings for vision and language inputs. The method demonstrates high detection accuracy against different attacks and is applicable to tasks like zero-shot classification and image-text retrieval. The study highlights GAD-VLP's robustness and versatility across multiple domains.

### Strengths
1.	The writing is clear. The formulas are correct.
2.	The experiment is multi-dimensional.
3.	The research topic is important for VLP.

### Weaknesses
1.	While the proposed method is effective, the metrics used are standard and not specifically tailored for the Vision-Language Pre-training (VLP) task.
2.	The paper does not sufficiently highlight the distinctions between unimodal models and VLP models, resulting in a lack of justification for the choice of metrics.
3.	Classical VLP models, such as BLIP [1] and X-VLM [2], are missing from the analysis.
4.	The adversarial attack methods utilized are limited and do not include more popular approaches like Set-level Guidance Attack (SGA) [3].

[1] BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation

[2] Multi-Grained Vision Language Pre-Training: Aligning Texts with Visual Concepts

[3] Set-level Guidance Attack: Boosting Adversarial Transferability of Vision-Language Pre-training Models

### Questions
Please see the weakness.

### Soundness
4

### Presentation
4

### Contribution
2
