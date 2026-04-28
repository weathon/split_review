# HALO: Human-Aligned End-to-end Image Retargeting with Layered Transformations

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
Image retargeting aims to change the aspect-ratio of an image while maintaining its content and structure with less visual artifacts. 
Existing methods still generate many artifacts or lose a lot of original content or structure.  To address this, we introduce HALO, an end-to-end trainable solution for image retargeting. 
The core idea of HALO is to warp the input image to target resolution. 
Since humans are more sensitive to distortions in salient areas than non-salient areas of an image, HALO decomposes the input image into salient/non-salient layers and applies different wrapping fields to different layers. To further minimize the structure distortion in the output images, we propose perceptual structure similarity loss which measures the structure similarity between input and output images and aligns with human perception. Both quantitative results and a user study on the RetargetMe dataset show that our algorithm achieves SOTA. 
Especially, our method increases human preference by 13.21% compared with the second best method.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The work uses saliency to achieve image retargeting in a learnable setting. The results are shown to be SOTA through an user study.

### Strengths
Nil

### Weaknesses
- The work relies heavily on a saliency detector - MDSAM, which is a challenge. Having the main task of retargeting rely on a pre-trained saliency detection network is a downer. The work could have been better with solid contributions than just assembling pre-trained models for other tasks.

- RetargetMe dataset is a standard one. However, the images are very simple and have distinct objects. The proposed work will fail when there are complex scenes with nonsalient objects. 

- Using saliency for retargeting has been explored extensively since the work of seam carving. There is hardly any novelty or contribution in this work.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce  a novel image retargeting method that leverages a layer decomposition approach to distinguish between salient and non-salient regions of an image. By applying distinct warping fields to these separate layers, the method minimizes overall distortion during aspect ratio changes. Additionally, the authors present a novel structure-prone perceptual loss, based on DreamSim, which evaluates structural similarity between input and output images.

### Strengths
1) The authors address an interesting image rescaling problem and achieve visually impressive results compared to previous methods.

2) Their proposed multi-flow network for estimating transformations intuitively utilizes both the original undistorted image and a naively rescaled version to the target aspect ratio.

3) The proposed augmentation technique is logical and straightforward allowing to utilize DreamSim as loss function.

### Weaknesses
1) The overall contribution of the method appears somewhat limited, as the primary innovation lies in the augmentation technique that enables the use of the DreamSim loss. Meanwhile, the layer decomposition and inpainting modules are employed in a plug-and-play manner without addressing their sensitivity or taking further steps to reduce reliance on off-the-shelf methods.

2) The quantitative evaluation is somewhat limited; incorporating additional no-reference perceptual image metrics, both traditional and learning-based, would strengthen the paper's claims. 

3) The writing quality and overall presentation should be enhanced to better reflect the promise of the proposed method's results.

4) The related work section requires improvement, particularly in highlighting the shortcomings of prior approaches and demonstrating how the proposed method overcomes the challenges outlined in the introduction.

### Questions
1) Why does GPNN outperform on the perceptual metric MUSIQ despite the provided visuals clearly showing that the proposed method delivers superior results?

2) How sensitive is the proposed approach to suboptimal inpainting results?

3) Why are the visual and quantitative results nearly identical when using either augmentation or the LPIPS loss? Does the model trained with the LPIPS loss not incorporate the augmentation method?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents an end-to-end trainable approach for image retargeting. The authors introduce a novel layered transformation to learn two warping fields utilizing a pre-defined saliency map and inpainting model. Additionally, they develop a tailored perceptual structural similarity loss for model training. Quantitative results and user studies showcase the method's effectiveness.

### Strengths
1. This paper proposes a end-to-end learnable image retargeting framework and the results are impressive.
2. This paper is well-written, showcasing a clear and coherent structure that effectively guides the reader through its main arguments and findings.

### Weaknesses
1. The performance of the proposed approach is fundamentally dependent on the choice of the saliency model and the image inpainting model utilized. The selected saliency model plays a crucial role in accurately identifying and highlighting the most important regions of the image. Meanwhile, the image inpainting model contributes significantly to the quality of the restored content. Together, these models work in tandem to optimize the overall results, making their selection a critical factor in achieving superior performance.
2. Although the paper offers a well-structured and clear introduction to the methodological process, guiding readers through the steps and techniques employed, it falls short in addressing the underlying principles that inform these methods.

### Questions
1. What image resolutions can the proposed method accommodate, and what is the processing time like?
2. What is the key to the proposed method's performance being superior to that of the comparison methods?

### Soundness
3

### Presentation
3

### Contribution
2
