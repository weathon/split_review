# Flex3D: Feed-Forward 3D Generation with Flexible Reconstruction Model and Input View Curation

- Decision: Reject
- Scores: 5, 6, 5, 6, 6, 5

## Abstract
Generating high-quality 3D content from text, single images, or sparse view images remains a challenging task with broad applications.
Existing methods typically employ multi-view diffusion models to synthesize multi-view images, followed by a feed-forward process for 3D reconstruction.
However, these approaches are often constrained by a small and fixed number of input views, limiting their ability to capture diverse viewpoints and, even worse, leading to suboptimal generation results if the synthesized views are of poor quality.
To address these limitations, we propose \method, a novel two-stage framework capable of leveraging an arbitrary number of high-quality input views.
The first stage consists of a candidate view generation and curation pipeline.
We employ a fine-tuned multi-view image diffusion model and a video diffusion model to generate a pool of candidate views, enabling a rich representation of the target 3D object.
Subsequently, a view selection pipeline filters these views based on quality and consistency, ensuring that only the high-quality and reliable views are used for reconstruction.
In the second stage, the curated views are fed into a Flexible Reconstruction Model (\netname), built upon a transformer architecture that can effectively process an arbitrary number of inputs.
\netname directly outputs 3D Gaussian points leveraging a tri-plane representation, enabling efficient and detailed 3D generation.
Through extensive exploration of design and training strategies, we optimize \netname to achieve superior performance in both reconstruction and generation tasks.
Our results demonstrate that \method achieves state-of-the-art performance, with a user study winning rate of over 92\% in 3D generation tasks when compared to several of the latest feed-forward 3D generative models.

See \href{https://junlinhan.io/projects/flex3d/}{\textcolor{red}{\tt\small{project page}}} for more immersive 3D results.
}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work focuses on feed-forward 3d generation. Following previous work, this paper adopts a synthesis-then-reconstruction method, where a multi-view diffusion generates multiple images at different camera views, and a regression model then reconstructs 3d representation based on multi-view images. The main contribution the author claimed is the view selection trick that curates generated multi-view images based on the back-view quality and consistency. Also, the proposed method uses 3DGS as a 3d representation for rendering efficiency.

### Strengths
- The writing is well-organized and easy to follow.
- This work proposed to select condition images from the generated multi-view images based on the quality, thereby improving the 3d reconstruction quality.

### Weaknesses
 - This work basically follows previous work like Instant3D and replaces the triplane NeRF representation with triplane Gaussian (as in [1]). The main contribution thus lies in the candidate view selection. It is evident that the reconstruction quality would improve with better generated multi-view images, but the key is how to define 'better' and automatically filter the better images. The proposed method adopts SVM trained with 2,000 manually labeled data to select back view, but the paper does not describe how to label the data and does not give the criterion. Also, 2,000 images are small and restricted by the bias of labelers. This would lead to very biased and uninterpretable labels for training a good classifier. How about the success rate of the selection model? How to determine whether it is a good classification? There is a lack of sufficient analysis and experiments that support the claim. There are similar concerns to the consistency selection model. Why do you choose manually crafted rules for selection, like using DINO, SVM, LOFTER? Are they the best choices? Any insights? 
- Based on the aforementioned comment, I would suggest the authors to compare with automatic selection with large multimodal model like GPT4V. It is straightforward to give the grid of images to the large model, and ask it to select images. Would it be better than the proposed method?
- There is a lack of comparison with diffusion-based baselines that predict 3d via 3d diffusion or 3d dit directly.
- The proposed method comprises two stages. Which stage does the improvement mainly come from? multi-view generation and selection, or flex reconstruction model? In Fig.4, and table 1, do the baselines use the same multi-view images as the proposed method? I would suggest evaluating two stages separately. Specifically, you may apply the view selection to baseline methods to check whether there are consistent improvements. Also, use the same selected multi-view images to evaluate different reconstruction model.
- For ablation results like table 3,4,5, do you use Blender rendered images or generated images as the multi-view condition? Could the data simulation address the domain gap of data? How about metrics in table 5 using GT multi-view images rather than generated multi-view images?

### Questions
How many views are used for calculation metrics for Flex3d in Table 1? More than baseline methods? If so, is the comparison fair?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Flex3D is a novel two-stage framework for generating high-quality 3D content from text prompts, single images, or sparse-view images. In the first stage, it generates a diverse pool of candidate views using fine-tuned multi-view image diffusion models and video diffusion models. A view selection pipeline then filters these views based on quality and consistency. The second stage employs the FlexRM, a transformer-based architecture capable of processing an arbitrary number of input views with varying viewpoints. FlexRM combines tri-plane features with 3D Gaussian Splatting to produce detailed 3D Gaussian representations. Experimental results demonstrate that Flex3D outperforms state-of-the-art methods in both 3D reconstruction and generation tasks.

