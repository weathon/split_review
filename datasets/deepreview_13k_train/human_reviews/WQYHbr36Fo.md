# Mind Your Augmentation: The Key to Decoupling Dense Self-Supervised Learning

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Dense Self-Supervised Learning (SSL) creates positive pairs by building positive paired regions or points, thereby aiming to preserve local features, for example of individual objects. However, existing approaches tend to couple objects by leaking information from the neighboring contextual regions when the pairs have a limited overlap. In this paper, we first quantitatively identify and confirm the existence of such a coupling phenomenon. We then address it by developing a remarkably simple yet highly effective solution comprising a novel augmentation method, Region Collaborative Cutout (RCC), and a corresponding decoupling branch. Importantly, our design is versatile and can be seamlessly integrated into existing SSL frameworks, whether based on Convolutional Neural Networks (CNNs) or Vision Transformers (ViTs). We conduct extensive experiments, incorporating our solution into two CNN-based and two ViT-based methods, with results confirming the effectiveness of our approach. Moreover, we provide empirical evidence that our method significantly contributes to the disentanglement of feature representations among objects, both in quantitative and qualitative terms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the problem of information leakage from the neighboring contextual regions in dense self-supervised learning. The contributions of this paper include the identification and confirmation of the coupling phenomenon when pairs have a limited overlap, the design of a decoupling branch, a novel region collaborative cutout augmentation, and the effectiveness of the proposed approach in the dense self-supervised learning frameworks. This approach can be applied to both CNNs and ViTs as the approach is only related to the augmentation.

### Strengths
This paper is well written and easy to follow.

The proposed method is simple and can be directly combined with existing dense self-supervised learning without introducing additional loss types.

The proposed method, RCC and decoupling branch, are demonstrated to be effective with several existing self-supervised learning methods in the experiments.

### Weaknesses
While the augmentation in Fig. 5 is easy to understand, the random masking in Fig. 2(a) is vague in terms of the illustration purpose.

The main text is expected to be self-contained. However, there are several cases where content is put in the appendix. For example, the figure 7(a) is useful to understand the definition of variables in equation 4, however, is put in the appendix. One possible way to address this problem is to merge Fig. 7(a) with part of Fig. 3. Again, the Alg 2 is another example for the understanding of the proposed RCC (region collaborative cutout).

The original contribution of the approach may be limited as the proposed RCC could be viewed as the combination of thresholding the cutout ratio within a region and filling the cutout region with background images. This is different from the Cutout, but more like combining existing strategies.

The order of Tables 4-6 does not match the appearance in the text.

Context within the region. The shape of each object varies and is irregular. And the region is defined by a bounding box (at least in object detection task), There would be context information in the bounding box. How to measure or address the coupling or leakage for this part of information?

This method would introduce another hyperparameter, the threshold of cutout ratio. How to set this across different datasets?

Ablation study. The numbers about COCO Det. in Table 6 do not match the numbers reported in Table 2 for iBOT. This is because the training epochs are different. If we view the results in Table 2 as the converged one, the comparison made in Table 6 may not lead to a convincing conclusion. While three experiments are presented in this section, a more interesting ablation study would be the effectiveness of the decoupling branch.

While the authors claim that the proposed method can be combined with existing SSL methods, there is a concern that the proposed method may not work well for the method with contrastive loss within each batch. The reason for this is that the decoupling branch serves a similar purpose. However, there may be additional contribution as the losses are computed at different levels with different masks.

### Questions
Context within the region. The shape of each object varies and is irregular. And the region is defined by a bounding box (at least in object detection task), There would be context information in the bounding box. How to measure or address the coupling or leakage for this part of information?

This method would introduce another hyperparameter, the threshold of cutout ratio. How to set this across different datasets?

Ablation study. The numbers about COCO Det. in Table 6 do not match the numbers reported in Table 2 for iBOT. This is because the training epochs are different. If we view the results in Table 2 as the converged one, the comparison made in Table 6 may not lead to a convincing conclusion. While three experiments are presented in this section, a more interesting ablation study would be the effectiveness of the decoupling branch. 

While the authors claim that the proposed method can be combined with existing SSL methods, there is a concern that the proposed method may not work well for the method with contrastive loss within each batch. The reason for this is that the decoupling branch serves a similar purpose. However, there may be additional contribution as the losses are computed at different levels with different masks.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a new method called Region Collaborative Cutout for self-supervised learning to alleviate the object coupling issue. This simple and straightforward method achieves evident gains over previous methods.

### Strengths
1. The paper is clearly written, and it is easy to catch the main motivation and solution. And I think the proposed method is well motivated.

