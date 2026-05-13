# Which pre-trained model is effective for speech separation ?

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
The effectiveness of the use of general audio pre-trained models to generate rep-
resentations suitable for speech separation has been explored in a previous study
Huang et al. (2022) with the main finding being that they provide minimal benefit
compared to features extracted without the models. The study hypothesised that
since the general audio pre-trained models were trained with clean audio dataset,
they are unable to generalize to noisy and mixed speeches hence not effective in
speech separation. This paper investigates this hypothesis by comparing the per-
formance of pre-trained model trained on contaminated speeches and that trained
on clean ones. We are interested in evaluating whether contamination leads to bet-
ter downstream performance. We also investigate if the type of input used to train
the pre-trained model impacts the quality of embeddings it generates. To sepa-
rate the sources, we propose a fully unsupervised technique of speech separation
based on deep modularization. Our findings establish that by injecting noise and
reverberation in the training dataset, the pre-trained model generate significantly
better embeddings than when clean dataset is used. Further, based on the model
presented here, working in short-time Fourier transform (STFT) results in bet-
ter features than using time-domain features. The proposed deep modularization
speech separation technique can improve SI-SNRi and SDRi by 1.3 and 2.7, re-
spectively, when mixtures contain less than four sources and improves the results
significantly for many source mixtures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an empirical study on the impact of the input feature choice and augmentation on speech separation as a downstream task. The pre-training is tailored to extract contrastive features.

### Strengths
The results presented in the paper reaffirm the established scientific consensus about the role of augmentation and its necessity. 
The paper presents a model for source separation as a downstream task. 
The idea of implementing source separation using pre-trained embedding extractor is though not novel but valuable.

### Weaknesses
While it's always valuable to have new data that supports existing theories and frameworks, it is not providing in an apparent manner novel  insights as it is generally understood in the field that augmentation helps with generalization and specifically in the field of audio enhancement it is a general practice to apply data augmentation.
The chosen downstream task is very much related to the pre-training, e.g., the research on contrastive predictive coding has already shown that using the loss used in the present paper leads to distinctive embeddings for different speakers. Hence, the power of the extracted embeddings doesn't seem to be conclusive from this downstream task.

### Questions
I appreciate the thoroughness of your work and how it reaffirms the established scientific consensus. It's always valuable to have new data that supports existing theories and frameworks. While the results presented appear to be in line with what is currently understood in the field, I'm curious to know if there are any aspects of your research that you believe could be built upon or explored further to uncover new insights or if there are any unique implications of your findings that might not be immediately apparent.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper describes a new variant of deep clustering for source separation and compares two different supervision signals for pre-training the encoder (same speaker vs simCLR-like dual augmentations) based on two different representations (STFT vs learned filterbank). These representations are then fed into a graph neural network that is further trained to cluster time-frequency points from the same speaker.

It is evaluated on several (clean, non-reverberant) mixtures of wall street journal sentences (wsj0-2mix, 3mix, 4mix, 5mix) along with other mixtures of LibriSpeech (Libri5Mix, Libri10Mix). The proposed system out-performs a number of systems described up until 2021, including SepFormer, SepFormer+DM, Wavesplit, Wavesplit+DM, and DeepCASA in terms of SI-SNR improvement and SDR improvement.

### Strengths
* The approach appears to perform quite well in comparison to existing methods.
* The literature review is very thorough and comprehensive
* The proposed work seems to be well motivated
* The experiments seem to be carried out carefully

### Weaknesses
In terms of clarity, I find the paper difficult to understand. One major point of confusion is the use of the term "frame" to, I believe, refer to individual spectrogram points. A frame of a spectrogram is an entire column, so it is not clear whether it is spectrogram points or spectrogram columns that are being clustered. Based on the results, I assume it is points, because clustering columns would not produce sufficient speech enhancement, but, for example, section 6.1 states "we divide a given speech in the training set into frames (chunks) of size 250 with 125 overlap between two subsequent frames." No units are provided for these numbers, but they appear to be columns of spectrograms. This critical detail is very unclear. The lack of explicit definition for the term "frame" and its relation to the input data (time-domain signal or spectrogram) makes it difficult to follow the methodology. It is unclear if the "chunks" of size 250 refer to time samples or frequency bins, and the overlap is also ambiguous in this context. This ambiguity is further compounded by the fact that the paper discusses both raw waveform and DFT transformed waveform inputs, making it unclear how the "frame" concept applies to each representation.

