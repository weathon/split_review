# SEINE: Short-to-Long Video Diffusion Model for Generative Transition and Prediction

- Decision: Accept
- Scores: 5, 5, 6, 6

## Abstract
Recently video generation has achieved substantial progress with realistic results. Nevertheless, existing AI-generated videos are usually very short clips (``shot-level'') depicting a single scene. To deliver a coherent long video (``story-level''), it is desirable to have creative transition and prediction effects across different clips. 
This paper presents a short-to-long (S2L) video diffusion model, \textbf{SEINE}, that focuses on generative transition and prediction. The goal is to generate high-quality long videos with smooth and creative transitions between scenes and varying lengths of shot-level videos. 
Specifically, we propose a random-mask video diffusion model to automatically generate transitions based on textual descriptions. 
By providing the images of different scenes as inputs, combined with text-based control, our model generates transition videos that ensure coherence and visual quality. Furthermore, the model can be readily extended to various tasks such as image-to-video animation and auto-regressive video prediction. To conduct a comprehensive evaluation of this new generative task, we propose three assessing criteria for smooth and creative transition: temporal consistency, semantic similarity, and video-text semantic alignment. Extensive experiments validate the effectiveness of our approach over existing methods for generative transition and prediction, enabling the creation of story-level long videos. Project page: {\small \url{https://vchitect.io/SEINE-project/}.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents the SEINE model, for generating "story-level" long videos from short clips. It introduces a unique problem in generative transition and prediction. Using a random-mask video diffusion based on textual descriptions, the model shows smooth transitions between scenes. To evaluate its efficacy, the authors provide three new criteria: temporal consistency, semantic similarity, and video-text alignment. Results show its potential for generating coherent long videos.

### Strengths
- The method of using masks was proposed in [1] and [2], but as far as I know, this is the first time it has been used in video transition. It could be novel.

- The proposed method shows better performance on the metric compared to the baseline.

- The proposed method can be applied in various areas such as long video generation and image-to-video animation.


References

[1] Voleti, Vikram, Alexia Jolicoeur-Martineau, and Chris Pal. "MCVD-masked conditional video diffusion for prediction, generation, and interpolation." Advances in Neural Information Processing Systems 35 (2022): 23371-23385.

[2] Fu, Tsu-Jui, et al. "Tell me what happened: Unifying text-guided video completion via multimodal masked video generation." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

### Weaknesses
 - [Major] My main concern is that there is not enough quantitative evaluation of video transitions. This paper conducted quantitative experiments by randomly selecting one caption from MSRVTT and determining CLIP-TEXT. However, since video transitions occur when scenes change, it does not seem appropriate to evaluate video semantic correlation. The CLIP-TEXT score, while useful for text-video alignment, does not directly measure the smoothness or coherence of the transition itself. A more appropriate evaluation would involve metrics that assess the visual continuity and semantic flow between the frames, especially during the transition period. Furthermore, no video quality evaluation metrics (such as FVD etc.) have been considered. This makes it difficult to quantify the exact quality of generation, especially the temporal consistency and visual fidelity of the generated transitions.

- [Major] Several details related to the human evaluation are missing. (such as number of frames in the generated video, the dataset used, and the questions posed in the user study.) Was the user study appropriately reflective of temporal coherence, text-video alignment, and semantic similarity? Without specific details on the experimental setup, it's difficult to assess the validity and reliability of the human evaluation. The lack of clarity on the evaluation criteria and the specific questions asked makes it hard to determine if the user study truly captured the intended aspects of video quality and transition smoothness.

- [Minor] For transitions to be applied in the real-world, it would require generating more than 16 frames. Would the quality be maintained if more frames are generated? The current evaluation is limited to short 16-frame transitions, which might not be representative of longer, more complex video sequences. It's unclear if the model can maintain the same level of quality and coherence when generating longer transitions, which is a crucial aspect for practical applications.

- [Minor] In Figure 5 related to video transition, the frame numbers and details are omitted. This makes it difficult to analyze the transition process and understand how the model generates intermediate frames. The lack of specific frame numbers and details makes it harder to assess the smoothness and coherence of the transition.

### Questions
How long does the inference take? Is it capable of handling transitions with multiple objects across more than two scenes?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the author focus on a new task, "generative transition", which aims at smooth and creative transitions between scenes. Specifically, this paper proposes SEINE, a short-to-long video diffusion model with random masks to generate transitions frames based on textual prompts that describe transitions. Given a few unmasked frames, the proposed random-mask based diffusion model is able to generate frames at arbitrary positions. Therefore, their model can be used for tasks including generative transition, long video generation, and image-to-video animation by giving unmasked frames at different positions. 

In the experiments, the authors compare their model with other baselines including morphing, VQGAN-based transition, and SD-based transition. Quantitative and qualitative results show that SEINE has better transition temporal coherence, semantic similarity across frames, and better video-text alignment.

### Strengths
- The task of generative transition is novel and rarely explored, which I believe is one of the main novelty of this paper. As current text-to-video generation models are mostly tacking short video clips, a smooth and creative transition between these short clips is of increasing importance.

- The proposed random-mask based model seems a good solution for this task. In addition to generating transition frames, the random-mask based model can also deal with long-video generation and image-to-video generation by giving unmasked frames at different positions. 

- The quantitative and qualitative experiments demonstrate the effectiveness of the proposed model.

### Weaknesses
 - From the qualitative result shown in Figure 6, it seems that the transition is more like a "interpolation" between two scenes. For example, the frames in (row1, col4). (row2, col2), and (row2, col3) are not very natural. Specifically, the intermediate frames appear to be a simple blending of the start and end frames, lacking the dynamic and creative elements one would expect from a generative model. The transitions often appear as a fade-in/fade-out effect rather than a genuine transformation of the scene.

- In Figure 5 right part (the cat example), it seems that morphing also provides a descent transition. So for two frames with small transitions needed in between, it seems that the proposed method might add unnecessary variety/creativity. In cases where the start and end frames are very similar, the model's attempt to introduce variety may result in unnatural or unnecessary changes. This raises questions about the model's ability to adapt to varying degrees of transition complexity.

- In general, it's hard to see if the proposed method provides a good solution to this new task. The paper also lacks enough ablation study of the model architecture design. More discussions and intuitions about this task would be helpful for future works. The paper does not provide a clear understanding of the specific architectural choices and their impact on the performance. The lack of ablation studies makes it difficult to assess the contribution of each component of the model. Furthermore, a deeper discussion of the challenges and nuances of the generative transition task is needed to better contextualize the proposed method.

- Some minor things: 
1. In Sec. 2, the citation for PYoCo is missing. 
2. In the last paragraph of Sec. 3, the sentence describing "Long video" is incomplete.
3. Figure 4 is not easy to understand at first glance. It would be nice to add more descriptions for better readability.
4. In Figure 10, the image on the left part has red-green-blue watermarks. Is that example from Gen-2 instead of SEINE?

### Questions
- For controllable transition generation, do we give the first and last frames unmasked to the modl for each prompt? If this is the case, I'm wondering maybe the model can also generate smooth zoom-in/out transitions without explicitly adding "camera zoom-in/out" in the prompt. It would be nice to provide ablation study that removes "camera zoom-in/out" in the prompts and see if the generation quality deteriorates.

- As mentioned in the above part, it would be nice if the author can provide some discussions about what kinds of scene transitions (small transition vs large transition, same object vs different objects) their model is good at.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new problem of generative transition and prediction, which can help generate story-level videos through different shot transitions. The author also proposed a short-to-long video diffusion model, which utilizes a random mask strategy for training. To evaluate the task, this paper proposes three assessing criteria. Both objective and subjective evaluation prove their proposed method’s effectiveness.

### Strengths
This article addresses the limitation of existing models that can only generate shot-level videos and proposes a method to generate story-level videos using transitions. They extend an existing video generation framework and achieve impressive results in generating long videos. They also propose a reasonable evaluation framework to assess the proposed model, and a large number of demos and quantitative evaluations demonstrate the effectiveness of their approach. The contribution of this work is significant.

### Weaknesses
The author should provide a more detailed description of the model for reproducibility, including training resources, training parameters, and so on. Additionally, the author should also report scores on commonly used evaluation metrics such as FID.

### Questions
I wondered how many GPUs they used and how long it takes for training. Besides, as far as I know, FID is used to evaluate video generation quality in many papers, can they provide this to make their paper more solid?

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
This paper proposes a method to train a diffusion model with random masking on the frame level to enable video generation, prediction, and interpolation. They demonstrate that their method is able to generate longer video and create smooth transitions between two different frames. The authors demonstrate that their method outperforms baseline methods.

### Strengths
- The paper is well written, and clear
- The paper shows good long video generations, and is able to generate complex transitions between semantically different frames

### Weaknesses
My primary concerns center around the lack of baselines and novelty. Particularly, the authors fail to cite a few very related works, that accomplish similar tasks that enable frame prediction and interpolation.

- MaskViT [1], MAGVIT [2]: MaskGit-like models trained on tokenized video frames. Given the masked learning object, these models can also usually generalize to enable generation, prediction, and interpolation. MAGVIT is trained explicitly to do this. 
- MCVD [3], RaMViD [4]: These two methods seem nearly identical to the proposed method, where a video diffusion model is trained with masked latents. An exception is a lack of text-conditioning and scale in [3,4], however, I do not believe that meets the bar as a point of novelty.

Could the authors please clarify on how their method is novel over the prior work mentioned above? In addition, it would be necessary to compare against a subset of these methods as baselines (or a similar model), as currently there are no baselines explicitly trained for the prediction / interpolation tasks.

### Questions
See weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
