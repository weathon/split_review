# A$^2$-Flow: Alignment-Aware Pre-training for Speech Synthesis with Flow Matching

- Decision: Reject
- Scores: 6, 5, 8, 3

## Abstract
Recent advances in speech synthesis have enabled highly natural and speaker-adaptive speech generation by leveraging large-scale transcribed datasets. However, requiring tens of thousands of hours of annotated speech is impractical in low-resource settings. Existing pre-trained speech models often utilize masked speech inpainting for pre-training and show strong performance on various speech generation tasks using limited task-specific data. Nonetheless, these models still require external alignment mechanisms or extensive additional training to learn alignment for alignment-aware tasks, such as text-to-speech (TTS). In this paper, we propose A$^2$-Flow, an alignment-aware pre-training method for flow matching models in speech synthesis. A$^2$-Flow integrates alignment learning directly into the pre-training process using discrete speech units, enabling the model to efficiently adapt to alignment-aware tasks without the need for separate alignment mechanisms. By embedding alignment learning into pre-training, A$^2$-Flow facilitates alignment-free voice conversion (VC) and allows for faster convergence during TTS fine-tuning, even with limited transcribed data, making it highly suitable for low-resource scenarios. Experimental results show that A$^2$-Flow superior zero-shot VC performance compared to existing models and matches state-of-the-art TTS performance using only a small amount of transcribed data. Moreover, we demonstrate that A$^2$-Flow can be more efficiently applied to alignment-aware speech synthesis tasks than existing pre-training methods, providing a practical and scalable solution for high-quality speech synthesis across diverse settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
A2-Flow is a zero-shot TTS model based on flow matching, which relies on self-supervised speech units from HuBERT for pre-training to implicitly align speech and duration. Subsequently, A2-Flow can perform speech synthesis without the need for separate alignment mechanisms  through fine-tuning with a small amount of text-speech paired data. Due to pre-training, A2-Flow can achieve alignment-free voice conversion and allows for faster convergence during TTS fine-tuning.

### Strengths
A2 Flow proposes using semantic tokens derived from unlabeled data for pre-training, aiming to align speech and text. This approach allows for zero-shot text-to-speech (TTS) synthesis using only a small amount of paired text-speech data, eliminating the need for separate alignment mechanisms. Additionally, due to the presence of pre-trained alignment, alignment-free voice conversion becomes possible.

### Weaknesses
The paper is somewhat helpful for community advancement, but I believe additional experiments could further demonstrate its validity and effectiveness. For example, some experiments like MOS, CMOS, and SMOS could be added to prove its effectiveness from a subjective perspective.



### Questions
- Can you explain how your overall speech duration predictor is designed, and whether it shows good robustness for shorter and longer texts? Additionally, when dealing with longer or shorter texts, is the alignment between your speech and text still stable?
- As iterations increase, will your WER and SECs-O metrics maintain a good level? Will there be a tendency to forget the alignment mechanism, or will they align with the E2TTS level? In this setting, will the improvements from pretraining still be superior to models like E2TTS?
- I've noticed that after feature extraction with HuBERT, there is a de-duplication step. Is this step intended to further align the text and semantic tokens? Would removing this step have a significant impact on the results?

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
The paper proposes a new way to pre-train an alignment-aware diffusion-based speech synthesis model. Instead of pre-training the model to inpaint the masked region without any conditions, the authors propose to train the models conditioned on deduplicated discrete HuBERT tokens and force the models to learn the alignment during training. The results show that the models can perform comparably to those without pre-training, all achieved without large-scale transcribed datasets. Additionally, the model can perform voice conversion directly after pe-training with high robustness and similarity to the reference speaker.

### Strengths
* **Originality**: The paper proposes a novel way to learn the alignment between phonetic representations and speech and shows that this pre-training scheme can transfer to high-quality text-to-speech synthesis with a small amount of transcribed data, while previous methods that do not incorporate alignment pre-training fails to do.

* **Quality**: The paper has compared various models and conducted extensive experiments to examine the effectiveness of its models against several baselines, including E2TTS, without pre-training in a small amount of transcribed data and multi-lingual settings. 

* **Clarity**: The paper has an excellent presentation of its methods and results, avoiding overcompcaliting with mathematical definitions, making it fairly easy to follow. 

* **Significance**: The paper has shown that it is possible to achieve comparable performance to the most recent duration-free E2TTS without a large amount of transcribed data.

