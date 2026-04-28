# DNASpeech: A Contextualized and Situated Text-to-Speech Dataset with Dialogues, Narratives and Actions

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 6, 6, 3, 3

## Abstract
In this paper, we propose contextualized and situated text-to-speech (CS-TTS), a novel TTS task to promote more accurate and customized speech generation using prompts with Dialogues, Narratives, and Actions (DNA). While prompt-based TTS methods facilitate controllable speech generation, existing TTS datasets lack situated descriptive prompts aligned with speech data. To address this data scarcity, we develop an automatic annotation pipeline enabling multifaceted alignment among speech clips, content text, and their respective descriptions. Based on this pipeline, we present DNASpeech, a novel CS-TTS dataset with high-quality speeches with DNA prompt annotations. DNASpeech contains 2,395 distinct characters, 4,452 scenes, and 22,975 dialogue utterances, along with over 18 hours of high-quality speech recordings. To accommodate more specific task scenarios, we establish a leaderboard featuring two new subtasks for evaluation: CS-TTS with narratives and CS-TTS with dialogues. We also design an intuitive baseline model for comparison with existing state-of-the-art TTS methods on our leaderboard. Comprehensive experimental results demonstrate the quality and effectiveness of \dataname, validating its potential to drive advancements in the TTS field.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new TTS task and benchmark to produce contextualized and situated synthetic speech using dialogues, narratives and actions.

### Strengths
The new dataset would be useful to the TTS community and will be made available
The data creation methodology seems reasonable as does the design of the DNA Speech model.

### Weaknesses
1. The precise meaning of situated and contextualized is not very clear from my reading of the paper. Further, it is not very clear how actions in particular aid in situated and contextualized TTS. 

2. From the data pipeline, it is not clear whether the obtained subtitles exactly match the speech, or are machine generated in some way. There seem to be many automated portions, for example, obtaining subtitles through OCR, getting Dialogues, Actions, Narratives and Characters from the original movie scripts, speech denoising etc. For all of these steps, there are no objective measures of quality reported, which casts doubt on the quality of data used.  Furthermore, the only quality evaluation used involves training a TTS models using DNASpeech and evaluating it. 

3. The proposed ASR filtering based on Whisper could be potentially aggressive because the authors remove all non perfect matches. This means that the data obtained is selected based on Whisper's biases for movie transcription, which is not ideal.

### Questions
1. Three listeners is a small number for a TTS MOS test. Did the authors conduct a wider test ?

### Soundness
3

### Presentation
2

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
This paper introduces DNASpeech, a novel contextualized and situated text-to-speech (CS-TTS) dataset designed to enhance TTS performance by incorporating prompts from dialogues, narratives, and actions (DNA). DNASpeech provides rich multimodal prompts aligned with speech clips, filling a gap in current datasets that lack comprehensive contextual information for TTS tasks. The dataset includes 2,395 distinct characters, 4,452 scenes, and 22,975 dialogue utterances, along with over 18 hours of high-quality speech recordings. To validate DNASpeech, the authors propose a leaderboard and evaluation benchmarks featuring two subtasks: CS-TTS with narratives and CS-TTS with dialogues. The experimental results demonstrate the potential of DNASpeech to drive advancements in controllable and expressive TTS systems.

### Strengths
The integration of dialogues, narratives, and actions (DNA) as contextual prompts is an innovative addition to existing TTS datasets, providing richer and more varied situational context. The dataset is constructed using a detailed and well-validated annotation pipeline, with emphasis on quality control through denoising, ASR verification, and manual assessment. The alignment method that combines both coarse-grained and fine-grained techniques is robust and well-implemented. The dataset addresses a crucial need for more context-aware TTS systems and offers a structured evaluation through the established leaderboard. This contribution is likely to inspire further research in controllable TTS using diverse prompts. Additionally, the paper provides a thorough explanation of the dataset construction and the challenges involved, with the use of visual aids to depict the pipeline and dataset characteristics aiding in comprehension.

