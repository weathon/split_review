# TANGO: Co-Speech Gesture Video Reenactment with Hierarchical Audio Motion Embedding and Diffusion Interpolation

- Decision: Accept
- Avg Score: 8.50
- Scores: 10, 8, 8, 8

## Abstract
We present TANGO, a framework for generating co-speech body-gesture videos. Given a few-minute, single-speaker reference video and target speech audio, TANGO produces high-fidelity videos with synchronized body gestures. TANGO builds on Gesture Video Reenactment (GVR), which splits and retrieves video clips using a directed graph structure - representing video frames as nodes and valid transitions as edges. We address two key limitations of GVR: audio-motion misalignment and visual artifacts in GAN-generated transition frames. In particular, (i) we propose retrieving gestures using latent feature distance to improve cross-modal alignment. To ensure the latent features could effectively model the relationship between speech audio and gesture motion, we implement a hierarchical joint embedding space (AuMoCLIP); (ii) we introduce the diffusion-based model to generate high-quality transition frames. Our diffusion model, Appearance Consistent Interpolation (ACInterp), is built upon AnimateAnyone and includes a reference motion module and homography background flow to preserve appearance consistency between generated and reference videos. By integrating these components into the graph-based retrieval framework, TANGO reliably produces realistic, audio-synchronized videos and outperforms all existing generative and retrieval methods. Our codes and pretrained models are available: \url{https://pantomatrix.io/TANGO/}

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
The paper introduces TANGO, a framework for generating high-fidelity co-speech gesture videos using a motion graph-based retrieval approach. It addresses audio-motion misalignment and visual artifacts in previous methods by implementing two key innovations: the AuMoCLIP, a hierarchical audio-motion joint embedding space for improved cross-modal alignment, and ACInterp, a diffusion-based interpolation network for generating high-quality transition frames. TANGO effectively synchronizes body gestures with speech audio, outperforming existing methods on datasets like Talkshow-Oliver and YouTube Business. The framework represents a significant advancement in gesture video generation, providing an open-source solution that integrates these novel components.

### Strengths
1. Contributions to Retrieval, Interpolation, and Datasets: The paper introduces TANGO, which enhances co-speech gesture video generation through improved retrieval methods, a diffusion-based interpolation model, and the introduction of the YouTube Business dataset.
2. Contribution to Open Source Gesture Generation: By making their code, pretrained models, and datasets publicly available, the authors significantly advance the field of gesture generation and encourage collaboration among researchers.
3. Comprehensive Experiments: The extensive evaluation of TANGO using various quantitative metrics and user studies demonstrates its superiority over existing state-of-the-art methods in generating realistic and audio-synchronized gesture videos.

### Weaknesses
1. Clarification on Graph Pruning Methodology: The paper does not provide sufficient detail on how the strongly connected component (SCC) subgraphs are merged, which is a critical operation in the Graph Pruning section. Specifically, the criteria for merging smaller SCCs into the largest SCC are not clearly defined. The paper mentions merging based on disconnected nodes but lacks specifics on how the decision is made, such as the threshold for the number of disconnected nodes or the size of SCCs that trigger a merge. This lack of detail makes it difficult to reproduce the graph pruning process.
2. Inconsistencies in Visual Representation: In Figure 3, the use of blue and green to represent different video motion clips lacks rigorous color correspondence during transitions, potentially leading to misunderstandings; the transitions between colors are not clearly explained, making it difficult to understand the flow of motion clips. Similarly, Figure 5 uses yellow for both the Wav2Vec2 transformer feature and input audio, which could cause confusion, as these are distinct data modalities and should be visually differentiated.
5. Typographical Errors: There is a typographical error in Figure 4 where "merge" should be corrected to "merging."
4. Testing Results: The generated gesture movements exhibit stuttering, which undermines the fluidity and realism of the videos. This stuttering suggests potential issues in the motion graph sampling or interpolation process, which need further investigation.

### Questions
See weaknesses above.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present a co-speech gesture generation approach through a gesture video reenactment framework. To align video segments with audio, the author proposes an audio-motion joint embedding space using contrastive learning.

Furthermore, an existing diffusion-based, pose-driven video generation model is employed to produce interpolated frames. By incorporating an additional reference motion module and a homography-based background flow, the method achieves improved appearance consistency.

Both qualitative and quantitative comparisons with existing state-of-the-art methods demonstrate that the proposed method outperforms alternatives.

### Strengths
1. Compared to existing works, the video results of the proposed method are strong in terms of both visual quality and audio-gesture alignment.
2.  The authors conduct thorough experiments to validate the effectiveness of the proposed method.
3. In terms of novelty, I would categorize this work as moderate. Although using contrastive learning for audio-motion retrieval is not new, the author deserves credit for applying it within the speech gesture retrieval domain. Beyond this, other contributions seem more incremental, such as adding graph pruning to GVR and incorporating an additional reference motion module and homography-based background flow to the animation process.

### Weaknesses
1. Some claims are not sufficiently justified. For example:

    The author claims, “BERT captures high-dimensional language semantics rather than just ‘audio textures,’ which is critical for the co-speech gesture retrieval task.” However, there is no analysis showing that the addition of BERT features actually generates language-semantics-aware gestures. It’s possible that the performance improvement is due to alignment information alone. If the author could conduct an experiment comparing the use of BERT features with using only CTC alignment information, this might demonstrate the necessity of BERT. Additionally, if the author could provide video examples showing that the generated gestures become more language-semantics-aware with the addition of BERT, it would further support the claim.

2. Since the authors compare their work to other co-speech gesture video generation methods, it would be beneficial to include recent state-of-the-art works, such as *Co-Speech Gesture Video Generation via Motion-Decoupled Diffusion Model (S2GMM).*”If the authors could add this to their evaluation, it would make the proposed work's claim to be state-of-the-art more convincing.

3. Both the objective and subjective evaluations use only one character, Oliver, making it difficult to verify whether the proposed approach would outperform other methods in different circumstances.The authors could perform a comparison experiment with an additional character to demonstrate the generalizability of their approach. Furthermore, if the proposed method does not perform well on characters commonly used by other state-of-the-art methods (e.g., TALKSHOW, PATS), it would be essential to discuss these potential limitations.

4. Writing and formatting improvements are needed for easier comprehension. For example:

- 4.1 Abbreviations:
    
    - GVR stands for Gesture Video Reenactment in the abstract, but GVR is later used to refer to the specific work (Zhou et al., 2022).
        
    - The abbreviation for (Liu et al., 2022c) should be ANGIE, not ANGLE.
        
- 4.2 Tables:
    
    - In Table 2, methods are listed as columns, while in Table 1, they are listed as rows.
        
    - There are no captions to explain some non-trivial numbers in the tables, which could be helpful for interpretation.
        

5. Some explanations and implementation details are unclear or missing. Please refer to the question section for further clarification.

### Questions
1. The appendix mentions, “We evaluate our approach using multiple few-shot sets.” Are each of the proposed models (AuMoCLIP, ACInterp) trained separately on only one of these few-shot sets?

2. The author states, “we leverage the power of the two-stage (pose2image and image2video) video generation diffusion model, AnimateAnyone.” However, there are no details on what "leverage" means in this context. Are they merely using the model’s structural concept, or are they initializing with a pre-trained version of AnimateAnyone?

3. Why does Section 4.4 use a different test set for evaluation?

4. Why are there missing results in Table 3?

5. In Figure 5, why is there a white segment within the low-level and high-level feature representations? According to the paper, it should include only the Wav2vec CNN feature and the Wav2Vec transformer feature with the BERT feature.

### Soundness
3

### Presentation
2

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
This paper proposes a framework for generating co-speech body-gesture videos, dubbed TANGO. TANGO integrates a specifically designed Gesture Video Reenactment (GVR) module, which facilitates the realistic portrayal of gestures, alongside a hierarchical joint embedding space known as AuMoCLIP, which enhances the quality of video generation. The authors conducted extensive experiments that demonstrate the method's superiority over existing approaches in terms of well-rounded metrics and visualization results.

### Strengths
This paper proposes a framework for generating co-speech body-gesture videos, dubbed TANGO. TANGO integrates a specifically designed Gesture Video Reenactment (GVR) module and a hierarchical joint embedding space known as AuMoCLIP to facilitate high-quality video generation. The strengths of this work are summarized as follows:
1. The authors present a novel and robust technical contribution through the introduction of a graph network baseline that adaptively incorporates the GVR and AuMoCLIP modules.
2. The motivation for this research is clearly articulated, and the insights provided are compelling. It is important to highlight that a unified framework for co-speech gesture modeling from audio to video sequences holds significant relevance in this community.
3. The dataset introduced in this paper is designed to facilitate ongoing research in gesture generation, providing valuable resources for future studies.
4. The visualization results are well-executed, allowing reviewers to thoroughly evaluate the findings and methodologies presented.

### Weaknesses
However, there are still some questions for me. I encourage the authors to give reasonable responses. The final rating would be raised if the solution can solve my concerns.
1. Some important related works might be missed, and I encourage the authors to discuss with them. For example, both of these two methods leverage the audio signal as input to generate human postures.
 
[1] Qi, X., Pan, J., Li, P., Yuan, R., Chi, X., Li, M., ... & Guo, Y. (2024). Weakly-Supervised Emotion Transition Learning for Diverse 3D Co-speech Gesture Generation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 10424-10434).

