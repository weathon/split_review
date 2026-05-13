# Simple-TTS: End-to-End Text-to-Speech Synthesis with Latent Diffusion

- Decision: Reject
- Scores: 5, 3, 1

## Abstract
We propose an end-to-end text-to-speech (TTS) latent diffusion model as a simpler alternative to more complicated pipelined approaches for TTS synthesis. In particular, we show that one can adapt a recently proposed text-to-image diffusion architecture, U-ViT, as an excellent backbone for audio generation.  We identify and explain the changes required for this adaptation and demonstrate that latent diffusion is an effective approach for end-to-end speech synthesis, without the need for phonemizers, forced aligners, or complex multi-stage pipelines. Despite its simplicity, our proposed approach, Simple-TTS, outperforms more complex models that rely on explicit alignment components and significantly outperforms the best open-source multi-speaker TTS system. We will open-source Simple-TTS upon acceptance, making it the strongest system publicly available to the community. Due to its straight-forward design, we expect that Simple-TTS can easily be adapted to many diverse TTS settings --- opening the stage to repeat the success of Stable Diffusion in computer vision, in audio generation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a TTS model in the form of Latent diffusion called Simple-TTS. It simplifies the training process of the TTS model by using a pre-trained text encoder and EnCodec and training only the weight of latent diffusion model. It outperforms the open-source zero-shot TTS model, YourTTS.

### Strengths
1. As the title of the paper, the training process of TTS has been greatly simplified. By utilizing a pre-trained Text Encoder (ByT5), the need to train the text encoder has been eliminated, and by aligning speech with text through cross-attention, the need for a duration predictor has been removed. Through this, the model is trained using only a simple v-prediction for diffusion model.

2. Listening to the samples provided in the Supplementary material, the generated samples sound expressive.

### Weaknesses
1. In simplifying the model training, there is a suspicion of potential issues in the process of learning monotonic alignment between text and speech through cross attention. Additionally, padding all sentences to a fixed length during training and allowing the diffusion model to learn on its own is presumed to be heavily influenced by the length of the speech data in the dataset. It seems that this model may also have the robustness issues that were present in autoregressive TTS models using cross-attention for alignment like Tacotron or TransformerTTS.

2. Sample quality in supplementary material is too bad.

3. Despite the proposed model has lower speaker adaptation performance compared to recent papers such as VALL-E, SPEAR-TTS, and VoiceBox, claiming to release the strongest publicly available system by showing performance improvements over an easily beatable baseline like YourTTS seems like an overstatement in abstract.

### Questions
* Despite using pre-trained models, why do you refer to Simple-TTS as an end-to-end TTS model?

* Regarding Weakness 1, does Simple-TTS have no robust issues in finding alignments even with the introduction of cross-attention? If not, it would be beneficial to provide the ASR metrics for the Hard sentences found in Appendix B of the FastSpeech paper as well.

* How can Simple-TTS generate speech that exceeds the predetermined length during training? For example, generating 30+ seconds of speech given a few long sentences.

* Regarding Weakness 2, the sample quality is too bad compared to existing zero-shot TTS models. NaturalSpeech 2 also models continuous latent representation similarly to the proposed paper, but the sample quality of the proposed method is relatively poor in comparison. It would be beneficial if this could be improved.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a TTS model, the simple-TTS, that uses latent diffusion models and U-Audio Transformer.

### Strengths
1. The usage of U-Audio Transformer is potentially useful for speech generation.
2. The results reported in the experimental section are encouraging.

### Weaknesses
1. The authors claim that the proposed model is an end-to-end model, however, it contains at least 3 separately training stages. Obviously, it is a not end-to-end model.

2. The authors call this model is a 'simple' model, however, it's not so simple. Taking the baseline model YourTTS for comparison, YourTTS is trained without using language model pre-training and En-Codec model, thus appears to be more simple.

3. In sections 1 and 2, the authors claim that simple-TTS is much simpler than NaturalSpeech2 and VoiceBox. However, in the experimental section, they do not provide a direct comparison to these models. 

4. The experiments are far from sufficient.
   1). Why not present the MOS results for Text-only TTS?  which is very important to evaluate this work. 
   2). Many important details are missing. For example, the sample rate of the audio samples. The synthesis speed is not presented.
   3). From my subjective evaluation, the audios in the supplementary Material are not as good as some SOTA models such as VITS and NatrualSpeech.

### Questions
Why not present the MOS results for Text-only TTS?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
They proposed a text-to-speech model which utilizes a latent diffusion model. They introduce a U-ViT for latent diffusion based speech synthesis, and they do not require text-speech alignment for speech synthesis.

### Strengths
This work utilizes a pre-trained language model for text encoder, and they can generate a speech without text and speech alignment. This facilitates training pipeline efficiently.

### Weaknesses
Although this work proposed a simple method for text-to-speech without text and speech alignment, I have many questions about this and others. 

1. They fixed the maximum length of speech by 20 seconds during training. This may make a training pipeline simple, but I think it is not efficient for GPU. In addition, this framework could not control the duration of speech.

2. It would be better if you could add an additional experiment according to text length. Because you train your model with a fixed length, you should demonstrate the robustness according to text length.

3. The authors may not know the definition of end-to-end. This model is not the end-to-end speech synthesis model. They need the pre-trained audio autoencoder and language model for the text encoder. They have overclaimed it. 

4. The audio quality is too bad. I think it is because the audio autoencoder has a lower quality. You should have trained an audio autoencoder with speech data or replaced it with a high-quality audio autoencoder. I recommend to use different audio autoencoder such as DAC or HiFi-Codec or utilizes a pre-trained codec-based vocoder such as Vocos for high-quality waveform audio. It is well known that re-training the codec-based vocoder could generate a better quality of audio.

5. I think NaturalSpeech 2 already introduced this kind of method for speech synthesis. The difference with NaturalSpeech 2 is only the necessity of duration predictor. However, I think removing the duration predictor decreased the controllability of the model so I hope the authors address this issue. I think that the authors should have listened to the demo samples of NaturalSpeech 2 and compared the audio quality with yours. In addition, although they propose new architecture, there is no ablation study for model architecture.

6. They only compared the model with YourTTS. YourTTS has a very low audio quality. You should have trained the VITS with same dataset and speaker prompt.

### Questions
I sincerely have a question about the audio quality. How do the authors think the audio quality of your model.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
