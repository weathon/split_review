# HQGS: High-Quality Novel View Synthesis with Gaussian Splatting in Degraded Scenes

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
3D Gaussian Splatting (3DGS) has shown promising results for Novel View Synthesis. However, while it is quite effective when based on high-quality images, its performance declines as image quality degrades, due to lack of resolution, motion blur, noise, compression artifacts, or other factors common in real-world data collection. While some solutions have been proposed for specific types of degradation, general techniques are still missing. To address the problem, we propose a robust HQGS that significantly enhances the 3DGS under various degradation scenarios. We first analyze that 3DGS lacks sufficient attention in some detailed regions in low-quality scenes, leading to the absence of Gaussian primitives in those areas and resulting in loss of detail in the rendered images. To address this issue, we focus on leveraging edge structural information to provide additional guidance for 3DGS, enhancing its robustness. First, we introduce an edge-semantic fusion guidance module that combines rich texture information from high-frequency edge-aware maps with semantic information from images. The fused features serve as prior guidance to capture detailed distribution across different regions, bringing more attention to areas with a higher concentration of Gaussian primitives. Additionally, we present a structural cosine similarity loss to complement pixel-level constraints, further improving the quality of the rendered images. Extensive experiments demonstrate that our method offers better robustness and achieves the best results across various degraded scenes. The source code and trained models will be made available to the public.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel view synthesis method called HQGS, specifically optimized for low-quality images, such as those with low resolution, blur, and noise. HQGS employs an Edge-Semantic Fusion Guidance (ESFG) module to enhance the detail-capturing ability of 3D Gaussian splatting and introduces a Structural Cosine Similarity Loss (LSCS) to further improve global consistency in image rendering. Experimental results show that HQGS demonstrates stable performance across various degraded scenarios, outperforming other NeRF and 3DGS-based methods in metrics like PSNR, SSIM, and LPIPS.

### Strengths
1. This paper combines edge-awareness and semantic awareness through the ESFG module, providing essential high-frequency edge information to improve 3D Gaussian splatting (3DGS) reconstruction on low-quality images. The introduction of LSCS further enhances the global structural consistency of rendered images, which is an innovative design.
2. The experiments cover a wide range of common degradation conditions (e.g., low resolution, JPEG compression, blur, and noise) and compare the performance of HQGS against other state-of-the-art methods. The results demonstrate that HQGS not only outperforms these methods in image quality but also maintains efficiency in rendering time.

### Weaknesses
1. This approach heavily relies on high-frequency edge maps. For severely degraded images, using the Sobel operator to generate edge maps may result in significant detail loss. Given the instability of edge information in low-quality images, it is questionable whether ESFG can reliably extract edge information under various levels of degradation. There is a lack of robustness experiments on edge maps to verify the applicability of this approach. Specifically, the paper does not explore the impact of varying edge map quality on the final view synthesis results. The use of a simple Sobel operator might not be sufficient to capture meaningful edges in highly corrupted images, potentially leading to the ESFG module introducing artifacts or noise into the reconstruction process. A more detailed analysis of how the quality of the edge maps affects the performance of HQGS is needed, including a quantitative evaluation of edge map quality under different degradation levels and its correlation with view synthesis accuracy.

2. The paper mentions that low-quality images produce sparse point clouds, which can negatively impact reconstruction quality. However, the paper does not clarify whether ESFG influences the density or number of Gaussian elements. If the point cloud density is insufficient, simply adjusting the distribution might not achieve optimal results. It is unclear if the ESFG module directly addresses the sparsity of the point cloud or if it merely redistributes existing Gaussian primitives. The paper should provide a more detailed explanation of how the ESFG module interacts with the densification process in 3DGS, and whether it introduces any modifications to the standard densification strategy. Furthermore, it is important to analyze if the ESFG module can increase the number of Gaussian primitives in sparse regions, or if it only affects the distribution of existing primitives.

