# GAIA: Zero-shot Talking Avatar Generation

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Zero-shot talking avatar generation aims at synthesizing natural talking videos from speech and a single portrait image. Previous methods have relied on domain-specific heuristics such as warping-based motion representation and 3D Morphable Models, which limit the naturalness and diversity of the generated avatars. In this work, we introduce GAIA (Generative AI for Avatar), which eliminates the domain priors in talking avatar generation. In light of the observation that the speech only drives the motion of the avatar while the appearance of the avatar and the background typically remain the same throughout the entire video, we divide our approach into two stages: 1) disentangling each frame into motion and appearance representations; 2) generating motion sequences conditioned on the speech and reference portrait image. We collect a large-scale high-quality talking avatar dataset and train the model on it with different scales (up to 2B parameters). Experimental results verify the superiority, scalability, and flexibility of GAIA as 1) the resulting model beats previous baseline models in terms of naturalness, diversity, lip-sync quality, and visual quality; 2) the framework is scalable since larger models yield better results; 3) it is general and enables different applications like controllable talking avatar generation and text-instructed avatar generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose to use a generative latent diffusion model to address the problem of talking head synthesis from audio and a single photo. The pipeline consists of a variational autoencoder that encodes the video frames into appearance and motion latent representations and a diffusion model that is trained to predict the pre-trained motion latent from audio and pose conditioning. The authors also propose to use a data filtering approach to remove the noisy samples from the dataset to achieve high-quality results. The experimental evaluation is quite extensive and includes audio, head pose, and text-driven examples.

UPD: The rebuttal has addressed my concerns, and the results look genuinely impressive.

### Strengths
- Impressive quality of the results in terms of both lipsync and visual quality
- The model's design is straightforward yet evidently effective
- The paper is well-written and the evaluation is pretty extensive

### Weaknesses
 - Missing evaluation of disentanglement between appearance and pose latent codes, i.e., cross-reenactment with the motion codes extracted from the image of a different identity. Specifically, the paper lacks a quantitative assessment of how well the appearance and motion latent spaces are separated, which is crucial for the model's ability to generalize to new identities and poses. A more rigorous evaluation would involve swapping motion latents between different identities and measuring the quality and identity preservation of the resulting videos.
- Missing discussion of the related works, such as [1, 2], that explored the concept of pose-identity disentanglement for talking head synthesis before this work. The absence of a thorough comparison with these methods leaves the reader unsure about the novelty and advantages of the proposed approach. Specifically, it is unclear how the proposed method improves upon the disentanglement strategies used in these prior works, and what specific limitations of those methods are addressed by the current approach.
- As far as I can tell, the proposed method and the baselines were trained on different datasets. The resulting comparison evaluates the proposed framework _and_ the dataset at the same time. A comparison should include the experiments where base methods are trained on the same dataset, and the proposed method is trained on unprocessed datasets used in previous works. This is a significant concern, as it is difficult to isolate the performance gains due to the model architecture from those due to the data preprocessing and filtering. A fair comparison requires training all models on the same data, using the same level of preprocessing, and this should include a comparison on the unprocessed datasets used in previous works.
- Comparison of the inference time between the compared methods is not provided. I would also argue that some baselines, such as SadTalker, can be substantially improved, given the computational budget of the proposed method that runs the diffusion model for every time step. Ex., with the fine-tuning of the model given the source frame. The paper should include a detailed analysis of the inference speed of the proposed method compared to existing approaches. Furthermore, the discussion should include the potential for optimizing the baselines, such as SadTalker, to achieve a more computationally fair comparison.

### Questions
- Please address the concerns mentioned in the weaknesses
- Could the authors clarify if they plan to release the filtered dataset and the pre-trained models?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes an audio-driven talking head synthesis model named GAIA that is an end-to-end trainable data-driven solution. The model has two main stages 1. disentanglement of motion and appearance with VAE 2. speech-to-motion generation based on diffusion model. Also, the paper proposes a new talking head dataset with 8.2K hours of video and 16.9K unique speakers.

### Strengths
The manuscript proposes a new dataset.

