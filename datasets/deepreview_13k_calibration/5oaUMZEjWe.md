# Unifying Diarization, Separation, and ASR with Multi-Speaker Encoder

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5

## Abstract
The rapid progress of single-task architectures has dominated recent developments in multi-talker speech processing, prompting the need for unified approaches. This paper introduces a unified multi-speaker encoder (UME), a novel model architecture that jointly learns representations for diarization, separation, and multi-speaker automatic speech recognition (ASR) tasks using a shared pre-trained foundational speech encoder. We leverage the hidden representations from multiple layers of UME to effectively use information from different semantic levels, contributing to bottom-up alignment between tasks. This joint training approach captures the inherent interdependencies among the tasks, enhancing overall performance on overlapping speech data. Our evaluations demonstrate that UME achieves substantial improvements over the single-task state-of-the-art (SOTA) baselines dedicated to speaker diarization, speech separation, and multi-speaker ASR. Notably, for speaker diarization, UME achieved SOTA performance by lowering the diarization error rate (DER) from 3.24 to 2.19 on the Libri2Mix dataset. Furthermore, our results in multi-speaker ASR outperform the previous results, reducing the concatenated minimum-permutation word error rate (cpWER) from 11.9 to 9.2 on the LibriSpeech2Mix evaluation set.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors introduce a method to concurrently train models for speech recognition, speech separation, and speaker diarization, utilizing embeddings from a pre-trained speech foundation model (SFM). They leverage a weighted sum of the model’s layer embeddings as input for each task. Experimental results indicate that this joint training approach enhances the performance of all three tasks.

### Strengths
The paper introduces a unified architecture that tackles Speech Separation, Speaker Diarization, and ASR tasks simultaneously. Experimental results confirm that this multitask framework enhances the performance of each task, demonstrating their mutual benefit.

### Weaknesses
As noted by the authors, previous works have utilized SFMs like WavLM for SS and ASR tasks. Although the proposed extension to cover all three tasks shows metric improvements compared to other SFMs, the innovation is minimal.

Additionally, the authors have only tested their approach on a simulated dataset. A more comprehensive evaluation using datasets like AMI, ICSI, or LibriCSS would better validate their method.

### Questions
1. Clarification on Figure 1:
Figure 1 appears misleading. Equation (3) shows different weights for different tasks, yet Figure 1 depicts only a single weight. Can you clarify this discrepancy?


2. Training with Real Data:
How do you propose to use real data for training the model, given that datasets for these tasks (e.g., ASR and speech separation) are typically disjoint? For example datasets for ASR do not generally contain ground truth for speech separation. How will this disjoint nature impact the joint training of the model?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This work proposes a method where one speech foundation model is used as backbone to three task-specific heads. Unlike the standard SUPERB protocol, these heads are trained in a multi-task setup to perform speaker diarization, speech separation, and multi-speaker speech recognition.

### Strengths
This work tackles the inherently difficult problem of solving different, orthogonal speech technology tasks. A real-world ASR system needs to solve these, and currently this is done with a pipeline approach of multiple models. Unifying this pipeline of speech separation, speaker diarization, speech recognition, etc into a single model is beneficial to the community.

### Weaknesses
I do not believe this work uses a fair evaluation protocol, as it is stated in Section 4.1 that the the speaker diarization test set uses 100% overlapped speech. From my understanding of DER, this means that the model needs to simply predict that each of the 2 speakers are talking all the time. The low but not perfect scores in Table 1 are then simply due to noise in the ground-truth labels?

The paper is well-structured, but there are some sentences which are not clear or contain typos. See e.g., 
* line 37-38 "A key limitation of training tasks independently is that inter-dependencies cannot be leveraged"
* line 40 "Most existing speech-processing frameworks address this limitation with unified, joint training architectures" (also, 'unified, joint training architecture' is vague)
* line 48: delete " so much", add, e.g., "do not work well on"
* line 154 "gorund truth" 
* line 156 "where a T-length..."
* line 298 "metrics" -> "metric"
* line 367 "Unlike WavLM ... outperforms WavLM" This sentence is hard to parse, split it up, e.g.: "WavLM uses overlapped speech mixtures, while OWSM is just trained on clean speech. We observe that... OWSM > WAVLM"
* line 369 "We explain" -> "We speculate" or "We hypothesize" 

I believe reproduction of this work is difficult due to missing details on dataset generation and model training, see my questions below.