3. Although the paper mentions that the method combines high and low-frequency information, it does not present the actual distribution of Gaussian elements in high- and low-frequency regions of the images. A lack of intuitive visualization makes it difficult to verify the practical effectiveness of ESFG and LSCS in these regions. The paper should include visualizations that show the spatial distribution of Gaussian primitives, specifically highlighting the density of primitives in high-frequency (e.g., edges, textures) and low-frequency (e.g., smooth surfaces) regions. This visualization should be accompanied by a quantitative analysis of the number of Gaussian primitives in these regions, to demonstrate the effectiveness of the ESFG module in allocating primitives based on frequency content. Without this, it is hard to assess if the method truly captures and represents both high and low-frequency information effectively.

4. While Figure 7 demonstrates that HQGS exhibits greater robustness compared to 3DGS, it lacks a direct comparison of robustness with SRGS (e.g., in noisy or low-resolution scenarios). This omission limits the understanding of HQGS's robustness relative to other 3DGS optimization methods. A more comprehensive comparison should include a robustness analysis against SRGS across various degradation levels, including different levels of noise, blur, and downsampling. This would provide a clearer understanding of the relative strengths and weaknesses of HQGS compared to other state-of-the-art 3DGS-based methods.

5. The paper mentions only the total training iterations but does not provide specific data on training time. Given that the addition of the ESFG module may increase training costs, the paper should ideally compare training efficiency, particularly in terms of the impact of ESFG on training duration. The paper should provide a detailed comparison of training times across different methods, including a breakdown of the time spent on different components of the training process, such as the ESFG module. This would allow for a more thorough evaluation of the computational overhead introduced by the proposed method.

### Questions
1. I am curious about the rationality of generating edge maps from low-quality images. Since edge maps are generated from low-quality images, can they still effectively capture key edge information in severely degraded scenes? Can the author provide edge maps with different degrees of visual degradation and the impact of failed edge map visualization on the results? Furthermore, in severely degraded scenes, is it possible to use a pre-trained image restoration model to generate high-quality images before extracting edge maps?
The paper mentions that low-quality images result in sparse point clouds but does not clarify whether the ESFG module impacts the density distribution of Gaussian elements. Can the ESFG module improve the density of the point cloud while maintaining the total number of Gaussian elements? Is there a densification strategy or explanation of how the ESFG module affects 3DGS densification to better handle the sparse point clouds generated by low-quality images?

2. The authors mention that the method combines high-frequency and low-frequency features. Could you provide a visualization of the number of the Gaussian elements across high- and low-frequency regions within an image to show how the method effectively handles these different areas?

3. Figure 7 shows only the differences between HQGS and 3DGS. Could the authors supplement this with a robustness comparison to SRGS for a more comprehensive evaluation of HQGS’s performance?

4. Could the authors provide a comparison of training times across different methods, especially discussing the impact of the ESFG module on training time?

### Soundness
2

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
3

### Summary
The authors identify that 3DGS performs poorly with low-quality images due to insufficient attention to detailed regions, leading to a lack of Gaussian primitives and loss of detail.

To improve this, this paper presents an approach named HQGS, including Edge-Semantic Fusion Guidance Module and Structural Cosine Similarity Loss.

Edge-Semantic Fusion Guidance Module: Combines high-frequency edge-aware maps with semantic information to guide the distribution of Gaussian primitives, enhancing detail in rendered images.

Structural Cosine Similarity Loss: Complements pixel-level constraints by focusing on structural similarities, further improving image quality.

Experimental results demonstrate that HQGS enhances robustness and performance in various degraded scenes.

### Strengths
The proposed HQGS framework effectively addresses the challenges of degraded images in novel view synthesis by introducing an Edge-Semantic Fusion Guidance (ESFG) module and a Structural Cosine Similarity Loss (LSCS).

The ESFG module enhances the distribution of Gaussian primitives and improves detail generation, while LSCS ensures global low-frequency structure consistency, leading to higher quality rendered images.

Extensive experiments demonstrate superior robustness and performance in various degradation scenarios, outperforming state-of-the-art methods.

### Weaknesses
The method relies heavily on high-quality edge and semantic information, which may be challenging to obtain in extremely degraded or noisy images. The robustness of the edge detection process itself under severe degradation is not thoroughly explored, potentially limiting the applicability of the approach in real-world scenarios where input data quality can vary significantly. The paper does not provide a detailed analysis of how the quality of the edge maps impacts the final reconstruction quality, which is a critical aspect given the method's reliance on them.

