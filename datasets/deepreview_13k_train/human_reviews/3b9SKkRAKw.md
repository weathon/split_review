# LeFusion: Controllable Pathology Synthesis via Lesion-Focused Diffusion Models

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Patient data from real-world clinical practice often suffers from data scarcity and long-tail imbalances, leading to biased outcomes or algorithmic unfairness. This study addresses these challenges by generating lesion-containing image-segmentation pairs from lesion-free images. Previous efforts in medical imaging synthesis have struggled with separating lesion information from background, resulting in low-quality backgrounds and limited control over the synthetic output. Inspired by diffusion-based image inpainting, we propose LeFusion, a lesion-focused diffusion model. By redesigning the diffusion learning objectives to focus on lesion areas, we simplify the learning process and improve control over the output while preserving high-fidelity backgrounds by integrating forward-diffused background contexts into the reverse diffusion process. Additionally, we tackle two major challenges in lesion texture synthesis: 1) multi-peak and 2) multi-class lesions. We introduce two effective strategies: histogram-based texture control and multi-channel decomposition, enabling the controlled generation of high-quality lesions in difficult scenarios. Furthermore, we incorporate lesion mask diffusion, allowing control over lesion size, location, and boundary, thus increasing lesion diversity. Validated on 3D cardiac lesion MRI and lung nodule CT datasets, LeFusion-generated data significantly improves the performance of state-of-the-art segmentation models, including nnUNet and SwinUNETR.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This manuscript presents a diffusion model that utilizes forward-diffused backgrounds and reverse-diffused foregrounds as inputs, allowing the model to concentrate on reconstructing lesions specifically. Additionally, a post-processing method is applied to enhance generation quality.

### Strengths
This manuscript is well-motivated, and the experimental results are satisfactory.

### Weaknesses
There are several concerns regarding this manuscript:

* The novelty of the proposed approach is limited. The method does not significantly modify the underlying conditional diffusion process but instead introduces variations solely in the input.
* Figure 2 lacks clarity, and it would be beneficial to include the lesion-focused loss in this figure for a more comprehensive understanding.
* The writing lacks organization and is difficult to follow, which may impede readability and comprehension.

### Questions
Please revise Figures 1 and 2 to more clearly illustrate the novelty of your proposed approach. Rather than emphasizing the strengths of the paper or incorporating numerous elements into a single pipeline, focus on presenting a straightforward and cohesive pipeline that highlights the mechanisms unique to your method.

### Soundness
4

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
5

### Summary
The authors introduce a latent diffusion model-based method for inserting lesions into healthy medical images while also providing an accompanying mask. They utilize a number of additions to their model to address limitations of prior work or naïve approaches to this task (both pre-existing and seemingly novel), such as combining forward-diffused backgrounds with reverse-diffused foregrounds, introducing intensity histogram-conditioning to the diffusion model to control lesion texture, as well as techniques for further control of the shape, size etc. of the generated lesion. They evaluate their method for a variety of experimental scenarios on 3D cardiac MRI lesion and CT lung nodule generation, showing that their technique results in noticeable improvements to existing approaches with respect to using their generated data to train downstream task segmentation models.

### Strengths
Major
1. The paper is polished, well-written and well-presented. Topics and concepts are organized and presented in a digestible fashion.
2. Overall, decent technical novelty. This incorporates many techniques which all come together to result in a strongly-performing methods, some pre-existing (such as combined noised backgrounds with denoised foregrounds), and some seemingly novel (such as histogram-based textural control). Also, despite the many components, the approach still seems relatively watertight because these additions are all pretty lightweight/simple (a good thing). No requirement for an additional network or something of that sort.
3. Overall, results are strong. Clear improvements over baseline methods is basically all cases, using reasonable metrics. They also study a range of training settings, which is good. Clear improvements over Cond-Diffusion, which would be the naïve approach that many would think of first trying for this task; the limitations of it as discussed in the introduction are clear from the experiments.
4. They also have fairly extensive ablation studies for their method, which is important given the number of components that they propose using. There are still a few related questions that I have, but they are minor.
5. In general, the evaluation is fair and appropriate. The datasets are challenging benchmarks, and I think two is sufficient given the wide range of experiments completed on them. There is also a good number of baseline models, especially considering that this task is relatively niche, so the methodological baselines that they compare to seem strong.

Minor
1. The motivation for this problem is clear: pathological subjects are indeed rare, especially for screening populations. Your survey of the limitations of existing lesion synthesis approaches also supports the motivation; for example, they result in low quality backgrounds, they lack precise control over generated lesions, etc.
2. The use of a histogram representation to condition the model on may seem too reductive for some applications, but it seems to work well here (makes sense given the clear correspondence between histogram shape/number of peaks and generated lesion morphology shown in Fig. 3), supported by the clear improvement to your method that including the -H module produced.