The writing is supported by equations and well-drawn figures that make the explanation clear.

Although the experiments with existing models are not enough (see weaknesses), the ablation study is rich and increases the overall quality.

### Weaknesses
The gap/ limitations of 3DMM-based models are found and addressed well by proposing an end-to-end trainable model. I am not sure it is novel enough as the other end-to-end trainable talking face synthesis models are not discussed enough.

The experiments are limited, especially comparison with end-to-end trainable models not provided. I suggest enriching the benchmarking with other existing models such as  PC-AVS and PD-FGC as they are also end-to-end trainable models. 

Although the writing quality is decent, it is hard to follow as it refers to other sections frequently and other issues (see Questions 1 and 2).

I am not sure the model can be named as zero-shot as it requires one shot for unseen faces. So, could you elaborate on the following '... generates a talking video of an unseen speaker with one portrait image ...'?

### Questions
1. In section 3, what does 'we collect High Definition Talking Face Dataset (HDTF) (Zhang et al., 2021) and Casual Conversation datasets v1&v2 (CC v1&v2) (Hazirbas et al., 2021; Porgali et al., 2023)' and 'we also collect a large-scale internal talking avatar dataset named AVENA' mean? Does it mean you collect those datasets you use their sample in your dataset or you use their samples in your training but they are not in your dataset? From the supplementary material, my understanding is you collect AVENA and use samples from other datasets (HDTF, CC v1, and v2) in the training of your model. Could you please elaborate and make it clear?

2. Why do you have a discussion section at the end of Section 4 Model? I think it makes more sense in/after experiments. So, you can consider reorganizing the manuscript to have a better flow and complete discussion.

3. 3. I am not sure the model can be named as zero-shot as it requires one shot for unseen faces. So, could you elaborate on the following '... generates a talking video of an unseen speaker with one portrait image ...'?

3. Ethical consideration is left in Appendix F. However, for this study ethical consideration is important. So, you might consider putting it into the main manuscript to give necessary importance if possible.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a data driven approach for generation of 2D avatars. The method disentangles motion and appearance and uses a diffusion model to allow motion generation conditioned on pose and speech data.

### Strengths
1) The method is conceptually simple and sensible.
2) It is shown to scale well in terms of model size and as a self-supervised method can utilize readily available training data at scale.
2) Method requires very few pretrained components.
3) Evaluation includes user study which is always good for addressing output quality.
4) Method is highly flexible and allows a high degree of control from pose, facial attributes and text.

### Weaknesses
1) A comparison with https://arxiv.org/pdf/2012.08261.pdf for video driven is critically missing as a recently proposed SOTA method. In their paper they show improvements compared to face-vid2vid and FOMM which are used as baselines here and they provide a pretrained checkpoint.

### Questions
1) will the dataset be shared as part of this submission?
2) It would be interesting to see an ablation on training data size to assess whether there are benefits from scaling data further.
3) How does randomness from the diffusion model affect generations?

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
This work aims to generate talking avatars with two separate modules: 1. first disentangle motion and appearance; 2 then generate head motions in accordance with speech.  As the proposed method does not utilize 3DMMs, the proposed data-driven method is promising to generate talking avatars with better diversity and naturalness.  The reported experiments show better quantitative results and better visual quality.

### Strengths
1. This work establishes a large-scale talking avatar dataset for data-driven talking avatar generation.

2. The proposed data-driven method could achieve taking avatar generation with superior performance on naturalness, diversity, lip-sync quality, and visual quality.  

3. The proposed method is scalable, and the authors conduct experiments that show the larger model is employed, the better performance could be achieved.

4. The authors show that the proposed method could support many related applications, such as controllable talking avatar generation and text-driven video generation.

### Weaknesses
The authors did not provide a large number of generation examples. I hope it is possible to see more visual results.
For example, 
1. long videos for the generated talking avatars;

2. different reference video/frame but the same driving video;

3. different driving video but the same reference video/frame.

### Questions
1. is it possible to drive cartoon characters (humanoid or non-humanoid)?

2. will the proposed method and the established dataset be publically available?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
