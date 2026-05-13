# DM-Codec: Distilling Multimodal Representations for Speech Tokenization

- Decision: Reject
- Scores: 1, 5, 3, 3

## Abstract
Recent advancements in speech-language models have yielded significant improvements in speech tokenization and synthesis. However, effectively mapping the complex, multidimensional attributes of speech into discrete tokens remains challenging. This process demands acoustic, semantic, and contextual information for precise speech representations. Existing speech representations generally fall into two categories: acoustic tokens from audio codecs and semantic tokens from speech self-supervised learning models. Although recent efforts have unified acoustic and semantic tokens for improved performance, they overlook the crucial role of contextual representation in comprehensive speech modeling. Our empirical investigations reveal that the absence of contextual representations results in elevated Word Error Rate (WER) and Word Information Lost (WIL) scores in speech transcriptions. To address these limitations, we propose two novel distillation approaches: (1) a language model (LM)-guided distillation method that incorporates contextual information, and (2) a combined LM and self-supervised speech model (SM)-guided distillation technique that effectively distills multimodal representations (acoustic, semantic, and contextual) into a comprehensive speech tokenizer, termed DM-Codec. The DM-Codec architecture adopts a streamlined encoder-decoder framework with a Residual Vector Quantizer (RVQ) and incorporates the LM and SM during the training process. Experiments show DM-Codec significantly outperforms state-of-the-art speech tokenization models, reducing WER by up to 13.46\%, WIL by 9.82\%, and improving speech quality by 5.84\% and intelligibility by 1.85\% on the LibriSpeech benchmark dataset.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper introduces DM-Codec, a speech tokenizer based on SpeechTokenizer (that distills speech self-supervised model, SM, to audio codec) that additionally distills representations from text LM to audio codec. The DM-Codec architecture uses a streamlined encoder-decoder structure with a Residual Vector Quantizer (RVQ), incorporating LM and SM representations only during training. Evaluation is done by comparing it against existing codec models on the quality of decoded speech.

### Strengths
The only strength of this paper is the idea of leveraging a text-based language model to improve audio codec, which is reasonable and interesting. That being said, the idea is not properly executed in this work (see weaknesses).

### Weaknesses
 - **Novelty**: DM-codec is essentially SpeechTokenizer with additional LM distillation, which is somewhat incremental.
- **Technical correctness**: While the extra text-based target embedding is the only novel component, it's unclear how the text representation and the acoustic representation are aligned. Text embeddings and acoustic embeddings are clearly **not** sharing the same length, but this work did not provide any detail on this. Instead, it uses a misleading notation $n$ to indicate the sequence length of both text and speech representation. Furthermore, the paper does not address the significant discrepancy in sequence lengths between text and audio. Given a typical speech rate of 100-140 words per minute and a codec producing 3000 tokens per minute, the text sequence is substantially shorter than the audio sequence. This implies that only a small fraction of audio tokens are being trained with meaningful text embeddings, while the vast majority are aligned with padding tokens, which is a fundamental flaw in the distillation process.
- **Depth of the study**: The content of the experiment is quite monotonous. It's basically repeating a single set of training and evaluation with different hyper-parameters, loss weights, and backbones. There is no in-depth analysis. For example, how LM distillation can affect bit rate (which is a very common metric for audio codecs), how well the first VQ layer aligns to text after training, does DM-codec possess speaker disentangle ability due to the text distillation (similar to SpeechTokenizer), etc.

### Questions
Most of my questions are covered in the weaknesses, please see above.

In addition, here are some minor questions/suggestions:
- The term speech-to-text (STT) used in the paper, although understandable, is not very common in the field. Is there a reason to not use the more common term automatic speech recognition (ASR)? 
- It would be a good improvement if human evaluation can be involved in the next version.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, a speech tokenizer method called DM-Codec is introduced. In this method, based on the encoder-decoder framework with a Residual Vector Quantizer (RVQ), two novel distillation methods are used to leverage multimodal (acoustic, semantic, and contextual) representations from a language model and speech self-supervised learning model. The experimental results showed the proposed method significantly outperforms state-of-the-art speech tokenization models, reducing WER by up to 13.46%, WIL by 9.82%, and improving speech quality by 5.84% and intelligibility by 1.85% on the LibriSpeech benchmark dataset.

### Strengths
The proposed DM-Codec method improved the existing speech tokenization system which only incorporates acoustic and semantic information (e.g SpeechTokenizer)  by adding textual representations via an LM-guided distillation method.  The contextual information is learned with continuous representation distillation technique, and it’s then combined with the speech self-supervised learning model  (SM) guided distillation. The proposed method is compared with several existing methods, including EnCodec, SpeechTokenizer  and FACodec. The experimental results prove its advantage over these baseline systems. And the ablation studies provide a thorough analysis of the performance of the proposed method.

### Weaknesses
•	The testing set is small. Only 300 audio samples are randomly selected from the LibriSpeech test subset as the evaluation set. Although the author explained that this is to make it consistent with the baseline, but 300 audios are not big enough to get a statistically meaningful conclusion. The results in table 3 maybe a proof of this: We couldn’t get obvious relation between WER and SM/LM loss weights based on these results.  E.g. the author said LM information is more helpful for lower WER but we could see LM weight = 0.9 get higher WER than LM weight=0.3/0.5. 
•	A lot of metrics results are given including the ablation study, some of them are confusing: 
o	The lowest WER in table 3 is 4.07, but it’s 4.05 in table 1. It’s not clear what’s the difference between them. 
o	The best results of WER, WIL, ViSQOL and STOI for system using distillation for both LM and SM in table 1 is 4.05/6.61/3.26/0.937. These results should be obtained by distilling semantic representation with RVQ layers 1 to 8 according to table 4. But in  table 5 and 6, the results for combining LM/SM-guided distillation are only with RVQ layer 1. Why didn’t the author use the best option in table 5 and 6? 
o	In table 5, the results of two LM, BERT and ELECTRA, have similar accuracy for LM-guided distillation only system. But for combined LM and SM-guided Distillation systems, the results are more different, the author didn’t give analysis about the reason for this.

