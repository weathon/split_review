# DICE: End-to-end Deformation Capture of Hand-Face Interactions from a Single Image

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Reconstructing 3D hand-face interactions with deformations from a single image is a challenging yet crucial task with broad applications in AR, VR, and gaming. The challenges stem from self-occlusions during single-view hand-face interactions, diverse spatial relationships between hands and face, complex deformations, and the ambiguity of the single-view setting. The first and only method for hand-face interaction recovery, Decaf~\cite{shimada2023decaf}, introduces a global fitting optimization guided by contact and deformation estimation networks trained on studio-collected data with 3D annotations. However, Decaf suffers from a time-consuming optimization process and limited generalization capability due to its reliance on 3D annotations of hand-face interaction data.
    To address these issues, we present \textit{\name}, the first end-to-end method for \underline{D}eformation-aware hand-face \underline{I}nteraction re\underline{C}ov\underline{E}ry from a single image. \name estimates the poses of hands and faces, contacts, and deformations simultaneously using a Transformer-based architecture. It features disentangling the regression of local deformation fields and global mesh vertex locations into two network branches, enhancing deformation and contact estimation for precise and robust hand-face mesh recovery. To improve generalizability, we propose a weakly-supervised training approach that augments the training set using in-the-wild images \textit{without} 3D ground-truth annotations, employing the depths of 2D keypoints estimated by off-the-shelf models and adversarial priors of poses for supervision.
    Our experiments demonstrate that \name achieves state-of-the-art performance on a standard benchmark and in-the-wild data in terms of accuracy and physical plausibility. Additionally, our method operates at an interactive rate (20 fps) on an Nvidia 4090 GPU, whereas Decaf requires more than 15 seconds for a single image. Our code will be publicly available upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a model for the simultaneous reconstruction of face and hand meshes from a single image, based on previous work and annotated data from Shimada et al. (DECAF). The model employs a Transformer-based image encoder to extract keypoints for face and hand through separate streams, utilizing parametric models for reconstruction. Designed for images that contain both a face and a hand, the approach extends training with unannotated data by leveraging a diffusion-based depth estimation model (Ke et al., 2024) to guide mesh reconstruction. After reconstructing the face and hand mesh, the depth maps are computed and aligned with depth estimates from the diffusion model. The model is trained with four types of losses: mesh loss and contact-point loss, similar to those in DECAF, as well as depth loss and adversarial loss, which support the depth supervision process. Experimental results show improvements over previous work for face-hand interaction images.

### Strengths
-- The use of depth supervision for weakly-supervised training in mesh reconstruction is innovative and potentially impactful for similar tasks.

### Weaknesses
 -- The model is focused specifically on face-hand images, which may limit its relevance to the broader computer vision community. The emphasis on this specific interaction appears to be largely application-driven, leaving questions about its applicability to other computer vision tasks.

-- Although the use of depth supervision in training mesh models appears novel, it leverages known components, which slightly reduces the overall technical novelty.

### Questions
Is it possible to apply depth supervision to other reconstruction tasks? What makes it particularly suited to the hand-face problem, aside from data availability? Could this approach be more broadly relevant to visual tasks involving contact points between two objects? I wonder if this could be explored further.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel method for reconstructing 3D hand-face interactions with deformations from a single image. The authors present DICE, a Transformer-based architecture that simultaneously estimates hand and face poses, contacts, and deformations. A key feature of DICE is its ability to disentangle local deformation fields from global mesh vertex locations into two separate network branches, which enhances the accuracy of deformation and contact estimation for precise hand-face mesh recovery. Additionally, the method utilizes a weakly-supervised training approach with in-the-wild images that lack 3D ground-truth annotations, thereby improving the model's generalizability. Experiments show state-of-the-art performance in terms of accuracy and physical plausibility, along with interactive inference rates on modern GPUs.

### Strengths
* The motivation is compelling. DICE provides the first end-to-end learning-based method for capturing hand-face interactions and deformations from a single image, filling a significant gap in the field.
* Good experimental results. The paper claims that DICE achieves superior reconstruction quality compared to baseline methods while operating at an interactive rate (20 fps), which is crucial for real-time applications.
* Technically sound. The weakly-supervised training scheme using in-the-wild images enhances the model's ability to generalize beyond the constraints of studio-collected data.

