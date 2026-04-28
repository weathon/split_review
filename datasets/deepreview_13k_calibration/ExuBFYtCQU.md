# MaskGCT: Zero-Shot Text-to-Speech with Masked Generative Codec Transformer

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 3, 6, 6

## Abstract
The recent large-scale text-to-speech (TTS) systems are usually grouped as autoregressive and non-autoregressive systems. The autoregressive systems implicitly model duration but exhibit certain deficiencies in robustness and lack of duration controllability. Non-autoregressive systems require explicit alignment information between text and speech during training and predict durations for linguistic units (e.g. phone), which may compromise their naturalness.
In this paper, we introduce \textbf{Mask}ed \textbf{G}enerative \textbf{C}odec \textbf{T}ransformer (MaskGCT), \textit{a fully non-autoregressive TTS model that eliminates the need for explicit alignment information between text and speech supervision, as well as phone-level duration prediction}. MaskGCT is a two-stage model: in the first stage, the model uses text to predict semantic tokens extracted from a speech self-supervised learning (SSL) model, and in the second stage, the model predicts acoustic tokens conditioned on these semantic tokens. MaskGCT follows the \textit{mask-and-predict} learning paradigm. During training, MaskGCT learns to predict masked semantic or acoustic tokens based on given conditions and prompts. During inference, the model generates tokens of a specified length in a parallel manner. 
Experiments with 100K hours of in-the-wild speech demonstrate that MaskGCT outperforms the current state-of-the-art zero-shot TTS systems in terms of quality, similarity, and intelligibility. Audio samples are available at \url{https://maskgct.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a masked generative codec transformer, MaskGCT, which performs speech synthesis using a mask-predict approach. MaskGCT generates semantic tokens from text input and is composed of two components: text-to-semantic MaskGCT, which generates semantic tokens from text, and semantic-to-acoustic MaskGCT, which generates acoustic tokens from semantic tokens. Each MaskGCT operates by filling masked parts based on confidence scores predicted in stages, from a sequence where all discrete speech tokens are masked at the start. Instead of using the commonly used method of obtaining semantic tokens through k-means clustering applied to pre-trained SSL models, MaskGCT employs a separate VQ-VAE model on SSL features to generate semantic tokens, reducing information loss through reconstruction loss. MaskGCT uses a similar mask prediction method for predicting discrete speech tokens as Soundstorm, which is based on MaskGIT. However, unlike Soundstorm, MaskGCT approaches the semantic token generation from text through masked token modeling and includes an additional module for total length prediction to align sequence lengths. MaskGCT demonstrates superior speaker similarity in widely used zero-shot TTS evaluation compared to various zero-shot TTS models. Moreover, a demo page with samples shows the versatility of MaskGCT across various tasks.

### Strengths
* The paper shows that a mask-predict approach on discrete tokens can achieve a high level of speaker similarity. 

* Samples on the demo page show that MaskGCT enables zero-shot TTS that effectively captures not only timbre but also emotion and style across a variety of voices, with excellent sample quality. 

* To assess how well the model captures accent and emotion, the paper introduces metrics such as Accent SIM and Emotion SIM, which utilize representations reflecting each attribute. Their results indicate that MaskGCT performs better in imitating accent and emotion than other approaches based on these metrics.

### Weaknesses
 * In Soundstorm, the mask-predict approach is introduced to acoustic token generation. It seems that the methodological novelty in MaskGCT lies mainly in extending this mask-predict approach to semantic token generation.

* The paper utilizes VQ-VAE to reduce information loss in semantic tokens compared to the k-means clustering approach; however, it does not experimentally demonstrate how this approach improves over k-means clustering.

* Additionally, while using a larger number of semantic tokens may yield good performance in zero-shot TTS, the semantic tokens do not seem disentangled from speaker information, making MaskGCT less suitable for voice conversion tasks. The voice conversion samples on the demo page also appear less similar to the reference speaker.  

* When comparing single-sample generation, MaskGCT's pronunciation accuracy appears lower than that of VoiceBox or NaturalSpeech 3.

* Regarding the seed-TTS evaluation method, although it is not explicitly shown as a baseline in the paper, the objective metrics appear to be worse than those of seed-TTS.

### Questions
Comments

* It would be helpful to mention the frame rate of semantic and acoustic tokens.
* I am curious whether only a single sampling step is used from the third layer during acoustic token generation. Is there any difference when using more sampling steps?
* It would be beneficial to also present the overall sampling speed of the model, including the Real-Time Factor.
* In Table 1, it seems that VoiceBox's Imp. Dur. should be marked as "X."

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces MaskGCT, a non-autoregressive (NAR) masked generative modeling method that sequentially generates audio from acoustic tokens, semantic tokens, and text. The semantic tokens are derived from VQ-VAE of W2V-BERT, a self-supervised speech learning model. The acoustic token approach extends DAC with improved training efficiency.

Results demonstrate that MaskGCT either outperforms or matches current autoregressive (AR) based methods and NAR duration-based methods with publicly available implementation details, across multiple benchmarks: LibriSpeech, SeedTTS (Chinese and English), zero-shot TTS, and speech style (timbre, emotion, accent, etc.) imitation learning. Additionally, MaskGCT surpasses AR-based methods in both naturalness and computational efficiency (inference time steps).

### Strengths
* This paper experimentally demonstrates that NAR (non-autoregressive) non-duration-based TTS methods outperform both AR (autoregressive) based and NAR duration-based TTS methods with publicly available implementation details. 

* The open-source implementation and comprehensive reproducibility details provided in the appendix represent valuable contributions to the field.

* The paper is well-structured, with clear presentation and thorough technical descriptions.

### Weaknesses
Major Concerns:

* The novelty and technical contribution appear limited. The core methodology seems to be primarily a combination of existing work (MaskGIT and SpearTTS). The speech acoustic code is derived from DAC, with no apparent novel methodological contributions.

* Regarding NAR methods, the authors cite phone-level duration prediction as a source of complex model design. However, this claim needs clarification: How is this complexity measured (e.g., training time, loss balancing)? Why are AR-based methods considered less complex? Experience with NaturalSpeech3/Fastspeech2 suggests duration modeling is manageable and straightforward to implement. Does this conclusion apply to traditional small-scale TTS models? The statement appears overly generalized.

* The Related Work section overlooks prominent flow-based methods like VoiceBox and p-flow, which also employ masked generative models. Their exclusion from this category requires explanation.

* Table 1 would be more appropriate in the appendix. Multi-task capability alone is not a significant contribution, as multi-task frameworks are common. The focus should be on concrete improvements in naturalness, prosody, efficiency, or reduced complexity. Placing Table 1 prominently suggests multi-task functionality is the main contribution, which diminishes the paper's actual value.

* In line 210, the claim that k-means based discrete SSL units lead to information loss needs substantiation. Why is VQ-VAE of W2V-BERT considered superior for semantic preservation despite also being discrete SSL units? While Appendix B provides semantic and acoustic comparisons, direct evidence supporting this specific claim is lacking.

Minor Points:

* Figure 2 would benefit from additional notations for clarity. Also, what is the difference between prompt semantic tokens and target semantic tokens? Can you give an example?

* While following the text-semantics-acoustics pipeline established by papers like SpearTTS, the superiority of this approach over alternatives (e.g., direct text2acoustic without semantics) should be justified.

* Section 4.2.3's purpose and motivation need clarification, particularly if addressing speed modification, as specialized tools exist for this purpose.

* Consider whether inference steps alone adequately measure efficiency, or if other metrics common in streaming methods (e.g., latency) would provide more comprehensive evaluation.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

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
The authors present a zero-short text-to-speech (TTS) system called Masked Generative Codec Transformer (MaskGCT), which comprises two stages: 1) predicting semantic tokens from text and 2) using these semantic tokens to generate acoustic tokens. Both stages leverage a non-autoregressive masked generative transformer with specific prompt tokens for in-context learning. A VQ-VAE codec and a residual vector quantization (RVQ) codec are separately trained to obtain the semantic tokens and acoustic tokens. Extensive experiments across various tasks demonstrate that MaskGCT, trained on 100k hours of speech data, surpasses existing state-of-the-art zero-shot TTS systems in quality, similarity, and intelligibility.

