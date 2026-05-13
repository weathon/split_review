# MovieDreamer: Hierarchical Generation for Coherent Long Visual Sequences

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Recent advancements in video generation have primarily leveraged diffusion models for short-duration content. However, these approaches often fall short in modeling complex narratives and maintaining character consistency over extended periods, which is essential for long-form video production like movies. We propose MovieDreamer, a novel hierarchical framework that integrates the strengths of autoregressive models with diffusion-based rendering to pioneer long-duration video generation with intricate plot progressions and high visual fidelity. Our approach utilizes autoregressive models for global narrative coherence, predicting sequences of visual tokens that are subsequently transformed into high-quality video frames through diffusion rendering. This method is akin to traditional movie production processes, where complex stories are factorized down into manageable scene capturing. Further, we employ a multimodal script that enriches scene descriptions with detailed character information and visual style, enhancing continuity and character identity across scenes. We present extensive experiments across various movie genres, demonstrating that our approach not only achieves superior visual and narrative quality but also effectively extends the duration of generated content significantly beyond current capabilities. Homepage: \url{https://aim-uofa.io/MovieDreamer/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents MovieDreamer to make long video. This is challenging because current video diffusion models can only deal with short clips and do not have character consistency. The model trains a MLLM that can predicts the visual tokens with movie script conditioning. Then using the diffusion decoder to decode the condition into key frames, and using I2V to render it into video clips.

### Strengths
The quality is GREAT!
Engineering wise, this paper produces a product-level solution to long-video (movie) generation; Scientificly, this paper also explores training a MLLM to output visual features given the input scripts, instead of simply using an agent framework to compose scripts, and use subject-driven models to preserve character identity.
The ID Preserving is also very effective

### Weaknesses
Lack of non-human results, don't know if such methods can generalize well to general domain long-vedio generation.

### Questions
Since authors are changeing LLaMA input to CLIP embedding (for sentence), does it cause much for the LLM to adapt to such input?
How much cherry-pick do you need for a single long video?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a hierarchical generation framework for long video sequence generation, which can be potentially applied to movie video generation. The key idea is to leverage the autoregressive models to generate key frame tokens, and then use diffusion models to decode the tokens into RGB frames. This approach leverages the advantage of any-length future prediction ability of AR model and the powerful rendering ability of diffusion models. Through some other techniques such as multimodal script, face embedding condition, etc., the framework can generate ultra-long video sequences with better quality.

### Strengths
+ The model provides an effective integration of autoregressive model and diffusion models, for the long visual sequence generation task. The combination is reasonable by successfully leveraging the arbitrary-length generation capability or AR model and the powerful rendering ability of diffusion models. 
+ The utilization of the gaussian mixture model for the continuous visual token prediction is reasonable and inspiring.

### Weaknesses
 - The paper proposes a lot of techniques to improve the identity consistency among different clips, however, I cannot find any ID-related evaluation on the generation results.
- The paper did not analyze the boundaries of the proposed method. For example, 
    - when will the model fail at ID consistency since the model only provides one face embedding as the condition. 
- The technical novelty is relatively limited. There exist many multimodal generative models can do the similar key frame generation task, though they may not be directly used for movie key generation.

### Questions
Please provide the evaluation of the ID consistency of the model, clarify the technical contributions, and discuss the limitations of the framework.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Existing diffusion model-based video generation models can only support short video generation and lack understanding of narrative structures and plot progressions. Therefore, this paper explores long-story video generation by leveraging the inference capability of autoregressive generation and video diffusion models’ rendering capability. Specifically, this paper proposes a hierarchical framework and a structured multimodal story input representation. The framework fine-tunes the multimodal large model LLAVA to generate compressed tokens of keyframes and fine-tunes SDXL as a decoder to generate keyframe images from the compressed tokens. Finally, SVD is used to generate the video. Additionally, the paper proposes a few-shot training method, enabling the model to achieve customized generation. Extensive experiments compare the proposed method with existing story keyframe generation methods, demonstrating superior performance.

### Strengths
1.	The proposed framework seems promising for generating long video. 
2.	The proposed method can effectively generate character-consistent story keyframes, and the experimental results show the superiority of the proposed method to other state-of-the-art methods.

### Weaknesses
The overall writing of the paper is relatively clear, and the experimental results are promising. However, some of the descriptions appear to be incorrect or misleading, and the experiments are also not entirely comprehensive.

1. In line 242, why are the parameters of the GMM stated as 2kd means and 2kd variances? According to the reference work, each GMM parameter should contain kd means, kd variances, and k coefficients for each compressed token.

2. What would the results look like if Eq. 2 were used as the sole objective function? There doesn't appear to be a corresponding analysis of this in the experiments. Is the inclusion of L2 and l2 necessary, or have previous works discussed the necessity of incorporating these terms?

3. In Fig 2, if I understand correctly, the multimodal script in the top-left corner is used to generate a single keyframe. However, the three keyframes shown on the right under the VLM section could easily give the impression that they were all generated by the same script. This may lead to some confusion for readers. Additionally, according to Equation 1, the input to the decoder should also include a noise latent. However, the inference process shown at the bottom of Figure 2 does not fully display the complete inputs and outputs, which could lead to some misunderstandings.

### Questions
I have outlined some concerns and suggestions in the weaknesses section, and there are additional questions that need clarification.

1. Is the covariance matrix in Eq. 7 of the supplementary material a diagonal matrix?

2. In the few-shot training section, what is the “episode’s visual tokens” (line 302)?

3. In Fig 8, what are the reference images for generating the few-shot results?  If I understand correctly, face embedding is also used as part of the multimodal script to generate zero-shot results. For the few-shot generation, what images are used as references, and how do these reference images help improve identity consistency?

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
5

### Summary
The paper proposed a novel hierarchical video generation framework MovieDreamer, which is able to generate long-duration videos with high visual fidelity. The framework consists of a SDXL-based visual autoencoder and a multimodality VLM. The autoencoder focuses on obtaining the visual tokens of input images, as well as rendering targeted keyframes, while VLM autoregressively predicts visual tokens. Quantitative evaluation shows that the proposed method outperforms sota in long video generation.

### Strengths
1. The proposed framework propose a hierarchical way to combine autoregressive modeling and diffusion image generator together for long-term complex video generation.
2. The paper proposed several novel techniques, e.g., continuous token supervision, anti-overfitting strategies, id-preserving, to improve the performance of the framework.
3. The proposed method achieved state-of-the-art performance on quantitative evaluation.

### Weaknesses
1. L212: Eq1, the DAE has not been clearly defined in the paper. Also, in Fig2, I could not find DAE in the pipeline. I hope the authors could clarify this. The description of the DAE is insufficient, lacking details on its architecture, training procedure, and how it is integrated within the larger framework. The paper needs to specify the exact layers, activation functions, and loss function used for the DAE, as well as how it handles the input image tokens, face embeddings and description embeddings.
2. It is a bit confusing whether Eq1 is the real training loss or not? According to Sec3.3 and Fig2, the input of SDXL should be image token, face embedding and description embedding, which does not align with Eq1. It is better to clarify the final training loss. The paper does not clearly state the final training loss function, especially how the face and description embeddings are incorporated into the loss calculation. The discrepancy between Eq1 and the described inputs in Sec3.3 and Fig2 needs to be resolved. It is unclear if Eq1 is only used in the initial training phase of the DAE, and if so, what the loss function is when face and description embeddings are included.
3. It is not clear how random masking strategies work during training and inference stages. The paper needs to provide more details on the random masking strategy, including the masking ratio, the type of masking (e.g., token-level, patch-level), and how the masked tokens are handled during training. It is also unclear whether the masking is applied to all inputs or only to specific parts, and why this strategy is not used during inference.
4. The high dropout rate (50%) seems to be unusual. Are all the parameters updated in VLM? Have the authors tried only tuning part of the network? The paper should provide justification for the unusually high dropout rate of 50%. It is unclear whether all parameters of the VLM are updated during training, or if only a subset of parameters are fine-tuned. The authors should also provide ablation studies to show the impact of different dropout rates and parameter tuning strategies on the performance of the model.
5. L323: if the feature of the first frame is always used, will generated character be limited to small motion, and limited content? For example, for large rotation and movement, the performance of the proposed method may drop? The method's reliance on the first frame's feature may limit the diversity of motion and content in the generated videos. The authors should discuss the potential limitations of this approach, especially for scenarios involving large rotations, significant movements, or substantial changes in the character's appearance. It is important to analyze how this choice affects the long-term consistency and the ability to generate complex actions.
6. What are the frame numbers of full-length video?
7. From Fig8, while compared to zero-shot setting, the few-shot setting indeed improves the ID-preserving ability. However, there is still an obvious gap between target ID and generated image. What could be the potential reason for this? Any solution?
8. What is the training cost? And what are the inference time and GPU memory requirements?  
9. For quantitative evaluation, it seems that the reported metrics all focus on image level. They can not evaluate how good the performance of spatio-temporal modeling. It is better the authors could evaluate the proposed method using other metrics for video generation.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
