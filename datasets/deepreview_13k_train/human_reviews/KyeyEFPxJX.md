# CLIP-Enhance: Improving CLIP Zero-Shot Classification via von Mises-Fisher Clustering

- Decision: Reject
- Scores: 3, 5, 3, 3, 5, 3

## Abstract
Contrastive language-image pre-training (CLIP) has revolutionized computer vision by integrating natural language understanding with image analysis, enabling zero-shot classification without prior training on specific classes. However, recent efforts to improve the performance of frozen CLIP models through prompt tuning and adapter mechanisms have introduced additional system complexity and training requirements, thus undermining CLIP's inherent efficiency in zero-shot knowledge transfer. In this paper, we propose to address two common challenges in zero-shot classification using CLIP: 1) the misalignment between textual and image embeddings, and 2) the long-tailed distribution of CLIP's training dataset. Our approach, CLIP-Enhance, is motivated by a re-interpretation of CLIP zero-shot classification as a clustering problem on a hypersphere using a von Mises-Fisher mixture model. Inspired by the DINO self-supervised learning framework, we optimize this mixture model to simultaneously improve the alignment of textual and image embeddings as well as represent data distribution disparities between training and evaluation datasets. Empirically, we show that jointly optimizing for both embedding alignment and concentration via self-supervised learning improves CLIP zero-shot classification significantly across multiple benchmark datasets. We also show empirically how CLIP-Enhance mitigates problems (1) and (2), as well as its robustness to limited data through a series of additional experiments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper propose a method named CLIP-Enhance to improve CLIP zero-shot classification. CLIP-Enhance addresses two challenges: (1) the misalignment between image and text embeddings, and (2) the long-tailed distribution of CLIP's training data. The authors re-fomulate zero-shot classification as a von Mises-Fisher clustering problem. Then an self-supervised learning method is proposed to optimize both alignment and concentration. Experiment results show that the proposed method can improve zero-shot classification accuracy.

### Strengths
1. The idea of reformulating CLIP zero-shot classification as a clustering problem is interesting.
2. This paper is well-organized and easy to follow.

### Weaknesses
1. My major concern is the limited evaluation. The results of CALIP and TPT on C-10, C-100 and MNIST are not provided. The results on Caltech101, Aircraft, Stanford Cars and UCF101 are not provided, which are widely used for zero-shot evaluation in prior works. 
2. The article claims to improve the misalignment between class embedding and image embedding, but how does this misalignment affect downstream task performance? The article needs to provide a more in-depth analysis. Specifically, it is unclear how the proposed method addresses the inherent ambiguity in mapping images to text embeddings, especially when multiple classes might share similar visual features. A more rigorous explanation of the mechanism by which the method disentangles these ambiguities is needed.
3. The reported improvement of "alignment" in Table 2 is too small to support the conclusion. Have the authors considered using other metrics or methods to demonstrate it? such as visualizations of the embedding space or quantitative measures of clustering quality. The current metric, while showing a slight improvement, does not provide a strong enough indication that the proposed method is effectively aligning image and text embeddings in a meaningful way. It would be beneficial to see a more substantial improvement or a more compelling metric.
4. The sensitivity of the initial concentration parameter was briefly examined. But when $\kappa_0 = 5000$, the performance drop significantly on F-102 (67.3 $\rightarrow$ 11.3) and MNIST (64.95 $\rightarrow$ 53.1). Further analysis of the robustness of the proposed method on different $\kappa_0$ is needed. This sensitivity raises concerns about the practical applicability of the method, as it suggests that the performance is highly dependent on the choice of this parameter. A more thorough investigation into the parameter's behavior and its impact on different datasets is necessary.

### Questions
see weaknesses

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
This paper proposes a vMF-based teacher-student knowledge distillation tuning framework to enhance the CLIP zero-shot performance. Technically, it proposes two strategies: (1) closed-form approximation of normalization term of vMF distribution to model variance statistics of different categories; (2) knowledge distillation with confident view selection for stabler fine-tuning. The experimental results demonstrate the superior performance of CLIP-Enhance compared with some baselines on multiple downstream zero-shot classification benchmarks.

