# Speech Robust Bench: A Robustness Benchmark For Speech Recognition

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
As Automatic Speech Recognition (ASR) models become ever more pervasive, it is important to ensure that they make reliable predictions under corruptions present in the physical and digital world. We propose \proposedFull (\proposed), a comprehensive benchmark for evaluating the robustness of ASR models to diverse corruptions. \proposed is composed of \numPert challenging speech recognition scenarios which largely cover the range of corruptions that ASR models may encounter when deployed in the wild. We use \proposed to evaluate the robustness of several state-of-the-art ASR models and observe that model size and certain modeling choices such as the use of discrete representations, or self-training appear to be conducive to robustness. We extend this analysis to measure the robustness of ASR models on data from various demographic subgroups, namely English and Spanish speakers, and males and females. Our results revealed noticeable disparities in the model's robustness across subgroups. We believe that \proposed will significantly facilitate future research towards robust ASR models, by making it easier to conduct comprehensive and comparable robustness evaluations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a comprehensive benchmark for automatic speech recognition (ASR) models. The benchmark aims to cover a large variety of real-world data-quality challenges for deployed ASR models.

To benchmark on clean speech, the authors use the Librispeech and TEDLIUM datasets.  
To benchmark on inter-personal speech, the authors use the CHiME-6 dataset.  
To benchmark on far-field speech, the authors use the AMI dataset.  
To benchmark on accented English, the authors use the Mozilla CommonVoice dataset.  
To benchmark on text-to-speech audio, the authors generate data using the model XTTS.  
To benchmark against adversarial attacks, the authors use utterance-specific and utterance-agnostic attacks.  
To benchmark against environmental effects, the authors add 1) white noise, 2) environmental noise, or 3) simulate echo and RIR.  
To benchmark against digital augmentations, the authors modify the audio data using most effects available in SoX.

The authors use the word-error-rate (WER) as the metric for clean speech. The metric for adversarial attacks is WER degredation (WERD). For all others, the authors use difficulty-normalized WER or WERD. The normalization is done based on a weight, which is an approximated speech quality given by a neural network.    

The authors apply their benchmark on popular ASR models and their variants, including Whisper, wav2vec 2.0, HuBERT, and Canary.
The following observations are made:
- Canary has the best performance on clean speech
- Whisper is robust against digital augmentations, echo and RIR, while Canary is not.
- Wav2vec 2.0 is robust against adversarial attacks. 
- There is a positive correlation between average robustness and amount of model parameters

Furthermore, the authors did an analysis on Spanish datasets with models fine-tuned (single-or multi-lingually) on Spanish. They find that multi-lingual models are more robust on English than Spanish.

Finally, the authors analyzed performance differences between male and female speakers. They observe it is data dependent.

### Strengths
### originality 

This work is combines multiple existing datasets to build a comprehensive analysis tool for ASR models. The authors place their work fairly into existing literature.

### quality 

The writing is mostly error-free and clear to understand. The authors analyzed relevant, contemporary ASR models. Nice-to-have but not required models to include could've been WavLM and, perhaps, OWSM.        

### clarity 

The authors use a familiar section lay-out for their paper. I also appreciate the take-away summaries in Section 4.    

### significance

I think this work can contribute to a better evaluation of ASR models. It is significant to the speech community to make it is easy for researchers to evaluate on data other than Librispeech test-clean and test-other.

### Weaknesses
### Benchmark protocol is unclear

Section 3 is missing important details for reproducing this work. I think practitioners cannot replicate the benchmark protocol by reading the paper as-is. It is critical for the usefulness of a benchmark that it can be independently reproduced. I have the following remarks:

