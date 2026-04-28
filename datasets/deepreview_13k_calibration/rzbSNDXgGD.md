# Minimal Impact ControlNet: Advancing Multi-ControlNet Integration

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
With the advancement of diffusion models, there is a growing demand for high-quality, controllable image generation, particularly through methods that utilize one or multiple control signals based on ControlNet. However, in current ControlNet training, each control is designed to influence all areas of an image, which can lead to conflicts when different control signals are expected to manage different parts of the image in practical applications. This issue is especially pronounced with edge-type control conditions, where regions lacking boundary information often represent low-frequency signals, referred to as silent control signals. When combining multiple ControlNets, these silent control signals can suppress the generation of textures in related areas, resulting in suboptimal outcomes. To address this problem, we propose Minimal Impact ControlNet. Our approach mitigates conflicts through three key strategies: constructing a balanced dataset, combining and injecting feature signals in a balanced manner, and addressing the asymmetry in the score function’s Jacobian matrix induced by ControlNet. These improvements enhance the compatibility of control signals, allowing for freer and more harmonious generation in areas with silent control signals.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a well-designed approach to multiple CtrlNet integration by addressing the challenge of control signal conflicts through a "minimal impact" strategy. 
Specifically, the authors address several issues they found in multi-ControlNet integration.
1. To handle data bias in silent control regions, they use data augmentation and segmentation masks. This adds texture to low-signal areas. 
2. To avoid conflicts between control signals, they use an MGDA-inspired feature injection method. This balances gradients so that no single control dominates. 
3. They introduce a conservativity loss function to ensure stable training. This function keeps CtrlNet's influence to original U-Net minimal and improves consistency in multi-control outputs.

### Strengths
The solution proposed is clear and systematic. Experiments are comprehensive and convincing, covering various control signal combinations and providing robust quantitative and qualitative results. Limitation is discussed in the appendix.

### Weaknesses
Based on the methods presented, it appears that the proposed framework effectively supports scenarios involving more than two CtrlNets. Did the authors conduct experiments to evaluate performance in such cases? Since the experiments primarily focused on pairs of CtrlNets, I am curious about how well the approach scales to accommodate multiple CtrlNets.

Additionally, the authors mention the "Conservativity of Conditional Score Function", which seems to be a general principle that influences ControlNet performance, regardless of whether there is one or multiple CtrlNets in play. I wonder if the solutions proposed in this context could also enhance performance in standard single-CtrlNet applications. It might be beneficial for the authors to discuss this potential in the paper.

### Questions
Please refer to the *weakness* section.

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
4

### Summary
- The paper introduces Minimal Impact ControlNet (MIControlNet), a novel framework designed to refine the integration of multiple control signals within diffusion models for image generation.

- The innovative approach of MIControlNet includes rebalancing data distribution, multi-objective feature combination, and reducing asymmetry in the Jacobian matrix to minimize conflicts between control signals.

- Experimental results demonstrate that MIControlNet outperforms baselines, achieving better compatibility and fidelity in generated images with multiple control signals.

### Strengths
- The method improves the compatibility of multiple control signals, which is crucial for applications requiring simultaneous control from different sources.

 - By addressing conflicts between control signals, the approach leads to higher quality image generation, particularly in areas with silent control signals.

### Weaknesses
 - In Figure 1, why is it not the canny signal that suppresses the openpose signal? Is there some analysis?

- The authors should supplement corresponding **prompts**. Detailed prompts often lead to the generation of complex textures. Comparing the total variance and visual results under detailed/brief/null text conditions would enhance the persuasiveness of the proposed method in this paper.

### Questions
See Weaknesses.

### Soundness
4

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
2

### Summary
In current ControlNet training, each control is designed to influence all areas of an image so that conflicts occur where lacking boundary information(low-frequency signals) especially in the black areas. The authors proposed the Minimal Impact ControlNet(MIControlNet) that can handle conflicts when different control signals are expected to manage different parts of the image. The introduced silent control signals which utilizes segmentation masks can rebalance the distribution of high-frequency information in the blank area. The authors reorganized the formula of ControlNet giving theoretical enhancement and ensuring more stable learning dynamics. The proposed multi-objective optimization strategies which utilizes Multiple Gradient Descent Algorithm (MGDA) improved the model performance.

### Strengths
The problem settings and overall paper structure are well organized.

The qualitative results for both single control signal and multi control signals utilizing segmentation masking are well aligned with handling the distribution of high-frequency information in the blank area. The blur effect shows in ControlNet even with single condition generation in silent area, however the MIControlNet shows more high-frequency informations in silent area.

The proof that gradient of the conservativity loss of ControlNet is equal to the gradient of the estimated conservativity loss and simplified loss for the ControlNet optimization are well explained.

The proposed model achieves the best FIDs in most cases within the multi-control signals.

