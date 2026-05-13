# NaturalSpeech 2: Latent Diffusion Models are Natural and Zero-Shot Speech and Singing Synthesizers

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Scaling text-to-speech (TTS) to large-scale, multi-speaker, and in-the-wild datasets is important to capture the diversity in human speech such as speaker identities, prosodies, and styles (e.g., singing). Current large TTS systems usually quantize speech into discrete tokens and use language models to generate these tokens one by one, which suffer from unstable prosody, word skipping/repeating issue, and poor voice quality. In this paper, we develop \textit{NaturalSpeech 2}, a TTS system that leverages a neural audio codec with residual vector quantizers to get the quantized latent vectors and uses a diffusion model to generate these latent vectors conditioned on text input. To enhance the zero-shot capability that is important to achieve diverse speech synthesis, we design a speech prompting mechanism to facilitate in-context learning in the diffusion model and the duration/pitch predictor. We scale NaturalSpeech 2 to large-scale datasets with 44K hours of speech and singing data and evaluate its voice quality on unseen speakers. NaturalSpeech 2 outperforms previous TTS systems by a large margin in terms of prosody/timbre similarity, robustness, and voice quality in a zero-shot setting, and performs novel zero-shot singing synthesis with only a speech prompt. Audio samples are available at \url{https://speechresearch.io/naturalspeech2}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents NaturalSpeech 2, a non-autoregressive TTS model that employs a diffusion mechanism to generate quantized latent vectors from neural audio codecs. It shows enhanced zero-shot TTS performance relative to the state-of-the-art large-scale neural codec language model. The proposed approach exhibits advancements in sample quality, intelligibility, robustness, speaker similarity, and generation speed when benchmarked against the baseline method. The authors further validate the superiority of their method over other alternatives via comprehensive qualitative and quantitative evaluations.

### Strengths
* The paper effectively tackles several major challenges inherent to non-autoregressive TTS modeling at scale. 
* The authors have carried out robust and wide-ranging experiments, yielding detailed results.
* The reference list is both extensive and comprehensive.

### Weaknesses
The proposed method's intricate modeling could hinder its extension to other applications. While the introduced model applies diffusion, it necessitates two additional losses and requires supplementary modules like a pitch predictor, prompt encoder and the second attention block. As an example, the recent state-of-the-art flow-matching based TTS method, VoiceBox [1] consists of rather simple model architecture; the flow-matching based duration predictor and audio model.

[1] Le, Matthew, et al. "Voicebox: Text-guided multilingual universal speech generation at scale." arXiv preprint arXiv:2306.15687 (2023).

### Questions
Given the concerns mentioned in the above weaknesses, it would be interesting to see if the proposed method could be adapted or refined to reduce its dependency on additional modules without increasing complexity or compromising sample quality.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper describes a TTS model combining a number of modern components these include in-context learning (prompting) a diffusion model to connect conditioning information to latents, and latents defined by an autoencoder for waveform reconstruction.

The resulting model has many of the zero-shot capabilities of LM based TTS that have been presented in recent years, but by maintaining duration prediction for alignment, the model stays robust to a hallucination and dropping errors that impact other generative models.

### Strengths
The model contains innovative structures in the in context learning for duration and pitch, and in the diffusion model.  Moreover the overall structuring of these components is novel.

The quality of the model is quite high and provides some important balancing between zero-shot capabilities and robustness compared to alternate models

### Weaknesses
The paper is sometimes unclear with regards to what the model components represent and how the components fit together.  For example, the use of SoundStream and wavenet is not obvious.  These are previously published approaches, that are used in novel ways here.  It took multiple readings to understand how they are being used in this paper, and even still i’m not 100% sure that my understanding is correct.  Broadly, the paper relies too heavily on Figure 1.0 to describe how the model fits together. 

The argumentation around continuous vs discrete tokens is very hard to follow.  It’s not clear why the discrete token sequence must necessarily be longer than a continuous sequence (Introduction).  The first three pages spend a lot of effort describing why a continuous representation is a better fit for this task.  Then in Section 3.1 “However, for regularization and efficiency purposes we use residual vector quantizers with a very large number of quantizers and codebook tokens to approximate the continuous vectors.  This provides two benefits…” This is a particularly surprising turn of the argument to then go on to describe why discrete tokens are useful here.

The diffusion formulation is too compact to be clearly followed.  Page 5. The following sentence includes a number of ambiguities.  “Then we calculate the L2 distance between the residual vector with each codebook embedding in quantizer j and get a probability distribution with a softmax function, and then calculate the cross-entropy loss between the ID of the ground-truth quantized embedding ej and this probability distribution. Lce−rvq is the mean of the cross-entropy loss in all R residual quantizers, and λce−rvq is set to 0.1”  I’d recommend including an appendix entry or describing each clause separately in place.

### Questions
Introduction “the zero-shot capability that is important to achieve diverse speech synthesis” – why is zero-shot necessary for diverse speech synthesis?  Also, for what contexts, and use-cases is diverse speech synthesis necessary?

In the introduction – the checklist between NaturalSpeech 2 and “previous systems” is somewhat strange.  Certainly there are previous systems that are non-autoregressive, or use discrete tokens.  I understand that this is not “all previous systems” but those listed. But why compare only to those three related systems? The introduction and related work draw contrast with a variety of alternate TTS models.

Why use a diffusion model instead of any other NAR model?

When presenting the “prior model” in section 3.2 is the phone encoder, duration predictor and pitch predictor pre-trained to some other target? or is there some other notion of a prior model here?

What is the units used in the L_pitch loss? Hz? log Hz? something else?

The variable z is used in a number of different ways, could this be clarified (e.g. in Figure 2 between the prompt, input to diffusion model and output?)

Section 4.1
Page 6 “Both speakers in the two datasets” are there only 2 speakers in the data sets?
Page 6 what is value of sigma in the sigma-second audio segment as a prompt?

How much loss is incurred by filtering the output by a speech scoring model?  E.g.  are 99% of utterances accepted? or 1%?  

Note: VCTK utterances are particularly noisy making is a poor comparison for CMOS, but the comparison to Librispeech is more representative.

Section 4.2 “We apply the alignment tool” – which alignment tool?

What is the variance of the prosodic measures – it’s hard to track whether the differences in Table 3 are significant or not.

“When we disable the speech prompt in diffusion, the model cannot converge” – this seems remarkable.  Why does the model require a speech prompt to learn?

Broader Impacts: What would such a protocol to protect users from misuse of this model look like? Presumably this model can generalize to unseen speakers already – so what protections are in place regarding the use of this model as of publication?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new TTS model that is capable of generating speech with diverse speaker identities, prosody, and styles, in zero-shot scenarios and it can also sing. It outperforms the current SOTA methods in both objective and subjective metrics. The way it works is the following. First the neural audio codec that converts a speech waveform into a sequence of latent vectors with a codec encoder, and reconstructs the speech waveform from these latent vectors with a codec decoder. Then the codec encoder extracts the latent vectors from the speech and uses them as the target of the latent diffusion model which is conditioned on prior vectors. During inference it generates the latent vectors from text using the diffusion model and then generate the speech waveform using the codec decoder.

### Strengths
-Paper is very well written and provides good intuition and justification for all model choices that the authors have made. These choices are intuitive to make generated speech more natural and to overcome past bottlenecks in previous methods.
-The new TTS algorithm has many capabilities such as generating diverse speech (different speakers, prosody, style) and in zero-shot scenarios. Singing is a bonus in this case.
-NaturalSpeech2 beats current SOTA methods in both objective and subjective metrics.
-Related work section is quite extensive.
-In the end I believe that this work is a good contribution to the community.

### Weaknesses
-One can hear in the more strenuous experiments that the audio samples have some kind of weird pitch or pace of speaking.
-Paper might not be a very good fit in this venue. Although it has to do with learning representations, NaturalSpeech2 is more fit for a Speech venue such as InterSpeech or ICASSP.

### Questions
-Why did the authors not include any experiments with single speaker data like LJSpeech.
-It would be interesting to hear some audio samples with people that have an accent. This has not been explored in the community.
-As an ablation what would be the shortest prompt in seconds that you can give for zero-speech synthesis?
-After the phoneme Encoder you have a Duration and Pitch predictor. Why didn't you also include an Energy Predictor like the authors did in FastSpeech2 since the idea seems to be derived form there?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes a latent diffusion-based speech synthesis framework for high-quality zero-shot speech synthesis. They utilize an audio codec as a latent representation and a conditional latent diffusion model could generate a latent representation. Then, the codec decoder generates a waveform audio. The zero-shot results show a better performance than the codec-based TTS model and YourTTS. Moreover, the audio quality is good.

### Strengths
They propose the latent diffusion-based speech synthesis model. This work may be the first successful implementation of a latent diffusion model for speech synthesis. Although recently large-language model (LLM) -based speech synthesis models have been investigated, they have too many problems for speech synthesis resulting from the auto-regressive generative manner. However, this work adopts a parallel synthesis framework with latent diffusion, and successfully shows their generative performance by several speech tasks.

Recent papers only compare their work with YourTTS but I do not think YourTTS is a good zero-shot TTS model. The audio quality of YourTTS is too bad. However, although recent models do not provide an official implementation, the authors tried to compare their model with many other works.

### Weaknesses
1. They also conducted an ablation study well. However, it would be better if the authors could add the results according to the dataset and model size. The model size of NaturalSpeech 2 is too complex compared to VITS. In my personal experience, VITS with speaker prompt could achieve significantly better performance than YourTTS. 
 
2. For inference speed, NaturalSpeech 2 still has a low latency for its iterative generation. Although this discussion is included in the Appendix, it would be better if the authors could add the discussion of inference speed in the main text. This is just a limitation of diffusion models so I acknowledge the trade-off between quality and inference speed. Furthermore, I hope to know other metrics of NaturaSpeech 2 according to Diffusion Steps (WER or Similarity metric). Recently, Flow matching using optimal transport is utilized for fast speech synthesis. This could be adopted to this work. 

3. Some details are missing. Please see the questions.

### Questions
1. This work utilizes a quantized latent vector for latent representation. In my experience, the quality of the model with the continuous latent representation before quantization showed a better performance in latent diffusion model for singing voice synthesis. Have you tried to train your model with the pre- or post-quantized representation for latent representation?

2. The details of singing voice synthesis are missing. It would be better if you could add the details for pre-processing of musical scores. How do you extract the duration of phonemes in this work?

3. How do you extract the pitch information? This significantly affects the performance so the details should be included. (about F0 min, F0 max, resolution, and pitch extraction algorithm).

4. The authors may train the audio codec with their speech dataset. I think it is important to utilize a high-quality speech codec for high-quality speech synthesis. In this regard, I hope that the authors will mention about this part by comparing your model with the same model utilizing an official Soundstream codec as a latent representation.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
