# Enhancing Zero-shot Text-to-Speech Synthesis with Human Feedback

- Decision: Reject
- Scores: 8, 3, 6, 5

## Abstract
In recent years, text-to-speech (TTS) technology has witnessed impressive advancements, particularly with large-scale training datasets, showcasing human-level speech quality and impressive zero-shot capabilities on unseen speakers. 
However, despite human subjective evaluations, such as the mean opinion score (MOS), remaining the gold standard for assessing the quality of synthetic speech, even state-of-the-art TTS approaches have kept human feedback isolated from training that resulted in mismatched training objectives and evaluation metrics. 
In this work, we investigate a novel topic of integrating subjective human evaluation into the TTS training loop. 
Inspired by the recent success of reinforcement learning from human feedback, we propose a comprehensive \textit{sampling-annotating-learning} framework tailored to TTS optimization, namely \textbf{un}certainty-aware \textbf{o}ptimization (UNO). Specifically, UNO eliminates the need for a reward model or preference data by directly maximizing the utility of speech generations while considering the uncertainty that lies in the inherent variability in subjective human speech perception and evaluations. Experimental results of both subjective and objective evaluations demonstrate that UNO considerably improves the zero-shot performance of TTS models in terms of MOS, word error rate, and speaker similarity. Additionally, we present a remarkable ability of UNO that it can adapt to the desired speaking style in emotional TTS seamlessly and flexibly.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel optimization framework, UNO, designed for zero-shot TTS systems, which integrates human feedback with the original TTS objectives. The proposed method enhances a TTS model through a three-step process:
1. Generating hundreds of samples using diverse speech prompts.
2. Annotating these samples with binary labels (like or dislike) based on feedback from real human raters or simulated by neural networks.
3. Training the TTS model using a combination of the original TTS objective and the (pseudo-)human feedback objective.
To account for the uncertainty and confidence associated with pseudo-human feedback, the framework incorporates an uncertainty-aware optimization strategy. This approach encourages the model to update more aggressively when presented with low-uncertainty samples and more conservatively with high-uncertainty ones.

In contrast to previous methods like DPO, UNO eliminates the need for paired good/bad samples, simplifying the sample generation process outlined in step 1. Experimental results demonstrate that UNO effectively improves correctness (as measured by WER), speaker similarity, and overall speech quality (measured by MOS) across TTS models.

### Strengths
- The paper is well-written, presenting a clear logical flow and strong motivation, supported by sufficient background knowledge. The authors effectively present the rationale behind their solution and provide intuitive explanations for the mathematical formulation, which might initially seem complex. The differences and improvements of the proposed method compared to previous work are also clearly outlined.
- The UNO framework consistently shows advantages when applied to various TTS models.
- A set of ablation studies is conducted to validate the rationale and effectiveness of the proposed method, including simulations of human feedback using a neural network (as seen in Table 2) and the significance of uncertainty-aware optimization (demonstrated in Table 4), etc.
- The emotional TTS experiments indicate that the UNO framework can be adapted to any binary signals, extending beyond human preferences to emotional valence and arousal, and potentially more factors.
- The Q&A section in the appendix candidly addresses the limitations of this work and outlines potential future directions for further research in this area.

### Weaknesses
On page 5, the definitions of EDL and I-CNF are clear but somewhat overwhelming. I recommend a minor restructuring of these sections to enhance readability and make the content easier to follow.

On Table 5 of page 16, the performance of VALL-E-UNO is unreasonably bad. The authors may need to further check the numerical results in their tables.

### Questions
On Table 5 of page 16, the performance of VALL-E-UNO is unreasonably bad. The authors may need to further check the numerical results in their tables.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores integrating subjective human feedback into the training process of text-to-speech (TTS) models through a method called uncertainty-aware optimization (UNO). It aims to address the mismatch between TTS training and evaluation methods like the mean opinion score (MOS). UNO introduces a framework that incorporates human evaluation into training, using a sampling-annotating-learning approach. It focuses on optimizing TTS performance without needing preference data, accommodating the inherent variability in human feedback. The method claims to improve zero-shot TTS performance in speaker similarity, word error rate, and emotional speech synthesis.

