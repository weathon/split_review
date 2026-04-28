# Towards Lightweight Deep Watermarking Framework

- Decision: Reject
- Avg Score: 7.60
- Scores: 8, 8, 8, 8, 6

## Abstract
Deep learning-based watermarking models play a crucial role in copyright protection across various applications. However, many high-performance models are limited in practical deployment due to their large number of parameters. Meanwhile, the robustness and invisibility performance of existing lightweight models are unsatisfactory. This presents a pressing need for a watermarking model that combines lightweight capacity with satisfactory performance. Our research identifies a key reason that limits the performance of existing watermarking frameworks: a mismatch between commonly used decoding losses (e.g., mean squared error and binary cross-entropy loss) and the actual decoding goal, leading to parameter redundancy. We propose two innovative solutions: (1) Decoding-oriented surrogate loss (DO), which redesigns the loss function to mitigate the influence of decoding-irrelevant optimization directions; and (2) Detachable projection head (PH), which incorporates a detachable redundant module during training to handle these irrelevant directions and is discarded during inference. Additionally, we propose a novel watermarking framework comprising five submodules, allowing for independent parameter reduction in each component. Our proposed model achieves better efficiency, invisibility, and robustness while utilizing only 2.2\% of the parameters compared to state-of-the-art frameworks. By improving efficiency while maintaining robust copyright protection, our model is well-suited for practical applications in resource-constrained environments. The DO and PH methods are designed to be plug-and-play, facilitating seamless integration into future lightweight models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper examines the loss function in deep watermarking models and introduces two innovative methods. The first method, the Detachable Projection Head, enhances decoding accuracy by aligning outputs with the intended classification through projection close to the decision boundary. The second method, Decoding-Oriented Surrogate Loss, ensures a stable training process and emphasizes decoding accuracy by maintaining a safe distance for the deflation and inflation parts of the loss function.

### Strengths
Discusses a very noteworthy issue: watermarking of several types of data.

### Weaknesses
Currently, the safe distance (\epsilon) in the DO loss is manually set. Could this parameter be improved with automated tuning or adaptive methods to enhance performance and ease of use?

Geometric distortions are common in real-world scenarios, yet PH and DO do not achieve the best performance under these conditions. Can the methods be improved to better handle such distortions?

While PH is not used during inference, it increases the complexity of the training process. How large is the PH in terms of parameter count and computational demand? Is substantial computational power required for its training, and could its size be optimized?

### Questions
Refer to Weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper analyzes the limitation of existing deep watermarking approach in the gap of the losses in the training and decoding phase. Therefore, they propose a Decoding-Oriented Surrogate Loss and a detachable projection head, which maintains the performance of the watermarking but also requires much less computational costs.

### Strengths
- The motivation of the paper is grounded in analysis and the experimental results sufficiently validate the claim.
- They also considered the robustness against diffusion-based attacks.
- The paper is well-written.

### Weaknesses
 - The citation format should be fixed. At least the items should be wrapped in a bracket.

### Questions
1. I'm wondering what about the robustness against clipping? 
2. What is the motivation behind the light-weight deep watermarking architecture design?

### Soundness
3

### Presentation
3

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
This article discusses the need for efficient deep learning-based watermarking models for copyright protection. It identifies a mismatch between common decoding losses and actual goals as a key issue, leading to parameter redundancy. The authors propose two solutions: a redesigned loss function and a detachable module for training. They introduce a new framework with submodules for parameter reduction, achieving better efficiency, invisibility, and robustness with significantly fewer parameters, making it suitable for resource-constrained applications. The proposed methods are designed for easy integration into future lightweight models.

### Strengths
1. The paper is well-written and well-organized.
2. The idea is interesting to the digital watermarking community. The method is simple and easy to deploy.
3. The evaluation is comprehensive, thoroughly considering robustness against multiple distortions.

### Weaknesses
1. The proposed end-to-end framework doesn't seem to have many modifications compared to existing frameworks. Why does this framework reduce parameters?
2. I understand that due to space limitations, the authors have placed a lot of content in the Appendix. However, some important content should be in the main text, such as some visual results and the implementation of the projection blocks.
3. Although the discussion in the evaluation section is thorough, I think it is necessary to summarize the advantages and disadvantages of the two proposed methods, PH and DO, in the conclusion.

