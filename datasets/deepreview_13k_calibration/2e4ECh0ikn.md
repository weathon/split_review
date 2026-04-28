# Talking Turns: Benchmarking Audio Foundation Models on Turn-Taking Dynamics

- Decision: Accept
- Avg Score: 5.80
- Scores: 8, 6, 3, 6, 6

## Abstract
The recent wave of audio foundation models (FMs) could provide new capabilities for conversational modeling. However, there have been limited efforts to evaluate these audio FMs comprehensively on their ability to have natural and interactive conversations. To engage in meaningful conversation with the end user, we would want the FMs to additionally perform a fluent succession of turns without too much overlapping speech or long stretches of silence. Inspired by this, we ask whether the recently proposed audio FMs can understand, predict, and perform turn-taking events? To answer this, we propose a novel evaluation protocol that can assess spoken dialog system's turn-taking capabilities using a supervised model as a judge that has been trained to predict turn-taking events in human-human conversations. Using this protocol, we present the first comprehensive user study that evaluates existing spoken dialogue systems on their ability to perform turn-taking events and reveal many interesting insights, such as they sometimes do not understand when to speak up, can interrupt too aggressively and rarely backchannel. We further evaluate multiple open-source and proprietary audio FMs accessible through APIs on carefully curated test benchmarks from Switchboard to measure their ability to understand and predict turn-taking events and identify significant room for improvement. We will open source our evaluation platform to promote the development of advanced conversational AI systems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a new evaluation protocol to assess the spoken dialog system's turn-taking capabilities, i.e., the Moshi and Cascaded model. They use a supervised model as a judge which is trained to predict turn-tasking events in human-human conversation (i.e., Switchboard). The paper presents a comprehensive user study that evaluates the Moshi and Casaded model on their ability to perform turn-taking events, and it finds that they sometimes do not understand when to speak up, can interrupt too aggressively, and rarely backchannel. The main contributions are:
1. A new evaluation protocol to assess the spoken dialog system's turn-taking capabilities.
2. Some insight about existing spoken dialogue systems through user study.
3. Additionally create a test benchmark using Switchboard dataset to evaluate SALMONN, Qwen2-audio-instruct, Qwen-audiochat, Whisper+GPT-4o on their ability to understand and predict turn-taking events.

### Strengths
1. The originality of the work is commendable. The authors propose a novel evaluation protocol to assess the turn-taking capabilities of spoken dialog systems.
2. The paper is well-written and provides sufficient experimental details in the Appendix.
3. The authors plan to open source the evaluation platform.

### Weaknesses
1. The evaluation protocol is highly expensive, as it requires a supervised dataset to train the judge model. This approach is not feasible if we lack a supervised dataset in other languages, such as Chinese.
2. The filler word set for backchannel detection is heuristic and may miss some backchannel cases that are not included in the filler word set.

### Questions
1. The Fisher dataset is a common dataset comparable to Switchboard. What is the performance of the supervised turn-taking prediction model on this dataset?
2. How can your evaluation protocol be adapted or applied in scenarios where supervised datasets are not available for other languages, such as Chinese?

### Soundness
3

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
3

### Summary
This paper addresses the challenges of evaluating the turn-taking capabilities of audio foundation models (FMs) in conversational settings.
It defines 6 types of Turn-Taking Events and evaluates the performance of end-to-end speech dialogue models as well as cascaded systems.
Through the results obtained from this study, the authors discovered numerous issues with existing AI dialogue systems in handling turn-taking, such as sometimes failing to intervene in conversations at appropriate times or excessively interrupting others. Furthermore, the authors conducted tests on multiple open-source and closed-source audio foundation models, revealing their limitations in understanding and predicting turn-taking events, and highlighting areas for improvement.

### Strengths
1. The definition of turn-taking is detailed and clear.

2. The evaluation protocol proposed in this paper contributes to better assessing the performance of audio foundation models in dialogues, providing strong support for the development of voice dialogue systems.

3. This paper reveals many issues existing in current AI dialogue systems when handling turn-taking, offering valuable references for future research.

### Weaknesses
1. This study only tested a few open-source and closed-source audio FM models.

2. There is a lack of comprehensive performance evaluation and summary.

### Questions
NA.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes an evaluation protocol to measure the turn-taking capabilities of audio foundation models.

