# Advancing Test-Time Adaptation for Acoustic Foundation Models in Open-World Shifts

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Test-Time Adaptation (TTA) is a critical paradigm for tackling distribution shifts during inference, especially in visual recognition tasks. However, while acoustic models face similar challenges due to distribution shifts in test-time speech, TTA techniques specifically designed for acoustic modeling in the context of open-world data shifts remain scarce. This gap is further exacerbated when considering the unique characteristics of acoustic foundation models: 1) they are primarily built on transformer architectures with layer normalization and 2) they deal with test-time speech data of varying lengths in a non-stationary manner. These aspects make the direct application of vision-focused TTA methods, which are mostly reliant on batch normalization and assume independent samples, infeasible. In this paper, we delve into TTA for pre-trained acoustic models facing open-world data shifts. We find that noisy, high-entropy speech frames, often non-silent, carry key semantic content. Traditional TTA methods might inadvertently filter out this information using potentially flawed heuristics. In response, we introduce a heuristic-free, learning-based adaptation enriched by confidence enhancement. Noting that speech signals' short-term consistency, we also apply consistency regularization during test-time optimization. Our experiments on synthetic and real-world datasets affirm our method's superiority over existing baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates Test Time Adaptation of pre-trained acoustic models. different real world shifts like noise, sining voice and accents are examined. For adaptation two issues are considered one is correlation between speech frames and the other is enhancing the confidence. Experimental results supports the gain of the proposed method.

### Strengths
- An important issue is addressed
- Paper is written well

### Weaknesses
- Experiments could be extended

### Questions
- In the ablation study the impact of the two terms in equation 5 is explained. I think the conclusion about the impact of components depends on the setups. The importance of the two components could be different in the noise shift than the accent shift. what do you think?

- Do you consider language as a shift? could a foundation model be adapted to a new language?

- what is a practical way to get alpha in equation 5?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the issue of test-time adaptation (TTA) for Speech Foundation Models, including wav2vec2, hubert, and the like. Conventional TTA methods for visual modality typically aim to minimize label entropy in test utterances. These utterances are chosen based on predefined entropy thresholds to prevent model updates that may lead to mode collapse (Niu et al., 2023).

However, applying this traditional approach to speech models doesn't yield the desired results because non-silent frames in speech models often exhibit high entropy and carry valuable information (thus, they shouldn't be pruned). To address this, the paper introduces a confidence-enhanced entropy method that proves effective for speech models.

Empirical findings from experiments on synthetic and real benchmarks underscore the practicality and effectiveness of this proposed approach.

### Strengths
1. The paper clearly highlights the reason for previous approaches to not work in audio modality. It make sense that non-silent frames have a high entropy as they are the ones where the non-blank labels are to be predicted.

2. The empirical results show the usefulness of the approach on various experimental protocol.

3. The paper is well-written and easy to follow.

### Weaknesses
1. The contributions seems minimal, as the core idea of TTA (Niu et al., 2023 and other related works cited in the paper) are already available in the literature.

### Questions
1. In comparison to different vocabulary sizes, such as employing a BPE model with a larger vocabulary, how does this work perform? Would the entropy for non-silent frames significantly increase under such circumstances?

2. Could this approach be adapted to function with a model architecture similar to RNN-Transducer? What specific modifications would be necessary to enable its compatibility with such an architecture?

3. Wav2vec2 features a self-supervised encoder. Would it be a viable alternative to the proposed TTA approach to fine-tune the wav2vec2 encoder using test utterance audio as a baseline? What advantages or disadvantages might this alternative approach present?

4. Could you provide further clarification on the decoding strategies outlined in Section 5.4 of your paper? Specifically, post-adaptation, how do different inference strategies, such as beam search or greedy decoding, impact the inference process, and what are the key differences in their outcomes?

### Soundness
3 good

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
This paper proposes a new approach to test-time adaptation.
Unlike previous work, this work explicitly focuses on sequential data (speech), as opposed to static and independent objects such as images. 
The proposed method is a heuristic-free, learning-based, confidence enhanced approach to adaptation.
The authors demonstrate the effectiveness of their method and superiority over existing approaches on synthetic and real-world data.

### Strengths
* This paper addresses test-time adaptation for sequential data (speech) and not only for static objects (images).
* The topic is relevant.
* The paper proposes a fully learnable approach for test-time adaptation.
* The experiments show small but consistent gains (up to a few % relative).

### Weaknesses
* One of the paper's goals is heuristic-free test-time adaptation. As for me, the authors mainly move existing heuristics into loss functions, which makes it a learnable approach and gets rid of hyper-parameters that need to be manually set (at least when ignoring optimization hyperparameters such as learning rate, etc.). But the heuristics remain, don't they?
* Unlike previous work, this paper focuses on sequential data (here, speech) rather than static objects like images. I commend the authors for this. However, the only twist that the authors add is an auxiliary loss based on some heuristic for speech signals' short-term consistency. According to Table 5, the benefits from this loss term are modest. Is this all we can/need to do for sequential data? See also question 1 below.

* I think there are a few issues with the equations:
  - Eq.(3) & Eq.(4): Are these frame-level (what the text says) or sequence-level (what the equations look like) quantities?
  - Eq.(4): Please fix subscript - subscript S with i or sum over i? Utterance-level E?
  - Eq.(5): Cardinalities of z’ don’t match.
* The text says "The classification of frames as silent or non-silent was determined based on pseudo labels derived from model predictions." For Figure 3, is the classification done once on the initial, non-adapted model or repeatedly on the respective adapted model?
* How are the hyper-parameters (e.g., loss coefficients) selected?
* Could you please clarify what LS-C stands for: LibriSpeech Noise Corrupted (Figure 3) vs synthetic dataset (Sec. 5.1)?
* Something is off with the inline citations.
* Figure 3: Is percentage in [0,1] or [0,100]? 
* Typo: "model training _phrase_"

