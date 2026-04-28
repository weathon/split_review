# Universal Sleep Decoder: Aligning awake and sleep neural representation across subjects

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6

## Abstract
Decoding memory content from brain activity during sleep has long been a goal in neuroscience. While spontaneous reactivation of memories during sleep in rodents is known to support memory consolidation and offline learning, capturing memory replay in humans is challenging due to the absence of well-annotated sleep datasets and the substantial differences in neural patterns between wakefulness and sleep.
To address these challenges, we designed a novel cognitive neuroscience experiment and collected a comprehensive, well-annotated electroencephalography (EEG) dataset from 52 subjects during both wakefulness and sleep. Leveraging this benchmark dataset, we developed the Universal Sleep Decoder (USD) to align neural representations between wakefulness and sleep across subjects. Our model achieves up to 16.6% top-1 zero-shot accuracy on unseen subjects, comparable to decoding performances using individual sleep data. Furthermore, fine-tuning USD on test subjects enhances decoding accuracy to 25.9% top-1 accuracy, a substantial improvement over the baseline chance of 6.7%.
Model comparison and ablation analyses reveal that our design choices, including the use of (i) an additional contrastive objective to integrate awake and sleep neural signals and (i) the pretrain-finetune paradigm to incorporate different subjects, significantly contribute to these performances. Collectively, our findings and methodologies represent a significant advancement in the field of sleep decoding.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces an approach for decoding memory content from brain activity during sleep. To be more specific, the authors show an experimental setup to extract memory reactivation during NREM sleep, along with the ground truth timing and content during the neural replay episode. Using the dataset from 52 subjects, they train a model capable of generalizing across subjects in a zero-shot manner.

### Strengths
The data collected for the paper could be useful for researchers in biosignals/sleep community.

### Weaknesses
 - The data is not released. Without the data it's difficult to verify the claims, since one of the main claims of the paper seems to be the unique data collected. Since this appears to be a dataset paper, it is essential that the data is released and verified before this can be accepted.
- There is no comparison with other works. Without the dataset, this paper does not contribute much else.
- With such low accuracy as shown in Figure 3, the efficacy of the method is put into doubt.
- What are the asterisks in Figure 3?
- Even if the data is released, other venues (more focused on health/physiological signals) would be suitable for this paper.

### Questions
Please address the weaknesses.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper reports on a novel EEG dataset with both sleeping and awake participants designed for memory reactivation decoding during sleep. In addition, it provides a comprehensive set of competitive baselines and ablations on this data demonstrating within-participant and cross-participant generalization.

### Strengths
The paper is clearly written, and the contributions are clearly detailed and (mostly) well supported. Furthermore the paper promises to release a novel dataset (in the supplementary material) and provides clean and reasonably well-annotated code for its contributions. The set of experiments is comprehensive.

### Weaknesses
My primary concern in reading the paper is that a core contribution regarding the relative performance of the various models is not supported as well as it could be. In particular, I think we should expect something like performance on awake+sleep+contrastive > awake+sleep > [awake or sleep in whatever order]. This data is all available in plots (Fig 3) but from just eyeballing those plots it's hard to tell whether the sleep->sleep CNN is better or worse than the awake+sleep->sleep CNN, for example. These should ideally be on the same plot. Similarly sections 4.2.2 and 4.2.3 report some statistics but no comparison to support the core claim above, and there's no results table for these experiments either, unless I have missed something. 

Separately, I have some notation concerns: 
* Is it really that $y \in \mathbb{R}^K$, i.e. each label is a vector of real numbers the length of the number of classes? I would think it's $y \in \{1 \ldots K\}$ or similar. 
* The $\mathcal{X}$s aren't explicitly defined. 
* If $\mathcal{P}(i) = \{k|k\in \mathcal{A}(i), y_k = y_i\}$ and $\mathcal{A}(i)$ is a set of instances $\{x_i, y_i\}$ then $k$ is such an instance and $y_k$ seems overloaded or poorly defined. 

These are just the ones I immediately caught -- another careful proofread of the math might be useful. 

Finally, some more unordered comments: 
* I think describing a dataset as "open set" is a bit odd (section 2.2) -- a dataset has a fixed number of classes, i.e. it is "closed set". In my understanding "open set" is a notion w.r.t models / tasks rather than datasets (i.e. ability to classify unseen classes, often by composition of seen classes, the use of a language model, or something else). 
* Kostas et al. 2021 (doi:10.3389/fnhum.2021.653659) is likely worth mentioning in discussion of larger-scale SSL pretraining for EEG. 
* I found Figure 2 more confusing than illustrative -- the caption is doing a lot of explanation and I'm not sure how much the figure adds. For example, the arrows and colors are not used consistently -- it's not obvious what the arrow colors mean, and the arrows seem to indicate data flow in the top part of the figure and an ordering of experiments in the bottom part.

### Questions
* The two plots in Figure 4 have the same y axis (which should facilitate comparison) but if I understand things correctly, the x axes indicate percentages of different amounts of data (even though each batch is balanced). Is that right? If so, maybe this plot's x axis should be the number of instances / hours etc to facilitate direct comparison. 
* The paper takes care to describe its paradigm as "TMR related" instead of "TMR evoked" because the paradigm is different from TMR -- how is it different?

### Soundness
2 fair

