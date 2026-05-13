# RB-Modulation: Training-Free Personalization using Stochastic Optimal Control

- Decision: Accept
- Avg Score: 8.00
- Scores: 10, 8, 6, 8

## Abstract
We propose Reference-Based Modulation (RB-Modulation), a new plug-and-play solution for training-free personalization of diffusion models.
Existing training-free approaches exhibit difficulties in (a) style extraction from reference images in the absence of additional style or content text descriptions, (b) unwanted content leakage from reference style images, and (c) effective composition of style and content. 
RB-Modulation is built on a novel stochastic optimal controller where a style descriptor encodes the desired attributes through a terminal cost. 
The resulting drift not only overcomes the difficulties above, but also ensures high fidelity to the reference style and adheres to the given text prompt. 
We also introduce a cross-attention-based feature aggregation scheme that allows RB-Modulation to decouple content and style from the reference image.
With theoretical justification and empirical evidence, our framework demonstrates precise extraction and control of *content* and *style* in a training-free manner. 
Additionally, our method allows a seamless composition of content and style, which marks a departure from the dependency on external adapters or ControlNets

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper borrows some concepts from optimal control and applies them to the diffusion models, which are training-free. The method is SOTA for the problems attempted on image stylization and composition.

### Strengths
+ The paper presents theoretical underpinnings from optimal control. It uses those ideas to solve the training-free stylization problems similar to Deep Image Prior, which is somehow not cited in the paper.

+ The work has several merits, especially in the problem of prompt-based image stylization in the training-free framework, though a pre-trained diffusion model is used for generation. 

+ The title RB-Modulation is pretty weird and does not suit the paper's excellent contribution. This must be revised to put the paper in the correct research context. 

+ The idea and theoretical contribution are quite good, and this work could lead to more interest in similar works.

### Weaknesses
- Title needs revision

- Missing references such as Deep Image Prior need to be cited.

### Questions
* Sorry to quote from your limitation. However, I am curious to know how feature descriptors can help this work.

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
4

### Summary
This paper introduces reference-based modulation (RB-Modulation) for training-free personalization of diffusion models. The modulation builds on concepts from stochastic optimal control to modulate the drift field of reverse diffusion dynamics, incorporating desired attributes (e.g., style or content) via a terminal cost. Besides, the author also proposes Attention Feature Aggregation (AFA) module to decouple content and style in the cross-attention layers. The qualitative and quantitative results verify its effectiveness.

### Strengths
1. The idea is novel. The author provides the first training-free personalization framework using stochastic optimal control. 
2. The author provides theoretical justifications connecting optimal control and reverse diffusion dynamics. 
3. The qualitative and quantitative results are very promising for not only stylization, but also content-style composition. The author also conducts user study to further verify its superiority.

### Weaknesses
1. As the title said, the method aims for personalization. Therefore, I recommend the author add some comparison with classical personalization method, not just style transfer methods.
2. The section on ablation study in the paper is too brief. Considering that the AFA and SOC models are central to the article, I recommend that the authors include numerical comparisons and more qualitative comparisons. Specifically, it is unclear how the performance changes with different configurations of the AFA module, such as varying the number of attention heads or the dimensionality of the feature aggregation. Similarly, for the SOC model, it would be beneficial to see how the choice of terminal cost function and the parameters of the stochastic optimal control affect the final results. A more detailed ablation study would provide a better understanding of the sensitivity of the method to these parameters.
3. For the content-style composition experiment, I recommend the author to provide more complicated ref content (dog, sloth, cat are simple cases, or you can change the color of the ref to see whether the proposed method has achieved better content-style composition) to verify its effectiveness. The current examples do not fully explore the method's ability to disentangle complex content and style attributes. For instance, using reference images with intricate textures, multiple objects, or varying lighting conditions would provide a more rigorous evaluation. Furthermore, changing the color of the reference content while maintaining its shape and structure would test the method's ability to separate color as a style attribute, rather than conflating it with content.
4. For situations that require ControlNet to control the layout, can the method generalize well to these scenarios?

### Questions
Please refer to the weaknesses part.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents am encoder-based (i.e. fine-tuning free) method for style personalization/ customization in text2image diffusion models.  The approach (RB-Modulation) is to consider the reverse dynamics of diffusion as a stochastic control problem with a terminal cost objective that aligns extracted style features with the exemplar style features using a pre-existing  style descriptor [Somepalli, CVPR 2024].   A novelty of the approach is the ‘AFA module’ proposed which separates style and content using cross-attention to mitigate content leakage from the reference image.  The authors claim but do not comprehensively show this allows controlled integration of style and content elements.

### Strengths
The formulation of the feed-forward instance personalization problem using a ‘optimal controller’ is novel over the majority of prior works in this category that focus up adaptation.  However the practicalities of the problem seem to demand iterative reverse/feed-forward steps which negates a lot of the benefit of theoretical arguments and underlying assumptions presented.