### Weaknesses
The major weakness is the contribution of this work seems incremental and does not demonstrate significant improvement over previous methods based on the argument presented in the paper. It is unclear what this pre-training scheme brings compared to previous methods such as SpeechFlow and E2TTS. There are a few arguments where the proposed alignment-aware pre-training can provide some advantages over previous methods. However, none of these seems to be fully supported by the results in the paper and existing literature:

1. It can be argued that this pre-training scheme allows simple transfer learning without transcription of speech data for high-quality TTS. However, most existing large-scale TTS models do not rely on human-labeled data but instead use automatically transcribed data. For example, Chen et al. 2024 [1] trained E2TTS on Emilia [2], which is a 100k-hour multilingual dataset with transcriptions obtained through the ASR model WhisperX. Chen et al. 2024 show that E2TTS trained on ASR-transcribed data can obtain a WER of 2.95, which is not significantly different from 2.2 in the paper. Similarly, NaturalSpeech 3 [3] has achieved a WER of 1.81, even lower than ground truth with ASR-transcribed data. It is unclear whether this method is better than training directly on ASR-transcribed data from a practical point of view, either in terms of quality or training resources. For example, in Figure (b), E2TTS trained on transcribed data only needs to be trained for 700k steps to have comparable performance of A2-Flow pre-trained for 700k steps plus 150k fine-tuning steps. Since E2TTS can perform well on the ASR-transcribed dataset, this suggests that A2-Flow takes more time and resources for training while achieving similar performance as E2TTS. It would be helpful for the authors to demonstrate other performance advantages of A2-flow, such as comparing it to E2TTS trained on an ASR-transcribed dataset (which can also be considered unlabeled), or comparing the total amount of time and resources required for training (i.e., to show that the entire pipeline of pre-training + fine-tuning of A2-flow is more efficient than transcribing + training for E2TTS).

2. It can be argued that this pre-training scheme allows for transferring learning in low-resource settings where transcribed data is limited. However, this advantage is not well supported in the paper either. It is well known that fine-tuning for a different language requires much less data than training it from scratch [4,5]. It is unclear whether this method is better than training E2TTS on a transcribed English dataset (which is enormous) and then fine-tuning it on a low-resource dataset (for example, French with 280 hours of data).

3. It can be argued that this method removes alignment labels for TTS models compared to SpeechFlow. However, it is unclear whether the alignment labels are hard to learn to begin with. Forced alignment can be obtained with a CTC-based ASR model, and it is shown in HuBERT and WavLM that CTC-based ASR models can be trained with sufficiently high quality with limited labeled data (960 hours). The contribution of this work can be further enhanced if the author shows that SpeechFlow fine-tuned on CTC-based alignments obtained from a fine-tuning HuBERT on 960 hours of data is worse compared to A2-Flow without pre-defined alignments.

In addition, the subjective evaluations are rather weak. The authors only compared 19 samples of E2TTS and 9 samples of SpeechFlow and concluded that the model is comparable to E2TTS and better than SpeechFlow in Table 2, and no statistical significance is reported for this result. Most recent papers [1, 3] use at least 40 samples (including the E2TTS paper), so 9 samples are insufficient to establish statistical significance. Moreover, no subjective evaluation is conducted for naturalness but it is a common practice for evaluating the true performance of speech synthesis models, as most current objective evaluation metrics only correlate weakly with MOS. Since the authors claim to have reproduced E2TTS and SpeechFlow in the paper, the paper's argument can be further enhanced by comparing to more samples of E2TTS and SpeechFlow, even with reproduced models.

### Questions
1. Is the HuBERT used in the paper trained in English only? If so, how does it work to reconstruct speech in other languages? Which layer is used?

2. What is the model used to compute SECS-O? Is it the WavLM-ECAPA large fine-tuned? 

3. Why only conduct subjective evaluations on 19 and 9 samples even though you have reproduced E2TTS and FlowSpeech? Why is there no subjective evaluation of naturalness?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces A2-Flow, an alignment-aware pre-training method for flow matching models in speech synthesis. A2-Flow integrates alignment learning directly into the pre-training process using discrete speech units extracted from HuBERT. This approach enables the model to efficiently adapt to alignment-aware tasks such as text-to-speech (TTS) and voice conversion (VC) without the need for separate alignment mechanisms. The authors demonstrate that A2-Flow facilitates alignment-free VC and allows for faster convergence during TTS fine-tuning, even with limited transcribed data. Experimental results show that A2-Flow achieves superior zero-shot VC performance compared to existing models and matches state-of-the-art TTS performance using only a small amount of transcribed data. Additionally, the method is effective in multilingual settings, highlighting its scalability and practical applicability in low-resource scenarios.

