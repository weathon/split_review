# VoiceNoNG: High-Quality Speech Editing Model without Hallucinations

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
Currently, most advanced speech editing models are based on either neural codec
language models (NCLM) (e.g., VoiceCraft) or diffusion models (e.g., Voicebox).
Although NCLM can generate higher quality speech compared to diffusion models,
it suffers from a higher word error rate (WER) (Peng et al., 2024), calculated by
comparing the transcribed text to the input text. We identify that this higher WER
is due to attention errors (hallucinations), which make it difficult for NCLM to
accurately follow the target transcription. To maintain speech quality and address
the hallucination issue, we introduce VoiceNoNG, which combines the strengths of
both model frameworks. VoiceNoNG utilizes a latent flow-matching framework to
model the pre-quantization features of a neural codec. The vector quantizer in the
neural codec implicitly converts the regression problem into a token classification
task similar to NCLM. We empirically verified that this transformation is crucial
for enhancing the performance and robustness of the speech generative model. This
simple modification enables VoiceNoNG to achieve state-of-the-art performance
in both objective and subjective evaluations. Lastly, to mitigate the potential
risks posed by the speech editing model, we examine the performance of the
Deepfake detector in a new and challenging practical scenario. Audio examples
can be found on the demo page: https://anonymous.4open.science/w/NoNG-8004/

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a speech generation model for speech editing that incorporates future context to ensure smooth and seamless transitions. The model is built on the Voicebox architecture, but with a modification that replaces the intermediate acoustic feature mel-spectrogram with the continuous hidden features of the neural codec model DAC. The author demonstrates that this modification leads to some performance improvements, particularly in terms of Word Error Rate (WER).

### Strengths
The authors compare the proposed method against two baselines, VoiceCraft and VoiceBox, representing autoregressive (AR) and non-autoregressive (NAR) models, respectively. The results demonstrate a performance improvement. Additionally, the authors conduct an ablation study that shows the effectiveness of the proposed approach.

### Weaknesses
There are several fundamental issues with this work:
- **Unbalanced Structure**: The paper's structure is uneven, with the first three pages primarily dedicated to background and related work, while the proposed method is introduced briefly in a single paragraph at the end of Section 2. This creates an imbalance that detracts from the focus on the contributions of the work.
- **Questionable Claim About Voicebox Performance**: In Section 2, the authors suggest that the poor performance of Voicebox in generating speech with background audio is due to its use of the HiFi-GAN vocoder and mel-spectrogram. However, this assertion could be problematic. HiFi-GAN with mel-spectrograms has been demonstrated to effectively generate a wide variety of sounds, including music and singing voices. This raises doubts about the validity of the paper’s motivation, as it seems based on an incorrect premise.
- **Prior Work Overlooked**: The introduction of cross-entropy loss as an auxiliary loss function for diffusion models has already been proposed in NaturalSpeech 2. The authors should clearly acknowledge this prior work in Section 2, as this is not a novel contribution and may lead to some confusion regarding the originality of the approach.
- **Previous Work on Codec Embeddings**: The use of diffusion models to generate codec embeddings was already explored in NaturalSpeech 2. Although the authors claim that performance differences arise from using embeddings from different layers (before versus after quantization), the novelty of this contribution appears limited and unlikely to significantly expand the current body of knowledge in this area.
- **Concerns About WER Evaluation**: Although it is not explicitly stated, it seems that the entire utterance is passed through the vocoder or codec decoder to generate the waveform. If this is the case, the claim in Section 3.1.3 that "the unmasked regions are expected to exhibit the same WER, and thus the WER differences among various editing models should be considerably more pronounced in the edited regions" seems problematic. This is because the WER would be heavily influenced by the choice of vocoder or codec decoder. In Table 1, since different models use different vocoders and codec decoders, the observed WER gap may primarily reflect differences in the vocoders rather than the models themselves. As such, the current experiments do not adequately support this argument.
- **Reference missing**:
    - Seed-TTS: A Family of High-Quality Versatile Speech Generation Models
    - UniCATS: A Unified Context-Aware Text-to-Speech Framework with Contextual VQ-Diffusion and Vocoding
    - E1 TTS: Simple and Fast Non-Autoregressive TTS

### Questions
The questions are listed above in the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a new speech editing model called VoiceNoNG, which is based on VoiceBox and has been improved in two ways. On the one hand, the target is replaced with DAC features, and on the other hand, it is trained on the gigaspeech dataset to improve the effectiveness of speech editing, especially in scenarios with background noise. The paper also proposes a new deepfake speech detection method that considers reconstructed real speech.

### Strengths
1. The method proposed in the article has its rationality, enhancing the effect of speech editing by predicting high-dimensional features instead of Mel features. Since DAC features are better for information compression, replacing Mel is a good solution.
2. The article proposes more practical deepfake detection metrics and corresponding models, which have certain practical value.

### Weaknesses
1. The pre-quantization feature by predicting DAC is a variant of Latent Diffusion, which has been widely proven to be effective. So the solution is not novel. The novelty comes from the additional CE loss.
2. The new method proposed in the article, in my opinion, should be experimented on both TTS and speech editing, and compared with the VoiceBox model. 
3. This article describes the VoiceCraft model extensively, just to show that using gigaspeech data sets can enhance the effect of speech editing with background sound. In my opinion, data selection is an engineering problem and should not be presented as a major contribution. The claim (These two factors result in Voicebox not being good at generating speech with background audio.) in Line 154 is not scientific, This drawback is due to training data, not Voicebox's drawback.
4. Rough writing, lack of model or flow chart. There is also a problem with the organization of the article. For example, the drawback of VoiceBox and VoiceCraft (Line 152 and Line 156) should not be placed in the proposed VoiceNoNG section. The ablation description (Line 248) should not be included in the WER metric. The article is in an unpolished or even unfinished state.