### Strengths
- This work utilizes non-autoregressive masked generative transformers to generate both sematic tokens and acoustic tokens, offering advantages such as flexible length control, better robustness, and higher inference efficiency. This is suggested by the experiments in Section 4.2.2, comparing to the system replacing the first stage with an autoregressive model (i.e., AR + SoundStorm). 
- The authors conduct extensive experiments on a variety of tasks to evaluate the effectiveness and sca of the proposed system, including not only standard zero-shot TTS, but also cross-lingual dubbing, voice conversion, emotion control, and speech content editing, with potential use of post-training and fine-tuning. 
- The selected state-of-the-art baselines are well-chosen.

### Weaknesses
 - The novelty of this work is somewhat incremental, though I would appreciate its engineering contributions. This work follows a two-stage codec-based sequence-to-sequence strategy, converting text into semantic tokens and then into acoustic tokens, which is in line with SPEAR-TTS [1]. The SoundStorm [2] paper also explores this strategy. Additionally, the idea of applying non-autoregressive masked generative transformer for codec-based TTS is presented in SoundStorm [2] and NaturalSpeech3 [3] (though the NaturalSpeech3 paper describes it from a diffusion perspective.). However, I would like to highlight the distinction that this work employs non-autoregressive masked generative transformers in both stages of the two-stage framework.