### Questions
* Can the authors comment on the use of 100% overlapped speech for evaluation of SD? Does the SUPERB benchmark for SD also use 100% overlapped speech?
* What model type was used for OWSMv3.1(base, small, medium , LR)? From Figure 3 I assume medium, but I do not think the text states this anywhere.
* What does a "flat start" mean in line 342?
* For how many epochs/steps did you train in total?
* How much VRAM is needed to train your model, which GPU(s) did you use, and how long did it take to train?
* What batch size did you use, and how were these sampled? 
* What is the minimum, maximum, and average duration of utterances in your train/eval dataset(s)?
* I think it is unexpected (From Figure 3 and Figure 4) that the weights are nearly identical between task heads. Do the authors know what weights are found when training in a single-task setup, and whether they are similar or different to the values displayed in these figures?

### Soundness
1

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors proposed a "Unified Multi-Speaker Encoder (UME)" for tasks such as speech separation, speech diarization, and multi-speaker ASR. Specifically, the UME employs a pre-trained OWSM encoder and is jointly fine-tuned across all three tasks. The latent embeddings from multiple layers of the UME are combined using a weighted sum with learnable coefficients. However, the novelty of this approach is limited, and its performance is not as good as that of state-of-the-art methods

### Strengths
This manuscript attempts to construct a unified encoder for speech-related tasks in multi-talker scenarios. This research question is necessary and important.

### Weaknesses
 - The manuscript lacks novelty. Numerous works have already discussed the use of multi-layer feature fusion/weighted sum, such as "Large-Scale Self-Supervised Speech Representation Learning for Automatic Speaker Verification," "Whisper-AT: Noise-Robust Automatic Speech Recognizers are Also Strong General Audio Event Taggers," and "Resource-Efficient Transfer Learning from Speech Foundation Model Using Hierarchical Feature Fusion." Compared to the aforementioned studies, this manuscript makes no novel contributions to methodology. Instead, it leverages existing techniques to address three speech-related tasks in multi-speaker scenarios.

- The authors overclaimed achieving state-of-the-art performance in speaker diarization, speech separation, and multi-speaker ASR.
  - However, for speech diarization, they only compared their method with ConvTasNet (2019) and did not benchmark against more recent methods such as Mossformer or Mossformer2.
  - For multi-speaker ASR, the proposed method achieved a WER of 9.2% on LibriSpeechMix. In contrast, the state-of-the-art performance is 3.43%, as reported in "Empowering Whisper as a Joint Multi-Talker and Target-Talker Speech Recognition System."
  - For speaker diarization, the authors only compared their method with EEND-based methods. The performance of their UME when combined with non-E2E method is not explored. 

- The author reported the model's performance solely on two-speaker simulated overlapped speech for all three tasks. The performance in real-world scenarios and with more speakers remains under investigation.

### Questions
1. Can you explain the novelty of your approach compared to existing multi-layer weighted sum methods, aside from fine-tuning the model on the three multi-speaker-related tasks?
2. Why did you not compare your method with the latest research?
3. Why did you not report the results from other papers that demonstrate better performance?
4. It would be beneficial to discuss the performance on a broader range of datasets, rather than limiting the evaluation to only two-speaker LibriMix and LibriSpeechMix.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a method of combining diarization, separation and ASR tasks with multi-layer feature learning in a unifed model. Experiments have been conducted to evaluate the effectiveness of the proposed method.

### Strengths
The paper is written clearly and easy to follow.

### Weaknesses
1) The novelty is limited. As introduced in Section 2, multi-layer feature learning and joint training of speech tasks have been investigated in plenty of previous studies. The main contribution of this paper is to include more speech tasks into joint training and to combine it with multi-layer feature learning, which is limited in my opinion. Specifically, the paper does not sufficiently demonstrate a novel architectural component or training strategy that significantly advances the state-of-the-art beyond simply adding more tasks. The core idea of using a weighted sum of features from different layers is not new, and the paper lacks a detailed analysis of why this specific combination of tasks and layers is particularly effective compared to other possible combinations.
2) As showin in experimental results, the task weights for joint training in Eq.(16) play an important role in model performance. Thus, how to optimize these weights should be carefully explained. The paper mentions using equal weights, but it does not explore or justify this choice adequately. It is unclear if this is the optimal strategy or if other weighting schemes could lead to better performance. The lack of a systematic exploration of different weighting strategies is a significant weakness.

### Questions
According to the results shown in Table 3 and 4, the layer weights for the three tasks were quite similar in both joint training configurations. Therefore, it may not be necessary to use task-dependent layer weights. How about the performance of using unifed layer weights across different tasks?

### Soundness
2

### Presentation
2

### Contribution
2