The computational complexity introduced by the ESFG module and LSCS could increase training and inference times, potentially limiting real-time applications. While the paper mentions rendering times, a more detailed breakdown of the computational cost of each module (ESFG and LSCS) would be beneficial to understand the bottlenecks and potential for optimization. The paper should also discuss the memory footprint of the proposed method, which is crucial for practical deployment, especially in resource-constrained environments.

The presentation of the paper is not optimal in several aspects:
Figure 1 suffers from color blending issues, making it difficult to distinguish between different color regions corresponding to various methods.
Figure 2 is mentioned before Figure 1 in the text, which can be confusing for readers.
Tables 1 and 2 present similar results but use different formatting (one with colored text and one without), leading to inconsistency and potential confusion.
For Figure 5, the effectiveness of the method cannot be understood due to the lack of visualized input views.

### Questions
How were the experiments for Table 3 and Table 4 conducted? In which scenes were they performed? What types of degradation were used?

From the input in Figure 2a, it is impossible to see the presence of the "power lines". I am curious whether it is really possible to reconstruct the clear "power lines" in Figure 2b from such low-quality input views. How can this phenomenon be explained? Shouldn't 3D Gaussians be unable to imagine and reconstruct features that are not present (or almost completely blurred) in the input views?

I noticed that the model was trained for 50,000 iterations, which is more than the number used for vanilla 3D-GS. Would this have an impact? If the model is trained for 50,000 iterations, would all other parameters remain unchanged, including those for densification? If so, do the additional 30,000+ iterations seem redundant, or are they used to mainly for the optimization of the MLPs?

Are the weights of the MLP optimized individually for each scene, or are they generalized after pre-training?

Regarding lines 531-532, since you have added an MLP and trained for 50,000 iterations, the training time for HQGS would at least be longer, right?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work is concerned with the improvement of 3D Gaussian Splatting-based radiance fields computed for images that have quality issues. In particular, blur, reduced resolution, compression artifacts, and noise. The authors present a proposed method with two key modifications over the prior art. The first modification is an edge fusion guidance module that merges semantic information with edge information to favor the representation of fine details in the final radiance field overcoming issues with the above distortions. The second key modification is the introduction of a structural cosine similarity loss that acts on the low frequency areas of the rendered images to ensure better representation of low texture areas of the radiance field.

### Strengths
This paper is very well written. The authors supply sufficient detail on the proposed method to allow it to be correctly understood both on it's own and in the context of the prior art. The contribution is quite novel and although the edge fusion guidance module is motivated by the prior art, it is certainly not a trivial increment on the prior art and represents a new way of looking at the problem of low quality input images to radiance field training. The experimental section is quite strong, with comprehensive comparisons to the prior art and convincing improvements. The ablation studies are quite thorough, showing that the authors have put a lot of thought into the study and gone to considerable efforts to explore the work. The results of the ablation studies support the inclusion of each aspect of the two proposed modifications clearly. Conclusions are well-founded and justified by the experimental results.

### Weaknesses
Overall the work is strong, but there are a couple of areas of improvement. I found that certain figures contained unnecessary details or were difficult to read, while certain aspects of the explanations are unclear or seem contradictory. I also found that the analysis of compression artifacts was somewhat limited. In the "Questions" section of this review, I list these areas specifically and make suggestions for improvements.

