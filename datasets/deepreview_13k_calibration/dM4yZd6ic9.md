# MAD: Multi-Alignment MEG-to-Text Decoding

- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 3, 3, 5, 6

## Abstract
Deciphering language from brain activity is a crucial task in brain-computer interface (BCI) research. Non-invasive cerebral signaling techniques including electroencephalography (EEG) and magnetoencephalography (MEG) are becoming increasingly popular due to their safety and practicality, avoiding invasive electrode implantation. However, current works under-investigated three points: 1) a predominant focus on EEG with limited exploration of MEG, which provides superior signal quality; 2) poor performance on unseen text, indicating the need for models that can better generalize to diverse linguistic contexts; 3) insufficient integration of information from other modalities, which could potentially constrain our capacity to comprehensively understand the intricate dynamics of brain activity.

This study presents a novel approach for translating MEG signals into text using a speech-decoding framework with multiple alignments. Our method is the first to introduce an end-to-end multi-alignment framework for totally unseen text generation directly from MEG signals. We achieve an impressive BLEU-1 score on the \textit{GWilliams} dataset, significantly outperforming the baseline from 5.49 to 10.44 on the BLEU-1 metric. This improvement demonstrates the advancement of our model towards real-world applications and underscores its potential in advancing BCI research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents **MAD**, an end-to-end framework for decoding MEG signals into text. They use a novel multi-alignment approach with audio and text representations. They present their results utilizing the GWilliams dataset showing high BLEU score on entirely unseen text. They highlight the framework's potential for generalization. They conduct comprehensive ablation studies that highlight the important of high dimensional representations alignment over direct text alignment for robust performance.

### Strengths
- **Clarity**: The paper is exceptionally well-written and easy to understand.
- **Novelty**: It introduces a novel multi-alignment approach that utilizes auxiliary modalities, such as Mel spectrograms, to enhance the translation of MEG signals into text. This work is notable for being one of the few that reports results without using teacher forcing.
- **Performance**: The method achieves state-of-the-art results on the BLEU-1 metric for this dataset.
- **Ablation Studies**: The paper includes comprehensive experiments and ablation studies that clarify the contributions of each model component, especially the loss functions and alignment mechanisms.

### Weaknesses
The residual connection in Figure 1 (b) is missing an arrow.
	The main experimental results in Table 2 have no advantage over RS and NeuSpeech, and are almost all lower except for B-1 and self-B.
	The brain module within Wav2vecCTC is not trained on text, so it exhibits poor performance and struggles to generate coherent words. The comparison is unfair.
	Baseline models should be compared both w/ and w/o tf.
	The paper aims to showcase the model's ability to generalize to unseen text, yet this attribute is not evident within the experimental setup presented. The paper solely conducts experiments on a test set with 46% overlap in words, which fails to represent unseen text. For a more thorough evaluation, it is crucial to compare the model with the baselines on both seen and unseen text separately. Furthermore, experiments should be conducted on additional datasets to enhance the validation of generalization.
	Ablation studies have demonstrated that L_t and LoRA are redundant and should be omitted from the model structure.

