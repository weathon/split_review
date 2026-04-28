# Zero-Shot Text-to-Speech from Continuous Text Streams

- Decision: Reject
- Avg Score: 4.60
- Scores: 3, 6, 6, 5, 3

## Abstract
Existing zero-shot text-to-speech (TTS) systems are typically designed to process complete sentences and are constrained by the maximum duration for which they have been trained. However, in many streaming applications, texts arrive continuously in short chunks, necessitating instant responses from the system. We identify the essential capabilities required for chunk-level streaming and introduce \modelname, a stream-aware model that supports infinitely long speech generation, text-audio stream synchronization, and seamless transitions between short speech chunks. To achieve these, we propose (1) adopting Mamba, a class of sequence modeling distinguished by linear-time decoding, which is augmented by cross-attention mechanisms for conditioning, (2) utilizing rotary positional embeddings in the computation of cross-attention, enabling the model to process an infinite text stream by sliding a window, and (3) decoding with semantic guidance, a technique that aligns speech with the transcript during inference with minimal overhead. Experimental results demonstrate that our models are competitive with state-of-the-art language model-based zero-shot TTS models, while also providing flexibility to support a wide range of streaming scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents L3Speech, a stream-aware zero-shot text-to-speech (TTS) model designed for continuous text input in short chunks, which is crucial for streaming applications. It leverages Mamba for linear-time decoding, rotary positional embeddings for infinite text stream processing, and semantic guidance for efficient text-audio synchronization. Experimental results demonstrate L3Speech's competitiveness with some other TTS systems while offering flexibility for various streaming scenarios.

### Strengths
The paper introduces L3Speech, a Mamba-based TTS system designed for continuous text input in short chunks, essential for streaming applications.

1. This paper explores the use of Mamba as the backbone for AR-based TTS.

2. It proposes a decoding method assisted by semantic guidance to enhance model stability.

3. Various tricks, such as improved rotary positional embeddings, are designed to improve the model's performance in streaming inference, including streaming text input.

### Weaknesses
The paper introduces L3Speech, a Mamba-based TTS system designed for continuous text input in short chunks, essential for streaming applications. It proposes techniques such as rotary positional embeddings for infinite text stream processing, semantic guidance, and optimized text chunk length and quantity selection. However, it has notable weaknesses, including:

1. Although this paper claims to support infinite text input and streaming inference, it only evaluates on the LibriTTS dataset. I think this dataset cannot truly demonstrate the model's benefits for long text input and streaming inference. The authors should evaluate on more suitable test sets, such as those containing longer dialogues or narratives, to properly assess the model's performance in realistic streaming scenarios. Additionally, the baselines chosen for comparison are relatively weak, as they do not include more advanced models like VoiceBox, NaturalSpeech 3, and CosyVoice. The absence of these state-of-the-art models makes it difficult to gauge the true competitiveness of L3Speech.

2. The authors did not demonstrate the necessity of the Mamba architecture, I think transformers could also achieve the same methods. The paper lacks a thorough ablation study comparing Mamba with a transformer-based architecture, which is crucial to justify the choice of Mamba. Without such a comparison, it remains unclear whether the performance gains are specifically attributable to Mamba or if similar results could be achieved with a more conventional transformer model.

### Questions
1. Do you evaluate the model on alternative datasets that would be more suitable for evaluating the performance of L3Speech in streaming scenarios?

2. Do you compare the model with more powerful TTS systems?

3. What evidence or experiments could you provide to demonstrate the necessity of the Mamba architecture over conventional transformers for achieving the proposed methods?

4. How might the performance of L3Speech differ if implemented with a conventional transformer architecture instead of Mamba?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of zero-shot text-to-speech (TTS) in continuous streaming scenarios, where text input is provided in short chunks, necessitating real-time, low-latency responses. The authors propose L3Speech, a stream-aware model incorporating several novel components: a Mamba-based decoder for efficient, linear-time decoding; rotary positional embeddings to manage continuous text flow; and semantic guidance using grapheme tokens to maintain alignment between text and speech. Experimental results show that L3Speech provides flexibility in streaming scenarios, achieving competitive or superior performance to existing TTS models in terms of content accuracy, speaker similarity, and overall audio quality.

### Strengths
- The paper is well-written and easy to follow. 

- This paper addresses an emerging and impactful area—streaming TTS with integration into large language models. By targeting the latency challenges and supporting flexible, continuous input, the model shows promise for real-time applications.

