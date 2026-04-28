# TEASER: Token Enhanced Spatial Modeling for Expressions Reconstruction

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
3D facial reconstruction from a single in-the-wild image is a crucial task in human-centered computer vision tasks. While existing methods can recover accurate facial shapes, there remains significant space for improvement in fine-grained expression capture.  Current approaches struggle with irregular mouth shapes, exaggerated expressions, and asymmetrical facial movements. We present TEASER (Token EnhAnced Spatial modeling for Expressions Reconstruction), which addresses these challenges and enhances 3D facial geometry performance⁠⁠. TEASER tackles two main limitations of existing methods: insufficient photometric loss for self-reconstruction and inaccurate localization of subtle expressions. We introduce a multi-scale tokenizer to extract facial appearance information. Combined with a neural renderer, these tokens provide precise geometric guidance for expression reconstruction. Furthermore, TEASER incorporates a pose-dependent landmark loss to further improve geometric performance⁠. Our approach not only significantly enhances expression reconstruction quality but also offers interpretable tokens suitable for various downstream applications, such as photorealistic facial video driving, expression transfer, and identity swapping. Quantitative and qualitative experimental results across multiple datasets demonstrate that TEASER achieves state-of-the-art performance in precise expression reconstruction.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new model for reconstructing facial expressions more accurately from a single image by combining explicit facial parameters with an implicit, multi-scale appearance token. The method includes a token-guided neural renderer that captures detailed facial features, such as shadows, lighting, and subtle expressions, and a token cycle loss for self-supervised training, enhancing stability and interpretability for downstream applications such as face editing and expression transfer.

### Strengths
+ The paper is well-written and the main aspects of the proposed methodology are clearly presented. 

+ The introduction of the appearance token (main novelty) seems to provide some advantages over the closely-related method of SMIRK (Retsinas et al. 2024). These are mostly related to the photorealism of the synthesized face images

+ The experimental evaluation is done on two datasets (LRS3 and HDTF) and shows that the proposed method achieves improvements in terms of estimation of the detailed 3D geometry of the face. 

+ The paper includes also a detailed ablation study comparing 6 different versions of the proposed pipeline and providing evidence that all components are indeed useful.

### Weaknesses
 - The novelty over the closely-related method of SMIRK (Retsinas et al. 2024) is rather limited. The only crucial addition is the appearance tokenizer. A careful inspection of the results reveals that this addition seems to have fairly small impact on the quality of the 3D face reconstructions.

- In terms of methodology, the pose-dependent masking of eq. (13) seems to be suboptimal. It is an overly hard masking, since it creates discontinuities when the yaw angle becomes +/- \epsilon (a smoothly-varying confidence score for every landmark would have been more appropriate). In addition, the masking doesn't take into account the pitch angle at all, which is unrealistic since variation of the pitch angle results to occluded landmarks too.


- From the description of Section 4, it seems that the same individuals of the LRS3 are used in both training of the method and test (Table 1). Even if different frames of the individuals are used in training and testing, this is an unfair and inadequate experimental protocol. 

- The paper includes quantitative as well as qualitative comparisons with only two recent SOTA methods of 3D face reconstruction (SMIRK and 3DDFA-V3), which is insufficient.  Other methods such as DECA, EMOCA, Deep3DFace and FOCUS could have been included.

- The paper presents results of applying the proposed method to the downstream tasks of Identity Swapping and Face Animation (Figs. 6 and 7). However, there is no comparison with SOTA methods, which is inadequate.

### Questions
- Please comment on the novelties and advantages over the closely-related method of SMIRK. 

- Please comment on the pose-dependent masking. 

- Please clarify the issue regarding the LRS3 dataset (training and testing) that I mentioned above.

- Please comment on my criticism regarding the insufficient experimental comparisons (in terms of 3D face reconstruction as well as the downstream tasks of identity swapping and face animation).

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
The authors in this paper propose a hybrid face representation for better 3D face reconstruction and associated applications. The facial geometry is represented by FLAME and appearance is represented by a multiscale appearance token, which are combined using a token-guided neural renderer to generate reconstructed mesh with high fidelity. The paper also introduces novel loss functions and achieves SOTA results, which are adequately substantiated by ablation studies and experimental analysis.

### Strengths
1) The incorporation of the multiscale appearance token in the generator is novel. I like the idea of combining AdaIN and Controlnet based feature incorporation and the reasoning provided by the authors for the same.
2) The details provided in the supplementary are really helpful to better understand the method (and makes the method implementable by the research community). The video results also prove some of the claims in the paper (like temporal stability).

### Weaknesses
The paper is heavily based on the architecture / methodology of SMIRK, so some novel contributions of this paper are marginal and/or inspired by other existing methods.

### Questions
1) The authors mentioned using MobilenetV3 for performance and efficiency. Since efficiency is considered, what is the inference execution time of the proposed approach?
2) How is the parameter $\epsilon$ tuned in equation 13?

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
3

