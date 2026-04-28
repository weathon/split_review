# Towards Syn-to-Real IQA: A Novel Perspective on Reshaping Synthetic Data Distributions

- Decision: Reject
- Scores: 5, 6, 6, 6, 6

## Abstract
Blind Image Quality Assessment (BIQA) has advanced significantly through deep learning, but the scarcity of large-scale labeled datasets remains a challenge. While synthetic data offers a promising solution, models trained on existing synthetic datasets often show limited generalization ability. In this work, we make a key observation that representations learned from synthetic datasets often exhibit a discrete and clustered pattern that hinders regression performance: features of high-quality images cluster around reference images, while those of low-quality images cluster based on distortion types. Our analysis reveals that this issue stems from the distribution of synthetic data rather than model architecture. Consequently, we introduce a novel framework SynDR-IQA, which reshapes synthetic data distribution to enhance BIQA generalization. Based on theoretical derivations of sample diversity and redundancy's impact on generalization error, SynDR-IQA employs two strategies: distribution-aware diverse content upsampling, which enhances visual diversity while preserving content distribution, and density-aware redundant cluster downsampling, which balances samples by reducing the density of densely clustered areas. Extensive experiments across three cross-dataset settings (synthetic-to-authentic, synthetic-to-algorithmic, and synthetic-to-synthetic) demonstrate the effectiveness of our method. Additionally, as a data-based approach, SynDR-IQA can be coupled with model-based methods without increasing inference costs. The source code will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a framework, SynDR-IQA, for improving blind image quality assessment (BIQA) models’ generalization by reshaping synthetic data distributions. It introduces two core strategies—distribution-aware diverse content upsampling (DDCUp) and density-aware redundant cluster downsampling (DRCDown)—to balance synthetic data diversity and redundancy, improving models' performance across synthetic and authentic datasets.

### Strengths
1. Identifies and addresses critical limitations in synthetic data for BIQA, specifically clustered feature distributions that hinder generalization.
2. Develops SynDR-IQA, which reshapes synthetic data distribution through theoretically grounded strategies (DDCUp and DRCDown), promoting model generalizability.
3. Extensive experiments confirm SynDR-IQA’s superior performance over existing methods in multiple cross-dataset scenarios.

### Weaknesses
See the questions

### Questions
1. The experimental setup and Table I could be improved by using a larger synthetic dataset annotated with human or pseudo labels, similar to the annotation method used in RankIQA. This would more effectively showcase the advantages of learning from synthetic data for BIQA tasks.


2. The paper’s selection of UDA (unsupervised domain adaptation) methods lacks classical approaches. Including comparisons with well-established UDA methods, such as Maximum Mean Discrepancy (MMD), Domain-Adversarial Neural Networks (DANN), and optimal transport for domain adaptation, would provide a more comprehensive analysis of SynDR-IQA’s performance.


3. There are numerous typographical errors throughout the paper, including "Kadid-10k" on line 521, and inconsistencies in capitalization on lines 281 to 283. Careful proofreading is needed to correct these and other similar errors.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
1. **Feature Distribution Issue**: Models trained on synthetic data show discrete and clustered features, limiting generalization due to synthetic data distribution.

2. **SynDR-IQA Framework**: Introduces DDCUp and DRCDown strategies to enhance diversity and balance density, reshaping data for better generalization.

3. **Validation**: SynDR-IQA proves effective across cross-dataset scenarios and integrates with existing models without extra inference costs.

### Strengths
1. **Innovative Approach**: Proposes SynDR-IQA, a novel framework that reshapes synthetic data distribution to improve BIQA generalization.

2. **Effective Strategies**: Introduces DDCUp and DRCDown, two strategies that enhance data diversity and reduce redundancy, addressing core issues in synthetic datasets.

3. **Strong Experimental Validation**: Demonstrates effectiveness across multiple cross-dataset settings, showing that SynDR-IQA enhances performance without increasing inference costs.

### Weaknesses
1. **lack of IQA result images**. Visual examples comparing predictions with ground truth would clarify SynDR-IQA's impact on quality assessment.
2. **Synthetic Data Focus**: Primarily targets synthetic data limitations, which may limit applicability to real-world data.
3. **Limited Analysis on Failure Cases**: The paper lacks discussion on SynDR-IQA's potential limitations or specific cases where it may underperform, such as certain distortion types or datasets. A balanced evaluation could clarify the framework's boundaries.

### Questions
1. **Lack of Comparisons with Advanced Methods**: : The paper does not include comparisons with state-of-the-art methods like Q-align[1], LIQE[2], CLIPIQA[3], and TOPIQ[4], which would provide a clearer benchmark of SynDR-IQA’s performance.

2. **Complex Implementation**: The DDCUp and DRCDown strategies, while theoretically valuable, add complexity in implementation. Practical adoption may be challenging without detailed instructions or code, possibly limiting its use in broader BIQA applications.

﻿3. **Synthetic Data Focus**: The framework mainly addresses synthetic-to-real transitions, which may limit its applicability and effectiveness on purely real-world distortions where data characteristics and distortion patterns differ substantially from synthetic ones.




[1] Wu, Haoning, et al. "Q-align: Teaching lmms for visual scoring via discrete text-defined levels." arXiv preprint arXiv:2312.17090 (2023).

[2] Zhang, Weixia, et al. "Blind image quality assessment via vision-language correspondence: A multitask learning perspective." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2023.

[3] Wang, Jianyi, Kelvin CK Chan, and Chen Change Loy. "Exploring clip for assessing the look and feel of images." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 37. No. 2. 2023.

