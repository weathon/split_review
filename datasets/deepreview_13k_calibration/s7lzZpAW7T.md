# Dynamic-SUPERB Phase-2: A Collaboratively Expanding Benchmark for Measuring the Capabilities of Spoken Language Models with 180 Tasks

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
Multimodal foundation models, such as Gemini and ChatGPT, have revolutionized human-machine interactions by seamlessly integrating various forms of data.
Developing a universal spoken language model that comprehends a wide range of natural language instructions is critical for bridging communication gaps and facilitating more intuitive interactions.
However, the absence of a comprehensive evaluation benchmark poses a significant challenge.
We present Dynamic-SUPERB \textit{Phase-2}, an open and evolving benchmark for the comprehensive evaluation of instruction-based universal speech models.
Building upon the first generation, this second version incorporates 125 new tasks contributed collaboratively by the global research community, expanding the benchmark to a total of \textit{180 tasks}, making it the largest benchmark for speech and audio evaluation.
While the first generation of Dynamic-SUPERB was limited to classification tasks, Dynamic-SUPERB \textit{Phase-2} broadens its evaluation capabilities by introducing a wide array of novel and diverse tasks, including regression and sequence generation, across speech, music, and environmental audio.
Evaluation results indicate that none of the models performed well universally.
SALMONN-13B excelled in English ASR, while WavLLM demonstrated high accuracy in emotion recognition, but current models still require further innovations to handle a broader range of tasks.
We will soon open-source all task data and the evaluation pipeline.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper builds on the prior work, Dynamic-Superb, by expanding its scope as an audio LLM benchmark to include a broader range of tasks centered on audio and speech understanding. It includes diverse tasks across speech, music, and general audio comprehension. The authors also evaluate several well-known audio LLMs, including SALMONN and Qwen-Audio, on this benchmark, showing that none of the current open-source audio LLMs can yet achieve satisfactory performance across all tasks.

### Strengths
This work is comprehensive and well presented. It brings the largest benchmark by far for speech and audio evaluation. It also conducts detailed experiments to assess the performance of several popular audio LLMs on the proposed benchmark.

### Weaknesses
There're a few possible issues that may further improve this paper.
- What is the motivation of creating this new benchmark? How will it guide the research community in advancing audio LLM research? I think the authors could emphasize this point further.
- I understand that the number of tasks has significantly expanded in Phase 2 compared to Phase 1. However, what is the primary focus of these additional tasks? Are there specific challenges unresolved in Phase 1 that Phase 2 addresses?

### Questions
Please refer to the weakness part.

### Soundness
3

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
3

### Summary
This paper presents Dynamic-SUPERB Phase-2, a benchmark designed to evaluate the capabilities of instruction-based universal speech models. By expanding the task count of its predecessor to 180, it becomes the largest benchmark for speech, music, and audio, encompassing a diverse array of tasks contributed by the global research community. This work is poised to drive further advancements in developing universal spoken language models and their evaluation methodologies.

### Strengths
1. Dynamic-SUPERB Phase-2 is the largest and most comprehensive benchmark for instruction-based universal speech models. It encompasses a wide range of tasks across speech, music, and audio, all paired with natural language instructions to evaluate models' cross-modal instruction-following abilities. This is a well-motivated and forward-looking approach that aligns with future trends in universal speech models, offering strong guidance for the field.
2. The paper is clearly written and easy to follow.

### Weaknesses
 1. The benchmark lacks tasks for audio, speech, or music generation.
 2. A primary concern is that the evaluation metrics heavily rely on large language models (LLMs) as referees. The reliability of these metrics is highly dependent on the capabilities of the LLMs themselves, which affects the benchmark's robustness and comparability. This reliance may also limit the benchmark's ability to expand to more complex tasks.

### Questions
My questions are listed above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a "Dynamic-SUPERB Phase-2", a benchmark for evaluating of audio-in-capable LLMs. This benchmark contains 180 tasks that cover a a large variety of tasks, spanning from music and audio classification to speech recognition, nonce word detection, intent and age classification, etc. These tasks were collected collaboratively. The audio-LLM are assumed to take in text instruction, an audio snippet, and produce text output. The interaction with the model is performed solely by the instruction, no finetuning is assumed. Depending on the task, the output encodes either classification label, regression value, or a natural language string. The benchmark is split into (a) full version, (b) an easier to operate representative sub-sample of tasks.

Given the benchmark, the authors also run a study comparing several off-the-shelf audio-capable LLMs, such as AudioQWEN, SALMONN, WhisperLLAMA, etc. One particular issue encountered is that various audio-LLMs would produce outputs in different formats, so the authors leverage another textual LLM to "translate/interpret" their outputs to the desired format.

