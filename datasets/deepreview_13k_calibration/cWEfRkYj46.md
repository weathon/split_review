# Towards Homogeneous Lexical Tone Decoding from Heterogeneous Intracranial Recordings

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 3, 8

## Abstract
Recent advancements in brain-computer interfaces (BCIs) have enabled the decoding of lexical tones from intracranial recordings, offering the potential to restore the communication abilities of speech-impaired tonal language speakers. However, data heterogeneity induced by both physiological and instrumental factors poses a significant challenge for unified invasive brain tone decoding. Traditional subject-specific models, which operate under a heterogeneous decoding paradigm, fail to capture generalized neural representations and cannot effectively leverage data across subjects. To address these limitations, we introduce \textbf{H}omogeneity-\textbf{H}eterogeneity \textbf{Di}sentangled \textbf{L}earning for neural \textbf{R}epresentations (H2DiLR), a novel framework that disentangles and learns both the homogeneity and heterogeneity from intracranial recordings across multiple subjects. To evaluate H2DiLR, we collected stereoelectroencephalography (sEEG) data from multiple participants reading Mandarin materials comprising 407 syllables, representing nearly all Mandarin characters. Extensive experiments demonstrate that H2DiLR, as a unified decoding paradigm, significantly outperforms the conventional heterogeneous decoding approach. Furthermore, we empirically confirm that H2DiLR effectively captures both homogeneity and heterogeneity during neural representation learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces the Homogeneity-Heterogeneity Disentangled Learning for Neural Representations (H2DiLR), a framework designed to improve neural decoding by separating homogeneous and heterogeneous components from intracranial recordings across multiple subjects. The study demonstrates that H2DiLR significantly enhances tone decoding performance in Mandarin-speaking participants using stereoelectroencephalography (sEEG) data. The framework outperforms traditional methods by effectively capturing and leveraging both shared and subject-specific neural features.

### Strengths
The introduction of the Homogeneity-Heterogeneity Disentangled Learning for Neural Representations (H2DiLR) is a novel approach that effectively addresses the challenge of data heterogeneity in neural decoding. By disentangling shared and subject-specific neural features, the framework enhances the decoding accuracy across multiple subjects.

The study employs a robust experimental setup using stereoelectroencephalography (sEEG) recordings from multiple Mandarin-speaking participants.

The proposed method demonstrates a substantial improvement in tone decoding accuracy over traditional subject-specific models.

### Weaknesses
The statement that a "comprehensive set of 407 Mandarin syllables covers nearly all Mandarin characters" requires further clarification. You need to provide the specific vocabulary list used in the rebuttal materials to support this claim.

The concept of private and shared codebooks is introduced in the paper but lacks a detailed explanation. A more comprehensive rationale and description are needed to clarify how and why these codebooks are defined and utilized.

Sharing the data and code would greatly enhance the validation and reproducibility of the proposed method by the research community. This transparency would contribute significantly to the field and support further advancements.

The claim of being "the first" to work with 407 Mandarin syllables is inaccurate, as the 2023 study titled "A high-performance brain-to-sentence decoder for logosyllabic language" also mentions using a dataset with 407 syllables. Although this work is cited, the related work section lacks a detailed discussion of this study and how the current work differentiates itself.

The paper asserts that it disentangles homogeneity and heterogeneity, yet the evidence provided relies on feature visualization of specific samples. A statistically robust analysis is necessary to substantiate this claim. 

While the framework allows for joint training across multiple subjects, the use of separate encoders for each subject may significantly increase computational costs, which should be addressed and optimized.

### Questions
Can you provide the specific list of 407 Mandarin syllables and explain how they represent nearly all Mandarin characters?

How and why are the private and shared codebooks defined and utilized within your framework?

Have you considered the computational cost implications of using separate encoders for each subject, and are there plans to optimize this aspect?

How does your work differentiate from the 2023 study "A high-performance brain-to-sentence decoder for logosyllabic language," which also uses a dataset with 407 syllables?

What is the total duration of the sEEG data in the dataset you provided?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper discusses a method called Homogeneity-Heterogeneity Disentangled Learning for neural Representations (H2DiLR) for decoding tone from stereoelectroencephalography (sEEG) data.  H2DiLR disentangles shared (homogeneous) and individual-specific (heterogeneous) neural representations using a two-stage learning paradigm. The first stage involves unsupervised learning of neural features via vector quantization with shared and private codebooks, while the second stage applies these representations to decode tones using a transformer model​. The authors claim that H2DiLR outperforms previous baseline methods by 12% when evaluated on Top-1 accuracy.