### Questions
- **Dataset**: Could you clarify your choice of dataset? Why did you select GWilliams instead of alternatives like Armeni (https://www.nature.com/articles/s41597-022-01382-7)? If the model is SOTA on unseen text, why not test it on other available datasets?

- **Inputs**: Can you explain how you transform a shifted 4-second window into a fixed-size sample for the Mel spectrogram?

- **Splitting**: Would it be possible to include experiments that demonstrate performance using different data splits (i.e., different combinations of the 4 stories)?

- **Multi-Modality Integration**: Could you elaborate on the challenges encountered when aligning MEG data with Mel spectrograms and hidden states?

- **Losses**: Can you provide the performance results when only using the Lt loss? Additionally, could you expand on the significance of the Le loss in this setup?

- **Discussion**: Could you elaborate on the other metrics used in your analysis? How does the performance behavior differ among them, and what insights do they provide to enhance the overall analysis?

- **Noise**: Would you consider experimenting with a model trained on noise, rather than merely evaluating it on noisy data?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a MEG2Text framework, which consists of a Brain Module and a Whisper Codec. MEG is initially decoded into a Mel spectrogram and subsequently translated into text using the Whisper model. The framework incorporates three alignments: low-level, high-level, and text-level alignments, which have potential inspiration for neural transcription.

### Strengths
1. The incorporation of a new modality in the MEG2Text translation is desirable.
2. High-level L_e loss is proven to be effective.

### Weaknesses
### Originality
- Brain activity (invasive and non-invasive) to speech/text translation has already been introduced in prior works, as summarized in section 2 (related work).

- The methodological contribution is incremental. 
Défossez et al. (2023) introduced the idea of aligning M/EEG signals with latent representations of a pre-trained ASR model (wav2vec2.0) with the CLIP loss. In the submission, the authors use a related approach (whisper encoder instead of wav2vce2.0, and MMD loss instead of CLIP). 
Yang et al. (2024) combined the whisper model with a convolutional adapter network (trained with AdaLoRa). In this submission, the authors propose a modified architecture that uses the brain module of (Défossez et al. 2023) as adapter network.

### Quality
- While I appreciate that the authors report results of the considered performance metrics for random effects (i.e., random shuffling and noise as input), their approach is insufficient to actually estimate the significance of the results. Instead of a single evaluation they should have used permutation testing (see e.g., Maris 2012) to estimate the metrics' distribution under the null hypothesis (i.e., no-relation between the MEG-derived text and the ground truth).

- Unlike (Défossez et al. 2023) and (Yang et al. 2024) the authors decided to analyze only one public dataset. I think the authors should have also analyzed the results for the (Schoffelen et al. 2019) dataset. Beyond that, the results lack quantification of the stability/variability of the results across random weight initializations.

### Clarity
- Figure 1(a) does not correspond to the proposed MAD model in Table 2.
This discrepancy suggests that the study might be affected by the double dipping problem (Kriegeskorte et al. 2009) in the sense that the authors tested many different configurations and then picked the final MAD model based on the test set result.

### Questions
1.	What is the purpose of random window shifting in line 304?
2.	How is cross-subject implemented in Section A.1? Why does it perform similarly to intra-subject despite having a different subject index input to the brain module?

### Soundness
2

### Presentation
2

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
The submission studies text decoding from brain activity based on a publicly available dataset that contains magnetoencephalography (MEG) recording of 27 subjects while they were passively listening to different stories.
Building upon recent prior work, the authors utilize a brain module and train it to predict mel spectrograms derived from the audio signals.
These MEG-derived mel spectrograms are then fed through a publicly available, pre-trained speech decoding model (whisper, OpenAI) to complete the MEG-to-text decoder.
The authors propose a combination of three loss terms with the aim to align mel spectrograms, latent speech encoder representations as well as decoder outputs and labels.
Given the small amount of data, they find that training merely the brain module parameters and freezing the remaining modules yielded best results (BLEU-1 of 10.44 % without teacher forcing) if the model was trained to align the latent speech encoder representations and the mel spectrograms.
Although the proposed method outperforms the considered baseline models, the overall poor performance (BLEU-1 values of approx. 10%) prevents practical utilization.

### Strengths
The paper can be classified as a combination of existing ideas.
In terms of architecture, the authors follow the idea of (Yang et al. 2024) and combine a convolutional network with a pre-trained whisper speech decoder; instead of standard convolution layers they propose to use the brain module of (Défossez et al. 2023).
As training objectives, they compare combinations of similar (and related) loss functions as proposed in (Défossez et al. 2023) and (Yang et al. 2024).

### Quality

I appreciate that the authors evaluated the models on unseen stories and put substantial effort in assessing the significance of the results. They compare the obtained results against shuffled data and models with random inputs.

### Clarity

The problem setting and the overall approach of the contribution are clearly communicated.

### Significance

The work confirms that pre-trained speech models (e.g., whisper here or wave2vec in (Défossez et al. 2023)) are helpful to extract a significant amount of language information from non-invasive brain activity (MEG here). Yet, the reported generalization results to unseen stories (Table 2) and subjects (Table 5) are discouraging.

### References

A. Défossez, C. Caucheteux, J. Rapin, O. Kabeli, and J.-R. King, “Decoding speech perception from non-invasive brain recordings,” Nat Mach Intell, Oct. 2023, doi: 10.1038/s42256-023-00714-5.

Y. Yang et al., “NeuSpeech: Decode Neural signal as Speech,” Jun. 03, 2024, arXiv: 2403.01748.[Online]. Available: http://arxiv.org/abs/2403.01748

### Weaknesses
### Originality
- Brain activity (invasive and non-invasive) to speech/text translation has already been introduced in prior works, as summarized in section 2 (related work).

- The methodological contribution is incremental. 
Défossez et al. (2023) introduced the idea of aligning M/EEG signals with latent representations of a pre-trained ASR model (wav2vec2.0) with the CLIP loss. In the submission, the authors use a related approach (whisper encoder instead of wav2vce2.0, and MMD loss instead of CLIP).
Yang et al. (2024) combined the whisper model with a convolutional adapter network (trained with AdaLoRa). In this submission, the authors propose a modified architecture that uses the brain module of (Défossez et al. 2023) as adapter network.

### Quality
- While I appreciate that the authors report results of the considered performance metrics for random effects (i.e., random shuffling and noise as input), their approach is insufficient to actually estimate the significance of the results. Instead of a single evaluation they should have used permutation testing (see e.g., Maris 2012) to estimate the metrics' distribution under the null hypothesis (i.e., no-relation between the MEG-derived text and the ground truth).

- Unlike (Défossez et al. 2023) and (Yang et al. 2024) the authors decided to analyze only one public dataset. I think the authors should have also analyzed the results for the (Schoffelen et al. 2019) dataset. Beyond that, the results lack quantification of the stability/variability of the results across random weight initializations.

### Clarity
- Figure 1(a) does not correspond to the proposed MAD model in Table 2.
This discrepancy suggests that the study might be affected by the double dipping problem (Kriegeskorte et al. 2009) in the sense that the authors tested many different configurations and then picked the final MAD model based on the test set result.

### References

A. Défossez, C. Caucheteux, J. Rapin, O. Kabeli, and J.-R. King, “Decoding speech perception from non-invasive brain recordings,” Nat Mach Intell, Oct. 2023, doi: 10.1038/s42256-023-00714-5.

Y. Yang et al., “NeuSpeech: Decode Neural signal as Speech,” Jun. 03, 2024, arXiv: 2403.01748.[Online]. Available: http://arxiv.org/abs/2403.01748

J.-M. Schoffelen, R. Oostenveld, N. H. L. Lam, J. Uddén, A. Hultén, and P. Hagoort, “A 204-subject multimodal neuroimaging dataset to study language processing,” Sci Data, vol. 6, no. 1, p. 17, Apr. 2019, doi: 10.1038/s41597-019-0020-y.

E. Maris, “Statistical testing in electrophysiological studies,” Psychophysiology, vol. 49, no. 4, pp. 549–565, 2012, doi: 10.1111/j.1469-8986.2011.01320.x.

N. Kriegeskorte, W. K. Simmons, P. S. F. Bellgowan, and C. I. Baker, “Circular analysis in systems neuroscience: the dangers of double dipping,” Nat Neurosci, vol. 12, no. 5, pp. 535–540, May 2009, doi: 10.1038/nn.2303.

### Questions
### Methods
- Please use consistent symbols for the same concept (for example either $n$ or $N$ for the batch size)
- $\phi$ is not defined in (2)
- line 304: define the random shifts. Were they samples from the interval $[-0.5, 0.5]$ or the set $\{-0.5, 0.5\}$?
- the considered baseline method `Wav2vec2CTC` was not proposed in (Défossez et al. 2023). 


### Wording, Grammar and Organization
- citation formatting: please use the `\citep` and `\citet` latex commands appropriately.
- line 42: "letter" -> "letters"
- line 201: "don't" -> "do not"
- lines 207 to 208: grammar issues
- line 231: "in default" -> "by default"
- some references miss important information (e.g., the journal). Please check thoroughly.


### References

A. Défossez, C. Caucheteux, J. Rapin, O. Kabeli, and J.-R. King, “Decoding speech perception from non-invasive brain recordings,” Nat Mach Intell, Oct. 2023, doi: 10.1038/s42256-023-00714-5.

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
3

### Summary
This paper proposes a novel brain-to-text perceived speech decoding pipeline (MAD) that leverages alignments from multiple modalities. The key contributions highlighted by the authors are the ability of their framework to generalize to unseen text, eliminating the need for word time segmentation (e.g. teacher-forcing, pre-training, or via eye-tracker), and a performance analysis with a suite of metrics, ablation testing, and benchmarking against other models. A comparison of different modalities is possible due to the modular structure of their design.

### Strengths
The approach as a whole is novel and the reported performance is strong across metrics for both high level accuracy and low level semantic content. The inclusion of random gaussian baselines should be noted and adopted as standard for future decoding studies. The push for evaluations on unseen text is also laudable.

### Weaknesses
There appears to be some issue with citation formatting that should be fixed (see ICLR 2025 style guide), as well as a few grammatical issues. Additionally, the benchmarking comparison with Défossez et al. (2023) appears to be in bad faith. Instead of comparing the performance of their decoding framework against Défossez et al.'s model as originally designed, it seems as if the authors of this paper use only the brain model and then apply a decoding head in the style of their framework. Thus, it results in many of the generated unigrams being gibberish as opposed to actual words and greatly reduces whatever the real performance of the Défossez et al. model should be across all reported metrics. The original model from Défossez et al. returns the most likely segment of audio given the meg input and therefore always returns real words. The paper by Défossez et al. explicitly mentions the ability to decode segments not present in the training set. Thus, it is still reasonable to benchmark with the Défossez et al. model as originally designed. If the intention was to underscore that the model from Défossez et al. needs access to the segmented test audio while the proposed framework operates with MEG data alone, this could have been stated and the Défossez et al. model omitted from bechmarking comparison.

### Questions
Questions:
- Are there results of benchmarking of the proposed model against other SOTA models using different test splits (i.e. not for entirely unseen data)? or with the Défossez et al. model as originally proposed (i.e. classification with the unseen test audio)?

Suggestions:
- fix the citation styling (see section 4.1 of the Formatting Instructions for ICLR 2025 Conference Submissions)

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces MAD, an end-to-end multi-alignment framework for translating MEG signals to text. This framework addresses challenges related to decoding unseen text by aligning MEG data with speech and text modalities. Using the GWilliams dataset, MAD achieves improved performance in MEG-to-text generation compared to prior approaches. The study also examines the impact of different loss functions on decoding performance, offering insights that may aid in future optimization of MEG-based language decoding.

### Strengths
- This paper introduces a new open-vocabulary MEG-to-Text translation framework MAD, avoiding the teacher-forcing problem seen in previous models and using a more reasonable evaluation method.

- The experimental design is robust, including comprehensive ablation studies that underscore the advantages of multi-modal alignment.

- Explanations of the model architecture, data, and experimental setup are clear and well-structured.

- The model sets a new standard in MEG-to-Text decoding accuracy, showcasing the valuable potential for real-world BCI applications.

### Weaknesses
The primary concern is the limited dataset, as the experiments were only conducted on the GWilliams dataset, while the model was trained with MEG-Speech-Text modality pairs. Testing on a single dataset limits the model's robustness and generalizability claims.

### Questions
1.	Lack of Multi-Dataset Testing: The model is only evaluated on the GWilliams dataset, unlike related works such as NeuSpeech and Wav2vecCTC, which test on additional datasets like Schoffelen. Although the authors acknowledge risks of overfitting on small datasets and discuss generalizability, a practical demonstration on other datasets like Schoffelen would better validate the model’s transferability and robustness.
2.	Inference Process for Sliding Windows: The model uses 4-second sliding windows with a shift of 1 second, incorporating random shifts of ±0.5 seconds to generate training samples. However, it remains unclear whether the inference stage aggregates outputs across windows or applies additional processing steps. Moreover, this raises concerns about the effect of different window sizes on the decoding results, an aspect not explored in the paper.
3.	Ablation Study on Loss Functions: The ablation studies discuss three loss functions—high-level feature alignment ($L_e$), low-level feature alignment ($L_m$), and text alignment ($L_t$)—but do not provide concrete evidence of how each influences decoding results. Adding examples of decoding results under different combinations of these loss functions would provide valuable insight, especially in validating the importance of high-level and low-level feature alignments as argued by the authors.

### Soundness
3

### Presentation
3

### Contribution
3