[4] Chen, Chaofeng, et al. "Topiq: A top-down approach from semantics to distortions for image quality assessment." IEEE Transactions on Image Processing (2024).

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a SynDR-IQA framework, which aims to improve the generalization ability of BIQA models by adjusting the distribution of synthetic data, i.e., distribution-aware diverse content up-sampling and density-aware redundant cluster down-sampling. Experiments across three cross-dataset settings, including synthetic-to-authentic, synthetic-to-algorithmic, and synthetic-to-synthetic, demonstrate the effectiveness of SynDR-IQA.

### Strengths
1. Improving the generalization of deep models by adjusting the distribution of synthetic data is a promising research direction.

2. A theoretical derivation of the effect of sample diversity and redundancy on the generalization error was made in the paper, thus laying a theoretical foundation for the proposal of SynDR-IQA.

3. Multiple experiments across dataset settings validate the effectiveness of the method. Furthermore, as a data-driven approach, SynDR-IQA can be used in conjunction with existing model-based approaches without increasing inference costs.

### Weaknesses
1. The proposed method may be more complex in practice, requiring additional steps to adjust the data distribution, which would increase the difficulty of implementation. In other words, although SynDR-IQA does not increase the inference cost, it requires more computational resources in the training phase, especially for large-scale datasets.

2. Although this paper proposes a BIQA method based on data distribution adjustment, more explanations and analyses need to be provided on why it improves generalization. 

3. Further tests to verify the robustness of SynDR-IQA when addressing different types and degrees of image distortion should be supplemented with experiments.

### Questions
Please refer to the weakness.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper analyzes the response of ResNet to images of varying quality, noting that the model emphasizes content in high-quality images while focusing more on degradation in lower-quality images. From these findings, the paper identifies diversity and redundancy in samples as two crucial factors affecting generalization ability. Correspondingly, it proposes an optimized strategy for constructing the training dataset, achieving promising results in cross-dataset evaluations.

### Strengths
1. Enhancing generalization is a critical issue in IQA, and this paper addresses it by proposing two effective strategies based on theoretical analysis, achieving improvement over baseline in quantitative metrics.
2. The Fig1 visualization is clear, and the paper provides ablation studies. The writing is also accessible and easy to understand.

### Weaknesses
1. In real-world IQA, the primary challenge in generalization is often the variety in degradation types, rather than content diversity alone. As illustrated in Figure 1, for heavily degraded images, the model tends to focus more on the degradation type. The proposed method adds more high-quality reference images but does not fundamentally address this issue.
2. Although Figure 1 reveals some aspects of ResNet's performance, many IQA methods utilize other models, such as CLIP. Thus, the conclusions drawn in Figure 1 may not be universally applicable. A more comprehensive analysis across various models would enhance the validity of the findings.
3. The use of a new dataset as a reference may lead to comparisons that are not entirely fair with other methods.
4. The paper does not compare its method against some of the most recent SOTA approaches in the field, such as CLIPIQA and Q-Align. While the proposed method shows some improvements, fundamental generalization is often best achieved by exposing the model to more diverse training data, covering different degradation types, content variations, etc. Relying solely on simulated degradation effects has its limitations.
5. The paper evaluates methods such as SR and denoising using SRCC and PLCC metrics. However, common metrics in these fields include PSNR, SSIM, and LPIPS, which are not compared here. Considering there may be no available reference images, non-reference metrics like MANIQA, MUSIQ, and CLIPIQA are also widely used.
6. Only quantitative results are provided, with no visual examples. As IQA metrics often diverge significantly from human perception, presenting visualizations with corresponding scores would help illustrate the effectiveness of the proposed approach.

### Questions
1. Why do Algorithms 1 and 2 use the median as a threshold? Is there any theoretical or empirical basis for this choice?
2. Does the proposed method improve performance on images with different degradation types, such as low light, noise, defocus, or more complex degradations? Please provide relevant results and analyses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper propose a framework to enhance syn-to-real generalization ability of BIQA models. Based on theoretical analysis, a DDCup strategy along with a DRCDown strategy are proposed to reshape the distribution of synthetic distortions, leading to improved syn-to-real generalization of a BIQA model from a data perspective. Tthe effectiveness of SynDR-IQA is empirically validated across three cross-dataset settings (synthetic-to-authentic, syntheticto-algorithmic, and synthetic-to-synthetic).

### Strengths
+ This work presents an novel data augmentation scheme for syn-to-real BIQA that automatically identify the most sample-worthy images from a large candidate pool.
+ Theoretical analysis is provided as a foundation of the implemented strategies.
+ Cross-dataset evaluation are conducted with three settings, corresponding to different application scenarios.

### Weaknesses
- The motivation of syn-to-real generalization should be better elaborated, given that existing BIQA models can already handle both syntheic and authentic distortions well with a single set of model parameters, e.g., UNIQUE, Q-align, LIQE, etc.
- In addition to ResNet-50, it's better to experiment with more advanced backbone (e.g., ViT, Swin Transformer, etc.) networks to verify the generalizability of the proposed data scheme.
- Why training the feature extractor used in DDCup for only three epochs?
- During training, one patch of resolution 224×224 from each image is sampled. How about inference ?

### Questions
1 Some results are inconsistent with prior work, e.g., the cross-dataset results of DBCNN on LIVEC and BID are significantly lower than that reported in [1]. The authors should double check the experiments.

[1] Uncertainty-aware blind image quality assessment in the laboratory and wild.

2 The proposed method seems also be useful in continual learning settings (e.g., Continual learning for BIQA, LIQA, Remember-and-Reuse, TSN-IQA, etc.). Some discussions are expected.

### Soundness
3

### Presentation
3

### Contribution
3