### Questions
1. Why do we need the auxiliary loss in Eq.(5) to improve the consistency of speech signals? Could we get rid of this heuristic by using a proper sequence-level loss (e.g., sequence-level instead of frame-level entropy in Eq.(2)) ?

2. Summary of Table 2, for example: 'Ours' outperforms 'SUTA' 0.2 - 1.1% absolute, but WER for lower SNRs is still a multiple of WER on "clean" data (as much as 82.2 vs 17.5). This makes me wonder what the lowest achievable WER (e.g., human WER) is, in particular on the heavily corrupted data sets? This information might be useful to understand the empirical results:

    (i) If bound by information loss of corruption: The proposed approach may be optimal and the small gains highly significant. But the task may be not the best to evaluate the proposed method.

    (ii) If not bound: What is missing to considerably close the WER gap?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper aims to investigate test-time adaptation tasks for pre-trained acoustic and speech models, considering them foundational in their respective domains.

During test-time adaptation that involves frozen pre-trained models, the principal innovations of this work are encapsulated in two proposed methods: `Confidence Enhanced Adaptation` and `Short-Term Consistency Regularization.` 

- Both methods release trainable parameters, whether through normalization layers or input-based feature modifications. These methods closely resemble the techniques used in neural speech model reprogramming, as reported in acoustic model reprogramming ICML 2021 [1], addressing similar challenges in the adaptation of frozen models.

Overall, the author seeks to address a critical issue in acoustic modeling and speech processing. However, the paper's effectiveness is compromised by a noticeable gap in the understanding of related work on frozen acoustic model adaptation. This lack, coupled with certain experimental setups and theoretical justifications, undermines the paper's ability to convincingly argue whether the proposed method is both novel and a parameter-efficient approach for the adaptation of frozen acoustic models.

As a reviewer, I will outline several potential and relevant perspectives for improvement below. Generally, I concur that the direction of open-set test-time adaptation warrants deeper study and is a worthwhile pursuit. 

From a neutral standpoint, it is necessary for the authors to significantly revise the manuscript, as there are fundamental LaTeX errors that need correction. Currently, the draft falls short of the above-average quality expected of a paper submission.

For instance, the authors should use `\citep` for parenthetical references, `\citet` when referring to the author(s) as part of the narrative, and `\cite` when mentioning the work as a standalone noun. Further details on this can be found in the strengths and weaknesses sections.

### Strengths
- The topic of test-time adaptation is generally interesting to the ml / speech community, although some perspectives on foundation (very large pre-trained) models based on in-context learning are not covered.

### Weaknesses
- writing quality could be very improved (perhaps doing in their next version)
  - citations code / format usages
  - grammar issues
  - The literature review on frozen acoustic model-based adaptation lacks depth. The current review primarily applies existing algorithms from the ML community, and the proposed method inadvertently overlaps with reprogramming/prompting due to an inadequate literature survey.
    - for example, the additional losses based adapters / input-only training has been also proposed in [4]
- The theoretical connection between test-time adaptation efficacy and frozen pre-trained models is unclear. A well-known recent insight involves latent space alignment via Wasserstein measurements, yet the related discussion is absent here.
- The related speech processing references are missing
  - frozen model adaptation via Bayesian adaptation in speech
  - frozen model adaptation with trainable inputs reprogramming / prompting 
- ablation experiments are missing on 
  - Similar parameter-efficient baselines work on frozen pre-trained adaptation diagrams (e.g., input reprogramming, adapters, prompting), making it difficult to justify the novelty on applying trainable layer norms
  - In terms of frozen pre-trained models, only Wav2Vec 2.0 Large has been evaluated. The term "foundation model" is often used for models with over 1 billion or even 100 billion parameters to showcase emergent abilities, which is not the case here.

***

**References**

1. Voice2series: Reprogramming acoustic models for time series classification, ICML 21
2. Wavprompt: Towards few-shot spoken language understanding with frozen language models, Interspeech 22
3. Comparison of Multilingual Self-Supervised and Weakly-Supervised Speech Pre-Training for Adaptation to Unseen Languages, Interspeech 23
4. Parameter-Efficient Learning for Text-to-Speech Accent Adaptation, Interspeech 23

### Questions
- high level question
   - the authors mainly highlight their claims on the perspective of foundation acoustic model adaptation, only a single pre-trained model has been discovered. A better takeaway to the community could be how different pre-trained speech and acoustic models in response to the input based adaptation. 
    - If the authors could provide studies different pre-trained acoustic models (e.g., AudioSet pre-trained, WavLM, Whisper, joint supervised and unsupervised w2v2 based methods) to have a deeper look on the (a) training data source and (b) size of model such as [5], this work could be with larger impacts. 
  - how's the proposed methods different with reprogramming and jointly reprogramming plus adapter [6] in the prior works? 

- low-level questions
  - what is the trainable parameters in both settings?
  - in terms of acoustic modeling, any acoustic classification or speaker-level open set has been studied in the proposed method?
  - I am curious how the entropy based additional losses training gonna impact the latent space distance measured from w2v2 pre-trained to target open set 


***
**References**

5. How to Estimate Model Transferability of Pre-Trained Speech Models? Interspeech 23
6. From English to More Languages: Parameter-Efficient Model Reprogramming for Cross-Lingual Speech Recognition, ICASSP 23


## post-discussion

- I raise my score to six (not argue to reject) and give conditional accept to this work toward checking their statements on
   - including frozen model adaptation discussion
   - Bit and P-tuning with revised entropy loss training
   - total trainable parameter numbers 

in their final version. Flagged for AC and SAC double checking if the recommendation is accepted.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
