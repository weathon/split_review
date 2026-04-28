# Vec-Tok Speech: Speech Vectorization and Tokenization for Neural Speech Generation

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 8, 5, 5, 3

## Abstract
Language models (LMs) have recently flourished in natural language processing and computer vision, generating high-fidelity texts or images in various tasks. In contrast, the current speech generative models are still struggling regarding speech quality and task generalization. This paper presents Vec-Tok Speech, an extensible framework that resembles multiple speech generation tasks, generating expressive and high-fidelity speech. 
Specifically, we propose a novel speech codec based on \textit{speech vectors} and \textit{semantic tokens}. Speech vectors contain acoustic details contributing to high-fidelity speech reconstruction, while semantic tokens focus on the linguistic content of speech, facilitating language modeling. Based on the proposed speech codec, Vec-Tok Speech leverages an LM to undertake the core of speech generation. Moreover, Byte-Pair Encoding (BPE) is introduced to reduce the token length and bit rate for lower exposure bias and longer context coverage, improving the performance of LMs.
Vec-Tok Speech can be used for intra- and cross-lingual zero-shot voice conversion (VC), zero-shot speaking style transfer text-to-speech (TTS), speech-to-speech translation (S2ST), speech denoising, and speaker de-identification and anonymization.
Experiments show that Vec-Tok Speech, built on 50k hours of speech, performs better than other SOTA models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a new generative speech network that combined conditioning on discrete tokens for semantic content with conditioning on continuous features for audio style. They use a pre-trained WavLM model as a source of both features where the discrete features are obtained via K-means clustering WavLM features, and the continuous features are encoded directly from WavLM features. During training, a language model is trained on BPE encoded discrete token sequences, while a decoder is trained on a combination of discrete and continuous inputs where the former are processed via an "inverse K-means" process. The resulting output is fed into a vocoder to produce speech.

The authors show that such a model can perform several tasks very well, including voice conversion, zero shot speaker style transfer TTS and speech to speech translation.

### Strengths
- Strong results on several benchmarks across several tasks
- Novel architecture that utilizes discrete and continuous features and avoids multi-pass decoding like VALL-E/SoundStorm

### Weaknesses
 - Quite complex and depends on previous pre-trained models (e.g. WavLM)
- No comparison with diffusion based models like NaturalSpeech2
- Missing ablations make it difficult to understand which parts contribute to the performance of the model. While certain parts of the architecture are ablated for certain tasks, it would be nice to ablation results for each task to understand how modeling choices (BPE, inverse K-means) contribute to the performance. It would also be good to know how much WavLM contributes to the overall performance or if it is replaceable with any other model. Choices on the LM side (how necessary it is to produce 256 candidates and then rank them? etc) are not ablated at all.
- Speech to speech translation results compare to one other prior work that outperforms the proposed architecture on BLEU and is missing all other metrics making comparison difficult.

### Questions
Most of my questions relate to the weaknesses section:
- Could you provide additional ablations that can make it clear what modeling choices lead to what outcomes?
- Could you provide a more thorough comparison on the STST task?
- Could you ablate the choice of relying on WavLM as the primary encoder in this method?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an encoder-decoder architecture that decouples acoustic style and semantic linguistics. The semantic tokens can be combined with prompts for LLMs to generate output token sequence which could be further combined with optionally modified acoustic style vectors to reconstruct speech for various speech tasks. The authors conducted experiments in VC, TTS, and S2ST to demonstrate that their proposed system can match or outperform some recent models on those tasks.

### Strengths
Originality: Decoupling or disentangling speech style and speech content with neural networks has been long studied since VAE and GAN. The authors are able to leverage recent developed models such as WavLM to extract speech vectors for downstream speech generation tasks. Using K-mean to cluster speaker vectors and using BPE to compress token sequences are also popular techniques in related publications, but the authors also incorporate them as essential components in their speech generation system. They also proposed inverse K-means that includes speaker vectors as part of the prompts to generate speech vectors rich in speaker style. 

Quality: Despite the novel engineering integration and encouraging experimental results, the authors did not attempt to develop their proposed system with a more theoretical approach. As a result, readers may not be able to gain as many insights as to why the proposed system and its components can outperform the competing systems.

Clarity: The paper is well-written and easy to follow. There are few errors. The authors used high level equations to describe their system design. The use of diagrams and coloring schemes are appropriate. The result tables contain the right amount of information for the readers. The demos on the github sites are well-organized.

Significance: The paper engages the latest trend of speech research in the community by bridging the use of LLM into speech generation.

### Weaknesses
A few sections are written without adequate explanation of the symbols or extensive reader knowledge is assumed beyond a reasonable context. For example, in Equation 6, a more detailed description of the adversarial setup should be given. Why is the loss constructed this way? Why are MPD and MSD selected specifically, and what are their individual roles in the discriminator? The equation of the feature matching loss (not named as such in the reference) and reconstruction loss (which norm, L1 or L2?) should also be clearly stated.  
Minor typo below equation 9. ^vec instead of ^wave. Less well-known acronyms such as CLVP in section 4 should be expanded first. The experimental section should also compare the model sizes of the proposed system and the competing baselines, including the number of parameters for each component (encoder, decoder, etc.) and the total model size. This is important for assessing the practical applicability of the proposed method compared to existing approaches.

