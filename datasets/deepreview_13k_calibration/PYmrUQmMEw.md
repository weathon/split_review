# LLaMA-Omni: Seamless Speech Interaction with Large Language Models

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Models like GPT-4o enable real-time interaction with large language models (LLMs) through speech, significantly enhancing user experience compared to traditional text-based interaction. However, there is still a lack of exploration on how to build speech interaction models based on open-source LLMs. To address this, we propose \name, a novel model architecture designed for low-latency and high-quality speech interaction with LLMs. \name integrates a pretrained speech encoder, a speech adaptor, an LLM, and a streaming speech decoder. It eliminates the need for speech transcription, and can simultaneously generate text and speech responses directly from speech instructions with extremely low latency. We build our model based on the latest Llama-3.1-8B-Instruct model. To align the model with speech interaction scenarios, we construct a dataset named InstructS2S-200K, which includes 200K speech instructions and corresponding speech responses. Experimental results show that compared to previous speech-language models, \name provides better responses in both content and style, with a response latency as low as 226ms. Additionally, training \name takes less than 3 days on just 4 GPUs, paving the way for the efficient development of speech-language models in the future.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposed a Speech-LLM model that can do speech-to-speech conversation with good latency and quality. The central design enables the low latency feature is the proposed streaming speech decoder.

### Strengths
This is probably the first public work that connects a speech-to-text Speech-LLM with a streaming text-to-speech model so as to enable low latency speech outputs.

### Weaknesses
1. The speech-to-text component of this model is not new (relevant works like SALMONN and Qwen2-audio) and the main addition is the text-to-speech component. The latter has a clear connection with the streaming TTS model research but the paper does not spend enough content to acknowledge and compare to this line of research. To elaborate on this, the paper should compare the proposed method with prior research in this space and motivate this unique CTC based design. The paper should also replace the baseline of SALMONN+TTS with SALMONN+streaming TTS so as to have a fair comparison and show the value of the proposed component.
2. The "response latency" used in this paper is misleading. It only considers the latency from streaming speech decoder, but in fact the non-streaming speech-to-text Speech-LLM also has latency which should be considered as "response latency". The paper fails to point this out and didn't give the overview of the latency breakdown given the proposed design
3. The audio quality of the proposed method is not good from the MOS score and is not compared with any external works, which challenges the value of this proposed CTC based design, especially considering there have been prior works in the streaming TTS area. It's hard to understand whether the proposed method is better or worse.
4. "On the other hand, the ASR model we use, Whisper-large-v3, has strong robustness. Even when the speech is somewhat discontinuous with smaller Ω," If this ASR model cannot identify the discontinuity and relevant quality issue, it may not serve well as a way to evaluate the intelligence of the generated speech. This is a limitation.

### Questions
please resolve the concerns in Weaknesses

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes LLaMA-Omni, an end-to-end model architecture designed for low-latency, high-quality speech interaction with large language models (LLMs). LLaMA-Omni integrates multiple components: a pre-trained speech encoder, a speech adaptor, a large language model, and a streaming speech decoder. To enable more natural, human-like speech interactions, the authors introduce InstructS2S-200K, a dataset of 200K speech instructions and responses crafted in a conversational, oral style, to fine-tune the model for speech-based dialogue. Experimental results show that LLaMA-Omni achieves low-latency speech responses while reducing training costs compared to similar models.

### Strengths
1. **Conversational Data with InstructS2S-200K:** The proposed InstructS2S-200K dataset addresses a notable gap in conversational, oral-style speech instruction data. By providing a large, purpose-built dataset tailored to natural, interactive speech patterns, this work supports more effective alignment of LLM responses with human conversational norms. 
2. **Cost-Effective Training Process:** The two-stage training process adopted in LLaMA-Omni demonstrates a practical approach to reducing training costs. Compared to prior end-to-end training methods, this staged training setup optimizes resource use, enabling faster model development without compromising performance.

### Weaknesses
1. **Lack of Novelty:** While the authors suggest that they proposed a "novel model architecture," it appears to primarily build on a combination of existing methods without a clear breakthrough in architecture: 
   1) The connection of a speech encoder to an LLM via a speech adaptor has been widely explored in prior research. 
   2) The streaming TTS module seems to be directly based on previous designs, specifically following the approach outlined in [1]. 
   
    In summary, while LLaMA-Omni successfully assembles a functional pipeline for speech-based interactions with LLMs, the architecture seems to build on prior work without delivering significant innovation in model design, which somewhat limits the paper’s impact from a research innovation standpoint. Further discussion is needed to emphasize the unique contribution of this work.
