# HERO: Harnessing Temporal Modeling for Diffusion-Based Video Outpainting

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Video outpainting expands the spatial perspective of a video, enabling it to adapt to various display devices with different aspect ratios.
Current diffusion-based approaches for video outpainting often suffer from quality issues such as blurred details, local distortion, and temporal instability, significantly impacting the user experience.
The root cause is the insufficient temporal modeling in video
outpainting, which inadequately represents the relationships between frames over time.
To address this issue, a novel approach called HERO~(Harnessing the tEmpoRal modeling for diffusion-based Outpainting) is proposed to effectively tackles these generated video quality problems.
HERO employs two critical components to enhance temporal modeling: the Temporal Reference Module, which provides reference features that extend beyond spatial dimensions; and the Interpolation-based Motion Modelling Module, designed to stabilize generated frames.
By integrating these modules, these quality issues in video outpainting are effectively addressed.
Extensive experiments on multiple benchmarks demonstrate that HERO outperforms existing methods qualitatively and quantitatively.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents HERO (Harnessing the tEmpoRal modeling for diffusion-based Outpainting), a novel video outpainting method that addresses quality issues such as blurred details, local distortion, and temporal instability.HERO uses two key components: the temporal reference module ( TRM) and an interpolation-based motion modeling module (IMM).TRM provides reference features beyond the spatial dimension, while IMM stabilizes the generated frames. The authors have conducted extensive experiments on several benchmarks to demonstrate that HERO outperforms existing methods both qualitatively and quantitatively.

### Strengths
- Innovative Approach: HERO introduces a novel approach to video outpainting by focusing on temporal modeling, which is a significant advancement in the field.
- Temporal Reference Module (TRM): The TRM effectively provides reference features that enhance the spatial-temporal context, leading to improved outpainting quality.
- Interpolation-based Motion Modeling Module (IMM): The IMM stabilizes generated frames, reducing temporal instability and improving the overall quality of the outpainted video.
- Comprehensive Experiments: The paper includes extensive experiments on multiple benchmarks, providing strong empirical validation of the method's effectiveness.

### Weaknesses
 - Limited Dataset Diversity: The experiments are primarily conducted on the DAVIS and YouTube-VOS datasets, which may not fully capture the diversity of real-world video content. I am curious about the model’s performance on ultra-high-resolution videos or other datasets with large and complex motion patterns. I would like to see more comprehensive experiments. Adding qualitative comparisons on real-world videos would be a big plus—for example, using the proposed algorithm to directly outpaint videos captured on a mobile phone. Specifically, can HERO perform well for 1080p videos, or higher resolution videos (2K or 4K), which are part of our daily lives? What is the runtime and computational complexity like on these scenarios? Also how well does the HERO perform for real-life scenarios in sports? For example, basketball and soccer in sports, or even badminton and table tennis in small resolution.

- Insufficient Error Analysis: The paper lacks a detailed error analysis that could provide insights into the method's limitations and failure cases. For example, will HERO have temporal discontinuous results? What are the reasons for these failure cases?

- Computational Efficiency: The computational efficiency of the method, especially in comparison to existing methods, is not thoroughly analyzed. I suggest that the authors provide a comparison of computational complexity, including metrics such as parameter count, FLOPs, runtime, and energy consumption.

- Hyperparameter Sensitivity: The sensitivity of the model to hyperparameters is not extensively discussed, which could impact its practical usability. For instance, is the diffusion model sensitive to hyperparameter choices?

- User Studies: I suggest that the authors include user studies. I would suggest that the authors could conduct a user study by finding a group of people (e.g., the size of 20 people) and counting the scores that these people give to the results obtained by the different methods.

- Comparison to Other Methods: The comparison to other methods is limited to a few benchmarks, and a more comprehensive comparison could strengthen the paper.

### Questions
Could you elaborate further on the significance of video outpainting. In my view, this area seems quite narrow, with arguably less value compared to video inpainting (minor point).

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
5

### Summary
# Summary

The paper proposes a diffusion-based video outpainting framework. The proposed framework designs a temporal reference module to better model the spatiotemporal representations and designs a interpolation-based motion modelling module for better temporal consistency. The proposed framework outperforms the selected video outpainting baselines

### Strengths
# Strengths

- The proposed modules both seems reasonable and technically sound
- Extensive experiments demonstrate the effectiveness of the proposed framework

### Weaknesses
# Weaknesses

- In Sec 2.1, the statements about denoising UNet seem incorrect; also DDPM is not a deterministic sampling process
- Considering there are no ground truth results for video outpainting, the usage of pixel-based metrics like MSE/PSNR/SSIM does not necessarily reflect the actual performance
- Diffusion models can generate diverse results with the same input conditions and different random seeds. The paper does not mention how results are selected are comparison. It might be better to repeat the experiments across different seeds to report mean+std and also report the success rate for each generation
- The paper does not mention if prompts were used in the evaluations
- The selected evaluation metrics do not necessarily reflect the actual visual quality and temporal consistency of generated videos and human evaluations remain the most reliable measure. User study should be used for comparisons
- We can still observe local jitting artifacts/object distortions in the outpainted regions (in supplementary videos)
- The paper does not evaluate the video outpainting on complicated scenes like occlusions, object re-appearance, fast motions. 

