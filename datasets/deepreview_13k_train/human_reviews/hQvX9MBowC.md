# DiTTo-TTS: Diffusion Transformers for Scalable Text-to-Speech without Domain-Specific Factors

- Decision: Accept
- Scores: 6, 8, 5, 6

## Abstract
Large-scale latent diffusion models (LDMs) excel in content generation across various modalities, but their reliance on phonemes and durations in text-to-speech (TTS) limits scalability and access from other fields. While recent studies show potential in removing these domain-specific factors, performance remains suboptimal. In this work, we introduce DiTTo-TTS, a Diffusion Transformer (DiT)-based TTS model, to investigate whether LDM-based TTS can achieve state-of-the-art performance without domain-specific factors. Through rigorous analysis and empirical exploration, we find that (1) DiT with minimal modifications outperforms U-Net, (2) variable-length modeling with a speech length predictor significantly improves results over fixed-length approaches, and (3) conditions like semantic alignment in speech latent representations are key to further enhancement. By scaling our training data to 82K hours and the model size to 790M parameters, we achieve superior or comparable zero-shot performance to state-of-the-art TTS models in naturalness, intelligibility, and speaker similarity, all without relying on domain-specific factors. Speech samples are available at https://lactojoy.github.io.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a latent diffusion model based zero-shot TTS as DiTTo-TTS.  The author have done rigorous investigations to improve LDM based TTS by replacing U-Net with DiT, remove dependency of domain-specific factors like phoneme and duration with several experiments on the model size and datasets. The experiment results shows the good performance of naturalness (CMOS), intelligibility (CER/WER) and similarity (SMOS and SIM).

The major achievements prove that the LDM TTS model could work as end-to-end in a joint modeling way for the text and speech representation, and it is scalable to different model size and dataset.

### Strengths
This paper clearly describes the work for an end-to-end fully diffusion model for zero-shot TTS. The strengths lie on the following aspects
1) Rich experiments have done to investigate the different model size of DiTTo model (small, base, large and Xlarge), data scalability; comparison between U-Net and DiT module, and comparison between speech length model with variable and fixed and etc. 
2) A lot of state-of-art TTS system comparison is provided. Although not all the system have compared all the metrics but several metrics are showed for readers to compare and get a relative complete picture on the metrics of different popular system include AR model like VALL-E, CLaM-TTS, NAR model like YourTTS, and SimpleTTS,  etc.
3) Ablation study and demo page quit clear.

### Weaknesses
The major weakness of this paper is the novelty. The most contribution as the author also mentioned is removing the domain-specific factors like phoneme and duration, and just giving a total duration estimation is good enough for the task which is even better. However, this is not new, and similar work has been done at SeedTTS https://arxiv.org/pdf/2406.02430#page=6&zoom=100,144,548. 

SeedTTS-DiT has no-dependence on the phoneme duration by just giving the total duration for the diffusion model. It already shows that this fully diffusion based speech generation model could achieve superior performance. This integration is just a quite natural way regarding the highly flexibility of noise iteration with DiT structure for a diffusion or flowmatching model. I would believe many folks/peers have applied it in speech generation before or after Seed-TTS-DiT and it indeed works as expected. According to these information, I would give the question on the novelty of this paper.

### Questions
1. Regarding successfully applying joint latent diffusion model for TTS,  the comparison between the autoregressive (AR) model like a language speech model (CLaM in this paper) and diffusion model would be attracting as they are the current two major methodologies as diffusion vs. AR model.  According to the result, the diffusion model archives better similarity and quality from subjective metrics, and also better CER. However, as the total training data is not large enough (82K), would it be enough to be convincing that diffusion model could achieve superior result rather than AR model while language model may work better on larger dataset? It would be a fantastic topic to discuss. 
2. The framework design a latent representation for diffusion model to generate, then use Mel-VAE to decode latent into mel-spectrogram, and get the synthesized speech via BigVGAN. This is a little confusing why not just model mel-spectrogram for diffusion model? 
3. The Table 3 shows the subjective result with SMOS and CMOS. How many speakers and how many test utterances in this test set? It would be related to the diversity of the model  capability.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work proposes DiTTo-TTS, a DiT-based architecture for zero-shot text-to-speech (TTS) synthesis applications. The proposed method does not rely on explicit alignments or phoneme units, thereby simplifying the TTS pipeline. For the neural codec, the paper proposes fine-tuning MelVAE to better align with pre-trained text encoders. This work includes exhaustive ablations on data and model scaling, architectural choices such as skip connections, choice of text encoders, and variable vs. fixed-length modeling to understand better the factors contributing to DiTTo-TTS's results. The authors also introduce a novel text and speech-token conditional speech length predictor based on auto-regressive training for variable-length modeling. Experiments on multilingual and English setups provide a detailed understanding of each component and demonstrate that DiTTo-TTS achieves SOTA results for zero-shot TTS without relying on domain-specific factors.

### Strengths
- The paper is clear and generally well-written. Detailed ablations highlight the importance of each factor in DiTTo-TTS.
- The contributions related to MelVAE fine-tuning and the auto-regressive speech length predictor are novel. While DiT has been explored previously in audio, the detailed ablations and contributions, such as long-skip connections, provide valuable insights for the field.
- The paper performs an exhaustive comparison against a number of baselines to demonstrate performance differences and establish SoTA results.

### Weaknesses
 - No major weaknesses, there are some minor details which could be added. See comments section.