### Strengths
The paper is well-organized, with a clear delineation of the contributions and methodologies. The progression from problem identification to solution proposal is logical and easy to follow.

The key contributions of this paper are two-fold, which seem to be of effectiveness according to the experimental analysis:
1. candidate view generation and curation: Introduction of a multi-view generation strategy that produces a diverse set of candidate views from varying azimuth and elevation angles, followed by a selection process that filters views based on quality and consistency.
2. flexible reconstruction model (FlexRM): Development of a robust 3D reconstruction network capable of ingesting an arbitrary number of input views with varying viewpoints. FlexRM efficiently processes these views to output high-quality 3D Gaussian representations using a combination of tri-plane features and 3D Gaussian Splatting.

The authors conduct detailed ablation studies to validate the effectiveness of each component of their proposed framework.

### Weaknesses
My major concerns lay in the following several aspects. If some of the may concerns can be solved during the discussion section, I would like to raise the final score.

1. The paper does not specify whether the proposed method has been tested across various datasets or object categories. Evaluating Flex3D on diverse and challenging datasets would demonstrate its generalizability and robustness to different types of input data.

2. The paper evaluates performance using 2D image-based metrics such as PSNR, SSIM, LPIPS, and CLIP image similarity. While these metrics are informative, they do not fully capture the geometric accuracy and consistency of the 3D reconstructions. Incorporating 3D-specific metrics, such as Chamfer Distance or Earth Mover's Distance, would provide a more comprehensive assessment of the reconstructed 3D models' quality.

3. The user study conducted to evaluate the overall quality of the generated content lacks detailed methodology. Information regarding participant demographics, selection criteria, and statistical significance testing is absent. Providing these details would enhance the credibility of the user study findings.

### Questions
See the weakness section.

### Soundness
2

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
This paper proposes Flex3D, a method for feed-forward 3D generation. The method is split into two stages, i.e., multi-view generation and subsequent conversion of these generated multi-view images into 3D Gaussians for arbitrary view rendering. The first stage uses a multi-view image model and a image-to-video model to generate multiple viewpoints of a scene. The second stage uses a LRM-like pipeline to generate 3D Gaussians. The results show competitive quality compared to previous works.