### Weaknesses
The experiments primarily focus on validating the dataset using specific subtasks (narratives and dialogues), but they could benefit from broader model diversity and more diverse metrics beyond MOS evaluations. Including results from a larger variety of baseline models would make the evaluation more comprehensive. While the paper claims that DNASpeech can generalize well for different TTS tasks, the experimental evidence supporting this claim is limited, and testing with a wider set of models and comparing performance on tasks beyond CS-TTS (e.g., emotional TTS) would strengthen this assertion. Additionally, the dataset's reliance on movie scripts might limit its applicability for general conversational TTS, as the movie-based context might not fully represent day-to-day conversational dynamics.

### Questions
Can the authors provide further insights into how well the dataset generalizes to tasks beyond CS-TTS, such as emotional speech synthesis or audiobook narration?

How do the authors address potential biases introduced by the use of movie scripts as the primary source for dataset construction?

Would additional metrics beyond MOS, such as word error rate (WER) or speaker similarity, provide more insights into the dataset's applicability?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces DNASpeech, a novel contextualized and situated text-to-speech (CS-TTS) dataset that incorporates comprehensive descriptive prompts aligned with speech data. The dataset contains "DNA" prompts - Dialogues (conversational context), Narratives (environmental scenes), and Actions (speaker's expressions/actions) - along with high-quality speech recordings. DNASpeech includes 2,395 distinct characters, 4,452 scenes, and 22,975 dialogue utterances totaling over 18 hours of speech. The authors developed an automated annotation pipeline for aligning speech clips, content text, and descriptions. They also established a leaderboard with two evaluation subtasks: CS-TTS with narratives and CS-TTS with dialogues. The paper proposes a baseline model and demonstrates DNASpeech's effectiveness through extensive experiments comparing it with existing TTS methods.

### Strengths
1. The paper introduces a novel and valuable contribution to TTS research through DNASpeech, a contextualized and situated text-to-speech dataset that incorporates comprehensive "DNA" (Dialogues, Narratives, Actions) prompts.

2. The authors develop an innovative automatic annotation pipeline that enables efficient multifaceted alignment among speech clips, content text, and corresponding descriptions, making the dataset construction process systematic and reproducible.

3. The dataset is substantial and diverse, containing 2,395 distinct characters, 4,452 scenes, and 22,975 dialogue utterances with over 18 hours of high-quality speech recordings, providing rich resources for TTS research.

4. The paper establishes a clear evaluation framework through a leaderboard featuring two specific subtasks (CS-TTS with narratives and CS-TTS with dialogues) and provides an intuitive baseline model for comparison.

### Weaknesses
1. Although the authors compared the dataset and two models on the other datasets, the dataset's reliance on movie scenes rather than real-world scenarios might limit its applicability to authentic speech patterns and natural conversations. The use of scripted dialogues and controlled environments in movie scenes may not capture the nuances of spontaneous speech, such as hesitations, filler words, and overlapping speech, which are common in real-world interactions. This could lead to models trained on this dataset performing poorly when applied to more naturalistic conversational settings.
2. The experimental evaluation metrics are somewhat limited, primarily focusing on MOS scores. Additional objective metrics could provide more comprehensive performance assessment such as spectral distortion or character error rates. The lack of objective metrics makes it difficult to quantify the specific aspects of speech quality that are being improved or degraded. For example, while MOS scores can indicate overall perceived quality, they do not provide insight into the accuracy of phonetic realization or the naturalness of prosody. Metrics like Mel-Cepstral Distortion (MCD) or Perceptual Evaluation of Speech Quality (PESQ) would offer a more detailed analysis.
3. The paper lacks detailed analysis of the baseline model's architecture choices and their impact on performance. Without a clear understanding of how different architectural components contribute to the model's performance, it is difficult to assess the effectiveness of the proposed approach. For instance, the paper does not discuss the specific design choices for the context encoder, style fusion module, or variance adaptor, nor does it provide any ablation studies to demonstrate the importance of these components. This makes it challenging to replicate the results or to build upon the proposed model.
4. The comparison with existing methods could be more extensive, particularly in analyzing how different types of prompts affect the speech generation quality. The paper does not provide a detailed analysis of how the different types of prompts (dialogues, narratives, and actions) individually impact the quality of the generated speech. A more thorough investigation would involve comparing the performance of the model when using each type of prompt separately, as well as in combination, to understand their relative contributions. This would help to identify which prompts are most effective for improving speech quality and under what conditions.
5. Similarly, for the public dataset comparison, the author did not select the SOTA models for the comparison. It would be great to see the comparison against them.

