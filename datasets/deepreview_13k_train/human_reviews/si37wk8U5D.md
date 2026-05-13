# Semantix: An Energy-guided Sampler for Semantic Style Transfer

- Decision: Accept
- Scores: 6, 8, 5, 6

## Abstract
Recent advances in style and appearance transfer are impressive, but most methods isolate global style and local appearance transfer, neglecting semantic correspondence. Additionally, image and video tasks are typically handled in isolation, with little focus on integrating them for video transfer. To address these limitations, we introduce a novel task, *Semantic Style Transfer*, which involves transferring style and appearance features from a reference image to a target visual content based on semantic correspondence. We subsequently propose a training-free method, *Semantix*, an energy-guided sampler designed for Semantic Style Transfer that simultaneously guides both style and appearance transfer based on semantic understanding capacity of pre-trained diffusion models. Additionally, as a sampler, *Semantix* can be seamlessly applied to both image and video models, enabling semantic style transfer to be generic across various visual media. Specifically, once inverting both reference and context images or videos to noise space by SDEs, *Semantix* utilizes a meticulously crafted energy function to guide the sampling process, including three key components: *Style Feature Guidance*, *Spatial Feature Guidance* and *Semantic Distance* as a regularisation term. Experimental results demonstrate that *Semantix* not only effectively accomplishes the task of semantic style transfer across images and videos, but also surpasses existing state-of-the-art solutions in both fields.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a training-free semantic style transfer method that innovatively leverages an energy-guided sampler, enabling it to produce both image and video results that surpass existing methods. The task of semantic style transfer is introduced to emphasize the alignment of semantic relationships,  enabling style and appearance transfer while avoiding content degradation and structural disruption.

### Strengths
1. Style Feature Guidance, Spatial Feature Guidance and Semantic Distance are clearly defined and correspond to the theme, successfully achieving semantic style transfer.
2. The paper is well-written and shows the model’s effectiveness through both quantitative evaluations and user studies.
3. The authors provide extensive supplementary materials and appendices to validate the effectiveness of the proposed method.

### Weaknesses
1. Some expression in Methods section lacks logical coherence. Some innovations are introduced rather abruptly, with insufficient theoretical foundation and clear explanations, such as the motivation of spatial feature guidance. Specifically, the paper does not adequately explain why minimizing the distance between context and output features in the feature space would preserve spatial structure. The connection between feature similarity and spatial structure preservation is not intuitively clear and requires more rigorous justification. Furthermore, the introduction of spatial feature guidance appears somewhat ad-hoc, without a clear explanation of why this specific approach was chosen over other possible methods for spatial control.
2. The related work section focuses on the field of style transfer but lacks a discussion of energy functions and diffusion-based inference guidance. The paper would benefit from a more thorough discussion of how energy functions have been used in diffusion models, particularly in the context of guiding the sampling process. This omission makes it difficult to contextualize the proposed method within the broader landscape of diffusion-based generative techniques. The lack of discussion on diffusion-based inference guidance also leaves the reader wondering how the proposed method compares to other guidance techniques.


### Questions
1. I have some confusion regarding spatial feature guidance. Why does calculating the similarity between output features and content features in the feature map preserve spatial structure? Would this impact the effectiveness of style guidance, such as injecting style information from the content reference? 
2. Regarding semantic distance, it seems that you have borrowed from previous methods ("Visual Style Prompting with Swapping Self-Attention") in the self-attention part. However, why does directly computing the L2 distance in the cross-attention mechanism help prevent overfitting? It would be helpful to explain the rationale behind this approach.
3. Acquiring feature maps requires three inference processes in total. Would this significantly increase inference time?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces Semantix, an energy-guided sampler designed for semantic style transfer that aims to transfer style and appearance features from a reference image to a target visual content based on semantic correspondence. The method leverages pre-trained diffusion models' semantic understanding capabilities to guide both style and appearance transfer. The approach consists of three key components: Style Feature Guidance for aligning style features, Spatial Feature Guidance for maintaining spatial coherence, and Semantic Distance as a regularization term. After inverting reference and context images/videos to noise space using SDEs, Semantix utilizes these components within a carefully crafted energy function to guide the sampling process.

### Strengths
1. The method is easy and can be easily applied to both image and video models without requiring additional modifications. 

2. The experimental results show that Semantix outperforms existing solutions in both style and appearance transfer tasks while maintaining structural integrity and semantic consistency.


3. The writing is mostly clear and the visualizations are decent. For example, I especially like the analysis presented in Fig. 3.

### Weaknesses
1. The motivation for semantic distance is not intuitive. The authors claim that this regularization is meant to prevent overfitting. It is unclear what overfitting the authors indicate, such as to prevent overfitting to the context or reference, or both? Also, it is hard to reason about why the regularization works to handle the problem.

2. Important reference is missing. For example, [1] also deals with universal style transfer which applies to both image and video domains, which is an ideal comparison and discussion.

3. Positional encoding doesn’t seem to have much impact. The qualitative difference between the default version and the deprived version is small. The quantitative difference is also small.