UPDATE: given the additional experiments provided in the rebuttal that show how the proposed tweaks can improve other models, I go back from "reject" to my original rating of "marginally below". This partially resolves the closed-source issue (in response to [this](https://openreview.net/forum?id=2vaTZH31oR&noteId=nksfmi6e00). Nonetheless, the extent of contributions is still small, and this remains a borderline paper.

### Strengths
- Visual quality: the results look good and similar/slightly better than previous works
- Back view quality assessment: using a multi-view video classifier to tackle typically lower back-facing views generation seems interesting, even though little information is provided.

### Weaknesses
 - There is a general lack of technical insights
- FlexRM stage already proposed (Stage 2): Previous works [1,2] in feed-forward 3D generation already proposed last year to decode triplane features into 3D Gaussian attributes. The specific method of decoding, while potentially different, does not present a significant departure from existing techniques.
- Multi-view image generation already proposed (Stage 1): MVDream [3] and follow-up works already turn pre-trained image generators into multi-view generators. The use of existing multi-view generation techniques without substantial modification or novel application limits the contribution.
- Multi-view image generation with video model already proposed (Stage 1): Previous works [4,5] already proposed to use video generators for novel view synthesis given an image as an input. The approach here appears to be a direct application of these existing methods.
- Conditioning with camera already proposed and marginal (Stage 2): previous works such as SV3D [5] already proposed to condition the generation with camera matrices. In this work it is used in the image encoder DINO. However, the ablation in Tab. 3 shows that the model with “No stronger camera cond” only shows very marginal improvement?
- Imperfect data simulation with marginal improvements (Stage 2): the data simulation part in the method section sounds rather complicated and unnecessary given its little impact in Tab. 5? Similar to the camera conditioning, the metrics only show very marginal improvement?
- No computational cost analysis: The method seems very complicated, it would be good to compare training and inference time against previous works.

### Questions
I don’t really have technical questions, and it is rather unlikely that I will change my score (I hesitated between 5:weak reject and 3:reject). 
This is because, while the quality of writing is decent and results marginally improve on the state of the art, the paper reads more like a white-paper for re-engineering a large-scale system rather than answering any specific scientific question.

What are the **insights** that were not proposed before that could be adopted in follow-up research?
Or is this work just about combining previous techniques with the sole purpose of getting (very marginal) improvements to metrics?

And given the metrics improvements are so marginal (as revealed by the ablations), why does all of this complication really matter?
Perhaps the small improvement in metrics does not reflect a drastic improvement in qualitative performance… but I wasn’t able to see a drastic improvement in qualitative results on the supplementary website… so I am having a very hard time to consider all the proposed complications to be truly worth it.

For a system paper that needs 128 A100 to train, I would have expected a **much** larger improvement in performance to justify a white-paper as a technical conference paper. The story would be different if the pre-trained model and/or code+data was released, and the method tested on public benchmarks.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a robust feedforward 3D generation pipeline to address inconsistent multiview inputs. Specifically, it fine-tunes multiview and video diffusion models to generate diverse viewing angles and incorporates a key view selection module using an existing feature-matching model. This approach ensures that high-quality and consistent views are chosen for 3D reconstruction.

### Strengths
1. Logical Model Design and Well-organized Writing. Good logical model design and clarity of writing. It effectively identifies the limitations of existing models and systematically addresses them step by step, making the problem-solving process easy for readers to follow. This demonstrates a well-structured research design, facilitating readers’ comprehension of the methodology and approach.

2. Practicality. The techniques for multi-view generation, view selection, and robustness through data augmentation provide substantial applicability and reusability. The paper builds on an existing Instant3D architecture and employs a systemically optimized approach, suggesting high utility. It would be beneficial If authors release all the pre-trained models.

### Weaknesses
1. Incremental technical improvement. The suggested pipeline combines and optimizes existing techniques rather than introducing innovative algorithms. The approach appears to rely heavily on integrating and optimizing pre-existing technologies rather than presenting a novel concept or unique contribution. Specifically, the core idea of using a diffusion model for multi-view generation, followed by a reconstruction model, is not new. The novelty is primarily in the specific combination and optimization of these components, such as the view selection module and the fine-tuning strategy, rather than a fundamental algorithmic breakthrough.

2. Complex Pipeline Requiring Extensive Fine-Tuning and Training. While the pipeline is logically structured, it is complex and demands extensive fine-tuning and training. Five rounds of fine-tuning are required. Initial multi-view generation involves data creation and two rounds of fine-tuning. The view selection step also utilizes existing models to build a new system module. Subsequently, the feed-forward model undergoes two additional rounds of fine-tuning, and the process includes one more phase of training with data augmentation. This level of complexity could hinder full implementation and reproducibility. The multiple stages of fine-tuning, each with its own hyperparameters, make the pipeline sensitive to parameter choices and difficult to optimize in practice. The reliance on multiple pre-trained models also adds to the complexity of the setup.

3. Performance Concerns Relative to Complexity. Given the overall complexity, the proposed model’s 3D generation performance shows rather minor improvements. For instance, as shown in Table 1, the performance metrics are slightly higher than those of other models. The gains in PSNR, SSIM, and LPIPS are marginal, raising questions about whether the added complexity justifies the small performance improvements. The user study results, while positive, are not sufficient to fully address the concern that the performance gains are not commensurate with the complexity of the pipeline.

### Questions
1. If the model is designed to be robust across various poses, view counts, and noise levels, could you provide visual results demonstrating this? For example, does the model perform well when given a side or back view as a single input? Additionally, how much inconsistency can be tolerated during the multi-view selection process?

2. Does the performance continue to improve as the number of views increases? How does the processing time scale with more views? If more views are beneficial, what strategies could be used to efficiently handle a greater number of input views?

3. It could be confusing if the notation for f in line 294 differs from f in line 288.

4. Where are the results for the 32-view test reported in line 489?

5. What would the outcome be if the selected views were used for a NeRF-based approach, similar to Instant3D? While GS may be preferred for faster training, NeRF could potentially yield better final performance.

6. Why are the two-stage training and imperfect input view simulation conducted as separate processes?

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
5

### Summary
The author follow the classical two-stage 3D generation model: 1) Multi-view Generation; 2) A Large Gaussian reconstruction model conditioned on multi-view images from stage one to generate 3D Gaussian model. The author present a simple but effective sample strategy to choose some high-quality multi-view images among generated images as the inputs for the reconstruction stage.

### Strengths
1) The paper is well-written and easy to follow. 

2) The results the author shows are compelling. 

3) The chosen multi-view strategy for improved quality is somewhat new.