### Weaknesses
Major
1. Some limitations of impact/scope: This task is clinically important but still fairly niche in medical image analysis, which itself is fairly niche within general machine learning and computer vision. The method (and task itself) also requires that dataset used needs the required annotations, which many medical datasets may not possess, and can be expensive/time-consuming to acquire. Overall, these limit the impact of the work somewhat, in the context of an ML conference at the level of ICLR, compared to a venue a bit more niche like MICCAI.

Minor
1. The benefits from using multi-channel decomposition (comparing the "-J" to no "-J" variants of your model in Table 2) are quite small. Can you provide some analysis or discussion of why this is the case, even if just hypothesizing? (However, I am guessing that the computational requirement to adding this component is practically negligible, so there is not really any harm in including it even if it results in only a very small performance improvement.)
2. You state in the abstract that synthesizing multi-peak and multi-class lesions is a "major challenge" I agree with the multi-peak case given how much your histogram-conditioning improved the generation of such lesions, but based on your channel decomposition module's only very small improvements to performance, I'm unsure if generating multi-class lesions could not already be done well by prior methods. Could you clarify this/point to your results that support this, and/or provide quantitative evidence that multi-class synthesis is challenging for prior approaches?

### Questions
1. In the tables (e.g. table 1), what do you mean by the significantly adverse/positive effects denoted by red/blue? Could you please clarify this in the text as well via a small note in the table caption(s)?
2. My suggestion: move image quality assessment quantitative results in the appendix (Table A2) to the main text if you have room. These are important metrics. You can shorten the related works to make space, that section doesn't need to be quite so extensive (or some of it could be moved to the supplementary).
    - Also, why didn't you evaluate unpaired perceptual metrics like FID, KID (https://arxiv.org/abs/1801.01401), SWD (https://arxiv.org/abs/1710.10196) etc.? the first two may have limitations for this task given that they use pretrained natural image features, but despite this they are still commonly used metrics for generative medical image models. I would consider adding these for future work, and also explaining why they are not used (particularly for the wider ICLR audience).
3. For the multiclass lesion case/-J model, did you study how performance/generation quality scales with adding more classes? This point may be a bit moot given how small the changes in performance were measured after adding the channel decomposition module to the base model, but I'm still curious.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a novel 3D lesion inpainting method, LeFusion, which uses diffusion models to address data scarcity in medical imaging. Its primary aim is to generate synthetic lesions in lung CT and cardiac MRI scans for augmenting training data in lesion segmentation tasks. The approach is validated through both visual quality assessments and data augmentation derived segmentation 

performance improvement. Three key contributions can be summarised below: 
LeFusion Model: The authors identify that existing lesion inpainting methods struggle to preserve anatomically accurate backgrounds alongside the inpainted lesion, remarking that modelling the former is both hard and unnecessary. LeFusion is introduced to address this challenge incorporating two distinct features: (a) Training on a lesion focused diffusion loss, which only considers the lesion region. (b) Preserving the background at inference time with RePaint [1] by generating the lesion separately, while integrating forward-diffused background contexts into the reverse diffusion process. This design yields realistic lesions, better preserved backgrounds and improves data augmentation outcomes in both CT and MRI compared to non-lesion-specific models (Cond-Diffusion) both with and without RePaint based sampling. 

Modality-Specific Variants: Two specialized variants are introduced to address modality-specific challenges. LeFusion-H uses histogram-based conditioning to capture diverse lesion textures in CT, succesfully solving the texture mode collapse observed for the baseline LeFusion. LeFusion-J models multiple tissue subtypes in MRI via multi-channel decomposition, which enables the joint generation of different lesion tissue types typically observed in cardiac lesions. Both variants demonstrate superior data augmentation effectiveness in their respective modalities. 

DiffMask for Mask Generation: All variants of LeFusion rely on either existing real masks or handcrafted ones as priors for generating lesions in healthy scans. As a more flexible alternative, DiffMask is a diffusion model that generates synthetic lesion masks from basic spatial constraints, defined as a sphere with user specified location and size. Using the generated masks for data augmentation leads to the largest improvement in segmentation performance relative to the baseline in both CT and MRI.

### Strengths
Lesion generating models are tools with significant potential for mitigating bias in medical vision AI algorithms concerning lesion detection, segmentation and quantification. Advancements in this topic should be highlighted in venues like this. 
The manuscript is sufficiently well written, all the provided Figures/Tables are insightful and adequately formatted. 
The choice of a 3D method for this inpainting problem is most adequate for CT and MRI. In these modalities, clinical lesion analysis workflows depend on the visualisation of multiple affected slices and 2D slice-wise inpainting methods would lead to slice-wise discontinuities. 

The proposed method is sufficiently contextualised in the Introduction and Related work sections, where the reseach gap is clearly defined. Beyond that, this gap is empirically demonstrated by experimenting with state-of-the-art approaches (Cond-Diffusion variants and RePaint). 

The proposed methodologies are thoroughly evaluated through comparisons with multiple other approaches, focusing on visual inspection of inpainted lesions (including comparison with real lesions) and their their downstream usability for training segmentation models. The latter evaluation used two different segmentation models, which contributes to the robustness of the findings across different segmentation training strategies. In addition, evaluating the approach on both MRI and CT datasets, ensures that the findings are not only applicable to one imaging domain. 

