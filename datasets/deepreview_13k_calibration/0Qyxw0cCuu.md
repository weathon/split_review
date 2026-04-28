# CONTROL: A Contrastive Learning Framework for Open World Semi-Supervised Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
In recent years, open-world semi-supervised Learning has received tremendous attention. This is largely due to the fact that unlabeled real-world data often encompasses unseen classes -- those that are not represented in labeled datasets. Such classes can adversely affect the performance of traditional semi-supervised learning methods. The open-world semi-supervised learning algorithms are designed to enable models to distinguish between both seen and unseen classes.  However, existing algorithms still suffer from the problem of insufficient classification of unseen classes and may face the risk of representation collapse. In order to better address the aforementioned issues, we propose a contrastive learning framework called CONTROL that integrates three optimization objectives: nearest neighbor contrastive learning, supervised contrastive learning, and unsupervised contrastive learning. The significance of the framework is explained by theoretically proving the optimization of contrastive learning at the feature level benefits unseen classification, and the uniformity mechanism in contrastive learning further helps to prevent representation collapse. Serving as a unified and efficient framework, CONTROL is compatible with a broad range of existing open-world semi-supervised learning algorithms. Through empirical studies, we highlight the superiority of CONTROL over prevailing state-of-the-art open-world semi-supervised learning algorithms. Remarkably, our method achieves significant improvement in both unseen class classification and all class classification over previous methods on both CIFAR and ImageNet datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents CONTROL, a contrastive learning framework designed to improve the performance of open-world semi-supervised learning (SSL) algorithms. CONTROL addresses the presence of unseen classes by integrating three optimization objectives: nearest-neighbor contrastive learning, supervised contrastive learning, and unsupervised contrastive learning. Experimental evaluations on CIFAR and ImageNet show promising improvements over state-of-the-art methods.

### Strengths
+ The proposed three objectives are interesting and helpful.  
+ The proof and derivation of the objectives are comprehensive and easy to understand. 
+ Extensive evaluations and comparisons to baselines show promising results.

### Weaknesses
The writing of this paper is kind of informal, some examples include:
- The whole Section 3 missed a lot of details, lacking the basic problem setting, and key components of relied models, which makes the whole method hard to understand. Specifically, the paper does not clearly define the input data format for the contrastive learning framework. It is unclear how the labeled and unlabeled data are structured and fed into the model. Furthermore, the specific architectures of the encoder networks used for feature extraction are not described, making it difficult to reproduce the results. The loss functions are introduced without sufficient context, leaving the reader to guess how they are applied to the extracted features. For instance, the nearest-neighbor contrastive loss is mentioned, but the details of how the nearest neighbors are found and used in the loss calculation are missing. The same is true for the supervised and unsupervised contrastive losses, which lack details on the specific contrastive pairs and the temperature parameter used.
- Fig 1 and Fig 4 should be further polished. There are also overlaps between those two figures. The figures are not clear in illustrating the data flow and the different components of the proposed framework. The use of the same example in both figures adds to the confusion rather than clarifying the method. The figures lack detailed annotations and clear labels, making it hard to understand the relationship between the different loss functions and the data.

Next, It's hard for me to evaluate the contribution of the three loss functions, as all of them have been somehow explored in other areas before, and open-world semi-supervised learning is a new task. I have no sense if the contribution is huge or minor, so as the performance gain.

### Questions
- Page 2: what is a seen-unseen pair, Figure 2 is also hard to understand.

- It should be good to include some real-world results except the two datasets. 

- Will the additional objectives significantly increase the training time, regarding the speed for convergence?

- For Table 3, why the $L_{superseen}$ and $L_{SimAll}$ are bundled together? I didn't see the dependency. 

I rate a borderline for now and will take the rebuttal and opinions from other reviews into consideration.

---- 

After seeing the rebuttal and comments from the other reviewers, I tend to maintain my original rating.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to apply contrastive learning for an interesting task setting, open-world semi-supervised learning. Though there has been previous work that attempts to introduce contrastive learning for semi-supervised learning (i.e., OpenCon), the paper claims that previous work does not consider the open-world task setting, which leads to failure due to distribution shift and unseen classes. The paper proposes to adapt various loss terms used in other SSL tasks. In addition, the paper focuses on performing SSL on the feature-level representations, where the author provides theoretical analysis to argue the superiority of contrastive loss over conventional BCE loss. Experiments combine the proposed CONTROL technique with two existing baselines and show noticeable improvements in the accuracy of both seen and unseen classes.