### Weaknesses
The multi-view generation model is too heavy. It requires two multi-view generations to produce dense-view proposals. I believe this process is time-consuming and memory-intensive. What is the inference time required to produce the multi-view image proposals? Does it possible to apply video diffusion mode to generate  a trajectory where elevation varies according to the sine function, and azimuth is selected at equal intervals instead of two multi-view diffusion model?

 The view selection method, while novel, may not be robust enough to handle complex geometries or objects with transparent or floating components. This could lead to inconsistent or incorrect 3D reconstructions. The paper lacks a detailed analysis of the failure modes of the view selection process, specifically how it performs with objects containing thin structures or transparent elements. The reliance on feature matching may also be problematic in cases where the generated views have significant occlusions or viewpoint changes, potentially leading to suboptimal view selection.

### Questions
1) Please show me some failure cases, especially for your view-selection method that failed.


2) Missing some Reference:

[1] Li W, Chen R, Chen X, et al. Sweetdreamer: Aligning geometric priors in 2d diffusion for consistent text-to-3d[J]. arXiv preprint arXiv:2310.02596, 2023.
[2] Qiu L, Chen G, Gu X, et al. Richdreamer: A generalizable normal-depth diffusion model for detail richness in text-to-3d[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024: 9914-9925.
[3] Chen R, Chen Y, Jiao N, et al. Fantasia3d: Disentangling geometry and appearance for high-quality text-to-3d content creation[C]//Proceedings of the IEEE/CVF international conference on computer vision. 2023: 22246-22256.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes Flex3D, a two-stage framework for generating high-quality 3D content using multi-view input views from a flexible reconstruction model. Initially, multiple candidate views are generated using separate multi-view diffusion models with distinct focus areas (elevation and azimuth), followed by a quality and consistency-based view selection. These selected views are then passed to a flexible reconstruction model (FlexRM), which leverages a tri-plane representation combined with 3D Gaussian Splatting (3DGS) for efficient 3D generation. Flex3D is shown to be effective in generating high-quality 3D representations and demonstrates state-of-the-art performance across several metrics in 3D generation and reconstruction tasks.

### Strengths
1. The two-stage process of generating and selecting views for flexible multi-view 3D generation is innovative and well-aligned with the goal of improving reconstruction quality.
2. The paper extensively validates each proposed module, demonstrating their significance through ablation studies and metrics across various tasks.

### Weaknesses
1. **Lack of Cohesion in Core Contributions**: The proposed approach, although effective, seems overly complex and tricky, and doesn’t clearly reflect Flex3D's core innovation. For instance, using two different models to generate two groups of multi-view images, and adding noisy inputs during reconstruction make the approach appear fragmented and difficult to generalize. The core contribution, which appears to be the view selection mechanism, is not presented as a significant advancement over existing methods. The motivation for using two separate diffusion models, one for elevation and one for azimuth, is not clearly justified, and the overall pipeline lacks a cohesive narrative that ties these disparate components together. The view selection process, while potentially useful, feels like an ad-hoc addition rather than a fundamental innovation that significantly improves the two-stage pipeline.
2. **Inconsistency Concerns**: The method’s use of two different models for elevation and azimuth views results in overlapping views limited to one view (that is the view with elevation of 6), raising questions about cross-model consistency. This single overlap view may not fully capture the complete object appearance, potentially leading to inconsistencies between two view sets. The limited overlap between the generated views from the two models raises concerns about the potential for artifacts or inconsistencies in the final 3D reconstruction. The lack of a more robust mechanism to ensure consistency between the elevation and azimuth views is a significant weakness.
3. **Inadequate Simulation of Multi-View Inconsistencies**: The noisy input augmentation during FlexRM training accounts for view quality but does not adequately model cross-view inconsistencies, due to its operation on the 3DGS. The noise injection, which operates on the 3D Gaussian Splatting representation, does not effectively simulate the types of inconsistencies that can arise from imperfect multi-view image generation, such as mismatched object parts or inconsistent lighting. This approach seems to address view quality rather than cross-view consistency.
4. **Lack of Flexibility Analysis**: The paper lacks a visual ablation study on FlexRM’s performance with varying input views to illustrate the model's robustness to input flexibility. The absence of a visual analysis demonstrating how FlexRM performs with different numbers and configurations of input views makes it difficult to assess the model's true flexibility and robustness.

### Questions
1. Could the authors provide more insight into how the two multi-view generation models (focused on elevation and azimuth) avoid consistency issues, given the limited overlap between generated views?
2. How does FlexRM handle scenarios where significant view inconsistencies occur, especially as noisy input augmentation does not seem to address cross-view consistency?
3. Is there a visual or quantitative comparison available regarding FlexRM’s reconstruction flexibility when provided with a varying number of input views?

### Soundness
2

### Presentation
2

### Contribution
3