### Questions
Have you guys conducted ablation studies showing the individual contributions of Dialogues, Narratives, and Actions to the overall speech quality?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a novel text-to-speech (TTS) dataset, DNASpeech, which is designed to support contextualized and situated TTS (CS-TTS) tasks. The dataset includes high-quality speech recordings annotated with Dialogues, Narratives, and Actions (DNA) prompts, aiming to enhance the accuracy and expressiveness of speech synthesis. Experimental results are provided to validate the quality and effectiveness of DNASpeech.

### Strengths
1. This paper proposes the "DNASpeech" dataset. It addresses a significant gap in existing TTS datasets by providing a rich dataset with contextualized and situated prompts, which is crucial for advancing TTS research.

2. The paper describes the comprehensive automatic annotation pipeline that aligns speech clips with detailed dialogue, narrative, and action descriptions, which is a complex and valuable contribution.

### Weaknesses
1. In Sec. 3.2, the authors individually apply information extraction for both speech and scripts in the movie in step 2. Then in step 3, they attempt to align them in two stages.
* 1.1 Why "more than 800 million potential matches are required"? The authors claim that each speech segment is matched against every line in the script, leading to a quadratic matching complexity. However, this seems inefficient, as movie titles or other metadata could be used for initial alignment, significantly reducing the search space. Furthermore, for the "DNA" prompt, the authors' heuristic extraction from scripts is questionable. What is the accuracy of this alignment? The paper lacks a quantitative evaluation of this crucial step. Methods such as directly extracting speech attributes (e.g., speaker identity, emotion) from the audio, and using these to guide the alignment, are not considered, which could improve accuracy and reduce reliance on noisy script data.
* 1.2 "Following the script writing paradigm, we extract four key elements from each movie script: Dialogues Narratives, Actions, and Characters." The paper lacks detail on the extraction process. How are dialogues distinguished from narratives and actions? What specific NLP techniques or rules are used to identify these elements? For example, are dependency parsing or named entity recognition employed? The lack of detail makes it difficult to assess the robustness of the extraction method.
* 1.3 All data is from the movie. So there is a risk of domain bias. Because the movie can not cover all diverse accents, languages, or speaking styles. This limits the generalizability of the dataset and any models trained on it.

2. This paper is an extension of textual-prompt-based text-to-speech synthesis. The authors propose to extend the descriptive prompt of speech to three dimensions: 1) dialogue, 2) narrative, and 3) action. However, it is only an incremental work of the existing prompt-tts paradigm by extending the annotation pipeline. The core idea of using contextual prompts is not novel, and the contribution seems limited to the specific combination of these three elements.

3. In the experiments:
* 3.1 It is better to categorize into three types: 1) None-Prompt TTS, 2) natural language description prompt-based TTS, and 3) speech prompt-based TTS. The current categorization is not comprehensive and does not clearly distinguish between different prompting paradigms.
* 3.2 The method for CS-TTS in Sec. 4.1.2 is not clear. What is for "but includes classification tasks for emotion, pitch, energy, and speed during training"? For emotion, how do you obtain the label? Furthermore, it is not clear how the author leverages the "DNA" prompt as a condition to guide the generation process. The paper lacks a detailed explanation of how these auxiliary tasks are integrated into the training process and how the DNA prompts are used to modulate the acoustic parameters.
* 3.3 It lacks an ablation study for the attribution controllability for the proposed "DNA" attributes. Without such an ablation study, it is difficult to assess the individual contribution of each DNA attribute to the final speech synthesis quality.