### Questions
Q1: In the abstract of the work, the author's state: "The fused features serve as prior guidance to capture detailed distribution across different regions, bringing more attention to areas with a higher concentration of Gaussian primitives.". I find this sentence to be confusing. Later in the work it becomes clear that the ESFG module emphasizes edge related information in the input images in order to adapt the layout and properties of Gaussian's to better capture key information during training. In other words, the ESFG module guides the training of the Gaussian primitives by bringing more attention to key areas of the input images. It does not bring "more attention to areas with a higher concentration of Gaussian primitives." as this implies that the ESFG module is concerned with drawing attention to the density of Gaussians in the radiance field, which is not the case. It draws attention to key features of the input images and this in turn effects the density of the Gaussian primitives. I suspect this is what the authors meant, but the language is vague and admits the other interpretation. I suggest the following rewording of this sentence: "The fused features serve as prior guidance to capture detailed distribution across different regions, bringing more attention to areas with higher semantic meaning, such as edges, in turn allowing for higher concentration of Gaussian primitives to be assigned to such areas.".
Q2: On line 48, the authors state "Our preliminary experiments (Figure 2(b)) show that, for reconstruction, the distribution of reconstructed Gaussian primitives becomes too sparse to allow the capture of fine scene details. " Which distortions are the authors referring to here? Noise? Low resolution? Blur? Compression artifacts? All distortions? Please clarify what is being referred in this text? Please state clearly whether this observation refers to specific types of distortions (for example if it refers solely to blur) or whether this statement refers to all types of distortions.
Q3: Figure 4 has a spelling error, "Position paprameter in Gaussians" should be  "Position parameter in Gaussians". In addition, in the caption, the authors state "It separately learns semantic-aware feature and edge-aware feature, and
then jointly guides the training of HQGS." Please avoid the usage of vague terms like "It". What is "It" precisely? For example a potential better sentence is: "The ESFG module learns semantic-aware features and edge-aware features, and...".
Q4: Equation (2) introduces a notation for matrix multiplication that is not explained until after equation 4. Please explain notation at the point at which it is introduced.
Q5: Line 275, "then HQGS model it as G(x)" should be "then HQGS models it as G(x)".
Q6: Line 352, "methods that provide codes and" should be "methods that provide code and".
Q7: Figure 7 is a pastel, set of 3D overlapping bars with partial transparency that make the plot overly artistic and hard to read. A simple set of non-overlapping groups bars would have provided the same information and been clearer.
Q8: Figure 8 contains pastel colored, semi-transparent overlaid plots with some form of fill gradient transitions. The pastel colors are very similar and hard to differentiate in the plot. Please simplify and remove the unnecessary additional graphics. Key information like the numbers on the graphs are overlapping making them difficult to read.
Q9: In section 3.1, the authors state that the JPEG Compression will only be studied at a quality level of 10. Please explain why this particular value was chosen and why only a singular value was chosen for this parameter. In addition, only one value of Low Resolution was selected (4x downsampling). Why was this number chosen? Please provide additional text to describe the justification of the choice of JPEG quality level and downsampling factor. In addition please consider the testing of a wider range of these parameters (for example JPEG quality settings higher and lower than 10 as well as downsampling factors of 2x and 8x). If it is not appropriate to test a wider variety of values for JPEG Compression and downsampling, please state the rationale clearly.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors proposed a novel training strategy that can help to reconstruct 3D scenes from low-quality images.

### Strengths
The proposed method performs better than other compared SOTAs on 3D reconstruction form low-quality images. And the idea that learning a modulation for the position is good.

### Weaknesses
I think the description of the paper is not clear. Please see my following questions.

 1. How to apply the colmap on low quality images. I think it's not accurate.
2. What is M in line 265.
3. Why do you downsample the I and E by 2?
4. In Eqn. 3, authors used F'M, while in the above contents, authors used F'. What's the difference of them?
5. No other layers after the fusion features but before the sigmoid?
6. I guess the M represents the number of points, then how to get fusion features in dimension M?
7. In the original 3DGS, there is a loss called D-SSIM loss. Does it help to emphasizes directional consistency in the low-frequency feature space? Why do you change it with SCS loss?
8. The number of points is not fixed. 3DGS will split and clone points. How to you know how many M do you need?

### Questions
1. How to apply the colmap on low quality images. I think it's not accurate.
2. What is M in line 265.
3. Why do you downsample the I and E by 2?
4. In Eqn. 3, authors used F'M, while in the above contents, authors used F'. What's the difference of them?
5. No other layers after the fusion features but before the sigmoid?
6. I guess the M represents the number of points, then how to get fusion features in dimension M?
7. In the original 3DGS, there is a loss called D-SSIM loss. Does it help to emphasizes directional consistency in the low-frequency feature space? Why do you change it with SCS loss?
8. The number of points is not fixed. 3DGS will split and clone points. How to you know how many M do you need?

### Soundness
3

### Presentation
3

### Contribution
3