### Weaknesses
 Deeper comparisons could have been made to the NST literature which bear some relevance both in task and in approach particularly the recent diffusion based approaches.  Specifically the paper bears some similarity with prior works that partly reverse the diffusion process and then run it ‘forward’ again with style conditioning either from CLIP or from style descriptors.  For example ‘Uncovering the Disentanglement Capability in Text-to-Image Diffusion Models’ [Wu et CVPR 2023) and PARASOL [Canet-Tarres et al., CVPR 2024] which uses ALADIN style descriptors for conditioning as does DIFF-NST [Ruta et al., ECCVW 2024].  Although the literature survey is quite broad in the areas of NST and style conditioned diffusion, there is limited focus on prior descriptor-based stylization work including these works and how the proposed approach fundamentally differs especially considering the use of cross-attention in AFA versus these works.  

The paper claims extensive experiments covering stylization and content-style composition as one of their three contributions.  It would have been helpful to see experiments exhibiting more nuanced control over style i.e. fine-grained variations of similar style, to exercise the controllability offered via the style descriptor conditioning.  Conditioning on text is sufficient to give coarse grain control over style (e.g. neon may be specified versus a descriptor for neon, as shown in the examples).  The fine-grained control offered by a continuous style descriptors in a feed-forward framework seems the main benefit but is not discussed or explored.  Similarly a matrix-like experiment showing descriptor interpolation and varying weights on the disentangled content/style would have been helpful to show the practical use/controllability of the approach.

### Questions
Please see the above questions in the weakness section.  Overall this appears a technically sound paper but that does not fully contextualize its contribution in the literature or fully evidence its practicality.  The authors can consider addressing this in the rebuttal.

POST-REBUTTAL:  Additional works raised in this review have been discussed within Section 2 of the main paper to contextualize the contribution.  Additional experiments have been added to the supplemental material to show the visual results of continuous variation of style strength and of style interpolation.  I have raised my initial score accordingly to reflect a recommendation to accept the paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose RB-Modulation, a method that allows training free stylization and content-style composition with diffusion models. The authors reframe the personalization task as an optimal control problem, and propose an additional Attention Feature Aggregation (AFA) module that performs content/style disentanglement. The authors include extensive qualitative/quantitative results that demonstrate the effectiveness of their proposed method.

### Strengths
1. AFAIK, personalization with diffusion models are inherently tricky in the sense that training based methods take a long time or training free methods lack in fidelity or fail in content/style disentanglement. The proposed RB-Modulation takes on a training free method that achieves both content/style disentaglement in a training free manner.

2. Evaluations are comprehensive and the proposed method surpasses previous SOTA methods. Qualitative results are especially impressive.

3. The paper is well written and easy to follow.

### Weaknesses
1. The choice of the baseline model (StableCascade) seems like a design choice. Authors might want to provide additional results on more widely adapted baseline models (e.g. SDXL), since this can show whether the inherent high fidelity results stems from the potency of StableCascade or their proposed method. It is unclear if the observed performance gains are due to the proposed method or the specific architecture of StableCascade, which is known for its high-fidelity generation capabilities. Testing on a more common baseline like SDXL would help isolate the contribution of RB-Modulation.
2. Most of the qualitative results seem to be on generated reference style/content images. The proposed method seems to be agnostic to whether the reference image is generated or not. Results with non-generated reference images would be appreciated. The reliance on generated reference images makes it difficult to assess the method's performance in real-world scenarios. Including results with photographs or other non-synthetic images would provide a more comprehensive evaluation.
3. Authors use Consistent Style Descriptor (CSD) to extract style features. Are there alternatives for this module? What was the main reasoning behind this choice? The paper does not sufficiently justify the choice of CSD over other potential style descriptors. A discussion of the trade-offs and limitations of CSD, as well as a comparison to alternative methods, would strengthen the paper.
4. For content style composition, it seems like the content is also processed in the same manner as style. Is this optimal in terms of content identity preservation? In algorithm 1 and 2, it seems like the image latent is only updated by the loss w.r.t the style descriptor loss. Would this not result in information loss about the identity of the content? The current approach appears to treat content and style features symmetrically, which may not be optimal for preserving content identity. The optimization process seems to prioritize style transfer, potentially at the expense of content fidelity. A more detailed explanation of how content information is preserved during the optimization process is needed.
5. In figure 1, the resulting images do not seem to hold the content identity of the reference content image, but instead seems to heavily rely on the given text description. Using examples from figure 2, additional content-style composition results on including/excluding $K_c, V_c$ would be appreciated. The results in Figure 1 suggest that the method struggles to maintain content identity, especially when the text prompt is strong. It would be beneficial to see an ablation study on the impact of the content features ($K_c, V_c$) on the final output, specifically how they contribute to content preservation.

### Questions
1. Does RB-Modulation also work for recent flow based models? Does the standard reverse SDE for the OU process hold for flow based models, or will the optimal controller have to be redefined?

### Soundness
4

### Presentation
3

### Contribution
3
