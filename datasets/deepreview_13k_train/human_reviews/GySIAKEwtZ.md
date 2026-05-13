# Representation Learning for Long Tail Recognition via Feature Space Re-Construction

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Deep learning has achieved significant success on balanced datasets. However, real-world data often exhibit a long-tailed distribution. Empirical results show that long-tailed data skews representations where head classes dominate the feature space. Many methods have been proposed to empirically correct the skewed representations. However, a clear theoretical understanding of the underlying causes and extent of this skew remains lacking. In this work, we provide a comprehensive theoretical analysis to elucidate how long-tailed data affects representations, deriving the conditions under which the centers of the tail classes shrink together or even collapse into a single point. This results in overlapping feature distributions of tail classes, making features in the overlapping regions inseparable. Moreover, we demonstrate that merely empirically correcting the skewed representations of training data is insufficient to separate the overlapping features, due to distribution shifts between training and real data. To address these challenges, we propose a novel long-tailed representation learning method, FeatRecon. It reconstructs the feature space so that features of all classes are arranged into symmetrical and linearly separable regions. Thereby, it enhances model robustness to long-tailed data. We validate the effectiveness of our method through extensive experiments on the CIFAR-10-LT, CIFAR-100-LT, ImageNet-LT, and iNaturalist 2018 datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a theoretical analysis and solution for the performance degradation of deep learning models when faced with long-tailed data distributions, introducing a method called FeatRecon. The authors provide a systematic exploration of how long-tailed data skews feature representations and detail the resulting limitations on the model's generalization capabilities. Their findings indicate that feature centers of tail classes may shrink and overlap, leading to inseparable representations across different classes.

To address this issue, the authors propose an algorithm that generates synthetic features to balance the sample sizes of all classes, constraining these synthetic features within confidence supports estimated from head class statistics. Furthermore, their iterative approach aims to create a symmetric and linearly separable feature space, thereby enhancing the model's robustness to long-tailed data. Extensive experiments conducted on multiple long-tailed datasets, including CIFAR-10-LT, CIFAR-100-LT, ImageNet-LT, and iNaturalist 2018, demonstrate the effectiveness of the proposed method.

Overall, this work effectively bridges theoretical insights and practical applications, offering valuable contributions and innovative techniques for tackling long-tailed data challenges, thereby possessing significant research merit.

### Strengths
This paper has remarkable advantages. In terms of innovation, the theoretical contributions are prominent, including in-depth analysis of the impact of long-tailed data on feature representation and the construction of a theoretical framework for optimal representation configuration; at the same time, the methodological innovation is unique, and the FeatRecon method effectively solves related problems by reconstructing the feature space. The experimental design is elaborate, with extensive and comprehensive datasets, detailed and sufficient comparisons, and reasonable ablation studies. The result analysis shows significant performance advantages and in-depth and detailed discussions.

### Weaknesses
1. Theoretical Basis

Limitations of Theoretical Assumptions: The theoretical analysis mainly relies on a simple one - vs - all scenario assumption, which involves adjusting the sample size of one category while keeping the sample sizes of the others equal and fixed. This assumption may have certain limitations in practical applications and fails to fully cover the complex distribution of long - tailed data. Specifically, the analysis does not account for the inter-class relationships and feature space overlap that occur when multiple classes are imbalanced simultaneously, which is the more common scenario in real-world long-tailed datasets. The assumption of fixed head class sample sizes also simplifies the problem, potentially overlooking the impact of varying head class distributions on tail class feature representation.

The Inadequate Combination of Theory and Practice: Although a theoretical framework is proposed in the paper, in practical applications, the connection between some designs of the FeatRecon method and the theoretical analysis is not direct and close enough. For example, the theoretical analysis focuses on the shrinking and overlapping of feature centers, but the method's synthetic feature generation and confidence support estimation do not explicitly address how these operations directly counteract the identified theoretical issues. The method generates synthetic features within a confidence support, but it is unclear how the size and shape of this support are theoretically derived to specifically address the feature center shrinkage and overlap. A more explicit link between the theoretical analysis of feature distribution and the practical implementation of the method is needed.

2. Experimental Comparison

Incomplete Comparison with the Latest Methods: Although the paper has compared with numerous existing methods, in some cutting-edge research directions of long-tailed learning, there might be some of the latest methods not included in the comparison experiments, making it impossible to fully determine the absolute superiority of the proposed method in the entire research field. For instance, recent methods that focus on disentangled representation learning or meta-learning for long-tailed recognition are not included in the comparison, which could provide a more comprehensive evaluation of the proposed approach.

