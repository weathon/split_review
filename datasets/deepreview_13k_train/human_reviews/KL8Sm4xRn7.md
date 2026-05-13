# Improving Semantic Understanding in Speech Language Models via Brain-tuning

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Speech language models align with human brain responses to natural language to an impressive degree. However, current models rely heavily on low-level speech features, indicating they lack brain-relevant semantics which limits their utility as model organisms of semantic processing in the brain. In this work, we address this limitation by inducing brain-relevant bias directly into the models via fine-tuning with fMRI recordings of people listening to natural stories--a process we name \emph{brain-tuning}. After testing it on 3 different pretrained model families, we show that brain-tuning not only improves overall alignment with new brain recordings in semantic language regions, but also reduces the reliance on low-level speech features for this alignment. Excitingly, we further show that brain-tuning leads to 1) consistent improvements in performance on a range of downstream tasks and 2) a representational space with increased semantic preference. Our results provide converging evidence, for the first time, that incorporating brain signals into the training of language models improves the models’ semantic understanding.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
- In short the main idea is to fine-tune existing speech models so they are better aligned with fMRI recordings and then show that this results in better, more semantic alignment with the brain, and better downstream performance on speech tasks.
- The data comes from fMRI recordings that have been aligned to the podcast audio stimulus. For baselines, the authors run the off-the-shelf models and also fine-tune using fMRI signal unrelated to the task as well as audio representations from another model
- Finally, the authors formalize a notion of low-level feature impact, i.e., how much of the alignment can be attributed to low level (non-semantic) audio features, and show that their brain-tuning results in an alignment that can be explained less by low-level features.

### Strengths
- The fact that brain-tuning yields improvements on automatic speech recognition is very noteworthy. I have some points that need clarification (see below) before I can endorse this conclusion, but if they are addressed, then this will increase my confidence in the significance of this work.
- The motivation for this project is good. This work closes the loop on the large amount of existing work that has shown the emergent alignment between pretrained speech models and the brain. It appears novel in this respect.
- The random fMRI and BigSLM baselines increase my confidence in the fact that the recorded brain activity is a useful target for alignment.

### Weaknesses
 - The conclusion that brain-tuning yields improvements over the off-the-shelf models is incredible, to the degree that I feel I must be misinterpreting the conclusion. There are two things I want to be sure of before this conclusion can be accepted:
  - First, is there any architectural enhancement that the brain-tuned version of wav2vec2 has that the original version does not? Extra projection layers?
  - Second, are the performances of wav2vec2 and HuBERT being fairly represented? It seems puzzling to me that the reported off-the-shelf ASR performances are so low (see questions below). One thing that may be happening: there is a distribution difference between the Librispeech data that wav2vec2 is trained on and the podcast audio used in the experiment. During brain-tuning, the model gets a chance to fine-tune on the podcast audio, or a proxy for that audio (via the brain), and this explains the improved performance. The gold standard experiment for this claim would be to do brain-tuning over one dataset of fMRI-audio pairs, and then show improvement on a completely new set of audio. To this end, it would be good to report the model performance on their original tasks. 
- The fact that brain-tuning does not result in catastrophic forgetting of the original speech model representations is so incredible that I feel I must be missing something. The brain is a very noisy proxy for the audio signal, and using the brain as a target seems to only give very weak incentive to preserve the original speech representations (see questions). As mentioned above, it would be good to report model performance on their original eval datasets (ex. Librispeech) to make sure that any forgetting did not occurr.
- I'm having a hard time following the reasoning behing the low-level feature impact results. If I understand correctly, models were brain-tuned. And then the low-level impact on the brain-tuned models was found to be smaller, compared to the random fMRI baseline. Why should this be the case? Shouldn't we expect the opposite based on the evidence cited on lines 237-238, which suggests that brain-tuning should increase alignment between the brain and the model, and therefore the reliance on low level features?