Additionally, the title of the paper suggests that existing pre-trained models (e.g., wav2vec 2.0) will be compared for speech separation. The abstract further argues that existing pre-trained models are trained on clean speech and so have trouble representing mixed speech. This line of reasoning is quickly abandoned, however, and a new model trained on a relatively small corpus is introduced instead of a large self-supervised model. The paper does not adequately justify why existing pre-trained models are not suitable, and the shift to a new model without a clear explanation is jarring. The motivation for training a new model on a relatively small dataset, given the availability of large pre-trained models, is not clear, and the paper lacks a thorough discussion of this design choice.

Several different loss functions are introduced, and it is not clear when each one is used. The paper introduces multiple loss functions without clearly delineating their specific roles in the training process. It is unclear which loss function is used for pre-training the encoder and which is used for the clustering stage. The relationship between these loss functions and their impact on the overall performance is not adequately explained, making it difficult to understand the training procedure.

The results tables from the appendix should be included in the main text because they include comparisons to baseline systems. The current tables need not be included and could be replaced by these. The current results tables lack sufficient context and comparison to baseline systems, making it difficult to assess the significance of the proposed method's performance. The inclusion of the more comprehensive tables from the appendix would provide a more complete picture of the method's performance relative to existing approaches.

The paper contains no paragraph breaks, making it unfriendly to read. The paper would be improved by removing some of the less relevant literature review to make space for proper spacing. Additionally, citations are all \cite{}, which are rendered as "Isik et al. (2016)" even when the entire citation should be in the parentheses. This effect can be achieved by instead using \citep{}, which will be rendered as "(Isik et al., 2016)". The lack of paragraph breaks significantly hinders readability, and the excessive literature review detracts from the core contributions of the paper. The improper citation format also contributes to the overall lack of polish.

### Questions
What do you mean by "frame"? And if it is indeed a traditional frame (i.e., spectrogram column), then is separation performing within frames or each frame is assigned to a single source entirely?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper compares the performance of pre-trained models trained on contaminated speeches versus those trained on clean ones for speech separation tasks. The author evaluates whether training on contaminated audio leads to better downstream performance, and also
investigates the impact of the type of input used for training on the quality of embeddings generated by the pre-trained model.
The key findings of the paper are 1. Pre-trained models trained with noise and reverberation generate significantly better embeddings than those trained with clean datasets. 2. Using short-time Fourier transform (STFT) features is more effective than using time-domain features. In terms of the separation approach, a fully unsupervised technique of speech separation based on deep modularization is proposed.

### Strengths
- Claimed by the authors, general audio pre-trained models offer only marginal improvements in speech separation compared to features derived without these models. This limited efficacy might stem from the models being trained on clean audio datasets, rendering them less adept at handling noisy and mixed speech environments. Exploring whether incorporating more diverse, noise-contaminated data into the training could enhance their performance, particularly for tasks like speech separation, presents an intriguing avenue of research.

- A novel speech separation model has been introduced, which utilizes features from pre-trained models within a graph-based framework. 

- The model has undergone ablation studies involving scenarios with more than two speakers. These studies have generated considerable interest and enthusiasm among the audience.

### Weaknesses
The main weaknesses of the paper lie in several aspects listed as follows:

- Missing Key References: The paper overlooks crucial literature related to the use of noise and reverberation in pre-training, particularly the WavLM-based pre-trained model as discussed in Chen et al. ("Wavlm: Large-scale self-supervised pre-training for full stack speech processing." IEEE Journal of Selected Topics in Signal Processing 16.6 (2022): 1505-1518.). Additionally, relevant studies on speech separation using WavLM, such as Chen et al.'s work ("Speech separation with large-scale self-supervised learning." ICASSP 2023), are not cited. These omissions are significant as these works also concluded the beneficial impact of noise and reverberation.