The Issue of Consistency in Experimental Settings: There are some differences in the experimental settings for different datasets, such as different backbone networks, varying numbers of training epochs, and diverse data augmentation methods. Although the author may aim to adapt to the characteristics of different datasets, this inconsistency could have a certain impact on the comparison and analysis of the results, and the rationality of different settings requires further explanation. For example, using different backbone networks makes it difficult to isolate the impact of the proposed method from the influence of the backbone architecture itself. Similarly, varying training epochs and augmentation techniques can introduce confounding factors that obscure the true performance gains of the proposed method.

3. Writing Standards

Complexity in Some Content Representation: In certain sections of theoretical derivations and method descriptions, the paper presents a relatively high level of complexity. It employs a substantial number of mathematical symbols and formulas, thereby augmenting the difficulty for readers to comprehend. For instance, during the proof of Theorem 2, some derivation steps could be elaborated more thoroughly to assist readers in better following the author's line of reasoning. The use of complex notation without sufficient explanation can hinder the accessibility of the paper, particularly for readers who are not experts in the specific mathematical techniques used.

### Questions
1. Theoretical Aspects

Expand the Theoretical Framework: Consider relaxing the one - vs - all assumption and researching more complex long - tailed data distribution situations to further enhance the theoretical framework and make it more versatile and practical.

Strengthen the Connection between Theory and Method: In the method description section, more explicitly expound on how to design and optimize the method according to theoretical analysis. For instance, in the processes of synthetic feature generation and confidence support estimation, clarify how to utilize theoretical results to guide the selection and adjustment of parameters, thus better integrating theory and method.

2. Experimental Aspects

Supplementary Comparative Experiments: Pay attention to the latest research advancements in the field of  long - tailed learning and add comparative experiments with more recent methods to evaluate the performance advantages and innovativeness of the FeatRecon method more comprehensively.
Unify Experimental Settings: Whenever possible, strive to unify the experimental settings across different datasets as much as possible, or provide a detailed explanation for the reasons behind different settings, in order to compare and analyze the experimental results more clearly.

3. Writing Aspects

Simplify the Expression: Simplify and elucidate the complex theoretical derivations and method descriptions. Employ more textual explanations to aid in understanding mathematical formulas and symbols, thus avoiding readers from getting lost while reading.

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
4

### Summary
This work proposes a method based on contrastive learning to address the long-tailed learning problem. By uniformly sampling the confidence supports of the corresponding classes, a consistent number of samples for each class is achieved for contrastive learning. Additionally, the method incorporates the LDAM loss to facilitate supervised learning with long-tail data.

### Strengths
1. The authors provide a comprehensive theoretical framework.
2. offers an intriguing method for sampling features with a balanced number of categories and provides a solid theoretical foundation.

### Weaknesses
1. Feature Visualization Lacks Clarity: The feature visualization presented in the manuscript is insufficient. For instance, Figure 4 appears to be a diagram created by the authors. I would like to see whether the actual training results align with expectations. Could the authors provide additional visualization results, such as t-SNE, to illustrate the training process more clearly?

2. Distribution Changes Despite Fixed Empirical Centers: In Figure 4, if the Empirical Centers remain unchanged, what accounts for the changes in distribution? In layman's terms, the class to which a sample belongs is ultimately determined by the "distance" of the sample from the class center.  Or maybe the expression regarding Real Distributions is somewhat unclear. I do not fully understand why the real distribution changes and how it should be aligned with confidence supports.  Specifically, what does this refer to? Is it the ground-truth distribution? If the results are as shown in Fig.4 (a), the training samples appear to be completely separated. If only the existing training data is used, the situation seems no different from Fig.4 (d), and the final classifier would not change. Could the authors provide further clarification on this matter?

3. There is a lack of related work, and some important and latest work is missing. 
For example, 

Decoupling methods:

[1] B. Zhou, et al., BBN: Bilateral-Branch Network with Cumulative Learning for Long-Tailed Visual Recognition, in CVPR 2020.

[2] Z. Zhong, et al. Improving Calibration for Long-Tailed Recognition, in CVPR 2021.

[3] M. Li., et al., Feature Fusion from Head to Tail for Long-Tailed Visual Recognition, in AAAI 2024.

Logit adjustment methods:

[4] J. Ren. et al., Balanced Meta-Softmax for Long-Tailed Visual Recognition, in CVPR 2020.

[5] M. Li., et al., Long-tailed visual recognition via gaussian clouded logit adjustment, in CVPR 2022.

Transfer learning (learving pre-trained transformer-based backbone): 

[6] J. Shi et al. Long-Tail Learning with Foundation Model: Heavy Fine-Tuning Hurts, in ICML 2024.

It is recommended that the author conduct a comprehensive analysis of related work. Or conduct a more detailed analysis of the long-tail learning method based on contrastive learning. However, important work should not be lacking.

