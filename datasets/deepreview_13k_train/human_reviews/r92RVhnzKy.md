# Diving Deep into Regions: Exploiting Regional information Transformer for Single Image Deraining

- Decision: Reject
- Scores: 5, 6, 8, 8

## Abstract
Transformer-based Single Image Deraining (SID) methods have achieved remarkable success, primarily attributed to their robust capability in capturing long-range interactions. However, we've noticed that current methods handle rain-affected and unaffected regions concurrently, overlooking the disparities between these areas, resulting in confusion between rain streaks and background parts, and inabilities to obtain effective interactions, ultimately resulting in suboptimal deraining outcomes. To address the above issue, we introduce the Region Transformer (Regformer), a novel SID method that underlines the importance of independently processing rain-affected and unaffected regions while considering their combined impact for high-quality image reconstruction. The crux of our method is the innovative Region Transformer Block (RTB), which integrates a Region Masked Attention (RMA) mechanism and a Mixed Gate Forward Block (MGFB). Our RTB is used for attention selection of rain-affected and unaffected regions and local modeling of mixed scales. The RMA generates attention maps tailored to these two regions and their interactions, enabling our model to capture comprehensive features essential for rain removal. To better recover high-frequency textures and capture more local details, we develop the MGFB as a compensation module to complete local mixed scale modeling. Extensive experiments demonstrate that our model reaches state-of-the-art performance, significantly improving the image deraining quality. Our code and trained models will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a regional basded transformer network to tackle single image deraining problem. The proposed method includes a new architecture called Region Transformer Block, which utilizes the power of a masked attention structure and a mixed gated forward component. The region transformer is trying to learn features from the non-rain region to better recover the rain affected parts. Extensive experiments show that the proposed method outperforms the baseline methods in a consistent manner.

### Strengths
1. This paper is well written with strong motivation of solving the deraining problem by learning the unique features from the same image. 
2. The proposed method consistently outperforms others on benchmarking datasets.

### Weaknesses
1. In Eq. (6), the big \Pi is  indicating that the result of element-wise addition are multiplied together to form feature F. It is not stated clearly  that how the multiplication should be done. And why using multiplication? 
2. The last line on page 6, what does it mean by n and k_i are all parameters?

3. One of the most important question in this paper is regarding the novelty. The region-based attention mechanism has been applied by many previous works in various areas. The proposed method does not show the advanced benefits of using the masked attention on the deraining problem, especially the explicit mechanism / design to identify the true features of non-rain regions.

### Questions
One of the most important question in this paper is regarding the novelty. The region-based attention mechanism has been applied by many previous works in various areas. The proposed method does not show the advanced benefits of using the masked attention on the deraining problem, especially the explicit mechanism / design to identify the true features of non-rain regions. 

The authors are suggested to answer the question and the weaknesses during the rebuttal period.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper dives into single image deraining in the aspect of rain-affected regions and unaffected regions, and tries to remove rain streaks and preserve background parts. Based on this motivation, it proposes Region Transformer Block, which is composed of a Region Masked Attention mechanism and a Mixed Gate Forward Block. The former takes the information of rain-affected regions and unaffected regions into consideration and generates attention maps with region masks. The latter utilizes different kernel sizes to extract features on different receptive fields. It achieves SOTA results on multiple datasets.

### Strengths
1. More explicit decomposition of rain removal issues into rain streak removal in rain-affected regions and detail  preservation in unaffected regions
2. Better performance with fewer parameters and equivalent computation cost compared with Restormer and DRSformer.

### Weaknesses
1. The main concern is that this approach may be only effective on synthetic datasets. As shown in Table 1, RegFormer only brings 0.06dB PSNR gain on real-world dataset SPA-Data compared to DRSFormer. And when testing on a more realistic dataset (such as WeatherStream [1]), I'm worried that this approach may offer little improvement. The marginal PSNR gain on SPA-Data raises concerns about the model's ability to generalize to real-world scenarios with complex rain patterns and varying intensities. The performance on WeatherStream, which includes diverse weather conditions, is crucial for validating the robustness of the proposed method, and the current results are not compelling.
2. The generation of region mask need to be further clarified. The expression in Sec. 3.2.1 seems to conflict with Figure 3. The description of how the region mask is generated is unclear, specifically how the 3x3 convolution leads to the three types of masks. The relationship between the shallow features and the decoder's restored features in the mask computation needs more detailed explanation. The current description lacks sufficient detail to replicate the mask generation process.
3. Could you provide the ablation studies (similar to Table 3) on SPA-Data dataset?
4. It would be better if comparisons of inference time were given.

### Questions
Please see 'Weaknesses'.

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
This paper proposes a novel and effective transformer-based method for Single Image Deraining (SID). In this paper, one significant motivation is the consideration of processing rain-affected and unaffected regions independently and then combining their effects for the final reconstruction. Such a hierarchical strategy helps to vastly improve the deraining effects, especially in these challenging cases. The proposed framework is called Region Transformer (Regformer), consisting of Region Masked Attention (RMA) mechanism and a Mixed Gate Forward Block (MGFB). Extensive experiments are conducted on all current representative deraining datasets, and both RMA and MGFB are verified to be effective in dealing with deraining degradations.

### Strengths
1.	The proposed framework first points out the importance of explicitly and individually processing rain-affected and unaffected regions, leading to new SOTA performance on all current SID datasets, without the increase of model parameters/flops compared with existing methods.
2.	Compared with current baselines, the visual results of Regformer are much better, especially in these regions with details while covered with the raindrop in the original image. Its performance for different real-world cases has also proven to be great.
3.	The writing and organization of this paper is satisfactory.

### Weaknesses
1.	More perceptual metrics can be added for comparison in Table 1 with strong baselines, like LPIPS, which can reflect the quality of the restoration from different aspects.
2.	The ablation study in Table 3 can be conducted on more datasets to get a more comprehensive analysis.

### Questions
1.	What is the effect of $k_i$ in MGFB?
2.	What are the implement details of baselines? i.e., how their scores are obtained in Table 1? These should be described in detail.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a region-aware Transformer for single image deraining, which consists of a region masked attention and a mixed gate forward block. The authors observe that existing deraining methods ignore the differences between rain-affected and unaffected regions.

### Strengths
S1. The design of region masked attention is simple and effective, which can process rain-affected and unaffected regions of images separately.

S2. The experimental evaluation and discussion are adequate, and the results convincingly support the main claims.

S3. The paper is well-organized and clearly written.

### Weaknesses
W1. The author should delve into the importance of the rain-affected and unaffected regions of rainy images. I am curious if utilizing the features of the unaffected regions can better guide image restoration?

W2. How to determine whether high-quality region masks can be generated? If some visual examples of intermediate feature maps that illustrate this property are added, the proposed method can become compelling.

### Questions
See the above Weaknesses part.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
