# Acoustic Prompt Tuning: Empowering Large Language Models with Audition Capabilities

- Decision: Reject
- Avg Score: 4.60
- Scores: 1, 6, 8, 3, 5

## Abstract
The auditory system plays a substantial role in shaping the overall human perceptual experience. While prevailing large language models (LLMs) and visual language models (VLMs) have shown their promise in solving a wide variety of vision and language understanding tasks, only a few of them can be generalised to the audio domain without compromising their domain-specific capacity. In this work, we introduce \textbf{A}coustic \textbf{P}rompt \textbf{T}urning (APT), a new adapter extending LLMs and VLMs to the audio domain by soft prompting only. Specifically, APT applies an instruction-aware audio aligner to generate soft prompts, conditioned on both input text and sounds, as language model inputs. To mitigate the data scarcity in the audio domain, a multi-task learning strategy is proposed by formulating diverse audio tasks in a sequence-to-sequence manner. Moreover, we improve the framework of audio language model by using interleaved audio-text embeddings as the input sequence. This improved framework imposes zero constraints on the input format and thus is capable of tackling more understanding tasks, such as few-shot audio classification and audio reasoning. To further evaluate the reasoning ability of audio networks, we propose natural language audio reasoning (NLAR), a new task that analyses across two audio clips by comparison and summarization. Experiments show that APT-enhanced LLMs (namely APT-LLMs) achieve competitive results compared to the expert models (i.e., the networks trained on the targeted datasets) across various tasks. We finally demonstrate the APT's ability in extending frozen VLMs to the audio domain without finetuning, achieving promising results in the audio-visual question and answering task.\let\thefootnote\relax\footnotetext{\textsuperscript{*}The work does not relate to H.P.'s position at Amazon.}

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study the work of empowering large language models with audition capabilities. However, the idea and the presentation of this paper is very similar to BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models (https://arxiv.org/pdf/2301.12597.pdf), we can see that the Figure 2 in this paper is very similar to Figure 2 in BLIP-2, the losses and masking strategies and so on are very similar to BLIP-2. To empower large language models with audition capabilities, the authors should propose some new idea. In the experiments, the authors don't compare their work with some well-known approaches such as SpeechGPT and so on.

### Strengths
1. The problem is interesting.

### Weaknesses
1. The Figure 2 in this paper is very similar to Figure 2 in BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models (https://arxiv.org/pdf/2301.12597.pdf), just replace the word image to audio. Thus, the novelty of this paper is very limited compared with BLIP-2. The Figure 1 in this paper is similar to Figure 3 in BLIP-2. The authors use the exactly three loss in BLIP-2, matching loss, contrastive loss and gounded text generation loss, with the exactly three mask strategies, and the authors use the learnable query. 

2. Model Capability: Unlike methods such as SpeechGPT, the approach presented in this article limits the use of speech modality to input only, preventing the synthesis of speech output. This results in a model lacking genuine speech interaction capability.

3. Experimental Comparisons and Results: The performance of the method falls below the expected standard, and there is a notable absence of performance comparison with established works such as SpeechGPT.

### Questions
1. The audio modality is different from image modality. Why the authors use the exactly thress losses and three mask strategies from Figure 3 in BLIP-2 ?
2. Apart from the novelty, in the experiments, the authors don't compare their model with some well-known works, such as SpeechGPT and so on.
3. For the audio modality, speech interaction is important, why not the authors focus on this part, which is different from image modality.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces Acoustic Prompt Turning (APT), an acoustic adapter that extends large language models (LLMs) and visual language models (VLMs) to the audio domain. Existing models have limited applicability to audio tasks. 

APT uses a multi-task learning framework and an instruction-aware aligner to generate fixed acoustic embeddings from audio feature maps. Various audio-related tasks are formulated in a sequence-to-sequence manner, allowing APT to be trained without constraints on input sequences. Experimental results show that LLMs coupled with APT achieve competitive performance compared to expert models across different tasks. APT is also evaluated on a novel audio reasoning task and shown to extend frozen VLMs to the audio domain, even without fine-tuning on audio-visual datasets.

### Strengths
1. This paper pioneers the exploration of audio-text language modeling, particularly in addressing the format constraint that previous work faced. In the past, there have been a few attempts at audio-text foundation modeling; however, they were limited to the input format [audio, Q, A], excluding support for other practical tasks. As a result, these models were unable to exhibit the same level of intelligence as popular language models like GPT-4. This paper overcomes this limitation by considering audio as a prompt in language modeling, enabling it to perform various tasks.

2. Additionally, the paper introduces a novel task called audio reasoning and provides a dataset that will prove invaluable for future research. This direction is highly significant as existing datasets often prove too simplistic for large models, failing to capture the complexity and intelligence required in real-world audio modeling scenarios. By introducing a more challenging audio reasoning task and accompanying dataset, the paper paves the way for the development of smarter and more sophisticated audio models that better align with real-world demands.

### Weaknesses
1. When examining the experimental results, it is apparent that the proposed model does not perform as strongly as the specific model on certain tasks. For instance, the baseline for AudioSet classification is around 47, whereas this paper only achieves 14.7. If a foundation model lags behind a specific model, its technical significance is limited. Furthermore, the model does not demonstrate sufficient strength in the audio caption task, which should ideally be robust considering the capabilities of the LLM as a decoder.

The authors should provide evidence to support the advantages of foundation models. If a foundation model is merely capable of performing multiple tasks, it may not be sufficient. It is important for the authors to demonstrate the unique strengths and benefits of the foundation model compared to other approaches. This could include showcasing improved performance, increased efficiency, or enhanced generalization across tasks. Providing such evidence will help establish the significance and value of the foundation model in the audio domain.

2.Upon examining the approach outlined in the paper, it becomes evident that it is similar to  existing speech-language models. Initially, when reading the title of the paper, I anticipated that the method would differ significantly from previous models such as AudioPaLM and SpeechLM. However, upon closer inspection, it appears that the method aligns closely with these established models, but changing the input from speech to audio. Given the current era of large language models (LLMs), my expectations for groundbreaking innovations were not high.

### Questions
1. How to gurantee the audio reasoning dataset qualilty? It is created by ChatGPT and may need some human participants for quality check.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces Acoustic Prompt Turning (APT), an acoustic adapter that extends large language models (LLMs) and visual language models (VLMs) to the audio domain. APT uses an instruction-aware aligner to acquire acoustic embeddings from audio feature maps, allowing it to handle diverse audio-related tasks in a sequence-to-sequence manner. The paper demonstrates the effectiveness of APT-LLMs through various tasks and introduces a novel audio reasoning task. It also shows that APT can extend frozen VLMs to the audio domain, yielding promising results in the audio-visual understanding task.

### Strengths
- The concept of APT is innovative and presents a new direction for extending LLMs and VLMs to the audio domain without compromising their domain-specific capacity. This also provides evidence that encoding sound clips as word tokens is an efficient approach to adapt LLM/VLM to the audio domain.
- Introducing the natural language audio reasoning task is a creative way to evaluate model's ability to understand, compare, and summarise two audio clips.
- The paper does a good job comparing its work with existing models, providing a clear context for the novelty and utility of APT.
- There are significant performance improvements across audio-visual baselines, highlighting the effectiveness of APT in the audio-visual domain. The performance on most of the open-ended tasks was good.

### Weaknesses
 - Performance on Certain Tasks: Despite the novelty of the idea, the performance of APT-LLMs on the close-ended datasets - ESC50 (few shot classification) and AudioSet (captioning) tasks is not competitive compared to state-of-the-art, task-specific models. This indicates a need for improvement in these areas. Specifically, the paper lacks a detailed analysis of why the model struggles with these tasks, such as whether the issue lies in the acoustic feature extraction, the alignment process, or the text generation. The paper should also explore the impact of the limited training data for these tasks on the overall performance.
- Handling of Errors: It is unclear how the model handles potential discrepancies or errors in the labeled examples used for in-context learning. This raises questions about the robustness of the model in real-world scenarios where such issues are common. The paper does not discuss how the model would react to noisy labels or if there is a mechanism to detect and correct such errors. Furthermore, the paper does not explore the model's sensitivity to variations in audio quality or the presence of background noise, which are common in real-world audio data.

### Questions
- How can APT's performance on tasks like ESC50 and AudioSet be improved to be more competitive with task-specific models?
- How does the instruction-aware aligner in APT handle different audio signals, especially those with complex characteristics?
- How can the model be improved to handle discrepancies or errors in the labeled examples used for in-context learning?
- How does APT perform for more specific types of audio (e.g., music, notes...)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper describes Audio Prompt Tuning (APT), a new model architecture that interleaves representations of audio with embeddings of text tokens in order to enable joint learning of text-generation tasks that are conditioned on one or more audio clips and related text prompts. When coupled with a pretrained LLM, APT forms the APT-LLM model architecture, capable of performing a variety of audio-text tasks including audio tagging, audio captioning, and few-shot audio classification. In addition, the authors created a new type of tasks called natural-language audio reasoning (NLAR), in which the model is tasked with answering natural-language questions concerning the relations between two audio clips (but see my concerns below).

### Strengths
S1. Proposing a novel way of representing an arbitrary number of audio clips and their associated textual information that interleaves representations of the audio clips with text token embeddings. This significantly enhances the versatility of the model, giving it abilities to perform a variety of audio-text bimodal tasks such as tagging, captioning, classification, as well as tasks that involve more than one audio clip such as NLAR.
S2. A multi-task training recipe for the APT model that encompasses different cross- and self-attention mechanisms between the audio input and associated text input.

### Weaknesses
W1. The levels of accuracy achieved by APT-LLM on the audio tagging and audio captioning are unfortunately slightly disappointing (Table 1. Section 4.2). They fall below the accuracy levels of domain-expert models, by a noticeable margin in the case of audio tagging. The authors argue that this has to do with the open-ended nature of APT-LLM's output, which puts APT-LLM at a disadvantage compared to the closed-ended nature of the previous models audio tagging models. However, in the context of visual benchmarks such as ImageNet, open-ended text-visual models such as CLIP have previously outperformed domain expert models such as various types of CNNs. A similar under-performance can be seen in the few-shot audio classification task (Table 2), especially for the 12-way case. The authors try to attribute this poor performance to the length of the input, but they did not explain why the model couldn't be configured and trained with a sufficiently long input context window in order to accommodate this task and thereby address this limitation.
W2. The section on integration of BLIP-2 and APT-LLM (Section 4.4) is not easy to follow for readers not familiar with the audio-visual tasks. Not enough background information is provided about either the BLIP-2 model architecture or the audio-visual learning task that the author performed evaluation on. This unfortunately makes this part of the claimed contribution less convincing.
W3. The natural-language audio reasoning (NLAR) dataset is constructed from a subset of the Clotho-AQA dataset by utilizing OpenAI's ChatGPT-turbo API. The NLAR dataset suffers from two issues: 1) the authors did not explain the criteria by which the subset was selected from Clotho-AQA, and 2) the authors did not describe how the quality of the examples generated by ChatGPT-turbo was controlled. Presumably, some sort of manual inspection was required to ensure that the LLM-generated test examples are correct.

### Questions
Q1. The diagram in Figure 1 seems to miss a part between the input text and the audio aligner for tokenizing the input text and looking up the embeddings for the input text for the aligner's use. This figure needs clarification.
Q2. How does the frozen LLM receive the audio-text juxtaposed embeddings? Its built-in embedding lookup layer should have been removed so that the mixed audio-text embeddings can be passed directly as the input to the LLM. This begs the question of why the authors decided to freeze the LLM. It seems that by freezing the LLM, the burden and opportunities for learning are limited to the audio encoder and the audio aligner. Is it possible allowing the weights of the LLM to change and adapt during training would lead to better learning outcomes by the entire APT-LLM model? The authors didn't describe any hyperparameter tuning processes.
Q3. Equation (1) and Equation (4) seem to have inconsistency with Figure 1. M_{\theta} should take an additional input (the text) according to the diagram in Figure 1.
Q4. How many examples does the NLAR dataset contain?
Q5. Figure 3 in the appendix lacks legends. In addition, the y-axis on the right-hand side is unlabeled. As a result, it is unclear what are plotted by the blue and orange curves, which makes this figure hard to read.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Acoustic prompt tuning (APT) is proposed in this paper, which integrates an Audio-MAE encoder, a Q-Former aligner, and a Vicuna LLM to implement a multimodal LLM that can hear and understand audio events. Three auxiliary loss functions are used to improve the training of the Q-Former aligner, including audio-text matching (ATM), audio-grounded text generation (AGTG) and audio-text contrastive (ATC). APT-LLM is evaluated on audio tagging, audio captioning, few-shot audio classification, audio-language reasoning and zero-shot audio-visual question-answering tasks.

### Strengths
1. The paper investigates the integration of LLM with an audio encoder to empower it with auditory abilities, which is currently an understudied research problem. 

2. The method is evaluated on a number of audio-event-related tasks evaluating the abilities of audio-event understanding and reasoning. 

3. The presentation of the paper is very clear, including a precise limitation section that elaborates on the scope of the approach.

4. In-context learning for audio-event classification is investigated.

### Weaknesses
1. The authors claimed "Diverse audio-related tasks are formulated in a sequence-to-sequence manner without imposing any constraints on input sequences", which is not true since the input sequence could not be speech or music, as claimed in the limitation section. There might also be a maximum input sequence length imposed by the use of the Audio-MAE encoder, and the Q-Former aligner. Specifically, the Audio-MAE encoder processes fixed-length audio segments, and while the authors may concatenate the resulting tokens, this introduces a hard limit on the total input length that the model can effectively process, which is not clearly addressed in the paper.

2. The authors claimed that one of the key contributions of the paper is: "this is the first attempt to unify fully-supervised learning with in-context learning." It is not clear to me what this means precisely. The authors need to make the motivation and benefits of combining multitask training with in-context learning clear. The paper does not provide a clear explanation of how the multitask training objectives directly facilitate in-context learning, or why this combination is novel or advantageous compared to other approaches that utilize either multitask learning or in-context learning separately.

3. The performance of the proposed approach is not satisfying based on Table 2, in particular on audio tagging on the AudioSet dataset. The reported performance is significantly lower than existing state-of-the-art methods, raising concerns about the effectiveness of the proposed approach for this task. The paper lacks a detailed analysis of why the model struggles on audio tagging, and what specific limitations of the architecture or training process contribute to this performance gap.

4. The model is not tuned to follow instructions and can only perform a small of tasks, which makes the use of LLM less reasonable. The paper does not demonstrate the model's ability to generalize to a wide range of audio-related tasks, which is a key advantage of using LLMs. The limited task scope raises questions about the necessity of using a large language model, as a smaller, task-specific model might achieve comparable or better performance.

5. It sounds less sensible to me to use a standard Q-Former to convert audio input sequences into a fixed number of 32 tokens. Generating a fixed number of tokens is a good choice for images with fixed sizes, but not so much for audio input sequences due to their variable input lengths. This fixed token length may lead to a loss of information, especially for longer audio sequences, and the paper does not justify why a fixed number of tokens is appropriate for varying-length audio inputs.

6. It is not clear what are the benefits of having the ATM, ATC, and AGTG multitask training on the Q-Former aligner. The paper does not provide a clear ablation study or analysis of how each of these auxiliary losses contributes to the overall performance of the model. Without this analysis, it is difficult to assess the necessity and effectiveness of each loss function.

### Questions
1. What's the size of the Vicuna LLMs used in the paper? 

2. What are the strengths of APT-LLM compared to other recent methods, such as LTU? It seems APT-LLM has worse performances based on Table 1.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
