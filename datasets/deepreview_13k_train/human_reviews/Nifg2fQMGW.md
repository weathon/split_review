# UniEdit: A Unified Tuning-Free Framework for Video Motion and Appearance Editing

- Decision: Reject
- Scores: 5, 8, 5, 1

## Abstract
Recent advances in text-guided video editing have showcased promising results in appearance editing (e.g., stylization). However, video motion editing in the temporal dimension (e.g., from eating to waving), which distinguishes video editing from image editing, is underexplored. In this work, we present UniEdit, a tuning-free framework that supports both video motion and appearance editing by harnessing the power of a pre-trained text-to-video generator within an inversion-then-generation framework.
To realize motion editing while preserving source video content, based on the insights that temporal and spatial self-attention layers encode inter-frame and intra-frame dependency respectively, we introduce auxiliary motion-reference and reconstruction branches to produce text-guided motion and source features respectively. The obtained features are then injected into the main editing path via temporal and spatial self-attention layers.
Extensive experiments demonstrate that UniEdit covers video motion editing and various appearance editing scenarios, and surpasses the state-of-the-art methods. Our code will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a method to simultaneously edit motion and appearance through text guidance. Unlike previous approaches that required fine-tuning a pretrained generator model for the target video, the proposed UniEdit method is tuning-free. It utilizes the temporal self-attention layer within the generator to naturally express motion. Additionally, the spatial self-attention layer preserves the regions that are not being edited. Furthermore, the method ensures that the spatial structure of the video remains intact during appearance editing.

### Strengths
The method can be applied to various Text-to-Video models, clearly stating the intended goal of simultaneously editing the content's motion and appearance.
The paper presents results applied to multiple Text-to-Video models. Experiments using various prompts demonstrate that this method is not limited to specific prompts.
The video quality available on the project page is excellent, and the experimental results are easy to understand.
Videos generated using UniEdit outperformed existing methods in terms of CLIP score, Frame Quality, and Temporal Quality.

### Weaknesses
The user study involved only 10 participants, which may lead to highly subjective results. Including subjective results in the main performance table could confuse readers, and it would be beneficial to either evaluate with more participants or clearly indicate near the table that the results may be subjective due to the limited number of participants.
The subjective evaluation from only 10 participants being included in the quantitative results could cause confusion among readers.

While the paper demonstrates performance improvements, the proposed method feels like an incremental enhancement over existing techniques. Specifically:
- The approach of injecting motion text seems like a minor modification rather than a significant technical breakthrough.
- Compared to existing methods that inject optical flow information or motion trajectories, it is unclear if providing a motion prompt offers greater control in practice.

The contribution of this paper appears to rely on manipulating spatial-temporal attention—a concept already widely explored in video editing—using a slightly modified approach. Some examples of related works that adopt similar attention-based techniques for video editing include:
- Video-P2P: Video Editing with Cross-attention Control
- Tune-A-Video: One-Shot Tuning of Image Diffusion Models for Text-to-Video Generation
- Zero-Shot Video Editing Using Off-The-Shelf Image Diffusion Models
- FateZero: Fusing Attentions for Zero-shot Text-based Video Editing
- Edit-A-Video: Single Video Editing with Object-Aware Consistency
- FLATTEN: Optical Flow-guided Attention for Consistent Text-to-Video Editing

Given these existing methods, the incremental nature of the proposed approach raises questions about its originality and its position within the broader landscape of video editing research.

I agree that 16 frames are too short to demonstrate practical utility, especially for long video editing tasks. Long video editing is an essential capability for many real-world applications, and addressing this limitation would significantly enhance the impact and applicability of your method.

While the emphasis on being tuning-free is appreciated, the limitations imposed by the baseline, particularly in extending the method to editability and long video generation, suggest that incorporating a fine-tuned model might be necessary. Additionally, the spatial and temporal attention mechanisms included in the proposed method have become standard in many video editing works. While such approaches were impactful in the early stages of video editing research, the field has progressed significantly. Thus, adopting more advanced, fine-tuning-based methods, such as those exemplified in recent works like *ReVideo: Remake a Video with Motion and Content Control* (NeurIPS 2024), seems necessary to achieve broader applicability.

### Questions
Please check if it is reasonable to have conducted the experiment with 10 subjects.

### Soundness
3

### Presentation
3

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
UniEdit presents a novel approach to text-guided video editing, utilizing a tuning-free framework that leverages the capabilities of pre-trained text-to-video (T2V) diffusion models. The key strength of UniEdit lies in its ability to perform both motion and appearance editing within a unified architecture. This is a significant advancement compared to prior methods, which often focus on either motion or appearance editing, but not both. The core idea behind UniEdit is to invert the source video into the latent space of a pre-trained T2V model, and then guide the generation process using the target text prompt and auxiliary branches that control motion and appearance.

### Strengths
- **Unified Framework for Motion and Appearance Editing**: UniEdit effectively addresses a key challenge in video editing by providing a single framework that can handle both motion and appearance modifications. This is achieved by leveraging the inherent properties of spatial and temporal self-attention layers in the T2V model. The motion-reference branch, conditioned on the target prompt, injects motion features into the temporal self-attention layers, enabling text-guided motion changes. The reconstruction branch focuses on preserving source content by injecting features into the spatial self-attention layers.