### Strengths
The topic of tone decoding is understudied, if somewhat narrow, and the idea to separate homogeneous and heterogeneous neural representations is interesting and could have use cases outside the specialized setting of tone decoding, if applied to semantic neural representations more generally. Overall, I think the idea is interesting enough to be in the "borderline accept" category of papers, mainly because I think the idea is general enough to have practicable value outside this particular application.

### Weaknesses
I feel that the authors limited themselves somewhat in specializing their approach to tone decoding only. I feel that the problem of disentangling subject specific effects from general ones is a wider problem with many downstream applications, most notably for semantic decoding, but also for problems of encoding as well. I would have liked to see a deeper exploration of this in the work. There is also disappointingly little exploration of the abundant neuroscience questions here - I would like to have seen a location-based ablation in addition to the parametric ablations of the method that showed which regions are most useful for tonal decoding. An analysis studying if there are region-specific differences to representational homogeneity (i.e. some regions tend to be more idiosyncratic to a particular subject) would also have been interesting, although I recognize that the chosen data setting, sEEG, has challenges in answering this question due to coverage differences.

### Questions
See weaknesses. What areas of the brain are most important to tone decoding? Does the exclusion of data from some electrodes have more of an impact than others? Is there any benefit of this method for neural encoding models that predict neural responses from feature input?

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
5

### Summary
The authors introduce a neural network architecture, H2DiLR, a self-supervised learning (SSL) method for pre-training models for sEEG tone decoding (4-way classification task) and a novel dataset (407-syllable reading sEEG dataset).

**Dataset**: The patients are asked to read 407 syllables aloud. To make their pronunciation as close to natural speech as possible, carrier words are added to form full sentences. The dataset includes `1221` trials (i.e., 3 trials per syllable). Simultaneously recorded audio signals are then used to precisely identify time stamps for extracting the target syllable from each trial. Each trial is truncated based on these time stamps, resulting in a neural recording of up to `1` second, labeled with one of `4` tones. According to the task paradigm demonstrated in [1], the total recording time for each subject is approximately `5` hours, with each trial lasting around 12 seconds. Therefore, the total amount of pre-training dataset is about `20` hours.

**Model**: They introduce two different codebooks to disentangle the shared and private parts of multiple subjects. During the pre-training stage, they reconstruct the original sEEG signals. After pre-training, they use the frozen pre-trained VQ-Encoder to obtain quantized embeddings of the input sEEG signals. These embeddings are then passed through a temporal Transformer for further temporal integration, followed by a classification head for tone decoding.

**Experiments**: Previous pre-training methods (including BIOT, NeuroBERT, etc.) are compared. Besides, the authors conducted different ablation studies regarding pre-training (partition ratio, # of subjects, etc.).

---------------------------------

**Summary**:

**This study might benefit from further validation to enhance its robustness.**

 - The observed performance improvement might be attributed to the careful selection of hyperparameters in the codebook. See **Private Comment by Reviewer AheB (1/3)** and **Final Comment by Reviewer AheB (1/2)** for more details.
 - Given the current preprocessing approach, the analyzed neuroscience results might be biased. See **Private Comment by Reviewer AheB (2/3)** and **Final Comment by Reviewer AheB (2/2)** for more details.
 - The advantages of the VQ code over the original signal have not been clearly demonstrated through ablation studies. Besides, the author's goal of disentangling different subjects (i.e., the brain's desynchronization nature [3]) does not appear to align with the capabilities of the current model architecture. See **Private Comment by Reviewer AheB (3/3)** and **Final Comment by Reviewer AheB (1/2)** for more details.

sEEG signals differ significantly from EEG signals, and cross-subject decoding remains a challenging task. Achieving notable improvements with such a small amount of subjects is uncommon in prior studies [1,2] related to sEEG-based speech decoding. While the authors' effort to tackle this difficult problem is commendable and encouraging, the effectiveness of the proposed method is ultimately more critical than the story itself. Therefore, I maintain my original **reject** vote. Thanks for the authors' contribution to the field of sEEG-based tone decoding.

**Reference**:

[1] Zheng H, Wang H T, Jiang W B, et al. Du-IN: Discrete units-guided mask modeling for decoding speech from Intracranial Neural signals[J]. arXiv preprint arXiv:2405.11459, 2024.

[2] Chen J, Chen X, Wang R, et al. Subject-Agnostic Transformer-Based Neural Speech Decoding from Surface and Depth Electrode Signals[J]. bioRxiv, 2024.

[3] Buzsaki G. Rhythms of the Brain[M]. Oxford university press, 2006.

