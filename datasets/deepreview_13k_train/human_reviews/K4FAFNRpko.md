# VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
Vision-language-action models (VLAs) have recently become highly prevalent in robot manipulation due to its end-to-end architecture and impressive performance. However, current VLAs are limited to processing human instructions in textual form, neglecting the more natural speech modality for human interaction. A typical approach of incorporating speech modality into VLA necessitates a separate speech recognition system to transcribe spoken instructions into text. Such a cascading pipeline raises two major concerns for robotic systems. First, the entire model grows in size and complexity, potentially resulting in redundant computations and increased memory consumption. Second, the transcription procedure would lose non-semantic information in the raw speech, such as voiceprint, which is crucial for a robot to successfully understand and complete customized tasks. To this end, we propose VLAS, the fisrt end-to-end policy model that seamlessly integrates speech modality for robot manipulation. We present a three-stage speech instruction tuning strategy leveraging multimodal datasets, including our manually curated SQA and CSI datasets. Furthermore, to facilitate personalized operations, we develop a voice retrieval-augmented generation (RAG) approach to enhance the robot's performance in tasks requiring individual-specific knowledge. Experimental results show that the proposed VLAS, following either textual or speech instructions, can achieve performance comparable to traditional VLAs on the CALVIN benchmark. In addition, we created a benchmark consisting of customization tasks, where our VLAS demonstrates absolute superiority by fully leveraging the auxiliary information in speech.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper recognizes the problems of losing auxiliary semantics and complicating the system in performing transcription on human speech as robot manipulation command. It proposes to include the speech modality into an end-to-end LVA model, resulting in the VLAS model.

The VLAS model directly process textual and speech instructions with vision and proprioception, and generates the robot action in an auto-regressive way. A VQA dataset and a he CALVIN dataset are augmented with the speech instructions to train the VLAS model, and the latter one is further used to tune the model on robotic manipulation tasks.

The experiments demonstrate the promising results of VLAS, and showcases interesting way of commanding robots through the ownership, preference, and compound tasks.

### Strengths
1. The paper is well-written and easy to read. It provides efficient background information and detailed illustration of the proposed method.
2. The speech-driven manipulation task is novel. The design of storing user information within the dataset and generate the actions with RAG is smart, demonstrating interesting use cases concerning user ownership and preference.
3. The real-world demonstration further showcase the capability of the model.

### Weaknesses
1. Despite the common issue of inference speed in tuning a large VL model as a VLA model, the authors should still provide an analysis on the time required on using the model, especially the bottleneck (is it the audio processing part?) as well as the possible strategies to boost it.
2. The evaluation on robotic manipulation is not efficient. It should be evaluated whether the policy generalizable to novel scenes (like training on CALVIN ABC and test on D, or in other simulations) or tasks. More importantly, if the model requires further training on novel cases, whether the speech processing modules can be transferred.

### Questions
1. I wonder if there are additional use case that leverage more semantics information from the speech, like the emotion?
2. How long historical information can the model handle? If there are multiple users in history and their ownership violates each other, will the model be able to handle this?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces VLAS, a novel vision-language-action model designed to facilitate robot manipulation tasks by integrating speech as a primary instruction modality, bypassing traditional speech-to-text conversion methods. This approach enables VLAS to capture essential non-verbal cues, such as voiceprints, which assist in executing personalized tasks based on individual user needs. Built on the LLaVA model, VLAS employs three training stages to process multimodal inputs across text, image, and speech, aligning these representations for seamless action generation. The authors also developed two datasets, SQA and CSI, to enhance the model’s handling of speech instructions, alongside a voice retrieval-augmented generation (RAG) system to access individualized knowledge. Experimental results demonstrate VLAS’s superior performance on complex, customized robot tasks, particularly when handling personalized commands, outperforming other models that rely on separate speech recognition systems.

### Strengths
1. The paper introduces VLAS, a vision-language-action model evaluated on a comprehensive set of tasks, including customized tasks that leverage speech input for personalized robot manipulation. 

2. Additionally, the authors contribute two new datasets, SQA and CSI, which enhance the model's ability to process multimodal inputs by including speech instructions alongside visual data.

### Weaknesses
 1. The necessity of incorporating raw speech, given the availability of video and language (transcripts), remains unclear. Many tasks focus on ownership, and contemporary speech recognition models are capable of discerning individual identities through voice characteristics. Integrating recognized user identity and vocal nuances as metadata in text input might achieve similar effects in current vision-language models (VLMs).

 2. While speech transcripts alone may lack certain nuances, the video input could compensate for these through visual cues like gestures. The paper’s limited treatment of emotion in its framework is another concern, especially as language models like ChatGPT already offer emotion detection from text ("Emotion detection GPT"), which could outperform humans [8].

 3. Overall, the additional complexity introduced by adding raw speech input to video and transcript data may not significantly enhance model performance in a meaningful way.

 4. The paper might benefit from using more recent multimodal VLMs, such as MA-LMM [1], Chat-UniVi [2], ST-LLM [3], LLaVA-NeXT-Video [4], VideoChat2 [5], VideoLLaMA 2 [6], and Video-LLaVA [7], to contextualize the VLAS model's contributions within the latest advancements.