2. Multiple previous methods are used as baselines to build the proposed Region Collaborative Cutout upon, and non-trivial improvements are observed. Besides, the method is proved effective for both CNNs and ViTs.

3. The ablation studies are comprehensive and convincing.

### Weaknesses
I am not very familiar with the research line of SSL. So I have no further suggestions for this paper. Generally, I like this simple yet effective method. It further highlights that constructing appropriate positive pairs by delicately designed strong augmentations is important.

However, one of my slight concerns is about the whole area of SSL since DINOv2 was released. It is pre-trained on extremely large-scale and curated data with several practical SSL optimization targets. It is very strong in many applications, such as retrieval, segmentation, and detection. Even with a frozen DINOv2 backbone, we can achieve state-of-the-art performance in some challenging tasks. Therefore, could the authors discuss the position of this submission by taking the recent SSL trend into consideration?

### Questions
No further questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Submission 945 presents a visual self-supervision method suitable for dense (/local) tasks such as detection/segmentation, etc. It motivates itself by presenting demonstrations that show that attention maps (/point affinities) do not localize well to object-parts and this is due to the false positives generated by current self-supervision methods.

It presents a variant of CutMix for dense self-supervision that mixes tokens from the input image with tokens from an external image. The mixing strategy is developed such that a token from the input image is largely surrounded by tokens from the output image so that the input token is positionally “out of context”. It then presents a regularizer for any visual self-supervision loss such that features extracted from the “in context” and “out of context” tokens (taken from the input image) are similar.

### Strengths
- The presented work is reasonably thorough in its experiments and generality. In particular, I like that it presents a rationale for both ViTs and CNNs.
- While confusingly presented, the high-level idea of asking token-wise features to be invariant to some of their surrounding tokens is a simple idea and appears to lead to better attention maps and downstream performance.

### Weaknesses
 (in no particular order)

### Poor presentation
Unfortunately, the unclear writing and figures significantly dampened any enthusiasm for this paper and it took multiple repeated readings to get a high-level sense of what is proposed. As a few examples,
- Paragraph 3 of the Introduction only makes sense if you already know the entire method.
- Figures 1(a) and 2(a) are really hard to understand and are used to motivate the work. For example, what do the red dashed lines, the arrows, and the “ViTs-based measuring pipeline” indicate in 2(a)?
- I don’t understand the written presentation of the mask generation (Sec. 4.1.1, par. 1) at all and its associated algorithm in the appendix uses undefined notation that is hard to follow (if it is defined elsewhere, please also add it to the caption). As a result, figure 4 does not immediately follow either.

IMO the paper requires a significant revision for clarity.

### Engineered token mixing has been done previously:
The proposed method has two main contributions: a cutmix style augmentation at the token level and a self-supervised loss leveraging that augmentation. However, while presented as new here, mixing tokens from different images in a carefully engineered way has been done before in TokenMix (ECCV’22, https://arxiv.org/abs/2207.08409 ) in the context of supervised classification and some other papers that follow up on it. Please discuss these works and clarify any differences, so as to better contextualize the key novel contribution of the self-supervised loss function that takes advantage of token mixing here.

### Unclear motivation and relationship to current work:
In my reading, the main motivation of this work is achieving higher quality part-level attention maps by reducing the dependence between a token’s features and its surroundings. It is then unclear to me if this strategy can then capture long-range nonlocal dependence – could you please comment on this point and clarify if I misunderstood?

Moreover, in recent work, DinoV2 (https://arxiv.org/abs/2304.07193) demonstrated that high-quality part-level representations can be learned by simply scaling up model and dataset sizes without considering the “coupling” between objects and background. I am not asking for comparisons, but I would like the response to briefly clarify the motivation of the proposed strategy in this context.

### Questions
### Suggestions:
- Please clarify the differences between TokenMix and similar token mixing works and this paper.
- Please revise and improve the writing and presentation of the first four sections of this paper to make it more immediately accessible.
- Please briefly discuss the motivation for the decoupling regularizer in the context of existing methods such as DinoV2 achieving high-quality part-level attention maps without considering the “coupling” phenomenon.
- Figure 5 on page 7 is what finally made the method click for me – please move it to earlier in the paper.

### Minor questions:
- Experimental clarifications would be beneficial: Why is 800 epochs of pretraining on COCO specifically chosen for all methods? How were the hyperparameters tuned for the baselines? Also, most of the experiments do not mention splits.
- Apart from the proposed masking, there appears to be no other augmentations mentioned and there is no code. Were standard augmentations such as jitters, flips, blur, etc. (https://github.com/bytedance/ibot/blob/main/main_ibot.py#L574) also used? Did the augmentation strategy match the existing methods on which decoupling was applied?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
