# SQS: Speech Quality Assessment in the Data Annotation Context

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3

## Abstract
Audio quality plays a crucial role in the data annotation process as it influences various factors that could significantly impact the annotation results. These factors include transcription speed, annotation confidence, and the number of audio replays, among others. Consequently, transcriptions often contain numerous errors and may have blank or incomprehensible sections. Most existing objective measures (e.g., Perceptual Evaluation Score Quality (PESQ), Speech Intelligibility Index (SII)) and subjective measures (e.g., Mean Opinion Score (MOS)), and speech quality measures (e.g., Word Error Rate (WER)) do not consider factors that could hinder the annotation process. These measures poorly correlate with the audio quality perceived by the annotator in the annotation context. We propose a novel subjective speech quality measure within the audio annotation framework, called Speech Quality Score (SQS). This measure encompasses the most relevant characteristics that can impact transcription performance and, consequently, annotation quality. Additionally, we propose a DNN-based model to predict the SQS measure. Our experiments were conducted on a dataset composed of 1,020 audio samples with SQS annotations created specifically for this study, using the RTVE2020 Database. The results demonstrate that our proposed model achieved a high performance with a linear correlation coefficient of 0.8 between ground-truth and predicted SQS values. In contrast, state-of-the-art MOS prediction models exhibited a poor correlation (i.e., 0.2) with ground-truth SQS values.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a novel subjective speech quality measure, known as Speech Quality Score (SQS), within the audio data annotation framework. It argues that existing objective and subjective measures do not effectively consider factors that may affect the annotation process, leading to poor correlation with the audio quality perceived by the annotator. The proposed SQS measure takes into account the most relevant characteristics impacting transcription performance and, thus, annotation quality. Additionally, the authors propose a Deep Neural Network (DNN)-based model to predict the SQS measure. The experiments conducted on a dataset of 1,020 audio samples with SQS annotations show promising results.

### Strengths
- The paper addresses an important (and open) issue in the field of audio data annotation, highlighting the need for a more effective measure of audio quality.
- Introducing the SQS measure is innovative, considering factors directly impacting transcription performance and annotation quality.
- The use of a DNN-based model for predicting SQS metrics demonstrates a strong correlation between ground-truth and predicted SQS values, indicating the reliability of the proposed model.

### Weaknesses
 - The paper could have expanded on the specific characteristics encompassed by the SQS measure to provide a more comprehensive understanding of its composition.