4. The obtained dataset contains about 18 hours including 2395 distinct characters, indicating that only 0.45 minutes for a single character. It is small to train a good TTS system. The limited data per speaker may lead to overfitting and poor generalization, especially for complex contextualized tasks.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work introduces a new TTS task called **Contextualized and Situated Text-To-Speech** (CS-TTS), which incorporates contextual descriptions into speech generation, aiming to enable TTS models to produce more expressive speech. As the lacking of CS-TTS datasets, they created a new CS-TTS dataset called **DNASpeech**. Each speech sample in DNASpeech is accompanied by three types of contextualized prompts: **Dialogues** provide conversational context, **Narratives** describe the environment surrounding the speaker, and **Actions** detail the speaker’s actions and expressions. For dataset construction, they developed an automated annotation pipeline, with human evaluations to validate the approach.

Additionally, they established a leaderboard to assess the performance of current TTS systems, and introduced a baseline model adapted to the CS-TTS.

### Strengths
1. This work introduces a new dataset called DNASpeech, specifically created for the innovative CS-TTS task.
2. An automatic annotation pipeline is presented, utilizing techniques likes OCR, speech denoising, ASR to ensure the quality of produced dataset. Additionally, human evaluation is conducted to confirm the effectiveness of the pipeline.

### Weaknesses
## Weaknesses 

1. The paper asserts that contextualized descriptions lead to more accurate and expressive speech generation. However, there is only one experiment validating the effectiveness of CS-TTS, and it shows no significant improvement when using contextualized descriptions. For example, in evaluating the alignment between speech and environmental information, the MOS-E score gap between prompt-based TTS methods and non-prompted TTS is less than 0.1. StyleTTS, the best non-prompted TTS model, performs comparably to the prompt-based models. This makes it difficult to confirm the quality of the proposed dataset and the effectiveness of CS-TTS. The observed MOS-E differences between prompted and non-prompted models are very small, on the order of 0.01 to 0.02, which raises concerns that these differences may be due to factors other than the presence of contextual prompts, such as variations in model architecture, hyperparameter tuning, or even human evaluation noise. The paper does not provide sufficient evidence to rule out these alternative explanations.
2. The work introduces a TTS dataset where each sample includes three types of contextual prompts : **Dialogue**, **Narrative**, and **Action**. It is claimed that **Action** describes the speaker's actions and expressions, while **Narrative** provides environmental context, as mentioned in lines 74-76. However, based on the descriptions and examples given in the paper, these categories are difficult to differentiate. Take Figure 1 for an example, the Action "showing the gun to JURORS" corresponds to the Narrative "He picks up a revolver...", which is also an action. There is also confusion as to why the speaker's emotions are categorized under Action. Furthermore, in lines 142-144, the authors state that MEAD-TTS highlights environmental information (MEAD-TTS seems to focus on Action since it uses templates like "A <gender> says with a <emotion level> <emotion> tone" to write fine-grained prompts), yet in Table 1, MEAD-TTS's prompt is categorized under Actions, not Narratives, which contradicts the definitions provided in lines 74-76. Additionally, it seems like DailyTalk's focus is more on Dialogues than Narratives, given that DailyTalk focuses on chat history.
3. One of the core contributions of the work is the automatic annotation pipeline for building the CS-TTS dataset from movie scripts. However, the description of this pipeline is unclear, making it difficult to understand how different type of prompts are extracted from movie scripts.

### Questions
1. Does **Dialogue** specifically refer to the immediate sentence before the user speaks, or is it a summary of the entire chat history?
2. Will all three types of contextual prompts be provided to the proposed baseline model at once, or only one at a time?

### Soundness
2

### Presentation
2

### Contribution
2
