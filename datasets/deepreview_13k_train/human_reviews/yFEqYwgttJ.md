# MDSGen: Fast and Efficient Masked Diffusion Temporal-Aware Transformers for Open-Domain Sound Generation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
We introduce \texttt{MDSGen}, a novel framework for vision-guided open-domain sound generation optimized for model parameter size, memory consumption, and inference speed. This framework incorporates two key innovations: (1) a redundant video feature removal module that filters out unnecessary visual information, and (2) a temporal-aware masking strategy that leverages temporal context for enhanced audio generation accuracy. In contrast to existing resource-heavy Unet-based models, \texttt{MDSGen} employs denoising masked diffusion transformers,  facilitating efficient generation without reliance on pre-trained diffusion models. Evaluated on the benchmark VGGSound dataset, our smallest model (5M parameters) achieves $97.9$\% alignment accuracy, using $172\times$ fewer parameters, $371$\% less memory, and offering $36\times$ faster inference than the current 860M-parameter state-of-the-art model ($93.9$\% accuracy). The larger model (131M parameters) reaches nearly $99$\% accuracy while requiring $6.5\times$ fewer parameters. These results highlight the scalability and effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
**Update after discussion period**:

My biggest concern of this paper is about its audio reconstruction pipeline. The original pipeline consists of an RGB VAE and a non-DNN mel2wave conversion module, resulting in terrible sound quality. Moreover, such a pipeline has been used in video2audio community widely, which is a pity.

During the rebuttal period, the authors not only added the experiment of using a vocoder for the mel2wave conversion, but also re-trained their models with an audio VAE. As a result of their efforts, the FAD score improved from 4.37 to 2.16 and eventually 1.34. Congrats on the achievement!

I listened to the latest samples in the Google Drive, and found a distinct advantage of audio VAE in samples that contain non-noise or musical sources (sample027__SrU3mfTPYg_000032.mp4, sample045_2es7oZzwLWM_000030.mp4). Although the AV-align score is slightly worse with an audio VAE, the score is still higher than conventional methods by a large margin.

Since the AV-align score is computed by a pretrained DNN model, moreover, considering the gap between v2a community and audio generation community, the metric might not be very reliable. For example, in samples such as "sample007_-2sOH8XovEE_000484.mp4", I don't feel the alignment is as good as the scores indicate. Perhaps some future works can be done to further improve the metric itself.

I increased my ratings to **encourage further collaboration between video2audio and audio communities**.

---------------

The paper proposes "MDSGen", an efficient model based on Masked Diffusion Transformer, for video-to-audio generation.

The challenges of video-to-audio generation are mainly:
1. Heavy computation and memory usage;
2. Requirements for the audio quality;
3. Requirements for the audio-video alignment;

MDSGen reduces the resource consumption by using very light-weight Transformer coupled with fast diffusion samplers such as DPM solver, as well as a dimension reduction module to reduce the size of the video conditioning embeddings.

MDSGen improves audio quality and audio-video quality by introducing a time-aware masking strategy into the mask DiT framework, together with other efforts.

Conceptualy, MDSGen looks like a framework that replaces the "text prompt" in text-to-audio DiT [StableAudioOpen],[MakeAnAudio2] by a video feature embedding. Hence the technical contributions are more in micro aspects.

However, some design choices may have severely affected the audio quality, making the work less solid or reusable to the community. Audio quality observed in the supplementary files is far from the level in modern text-to-audio models such as [AudioLDM], [MakeAnAudio2], [SpecMaskGIT], [StableAudioOpen].

### Strengths
Most contributions of MDSGen are about micro design aspects.
1. Channel selection of Mel-spec
2. Time-aware masking strategy for generative models
3. Reduced dimension of the video features
4. Small model size and fast inference speed

