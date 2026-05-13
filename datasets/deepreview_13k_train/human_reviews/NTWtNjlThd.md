# Explicitly Disentangled Representations in Object-Centric Learning

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Extracting structured representations from raw visual data is an important and long-standing challenge in machine learning. Recently, techniques for unsupervised learning of object-centric representations have raised growing interest. In this context, enhancing the robustness of the latent features can improve the efficiency and effectiveness of the training of downstream tasks. A promising step in this direction is to disentangle the factors that cause variation in the data. Previously, Invariant Slot Attention disentangled position, scale, and orientation from the remaining features. Extending this approach, we focus on separating the {\em shape} and {\em texture} components. In particular, we propose a novel architecture that biases object-centric models toward disentangling shape and texture components into two non-overlapping subsets of the latent space dimensions. These subsets are known {\em a priori}, hence before the training process. Experiments on a range of object-centric benchmarks reveal that our approach achieves the desired disentanglement while also numerically improving baseline performance in most cases. In addition, we show that our method can generate novel textures for a specific object or transfer textures between objects with distinct shapes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors develop a network architecture to explicit extract shape and texture information from images, thus extending an approach to extract position, orientation and scale. The architecture is specific to the problem at hand, removing texture information to help extract shape and using shape-derived masks to extract texture information. The benefit of the disentangled representation is demonstrated in both scene understand tasks and image reconstruction tasks.

### Strengths
* Great results on image reconstruction tasks, good results on scene understanding tasks, good results on qualitative measures.
 * Improved latent representations are amendable for better interpretation.

### Weaknesses
 * The architecture is explicitly designed for shape and texture and cannot be extended to other latent dimensions, thus limiting the significance of the results. This represents a significant effort which is ad-hoc and hence should be saved only to crucial latent dimension; not sure texture is such.
 * Texture decoding uses shape information, which reduces the applicability of the method outside the context of the current projectt.
 * Shape decoding uses texture removing filter, which may by itself be responsible for some of the benefits of the approach.

### Questions
* Why was rotation invariance removed from the experiments?
 * Is the new shape and texture dimensions disentangled from position and scale information? To what extent were position and scale varied in the experiments?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to explicitly disentangle shape and texture of objects, while training using an unsupervised autoencoding loss. The paper shows that this disentanglement can achieve competitive performance at object discovery while achieving significantly higher performance on image reconstruction. Further the paper shows that their representations are indeed disentangled by doing a property prediction task.

### Strengths
- the motivation of disentangling shape and texture seems promising
- the paper proposes a  unique approach for disentangling texture from shape using Sobel Filter.
- the paper has good and dense comparisions in its experiment section
- the paper does a good job at presentation and figures.

### Weaknesses
 - the paper motivates the intro with better representation, generalization and downstream transfer by having an explicit disentangled representation, however doesn't compare with ISA or SA with that metric. 
- The paper relies on sobel filter to achieve this disentaglement but doesn't do a good job at explaining how exactly does the Sobel filter work and is able to remove the texture. Is sobel filter limited to CLEVR images for removing filter or can scale to COCO like images?
-  The paper says: "However, to the best of our knowledge, no research has been carried out on the explicit disentanglement of the texture and shape dimensions in object-centric learning,", i don't think this is true as there is work such as: D3DP (https://arxiv.org/abs/2011.03367), that do disentangle shape and texture explicitly in an object-centric manner. They use adaptive instance norm instead of using Sobel filter.
- The paper lacks a thorough analysis on the scalability of the Sobel filter for texture removal, particularly in comparison to other disentanglement techniques like Adaptive Instance Normalization (AdaIN). The current evaluation does not sufficiently demonstrate the robustness of the Sobel filter beyond the CLEVR dataset. Furthermore, the paper does not include downstream task comparisons with other object-centric learning methods such as Slot Attention and Independent Slot Attention (ISA), which is crucial for validating the practical utility of the proposed disentangled representations.

### Questions
- How does the paper compare against ISA or SA in terms of Figure 2 or other downstream tasks such as the one considered in this paper https://arxiv.org/pdf/2305.11281.pdf?
- What is the intuitive idea + the math behind sobel filter? Would such Sobel Filter generalize to real world texture like the one seen in COCO?
-  I think this authors should discuss D3DP in their paper.  Also compare against AdIN, as a way of disentangling shape and texture instead of using  Sobel Filters.