[2] Mughal, M. H., Dabral, R., Habibie, I., Donatelli, L., Habermann, M., & Theobalt, C. (2024). ConvoFusion: Multi-Modal Conversational Diffusion for Co-Speech Gesture Synthesis. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 1388-1398).

2. In the experimental setting, it is very interesting to explore the frame interval with different settings rather than 4. Please note that this is not an ask for additional experiments in the rebuttal, and this does not impact the paper score. I encourage authors to conduct this discussion in the future.

3. In the user study, did the authors assess participant engagement, specifically regarding whether responses were submitted too quickly or too slowly, and whether any such responses should be discounted? For example, whether the authors considered using response time thresholds or including control questions to check for consistent responses. I encourage authors to add these discussions in the appendix.

### Questions
Please refer to Weaknesses.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents TANGO, a novel framework for generating co-speech body-gesture videos that effectively synchronizes gestures with speech audio. The key contributions of TANGO include:

Motion Graph-Based Retrieval: TANGO enhanced the motion graph-based model with more fine-grained designed AuMoCLIP to obtain relevant body gestures that align with the audio input, enhancing the realism and relevance of the generated gestures.

Diffusion-Based Interpolation Network: The framework utilizes a diffusion-based approach for video frame interpolation, which improves the quality and fluidity of the generated videos, addressing limitations found in previous methods.

