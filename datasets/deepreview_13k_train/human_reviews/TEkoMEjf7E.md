# Phidias: A Generative Model for Creating 3D  Content from Text, Image, and 3D Conditions with Reference-Augmented  Diffusion

- Decision: Accept
- Scores: 6, 6, 5, 6, 8

## Abstract
In 3D modeling, designers often use an existing 3D model as a reference to create new ones. This practice has inspired the development of \emph{Phidias}, a novel generative model that uses diffusion for reference-augmented 3D generation. Given an image, our method leverages a retrieved or user-provided 3D reference model to guide the generation process, thereby enhancing the generation quality, generalization ability, and controllability. Our model integrates three key components: 1) meta-ControlNet that dynamically modulates the conditioning strength, 2) dynamic reference routing that mitigates misalignment between the input image and 3D reference, and 3) self-reference augmentations that enable self-supervised training with a progressive curriculum.  Collectively, these designs result in significant generative improvements over existing methods. \emph{Phidias} establishes  a unified framework for 3D generation using text, image, and 3D conditions, offering versatile applications. Demo videos are at: 
\href{https://RAG-3D.io/}{\textcolor{red}{\tt\small{https://RAG-3D.io/}}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper present a reference-augmented method using retrieved 3D objects as auxiliary guidance to reduce the ill-posed nature of the single-view 3D reconstruction task. The method leverages multi-view diffusion zero123++ for the generation of 6 novel view images, and scale-up the LGM for 3D reconstruction. The main contribution of the paper is to use input concept image (typically lack of 3D information of the back or side view, etc.) to refer a similar 3D objects from their 3D database (40K objects selected from Objaverse), the 6 canonical coordinate maps (CCM) from referred 3D object is used to generate better multi-view images. Meta-ControlNet with dynamic resolution of the intake CCM during diffusion sampling contribute to the misalignment dilemma between the concept images and referred 3D object. The results show that the method outperform other SOTA models in image-to-3D tasks given the proper 3D object reference. And it may extend to text-to-3D, and 3D-to-3D applications.

### Strengths
1. The framework extends the controllability of current image-to-3D models. The model retrieves an auxiliary 3D object as guidance to improve the 3D reconstruction quality. The results shows outperformance than current SOTA models.

2. The paper propose meta-controlnet, and self-reference inference to let model learn how to resolve the conflict between retrieved objects and concept front-view image. Given the setting by the paper claimed, the model is able to provide reasonable 3D generation results matches on both sides.

3. The model is able to extend to text-to-3D and 3D-to-3D generation tasks, which may contribute to more broad applications.

### Weaknesses
1. (model behavior) The model is trained with self-augmented ground-truth 3D objects, in order to handle the misalignment dilemma. However, as the A.4 specified, the augmented ones are still very similar to the ground truth. Moreover, all showcases are with no explicit conflicts between concept image and 3D objects. This raises the question of how a bad retrieval influence the model performance, which is actually common in practical case (as line 878-879). More comprehensive analysis or comparisons are necessary. Specifically, the paper lacks a detailed analysis of the model's behavior when presented with significant discrepancies between the input image and the retrieved 3D reference. The current experiments do not adequately explore the failure modes of the model when the retrieved reference is geometrically dissimilar or semantically inconsistent with the input image. This is crucial because real-world retrieval scenarios often produce imperfect matches, and the model's robustness to such cases is not sufficiently demonstrated.

2. (retrieval robustness) The quality of the retrieval directly influence the improving of the generation quality, especially on the back or side views. I elaborate in detail in Question-1. If the user have either a out-of-retrieval-database front-view concept image, or the retrieval brings an unreasonable objects, the model output may not be as good as claimed. As Fig.7 shows, random reference as an example of non-similar retrieval may provide unreasonable results. This restricts the usage of the method. The paper does not provide a clear strategy for handling cases where the retrieval process fails to find a suitable 3D reference. The reliance on a pre-existing database of 3D objects limits the applicability of the method to scenarios where such a database is not available or does not contain relevant objects. The paper should include a discussion on the limitations of the retrieval component and potential strategies for mitigating its impact on the overall performance.

3. (restricted/unfair experiment setting) Followed by weakness-1, the paper constrains the input image as only-front-view (line 221-222) to all competitor models. A random view, or 2-4 views as other related works defined, will contain more geometric information of the 3D details of the object. If not restricting to only-front-view input, using other models which do not require an auxiliary 3D object input like OpenLRM may already provide reasonable results. Their results may be better than the results with no reference in Fig.1, and Fig.7, and SOTA results in Fig. 5. The restriction to front-view inputs for all competing methods creates an artificial disadvantage for those methods that are designed to leverage multi-view information. This makes the comparison unfair and does not accurately reflect the capabilities of the compared methods. The paper should include a more comprehensive evaluation that considers different input view settings.

4. (restricted/unfair experiment setting) In the model evaluation section, all showcase examples meet the optimal situation of the framework. (a) The retrieved 3D objects is very similar to the concept image in the front view, (b) there is no/little conflicts on the other views. Given that, the improvement of the quantitative results in Tab.1 is still marginal. The row "Ours (GT Ref.)" may not be a reasonable comparison, since it provides ground truth geometric information in 6-view. I am not surprise it provides better generation results from the unseen view. The evaluation primarily focuses on scenarios where the retrieved reference is highly similar to the input image, which does not reflect the challenges of real-world applications. The marginal improvements in the quantitative results, even with ground truth references, suggest that the method's effectiveness may be limited. The comparison with ground truth references is not a fair evaluation of the method's practical performance.

5. (model usage) When there is considerable conflict between retrieved 3D objects and concept images (as line 878-879, it is actually very common), which side would the model follow the most? Potential users may want to see more examples of practical cases. And from a point of view as graphics designer, it will be better to provide a controlling nob for user to decide the extent of guidance from either side, rather let the model itself decides the extent. Right now, it is still uncontrollable. The lack of user control over the influence of the 3D reference is a significant limitation. The model's behavior in cases of conflict between the input image and the reference is not well-defined, and the absence of a mechanism for users to adjust the guidance strength makes the method less practical for real-world applications where specific artistic or design choices are needed.

6. (novelty) The novelty of the paper concentrated on the meta-controlnet and reference-based inference. However, given the weakness aforementioned, it may solve an restricted task or with limited contribution to the real problem, and compare to SOTAs in an unfair setting. Moreover, the reason to use diffusion models, and following reconstruction model may need more elaborations. The novelty of the proposed method is not fully justified given the limitations in the experimental setup and the lack of robustness to imperfect retrieval results. The paper needs to provide a more detailed explanation of the rationale behind using diffusion models and the subsequent reconstruction model, and how these choices contribute to the overall performance and novelty of the approach.

### Questions
Great work! I elaborate more based on weakness, and provide some suggestions and questions.

1. What is the main research goal of the paper? Is it to improve the quality of the 3D reconstruction on un-seen views (which indicates the output model should faithfully obey the input concept image), or it provides more customization freedom by given auxiliary 3D object reference (which indicates the output should lean to the given 3D objects.). Based on a full reviewing of the paper, my understand is the paper lean to the former one (correct me if I am wrong). So when there is conflict between retrieved 3D objects and concept images, which side would the model follow the most? If I am a graphics designer, a useful one will be a model doing either way, rather than a model-decided interpolation between two sides.
 
2. Is it a correct understand that the meta-controlnet is actually to learn a 3D texture mapping, which utilize the pixel-based texture in the concept image, map it to the retrieved 3D object surface based on 6-view CCMs? In that, the best way to phrase the contribution may like "using the front-view image as 2D texture guidance to generate unseen views given the 6-view CCM priors".

3. Follow Question-2, would you elaborate more about the role and reason to use diffusion model here? My understanding is, because there is conflict if we directly use 3D texture mapping using concept images and 6-view CCMs, so you let the diffusion process handle those conflicts. Any reason to exclude other pixel-based networks or traditional CG methods?

4. There are a lot of necessary details in the supplementary, like details of retrieving, dataset, etc. It will be better to move them into the main paper, even some of details may raise questions from reviewers. There is still a half-page blank now.

 I reserve the change of grades upon authors' responses to my reviewing.

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
This paper presents a new 3D generation approach that utilizes a reference 3D model to enhance the generation process. The method comprises three key components: (1) Meta-ControlNet (2) Dynamic Reference Routing (3) Self-Reference Augmentation. Experimental results demonstrate the effectiveness of this method in enhancing 3D generation quality, generalization ability, and controllability.

### Strengths
- Gathering information from a 3D reference model is straightforward.
- The evaluation of generation quality shows the effectiveness of the approach.
- The paper is well-written and easy to follow.

### Weaknesses
 - In the evaluation, only generation quality is assessed, with no evaluation of generation speed. For Phidias, retrieving information from the reference 3D model requires both 3D model retrieval and rendering of the canonical coordinate maps, which introduces additional latency. However, the paper does not report specific latency overheads. The lack of detailed timing breakdowns for each stage of the pipeline makes it difficult to assess the practical applicability of the method, especially when considering the overhead of 3D model retrieval and CCM rendering.
- From Table 3, the effectiveness of dynamic routing appears to be limited. The quantitative gains are marginal, raising questions about the necessity and computational expense of this component. It is unclear if the added complexity of dynamic routing justifies the small improvements observed in the experiments.

### Questions
- With the dynamic reference routing mechanism, the meta-ControlNet should be capable of handling inputs at various resolutions. Is the meta-ControlNet trained on images of different resolutions, or is it trained solely on the highest resolution and expected to generalize to lower resolutions?

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
3

### Summary
The paper introduces a generative model designed for creating 3D content from text, image, and 3D conditions with reference-augmented diffusion. Phidias aims to enhance the quality, generalization, and controllability of 3D generation by leveraging existing 3D models as references. The model integrates three key components: meta-ControlNet for dynamically adjusting conditioning strength, dynamic reference routing to address misalignments between input images and 3D references, and self-reference augmentations for self-supervised training with a progressive curriculum. 

These components collectively improve generative performance over existing methods, offering a unified framework for 3D generation using diverse inputs. Phidias enables various applications, including retrieval-augmented image-to-3D, text-to-3D, theme-aware 3D-to-3D generation, interactive 3D generation with coarse guidance, and high-fidelity 3D completion.

### Strengths
1. This paper proposes a dynamic reference routing approach. Recognizing that reference models do not perfectly correspond to the conceptual image, this paper utilize a feature pyramid to address this discrepancy. The motivation is that, it has been widely observed during the reverse diffusion process that the coarse structure of a target image is established in the early, high-noise timesteps, while finer details emerge progressively as the timesteps advance. This motivates to start with low-resolution reference CCMs at high noise levels.
2. This paper facilitates a range of downstream applications, including retrieval-augmented image-to-3D, text-to-3D, theme-aware 3D-to-3D generation, interactive 3D generation with coarse guidance, and high-fidelity 3D completion.

### Weaknesses
1. Dependence on Retrieval Quality: As stated by the author The performance of Phidias is contingent upon the quality and relevance of the retrieved 3D reference models, which may not always be optimal. This dependency introduces a potential bottleneck, as poor or irrelevant reference models could lead to suboptimal generation results. The method does not explicitly address scenarios where the retrieved reference is significantly different in shape or structure from the desired output, which could lead to artifacts or distortions in the generated 3D model. Further investigation is needed to understand the robustness of the method under such conditions.
2. Database Limitations: The current 3D database used for retrieval is limited in size, which could restrict the diversity and accuracy of reference models available for augmentation. Moreover, the model necessitates an additional dataset for inference, which may further restrict its applicability. The limited size of the database also restricts the generalization capabilities of the model, as it may not have encountered a wide enough range of 3D shapes and structures during training. This could lead to a bias towards the types of objects present in the database and limit the model's ability to generate novel or complex 3D shapes.

### Questions
1. In line 186, there is a missing citation regarding the canonical coordinate map. I believe this map is also referred to as the NOCS map, as introduced in reference [a].

[a] Normalized Object Coordinate Space for Category-Level 6D Object Pose and Size Estimation

### Soundness
3

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
4

### Summary
This paper introduces Phidias, a RAG-based framework for high-fidelity 3D content creation from multimodal inputs, including text, images, and 3D references. The framework introduces key innovations include Meta-ControlNet to dynamically modulate reference influence, dynamic reference routing to progressively refine outputs through a coarse-to-fine strategy, and self-reference augmentation to enhance generalization. Phidias enables sparse-view reconstruction, theme-based model variation, and user-interactive generation, demonstrating clear superiority over state-of-the-art approaches in both geometric precision and visual fidelity.

### Strengths
1. This paper presents a well-founded solution for multi-view generation, effectively addressing challenges such as the generation of unseen views and other ill-posed problems.
2. This paper is well-organized and clearly written, making it accessible to readers.

### Weaknesses
1. A significant weakness is the limited analysis of the retrieval mechanism for 3D references, which plays a critical role in guiding generation. The reliance on existing 3D models introduces a potential bottleneck, as Phidias’s performance may degrade if the retrieved references are irrelevant or of poor quality. Specifically, the paper lacks a detailed analysis of the feature space used for retrieval and how it impacts the quality of the retrieved 3D models. The paper should include a more thorough investigation into the robustness of the retrieval process under various conditions, such as noisy or incomplete 3D models in the database.
2. The control mechanism introduced via Meta-ControlNet is promising, but the paper does not delve deeply into more challenging settings. For example, scenarios where the input concept conflicts with the reference, or where the reference has significant structural differences from the input, are not adequately explored. The paper should include experiments that specifically test the limits of the control mechanism, such as cases where the reference object has different topology or geometric details compared to the desired output.

### Questions
1. why the point cloud for retrieval only contains 10K points, is it limitation stems from constraints imposed by Uni3D?
2. Why are the performences in Figure 14 so different from the results of the last row of figures in Figure 4? It looks like that some case's pose in Figure 4 doesn't match the input image, either.
3. The time and resource consumption for retrieval during each inference is not clearly stated

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new 3D generation method that introduces a meta-ControlNet and dynamic reference routing, leveraging user-provided 3D reference models and images to produce high-quality, controllable 3D object synthesis.

### Strengths
- The introduction of meta-ControlNet, combined with 3D reference models, provides strong guidance for the generation process, resulting in high-quality 3D outputs with excellent geometric consistency.

- As a reviewer familiar with this field, I believe that the combination of 3D reference models and images for generating 3D results has significant industrial value and could greatly inform future work in 4D generation as well.

- The method is simple, easy to understand, and the paper is clearly written.

### Weaknesses
 - Obtaining a reference 3D model can be quite challenging. Although this is valuable in certain application scenarios, it can be difficult to find appropriate reference 3D models in extreme cases. Specifically, the method's reliance on a high-quality, semantically aligned 3D model limits its applicability in scenarios where such models are not readily available or are significantly different from the desired output. This dependency introduces a practical bottleneck, as the quality of the generated 3D object is heavily influenced by the quality and relevance of the reference 3D model. I recommend that the authors add this limitation to the paper.

- While the strategy of combining ControlNet for generation appears straightforward, this could be criticized for lacking novelty. The core idea of using ControlNet for conditional generation is well-established, and the paper's application of this technique, while effective, does not introduce significant methodological innovation. The adaptation of ControlNet to incorporate 3D reference models, while practically useful, might be seen as an incremental step rather than a groundbreaking contribution. However, in my opinion, simplicity often leads to elegant and effective solutions, and I don’t consider this a reason for rejection.

### Questions
- I strongly support the task of combining reference 3D models with images for 3D generation as proposed in the paper, especially considering its relevance to the gaming industry and asset creation. Some related 3D generation methods discuss a texture editing task using complex images to guide coarse 3D object generation, which is highly relevant to this work. Could the authors provide some discussion or analysis on how to improve the method when there are significant differences between the reference image and the reference 3D model? This could be addressed in future work.

- I am inclined to accept this paper, as I also work on related tasks. Currently, I rate it as 6 but would likely increase the rating to 8 during the rebuttal phase.

### Soundness
3

### Presentation
3

### Contribution
3
