# Scale-Invariant Continuous Implicit Neural Representations For Object Counting

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 6

## Abstract
Many object counting methods rely on density map estimation (DME) using convolutional neural networks (CNNs) on discrete grid image representations. However, these methods struggle with large variations in object size or input image resolution, typically due to different imaging conditions and perspective effects. Worse yet, discrete grid representations of density maps result in information loss with blurred or vanished details for low-resolution inputs.
To overcome these limitations, we design Scale-Invariant Implicit neural representations for counting (SI-INR) to map arbitrary-scale input signals into a continuous function space, where each function produces density values over continuous spatial coordinates. SI-INR achieves robust counting performances with respect to changing object sizes, extensive experiments on commonly used diverse datasets have validated the proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper use implicit functions for resolution-agnostic scene representation.They first exact deep-features of the input images and map them into a "scale-invariant" latent space and finally, decode them back to density map for counting. The method is tested for several REMOTE SENSING datasets where it achieves competitive results.

### Strengths
Counting objects of varying scales is challenging.
Using implicit neural representation for scale variations is reasonable.

### Weaknesses
The presentation could be significantly improved to enhance clarity. Currently, the methodology section is challenging to follow. For example, the paragraph from lines 137 to 142 is particularly dense:  "Here h denotes an element of the Scale-Translation group H and represents one scale-translation operator, p1(·) denotes the corresponding group actions of h acting on the image domain."  - what does it means by "Scale-Translation group H" or "scale-translation operator"? In the following paragraph, the authors bring up the "continuous function space" without any explanation and with many notations are not clearly defined including I_a or D^gt (unclear where does this continuous ground-truth coming from?).  Overall, the writing creates several logical gaps that make it difficult to fully grasp the method. To the best of my understanding, the method is basically: 1) extract deep-features using a scale-equivariant backbone B, 2) using an encoder to map output of B into a latent space and 3) decode this latent representation into a fixed scale for counting. Could the authors confirm whether this understanding is accurate?

The problem statement also seems somewhat misleading. The authors should clarify that the paper addresses scenarios where the input image scale is unknown, rather than scale variations within a single image. However, the method has only been tested on remote sensing datasets, where this specific problem may not be prominent; in many cases, images are often at a uniform scale, or metadata about the sensor is available. Thus, it is not immediately clear in which practical scenarios the proposed method would be applicable. 

The evaluation is also questionable. It is unclear to me why it is not tested on crowd-counting dataset and also few-shot counting datasets (FSC-147) where the scale-invariant issue is particularly relevant. If the method is designed only for remote sensing data then the title should reflect that. The method doesn't actually achieve state-of-the-art performance (in both RSOC and CARPK) since the SOTA method [1][2] are not included in the table. Can the authors provide explanation for this?

### Questions
Intuitively, can the authors comment on why using implicit function is able to extract robust scale-invariant representations? Using implicit function is time-consuming and the speed test should be included.

Why not test the method on crowd-counting and few-shot counting datasets?

Why are SOTA methods not included in the evaluation?

For remote sensing data, can we simply use object detection or some simple baseline to infer the object scale?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a scale-invariant method that maps discrete grid image signals into a continuous 2D function space. This approach allows the model to represent an image as a continuous function rather than fixed discrete pixels. The model learns through supervised learning to capture and represent scale-invariant features.

### Strengths
1. The proposed mehtod achieves better performance than several baseline on some simple datasets.

### Weaknesses
1. The comparison methods are very limited; many state-of-the-art methods are not included, such as those using optimal transport and point-to-point matching.
2. As shown in Figure 2, the objects are of similar size, making it difficult to justify that the method effectively addresses the multi-scale challenge.
3. The proposed method should be evaluated on a typical dataset with dense crowds, which are known to have multi-scale individuals.
4. The description of the scale-invariant model is unclear.

### Questions
1. Why can it be used to extract scale-invariant features? 
2. Since the multi-scale challenge has been investigated for a long time, how does the performance compare to other approaches?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel framework, Scale-Invariant Implicit Neural Representation (SI-INR), aimed at addressing significant challenges in object counting under varying scales and image resolutions. Traditional CNN-based counting methods often suffer from performance degradation when encountering objects at unseen scales or perspectives due to their reliance on discrete grid representations and non-scale-invariant models. The proposed SI-INR framework leverages a continuous function space, transforming discrete image signals into scale-invariant, continuous representations to improve accuracy and generalizability in object counting tasks.

### Strengths
1. The formulas are sufficient, demonstrating a solid mathematical foundation.  
2. The method is reasonable.  
3. The experiments are comprehensive, proving the effectiveness of the method through empirical validation.

### Weaknesses
1. After reading the paper, my understanding is that a VAE-like approach is used to obtain a fixed-size output, ensuring that inputs of different scales can be mapped to the same output, thus addressing the issues mentioned in the paper. However, the paper is written in a very complex manner and requires careful reading to understand. I suggest redrawing Figure 1. First, the new Figure 1 should allow readers to immediately grasp your network, especially the input and output. Additionally, it should include both the overall framework and detailed components of the network. The current Figure 1 does not provide a clear understanding of your work, making it difficult to reproduce.

2. Although your method is reasonable, it does not achieve the result mentioned in line 139 of the paper, i.e., obtaining the same output from inputs of different scales. In previous methods, multi-scale image augmentation was commonly used during training to address this problem. Although your approach is different, the goal remains the same.

3. In line 150, it is mentioned that GT is continuous. Why is GT continuous, whereas the output of previous methods is discrete? And why is your method’s output continuous?

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a framework, Scale-Invariant Implicit Neural Representations (SI-INR), for object counting across varying image scales and resolutions. SI-INR addresses limitations in current methods, particularly the challenge of scale invariance in object counting tasks involving dense object scenes. The approach combines a scale-equivariant backbone with implicit neural representations, achieving high accuracy across benchmarks like the RSOC and CARPK datasets.

### Strengths
- The framework’s focus on handling scale invariance through a continuous mapping function and modular structure is particularly valuable for applications involving heterogeneous datasets or remote sensing imagery with objects of varying sizes.

- Experiments across multiple datasets, such as RSOC and CARPK, showcase the generalizability of SI-INR. The paper also provides sufficient details on network configurations, making the work reproducible.

### Weaknesses
 - The paper does not fully explain the operational details of the "scale-invariant continuous mapping," especially regarding how SI-INR preserves fine details for low-resolution inputs. A more comprehensive description would enhance reproducibility.

- While computational demands are briefly mentioned, there is no clear comparison of SI-INR's runtime performance against baselines in various resolutions. This omission makes it difficult to assess scalability for real-time applications.

- The paper could benefit from additional experiments testing SI-INR’s robustness with images at extreme resolutions, especially low resolutions (e.g., <200 pixels), to provide a more complete understanding of its limitations.

- Missing some important previous work:

[1] Learning spatial awareness to improve crowd counting. (2019). ICCV 2019

[2] Rethinking spatial invariance of convolutional networks for object counting. (2022).CVPR 2022

### Questions
- Could you provide further clarification on the continuous mapping mechanism in SI-INR? Specifically, how does it handle low-resolution inputs without sacrificing accuracy?

- Would you consider evaluating SI-INR’s performance in sequential data or video-based counting tasks?

- Have you identified any potential biases in SI-INR when applied to diverse environmental conditions, such as different lighting or weather effects in remote sensing?

### Soundness
3

### Presentation
3

### Contribution
3
