# Multimodal Depression Detection with Contextual Position Encoding and Latent Space Regularization

- Decision: Reject
- Scores: 6, 5, 3, 3

## Abstract
Clinical interviews are the gold standard for detecting depression, and previous work using multimodal features from participants' audio, transcribed text, and video have shown promising results. Recent approaches further improve performance by incorporating an additional textual modality—the interviewer’s prompts—during training. However, these approaches risk introducing biases, as models may over-rely on specific prompt-response pairs, which may not always be present in real-world settings. This leads to models exploiting these cues as shortcuts for detecting depression rather than learning the language and behaviors that genuinely indicate the subject's mental health, ultimately undermining consistency and objectivity. To address this, we propose a novel approach that combines Contextual Position Encoding (**CoPE**) and Latent Space Regularization (**LSR**), leveraging both subjects' responses (audio) and the interviewer's prompts (text). CoPE captures the evolving context of the interview, ensuring that the model utilizes insights from the entire conversation, preventing over-reliance on isolated or late-stage cues. This helps the model understand interactions holistically and more accurately reflect mental health indicators. LSR introduces constraints to enforce consistency in the model’s learned representations, reducing overfitting to superficial cues and guiding the model toward more generalizable patterns. By smoothing the latent space, LSR helps the model focus on meaningful, high-level representations of both audio and text.
Our approach yields competitive results on the **DAIC-WOZ** benchmark and surpasses the state-of-the-art on the **EATD** benchmark. The code is released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The document presents a novel approach to detecting depression by leveraging multimodal data from clinical interviews. This method combines **Contextual Position Encoding (CoPE)** and **Latent Space Regularization (LSR)** to enhance model accuracy and generalizability. By analyzing both participants' audio responses and interviewers' text prompts, CoPE enables the model to capture the full conversational context rather than relying on isolated cues. Meanwhile, LSR helps prevent overfitting by encouraging the model to focus on meaningful patterns in the data. The applicability of the proposed approach has been evaluated using two state-of-the-art datasets, including **DAIC-WOZ** and **EATD**.

### Strengths
* Multimodal approach relying on the inclusion of contextual positional embeddings and latent space regularization for depression detection.
* Inclusion of participant's audio responses and the interviewer's text prompts for improving the accuracy and generalizability of depression detection models.
* State-of-the-art results on the DAIC-WOZ and EATD datasets for multimodal depression detection.

### Weaknesses
* The interview is classified as a distinct modality; however, it would be more accurately rephrased as a text modality. 
* In **Table 1**, it is unclear whether CoPE has been applied to the text modality within the first set of audio-specific models. 
* Why was the visual modality not considered in the modeling phase?
* In **Table 2**, the table should be divided into sections based on respective datasets.
* LSR implements regularization at the level of latent embeddings. How does this compare to weight-based approaches, such as L2 and L1 regularization techniques? 
* Instead of utilizing attention-based weighting, what was the rationale behind not considering cross-attention-based fusion for the text and audio modalities?

### Questions
* Have the authors thought about utilizing RoPE embeddings for encoding relative positions regarding contextual position encoding?
* Do the existing contextual CoPE embeddings apply effectively to interview sessions of varying lengths, from short to long?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a novel approach to detecting depression from clinical interviews by combining Contextual Position Encoding (CoPE) and Latent Space Regularization (LSR) to overcome limitations of existing methods that rely too heavily on specific question-answer pairs. The system processes both audio responses and interviewer prompts through a multimodal framework, achieving competitive results on the DAIC-WOZ dataset and state-of-the-art performance on EATD.

### Strengths
Main contribution/ideas: 1) Proposed to use Contextual Position Encoding (CoPE) to capture the evolving nature of clinical interviews, 2) Uses Latent Space Regularization (LSR) to prevent overfitting and encourage more generalizable patterns, 3) Combines both audio features and interviewer prompts. 1-is the main contribution and should have been the focus of the paper.

The performance is strong compared to other audio and audio+interviewer baselines. Good ablation analysis verifies the importance of CoPE for this dataset

Well-written paper, well-presented ideas, good technical detail.