- The authors emphasize that the proposed method does not require text-speech alignment supervision or phone-level duration prediction. However, it appears that the method does require a specified length for the target semantic token sequence, thereby to control the length of the generate speech. The presented experimental results in Table 2, comparing to baseline methods, are based on either ground-truth duration or predicted duration. As descibed in the paper, the authors train a duration predictor to estimate the phone-level durations, which are then summed to determine the total duration of the target speech. This process relies on pre-computed ground-truth phone-level durations. Therefore, it seems that this may not fully align with the claim of not requiring text-speech alignment supervision or phone-level duration prediction.
- The authors claim that training a VQ-VAE model to quantize the semantic representation can reduce the information loss, compared to using k-means clustering as in previous works. I think it would be better if the authors can provide ablation results or relevant references to support this assertion.

### Questions
- In Table 1, does "ZS TTS" denote "zero-shot TTS", and what's "CL TTS"? For "Imp. Dur.", I also don't fully agree that this work implicitly models duration, as it requires a specified length of the target generated speech.  
- In Section 3.2.3,  why "the number of frames in the semantic token sequence is equal to the sum of the frames in the prompt acoustic sequence and the target acoustic sequence"? 
- Is the output length of the text-to-semantic stage equal to that from the semantic-to-acoustic stage? From Figure 2, the former seems shorter than the latter? 
- In the first paragraph of Section 2, about "SpearTTS utilizes three AR models to predict semantic tokens from text, coarse-grained acoustic tokens from semantic tokens, and fine-grained acoustic tokens from coarse-grained tokens.", the terms "coarse-grained" and "fine-grained" do not seem to be mentioned in the SpearTTS [1] paper, what do the authors mean by them? 
- What's the length of prompt audio? Does it affect the quality of the generated speech?

[1] Kharitonov, E., Vincent, D., Borsos, Z., Marinier, R., Girgin, S., Pietquin, O., ... & Zeghidour, N. (2023). Speak, read and prompt: High-fidelity text-to-speech with minimal supervision. Transactions of the Association for Computational Linguistics, 11, 1703-1718.

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
4

### Summary
This paper presents MASKGCT, a compact Non-Autoregressive (NAR) text-to-speech model. This model is meticulously designed with a specific emphasis on attaining outstanding audio quality. What sets it apart from prior works is its utilization of semantic tokens extracted from the SSL representation using VQVAE and its avoidance of relying on explicit alignment information.

### Strengths
- This paper offers quite interesting and remarkably high-quality demo audio. The audio samples provided within the paper not only demonstrate clear and distinct sound qualities but also exhibit a certain level of innovation in terms of the audio characteristics they present. They are able to effectively capture the attention of the readers and give a practical sense of the research outcomes in the audio domain.
- The proposed pipeline is significantly more compact than previous ones such as NaturalSpeech3. This compactness implies a more streamlined and efficient design. It potentially leads to reduced computational complexity and may offer advantages in terms of implementation and resource utilization.

### Weaknesses
 - The Word Error Rate (WER) in Table 4 and 5 of all methods is much higher than previously reported. This discrepancy requires more in-depth explanation. It is essential to analyze the factors contributing to this higher WER, such as possible differences in the data sets used, the experimental settings, or any unique characteristics of the methods employed in this study. A detailed exploration and clarification of these aspects would enhance the understanding and validity of the results presented.
- In Section 3.2.1, the authors utilize VQVAE to obtain discrete semantic tokens instead of k-means. However, no corresponding experiment result is provided. It would be beneficial to include the experimental results related to the use of k-means for a more comprehensive understanding. These results could demonstrate the effectiveness and performance of VQVAE in this context, and also facilitate a comparison with the potential outcomes if k-means had been used. This would add more substance to the discussion and support the authors' choice of using VQVAE.
- To my knowledge, using text as a condition without expanding by duration for a Non-Autoregressive (NAR) model was first proposed in e2-tts. The authors should point out this in Section 3.2.2. Acknowledging the prior work in this area is important for providing a complete context and showing the evolution of the research. By highlighting the connection to e2-tts, the authors can better position their work within the existing body of knowledge and give credit to the relevant pioneering research. It also helps readers to better understand the background and significance of the approach taken in this study.

### Questions
Address my concerns in the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