### Strengths
Strengths:

- The idea of closed-form approximation of the vMF normalization constant is novel.
- The ablation results can validate the effectiveness of vMF distribution modeling.

### Weaknesses
Limitations:

- Missing baselines: It seems there is a line of missing related works that are not compared, including [1], [2], [3], [4]. Furthermore, the authors still seem to miss an important related work that achieves the same goal [1]. I consider it necessary to have a direct comparison.
- Insufficient experiments: (1) Although the author claims that the proposed method with vMF distribution can address the long-tail issue of CLIP, it is still indispensable to ablate the long-tailed downstream tasks. (2) What are the performance gains from the confident view selection? Why it is top 10%?
- Question: How does the learned $\kappa$ differ from different classes? Better to present statistics or analysis. Why cannot tune the existing blocks of CLIP and add an additional projector?
- The alignment calibration between visual and language embeddings is minor. Could you please provide more results on additional baselines to get the knowledge of the difficulty of this task? This can better solidify your hypothesis on the explanatory factors. Besides, when authors claim the parameter efficiency compared with previous tuning methods, it is also necessary to list the FLOPs or #params or wall-clock tuning time to clarify, since this work also involves dataset-specific tuning at test time.

### Questions
All my concerns are listed in the weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces CLIP-Enhance, a method to improve CLIP's zero-shot classification by addressing two key issues: misalignment between text and image embeddings and the long-tailed distribution of the training data. CLIP-Enhance reinterprets zero-shot classification as a clustering problem on a hypersphere using a von Mises-Fisher (vMF) mixture model. This model optimizes both the alignment and concentration of embeddings through self-supervised learning, inspired by the DINO framework. The empirical findings reveal a remarkable enhancement in the performance of zero-sample classification across multiple benchmarks, manifesting superior management of data distribution disparities and robustness under limited data circumstances.

### Strengths
1.As claimed by the authors, they propose a SOTA zero-shot classification structure based on CLIP, which performs well on related benchmarks and limited compute/data resources.

2.The novel vMF mixture model proposed in the paper is justified, as the knowledge distillation introduced in the confidence selection section is quite reasonable, and the convergence of von Mises-Fisher clustering can be mathematically substantiated.

### Weaknesses
1.More ablation experiments are needed to increase confidence of your method, as experimental result comparisons with counterparts on some important datasets are missing.

2.There are some imprecise statements in the paper, and the CLIP-Enhance method lacks visual demonstration of results. It is necessary to add the relevant content in the appendix.

3.Using only naive TPT as the baseline in your ablation studies is unreasonable. At minimum, the state-of-the-art (SOTA) results from CoOp+TPT should also be included as a baseline. As we all know, CoOp+TPT outperforms naive TPT across the board, and for CLIP-Enhance to be considered a SOTA method, it needs to surpass those results of CoOp+TPT.

4.The statement of 'This is an image of a [CLASS].' isn't accurate, as the default use of CLIP prompt template is 'A photo of a [CLASS].'. Like  the figure 1 presented in your paper, these two prompt templates are different in embedding hypersphere and bring discrepancies to the experimental results, even if the difference is quite slight. Scientific writing should be professional and rigorous, and 'the devil is in the details'. You may have been careless, but I still can't believe that such a rookie mistake would appear in a paper submitted to ICLR. I hope you can carefully check the references and mathematical derivations in the paper again, to ensure the accuracy and standardization of the article.

### Questions
1.Your experiments on 10 datasets are quite far from enough. As your most competitive counterparts, CALIP and TPT have both conduct experiments on ImageNet-V2/ A / R/ Sketch, as well as other smaller but typical datasets like OxfordPets and StanfordCars. I have no idea why your work ignore those important experiments. Maybe lack of time for the submission deadline? If so, you can supplement the information during the subsequent rebuttal phase. Once the requirements are met, I will reset my review score.