### Questions
See above. In my opinion, the contribution of the article is limited or not fully explored. And more importantly, the rough writing makes it within an unpolished or even unfinished state.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper first examines the limitations of current advanced speech editing models. Voicebox produces lower-quality speech when background audio (such as noise or music) is present, while VoiceCraft struggles to accurately follow text input, a common hallucination issue with autoregressive models. To address these challenges, the paper introduces VoiceNoNG, which leverages the advantages of both models. The authors also explore the impact of the vector quantization module in the neural codec on achieving a robust speech editing model. Finally, to mitigate potential risks posed by the speech editing model, the authors examine the performance of a deepfake detector in a new, challenging practical scenario.

### Strengths
The paper first discusses the advantages and limitations of two different architectures for speech editing models. It then introduces a novel speech editing model based on DAC and latent flow-matching, which can be seen as an improvement to the VoiceBox model. The improved model achieves a lower WER and enhanced speech quality. The authors also investigate the impact of the VQ module on speech editing, with findings that may extend to other application areas. Finally, the authors examine the performance of a deepfake detector in a new and challenging practical scenario, contributing to the deepfake detection community.

### Weaknesses
The paper presents a rather simplistic introduction to the proposed method, with much of the first two chapters focusing on popular science explanations. In the abstract, the authors state that the poor performance of the NCLM-based model is due to attention errors (hallucination phenomena), but they provide only a few examples to support this claim, lacking more extensive experiments on attention mechanisms. The paper mentions that the model combines the advantages of VoiceCraft and VoiceBox, but it seems to only merge the Codec with VoiceBox. Additionally, the authors point out that the poor performance of VoiceBox is due to the HiFi-GAN being trained on clean speech; however, the experimental section lacks a comparison with a HiFi-GAN trained on noisy speech for VoiceBox.

### Questions
Q1: The paper states that the poor performance of the NCLM-based model is due to attention errors (hallucination phenomena). However, the poor performance of LM-based models could also be influenced by factors such as sampling methods and codebook size. How can it be proven that the issues are specifically caused by hallucination?

Q2: In line 199, the statement "Since no code and model checkpoints are available for Voicebox, we reproduced the results" raises a question. Does this mean that you retrained Voicebox based on open-source code, or did you replicate the experimental results from Voicebox? If it is the latter, please specify which tables the data comes from, as I could not find the same data in the Voicebox paper.

Q3: The "Spotify" column in Table 1 should indicate that VoiceCraft (330M) performs the best.

Q4: Is VoiceBox and HiFi-GAN trained on GigaSpeech, and then compared with it?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces VoiceNoNG, a new speech editing model that combines the strengths of two existing approaches in the field: Voicebox (based on flow-matching model) and VoiceCraft (based on neural codec language models). While current speech editing models like VoiceCraft can generate high-quality speech, they suffer from hallucination issues that lead to higher word error rates, including problems like unintended silences, slow speaking pace, or missing/repeated words. VoiceNoNG addresses these issues by utilizing a latent flow-matching framework and incorporating the Descript Audio Codec (DAC) instead of traditional Mel-spectrograms as its input feature representation.
The key innovation of VoiceNoNG is its use of pre-quantization features and a vector quantizer (VQ) module, which provides additional robustness against minor prediction errors similar to quantization noise. The model also employs a cross-entropy loss to enhance codec prediction accuracy. In experimental evaluations using the RealEdit dataset, VoiceNoNG outperformed both VoiceCraft and Voicebox variants in terms of word error rate (WER) and speech quality metrics. The authors demonstrate that modeling pre-quantization features and including the VQ module are crucial for developing a robust speech editing model that can maintain high quality while avoiding hallucination issues.
Finally, the authors develop a deepfake detector by classifying edited, real and synthesized speech portion in an utterance. The proposed method is an extension of prior model by adding a new class (synthesized) into the target.

### Strengths
1. Well written paper with clear and concise description of the proposed method. 
2. The problem statement is extremely interesting with good motivation
3. Shows that feature representation from neural codecs can be helpful for tasks like editing
4. Development of deepfake detector which is crucial given how these models can be abused by bad actors

### Weaknesses
1. The overall contribution is minimal with no original idea presented in the paper.
2. It appears that the authors have merely replaced the feature representation in VoiceBox model with DAC features.
3. The statements in the paper are sometimes very vague such as "This diversity makes RealEdit more challenging compared to ..." on line 222. Given that this is a scientific paper, there needs to be an explicit description of what other datasets lack which RealEdit provides.
4. Evaluation of edited speech by WER is not helpful in determining the quality/intelligibility of generation because ASR models have an implicit language model that corrects mispronunciations and even words based on context.
5. The hallucination claim is completely based on WER which is not astounding to begin with (see point 4). Further, the WER difference between Voicecraft and proposed technique is minimal except for YouTube dataset.
6. The SI-SDR difference are again very small to be meaningful across various models. This is probably not perceivable by human listeners.
7. MOS evaluation is unrealiable given there is only 3 rating per sample for a total of 10 samples per model (see ITU-T P.800 recommendations).

### Questions
None

### Soundness
2

### Presentation
3

### Contribution
1
