# VoxDialogue: Can Spoken Dialogue Systems Understand Information Beyond Words?

- Decision: Accept
- Scores: 8, 8, 3, 8, 6

## Abstract
With the rapid advancement of large models, voice assistants are gradually acquiring the ability to engage in open-ended daily conversations with humans. However, current spoken dialogue systems often overlook multi-modal information in audio beyond text, such as speech rate, volume, emphasis, and background sounds. Relying solely on Automatic Speech Recognition (ASR) can lead to the loss of valuable auditory cues, thereby weakening the system’s ability to generate contextually appropriate responses. To address this limitation, we propose \textbf{VoxDialogue}, a comprehensive benchmark for evaluating the ability of spoken dialogue systems to understand multi-modal information beyond text. Specifically, we have identified 12 attributes highly correlated with acoustic information beyond words and have meticulously designed corresponding spoken dialogue test sets for each attribute, encompassing a total of 4.5K multi-turn spoken dialogue samples. Finally, we evaluated several existing spoken dialogue models, analyzing their performance on the 12 attribute subsets of VoxDialogue. Experiments have shown that in spoken dialogue scenarios, many acoustic cues cannot be conveyed through textual information and must be directly interpreted from the audio input. In contrast, while direct spoken dialogue systems excel at processing acoustic signals, they still face limitations in handling complex dialogue tasks due to their restricted context understanding capabilities. All data and code will be open source at \url{https://voxdialogue.github.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a new benchmark called VoxDialogue for evaluating the audio comprehension capabilities of voice dialogue systems. The benchmark encompasses 12 sound-related attributes, including speaker attributes (age, gender, accent, language), paralinguistic features (emotion, volume, speed, fidelity, stress, non-verbal expressions), and background sounds (audio, music). The paper also conducted a systematic evaluation of existing spoken dialogue systems, comparing their performance in terms of understanding acoustic information. Besides, the paper proposed a comprehensive method for constructing spoken dialogue data tailored to different acoustic attributes, enabling large-scale data synthesis to support model training.

### Strengths
1. This paper addresses the current issue of speech dialogue systems ignoring audio information by proposing a new benchmark test, which is a meaningful research endeavor.

2. The evaluation of ASR-Based/Direct Spoken Dialogue Systems reveals the limitations of current ASR-based and direct speech dialogue models.

3. The construction of a challenging test set containing 4.5K multi-turn dialogue samples can provide assistance to the voice dialogue systems research community.

### Weaknesses
1. Recommend to add the specific values of text generation metrics in the appendix.

2. Suggest to include statistics on the duration of the dataset.

### Questions
What do AVG and Dur. refer to in Table 3?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper provides a dataset involving a spoken dialogue corpus between two humans. It is designed to evaluate spoken dialogue systems. The data is selected so as to include 12 different characteristics where speech would help, such as emotion.

### Strengths
Overall, this is a clean paper proposing a valuable dataset for spoken language researchers. It is creative to use GenAI to create spoken data for target dimensions related to Speech. I also opened the examples in the github repo and it is very possible that this dataset will be employed by many researchers in this field.

### Weaknesses
The dataset does not include any task oriented dialogue. Hence the evaluation is limited to BLEU or GPT ratings. In many real life scenarios, the spoken dialogue systems are aiming at either an agent like scenario, like Google Home/Alexa style personal assistants, or call center automations, or outbound calls. Their performance cannot be evaluated using BLEU only and the target goal completion is critical. Maybe in the next version of the dataset the authors may want to extend this dataset with such data.

### Questions
- the dataset may also be expanded with a target goal as in MultiWoz / ATIS. For example there is a frustrated call center example but the content is not there, it is just emotional exchanges.
- can you elaborate further and think of some ablations especially regarding the difference of FunAudioLLM from direct dialogue models? why exactly is this model performing better and in which dimensions?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Voice assistants are systems that interact with human beings, but current systems usually only focus on linguistic information from text, neglecting useful verbal cues. This work provides a benchmark to evaluate current multimodal systems. In addition, they also identified 12 features that highly correlated to acoustic information and evaluated other dialogue systems on these features.

### Strengths
Other than semantic information from text, the authors proposed three directions worth investigating in dialogues: speaker information, paralinguistic information, and background sounds, which are valuable and well-designed.

### Weaknesses
1. On page 2, around line #100, 'For each of these attributes, we designed the most appropriate spoken dialogue synthesis pipelines' This needs more clarification; what is 'most appropriate'? How is it defined? The term 'most appropriate' lacks a clear definition, making it difficult to understand the rationale behind the chosen synthesis pipelines. It is unclear whether this 'appropriateness' is based on empirical evidence, theoretical considerations, or a combination of both. Without a precise definition, it is hard to assess the validity of the approach. Furthermore, it is not clear if the authors considered other synthesis pipelines and why the chosen ones are superior.
2. The second and third contributions listed at the end of the 'Introduction' section need a little more details, such as metrics for evaluating performance. From the description of the third contribution, it is unclear how and why the way to construct spoken dialogue data is unique/beneficial.
3. For the first two paragraphs under section 2.1, what are the differences between 'audio-language models' and 'spoken dialogue models'? There are no clear differences between the listed works and why they were separately discussed. In other words, I cannot find reasons to use two separate paragraphs, especially since they are all under the 'Spoken Dialogue System' subsection.
4. I think the third paragraph under section 2.1 is not appropriately placed. This subsection mainly discusses spoken dialogue systems, but not why the lack of a comprehensive benchmark for different evaluation tasks. It will be more appropriate to place it at end of section 2.2. Currently, the contents for the last paragraph from sections 2.1 and 2.2 are heavily overlapped.
5. I am confused for Table 2. For example, based on the examples given, 'business tasks' is dependent on 'man voice', and 'free juice' or/and 'beef burger' is dependent on 'young voice'. From the manuscript, I did not see how this is established for the speaker's information. The connection between speaker attributes (age, gender) and the generated dialogue content is not clearly explained. It is unclear how the model ensures that the generated dialogues are appropriate for the specified speaker attributes. The examples provided in Table 2 seem arbitrary without a clear methodology.
6. Many details are missing under section 3. Under section 3.2, authors state that they are referring to [Lin et al., 2024a] for their implementation of LLMs with advanced reasoning capabilities to synthesize spoken scripts. They did not specify the exact reason for this, especially what LLMs were used. It is not clear if GPT-4o is the only one that has been used or if it is one among a few. Also, under stage 2, 'We carefully tailored the most appropriate speech synthesis method for each attribute during the generation process,' what does 'most appropriate' even mean here? And how was it compared? For instance, if another work also considered paralinguistic information for their data synthesis process, why is your approach more 'appropriate' than theirs? Under stage 4, the authors state that 'For attributes such as volume, fidelity, audio events, and music, we performed post-processing to ensure that the audio aligns with the required expectations.' how do we interpret 'music' as an attribute here? In addition, 'For music, we randomly apply two different methods to integrate the music with the dialogues.' What does this even mean? How is it post-processed to align with the required expectations? How is music processed? What exactly is the expectation?
7. At the end of section 4.1 for task definition, is there a particular reason to use only the last response from the entire dialogue history for evaluation of the spoken dialogue systems? The rationale for using only the last response for evaluation is not clearly justified. It is unclear why the entire dialogue history is not considered, especially since the goal is to evaluate the system's ability to understand context. Evaluating only the final response might not fully capture the system's ability to maintain coherence and consistency throughout the dialogue.
8. It is not counter-intuitive that ASR-based systems perform poorly compared to multimodal systems because they only take text at input. The authors demonstrate (from the abstract section, conclusion section, and all the experiments) that ASR systems fail to capture important acoustic signals; it is never a fair comparison in the first place.

### Questions
Please refer to the weaknesses listed.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper contributes to the design and creation of a novel dataset for dialogue systems benchmarking. Its design and creation relies on synthetic data and its main attempt is to close the gap on paralinguistic information understanding which its more appropriate to infer directly from acoustics than from the recognized text.

The paper summaries the current gap in SOTA benchmarks and the limitations of the existing data sets and evaluation protocols. This contribution is oriented for enhancing dialogue understanding. The protocol and steps how Voicebox is created is detailed into steps and quantitative and qualitative assessed.

### Strengths
This paper presents a solid contribution to standardize, democratize, and accelerate the evaluation of spoken dialogue systems. The summary of the state of the art and status quo is well described and the voice attributes and dialogue rubrics is well covered. Authors also commit to open source their protocol and database, which will help the community to iteratively improve it beyond the current contribution. The mental model proposed on synthetic data is a strong tool to accelerate the capabilities of dialogue understanding on GPT-based foundational model.

### Weaknesses
The paper and background is slightly bias oriented to understanding, although in order to move the SOTA in dialogue modelling in human computer interaction, the faithful generation of spoken response is also critical. The paper lists the attributes pursued in the synthetic generation, and they dedicated effort in choosing sufficient good tools to generate the response, but there is not formal assessment of how faithful and suitable those target realizations are realistic. Without a human preference assessment between actual dialogues and the synthetic generated ones, the data set and benchmark presented in this work can limit the ceiling truth of the models developed using it as a benchmark. Still the work is valuable and will contribute to accelerate the foundational properties a the pre-training stage of Foundation models that power spoken dialogue systems.

The authors based there decisions on the audio generation side based only superficial knowledge of speech. Even their statements about the speech bandwidth is inaccurate and not scientifically supported. Authors should expand, improved and detailed describe the process and decision making on the fidelity and other speech attributes.

### Questions
a) How do we ensure the synthetic data is faithful respect to human-human interactions? the emotion modelling and its realization is not a 1-1 mapping and its suitability given the input emotion from the user of the system is not trivial. 

