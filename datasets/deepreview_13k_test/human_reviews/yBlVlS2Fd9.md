# WavTokenizer: an Efficient Acoustic Discrete Codec Tokenizer for Audio Language Modeling

- Decision: Accept
- Scores: 10, 3, 8, 5

## Abstract
Language models have been effectively applied to modeling natural signals, such as images, video, speech, and audio. A crucial component of these models is the codec tokenizer, which compresses high-dimensional natural signals into lower-dimensional discrete tokens. In this paper, we introduce \textbf{WavTokenizer}, which offers several advantages over previous state-of-the-art (SOTA) acoustic codec models in the audio domain: 1) \textbf{extreme compression.} By compressing the layers of quantizers and the temporal dimension of the discrete codec, one-second audio of 24kHz sampling rate requires only a single quantizer with 40 or 75 tokens.
2) \textbf{improved subjective reconstruction quality.} Despite the reduced number of tokens, WavTokenizer achieves SOTA reconstruction quality with outstanding UTMOS scores and \textbf{also inherently contains richer semantic information}.
Specifically, we achieve these results by designing a broader VQ space, extending contextual windows, improving attention networks, and introducing a powerful multi-scale discriminator and an inverse Fourier transform structure. We conduct extensive reconstruction experiments in the domains of speech, audio, and music. WavTokenizer exhibits competitive to superior performance across various objective and subjective metrics compared to SOTA models. We also evaluate WavTokenizer on semantic representation, VQ utilization, and adaptability to generative models. Comprehensive ablation studies confirm the necessity of each module in WavTokenizer.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper introduces WavTokenizer, a codec tokenizer for audio that achieves extreme compression and superior reconstruction quality compared to previous state-of-the-art models. WavTokenizer requires only a single quantizer with 40-75 tokens per second for 24kHz audio, while still preserving high subjective quality and rich semantic content. Extensive experiments demonstrate WavTokenizer's effectiveness across speech, audio, and music, with competitive results in both objective and subjective metrics, and ablation studies confirm the impact of each component.

### Strengths
- Achieves state-of-the-art performance using only a single codebook with 40 or 75 tokens, demonstrating remarkable efficiency.
- Covers multiple domains, including audio, speech, and music.
- Its single codebook capability supports efficient training of large language models (LLMs).
- Provides a comprehensive analysis of different settings, along with detailed ablation studies that validate the impact of each component.
- The paper is well-written and easy to follow, with a comprehensive analysis included.

### Weaknesses
Here’s a refined version of the weaknesses:

- The evaluation could be more thorough by incorporating existing benchmarks such as Codec-Superb and DASB to enable a more comprehensive comparison of the proposed method against existing models under standardized settings.
- The model currently supports only a 24kHz sampling rate; I wonder if you anticipate any challenges in adapting WavTokenizer to different sampling rates. It would be valuable to study its performance across different sampling rates, such as lower (16kHz) and higher (44kHz or 48kHz) rates.

### Questions
refer to weakness

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
The paper introduces WavTokenizer, a single-vq codec aimed at simplifying and improving the current audio language modeling approaches by replacing codec with multiple-vq. It claims to achieve competitive reconstruction quality while enhancing integration with language models.

### Strengths
The overall approach is sound.  The paper is straightforward and easy to understand, with a clear structure that makes it accessible to readers. Additionally, the introduction provides a good overview of the context and background, helping readers to understand the problem.

### Weaknesses
The paper introduces WavTokenizer, a single-VQ codec designed to replace the current codec + LLM audio generation systems. However, there is no experimental evidence to support that WavTokenizer can effectively achieve this. Existing codec + LLM systems can generally be categorized into RVQ-style generation (e.g., VALL-E, MusicGen, Moshi) or semantic-to-acoustic approaches (e.g., SpearTTS, SeedTTS, MusicLM), all of which demonstrate strong performance.

Firstly, there are no experiments showing that WavTokenizer combined with an LLM outperforms any of the existing systems in practical applications such as TTS or music generation. Secondly, when considering the codec itself, WavTokenizer's reconstruction quality is significantly worse than RVQ-based codecs, and its semantic performance falls short compared to semantic token like HuBERT or WavLM.

Given these shortcomings, it is difficult to see any tangible improvements or significant contributions that WavTokenizer offers to the current field of audio generation.

### Questions
1, Missing baselines: SemantiCodec[1], Single-Codec[2], Mimi (Moshi) [3].