### Questions
1. The Decoding-Oriented Surrogate Loss is derived from the MSE loss. Why not use the BCE loss derived in Eq. (21)?
2. What are A and B in Eq. (4)? Are they learnable? I did not find details about A and B in Appendix C.
3. Why does the PSNR reach as high as 72.64 and 67.75 in Table 6 and Table 8?
4. The paper claims that NWIP mitigates the impact of distortions on the watermarked image. However, NWIP and the ME module are deeply coupled and trained end-to-end. How can you determine the function of each module when they function together?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper provides a proper exploration of parameter lightening for watermarking models. The problem of mismatch between the actual decoding objective and the optimization objective of the commonly used decoding loss is solved. The solution to the above problem is attempted from the point of view of adding projection blocks and proxy losses. And the impact of each block on robustness at fine granularity is discussed after subdividing the watermarking framework.

### Strengths
For the first time, we identify the mismatch between the optimization objectives of commonly used decoding losses (e.g., mean-square error and binary cross-entropy loss) and the actual decoding objectives, and confirm the existence of such a mismatch and its impact through ablation studies, which provides a new perspective for model optimization.
The proposed separable projection head (PH) and decoding-oriented alternative loss (DO) effectively mitigate the negative impact of irrelevant optimization directions, allowing the lightweight model to achieve SOTA performance while maintaining high performance.
The lightweight model outperforms existing models in terms of invisibility, robustness, and efficiency for other domains with limited computational resources, and minimizes performance loss by further compressing the model with a fine-grained deep watermarking framework.

### Weaknesses
1. the authors don't seem to have considered the issue of capacity, and suggest discussing this part; 
2. there are some spelling problems, e.g. "robust- ness" in table9 at line 1005 
3. we know that robustness depends mainly on the type and intensity of noise added during the training phase, i.e., the NWIP module, but in the The paper does not give detailed experimental parameters, but only describes the noise parameter settings in the testing phase.

### Questions
1. In terms of comparison experiments, because the main concern in watermarking is capacity, imperceptibility, robustness and efficiency. In this paper, we mainly focus on the efficiency improvement, but we should ensure that the other parameters are the same for a fair comparison.HiDDen's algorithm can guarantee that the embedding in the grey scale image of size 16*16 embedded in the length of 52 bits of information, the embedded information capacity can be up to 0.203 BPP.And the image used in this paper is a 3*128*128 colour image, the embedded information length is 64 bits, the capacity is much lower than HiDDen's, so the result of such a comparison should be understood as unfair, please explain why. Besides, the embedding capacities of several other compared algorithms are not consistent, how are they compared? 
2. Discriminative networks have been used in image watermarking frameworks since HiDDen and have shown advantages in enhancing the invisibility of watermarking frameworks. The authors of this paper did not consider this module in the newly proposed framework, please explain the reason, is it because high invisibility can be achieved without discriminative networks, to reduce the parameters so it is not used or there is another reason, please explain. 
3. In response to the decomposition of the MSE loss function in the paper, we see the role of the different loss components, would like to ask if this decomposition is first proposed in this paper? Or is there already a readily available scheme in the field of knowledge distillation that performs a similar decomposition of the loss function, and this will affect the reassessment of the paper's innovativeness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the limitations of current deep learning-based watermarking models used for copyright protection, which often have too many parameters, making them impractical for deployment, and lack robustness and invisibility. The authors identify a key issue: a mismatch between commonly used decoding losses and the actual decoding objectives, leading to redundant parameters. To tackle this, they propose two innovations: a Decoding-oriented surrogate loss (DO), which redesigns the loss function to minimize the impact of irrelevant optimization directions, and a Detachable projection head (PH), which adds a redundant module during training to handle irrelevant directions and is removed during inference. Additionally, the paper introduces a new watermarking framework with five submodules that allow for parameter reduction in each component. The proposed model achieves high efficiency, invisibility, and robustness, using only 2.2% of the parameters of current state-of-the-art frameworks, making it well-suited for resource-constrained environments.

### Strengths
- The experiments are comprehensive, yielding satisfactory results, particularly under lightweight structural conditions (where the number of model parameters is significantly reduced), with performance surpassing the baselines.
- The motivation is fairly strong.

