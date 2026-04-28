# Controllable Blur Data Augmentation Using 3D-Aware Motion Estimation

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Existing realistic blur datasets provide insufficient variety in scenes and blur patterns to be trained, while expanding data diversity demands considerable time and effort due to complex dual-camera systems. To address the challenge, data augmentation can be an effective way to artificially increase data diversity. However, existing methods on this line are typically designed to estimate motions from a 2D perspective, e.g., estimating 2D non-uniform kernels disregarding 3D aspects of blur modeling, which leads to unrealistic motion patterns due to the fact that camera and object motions inherently arise in 3D space. In this paper, we propose a 3D-aware blur synthesizer capable of generating diverse and realistic blur images for blur data augmentation. Specifically, we estimate 3D camera positions within the motion blur interval, generate the corresponding scene images, and aggregate them to synthesize a realistic blur image. Since the 3D camera positions projected onto the 2D image plane inherently lie in 2D space, we can represent the 3D transformation as a combination of 2D transformation and projected 3D residual component. This allows for 3D transformation without requiring explicit depth measurements, as the 3D residual component is directly estimated via a neural network. Furthermore, our blur synthesizer allows for controllable blur data augmentation by modifying blur magnitude, direction, and scenes, resulting in diverse blur images. As a result, our method significantly improves deblurring performance, making it more practical for real-world scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript presents a 3D-aware blur synthesizer designed to generate diverse blur images for data augmentation, which further improves the deblurring performance of existing approaches.  The blur synthesizer enables controllable blur data augmentation not requiring any extra data during the training by combining 2D motion and 3D residual component.

### Strengths
The strengths of this paper could be summarized as follows:

1. Comprehensive experiments have been conducted to demonstrate the 
effectiveness of the proposed method.


2. The proposed blur image augmentation method could be beneficial to relative research.

### Weaknesses
There are some concerns and problems that should be further clarified and addressed:
1. The amplitude-phase integration directly offers controllability to motion patterns behind the blur images. However, it seems unable to explicitly adjust the overall blur intensity. Have the authors ever considered providing a way to control it? Such as adjusting exposure time or introducing a blur intensity parameter.


2. Please give more details about how to derive the projected 3D residual vector.


3. Authors have explored the effects of different values of M on the final deblurring performance. But what concerns me most is the correlation between the value of M and blur diversity, which could possibly provide more controllability to the blur synthesizer. For example, the visualizations or metrics showing how blur patterns change as M varies, or specific experiments to show blur diversity and its relationship to M.


4. As observed by the authors, inaccurate depth measurements can lead to performance degradation. On the other hand, Motion estimation itself is a very complex problem, even under 2D space. So, how can the authors guarantee that the inaccuracy of the estimated displacement field will not corrupt the final deblurring performance? Or authors can prove that deblurring effects are not sensitive to the accuracy of the motion field. For example, when training the blur synthesizer, we can randomly apply perturbations to the generated displacement fields to see whether it would make a difference.


5. In the experiments, the blur synthesis model is separately trained for different datasets. Nevertheless, this reduces the credit of the proposed model having better generalization ability compared with existing approaches. I would like to see more experiments involving a blur model trained on a single dataset and tested on different datasets.

6. Please provide more comparisons of real-world blurred images captured by the authors and clarify whether the compared models utilize existing blur augmentation methods.

### Questions
See the Weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a method for controllable blur image synthesis to address the challenges in capturing datasets for deblurring (GeoSyn). Specifically, it estimates M-many 3D vector fields for each pixel of a blur image and reconstructs the original blur image through projections of these estimated vector fields. During evaluation, blur with various trajectories can be generated by adjusting these 3D-aware vector fields. The method combines both parametric and non-parametric trajectory fields to capture both object motion and 3D camera motion. Training deblurring models with this augmentation leads to improved performance.

### Strengths
1. The paper effectively identifies key challenges in blur data augmentation and addresses them logically and directly by leveraging 3D spaces.

2. The writing and figures clearly illustrate the motivation and methodology of the proposed approach.

3. The ablation studies and experiments provide strong evidence of the proposed augmentation's effectiveness.

### Weaknesses
1. Limitation of motion trajectories: Since motion trajectories are determined independently of content, unrealistic trajectories can occur. For instance, part of a car might move left while another part moves right. Additionally, the method cannot represent motion caused by shape-changing objects. While real-world blur includes cases (e.g., folding fingers or blinking eyes), the proposed method only addresses part of this blur complexity.

2. The proposed method increases computational costs. The reviewer acknowledges that the augmentation scheme could help build an efficient deblurring mode, as mentioned in lines 507-513 of the main paper. However, could the authors provide quantitative metrics (latency, GMACs, and memory usage) when adopting GeoSyn?

### Questions
1. Could the authors provide the distribution of 2D-based motion trajectories (obtained via optical flow between the sharp and original blur images) and the distribution of the proposed 3D-aware vector fields? The reviewer would like to see if the augmented blur trajectories align well with real ones. This could be visualized using t-SNE projection of the motion vectors.

2. How do the authors obtain the camera intrinsics, as this could be ill-posed from a single image? Do the authors fix the intrinsic parameters and then optimize only the extrinsic scaling factor?

3. For the synthetic dataset, the reverted sharp image mean({\sum^{M}_{*=1}}\tilde{S}_{τ}_{*}) should be identical to the sharp image, based on Equation 10. Could the authors provide quantitative results on this?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents a novel, controllable blur data augmentation method aimed at enhancing the performance of learning-based deblurring models. The authors propose using a neural network to learn both a parametric vector field (2D rigid transformation) and a non-parametric vector field (3D residual field) to simulate 3D transformations. By adjusting these learned vector fields, the method can generate diverse and realistic blur patterns for data augmentation.

### Strengths
The motivation is well-founded: improving deblurring performance through data augmentation is highly cost-effective.  
The paper is clearly written and easy to follow.  
Based on the experimental results, the proposed method achieves state-of-the-art performance in deblurring tasks.

### Weaknesses
The upper performance limit for video deblurring is typically higher than for image deblurring, as videos provide more temporal information. It remains unclear whether the proposed data augmentation method can handle video sequences while maintaining temporal consistency, which is crucial for real-world applications like Apple Live Photos.

The paper repeatedly emphasizes the term "physical," which this reviewer finds somewhat exaggerated. From a single image, a neural network theoretically cannot disentangle object motion from camera motion due to the numerous possible motion combinations. At best, the method can adapt to the motion patterns of the dataset it is trained on. Additionally, even if the transformation accurately models 3D motion, the transformed image is still 2D and inherently lacks occluded information, making it less "physical" than synthesis methods using nearby video frames.

The paper does not sufficiently address blur caused by object motion (This reviewer did not see any blurred images dominated by object motion). This raises doubts about the method's "physical" nature and its effectiveness in real-world scenarios involving complex object motion.

> "ID-Blau requires ground-truth video frames to extract optical flows, so it cannot be trained on datasets containing only blurred and sharp images, such as RealBlur and RSBlur."

Given the advantage of synthesis methods using nearby frames, for a fair comparison, ID-Blau could utilize datasets like BSD[1] and RBI[2], which contain blur-sharp video pairs. Specifically, the BSD[1] dataset offers subsets with varying blur intensities. A cross-dataset evaluation between RealBlur and BSD is necessary to demonstrate the generalization capability of the proposed data augmentation method.

### Questions
Please address the concerns raised in the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2
