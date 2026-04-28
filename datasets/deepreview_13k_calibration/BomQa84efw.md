# dMel: Speech Tokenization Made Simple

- Decision: Reject
- Avg Score: 5.40
- Scores: 8, 5, 3, 5, 6

## Abstract
Large language models have revolutionized natural language processing by leveraging self-supervised pretraining on vast textual data.
  Inspired by this success, researchers have investigated complicated speech tokenization methods to discretize continuous speech signals so that language modeling techniques can be applied to speech data.
  However, existing approaches either model semantic (content) tokens, potentially losing acoustic information, or model acoustic tokens, risking the loss of semantic (content) information. 
  Having multiple token types also complicates the architecture and requires additional pretraining.
  Here we show that discretizing mel-filterbank channels into discrete intensity bins produces a simple representation (\dmel), that performs better than other existing speech tokenization methods.
  Using an LM-style transformer architecture for speech-text modeling, we comprehensively evaluate different speech tokenization methods on speech recognition (ASR) and speech synthesis (TTS).
  Our results demonstrate the effectiveness of \dmel in achieving high performance on both tasks within a unified framework, paving the way for efficient and effective joint modeling of speech and text. 
  The code will be open sourced.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a novel approach to speech tokenization by discretizing mel-filterbank channels. This method effectively preserves both semantic and acoustic information, offering an interpretable, model-free representation grounded in the raw acoustic space. The authors train a transformer-based language model for speech-text modeling and evaluate their proposed tokenization approach on speech recognition (ASR) and speech synthesis (TTS) tasks.

### Strengths
- The proposed method is efficient, as it avoids hierarchical dependencies among mel-spectrogram channels, allowing for independent modeling of each channel within each frame using a straightforward, decoder-only (LM-style) transformer architecture.
- The approach is robust, simple yet innovative, with comprehensive evaluations that support the design choices.
- The encoder operates independently of the decoder, unlike many other tokenizers, making it compatible with any vocoder that accepts mel-spectrogram inputs.
- A detailed analysis of the setup is provided to enhance reproducibility.
- The paper is well-written and easy to follow, with a comprehensive analysis included.

### Weaknesses
 - The evaluation could be more thorough by incorporating existing benchmarks such as Codec-Superb and DASB, allowing for a more comprehensive comparison of the proposed method against existing models under standardized settings.
 
- The related works section could be expanded to include methods that use frequency domain inputs, such as those discussed in the following papers:
    -  https://arxiv.org/pdf/2406.05298
    -  https://arxiv.org/pdf/2201.09429
    -  https://arxiv.org/pdf/2405.00233
    -  https://arxiv.org/pdf/2402.10533
    -  https://www.arxiv.org/pdf/2406.07422
- While Hubert-KM, Encodec, and Speech Tokenizer are reasonable baselines, it would be beneficial to include additional baselines with more similar setups, such as SPECTRAL CODECS (https://arxiv.org/pdf/2406.05298) or SemantiCodec (https://arxiv.org/pdf/2405.00233), for a fuller assessment.
- The proposed model is only evaluated on speech data, leaving other domains, such as general audio and music, unexplored.

### Questions
refer to weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents dMel, an encoder-free speech tokenizer that simplifies speech tokenization by discretizing log mel-filterbank outputs into discrete intensity bins, eliminating the need for complex encoding architectures. Unlike previous tokenization methods that separate semantic and acoustic information, dMel maintains both in a single, unified representation. The tokenization process reduces precision of each filter output per frame while retaining the essential information needed for high-quality speech resynthesis, achieved by leveraging pre-trained vocoders. Additionally, the paper explores the application of dMel in language model (LM)-style training for both automatic speech recognition (ASR) and text-to-speech (TTS) tasks. The results demonstrate that dMel performs comparably or better than existing methods in preserving semantic content and reconstructing natural-sounding audio. This efficient, unified approach to speech tokenization facilitates streamlined ASR and TTS training, advancing joint modeling of speech and text.

### Strengths
- The idea of quantizing mel spectrogram as tokenization is interesting and simple (in a good way).
- Results on TTS and ASR show dMel quantization has a small impact on models trained on continuous representation, training downstream models on top of dMel also provided similar results to their continuous counterparts.  These observations are interesting, showcasing the generalizability of dMel.
- Overall, I believe dMel is much more efficient in terms of model size and inference speed comparing to existing speech tokenizers (but this part is not well evaluated in the experiment section, see weaknesses).

### Weaknesses
 - As a speech tokenization paper, this work lacks a discussion on the overall bit rate for compression besides frame rate. Especially in the comparison with the prior works (e.g., Table 3).  dMel is over 12.8kbps~5kbps (assuming 40 fps $\times$ 32 mel filters $\times$ 4 bit-per-filter)~, which is higher than Hubert-KM and Speech Tokenizer. The paper does not adequately address the implications of this higher bit rate, particularly when compared to existing tokenization methods that achieve similar or better performance at lower bit rates. This omission is significant because bit rate directly impacts storage requirements, transmission bandwidth, and computational complexity in downstream applications. The comparison in Table 3 is therefore incomplete without considering this crucial factor.

- This paper spent most of the space discussing ASR & TTS systems based on dMel. While the numbers are good, it is still not as good as a normal mel spectrogram (which is expected). This makes the content of the paper somewhat sparse, which is the biggest weakness in my opinion. The current paper seems to only suggest dMel is a spectrogram quantization approach, as it is essentially lowering numerical precision and showing the distortion is minimal on vocoder, ASR, and TTS. It would be more interesting to involve some other studies, for example:
  - Efficiency-related studies, such as how the encoder-free and lightweight-decoder design of dMel can speed up or lower memory usage downstream applications. The paper does not provide a detailed analysis of the computational benefits of dMel's architecture compared to other tokenization methods, especially in terms of inference speed and memory footprint. A thorough evaluation of these aspects would strengthen the claims of efficiency.
  - Applications where speech tokenization matters more, e.g., spoken LM [1,2], would better justify whether dMel can be viewed as a good speech tokenization approach. The current evaluation is limited to ASR and TTS, which are not the most demanding applications for speech tokenization. Exploring the performance of dMel in tasks such as spoken language modeling, which require more robust and efficient token representations, would provide a more comprehensive assessment of its capabilities. These scenarios/experiments would all be more suitable (than just plain ASR/TTS WER/MOS) for assessing the value of dMel. (I would like to note that these are not concerns that are expected to be addressed during the ICLR rebuttal period, they can be viewed as suggestions for future version of the paper)

### Questions
- Is there a fundamental difference between finite scalar quantization (FSQ; [1]) and dMel's quantization?
If not, I think the FSQ paper should be acknowledged.

[1] https://arxiv.org/pdf/2309.15505

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes dMel, a simple method for quantizing Mel spectrograms into discrete units for LM-style decoder-only ASR and TTS. Unlike self-supervised semantic tokens and neural codecs, dMel is parameter- and optimization-free. Experimental results indicate superior ASR and TTS performance compared to prior methods like HuBERT + K-means and SpeechTokenizer.

### Strengths
The proposed dMel mitigates the issues in existing speech tokenizers. First, prior works like self-supervised learning (SSL) based tokenizers require extensive pre-training and sometimes not being able to preserve acoustic details for speech generation and synthesis. Second, neural codecs preserve fine-grained acoustic representations but might not be able to perform ASR and TTS because of the weak correlations between codebooks and frames. The authors propose a parameter- and training-free approach to achieve similar ASR and TTS performance.

### Weaknesses
Despite the success of the dMel method presented in the experiment results, the following issues question its novelty and effectiveness.

1) **Bitrate:**
Bitrate is a crucial metric for comparing different tokenizers in prior studies but is not included in this paper. According to the provided information, dMel@40Hz, HuBERT-KM, and SpeechTokenizer, respectively, have bitrates of 12.8, 0.4, and 4kbps. The huge difference in bitrates might lead to an **unfair comparison**. Moreover, the number of centroids of K-means clustering in HuBERT-KM could be increased since 200 is considered a small codebook size (Table 2), while 500 and larger values are more commonly used in past literature.

