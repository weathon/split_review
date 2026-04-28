# SCoRF: Single-stage convolutional radiance fields for effective 3D scene representation

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5

## Abstract
Novel view synthesis captured from multiple images is a critical research topic in computer vision and computational photography due to their wide range of applications. Neural radiance fields significantly improve performance by optimizing continuous volumetric scene functions using a multi-layer perceptron. Although neural radiance fields and their modifications provide high-quality scenes, they have various limitations in representing color and density due to their hierarchical architecture comprising coarse and fine networks. They also require numerous parameters and considerable training time, and generally do not consider local and global relationships between samples on a ray. This paper proposes a unified single-stage paradigm that jointly learns relative position on three-dimensional rays and their relative color and density for complex scenes using a convolutional neural network to reduce noise and irrelevant features and preventing overfitting. Experimental results including ablation tests verify the proposed approach superior robustness to current state-of-the-art models for synthesizing novel views.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method to improve NeRF rendering quality by predicting new 3D point samples along camera rays. The main idea is to apply an 1D convolution over point positions and ray directions and predict a set of new 3D positions for volumetric rendering.

### Strengths
The idea of exploring local relationship among 3D point samples along a ray is interesting.

### Weaknesses
 **A. Technical-wise issues**
1. Contribution 1 claims “considerably reducing overfitting”, which does not have any evidence showing in the experiment section. The claim lacks quantitative support, such as a comparison of training and validation performance gaps between the proposed method and baseline NeRF models. It's unclear how the method inherently reduces overfitting without specific metrics or analysis.
2. Not sure I understand the 2nd last sentence “they suffer from limitations in applying to many photorealistic view synthesis areas” at the end of section 3.1? This statement is too vague. What specific limitations are being referred to? Which photorealistic view synthesis areas are particularly problematic for existing methods, and why?
3. Section 3.2 title is about “single stage convolutional NeRF” but the entire section does not explain how the “single stage convolutional” is conducted. The only sentence vaguely express this idea is “we devise a network generating S position-related values {t_i}…”, whereas the majority of this section is about how to handle/avoid {t_i} not being monotonic increase. There should be at least a math formulation to show how the convolution is done, I.e. input and output. The lack of a clear mathematical formulation makes it difficult to understand the core mechanism of the proposed method. The input to the convolution, the kernel size, and the output should be explicitly defined.
4. The draft spends almost a page (page 5) on getting {t_i} to be monotonic increase, while it could be resolved with some implementation tricks. For example, predicting {$\Delta$t_i} instead of predicting {t_i} directly. The extensive discussion on ensuring monotonic increase seems unnecessary given the existence of simpler solutions. This section could be significantly condensed by adopting a more straightforward approach.
5. Table 2a, why is the real dataset down-sampled to 504x378? The photo-realistic rendering performance would be more meaningful at higher resolutions. Evaluating performance at a lower resolution might not accurately reflect the method's capabilities in high-fidelity rendering scenarios. The choice of this specific resolution needs justification, especially when aiming for photorealistic results.
6. It seems like Table 3 tries to show that the proposed method provides better PSNR while having less network parameters comparing to previous methods. In this case, there are several baselines missing, for example TensoRF and K-planes. The comparison is incomplete without including state-of-the-art methods like TensoRF and K-planes, which are known for their efficiency and performance. This makes it difficult to assess the true contribution of the proposed method.
7. It seems like Table 4 tries to show the NVS performance under various number of point samples along a ray. First, this result would be more clear in a graph. Second, it needs to be compared with other baselines. How do other methods perform when the number of point samples drop? The analysis of performance with varying sample numbers would be more insightful if presented graphically. Furthermore, a comparison with how other methods perform under similar conditions is essential for a comprehensive evaluation.

--- 
**B. Presentation-wise issues**
1. Figure 1 and Figure 2 should have more caption text. Currently Fig. 1 has no legend and it’s unclear about what’s the idea the figure would like to convey (I kind of understand it after staring it for long time). Also the entire paper is about applying an 1D convolution, which should be highlighted in figure 2. The lack of clear captions makes it difficult to understand the figures' purpose and the key ideas they represent. Figure 2, in particular, should explicitly highlight the 1D convolution process.
2. Figure 5, the depth map of the proposed method looks so different from others. I suspect it’s a scaling or visualisation range issue?

