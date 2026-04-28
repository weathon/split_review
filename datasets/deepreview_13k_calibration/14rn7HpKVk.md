# SALMONN: Towards Generic Hearing Abilities for Large Language Models

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Hearing is arguably an essential ability of artificial intelligence (AI) agents in the physical world, which refers to the perception and understanding of general auditory information consisting of at least three types of sounds: speech, audio events, and music. In this paper, we propose SALMONN, a speech audio language music open neural network, built by integrating a pre-trained text-based large language model (LLM) with speech and audio encoders into a single multimodal model. SALMONN enables the LLM to directly process and understand general audio inputs and achieve competitive performances on a number of speech and audio tasks used in training, such as 
automatic speech recognition and translation, auditory-information-based question answering, emotion recognition, speaker verification, and music and audio captioning \textit{etc.} SALMONN also has a diverse set of emergent abilities unseen in the training, which includes but is not limited to speech translation to untrained languages, speech-based slot filling, spoken-query-based question answering, audio-based storytelling, 
and speech audio co-reasoning \textit{etc}. The presence of cross-modal emergent abilities is studied, and a novel few-shot activation tuning approach is proposed to activate such abilities. To our knowledge, SALMONN is the first model of its type and can be regarded as a step towards AI with generic hearing abilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed SALMONN, which is a single unified multimodal model to integrate speech and audio encoders with a pre-trained text LLM. The paper shows that SALMONN can achieve competitive performance on a variety of speech tasks used in training, including ASR, ST, emotion recognition, audio QA, speaker verification, audio and music captioning etc. The paper also studies the capabilities of SALMONN on zero-shot capabilities such as ST on untrained languages, SLU, SQA, audio-based story telling, speech-audio co-reasoning etc. The paper also explores a new few-shot activation tuning approach.

### Strengths
(1)	Value to the community: The proposed SALMONN model unifies modeling a wide variety of speech, audio, and music perception and understanding tasks into a single framework, which is a useful step towards the research for AGI. 

(2)	The innovation of the paper is mostly in choosing and piecing together existing approaches for this unified framework, using and evaluating a diverse set of speech/audio/music tasks for pre-training/instruction-finetuning, studying emergent capabilities, analyzing task-overfitting issue and exploring cheap activation tuning to alleviate catastrophic forgetting to training tasks.  SALMONN reasonably adopts several existing approaches. For speech and non-speech audio encoding, SALMONN integrates a speech encoder from Whisper and a BEATS audio encoder. SALMONN uses a Q-Former to convert encoder output to audio tokens for the text LLM (Vicuna in this work). LoRA is applied to align the augmented input space with output space to improve cross-modal alignment for the text LLM.  Following other works, SALMONN used a diverse set of speech, audio, and music tasks in pre-training and instruction finetuning of Q-Former and LoRA.  Notably,  this paper analyzed the task overfitting issue and provided insights for activation tuning to alleviate catastrophic forgetting from instruction tuning. The paper also studies the capabilities of SALMONN on handling cross-modal emergent tasks.  

(3)	Overall, the paper is clearly written.

(4)	Empirical evaluations are comprehensive. The three levels are helpful organizations, as  speech tasks used in instruction tuning, unseen speech-based NLP tasks which can effectively evaluate speech-text cross-modal alignments, and the proposed new audio-based story telling and speech audio co-reasoning tasks which require understanding mixture of speech and non-speech auditory information.

### Weaknesses
(1) In empirical validations, the choice of reference values (as shown in Table 2) needs to be clarified, and more importantly, these choices need to be justified. It is not clear which model size is used for Whisper when it is used as reference values. For example, what is the performance of different sizes of Whisper on the ASR task? Also, the choice of simply cascading Whisper + Vicuna needs to be justified as the reference value for many tasks, since it may not be as competitive as other E2E models (e.g., recent speech LLMs), including SOTA. Without clear knowledge how strong these reference values are, it is not easy to judge how strong SALMONN performs as shown in Table 3. More specifically, while the authors claim that the reference values for tasks like AAC, PR, ER, MC, and OSR are SOTA, it would be beneficial to see a direct comparison with other established models in these domains. For instance, for speech emotion recognition, how does SALMONN compare against models like vesper-12? For automatic audio captioning, how does it compare against an ensemble model like the one proposed by Koizumi et al.? These comparisons are crucial to understand the true performance gains offered by SALMONN.

(2) Some key implementation details are missing. The training data as shown in Table 1 are highly unevenly distributed. It is not clear methods such as data upsampling are used, or batches are designed for multi-task instruction fine-tuning. Specifically, how are the batches constructed to ensure that tasks with less data, such as ER and MC, are adequately represented during training? Are there any specific strategies used to mitigate potential overfitting or underfitting for tasks with limited data?