# Other comments (not weaknesses)

- In Fig 3, the captions for "Binary Mask" and "Optical Flow" are incorrectly positioned
- The overview (Fig 3) lacks clarity, which might need a better visualization of the shared UNet

### Questions
Please refer to the weaknesses section

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper describes a method called HERO, which solves the problems of blurred details, local distortion, and temporal instability common in existing methods by introducing two key components: a temporal reference module and an interpolation-based motion modeling module. The former provides reference features beyond the spatial dimension, stabilising the generated frames through the relationship between neighboring frames.

### Strengths
HERO has shown qualitative and quantitative results in several benchmark tests that outperform existing methods.
The HERO design consists of two independent but complementary modules that can be flexibly applied to different video generation tasks.

### Weaknesses
The paper points out issues with existing diffusion model-based video episodic processing, like detail blurring, local distortions, and temporal instability. However, it doesn't dive deep into what’s causing these problems. It claims inadequate temporal modeling is the main issue but doesn’t explain why current methods can’t tackle these challenges effectively.
There’s a noticeable lack of innovation in the paper. The time-referenced module and the interpolation-based motion modeling module in HERO mainly combine existing models like VAE, 3D-RefNet, 3D-UNet, and other diffusion models that are already well-known in this field. The motion modeling module of the 3D-UNet is essentially an optical flow module, which has been used in various other tasks.
While HERO shows promising results in various benchmarks, the experimental section doesn’t properly validate important aspects like model parameters and speed. These factors are crucial for a full evaluation of how well the model performs.

### Questions
The author’s description of the model structure in section 2.2 doesn’t align with what’s shown in Figure 3. This is particularly evident in the Temporal Reference Perspective section, where it’s unclear why the results from Optical Flow Enc are handed off to the second half of 3D-UNet.
In Figure 3, it’s unclear why the Spatial Reference Perspective shows CLIP pointing to both the front and back parts of 3D-UNet. This could use some clarification.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a novel approach for high-quality video outpainting. The temporal reference module provides a new perspective besides the spatial perspective, alleviating the inadequate temporal modeling problem. The proposed interpolation-based motion modeling module utilizes adjacent frame relations, enabling more stable results. Qualitative and quantitative experiments show that the proposed approach outperforms previous methods.

### Strengths
1. In addition to the spatial perspective, this paper gives insight into diffusion-based video outpainting from a temporal perspective, proposing corresponding solutions to remove temporal limitations from prior studies.

2. This paper innovatively introduces optical flow to enrich temporal information and strengthen the relationship between adjacent frames. Besides, the proposed $IM^3$ improves the stability of results in a low learning cost.

### Weaknesses
1. The parameters and computation for the network introduced in this paper are notable. Although its impacts on GPU memory and inference time are discussed in Lines 508-510, quantitative evaluation of parameters and computations should be demonstrated and compared with related methods. Specifically, the paper should include a detailed breakdown of the parameter count for each module (e.g., the temporal reference module, the interpolation-based motion modeling module, and the base diffusion model), along with the FLOPs for both training and inference. This would allow for a more thorough comparison with existing methods and a better understanding of the computational overhead introduced by the proposed approach.

2. The ablation results in Table 4 and Table 5 are insufficient to support that $IM^3$ is necessary for both 3D-RefNet and 3D-UNet (Line 471-472). Ablation experiments for 3D-UNet w/o $IM^3$ should be conducted. The current ablation study only shows the performance of 3D-UNet and 3D-RefNet with and without $IM^3$ jointly, but it does not isolate the impact of $IM^3$ on each module individually. To properly evaluate the necessity of $IM^3$, the authors should conduct experiments where $IM^3$ is removed from 3D-UNet while keeping 3D-RefNet, and vice versa. This would provide a clearer picture of the contribution of $IM^3$ to each component.

3. Some minor errors: Check the spelling of “INTRODUTION” which leaves out the letter C (Line 047). The sentence on line 159 misses a period. There is an extra space on line 161. Check the citation format of the sentence on line 186. Missing a space in the sentence on line 782. The positions of Binary Mask and Optical Flow in Figure 3 are reversed.

### Questions
1. As stated in lines 155-156, the padded video is transformed into optical flow maps and then concatenated with binary masks, while on lines 209-211, it claimed that the dense optical flow of the input video is first estimated and the unknown regions will be filled with zero. It is confusing whether the input video is padded or not when calculating optical flow. Besides, if follow the statement on lines 155-156 that the input video is padded, the padding area will affect the generation of optical flow in known regions, making an influenced input.

2. Considering that the first and last frames only have one adjacent frame rather than two, does the lack of enhancement for these frames in the $IM^3$ module potentially result in poorer restoration quality for them?

### Soundness
2

### Presentation
2

### Contribution
3
