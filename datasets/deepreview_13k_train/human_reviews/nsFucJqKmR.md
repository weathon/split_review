# DASB-Discrete Audio and Speech Benchmark

- Decision: Reject
- Scores: 6, 3, 6, 3

## Abstract
Discrete audio tokens have recently gained considerable attention for their potential to connect audio and language processing, enabling the creation of modern multimodal large language models.
Ideal audio tokens must effectively preserve phonetic and semantic content along with paralinguistic information, speaker identity, and other details. 
While several types of audio tokens have been recently proposed, identifying the optimal tokenizer for various tasks is challenging due to the inconsistent evaluation settings in existing studies. 
To address this gap, we release the Discrete Audio and Speech Benchmark (DASB), a comprehensive leaderboard for benchmarking discrete audio tokens across a wide range of discriminative tasks, including speech recognition, speaker identification and verification, emotion recognition, keyword spotting, and intent classification, as well as generative tasks such as speech enhancement, separation, and text-to-speech.  %We propose a framework using task-specific lightweight prediction heads on top of a frozen shared audio encoder, with an audio decoder employed to transform predicted tokens into audio for generative tasks. 
Our results show that, on average, semantic tokens outperform compression tokens across most discriminative and generative tasks. However, the performance gap between semantic tokens and standard continuous representations remains substantial, highlighting the need for further research in this field.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- The authors offer a benchmark for evaluating the quality of neural audio codecs and assessing their impact on various downstream tasks.
- These downstream tasks encompass several standard audio processing applications, including speech, sound, and music.

### Strengths
- This is an open-source project dedicated to enhancing the quality of neural audio codecs, which are becoming increasingly valuable to the community as their importance grows.
- It provides an exciting opportunity to benchmark performance across a variety of downstream tasks—not only for speech but also for broader audio and music applications

### Weaknesses
 - I've noticed a surge in similar open-source projects released recently—some of which were published after the ICLR submission deadline, highlighting the relevance of this work. However, I have some concerns regarding its future adoption. To encourage broader usage, it might be beneficial to emphasize the unique advantages of this repository and clarify why researchers would prefer it over others. For instance, a comparison table could be added to showcase its strengths in contrast to similar projects.

Examples of recent related works include: [1] Wu, Haibin, et al. "Codec-SUPERB@ SLT 2024: A lightweight benchmark for neural audio codec models." arXiv preprint arXiv:2409.14085 (2024). [2] Shi, Jiatong, et al. "ESPnet-Codec: Comprehensive Training and Evaluation of Neural Codecs for Audio, Music, and Speech." arXiv preprint arXiv:2409.15897 (2024).

- Inference time may be quite lengthy, potentially taking up to 8 hours for tasks like ASR. Providing a smaller development set for quick experiments could be a valuable addition.

### Questions
- In addition to the GitHub repository, do the authors plan to provide a leaderboard for tracking and comparing results?
- Would it be possible to include a comparison of computational costs as well?
- Do the authors have plans to add support for higher sample rates in future comparisons?
- Since a codec might perform well on one downstream task but poorly on another, what approach would you recommend to achieve balanced results for selecting a universally effective codec?

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
This article provides a benchmark of discrete tokens of speech and audio on comprehension and generation tasks. This paper divides tokens into three categories, namely semantic, compression, and hybrid. Through a large number of experiments, the paper gives some conclusions.

### Strengths
1. The paper conducted plenty of experiments to evaluate the understanding and generation tasks of different types of speech tokens. 
2. The presentation is clear and the results are easy to follow.

### Weaknesses
1. Training data of different types of tokens is different, in addition, the decoders(Vocoders) of semantic tokens are only trained on Librispeech 960. As a result, the horizontal comparison is not particularly fair, especially for music and sound. 
2. The amount of experiments in the paper is large, but there is no obvious insight. Most of the conclusions are already common sense, such as semantic tokens are good at content and compression tokens are good at paralinguistics. 
3. The experimental design and data of the paper are basically the same as SUPERB, Codec-SUPERB, and SUPERB-SG, with limited novelty.
4. I don't understand why in the author's experiment, the high bit rate is not as good as the medium one. I suspect there is some kind of implementation or hyperparameter setting problem.

### Questions
1. What is the continuous baseline? it doesn't seem clear. 
2. Why are the SI and SV performance of SSL baseline best? It feels a little weird because they are semantic features.

### Soundness
2

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
3

### Summary
This paper presents DASB, a benchmark for evaluating discrete speech and audio units. DASB consists of several discriminative and generative tasks, including speech recognition, emotion recognition, speech enhancement, text-to-speech synthesis, etc. It provides a unified pipeline for leveraging different discrete units to perform these tasks. Preliminary evaluation results indicate that units derived from self-supervised learning models generally outperform codec units and that continuous representations significantly outperform discrete units.

### Strengths
This paper presents a benchmark for evaluating the direct use of discrete speech and audio units. The authors have constructed a unified pipeline along with open-source implementations, making it convenient for researchers to conduct various experiments using the benchmark. I anticipate that this benchmark will enable fair comparisons in future research on discrete speech and audio units. The evaluation results appear mostly reasonable. The presentation is clear and easy to read.

### Weaknesses
Although the authors present DASB as an audio and speech benchmark that includes both speech and audio tasks for evaluation, the number of audio tasks is rather limited, and there are fewer relevant descriptions regarding the development of audio and music units. Additionally, the models used in the experiments are limited. For example, I believe there have been several works on hybrid tokenizers, but in the experiment section, only SpeechTokenizer is included.



### Questions
1. In the abstract, the authors use the terms "semantic" and "compression" tokens, whose definitions do not appear until Section 3.1. Therefore, I was a bit confused when reading the abstract (though I could still guess to some extent). It would be helpful if the authors could elaborate more on this.