### Weaknesses
 * DICE is better than optimization-based methods like Decaf. However, there is a notable gap in physics plausibility metrics compared to Decaf. Can the authors provide a clearer explanation? I wonder if it struggles to balance reconstruction accuracy and physics plausibility.
* In Table 3, using in-the-wild data negatively impacts the F-score. The authors should provide a clearer explanation.
* The novelty is limited. The techniques used in this paper are commonly employed in the community.
* The authors are encouraged to include more discussion on failure cases.
* Some results are not convincing. In Figure 4, the head reconstruction of Decaf is noticeably better than that of the authors' method for the third sample from in-the-wild data.
* Some videos should be included to demonstrate real-time capability.

### Questions
Explain the notable gap in Decaf regarding physics plausibility metrics.

### Soundness
3

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
5

### Summary
### Motivation
- Modeling the geometry and interactions of human hands and face from a monocular image is an underexplored tasks in 3DCV, with broad applications (AR/VR, motion capture, etc.).
- To the best of the authors' knowledge (and mine), only one prior method tackle this problem in an exhaustive and end-to-end manner, Decaf [Shimada et al., 2023]. This seminal work is however optimization-based, and therefore too slow for interactive use.

### Contributions
- The authors thus introduce DICE, which performs the above-mentioned task in a forward-inference manner. The method relies on a Transformer-based network, with two branches separately tackling the regression of (a) the hand+face geometry and (b) the face deformation caused by hand contact.
- Furthermore, the authors introduce a weak supervision to expand training to in-the-wild-ish images (2D keypoint annotations are still needed, though not 3D ones). Depth supervision is also enabled on such data by integrating a pre-trained monocular depth estimator to generate pseudo ground-truth. Predicted meshes are projected into depth images using a differentiable renderer for comparison.


### Results
- Experiments on the Decaf benchmark show that DICE outperforms prior art in terms of 3D reconstruction accuracy and provides competitive runtime on par with regression-based baselines (~0.1s, whereas Decaf needs ~15s). Unlike prior art though, the authors did not fully disclose their results on physics-plausibility relating to touchness and collision.
- An ablation study, as well as plenty of convincing qualitative results, are also provided. 

### Relevance
- This paper addresses a relevant yet under-explored 3DCV task. The community would benefit from this iteration over the seminal Decaf.

### Strengths
_(somewhat ordered from most to least important)_

### S1. Clear Explanations and Decent Reproducibility
- The Methodology is clear, thoroughly explained, and overall well-formalized. 
- While the actual implementation has not been provided, an expert in the art should be able to re-implement this work.
- The paper is also well illustrated and easy to follow (pipeline figures + qualitative results).
- Limitations are well-discussed, with failure cases provided (Appendix D).

### S3. Convincing Evaluation
- The evaluation is also clear, comprehensive, and well presented (e.g., highlighting optimization-based vs. regression-based methods in Table 1, providing various qualitative results, etc.).
- The proposed DICE method outperforms the SOTA on 3D reconstruction metrics, at a competitive running time.
- Qualitative results and the ablation study are also convincing. In-the-wild examples help illustrate the generalizability of the method.

### S3. End-to-End Solution Targeting an Under-explored Task
- As mentioned above, this paper is seemingly only the second (after Decaf [Shimada et al., 2023]) to address the joint modeling of hand/face geometry and interaction in a comprehensive, end-to-end manner. As such, it would be valuable to the community.
- While the proposed method mostly relies on existing components (CNN-backbone, Transformer processing, weak supervision using large monocular depth regressor, etc.), it holds value as a well-designed end-to-end system.

