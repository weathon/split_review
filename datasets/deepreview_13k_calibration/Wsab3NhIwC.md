# Resource Efficient Self-Supervised Learning for Speech Embeddings

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3

## Abstract
Representation learning from sequential data using self-supervised learning (SSL) has proven to be a powerful technique and improved state-of-the-art (SOTA) results when fine-tuned for various downstream tasks. So far the success of SSL frameworks, e.g., Wav2Vec2 and Data2Vec2, for learning audio embeddings is primarily carried out by masking intermediate features and then solving a contrastive or non-contrastive task in an end-to-end manner, respectively. In comparison to contrastive SSL methods such as Wav2Vec2, non-contrastive techniques such as Data2Vec2 have emerged having better model quality and training time. However, Data2Vec2 is still quite demanding in terms of resources, namely infrastructure (more and better GPUs), which remains a significant barrier to further improving models for downstream tasks. In this work we show that non-contrastive learning, such as an extension of the Barlow--Twins methodology, when applied to a range of downstream tasks simultaneously decreases training time and resource requirements while maintaining or improving SOTA results in key benchmark datasets. From a computional point of view, our approach decreases Data2Vec2 training time by $2\times$ and permits effective training with smaller sequence lengths and batch sizes without requiring gradient accumulation reducing GPU VRAM requirements from NVIDIA A100's to V100's.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
While wav2vec-style contrastive learning has shown to be very successful for ASR, it requires a lot of resources and time for training. In the vision domain, Barlow Twins, a solution that naturally avoids collapse, has shown to be able to achieve better (or competitive) performance compared with contrastive learning (e.g., SimCLR) while using much smaller batch size. However, Barlow Twins style training is under-explored in the ASR/audio domain.

The authors explored using BT to speech representation learning and achieved competitive performance compared with wav2vec2; The authors further combined their approach with wav2vec2 to further boost the performance. The authors claim the proposed methods can reduce training time, GPU usage and improve convergence.

### Strengths
This is, if not the first, among the early explorations that applies Barlow-Twins methodology to learn representation for ASR; The adoption of BT into sequential representation learning is not trivial. Previously, BT was mostly used to learn a global representation of a sequence.



— The authors show that the proposed methods are more resource efficient and achieve comparative performance. a) It improves convergence, b) it reduces training time, c) it significantly reduces GPU training times, d) it requires smaller batch size thus reducing memory requirements.



— The authors also found that combining the proposed method with a wav2vec-style contrastive learning approach is helpful.

### Weaknesses
The proposed approach, though has some computational benefits when compared to Data2vec2, it achieves clearly worse performance compared to Data2vec2.

The authors try to combine wav2vec2 pre-training and the proposed method, which can significantly improve the performance, but the performance is still worse than Data2vec2. What's more, after combining with wav2vec2 pre-training, the computational resources needed would increase drastly. 



— Regarding Time Unrolling and time merging losses: To calculate both the F by F and B by B correlation matrix, the calculation can become a burden when sequence length T is big. In this work, the authors propose to crop the audio into 5-seconds. However, these limitations could affect learning in a large context.


The authors do not test their model on tasks other than ASR.

### Questions
See Weaknesses section

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- self-supervised learning (SSL) approaches have helped to improve speech model performance
- these techniques have included both contrastive and non-contrastive methods
- non-contrastive methods (like Data2Vec2 vs Wav2Vec2) have improved performance and reduced training time, but still suffers from significant GPU resource constraints
- this work introduces a non-contrastive approach which is an extension of the Barlow-Twins methodology to reduce training time and resource requirements for self-supervised model training
- to adapt speech for the Barlow-Twins method, they use time-unrolling ([B, T, F] -> [B * T, F]) and time-merging ([B, T, F] -> [T * F, B]) approaches when computing two different cross-correlation terms for the losses
- the primary comparisons are done with wav2vec2, data2vec2, non-contrastive (their approach), and sequentially combined (wav2vec2 training then non-contrastive)
- these comparisons are done when fine-tuning on LibriSpeech 960h, train-clean-100h, and LibriLight-10h
- 960h: the results are slightly better w/o LM but w/ LM they're competitive
- for the 10h and 100h settings, the result trends broadly follow:
         - non-contrastive consistently outperforms wav2vec2
         - sequentially combined outperforms non-contrastive
         - but sequentially combined and data2vec2 are more competitive with each other
- the main benefits come from requiring less resources by being able to use smaller batch sizes (reducing training time) as well as fewer GPUs

### Strengths
Straightforward motivation, modification/adaptation of an existing idea, and execution. Primarily isolating changes to the loss, while keeping architectural changes minimal.

### Weaknesses
Despite the similarities to Wav2Vec2 and Data2Vec2, it would be nice to include more non-contrastive comparisons (especially since the application focus is on speech), these would ideally include at least one of HuBERT and WavLM. Since the takeaway here seems to be about reducing resource requirements while maintaining high-quality performance, comparison with these popular approaches both in terms of training resources required and inclusion in the WERs table would be helpful.

Also, in the abstract, SSLs are mentioned as being great for a variety of tasks. Seeing the performance of this non-contrastive approach on not only ASR but other speech tasks as well could help to distinguish it from Data2Vec2 (since it often needs to be sequentially combined with wav2vec2 to match Data2Vec2 performance on the "other" partition of dev or test). These SSLs are useful in a variety of cases, so an idea of the general performance hit (in service of resource savings) on these other tasks would be helpful.

