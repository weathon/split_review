# Composed Image Retrieval with Text Feedback via Multi-grained Uncertainty Regularization

- Decision: Accept
- Scores: 8, 3, 8

## Abstract
We investigate composed image retrieval with text feedback.
Users gradually look for the target of interest by moving from coarse to fine-grained feedback.  
However, existing methods merely focus on the latter, \ie, fine-grained search, by harnessing positive and negative pairs during training. This pair-based paradigm only considers the one-to-one distance between a pair of specific points, which is not aligned with the one-to-many coarse-grained retrieval process and compromises the recall rate. 
In an attempt to fill this gap, we introduce a unified learning approach to simultaneously modeling the coarse- and fine-grained retrieval by considering the multi-grained uncertainty. 
The key idea underpinning the proposed method is to integrate fine- and coarse-grained retrieval as matching data points with small and large fluctuations, respectively.
Specifically, our method contains two modules: uncertainty modeling and uncertainty regularization. 
(1) The uncertainty modeling simulates the multi-grained queries by introducing identically distributed fluctuations in the feature space. 
(2) Based on the uncertainty modeling, we further introduce uncertainty regularization to adapt the matching objective according to the fluctuation range.
Compared with existing methods, the proposed strategy explicitly prevents the model from pushing away potential candidates in the early stage, and thus improves the recall rate.  
On the three public datasets, \ie, FashionIQ, Fashion200k, and Shoes, the proposed method has achieved +4.03\%, +3.38\%, and +2.40\% Recall@50 accuracy over a strong baseline, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel approach to simultaneously model the coarse- and fine-grained retrieval by using multi-grained uncertainty, which contains uncertainty modeling and uncertainty regularization. The corresponding experiments validate the effectiveness of the proposed method on three public datasets.

### Strengths
1.The authors propose a new learning strategy in this paper, which is well-written and easy to follow.
2.This paper provides comprehensive experimental analysis and ablation discussion.

### Weaknesses
1.	The novelty is not well explained, please explain the difference from existing methods. The authors have to provide convincing proof to show why their proposed learning strategy is significantly different from the former methods. In Table 4(b), the author has provided a very simple discussion and experiment. However, it would be beneficial to include additional comparison methods and provide a more detailed discussion.
2.	In the method section of this paper, it is important to highlight the unique aspects of your proposed learning strategy. While the uncertainty modeling approach presented is easy to follow, it should be acknowledged that its simplicity may also be considered a limitation in terms of novelty.
3.	The comparison baseline of this paper is not sufficiently novel, consider exploring alternative methods that may be more unique. Recent three years of state-of-the-art methods should be included in the comparison experiment section to validate the effectiveness of the proposed method.
4.	As mentioned, the main contribution of this paper includes three points. The description of the first contribution is not clear enough.
5.	The tables in this paper are informative, but several of them require further standardization and uniformity.

### Questions
None

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper identifies a training/test misalignment between the fine-grained metric learning and the demand on coarse-grained inference in the real-world image retrieval with text feedback. This paper introduces a new unified method to learn both fine- and coarse-grained matching during training. In particular, we leverage the uncertainty-based matching, which consists of uncertainty modeling and uncertainty regularization.

### Strengths
1. The application is interesting, matching source image and text with target image.
2. The paper is overall well-written and easy to follow.2
3. The designed method is reasonable.
4. The experimental results look good.

### Weaknesses
1. The technical novelty and contribution are limited. It is trivial that adding noise to features can enhance the robustness. The other components in this method are trivial.
2. The qualitative results are insufficient. The authors should provide more qualitative results, and provide in-depth analyses on the cases where the proposed method outperforms or underperforms the baselines.

### Questions
1. Highlight the technical contributions.
2. Provide more qualitative results and analyses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors studied the image text composed retrieval in the field of fashion, aiming to prevent the model from prematurely excluding the correct candidate results in the early retrieval stage, and improve the recall of the retrieval task. To solve this problem, this paper proposed a composed retrieval model based on multi-granularity uncertainty regularization, which models coarse-grained and fine-grained retrieval simultaneously by considering multi-granularity uncertainty. The experiments showed that compared with existing methods, the proposed model can significantly improve the retrieval accuracy. This paper has strong practical significance and clear research motivation. However, there are also some problems in writing, which need to be strengthened.

### Strengths
a.	This paper found that in the process of image text combination query in the real world, the multi-round interaction process inevitably includes coarse-grained retrieval and fine-grained retrieval, and the traditional fine-grained metric learning method cannot meet the requirements of coarse-grained reasoning.
b.	In this paper, a new multi-granularity uncertainty regularization method is proposed. By uncertainty modeling and uncertainty regularization, fine-grained and coarse-grained matching can be learned during training. By controlling noise levels, the proposed method can be reduced to one-to-one metric learning, which is an extension of the traditional method.
c.	In this paper, a large number of experiments are carried out on three public data sets, and the experiments showed that the proposed method can improve the recall rate of existing methods.
d.	Since the proposed method is orthogonal to traditional methods, it can be combined with existing works to further improve their performance.

### Weaknesses
a.	Figure 1.a and section 3.1 did not clearly explain why there is uncertainty in triplet matching, and it is recommended to give examples of situations where the description is unclear or the source image is inaccurate.
b.	Since this paper mainly built the network using existing works [1][2], but did not describe their implementation, it is recommended to provide a more detailed explanation of the details of the network.
c.	There are some colloquial problems in the language of this paper, and some expressions need to be improved. It is suggested to polish the language.

Reference
[1]	Lee S, Kim D, Han B. Cosmo: Content-style modulation for image retrieval with text feedback[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021: 802-812.
[2]	Chen Y, Gong S, Bazzani L. Image search with text feedback by visiolinguistic attention learning[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020: 3001-3011.


Typos and minors
There are non-standard punctuation marks, such as P8, the third line of "Parameter sensitivity of the balance weight", etc. It is recommended to check the whole paper.

### Questions
please see the weaknesses.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
