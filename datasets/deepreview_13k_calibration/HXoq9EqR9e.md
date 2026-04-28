# FairerCLIP: Debiasing CLIP's Zero-Shot Predictions using Functions in RKHSs

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Large pre-trained vision-language models \review{such as CLIP} provide compact and general-purpose representations of text and images that are demonstrably effective across multiple downstream \review{zero-shot prediction} tasks. However, owing to the nature of their training process, these models have the potential to 1) propagate or amplify societal biases in the training data and 2) learn to rely on spurious features. This paper proposes \methodName{}, a general approach for making zero-shot predictions of \review{CLIP} more fair and robust to spurious correlations. We formulate the problem of jointly debiasing \review{CLIP's} image and text representations in reproducing kernel Hilbert spaces (RKHSs), which affords multiple benefits: 1) \emph{Flexibility:} Unlike existing approaches, which are specialized to either learn with or without ground-truth labels, \methodName{} is adaptable to learning in both scenarios. 2) \emph{Ease of Optimization:} \methodName{}{} lends itself to an iterative optimization involving closed-form solvers, which leads to $4\times$-$10\times$ faster training than the existing methods. 3) \emph{Sample Efficiency:} Under sample-limited conditions, \methodName\ significantly outperforms baselines when they fail entirely. And, 4) \emph{Performance:} Empirically, \methodName{} achieves appreciable accuracy gains on benchmark fairness and spurious correlation datasets over their respective baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes FairVLM, which is an additional module top on the frozen CLIP features, to de-bias the prediction. Using the frozen CLIP vision and text encoders, the proposed method extracts visual and texture features, and lets them be de-biased using the Hilbert-Schmidt Independence Criterion (HSIC), a famous approach in de-bias literature. Instead of using the original HSIC, this paper proposes to use a simplified version following Sadeghi et al. The proposed simplified HSIC provides a closed-form solution to the additional feature encoders when the features are fixed. To make the method efficient, this paper proposes to approximate Cholesky decomposition using random Fourier features (RFF), resulting in reducing the computational complexity from $O(n^3)$ to $O(n^2)$. Experimental results show that the proposed method shows the effectiveness of the proposed method in both intrinsic dependency (i.e., fairness scenario) and spurious correlation.

### Strengths
HSIC is a promising approach to achieving de-biased representations, as many previous studies have observed. This paper successfully brings the advantage of HSIC to CLIP feature refinement tasks. I also think that this paper has a non-trivial contribution to introducing the closed-form solutions used for updating the parameters, including the approximated version of Cholesky decomposition using RFF. Straightforwardly, an iterative algorithm using a closed-form solution will converge much faster than gradient-based algorithms, as shown in classic machine learning studies, such as ADMM [R1]

- [R1] Boyd, Stephen, et al. "Distributed optimization and statistical learning via the alternating direction method of multipliers." Foundations and Trends® in Machine learning 3.1 (2011): 1-122.

Combining two good properties (HSIC, a promising approach, and an efficient update algorithm using a closed-form solution), the proposed method shows promising performances on the given evaluation benchmarks.

### Weaknesses
### Scope of the paper

The terminology "VLM" is misused in this paper. VLM literally includes a vast area of models trained with vision and language. For example, visual-question answering (VQA) is a VLM model, vision-language pre-training (VLP) with cross-attention transformers (such as ViLBERT [R2], ViLT [R3], Align [R4], VinVL [R5], ALBEF [R6], BLIP [R7]) is VLM, multi-modal generation models, such as dall-e 1, 2 and 3, stable diffusion or dreambooth, are VLM, and recent language-model combined vision models, such as BLIP2 [R8], Fromage [R9], GPT-4, are VLM. (I omitted some famous works, such as dall-e, SD, GPT ...).

- [R2] Lu, Jiasen, et al. "Vilbert: Pretraining task-agnostic visiolinguistic representations for vision-and-language tasks." Advances in neural information processing systems 32 (2019).
- [R3] Kim, Wonjae, Bokyung Son, and Ildoo Kim. "Vilt: Vision-and-language transformer without convolution or region supervision." International Conference on Machine Learning. PMLR, 2021.
- [R4] Jia, Chao, et al. "Scaling up visual and vision-language representation learning with noisy text supervision." International conference on machine learning. PMLR, 2021.
- [R5] Zhang, Pengchuan, et al. "Vinvl: Revisiting visual representations in vision-language models." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2021.
- [R6] Li, Junnan, et al. "Align before fuse: Vision and language representation learning with momentum distillation." Advances in neural information processing systems 34 (2021): 9694-9705.
- [R7] Li, Junnan, et al. "Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation." International Conference on Machine Learning. PMLR, 2022.
- [R8] Li, Junnan, et al. "Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models." arXiv preprint arXiv:2301.12597 (2023).
- [R9] Koh, Jing Yu, Ruslan Salakhutdinov, and Daniel Fried. "Grounding language models to images for multimodal generation." arXiv preprint arXiv:2301.13823 (2023).

However, the scope of this paper is very narrow compared to the entire VLM family. I feel that the title "FairVLM" and the terminology "VLM" are too much overclaimed, and a reader can misunderstand the focus of this paper. I think this paper should tone down its contribution and focus more specifically. This paper only targets a feature refinement method top on the frozen CLIP model, and the comparison methods are also methods using frozen CLIP encoders. Note that it is still a narrow topic in "de-biasing CLIP zero-shot prediction" because a number of works focus on the fine-tuning strategy [R10-12]. On the other hand, this paper relies on the pre-trained feature encoders that may weakens its contribution.

- [R10] Wortsman, Mitchell, et al. "Robust fine-tuning of zero-shot models." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.
- [R11] So, Junhyuk, et al. "Geodesic multi-modal mixup for robust fine-tuning." arXiv preprint arXiv:2203.03897 (2022).
- [R12] Vogt-Lowell, Kevin, et al. "Robust Fine-Tuning of Vision-Language Models for Domain Generalization." IEEE High Performance Extreme Computing Conference (HPEC). 2023.

### Missing related works

Including [R1-12] in the first comment, there are a number of missing related works that should be discussed. For example, HSIC is a popular approach in de-biasing studies [R13, R14]. R13 directly optimizes the HSIC between features and sensitive attribute labels, similar to Dep(Z, Y) in the paper; R14 optimizes the HSIC between biased features and target features to avoid using sensitive attribute labels Y. If we extend our viewpoint to RHKS, there is work using MMD to achieve fairness [R15]. I omitted many HSIC-based regularization methods that could be related to this work, but if possible, it would be great to add more citations for methods using HSIC.

- [R13] Quadrianto, Novi, Viktoriia Sharmanska, and Oliver Thomas. "Discovering fair representations in the data domain." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2019.
- [R14] Bahng, Hyojin, et al. "Learning de-biased representations with biased representations." International Conference on Machine Learning. PMLR, 2020.
- [R15] Jung, Sangwon, et al. "Fair feature distillation for visual recognition." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2021.

Also, in terms of employing pseudo-labels for the de-biasing optimization, I think this paper is also related to [R16]; where R16 is based on semi-supervised learning without the pseudo-label refinement process.

- [R16] Jung, Sangwon, Sanghyuk Chun, and Taesup Moon. "Learning fair classifiers with partially annotated group labels." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

### Unclear or missing details

While reading the paper, I had trouble understanding the details of the paper. For example, it is still unclear to me how the "encoder" works. I presume that the encoder parameter $\Theta$ is a linear projection and an RBF kernel is used for computing HSIC, but it is unclear. Also, there is no description of $r$ (r becomes the dimensionality of the generated representation) and the value of $r$ as well. It means that this paper does not provide any detail of RKHS hyperparameters, such as the dimensionality of the projection layer and the hyperparameter of the kernel method. Similarly, I cannot find any detail of the choice of the learning hyperparameters, such as the number of iterations, and batch size. It means that it is impossible or extremely difficult to reproduce the results in this paper. Overall, this paper is very hard to understand the method details and implementation details, although I think this paper has certain contributions in terms of the methodology development.

### Questions
I think the technical contribution of this paper is sound and empirical evaluation results look reasonable. However, this paper has a critical problem in its writing and presentation, including many missing related works and details. Please check my initial review and respond to my concerns. Specifically, I would like to clarify all the details of how the method is implemented and trained in the revised version, which is not presented in the initial version. I think the initial version is improper to be published as an ICLR paper, but my concern is mostly around the writing, that could be improved during the revision period. I presume that the revised manuscript will need significant efforts, but mainly in the presentation, rather than technical enhancement. Hence, if the revised manuscript is sound and can resolve my initial concerns, I am willing to update my score.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper introduces FairVLM, a novel approach designed to address bias in zero-shot predictions made by VLMs. FairVLM demonstrates versatility in mitigating bias arising from two primary sources: spurious correlations and intrinsic dependencies within the data. Moreover, it offers the flexibility to be trained with or without the presence of ground-truth labels.

### Strengths
1. The paper demonstrates that a single general method can debias the image and text features of VLMs under different scenarios more effectively than specialized solutions for each scenario. The scenarios include accounting for both spurious correlations and intrinsic dependencies, learning with and without ground-truth labels, and learning from small and medium-sized datasets
2. The words are fluent.

### Weaknesses
1. The experiment results on the datasets (w/ labels) are not good enough.
2. The pare of the method is too complex.

### Questions
I don't have any questions because I cannot understant the method part.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper suggested a VLM debiasing method that remove bias in visual and text representations jointly by using reproducing kernel Hilbert space and deploying statistical dependency measure in RKHS. This enables to considering nonlinearity between the representation and the attribute. This paper provides a closed form solution for such formulation, and theoretical analysis on its complexity. Experiments show that the suggested method can work well both with and without true labels setting.

### Strengths
- Paper is well written and organization is clear.
- While previous methods mainly depend on the linearity of representation and the attribute, the suggested method can overcome such linearity assumption using RKHS.
- The suggested method is practically competitive in both of settings — w or w/o labels.
- Ablation experiments cover various scenarios, providing solid understanding of variables that affect performance.

### Weaknesses
While one of core features of VLM is zero-shot classification, the suggested method still requires parameter tuning (RBF kernel parameter) and stacking train data for cross-validation, which could be a limitation of the method. Furthermore, while the method can be applied to a single test sample at inference time, it cannot be trained on a single test sample, requiring a separate dataset for training or stacking test data for test-time adaptation. This limits its applicability in scenarios where only a single or few test samples are available without a separate training set. The method also appears to sacrifice average accuracy more than other methods like Contrastive Adapter in Table 2 when labels are available, and its performance is similar with and without labels on CelebA, raising questions about its effectiveness in scenarios where labels are readily available. The CFD results, while interesting, also highlight a potential limitation of the method when the initial zero-shot predictions are poor, which could impact the pseudo-labeling process. Finally, the lack of a theoretical convergence guarantee for Algorithm 1, especially concerning the propagation of errors from the initialization step, is a concern.

### Questions
- Can this method be extended to a single point debiasing? (i.e. a single point inference for online prediction?)
- It looks like FairVLM sacrifices average scores more than other methods such as Contrastive Adapter in Table 2 w/ labels result. Furthermore, FairVLM works similarly in w/labels and w/o labels in CelebA. What’s a good interpretation on this?
- Table 3 CFD results look interesting! Does it imply FairVLM has its strength when the number of training samples is limited? How do other zero-shot methods in CFD dataset?
- Is there any convergence guarantee for Algorithm 1 (FairVLM Training Without Labels)? Also, I am wondering if there can be a failure mode that the errors in the initialization step propagate further in iteration steps.
- Possibly related works
    - Chen, A. S., Lee, Y., Setlur, A., Levine, S., & Finn, C. (2023). Project and Probe: Sample-Efficient Domain Adaptation by Interpolating Orthogonal Features. *arXiv preprint arXiv:2302.05441*.
    - Adila, D., Shin, C., Cai, L., & Sala, F. (2023). Zero-Shot Robustification of Zero-Shot Models With Foundation Models. *arXiv preprint arXiv:2309.04344*.
    - An, B., Zhu, S., Panaitescu-Liess, M. A., Mummadi, C. K., & Huang, F. (2023, July). More Context, Less Distraction: Improving Zero-Shot Inference of CLIP by Inferring and Describing Spurious Features. In *Workshop on Efficient Systems for Foundation Models@ ICML2023*.

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
In this work, the authors address the fairness problems in visual-language models (VLMs). More specifically, they propose a framework for jointly debiasing VLMs’ image and text representations. The proposed framework utilizes an alternating optimization-based approach to debias VLM representations. The authors evaluate their work using several datasets and show that FairVLM alleviates the debiasing problems of vanilla VLMs.

### Strengths
1. Compared to previous debiasing works in VLMs, FairVLM results in the debiasing of both image and textual representations.

2. FairVLM is agnostic to the availability of data labels and can generate debiased representations with or without labels.

3. Using the properties of RKHS in mapping the original VLM representations to a debiased space is interesting.

### Weaknesses
1. The authors did not compare their results with unimodal baselines, i.e., techniques that debias only the image/text representations of the VLM.

2. While the authors argue that RKHS has nice universal approximation properties, it's unclear how and why they aid in debiasing the original representations.

### Questions
Please refer to the weakness section for more details.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