1. I find the usage of the word 'Perturbations' unclear. I see how adversarial attacks, environmental effects, and digital augmentations can be classified as perturbations of the audio signal. However, I do not see how accented speech, computer generated speech, and inter-personal communication, can be seen as a perturbation. I would prefer the usage of "domain" over "perturbation". My suggestion would be to change the taxonomy (Figure 2) to include the domains clean/professional, social gathering, accented, text-to-speech, noise (with subgroups environment, digital augmentation), and adversarial.    
2.  It follows from 1 that is unclear to me exactly which dataset is used in which setting of the benchmark. I made a best guess in the summary above. For example, is environmental noise, or adversarial attacks, used only on Librispeech and TEDLIUM? Moreover, which split of Librispeech should be used? Only test-clean, or also test-other? Another example, which version of Mozilla CommonVoice is used? Do you filter out any data from CommonVoice if it is not labeled as 'accented'? I think the paper would be greatly improved by having a subsubsection for each domain/perturbation in Section 3.2, which list all details needed to generate the (exact) test set(s).  
3. I praise the authors for sharing an (omited) link to perturbed versions of the datasets. I think this benchmark should require to use these exact perturbed versions in the noise domain, otherwise comparisons are unfair. The paper currently does not touch upon this topic.
4. Section 3.2 does not include any information on the generation of adversarial perturbations. These details should be in the main text of the paper.
5. There is no information on which text is used to generate the text-to-speech audio. Moreover, it would be desirable for these generated audio files to be shared so everyone can test on the same data. 
6. Section 3.1 does not mention any Spanish datasets. Moreover, it is missing datasets for the noise domain (WHAM!, MUSAN, etc)
7. It is unclear to me whether this benchmark includes Spanish data, or whether this is simply an extra analysis from the authors. 
8. For reproducing the benchmark, it is required to have the speech perception weights of each utterance to calculate the NWER(D). 

### Confusing details in analysis

Section 4.1 mentions the use of DeepSpeech (which does not have open weights?) and speech-t5, these are not used in Table 1, only Figure 7. Moreover, Section 4.4 mentions the use of 4 more models, it would be more clear to include these in Section 4.1. 

It is unclear when WER or WERD should be used. From Table 1 I assume that you use NWERD for e.g., accent and text-to-speech data. I don't see how one can have an $X$ and $X_p$ audio sequence to calculate the WERD in these scenarios. 

### Figures and tables are difficult to read

I find Figure 4, 5 and 7 too small to read. As the page limit is 10, there should be enough room to increase the size without exceeding the page limit.  

### Editorial remarks

* I would advice the authors to use \citep instead of \cite. Currently, the reference style (other than in section 2.2) makes the text hard to parse. 
* Figure 3's space exceeds the bottom margin, and indents the texts on page 7 unnecessarily. 
* Table 1 and Table 2 have a different format. I would recommend the use of the booktabs package and no usage of vertical lines. 
* Appendix A is empty.
* Table 4 and Table 6 exceeds the page margin. 
* The citation of Canary (Elena Rastogueva) is incorrectly formatted, is missing data, and exceeds the page margin. 

#### Typos
- ln 41: is comphe.. -> are comphre...
- ln 107:  them -> those
- ln 161:  "others" does not fit here (Radford et al is in both)
- ln 346:  than -> compared to
- ln 472 (and others): the term accuracy is specific to classification, 'quality' is more appropriate to describe ASR predictions.

### Questions
1. Can the authors clarify, for each domain, what dataset(s) are used, specify their statistic (min/max/avg length, male/female, total number of utterances), exactly how a model is evaluated (WER, WERD, NWERD with speech quality weights from...) , and how the data is perturbed, if applicable?
2. Can the authors clarify whether Spanish data is included in the benchmark, or whether this is a separate analysis?
3. Can the authors clarify how weights for the DeepSpeech were obtained?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new benchmark data and pipeline to measure the ASR robustness under different perturbations. The proposed work has 4 components: 1. clean datasets and noise sources; 2. bank of perturbations; 3.ASR transcription extractions; 4. metric computations. Compared to existing benchmark pipeline, the authors claimed that “the proposed pipeline combines several benchmark datasets containing known noise sources to allow researchers to comprehensively evaluate the robustness of their models using a single benchmark”. During experiments, the authors evaluated a couple state-of-the-art ASR systems on the proposed benchmark, and conduct a series of analysis on robustness.

### Strengths
* The experiments are comprehensive. It considers a couple state-of-the-art ASR systems, and it analyzes adversarial/non-adversarial perturbations.
* It analyzed the correlation between different models in terms of robustness.  
* It analyzed the robustness of speakers from different sub-groups (accent, gender).