This paper provides multiple key contributions which not only address the research gap but also deal with modality specific challenges related to lesion texture and shape heterogeneity. The corresponding claims are well supported by the results.

### Weaknesses
While S4, the Introduction and Background sections seem to imply that the proposed lesion focused loss is a novel contribution proposed for the first time by the authors. This might not be necessarily true considering that there have been other works that employ similar approaches [2, 3]. While few and perhaps not as thoroughly evaluated, mentioning them could further strengthen the contextualisation of the approach. 

The description of the RePaint method in the experimental section implicitly suggests it consists of Cond-Diffusion using the RePaint [1] inference scheme. If that is the case it should be mentioned explicitly, if not then it should be better described. 
In the segmentation experiments, it is understood that masks priors for generating lesions in healthy scans (N’) are either derived from real masks, handcrafted or generated by DiffMask. However, additional information should be provided on how exactly the conditioning histograms in this N’ setting are selected when using LeFusion-H variants. 

Regarding DiffMask, the definition and role of boundary mask is not very clear. From Figure 4, it is presumed that it corresponds to the bounding box defining the volume crop centred on the lesion. However, the statement “The boundary mask removes areas outside the boundary at each diffusion step” challenges this concept. Further clarity on this point would be appreciated. Furthermore, it is only implicit, that the DiffMask takes the CT/MRI volume crop as an input in addition to the conditioning control sphere. Section 3.3. should be updated to enhance clarity on all these aspects. 

Adding supplementary details on how the model training and checkpoint selection was conducted for the RePaint, Cond-Diffusion, Cond-Diffusion (L) would improve transparency. 
 
[Minor]	 
More detail on the dataset preprocessing would be beneficial for further reproducibility. A mention to the volume resolution is particularly lacking. 

The choice of the specific crop-size could be further supported on previous work, for instance [4]. In addition, while not critical for acceptance, it would be interesting to study its effect over the results and would maybe answer the question: “How much local context is it necessary to generate realistic lesion?” 

While the purpose of the inpainted lesions is for downstream model training, further validating them using a radiologist would safeguard from potential biases that the generative model might be introducing the lesions. 

While describing Tables 1 and 2 it would be useful to clarify what is considered as “significant”. Since no standard deviations were provided, it is implied that these results were obtained for a single fold, so the concept of significance here is vague. In addition, while S5, the robustness of these findings to the specific data split could still be reinforced by adopting some sort of cross validation strategy. 
The authors left unclear whether the segmentation model was trained on the volume crops centred on the lesion or on the entire scans. From using the Copy-Paste method in the evaluation, the latter is presumed but it is not explicitly mentioned. 

In the cardiac MRI experiments, the LeFusion baseline of modelling the two lesion tissue types with separate models is mentioned as LeFusion in Table 2 but as LeFusion-S in Figure 5 and in the Appendix. It is suggested that the authors stick to one terminology. 
As a work mainly focusing on specific diffusion model mechanics for improved lesion inpainting, it makes sense that the evaluation focus on comparing different diffusion based methods. That said, it would still be interesting to see how GAN based approaches like [4, 5] would fair in this comparison.

### Questions
For specific questions please refer to the points made in weaknesses.

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
5

### Summary
This paper focuses on generating lesion-containing images from healthy images to address challenges in downstream segmentation tasks, such as real-world data scarcity and long-tail distribution issues. Previous research on medical image synthesis has primarily concentrated on lesion generation design, often overlooking high-fidelity background preservation. The authors propose a lesion-focused diffusion model, LeFusion, which maintains high-fidelity background by integrating the background from forward diffusion into the reverse diffusion process, thus simplifying the learning process and improving output control. Additionally, two effective strategies are introduced: histogram-based texture control and multi-channel decomposition to address the two main challenges in lesion texture synthesis: 1) multimodal and 2) multiclass lesions. The paper is well-written, with comprehensive experimental comparisons.

### Strengths
1. The overall paper structure is clear and well-expressed.
2. A novel diffusion model is redesigned from the perspective of high-fidelity background preservation, with two texture generation control techniques developed to address multimodal and multiclass issues.
3. The comparative methods are recent benchmarks from the past two years, making the results highly convincing.

### Weaknesses
1.There is a lack of detail on implementation specifics (such as the sampling process) and theoretical support for the method.
2. Analysis and discussion on the continuity at the fusion boundaries between lesion and background are missing, as well as the impact on downstream tasks.

### Questions
1. The reverse diffusion sampling process is not clearly defined; it appears to rely solely on the transformation in Equation (1), without detailing the sampling process or providing theoretical justification for omitting it.
2. Although the background from forward diffusion is used as the background in the reverse sampling process, and the loss constraint is applied only to the lesion area, how is continuity and smoothness ensured in the intersecting regions between the lesion and background?

### Soundness
3

### Presentation
3

### Contribution
3