### Strengths
**Integration of Human Feedback** This paper introduces an interesting approach by incorporating subjective human evaluation directly into the TTS training process through the Uncertainty-Aware Optimization (UNO) method. This aims to address a key challenge in aligning TTS models with human preferences and eliminates the need for complex reward models or preference data.

**Flexible and Adaptable Method**  The UNO method is presented to be adjust to different speaking styles, including emotional TTS, offering flexibility in generating synthetic speech.

### Weaknesses
 **Limited Novelty of the Proposed Approach** The UNO method presents an algorithm that closely resembles the KTO algorithm, which was introduced earlier on February 2, 2024. While UNO incorporates uncertainty into its framework, the results in Section 6.3 indicate that it achieves comparable Mean Opinion Scores (MOS) to the UNO-null variant (which does not have uncertainty), with scores of 4.31+0.66 and 4.24+0.59, respectively. This suggests that the inclusion of uncertainty does not significantly enhance performance compared to KTO. Given this similarity and the limited improvement of uncertainty, the novelty of the proposed approach appears to be minimal, as the core methodologies are not fundamentally new. This raises questions about the contributions of UNO to the field, as it does not seem to offer substantial advancements over existing techniques. Can you provide a more detailed comparison between UNO and KTO, highlighting any key differences or improvements? Additionally, can you elaborate on the specific contributions of incorporating uncertainty, given the similar performance to the UNO-null variant?

**Potential limitation in the paper's approach to aligning TTS training with MOS-like subjective evaluation metrics** In introduction, you argue that the TTS system has a clear mismatch between the training objectives and human evaluation. Motivated by this, you propose to use UNO to incorporate human feedback into the TTS training process, aiming to align training objectives with MOS-like subjective evaluation metrics. You train I-CNF with real human-labeled SOMOS dataset to simulate human-like annotations. However, because SOMOS mainly evaluates naturalness, a TTS model optimized for a high naturalness score might still struggle with intelligibility, leading to possible issues in accurately mapping the generated speech to the text content.

**Evaluation discrepancies for Voicecraft** Voicecraft is reported to achieve high MOS for both intelligibility (MOS of 4.23±0.06) and naturalness (MOS of 4.17±0.06) based on evaluations by 59 human participants in the original paper. But you report significantly lower MOS scores for Voicecraft (3.65 by MOSNet and 3.38 from 10 participants) in the evaluation results. This raises concerns about the reliability of the evaluation. If it is because you use LibriTTS to evaluate Voicecraft but the original paper use REALEDIT dataset, it is unclear why you did not utilize REALEDIT, which is publicly available, for fine-tuning with UNO, which could strengthen the comparison.

**Lack of clarity on the accuracy of EDL and I-CNF in predicting human-like annotations and their associated uncertainty** Although the paper compares the distribution of I-CNF predictions and human labels, it doesn’t demonstrate the accuracy and reliability of these models. Given that these predictions significantly impact UNO's overall performance, without validation of EDL and I-CNF's accuracy, it’s challenging to assess the trustworthiness of the results and the proposed method’s effectiveness.

**Validity of ICNF as Human Feedback Proxy** In table 2, the UNO-Human experiment has lower human MOS and MOSNet MOS compared to UNO-ICNF seem unusual and raises concerns. This could suggest that the ICNF predictions might not be truly representative of human preferences. It raises questions about the validity of ICNF as a proxy for human feedback—if real human feedback leads to poorer performance, it may indicate that the ICNF model is capturing a different aspect of the data that is not entirely aligned with human judgment. The paper should clarify why ICNF annotations outperform human-labeled data and whether the evaluation method favors ICNF annotation over true human annotation.