### Weaknesses
Although the analyzes are very comprehensive, the contributions/novelty are not clearly stated. According to the quoted claim above, it feels like the most significant contribution compared to prior work is having more noise sources? Please explain more about the contributions/novelty here. It would be helpful to have a table to compare between the proposed approaches with baselines on the diffs from the 4 modules.

### Questions
See Weaknesses section

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes SRB, a benchmark to evaluate the robustness of Automatic Speech Recognition (ASR) models. Extensive evaluations are conducted on several recent and popular ASR DNNs to analyze their robustness to non-adversarial and adversarial input perturbations,  and various sub-groups, namely English speech and non-English (Spanish) speech, and male and female speakers. From the above analysis, several conclusions are drawn.

### Strengths
1. The paper conducts extensive and detailed analysis to evaluate the robustness of recent ASR models. The Takeaways help develop robust ASR models.

### Weaknesses
1. While I appreciate the efforts to evaluate the robustness of recent ASR models, the paper offers limited novelty. I suggest that the authors compare their benchmarks to existing robustness metrics or frameworks in the ASR field. Specifically, the paper should clearly articulate how the proposed benchmark differs from existing benchmarks in terms of the types of noise, the diversity of acoustic conditions, and the specific evaluation protocols used. Without this, it's difficult to assess the unique contribution of this work.
2. To evaluate the robustness of ASR models, the current framework adds noise to clean speech data to evaluate the performance. How do recent ASR models perform in real-world noisy data? In other words, how can we evaluate the robustness of ASR models to real-world noisy data? The paper should address the challenge of evaluating ASR models on naturally occurring noisy speech, which often includes complex and non-stationary noise characteristics. The current approach of adding synthetic noise may not fully capture the complexities of real-world scenarios.
3. The paper lacks a discussion on strategies for improving robustness. It would be great if the authors could provide some sights or suggestions to improve the robustness. The paper should explore potential methods for enhancing ASR robustness, such as data augmentation techniques, noise-robust training strategies, or model architectures specifically designed for noisy environments. Without this, the paper remains primarily an evaluation study, rather than a guide for developing robust ASR systems.
4. The experimental sections of the paper need reorganization. I can not see a clear logic for the experimental parts. The experimental section lacks a clear narrative flow, making it difficult to understand the rationale behind each experiment and how they contribute to the overall findings. The authors should consider grouping experiments based on the research questions they address, and clearly state the purpose of each experiment.

### Questions
Listed in the weaknesses part

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes Speech Robust Bench, a benchmark framework for testing speech recognition models . It collects almost all speech variation techniques available in the field, with close connection with real-time application scenarios. Results on

### Strengths
1. The dataset description is very detailed and the related pipeline has been open-sourced, which is a decent contribution to the speech community.
2. The models covered in the field has been quite at the level of state-of-the-art.
3. The paper has answer to the critical question - "does the improvement come from additional variants from data or simply just MORE data?" in section 4.4, which is rare and good.

### Weaknesses
1. The reviewers think the presentation of the paper is good, but has room for improvement. Some of the extensive statistics and information (e.g. about attacks) can be enlisted or illustrated in the main text, rather than extensive text description in both main text and appendix; Some resulting figures (e.g. Figure 5) are hard to read; Also there are minor formatting issues.
2. One limitation of this work is lacking comparison or having initial attempts with some hybrid audio processing pipeline, especially based on its growing popularity on speech processing fields. In fact, applying noise and perturbation has been a long-time practice since Kaldi era.
3. It would be good if the authors can correspond the related earlier works onto the methods enlisted and highlight the differences and potential variants the authors covered.
4. The authors highlighted in the paper about multi-lingual scenario but in fact, only English and Spanish are covered, and the models are mostly mono-lingual. The authors may either remove such statement or want to conduct additional experiments using other languages and multi-lingual models for ASR (e.g. Google T5). This is not major problem though.

### Questions
The reviewer does not have explicit further questions apart from above commetns.

### Soundness
3

### Presentation
3

### Contribution
3
