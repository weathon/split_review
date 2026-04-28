# CerebroVoice: A Stereotactic EEG Dataset and Benchmark for Bilingual Brain-to-Speech Synthesis and Activity Detection

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 5, 6

## Abstract
Brain signal to speech synthesis offers a new way of speech communication, enabling innovative services and applications. With high temporal and spatial resolution, invasive brain sensing such as stereotactic electroencephalography (sEEG) becomes one of the promising solutions to decode complex brain dynamics. However, such data are hard to come by. In this paper, we introduce a bilingual brain-to-speech synthesis (CerebroVoice) dataset: the first publicly accessible sEEG recordings curated for bilingual brain-to-speech synthesis. Specifically, the CerebroVoice dataset comprises sEEG signals recorded while the speakers are reading Chinese Mandarin words, English words, and Chinese Mandarin digits. 
We establish benchmarks for two tasks on the CerebroVoice dataset: speech synthesis and voice activity detection (VAD). For the speech synthesis task, the objective is to reconstruct the speech uttered by the participants based on their sEEG recordings. We propose a novel framework, Mixture of Bilingual Synergy Experts (MoBSE), which uses a language-aware dynamic organization of low-rank expert weights to enhance the efficiency of language-specific decoding tasks. The proposed MoBSE framework achieves significant performance improvements  over current state-of-the-art methods, producing more natural and intelligible reconstructed speech. 
The VAD task aims to determine whether the speaker is actively speaking. In this benchmark, we adopt three established architectures and provide comprehensive evaluation metrics to assess their performance. Our findings indicate that low-frequency signals consistently outperform high-gamma activity across all metrics, suggesting that low-frequency filtering is more effective for VAD tasks. This finding provides valuable insights for advancing brain-computer interfaces in clinical applications. 
The CerebroVoice dataset and benchmarks are publicly available on Zenodo and GitHub for research purposes.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents CerebroVoice, a bilingual brain-to-speech synthesis dataset featuring stereotactic EEG recordings of Chinese and English words and digits. The dataset is benchmarked for two key tasks: speech synthesis and voice activity detection. Additionally, the authors introduce a novel framework, Mixture of Bilingual Synergy Experts (MoBSE), which employs low-rank expert weights tailored for language-specific decoding tasks. The proposed MoBSE framework demonstrates superior performance compared to the baseline FastSpeech 2 model.

### Strengths
1) This paper tackles a highly under-explored area, largely limited by the scarcity of curated datasets, by introducing a publicly available bilingual brain-to-speech dataset that holds significant potential for advancing research in this field.

2) The authors propose the MoBSE framework for brain-to-speech synthesis, which achieves improved performance over the FastSpeech 2 baseline.

### Weaknesses
1) The authors explain the advantages of stereotactic EEG over ECoG; however, these invasive methods have limited practicality due to the complexity of data collection. It would be beneficial if the authors addressed why surface EEG, a non-invasive alternative, was not used instead in their study.

2) In Subject 1, electrodes were implanted in the right hemisphere, while in Subject 2, they were implanted in the left. However, both hemispheres could contribute to speech production, suggesting that electrodes should ideally be placed in both hemispheres for each participant. Additionally, data collection was limited to only two participants, which restricts the generalizability of the models built with this dataset.

3) The paper uses only one baseline, based on the FastSpeech 2 architecture, which is primarily designed for text-to-speech tasks. However, there are existing models in the literature for synthesizing speech from invasive and non-invasive multi-channel EEG signals, such as [1], [2], and [3], etc. These models could have been used as baselines for more comprehensive benchmarking of the dataset and comparison with the proposed MoBSE framework.

4) Although the paper focuses on speech synthesis and reports using a Hifi-GAN vocoder for generating speech, it does not present any results for the synthesized audio output. To fully assess the quality of the reconstructed speech, it is essential to include both subjective evaluations (such as mean opinion score) and objective metrics (like mel cepstral distortion and root mean squared error).

