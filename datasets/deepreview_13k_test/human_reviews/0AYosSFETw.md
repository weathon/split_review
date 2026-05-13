# Towards human-like spoken dialogue generation between AI agents from written dialogue

- Decision: Reject
- Scores: 6, 8, 5

## Abstract
The advent of large language models (LLMs) has made it possible to generate natural written dialogues between two agents.
However, generating human-like spoken dialogues from these written dialogues remains challenging.
Spoken dialogues have several unique characteristics: they frequently include backchannels and laughter, and the smoothness of turn-taking significantly influences the fluidity of conversation.
This study proposes \textit{CHATS} --- \textbf{CH}atty \textbf{A}gents \textbf{T}ext-to-\textbf{S}peech --- a discrete token-based system designed to generate spoken dialogues based on written dialogues.
Our system can generate speech for both the speaker side and the listener side simultaneously, using only the transcription from the speaker side, which eliminates the need for transcriptions of backchannels or laughter.
Moreover, CHATS facilitates natural turn-taking; it determines the appropriate duration of silence after each utterance in the absence of overlap, and it initiates the generation of overlapping speech based on the phoneme sequence of the next utterance in case of overlap.
Experimental evaluations indicate that CHATS outperforms the text-to-speech baseline, producing spoken dialogues that are more interactive and fluid while retaining clarity and intelligibility.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the task of generating spoken dialogues between 2 parties using autoregressive models. It follows the earlier work on DLM (dialogue language model), and tries to extend it for better turn-taking and pause modeling. This results in more natural generated dialogs. The authors train all models from scratch.

### Strengths
It makes sense to incorporate pitch and content units in a multi-stream dialog language model for spoken dialog generation. The authors also build secondary models for turn taking and pause modeling. These are very critical for a more natural sounding dialog generation, and are lacking in textual dialogs. Especially the audio samples with overlapping speech are impressive.

### Weaknesses
I had a hard time to understand the concept of "units" and has to read Kharitonov. The paper should do a better job explaining what they are with motivation. Furthermore I had a hard time understanding uLM and had to read the DLM paper. The authors should first explain DLM. But after reading these 2 papers, it is clear that the contribution is actually not that significant, but still very creative idea, applied to Japanese data.

### Questions
dGSLM is trained with 2000 hours of English data. In this paper authors use only 74 hours of Japanese data. And they train the dGSLM models from scratch using that 74 hours. The experimental results show inferior comprehensiveness compared to the original dGSLM paper. This begs the question of authors replicating the experiments for English with larger training set. In other words, we do not know whether their improvements will disappear with more data.

### Soundness
4 excellent

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method to generate natural overlapping spoken dialogue with the listener cues like backchannels and laughter only using the written transcripts (that lack the rich spoken dialog modes). This system generates speech for both the speaker and the listener simultaneously, using only the transcription from the speaker side by finetuning the modified dGSLM model with careful curation and pre-processing of natural dialog. The overall pipeline is similar to the one used by the dGSLM system; however using the careful finetuning process delivers very strong results and a practical tool for enriching the dialogs with natural spoken dialog properties. 

The model has extensive experiments to show that the utterance quality is good, the dialog segments contain high quality of close to ground truth backchannels and pauses and the turn taking events also resemble the ground truth. Most important, the qualitative human evaluation experiments also show very good naturalness, meaningfulness and sound quality.

### Strengths
- There are many Dialog generation LLMs available today. These are currently not very natural generation systems, meaning, they cannot mimic human-to-human conversations that contain rich elements like laughter, backchannel, fluid turn-taking, etc. This paper aims to solve this problem and generates natural spoken dialog and presents methods including how to prepare datasets, create context properly in the training data and predict turn-taking events using the dual-transformer architecture (dGSLM). 
- The methods also shows how smaller datasets (74 hr of 2 channel speech) can be used to train a high quality spoken dialog generator (using a pre-trained uLM model). 
- Ablations show that data augmentation, next sentence objectives, turn-taking mechanism were all important pieces of the architecture and pipeline are all important for getting the overall natural dialog output.

### Weaknesses
- the paper presents the overall system very well, however, it is not clear if the original contribution of the work is significant. It seems like a straightforward extension of the dGSLM model where it has been fine-tuned to create this improved version of natural dialog corpora. 
- there is no comparison to any other baseline system that is described in the paper. 
- human evaluation does not try to assess the content and quality of generated backchannels. 
- Also, it is not clear how the generation will transfer to various other data domains.

### Questions
- it is not clear how many backchannel tokens are in the vocabulary (like laughter, ums, etc).

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes CHATS (CHatty Agents Text-to-Speech), a system for transforming written dialogue into spoken dialogue, whose content is coherent with the input written dialogue but generated with backchannels, laughter, and smooth turn-taking. Several contributions are announced: a method to prepare written dialogue by excluding backchannels, a mechanism for taking turns in conversation, and a Multi-Stream Dialogue Transformer Language Model. Paper builds upon previous work, such as dGSLM and Dialogue Transformer Language Model by Nguyen et al. in 2023 and it provides evaluations for different parts of the proposed system, including the dialog model, turn-taking model, and back-channeling model. 

When I take a closer look, it's clear that paper has too much stuff in it. There are many models and evaluations crammed together in one document w/o enough details of each of them. This makes it hard to read and understand the paper. It's unfortunate because this is an ambitious and relevant research objective that is described here. Current version of the paper needs a big re-organization to make it clearer and maybe each problem addressed should correspond to a single paper with deeper / more detailed description and evaluation; that would allow reader/reviewer to better understand and appreciate the valuable insights it offers.

### Strengths
-This research is ambitious because it explores how people talk in real conversations, not just in written text.

-It introduces a Turn-Taking and Backchanneling Mechanism, which is important for making better autonomous spoken conversational agents.

-The Multi-Stream Dialogue Transformer Language Model (MS-DLM) seems the main contribution and is definitely an interesting architecture

### Weaknesses
* It's unfortunate that the spoken dialog examples on GitHub are not in English. This makes it challenging for me to evaluate, and it limits its accessibility since only Japanese speakers can understand it. English examples would have been more universal.

- In the contributions mentioned in the paper, it is not clear why "Conversion from Spoken to Written Dialogue" is valuable or innovative. Authors mention using both rule-based and machine learning approaches to identify backchannels and exclude them from written dialogues, but the paper lacks detail on the challenges this addresses. Is it mainly about data preprocessing?

- As said above, the paper's structure needs improvement, as it tries to cover too many topics in one document.

- The paper builds on the work of dGSLM (Nguyen et al., 2023) and the Dialogue Transformer language model (DLM) (Nguyen et al., 2023), but it doesn't provide enough information about these previous models to make this paper self-understandable

- Section 3.1.2 seems to be a core part, but it's too brief to fully understand its significance.

### Questions
see main remarks above +
 not clear was is the challenge in the part "Conversion from Spoken to Written Dialogue"

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
