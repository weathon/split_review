# LAURAGPT: LISTEN, ATTEND, UNDERSTAND, AND REGENERATE AUDIO WITH GPT

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Generative Pre-trained Transformer~(GPT) models have achieved remarkable performance on various natural language processing tasks, and have shown great potential as backbones for audio-and-text large language models (LLMs). Previous mainstream audio-and-text LLMs use discrete audio tokens to represent both input and output audio; however, they suffer from performance degradation on tasks such as automatic speech recognition, speech-to-text translation, and speech enhancement over models using continuous speech features. In this paper, we propose \textbf{LauraGPT}, a novel unified audio-and-text GPT-based LLM for audio recognition, understanding, and generation. LauraGPT is a versatile LLM that can process both audio and text inputs and generate outputs in either modalities. We propose a novel data representation that combines continuous and discrete features for audio: LauraGPT encodes input audio into continuous representations using an audio encoder and generates output audio from discrete codec codes. We propose a one-step codec vocoder to overcome the prediction challenge caused by the multimodal distribution of codec tokens. We fine-tune LauraGPT using supervised multi-task learning. Extensive experiments show that LauraGPT consistently achieves comparable to superior performance compared to strong baselines on a wide range of audio tasks related to content, semantics, paralinguistics, and audio-signal analysis, such as automatic speech recognition, speech-to-text translation, text-to-speech synthesis, speech enhancement, automated audio captioning, speech emotion recognition, and spoken language understanding.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper describes an integrated Audio-Text LLM that uses continuous features to represent input audio and discrete tokens to generate output audio. This allows it to be used for audio generation and audio->audio tasks like text-to-speech synthesis and speech enhancement, in contrast to most (but not all) existing Audio-Text systems. The system is evaluated on many standard tasks in the various modalities and in comparison to reasonable existing single-task systems provides significantly improved performance on spoken language understanding accuracy, speech to text translations from english to Chinese, equivalent performance on ASR, spoken language understanding f1, speech emotion recognition, speech to text translation from Chinese to english, and worse performance on automatic audio captioning, speech enhancement, and text-to-speech. Overall, the system seems competitive in these various tasks compared to these baselines.

### Strengths
* The problem of general audio-text understanding, modeling, and generation is an important one, as is multi-modality in LLMs in general.
* Ambitious combination of many tasks into a single model
* Experiments seem well conducted, reasonable selection of tasks and benchmarks

### Weaknesses
In terms of novelty, this is a popular area of research at the moment, with SeamlessM4T being released in August, a few weeks before the submission deadline in addition to the many relevant recent references cited here. If the new capability enabled by the proposed approach is audio output, then one of the most relevant systems appears to be AudioGPT, which also supports speech enhancement. The reason that it is not compared or included in Table 1, which shows capabilities of different existing models, is that it integrates an "expert audio model with LLM", which I don't fully understand the meaning of. An expanded explanation of this would be very useful in understanding this key point.

Also regarding Table 1, it should be clarified that it is showing just what the model has been trained/evaluated on, not what it is necessarily capable of. For example, any system that can perform speech to text translation should also be able to perform automatic audio captioning. Similar arguments hold for speech emotion recognition and spoken language understanding.

In terms of the significance of the results, it is interesting that these tasks can all be solved by a single model, but it's not clear that doing so gives the model advantages over separate models. The performance seems mostly on par. It is also not clear whether the other multimodal systems described in Table 1 (especially SpeechT5) would do better than the proposed system on these tasks as the comparisons are only against single-task systems trained on much less data (the subset of the data that the proposed system was trained on for each particular task).

In terms of clarity, two different taxonomies of related models are introduced in sections 1 and 2, these could be combined into a single one to make space for more explanation of the data that the model was trained on from the appendix. In particular, it is not clear in the body of the paper whether the model is trained once on all of the data or separately for different tasks or how that is navigated and how much data it is overall.

Some claims about the proposed model's superiority are not well supported by the results. Specifically the claim of being best on SLU, when it is really just SLU accuracy, but not f1 scores. This is also the case for SER in that the proposed model is better on unweighted accuracy, but not weighted f1 or accuracy.

