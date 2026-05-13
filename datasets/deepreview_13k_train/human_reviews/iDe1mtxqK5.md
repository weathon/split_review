# Spatial-Mamba: Effective Visual State Space Models via Structure-Aware State Fusion

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
Selective state space models (SSMs), such as Mamba \citep{gu2023mamba}, highly excel at capturing long-range dependencies in 1D sequential data, while their applications to 2D vision tasks still face challenges. 
Current visual SSMs often convert images into 1D sequences and employ various scanning patterns to incorporate local spatial dependencies.
However, these methods are limited in effectively capturing the complex image spatial structures and the increased computational cost caused by the lengthened scanning paths.
To address these limitations, we propose \textbf{Spatial-Mamba}, a novel approach that establishes neighborhood connectivity directly in the state space. Instead of relying solely on sequential state transitions, we introduce a \textit{structure-aware state fusion} equation, which leverages dilated convolutions to capture image spatial structural dependencies, significantly enhancing the flow of visual contextual information.
Spatial-Mamba proceeds in three stages: initial state computation in a unidirectional scan, spatial context acquisition through structure-aware state fusion, and final state computation using the observation equation. Our theoretical analysis shows that Spatial-Mamba unifies the original Mamba and linear attention under the same matrix multiplication framework, providing a deeper understanding of our method.
Experimental results demonstrate that Spatial-Mamba, even with a single scan, attains or surpasses the state-of-the-art SSM-based models in image classification, detection and segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Spatial-Mamba introduces a "structure-aware state fusion" (SASF) mechanism using dilated convolutions in the Mamba architecture. This mechanism claims to add neighborhood connectivity directly in the state-space of SSM. The method is benchmarked on common image benchmarks, i.e. segmentation, classification, and detection using common datasets.

### Strengths
SSMs do have the problem of spatial sense. While the recent papers of ViM and VMamba try to solve them in their way, the solution feels rather underwhelming. The idea of introducing dilated convolutions as a means of capturing structural dependency in images is quite intriguing. I like the idea and the authors have done a good job of explaining most of the paper and related works. It is written clearly and concisely.

### Weaknesses
There are not many weaknesses in this paper. Apart from Figure 5 (and qualitative and erf figures in supp.), the paper could improve on convincing the reader with visuals if the resultant SSM with SASF mechanism extracts structural dependencies from the images.
Minor mistakes exist in the paper; specifically, on lines 199 and 200, equation 2 lacks a definition for alpha_k. It is only on line 212 that the alpha_k is mentioned as weights. Also, it is not clear from the text how exactly is this linear weighting being applied/calculated (on line 99, it mentions dilated convolutions to re-weight and merge states but it will be nice to add some clarity after equation 2 is introduced).

The results for Cascade Mask R-CNN seem to be missing...
Minor: On line 204, it is mentioned "considering both temporal and spatial information", but what exactly is the temporal information here? Or is it a typo?

### Questions
The results for Cascade Mask R-CNN seem to be missing...
Minor: On line 204, it is mentioned "considering both temporal and spatial information", but what exactly is the temporal information here? Or is it a typo?  

Overall, the paper is sound and presents a good idea for an existing problem. I am open to adjusting my evaluation should any significant concerns be raised by other reviewers that I may have overlooked.

### Soundness
3

### Presentation
4

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
This paper introduces Spatial-Mamba, a  state space models visual backbone designed for 2D visual tasks. It mainly introduce a multi-scale depthwise conv layer after the mamba operators to fuse the contextual information from different spatial locations. The author conducts theoretical analysis. Extensive experiements like image classification, dense prediction tasks are conducted.  The results show it outperforms the baselines and achieve competitive resutls.

### Strengths
1. The motivation is reasonbal and good. The vision mamba models suffers from processing  2D visual data due to the complexity of spatial structures. It heavily relys  on the 1D scanning strategy to transform 2D format into 1D sequence. The author apply conv-based layers to fuse the contextual information  in spatial domain, which is complemenary to the Mamba based operator. 

2. The experimetanl results are good. The accuracy in imageNet shows the improvement. The speed is still competitive as the conv operators are optimized, thus bringing less latency. 

3. The overall method is simple and easy to understand. Applying conv layers as a compelmentary module to improve the spatial modeling capability of the mamba is simple and direct.

### Weaknesses
1. The method seems to be a combination of Mamba and a classical module (depthwise conv).  It is also mentioned in No.3 point in Strengths. I would recommend author to validate/explore the spatial modeling enhancement methods more thoroughly. For example, applying the multi-scale conv layer to the original bi-directional Mamba (Vim) and cross-scan mamba (VMamba) to see the improvements. Though the one-direction scan and conv layer can aggregate enough spatial contextual information. 

2. The analysis of linear attention, mamba and the proposed method in section 4.3 is good. But the method proposed is rather straightforward. It seems the method does not improve the weakness of Mamba from the in-depth analysis. It first uses the Selective scan in Mamba to calculate the hidden states (one direction), following a depthwise conv to fuse the hidden states, then calculate the output y. It is not known the improvements over the method that adding more directions into the selective scan and computing the output. 

3. The modules/operators to fuse the contextual information can have multiple choices. The paper chooses depthwise conv. Conv operator may have inductive bias, which aggregate the spatial information by a fixed pattern. I would see more explorations, which could improve the paper.

### Questions
Please see weakness.

### Soundness
3

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
2

### Summary
This manuscript proposes to aggregate neighborhood features in state-space models for more efficient state-space modeling. The experiments are convincing, and the manuscript is well-organized.

### Strengths
+ The proposed fusing operation seems to have a decent performance gain onto the baseline.
+ The manuscript is well-organized.
+ The ablation studies are clear and convincing.

### Weaknesses
 +  Novelty. The proposed fusion seems to be a re-invention and re-introduce of convolution on the feature map of state-space modeling but is claimed as "Structure-Aware State Fusion". The LPU, overlapped stem,  re-parameterization  and MESA are all proposed in previous works. The technical contribution seems to be limited.
+ Clearness. The fusion seems to be applied after scanning. However, in Eq(2), the $x_t$ is the same in scanning and fusion. The notation here is not clear. It would be better to use $x_t^{\prime}$ in the fusion formula if my understanding is correct.

### Questions
Please refer to weakness part where I have expressed my concerns.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Spatial-Mamba, a novel state space model (SSM) designed for visual tasks, capable of effectively capturing spatial dependencies in images to enhance contextual modeling. Experimental results demonstrate that Spatial-Mamba outperforms existing SSMs and other mainstream models in areas such as image classification and semantic segmentation.

### Strengths
1. Improved upon existing SSMs by directly integrating spatial neighborhood dependencies into the state transition process.

2. Analyzed the connections between Spatial-Mamba, Mamba, and linear attention, unifying them under a matrix multiplication framework.

### Weaknesses
1. The paper does not mention the number of hidden states used in the SSM, and the ablation study lacks an analysis of the impact of different numbers of hidden states.

2. While the authors analyze the relationship between Spatial-Mamba, Mamba, and linear attention, they do not clarify the framework used to implement Spatial-Mamba, such as Mamba's hardware scanning algorithm or Mamba2's SSD framework.

3. In Mamba’s proposed SSM, hidden states do not inherently have spatial relationships. I suspect the authors intend to model the hidden states as 2D local observation points?

### Questions
1. Could you further explain how state variables are modeled in the state space to design the structure-aware state fusion?
2. Please provide details on the number of hidden states in each SSM layer and include relevant ablation experiments.
3. Is Spatial-Mamba implemented using the hardware scanning algorithm proposed by Mamba?

### Soundness
3

### Presentation
2

### Contribution
3