### Presentation
4 excellent

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
The authors present a dataset and a deep learning pipeline to decode evoked semantic categories during sleep. They collect a dataset of 64-channel EEG recorded while participants (n=52) were exposed to image and sound stimuli from 15 semantic categories while awake. Following this, participants were re-exposed to a subset of the previous sound stimuli while they were in N2/3 sleep. Deep learning pipelines based on CNNs or Transformers and combining a classification objective and a domain (i.e. awake-image, awake-sound, sleep-sound) adaptation objective were then trained to predict the category of a presented stimulus from the corresponding EEG. Different training and evaluation settings are investigated. Results suggest semantic categories can be decoded significantly above chance performance even during NREM sleep.

### Strengths
Originality: The proposed dataset, research question and decoding approach (combining classification and contrastive objectives for domain adaptation) appear to be novel.

Quality: The paper is of overall good quality and presents a complete picture of the research question, data and deep learning pipeline.

Clarity: The paper is overall clear, with the different components of the study and results exposed and mostly clearly described. See Weaknesses for proposed clarifications.

Significance: The study appears like an important step towards the understanding and improvement of semantic decoding during sleep. Along with the dataset (when released) this has the potential to effectively become a baseline framework for studying semantic decoding during sleep.

### Weaknesses
A core claim of the paper is that the experimental paradigm allows probing memory reactivation during sleep. However, I am not convinced the presented analyses actually allow studying memory reactivation. Rather, the trained neural encoders likely picked up on evoked activity related to the audio stimuli presented during sleep. First, the EEG recordings were epoched from -0.2 to 0.8 s around the stimulus onset (Section 4.1). The paper does not describe the distribution of audio stimuli duration, but it is likely that the audio clips lasted a few hundreds of milliseconds. In that case, the EEG windows likely contained evoked responses to these auditory stimuli rather than an associated memory. To assess that, an analysis of the evoked response that also takes into account the spatial dimension would be important (see Q1). On a related note, details of how auditory cues impacted sleep would be important to provide (Q2).
Second, I believe the data that was collected during sleep could be used to clarify this point. What kind of decoding performance can be achieved when only looking at auditory cues of mismatched pairs? If semantic category classification performance remains high for cues for which the evoked response should be different from the “memory-evoked” response (i.e. mismatched pairs), this could support the authors’ claim (see Q3).  It is unclear if the presented image-audio pairs were consistently matched or mismatched, and the number of unique stimuli used is not explicitly stated. The paper mentions 600 image-audio pairs, but it is not clear if these are 600 unique images and 600 unique audio clips, or if there are only a few unique stimuli that are repeated multiple times. If the number of unique stimuli is low, the results might be limited to instance-level classification, rather than supporting generalization across categories.
Finally, to further support the claim that the paradigm tests memory reactivation, an analysis of the behavioral responses during the post-sleep session for presented vs. non-presented stimuli could be carried out. A significant increase in performance for stimuli presented during sleep could support the effect of the TMR-like protocol.
Overall, I believe these questions should be answered for the memory-related claims to be kept in the manuscript.

The description of the models in the Appendix is a bit confusing (see Q4). Summarizing the entire architecture (i.e. including more than just the Conv layers in the table) would be helpful. Also, a single description of the “Subject block” might be clearer (instead of having two separate tables that appear to contain the same information).

### Questions
1. What do the evoked responses look like? It would be important to provide descriptive analyses of the time-locked response to images, auditory cues and auditory cues during N2/3 to confirm the validity of the collected data. Importantly, do time-locked responses during sleep follow a different temporal pattern that maybe spans a longer window (as memory reactivation might happen after the stimulus presentation)? Moreover, considering the spatial dimension of the evoked response (i.e. how it is distributed across the different EEG channels, e.g. with topomaps) might help confirm the responses collected during sleep are actually closer to (awake) auditory or visual responses.

2. Is there a chance the audio cues during N2/3 woke up the participants? Showing examples and/or a summary of sleep staging (e.g. hypnograms showing how N2/3 stages were not interrupted by the cues) would be useful.

3. How does decoding performance during sleep differ for auditory cues coming from matched vs. mismatched pairs? My understanding from Section A2 is that the sleep auditory cues were randomly selected from the whole audio set, meaning there should be examples from both matched and mismatched pairs available. A supplementary figure like Figure 3 could then be used to report the results for both categories. If performance remains as high for auditory cues of mismatched pairs, then the “memory-replay” hypothesis might be validated.

4. In Section 2.3: “Since there are fewer publicly available EEG recordings during sleep compared to those during wakefulness, applying unsupervised pretraining methods for sleep decoding is not feasible.” I believe that is not true, as there are a lot of openly available sleep datasets (SHHS, MASS, SleepEDF, Physionet Challenge 2018, etc.). My understanding is the limiting factor might be the spatial coverage for those datasets though, which often include a few channels only whereas the presented dataset contains 64 channels.

5. What is the impact of the hyperparameter $\lambda$ in Equation 2, and how was the value of 0.5 selected in Section 4.2.3?

6. The performance of the Lasso GLM is about the same as the neural decoders in Figure 3c. How does the Lasso GLM fare in the Awake+Sleep → Sleep setting (Figure 3d)?

7. In Section 4.2.1: “We take the test accuracy according to the maximum validation accuracy as its performance.” I am not sure I understand what this means.

8. Use of the word “migration” (e.g. Section 4.2.2): maybe “transfer” would be clearer and more connected with the literature?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