- The proposed architecture is well-grounded, utilizing the Mamba-based decoder, rotary positional embeddings, and semantic guidance via grapheme tokens. These design choices are technically solid, and their contributions to the model's performance are validated through an extensive ablation study.

- The model supports a range of lookback and lookahead settings, making it adaptable to various streaming TTS applications. This flexibility is an essential feature for practical deployment across different tasks and latency requirements.

### Weaknesses
 - Missing reference section.
- Lack of Real-Time Runtime Analysis: A runtime analysis comparing the proposed method with baselines—especially in scenarios where L3Speech is cascaded with a language model—would provide a clearer picture of the latency benefits. Including this analysis would strengthen the paper by illustrating the real-world efficiency gains.


### Questions
Baseline Comparison with Transformer Decoder: Incorporating a baseline using a transformer-based decoder could further validate the performance and efficiency advantages of the Mamba architecture. There are well-known techniques to improve the inference speed and local attention mechanism. 
This addition would provide a stronger basis for the choice of Mamba over more conventional architectures.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this work, the authors proposed a zero-shot TTS system L3System to supports 1) infinitely long speech generation 2) text-audio stream synchronization 3) seamless transitions among the generated audio chunks. The system includes a speech encoder to generate fix-length embedding from enrollment speech audio, a text module to convert the input text into corresponding embeddings, a mamba based decoder is used to generate audio conditioned on the speech and text representations from the speech encoder and text embeddings. Only text in the related chunks are used for condition during speech generation. During training and inference, semantic guidance generated by a CTC based ASR model is used to alleviated misalignment. The model shows good results as shown in experimental sections. The audio samples provided also show good quality.

### Strengths
- A streaming TTS approach is provided with good results
- Semantic guidance is used to alleviate speech text misalignment.

### Weaknesses
 - Related work is not complete. There are many streaming based TTS models have been proposed, such as Transducer based TTS [1,2], which is time synchronized based and naturally fit to the streaming applications.
- Reference section is missing
- Motivation of some method choices are not discussed, for example,  positional indices based on arrival time. 
- Missing the study of the importance of acoustic model choice during soft guidance. It could be critical for languages with low resource and inferior ASR model.
- The semantic guidance is one of the contributions in this paper. It would be useful to compare the complexity during training and inference time when it is used.
- There are some typos in the paper submitted.

### Questions
- How do we know the generation for one chunk is done? Is it based on the ASR model?
- Motivation to have positional indices based on arrival time? We can get that information during training when the target audio is given, how about inference, especially for $\tau_{f(t)}$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a zero-shot text-to-speech (TTS) system, called L3Speech, aming for real-time speech synthesis from continuous text chunks. Specifically, they 1) adopt a Mamba-based autoregressive decoder for linear-time generation, integrating cross-attention mechanisms utilize enrollment speech and transcript; 2) employ rotary positional embeddings within the cross-attention mechanisms to handle an infinite text stream by sliding a window; 3) apply semantic guidance to mitigate the misalignment between text and speech. The models are trained on LibriLight dataset and evaluated on the test-clean set of LibriTTS. Experimental results demonstrate that the proposed system achieves performance comparable to state-of-the-art TTS models while providing flexibility to balance latency and content accuracy in streaming scenarios.

### Strengths
- The proposed system accesses past and future text contexts in chunk-wise decoding, which improves the performance of steaming TTS. By incoperating semantic tokens (i.e. graphemes) alongside acoustic tokens, the authors address the problem of misalignment in autoregressive generation. These are validated by the ablation studies.  
- The writing style is good, and the English is clear and concise. The provided discussions and analysis are insightful.

### Weaknesses
 - The submitted maniscript does not include the Section of References, which hampers the reading and reviewing process.
- While the authors emphasize the advantage of linear-time decoding with the Mamba-based decoder, they don't provide ablation experiments that compare against a counterpart with transformer-based decoder. I would suggest conducting comparisons in terms of inference time or quality-speed trade-offs at different sequence lengths. Specifically, it is unclear how the proposed Mamba-based decoder compares to a transformer-based decoder in terms of computational cost and generation quality, especially when considering different input sequence lengths. This comparison is crucial for validating the claimed efficiency of the Mamba architecture.
- The authors propose to use rotary positional embeddings in the cross-attention modules where the positional indices are based on arrial time, but don't provide ablation experiments about this. I would suggest comparing to using fixed positional encodings and no positional encodings. The lack of ablation studies on the positional embeddings makes it difficult to assess the impact of the proposed arrival-time-based positional encoding scheme. It is important to understand if the performance gain is due to the specific positional encoding method or other factors.

