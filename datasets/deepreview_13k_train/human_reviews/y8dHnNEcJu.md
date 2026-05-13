# SemPLeS: Semantic Prompt Learning for Weakly-Supervised Semantic Segmentation

- Decision: Reject
- Scores: 8, 5, 5, 3

## Abstract
Weakly-Supervised Semantic Segmentation (WSSS) aims to train segmentation models using image data with only image-level supervision. Since precise pixel-level annotations are \textit{not} accessible, existing methods typically focus on producing pseudo masks for training segmentation models by refining CAM-like heatmaps. However, the produced heatmaps may capture only the discriminative image regions of object categories or the associated co-occurring backgrounds. To address the issues, we propose a \textit{\namebf~(\textbf{\nameshort})} framework, which learns to effectively prompt the CLIP latent space to enhance the semantic alignment between the segmented regions and the target object categories.
More specifically, we propose \textit{\nameb}~and \textit{\namec}~to learn the prompts that adequately describe and suppress the co-occurring backgrounds associated with each target object category. In this way, \textit{\textbf{\nameshort}}~can perform better semantic alignment between object regions and the associated class labels, resulting in desired pseudo masks for training the segmentation model. The proposed \textit{\nameshort}~framework achieves SOTA performance on the standard WSSS benchmarks, PASCAL VOC and MS COCO, and
shows compatibility with other WSSS methods.
The source codes are provided in the supplementary.

\keywords{Weakly-Supervised Semantic Segmentation \and CLIP \and Prompt}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A new Weakly-Supervised Semantic Segmentation (WSSS)  method, called SemPLeS, is proposed in this paper. In SemPLeS, Contrastive Prompt Learning and Class-associated Semantic Refinement are used to learn the prompts that adequately describe and suppress the image backgrounds associated with each target object category. The authors tested SemPLeS, and it outperformed the existing SOTA on popular benchmarks like PASCAL VOC and MS COCO.

### Strengths
Using contrastive learning and CLIP text/visual encoders is an interesting idea. Especially optimizing learnable negative prompts and applying it to contrastive learning with positive image regions is very interesting. The novelty of the proposed method seems to be high.

By the experiments, the effectiveness of the proposed method was clearly shown. The proposed method seems to outperform the current SOTA method, WeakTr.

### Weaknesses
According to Paper-with-code, SOTAs for val and test are 78.4 and 79.0 by WaekTr, respectively. Why the results of the baselines shown in Table 2 are less than that ? The authors should present results of the proposed method under the same settings as Paper-with-code SOTA.
https://paperswithcode.com/sota/weakly-supervised-semantic-segmentation-on-1
https://paperswithcode.com/sota/weakly-supervised-semantic-segmentation-on

### Questions
I'm wondering if the proposed method is also effective for panatomic segmentation tasks such as Pascal Panatomic and CityScapes.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a Semantic Prompt Learning for WSSS (SemPLeS) framework. The author proposes contrastive prompt learning to acquire class-associated background prompts and further proposes a Class-associated Semantic Refinement module to suppress erroneous associations of co-occurring backgrounds. This method shows better performance.

### Strengths
1. The authors propose a novel CLIP prompt method that was automatically learned rather than manually designed, which effectively promotes the alignment of the semantic space.

2. The authors provide a detailed explanation of the modulation process, demonstrating the effectiveness of learnable prompts.

3. The logic of this paper is clear and easy to read.

### Weaknesses
1. In Sec. 2.1, the author briefly introduces the current research status of WSSS three-stage learning. However, this method is only a research branch of WSSS, and the end-to-end method should be supplemented. Furthermore, as far as we know, the recent WSSS research is basically based on CLIP. The author's innovation lies in the non-manual design of prompts rather than establishing vision-language associations, thus there is no need to emphasize the contribution of using CLIP.

2. In Figure 2 (a), symbol abbreviations X_k^f and X_k^b are given for the foreground and background of the image, and the text prompt t_k should also be indicated in this figure.

3. In Sec. 3.2.2, it writes “learnable prompts p_k as the input of the text encoder E_t”. It is necessary to illustrate how to initialize it and its shape. The motivation for learning prompts is not new, there exist many works that learn prompts in the CLIP community, such as COOP. More differences between these methods should be discussed.

4. Missed comparison with other methods, such as the work titled "MARS: Model-agnostic Biased Object Removal without Additional Supervision for Weakly-Supervised Semantic Segmentation " from ICCV 2023. To ensure a comprehensive research evaluation and establish a fair assessment of the proposed method's performance, the authors should include extensive analysis and comparison with more SOTAs.

5. Figures 3 and 4 can be augmented by incorporating a dedicated column on the left-hand side to present image labels, rather than embedding them within the figure itself. This graphical modification not only improves visual clarity but also aligns with the model's separate processing of images and labels.

6. What does "All BG Prompts" in picture 4 mean?

7. Result of L_match + L_prompt^b + L_prompt^f  should be added in Table 4.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper propose a prompt-learning method to enhance weakly-supervised semantic segmentation prediction.  Existing works often utilize pre-trained CLIP models to guide the class-specific foreground mask predictions, however, they often fail to separate co-occurring background categories from foreground (e.g. train vs. railroad, horse vs. grass).  Prior works address such issues by manually design background prompts for each category, hoping to refine the predicted pseudo mask.  Such methods require human efforts to manually annotate the background prompts.  This paper propose a stage-learning technique, by first training object mask predictors and then background prompts with image-text contrastive learning.  This paper demonstrates SOTA performance on standard benchmakrs, such as VOC and MSCOCO.