### Questions
- Table 7:
  - Are the DiTTo-Encodec and DiTTo-DAC models also fine-tuned with an LM objective? If not, please include DiTTo-MELVAE for comparison.
  - Please report sim-o when comparing different neural codecs.
- In general, reporting sim-o for other ablations would be beneficial for the community to facilitate comparisons with any results in the paper.
- Page 7, line 518: "We cannot measure the total inference time due to the lack of a speech length predictor for their embeddings, but even with ground truth lengths, their 7-8 times longer latents lead to significantly slower generation."
  - What is the feature rate for the MelVAE model? Encodec operates at 75Hz, so does this mean that MelVAE operates at approximately 10Hz? The original MelVAE in CLAM-TTS mentions a coderate of 100Hz. It would be helpful to include this information in the paper to make it more self-contained.
- How does speech editing, particularly for the infilling task, work? Do you only provide the prefix as a prompt to determine the duration of the edited segment? Specifically, could you describe the process for editing: 

  **<prefix> <old text> <postfix> to <prefix> <new text> <postfix>**?  
  - My guess is that this might require an alignment model to identify the start and end timings for <old text>, followed by predicting the duration of <prefix> <new text> conditioned on prefix speech tokens.
  - What happens if <prefix> is null? How does the model handle durations in this case? I assume with an alignment tool one could use any partial text and corresponding tokens for prompting.
- Ablation suggestion: Could you explore the impact of the number of training steps on performance? 
- Minor:
  - Typo on page 1: "honemes".

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces DiTTo-TTS, a scalable TTS model based on diffusion transformers that avoids reliance on domain-specific factors like phonemes or durations, achieving high-quality results and efficiency improvements over conventional TTS methods.

### Strengths
1. Develop a diffusion-based TTS model, DiTTo-TTS, that avoids reliance on domain-specific factors while maintaining competitive quality. 
2. DiTTo-TTS is shown to achieve better performance compared to state-of-the-art baselines with significantly reduced inference time.

### Weaknesses
 **Dependency on Domain-specific factors** DiTTo-TTS is claimed to avoid reliance on domain-specific factors like phonemes or durations; however it needs the pre-trained Text Encoder (ByT5, SpeechT5), which aligns the textual and acoustic information into a unified semantic space, and a pre-trained neural audio codec which aligns the speech latents with the linguistic latents of the pre-trained language model during the autoencoding process. Moreover, DiTTo-TTS also needs a Speech Length Predictor for managing duration. Given these dependencies, it’s unclear how the model avoids domain-specific factors.  Could you clarify your definition of "domain-specific factors" and explain how your approach differs from traditional TTS systems in terms of reliance on phonemes and durations, even with the use of pre-trained components?

**Limited Novelty of the Proposed Approach** Simple-TTS and NaturalSpeech 2 has already proposed to use a pre-trained text encoder and neural audio codec to align the speech with text through cross-attention and training only the weight of latent diffusion model. Could you provide a more detailed comparison between DiTTo-TTS and Simple-TTS/NaturalSpeech 2 and highlight the key innovations or improvements in DiTTo-TTS that differentiate it from these prior works?

### Questions
1. Can you provide confidence intervals or p-values for the comparisons in your result tables? Without these, it is impossible to tell if the result is significantly better than state-of-the-art baselines.

2. In Appendix A3, the instruction for comparative mean opinion score (CMOS) shows that you only ask participants to compare the quality of the synthesized audio and reference, but in the main text you mention that DiTTo-en significantly outperforms the baseline models in naturalness, quality, and intelligibility (as assessed by CMOS). This raises questions about how the evaluations of naturalness and intelligibility for the synthesized audio were conducted in the experiments.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study presents a model for personalized speech synthesis based on an LDM structure. Personalization is achieved by modeling z obtained through Mel-VAE using an infilling approach. Instead of explicitly calculating text-speech alignment and providing text information accordingly, as is common in previous research, the model allows the text and speech representations to learn alignment autonomously via cross-attention. Additionally, a variable-length predictor is introduced to predict the total speech length during inference. To validate the proposed structure and methodology, the authors conducted comparisons with numerous strong baselines across various languages and benchmarks, as well as extensive ablation studies on proposed elements, data quantity, hyperparameters, and other factors.

### Strengths
The most notable strength is that the authors conducted comparisons with various baselines and performed extensive ablation studies and analyses on numerous elements. In addition, the paper is well-written, with a high level of detail in the experiments, making it easy to understand the study.

### Weaknesses
Personally, I feel that the novelty is somewhat limited, as LDM-based structures in zero-shot TTS are not entirely new (e.g., NaturalSpeech 2, 3, as you already mentioned in your paper.), and the approach of allowing the model to learn speech-text alignment with cross-attention has been seen in previous works, such as Simple-TTS. Nonetheless, the systematic analysis of each component and the guidance provided to readers on existing design choices and their limitations are indeed valuable contributions.

### Questions
1. Are you plan to release the code and checkpoints of DiTTo-TTS? 

2. Regarding the content in Appendix A.13, I am interested in whether the model performs well in smaller data scenarios, such as a single-speaker setup with less data than LibriTTS. The scale-up trend in performance relative to data quantity seems less pronounced compared to other zero-shot TTS models (e.g., Voicebox Section B.2). I would like to understand the authors' perspective on why DiTTo-TTS remains robust even with limited data.

### Soundness
3

### Presentation
3

### Contribution
3