2. I believe there have been several studies on hybrid tokens this year, but only SpeechTokenizer is included. This type of token is a very active area of research. Is there a chance of providing more results in this category?

3. At the beginning of Section 4, there is an error in the Appendix index. Please fix it.

4. Which continuous SSL models are used exactly in Tables 2, 3, and 4?

5. In ASR, the authors include two low-resource languages. I wonder if there are any specific reasons for choosing them. The evaluation results on these two languages are very poor across the models, and I think that instead of directly comparing them at this level, using phoneme recognition could lower the difficulty of the task and provide more comparable results.

6. For speech generation tasks, the authors use automatic MOS prediction models to evaluate the quality of generated speech. I understand that this is mainly because MOS involves human effort, and it is infeasible to use only the original MOS in a benchmark. However, as far as I know, the correlation between automatic MOS models and human ratings is still limited. Could you provide the correlation of these results with human ratings?

7. In Tables 5 and 6, the discrete SSL parts are all replaced with CNN14 and MERT. Is there a chance to add results on the discrete HuBERT and WavLM? This could help test the generalizability from speech to audio and music.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces DASB, a benchmark for testing how well different architectures that generate "discrete" audio tokens perform in speech- and audio-related tasks. The benchmark include both discriminative tasks (e.g., ASR or classification) and generative ones (e.g., speech enhancement and TTS). 

The paper clarify that the goal is to test different types of tokens, semantic-based, compression-based and hybrid. It tests several models on the benchmark in those three categories. For compression-based tokens it investigates how the bitrates affect token quality. In the results, however, there is no clear evidence of better models given by higher bitrates.

The main goal of the paper can be summarized as the definition of a standard ways to evaluate tokens generated by different SSL models that have been pretrained for different tasks and using different approaches (i.e., codec, wav2vec2-style mainly).

### Strengths
1. The paper addresses an important issue in emerging areas of Audio Representation Learning: evaluating the quality of representations, in this specific case given by discrete tokens. 
2. The benchmark actually covers a broad set of speech-related tasks (e.g., ASR, classification with keyword spotting and intent classification, speaker identification and so on). It also include TTS and Speech Enhancement tasks as generative tasks.
3. The paper propose a straightforward explanation of each task and the architecture setup personalized by the paper for the task at hand. The paper clearly mention the dataset used for the evaluation.

### Weaknesses
1. The main goal of a benchmark framework should be to fairly assess the quality of the tested models. However, the current version of the evaluation design, while broad in terms of tasks, include multiple trainable components for each task making very hard to isolate the evaluation of the token quality. This issue is even more puzzling because the results are reported as a single run of a model instead of averaging multiple runs and reporting standard deviations. The results may be influenced by several factors that may hinder the real comparison.
2. The benchmark design involved selecting specific metrics for each task. While the selection for most of them is standard (e.g., accuracy for classification), in other cases it may need discussion (e.g., why not PESQ instead of DNSMOS for speech enhancement?).
3. There are several experimental details that are missing. For example, the extraction of discrete tokens from WavLM and HuBERT involves a K-Means step, what is the value of K used in the paper? It may significantly influence all the experiments together with all set of other parameters (e.g., batch size, learning rate...). Are those hyperparameters consistent for all models? In addition, it is not clear what is the hardware used to train the downstream models, Is it consistent for all models? The paper make reference to the RTX 3070 GPU (8GB of VRAM) for computing time and memory requirements but then states in Appendix A1 "Every task runs on GPUs with 32 GB or more of VRAM".
4. The benchmark fails to reference existing benchmark that evaluate audio representations. It makes reference to SUPERB, however, the benchmark position itself as a general one (Discrete **Audio** and Speech Benchmark). There are several examples of general (including speech) audio representation frameworks [1][2][3]. The paper fails to compare with them leaving an unclear picture of DASB's specific contributions. In most of the downstream tasks, the model under testing is obtaining tokens -- that are then mapped back to "vectors" using codebooks, is thus only a matter of how those models are pre-trained (or discretized in the case of WavLM and HuBERT) that changes? Why evaluating them in an existing benchmark is not sufficient? DASB includes ASR and generative tasks (e.g., speech enhancement and TTS), is this the only difference in addition to the evaluated models?
5. Concerning audio events, the paper states "For sound classification, we utilized the pre-trained CNN14 model...", this is quite a difference with respect to other transformer-based models used all along the paper. Transformer-based SSL models exist pre-trained on general audio datasets (e.g., AudioSet)[2][4] and they are available open-source.

### Questions
1. How do you ensure that the benchmark isolates token quality when multiple trainable components are included?
2. Why were layers 1, 3, 7, 12, 18, and 23 selected for WavLM and HuBERT token extraction? This choice may appear arbitrary without reference to literature or specific validation.
3. The results lack practical takeaway. How do you plan the community to benefit from the insights obtained using DASB? There seems to be contrasting results (e.g., DAC vs Encodec) compared to recent papers [1] (e.g., on ESC-50); what could be the cause of these differences?
4. How DASB compares with existing benchmarks in the literature?
5. Do you notice any differences across multiple runs of the same model on specific DASB tasks? Can those differences influence the evaluation?
6. Are the experimental settings (in terms of hyperparameters) the same for all evaluated models?

[1] Ji, Shengpeng, et al. "Wavtokenizer: an efficient acoustic discrete codec tokenizer for audio language modeling." arXiv preprint arXiv:2408.16532 (2024).


Minor remarks:
- BERT is cited as an autoregressive model, how is it classified in this category?
- Mentioning Speech Enhancement with discrete tokens, the authors cited Deep Learning, the book from Goodfellow et al. (2016), the citation seems not pertinent.

### Soundness
2

### Presentation
3

### Contribution
1