### Strengths
* The paper tackles perhaps one of the most important problems in the audio-LLM space: the lack of audio-text benchmarks. In contrast to text-LLMs, where sets of hundreds of tasks are readily available, audio-LLM development is hindered by the lack of standard testing suites.
* I find the organization of the benchmarks to be thoroughly thought through.
* The paper runs a nice study on comparing off-the-shelf models, thus validating the proposed benchmarks.
* The paper validates referee model selection against human preferences.

### Weaknesses
 * Using GPT-4o as a referee, I believe, jeopardizes reproducibility of the reported results and usefulness of the paper. Imagine that in two years someone wants to compare their model to the benchmark numbers reported in this paper. Would GPT-4o still be around? Would this particular version of it be still accessible? This is even more puzzling, since, according to Appendix E, LLaMA-3.1-70B-Instruct is extremely close to GPT-4o here. It seems to me that using an openly accessible model here would be extremely beneficial.

* Regarding the model evaluation study: it is not clear how sensitive the tested models are wrt the prompts used. It would be very nice to have a small study on that.

* Whenever the evaluated model doesn't follow the instruction, its score is multiplicatively penalized by (1-N/A) or 1.0/(1-N/A) (depending on the metric). This is convenient as allows to have a single number but it totally hides how good models are at instruction-following.

### Questions
* The paper text reports that In Figure 3, Whisper-LLaMa performs best in speech recognition and understanding. However, when we look at Table 2, it is way behind SALMONN in phone recognition. Looking at ASR performances across tables, it does seem that SALMONN mostly falls behind on a few non-English transcriptions (SUPERB OOD Asr Zh). I wonder if there is a more nuanced story here than is told in S5.1.

* Table 7 has inconsistent WER reporting, ie "Children Song Transcript" has WER not scaled by 100% while it is scaled in other places.

* It would be nice to have the "N/A rate" reported for the models.

### Soundness
3

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
3

### Summary
The paper suggests a new (milestone of a) benchmark to test the audio analysis tasks of universal speech models. It presents an overview of 180 tasks, contributed by the research community and categorized into a a taxonomy, which all have in common that one or multiple audios, as well as a task prompt are presented to a to-be-evaluated model, which then provides a language response, aiming to solve the given task. The response is then evaluated by a post-processing pipeline, potentially including a "judge LLM". Besides providing the evaluation benchmark pipeline, the authors conducted an analysis of current universal (at times specialised) speech models. They conclude that no model excels at all tasks, but strengths and weaknesses can be observed across different models and tasks.

### Strengths
The paper addresses an important point challenging the "universality" claim universal speech models. The authors claim to have gathered the largest benchmark by a large margin, improving on top of presumably their own work and provide a detailed analysis comparing several current speech models. The benchmark has the potential to have a large impact on the research community and it provides useful insights into the limitations of LLMs.

### Weaknesses
L.371: Maybe it is worth that the authors iterate why they didn't choose a more "direct" approach for the evaluation, in which the model is prompted to give a single word based on the fixed set of possible answers. In the case of emotion recognition, it could be "answer with a single word out of the choices 'happy, sad, neutral,...'", which would allow a more direct evaluation. Especially in the case of emotion recognition a non-pre-defined set of emotions will also make it difficult for the judge LLM (and humans for reference) to judge how accurate the result is. This might at least be considered as a second evaluation metric, this seems more or less as what is being done for regression, but why isn't this "extra" step directly asked from the model being evaluated? For sequences evaluation it is stated that the evaluation of unprocessed outputs "guarantees consistency and objectivity".

Section 5.1. It might be difficult to define for some tasks, but a comparison to chance level and/or state-of-the-art task-specific models and/or "perfect" scores would seem a very interesting insight. As is, it seems that the evaluation allows relative comparison between -quite elaborate- models, which allows to see which model is better amongst two, but doesn't really allow to see if the models are still doing reasonably well in these tasks and how much room for improvement there still is. For instance in the case of of spatial audio, none of the models are performing better than the baseline, but it not clear, if none of them or all of them are reasonably good at the task. This is somewhat done in section 5.2. but seems to be missing in 5.1.

### Questions
What is the justification of using Whisper + LLaMA as the baseline? There should be some explanation why this particular architecture has been chosen.

L.267: I think the phrase for distinguishing sources "speech is produced by humans" could be rephrased, as humans could also "produce" other non-speech sounds. Speech should rather be connected to the vocal chords.
L.286: The example of Speech Enhancement to mitigate does not become clear. Above it is stated that the models should produce text as output (which can maybe be interpreted as lists). Under Speech Enhancement for mitigating noise (unless you mean only e..g, SNR estimation) I would expect an audio output.

### Soundness
3

### Presentation
4

### Contribution
3