### Questions
1. In Section 4.1, you mention distinguishing desirable and undesirable samples through human feedback, stored in separate pools (P_pos and P_neg). However, in the third paragraph, you state that EDL and I-CNF are trained on the SOMOS dataset to simulate human-like annotations and uncertainty, rather than through true human distinction. Could you clarify how "human-like" annotations from EDL and I-CNF are predicted? Does I-CNF predict a MOS score per audio, given that SOMOS only provides MOS scores? If EDL and I-CNF are trained to predict MOS with uncertainty, the method for classifying samples into desirable and undesirable categories based on these predictions remains unclear. Can you provide a detailed explanation of the process for classifying samples into P_pos and P_neg, including any specific thresholds used and how these were determined? Can you provide a sensitivity analysis of the boundary score? This gap in the methodology makes it difficult to understand the criteria for categorizing samples into P_pos and P_neg​.  

2.  Can you provide confidence intervals or p-values for all key comparisons, particularly those between UNO and the baseline methods (PPO, DPO, and ODPO) across all reported metrics? Without these, it is impossible to tell if the result is significantly better than PPO and DPO and ODPO.

3. The claim in Appendix D, UNO training: “Due to the constraint of the reference model, it will not result in over-fitting.” is not correct.

4. Can you provide qualitative examples or audio samples that illustrate the improvements made by your approach?

5. The experiment in 6.5 EXTENSION ON EMOTIONAL TTS and Appendix F is not clear. How do you identify the samples with high and low valence and also arousal, do you train a model to identify them? What is your evaluation metric for identifying the emotion state of UNO's results, the same model you used for identifying high and low valence/arousal? Can you also provide some audio samples that illustrate the emotion change made by your approach?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel framework, UNO, aimed at integrating human feedback into the text-to-speech (TTS) learning loop. The proposed framework leverages an uncertainty-aware optimization approach and follows a sampling-annotating-learning pipeline. First, the authors generate multiple samples by using inference with varied prompts. Next, they train an annotation simulator to model human decision-making with associated uncertainties. Finally, the framework fine-tunes the pre-trained model through a proposed Uncertainty-aware Optimization loss.

### Strengths
1. This work addresses an important problem by incorporating human feedback into TTS model training, and it is theoretically well-founded.
2. The authors present extensive evaluations and experiments, providing a thorough analysis of the proposed framework.
3. The framework appears to be a generalizable pipeline, though additional analyses and experiments would further strengthen the work.

### Weaknesses
1. In the simulation and annotation steps, the simulators I-CNF and EDL rely on systems that are already well-established in prior research, limiting the novelty of the annotation procedure. The use of these existing systems, while practical, doesn't introduce new methods for modeling human feedback, which is a core aspect of the paper's contribution. The annotation process essentially becomes a re-application of known techniques rather than a novel approach to simulating human judgment.
2. The equations in the paper could benefit from better formatting, as double references, such as "Eqn. equation," detract from readability. The current formatting makes it difficult to follow the mathematical derivations and understand the relationships between different equations. This lack of clarity hinders the reader's ability to fully grasp the technical details of the proposed method.
3. Many important points and comparisons are located in the appendix. These should be moved to the main sections to improve the readability. The writing should be improved. The current structure buries critical analysis, making it harder for the reader to assess the significance and limitations of the work. The main body of the paper lacks sufficient detail, forcing the reader to constantly refer to the appendix for key information.

### Questions
1. In lines 282-283, the authors mention that due to the lack of diversity, existing TTS models struggle to generate paired sw and sl using fixed target transcripts and speech prompts. I am unclear about this assumption, as many TTS models can produce varied speech by using different random seeds in the sampling process. Could you clarify this point? 
2. Why does VALLE-UNO perform significantly worse than VALLE on the WER metric? Given the high WER, it’s surprising that both similarity and MOS scores remain high.
3. In line 794, author mentioned that theoretically feasible for UNO to optimize diffusion-based TTS. Could you provide experimental results to support UNO’s application to other diffusion-based TTS models?
4. On the demo page, the authors highlight some failure cases for the Voicecraft system. Assuming similar issues could arise after UNO optimization, could you provide comparative statistics on these failure rates?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors introduce an optimization scheme termed Uncertainty-Aware Optimization (UNO) designed to enhance zero-shot Text-to-Speech (TTS) systems through human feedback. Unlike previous RLHF methods, UNO does not require pairwise preference data or a reward model. Experimental results indicate that, following post-training with UNO, the TTS system demonstrates improvements in both subjective metrics (speaker similarity, word error rate) and objective metrics (MOS) compared to the baseline system. Additionally, the authors demonstrate that UNO can seamlessly and flexibly adapt to the desired speaking style in emotional TTS.

