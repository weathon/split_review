# TokenFlow: Consistent Diffusion Features for Consistent Video Editing

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
\vspace*{11pt}  %{-1.05em}
 The generative AI revolution has recently expanded to videos. Nevertheless, current state-of-the-art video models are still lagging behind image models in terms of visual quality and user control over the generated content. In this work, we present a framework that harnesses the power of a text-to-image diffusion model for the task of text-driven video editing. Specifically, given a source video and a target text-prompt, our method generates a high-quality video that adheres to the target text, while preserving the spatial layout and motion of the input video. Our method is based on a key observation that consistency in the edited video can be obtained by enforcing consistency in the diffusion feature space. We achieve this by explicitly propagating diffusion features based on inter-frame correspondences, readily available in the model. 
 Thus, our framework does not require any training or fine-tuning, and can work in conjunction with any off-the-shelf text-to-image editing method. We demonstrate state-of-the-art editing results on a variety of real-world videos.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a method for text-based video editing, called TokenFlow. TokenFlow utilizes a pre-trained text-to-image diffusion model without the need for finetuning or video training data. Independently using text-based image editing techniques on frames will produce temporal artifacts. The paper proposed a method to improve the temporal consistency. More specifically, the method uses extended attention to edit several keyframes and then propagates the keyframe features to all the frames based on a Nearest Neighbour field. The Nearest Neighbour field is computed based on features of DDIM inversion.

### Strengths
- The video editing results are impressive, the temporal consistency is pretty good.
- The analysis and visualization of UNet features on video tasks are helpful for future research on video generation.
- The idea of TokenFlow is novel. Based on the ablation study and qualitative results in the supplemental material, TokenFlow is also very critical to good temporal consistency. 
- The paper reads well and is easy to follow.

### Weaknesses
Although it's not necessary, it will be helpful to compare TokenFlow with Pix2Video.

### Questions
Are self-attention features the only features that are replaced by features of neighboring frames? Have you tried to replace some other features such as ResBlock features or attention masks?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes TokenFlow for text-driven video editing, aiming to generate a temporally consistent video that adheres to the text prompt while preserving the spatial structure/motion of the source video. Specifically, TokenFlow leverages a pre-trained text-to-image diffusion model to extract features/tokens of each video frame, compute latent patch correspondence between neighboring frames, and temporally propagate the key-frame tokens to other frames during the diffusion process. Qualitative and quantitative results show that the TokenFlow performs similarly to prior methods in terms of edit fidelity (CLIP similarity) while achieving higher temporal consistency (warping error and user study).

### Strengths
S1: Sensible model design
Although the ideas of 1) using text-to-image diffusion model for video generation and 2) using latent feature flow for temporal consistency are not new, the proposed framework combines these components sensibly. The simplicity of this method also makes it compatible with existing video editing methods and more efficient than most prior arts.

S2: Temporally consistent results
The visual results show a significant improvement from prior methods in terms of temporal consistency of both texture and structural details.

S3: Good writing
The paper is well-written and easy to follow. I find the illustrations and algorithm pseudo-code quite helpful to understand the framework.

### Weaknesses
W1: Novelty 
The novelty of the proposed framework is slightly limited, considering that the key components (keyframe sampling, feature aggregation and propagation across frames) are introduced in prior works. Also, it is unclear which part of Section 4.1 is newly proposed in the paper and which is borrowed from other works. It would be great if the authors can elaborate on the main differences from prior methods and specify the novel components/modifications. 

W2: Limited structural deviation 
As shown in Figure 7, TokenFlow outputs strictly follow the structural layout of the source video, which might limit its generative capability/application. I’m wondering if there is a way to relax the temporal consistency constraint around object boundaries, so that one can find the desired tradeoff between temporal consistency and structural editing (maybe by tuning some hyper-parameters).

### Questions
Q1: The paper mentions that TokenFlow is more computationally efficient. What is the overall runtime to generate a new video and how is it compared to the methods listed in Table 1?

Q2: The ablation study on keyframe sampling only covers fixed and random sampling. It would be good to also ablate on sampling interval (tradeoff between computation overhead and temporal smoothness). I’m also curious if a dynamic keyframe sampling scheme would further improve the results, especially for occlusion cases.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper aims to address the problem of consistent video editing. The proposed method is based on text-to-mage diffusion models, and the task is to convert a source video with a target text prompt into a new video that associates with the target text while preserving the motion of the source video. The emphasis is on producing consistent frames as naively applying an image-based text-to-image diffusion model would generate individually good-quality frames, but when they are put together, it would jointly result in an inconsistent video. The key idea proposed in this paper to solve the problem is called TokenFlow, which enforces the edited internal representation of the diffusion process to preserve the inter-frame correspondences of the original video. The approach is simple and the results shown in the paper and the supplementary material look quite good.

### Strengths
1. 
The proposed method is simple and lightweight. It is built on an existing diffusion-based image editing method and does not need to fine-tune the model. The "TokenFLow Editing" algorithm is easy to implement (code available in the supplementary material). It directly utilizes Stable Diffusion, DDIM inversion, and PnP-Diffusion, and the TokenFlow procedure just requires computing the nearest-neighbor fields for token feature maps. 
Further, as mentioned in the summary in Sec. 1 of the paper, state-of-the-art editing results are one of the main contributions of this work. Indeed, the edited videos presented in the supplementary results exhibit better consistency than other methods' outputs.  