### Questions
- How is performance on the original speech task preserved even during brain-tuning? Do the authors have an explanation for why no catastrophic forgetting occurs, given that there is no incentive for the base model to retain it's original speech representations during brain-tuning? Is it just because the learning rate is very small? The brain-tuning set is very small?
- The ASR performance of wav2vec2 seems low? The original wav2vec2 paper (https://arxiv.org/pdf/2006.11477) reports accuracies of >0.8 on Librispeech. What explains the difference?
- I'm having a hard time following the reasoning behing the low-level feature impact results. If I understand correctly, models were brain-tuned. And then the low-level impact on the brain-tuned models was found to be smaller, compared to the random fMRI baseline. Why should this be the case? Shouldn't we expect the opposite based on the evidence cited on lines 237-238, which suggests that brain-tuning should increase alignment between the brain and the model, and therefore the reliance on low level features?

## small stuff
- Figure 1c: Are the bar charts supposed to have an x-axis label?
- Line 257: `` gives open quotes in LaTeX

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
4

### Summary
The paper incorporates a new finetuning approach for speech encoder models using neural recordings from subjects listening to stories. The approach uses the fMRI responses as a target during finetuning and modifies transformer layers of the speech. The paper demonstrates three areas of general improvement: (1) better brain alignment, (2) reduced impact of low level features for brain alignment, and (3) improved downstream performance across certain tasks.

### Strengths
* Novelty: The paper isn’t the first to propose brain-tuning (which has been proposed in the vision and language domains) but is the first to apply this approach to speech models which often lack semantic understanding.
* Improvements in downstream performance: Most impressively is the finding that tuning with fMRI leads to strong improvements in ASR. While prior work has shown improvements from incorporating neural signals, I haven’t seen consistent improvements on downstream performance. 
* Reduced impact of low level features in brain alignment: Low level features become less impactful indicating fewer simple audio features are driving alignment to the brain. This is a beneficial and impactful finding. 
* Phonetic-Semantic Split: Following the prior strength, I liked Appendix C which quantified the phonetic-semantic preferences between finetuning and pretrained models.

### Weaknesses
 * Baselines: In general, I think the current baselines are noteworthy but I think there are a few baselines which are missing. 
    * If the goal of the paper is to improve semantic understanding in speech models, the SLM baseline is a bit odd to me. Wouldn’t it be better to use a pretrained language model embedding as a target instead? I would recommend adding this baseline as another way to incorporate semantic information into the model. I also found a model embedding target to be a bit unfair in comparison to fitting voxels since the target is one-dimensional but any target from an embedding model is higher-dimensional according to my understanding, reducing the complexity of the fit.
    * I also think it would be great to include a baseline that controls for particular voxels of fMRI recordings. For example, I was wondering whether the area of the brain had an effect on the outcome of the model.
* Forgetting: One problematic aspect of finetuning is catastrophic forgetting where models can forget currently learned capabilities. I have this concern after seeing the performance decrease in your emotion prediction task. It would be very useful to quantify this point more formally to give a sense of whether semantic information is better incorporated at the sacrifice of basic phonetic understanding. This doesn’t seem to be reflected in appendix C as well. I would appreciate seeing 1-2 low level audio tasks benchmarked as well.
* Neural Signal Details: Some details were missing. See questions.
* (Nit) Consider adding [1] to your related work as another paper that tunes models based on neural information.

### Questions
* What areas of the brain were voxels covering for your fMRI target? Were semantic areas covered or other areas covered?
* My familiarity with fMRI is low by why would you downsampling using a 3-lobed Lanczos filter? Just a bit confused on the need to do so, not anything wrong with the choice.

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
4

### Summary
This paper explores an innovative approach to enhance the semantic alignment of speech language models with the human brain by incorporating brain data. By fine-tuning models using fMRI data of participants listening to natural stories, The goal is to improve the models' semantic understanding by aligning them better with brain regions involved in language comprehension. The authors evaluate the method across three model families (Wav2vec2.0, HuBERT, Whisper) and show improvements in brain alignment, reduced reliance on low-level features, and better performance on downstream tasks that require semantic understanding. This idea is excitingly novel due to its cross-disciplinary implications between neuroscience and AI.

### Strengths
1. **Novelty**: The concept of "brain-tuning" is a novel way to integrate neuroscience data into AI training, bridging the gap between machine learning and brain sciences.
2. **Comprehensive Evaluation**: The evaluation strategy is thorough, with alignment tests, low-level feature analysis, and performance on multiple downstream tasks.
3. **Cross-disciplinary impact**: The paper offers insights valuable to both cognitive neuroscience and AI communities, particularly for understanding semantic processing in the brain and improving language models.
4. **Significant Results**: The results are robust, showing improved alignment with brain regions and downstream task performance, indicating the model's improved semantic capabilities, **but only in their restricted comparison models.**

### Weaknesses
1. **Comparison models are too weak and restrictive for the experiment**: There are **only two** comparison models: BigSLM Fine-tuned and Random-fMRI, the latter is not very valid since using random-fMRI results will definitely deteriorate performance, so there is in fact **only one** valid compasion model BigSLM, which is not convincing at all! BTW, BigSLM sometimes degrade performance as Fig 4, it's not valid as well.  **To prove effectiveness of brain-tuning, the paper should better compare brain-tuning with other valid finetuning models, ont only pretrained models.**
2. fMRI data, in some degree, is too hard to acquire. As the paper mentioned, the largest public dataset of fMRI recordings only cover 8 participants. This will limit the usability of the proposed method, but this won't downgrade my rating for this paper since I think the idea side is novel and useful enough.

### Questions
1. Please provide more detailed explanation why so few comparison models are provided or add more comparison models in the paper. This will dramatically affect my rating, if no reasonable explanation were provided, I would highly question the effectiveness of the method and definitely downgrade my rating.
2. If possible, answer the second weaknesses, this is relatively subtle.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose the concept of brain-tuning in this paper, which aims to augment pretrained speech model training directly with brain recordings. In this way, the authors claim to compensate for the shortcomings of previous methods that only use low-level speech features for brain and speech model alignment, and successfully incorporate speech models with improved brain-relevant semantics. Experiments on three popular pretrained transformer-based speech language model families in three distinct ways (alignment with new brain recordings in semantic regions of the brain, effect of low-level features, such as Tri-Phones and Articulation, on the alignment with these semantic regions, downstream performance on linguistic tasks that require semantic understanding) also highlight the significance of inducing brain-relevant semantics in brain and speech model alignment.

### Strengths
1. This paper first proposes fine-tuning pretrained speech models with brain responses to help improve the alignment between computational models and human brain. The experimental results are also impressive and solid.
2. The authors design several interesting experimental settings and baseline methods to help investigate the influence of brain-tuning.
3. The motivation is clear enough. The paper is also very well written with many experimental details supported.

### Weaknesses
1. Despite the authors effort in illustrating the effect of brain-tuning, the experiments are still insufficient in the following two aspects. (1)  The authors choose LeBel's dataset which only contains 8 subjects for practice. I don't think the conclusion drawn from this dataset is convincing enough given the very few subjects. Instead I suggest trying the Narratives dataset [1] which contains hundreds of subjects in a passive storying hearing task for experiments (by the way this dataset is considered as the largest fMRI dataset in naturalistic language comprehension, not the LeBel's dataset as the authors claimed in line 54), as many previous work [2][3][4] did. Specifically, the limited number of participants in the LeBel dataset raises concerns about the generalizability of the findings. The variability in brain responses across individuals is substantial, and a larger cohort is necessary to establish robust and reliable conclusions. Furthermore, the claim that the LeBel dataset is the largest for naturalistic language comprehension is inaccurate, as the Narratives dataset provides a much larger pool of participants and more diverse data. (2) The authors fail to investigate the influence of model parameters in the brain-tuning process. I think such experiments are easy but important, and should be included in the paper. Specifically, it is unclear how different model sizes and architectures respond to brain-tuning. The authors should explore how the number of parameters affects the alignment with brain data and the resulting downstream task performance. This is crucial for understanding the limitations and potential of the proposed brain-tuning method. 

2. The methods of obtaining four low-level speech features need to be detailed in this paper (at least in Appendix), instead of just citing previous work.

### Questions
1. Why is brain-tuning not effective for whisper? More analysis needs to be conducted. Is it caused by the encoder-decoder architecture?
2. How is the cortical parcellation conducted? The LeBel dataset doesn't provide any standardized space for all the subjects if I remember correctly. Are the fMRI images from different subjects first projected to the same space?

### Soundness
3

### Presentation
4

### Contribution
3