### Weaknesses
## Major issues
### 1. Improper audio reconstrution pipeline
MDSGen ustilizes the VAE from Stable Diffusion, which is not trained for Mel-spec. Although the authors carefully discussed how to take the most advantage of this image VAE, the discussion itself is **NOT** reusable for the audio community, as there have been plenty of audio VAE designs, some of which are publicly available such as [AudioLDM], [MakeAnAudio2], [StableAudioOpen], [DAC]. The use of an image VAE, even with careful adaptation, inherently limits the quality of the reconstructed audio, as these VAEs are optimized for visual data, not the specific characteristics of mel-spectrograms. This mismatch leads to suboptimal feature encoding and decoding for audio signals, resulting in a loss of fidelity and detail. The community has developed specialized audio VAEs that capture the nuances of audio data much more effectively, and these should be considered for a robust audio reconstruction pipeline.

Another improper choice is that, MDSGen utilizes the Griffin-Lim Algorithm (GLA) to convert mel-spec back to wave forms. GLA has almost been abandoned by audio community, due to the recent advance in neural vocoder, e.g., [HiFiGAN], [UnivNet], [BigVGAN]. I believe the apparent phase distortion in the supplementary files might have been caused by GLA. The GLA algorithm is known for its limitations in accurately reconstructing phase information, which is crucial for high-quality audio. Modern neural vocoders, on the other hand, are trained to learn complex phase relationships and can generate much more realistic and artifact-free waveforms. The use of GLA introduces unnecessary distortion and limits the overall audio quality achievable by the model.

There is a rough comparison on the quality of audio reconstruction pipeline in a recent paper [SpecMaskGIT], I hope it could be useful for the improvement of MDSGen.

I strongly recommend the authors to consider audio-specified reconstruction pipelines for improved audio quality. Even in audio-visual generation community, we can see the usage of such audio VAE for excellent audio quality, e.g., [VisualEchoes]
### 2. Invalid claims on the result
Because the audio quality is far from the baseline in audio generation community, it is improper to claim that MDSGen is better in "audio-video alignment". The current audio quality issues make it difficult to assess the true alignment capabilities of the model. The alignment metric, while seemingly objective, might be biased by the poor audio quality, leading to misleading results. A model with low audio quality might still achieve a high alignment score if the alignment classifier is not robust to such artifacts. Therefore, the reported alignment scores should be interpreted with caution.

I believe, the audio-video alignment can be evaluated only when the audio quality is sufficiently good. Given the current audio quality, I don't think the model is ready for further evaluation.
## Minor issues 
### 1. Evaluation metrics
The FID used in this paper comes from the implementation of SpecVQGAN, a pioneer of audio generation. However, the FAD implementation ([AudioLDM],[FAD_github]) has been more widely accepted in audio community. Evaluating with the widely adopted FAD metric can also help the readers to compre the audio quality with other audio generation models.
### 2. Insufficient ablation study
MDSGen trains a learnable module to reduce the video feature sequence into a single vector. From Figure 6, we can observe that the learned weights are quite evenly distributed (except the beginning and ending frames).

The observation posts a question: How much improvement can the learnable reducer bring compared to a naive average pooling?

### Questions
Three models are presented in the paper (Tiny, Small and Base) except the overfitting large model. What is the model presented in the supplementary files?

Is there any reason to use an image VAE instead of audio VAEs? 

Did the authors observe any advantage of GLA over a neural vocoder?

Is it possible to run a subjective listening test, and see the consistency between human evaluation and the audio-video alignment accuracy measured by a DNN model?

Could the authors measure the FAD scores on top of the current FID scores?

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents MDSGen, an efficient framework for vision-guided sound generation that minimizes model size, memory usage, and inference time. Key innovations include a temporal-aware masking strategy to enhance alignment accuracy and a redundant feature removal module to filter unnecessary video information. Using a lightweight masked diffusion transformer, MDSGen outperforms larger Unet-based models on VGGSound and Flickr-SoundNet, achieving high synchronization and alignment with significantly reduced computational costs.

### Strengths
The paper introduces a novel framework for video-to-audio sound generation that effectively combines a temporal-aware masking strategy with a redundant feature removal module. 