### Weaknesses
 **Cons:**
- The contribution of the paper primarily relies on the proof and explanation of Equation (3). However, the explanations for the three types of loss lack intuition, or the intuition is not sufficiently evident, which undermines the technical rigor of the paper. Specifically, while the decomposition of the MSE loss into three components ($L_{deflation}$, $L_{inflation}$, and $L_{regularization}$) is presented, the paper does not provide a clear, intuitive explanation of why these specific components are chosen or how they relate to the decoding objective beyond a mathematical derivation. The paper needs to clarify why minimizing $L_{deflation}$ aligns with the decoding objective, and why $L_{inflation}$ and $L_{regularization}$ are detrimental, beyond the presented equations.
- The proposed framework does not introduce a clear distinction from existing methods, and its novelty is not apparent. The paper does not adequately articulate how the proposed decoupling of the decoder into Noised Watermarked Image Preprocessing (NWIP) and Message Extraction (ME) modules fundamentally differs from existing approaches. It is unclear what specific limitations of previous integrated decoder designs are addressed by this separation, and why this separation is crucial for parameter reduction beyond simply having two modules instead of one.
- The writing in the methods section (Section 3) is poor, making the purpose of adding the Detachable Projection Head unclear. The writing approach is problematic; you should first clarify the goal of this method (is it based on insights or analysis from Equation (3)?) and then explain how it achieves this goal. Currently, the explanation is difficult to follow. The paper fails to clearly articulate the problem the Detachable Projection Head is designed to solve. It is not clear whether the projection head is intended to mitigate the impact of $L_{inflation}$ and $L_{regularization}$ during training, or if it serves another purpose. The connection between the theoretical analysis of the loss function and the practical implementation of the projection head is weak.
- Furthermore, the discussion of the gap is limited to issues with MSE loss; the paper should also address cases with non-MSE loss functions. The analysis of the mismatch between the decoding loss and the decoding objective is primarily focused on MSE loss. The paper lacks a discussion of how the proposed framework and analysis would extend to other commonly used loss functions in watermarking, such as binary cross-entropy (BCE) loss, which is frequently used for binary message extraction. The paper should discuss whether the same decomposition and analysis apply to BCE or other loss functions, and if not, how the framework would need to be adapted.

**Minor Points:**
- Ensure that the full term accompanies the abbreviation the first time it appears. In Figure 1, the abbreviations are challenging to understand without prior context.

### Questions
**Questions and Suggestions for the Authors:**

1. **Clarification of Equation (3) and Loss Functions**  
   Could you provide a more intuitive explanation of the three loss functions associated with Equation (3)? While Equation (3) appears central to the paper’s contribution, the intuition behind the chosen loss functions is not immediately clear. Offering a deeper rationale or illustrative examples could significantly strengthen the technical clarity and impact of the work.

2. **Differentiation of Framework from Existing Methods**  
   How does the proposed framework fundamentally differ from other established methods? Currently, the distinctions between this framework and prior work are unclear, making it difficult to assess the novelty of your approach. A discussion contrasting your framework’s unique aspects or providing a comparative analysis would be helpful.

3. **Purpose and Rationale for the Detachable Projection Head**  
   Can you elaborate on the motivation for including the Detachable Projection Head in your framework? The methods section does not clarify its purpose or the anticipated effect on the model’s performance. It would be beneficial to specify whether its addition is grounded in the analysis of Equation (3) or derived from other empirical insights. Furthermore, explaining how the Detachable Projection Head contributes to the objectives of the model would improve readability and comprehension.

4. **Addressing Non-MSE Loss Functions**  
   Are there insights or considerations regarding loss functions beyond MSE? The current discussion appears to focus solely on MSE loss, yet it would be valuable to understand how the proposed framework performs or could adapt with non-MSE loss functions. Addressing this could broaden the applicability and relevance of your approach.

5. **Terminology and Abbreviations in Figures**  
   In Figure 1 and throughout the text, could you ensure that each abbreviation is first accompanied by its full term? This will greatly enhance readability, especially for readers unfamiliar with the specific terminology.

### Soundness
3

### Presentation
2

### Contribution
3