### Weaknesses
### W1. Limited Technical Novelty
- The proposed solution has value as an end-to-end system tackling an under-explored task, but its technical novelty is limited.
- The main/only technical contribution claimed by the authors are their weak depth supervision module, relying on a large/foundation model [L110-112]. There might be some novelty in applying such a model to this specific task (e.g., in terms of processing the depth-map predictions to supervise the facial keypoints), but the underlying idea of leveraging a large monocular depth model for weak supervision is not novel. The specific method of using keypoint-to-keypoint correspondence for depth supervision, while potentially effective, lacks a thorough justification of its advantages over pixel-to-pixel approaches, especially given the availability of differentiable renderers. The paper does not sufficiently explore or compare the performance of these different depth supervision strategies.
- Most of the loss functions appear borrowed from Decaf [Shimada et al., 2023], even though this is not made obvious in the paper (both in Section 3.3. and in Appendix C). The lack of explicit acknowledgement and comparison to Decaf's loss terms makes it difficult to assess the true contribution of the proposed method.



### W2. Lack of Insight w.r.t. Physics Metrics
- Unlike Decaf, the authors here did not report all physics-related metrics (non-collision / touchness accuracy). The absence of these metrics makes it difficult to fully evaluate the plausibility of the generated hand-face interactions. The F-score alone, while useful, does not provide a complete picture of the collision and touch accuracy.
- The authors could provide more insight in terms of the challenges faced by regression-based methods for accurate modeling, compared to optimization-based solutions. The paper lacks a detailed analysis of why regression-based methods struggle with physical plausibility, particularly in comparison to optimization-based approaches that iteratively refine the solution. A discussion of the inherent limitations of single-pass regression for such a complex task is needed.
- Similarly, Table 2 and corresponding paragraph [L417-421] lack proper insight/description. The superiority of DICE is not as obvious as claimed. The discussion around the F-score, while present, does not sufficiently explain the underlying trade-offs between precision and recall in the context of contact estimation. A more detailed analysis of the results, including potential failure modes, is necessary.

### W3. Somewhat Limited Comparison to Prior Art
- The authors compare their method to 3 other solutions: Decaf [Shimada et al., 2023] (most relevant as it also targets hand/face interaction), PIXIE [Feng et al., 2021a] and METRO [Lin et al., 2021a)] (both originally developed for full-body regression), and a baseline/benchmark solution [Lugaresi et al., 2019; Li et al., 2017)] (composed of two independent hand-only and face-only models). While the literature does indeed lack in prior art focusing on hand/face interaction, more baseline methods could have been considered, e.g., mixing other single-target methods (MinimalHand , RingNet, FastMETRO, etc.). This could have further highlighted the benefits on modeling both body parts jointly. The choice of baselines, while following Decaf's protocol, could be expanded to include more recent and relevant single-target methods, which would provide a more comprehensive evaluation of the proposed approach.
- To counterbalance this "weakness", it should be noted that the aforementioned set of prior methods have been entirely borrowed from Decaf, so the authors here stuck to Decaf's protocol, which is fair. More comparisons could make the paper stronger.

### W4. Minor Remarks
- Societal impact is not discussed, showing a lack of self-reflection. While positive applications are actually listed in the Introduction (e.g., benefits to AR/VR and gaming industry), a variety of negative applications can also come to mind: surveillance (appearance + gesture), animatable deepfakes, etc. Discussions on data fairness/bias are also always relevant when it comes to human-modeling solutions.

### Questions
_see **Weaknesses** for key questions/remarks._


### Q1. Hand Rigidity $\rightarrow$ Applicability of CONTHO
- One limitation of this method, as well as prior Decaf, is to only consider face deformation and ignore hand one. While the hands are definitely _stiffer_, ignoring their soft tissues can yield incorrect results in some cases (e.g., hand pressed against forehead). Moreover, by considering the hand as piece-wise rigid, the target task becomes similar to the much less under-explored domain of human/object interaction modeling (i.e., both tasks can be expressed as modeling 3D non-rigid/rigid interactions). It seems that recent solutions such as CONTHO [Nam et al., 2024] could be adapted to face/hand reconstruction. What is the authors' position w.r.t. these adjacent methods? How would the authors differentiate their own approach?

### Soundness
3

### Presentation
3

### Contribution
2
