# Edge-aware Image Smoothing with Relative Wavelet Domain Representation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Image smoothing is a fundamental technique in image processing, designed to eliminate perturbations and textures while preserving dominant structures. It plays a pivotal role in numerous high-level computer vision tasks. More recently, both traditional and deep learning-based smoothing methods have been developed. However, existing algorithms frequently encounter issues such as gradient reversals and halo artifacts. Furthermore, the smoothing strength of deep learning-based models, once trained, cannot be adjusted for adapting different complexity levels of textures.  These limitations stem from the inability of previous approaches to achieve an optimal balance between smoothing intensity and edge preservation. Consequently, image smoothing while maintaining edge integrity remains a significant challenge. To address these challenges, we propose a novel edge-aware smoothing model that leverages a relative wavelet domain representation. Specifically, by employing wavelet transformation, we introduce a new measure, termed Relative Wavelet Domain Representation (RWDR), which effectively distinguishes between textures and structures. Additionally, we present an innovative edge-aware scale map that is incorporated into the adaptive bilateral filter, facilitating mutual guidance in the smoothing process. This paper provides complete theoretical derivations for solving the proposed non-convex optimization model. Extensive experiments substantiate that our method has a competitive superiority with previous algorithms in edge-preserving and artifact removal. Visual and numerical comparisons further validate the effectiveness and efficiency of our approach in several applications of image smoothing.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The main contribution of this work is the introduction of RWDR that effectively distinguishes textures from primary structures and preserves weaker edges. Additionally, the paper proposes an innovative edge-aware scale map method that dynamically adjusts scale based on the image structure, resulting in clearer distinctions between structure and texture. Experimental results demonstrate that the proposed approach provides superior edge-preserving smoothing compared to existing methods.

### Strengths
1. This paper introduces relative wavelet domain representation into bilateral filtering, which is reasonable and novel.

2. The method achieves superior visual results compared to previous studies. 

3. The paper includes comprehensive theoretical derivations, technical descriptions, and runtime analysis of the algorithm.

### Weaknesses
1. The paper provides extensive visual results, but I’m curious how different algorithms are objectively evaluated based on visual quality. The authors should consider comparing performance on downstream tasks with objective metrics. A user study could also statistically confirm the advantages of the proposed method.

2. As a new method, it likely performs well in certain scenarios. However, I am more interested in its robustness and stability. In other words, can the authors provide a lower bound for the algorithm's performance? In which scenarios might it fail? Additionally, how sensitive is the algorithm to parameter changes?

### Questions
Could the authors provide an online demo to allow users to test the method easily? While it’s not essential for acceptance, it would add value for potential users.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The author introduces a mutually guided edge-aware smoothing model based on relative wavelet domain representation. Their proposed RWDR serves as a novel measure for effectively differentiating between textures and structures.

### Strengths
1. The solution of the proposed model is supported by a complete theoretical guarantee, which is a strong point.
2. Extensive experiments prove that the proposed method outperforms existing algorithms in mitigating gradient reversals,
 staircase artifacts, and halos and achieves a superior performance in balancing smoothing strength and edge preservation.

### Weaknesses
1. Though the authors support their claims by extensive qualitative results, but they should also provide the quantitative results to validate their points in the main paper or at least in the supplementary. For instance, the authors can include PSNR (Peak Signal-to-Noise Ratio), SSIM (Structural Similarity Index), or MSE (Mean Squared Error) on standard synthetic benchmark datasets and LPIPS, MUSIQ, NIQE, MANIQA for real-world tasks. This would allow for a more objective comparison with existing method.
2. The method section needs to be refined, as mentioned in Fig1 (that the detail enhancement image is boosted by four detail layers), this statement is not explained in the method section, how the four detail layers are being generated , is it from the wavelet decomposition?
3. The paper has lacks ablation study. The authors have given mathematical proofs of choosing the particular operations like RWDR and the edge-aware scale map, they should also try to prove the effectiveness of each proposed component  on the overall model.
4. The authors should also try to report the results on some real-world applications in Super-Resolution (RealSR, DrealSR,RealLR200), denoising (SIDD, DND) that would further prove the use of the proposed model, if the time permits and should also check on synthetic SR datasets like Manga109, Urban100, and BSD68 (for denoising).

### Questions
Please check the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this article, the author reviews image smoothing methods based on local information, global information, and deep learning, and discusses the limitations of current image smoothing techniques when dealing with image textures and image structural edges. To address this issue, first, the author proposes a novel edge-aware smoothing model that more effectively distinguishes between image textures and image structures through relative wavelet domain representation (RWDR). Second, the author reintroduces edge-aware scale maps into bilateral filters to improve image edges during the smoothing process. Finally, the author demonstrates the superiority of this method in texture preservation and artifact removal after image smoothing through comprehensive theoretical derivations and experimental results compared to other algorithms.

### Strengths
1.This paper proposes a relative wavelet domain representation and an edge-aware smoothing model, achieving certain progress in image smoothing technology; 2.The paper utilizes extensive theoretical proofs to establish a mathematical model for the relative wavelet domain. The experimental validation is well-supported by theory; 3.The writing of this paper is relatively fluent and conforms to the standards of English academic writing.

### Weaknesses
1.In the experimental part of this paper, there is a predominance of qualitative analysis of images. However, due to the significant subjective factors inherent in qualitative experiments, supplementing with more quantitative experiments would enhance the persuasiveness of the results; 2.Image smoothing operations, as one of the fundamental image processing tasks, play a crucial role in various visual tasks. However, the paper seems to lack exploration of specific visual tasks (for example, in super-resolution tasks, the textures and structures preserved after image smoothing are vital for image reconstruction).

### Questions
1.In the experimental part of this paper, there is a predominance of qualitative analysis of images. However, due to the significant subjective factors inherent in qualitative experiments, supplementing with more quantitative experiments would enhance the persuasiveness of the results; 2.Image smoothing operations, as one of the fundamental image processing tasks, play a crucial role in various visual tasks. However, the paper seems to lack exploration of specific visual tasks (for example, in super-resolution tasks, the textures and structures preserved after image smoothing are vital for image reconstruction).

### Soundness
3

### Presentation
3

### Contribution
2