### Strengths
- The paper investigates a somewhat interesting task setting, termed open-world SSL, which is of interest for the deployment of vision models in the wild.
- The presentation for the benefit of using the contrastive loss over conventional BCE loss is good with theoretical analysis, which provides a good motivation for introducing contrastive loss to open-world SSL, and can potentially facilitate future research.
- The paper provides good experimental results where the proposed method is combined with two previous baselines on CIFAR-10, CIFAR-100, and the ImageNet-100 datasets. The ablation study of CONTROL on CIFAR-100 also justifies the motivation for different introduced loss terms. The final analysis on the improved 'recall' rate of samples from unseen classes also provides good motivation for the proposed method

### Weaknesses
 - The main weakness of the paper lies in the narration of the paper, which makes it hard for a broader audience to capture the contributions of the paper. In many parts of the paper, the writing is focused on *what* is done but not *why* this is better than alternative methods. This makes the paper seem like a technical report rather than a research paper. A good paper is expected to provide insights to other researchers on 'why' the method works and how it can help with future research and real-world applications. This issue is particularly concerning in the introduction section, which is supposed to provide readers with high-level motivation of the methods. However, in the introduction, the third paragraph lists BCE-based methods and non-BCE methods without discussing when each of the methods is preferred and why each is motivated. Though the fourth paragraph attempts to argue for the superiority of BCE-based methods for open-world SSL, it again does not talk about high-level motivation for BCE-based methods. Instead, it directly dives into the details of similarity functions and talks about 'pulling closer sample pairs'. Such a discussion misses out a lot of context and causes confusion on what are the actual contribution of the paper. Also, the highlighted question in the introduction section seems to overlap greatly with the contribution with OpenCon. The only difference is that the authors claim CONTROl is 'unified' and 'open-world', but there is no further analysis on these two factors and how CONTROL differentiates itself from OpenCon.
- The paper seems to miss out on the addition of CONTROL to an important baseline OpenCon. OpenCon also proposes to apply contrastive learning for SSL. The paper argues that OpenCon is 'incapable of sustaining continuous optimization of representations during the process of semi-supervised learning'. However, from the final table 1 and table 2, the performance of OpenCon is pretty close to NACH+CONTROL, which somewhat undermines the claim of the novelty and contributions of CONTROL. A more convincing experiment would be to extend OpenCon with techniques proposed in this paper.

### Questions
I am slightly leaning toward the negative side mainly due to the concerns in narration and minor concerns in the experiment, as listed in the weaknesses above. However, I am open to discussions if the authors could kindly address the following questions

- **Narration.** Can the author elaborate more on high-level discussion on the motivation of the method and how it differentiates from previous work? This can be regarded as a revision of the introduction section but can be brief just for discussion now.
- **A small-scale additional experiment.** It would greatly enhance the claim of contributions in this paper if the author could provide a small-scale experiment on a dataset where CONTROl is combined with OpenCon.

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
This paper introduces a contrastive loss designed to enhance the performance of open world semi-supervised learning (OWSSL). Specifically, it proposes three distinct loss functions tailored for nearest neighbor contrastive learning, supervised contrastive learning, and unsupervised contrastive learning. The primary aim of these functions is to address and mitigate the representation collapse issue. The method presented has achieved state-of-the-art performance on benchmark datasets including CIFAR-10, CIFAR-100, and ImageNet-100.

### Strengths
1. The proposed approach is straightforward and easy to understand.
2. The method's efficacy has been demonstrated across various datasets.

### Weaknesses
 **1. Novelty Concerns**:
The proposed method essentially adds three types of contrastive losses to the existing OWSSL loss. Of these, the supervised contrastive loss is merely a standard contrastive loss. Additionally, both the NN contrastive loss and the SimAll contrastive loss that utilizes augmented images as positive keys lack distinctive features compared to existing research [A, B]. Specifically, the nearest neighbor contrastive loss is very similar to the approach in [A], which uses nearest neighbors in feature space as positives, and the SimAll loss appears to be a variation of the augmentation strategy used in [B], where multiple augmented views of the same image are used as positives. The incremental contribution of these losses over existing methods is not clearly justified.

**2. Overall Paper Completeness**:
The completeness of the paper is generally lacking. The proof provided in Section 4.1 for motivation is not rigorous, with some intermediate steps omitted, making it difficult to follow the argument. Furthermore, the paper introduces three hyperparameters associated with the proposed loss functions, but it fails to provide any details on how these parameters were selected. There is no discussion of parameter sensitivity, nor is there any experimental analysis to demonstrate the robustness of the method to changes in these hyperparameter values. This lack of detail makes it difficult to assess the reliability and practical applicability of the proposed approach.

**3. Reproducibility Concerns**:
The absence of a reproducibility statement, along with the lack of hyperparameter details, raises significant doubts about the possibility of replicating the claimed state-of-the-art performance. Without specific information on the experimental setup and parameter values, the results cannot be independently verified, which is a major concern.

