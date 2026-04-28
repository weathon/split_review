# UniWav: Towards Unified Pre-training for Speech Representation Learning and Generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 5, 8, 6, 6

## Abstract
Pre-training and representation learning have been playing an increasingly important role in modern speech processing.  Nevertheless, different applications have been relying on different foundation models, since predominant pre-training techniques are either designed for discriminative tasks or generative tasks. In this work, we make the first attempt at building a unified pre-training framework for both types of tasks in speech. We show that with the appropriate design choices for pre-training, one can jointly learn a representation encoder and generative audio decoder that can be applied to both types of tasks. We propose UniWav, an encoder-decoder framework designed to unify pre-training representation learning and generative tasks. On speech recognition, text-to-speech, and speech tokenization, UniWav achieves comparable performance to different existing foundation models, each trained on a specific task. Our findings suggest that a single general-purpose foundation model for speech can be built to replace different foundation models, reducing the overhead and cost of pre-training.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
UniWav is an encoder-decoder framework designed to unify pre-training representation learning and generative tasks. With the appropriate design choices for pre-training, UniWav can jointly learn a representation encoder and generative audio decoder that can be applied to both types of tasks.

### Strengths
The paper introduces the first unified pre-training framework (UniWav) for speech representation learning and generation.
UniWav can compete with different foundation models with low bitrate speech tokenization and high-quality resynthesis.

### Weaknesses
1. The results of the method in this paper do not show an advantage over existing methods in speech recognition and speech generation. 
2. In the speech tokenization section, there is a lack of experiments related to the modeling performance of the speech language model (LLM-TTS) as mentioned in SpeechTokenizer[1]. Such experiments could effectively evaluate the potential of the tokenizer proposed in this paper when applied to autoregressive speech synthesis.

### Questions
Can the method proposed in this paper be applied to general audio such as sound and music?

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
The paper proposes UniWav, a unified pre-training framework for speech representation learning and generation. Traditionally, pre-training models for speech have been specialized either for discriminative tasks, like speech recognition, or for generative tasks, such as text-to-speech. UniWav aims to bridge this gap by integrating both functions into a single encoder-decoder model. The encoder is responsible for learning robust speech representations, while the decoder generates speech through Flow Matching.

### Strengths
1. The paper conducts experiments across multiple tasks like speech recognition, text-to-speech, and tokenization. It includes analyses, such as ablation studies and mutual information metrics.
2. The paper is well-organized and clearly presents technical details, such as the encoder-decoder structure and the Flow Matching method, making it easy to follow. Visual aids and concise explanations further contribute to the clarity of the complex concepts.

### Weaknesses
1. Firstly, I have some doubts regarding the motivation and novelty validation in this paper. The introduction states that ideally, speech representation learning and generation can mutually enhance each other and that this approach can reduce the overhead and cost of pre-training. However, I did not find evidence for these conclusions in the experimental section. Specifically, it seems that the paper does not address whether pre-training on just one task (either speech representation learning or generation) would yield better performance on downstream tasks compared to simultaneous pre-training on both tasks. Additionally, the model's performance on downstream tasks does not appear to be very strong; for instance, its performance on the speech recognition task is worse than that of other baselines. So the experiments can not show that the overhead and cost can be reduced. Because there is neither proof that pre-training on both tasks together is better, nor evidence that there are significantly better results on a single downstream task. If these advantages cannot be clearly demonstrated, then why combine the two tasks? Merely putting speech representation learning and speech generation together without thoroughly explaining the rationale and benefits of this approach significantly limits the contributions of the paper. Overall, the results seem to contradict the stated motivation and novelty, or these points have not been well validated.

2. Secondly, the selection of baselines in the paper is quite limited, especially for the speech generation and tokenization tasks. Speech generation could be compared with Natural Speech 3 [1], while the speech tokenization task could benefit from comparisons with the latest models like Funcodec [2], Encodec [3], and DAC [4]. Furthermore, the paper should include comparisons with the experimental results of DinoSR for both the speech recognition and tokenization tasks, as the encoder component of the paper is primarily based on the DinoSR model.

3. Lastly, the metrics used for evaluating downstream tasks are insufficient. For example, in the speech generation task, subjective evaluations such as Mean Opinion Score (MOS) should be included, as this is a critical metric. For speech tokenization, additional metrics related to speech reconstruction, such as Mel/STFT distance, could be incorporated.

### Questions
1. How does the experimental section provide evidence for the claim that simultaneous pre-training on speech representation learning and generation enhances performance compared to pre-training on only one task, and what justifies the assertion of reduced overhead and cost?

2. Could you include comparisons with models like Natural Speech 3, Funcodec, Encodec, DAC, and DinoSR to improve the evaluation of the proposed methods in speech generation and tokenization tasks?