The authors conduct extensive evaluations, including both objective metrics and user studies, demonstrating that TANGO outperforms existing methods like Gesture Video Reenactment (GVR) and Speech-Driven Templates (SDT) in terms of video quality, audio-motion alignment, and overall user preference.

### Strengths
For the method design:

1. This work presents a retrieval framework for gesture generation. It resolved a significant issue by the former work GVR (retrieval naively relies on audio onset features and keyword matching) 

2. The author represent the gesture patterns within the video as graph and present an efficient pruning strategy to achieve long-sequence representation. This strategy seems effective.

3. The author propose the AuMoCLIP for aligning the two modalities and demonstrate an effective merging of text semantics, high-level audio, and low-level audio features. The ablation study for low-level and high-level retrieval is insightful with very detailed analysis and design. The author analyzed how the temporal alignment of two modalities can be achieved and also the high level semantics.

4. While uplifting the geature pattern generation to the pixel-level video synthesis, the author did not simply reply on commonly used ReferenceNet-like modules but in addition propose homography background offset flow for the consideration of camera changes for realistic videos. The author did very deep analysis of temporal dependencies and resolved the background and jittering problems introduced by camera motion commonly seen in video generations.


For potential insight and benefits for Future studies:
1. Auto-Evaluation: The AuMoCLIP seems to be a very good generalizable evaluation method for automatic evaluation of gesture motion naturalness conditioned on speech. Unlike FGD, diversity or Beat Alignment (BAS), which cannot precisely include the naturalness of motion patterns, the semantics or beat alignment of audio and speech, this model might be very beneficial for future auto-evaluations, though the author did not propose this point.