### Strengths
1. The idea of separating co-occurring background from foreground for each class makes a lot of sense.  In particular, the examples of the train and co-occurring railroad is convincing.

2. The results are SOTA on both benchmarks.

3. The paper is well written and easy to follow.

### Weaknesses
1. There are some citations missing:
    * ***intra-class foreground-background discrimination***: Learning Integral Objects With Intra-Class Discriminator for Weakly-Supervised Semantic Segmentation.  Fan et al. CVPR 2020.
    * ***pixel-wise contrastive learning for WSSS***: Universal Weakly Supervised Segmentation by Pixel-to-Segment Contrastive Learning. Ke et al. ICLR 2021.

2. The efficacy of class-specific background prompt is not clear.  In Table 4, training with $L_{prompt}^f$ seems to be more effective than $L_{prompt}^b$ and $L_{refine}$.

3. Segment Anything (SAM) is a strong framework for mask proposals.  Without fine-tuning on VOC / MSCOCO, I believe SAM can still provide high-quality segmentation on out-of-distribution imagery.  Reasonable baselines are: 1) classifying mask proposals with SAM using OVSeg[1]/CLIP/MaskCLIP+[2] features, and 2) instead of learning background prompts, one can learn to refine per-category mask proposals using dense segmentations derived from SAM.  We can vote the foreground confidence within each SAM segment (very like refine binary masks with CRF).  However, this paper does not provide any comparison to SAM (see questions for details).

### Questions
1. My first concern is the idea of using CLIP to guide mask predictions.  CLIP is notoriously know to perform poorly on segmentation.  May works have been proposed to address such issues (e.g. OVSeg[1] and MaskCLILP+[2]).  My question is why the authors choose to use CLIP but not MaskClip+ features?  In fact, probably we don't even need the proposes background prompt learning when using mask-sensitive CLIP features. The authors should provide analysis on OVSeg/MaskCLIP+ features.

2. I'm not sure how necessary it is to train the Mask Predictor. SAM is an existing strong segmentation framework.  Why not apply OVSeg[2] (with intra-class background prompt tuning) on mask proposals from SAM?  Or even refine the mask predictions with SAM.

3. In Table 4, what's the performance if you train with only $L_{match}$ and $L_{prompt}^f$?  It seems to me that training with $L_{prompt}^f$ brings the most performance gain, meaning the background prompts might not be as effective as the paper claims.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a novel method for weakly-supervised semantic segmentation (WSSS) by exploiting the large vision-language model, CLIP. By adopting a pre-trained WSSS model as a mask generator, they update the parameters of the generator using contrastive learning between the image-text triplet. After that, the learnable prompts are trained by contrastive prompt learning. Then, the mask generator is further updated using the proposed class-associated semantic refinement. By leveraging the CLIP-based image-text aligning, they improve the strong baseline, WeakTr, and achieve state-of-the-art performances on VOC 2012 and COCO 2014 benchmarks.

### Strengths
1. The paper is well-written, and the description of the proposed methods is clear with well-illustrated figures.

2. The proposed method (segment-label matching, contrastive prompt learning, class-associated semantic refinement) is intuitive and convincing.

3. The experiment is somewhat complete and the proposed methods are well-ablated.

### Weaknesses
## 1. complex training pipeline.

As I understand, this method is a refinement method for existing WSSS methods using knowledge of CLIP.
Namely, this paper adopts WeakTr as a strong baseline WSSS method and refines it using CLIP-based contrastive learning.
From a from-scratch training perspective, WeakTr requires a two-step training pipeline (CAM generation and online retraining) and SemPLeS requires a three-step training pipeline (segment-label matching, contrastive prompt learning, and class-associated semantic refinement).

I wonder if the mask generator could be replaced by attention maps of CLIP or activation maps from CLIP (as done in CLIP-ES).

## 2. dependency of the mask generator.
I have a concern that the performance of the proposed method may largely depend on the mask generator. If the mask generator fails to generate proper segmentation masks, the WSSS performance is largely dropped.
I guess the proposed (refinement) method can be adapted to other WSSS methods, but there is only one experiment using WeakTr.

## 3. more meaningful comparison.
The methods in Table 3 can be categorized into two groups, CLIP-based methods (CLIMS and CLIP-ES) and CLIP-free methods.
Considering that CLIMS achieved 68.7% and CLIP-ES achieved 71.4% in VOC 2012 testset, the baseline method, WeakTr, already shows a much higher performance of 74.0%.
Although SemPLeS achieved a 74.8% performance, I think this outstanding performance is mainly from WeakTr.
It would be great if there were any attempts to compare with CLIP-based methods more meaningfully (e.g., using the same seg model or the same baseline model).

Also, even though the SemPLeS used the large-scale vision-language model (CLIP) with the complex three-step refinement training, it is questionable that the 0.5% improvement in COCO 2014 validation set (Table 3) is promising.

### Questions
Overall, I think the proposed method is interesting and convincing.
However, I have some concerns related to the complex training pipeline and dependency of the mask generator model.

Therefore, my initial rating is weak reject (4), and I finalize the rating after rebuttals.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
