# GT-Mean Loss: A Simple Yet Effective Solution for Brightness Mismatch in Low-Light Image Enhancement

- Decision: Reject
- Scores: 5, 5, 5, 5, 3

## Abstract
Low-light image enhancement (LLIE) aims to improve the visual quality of images captured under poor lighting conditions. In supervised LLIE tasks, there exists a significant yet often overlooked inconsistency between the overall brightness of an enhanced image and its ground truth counterpart, referred to as brightness mismatch in this study. Brightness mismatch negatively impact supervised LLIE models by misleading model training. However, this issue is largely neglected in current research. In this context, we propose the GT-mean loss, a simple yet effective loss function directly modeling the mean values of images from a probabilistic perspective. The GT-mean loss is flexible, as it extends existing supervised LLIE loss functions into the GT-mean form with minimal additional computational costs. Extensive experiments demonstrate that the incorporation of the GT-mean loss results in consistent performance improvements across various methods and datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces GT-Mean Loss, a novel loss function designed to address the issue of brightness mismatch in low-light image enhancement (LLIE). GT-Mean Loss aims to align the brightness of enhanced images with their ground truth counterparts by dynamically adjusting the loss during training, ensuring that the model focuses on factors beyond brightness mismatches.

### Strengths
1. Proposes a straightforward loss function that effectively mitigates brightness mismatches in LLIE.
2. Demonstrates performance improvements across various LLIE models, supporting the generalizability of GT-Mean Loss.
3. The approach adds minimal computational overhead, making it easy to integrate into existing models without significant resource costs.

### Weaknesses
The authors claim that "brightness mismatch dominates the PSNR values," suggesting that brightness inconsistency heavily biases this commonly used metric, leading to inaccurate quality evaluations. However, this assertion may oversimplify the limitations of PSNR, as the issue presented seems to be a specific type of counterexample rather than an overarching flaw in PSNR itself. PSNR is limited primarily in its sensitivity to perceptual qualities rather than simply brightness mismatch, and as such, is inherently less reliable for subjective quality evaluation. It’s possible to generate similar counterexamples through methods like the MAD competition, which reveal PSNR’s broader limitations in capturing perceptual quality accurately. Further, rather than focusing only on brightness mismatch, utilizing perceptually-oriented image quality assessment (IQA) metrics, such as LPIPS and DISTS, would provide a more holistic and accurate quality differentiation. These metrics are specifically designed to capture perceptual differences that metrics like PSNR or SSIM may overlook. By comparing GT-Mean Loss to metrics like LPIPS and DISTS, the authors could strengthen the argument for their loss function's contribution to enhancing perceptual quality in LLIE tasks, rather than solely addressing the limited case of brightness mismatch.

The method’s focus on brightness mismatch as the sole training issue may overlook other complex image degradation factors in low-light settings, such as the noise, the color bias, the unaccurate white balance,  limiting the applicability of the method for more holistic quality enhancement.

The performance improvements presented in the paper, while consistent, appear modest in scale. The GT-Mean Loss achieves incremental gains in metrics like PSNR and SSIM, but these enhancements are relatively small and may not justify the added complexity of implementing a new loss function focused on brightness alignment alone. For real-world applications, such minor improvements could be seen as insufficient.

In addition to quantitative metrics, conducting a user study on the enhanced images could provide a more reliable and insightful demonstration of GT-Mean Loss’s impact on perceptual quality. Objective metrics, especially pixel-based ones like PSNR and SSIM, do not fully capture human perception

The captions in the paper’s figures would benefit from additional context, allowing them to convey key insights independently of the main text. Currently, they lack sufficient detail to stand alone, which can make it challenging to grasp the full significance of the visual data without referring back to the text. 

The motivation section, particularly the second paragraph of the Introduction, would benefit from a clearer and more robust explanation. Currently, the rationale behind the proposed GT-Mean Loss is somewhat limited.

### Questions
1. Although the paper presents GT-Mean PSNR and GT-Mean SSIM as enhanced metrics, the evaluation lacks comparison using perceptual quality metrics such as LPIPS, DISTS, Q-Align, and LIQE, which could better reflect subjective image quality.

2. The method’s focus on brightness mismatch as the sole training issue may overlook other complex image degradation factors in low-light settings, such as the noise, the color bias, the unaccurate white balance,  limiting the applicability of the method for more holistic quality enhancement.

3. The performance improvements presented in the paper, while consistent, appear modest in scale. The GT-Mean Loss achieves incremental gains in metrics like PSNR and SSIM, but these enhancements are relatively small and may not justify the added complexity of implementing a new loss function focused on brightness alignment alone. For real-world applications, such minor improvements could be seen as insufficient.

4. In addition to quantitative metrics, conducting a user study on the enhanced images could provide a more reliable and insightful demonstration of GT-Mean Loss’s impact on perceptual quality. Objective metrics, especially pixel-based ones like PSNR and SSIM, do not fully capture human perception