3. Could you incorporate additional subjective and objective metrics, such as Mean Opinion Score (MOS) and Mel/STFT distance, provide a more comprehensive assessment of model performance?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work proposes a self-supervised speech representation learning objective which combines 1) masked prediction with online clustering from an EMA teacher model (DinoSR) to train a transformer-encoder network and 2) reconstructing noise-inserted input data based on the encoder representations with Flow Matching to train a transformer-decoder network. The aim of this method is to unify the creation of foundation models for discriminative tasks (such as ASR) and generative tasks (such as TTS). 

The method is evaluated by pre-training on 60k hours of LibriLight, and fine-tuning for speech recognition, speech synthesis, and speech tokenization and resynthesis, on Librispeech. 

For speech recognition, they show limited degradation of performance compared to SSL methods like HuBERT, WavLM, and data2vec.   
For speech synthesis, they show performance matching contemporary models like VoiceBox and SpeechFlow.  
For speech tokenization and reconstruction, performance exceeds SpeechTokenizer and HuBERT+HifiGAN.  

The method is also ablated on the encoder and decoder depth, which shows that a 12-layer encoder does not benefit from adding the decoder objective, while a 24-layer encoder does benefit. Moreover, it is shown through a mutual-information analysis that their encoder has different characteristics on how speaker and speech information is processed compared to HuBERT.

### Strengths
### Originality

The method proposes a new speech SSL method, combining existing methods DinoSR (encoder-only) and SpeechFlow (encoder-decoder) . This method has strong performance on generative and discriminative tasks compared to foundation models which are generative-only or discriminative-only. 

### Quality

The method is evaluated on multiple speech technology tasks, and a small ablation study is performed for further insights. 

### Clarity

The paper is well-written, easy to follow, and appropriately places itself into existing literature.

### Significance

This work will definitely spark future work in the speech community.

### Weaknesses
### domain
This works only evaluates on Librispeech, i.e., the audio book domain, which has very homogenetic speaker conditions. The observation that ASR performance closely matches HuBERT, WavLM, etc, does not take into account the robustness these models have to other domains. The authors could discuss this limitation or add experiments with the SUPERB benchmark.

### modelling
As the proposed method is an extension of DinoSR, it would be nice to see UniWav w/o decoder, as in Table 3 for 200k steps, in Table 1 with 600k steps of pre-training. Moreover, Speechflow also uses an encoder-decoder model. This encoder could in theory be fine-tuned for ASR. The original work did not do this. Can the authors comment on expected results when the SpeechFlow encoder would be fine-tuned for ASR, and how this would compare to UniWav? Could this be discussed in a future work section?

### speaker recognition
One of the central claims is that UniWav bridges the inherent orthogonality between speech recognition, which normalizes over speaker and environment information, and speech synthesis, which requires speaker and environment information. This is touched upon slightly by the mutual information analysis, where UniWav is seen to lose speaker information through the encoder layer. It would seem to me that UniWav will not be better for the speaker recognition task than, e.g., WavLM, based on the speculation that most environment and speaker information is stored in the decoder. I think evaluating UniWav on the (SUPERB) speaker recognition and speaker verification task would strengthen the claim significantly. I think for now, this limitation should be made more explicit in the limitation section, or if possible, the authors could perform additional experiments on SUPERB.

### Minor comments

1. line 215: Encodec has not been introduced yet, so cite it here. I find this paragraph confusing due to missing context on how the network uses Encodec as input features (line 239) instead of Mel spectrograms as suggested in line 108. 
2. line 236: \proposed~is
3. line 242: in~\ref 
4. line 358: kmeans instead of k-means
5. line 370: we follow...run k-means, use e.g., by first identifying .. on which to run

### Questions
1. Based on Figure 2, have the authors considered only conditioning the decoder on the first, e.g., 12 layers of the encoder? 
2. Can the authors clarify how speaker similarity is computed? Is it the average cosine similarity between the WavLM speaker embedding of pairs of ground-truth and synthesized utterances? If so, I think it would make sense to share the standard deviation as well. 
3. Can the authors comment on their batch size and how they are sampled (e.g., like wav2vec 2.0)? This would help with reproducibility, and figuring out how much data is seen throughout pre-training, and where UniWav lies in Figure 2 of the DinoSR paper (trade-off between performance and data efficiency)
4. Line 233, "sinusoidal pos. enc. is appended to the input." Is this appended to the feature dimension or the time dimension? Isn't it normally the case that positional embeddings are summed with the input features? Can the authors comments on this design decision?

### Soundness
3

