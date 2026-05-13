# ViP: A Differentially Private Foundation Model for Computer Vision

- Decision: Reject
- Scores: 8, 3, 3

## Abstract
Artificial intelligence\,(AI) has seen a tremendous surge in capabilities thanks to the use of \emph{foundation models} trained on internet-scale data. On the flip side, the uncurated nature of internet-scale data also poses significant privacy and legal risks, as they often contain personal information or copyrighted material that should not be trained on without permission. In this work, we propose as a mitigation measure a recipe to train foundation vision models with differential privacy (DP) guarantee. We identify masked autoencoders as a suitable learning algorithm that aligns well with DP-SGD, and train \emph{ViP}---a \textbf{Vi}sion transformer with differential \textbf{P}rivacy---under a strict privacy budget of $\epsilon=8$ on the LAION400M dataset. We evaluate the quality of representation learned by ViP using standard downstream vision tasks; in particular, ViP achieves a (non-private) linear probing accuracy of $55.7\%$ on ImageNet, comparable to that of end-to-end trained AlexNet (trained and evaluated on ImageNet). Our result suggests that scaling to internet-scale data can be practical for private learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors proposed VIP, a recipe of privately training vision foundation models through self-supervised learning. The main insights are two-fold: 1) masked autoencoder is a suitable algorithm for DP-SGD which allows per-sample gradient clipping, as opposed to contrastive learning; 2) warm-start through non-private synthetic pretraining can greatly accelerate the training. The authors conducted comprehensive experiments to demonstrate the effectiveness of VIP, showing that it surpasses state-of-the-art methods on a variety of learning tasks.

### Strengths
- The motivation and insights are adequately delivered
- Strong and comprehensive empirical results
- Good writing and presentation

### Weaknesses
I don't see any apparent weakness of this work, but only a few minor suggestions:
- The experiments should be running over multiple random seeds, and please include the standard deviations in the tables as well
- It would be better to include a non-private version of VIP (i.e., non-private MAE) for comparison in the experiments (to reflect the cost of DP)
- It would be better to emphasize in the title and abstract that this paper focuses on applying DP to SSL, which is different from most prior works that focus on applying DP to supervised learning
- There is a concurrent work [1] which applied DP to the continued pretraining CLIP (using batched gradient clipping). The authors should discuss this work in Section 5
- Section 2, Eq. equation 1 -> Eq. (1)


Reference

[1] Huang, Alyssa, et al. "Safeguarding Data in Multimodal AI: A Differentially Private Approach to CLIP Training." arXiv preprint arXiv:2306.08173 (2023).

### Questions
I don't have further questions.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes how to train vision foundation models with privacy using the framework of differential privacy. The work targets only a single version of self-supervised encoders, namely MAE. The motivation is that the encoders can still leak private information. The ViP pre-trained encoder achieves accuracy for linear probing of 55.7% on ImageNet, which is comparable with AlexNet.

### Strengths
1. The paper proposes a DP method for the large-scale encoder models.

### Weaknesses
1. The motivation is very poor: the encoders should not be trained on copyright or private data in the first place instead of preventing the detection that they were trained on such data.
2. The method is limited to only the MAE and state-of-the-art methods such as DINO or DINO v2 are not supported, let alone the contrastive-based encoders such as SimCLR. 
3. The performance of the encoder trained on the large data is only 55.7% for the linear probing on ImageNet. One does not have to go through the same huge effort but instead, use a publicly trained model such as AlexNet to obtain the same performance.

