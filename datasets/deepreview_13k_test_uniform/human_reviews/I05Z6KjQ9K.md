# Gradient Regularization-based Cross-Prompt Attacks on Vision Language Models

- Decision: Reject
- Scores: 1, 3, 1, 5

## Abstract
Recent large vision language models (VLMs) have gained significant attention for their superior performance in various visual understanding tasks using textual instructions, also known as prompts.
However, existing research shows that VLMs are vulnerable to adversarial examples, where imperceptible perturbations added to images can lead to malicious outputs, posing security risks during deployment.
Unlike single-modal models, VLMs process both images and text simultaneously, making the creation of visual adversarial examples dependent on specific prompts.
Consequently, the same adversarial example may become ineffective when different prompts are used, which is common as users often input diverse prompts.
Our experiments reveal severe non-stationarity when directly optimizing adversarial example generation using multiple prompts, resulting in examples specific to a single prompt with poor transferability.
To address this issue, we propose the Gradient Regularized-based Cross-Prompt Attack (GrCPA), which leverages gradient regularization to generate more robust adversarial attacks, thereby improving the assessment of model robustness.
By exploiting the structural characteristics of the Transformer, GrCPA reduces the variance of back-propagated gradients in the Attention and MLP components, utilizing regularized gradients to produce more effective adversarial examples.
Extensive experiments on models such as Flamingo, BLIP-2, LLaVA and InstructBLIP demonstrate the effectiveness of GrCPA in enhancing the transferability of adversarial attacks across different prompts.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The authors proposed a method termed Gradient Regularized-based Cross-Prompt Attack (GrCPA) that creates adversarial images that transfer across prompts. The GrCPA method extends the previous cross-prompt framework by applying gradient regularisation. The effectiveness of the GrCPA is evaluated with Flamingo, BLIP-2, LLaVA, and InstructBLIP on different tasks.

### Strengths
- The paper conducts extensive experiments on various VLMs to prove the effectiveness of GrCPA.
- The paper is easy to follow.

### Weaknesses
- **The novelty is limited**: As detailed in Section A.2 (line 878), the only difference between GrCPA and a recent work termed CroPA [1] is the addition of Gradient Regularization. The pipeline of GrCPA is highly similar to that of CroPA.

- **Practical applicability to the real world is limited**: As shown in Table 11, GrCPA does not demonstrate strong transferability across different models, with the average ASR remaining below 10%.

[1] Luo, Haochen, Jindong Gu, Fengyuan Liu, and Philip Torr. "An image is worth 1000 lies: Transferability of adversarial images across prompts on vision-language models." In The Twelfth International Conference on Learning Representations. 2023.

### Questions
- What is the impact of using different extrema K?

- Why the top k largest values of the gradient vectors are clipped directly to 0 instead of other constant values?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the challenge of creating transferable adversarial attacks across different prompts for vision language models (VLMs). The authors propose GrCPA (Gradient Regularized-based Cross-Prompt Attack), which utilizes gradient regularization to generate more robust adversarial examples.

### Strengths
1.	The experiments show the consistent better performance.
2.	The writing is easy to follow.

### Weaknesses
1.	The novelty and contribution are marginal. It only modifies the training loss in a very simple way.
2.	The logic is unconvincing to me. It is claimed that large gradients can lead to local optima and trigger overfitting issues. However, the Gradient Regularization simply sets the largest and the lowest gradients to zero. This raises two questions: (1) Why do you set the lowest gradient to zero? (2) Does the largest gradient represent a ‘large’ gradient? For example, in some cases, the largest gradient could be lower than the lowest gradient in another sample or batch. How do you define ‘large’ and ‘small’?"

### Questions
1.	During training and testing, do you use the same text prompts? If so, it seems that cross-prompt is just overfit on several prompts rather than one.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The similarities between this work and [1] in problem motivation, paper organization, experimental design, and writing text raise concerns about originality and potential plagiarism. Although the proposed approach does present some differences, the extent of overlap indicates that the authors may not have adequately distinguished their work from [1], published in ICLR 2024.

Here are some specific instances that suggest potential plagiarism:

1. The paper introduces a new problem, "cross-prompt transferability," which was first proposed in [1]. Notably, the main text, abstract, and introduction do not reference this prior work.

2. The organisation of this paper closely mirrors that of [1], with some tables being directly copied and merely modified to add an additional row.

3. Several paragraphs in this manuscript appear to be simple paraphrases of corresponding sections in [1].

4. In the experimental design, instead of acknowledging [1] as a basis, the authors claim to have independently designed the experiment, even though the design and details align precisely with those in [1].

There are additional similar issues present in the manuscript. Overall, this paper clearly does not adhere to accepted scientific writing standards.

[1] Luo, Haochen, et al. "An image is worth 1000 lies: Transferability of adversarial images across prompts on vision-language models." In The Twelfth International Conference on Learning Representations. 2023. Url: https://openreview.net/pdf?id=nc5GgFAvtk

### Strengths
N/A

### Weaknesses
N/A

### Questions
N/A

### Soundness
2

### Presentation
1

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
The paper presents a novel Gradient Regularization-based Cross-Prompt Attack (GrCPA) targeting Vision-Language Models (VLMs), which addresses the issue of adversarial non-stationarity across diverse prompts. By leveraging gradient regularization, GrCPA mitigates the variability in adversarial success when multiple prompts are used. This approach enhances the robustness of adversarial examples, improving their transferability across prompts. Experiments on models such as Flamingo, BLIP-2, LLaVA, and InstructBLIP validate GrCPA’s effectiveness, showing superior attack stability and transferability compared to existing methods.

### Strengths
1. The method introduced is original. GrCPA’s use of gradient regularization for adversarial robustness across prompts introduces an effective method for enhancing VLM attack transferability.

2. The extensive experimental analysis across models and tasks (e.g., image captioning, VQA) confirms the soundness of the approach.

3. The method’s formulation and rationale are clearly articulated, supported by structured experiments that compare GrCPA with established baselines.

### Weaknesses
1. The technical depth of this paper is somewhat limited. Adversarial attacks are really not something that is surprisingly new in machine learning models, even in VLM. Incremental improvement in this area does not contribute much to this community. The method only introduces gradient normalization to stabilize the adversarial optimization, which is more like a trick for attack implementation.

2. I would expect some black-box transferability analysis to demonstrate the effectiveness of this attack.

### Questions
See the weakness section

### Soundness
3

### Presentation
3

### Contribution
2
