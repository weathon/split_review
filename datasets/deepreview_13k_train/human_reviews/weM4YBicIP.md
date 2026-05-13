# Loopy: Taming Audio-Driven Portrait Avatar with Long-Term Motion Dependency

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
With the introduction of diffusion-based video generation techniques, audio-conditioned human video generation has recently achieved significant breakthroughs in both the naturalness of motion and the synthesis of portrait details. Due to the limited control of audio signals in driving human motion, existing methods often add auxiliary spatial signals to stabilize movements, which may compromise the naturalness and freedom of motion.
In this paper, we propose an end-to-end audio-only conditioned video diffusion model named Loopy. Specifically, we designed an inter- and intra-clip temporal module and an audio-to-latents module, enabling the model to leverage long-term motion information from the data to learn natural motion patterns and improving audio-portrait movement correlation. This method removes the need for manually specified spatial motion templates used in existing methods to constrain motion during inference. Extensive experiments show that Loopy outperforms recent audio-driven portrait diffusion models, delivering more lifelike and high-quality results across various scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes an audio-only conditioned video diffusion model. The model consists of three key components: an inter- and intra-clip temporal module, and an audio-to-latents module. These modules are designed to facilitate long-term movement modeling, enhancing the correlation between audio and motion. During inference, a single reference image as well as the audio is sent as input to autoregressively generate future frames window by window.

### Strengths
1. The proposed method is solid, with enough technical contributions to address the long-term dependency between motions and audio conditions.

2. The experiment results are strong enough compared to prior works and baselines, in particular on FVD metrics and DExp metrics.

3. Both qualitative results and the demos shown in the supplementary webpage are appealing and convincing enough, where the long-term dependencies and correlations between audio and portrait motions are consistently maintained.

4. Overall, the paper is well-written and easy to follow, albeit having many technical details.

5. The human study results clearly show that the proposed method perceptually outperforms other baselines and prior arts.

### Weaknesses
1. For audio-to-latent module, why replacing it with cross-attention module leads to largest performance drop as seen in Table 3. What are missing from cross-attention that makes it fail to perform as good.

2. During inference, audio ratio and ref ratio are manually set for classifier guidance, an ablation study is suggested to their impact on the final quality of generated video to have some insights about this weighting scheme.

3. Could the proposed method be further optimized and adapted to real-time settings, where the audio is being played and video follows interactively?

4. What are limitations of the proposed method and what could be improved? Are there failure cases where the generated motions cannot follow the audio closely?

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
The paper presents Loopy, an innovative audio-driven diffusion model for generating portrait videos that addresses limitations in current methods related to motion naturalness and dependency on auxiliary spatial signals. Existing approaches often compromise the natural freedom of movement by using preset spatial constraints like movement regions or face locators to stabilize motion, leading to repetitive and less dynamic results.

Loopy stands out by adopting an end-to-end audio-only conditioning framework, leveraging two main components: 1. Inter- and Intra-clip Temporal Modules: These modules are designed to extend the model’s temporal receptive field, enabling it to utilize long-term motion dependencies and generate consistent, natural motion across video frames without external movement constraints; 2. Audio-to-Latents Module: This module enhances the correlation between audio input and portrait motion by converting audio features and motion-related characteristics into latent space representations that guide the synthesis process.

Experiments show that Loopy outperforms existing methods, generating lifelike and stable videos with natural facial expressions.

### Strengths
1. The paper introduces an end-to-end audio-only conditioned video diffusion model, which moves beyond traditional methods that rely on spatial constraints for motion stabilization.

2. The proposed novel modules like inter- and intra-clip temporal modules and audio-to-latents module are well-designed, resulting in more natural and consistent portrait movements and leading to better synchronization and more expressive facial movements.

3. The paper includes extensive experiments that demonstrate Loopy’s superiority over other audio-driven portrait diffusion models both quantitatively and qualitatively, with evidence of more lifelike and stable video outputs in the supplemental website.

4. The paper is well-written, the proposed components and architecture are described clearly.

### Weaknesses
1. While the audio-to-latents module improves the audio-motion correlation, there is no mention of how different audio characteristics (e.g., background noise, varying loudness) might impact the model’s performance, which could be critical for real-world applications. Specifically, the paper does not discuss the model's sensitivity to different types of noise (e.g., white noise, babble noise, environmental sounds) or the effect of varying signal-to-noise ratios (SNRs) on the quality of generated videos. Furthermore, the impact of dynamic range compression or expansion in the audio signal on the generated facial movements is not explored, which could be relevant in practical scenarios where audio levels fluctuate significantly.