### Summary
This paper proposes a method for accurate facial reconstruction from single images. The central contribution of this method is a token-based neural renderer, that the authors argue helps improve geometry reconstruction by minimizing rendering errors. The neural renderer takes as an image, from which features are extracted using a CNN encoder. Different layers of this CNN are treated as a multi-scale feature bank which are projected to a common dimensional space by an MLP and concatenated together to generate the final appearance feature.  The appearance feature is then used to condition a UNet that renders the final image. In order to ensure the appearance tokens do not leak any information a token consistency loss is used. Additional losses to ensure rendering fidelity are specified in equation 10 of the paper. Both quantitative and qualitative results show improvements over prior work. However, I believe that in its current form, the evaluation is incomplete.

### Strengths
1) The paper is easy to follow and well written
2) The intuition of having a more powerful renderer for better reconstruction is, I believe, the right one. 
3) Both qualitative and quantitative results show improvements over prior art.

### Weaknesses
1) Right now the paper only reports image reconstruction error and contains no measure of ground-truth reconstruction accuracy. Since the renderer is conditioned on the input image, it is possible that the geometric reconstruction itself is not that great but the renderer just learns to copy the appearance pixels from the tokens. There is no evaluation in the paper to demonstrate that this does not happen. Ideally, I would’ve likes to see at least some ground-truth measure of error, for example, using the NoW dataset. In this case, two images of different views can be chosen at random, one can be used to condition the neural renderer and the other can be treated at the RGB ground-truth. Then both the geometric reconstruction error and the RGB error can be measured independently. This would make sure the renderer is actually learning the appearance tokens and not just copying the input pixels.

2) In general the sensitivity of the appearance tokens to different expressions/views of the same person must be evaluated. There is hardly any analysis of that. Specifically, it is unclear how the token consistency loss is actually preventing the tokens from encoding view or expression information, and what the trade-offs are. For example, if the token is forced to be completely invariant to expression, it might lose the ability to represent subtle but important appearance details.

3) While using multi-scale features does make sense, I would imagine the SMIRK renderer with more parameters would be able to learn them without explicit inductive bias. A general parameter count comparison with the SMIRK renderer would help place the current contributions in context. Furthermore, it is not clear how the multi-scale feature maps are combined. Is it a simple concatenation or is there a learned weighting scheme? This detail is missing from the method description.

### Questions
I have summarized by criticism and questions in points 1) and 2) of weaknesses. In general I would like to see greater analysis of the robustness of the renderer to difference expressions and views of the same person.

### Soundness
2

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
This work proposes a compact representation of self-occlusion shadows, glasses, lighting and various skin tone into a token. A facial neural renderer that output photo-realistic human portrait conditioning on the tokens. A token cycle loss for self-supervised training of the tokenizer and the neural renderer, and a pose-dependent loss and a region loss for better details reconstruction. Experiments show better image reconstruction quality compared to SMIRK.

### Strengths
1. The temporal consistency of the rendered portrait clips is significantly better than SMIRK.
2. The reconstructed facial geometry shows better expression details.

### Weaknesses
1. (L063-L069) states the limitations of previous methods: texture color is coupled with illumination, the rendered outputs are over-smoothed, and failed to render highly reflective facial surfaces. However, the results of the proposed method still suffer from these issues. The rendered portrait clips still suffer from over-smoothed textures, lack of highlights and fail to faithfully model the high specular region. Specifically, the lack of high-frequency detail in the rendered textures is noticeable, and the specular highlights appear diffused rather than sharp, indicating a limitation in accurately capturing lighting effects and surface properties.
2. Lack of an analysis of the concept represented by the multi-scale appearance tokenizer. i.e. which scale corresponds to the semantics and which scale corresponds to the texture details? What is the definition of the ‘semantics’? What would happen if we only change certain scales? Compared to previous methods which use simple render pipelines, the interpretability of the current method is hindered by the reliance on the deep neural renderer. Thus a complete analysis of the MSAT is crucial to determine to what extend can the pipeline be interpreted. The absence of a clear understanding of how each scale contributes to the final rendering makes it difficult to debug or improve the model. Furthermore, without a precise definition of 'semantics' within the context of the tokenizer, it's challenging to evaluate the model's ability to disentangle different aspects of appearance.
3. Though targeted at 3D facial reconstruction, this work completely drops metrics related to the face geometry, relying solely on the 2D image metrics. The argument (L393-L395) is possibly correct, no experiments are conducted to validate it. Running some experiments on a dataset with ground-truth 3D geometry can possibly support it. The lack of direct 3D geometry evaluation leaves a gap in assessing the accuracy of the reconstructed facial shape and expression, which are crucial aspects of 3D reconstruction.

### Questions
1. What contributes to the better temporal consistency?
2. How to measure the matching between the geometry and the rendered face? A reason previous method use simple renderer is because this mapping is defined explicitly. However here the mapping is implicit and there is no explicit textures obtained for downstream tasks.
3. (L372-L374) Training: the pre trained geometry encoder contains the shape, expression and head-pose encoder. Do the shape and head-pose encoder keep frozen during the entire training process, and only the expression encoder is updated? If this is the case, can we say that the contributions to better shape-matched facial rendering all come from the neural facial renderer, rather than the geometry shape estimator?

### Soundness
2

### Presentation
3

### Contribution
2