### Questions
Resource and performance comparisons with HuBERT and WavLM would be helpful (for more non-contrastive comparisons).

It would be nice to see the trade-off between training time (or # of GPUs) and performance between these models (i.e. if you speed up the training recipe of the contrastive vs non-contrastive approaches does the performance degrade similarly in cases where you have even more significant resource constraints than those given).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a non-contrastive learning approach to self-supervised learning from speech. More specifically, the proposed method extends the Barlow-Twins methodology so the loss is defined over sequential data. The method also requires fewer resources, while providing competitive performances, especially in low-resource languages.

### Strengths
- The proposed time unrolling and time merging methods appear to be an adequate extension of the Barlow-Twins method, which was originally proposed for non-sequential data. 

- The proposed method shows consistent performance; it either competes with the sota performance or improves it. 

- The overview of the proposed method is summarized well in Fig 1.

### Weaknesses
 - It's not clear which of the two terms is contributing more to the performance of the model, in the proposed loss function L_U and L_M. Specifically, the paper lacks an ablation study to determine the individual impact of the unrolling loss (L_U) and the merging loss (L_M). Without this, it's difficult to assess the necessity of both terms, or if one is significantly more important than the other. 

- In general, the paper doesn't provide an in-depth justification for the claims, and relegate the explanation to the reference, such as the implication and importance of gradient stopping. For example, the paper mentions gradient stopping as a crucial component, but does not elaborate on why it is necessary or how it affects the learning dynamics in the context of the proposed method. This lack of explanation makes it difficult to fully understand the method's inner workings.

- It seems that the proposed method could save some GPU time, but not too significantly (1.3X less). The reported 1.3x reduction in training time, while beneficial, might not be substantial enough to justify the complexity of the proposed method, especially if the performance gains are marginal. A more detailed analysis of the computational cost and its impact on practical applications would be beneficial.

- The presentation of the loss function is somewhat abrupt, lacking explanation. The paper introduces the loss function without sufficient context or motivation, making it difficult for the reader to grasp the underlying rationale and design choices. A more thorough explanation of each term and its contribution to the overall objective would improve clarity.

- Literature review could be more organized. The literature review lacks a clear structure, making it difficult to understand how the proposed method relates to existing work. A more systematic and organized presentation of related research would improve the paper's overall coherence.

### Questions
- One of the main claims is that the proposed method provides a new SOTA result on the low-resource labeled data, which is good. However, it's not clear why the proposed method cannot compete with the Data2Vec2 method in the high-resource labeled data experiments.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a non-contrastive self-supervised learning (SSL) method for speech models. The core idea of this method is to leverage the Barlow-Twins (BT) training technique, which tracks the EMA of the model and compares it with the original to compute loss. Specifically, the method encourages the correlation matrix to become identity, both in a batch-wise and time(frame)-wise manner. Because additional time-axis presents in speech data, the authors show two ways to incorporate time information (time unrolling and time merging). By combining these losses with latent-level augmentation (like SpecAug) and hyper-parameter optimization, the proposed method achieves comparable speech recognition performance to previous models such as Wav2Vec2 and Data2Vec2 while utilizing fewer GPU resources.

### Strengths
* This paper appears to be the first adaptation of a BT-like approach for speech SSL domain. The method naturally integrates the time dimension, making the method more tailored to speech.
* It is good to see the research that addresses the resource-intensive nature of SSL training. Especially, the suggestion of training with shorter sequence length is a novel contribution not much explored in previous works.

### Weaknesses
 * Despite the title of this paper mentioning “speech embeddings”, experiments only evaluate the learned representations in the context of the ASR task. A broader evaluation including common SSL benchmarks such as SUPERB[1] would provide a more comprehensive understanding. Specifically, the SUPERB benchmark includes tasks such as speaker identification, emotion recognition, and keyword spotting, which would offer a more complete picture of the quality and generality of the learned embeddings.
* Related works on SSL do not include recent SSL papers such as WavLM[2] or BEST-RQ[3]. This omission is significant as these models represent state-of-the-art approaches in self-supervised speech representation learning, and a comparison with them is crucial to properly contextualize the contribution of the proposed method.
* I am not quite sure that speech SSL methods are either contrastive or non-contrastive. For example, HuBERT is more like a BERT-style Masked Language Modeling (MLM) approach rather than a contrastive one. This line of work includes w2v-BERT, WavLM, and BEST-RQ. As HuBERT / WavLM are gaining popularity, I think a comparison with these methods would be beneficial. The lack of clarity on the distinction between contrastive and non-contrastive methods in the context of speech SSL is a significant issue that needs to be addressed.
* The authors discuss static and dynamic scaling techniques for balancing the loss; however, there are no corresponding experimental results. The absence of empirical validation for these scaling techniques makes it difficult to assess their effectiveness and practical utility.
* (minor) The reference style is inconsistent across different sections of the paper, which makes it difficult to read. Please consider unifying the style throughout the paper.

### Questions
* The performance gap of ‘non-contrastive’ vs. ‘sequentially combined’ is not small for low-data scenarios. This raises the question of whether the non-contrastive approach sufficiently provides information for speech recognition. Is the performance gap caused by contrastive learning’s ability, or, is it a by-product of longer training? I’d like to hear your thoughts on this.
* Regarding the numbers in Table 3, for sequentially combined cases, where do 3040 (2376+664) and 380 (297+83) come from? It does not seem that there are clear explanations for these numbers.
* The authors mention the Appendix in Table 5, but I cannot find the Appendix.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