5) The model architecture presented in Figure 3 is unclear. FastSpeech 2 typically processes text inputs, yet the authors are instead feeding multi-channel EEG signals to the model. The method for obtaining sEEG embeddings from these multi-channel EEG signals is not explained. Additionally, Figure 3 (c) lacks details regarding the structure of the Universal Expert module.

### Questions
1) When participants read words aloud, the movement of their vocal tract can influence the EEG recordings. Could the authors address this by using visual cues and having participants read the cues silently without the movement of the vocal tract?

Reason for the Rating (3: Reject): I recommend rejecting the paper post-rebuttal due to the lack of subjective evaluation against baseline Brain-to-Speech systems and the limited generalizability caused by the small number of participants in the dataset.

### Soundness
1

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
The paper presents a data set consisting of pairs of stereotactic EEG and speech signals recorded simultaneously and a set of experiments in the context of brain-to-speech synthesis aiming to provide a benchmark for further research in this area. The dataset comprises sEEG and speech signals from two participants, and the protocol included the repetition of auditory stimuli in two languages. The paper also analyses the voice activity detection problem from the sEEG signals. The paper uses a similar architecture to that of the FastSpeech2 TTS model but substitutes phoneme embeddings with a sEEG embedding layer and proposes an alternative way to codify the language information into the network through a MLP layer that weights the feature representation of the network depending on a one-hot-encoding vector that indicates one of two possible languages in the dataset.

### Strengths
The paper addresses a relevant topic and introduces a new open dataset that can help advance a field far from being consolidated and where the data is highly costly and complex to acquire.  It also provides relevant measures that can help objectively evaluate the improvement of further approaches in this field.

### Weaknesses
The general novelty of the work is limited. The introduced dataset is valuable and constitutes a significant contribution to the academic community because of its complexity, but with such a limited number of participants in the study, it is hard to consider this work a valid benchmark for the task.  Moreover, the proposed mixture of bilingual synergy experts component is not presented clearly, and the whole pipeline is not well presented.

I acknowledge the authors for addressing most of my questions. Still, the paper's main drawback is that the small number of samples is insufficient to support the authors' claims to consider the proposed dataset as a benchmark. Moreover, several results are inconclusive because they come from two different models (one per subject/electrode position), which makes the manuscript's contribution unclear. Therefore, I agree that, in its current state, the global score of the paper is below the acceptance threshold.

### Questions
- Why do the authors argue that other datasets can not be used for VAD if the labels for that task are obtained automatically?
- The authors assert that the audio quality was assessed and the recordings edited accordingly during the data curation process. Was this task performed subjectively? Who was in charge of this task? 
- Specifications of audio recording equipment were not included, which is relevant to analysis results and prevent biases in case future data fusion tests can be performed.
- The authors presented independent results per subject. Were these results obtained using a single model trained with data from the two subjects, or were also two models trained (one per patient)?
- Results regarding LFS, HGA, and BBS signals are confusing. There is no apparent coherence regarding frequency bands or between subjects' behavior. Why do the authors consider that these experiments provide a benchmark in this field, considering the scarcity of subjects, which limits the power of any analysis? 
- The organization of the paper could be improved. The meaning of LFS, HGA, and BBS features and the relevance of their evaluation should be presented in section 5.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces CerebroVoice, a new dataset for bilingual brain-to-speech synthesis and Voice Activity Detection (VAD) using stereotactic EEG (sEEG). It includes recordings from two bilingual participants who read Chinese Mandarin words, English words, and Chinese Mandarin digits. The authors developed a novel method called Mixture of Bilingual Synergy Experts (MoBSE) that uses a language-aware dynamic organization of low-rank expert weights and tested it against the FastSpeech2 baseline, setting a new benchmark for their dataset. They found that MoBSE performs better than FastSpeech2 in producing speech from neural recordings. Additionally, they reproduced three existing VAD methods and established benchmarks for VAD using CerebroVoice. The dataset is publicly available on Zenodo, and the preprocessing code can be found on GitHub.