2. The paper lacks a detailed analysis of potential failure modes or scenarios where Loopy may struggle. Highlighting these cases would provide a more balanced view of the model's robustness and limitations. For example, the paper does not discuss the model's performance when presented with out-of-distribution audio or visual inputs, such as non-human speech, music, or images with unusual poses or occlusions. It would be beneficial to understand how the model behaves under such conditions and whether it exhibits any undesirable artifacts or unstable behavior.

### Questions
1. Are there specific cases where Loopy struggles to maintain natural motion or facial expressions? An analysis of these limitations would provide a more complete understanding of the model’s strengths and weaknesses.

2. In the experiments section, the baseline models compared with Loopy were not trained using the collected dataset. It would be helpful to see how these baseline models perform when trained on the same dataset. This could further validate the effectiveness of the proposed modules and confirm that the performance gains are due to the model’s design, rather than advantages inherent to the dataset itself.

3. Will the collected dataset be made publically available?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes an end-to-end audio-driven portrait video generation method. This method introduces an inter- and intra-clip temporal module and an audio-to-latent module to establish long-term natural correlations between audio and portrait movements. Many lifelike and impressive results are presented.

### Strengths
1. The motivation is clear. The authors focus on the weak correlation between audio and portrait motion in end-to-end audio-driven methods.
2. Overall, this paper is easy to follow. The proposed TSM module is technically sound in its design, and the experimental validation is effective.
3. Many synchronized and vivid portrait videos are generated.

### Weaknesses
1. In the A2L module, the effects of Movement and Expression on the method have not been thoroughly validated. The audio inputs shown in Fig. 4 are somewhat confusing. I assume they refer to audio features from wav2vec. 
2. Human expressions are closely related to many facial details, but the implementation in the paper is rather trivial. 
    1) the detected landmarks are too sparse and not accurate enough (DWPose), which makes it difficult to capture a person's expression accurately. 
    2) using the variance of keypoints to calculate head movement and expression changes presents several practical issues, 
such as the entanglement of head movement and camera movement. Why not use FLAME coefficients or results from other emotion estimation methods? 
3. The TSM module needs a deeper discussion on its impact on overall computational efficiency.
4. In Tables 1 and 2, the methods perform worse than others on some metrics, especially those related to Glo and Exp. The authors do not provide detailed analysis or discussion on this.
5. The paper has several writing issues. Some symbols and abbreviations are introduced without explanation, such as TSM in Fig. 2. Additionally, some text in the figures is too small to read, such as "other computational layers" in Fig. 3. The main paper does not reference Table 2. There are also some typos, such as in Line 302, where there is an error with punctuation.
6. The paper does not include a discussion of the limitations of the proposed method.

### Questions
1. Currently, end-to-end audio-driven portrait generation is typically trained on training sets of varying sizes, which is crucial for a good model. How can we reasonably evaluate the performance of the method?
2. In Table 3, the metrics for audio-visual synchronization related to Loopy w/o TSM and w/o ASL still outperform other methods. Does this indicate that the performance improvement of the method primarily comes from the self-collected data?
3. Regarding training A2L, how do head movements and expressions individually affect the results?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces an audio2video model for co-speech human portrait video synthesis. A novel temporal module is proposed to enable natural movement generation. A joint audio, movement, and expression latent space is learned to achieve better head pose and facial expression control from speech. Experiments and demonstrations show better performance and more realistic results.

### Strengths
1. The results are good. 
2. The introduction of two modules (Temporal and Audio) is reasonable and interesting. Ablation study supports the benefits of these modules.

### Weaknesses
1. Lack of ablation of stand-alone intra- / inter-temporal model. Is both of them necessary or only the inter-clip temporal layer is enough?
2.  The functionality of the Temporal Segment Model is unclear. Is it for capturing the appearance of the character under different expressions? If so, why (L478) longer motion frames lead to worse results?
3. Similar to the above issue. I watched the video samples of the ablated model. Seems to me the ablation of either part leads to similar degradations — lack of head pose variance and subtle expression. This makes me unclear about the different roles of the two proposed modules.

### Questions
1. During inference what if motion frames are provided? How would they influence the results?
2. Can the overall head motion be controlled?
3. (L291) Is there any analysis of the strong correlation between the head movement and expression variances? Can the type of expression be controlled?

### Soundness
4

### Presentation
4

### Contribution
3