4. Tiny issue:
A. K. Menon, et al., Long-tail learning via logit adjustment. ICLR 2021. The work is publushed in ICLR 2021, not 2020.

### Questions
See Weaknesses 1 and 2.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
* _Theoretical contributions_: The paper introduces a theoretical framework to study how imbalanced/long-tailed (LT) data distributions distort class representations in feature space. It mathematically demonstrates that feature centers of underrepresented classes (tail classes) collapse or shrink, leading to overlapping regions that make class separation challenging. 

* _Technical contributions_: The paper proposes a new method, FeatRecon, which reconstructs the feature space to enforce symmetry and linear separability among classes. FeatRecon achieves this by generating _synthetic features_ for underrepresented classes and iteratively adjusting class representations to counteract the collapse effect. It introduces a novel approach to estimate and regularize "confidence supports", ie regions in feature space for tail classes using head class statistics.

* _Experimental evaluation_: FeatRecon demonstrates state-of-the-art performance on the common LT benchmarks, with strong accuracy improvements in places, eg for the more challenging iNat dataset.

### Strengths
The paper offers an analysis on imbalanced data feature space geometry for the case of the SCL loss. It presents a novel and technically sound theoretical framework that motivates a novel method. The analysis in Sec 2 is complemented with clearly drawn figures/ilustrations. The paper is clearly written and has strong experimental validation supporting the new method.

### Weaknesses
W1: In the proposed method,  the regularize tail classes’ estimation of statistics using the statistics of neighboring head classes. The intuition behind that choice is not clear to me.

W2: There seems to be a typo in Table 5: loss in row 3 is relative to row 2, but gains in rows 4 and 5 are relative to row 1.

### Questions
Q1: In Sec 3.2 "optimal" representation is defined wrt to training loss. It is unclear to me how this correlates to performance for the case of LT, where at test time we care equally about accuracy over all classes, ie what is defined as  "distribution shift." in 4.1. It would be nice to discuss in the theoretical part how optimality at training in this case is not the same as optimality for recognition accuracy, where the average is over classes.

Q2: You now sample uniformly in the estimated confidence support region. Would it make sense to sample that support space better? e.g. methods like MoCHi [Hard negative Mixing, NeurIPS 2020] generate synthetic features for contrastive learning by interpolating neighbouring features in feature space. Interpolating tail class features using the neighbouring head class features would result in a similar generation (eg in Fig 4). Could be an interesting sampling to ablate.

Q3: How sensitive is regularisation to the hyper parameters like q (ie top-q head classes selected)?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper aims to address the long-tailed recognition problem.
The paper provides a sound theoretical analysis of contrastive learning from the perspective of neural collapse.
Based on the analysis, they draw the conclusion that increasing the size of samples for tail classes can alleviate the collapse issue.
Thus, the proposed method is to synthesize sample features for tail classes.
Moreover, a class-wise temperature schedule is used in their algorithm.

Experiments are conducted on popular long-tailed benchmarks, like ImageNet-LT, iNaturalist, and CIFAR-LT. Some improvements are observed when compared with baselines, like KCL, TSC, and BCL.

### Strengths
(1) Sound theoretical analysis on neural collapse for contrastive learning.     
(2) The paper is well-organized and easy to follow.

### Weaknesses
(1) Lack of comparisons with current state-of-the-art methods, like GPaCo, especially on large-scale data including ImageNet-LT and iNaturalist 2018.

[ref1] Generalized Parametric Contrastive Learning, TPAMI 2023.

(2) Synthesizing sample features for tail classes is not a novel idea. The paper should discuss the differences between the proposed method and previous relevant works, like ReMix and work[ref2].

[ref2] Feature Space Augmentation for Long-Tailed Data, ECCV 2020.

(3) The connection between the proposed method, like feature augmentation and temperature adjustment, and the neural collapse theory is not strong. Increasing the samples for tail classes can obviously alleviate the long-tailed recognition problem. 

(4) The claim that "Head classes benefit from a larger τ while tail classes benefit from a smaller one. We demonstrate
(in Appendix A.3.2) it holds for SC loss too." seems to contradict Eq. (11) that the tail classes will be assigned with a large temperature.

(5) Minor typo, "N_min - N_min" should be  "N_max - N_min" in Eq. (11).

### Questions
(1) Fair comparisons with current state-of-the-art methods, like GPaCo [ref1], on large-scale datasets including ImageNet-LT and iNautralist 2018.    

(2) Discussion on the differences between the proposed method and previous augmentation-based methods, like ReMix and work[ref2].
     What are the advantages of the proposed method over them?

(3) Clarification on the temperature adjustment.

### Soundness
3

### Presentation
3

### Contribution
2