Other comments:
1. Figure 1 is misplaced. First of all, it is way too early, since even no reference to the Figure is given on page 1. Second, the comparison is a strawman argument. ViP should be compared with the corresponding MAE encoder trained without DP.
2. It is claimed that: "More recently, Meehan et al. (2023) showed that non-generative vision SSL models can also be probed to reveal sensitive information about individual samples in its training data when given partial information." However, this work does not address the issues in the SSL encoders from Meehan et al. (2023), where no MAE encoders were considered!
3. " However, most vision SSL training algorithms are based on contrastive learning, where the objective function
depends on multiple samples in an entangled manner". This is not correct. There are many non-contrastive SSL methods, for example, SimSiam [1], DINOv1 [2], or DINO v2 [3], which is a state-of-the-art SSL encoder. In general, [4] considers contrastive and non-contrastive encoders.

**References:**
1. "Exploring Simple Siamese Representation Learning". Xinlei Chen, Kaiming He. https://arxiv.org/abs/2011.10566 CVPR 2021.
2. "Emerging Properties in Self-Supervised Vision Transformers" https://openaccess.thecvf.com/content/ICCV2021/papers/Caron_Emerging_Properties_in_Self-Supervised_Vision_Transformers_ICCV_2021_paper.pdf
3. "DINOv2: Learning Robust Visual Features without Supervision" https://arxiv.org/abs/2304.07193
4. "Contrastive and Non-Contrastive Self-Supervised Learning Recover Global and Local Spectral Embedding Methods" https://arxiv.org/pdf/2205.11508.pdf

### Questions
See the Weaknesses above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on differentially private representation learning for images. The authors empirically found that pretraining an MAE on synthetic images as the initialization then fine-tuning on private dataset with DP-SGD can boost the utility of learned features. Experiments show that it is even better than some non-private counterparts.

### Strengths
1. The differentially private representation learning is a well-motivated problem and has a wide range of applications.
2. Experimental results look superior compared to baselines.

### Weaknesses
1. The proposed training recipe is not new. It contains two main steps: (1) pretraining on a synthetic dataset where there is no privacy concern, then (2) fine-tuning on a private dataset with DP-SGD. Something similar was proposed in many prior papers. To name a few, [1,2] in NLP (which are also cited by the authors), and [3] in CV. A minor difference is that these works choose to pretrain on a public real dataset instead of a synthetic dataset. Therefore, I do not see much novelty in this training recipe.
2. The authors also claim that this recipe used by prior works, e.g. [1,2], is on supervised training. However, it is unclear what challenges you will have if you apply this recipe to SSL.
3. The motivation for choosing MAE is not adequately clear. There are certainly other methods that can compute gradient in a disentangled manner. Naively, the ordinary autoencoder (without mask) should also be able to do this job. Why is MAE particularly picked? If there are more options, a comparison is desired.
4. AlexNet is too old to compare, which was proposed more than 10 years ago. There are too many recent baselines you can compare. (Even SimCLR is not the latest, but at least it is within 3 years).
5. Comparison in Table 1 is not fair. It looks to me that the ViP-LAION should be ViP-ImageNet-1k so that the readers can appreciate the benefit of an additional pretraining on the synthetic dataset.
6. There are many claims in this paper without enough explanations. See my questions below.


[1] Yu, Da, et al. "Differentially Private Fine-tuning of Language Models." ICLR 2022.

[2] Li, Xuechen, et al. "Large language models can be strong differentially private learners." ICLR 2022.

[3] Luo, Zelun, et al. "Scalable differential privacy with sparse network finetuning." CVPR 2021.

### Questions
1. Point 1 in page 2, "...attaining high-utility learned representations requires significantly more training data...", why it is more than supervised learning?
2. Point 3 in page 2, "SSL training requires a much larger number of training epochs compared to supervised learning,..." why?
3. Still in page 2, "We also show that it is tolerant to the large amount of Gaussian noise added in DP-SGD." Where do you show and why?
4. How are your synthetic data generated? From a generative model? If so, does the training set of the generative model contain any private information?
5. At the beginning of sec 3, "1. Scaling up the number of training samples via SSL with masked autoencoder;" what does this mean?
6. At the end of sec 3.1, "With more training samples, the magnitude of the injected noise becomes smaller." Why?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