I'm happy to change my reviewer if the authors address my concern.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes an extension to previous Slot Attention and the subsequent Invariant Slot Attention algorithms for object discovery and representation factorization. Specifically, the proposed formulation incorporates the explicit goal of disentangling shape and texture into separate latent components.  This is achieved through constructing two streams of data, one specifically devoid of texture/color information through the application of a sobel filter. The feature representation from the latter is considered to be shape-only, with the assumption that the representation learned from the remaining stream should encompass everything else (textures and colors).

### Strengths
- It's a bit surprising to see that a weak application of the equivariant constraints still works sufficiently well here.
- Writing was generally clear, especially with regard to its relation to Slot Attention and Invariant Slot Attention

### Weaknesses
 - Works such as Lorenz et al. seem more closely related to this work than stated in the related works section. Specifically, the task of unsupervised landmark detection is nearly identical to the object-centric learning framework. Furthermore, both works are based on the same two-stream information bottleneck setup where you apply some sort of transformation to ensure either shape or texture information is only available in one stream but not the other. I think it would be necessary for the authors to elaborate further in the paper on the relation to works in that section of the writing.
- I think one of the strengths of the prior work ISA was the incorporation of more realistic settings such as Objects Room, CleverTex, and WaymoOpen. However, the results in this work seem limited to simpler synthetic datasets with only very smooth almost mono-color textures. I think it would be necessary to demonstrate improved results on at least some of those harder datasets to convincingly show that the solution proposed here is a step in the direction of real-world applicability.

### Questions
- Are there known limitations to using the sobel filter? How does the sobel filter setup perform on high frequency texture patterns?
- Can the authors also clarify the exact formulation for the variance regularization loss? Is the variance computed across dimensions like layernorm? or more like batch norm and across batch elements?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Edit: I believe that the revised paper is substantially improved due to the more thorough ablations and experiments, so I have raised my score to 6.

The authors propose to explicitly disentangle texture and shape information in slot attention by structuring the architecture in a specific way that encourages this. The image is passed through an edge detection filter to remove part of the texture information, which is then used to predict only the per-slot masks. The texture model takes the normal image as input and predicts the usual per-slot images, conditioned on the information from the shape encoder. Multiplying the two results in the usual slot attention reconstruction.

### Strengths
The motivation for the variety of modeling decisions is expressed clearly.
The experimental evaluation is thorough with many tests to evaluate specific contributions of the method. I especially like the disentanglement analysis experiments that confirm what type of information is represented by what encoder. It is encouraging to see that this decomposition appears to even improve results, a difference to many disentanglement methods that limit capacity instead.

### Weaknesses
The main weakness for me is the lack of consideration for the applicability on real world data. All the experiments are performed on tasks where a simple notion of texture and shape is possible. This is especially the case of approaches like DINOSAUR, where a simple Sobel filter will likely not work on the higher-dimensional features. I am therefore worried that the proposed approach is only useful in the toy examples studied, but not in more realistic use cases.

The approach proposed in the paper only *biases*, not enforces, the two models to focus on shape and texture information separately. In the case of the even just slightly more complex CLEVR dataset, we already see that the disentanglement results are degrading (end of section 5.2). This raises concerns about the robustness of the method to even moderately complex scenes. The reliance on a simple edge detection filter as a proxy for shape information is a significant limitation, as real-world shapes are often far more intricate and may not be adequately captured by such basic filters. Furthermore, the lack of explicit constraints on the disentanglement process means that the model might still learn to encode texture information in the shape encoder, and vice-versa, especially when the texture and shape are not easily separable.

### Questions
- It would be good to see ablation tests on exactly how much of an impact the quality of the edge filter has (for example, how well does it still disentangle if you don't use any edge filter at all?), or an experiment that uses slightly more complex textures (ClevrTex for example). For me, this is the most critical point since it pertains to how well we can expect it to work with realistic data; if it can be addressed I am willing to change my score to an accept.
- In the generative experiments, what happens when you sample shapes instead of textures?
- It is not clear to me if basing the approach on the ISA approach instead of base SA is necessary at all, or simply a modeling choice

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