4. Demonstration problems: 1) Fig. 2 is very uninformative. The rightmost part is hard to perceptually understand. The leftmost part does not convey much information. The middle part is hard to observe different arrows and get their exact meanings. 2) Some tables have varied font sizes for titles, such as Tab. 2, 3, 4.

### Questions
Why do you revert the images at step 601 rather than smaller steps since from my point of view, smaller steps seem to induce better correspondence?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces an approach to transferring style between a reference image/video and a context image/video while accounting for the semantics of the elements observed in the images. This is achieved by providing guidance in a diffusion model in the form of an energy function. The proposed energy function leverages semantic correspondences between the reference and context inputs while preserving spatial relationships.

### Strengths
- Using semantic correspondence to perform style transfer is intuitive
- The training-free aspect of the method makes it attractive
- The results are visually convincing
- The paper is generally clear and reasonably easy to follow (with some exceptions listed in Weaknesses)

### Weaknesses
1) Originality:
- The idea of accounting for semantics in style transfer has been studied in the past. The most closely related work is Ozaydin et al. TMLR 2024, DSI2I: Dense Style for Unpaired Exemplar-based Image-to-Image Translation, which also uses the notion of semantic correspondence. However, other references therein already looked into leveraging semantics for style transfer (Shen et al., CVPR 2019; Bhattacharjee et al., CVPR 2020; Jeong et al, CVPR 2021; Kim et al. CVPR 2022). I acknowledge that there are methodological differences between these works and the proposed method, but this limits the conceptual originality of this submission, and this line of research should be discussed.

2) Methodology:
- The choice of T=601 seems a bit arbitrary. Does this work for any scenario/generative model? Is the influence of this studied empirically (this does not seem to be part of the ablation study)?
- The method has a number of hyper-parameters (\omega in Eq. 4, the \gammas in Eq. 5, \lambda in Eqs. 9-10), which seem to be set to fairly precise values according to Appendix B. Their influence is to some degree studied (in a on-off manner in Table 4, and on one particular example in Fig 12), but this analysis could be made more thorough.
- Line 313-314: This statement is not clear. How are the object region masks used?
- Won’t the spatial guidance of Eq. 12 tend to prevent the style transfer, i.e., by encouraging to preserve the appearance from the context image?
- It seems that the semantic aspect of the transfer is achieved via both the semantic correspondences used in F_{ref}, and the semantic distance employed in F_{reg}. Why is either one of these not sufficient, i.e., why are both needed?
- In Eq. 14, does sg stand for gradient clipping (as argued below the equation), or stop gradient (as would seem more intuitive based on the name)?
- As I understand it, in the case of video, motion consistency is assumed to be inherent to the generative model itself. However, even if it is the case, is there any guarantee that the style transfer process won’t destroy, or at least damage, this motion consistency?

Experiments:
- From Table 1, the proposed method offers a good tradeoff between the different metrics. However, so do StyleID and, to some degree, StyleFormer. Nevertheless, I acknowledge that the qualitative results show that the proposed method yields better quality than these baselines. This raises the question of whether these qualitative examples were cherry-picked to highlight the better performance of the proposed method over StyleID and StyleFormer, or if the metrics are far from being perfect. I acknowledge that the user study of Table 3 helps clarifying things.

Clarity:
- I find the overview of the method, both in the introduction and in Section 4, hard to follow.
- The purpose of the preliminaries (Section 3) is not clear, with mathematical notation sometimes not explicitly defined (e.g., x_t, \phi, \theta), and the link to the proposed method missing.

Minor:
- The authors should use \citep instead of \cite, unless the names of the authors of the corresponding reference should be part of the sentence.

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
3

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
This paper proposes a semantic style transfer method called Semantix that can handle style transfer and appearance transfer simultaneously. The key idea of this paper is to use the gradients of well-designed energy functions to guide the sampling process of pretrained diffusion models. Specifically, the three terms Style Feature Guidance, Spatial Feature Guidance, and Semantic Distance collectively form the energy function of this paper.

### Strengths
1. The proposed method is capable of performing both style transfer and appearance transfer with a single framework.
2. The proposed method is training-free and can be extended to video style transfer.
3. The stylized images generated by the proposed method are plausible.
4. Extensive experiments are conducted to evaluate the performance of the proposed method.

### Weaknesses
1. My primary concern is the lack of novelty in this paper. The use of energy function gradients to guide the diffusion sampling process has been extensively studied in prior diffusion-based research. Additionally, the energy function itself is not novel: the style feature guidance term resembles the style loss in style transfer, and the spatial feature guidance term aligns with content loss in style transfer.

2. The paper mentions style transfer for videos. What specific adaptations are made in the proposed method for video style transfer? Are motion aspects considered in both the context and synthetic images? Additionally, does applying this method to pre-trained video models impact stability and consistency? If so, why?

3. In the first row of Figure 7, the stylized images generated under different settings appear very similar, without showing significant differences.

4. In Figure 3, why is it claimed that the best results occur at t=601? The results across time steps seem quite similar. It is recommended to compare results across different time steps in the experiments.

5. I’m curious about the runtime of the proposed method. Is its inference speed comparable to or faster than previous methods?

### Questions
please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