2. **Questionable Experiment Results:** Some experiment results in this paper is questionable:
   1) **ChatGPT-Score in Table 2:** While LLaMA-Omni shows improved performance over baseline models in ChatGPT-Score, this result is potentially misleading. The evaluation prompt used (detailed in Appendix A) was crafted to reward concise responses and penalize extraneous information. This prompt design aligns closely with the prompts used to construct the InstructS2S-200K dataset, creating a circular evaluation condition where the model is likely to excel by design. A more objective and meaningful approach would involve conducting a human evaluation to capture human preferences more accurately. 
   2) **WER & CER in Table 2:** In Table 2, Qwen2-Audio + TTS shows an unexpectedly high WER of 55.72%, yet it achieves a relatively moderate S2SIF score of 2.32/2.58, which implies a more acceptable response quality. This discrepancy suggests an inconsistency, as such a high WER would typically indicate a low intelligibility level that should correlate with a poor S2SIF score. This contradiction casts doubt on the reliability of the WER measurements or, potentially, the effectiveness of the S2SIF scoring methodology when used alongside TTS outputs.
    
        A likely explanation for these irregularities lies in the TTS model used, VITS, which is primarily trained on **short audio clips** [2]. This limitation may hinder VITS’s ability to process longer inputs effectively, causing high error rates when it encounters the longer outputs of models like Qwen2-Audio and SALMONN. Sending unchunked, lengthy responses directly to VITS without segmentation could result in degraded performance, as evidenced by the elevated WER and CER scores. 

        To address these limitations and obtain more accurate metrics, it would be more appropriate to adopt a TTS model trained for longer utterances or to chunk input text before passing it to VITS. Such adjustments would likely yield more realistic WER and CER values and provide a fairer basis for comparing baseline models.
    3) **Average decoding time in Table 4:** The decoding time reported in Table 4 does not convincingly demonstrate the superiority of the proposed streaming decoding architecture. The average decoding time is measured for generating complete speech responses; however, since baseline methods produce longer responses, they naturally require more time for decoding. This dependency on response length makes the reported decoding times trivial and limits their effectiveness in showcasing any advantages of the proposed approach. To provide a fair and meaningful comparison, it would be more appropriate to compare with Qwen2-Audio + streaming TTS model and report decoding time per token rather than total decoding time. 
3. **Limited speaker support:** While InstructS2S-200K provides valuable conversational data, it has limitations due to the lack of speaker diversity. The input speech in this dataset is synthesized using CosyVoice-300M-SFT, which represents a single voice and does not capture the variability in accents, pitch, tone, and other speaker characteristics found in real-world interactions. This limitation restricts LLaMA-Omni’s adaptability to diverse user-profiles and reduces its effectiveness in applications requiring personalized or varied speaker responses. Integrating a broader range of voices could significantly improve LLaMA-Omni’s applicability in real-world scenarios.

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents an end-to-end spoken dialogue model LLAMA-Omini, which integrates a pretrained speech encoder, a speech adaptor, an LLM, and a streaming TTS module. The model can directly understand continuous speech features and can simultaneously generate text and speech responses directly with low latency. To achieve alignment between different modules, this work also proposes a pipeline for constructing speech-to-speech dialogue data, with a style that better matches the characteristics of speech interaction scenarios.

### Strengths
1. The paper is well-written and presents a promising approach to seamless speech interaction with LLMs. The reported response latency of 226ms is impressive and demonstrates the value for real-world applications.

2. The authors have made a valuable contribution by creating the InstructS2S-200K dataset, which is tailored to speech interaction scenarios. The core motivation for building this dataset is that "in speech interactions, concise yet informative responses are typically preferred", which has not been considered in previous work.

### Weaknesses
1. Although this work presents a seamless spoken dialogue model, the choice of connecting a LLM with a CTC-based streaming TTS module is not well-motivated.
    - Autoregressive TTS models naturally support streaming decoding, but this paper does not discuss or compare with the traditional autoregressive decoding.

    - The CTC-based streaming TTS module incorporates ideas from StreamSpeech [1] and achieves streaming output by segmenting generated units into chunks. However, it is not evident what benefits the end-to-end model offers over a straightforward cascaded solution where the text response is segmented into chunks and then fed into an offline TTS model.

2. Another contribution of this work is the constructed dataset InstructS2S-200K, but there is a lack of sufficient experiments to demonstrate the advantages of this dataset.

   - First of all, the speech input in this dataset is synthesized using CosyVoice-300M-SFT, which can only synthesize standard speech from limited speakers. This may lead to the model only being able to handle tts-synthesized input speech, lacking speaker generalization. Therefore, in order to demonstrate the practical value of this dataset, evaluation on human recorded speech is necessary. For example, ASR and ST performance in academic dataset (LibriSpeech, CoVoST), or evaluation on general benchmarks (such as AIRBench [2]) is necessary to demonstrate the model's understanding of real speech. But this work is only evaluated on their TTS-synthesized InstructS2S-Eval.

   - One advantage of this dataset is that the response is accurate and concise, which is more suitable for the speech interaction scenario. However, in order to prove this statement, human evaluation is very necessary to demonstrate that humans would prefer shorter replies. In Table 1, the author uses GPT4 as a judge, but in Appendix A, we can see that the author has incorporated the need for short and accurate responses into the GPT4 evaluation prompt. This can only prove that the model's responses are accurate and concise, but cannot prove that they are more in line with human preferences.