### Questions
- For line 034-035, the citations are not included in parentheses.  
- For line 190-191, "The speech encoder is a transformer-based encoder that converts enrollment speech of arbitrary length into a fixed-length sequence of embeddings." Could the authors provide more details on how to obtain a fixed-length sequence of embeddings? 
- For line 241-242, should $\tau_{i+1}$ be $\tau_{i}+1$? 
- For line 245-246, I can't understand the formulas of $p(t)$ and $f(t)$. Are they correct? 
- For line 268-270, as the author mentioned "we replace each blank token with the first non-blank tokens to the right of the sequence", but in the given example, why the last two tokens in the processed sequence are still blank tokens? Shouldn't they be "c"? 
- For line 270-272, could the authors provide more details about the upsampling process (from 50 tokens per second to 75 acoustic tokens per second)? 
- In Algorithm 1, for line 310-311, should $p_t^{(g)}$ be the modified (scaled) one? Why is $T_{top-k}$ is not used? Steps in line 306-312 seem not fully consistent with descriptions in line 279-281. 
- For Equaltion 1, the attention formula is not correct. I think the value tensors should be placed out of the softmax function.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This study introduces a low-latency streaming zero-shot TTS system with several key advancements: 1) the adoption of Mamba architecture for linear-time decoding, 2) the incorporation of rotary positional embeddings within the cross-attention module to manage infinite text streams, and 3) the implementation of semantic guidance to enhance system robustness. The proposed system achieves comparable performance in both offline and online inference settings.

### Strengths
- This work presents a novel scenario for zero-shot TTS systems and highlights its non-trivial challenges.
  
- This work validates the feasibility of Mamba, a linear-time decoding sequence modeling architecture, for zero-shot TTS tasks, providing insights that may inspire future research.
  
- The proposed streaming zero-shot TTS model achieves comparable performance in a simluated online inference setting.

### Weaknesses
 - Some key motivations in this paper, such as those mentioned in Table 1, haven't been thoroughly validated. Specifically:
  
  - The authors should consider adding experiments that test the model's robustness with sufficiently long text streams to support its claim of "infinitely long speech streaming" capabilities. The current experiments, limited to 10-20 second samples, do not adequately demonstrate the model's ability to maintain coherence and quality over extended durations. It would be beneficial to evaluate the model on significantly longer text inputs, perhaps several minutes in length, to truly assess its long-range dependency handling. Additionally, it would be beneficial for the authors to design experiments that demonstrate the advantages of modeling entire text streams compared to synthesizing them sentence by sentence. This could involve comparing the proposed model against a baseline that processes text in a segmented manner, with a focus on how the proposed model maintains context and avoids abrupt transitions between segments.
    
  - The authors should compare the performance gap between complete texts and incomplete streaming texts to verify the model's ability to make "seamless transitions between short speech chunks". This comparison should not only focus on overall quality metrics but also specifically analyze the continuity and naturalness of speech at the boundaries between synthesized chunks. A perceptual study focusing on the transitions would be beneficial.
    
  - Furthermore, regarding the "text-audio stream synchronization" capability, there seems to be a lack of clear explanation and corresponding experiments. The paper should clearly define what constitutes synchronization in this context and provide quantitative metrics to evaluate the model's performance in maintaining this synchronization. It is unclear how the model ensures that the generated audio aligns with the incoming text stream, especially when the text input rate varies.
    
  - In addition, the paper positions itself as a low-latency streaming zero-shot TTS system, yet it falls short of providing a latency comparison. The paper should include a real-time factor (RTF) analysis, comparing the proposed model's latency against existing baselines. This analysis should consider the computational cost of the model, including the overhead of the Mamba architecture, and the impact of different batch sizes and hardware configurations on the overall latency.
    
- Some experimental details are missing, which could affect the reproducibility of the proposed system. Please refer to the Questions.

### Questions
- The paper states, "The embeddings can remain unchanged or be updated any time during streaming." on L191. Could you elaborate on the mechanisms for updating the enrollment speech embeddings? Furthermore, were these embeddings actually updated in the experiments conducted?

- Could you provide statistical information for the reference enrollment speech? From experience, the duration of the reference enrollment speech greatly influences the speaker similarity.

### Soundness
1

### Presentation
3

### Contribution
3
