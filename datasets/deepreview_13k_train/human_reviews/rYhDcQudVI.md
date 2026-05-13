# Score-based Conditional Generation with Fewer Labeled Data by Self-calibrating Classifier Guidance

- Decision: Reject
- Scores: 5, 5, 5, 5, 5

## Abstract
Score-based generative models (SGMs) are a popular family of deep generative models that achieve leading image generation quality. Early studies extend SGMs to tackle class-conditional generation by coupling an unconditional SGM with the guidance of a trained classifier. Nevertheless, such classifier-guided SGMs do not always achieve accurate conditional generation, especially when trained with fewer labeled data. We argue that the problem is rooted in the classifier's tendency to overfit without coordinating with the underlying unconditional distribution. To make the classifier respect the unconditional distribution, we propose improving classifier-guided SGMs by letting the classifier regularize itself. The key idea of our proposed method is to use principles from energy-based models to convert the classifier into another view of the unconditional SGM. Existing losses for unconditional SGMs can then be leveraged to achieve regularization by calibrating the classifier's internal unconditional scores. The regularization scheme can be applied to not only the labeled data but also unlabeled ones to further improve the classifier. Across various percentages of fewer labeled data, empirical results show that the proposed approach significantly enhances conditional generation quality. The enhancements confirm the potential of the proposed self-calibration technique for generative modeling with limited labeled data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to solve the problem of conditional generation with fewer labeled data. The authors propose a new method to improve classifier-guided score-based generation by regularizing the classifier during training time. The key idea of this regularizer is to use principles from energy-based models to convert the classifier as another view of the unconditional SGM. Experimental results illustrate the superiority of the proposed method over several related baselines.

### Strengths
First, I am not an expert in conditional score-based generation and may miss some related work.

## Quality
* Experimental results illustrate the superiority of the proposed method.

## Clarity
* Overall, this paper is very well-written.
* The related works are discussed clearly.

## Significance
* The paper can contribute to the area of semi-supervised conditional generalization.

### Weaknesses
## Originality
* I am afraid that the novelty may be limited since the techniques are common in deep-generation models.

## Quality & Clarity
* For the proposed method, the classification ability of the trained classifier is not tested experimentally.

## Significance
* The proposed method may have little effect on other sub-fields of machine learning.

### Questions
1. In my view, the proposed method involves a classifier, so why not test its classification ability?
2. Please discuss the relationship with a recent highly relevant paper [1*].

[1*] Diffusion Models and Semi-Supervised Learners Benefit Mutually with Few Labels, NeurIPS 2023

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This methodology innovatively reinterprets classifiers as time-dependent Energy-Based Models, offering enhanced regularization through a gradient-based approach and introducing a novel self-calibration loss. These advances significantly improve alignment with underlying data distributions, boosting generalization and robustness in classifier-guided generative modeling.

The approach enables more effective utilization of unlabeled data instances by integrating them into the learning process through self-calibration, enhancing the model's ability to capture and represent the broader, underlying data distribution.

### Strengths
This methodology excels in intra-FID scoring, which is crucial for class-wise interpretation, particularly in scenarios with partially labeled data, demonstrating its effectiveness in maintaining class-specific fidelity even with limited label availability.

The approach of using score-based conditional generation in a semi-supervised learning context is not a commonly explored direction in research. This lends a novel aspect to the problem being addressed by this methodology.

### Weaknesses
The methodology appears incremental, building marginally upon JEM's foundation of interpreting classifiers as time-dependent EBMs. The newly introduced self-calibration loss primarily enhances this by applying a standard DSM technique to train the internal score function, thus lacking substantial novelty.

The authors have judiciously selected a range of baseline candidates for semi-supervised learning and reported performance results. However, the focus on datasets like CIFAR-10 and CIFAR-100 limits the assessment of the methodology's generalizability to more diverse or complex data scenarios.

* Minor weaknesses
The allocation of Figure 1 is too naive. Overall, you could have edited the space of main paper more wisely.

### Questions
Q1. Does the author's argument also suggest that, compared to Deep Generative Models (DGMs), classifier architectures may be more prone to over-fitting?

Q2. Why are the FID (Fréchet Inception Distance) scores for CFG-all or CFG-labeled methodologies notably poor?

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
The paper argues that the performance of classifier guidance score generative models(CGSGM) under limited labeled data setting is bottlenecked by over-fitting of the classifier whose conditional scores may be unreliable. The paper argues that while there are several regularization methods to prevent over-fitting of the classifiers the score of such classifiers is often not aligned with the unconditional SGM’s view of the underlying distribution and thus offers limited benefits. While other approaches exist to solve this issue of distribution alignment, they regularize the classifier by using an external SGM. In contrast, the paper does not use any external SGM to regularize the classifier, by taking inspiration from Joint energy-based models which interpret classifiers as energy-based models. The authors propose a self-calibration loss for regularizing the classifier without using using any external SGM and thus can train the classifier and the SGM on both labeled and unlabeled datasets.