5. The captions in the paper’s figures would benefit from additional context, allowing them to convey key insights independently of the main text. Currently, they lack sufficient detail to stand alone, which can make it challenging to grasp the full significance of the visual data without referring back to the text. 

6. The motivation section, particularly the second paragraph of the Introduction, would benefit from a clearer and more robust explanation. Currently, the rationale behind the proposed GT-Mean Loss is somewhat limited.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a GT-mean loss to address the brightness mismatch in low-light image enhancement. The authors first define the brightness mismatch and describe its impact on evaluation and training. Subsequently, the GT-mean loss and weight design are introduced. The evaluation is performed on several backbones with three low-light enhancement datasets. The GT-mean loss can consistently improve performance.

### Strengths
1.	The proposed loss leads to consistent performance for several backbones on three low-light image enhancement datasets.
2.	The paper is well-motivated and elaborately develops a loss function for the observation.

### Weaknesses
1.	In Fig.2, it seems more like a metric problem. If PSNR is not sensitive to this mismatch, why can the proposed loss function improve the PSNR performance? The core issue is that PSNR, as a pixel-wise metric, is inherently sensitive to absolute intensity differences, which is why a simple brightness scaling can drastically change its value. The paper needs to clarify how the proposed loss, which also operates on pixel intensities, avoids this sensitivity. Furthermore, the paper should provide a more detailed explanation of how the brightness mismatch problem is specifically illustrated in Fig. 2. The current explanation is not sufficient to demonstrate that the PSNR is failing due to brightness mismatch rather than other factors such as noise or artifacts.
2.	The paper couples the original loss and the introduced one using W. It is unclear how this weighting factor is determined and whether it is adaptive. The paper needs to provide a more detailed explanation of how the two loss functions relate to each other, beyond the fact that one is applied to the original output and the other to a scaled version. Specifically, what is the theoretical justification for combining these two losses in this manner? How does this combination ensure that the network learns to correct the brightness mismatch without sacrificing other aspects of image quality?
3.	Tab. 1 shows that perceptual loss can also identify the scaled image as better. The paper should explore the relationship between the proposed loss and perceptual loss more thoroughly. Specifically, can the perceptual loss achieve similar or better results when applied to algorithms that did not initially use this loss? If so, what are the advantages of the proposed loss over perceptual loss? The paper should also investigate whether combining the proposed loss with perceptual loss leads to further improvements, and if so, under what conditions.
4.	Some typos. Lv1->LOLv1. The citation for ZeroDCE is missing.

### Questions
Please see weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors propose to align overall brightness of the enhanced image with ground-truth images for supervision in low-light enhancement models. Experiments have shown that the proposed GT-mean loss results in consistent performance gain in PSNR.

### Strengths
1. The proposed method is well-motivated.  The MSE/L1-based metrics, say PSNR or RMSE, do have a problem identifing noise from lightness bias in RGB color space.
2. The experiment results are reasonable.

### Weaknesses
1. Novelty. The GT-mean metric was first proposed in KinD[1], and has been adopted by many previous methods[2,3]. I don't think the effectiveness of GT-mean **metric**, can be considered as a contribution.
2. Formulation of global lightness. The author models the global brightness with normal distribution, which breaks in most real-world scenarios.

### Questions
1.  Estimating W with the average of two KL divergences is confusing. Why? More in-depth analysis should be conducted.
2.  In Figure 3, the authors plotted average brightness. Is this average brightness distribution obtained from images? In my experiments, the brightness distribution of images (widely visualized as a histogram) doesn't always come with a perfect Gaussian distribution.
3. With the proposed gt mean loss, the models are still aligning input with reference images. However, as an **enhancement** task, there exists no ground truth image. It is not surprising that gt-mean alignment helps align the output with reference images, and thus improves the performance on reference-based metrics, say, PSNR and SSIM. Please report the non-reference metrics MUSIQ[1] and Q-align[2] for DICE, MEF, LIME, NPE, and VV datasets.

[1]Ke et. al,  MUSIQ: Multi-Scale Image Quality Transformer, ICCV 2021.

[2] Wu et. al, Q-Align: Teaching LMMs for Visual Scoring via Discrete Text-Defined Levels, ICML 2024.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Low-light image enhancement (LLIE) aims to improve the visual quality of images captured under poor lighting conditions. In supervised LLIE tasks, there exists a significant yet often overlooked inconsistency between the overall brightness of an enhanced image and its ground truth counterpart, referred to as brightness mismatch in this study. Brightness mismatch negatively impact supervised LLIE models by misleading model training. However, this issue is largely neglected in current research. In this context, we propose the GT-mean loss, a simple yet effective loss function directly modeling the mean values of images from a probabilistic perspective. The GT-mean loss is flexible, as it extends existing supervised LLIE loss functions into the GT-mean form with minimal additional computational costs. Extensive experiments demonstrate that the incorporation of the GT-mean loss results in consistent performance improvements across various methods and datasets.