2, Weak Semantic Performance: Compared to the ARCH benchmark (https://huggingface.co/spaces/ALM/ARCH), the semantic performance of WavTokenizer is far worse than models like HuBERT base. Therefore, the claim of "rich semantic information" does not hold up well. Moreover, it is unclear why WavTokenizer's semantic capabilities were compared only against acoustic codec models, rather than semantic codecs. Why not compare against semantic codecs like SpeechTokenizer[4], SemantiCodec[1], or Mini[3]?

3, Single-VQ Assumption: The entire premise of the paper is based on the assumption that using a single-VQ codec is better for audio language modeling compared to RVQ. But is this correct? The paper mentions that RVQ-based codecs like DAC require 900 tokens per second, which is true, but it fails to acknowledge that RVQ codecs typically have a temporal resolution of only 50Hz, and the most advanced models like Mini have even lower resolution at 12.5Hz. In practice, language models typically need to model at frequencies of 50Hz or less. So, what is the real advantage of a single-VQ codec with 40 or 75 tokens per second? Moshi and Mini have already demonstrated success in low-latency speech dialogue applications, but what about single-VQ? Is reconstructing all acoustic details truly beneficial for language modeling?  Does an LLM truly need to model timbre and detailed acoustic features, or is focusing solely on semantic content sufficient?  Therefore, you must at least demonstrate the effectiveness of single-VQ in practical applications, as stated in the weakness section, rather than constructing the paper solely based on this assumption.

[1]: Liu H, Xu X, Yuan Y, et al. SemantiCodec: An Ultra Low Bitrate Semantic Audio Codec for General Sound[J]. arXiv preprint arXiv:2405.00233, 2024.

[2]: Li H, Xue L, Guo H, et al. Single-Codec: Single-Codebook Speech Codec towards High-Performance Speech Generation[J]. arXiv preprint arXiv:2406.07422, 2024.

[3]:Défossez A, Mazaré L, Orsini M, et al. Moshi: a speech-text foundation model for real-time dialogue[J].

[4]:Zhang X, Zhang D, Li S, et al. Speechtokenizer: Unified speech tokenizer for speech large language models[J]. arXiv preprint arXiv:2308.16692, 2023.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces WavTokenizer, while preserving the classical acoustic codec model paradigm, achieves high-quality audio reconstruction using only 40 or 75 tokens per second. By proposing a larger codebook space, integrating attention mechanisms, and extending the context window, WavTokenizer demonstrates impressive results in audio reconstruction, semantic understanding, and downstream TTS tasks.

### Strengths
- The acoustic codec representation model is a crucial technology in the current speech domain. WavTokenizer addresses one of the core challenges in the field by achieving high-quality audio reconstruction with only 40 or 75 tokens.
- WavTokenizer introduces a novel single-layer quantizer concept, demonstrating its potential in TTS tasks and offering a promising single-layer solution for codec-LLM architectures.
- From a methodological standpoint, WavTokenizer revisits vector quantization (VQ) in the speech domain and proposes a larger codebook space, a more powerful decoder (with attention mechanisms), and an extended context modeling window. These innovations appear to be effective.
- The model achieves strong experimental results across reconstruction tasks, semantic understanding tasks, and downstream TTS tasks.
- The open-sourcing of the complete training and inference code, along with model weights, will contribute to the development of the research community.

### Weaknesses
Overall, this work does not present significant weaknesses. However, the design of a highly powerful decoder in WavTokenizer raises some concerns. Specifically, I am concerned that the increased model parameters and the introduction of attention mechanisms may potentially slow down the codec's reconstruction speed?

### Questions
- How was VQ utilization calculated in Figure 2(b) of the paper?
- It seems that WavTokenizer is not inherently streamable. Can WavTokenizer be extended to support streaming encoding and decoding?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces WavTokenizer, a GAN-based neural audio codec that uses a single vector quantization (VQ) codebook, in contrast to previous methods that rely on multiple residual vector quantization (RVQ) codebooks. This results in a bitrate as low as 480 bits per second, and to recover quality, the authors propose replacing the time-domain decoder with a Fourier-based decoder, preceded by attention layers. The ablation study confirms these design choices, and a comprehensive evaluation, including both subjective and objective metrics, shows that WavTokenizer maintains competitive reconstruction quality with state-of-the-art models.

### Strengths
- The paper effectively motivates and addresses an important problem in neural audio codecs - quantizing audio into a single sequence of tokens rather than multiple sequences, which complicates modeling for downstream tasks.
- It presents useful findings regarding decoder design, which are supported by the ablation study. In particular, a Fourier-based decoder combined with an attention layer yields better results, while a time-domain decoder with attention performs surprisingly worse.

### Weaknesses
While the motivation for scaling the single VQ codebook to many entries is clear, the paper falls short of achieving high codebook utilization when expanding beyond a size of 4096. What the authors list as contributions in VQ, such as k-means initialization and random restarts, are in fact well-established techniques in neural audio compression, and this paper doesn’t offer any novel methods to improve codebook usage. This is somewhat disappointing, given that a key focus of the paper is to provide a single quantizer. More experimentation to scale the VQ codebook is needed, as the current contribution feels more incremental and may be better suited for a different venue.

### Questions
1. Did the authors try other techniques to improve VQ codebook utilization? The current approach closely mirrors EnCodec, but DAC demonstrates that low-dimensional code lookups and L2-normalization can significantly improve RVQ scalability. A useful reference to consider is [1], which shows effective scaling strategies in image reconstruction that could be also valuable for audio codecs. I recommend continuing work on the paper, as a single-quantizer audio codec has potential, but the paper’s current scientific contribution is limited.


2. What is the motivation for evaluating semantic representation? Neural audio codecs are expected to encode low-level acoustic features rather than abstract semantic concepts. Comparing audio codecs on semantic representation could be misleading, especially given the results e.g. all codecs score below 10% on the SLURP dataset, while self-supervised models like HuBERT achieve nearly 50% (not shown in this paper). This gap calls into question the statement on line 445 that "WavTokenizer effectively captures rich semantic information" which may be an overclaim. That said, audio codecs might have a significant impact on representation learning, as shown by EnCodecMAE [2], so it may be more appropriate to treat semantic representation as a downstream task. WavTokenizer's single codebook could be particularly useful for discrete targets in BERT-like setups.

[1] Zhu, Lei, et al. "Scaling the Codebook Size of VQGAN to 100,000 with a Utilization Rate of 99%."

[2] Pepino, Leonardo, Pablo Riera, and Luciana Ferrer. "EnCodecMAE: Leveraging neural codecs for universal audio representation learning."

### Soundness
3

### Presentation
2

### Contribution
2
