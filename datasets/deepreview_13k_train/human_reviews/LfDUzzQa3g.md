# RepCodec: A Speech Representation Codec for Speech Tokenization

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
With recent rapid growth of large language models (LLMs), discrete speech tokenization has played an important role for injecting speech into LLMs. However, this discretization gives rise to a loss of information, consequently impairing overall performance. To improve the performance of these discrete speech tokens, we present {\rpc}, a novel speech representation codec for semantic speech tokenization. In contrast to audio codecs which reconstruct the raw audio, {\rpc} learns a vector quantization codebook through reconstructing speech representations from speech encoders like HuBERT or data2vec. 
Together, the speech encoder, the codec encoder and the vector quantization codebook form a pipeline for converting speech waveforms into semantic tokens. 
The extensive experiments illustrate that {\rpc}, by virtue of its enhanced information retention capacity, significantly outperforms the widely used k-means clustering approach in both speech understanding and generation. Furthermore, this superiority extends across various speech encoders and languages, affirming the robustness of {\rpc}.
We believe our method can facilitate large language modeling research on speech processing.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A novel RepCodec, a speech representation codec for semantic speech tokenization, has been introduced. RepCodec utilizes a vector quantization codebook to reconstruct speech representations from speech encoders like HuBERT or data2vec. RepCodec significantly outperforms the widely used k-means clustering approach in both speech understanding and generation tasks.

### Strengths
The paper is great in its clarity and well-structured organization. Its proposed approach is lauded for its simplicity and effectiveness. The comprehensive nature of the experiments conducted further strengthens the paper's credibility. Based on these positive aspects, it is recommended for publication at the conference.

### Weaknesses
The simplicity and effectiveness of the proposed approach are commendable. While there are no significant weaknesses to highlight, it would be intriguing to see the application of RepCodec in the context of zero-shot Text-to-Speech (TTS) systems, such as Vall-E. Exploring its potential in this domain could provide valuable insights and possibly further advancements in speech-processing technology.

The idea of SpeechTokenizer (SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models) has some similarities, could you please elaborate more regarding the difference? If possible, adding some baseline numbers using https://github.com/ZhangXInFD/SpeechTokenizer would add value to this paper.

### Questions
See comment in the Weaknesses.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces RepCodec, a speech representation codec designed for semantic speech tokenization. It applies VQVAE to the representations from pretrained speech encoders to learn audio semantic tokens. The authors demonstrate the superiority of their proposed method over other discrete speech representation techniques, as evidenced by improved WER scores on ASR and speech resynthesis tasks.

### Strengths
* The authors demonstrate the superiority of their proposed method over other discrete speech representation techniques in terms of the WER scores on both ASR and speech resynthesis tasks.
* The authors analyze the issue with the quality measure of semantic tokens based on their similarity to ground truth phonemes, while illustrating that the reconstruction loss of their proposed method exhibits a higher correlation.

### Weaknesses
 * Insufficient evaluation metrics. The research predominantly relies on WER as the principal evaluation metric for the performance of semantic speech tokens. To make a compelling case for the proposed method's superiority, it's essential to include other the evaluation metrics such as speaker similarity, F0 error, or mean-opinion score in the speech resynthesis experiments. Specifically, the lack of speaker similarity metrics makes it hard to assess if the method preserves speaker identity during resynthesis, and the absence of F0 error metrics leaves the quality of prosody generation unclear. Furthermore, relying solely on WER, which primarily measures content accuracy, neglects other crucial aspects of speech quality.
* Limited exploration of core downstream tasks. While semantic tokens are integral to token-based language modeling of speech, the paper's experiments are primarily focused on ASR and speech resynthesis. It lacks empirical investigations into other vital application tasks such as language modeling of audio, text-to-speech, speech-to-speech translation, or conditional modeling of acoustic tokens given the semantic tokens. The absence of language modeling experiments, for example, makes it difficult to assess the utility of the learned tokens for capturing sequential dependencies in speech, a key aspect of semantic representation. Similarly, the lack of text-to-speech experiments leaves open the question of how well the tokens can be used to generate speech from text, a critical task for many applications.

### Questions
I have concerns regarding the lack of evaluation results, as mentioned in the above weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, a speech representation code called RepCodec is introduced for semantic speech tokenization. It is seamlessly integrated into an end-to-end framework.

### Strengths
1. RepCodec demonstrates promising results in both ASR and unit-to-speech resynthesis compared to the clustering method.
2. The discovery that PMNI can deviate from performance is intriguing.

### Weaknesses
1. Overall, this paper lacks novelty, as compared to SouldStream, it simply replaces the input from raw waveform with SSL representations.
2. Some parts of the details in this paper are confusing:
    * The difference in bar height in the encoder and decoder parts in Figure 1 is confusing because neither sampling nor dimension reduction is applied.
    * Equation (5) lacks sufficient explanation. I am unsure of its correctness as neither ${\overset{\sim}{n_k}}$ nor $\mathbf{e}_{i}$ is adequately defined or explained. 
    * Shouldn't equation (7) be
$ F^* = \arg\max_F p(\mathbf{y}|\mathbf{s}) = \arg\max_F \prod_{i=1}^{m} p(y_i|y_{<i}, \mathbf{s}) $?

3. It would be better to include a more in-depth analysis of the weights ($\lambda_{r}$, $\lambda_{q}$) of reconstruction loss and quantization loss.

### Questions
3. Is WER a common metric for speech resynthesis?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed a new speech tokenization for semantic modeling in this paper. Previous methods usually use k-means to discrete semantic representation, leading to information loss. Inspired by the audio codecs which reconstruct the raw audio, RepCodec encodes speech semantic representation from Hubert or data2vec to a set of vector quantization codebooks and reconstructs them by a decoder. The experiments demonstrate the superior performance of RepCodec in speech understanding and generation. Many detailed experiments also evaluate the performance in different configurations.

### Strengths
The motivation and description of the proposed method are very clear and easy to understand. The experiment is sufficient and demonstrates the effectiveness of RepCodec.

### Weaknesses
1. In the introduction, the term "semantic quality" is mentioned. For clarity and the benefit of readers, could you provide a definition on what "semantic quality" encompasses?
2. In previous works such as VALLE, AuidoLM, and PolySpeech mentioned in this paper, they all use the k-means clustering method to obtain semantic tokens. For the speech generation task (TTS, VC), the semantic information is important in discrete tokens, but the other 
encoded information such as speaker timbre is harmful to the task. Given the importance of speaker timbre information for downstream speech generation tasks, it would be of great value if a verification for speaker information of the encoded features is incorporated.



### Questions
1. Section II.Speech Tokenization. "However, the discretization step of k-means discards plenty of information of the speech“. Can you give some examples so that readers can better understand the limitations of k-means?
2. The first paragraph in Sectiion III. "In AudioLM (Borsos et al., 2023), the WER is dramatically increased from 2.5% to 6.0% by using the discrete tokens of k-means from w2v-BERT XL". What does this number 2.5% refer to? 
3. In Equation 5, some symbols are not defined. 
4. One question not related to the proposed method.  Why does the performance gap change among different speech encoders after VQ and K-means quantization compared with the original speech representations, especially whisper.  In other words, what kind of representations are suitable for clustering?
5. Can you provide some samples of the speech resynthesis?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