- **Zero-Shot Editing Capability**: UniEdit operates in a tuning-free manner, meaning it doesn't require fine-tuning the base T2V model for each new video or editing task. This makes it highly efficient and user-friendly, as it avoids the computational cost and complexity associated with model training.

- **Emphasis on Temporal Consistency:** Maintaining temporal consistency is crucial for high-quality video editing. UniEdit tackles this challenge by injecting features from the reconstruction branch into the spatial self-attention layers, which helps preserve the content and structure of the source video. The use of mask-guided coordination further enhances the consistency of unedited areas.

### Weaknesses
1. The problem is challenging, and I believe this paper only partially addresses it. The editing capabilities need to be more clearly defined. For example, are all text prompts representing motion control or appearance control feasible? The scope requires further clarification. The inherent ambiguity of language and the complexity of video editing tasks make it practically impossible to guarantee success for every possible textual input.

**Defining Boundaries and Constraints:** To enhance clarity regarding its scope, the UniEdit paper should clearly state:

- **Types of Edits Supported:** Specify the categories of motion and appearance edits that UniEdit is designed to handle effectively.

- **Limitations in Prompt Complexity:** Provide guidelines or examples of text prompts that might pose challenges for UniEdit, particularly those involving complex scenes or multiple simultaneous edits.

- **Known Failure Cases:** Discuss specific scenarios where UniEdit is known to perform poorly, offering insights into the reasons for these limitations.