2. 
A helpful finding from this work is that the internal features offer a shared and consistent representation across frames, and the corresponding features are interchangeable for the diffusion model. The spatial and semantic properties of diffusion features are also mentioned in the concurrent work "Emergent Correspondence from Image Diffusion" as DIFT, proposed by Tang et al.; however, they focus more on matching different images and show some results for edit propagation in image editing and for video label propagation on DAVIS and JHMDB instead of enforcing consistency in video editing. While it is not necessary to empirically compare TokenFlow with DIFT, it would be helpful to highlight the differences and the shared ideas.
Nevertheless, these findings of diffusion features provide a promising direction to revisit prior ideas like *Image Analogies* and *PatchMatch*.

### Weaknesses
1. 
The results in the paper and the supplementary material mainly demonstrate the visual effect of video style transfer. For more general video editing tasks, one might expect to see some results of motion-based or composition-based video editing. Since the proposed method relies on the feature correspondences in the original video, it seems not trivial if one would like to modify the TokenFlow for motion-based editing. Specifically, the method's reliance on inter-frame feature correspondences, while effective for style transfer, may limit its applicability to scenarios requiring significant object motion changes or the introduction of new objects into the scene. The current approach appears to be constrained by the original video's motion patterns, making it difficult to implement edits that involve substantial deviations from the source video's dynamics. For example, editing a video of a walking person to make them run or adding a new object that interacts with the scene's existing motion would likely pose a challenge for the current TokenFlow implementation.

2. 
Regarding the quantitative evaluation:
- The *edit fidelity* measured by CLIP score does not provide useful/discriminative information. It might also need to include a user study on the visual quality and fidelity. The CLIP score, while useful for assessing semantic similarity between text prompts and images, does not adequately capture the nuances of visual quality and editing fidelity in video. A high CLIP score might indicate that the edited video aligns with the target text prompt, but it doesn't guarantee that the visual quality is high or that the edit is perceptually pleasing. A user study is essential to evaluate the subjective visual quality of the edited videos, as human perception is the ultimate judge of the success of an editing task. The user study should include a diverse set of participants and a well-defined evaluation protocol to ensure reliable results.
- The *temporal consistency* measured by optical flow and warping might over-penalize edits that change in shape and tend to favor edits that involve only color/texture changes. The use of optical flow and warping as metrics for temporal consistency may not be suitable for all types of video edits. These metrics are sensitive to changes in object shape and motion, and they may penalize edits that involve significant changes in these aspects, even if the edits are visually consistent. For example, an edit that changes the shape of an object while maintaining its overall motion might be penalized by these metrics, even if the edit is visually coherent. The metrics tend to favor edits that involve only color or texture changes, which might not be representative of the full range of video editing tasks.


3. 
Minor typos:  
-  "to operate on more **then** a single frame"
-  **keyframess'**
- The first words after Eqs. (4) & (5) are in upper case: **Where**

### Questions
* What would happen if the target of editing is partially occluded for a few frames in the video?
* The supplementary material shows some results of per-frame editing using ControlNet. Is it possible for ControlNet to be used not only for editing but also for providing optical flow guidance? If so, how would it differ from TokenFLow?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a framework, TokenFlow, for video editing task.
TokenFlow runs in a correspondence-propagation manner, i.e., first seeks for the correspondences across different frames, jointly edits the keyframes, and then propagates features to ensure the temporal consistency. 
Compared to prior arts, TokenFlow shows a better temporal consistency and competitive editing fidelity.

### Strengths
Approach:
- Global consistency. TokenFlow utilizes a joint editing and feature propagation via NN feature correspondences. Compared to attention-based methods, this way is more explicit and tends to keep a global consistency across different frames in a video. 
- Compatible with other image-based editors. TokenFlow seems to be able to work with other diffusion-based image editors. 

Experiments & validation:
- Proposed method is intuitive. First doing joint editing and then propagating the features makes sense. 
- From qualitative results, TokenFlow improves the temporal consistency and preserves fair fidelity. 
- Instead of using other pixelwise correspondences (e.g., dense flow or pixelwise trajectory), the authors propose to use nearest neighbor (NN) to find the correspondence. This seems new to me. 

Writing & presentation:
- The paper is well-written and easy to follow.

### Weaknesses
Experiments:
- Compared to other baselines, like Text2LIVE and Gen1, TokenFlow still shows some "flickering" when there are high-frequency patterns. For example, in "Comparisons to Baselines" SM, in the first example "running dog", the ground has severe flickering compared to Gen 1. Also in the third example "cutting bread", there is more flickering in the bread and background compared to Gen 1. Same thing also happened in the comparison to Text2LIVE in "Additional Qualitative Comparisons". Why is TokenFlow not able to maintain the consistency for the high-frequency patterns? It would be beneficial to understand if this is due to the feature matching process or the diffusion model itself.
- Based on the previous point, I think the authors could consider analyzing the reason behind the flickering and include it in **Limitations**.
- How do different image editors affect the results? Specifically,  the comparison w/ PnP + propagation. The authors mention that they have an additional comparison with PnP-Diffusion + propagation in the **last sentence, Section 5 Baselines**, but this part seems missing either in the main paper or in the SM. It is unclear how the choice of image editor impacts the temporal consistency and fidelity of the results.
- It would be great if the authors could also include runtime comparisons. This is especially important since the method involves feature propagation across frames, which could be computationally expensive.

### Questions
- Features & RGB images: In Figure 3, authors show that TokenFlow improves the consistency in feature level. However, can the feature level consistency ensure the RGB output consistency? 
- Correspondence ablation: Why using NN for the correspondences instead of using optical flow? Can pixel-level correspondences like dense optical flow be used for this token-based framework? Can we apply downsampled optical flow maps to the feature maps? 
- Occlusion: Is the current framework be able to handle some extreme cases, like occlusion? For example, a dog running through some poles but sometimes the dog is occluded by pole. 
- Video length: What is the maximal length TokenFlow can handle? 
- What is the post-procssing deflickering that is used in the SM?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