With experiments on CIFAR-10 and CIFAR-100 on only 5% of the labeled data the authors show improved performance in intra-FID and accuracy metrics compared to other CGSGM approaches.

### Strengths
1. The experimental results for CIFAR-10 and CIFAR-100 are good an show the efficacy of the proposed approach.
2. The theoretical analysis done by the paper is sound.

### Weaknesses
1. While the paper mentions that simply regularizing the classifier to prevent over-fitting suffers from distribution alignment, not much experiments are done to justify this. The only baseline which the paper considers is the adversarial training of the classifier. I would like to see more experiments done with strong regularizers such as using RandAugment or CutMix augmentations. 

2. Further what would happen if the classifier is itself trained in a semi-supervised fashion with methods such as [1]. Such semi-supervised approaches perform very good with a limited data. The authors should do experiments with classifiers trained with such semi-supervised approaches.

3. For the CIFAR-100 results in table1 why doesn't it have the accuracy metric?

4. For the baseline CG-DLSM, the classifier is regularized over only labeled data using external SGM. However, this classifier can be regularized over unlabeled data also? What happens if this baseline's classifier is also regularized over unlabeled data? This would be a fairer comparison with the paper's results.

### Questions
I have already mentioned it in the weakness section

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on the development of a classifier guidance score-based generative model (CGSGM) for the semi-supervised setting with limited labeled data. The authors introduce a self-calibration (SC) loss that internally calibrates the classifier without depending on the unconditional SGM. Drawing inspiration from the reinterpretation of classifiers as energy-based models (EBM) as proposed by JEM, the authors devise a loss function trainable with both labeled and unlabeled data. This approach not only bolsters the generative capability of the classifier but also enhances the accuracy of the learned conditional distribution scores, which are computed from the classifier's logits output, thereby augmenting its conditional generative capacity. In terms of experimental validation, the authors initially test on a toy dataset using SC loss, illustrating how the SC loss improves classifiers by generating precise conditional distribution scores. They then contrast the CGSGM-SC approach with the existing vanilla classifier-guidance method (CG), various regularization methods designed to refine the classifier (CG-DLSM, CG-LS, CG-JR), and the classifier-free method (CFG) on the CIFAR-10 and CIFAR-100 datasets. The results demonstrate the superiority of their method in a semi-supervised setting with sparse labeled data.

### Strengths
1. This paper is commendable for its clear articulation of motivation. The writing exhibits a logical structure, and the methodology employed is both concise and straightforward, making it easy for readers to understand.
2. This paper has conducted extensive and thorough experiments comparing with all existing conditional score-based generative models, demonstrating the enhanced image generation capability of the classifier trained with the proposed SC loss (as shown in the Appendix G) and its superior performance in generation in the semisupervised setting with fewer labeled data (Sec 4.2).

### Weaknesses
1. This work is the lack of technical novelty. The proposed self-calibration (SC) loss in this paper heavily depends on two prior works. One is EBMs, which connect probability distribution and energy function. The other one is JEM, which reinterprets classifiers $f(\boldsymbol{x}, y ; \boldsymbol{\phi})$ as EBMs and enforcing regularization with related objectives helps classifiers $f(\boldsymbol{x}, y ; \boldsymbol{\phi})$ to capture more accurate probability distributions. Specifically, the SC loss essentially applies the JEM objective to the classifier within a score-based generative model framework, which does not introduce significant innovation beyond the existing literature.

2. While the method proposed in this paper demonstrates stronger capabilities when labeled data is extremely scarce (only 5% of the data is labeled), in many instances where labeled data exceeds 50% (as shown in Sec 4.2 and Appendix A), the CFG method exhibits greater conditional generative power than the proposed CG-SC method and traditional CG methods. Currently, the CFG method is the more prevalent approach in conditional generation, mainly because it eliminates the need for training an additional classifier and can seamlessly integrate into the conventional DSM loss, which is much more easier to be applied in downstream tasks.

### Questions
1. What is the hyperparameter $\lambda_{CG}$ for classifier guidance with and without self-calibration set in Table 1 for CG and CG-SC methods? As the traditional CG method regularizes the classifier externally by $\lambda_{CG}$ and the choice of the parameter $\lambda_{CG}$ chosen has a significant impact on the generation outcomes[1], there may be more experiment for CG by tuning the hyperparameter $\lambda_{CG}$ for a fair comparison. Moreover, there is also a hyperparameter classifier-free guidance scale $\lambda_{CFG}$ for CFG method [2], there should be more experiment on CFG methods by tuning the hyperparameter $\lambda_{CFG}$ for a fair comparison.