2. UniEdit's core techniques are indeed inspired by existing approaches:
   - **Auxiliary Branches:** The concept of using auxiliary branches for specific tasks, such as reconstruction or motion guidance, is not entirely new.
   - **Feature Injection via Self-Attention:** Injecting features into specific layers of a neural network, especially within attention mechanisms, is a common practice in various image and video editing tasks.
   - **Temporal and Spatial Self-Attention:** The observation that temporal self-attention layers encode inter-frame dependencies, while spatial self-attention layers capture intra-frame information, is a widely recognized principle reported in other works like I2VEdit (https://i2vedit.github.io/) for diffusion-based methods and SIFA (https://github.com/FuchenUSTC/SIFA) for other video editing tasks.

   While UniEdit's core techniques are not entirely novel, **the integration and adaptation of these mechanisms for tuning-free video motion editing demonstrate a degree of innovation.**

3. The improvements, while statistically significant, do not represent a leap in performance but rather a refinement of existing techniques. For instance, UniEdit's performance on Frame Quality and Temporal Quality metrics surpasses competing methods like TokenFlow and Rerender, but the margins are relatively modest (e.g., a 1-2% improvement in some metrics).

4. As the authors have pointed out, UniEdit has a **performance ceiling** when performing both motion and appearance editing simultaneously and struggles with complex scenes.

5. **Missing Critical Baseline:** ReVideo (https://mc-e.github.io/project/ReVideo/) should be included as a baseline. ReVideo's focus on remaking videos with control over both motion and content aligns well with UniEdit's capabilities. A direct comparison would reveal their strengths and weaknesses in tasks such as object replacement, style transfer, and motion modification.

   Including additional works for comparison will further strengthen this paper. 

  In addition, a discussion with the following related works is beneficial:
   - **AnyV2V:** Its compatibility with various image editing methods and emphasis on simplicity and consistency present an interesting comparison point for UniEdit.
   - **I2VEdit:** Comparing with I2VEdit would reveal the advantages and disadvantages of using an edited first frame versus direct text guidance for video editing. This comparison could be particularly insightful for tasks involving local edits, global style transfer, identity manipulation, and subject customization. The temporal consistency of I2VEdit appears to be quite robust.
   - **FLATTEN:** Comparing FLATTEN to UniEdit would showcase the differences between explicitly incorporating optical flow information and UniEdit's approach to motion injection.

6. **Metric Coverage:** The evaluation relies heavily on CLIP scores and user preferences. While these metrics are valuable, the absence of more comprehensive metrics (e.g., temporal coherence measures beyond flickering, user engagement metrics) limits the robustness of the evaluation.
   - **Flow Warping Error (Ewarp):** This metric can be used to assess visual consistency by comparing the edited video frames warped according to the estimated optical flow of the source video.
   - **Frame Variance Metric for Motion Detection (FVMD):** This may provide a more objective measure of how well the model preserves motion consistency across frames.

7. The evaluation dataset could include BalanceCC if possible.

8. **Sensitivity Analysis** can be more detailed:
   - **Sensitivity to Injection Steps:** The quantitative analysis clearly shows that the choice of injection steps influences the quality and consistency of the output.
   - **Sensitivity to Blend Layers and Steps:** The qualitative exploration indicates a trade-off between stylization and fidelity controlled by the blend layers and steps. This suggests a need for adjustment based on the desired outcome.

9. The related works are primarily categorized by broad topics (e.g., video generation, video editing) rather than by the specific innovations relevant to UniEdit (e.g., tuning-free frameworks, self-attention manipulation). This top-down organization makes it harder to discern how UniEdit differentiates itself from existing methods.

### Questions
Please refer to the weaknesses section for my questions. I may revise my rating based on the authors' rebuttal.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose UniEdit, addressing the task of video motion and appearance editing using pre-trained video diffusion models (VDMs) in a united and tuning-free manner. Specifically, they apply the common "inversion-and-generation" with two innovative auxiliary branches, i.e., the reconstruction branch for content preservation and the motion-reference branch for motion editing, in addition to the main editing path. The appearance editing, motion editing and structure preservation are realized by swapping attention features (QKV) in specific types and depth of attention layers, and denoising steps as well. UniEdit is compared with previous zero-shot/tuning-free methods and outperforms them both quantitatively and qualitatively.

### Strengths
- The paper demonstrates good clarity in writing, making it easy for readers to follow the flow of ideas.
- The paper is well-motivated, offering various types of video editing while preserving non-target properties using a unified framework.
- The design of attention replacement for appearance, structure, and motion editing is technically sound, leveraging the insights and functionality of spatial and temporal self-attention, respectively.
- The paper and the auxiliary material show impressive editing results produced with their framework with substantial improvement on existing baselines, especially in temporal coherence.

### Weaknesses
 - The authors claim in L217 that "better tackle source video with large dynamics". However, most visual examples are with small motion magnitudes. Does the model struggle with appearance and motion editing in videos with larger dynamics? Temporal inconsistencies are noticeable in videos with large motion (see Fig G.1). Specifically, the "cat" to "dog" example shows a clear breakdown in temporal coherence during the dog's head turn, suggesting the method struggles with significant motion changes.
- The authors claim in L312 that "UniEdit is not limited to specific video diffusion models", which is inaccurate. The proposed framework depends on the separate spatial and temporal attention design of video diffusion models, which is incompatible with full 3D attention DiT-based video generators. And 3D full attention is increasingly being proven to be more effective [1]. This reliance on a specific attention architecture limits the general applicability of the method to a subset of video diffusion models, excluding those with fully integrated 3D attention mechanisms.
- This work still follows the common "inversion-and-genertation" paradigm, potentially performing better on generated videos but struggling with out-of-domain real videos. The inversion process, while effective on synthetic data, may not accurately capture the complexities of real-world video content, leading to potential artifacts or inconsistencies during editing. The reliance on this paradigm raises questions about the method's robustness and generalizability to diverse video sources.
- In Fig.4 (bottom-right case), motion-editing results show background changes, such as alterations in the lawn. This indicates a lack of precise control over the editing process, where changes intended for the foreground object inadvertently affect the background, highlighting a potential limitation in the method's ability to isolate edits to specific regions.
- The user study involved an insufficient number of participants (only 10), making it difficult to support the conclusions effectively with robust experimental results. A larger, more diverse participant pool would be necessary to validate the subjective quality of the editing results.

Minor concerns:
- [Clarity] Consider including a note below the table or in the caption indicating that higher values are better.

### Questions
- [Ablation study] Why does the *content preservation* improve *textual alignment* a lot in Table 2?
- I believe different methods have their own "success rate" in generation. Is there a way to measure this rate for fair comparison, beyond just showcasing several visual examples? Additionally, how to know if this tuning-free method really works or not (to what degree), compared to potential methods with large-scale training?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
Recent advances in text-guided video editing have showcased promising results in appearance editing (e.g., stylization). However, video motion editing in the temporal dimension (e.g., from eating to waving), which distinguishes video editing from image editing, is underexplored. In this work, They present UniEdit, a tuning-free framework that supports both video motion and appearance editing by harnessing the power of a pre-trained text-to-video generator within an inversionthen-generation framework. However, this paper seems not latest version. Some new sota approaches are not included and had a comparison.

### Strengths
In this work, they present UniEdit, a tuning-free framework that supports both video motion and appearance editing by harnessing the power of a pre-trained text-to-video generator within an inversionthen-generation framework. To realize motion editing while preserving source video content, based on the insights that temporal and spatial self-attention layers encode inter-frame and intra-frame dependency respectively, they introduce auxiliary motion-reference and reconstruction branches to produce text-guided motion and source features respectively. The obtained features are then injected into the main editing path via temporal and spatial self-attention layers.

### Weaknesses
 - Novelty.  Using ReferenceNet is not a novel approach in video generation. What is the difference between yours and previous work.
- Overclaim.  "UniEdit represents a pioneering leap in text-guided, tuning-free video motion editing."  Why this work is a pioneering leap? 
- Lack of comparison. Many new works, such as Revideo, COVE , accepted by NeurIPS 2024, are all not included in this paper. 
- Long video editing,  All results are only 16 frames，which is too short.
- Motion Editing. It seems that all motion are similar. How to editing it ?
- Inconsistency.  Such as cat -> dog. The consistency of the head turn is problematic and exhibits sudden changes.

### Questions
See weaknesses

### Soundness
2

### Presentation
2

### Contribution
2