2. Audio and Gesture Motion Modality alignment: Previous works in this domain have very limited analysis of the how the speech signal functions as the trigger for gesture patterns. Many previous works, (like DiffSheg, CaMN, TalkShow, EMAGE, AMUSE, etc) only designed the generator by incorporating the audio features or text as the control signals to drive the gesture generation but never analyzed how the inner relationships of different modality should be. GestureDiffuCLIP did preliminary studies in aligning the speech word context and gesture motion patterns but ignored the temporal alignment between modalities. In this work, the author did very detailed analysis of the low-level retrieval and high-level retrieval, reconsider the temporal alignment and semantic alignment (low-level indicates the temporal alignment, I consider the local temporal contrastive loss might functions for the beat-dynamic of the gestures, high-level indicates the global semantic alignment of the two modalities. The ablation of the retrieval is very insightful)

### Weaknesses
1. The dataset for comparison are limited. The author only selected Oliver in the Show dataset and a small scale in-the-wild YouTube videos. (However, as far as I know, this filed lacks of high-quality data, PATS is another option, but it contains too many low-quality/low-resolution videos and blurry frames for large shoulder and hand motions)

2. It seems like the temporal contrastive learning is based on the low-level features obtained from the CNN encoder. I am not quite sure if I understand it correctly. It will be better if the author can include this information in the final draft for easy understanding.

3. For the method design, in case I am uncertain of some technical details, I will present some potential weakness in the Question section instead of here.

4. For the gesture motion representation, the author utilized 3D SMPL/SMPL-X template model parameters. I assume the author based on the first frame of the given image, do the tracking to obtain the camera and based on the camera to project the generated 3D joints onto the 2D-space for image-level pose guided generation. I think the author could add this information to the final draft.

5. Some of the training details of the model is missing, like what are the GPUs for training, time for training, learning rate.

### Questions
1. Representing the gesture as the motion graph: While it is good to represent the gesture patterns from the video as the graph, the retrived features are discrete tokens not uniformly sampled. Will this reduce the quality of gesture generation as the speech audio in natural should be continuous?

2. It seems like for high-level representation, the author only used one transformer layer upon the low-level features from CNN encoders. Is it possible the limited number of transformer level leads to a low performance for the global retrieval? I have this doubt because the author draw inspiration from Wav2Vec 2 for the model design. However, Wav2Vec ustilized 11 transformer layers upon the CNN encoder and the self-supervised learning is also based on the transformer layer feature. Is it possible adding additional layers of transformers can help improve the high-level retrieval?

3. For one technical detail of the paper, why random search of low-level retrieval has a 25% accuracy? In addition, can the author include some other metrics like F1 score, recall? There should be mostly negative samples for the retrieval if my understanding is correct.

4. One further question based on weakness 3, why the temporal contrastive learning is used for the low-level feature instead of applied to high-level features from transformer layers?

5. Refer to Weakness 5, I am assuming the the camera during inference will be kept the same. One claim the author mentioned is "homography background offset flow to eliminate artifacts due to camera parameter changes". Does this only apply for the training but not inference for stablizing training?

### Soundness
4

### Presentation
4

### Contribution
4