### Strengths
The paper propose GT-mean loss, a simple yet effective loss function directly modeling the mean values of images from a probabilistic perspective.

### Weaknesses
 * The authors in this paper define a new term, “brightness mismatch” which refers to the “inconsistency” between enhanced image and the ground-truth image (lines  028-030). However, it is quite unclear as to how it impacts the model training as mentioned in lines 030-032. The authors are trying to imply that the outcome of the trained model affects the training of the model? It is somewhat difficult to follow. The same has several occurrences in the manuscript, but it is not quite clear how the brightness mismatch is affecting the model training. The authors are requested to provide clear and crisp information regarding the claims made. 
* Figure 2 and the explanation provided is somewhat misleading/not easy to understand. The “scaled” version of the GT image supposedly has “infinite” GT-mean PSNR Values; this seems quite untrue. This brings to next discrepancy/confusion in the paper, the GT-mean PSNR. The manuscript seems to not have a said definition for GT-mean PSNR. The authors are requested to provide more information and clarity on this. There is no information as to how the GT-mean PSNR is computed to recreate the Figure 2, and also how the result of infinity is achieved. Is it for some kind of demonstration purpose? 
* Lines 086-094 are not quite clear. Several Methods in literature make use of non-PSNR like metrics such as perceptual loss [1], color fidelity losses [2] which somewhat aim at solving the “brightness mismatch” issue as claimed by the authors. Towards this the authors are requested to provide adequate information for the claims made. 
* Lines 230-234 are extremely difficult to follow. For example., what is the meaning of “At this stage, the GT-mean loss value measures the fidelity between the two images by excluding brightness mismatch in advance considering brightness mismatch, thereby sustaining effective model training”? The writing style and the information provided at this point makes it quite difficult to comprehend the manuscript. 
* The overall contribution of this paper is supposedly GT-mean “loss” but the authors (in lines 122-125) describe it as “extension” to any existing loss function pushing the reader in the direction of if this is really a loss function or rather a regularization term. 
* The manuscript overall is rather difficult to follow and understand. 
* The qualitative results in section E show least/minimal differences between the baseline results and the proposed GT-mean version. There is no drastic change in the results shown and supposedly a non-issue due to the availability of losses like perceptual loss, color loss, cosine similarity loss for minimizing color deviations. The observed improvements seem to not fit for the level to claims made.

### Questions
Authors to consider major concerns mentioned.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a simple and effective GT-mean loss for low-light image enhancement. The GT-mean loss aims to align the average image pixel value intensities of the enhanced image to that of GT image. The authors provide an analysis from the point of view of probabilistic modeling. A design of the balancing weights between L1 loss and GT-enhance loss based on KL divergence is designed.

### Strengths
(a) The presentation of this paper is well-dressed. The writing is good and easy-to-follow. Although the proposed method is simple, but I found some insights in the weight design part. 

(b) The experimental results are good and solid. The authors have validated the effectiveness of the proposed GT-mean loss on seven methods on three datasets in both terms of normal enhanced results and GT-mean enhanced results. The Visual comparison also looks good. The ablation studies can demonstrate the effectiveness of the proposed techniques.

### Weaknesses
(a) The novelty is poor. The GT-mean enhancement is actually a cheat. It was first used by KinD [1]. However, KinD does not achieve very high results. Thus, this trick does not attract much attention. Later work LLflow [2] uses this trick to achieve a very high result on LOL-v1 dataset. Since then on, more and more methods used this trick to pursue better PSNR and SSIM. Although Retinexformer pointed out this is wrong and bad, it cannot stop the community from using this trick. From my point of view, using the average value of GT image pixels to achieve higher numeric results does not make sense. It is not essential. And this is just a small trick. I do not think this trick is worth an ICLR publication.

(b) The proposed GT-Mean Loss does not work in any case, especially for the out-of-distribution scenes. For example, in lines 1123 - 1129, 
the original LLformer performs better without the GT-Mean Loss. This is because the correction of GT-Mean has a bias on the trained dataset. This is the main technical drawback of the proposed method. The GT-mean loss, by design, forces the enhanced image to have a similar average pixel intensity as the ground truth. This constraint can lead to a loss of detail and texture in the enhanced image, especially when the ground truth image has a significantly different distribution of pixel intensities. This is a fundamental limitation of the approach, as it prioritizes global intensity matching over local content fidelity.

(c) Algorithm 1 is unnecessary since it is very simple. There is no need to draw the algorithm table.

(d) Code and pre-trained weights are not submitted, the reproducibility cannot be checked.

### Questions
The proof in Appendix A is just the normal definition and formulation of the KL divergence. Why write it? it seems unnecessary.

### Soundness
3

### Presentation
3

### Contribution
1
