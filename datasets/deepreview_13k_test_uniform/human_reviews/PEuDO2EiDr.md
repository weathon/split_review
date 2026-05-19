# RTFS-Net: Recurrent Time-Frequency Modelling for Efficient Audio-Visual Speech Separation

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Audio-visual speech separation methods aim to integrate different modalities to generate high-quality separated speech, thereby enhancing the performance of downstream tasks such as speech recognition. Most existing state-of-the-art (SOTA) models operate in the time domain. However, their overly simplistic approach to modeling acoustic features often necessitates larger and more computationally intensive models in order to achieve SOTA performance. In this paper, we present a novel time-frequency domain audio-visual speech separation method: Recurrent Time-Frequency Separation Network (RTFS-Net), which applies its algorithms on the complex time-frequency bins yielded by the Short-Time Fourier Transform. We model and capture the time and frequency dimensions of the audio independently using a multi-layered RNN along each dimension. Furthermore, we introduce a unique attention-based fusion technique for the efficient integration of audio and visual information, and a new mask separation approach that takes advantage of the intrinsic spectral nature of the acoustic features for a clearer separation. RTFS-Net outperforms the prior SOTA method in both \textbf{inference speed} and \textbf{separation quality} while reducing the number of parameters by \textbf{90\%} and MACs by \textbf{83\%}. This is the first time-frequency domain audio-visual speech separation method to outperform all contemporary time-domain counterparts.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors present a novel time-frequency domain audio-visual speech separation method (Recurrent Time-Frequency Separation Network), a unique attention-based fusion technique for the efficient integration of audio and visual information, and a new mask separation approach. Results show that the proposed approach outperforms the previous SOTA method using only 10% of the parameters and 18% of the MACs. The authors claim that this is the first time-frequency domain audio-visual speech separation method to outperform all contemporary time-domain SOTA ones.

### Strengths
One main strength of this paper is the proposed Recurrent Time-Frequency Separation Network that processes the data in the frequency dimension, the time dimension, and the joint time-frequency dimension.

### Weaknesses
It is mentioned that the RTFS blocks share parameters (including the AP Block), leading to reduced model size and increased performance. Therefore, more description/explanation for this would be helpful.

### Questions
Are there any overlapping speech in the train/test data?
Do the authors perform any downstream task like speech recognition on the reconstructed speech?
One possible downstream task for speech separation is speech-to-speech dubbing. In this case, both the speech and background/nonspeech sound are needed. Have the authors looked into reconstructing background/nonspeech sound?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes RTFS-Net, a new time-frequency (TF) domain audio-visual speech separation method. It introduces three main innovations:

* RTFS Blocks independently model time and frequency dimensions of audio
* Cross-dimensional Attention Fusion Block efficiently fuses audio and visual data
* Spectral Source Separation Block preserves phase/amplitude information

Experiments show RTFS-Net matches or beats prior time domain methods on LRS2, LRS3, and VoxCeleb2 datasets, while using 10x fewer parameters and 3-6x fewer computations.

RTFS-Net is the first TF model to surpass most contemporary time domain methods for audio-visual speech separation. It demonstrates TF domain methods can achieve good performance at lower computational cost through novel modeling of time-frequency spectrograms.

### Strengths
* Achieves near state-of-the-art performance for audio-visual speech separation while being very parameter and computationally efficient
* Outperforms all compared time domain methods, proving time-frequency domain modeling can achieve better performance if done effectively
* Innovative modeling of time and frequency dimensions independently in RTFS Blocks
* Attention-based fusion mechanism in CAF Block is very lightweight but fuses audio and visual data very effectively
* Spectral Source Separation Block properly handles phase/amplitude to avoid losing audio information
* Model code and weights will be released for full reproducibility

### Weaknesses
* Testing is limited to only 2 speaker mixtures. Performance with more speakers is uncertain.
* Missing PESQ evaluation in results which most other target speech extraction papers provide
* Doesn't include latest SOTA model comparison: Dual-Path Cross-Modal Attention for Better Audio-Visual Speech Extraction, ICASSP 2023.
https://arxiv.org/pdf/2207.04213.pdf. This gives superior performance for SI-SNRi and provides PESQ results as well. It does not provide MACs analysis.

### Questions
None

### Soundness
3 good

### Presentation
3 good

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
The authors build upon previous research in audio-only and audio-visual speech recognition by focusing on improving efficiency and fidelity of separated speech. They draw a lot of inspiration from the CTCNet paper and extend it to the TF domain to improve the efficiency. The solution has been evaluated on standard benchmark datasets and compared to previous state-of-the-art methods.

### Strengths
1. Audio samples of separation are available and source to be made available when the paper is published.
2. The writing is easy to follow.
3. Clear modeling details are provided.

### Weaknesses
1. The baseline methods listed in table 1 should include their references.
2. RTFS-Net-12 is only about 10% more efficient that CTCNet. How much difference does that make in practical applications?
3. Some of the comparison examples are not distinguishable to this reviewer. This makes me wonder how to interpret the relative SNR gains.

### Questions
1. Since the best performance is achieved with R=12, why not explore a higher R?
2. Have the authors considered conducting studies with human listeners? If the target application is ASR, would it be helpful to measure WER in a recognition task?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a novel Recurrent Time-Frequency Separation Network architecture that performs audio-visual source separation tasks effectively and efficiently. The model is characterized by three parts. First, each modality goes through its own processing module, and then the cross-dimensional attention fusion (CAF) consolidates information from both modalities. The spectral source separation block performs masking-based separation. The separation results show promising improvement given the compact size and computational efficiency the new model architecture introduces.

### Strengths
- The paper presents solid improvement compared to the existing baseline systems. Considering the amount of model compression the proposed model introduced, the improvement is significant.

- All the procedures and modules are well-defined with enough details.

- The choice of the model architectures makes sense, including the dual-path structure, attention-based consolidation, and complex masks.

- Ablation studies are thorough.

### Weaknesses
While the paper is packed with useful information, there are still some parts that need elaboration.

- As the authors mention, the dual-path RNN idea is not new to this problem. I understand that the authors chose SRU for their complexity-related considerations, but I also wonder if the audio processing module could benefit from its own self-attention mechanism, such as in the SepFormer model. 

- The spectral source separation module might be the weakest contribution, because complex masks have been extensively studied in the audio-only source separation literature. 

- I wish the paper provides more details on the TDANet block for video processing, which is relegated to the reference in the current version.

### Questions
- The authors chose to "add" f_1 and f_2 (eq 11) after the CAF processing. I think it's a little abrupt in the sense that there might be other choices that preserve the unique information that each vector learns, such as concatenation. Have the authors considered other ways to combine the two vectors?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