2.Using only naive TPT as the baseline in your ablation studies is unreasonable. At minimum, the state-of-the-art (SOTA) results from CoOp+TPT should also be included as a baseline. As we all know, CoOp+TPT outperforms naive TPT across the board, and for CLIP-Enhance to be considered a SOTA method, it needs to surpass those results of CoOp+TPT.

3.The statement of 'This is an image of a [CLASS].' isn't accurate, as the default use of CLIP prompt template is 'A photo of a [CLASS].'. Like  the figure 1 presented in your paper, these two prompt templates are different in embedding hypersphere and bring discrepancies to the experimental results, even if the difference is quite slight. Scientific writing should be professional and rigorous, and 'the devil is in the details'. You may have been careless, but I still can't believe that such a rookie mistake would appear in a paper submitted to ICLR. I hope you can carefully check the references and mathematical derivations in the paper again, to ensure the accuracy and standardization of the article. 

4.More experimental details and visualized experimental results can be placed in the appendix, which would further analyze and demonstrate your method, allowing readers to more intuitively understand the value and significance of your work. Although ICLR has restrictions on the length of the main text, detailed mathematical derivations and experimental results can be elaborated in the appendix section.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose CLIP-Enhance to tackle the misalignment between multi-modal embeddings and the long-tailed distribution of CLIP's training dataset.
They reinterpret CLIP's zero-shot classification as a clustering problem on a hypersphere using a von Mises-Fisher mixture model and use a knowledge distillation loss for optimization.
Empirical results demonstrate that CLIP-Enhance improves CLIP's zero-shot classification performance across various benchmarks.

### Strengths
1. The authors analyze in detail the reasons why CLIP's performance is limited, mainly due to the misalignment between modalities and the imbalance of training data.
2. The authors proposed CLIP-Enhance, which consists of von Mises-Fisher mixture model and knowledge distillation, to further improve the classification performance of CLIP.

### Weaknesses
1. The experiment lacks some commonly used datasets, such as fine-grained datasets such as Caltech101 and out-of-distribution datasets such as ImageNet-A. Please follow TPT paper to organize experiments to prove the effectiveness of the proposed algorithm.
2. The comparison in the experiments is not fair. CLIP-Enhance uses the entire dataset in the distillation stage and is an unsupervised fine-tuning method based on the entire data, while TPT only uses one test sample for optimization and prediction. Therefore, CLIP-Enhance uses more information, resulting in unfair comparison. 
3. The writing of the submission is not clear. For example, some concepts in Line248-Line252 are confusing.

### Questions
1. The author mentioned the modal misalignment and data imbalance of the clip model, why CLIP-Enhance solve these two challenges?
2. There are 'N/A' in the experimental results of methods such as TPT in Table 1. These methods are open-source, why not reproduce them?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposed a new approach, named CLIP-Enhance, to improve the zero-shot ability of CLIP. CLIP-Enhance re-interprets the CLIP zero-shot classification as a clustering problem on a hypersphere using a von Mises-Fisher mixture model. Besides, CLIP-Enhance is optimized to improve the alignment of text and image vectors. Experiments on multiple benchmarks show the effectiveness of the proposed method.

### Strengths
1. This paper presents CLIP-Enhance, a novel approach to strengthen CLIP's zero-shot capabilities. CLIP-Enhance reframes CLIP's zero-shot classification as a clustering problem on a hypersphere, utilizing a von Mises-Fisher mixture model.
2. A self-supervised learning framework is proposed to improve the alignment between text and image features. 
3. Experiments on ten datasets show the effectiveness of the proposed method.

