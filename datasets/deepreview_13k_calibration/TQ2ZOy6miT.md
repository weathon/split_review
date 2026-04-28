# CLIPure: Purification in Latent Space via CLIP for Adversarially Robust Zero-Shot Classification

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6, 6, 6

## Abstract
In this paper, we aim to build an adversarially robust zero-shot image classifier that can accurately and efficiently classify unseen examples while defending against unforeseen adversarial attacks, addressing critical challenges in real-world safety-sensitive scenarios. To achieve this, we focus on two key challenges: zero-shot classification and defense against unforeseen attacks. We ground our work on CLIP, a vision-language pre-trained model to perform zero-shot classification. 
To defend against unforeseen attacks, we adopt a purification approach, as it is independent of specific attack types. 
We then define a purification risk as the KL divergence between the joint distributions of the purification and attack process. 
The derived lower bound of purification risk inspires us to explore purification in CLIP's multi-modal latent space. 
We propose a CLIP-based purification method called CLIPure, which has two variants: _CLIPure-Diff_, which models image likelihood with a generative process of its latent vector, and _CLIPure-Cos_, which models the likelihood based on the similarity between embeddings of the image and a blank template. As far as we know, CLIPure is the first purification method in latent space and _CLIPure-Cos_ is the first purification method not relying on generative models, substantially improving defense efficiency. Extensive experimental results show that the robustness achieved by CLIPure is within a small gap of clean accuracy, outperforming SOTA robustness by a large margin, e.g., from 71.7\% to **91.1\%** on CIFAR10, from 59.6\% to **72.6\%** on ImageNet, and **108\%** relative improvements of average robustness on the 13 datasets over previous SOTA, with only 14\% extra inference cost and no additional training.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes CLIPure, an adversarial purification method that operates within the CLIP models' latent space. This approach can enhance adversarial robustness on zero-shot classification without additional training. Even CLIPure-Cos can improve adversarial robustness without an external diffusion model. They demonstrate the effectiveness of CLIPure on various datasets.

### Strengths
1. This paper robustifies CLIP in latent space instead of pixel space, and they show the strength of this strategy in analysis.

2. The proposed method can improve the adversarial robustness of zero-shot classification of CLIP without training. In particular, CLIPure-Cos even does not require generative models, which are much more efficient regarding inference cost.

### Weaknesses
1. Missing baselines: [1] proposed adversarial and certified robustness of CLIP, compared to TeCoA.

[1] Choi et al., Adversarial Robustification via Text-to-Image Diffusion Models, ECCV 2024

### Questions
Please answer the Weakness part.

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
3

### Summary
This paper aims to build an adversarially robust zero-shot image classifier, based on CLIP. The authors propose two variant purification-based methods, CLIPPure-Diff and CLIPPure-Cos. The new approach is demonstrated to greatly boost the adversarial robustness and consistently set a new state-of-the-art across several datasets.

### Strengths
1. The paper is well motivated by measuring the KL divergence between the joint distributions of the purification and attack steps.
2. Although purification has been widely studied in pixel space, this paper showcases the potential of multi-modal latent space for learning robust zero-shot classification.
3. The proposed method is the first, as far as I know, purification method in multi-modal latent space.
4. The experiments and analysis are comprehensive and demonstrate the excellent of the proposed method

### Weaknesses
1. My main concern is related to the impact of VLMs. As the authors stated, the CLIP is a strong VLM and has shown superiority on many tasks. With this regard, the advantages of the proposed method could be substantiated better through an ablative study with different VLMs. Specifically, the paper should explore how the choice of VLM architecture affects the performance of the proposed purification methods. It is unclear whether the observed robustness gains are specific to CLIP or generalize to other VLMs with different architectural properties and pre-training objectives. For instance, models with different attention mechanisms or pretraining datasets might exhibit different levels of vulnerability and purification effectiveness.
2. The used models for evaluating the proposed method are limited, compared with the prior works [1]. For example, the results on ImageNet are only based on WideResNet-50. Transformer-based models are suggested, cf. 
[1] Diffusion Models for Adversarial Purification. The evaluation should include a wider range of models, particularly those with transformer-based architectures, to provide a more comprehensive assessment of the method's effectiveness. The current evaluation does not fully explore the potential of the proposed method across diverse model architectures, which is essential for understanding its general applicability.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper enhances adversarial robustness by purifying images in latent space. The experiments show a substantially improvement.

### Strengths
1. Good performance.

2. Clear figures with bright color.

### Weaknesses
Although the method shows a significant improvement, it still has many non-ignorable problems:

1. The motivation and contribution are too verbose, as well as the background description.
The authors should compact it.
For example, The prompt content of _"... by matching an image with text prompts “a photo of <class-name>”. "_ in abstract can be completely removed.

2. The method seems just do purify in feature space instead of in pixel space.

3. Lack a figure to illustrate the process of the method.

4. The theoretically analysize about purification risk is difficult to understand. It seems just a SDE?

5. And the analysize only is from CLIP, how can you extend it to diffusion model?

6. The definition of Zero-shot Learning is not correct.
In the original paper of CLIP, it has clearly claimed they changed the definition of ZSL from class-level to dataset-level.

_"In computer vision, zero-shot learning usually refers to the study of generalizing to unseen object categories in image classification (Lampert et al., 2009). We instead use the term in a broader sense and study generalization to unseen datasets."_

7. Where is the ablation study?