### Strengths
-The authors introduce CerebroVoice, a publicly accessible sEEG dataset tailored for neural to speech synthesis and Voice Activity Detection (VAD). This is particularly significant given the scarcity of publicly available sEEG datasets and benchmarks, providing a valuable resource for researchers to compare and validate their methods, fostering progress in brain-computer interface applications.

-By incorporating bilingual data, specifically focusing on a tonal language, Chinese Mandarin, the dataset opens new avenues for research, addressing the complexities associated with tonal languages in brain-to-speech synthesis.

-The methodology for data acquisition is thoroughly and clearly explained, ensuring transparency.

-The authors introduce a Mixture of Experts (MoE)-based framework for neural-to-speech synthesis, which improves bilingual decoding by dynamically organizing language-specific experts. This novel approach outperforms the FastSpeech2 baseline, demonstrating its effectiveness.

-The authors address important ethical concerns related to patient privacy and the sensitive nature of invasive neural recordings, demonstrating a strong commitment to ethical research practices.

### Weaknesses
-The CerebroVoice dataset is limited by its small size, featuring only two participants and a repetitive, narrow vocabulary, which restricts its generalizability and raises concerns about potential overfitting. Its focus on simple speech synthesis tasks diminishes its flexibility for broader neuroscience research areas such as brain decoding and semantic reconstruction. Additionally, the task design lacks originality, as many similar speech synthesis/reconstruction objectives have been addressed in previous studies [1, 2, 3], Most existing invasive datasets can be requested from the authors while non-invasive ones are generally publicly available, reducing the novelty of CerebroVoice’s contribution to the field. To enhance its impact, the authors could consider expanding the dataset with more participants and a more diverse vocabulary and/or task in future work.

-The GitHub repository lacks implementations of the proposed models, hindering reproducibility and preventing other researchers from building upon the work. It would be beneficial for the authors to include model implementations, training scripts, and detailed documentation in their GitHub repository.

 -It is unclear how FastSpeech2 was adapted to produce audio from sEEG signals. The paper does not provide a detailed explanation of the training procedures, architectural changes, or loss functions used in adapting this text-to-speech model for brain-to-speech synthesis. Providing specific details about these adaptations would make the methodology more understandable and reproducible.

-The architecture of the experts within the MoBSE framework is not clearly explained, leaving gaps in understanding how the model functions. It does not specify how many experts were used in the MoBSE framework and lacks ablation studies to justify this choice, hindering the evaluation of the model's components.

-The evaluation primarily uses Pearson Correlation Coefficient (PCC). Including additional metrics like ESTOI (Extended Short-Time Objective Intelligibility) would provide a more comprehensive assessment of speech synthesis quality. This is a very common metric in speech synthesis/reconstruction tasks.

### Questions
Did you perform any statistical significance testing to confirm that the improvements of MoBSE over FastSpeech2 are meaningful?

Is there a reason why raw sEEG data is not provided alongside the processed data, allowing researchers to perform custom preprocessing and explore different frequency bands?

How and why is positional encoding used in the MoBSE framework? Can you provide more insight into its implementation?

Are there any samples of the reconstructed speech available for qualitative assessment?

How is VAD accuracy measured exactly? I'm trying to figure out if you chose a window of silence vs speech? how long was the window?

Have you considered combining electrode data from both subjects to create a "super subject" to enhance coverage?

Thanks,

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce a novel dataset, CerebroVoice (publicly available), for bilingual brain-to-speech synthesis and a neural architecture MoBSE, which utilizes a language-aware prior dynamic organization for efficient handling of language-specific decoding tasks.

**Dataset**: The audio stimulus set contains `50` different stimuli, including 30 Chinese Mandarin words, 10 Chinese Mandarin digits, and 10 English words. For each trial, one randomly selected audio stimulus is played; then, the patient is asked to repeat that word (or digit). The dataset includes `1600` trials (i.e., 29 trials per Chinese Mandarin word, 48 trials per Chinese Mandarin digit, and 24 trials per English word). In each trial, two kinds of brain responses are recorded, including listening and reading. Each trial lasts either `4` or `5` seconds and is paired with the corresponding audio recording.