- The research relies heavily on the RTVE2020 Database for experimentation. The results might be limited and may not generalize well to other databases or real-world scenarios. For e.g., the paper does not speak much about the data collection framework setting (whether clean references provided, quality of those clean references, raters qualifications, what type of questions asked...)
- An idea of how noisy the recordings were (e.g., using a spectrogram) would have conveyed the point on how inherently noisy the recordings were (based on Fig 4(a), looks like most NISQA scores are below 3ish, so that says about the relationship b/w intelligibility and quality esp for low quality scenarios.
- The basic premise of the paper is SQS and the NISQA-based model can improve speech annotation (see Figure 1), but this was never done. That is, SQS and the NISQA-based model have not been shown to have any end-to-end utility.
- In addition, it isn't clear SQS is even needed. Why not just do speech enhancement for all speech clips, or play both speech enhanced and originals to the annotators?
- Minor issues: Some references have errors, e.g., ITUT Rec. Itu-t rec. p. 800.1 => ITU-T Rec. P.800.1 pesq => PESQ Dnsmos => DNSMOS

### Questions
- How can the SQS measure be validated against other subjective measures like MOS (or is MOS even the right framework for this)?
- What are the specific characteristics considered by SQS that make it more effective than existing measures? (Some ablations on combining WER and NISQA to build this hybrid metric compared to SQS might have been useful)
- Can the proposed model generalize well to other datasets or real-world scenarios?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper creates a new subjective test (Speech Quality Score, SQS) for annotating speech clips. SQS is shown to correlate moderately with annotation time (r=0.38) and it is suggested to use the SQS value to determine whether to apply a speech enhancement method before transcription or not. NISQA is fine-tuned with a SQS dataset and shown to have good performance (r=0.86).

### Strengths
This is a novel idea that could help improve speech annotation, which is a challenging problem. 
The results of the NISQA-based model are good.

### Weaknesses
The clarity of the paper is hindered by the use of common technical terms in non-standard ways. For example, there is a frequent conflation between speech quality and speech intelligibility. The name of the proposed metric is the Speech Quality Score, although it predicts intelligibility (how easy it will be to transcribe for a human listener). While these are often related, they are not always, despite the first sentence's unsupported claim ("Speech intelligibility is directly associated with audio quality"). Similarly, MOS (Mean Opinion Score) is described as a metric even though it is merely a scale upon which many different metrics are measured (speech quality, noise suppression, overall quality, etc). Word error rate is mentioned as a measure of speech quality, but it is explicitly a measure of intelligibility. Furthermore its use in this paper is to compare one human transcription against a consensus human transcription, but this is not explained until page 5 after being mentioned several times.

The relevance of the paper to ICLR is not clear. It is a paper about speech intelligibility prediction and while of interest to the speech community, I don't think is general enough in terms of machine learning approaches or applicability to warrant publication at ICLR, which focuses on machine learning.

The reproducibility of the results is quite low without the release of either the dataset or the model. This is a new task with guidelines that could be interpreted differently from different readings of the paper, so without some aspect of the work being released, it is not clear exactly what a reader of the paper is meant to take away from it. I don't think the fact that it is possible to perform this general task is sufficiently interesting to warrant publication on its own.

It is not clear why this subjective measure of "Speech Quality Score" is necessary as opposed to a more objective measure like the actual time that it took to annotate a given utterance or the inter-rater (dis)agreement. No justification is provided, nor is any quantitative evaluation undertaken. Such an objective score would need to account for differences in utterance duration and different overall speeds between raters, so could normalize within each rater and by utterance duration. It seems that even without these normalizations, SQS is still correlated with annotation time (r=0.38). Presumably with them it would be even more correlated.

### Questions
What is a Sigma's proprietary tool (Section 2.1)? Add a reference
Why does Table 1 not have 5: Excellent? 
Why are only N=2 ratings done for the dataset in 2.1? That makes your training data fairly noisy.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper describes experiments to predict a new rating of the difficulty with which a speech utterance can be transcribed directly from the audio. It uses an in-house 1000-utterance dataset with this new annotation. The new annotation is correlated with NISQA predictions, DNSMOS predictions, accuracy of a single human transcriber compared to an exhaustive human transcription panel, and speed of annotating an utterance. The NISQA model can be fine tuned to predict this annotation to achieve r = 86% correlation with the ground truth.

### Strengths
This is an interesting application: triaging utterances for transcription by annotators of different skill level.

This seems like a well defined task that can be solved accurately with fine tuning of an existing model.

The paper is relatively easy to follow.

### Weaknesses
1) The presentation is not very clear, I’m not sure what is the main difference between the proposed Speech Quality Score (SQS) and the common MOS.
2) The novelty of this paper is very limited. In fact, there is no novelty in terms of the machine learning perspective. This paper is more suitable to be submitted to speech-related conferences (e.g., Interspeech, Icassp, etc.). Specifically, this work simply employs a pre-trained speech quality estimator (NISQA) and finetunes on its own dataset.
3) The comparison to other models (e.g., NISQA, DNSMOS) is also unfair, because of different training data and the label scale. In DNSMOS, the MOS scale is from 1 to 5, however, in the collected dataset, the label scale is from 1 to 4. Although it may be okay for Pearson correlation, metrics such as Mean Square Error (MSE) will be significantly affected by this scale mismatch.

### Questions
Results are only provided in the paper for fine tuning the pretrained NISQA model. What are the results of training the model from scratch to predict SQS?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on studying the factors that may affect data annotation for audio signals. A small-scale dataset is collected (1,020 audio samples, each audio sample has a duration of 10 seconds). Then a quality estimation model is trained by transfer learning and the collected data.

### Strengths
The finding between transcription time and SQS, WER is interesting.

### Weaknesses
1) The presentation is not very clear, I’m not sure what is the main difference between the proposed Speech Quality Score (SQS) and the common MOS.
2) The novelty of this paper is very limited. In fact, there is no novelty in terms of the machine learning perspective. This paper is more suitable to be submitted to speech-related conferences (e.g., Interspeech, Icassp, etc.). Specifically, this work simply employs a pre-trained speech quality estimator (NISQA) and finetunes on its own dataset.
3) The comparison to other models (e.g., NISQA, DNSMOS) is also unfair, because of different training data and the label scale. In DNSMOS, the MOS scale is from 1 to 5, however, in the collected dataset, the label scale is from 1 to 4. Although it may be okay for Pearson correlation, metrics such as Mean Square Error (MSE) will be significantly affected by this scale mismatch.

### Questions
Although each audio sample is 10 seconds, do they contain the same number of words? I believe it will also affect the transcription time.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