### Presentation
4

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
This paper introduces UniWav, a new pre-training framework focused on both speech representation learning for discriminative task and for generation task. Using an encoder-decoder architecture, UniWav learns speech representations and generates speech together, letting it perform well in both discriminative tasks and generative tasks. UniWav aims to unify the approach, simplifying the speech processing pipeline and reducing need for many specialized pre-trained models. Experiments in speech recognition, text-to-speech synthesis, and speech tokenization show UniWav's effectiveness, achieving results competitive with other top models for specific tasks.

### Strengths
The paper is well motivated to jointly pre-train for discriminative and generative tasks. The paper shows SOTA, if not comparable, results on the generative tasks and lag a little on the discriminative task.
They show very good results when tokenizing speech using UniWav, compared to other works in the literature.  
The paper is well written.

### Weaknesses
The authors propose UniWav, a pre-training method for jointly learning representations for both discriminative and generative tasks in speech processing. This method uses an encoder-decoder architecture to learn effective representations as part of the training process.

For the discriminative task of speech recognition, the authors fine-tune the encoder on 100-hour and 960-hour splits, showing competitive results compared to other methods. However, they do not provide results for low-resource scenarios (e.g., 10 hours or 1 hour of data) or results using a frozen encoder (SUPERB benchmark). These two setups are essential to support their claim that the learned encoder representations are effective for speech recognition tasks. Because with large finetuning data, effect of pre-training is less. 

Figure 2 shows that the encoder’s full capacity is not optimized for learning features specific to speech recognition. UniWav achieves the highest mutual information (MI) on layer 10 out of 24, which then gradually decreases. This pattern suggests that the model divides its capacity between the discriminative and generative tasks, similar to observations in WavLM and prior works. This could explain UniWav’s strong performance in speech generation tasks, as a significant portion of the model’s capacity is allocated to optimize for generation. This trend is consistent across the paper’s reported results.

Regarding speech tokenization, it’s unclear if the comparison is entirely fair. For speech tokenization, the input to the SpeechTokenizer is raw audio, while for UniWav, the input is Encodec encoder features, which are further transformed by UniWav’s 10-layer encoder. It is as if UniWav is heavily overparameterized and most of the parameters are used for generation task.

### Questions
On line 108, the authors claim that the model uses mel spectrograms as input, but on lines 239–240, they mention using Encodec features instead.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a framework named UniWav. It is an encoder-decoder framework aimed at unifying pre-training representation learning and generative tasks. The authors claimed that this is the first such framework and achieves comparable performance to different existing foundation models, each trained on a specific task, on speech recognition, text-to-speech, and speech tokenization tasks.

### Strengths
The main contribution of this work is the combination of DinoSR and a flow matching model to train a unified representation model. While not considered significant, this special setup is somewhat novel.

The paper contains sufficient experimental results to support their claims although some setups are questionable (in detail below). 

The paper clearly indicated the limitations of the work.

### Weaknesses
The claim their work is "the first unified pre-training framework for speech representation learning and generation" is arguable. For example, the paper "Speechgptgen: Scaling chain-of-information speech generation." introduced an approach to train a discrete representation that works for both understanding and generation. The paper "Moshi: a speech-text foundation model for real-time dialogue" further improved the approach.

The presentation needs to be improved.
1. the DinoSR part in Figure 1 is confusing since the softmax layer is not clearly shown since the encoder, according to the text description, does not include that layer. In contrast, the figure in the original DinoSR paper is very clear.
2. The majority of Section 2.1 is describing DinoSR. However, notation is not clearly explained sometimes. for example, what is "k" in s^k_v right below eq. 3? it's unclear why Euclidean distance (instead of COS distance) is used given that Cos distance is usually more preferred in higher-dim spaces.
3. notation "z" is overloaded in eq 9.
4. the footnote under Table 1 is not clear. alignment is only used for generation tasks?
5. eq 11 is wrong? argmin returns an index instead of a representation.

When researchers train a representation model they usually keep the encoder fixed when using them in downstream tasks such as ASR. however, in this work the encoder is finetuned. This causes the claims weaker. Similarlly if flow matching is used in the generation part the quality of the generated speech will of course become better. However, this gain comes from the flow matching model instead of the way the representation is learned. Some clarification here is needed.



### Questions
why "For speech recognition with a shallow encoder, we found introducing the decoder degrades WER regardless of the size. Interestingly, an opposite trend is observed when the encoder size is doubled"? This is something requires more analysis and explanation.

In section 3.1, "We extract the prequantized latent feature from a 16kHz EnCodec (D´efossez et al., 2022) encoder, pre-trained on the same dataset, to serve as the input for our model." This is contradictory to the claim in early sections that the input to your model is mel spectrum?  In addition, this makes the comparison with other approaches unfair since you used another model as the pre-processing module (i.e., total model size is actually increased significantly).

### Soundness
3

### Presentation
3

### Contribution
2