**Model**: The authors propose MoBSE, which is similar to `model ensemble`. MoBSE uses an additional gating module to support the dynamical fusion of the outputs from different experts.

**Experiment**: Previous methods (e.g., FastSpeech2, EEGNet, STANet, EEGChannelNet) are compared. Besides, the authors conducted different ablation studies regarding sEEG settings (sEEG feature, subject, word categories, etc.).

**In summary, it seems like a dataset paper.**

-----------

**Summary**

I have throughly seen other reviewers' comments, I decide to decrease my score to 6. **This article is overall at a borderline level, and the author may consider collecting more data to further enhance the manuscript.**

 - the limited qualitative assessment, an extremely small number of participants in the dataset (only 3 subjects), compared to NeurIPS 2024 dataset paper Brain Treebank [1].
 - the lack of a detailed analysis based on existing datasets to demonstrate the value added from the new dataset (e.g., detailed distribution analysis and cross-dataset testing), compared to Edward Chang's NBE paper [2].

This work provides a sEEG alternative to ECoG-based bilingual speech dataset [2].

**Reference**:

[1] Wang C, Yaari A U, Singh A K, et al. Brain Treebank: Large-scale intracranial recordings from naturalistic language stimuli[J]. arXiv preprint arXiv:2411.08343, 2024.

[2] Silva A B, Liu J R, Metzger S L, et al. A bilingual speech neuroprosthesis driven by cortical articulatory representations shared between languages[J]. Nature Biomedical Engineering, 2024: 1-15.

### Strengths
**Significance**: Open-source sEEG speech datasets are rare. Their publishing of the dataset (Line 035) is good news for the community as it will lower the entry threshold for future research. Additionally, they demonstrate how different sEEG features (e.g., LFS, HGA, BBS) affect the performance of brain-to-speech synthesis and voice activity detection. These results may help future works on speech decoding.

**Clarity**: The text has a good structure and is well-written. The figures also help in understanding the method.

### Weaknesses
 **Major**
1. Why is common average referencing, instead of laplacian reference, used in BrainBERT[1] (for listening decoding) or bipolar reference used in Du-IN[2] (for speech decoding)? Could you provide brain-to-speech synthesis results based on either laplacian reference or bipolar reference? Although previous studies[3] on speech synthesis use common average referencing + HGA, the speech synthesis task has a trivial solution (the mel-spectrum distribution of human speech is easy to regress). Maybe I’m wrong, but with these additional results, we can gain a deeper understanding of the dataset. Could the authors include the results of brain-to-speech synthesis (i.e., Table 1) baesd on the preprocessed data after either laplacian reference or bipolar reference?

2. How about the results of word classification? CerebroVoice dataset includes at least `24` trials per words, it should be able to evaluate 30-way classification task (i.e., 30 Chinese Mandarin words). Could the authors include results on word-classification tasks (e.g., 30-way on Chinese words, 10-way on Chinese digits, 10-way on English words)?

**Minor**
1. Line 90: Additional publications the authors should be aware:
  - In Du-IN (https://arxiv.org/abs/2405.11459), their preprocessed dataset is open available.

Could the authors summarize these works in Table 1?

2. Line 99: Additional publications the authors should be aware:
  - In Feng et al. (https://www.biorxiv.org/content/10.1101/2023.11.05.562313v3), they also explore speech decoding based on tonal language (i.e., Chinese Mandarin).

Could the authors summarize these works in the Related Works?

### Questions
1. Line 162: What does “a Python-scripted audio playback and sEEG-marking mechanism” mean? At the onset of audio stimuli (not the participant’s audio), the system sends a marker to ths sEEG recordings to identify the onset of audio stimuli.

### Soundness
2

### Presentation
3

### Contribution
3
