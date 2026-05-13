# Realistic-Gesture: Co-Speech Gesture Video Generation through Semantic-aware Gesture Representation

- Decision: Reject
- Scores: 3, 5, 6, 6, 8

## Abstract
Co-speech gesture generation is crucial for creating lifelike avatars and enhancing human-computer interactions by synchronizing gestures with speech in computer vision. Despite recent advancements, existing methods often struggle with accurately aligning gesture motions with speech signals and achieving pixel-level realism. To address these challenges, we introduce Realistic-Gesture, a groundbreaking framework that transforms co-speech gesture video generation through three innovative components: (1) a speech-aware gesture tokenization that incorporate speech context into motion pattern representation, (2) a mask gesture generator that learns to map audio signals to gestures by predicting masked motion tokens, enabling bidirectional contextually relevant gesture synthesis and editing, and (3) a structure-aware refinement module that employs differentiable edge connection to link gesture keypoints to improve video generation. Our extensive experiments demonstrate that Realistic-Gesture not only produces highly realistic and speech-aligned gesture videos but also supports long-sequence generation and video gesture editing applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses challenges in co-speech gesture video generation through a proposed method called Realistic-Gesture. This method incorporates three main components: a speech-aware gesture motion representation, a masked gesture motion generator, and a pixel-level refinement module. Experimental results show that the proposed approach generates realistic co-speech gesture videos, while also enabling long-sequence generation and video editing capabilities.

### Strengths
1. The authors identify three key challenges in co-speech gesture video generation and propose solutions to address each one.

2. Amount of ablation studies are conducted to verify the effectiveness of the proposed modules.

### Weaknesses
Generally, some challenges identified in this paper have been addressed in prior research; however, the authors failed to cite these studies or compare their findings with the experiments conducted in this work. Notable examples include:

1. **"Rhythmic Gesticulator: Rhythm-Aware Co-Speech Gesture Synthesis with Hierarchical Neural Embeddings."** This study proposed a shared hierarchical embedding for both speech content and motion, which closely resembles the approach taken by the authors.
  
2. **"Make-Your-Anchor: A Diffusion-based 2D Avatar Generation Framework."** This research adopted SMPL-X parameters as motion representations for co-speech video generation, enhancing the clarity of hand movements.

Additional weaknesses include:

1. While the proposed method can perform gesture inpainting, the authors inaccurately claim that it supports video gesture editing. This assertion is misleading, as the inpainted gestures are not controllable.

2. In some of the "Gesture Pattern Transfer" videos, the character appears distorted, likely due to differences in body proportions between the source and target characters.

### Questions
See weaknesses part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work proposes Realistic-Gesture, a framework that enhances this process through speech-aware gesture tokenization, a mask gesture generator for audio-to-gesture mapping, and a structure-aware refinement module. The results demonstrate that Realistic-Gesture creates realistic, speech-aligned gesture videos and supports long-sequence generation and editing.

### Strengths
This paper proposes a framework for generating co-speech body-gesture videos, dubbed Realistic-Gesture. Realistic-Gesture integrates a speech-aware gesture motion representation, a masked gesture motion generator, and a pixel-level refinement module to facilitate high-quality video generation. The strengths of this work are summarized as follows:
1. The insight of the work is interesting and significantly practical in real-life applications.
2. The experimental workload is solid and persuasive.
3. The demo videos are helpful for reviewers to have a comprehensive understanding of this work.

### Weaknesses
However, I still find some weaknesses and some main questions in this manuscript:

1. In the introduction section, the authors put much effort into introducing existing works. This may lead to much overlap with the ``related work'' section. The motivation and insight of this work could be summarized more compactly. Authors can leverage more space to elaborate on the high-level technical contribution of their work.

2. The teaser figure (Fig. 1) seems confused. I cannot obtain significant insight into it. Meanwhile, there are no effective captions in the manuscript.

3. There are some typos, e.g., in line 173, To achieve this goal, We... The letter ``W'' should be lowercase.

4. The technical novelty seems a little bit weak. The Residual Gesture Generator, Masked Gesture Generator are very similar to the previous works, like:

[1] Generating Holistic 3D Human Motion from Speech, in CVPR 2024.

[2] EMAGE: Towards Unified Holistic Co-Speech Gesture Generation via Expressive Masked Audio Gesture Modeling, in CVPR 2024.

[3] BEAT A Large-Scale Semantic and Emotional Multi-Modal Dataset for Conversational Gestures Synthesis, in ECCV 2022.

5. I am very curious that the FGD and FVD in Experimental Table 1 seem a bit weird. While the authors' method achieves a larger marginal improvement in FGD than the suboptimal S2G (1.303 vs 23.646). The FVG of these two methods is very propinquity (476.120 vs 486.134). Does this mean that the author's proposed ``STRUCTURE-AWARE IMAGE REFINEMENT'' is not effective?

