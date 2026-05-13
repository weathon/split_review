# SelfEval: Leveraging the discriminative nature of generative models for evaluation

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
We present an automated way to evaluate the text alignment of text-to-image generative diffusion models using standard image-text recognition datasets.
    Our method, called \OURS, uses the generative model to compute the likelihood of real images given text prompts, and the likelihood can be used to perform recognition tasks with the generative model.
    We evaluate generative models on standard datasets created for multimodal text-image discriminative learning and assess fine-grained aspects of their performance: attribute binding, color recognition, counting, shape recognition, spatial understanding.
    Existing automated metrics rely on an external pretrained model like CLIP (VLMs) or LLMs, and are sensitive to the exact pretrained model and its limitations.
    \OURS sidesteps these issues, and to the best of our knowledge, is the first automated metric to show a high degree of agreement for measuring text-faithfulness with the gold-standard human evaluations across multiple generative models, benchmarks and evaluation metrics.
    \OURS also reveals that generative models showcase competitive recognition performance on challenging tasks such as Winoground image-score compared to discriminative models.
    We hope \OURS enables easy and reliable automated evaluation for diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method for evaluating text-to-image generative models using the model's own capabilities. The proposed SELFEVAL approach computes the likelihood of real images given text prompts, enabling the generative model to perform discriminative tasks. This allows for fine-grained evaluation of the model's performance in attribute binding, color recognition, counting, shape recognition, and spatial understanding. Paper claims that SELFEVAL is the first automated metric to show a high degree of agreement for measuring text-faithfulness with human evaluations across multiple models and benchmarks. Unlike other metrics such as CLIP-score, which can show severe drawbacks when measuring text faithfulness, SELFEVAL offers reliable, automated evaluation for diffusion models without additional pre-trained models.

### Strengths
1. The proposed method provides a way to automate the evaluation process, making it less dependent on often subjective and time-consuming human evaluations. It allows for detailed assessment of various aspects of a model's capabilities, such as attribute binding and color recognition. The ability to evaluate models without needing additional pre-trained models is a significant advantage.
2. Sufficient evaluations of the proposed metric along with others are given. It shows consistency with human evaluations.

### Weaknesses
1. The performance of SELFEVAL is inherently linked to the effectiveness of the generative model itself, which could limit its reliability if the generative model has weaknesses in certain areas. From this perspective, more generative models should be evaluated. Specifically, the paper should address how the evaluation metric behaves when the underlying generative model struggles with specific attributes or concepts. For instance, if the generative model has difficulty with fine-grained color distinctions, how does this impact the SELFEVAL score for color recognition? This dependency on the generative model's capabilities raises concerns about the metric's robustness across diverse model architectures and training regimes.
2. The authors don't discuss the potential limitations of their proposed method in detail. For example, the computational cost associated with calculating likelihoods using the generative model is not addressed. Furthermore, the paper lacks a discussion on how the sampling strategy of the generative model impacts the evaluation results. Different sampling techniques could lead to varying likelihood estimates, and the paper should explore the sensitivity of SELFEVAL to these variations. It is also unclear how the method handles cases where the generative model produces low-quality or nonsensical images, and whether these cases are appropriately penalized by the metric.

Minor issues:
1) There may exist some misuse between \cite and \citep as some citation formats seem improper in the paper.

### Questions
1. How well does the SELFEVAL method generalize across different types of generative models and datasets?
2. Can this method be employed in GAN, VAE, and flow-based generative models?
3. Including a broader range of comparative studies with current methods for assessing the quality of text-to-image generative models could strengthen your arguments.
4. How different text encoders impact the performance of SELFEVAL.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method that can evaluate text-faithfulness of text-to-image generative models. The main idea is to employ the generative model itself for discriminative tasks, thereby evaluating the performance. Experimental results show that the proposed method can achieve a high degree of agreement for measuring text-faithfulness with human evaluations on several models and datasets, proving the effectiveness.

### Strengths
1. The method is simple but effective, which can be easily implemented and applied to other tasks.
2. Experiments show the effectiveness and good performance for measuring text-faithfulness.

### Weaknesses
As the authors said, the formulation can extend to any conditional diffusion model. However, the current analysis and experiments only demonstrate that the method is effective for text-to-image generation tasks with diffusion models. 

1. Considering the method only evaluates the text-faithfulness without image quality in text-to-image generation tasks, the application scope will be very limited. Therefore, the contribution is not overwhelming and might not be enough for this conference, in my opinion.

2. The experiments are also limited. Since the proposed method is an evaluation metric, trying it to evaluate other frameworks, such as VAEs and GANs, is also necessary. If the method can only be applied to diffusion models, it will be less valuable.

### Questions
Although diffusion models have become very popular recently, this framework has not become the only generative model. Meanwhile, other frameworks also perform well in text-to-image generation tasks. Therefore, I think the method has a limited application scope. In my opinion, the authors should try other conditional generation tasks rather than only text-to-image generation tasks, or try applying the method to other generative models.

However, in addition to this problem, I cannot find other technical flaws or missed experiments. Thus, I tend to a marginal score.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed an automatic evaluation method by measuring text-image faithfulness, showing an agreement with human evaluations in multiple benchmarks. By arguing that CLIP-score has severe drawbacks in DrawBench, for example, they argued that their method, SelfEval, solves or detours these issues, hoping for its role as a reliable and easy-access method to evaluate multimodal diffusion models.

### Strengths
- They showed the limitation of CLIP-score in quantitative evaluation with extensive analysis. 

- One may exploit a strong text-to-image generativel model to evaluate others.

### Weaknesses
 - W1. Novelty. The motivation of their method is reminiscent of the CLIP-R-Precision of Park et al. (2021), where the goal is to pick the right caption among distractors. Although the authors used the likelihood estimations to get a score for text-image matching, it can be seen as an ad-hoc method to replace the cosine similarity in CLIP. Since we cannot control the pretrained models where one is CLIP and the other one is diffusion models, the authors need to study the effectiveness of the proposed method extensively. The limitation of the CLIP score was also explicitly explored in MID [2].

- W2. State-of-the-art comparison. For the text-image faithfulness, you could compare the state-of-the-art performance with DALL-Eval [1], MID [2], LLMScore [3], and VPEval [4]. The paper failed to cite them. Please allocate the dedicated paragraph in Sec. 2 to include them and compare the related works.

### Questions
Could you let me know why you excluded the closely related works mentioned in Weaknesses W2?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
