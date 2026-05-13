# EDM2+: Exploring Efficient Diffusion Model Architectures for Visual Generation

- Decision: Reject
- Scores: 3, 6, 6, 5

## Abstract
The training and sampling of diffusion models have been exhaustively elucidated in prior art. Instead, the underlying network architecture design remains on a shaky empirical footing. Furthermore, in accordance with the recent trend of scaling law, large-scale models make inroads into generative vision tasks. However, running such large diffusion models incurs a sizeable computational burden, rendering it desiderata to optimize calculations and efficiently allocate resources. To bridge these gaps, we navigate the design landscape of efficient U-Net based diffusion models, stemming from the prestigious EDM2. Our exploration route is organized along two key axes, layer placement and module interconnection. We systematically study fundamental design choices and uncover several intriguing insights for superior efficacy and efficiency. These findings culminate in our redesigned architecture, EDM2+, that reduces the computational complexity of the baseline EDM2 by $2\times$ without compromising the generation quality. Extensive experiments and comparative analyses highlight the effectiveness of our proposed network architecture, which achieves the state-of-the-art FID on the hallmark ImageNet benchmark. Code will be released upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents EDM2+, an exploration of efficient U-Net based diffusion model architectures that builds upon EDM2. While prior work has extensively studied training and sampling of diffusion models, the underlying network architecture design remains underexplored. The authors investigate the design landscape along two key axes - layer placement and module interconnection - leading to several critical insights for superior efficiency. Through systematic analysis and ablation studies, they develop EDM2+, which reduces the computational complexity of EDM2 by 2× without compromising generation quality.
The authors' main contributions include: (1) conducting comprehensive experiments to identify EDM2's architectural limitations, (2) conceptualizing performance-optimized solutions for both generation quality and efficiency, and (3) developing an architecture that excels other leading diffusion models and GANs on the ImageNet benchmark. When equipped with autoguidance, EDM2+ sets new record FID scores on ImageNet 64×64 using deterministic sampling, offering a new standard in the field of generative modeling.

### Strengths
- Clear demonstration of computational savings (2× reduction in FLOPs)
- Practical improvements in both CPU and GPU runtime performance
- Systematic exploration of depthwise separable convolutions in diffusion context
- Practical consideration of both training and inference efficiency

### Weaknesses
Critical gaps in theoretical understanding:
- No rigorous analysis of why channel mixing becomes more important under computational constraints
- Missing theoretical justification for embedding bottleneck design
- Limited connection to existing theory on efficient architecture design
- Insufficient analysis of how these modifications interact with diffusion dynamics

Incomplete Experimental Analysis:
- No parameter interpolation studies showing trends and sweet spots for architectural design.
- Absence of scaling law analysis across different model sizes
- Limited investigation of failure modes and edge cases
- Missing analysis of how modifications affect different stages of the diffusion process

Others:
- Most architectural choices seem derived from existing efficient CNN literature without sufficient adaptation to diffusion-specific challenges
- Minimal discussion of why certain modifications work better than others
- Few transferable insights compared to previous works like EDM2
- Limited exploration of trade-off spaces

### Questions
The paper presents results for EDM2+-S, L, and XL variants, but notably omits the medium-sized (M) model experiments that were present in the original EDM2 paper. Could you explain the reasoning behind this omission?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper explores the design landscape of efficient U-Net based diffusion models through comprehensive experiments based on EDM2. The findings can be summarized into two main points: first, decomposing the spatial/channel mixing operations and shifting the computation focus from spatial to channel dimension strikes a better balance; second, the key to both efficacy and efficiency is modulating the condition embedding into the denoising network’s bottleneck layers.

### Strengths
1. The efficient diffusion model architectures reduce the computing resources required for experiments, which is beneficial for further research in related fields.

2. The results on ImageNet are impressive, as they maintain generation quality while reducing computational complexity by about half.

3. The experiments are well-designed and conducted, incorporating the conventional wisdom of previous classic works.

### Weaknesses
1. How do different architectures affect the training time?
2. Curious about whether the proposed architectures could be generalized to accelerate the training of consistency models [1, 2]. ECT [2] is also based on EDM and EDM2, though this may still necessitate comprehensive implementation and is not a primary part of my decision assessment.

### Questions
See above.

### Soundness
3

### Presentation
3

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
This paper systematically studies the architecture design space of the EDM2 model. By substituting standard convolution with depthwise and pointwise convolution and decreasing the condition embedding dimension, the proposed EDM2+ model reduces the computational complexity by 2× (measured by the number of parameters and FLOPs) while maintaining the generation quality (measured by FID).

### Strengths
1. The writing of the paper is clear and easy to follow overall.
2. The paper conducts a comprehensive ablation study to evaluate the impact of various design choices on the network architecture. After systematical study and careful design, the final EDM2+ excels on the ImageNet benchmark.

### Weaknesses
1. While the reduction in FLOPs and CPU latency along with the increased GPU throughput is remarkable, the depthwise and pointwise convolution operations may not contribute significantly to GPU latency improvements. Including additional results on GPU latency, specifically with varying batch sizes, would enhance the comprehensiveness of the experimental findings. The current focus on throughput, while relevant, does not fully capture the latency characteristics that are crucial for real-time applications. Furthermore, a breakdown of the latency contributions from different parts of the network (e.g., convolution layers, embedding layers) would be beneficial.
2. The architecture design presented in this paper aligns closely with established efficient network designs, such as the MobileNet and EfficientNet series, which somewhat constrains its novelty. Although the paper explores the design space within the image generation domain, the core architectural components are not fundamentally new. The use of depthwise separable convolutions, while effective for reducing parameters and FLOPs, is a well-established technique. The paper could benefit from a more in-depth discussion of how the specific arrangement and interconnection of these components contribute to the performance gains, beyond simply adopting a known efficient design pattern.

### Questions
I do not have other questions.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In order to solve the problem that the existing diffusion model de-noising network frame parameters are too large, this paper explores the design of the efficient diffusion model EDM2 based on UNET, and explains the role of each component through the ablation experiment of several components. The EDM2++ architecture is redesigned to reduce the computational complexity of EDM2.

### Strengths
1. The paper is well-written and easy to understand.
2. A large number of ablation experiments are done to verify the role of each component of the EDM architecture.
3. The experiment of this paper is very sufficient, which fully demonstrates the high efficiency of EDM2+.

### Weaknesses
1.There is a lack of adequate theoretical understanding of these components only through ablation experiments. More in-depth theoretical analysis is needed to understand the role of denoising architectures in capturing probability distributions in diffusion models. For example, try to analyze from a geometric point of view. [1]  
2.Existing generation models have been extended to a wider range of fields, such as stream matching. The diffusion model can be seen as an example of this. This model framework does not seem to show superior results in other generative paradigms.  


### Questions
1. Does this denoising network model architecture perform well in other generative paradigms?
2. This denoising architecture is very fast. In contrast, many works studying scaling law in diffusion models require large consumption. So what are the limitations of your model compared to these models?

### Soundness
2

### Presentation
2

### Contribution
2