3. There are some unconvincing evaluation metrics and results analysis.

   - In Table 1, a biased prior has been introduced in the evaluation prompt of GPTscore (see 2.b), therefore the content and style scores are not reasonable.

   - In Table 1, the pipeline models SALMOON/Qwen2-Audio + TTS have very poor alignment scores. Although the authors explained in Line 392-393 that the responses of these two models contain characters that cannot be synthesized into speech, we can see in the case study in Table 5 that SALMMON does not have any unsynthesizable characters, and Qwen2-Audio only has \n that is unsynthesizable. I speculate that the very poor alignment score here is due to the fact that the TTS model used only supports synthesizing speech for around 10 seconds, while SALMOON and Qwen2-Audio generate very long responses that exceed the maximum supported length of the TTS model. I believe the authors need to provide a detailed description of how they used the TTS model, or to segment long text responses into shorter chunks to fed into TTS model to ensure fairness in comparison.

   - Table 4 reports the total time for completing a single response, and it is quite apparent that shorter responses result in shorter completion times. However, this does not provide any new insights or perspectives to demonstrate the advantages of this work.

4. The author emphasizes that LLAMA-Omini is an interactive dialogue model, or a GPT-4o-like model, and therefore needs to demonstrate its ability for multi-turn conversations. However, evaluations have only been conducted on single-turn responses. I think that quantitative metrics or qualitative demos are necessary.

### Questions
1. Could the author please emphasize the contribution of this article?
   - If it is a streaming TTS module, there is a lack of comparison with other streaming generation methods (autoregressive TTS models)
   - if it is the speech instruction dataset, there is a lack of human evaluation to prove its greater alignment with human preference, and the limitations of TTS synthesized speech input also restrict its application
   - if it is an open-source seamless spoken dialogue model, evaluation on real speech benchmarks is also needed.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces LLama-Omni, a novel end-to-end architecture that enables real-time interaction with LLMs through speech. Llama-Omni has a pretrained speech encoder, a speech adaptor, an LLM, and a streaming speech decoder. Speech is fed continuously into the LLM, while text is generated discretely. Then, each text unit is replicated a fixed number of times and aligned with HuBERT k-means units using non-autoregressive CTC. Once the units accumulate to a preset number, they form a chunk and feed to a vocoder for speech reconstruction. This non-autoregressive architecture supports simultaneous text and speech generation from spoken instructions with very low latency, while achieving very low training overhead.

### Strengths
- LLama-Omni carries out a novel non-autoregressive architecture for simultaneous text and speech generation, providing a fresh approach among recent GPT-4o-like models. It achieves a sufficiently low latency of 226ms and high-quality speech interaction, making it suitable for real-time scenarios.

- LLaMA-Omni can be integrated with any open-source LLM at minimal training cost, requiring only 4 GPUs and less than 3 days to train. This makes it accessible for academic research, allowing more institutions and researchers to use high-quality, speech-interactive LLMs.

- One notable strength is that LLaMA-Omni largely preserves the intelligence of pre-trained LLMs.

### Weaknesses
 - One limitation is that the LLM outputs text only. While this preserves its reasoning abilities, it losses richer features such as emotional nuance and speaker identity.

- As the authors mentioned in Section 4.4, the cascaded use of VITS TTS in SALMONN and Qwen2-Audio may introduce errors affecting S2SIF and alignment due to propagated TTS inaccuracies, making this comparison less of an apple-to-apple evaluation.

- The paper lacks a thorough investigation into potential audio artifacts, specifically 'popping' sounds, at the boundaries between generated speech chunks. This is a crucial aspect for real-time applications and requires more detailed analysis.

- Although the authors repeatedly claimed in the paper that their method could "retain the original model’s language capabilities with minimal degradation," they provided no evaluation to substantiate this claim. The absence of a direct comparison of the LLM's performance on standard benchmarks before and after the integration of speech modalities is a significant oversight.

### Questions
- Is there a risk of audio artifacts, such as "popping", at the boundaries when using the vocoder to generate speech chunks? If so, how does the model mitigate these issues?

- Could you provide more detailed comparisons between LLaMA-Omni and other speech-interactive LLMs to evaluate whether introducing speech as an input/output modality affects the model’s reasoning and language comprehension abilities? Specifically, does enabling speech interaction in a text-based LLM reduce its core language understanding and intelligence? Personally, I evaluated another GPT-4o-like model, mini-Omni, and found that their method to introduce the speech modality significantly reduced the language model's core intelligence. Although the authors repeatedly claimed in the paper that their method could "retain the original model’s language capabilities with minimal degradation," they provided no evaluation to substantiate this claim.

### Soundness
4

### Presentation
4

### Contribution
3