### Questions
In Section 3.1, shouldn't $C_{\text{seen}}$ be defined as $C_L$ instead of $C_{\text{seen}} = C_L \cap C_U$?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper enhances previous open-world semi-supervised learning (OWSSL) methods such as ORCA and NACH by adding various contrastive learning losses, including supervised (SupCon), nearest neighbor (SupNN), and self-supervised (SelfCon) ones.

### Strengths
- Open-world semi-supervised learning is a practical problem.
- The proposed method improves previous approaches, such as ORCA and NACH.

### Weaknesses
 **Unclear presentation and unjustified claims**

Before delving into the other concerns, the presentation lacks clarity and is missing essential information.

- In Sec. 1 - paragraph 3, the paper categorizes OWSSL methods into "BCE-based" and "Other" methods. Why is the use of BCE loss a meaningful categorization? The paper does not clearly articulate why methods using BCE loss form a distinct and meaningful category, especially given that other loss functions could also be used to achieve similar objectives in OWSSL.
- In Sec. 1 - paragraph 4, the paper claims that using MSE instead of BCE lacks "flexibility." What is the definition of flexibility in this context, and why is BCE considered better than MSE for this purpose? The term "flexibility" is not defined, and the paper does not provide a clear explanation of why BCE offers a specific advantage over MSE in the context of OWSSL.
- In Sec. 1 - paragraph 5, the paper suddenly discusses "seen-unseen pairs." Why is this concept important, and how is it related to the problem? This relationship is not explained. The paper introduces the concept of seen-unseen pairs without adequately explaining their relevance to the OWSSL problem, leaving the reader to guess why this distinction is crucial.
- In Sec. 2 - paragraph 2, the paper claims that previous works do not consider optimization at the feature level. However, they also jointly optimize the feature and classifier. This statement is misleading, as many existing methods do optimize both features and classifiers, making the claim inaccurate.
- In Sec. 2 - paragraph 3, the paper claims that OpenCon is incapable of sustaining "continuous optimization" of representations. What is continuous optimization, and why can't OpenCon achieve this? The concept of "continuous optimization" is not defined, and the paper fails to explain why OpenCon is unable to achieve it, making the claim unsubstantiated.
- In Sec. 3.2, why should one consider BCE-based methods? BCE-based methods are just one specific approach by Cao et al. and some follow-ups. Eq. (1) does not represent all OWSSL methods. The paper implies that BCE-based methods are representative of all OWSSL approaches, which is incorrect, and the choice of Eq. (1) as a general representation is not justified.
- ...but not limited to.

Aside from the unclear overall logic, the sentences are significantly unpolished. Many grammatical errors make it difficult to grasp the meaning.
There are also typos and inconsistent use of terminologies. For example, "L" in the abstract, uncapitalized "all" in Table 1, unformatted "seen/unseen" in Sec. 3.1, and "OWSSL" is not defined in Sec. 3.2.


--- 
**Proposed method is merely a combination of existing techniques**

The motivation if the method is (1) enhance the separability of known class features and (2) prevent the collapse of unknown class features.
The paper employs SupCon (and a NN variant) for (1) and SelfCon for (2).

There are two issues here:
1. It is obvious that contrastive learning would enhance performance. In fact, this benefit for OWSSL has already been demonstrated in prior works, such as GCD [1] and OpenCon [2]. The paper fails to acknowledge that contrastive learning is a well-established technique in OWSSL, and the proposed method seems to be a straightforward application of existing ideas.
2. The addition of Sup/SelfCon generally enhances the models, not only for the OWSSL problem. To verify this, one can apply the proposed method to (1) the standard SSL setup and (2) other SSL methods. I believe it will also result in improvements in those cases, suggesting that the method does not exclusively target the OWSSL issue. The paper does not demonstrate that the proposed method is specifically tailored to OWSSL, and it is likely that the performance gains are due to the general benefits of contrastive learning rather than a novel solution to the OWSSL problem.

---
**Missing important baselines**

The paper omits a comparison with a highly related work, OpenCon [2]. The reasons provided in the paper for avoiding this comparison are not convincing. Additionally, GCD [1] is highly relevant to the paper but is missing from the comparison.
Furthermore, the paper does not include a comparison with papers published in 2023, such as RoPAWS [3], which also employs contrastive learning for SSL. Not only them, but there is also a long list of related works.
The OpenCon paper has 6 pages of references, in contrast to this paper with only 2 pages. Checking them would enable a more comprehensive context in the related work section, thereby making the paper more self-contained.

### Questions
1. Why is BCE better than other approaches, such as MSE?
2. Why is OpenCon not capable of continuous optimization?
3. Does the proposed method also improve non-OW SSL benchmarks and other OWSSL methods?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