### Strengths
1. Originality: The paper presents a novel approach by integrating alignment learning directly into the pre-training phase using discrete speech units. This method addresses the limitations of existing models that require external alignment mechanisms or extensive additional training.

2. Quality: Extensive experiments support the effectiveness of A2-Flow. The model demonstrates superior performance in zero-shot voice conversion and matches state-of-the-art results in TTS with significantly less transcribed data.

3. Clarity: The paper is generally well-organized and provides detailed explanations of the methodology, including the integration of discrete speech units and the flow matching framework. The inclusion of diagrams and ablation studies aids in understanding.

4. Significance: A2-Flow offers a practical solution for high-quality speech synthesis in low-resource settings. By reducing the dependency on large amounts of transcribed data, it has substantial implications for multilingual and low-resource language applications.

### Weaknesses
1. Limited Baseline Comparisons: While the paper compares A2-Flow with several existing models, a more comprehensive comparison with other state-of-the-art methods, especially in multilingual settings, would strengthen the evaluation. The current comparisons are primarily focused on English language tasks, and the paper would benefit from a more thorough evaluation against other multilingual models to demonstrate the generalizability of the approach. Specifically, comparisons against models trained on similar multilingual datasets, or those that explicitly address low-resource scenarios, would be valuable.

2. Discussion of Limitations: The paper acknowledges some limitations, such as reliance on self-supervised speech units, but does not deeply explore potential solutions or future work to address these issues. The reliance on HuBERT units, while effective, might introduce biases or limitations in capturing the full range of phonetic variations across different languages or accents. A more detailed discussion on how these units might affect the model's performance and potential strategies to mitigate these effects would be beneficial. Furthermore, the paper could explore the implications of using a fixed set of discrete units and whether adaptive or learned units could improve performance.

3. Ablation Study Depth: The ablation studies could be expanded to include more variations in hyperparameters and architectural choices to better understand their impact on performance. For example, the impact of different flow matching configurations, such as the number of flow steps or the choice of the flow architecture, could be investigated. Additionally, exploring the sensitivity of the model to different training parameters, such as learning rates or batch sizes, would provide a more complete understanding of the model's behavior. The current ablation studies are somewhat limited in scope, and a more thorough analysis would be valuable.

4. Methodology Clarity: Certain aspects of the methodology, like the training details of the total length predictor and the timestep shifting strategy, could be explained in more detail to enhance reproducibility. The paper mentions a total length predictor, but the specific training procedure and its integration into the overall framework are not entirely clear. Similarly, the timestep shifting strategy, which is crucial for the flow matching process, requires a more detailed explanation. Specifically, the paper should clarify how the timestep shifts are determined and how they affect the training and inference processes. A more precise description of these components would improve the reproducibility of the method.

### Questions
1. Total Length Predictor: Could the authors provide more details on how the total length predictor is trained and integrated into the TTS fine-tuning process? 
2. Multilingual Evaluation: Have the authors considered evaluating A2-Flow on additional low-resource languages or dialects to further demonstrate its effectiveness across diverse linguistic settings?
3. Comparison with Alignment-Free Methods: How does A2-Flow compare with other alignment-free speech synthesis methods in terms of computational efficiency and inference speed?

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
The paper introduces A2-Flow, a alignment-aware pre-training method for flow matching models in speech synthesis. This approach facilitates alignment-free voice conversion and enhances convergence speed during TTS fine-tuning, making it particularly effective in low-resource settings.

### Strengths
1. Good presentation.
2. One framework can solve VC and TTS tasks.

### Weaknesses
1. It is hard to understand what alignment-aware pre-training is and its advanteges.

2. It is difficult to grasp the difference between using de-duplicated HuBERT tokens and text for pre-training. In my view, the only advantage is support for voice conversion tasks. However, the idea of a single model addressing multiple audio tasks has been widely discussed in previous works, such as VoiceBox, AudioBox. Thus, it is challenging to view this as a novel contribution.

3. For the TTS task, this work still requires a sentence duration predictor to control duration. Such strategies have been widely used in diffusion-based TTS systems, including SimpleSpeech, DiTTo-TTS, and E3TTS, and so on.

### Questions
(1) Please explain the advanteges of alignment-aware pre-training?

(2) Can you summarize your core contributions? For example, list them as 1,2,3... From this version, I cannot understand your core contributions.

(3) VC task does not need any alignment information, because the output duration can always the same as the input audio. Your TTS model still need additional sentence duration prediction model. So, why do you propose alignment-aware pre-training?

### Soundness
2

### Presentation
2

### Contribution
2
