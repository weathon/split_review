# Towards Realistic Unsupervised Fine-tuning with Vision-Language Models

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 5, 6

## Abstract
The emergence of vision-language models (VLMs), such as CLIP, has spurred a significant research effort towards their application for downstream supervised learning tasks.
Although some previous studies have explored the unsupervised fine-tuning of CLIP, they often rely on prior knowledge in the form of class names associated with ground truth labels.
In this paper, we delve into a realistic unsupervised fine-tuning scenario by assuming that the unlabeled data might contain out-of-distribution samples from unknown classes.
Furthermore, we emphasize the importance of simultaneously enhancing out-of-distribution detection capabilities alongside the recognition of instances associated with predefined class labels.

To tackle this problem, we present a simple, efficient, and effective fine-tuning approach called Universal Entropy Optimization (UEO).
UEO leverages sample-level confidence to approximately minimize the conditional entropy of confident instances and maximize the marginal entropy of less confident instances.
Apart from optimizing the textual prompts, UEO also incorporates optimization of channel-wise affine transformations within the visual branch of CLIP.
Through extensive experiments conducted across 15 domains and 4 different types of prior knowledge, we demonstrate that UEO surpasses baseline methods in terms of both generalization and out-of-distribution detection.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study tackles the problem of finetuning a vision-language model like CLIP on new unlabeled data with samples of unknown classes. To this end, a new approach called universal entropy optimization (UEO) is proposed. UEO utilizes the CLIP output score with known classes to determine whether a sample is an out-of-distribution (OOD) one. Then, the in-distribution samples are optimized following the standard entropy minimization strategy whereas the OOD samples are forced to maximize their prediction entropy. This finetuning process is parameter efficient as only the text prompts are involved during finetuning. Results using various methods across different open-set finetuning scenarios are evaluated, and the proposed strategy is validated to be effective.

### Strengths
- The attacked problem of the side effect caused by out-of-distribution samples during unsupervised finetuning is interesting, as it is encountered for many downstream applications of a large pretrained model.
    
- The effort of trying to adopt a unified adaptive loss function for both ID and OOD samples are appreciated, even though this goal is not quite accomplished in this study as would be later discussed.
    
- This method is validated on both ResNet and Vit-B backbones across various domain adaptation datasets, and comparisons with previous studies indicate a superior performance of the current method.

### Weaknesses
 - The strategy of entropy minimization for ID samples and entropy maximization for OOD samples have been a popular method[1, 2, 3]. This study applies the principle to the field of vision-language models. Despite its effectiveness on different benchmarks, the core idea resembles traditional ones, which would compromise the novelty of this study.
    
- I understand that the authors contribute in a generalized form as in Eq. (3) & (4) for the loss function of both ID and OOD samples. However, a similar principle of maximizing Mutual Information ID samples and penalizing the mutual information of OOD samples has been also proposed in [4].
    
