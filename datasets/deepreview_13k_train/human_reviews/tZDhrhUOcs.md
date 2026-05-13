# SSR: Alignment-Aware Modality Connector for Speech Language Models

- Decision: Reject
- Scores: 8, 3, 5, 6

## Abstract
Fusing speech into pre-trained language model (SpeechLM) usually suffers from inefficient encoding of long-form speech and catastrophic forgetting of pre-trained text modality. We propose \method (Segmented Speech Representation Connector) for better modality fusion. Leveraging speech-text alignments, our approach segments and compresses speech features to match the granularity of text embeddings. Additionally, we introduce a two-stage training pipeline that includes the distillation and fine-tuning phases to mitigate catastrophic forgetting. \method outperforms existing mechanism for speech-text modality fusion, consistently achieving better speech understanding (\eg $+10$ accuracy on StoryCloze and $+20$ on Speech-MMLU) while preserving pre-trained text ability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new architecture with the corresponding loss design to connect speech embeddings to LLM. Thorough experiments are conducted to demonstrate the values of the proposed method.

### Strengths
The proposed method has some connections with the previous methods in speech downsampling and model distillation but is novel enough. The evaluation is very thorough.

### Weaknesses
Although the paper acknowledges the three categories of connector designs in Figure 1, it does not compare enough to Figure 1(a). Compared with the proposed 2-stage method, a single-stage or 2-stage baseline with a much simpler 1(a) design can motivate the more complex design in this paper.

Some experiment comparisons and explanations can be improved (see questions).



### Questions
1. need to explain why unitY2 based method is much better than others
2. "Even our weakest system (CHAR-CTC (Unit-based)) can outperform SPIRITLM ’s 10-shot result." the aligner in the proposed method is trained with paired ASR speech-text data, which is unfair to compare with SPIRITLM. 
3. missing description of speech-MMLU

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper tackles the issue of catastrophic forgetting in the Language Model (LM) during speech fusion. The authors introduce the SSR-Connector method to enhance modality fusion. This approach utilizes a speech-text aligner and a decoder-only compressor to produce speech representations that align with the granularity of text embeddings.

### Strengths
The proposed method outperforms existing speech fusion mechanisms in terms of speech understanding.

### Weaknesses
The cost-performance ratio of the proposed method is lower when compared to a cascaded ASR+LLM system.
Please refer to the questions section regarding my queries.

### Questions
At the very beginning, it is mentioned that integrating speech often results in catastrophic forgetting of the primary pre-training. Have you quantified the severity of this issue? During the second stage of training where you fine-tune the Large Language Model (LLM), is there a risk of forgetting within the LLM itself? Specifically, I am referring to the LLM's performance (across various NLP tasks) before and after incorporating the speech modality.

Could you provide the specific figure for the original LaLLM3 as listed in Table 6?

Could you provide further explanation for the statement "lack the ability to support text or speech generation unless further instruction-finetuned" in the introduction section?

Given the option to use a decoder-only compressor and considering the overall model complexity, why not opt for a cascade system like Whisper+LLM? My assumption is that post the entire training process, the adapted representation z (as shown in Figure 3, right-hand side) will closely resemble the input embedding of the corresponding text (or sub-word units). This scenario might make the entire SSR-Connector resemble an Automatic Speech Recognition (ASR) system. In that case, why not simply use an ASR with text (or sub-word units) output directly?

Does the Speech Signal Representation (SSR) convey any audio/voice information beyond text? If so, have you conducted an analysis on this aspect? This is crucial as the community is progressing towards general audio Large Language Models as opposed to solely speech-based models. If not, similar to the previous question, what is the rationale behind incorporating an ASR system?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents SSR-Connector, an innovative approach to integrating speech data into pre-trained LLMs by aligning and compressing speech representations to match text embeddings, enhancing speech-text modality fusion. This technique tackles two main challenges: inefficient processing of long speech sequences and the risk of catastrophic forgetting of text-based capabilities. SSR-Connector employs a two-stage training process: an initial distillation phase aligns speech representations with text embeddings, followed by fine-tuning to improve cross-modal understanding. The approach incorporates alignment-aware segmentation of speech features, optimized to work with text-compatible granularity, and achieves some gains in some speech understanding benchmarks, surpassing prior frameworks such as SpiritLM and VoxtLM.