### Questions
In Figure 1, what's the use of two codec encoders for the TTS pipeline? 
Did the author compare the performance of TTS and S2ST with AudioPaLM?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a new way to encoding speech, by using continuous feature to capture acoustic and discretized token to capture semantics. Based on this mixed codec, a new framework been proposed to to speech generation task. Downstream task include TTS, voice conversion and speech to speech translation.

### Strengths
(1) I would like to highlight one concept the paper proposed which is different than previous audio lm based work, it's not necessarily to discretize both acoustic and semantic information. A combined approach (discretize and continuous) might also work.   

(2) I covers many different applications, and the framework is easy to adopt.

### Weaknesses
(1) The paper is poorly written. Section 3.2 is very hard to understand. I would suggest anything in the figure, should clearly defined in the method section. For example, "codec decoder". I also highly suggest the author describe tortose (Betker, 2023) in the related work. It seems some component borrowed from here, but it's unclear which part is being used.  

(2) The way to disentangle acoustic and semantic are very empirical, e.g. assume 6-layer of wav-lm, assume mean capture speaker information. There is no solid evidence to justify those claim.

(3) Results are unsound. It keep mention low bit rate, but I even don't know what the bit rate used here. From the demo, the reconstruction audio quality are poor, which make it hard to believe the proposed codec are really working.

### Questions
"First, these codec tokens usually contain as many speech attributes as
possible to high-fidelity reconstruction quality, which leads to information redundancy and increases
the difficulty of predicting the tokens in downstream tasks...." 

One key contribution of the paper is replace acoustic tokens in audioLM. But those claim are very vague, are there any empirical or theoretical analysis to justify this claim?

"a neural vocoder is used to reconstruct speech waveforms based on the extracted speech vectors vec
since the vocoder can produce waveforms that are nearly indistinguishable from recorded waveforms
and are highly generalizable outside of the training set (Betker, 2023). "

I highly recommend the author fix citation like this, what are citing here? the claim or the decoder architecture or something else?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel speech generation model called Vec-Tok Speech with a codec  leveraging speech vectorization and tokenization to facilitate various speech generation tasks. The proposed architecture is beneficial for both high-fidelity speech reconstruction and accurate linguistic content of speech.
The paper further introduces Byte-Pair Encoding technique in order to reduce the token length and bit rate for lower exposure bias and longer context coverage, thus improving the performance of language models.

### Strengths
1. This paper tackles the shortcomings of the previous works related to neural audio codec, RVQ-based codecs, which leads to information redundancy and increases the difficulty of predicting the tokens in downstream tasks, by proposing Byte Pair Encoding to compress the length of semantic tokens.
2. The authors have conducted extensive amounts of downstream tasks, showing the superiority of Vec-Tok Speech: Zero-shot VC, Zero-shot speaking style transfer TTS, Speech to Speech translation, Speech denoising and bandwidth extension, and speaker de-identification and anonymization.
3. This paper is well structured and easy to read.

### Weaknesses
1. The proposed model seems to be the combination of the existing technique: vectorization, tokenization, and BPE, without any novel architecture.
2. I am not sure it is novel enough to adapt Byte-Pair Encoding technique to compress the length of semantic tokens. Many existing works have leveraged the BPE technique in audio processing [1,2], so it is better to distinguish the proposed model from the ones that have utilized the BPE. 
3. I think even though the authors have presented various amount of downstream task, the performances of previous works that they are comparing with seem to be limited overall. For example in zero-shot tts, why not comparing with Voicebox?
4. Moreover, there is no quantitative performance on speech denoising. Although the results are shown in the demo page, it is better to report the qualitative results with metrics like MCD, STOI, PESQ for performance reporting.

### Questions
Please refer to the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces VEC-TOK SPEECH, an extensive framework for a variety of speech generation tasks. The framework integrates an innovative codec that is capable of disentangling linguistic content and acoustic details from speech, as well as a language model tailored for conditional semantic token generation. Moreover, the authors ease the token sequence length issue by implementing the BPE technique. The experimental results confirm the effectiveness of the proposed approach.

### Strengths
1.	This work introduces a novel paradigm: representing relatively simple linguistic content with a single semantic token sequence, while capturing complex audio details using continuous vectors, as opposed to the multiple acoustic token sequences in previous works. This design can lessen the challenges of language modeling and enhance generation quality.
2.	The article consolidates multiple speech generation tasks within a single, concise, and scalable framework.

### Weaknesses
1.	The paper may need more experimental results to improve its soundness, including:
a) The state-of-the-art (SOTA) model for cross-lingual zero-shot TTS is not VALL-E X, but Mega-TTS[1]. Including such a comparison would make the paper sounder.
b) The reconstruction quality of the proposed codec is not assessed thoroughly.
2.	The quality of the provided samples is not satisfactory when compared with the samples from [1] (demo link: https://mega-tts.github.io/demo-page/).
3.	The abstract contains some overstatements. Indeed, this work is not the first work to unify multiple speech generation task ([1-4]).
        `` "In contrast, the current speech generative models are still struggling regarding speech quality and task generalization."``

4.	The use of BPE for semantic tokens was first proposed in [5]. Including the reference and a discussion on this topic may be necessary.

### Questions
1. Does the SCS metric measure the similarity between the generated audio and the original recording or the reconstructed samples?
2. Do consecutive repeating tokens impact the BPE efficiency? Could you provide the average token sequence length after deduplicating the tokens?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