MDSGen demonstrates significant improvements in model efficiency by using a smaller masked diffusion transformer architecture. The framework achieves high alignment accuracy on benchmark datasets with a fraction of the parameters, memory usage, and inference time compared to baselines. 

The paper provides a structured explanation of MDSGen’s architecture and mechanisms, including the Temporal-Awareness Masking (TAM) and the Reducer module for filtering out redundant features. Extensive experimental results on VGGSound and Flickr-SoundNet datasets clearly validate the method’s effectiveness, with MDSGen achieving superior performance across alignment accuracy and efficiency metrics.

### Weaknesses
1. Lack of Novelty and Contribution: The paper presents the primary contributions are the Temporal-Awareness Masking (TAM) strategy and the visual Reducer module. However, masking strategies have been widely explored in audio generation research, as seen in works like [1, 2], and the specific concept of Temporal-Awareness Masking has been studied in [3, 4]. The visual Reducer module, primarily a 1x1 convolutional layer (line 181), lacks detailed design innovations, which limits its distinctiveness and impact.

2. Insufficient Exploration of Design Choices: For video-to-audio generation, the choice of video encoder plays a crucial role in understanding the video content. Clarification on the selection of CAVP as the video encoder would add valuable insight. Additionally, the paper could explore using more video encoders, such as CLIP [5], VideoMAE [6], ViVit [7], and TAM [8], which could enrich the technical depth of the proposed method.

3. Presentation and Writing:
Some claims in the paper lack supporting evidence, such as the statements in lines 183-185 that the proposed method “minimizes redundant features that could lead to overfitting” and in line 224 that setting N_2 = 4 “gives better performance for audio data.” These points would benefit from empirical support to substantiate their validity.

4. Supplementary Material: The quality of generated audio samples in the supplementary material raises concerns regarding the overall quality of results produced by the proposed method, which may affect its effectiveness and appeal.

### Questions
Please see Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces MDSGen, an innovative framework designed for vision-guided open-domain sound generation with a focus on optimizing model parameter size, memory consumption, and inference speed. It features two major innovations: a redundant video feature removal reducer and a temporal-aware masking strategy. Utilizing denoising masked diffusion transformers, MDSGen achieves efficient sound generation without the need for pre-trained diffusion models. On the VGGSound dataset, the smallest MDSGen model demonstrates a 97.9% alignment accuracy while using fewer parameters, consuming less memory, and performing faster inference compared to the current state-of-the-art models. The results underscore the scalability and effectiveness of this approach.

### Strengths
1. The idea of compressing visual representations into one single vector is bold and intriguing, which reduces significant computing pressure on the DiT side.
2. The proposed TAM strategy is interesting and makes sense. Previous works about masking audio representations, such as AudioMAE, have drawn conclusions that the unstructured masking strategy is superior, which contradicts the conclusion in this paper. I believe this paper brings more insights into this topic. 
3. The authors have conducted tons of ablation experiments to support their model design and parameter decision, making the conclusions plausible.

### Weaknesses
1. The major concern is about the modeling of audio representations, as I am familiar with this field. I believe that Mel spectrum is more of a 1D feature rather than 2D, because the spectrum does not satisfy translational invariance (if a formant chunk in a spectrum is moved from the bottom left to the top right, the semantics of the sound are likely to be completely destroyed), and the frequency domain and time domain cannot simply be simulated by spatial coordinates. A relevant observation in this paper is that a complete random masking strategy is underperformed by the temporal-aware masking strategy. Therefore, I believe that considering Mel spectrograms as gray-scale images and modeling them using 2D VAE pretrained with real images is suboptimal, which further prevents modeling sounds with varying lengths. There are already approaches that model audio using 1D VAE, such as Make-an-audio 2. So can the authors provide justifications for choosing 2D rather than 1D? In my view, choosing 1D combined with the TAM strategy could form a more compelling motivation.
2. The idea of compressing visual representations into one single vector is intriguing. However, I don't understand why this could work. How does one single vector provide accurate information about temporal position? I believe Diff-foley works because it adopts a sequence-to-sequence cross-attention mechanism, which provides rough sequential and positional information for the audio to follow. Could the author provide further analysis and discussion on this point? For example, analyzing the components related to temporal position within that vector, or the relation of the learned weights of reducer between key frames of videos.
3. Similar concern: the learned weights of reducer seem to be focused more on the head and tail frames of videos. Does this imply that the reducer is more focused on global video information? How can it be determined that it is capable of extracting local positional information?
4. The alignment classifier proposed in Diff-foley only reaches 90% accuracy on their test set. However, the best performance in this paper reaches 98+. How could this happen? Is the classifier involved during the training process?