Minor comments:
* A definition of the "endless looping problem" and "loop ratio" would be helpful in the appendix
* "These results indicate that LauraGPT tends to generate captions that closely match one of the references..." can you explain how you reach this conclusion?
* Please define exactly what "clean_codec_syn" is in table 7
* In the appendix, prosody includes both tone and speed, so no need to list them separately
* In the appendix, I believe "dereverberation" is meant instead of "echo cancellation" which involves an echo back to the far end of a telephone call, typically.
* In the appendix, "For the SER task, we collect corpora including..." are there other corpora used? If so, please list them. If not, reword.

### Questions
Can you clarify the difference between the proposed system and AudioGPT?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors propose a unified GPT model(LauraGPT) for audio recognition, understanding, and generation. They encode input audio into continuous representation and decode output audio from discrete codec codes and fine-tune a language model. They evaluate the LauraGPT on various audio processing benchmarks like ASR, S2TT, TTS and so on. The experimental results conducted on tasks show the effectiveness of the LauraGPT and the flexible design of the model.

### Strengths
1.The proposed model supporting largest number of and most diverse audio processing tasks compared with other structure, which is interesting and reasonable. The authors also give detailed analysis and descriptions about these tasks and results with baselines.

2.The article provides a clear categorization of tasks and the model provides an extensible framework to support complex tasks with its modular and flexible design. It can break a task into sub-tasks among the basic types and perform well. This makes the model well extensible.

3.The model combines continuous and discrete features for audio signals. It utilizes the continuous features and analyzes the impact of discrete versus continuous representations in ASR, S2TT, and SE tasks.

### Weaknesses
1.The task-related token included in the matrices is not explained enough, how is it utilized and how is it embedded to give the information of the types of the tasks. It lacks some details about it in the description.

2.In evaluation part, there’s a lack of adequate analysis of the relationship between the poor performance in some tasks and model size. Specifically, it's unclear if the observed performance limitations on certain tasks are due to inherent model architecture constraints or simply insufficient model capacity, which should be further investigated with different model sizes.

3.In Part 3, there is a lack of detailed visualizations to show the internal framework of the model, as well as the details of the training and inference process. For instance, a diagram illustrating the flow of information through the model, including the audio encoder, the embedding layers, and the LLM, would be beneficial. Furthermore, the specific training procedure, including loss functions and optimization techniques, should be visualized.

### Questions
1.In the article, the model is able to perform in more task domains, compared to the most related multi-task unified audio-text models, but in the comparison, why is there no comparison with these multi-task models for the various metrics of these tasks?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- LauraGPT is a single GPT-like LLM that operates on a combination of discrete and continuous features for audio signals and text, and is fine-tuned to perform a wide range of speech and audio processing tasks.
- A pre-trained text-only language model (Qwen) serves as the backbone for Laura. For audio, LauraGPT uses a combination of discrete tokens obtained from an improved Encodec-based audio codec (where only the first quantizer is used as the tokenizer), as well as a conformer-based encoder which is initialized with weights from a pertained ASR model. The autoregressive model predicts the next token (text or audio) given the input embeddings, task embeddings, and the previously predicted tokens. The output text is obtained from the Qwen tokenizer and the final audio is obtained from a so-called codec vocoder.
- Instead of directly using the decoder of the pre-trained audio codec, LauraGPT uses a codec vocoder wherein a transformer model serves to predicted the sum of all quantizers embedding for ground truth audio given just the first quantizer embedding and additional context. Subsequently, during inference, the predicted audio token embedding can be transformed into the summed token embeddings and passed to the pre-trained codec decoder to generated raw audio.
- The authors evaluate LauraGPT against strong baselines for each of the task it is capable of performing. LauraGPT performs well on most tasks, only failing to beat baselines in the Speech enhancement and TTS task. It also fails to beat Whisper-Large V2 in English, which is understandable given the smaller amount of English data it was pre-trained on.

### Strengths
- The paper demonstrates a strategy to fine-tune existing LLMs trained only for text to perform various audio processing (generation and understanding) tasks. 
- Unlike other related work, this paper shows that utilizing a mix of continuous and discrete representations of audio in the transformer architecture leads to improved performance in the final generation task (as ablated in section 5.2).
- The evaluation is pretty comprehensive and strong baselines have been chosen for most tasks.

### Weaknesses
 - The ablation regarding discrete tokens vs continuous + discrete tokens feels incomplete without also using the VALL-E style token prediction setup. Currently, the token prediction scheme is similar to that used by SPEAR-TTS wherein each quantizer level token is predicted one-by-one before moving on to the next audio-frame’s tokens. It would be beneficial to see how the model performs when predicting all quantizer tokens for a given frame simultaneously, as this is a common approach in other audio generation models.