### Weaknesses
I would have personally preferred to focus just on the CoPE embeddings and similar ideas to explore the nature of clinical interviews and how transformers can better model this structures. I think this is the main idea/contribution of the paper and it gets diluted as the authors are chasing SoTA. 

Questions about generalizability: I am missing a more detailed deep dive into the databases to understand the impact of each proposed methods to a differently structured interaction, e.g., would CoPE be relevant for a podcast interview, what is the power of representation it is adding to the model etc. Also can you better explain the effect of I, why is it important, is the question order reshufle that you do important?

All methods proposed are not new (cope, lsr, cross-modal attention, feature fusion) so the originality of the paper is limited. 

Missing Comparisons with the SoTA multimodal approaches.

### Questions
Why don't you present any results even for simple fusion for text and video, since SoTA is what you are after?

See also question above about generalizability and deeper data analysis,

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents an architecture for automatic depression detection from clinical interviews. The input information is obtained as a combination of the patient's audio recordings and the interviewer's textual prompts. The key components of the architecture are the Contextual Positional Encoding, which is a combination of absolute and relative positional encodings, and the application of L2 regularization to the fused modality features. The proposed approach achieves competitive results on the DAIC-WOZ benchmark and state-of-the-art results on the EATD benchmark.

### Strengths
* The paper does a good job on presenting the current progress on the field of automatic depression detection.
* Ablations are performed for each architectural component.

### Weaknesses
* The novelty of the proposed approach comes into question, as it appears a combination of pre-existing methods, applied to well-studied datasets
* There are some issues with the presentation of the method. Specifically, in L257 the equation describing the LSR loss includes a dropout term, while in L340 no such term exists in the loss. My guess is that L257 is inaccurate and simply aims to demonstrate that dropout is applied during training, but this may confuse future readers.
* The presentation of Table 1 could be improved by including some extra columns (Text encoder, Audio encoder etc.)
* No statistical significance testing is presented about the results. This is especially relevant because the explored datasets are fairly small, and the improvements are rather marginal.
* Regarding formatting there are two issues worth of mention. 1) all equations are unnumbered. Including equation numbering can help referencing equations during reviewing or analyzing the paper. 2) The gap after Fig. 1 could be utilized to present more relevant information in the main part of the paper.

### Questions
* The Equations about the LSR loss need further clarifications.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper provides a method for detecting depression in clinical interviews by combining Contextual Position Encoding and Latent Space Regularization. This involves tracking the context as it evolves over the conversation, and subsequently smoothing latent representations. This is meant to better capture the ‘flow’ of the conversation and avoid overfitting. Although this provides good results on DAIC-WOZ and EATD, additional modalities (like video) could have been pursued.

### Strengths
- the more contextual approach of CoPE is a good addition to the (varied and numerous) approaches to this problem. This might be a better way to obtain pragmatic cues or more speaker-specific baselines than focusing on cross-sectional aspects across speakers. Using LSR to smooth the latent space is also a correct step to take, although there are alternatives. This is, on the whole, positive but fairly evolutionary.
- SotA performance is, of course, reported on this important task. Ablations are run on the appropriate parts of the model in Table 3, and various alternatives are mentioned in Table 2 for comparison.

### Weaknesses
- While it is positive that DAIC-WOZ and EATD were used, this is still a somewhat reduced and well-trodden set. They are also fairly curated and may not reflect real-world variability or noise, which limits claims of generalization or robustness.
- Despite the (almost necessary) ablations, the evaluations are fairly superficial, focusing on precision, recall, and F1 but not going deeper into the results to vary the parameters further, or to explain them, or to identify patterns in performance on aspects of the dataset. The result is a fairly ‘paint-by-numbers’ set of experiments with unclear gain in knowledge.

### Questions
- Could you check your references for, e.g., completeness (e.g., how the WHO 2017 paper was published) or formatting?
- What real-world aspects may be relevant to consider for additional analysis? E.g., how might environmental considerations or more unstructured data collection relate to your results? What are the limitations of this work that you are able to identify?

### Soundness
2

### Presentation
2

### Contribution
2