b) Speech and spoken language communication is a 1 to many problem. Authors seem to define 1 single realization of a dialogue as the "ground-truth". Although multiple performances of the same dialogue (from the "speech generation" perspective would be acceptable. How authors and VoxDialogue datasets enable to consider the stochastic nature of human communication?

c) How VoxDialogue is scalable to mutliple languages and low resource languages?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present a dataset called VoxDialogue to benchmark the ability of spoken dialogue systems to leverage acoustic information to adapt their interaction. Using LLMs and TTS, they created 4.5K multi-turn spoken dialogue samples according to 12 factors (e.g. age, language, accent, volume, noise...). The authors then evaluated several existing spoken dialogue systems on this benchmark showing that such systems struggle in these situations given their low BLEU and ROUGE scores.

### Strengths
Making available such datasets  with controlled conditions over 12 factors (Gender, Speed, Emotion, Stress, Language, Non-verbal Expressions, Volume, Fidelity, Audio Events Music, Age, and Accent) is a very interesting contribution to the field. The creation process has been performed with care using the latest industrial methods (GPT-4o and GTP4Microsoft Edge's online text-to-speech). 

The evaluation of the five systems (Audio-Flamingo, Qwen-Audio, SALMONN, Qwen-Audio2 and FunAudioLLM) is also very interesting, and forms the basis of the comparative analysis.

### Weaknesses
The paper does not present technical novelty nor original metrics to evaluate dialogue systems. For instance, the evaluation has been performed using n-gram metrics which fails to handle variations in answers. BERT-Score is  similar in all conditions and error bar is not provided. This makes it difficult to assess the difference between models. The evaluation with GPT4 is correlated to other metrics but with more extreme differences. Human evaluation would definitely be an added value here. 

As raised by the authors using TTS and LLM-generated content might be too far from realistic settings. The benchmark might thus be useful for developing systems rather evaluating them. It is true that TTS is useful for training models (Liu et al. 2024 was about lip movements generation) it can be harmful when it is the only data available (Desot et al. 2020, Corpus generation for voice command in smart home and the effect of speech synthesis on End-to-End SLU). But if that informs about the training, it does not support using it for evaluation.

The generated dialogues I have listened and seen do not seem to have a goal (not task oriented) hence it is difficult to understand how a system should answer for reached a target. 

The other question is related to the choice of the human behind. Assessing a gender from voice can be a bad idea simply because the system could be wrong and also because the human behind might not agree being attributed a title related to a gender. 

Some of the attributes (age for instance) might be seen as too much intrusiveness. What is the stance of the authors about this?

How many languages have been considered in the datasets? 

details 

SUPERB is not the only benchmark in 2021, Lebenchmark (Evain et al. 2021), was also there

there are repetitions of sentences between the introduction and section 2

### Questions
The generated dialogues I have listened and seen do not seem to have a goal (not task oriented) hence it is difficult to understand how a system should answer for reached a target. 

The other question is related to the choice of the human behind. Assessing a gender from voice can be a bad idea simply because the system could be wrong and also because the human behind might not agree being attributed a title related to a gender. 

Some of the attributes (age for instance) might be seen as too much intrusiveness. What is the stance of the authors about this?

How many languages have been considered in the datasets? 


details 

SUPERB is not the only benchmark in 2021, Lebenchmark (Evain et al. 2021), was also there

there are repetitions of sentences between the introduction and section 2

### Soundness
3

### Presentation
3

### Contribution
3