2) **Baselines:**
Advances in speech tokenization techniques have improved many downstream applications, including ASR and TTS. However, this paper only compares dMel with HuBERT + K-means and SpeechTokenizer, where the K-means method was proposed in 2021 [1]. Also, speech tokenization papers usually consider spoken language modeling a standard evaluation task [2,3,4].

3) **Writing:**
Writing could be improved with the assistance of writing tools, including LLMs. For instance, from lines 299 to 301, the original text is "From Table 3, we can see that semantic tokenization (HuBERT-KM) is not good for speech reconstruction. Meanwhile, acoustic tokenizers that are optimized to reconstruct the signal directly (EnCodec and SpeechTokenizer) do well." The sentence is generally clear, but in academic writing, it's often better to use more precise language and avoid subjective terms like "not good" or "do well." A revised version is "Table 3 shows that semantic tokenization (HuBERT-KM) performs poorly in speech reconstruction, while acoustic tokenizers optimized for direct signal reconstruction (EnCodec and SpeechTokenizer) demonstrate superior performance."

### Questions
1) What are the hyperparameters for extracting log Mel spectrograms? Window size? Stride?
2) Why are the model names "RichASR" and "RichTTS?" Any specific reasons?
3) What is the codebook utilization rate or distribution of dMel? The proposed quantization approach divides the intensity into equally-spaced bins. However, a potentially better way is to assign bin sizes according to the data distribution for a uniform codebook utilization.
4) Does pre-training the LM with speech-only data help downstream performance? In spoken LM applications, it is common to pre-train the LM on speech tokens with large unlabeled data.
5) Are there any decoding techniques involved in RichTTS and RichASR? E.g., beam search.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work propose to discretize mel-spectrum into a special kind of intensity bins, which is proved to be a simple representation but more effective than commonly used speech tokenizers (i.e., codec). The authors claim that the newly proposed dMel well carry both acoustic and semantic information within speech signal, without losing information during quantization like codec. Experimental results have proved the effectiveness in tts and asr tasks.

### Strengths
- New idea of using mel spectrum, which is continuous signal, for language modeling. This is different from recently popular codec based TTS.

### Weaknesses
 - For TTS and ASR evaluation, there are only limited baselines for comparison, more powerful models like vall-e (TTS) and whisper (ASR) should also be included.
- The results of dMel are only reported on top of RichTTS and RichASR, experiments on more backbones are expected for better evaluation.

### Questions
- For RichTTS and RichASR, what about the implementation details like architecture/training data (compare to speechgpt?)
- Is there any open-source plan to support the community?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work propose to solve the problem of codec: it is hard for one codebook to cover both semantic and acoustic information, but multiple codebook will complicate the architecture and require additional pretraining. Therefore, this work proposes to discretize mel-filterbank channels into discrete intensity bins, which produces a simple representation that outperforms existing speech
tokenization methods.

I believe this is a pioneering work that may open a potentially new track of TTS research --> use continous mel to replace discrete codec in lm base TTS.

One question:
- How is it compared to another similar work MELL-E (https://arxiv.org/abs/2407.08551) that also use continous mel tokens for lm based TTS?

### Strengths
see above

### Weaknesses
see above

### Questions
see above

### Soundness
3

### Presentation
3

### Contribution
3