6. The proposed ``learnable edge heatmaps'' is similar to the work named [4]. I suggest the authors compare with it.

[4] Audiodriven neural gesture reenactment with video motion graphs, in CVPR 2022.

### Questions
Please refer to Weaknesses

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes Realistic-Gesture, a gesture video generation model with speech audio and the first video frame inputs. The proposed method first learns a joint embedding of the speech audio and gesture motions for speech-gesture alignment with CLIP-like contrastive learning. The pose features are 2D face and body landmarks from MMPose. The speech-audio features are the concatenation of WavLM, Mel spectrogram, and beat detections. The gesture motions are tokenized using Residual VQ (RVQ) with the distillation to minimize the cosine similarity with the motion encoder output in the gesture-audio joint embedding. Inspired by VALL-E, the method uses the Masked Gesture Generator for RVQ's base layer and the Residual Gesture Generator for residual layers. The Masked Gesture Generator is a transformer with the cross-attention between the audio embedding and the gesture embedding with AdaIN after the feed-forward layer to condition the model with the speaker identity. The Masked Gesture Generator is trained with randomly masked tokens. The Residual Gesture Generator is similar but consists of embedding layers corresponding to the RVQ residual layers. During training, one residual layer is randomly selected. The inference iteratively predicts the mask probabilities conditioned by the audio embedding to remask the token with the lowest probability for the next iteration. Finally, the source image is warped with TPS [Zhao and Zhang 2022] with the edge maps from the generated keypoints, followed by the image refinement GAN conditioned by the same edge maps, to generate the gesture videos.

### Strengths
- Speech-gesture alignment with CLIP-like joint embedding with contrastive learning
- Motion tokenization with RVQ distilled by the joint embedding above
- Audio-conditioned Masked Motion Model with dedicated residual generators for the RVQ residual layers

### Weaknesses
The contributions boil down to the motion representation and the motion generation model. There is not much to the image generation module. The visual quality may also be suffering because of the image generation module (see below).

Qualitatively, the generated videos from this method generally look better than other methods in comparison (ANGIE, MM-Diffusion, S2G-Diffusion), especially if I focus on the speech-gesture motions. However, there are moments where the human generation is creepier than others with this method, e.g. in noah1.mp4, the head and the body look disconnected. I am not too surprised that the TPS warping will introduce unnatural human poses, especially with larger 3D motions. Perhaps the image warper and the refiner need more work. The motion representation and the generation model perhaps could be hooked up to some other conditional image/video generator.

The writing is somewhat unclear on the image generation module. The main text directly jumps to the image refinement module without mentioning the TPS image warping, which confused me a bit. Perhaps 4.3 should be titled differently and recap the image warping module while clarifying this is not the paper's contribution (no strong opinion here).

I understand that the space is very limited but I would like more elaborations on the ablations, especially on the motion representation and the generator design, so I can be confident that the main contributions of this paper are indeed effective. See my question.

### Questions
Can authors provide videos for the ablation study, especially on the motion representation and the generator designs? I want to be confident that the use of the CLIP-like joint embedding to distill the RVQ for the Masked Motion Model to generate tokens is helping to improve the visual quality.

The speech-gesture joint embedding could perhaps be used to evaluate the alignment of the speech audio and gestures, like the CAPP model from VASA-1 [Xu et al. 2024].

### Soundness
4

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
The paper introduces a framework aimed at generating realistic co-speech gesture videos. This framework tackles the challenges of establishing correspondences between speech signals and body movements, inferring suitable gestures from speech samples, and rendering the target speaker performing these gestures in a lifelike manner. The authors propose three innovative components to accomplish this:
1. A speech-aware gesture representation that aligns facial and body gestures with speech semantics, enabling fine-grained control.
2. A mask gesture generator that maps audio signals to gestures by predicting masked motion tokens, thereby enabling bidirectional and contextually relevant gesture synthesis and editing.
3. A structure-aware refinement module that uses a multilevel, differentiable edge connection to link gesture keypoints for the generation of detailed videos.

The paper's contributions include the production of highly realistic, speech-aligned gesture videos, as well as support for long-sequence generation and video gesture editing applications. The experiments demonstrate the method's superiority over existing approaches in both quantitative and qualitative metrics.

### Strengths
The paper presents a well-articulated approach to generating co-speech gesture videos, demonstrating a clear understanding of the associated challenges and the necessity for a sophisticated method to address them.
- The authors have crafted a compelling narrative surrounding the design of their method, offering adequate motivation for each component.
- From a visual standpoint, the proposed method surpasses existing state-of-the-art techniques.
- The integration of speech-aware gesture representation, masked gesture generation, and structure-aware refinement is a significant strength, enhancing both the realism and controllability of gesture synthesis.