(3) The paper focuses on general hearing capabilities of speech/audio/music. It would be useful to discuss how to extend the model to speech/audio/music generation tasks. This is particularly relevant given the recent advancements in generative models and the potential synergies between perception and generation tasks.

### Questions
Please check the comments and concerns raised under Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents SALMONN, a novel method for equipping LLMs with hearing abilities by leveraging additional adapter modules and LoRA weights to train the LLM on a range of speech, audio, and music understanding tasks.

### Strengths
- The overall architecture design is quite clever, and its use of generally open source models and datasets is very important to the audio-text field as a whole.
- The amount of time spent towards analyzing and mitigating the models failure modes is quite useful, and the authors provide an incredibly detail analysis of model behavior under different finetuning configurations.

Despite some of the concerns mentioned below (which mostly address overall clarity rather than content), the paper presents an incredibly detailed analysis of a novel architecture and how to adapt LLMs for audio-based reasoning, and thus I recommend acceptance.

### Weaknesses
 - The explanation of the pretraining stage could use a bit more depth. Namely, how is it that the Q-Former and LoRA weights are actually trained during the pretraining stage? What specific loss functions are used, and how are they weighted? Furthermore, what is the exact architecture of the Q-Former, and how does it process the audio features? Is it a transformer-based architecture, or something else?
- I think in general, the sections on task-overfitting and activation tuning are relatively hard to parse reading-wise and could be simplified. Unless I am misunderstanding something, task-overfitting is simply the idea that SALMONN overfits to the overrepresented tasks in the dataset, which I think the math in section 3.2 overcomplicates. The explanation of how activation tuning mitigates this is also not entirely clear. What exactly is being tuned? Is it a scalar value applied to the activations, or is it a more complex transformation? The connection between the activation tuning and the task over-fitting could be made more explicit.
- It is hard to tell in the ablations (5.2-5.4) what is being held fixed and what training configurations are being used. Namely, in section 5.2 are the results on the reduced LoRA scaling factor done with or without activation tuning? It's also not clear if the same datasets are used across all ablations, and if the training hyperparameters are consistent. This makes it difficult to isolate the impact of each ablation. In general, the ablations need more detail on the experimental setup.
- The authors claim that the Level 3 tasks are harder directly, but given the myriad of evaluation metrics for each task it's hard to tell *why* these tasks are necessarily in their own class. Is there some way to show how these tasks are by nature an entirely more difficulty class of problems? Especially as SAC seems to be evaluated by ChatGPT outputs, it is hard to tell much about the actual performance of the model. The use of ChatGPT for evaluation is also concerning, as it introduces an external LLM into the evaluation pipeline, which may not be consistent or reliable.

### Questions
- What is "monotonic alignment" as mentioned in the Q-Former section?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose to fuse both speech encoder (whisper) and general audio encoder (beats) as inputs, connect with LLM via a Q-Former and fine-tune with LoRA. Besides pre-training and instruction tuning stages, the authors also propose an activation tuning stage, which is to prevent from overfitting to short captions and is able to generate long and diverse stories. For some of the instruction tuning dataset, the authors leverage LLM for curation.

### Strengths
- The combination of speech and audio encoders are interesting ideas and the results of speech audio co-reasoning provide new capabilities for audio understanding.

### Weaknesses
 - According to the results in table 3, it seems that the proposed method only works significantly better on level 3 tasks of Story and SAC, which the evaluation metrics are specifically designed and there is no other reference value from other models provided. It would be better to provide more information on the 2 tasks and providing other baseline performance on these two tasks.
- For the Story task, it is worth including accuracy FR along with diversity FR. This can provide a more holistic understanding of the tradeoffs.
- For some tasks in level 1 and 2, the performance of proposed method is significant worse, e.g. PR, OSR. and SQQA for level 2. It might worth providing some in depth discussion and analysis. For example, can it be that adding both whisper and beats features introduce more confusion to the model? How are the Q-former attending to the concatenated features to make predictions?

### Questions
- The process of activation tuning stage is not clear described, according to the last paragraph of 4.2, if the data is generated by SALMONN model, what do they look like? It would be helpful to provide an example. Also for teacher-forcing training, is it just a standard cross-entropy loss on generated text? How do you control the diversity and length of generated examples?
- How are the instruction prompted for evaluation tasks? How do you instruct the model for evaluating these tasks?
- Is ChatGPT also leveraged to generate text data for some evaluation tasks, especially for SAC and Story. If so, how are they leveraged to curate answers?
- How are the prompted QA for training generated by ChatGPT verified?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