### Strengths
**Significance**: ~~**Open-source sEEG speech datasets are rare. Their promise of publishing the dataset upon acceptance (Line 780) is good news for the community as it will lower the entry threshold for future research.**~~ Additionally, they demonstrate how SSL-based pre-training allows improving performance compared to only supervised training (**doubtful**).

**Clarity**: The text has a good structure and is well-written. The figures also help in understanding the method.

### Weaknesses
 **Major**
1. The authors don’t mention the introduction of data augmentation (e.g., temporal jittering, additive noise, etc.) to avoid overfitting, a common strategy used in sEEG-based speech decoding [2,3]. Since the number of available trials (i.e., $\sim$1221 trials) within each subject is too small, I’m not sure whether the improvement of pre-training comes from this.

2. The preprocess details are missing. Could you provide a detailed description of sEEG preprocessing (i.e., from the originally collected sEEG signals at a sample rate of 2kHz to the epoched trials at a sample rate of 1kHz)? Specifically, it is unclear whether any referencing scheme, such as bipolar or Laplacian referencing, was applied to the raw sEEG data to mitigate common-mode noise and enhance the signal-to-noise ratio. The absence of such preprocessing steps could significantly impact the quality of the neural signals and the subsequent decoding performance.

3. In [1], their CNN baseline achieves about 40% on average, and their NAR model achieves 45.75% on average. All these methods are supervised (heterogeneous) baselines, and these results make it hard to assess the contribution of H2DiLR.

4. No code and demo dataset is provided. Without the code and data, it's difficult to verify the claims.

5. Some aspects of the method are undefined or unclear. Please see the Questions section below. These aspects need to be clarified in the manuscript.

**Minor**
1. Figure 1: It could mislead readers into thinking that H2DiLR uses Product Quantization. In Figure 3 and Section 3.3, the authors actually quantize each item in the embedding sequence using one of different codebooks. However, in Figure 1, the “disentangled embedding” suggests that different parts of each individual embedding are quantized with different codebooks.

2. Line 155: typo “LaBraM Anonymous (2024)”

3. Line 841: typo “the learning of 5e-5” should be “the learning rate of 5e-5”? Is the only difference between fine-tuning pre-trained models and training non-pretrained baselines the learning rate? Are all other settings the same?

4. Use `\citet` or `\citep` instead of `\cite` when referencing other works.

5. Since you collected a 407-syllable reading sEEG dataset, how does H2DiLR perform on other types of syllable classification tasks, such as initial syllable classification? Including these additional results might further highlight H2DiLR's effectiveness.

### Questions
1. Table 1: What is the codebook size of Heterogeneous H2DiLR with ($\nu=0$)? Is it `K=32`?

2. Did you use a different signal length for pre-training and downstream classification? Are there any differences between the pre-training dataset and the downstream classification dataset?

3. Line 879: Did you apply normalization to each channel independently (i.e., calculating the mean and standard deviation for each channel separately) or across all channels together?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors propose H2DiLR to capture both homogeneous and heterogeneous information from intracranial recordings across multiple subjects for lexical tone decoding. The H2DiLR framework first obtains discrete vectors through a reconstruction task (vq-autoencoding manner), then builds shared codebook and private codebook for the decoding of different subjects. Experiments on a newly acquired, not publicly released sEEG dataset show the H2DiLR method outperforms other baseline methods.

### Strengths
1. The motivation of this paper is clear. The authors seek to address a very important problem in brain decoding: dig homogeneity within the brain responses of different subjects, and hope the obtained homogeneity representation can help improve decoding performance. The presentation of this paper is also good.
2. The proposed vq-autoencoding based method outperforms previous models in decoding performance. Additional ablation analysis further confirms the effectiveness of model design.
3. The authors build a new sEEG dataset (promise to release if this paper gets accepted) which has potential to boost researches related to lexical tone decoding.

### Weaknesses
1. Since lexical tone decoding is not a very common task in the brain decoding area, I think the task / problem setting needs to be first introduced and defined in the methodology part.
2. The paper lacks analysis of the generalization ability of captured common representation, i.e. if the shared codebook of three subjects well generalizes to the fourth subject, and whether any three of the four subjects lead to similar shard codebook. The authors also mention this issue in limitations, but I think the dataset containing four subjects is enough to conduct such experiments.

### Questions
1. The usage of non-invasive brain recordings is an emerging topic. What's the performance of H2DiLR in decoding EEG signal?
2. Why the size of codebook and dimension of codebook are set as the same?

### Soundness
3

### Presentation
3

### Contribution
3