### Questions
"The voice retrieval-augmented generation (RAG) (Zhao et al., 2024) is subsequently proposed": 

If this method was previously developed by Zhao et al. (2024), why is it described as "subsequently proposed" here? Is the paper introducing a new variant or application of this technique, or is it simply implementing the existing RAG approach as described in Zhao et al. (2024)?

### Soundness
2

### Presentation
4

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper creates a vision-language-action model by incorporating speech to create a VLAS model.  Two new datasets SQA and CSI are introduced.  A RAG setup is used for handling contextual queries.  Section 1 gives background for why they incorporated speech, including contextual queries.  The model is built on top of LLaVA.  A pretrained speech encoder was used.  The model is called, “Speech LLaVA.”  Comparable accuracy can be found on the CALVIN benchmark to traditional VLAs.  For customization tasks, this approach appears to do very well.  Section 2 describes related work.  Section 3 describes the approach, including the LLaVA-based approach, action tokenization / detokenization.  SQA dataset was created by sampling examples from the original LLaVA dataset and running them through a TTS system.  CSI dataset used 389 textual examples x 500 voices to result in 194k examples; training was interleavesd with text and audio.  A three stage process involving audio alignment, speech question answering and then robot manipulation fine tuning was performed.  Section 4 describes experiments and results across CALVIN, customized tasks and LLaVA.

### Strengths
This paper presents a natural extension to LLaVA to use speech input. With minor reservations about related work, the confounding nature of speech with and without context (and the lack of a text baseline), the exclusive use of TTS outputs and a few baselines, the paper is well-written and the results appear to be reproducible.

### Weaknesses
 This paper presents a natural extension to LLaVA to use speech input. With minor reservations about related work, the confounding nature of speech with and without context (and the lack of a text baseline), the exclusive use of TTS outputs and a few baselines, the paper is well-written and the results appear to be reproducible.

 see above

### Questions
Some questions about the paper:

* The RAG pipeline appears to be intimately coupled with speech in this paper, but needn’t be.  Why wasn’t a baseline with language only inputs performed?  What would be the results?
* All the experiments appear to be with TTS output, which will certainly be biased.  Some results need to be with real speech.  Do you have any quantitative numbers with real speakers?  Even on a subset of any of the data you presented?
* The incorporation of RAG into the pipeline makes some parts of the paper confusing.  For example, in Section 4.1 it wasn’t clear if these leveraged the context part of the model (e.g., RAG) (e.g., Table 1).
* Why wasn’t OpenVLA shown in Table 1?


For related work, it would be good to cite at least the following:
* Other multi-modal models that incorporate audio should be included here.  Some missing references include, but there are likely more:
    * Unified-IO 2: https://arxiv.org/abs/2312.17172
    * Gemini (inherently multi-modal)
* Other VLMs, such as IDEFICS and Prismatic:
    * https://huggingface.co/blog/idefics
    * https://github.com/TRI-ML/prismatic-vlms

Other small things:
“pre-cess” -> “process” p2.
Inconsistency between VLAS and SpeechLLaVA terms.
“Absolute superiority” -> probably weaken this term.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes VLAS and integrates speech for robot manipulation. It makes communication more natural and presents two new datasets for the community.

### Strengths
1. This paper is easy to read and follow.
2. The core idea and motivation are interesting and practical. I believe it is great to have the speech modality in interactions with robots, as it feels natural and intuitive. Using speech to capture human intent is also a good idea. Creating a unified model provides a solid foundation for future work.
3. The illustrations are very helpful.
4. The datasets provided to the community are beneficial for the field.

### Weaknesses
Some ablation studies may be needed. Please refer to the "Questions" section.

### Questions
1. Are there any statistics from real-world experiment results? I think it's important to understand how the impressive results from simulations can transfer to real-world applications.
2. You use the RAG and the pretrained speech model to obtain the voiceprint, which is then used to retrieve preferences from the database. It seems the voiceprint is derived from the RAG module. You only present the VLA experiment in a customized task, and I wonder about the performance of the VLA combined with speech RAG in this context. I think this need to be given to support your motivation ( why not use the cascading pipeline, you mentioned the cost and the intent capture), I suspect that the speech RAG can capture the intend and give the intend text from the database to VLA model.
3. I think you need some more ablation studies, such as examining the effects of not using the RAG module in the customized task.

I think if these questions are addressed, I will raise my score cause I think the unified large model for speech, vision, text and action is meaningful.

### Soundness
3

### Presentation
3

### Contribution
3