### Strengths
The strengths of this paper are as follows:
 1. This paper provides an automated turn-taking protocol for audio foundation models
 2. The evaluation platform will be open-sourced.

### Weaknesses
The weaknesses of this paper are as follows:
 1. The study aims to measure precise turn-taking, but the thresholds are set to arbitrary values.
 2. The participants introduced in Sec 3 seem biased, consisting of the authors and related individuals.
 3. The confidence in some evaluations (Fig. 3(b), (e)) appears high, but no explanation is provided.

### Questions
Here are questions for the authors:
 - The thresholds in Sec. 4.4-4.8 seem arbitrary. Is there a specific reason for choosing these values? All units appear to represent likelihoods, yet they range from negative ($threshold_3$ = -0.45) to positive values ($threshold_2$ = 0.1).
 - There are concerns about the reliability of the judge model. Since all results are based on comparisons with this model, is there concrete evidence supporting its credibility? Specifically, the conclusion that Moshi[1] is "too aggressive" lacks persuasiveness if it relies solely on comparisons with the judge model.

[1] Defossez et al. Moshi: a speech-text foundation model for real-time dialogue

### Soundness
2

### Presentation
2

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
The paper presents an evaluation protocol designed to assess the turn-taking capabilities of spoken dialogue systems. It evaluates the exact timing of these events using a supervised model trained to predict them. The experimental results reveal interesting insights about existing spoken dialogue systems and offer valuable suggestions for their future development.

### Strengths
1. This paper proposes a comprehensive evaluation protocol and well-designed metrics to assess the turn-taking capabilities of spoken dialogue systems. The evaluation framework and metrics are thoughtfully developed and provide valuable insights.
2. The paper extends the evaluation of turn-taking capabilities of spoken dialogue systems from corpus-level statistics to a more granular assessment of the timing of turn-taking events. This fine-grained approach enables a more accurate reflection of a spoken dialogue system’s turn-taking capabilities.
3. The proposed evaluation metrics provide insights into the limitations of current systems in achieving interactive and natural conversations, highlighting areas for potential improvement.

### Weaknesses
1. In Metric (E), the judge labels show low consistency with human relevance judgments, indicating that this metric may have limited reliability in assessing the model's ability to handle user interruptions effectively.
2. My primary concern is the relatively low agreement between the majority of judge labels and human judgments, with most falling below 80%. This raises questions about the strength of the claim that the proposed metrics maintain high consistency with human decisions. The lack of clarity on how the judge labels were obtained and validated further exacerbates this concern. Specifically, it is unclear what training data was used for the judge model, what its architecture is, and how its performance was evaluated beyond the reported consistency with human judgments. This lack of transparency makes it difficult to assess the reliability of the judge model and, consequently, the validity of the evaluation protocol.
3. GPT-4o was not evaluated.

### Questions
My questions are listed above.

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel evaluation framework for assessing turn-taking capabilities in audio foundation models (FMs). The authors first propose metrics for five core conversational abilities: determining when to speak up, backchannel, interrupt, convey turn-taking cues, and handle interruptions. They develop a supervised model trained on human-human conversations to serve as a judge for evaluating these turn-taking events. Using this framework, they conducted a user study with different spoken dialogue systems (full-duplex E2E spoken dialogue system Moshi and VAD-based cascade dialogue system) and evaluated them. They evaluate several open-source and proprietary audio FMs on their ability to understand and predict turn-taking events.

### Strengths
1. The evaluation protocol is novel and well-motivated.
2. The experimental analysis provides valuable insights into turn-taking capabilities of audio foundation models (FMs).
3. The user study reveals noteworthy observations about current spoken dialogue systems.

### Weaknesses
1. Turn-taking prediction models used in evaluation protocol require training, which limits scalability and applicability. 
2. The paper does not thoroughly address how its proposed evaluation protocol compares with previous turn-taking approaches, such as Ekstedt and Skantze (2022).

### Questions
1. What is the main difference between the proposed evaluation protocol and the previous approach by Ekstedt and Skantze (2022)? Is it impractical to apply the metrics from prior turn-taking evaluation methods to audio FMs?
2. While the turn-taking prediction model has been evaluated on an out-of-domain task-oriented spoken dialogue corpus, could you evaluate it on additional non-task-oriented spoken dialogue datasets to assess the generalizability of the model?

### Soundness
3

### Presentation
3

### Contribution
3