### Questions
See weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a single-stage convolutional pipeline to replace the two-stage sampling strategies in the original nerf. The paper proposes a network with convolutions, which take the encoding positions and directions as input, and estimate the positional related values. These positional related values works like the distance between two sampled point in the standard volume rendering equations. The experiment shows competitive performance.

### Strengths
1.	This method proposes to replace the time/memory consuming hierarchical sampling strategy with a single-stage convolutional pipeline, which is a reasonable motivation.
2.	The experiment shows competitive performance in terms of image equality.

### Weaknesses
1. The paper claims the problems of the original nerf including:

a)	“require considerable training data and resources”

b)	“computational cost and time”

c)	“many rays do not contain valid and pivotal point”

d)	“MLP-base NeRF are particularly inefficient”

And this method is proposed to solve these problems by a single-stage convolutional framework.

However, from my view, none of these problems are solved according to the presentation of this paper. First, the number of the parameter of this method is almost the same with NeRF according to Table 3. Second, the speed of the method is not compared. Third, the input points of the method are sampled the same with coarse NeRF, so the input points of this method also “many rays do not contain valid and pivotal point”, right? Furthermore, the method does not address the fundamental inefficiency of sampling many points along a ray that do not contribute to the final rendering, a problem inherent in the original NeRF's sampling strategy. The convolutional approach, while potentially offering some local aggregation benefits, does not inherently solve this issue of wasted computation on empty space.

2.	More visual results are needed to show the performance of the method. Videos are critical to prove the effectiveness of the method in NVS area. The current static images are insufficient to demonstrate the view synthesis quality, especially for complex scenes with occlusions and varying depths. The lack of video results makes it difficult to assess the temporal consistency and stability of the synthesized views, which is crucial for NVS applications.

3.	This method lacks interpretability. The equation 5 violate the theory of volume render (change the distance between two samples to some value estimate by the network). How would you explain this equation, or how would this equation work? The core issue is that the network is directly predicting a value that is used as a proxy for the distance between samples, rather than adhering to the established principles of volume rendering where distances are calculated geometrically. This raises concerns about the physical plausibility of the learned representation and makes it difficult to understand what the network is actually learning about the scene's geometry and density.

### Questions
1.	I notice that the loss (6) is proposed to ensure ascendant values. But is it really ascendant during the test?
2.	How would you explain the generalization ability from training views to test views of this method? Since the network takes rays as input and the test rays are not available during the training stage, how would this network render reasonable test images?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper outlines an improved method for novel view synthesis and 3D scene reconstruction named Single Stage Convolutional Radiance Fields (SCoRF). SCoRF proposes to overcome existing limitations of Neural Radiance Fields (NeRF) by proposing a single-stage paradigm that jointly learns the relative position, colors, and densities of 3D rays using a Convolutional Neural Network (CNN). The authors also introduce an innovative adaptive position optimization loss function to enhance learning. Experimental results are presented, showing that SCoRF outperforms existing state-of-the-art methods in terms of photorealism and computational efficiency.

### Strengths
The paper is original in its proposal of SCoRF, combining convolutional blocks with fully connected layers in a single-stage architecture to optimize complex scenes. The inclusion of an adaptive position optimization loss further strengthens the unique approach. 
In terms of quality, the methodology appears well-developed and justified, with meticulous attention to detail in the experimental setup. 
The paper is also highly significant as it addresses key limitations in existing NeRF-based approaches, opening up the potential for various applications in computer vision and computational photography. 
The writing is clear, with relevant figures and tables to aid understanding, making the complex topic accessible to a wider audience in the field.

### Weaknesses
The visual results in Fig. 4 are worse than NeRF, especially in the highly reflective regions.
Conversely, although the paper indicates that the proposed SCoRF is computationally efficient, quantitative metrics such as training time or inference speed are not provided, weakening the argument.
The proposed method cannot be integrated with explicit voxel-based methods. Please correct me if  I am wrong.

### Questions
- Can the authors provide some metrics on the training and inference time of the proposed method?
- Could the authors comment on how to integrate the proposed convolutional sampling strategy with existing explicit representations such as voxel, hash, or 3D Gaussians?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