### Strengths
* This paper introduces uncertainty-aware optimization (UNO), an RLHF method for zero-shot TTS that does not require a reward model or preference data pairs.
* UNO addresses issues in the TTS domain, such as the uncertainty in subjective human evaluations of speech synthesis, offering insights for research in this field.
* The baseline TTS system (VoiceCraft) optimized with UNO shows significant improvements in WER, SIM, and MOS metrics on the LibriSpeech dataset.

### Weaknesses
 * Firstly, some of the authors' statements are not rigorous. The authors claim that their method does not require a reward model, but in fact, they trained a model to simulate SOMOS and used the results of the SOMOS simulation model as a proxy for the reward, which does not eliminate the need for a reward model. The use of a proxy, even if it's a binary classifier, still constitutes a reward model in the context of reinforcement learning. The authors should clarify that they are using a proxy reward model, not that they are eliminating the need for one entirely.

* Additionally, the authors use SOMOS as a proxy for real human scoring, but the SOMOS samples only include a single speaker (LJSpeech), and its generalization is questionable. I hope the authors will provide more discussion about it. The reliance on a single speaker dataset for training the SOMOS proxy raises concerns about its ability to accurately reflect human preferences across diverse speakers and speaking styles. This limitation could introduce bias and affect the reliability of the optimization process.

* The paper shows that the baseline TTS system improves in SIM, WER, and MOS after training with UNO on LibriSpeech, however, the dataset used for UNO training is LibriTTS, which is derived from the original materials of the LibriSpeech corpus, so it is questionable whether the results on LibriSpeech are brought by RLHF. I think it is necessary to check the performance of the model directly fine-tuned on LibriTTS. The authors should provide a direct comparison to a model fine-tuned on LibriTTS without the RLHF component to isolate the impact of their proposed method. This is crucial to validate the effectiveness of UNO.

* Moreover, the approach of UNO not requiring paired data is not entirely novel; UNO can be seen as REINFORCE with baseline, similar approaches include ReMax [1]  However, I don't think this is a major issue, as UNO may be more suitable for TTS.

* The authors believe that current TTS systems do not exhibit strong diversity in samples generated from the same text and prompt. One possible reason is that the authors tested on LibriTTS, which is an audiobook dataset. In fact, more powerful TTS models (trained on large-scale in-the-wild data) can generate speech with diversity that supports human judgment (at least in some cases) for certain real-life prompts, especially with varying prosody. The claim about limited diversity should be substantiated with more diverse datasets beyond audiobook recordings. The authors should acknowledge that the diversity issue might be dataset-specific.

Some typos:
* line 215, equation (7): $s_i$ should be $s_j$.
* demo page: "NeurIPS 2024 Conference Submission" should be revised.
* line 815, Table 5: The WER of VALL-E UNO seems to be a typo.

### Questions
Some questions have already been raised in the weaknesses section, with additional questions including:

* The authors use the predicted values of SOMOS as a proxy for the reward, and the experimental results show improvements in the SOMOS metric (which I believe is an expected outcome). I would like to ask the authors if they have tried using WER or SIM metrics directly as proxies for the reward to optimize WER and SIM?

* The authors mention in line 336 that they use WavLM-TDCNN for calculating the SIM metric. However, I believe the model they actually used should be https://huggingface.co/microsoft/wavlm-base-sv instead of WavLM-TDCNN, as the results on LibriSpeech generally exceed 0.8. As far as I know, the current SOTA models using WavLM-TDCNN for calculating the SIM metric typically yield results around 0.7.

* Have the authors explored the generalization capabilities of their model on in-the-wild data?

### Soundness
3

### Presentation
3

### Contribution
2