### Weaknesses
1. The self-supervised training approach is not new; using data augmentation to create varied views and encourage the model to produce predictions consistent with the original sample is a common strategy in current SSL methods. The method used in this paper is a simplified version of approaches like SimCLR, which maximizes similarity between augmentations of the same image, or BYOL, which generates different augmented views and trains the model to predict the representation of one view from another.
2. The paper claimed that jointly optimizing both vision-text alignments in embedding space and embedding concentration estimates based on SSL benefits the vMF mixture model. However, as illustrated in Figure 2, there is no component specifically for vision-text alignment.  Additionally, I did not find any explicit constraints in the paper to enforce this alignment. I would appreciate it if the author could clarify whether the alignment is simply a byproduct of the self-supervised training process.
3. The author found the long-tailed distribution of CLIP's training dataset, The method proposed in this paper addresses this issue by constructing a balanced training dataset. However, this approach has practical limitations, as it is often infeasible to collect an equal number of training samples for each class, and long-tailed distributions are common in the real world.

### Questions
The current method focuses more on the image encoder of CLIP. Did the author consider how to generate better text features outputted by the text encoder?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an approach that learns teacher-student von Mises-Fisher (vMF) mixture models on test data to improve zero-shot image classification performance of CLIP. 
It first reformulates the zero-shot classification into the vMF clustering problem parameterized by vMF mixture weights and concentration parameters. Then it constructs a teacher-student pipeline and performs knowledge distillation by encouraging the teacher predicted probability (based on full view of image) to be close to the student predicted probabilities (based on augmented local views).

### Strengths
1) It is an interesting angle to formulate the zero-shot classification into vMF clustering problem 
2) Training the vMF weights on test data leads to performance improvement on several image datasets

### Weaknesses
1) In the abstract and introduction, the paper motivates that the usage of vMF mixture model addresses two common challenges a) the incorrect assumption that embeddings of images of a given class are distributed anisotropically around the canonical text embedding  b) the long-tailed distribution of CLIP’s training dataset.
However, I do not see how the proposed approach equipped with vMF mixture model addresses these two challenges. 
It seems to me that the approach just iteratively tunes the CLIP text embedding (which is the W matrix in the vMF model) of category texts (which are initialized with the template “This is an image of [class]”) in a teacher-student setup. The setup is similar to TPT (Shu et al. 2022) which performs tuning of learnable prompts in the input (instead of CLIP text embedding). 
The authors can provide more explicit explanations or empirical evidence demonstrating how their vMF mixture model approach addresses the two challenges mentioned. 
2) In line 413, it is mentioned that “the online test-time adaptation setup of TPT (Shu et al. 2022)”. According to my understanding, TPT does not have an online test-time adaptation setting but a single-sample test-time adaptation setting. It adapts to and then evaluates on a test sample every time. The model updates are not accumulated across different test samples. 
While TPT only adapts to one test sample at a time, this paper, however, adapts to the entire test set. Therefore the comparison in Table 1 is not completely fair. The authors could also try the single-sample adaptation setting for a fair comparison. 
3) In Algorithm 2, we see that the teacher and student vFM mixtures are initialized as \kappa_0 * W_text. 
W_text is computed from from CLIP text embedding of the category texts “This is an image of [class]”. 
In the experiment, \kappa_0  is set to a large value of 3000 based on the empirical observation that the CLIP similarities are in the range [0.2, 0.4]. This might not generalize to datasets of varying CLIP similarities.
How is the impact of \kappa_0 on the performance? The authors could consider conducting an ablation in this regard, testing a range of \kappa_0 values and report how they affect performance across different datasets.
4) The structure of the related work section is cluttered. It is better to organize that with corresponding headings.

### Questions
1) In equation 5, why do we need the component  F_d(W)? Is there an ablation study to validate the contribution of F_d(W)? 
2) Line 228 “We remark that if all concentration parameters are equal, then in fact P_W (x_hat) = /sigma (W x_hat)”. When are all concentration parameters equal?

### Soundness
2

### Presentation
1

### Contribution
2