- Some statements are not clearly backed up by experiments. For example, one of the main contributions listed is the fact that continuous and discrete representations of audio are used in LauraGPT and that this preserves both fidelity and generality of audio data. Firstly, I am not quite sure what it means to preserve generality of audio. Second, while it is shown in the ablation that the Discrete IO model suffers, it is not clear to me how these results show that fidelity and generality is preserved because of the use of combined representations. All I see is that performance on various task is improved by using the combination. Also, one additional benefit the combined representation model sees is the use of the codec vocoder. Perhaps that is the source of the improvements in LauraGPT? The paper does not sufficiently isolate the effect of the combined representation from the effect of the codec vocoder.
- Section 3.4 would be well served with some more detail. The reader would benefit from some repeating information that the GPT model only uses the first quantizer. I found it difficult to understand initially and had to read from the start of section 3 again. It is not immediately clear why only the first quantizer is used and how this relates to the codec vocoder. The explanation of how the codec vocoder is trained and used during inference is also somewhat vague and could benefit from more detail.
- A few figures going into more detail for each of the components in figure 1 would also greatly improve the readability of the the method section. Currently, figure 1 is very high-level and does not offer the reader too much. For instance, a more detailed diagram of the audio encoder, showing the conformer layers and how the continuous features are processed, would be helpful. Similarly, a more detailed view of the codec vocoder, showing how the first quantizer embedding is used to predict the summed token embeddings, would be beneficial.

### Questions
- Do I understand correctly that the model uses continuous features from only the input audio, and uses audio token embeddings for previous audio tokens, meaning that the generated audio is always seen as tokens within the GPT model? It would benefit the reader if this is stated in the text explicitly as well.

### Soundness
3 good

### Presentation
2 fair

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
In general, the paper is an experiment oriented work which demonstrates the GPT-style structure can do various speech tasks. Specifically, this paper introduces LauraGPT, a versatile GPT model designed for audio tasks, including: automatic speech recognition, speech-to-text translation, text-to-speech synthesis, machine translation, speech enhancement, automated audio captioning, speech emotion recognition, and spoken language understanding. To enable these capabilities, the model combines continuous and discrete audio features, utilizing an audio encoder for input and a discrete codec for output. The model is then fine-tuned through supervised multitask learning on a range of audio-to-text, text-to-audio, audio-to-audio, and text-to-text tasks. Extensive experiments demonstrate that LauraGPT achieves competitive or superior performance compared to existing state-of-the-art models across various audio processing benchmarks.

### Strengths
The paper presents a thorough set of experiments, showcasing the capabilities of LauraGPT in handling both audio and text inputs and generating outputs across a diverse range of tasks. These tasks encompass content analysis, semantics, paralinguistics, and audio-signal analysis.

As far as my knowledge extends, the paper provides extensive coverage of speech tasks in its evaluation, as indicated by the authors in Table 1.

### Weaknesses
While the paper presents solid research, it falls short in paving the way for future investigations.

1. By the end of 2023, speech researchers generally believe that GPT-style models can handle various speech tasks, even though certain specific tasks may not achieve state-of-the-art performance when compared to baseline models of the same size. Instead of offering insights beyond the extensive experiments conducted, the authors primarily focus on demonstrating the effectiveness of GPT-style models across multiple speech tasks.
I hope the authors will consider demonstrating whether multi-task learning can result in task synergy, where tasks can benefit from each other rather than being treated as separate or even conflicting objectives. For instance, if I have a 1B model that solely focuses on automatic speech recognition (ASR), would it outperform a 1B model capable of performing ASR, text-to-speech (TTS), and speech-to-text (ST) tasks? If the answer is no, then why should we incorporate all these tasks into the same model? It would be valuable for the authors to analyze the relationship between task performance in the context of multi-task learning, as evidenced in Table 2, where LauraGPT lags significantly behind the state-of-the-art LibriSpeech despite its 2B model size.

2. In the realm of fundamental speech models, are there any emerging points of interest similar to those in the field of natural language processing (NLP)? Exploring this aspect could be a valuable research direction. If speech researchers are unable to answer this question, I believe that running multi-task learning experiments alone may not be sufficient to construct the next generation of speech models.

### Questions
Apart from Speech translation, could you list more complex tasks that should use foundamental model to solve rather than do them one by one?

If the performance is worse than train an ASR model alone, what is the value of the multi-task learning model?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