8. From table 3, we can clearly see CLIPure-Diff also increases the inference time significantly. And the efficiency comparsion misses the result of  FARE.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work,the author propose CLIPure, which conducts purification in CLIP's latent space for adversarially robust zero-shot classification.CLIPure leverages the image encoder and text encoder of the CLIP model to achieve effective purification in the latent space.By minimizing the KL divergence between the purification process and the adversarial process, CLIPure reduces purification risks and enhances the model's robustness against adversarial attacks. The algorithm includes two versions: CLIPure-Diff and CLIPure-Cos, which are based on the DiffusionPrior model and the cosine similarity metric of CLIP respectively. Experimental results demonstrate that CLIPure significantly outperforms existing methods when defending against AutoAttack on multiple datasets.

### Strengths
This paper introduces CLIPure-Diff and CLIPure-Cos, which perform purification in CLIP's latent space rather than in pixel space. Both methods exhibit significantly larger KL divergence between adversarial and benign sample distributions when compared to methods operating in pixel space and uni-modal latent space. Furthermore, CLIPure-Cos enhances defense efficiency by not relying on generative models. Results demonstrate that CLIPure significantly improves the SOTA robustness.

### Weaknesses
1、Although the article conducts numerous experiments, the selected comparison methods are not entirely appropriate. For instance, the adversarial training method in Table 2 is intended for defending against attacks on the text functionality of CLIP, rather than for zero-shot defense based on CLIP.
2、It is recommended to conduct further comparisons with models in the same direction, such as "Understanding zero-shot adversarial robustness for large-scale models" (ICLR 2023) and "Pre-trained Model Guided Fine-Tuning for Zero-Shot Adversarial Robustness" (CVPR 2024).

3、The paper mentions using 80 different description templates to enhance stability. How were these templates selected? Is it possible to optimize the selection of these templates through an automated approach?


4. Regarding the defensive effectiveness of the model, how does it perform under different threat levels (ϵ values)? Is there a detailed analysis available?

5、The article mentions that the selected purification step is 10 steps, but it lacks relevant experimental evidence to support this. How is this number determined? Is there experimental proof that this is the optimal number of steps, or is there a potentially better number of steps?

### Questions
1.The paper mentions using 80 different description templates to enhance stability. How were these templates selected? Is it possible to optimize the selection of these templates through an automated approach?


2. Regarding the defensive effectiveness of the model, how does it perform under different threat levels (ϵ values)? Is there a detailed analysis available?

3、The article mentions that the selected purification step is 10 steps, but it lacks relevant experimental evidence to support this. How is this number determined? Is there experimental proof that this is the optimal number of steps, or is there a potentially better number of steps?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper presents CLIPure, an approach for building adversarially robust zero-shot image classifiers based on CLIP. CLIPure performs purification in the latent space of CLIP to enhance robustness against adversarial attacks. It introduces two purification methods: CLIPure-Diff, which uses DALLE 2's diffusion prior to pure latent vectors ,and CLIPure-Cos, which performs purification by computing cosine similarity between the embeddings of an image and textual embedding of the blank templates. This paper conducts extensive experiments on CIFAR-10, ImageNet, and other 13 datasets and the proposed method demonstrates strong performance, exceeding previous SOTA results.

### Strengths
1. The proposed method performs purification in CLIP's latent space, which is technically sound. 

2. Based on the cosine similarity used in CLIP, this paper further proposes a purification method that is not based on generative models, which improves the computational efficiency.

### Weaknesses
1. The motivation is not strong enough. It seems that the key motivation is simply that performing purification in the latent space of CLIP is promising to achieve improved performance. However, there are only a few discussions about why it is necessary to perform purification methods for CLIP in its latent space and what issues exist with previous methods for CLIP.

2. Some baseline methods need further clarification. It is unclear whether the authors pre-trained or trained the baselines themselves or used publicly available versions. If off-the-shelf models are used, it is necessary to specify the references and discuss whether the difference in training data influences the comparisons. If the authors conducted the training themselves, which dataset is used and what is the setting for the training?

3. It seems that the experimental settings for baselines are not clear enough. For the compared purification methods, the base generative models should be unified for a fair comparison. Especially, it would be better to compare to the purification method with DiffPure based on DALLE2. For the AT methods, as the proposed method is specifically designed for CLIP, further discussion is needed on the comparability between different base models.

### Questions
I am not familiar with this field. Please refer to the weaknesses for my major concerns.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper propose two variants (i.e., CLIPure-Diff and CLIPure-Cos) for our CLIPure approach, which explore purification in the multi-modal latent space of CLIP. In addition, CLIPure-Cos is the first purification method that is not based on generative models. Experiment results show that purification in multi-modal latent space is promising for zero-shot adversarial robustness.

### Strengths
1. Conducting purification in multi-modal latent space for adversarially robust zero-shot classification is novel.
2. The overall organization is reasonable, and the writing is good.
3. Sufficient experiments are performed, and the proposed method exceeds the comparison methods.

### Weaknesses
1. Line 184: $p_{ben}(X)$ is not mentioned in Eq. (3).
2. I wonder why $KL((p(x_{adv})||(p(x_{ben}))$ in Eq. (6) can excel at detecting out-of-distribution adversarial examples. Please further explain it.
3. In the experiment setting, authors should provide more training and testing details, and  Hyperparameter settings.
4. Providing more visual results about the Purification process like Figure 5 would be better.

### Questions
Please refer to the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