- Lack of Baseline System: The paper is not able to provide baseline performance for the comparable downstream speech separation model. This absence hinders readers' ability to effectively assess and compare the proposed model's effectiveness.



### Questions
- Elaborating more on the limitations of the study, as noted above, is crucial for a comprehensive understanding.
- Incorporating an analysis of run-time factors would significantly enrich the paper, considering the typically high computational costs associated with pre-trained models. 
- The rationale behind selecting CONDEEPMOD as the pre-trained model remains ambiguous. The paper would benefit from a more detailed justification of this choice.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper investigates using pre-trained models to generate representations for speech separation, hypothesizing that models trained on noisy/reverberant speech will perform better than ones trained on clean speech. They propose a fully unsupervised speech separation technique based on deep modularization that avoids permutation ambiguity. Through experiments, they find that contaminating the pre-training data with noise/reverberation improves performance, as does using STFT features over time-domain, and their proposed technique performs well on separations with varying numbers of speakers.

### Strengths
1. The authors introduced contrastive learning and deep modularization networks into the domain of speech separation. They employed models pre-trained on a training dataset to extract features and accomplish speech separation tasks. Experimental results indicate a commendable quality of separation.

2. The authors employed the deep modularization network method to maximize the separation of mixed speech signals. Compared to other separation models, their approach achieves superior results in situations with multiple speakers.

### Weaknesses
1. While the authors claim to explore the influence of pre-trained models on the separation task, the paper appears more akin to a two-stage training paradigm leveraging contrastive learning. Conventionally, pre-trained models refer to general-purpose speech models, such as Wav2vec and WavLM. The authors do not adequately justify why these established models are insufficient for the task at hand, instead opting to train their own using contrastive learning. This approach deviates from the typical use of pre-trained models and should be more clearly motivated.

2. The two core contributions of this paper are the pre-trained model using contrastive learning and the deep modularization network. Firstly, I believe the authors should demonstrate the significance of the pre-trained model for the separation task. The authors displayed in Table 1 the impact of different pre-trained inputs on performance when using a deep modularization network. This perspective might be narrow, as it may be specifically tailored for this network structure. Comparative evaluations with other separation networks like Conv-TasNet and DPRNN are warranted. Secondly, the authors should contrast the use of existing pre-trained models combined with the deep modularization network to underscore the network's significance. Without this comparison, it is difficult to ascertain whether the performance gains are due to the pre-training approach or the modularization network itself.

3. The authors' claim of using an unsupervised method seems to be imprecise. During the pre-training phase, the Encoder has already acquired all the single speaker information from the training set. If the approach were genuinely unsupervised, the mixed signals should be used during the pre-training phase. The current methodology appears to be more of a self-supervised approach, where the model learns from labeled data (single speaker signals) to perform a downstream task (separation of mixed signals). This distinction is crucial and should be accurately represented.

4. The paper contains some typographical errors and figure reference inaccuracies. For instance, all equations should be followed by punctuation, "equation 3" in Figure 1 should be "equation 2", and in Section 4, "$A_{ij}$ iff" should be corrected to "if". I hope the authors can meticulously address these mistakes.

### Questions
1. Given that the authors utilized speech signals with noise and reverberation as inputs for the pre-trained model, can their method separate mixed signals that contain noise or reverberation? For instance, have experiments been conducted on datasets like WHAM! or WHAMR!?
2. I perceive the clustering parameter 'k' as a pivotal hyperparameter. Is it possible to evaluate the model's performance under various 'k' values?
3. Considering that, for example, TF-GridNet can achieve an SI-SNRi=23.4 on WSJ0-2mix, the authors' method of pre-training followed by separation is inherently more intricate. How do the authors rationalize this complexity?
4. The datasets used by the authors have a 100% overlap. Does the deep modularization network proposed by the authors remain viable for data with varying degrees of overlap?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