### Questions
1. The reducer is designed to have fixed weights, serving as a weighted average of all the frames. However, the sound events of different videos are distinct, so why not adopt a dynamic weighted average strategy, e.g., attention pooling?
2. What is the exact implementation of the model? How is the visual conditioning (i.e., $p(x|v)$) implemented?

### Soundness
3

### Presentation
4

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
This paper presents MDSGen, an efficient and compact framework for generating open-domain sounds guided by visual input. MDSGen uses masked diffusion transformers instead of the usual U-Net architectures, optimizing for faster speed, lower memory use, and parameter efficiency. Key features include a module to remove redundant video data and a Temporal-Awareness Masking (TAM) strategy, both aimed at efficient, high-quality audio-visual alignment. Tests on the VGGSound and Flickr-SoundNet datasets show that MDSGen achieves strong alignment accuracy with much lower computational demands than larger models.

### Strengths
1. MDSGen achieves strong results with a small model size, making it useful for real-time applications. Compared to larger models, it is faster and more memory-efficient.
2. TAM is an interesting approach that focuses on time-based information in audio, aiming to improve alignment by using masking based on temporal patterns rather than spatial patterns (commonly used for images).
3. The paper provides extensive experiments with detailed comparisons against other models. Ablations for each key component further clarify the model’s design choices.

### Weaknesses
1. I question the decision to use an image-trained VAE (from Stable Diffusion) rather than an audio-specific VAE, such as those in AudioLDM [1]. An audio-dedicated VAE could better capture the temporal and spectral nuances inherent to sound, which are often lost when treating audio as an image. Relying on an image-based VAE reduces the model’s potential to fully leverage audio-specific features and may affect TAM’s performance. Specifically, the image VAE may not be optimized for the complex time-frequency relationships present in audio, potentially leading to a loss of fidelity in the reconstructed spectrograms and limiting the effectiveness of the temporal masking strategy.
2. The authors highlight channel selection within the RGB output as a means of optimizing the final mel-spectrogram. While using the G channel showed marginal improvements, I question if relying on such RGB channel selection can sufficiently address the nuances of audio spectrogram representation (similar to 1). A more audio-specific solution that doesn’t require treating spectrograms as RGB images would likely be more consistent with the needs of audio data, as these channels are meant for pixels, not spectral data. The inherent structure of RGB channels is designed for spatial information, not the spectral and temporal information present in audio spectrograms. This approach may lead to suboptimal feature extraction and limit the model's ability to capture fine-grained audio details.
3. I would suggest that the authors conduct a human perceptual study to better assess audio quality. Relying solely on quantitative metrics may not fully capture perceptual quality, as these measures can sometimes be unreliable. Metrics like FAD and alignment accuracy, while useful, do not always correlate perfectly with human perception of audio quality and realism. A subjective evaluation is necessary to validate the model's output.
4. In Section 5.4, various masking strategies are explored, and TAM shows a clear improvement over random masking and FAM. However, the reasons for TAM’s superiority are not fully explained. It would be beneficial to discuss why TAM outperforms FAM in this context, particularly since FAM is intuitively suitable for audio data. The paper lacks a detailed analysis of how temporal masking specifically benefits the model's ability to learn audio representations compared to frequency-based masking. A more thorough explanation of the underlying mechanisms is needed.
5. I noticed a missing citation for SpecAugment [2] and AudioMAE [3], a masking approach relevant to TAM proposed here.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
4