### Strengths
1. The paper is well-structured and systematically describes each component of the SSR-Connector. Additionally, it clearly explains the methodology used to prevent catastrophic forgetting and offers comparisons with prior models.
2. The SSR-Connector introduces a novel "alignment-aware" approach to speech-text modality fusion.
3. The paper provides a comprehensive analysis of the proposed SSR-Connector across a variety of benchmarks, including StoryCloze, sWUGGY, and Speech-MMLU.

### Weaknesses
1. One significant aspect of SpeechLMs is their ability to capture information in speech beyond just the content. This has been analyzed in many related studies; for instance, in SALMONN [1] and Qwen2-Audio [2], paralinguistic information, such as emotion, is treated as an important evaluation aspect, and SpiritLM also examines capabilities related to understanding paralinguistic information. In addition, as the authors mention in the introduction, cascade systems are unable to learn paralinguistic information in speech, which is an advantage of end-to-end SpeechLMs. However, this paper lacks an analysis of the proposed model’s understanding of paralinguistic information and focuses solely on performance from a content comprehension perspective. If the model lacks the ability to understand paralinguistic information, then even if it addresses the issues of long speech sequences and catastrophic forgetting, it still wouldn't make for an ideal SpeechLM.

2. From the perspective of model methodology, it is challenging for the approach to capture paralinguistic information from speech. The methodology focuses on understanding speech content while overlooking other information within the speech. For instance, in stage 1, the target is text embedding, and achieving the best result would mean that the model could directly predict text embedding from speech but ignore other information. In stage 2, the SSR-Connector is fixed, and only the LLM is trained, so the LLM is also unable to learn information beyond content. Therefore, the entire training process essentially resembles a speech recognition model’s functionality by learning to extract textual information from speech. This limits the novelty of the paper, as the method does not introduce a more comprehensive SpeechLM capable of learning beyond content and instead functions more like an end-to-end model which integrates a speech recognition model with an LLM.

3. Another concern might be that the model’s best performance relies on the UNITY2 model for alignment, which itself requires both speech and transcription for alignment results. Given that a transcript is already available, why not use it directly as the LLM’s input instead of processing it through the SSR-Connector? In my view, using a model that doesn’t rely on transcription for alignment would better align with the scenario proposed in the paper.

4. As far as I know, the test sets used in the paper, such as sWUGGY and sBLIMP, are those employed in the Zero Resource Speech Challenge, where one of the key functions of the models is speech continuation. All the baseline models compared in the paper include speech generation capabilities. I would suggest comparing more models that, like the proposed model, take speech as input and output text, such as SALMONN [1], Qwen-Audio [3], and Qwen2-Audio [2].

### Questions
I have outlined my main concerns in the Weaknesses part. Here are the corresponding questions:
1. How does the proposed model account for paralinguistic information (e.g., emotions) in speech, and why has the analysis of this aspect been omitted from the paper, despite its significance in related studies?
2. Given the methodology’s focus on content comprehension, how does the model address the capture of paralinguistic information?
3. Why does the model rely on the UNITY2 alignment method, which uses both speech and transcription, rather than directly using the available transcription as input for the LLM? Would a model that does not depend on transcription for alignment be more aligned with the paper's goals?
4. Could you include more baseline models, such as SALMONN and Qwen2-Audio?

### Soundness
2

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
This paper presents a method to improve speech langauge models by using speech-text alignment. Experiments have been conducted to evaluate the performance of the proposed method.

### Strengths
1. The idea of utilizing the alignement between speech and text sequences to build speech LMs is novel to me.
2. The paper is written clearly and easy to follow.

### Weaknesses
Since the speech-text alignement is considered in the proposed method, it has similarities with the ASR+LLM (cascade) implementation of speech LMs. For an ASR model, its task is to derive the aligned text from given speech. In Table 4, the performance of the cascade system was quite good. So, some discussions on comparing the proposed method with cascade systems should be emphasized.



### Questions
1) In Section 3.1, what is the unit of the transcription sequence y for alignement? characters, phonemes or words?
2) In Eq. (4), why are both similarity loss and MSE loss used? How to determine the weight for combining them?
3) In Section 5, why is the Char-CTC model used for evaulation since it didn't perform as good as UnityY2 in Section 4?
4) In Table 4, LLaMa2 was used for the cascade system while LLaMa3 was used in the proposed method. This seems unfair.

### Soundness
3

### Presentation
3

### Contribution
2