- The theoretical derivation of Eq. (3) & (4) could be more explicit and detailed. The current version appears to be intuitive and lack thorough theoretical analysis. Eq. (3) is proposed just to satisfy the rule that minimize the entropy ID instances and maximization the entropy of OOD samples”. However, no theoretical guarantee is provided so that Eq. (3) & (4) would always satisfy the above principle. The explanation is also missing of how Eq. (3) & (4) would be more suitable than a simple stepwise function, e.g. $L_{ID}=H(p(x)$ and $L_{OOD}=-H(p(x))$, and the determination of OOD samples follows the common practice as introduced in Sec. 3.1.
    
- As for the scope of application of the proposed method, it appears to be a general OOD method that can be also applied to traditional classification networks. I wonder why this method is applied to only CLIP method instead of extending it to other pretrained backbones.

### Questions
From my point of view, Eq. (3) can also be viewed as an implicit threshold strategy to determine OOD samples. Specifically, assume of the max softmax probability $w$ follows a uniform assumption $w\sim \mathcal U(\frac{1}{C},1)$ , where $C$ denotes the total number of ID classes. The expectation $\mathbb E(w)=\frac{1}{2}(1-\frac{1}{C^2})$ and $\mathbb E(\frac 1 w)=log(C)$. Therefore, $\tilde w(x) - \tilde \Phi(w(x))\approx \frac{w}{\mathcal B_t \mathbb E(w)} - \frac{1/w}{\mathcal B_t \mathbb E(1/w)}$, and the thereshold for determining whether a sample is OOD now becomes $\lambda=\frac{1}{2} (1-\frac{1}{c^2})\log(C)$. In other words, Eq. (3) could be also one implicit form of thresholding strategy. I think the author should state the explicit benefit brought by the unified form as in Eq. (3) and (4) compared to a hard thresholding one. For example, we can observe in the form of $\lambda$ that $\lambda$ increases with the number of classes $C$ , yet I could not understand the rationale of this property.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel setting called "unsupervised universal fine-tuning," which involves both in-distribution prediction and out-of-distribution detection. To tackle this problem, the authors presented an approach called "universal entropy optimization." It utilizes the confidence of each sample to minimize the entropy of confident samples but maximize the entropy of confident samples. These combined lead to improvement for both generalization and out-of-distribution detection on benchmarks like DomainNet, VISDA-V, Office-OF, etc.

### Strengths
* The problem setup of "unsupervised universal finetuning" seems reasonable and is grounded in the disadvantages of previous settings.
* I think the approach of "universal entropy optimization" (UEO), especially Eqn. 3, is interesting in achieving maximization and minimization at the same time. I don't directly work in this field and am not sure whether Eqn. 3 has been used by other people. Nonetheless, I think the UEO approach in the paper is intriguing.
* The performance demonstrated in the experiment section supports the effectiveness of the approach.

### Weaknesses
(Details in the questions section) While the proposed "unsupervised universal finetuning" setting is intriguing, I believe further clarification is needed to fully understand its novelty and significance, particularly regarding the role of vision-language models. The authors should elaborate on how this setting fundamentally differs from existing approaches beyond its application to CLIP. Furthermore, although the extensive evaluation is commendable, the numerical results in Tables 1-4 are relatively close on certain datasets, and the performance of UEO is not consistently superior. This necessitates a more in-depth analysis of the results, including a discussion of variance, identification of the most challenging dataset, and a thorough investigation into the potential causes of performance discrepancies between UEO and other methods, such as UPL, as observed in Table 1.

### Questions
1. What is the special role of the "vision-language model" in the paper or the investigated problem? It seems to me the approach and problem-setting are applicable to models beyond CLIP?

2. Following the above question, I think the authors need to better clarify how their experiment setting differs from previous works. Specifically, the authors mentioned "unsupervised universal fine-tuning" as a novel fine-tuning setup, but it seems the evaluation directly adopted the previous datasets without special curation. Therefore, I am wondering if this is a new setting, or some previous setting adapted to CLIP, or some other cases?

3. The numbers in the tables are quite close for some datasets, and the performance for UEO is not the best on some datasets, such as  the avg numbers. Therefore, I think clarifications on the following questions would be helpful:
* Is there a clear baseline of the UEO approach, e.g., some simple modification or fine-tuning strategy to CLIP for this setting?
* What is the variance of these numbers?
* Which is the largest and hardest dataset?
* State-of-the-art is not necessary for me, but the authors might need to investigate more into the difference in performance and offer some insights. Let's take Table 1 for example, the gap between UEO and UPL on OH (Avg.) in quite significant, what might be the cause?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel task setting for unsupervised CLIP fine-tuning, where the label spaces of unlabeled data and predefined text classes are partially overlapped. As a result, the trained model is required to concurrently detect out-of-distribution categories while recognizing samples within the predefined classes. To address this challenge, the paper proposes a straightforward approach that aims to minimize the conditional entropy of confident samples and maximize the marginal entropy of less confident ones. Experiments are performed on benchmark datasets.

### Strengths
1. To the best of my knowledge, the proposed task setting is novel. I believe it offers a valuable direction for unsupervised CLIP adaptation.
2. The proposed approach is straightforward and results in a general improvement.
3. Experiments are carried out on widely accepted DA benchmarks.

### Weaknesses
1. The paper's primary focus, as highlighted in the introduction and method sections, is the class discrepancy between unlabeled data and the predefined label space. However, the principal experiments are based on domain adaptation datasets, which are characterized predominantly by distributional differences between domains. To properly define the task setting and verify the efficacy of the proposed method, more general classification datasets should be employed. For instance, datasets like ImageNet and SUN397, which are used in CoOp, could provide a more suitable evaluation framework for this specific problem.

2. The introduced method bears a significant resemblance to existing mutual information maximization losses. The sole distinction appears to be the instance weight, which is based on the maximum prediction probability. This raises concerns about the novelty of the proposed approach. Furthermore, the performance gains seem rather marginal when compared with its peers, particularly when considering the complexity introduced by the instance weighting scheme.

3. There is a lack of ablation studies. The methodology encompasses two critical components: the entropy-related training objective and parameter-efficient tuning. It is unclear whether the competing methods in Table 1 also implement the same parameter-efficient tuning. Additionally, the prompt and affine parameters of the parameter-efficient tuning should be dissected and examined individually to understand their respective contributions to the overall performance.

4. Some relevant studies that delve into various task settings are not cited. For instance, the paper should consider referencing studies on black-box DA [1], partial DA [2], and universal DA [3]. These references provide context and establish connections with existing research in related areas.

### Questions
See weaknesses.

### Soundness
1 poor

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
This paper introduces Universal Entropy Optimization (UEO), a method for unsupervised universal fine-tuning of vision-language models (VLMs) like CLIP. UEO aims to enhance the model's performance in two key aspects: accurate classification of samples from known classes and effective identification of samples from classes not present in the predefined classes. It does this by leveraging sample-level confidence and entropy optimization to handle out-of-distribution (OOD) samples. The paper presents results from experiments conducted across 15 domains, demonstrating that UEO outperforms baseline methods in terms of both generalization and OOD detection.

### Strengths
**Originality**

The paper proposes a simple yet efficient solution to address a unique and realistic setting of unsupervised universal fine-tuning. According to the authors, this is the first paper to tackle this practical setting. While the key principle of the method is similar to DANCE, unlike DANCE, the proposed approach does not require hyper-parameter selections, which can be challenging in the unsupervised setting.

**Quality**

This paper exhibits notable strengths in its hyper-parameter-free approach, Universal Entropy Optimization (UEO), which addresses the challenging task of unsupervised fine-tuning of vision-language models (VLMs) under real-world conditions, including potential out-of-distribution (OOD) samples in unlabeled data. Through comprehensive experiments conducted across diverse domains and the introduction of novel evaluation metrics like the AUC score, the paper showcases the effectiveness of UEO in both in-distribution classification and OOD detection. UEO's parameter-efficient methodology and emphasis on real-world scenarios make it a valuable contribution, marking its quality in the field of VLMs and unsupervised fine-tuning.


**Clarity**

The paper is well-written and easy to follow. The motivation of the paper is clear. The authors build upon previous works and cite them appropriately. 

**Significance**

The proposed setting is practical. The paper tackles the problem where unknown classes can be present in the unlabeled data, replicating real-world scenarios. The analysis is thorough and the experiments across multiple settings show consistent improvements.

### Weaknesses
One potential weakness of the paper is that it relies on sample-level confidence weights to approximate entropy minimization and maximization. While this approach is innovative, it may be sensitive to the distribution of confidences within the unlabeled data. If the confidences are not well-calibrated or vary significantly across samples, it could affect the effectiveness of UEO. The performance of UEO might be influenced by the quality and reliability of the confidence estimates, and if the confidence estimates are noisy or inaccurate, it could lead to suboptimal results.

One experiment that is missing would involve applying the method to VLMs that are not well-calibrated and observing its impact on the performance of the fine-tuned model.

Another potential drawback is that, when compared to InfoMax, there does not appear to be a significant improvement in accuracy on certain datasets. For instance, on the DomainNet dataset, there is no noticeable difference in performance in accuracy.

### Questions
1. Can the universal entropy optimization loss be potentially incorporated during the contrastive pre-training phase as well? 

2. Apart from being hyper-parameter free, could the author elaborate more on the benefit of using the proposed universal entropy optimization instead of the entropy separation loss in DANCE? 

3. Since the method relies on the confidence of the model, could the authors discuss the effect of calibration of predicted probabilities on the performance of the method? 

I would be willing to raise my score if the authors could address my concerns and answer the questions above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