### Weaknesses
In 2.2, the notations and symbols are confused and hard to read.

The proposed estimated conservativity loss function needs to construct second order derivatives, which is computationally expensive.

The authors proposed three main contributions with rebalancing the data distribution, feature injection and combination, and conservativity loss, however there are no ablation studies at each component in the paper. The only comparison is that both the original feature combination and a balanced version together between ControlNet and proposed model. For example, there are no comparison about Jacobian Asymmetry between the other baselines in Figure 4.(b). To claim the main contributions of each method, it would be beneficial to compare the performance improvements of each method against ControlNet.

The problem settings and the flow of the solutions are well-structured, however, the segmentation masking and the feature injection process shown in Figure 3 seems to be a little simple. Although the two main contributions(silent control signals, feature injection method) enhanced the model performance in the targeted problems, the method to apply the techniques are not quite novel.

Minor:

In Figure 6, the legend seems to have lack of information.

### Questions
In line 121, $f^e_c$ seems weird. Doesn't the value under $f$ mean layer number?

### Soundness
4

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
3

### Summary
This article addresses the coordination of diverse control signals in diffusion models for precise manipulation, specifically focusing on the conflicts caused by low-frequency signals, termed "silent control signals." Such signals often interfere with those that generate finer details, resulting in suboptimal outcomes. To tackle this, the authors propose the Minimal Impact ControlNet (MIControlNet) framework, which minimizes ControlNet’s influence on the original U-Net and mitigates conflicts through modified training data, multi-objective optimization, and adjustments to the Jacobian matrix asymmetry in the score function. A two-stage training process is used: first, balanced data and feature injection for various conditions, followed by a secondary phase incorporating a conservativity loss to enhance signal compatibility and image fidelity.

### Strengths
1. Analyzed challenges in training diffusion models with multiple control signals for ControlNet: 

* Data Bias: Handling biases in regions influenced by "silent" control signals.

* Optimal Combination Ratios: Determining ideal ratios for integrating multiple ControlNet layers.

* Conditional Score Function Stability: Ensuring balanced, stable updates across control signals (referred to as the “conservativity” of the score function).

2. Introduced a conservativity loss function within a modular network structure, supported by theoretical analysis.
3. Results demonstrate that the new loss function improves texture details specifically in areas affected by silent control signals, achieving finer and more accurate generation.

### Weaknesses
1. ControlNet is not yet a widely recognized concept. It is recommended that the authors briefly introduce its definition when first mentioned; otherwise, readers may feel confused starting from the abstract.

2. Some phrases lack clarity. For example, in lines 18-19 of the abstract, "..., the silent control signals can suppress the generation of textures in related areas,..." leaves "related areas" ambiguous. Does this refer to areas that are texturally similar, spatially close, or something else? The lack of specificity makes it difficult to understand the exact nature of the problem being addressed. It would be beneficial to clarify if the suppression is due to spatial overlap, feature interference, or other factors.

3. There is a lack of necessary citations, such as in lines 164-165, where it states "to find the Pareto optimal solution, a state where no single objective can be improved...". Adding citations here would provide more credibility to the explanation. Specifically, the authors should cite work that formally defines and analyzes Pareto optimality in the context of multi-objective optimization.

4. The organization of the paper could be improved, as it is currently somewhat challenging to follow. Additionally, the main text does not sufficiently emphasize results showing the balancing of coefficients among multiple control signals. The paper would benefit from a more explicit discussion of how the proposed method achieves this balance and why it is important for the overall performance.

5. The three main issues highlighted in the problem analysis section lack clear support in the experimental results. The connection between the identified problems (data bias, optimal combination ratios, and conditional score function stability) and the experimental setup and results is not sufficiently clear. The authors should provide more direct evidence that these problems are indeed being addressed by their proposed method.

6. Ablation studies are missing, which would help illustrate the individual contributions of each component to the overall outcome. Without ablations, it is difficult to determine the necessity of each component of the proposed method. For example, it is unclear how much each of the modified training data, multi-objective optimization, and Jacobian matrix asymmetry adjustments contribute to the final result.

### Questions
* In Equations (8) and (9), what do v1 and v2 represent? Additionally, since λi varies across layers, should v1 and v2 also include subscripts to indicate properties at different layers within the network? 

* The concept of "conservativity" in ControlNet doesn’t seem to be a commonly used term. I find it somewhat confusing—could the authors provide further clarification? 
* In Figure 4(b), why is there no comparison with ControlNet? From the results, it appears that Stage-1 has a more significant impact than Stage-2. How do the authors view the balance between these two stages? This may relate to the previous question, as the authors mention that Stage-2 primarily enhances the "conservativity" of control signals. 

* Could this approach potentially be extended by first separating foreground and background for guided generation and then synthesizing the layers? This might allow for even greater control over specific elements.

### Soundness
2

### Presentation
1

### Contribution
2