2. Why there is an inconsistency between conditional metrics and unconditional metrics? (Appendix H) The FID (Fréchet Inception Distance) serves as a metric to assess the diversity and authenticity of generated data distributions in comparison to true data distributions. In my view, if the conditional metrics for each category (intra FID) are better, then the overall unconditional metrics (FID) should also be better.

[1] Dhariwal P, Nichol A. Diffusion models beat gans on image synthesis[J]
[2] Ho J, Salimans T. Classifier-free diffusion guidance[J]. arXiv preprint arXiv:2207.12598, 2022

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a regularization approach for improving the training of Classifier-Guided Score-based Generative Models (CGSGM). The proposed method leverages the interpretation of the Joint Energy-based Model (JEM) model and adopts the Denoising Score Matching (DSM) loss in the optimization process to enhance its performance. The experiments show that the proposed Self-Calibration (SC) regularization loss is effective in conditional generation in terms of the intra-FID metric under the context of semi-supervised learning.

### Strengths
- Considering the computational cost, the proposed SC loss seems to be a more appealing option in comparison to the JEM’s maximum likelihood objective in augmenting the classifiers' ability to capture the underlying energy function.
- The comprehensive review in Section 2 offers readers a holistic perspective, aiding in their understanding of the background information related to CGSGM. In addition, the illustrative example in Fig. 3 serves as empirical evidence supporting the effectiveness of the proposed SC loss.
- The proposed method has demonstrated enhanced performance compared to other baseline methods on the selected two datasets when working with limited accessible labels.

### Weaknesses
 - The current formulation of the proposed method appears to lack conciseness, given that both $s(\boldsymbol{x},t;\phi)$ and $\nabla_\boldsymbol{x} \log \sum_{y} f(\boldsymbol{x}, y,t;\phi)$ can serve as parameterized score functions. In the context of the CG framework, one of these components should be redundant. Specifically, the paper does not clearly articulate the necessity of using both a learned score function $s(\boldsymbol{x},t;\phi)$ and the gradient of the log probability $\nabla_\boldsymbol{x} \log \sum_{y} f(\boldsymbol{x}, y,t;\phi)$ when both are, in essence, estimating the score. The justification for this redundancy, particularly in the context of classifier-guided generation, is not sufficiently explained.
- Table 1 lacks a performance comparison between the introduced method and the JEM framework. Given that the design of the proposed method bears considerable resemblance to JEM, it seems necessary to have a performance evaluation against JEM on real-world datasets. To incorporate the diffusion process into the JEM framework (i.e., the CG-JEM setup mentioned in Section 3.2) in real-world setups, the reviewer suggests using the method presented in [1]. Furthermore, the absence of a direct comparison with JEM makes it difficult to assess the true advantage of the proposed method, especially considering that JEM also aims to learn the underlying energy function.
- Diffusion score-based models have exhibited state-of-the-art performance for years, showcasing exemplary results on numerous benchmarks with photo-realistic data. However, the experiments in this paper are confined to an initial setup, focusing on images with a 32x32 resolution and only encompassing 100 classes. The reviewer is uncertain whether the proposed approach can demonstrate superior performance among the baselines on widely recognized benchmarks such as ImageNet. The limited scale of the experiments raises concerns about the generalizability of the proposed method to more complex and realistic scenarios.

### Questions
- The rationale behind the design of the proposed SC loss remains ambiguous. Could the authors elucidate with an analytical perspective why the proposed method should outperform the baselines (i.e., DLSM and JEM), which explicitly minimize the Fisher and KL divergences, respectively? Furthermore, could the authors theoretically justify the effectiveness of the proposed loss in a semi-supervised setup (e.g., defining the relationship of data-label pairs through optimal transport [2])?
- How were the hyper-parameters for the baseline methods, specifically the balancing factors of CG-DLSM and CG-JR, and the smoothing factor in CG-LS, chosen to ensure a fair comparison in Section 4?
____
Overall, I believe that semi-supervised CGSGM holds the potential to become a promising research direction. However, because of the aforementioned concerns and questions, I am giving this paper a borderline score. I am open to revising the score upwards if the issues and queries are adequately addressed.
____
**References**

[1] Gao *et al.* Learning Energy-Based Models by Diffusion Recovery Likelihood, *ICLR*, 2021.\
[2] Seguy *et al.* Large-Scale Optimal Transport and Mapping Estimation, *ICLR*, 2018.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