### Weaknesses
 **Long Sequence Generation Quality**: The author identifies the capacity to generate long sequences as a primary contribution of their method. However, the supplementary video material reveals that the quality of long sequence generation is subpar; in later stages, the hands become blurry, and behavioral patterns tend to repeat. Furthermore, the author provides a limited number of videos and fails to present quantifiable metrics for assessing the quality of long sequence generation. Consequently, I have significant doubts regarding the framework's ability to generate long sequences effectively.

**Lack of Novelty in Core Components**: Although the framework offers an integrated approach to gesture synthesis, its core components—speech-aware gesture representation and masked gesture generation—have been examined in various forms in recent literature.
- The contrastive learning approach for speech-gesture alignment has been utilized in gesture synthesis methods [1,2,3] and is very similar to the CSMP introduced in [1].
- Similarly, the use of RVQ [4,5] and masked gesture synthesis techniques [6] is not new to the field.

The paper should offer a more detailed comparison with these methods and present a more comprehensive review of the related works.

### Questions
- This method utilizes 2D keypoints as guiding conditions. However, variations in human skeletal structure and facial shape may result in distortions of the generated portrait identity. Has alignment been performed in this context? If so, what techniques are employed for alignment?
- What is the quality of generation for long sequences? Can the author provide quantitative indicators to support their findings?
- Can the author provide a more detailed description of the differences compared to the literature referenced in the Weakness? If the author can offer sufficient explanations to enhance the novelty of the paper, I will consider increasing the score.

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
5

### Summary
This paper improves two-stage co-speech video gesture generation method in two main aspects. Two-stage here is auido2pose and pose2video stages. The authors:

**1. Improve audio2pose stage by contrastive pretraining.**

- The baseline started from a mask represenation learning and Residual VQ-VAE, refer to MoMask [Guo et al. 2024]. The authors modify it to fuse audio feature by cross-attention. 
- The authors pretrain gesture encoders, and audio encoders using a audio2pose contrastive learning. Then, the audio encoder in audio2pose generation stage is initialized by pretrained audio encoder. The gesture encoder, in generation stage is distilled to keep the similarity to pretrained gesture encoder.

**2. improve pose2video stage by learned edge-map for image warping.** 

- The baseline is a pixel-level image-warping based pipeline. Using Thin Plate Splines (TPS) as mentioned in Appendix. G. The image was initially warpped and then refined by network.
- The authors propose a thickness learnable edge heatmap. And using this heatmap to improve the warping results. 

The authors present experiments to show the overall results outperform previous methods, and have the ablation studies for demonstrating each improvement is effective.

### Strengths
The proposals in this paper are correct and have insights:

**1. Improve audio2pose stage by contrastive pretraining.**

The concept of improving the audio2pose generation via contrastive learning pretraining is correct and from the results, it improves the audio2pose generation significantly.  In image generation field, researchers use pretrained text-image CLIP encoder to improve the results. this paper shares the same insight in audio2pose domain. 

**2. improve pose2video stage by learned edge-map for image warping.**

This is a valuable improvement to pixcel-level image warping based approach. Firstly, most of current methods may focus on the improvement of latent-diffusion based methods, but they are typically slow in real-world applications, and have noisy background which require further post-processing. The pixcel-level approach, is very valuable for improvement due to the clean background and faster inference speed. Second, it is correct the most important problem is the correctness of "flow" for warpping based approach, and the thickness of flow is the most important factor. using a learned approach to solve this avoid a lot of manually parameter adjustments.

The experiments, in particular for the ablation part, show the effectiveness of each proposed module.

### Weaknesses
I have a few unclear implementation details.

1. Random mask for contrastive learning training. in Line 211-212. "we random mask 30% ..." I'm confused the mask is in a continues short-sentence level or frame-level. and why it could improve the low-level similarity learning. I suggest writing more explainations here.

### Questions
The questions will influence my score is: 

1. Random mask for contrastive learning training. in Line 211-212. "we random mask 30% ..." I'm confused the mask is in a continues short-sentence level or frame-level. and why it could improve the low-level similarity learning. I suggest writing more explainations here.

2. What is the sequence length used for training the contrastive learning and audio2pose generation?

3. Similarly, what is the resolution for the image training and evaluation stage, will the image-warping based approach suffer a GPU memory issue when resolution increase? 

The question will not influence my score is:

1. some discussion about early stage audio2pose + pose2video work like speech2gestures [Ginoar et al. 2019] and Speech Driven Template [Qian et al. 2021]. in related work section.

### Soundness
3

### Presentation
3

### Contribution
3