•	In equation 1, for a given speech x, the length of S(:,d) is the token length of text x’ output from LM (n in figure 2). The length of Q(:,d) should be the time length (T’ in figure 2). How to make sure they are the same?  
•	There are several weighting factors in equation 10, how are they decided except LM/SM weights?
•	In the paper of SpeechTokenizer , the speaker similarity also been evaluated. Why isn’t this evaluated in this paper with the proposed method? Do the author think adding LM would increase or decrease the speaker similarity?

### Questions
•	In equation 1, for a given speech x, the length of S(:,d) is the token length of text x’ output from LM (n in figure 2). The length of Q(:,d) should be the time length (T’ in figure 2). How to make sure they are the same?  
•	There are several weighting factors in equation 10, how are they decided except LM/SM weights?
•	In the paper of SpeechTokenizer , the speaker similarity also been evaluated. Why isn’t this evaluated in this paper with the proposed method? Do the author think adding LM would increase or decrease the speaker similarity?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduce a new speech tokenization model that combines acoustic, semantic, and contextual information into a comprehensive multimodal speech representation. The primary contribution lies in DM-Codec's ability to integrate contextual representations from language models and self-supervised speech models to improve speech tokenization accuracy and quality. DM-Codec’s approach highlights the value of integrating multimodal data for speech tokenization, promising advances in speech quality, intelligibility, and contextual preservation in applications.

### Strengths
This work first incorporates contextual representations via an LM-guided distillation method, and it enhancs the retention of acoustic and speech information in reconstructed speech.

### Weaknesses
I do not fully agree that contextual representation should hold equal importance to acoustic and semantic representations. The improved intelligibility of DM-Codec is mainly due to an additional teacher LM serving a distillation role within the RVQ. However, this LM relies on an ASR system (M_STT in Fig2) for transcription. Given this setup, it is difficult to ascertain whether the improvements are driven by 
the Bert LM or by the M_STT ASR system. More importantly, the reason audio codecs are being actively explored today is that they serve as a discretization tool designed for audio LLMs or TTS systems. Unfortunately, I did not see any extension related to this aspect in the paper. In other words, if DM-Codec is based solely on the concept of contextual representation, I believe it would be challenging to consider it a preferred choice when designing TTS or audio LLM systems.
Additionally, from the technical contribution perspective, this work essentially adds an extra LM distillation on top of the SpeechTokenizer. I think this may struggle to meet the acceptance threshold for ICLR.

### Questions
Small suggestion: Table 3 can be replaced by a line chart

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes DM-Codec, a neural codec to tokenize speech via knowledge distillation from language models for better contextualized representations. The experimental results indicate superior speech reconstruction performance on several metrics compared with prior methods.

### Strengths
The authors conducted significance tests, an important analysis that demonstrated the performance gap between methods but was not included in most prior literature. Moreover, the ablation studies are comprehensive and cover most aspects of the method design.

### Weaknesses
1) **LM Guided Distillation (learning target):**
According to the text, the authors did not explicitly mention how they aligned the codec encoder features with the LM hidden representations. It is a commonly known fact that transcribed speech has a significantly shorter utterance length, especially when the transcription is tokenized as words or subword units. Hence, the LM representations of the transcriptions must be shorter than the codec encoder output, leading to a length mismatch when computing the distillation loss. By looking through the code provided in the supplementary materials, line 107 of `extract_rep.py` pads the transcriptions to the length of the logits produced by the wav2vec2-CTC model, but the BERT-based LM only processes the unpadded part of the text sequence, making the actual LM representations consist of a small part of the encoded sequence. Thus, without further speech and text alignment techniques, it is difficult to justify the effectiveness of the LM-guided distillation targets. Also, the distillation loss in Eq. (1) was first proposed by Chang et al. [1], as indicated in the SpeechTokenizer paper.
2) **LM Guided Distillation (necessity):**
In addition to the unaligned learning targets for this distillation approach, the use of a supervised ASR model in this method (wav2vec2-CTC) raises another question: can the transcription (either ground truth or the ASR) directly be used as a supervised target? For instance, CTC ASR can be performed with the RVQ representations as an additional loss. Furthermore, it is still unclear how the contextualized representations relate to speech reconstruction and other applications.
3) **Evaluation tasks and metrics:**
For the speech reconstruction quality evaluation, some commonly used metrics are not reported like mean opinion scores (MOS). Simply reporting automatic assessment results like UTMOS [2] is also acceptable, as they appear in many prior works [3]. When listening to the audio provided in the supplementary materials, I found SpeechTokenizer has a better reconstruction quality, which implies the necessity of including MOS. Besides speech reconstruction, other downstream applications of the proposed speech tokenizer are not considered in this paper. For instance, ASR, TTS, and spoken language modeling could be used.
4) **Baseline comparison:**
The authors missed a very simple baseline, which is DM-Codec without any distillation objectives. Because the implementation and training data of previous tokenizers like EnCodec and SpeechTokenizer might differ from this paper's, the authors must include this baseline to demonstrate the effectiveness of the proposed distillation methods.

### Questions
As mentioned in the Weakness Section, I would like to ask the authors to explain and justify why the LM-guided distillation method is useful even though it seems like the speech and LM representations are not aligned in time. All the issues listed in the Weakness Section must be addressed or answered in order to get a higher rating.

### Soundness
1

### Presentation
2

### Contribution
1
