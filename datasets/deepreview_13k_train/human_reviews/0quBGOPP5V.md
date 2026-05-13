# Deep ECG-Report Interaction Framework for Cross-Modal Representation Learning

- Decision: Reject
- Scores: 6, 3, 3, 3

## Abstract
Electrocardiogram (ECG) is of great importance for the clinical diagnosis of cardiac conditions. Although existing self-supervised learning methods have obtained great performance on learning representation for ECG-based cardiac conditions classification, the clinical semantics can not be effectively captured. To overcome this limitation, we proposed a $\textbf{D}$eep $\textbf{E}$CG-$\textbf{R}$eport $\textbf{I}$nteraction ($\textbf{DERI}$) framework to learn cross-modal representations that contain more clinical semantics. Specifically, we design a novel framework combining multiple alignments and feature reconstructions to learn effective cross-modal representation of the ECG-Report, which fuses the clinical semantics of the report into the learned representation. An RME-module inspired by masked modeling is proposed to improve the ECG representation learning. Furthermore, we extend ECG representation learning with a language model to report generation, which is significant for evaluating clinical semantics in the learned representations and even clinical applications. Comprehensive experiments on various datasets with various experimental settings show the superior performance of our proposed DERI.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The novel DERI approach enhances cross-modal representation learning by incorporating clinical report generation. The work extends the MERL approach [1], integrating multiple alignments and a report generative approach with a novel latent random masking module (RME). The novelty of the approach lies in not only aligning the ECG and report features but also decoding cross-modal features. The author demonstrated a performance improvement compared to other SOTA approaches, verified through supervised tasks on unseen data.

### Strengths
The work is a natural extension of MERL[1], with more accurate zero-shot classification and the possibility of automatic report generation. The zero-shot classification performance shows significant improvement from [1]. The cross-modal decoders allow the additional capability of automatic report generation utilizing GPT-2 architecture.

### Weaknesses
The paper needs rephrasing to improve clarity and readability, especially in the methodology section. The training approach is not applicable to unlabelled ECG in the usual context and necessitates the availability of accurate diagnostic reports by a cardiologist. The performance is related to the quality, distribution, and context of these reports and may not extend to novel tasks outside the scope of diagnostic reports. The alignment loss in Equation 1 does not explicitly address the scenario where multiple ECGs might correspond to similar text reports, potentially leading to suboptimal feature learning. The random masking approach, while intended to enhance global feature learning, lacks a clear explanation of how it differs fundamentally from random dropout, particularly in the context of the ResNet encoder's output. Furthermore, the performance of other approaches is not consistently evaluated by the authors, raising concerns about the fairness of comparisons, especially given the sensitivity of deep learning models to hyperparameter tuning. The methodology section lacks crucial details regarding the text encoder, masking/reconstruction processes, and the origins of equations 1 to 5, making it difficult to reproduce the results and assess the novelty of the approach. The description of the cross-modal decoders and their integration into the mixed-modal representation is vague, particularly regarding how different dimensional feature spaces are handled. Finally, the experimental results and their implications for classification are not clearly articulated, hindering the understanding of the model's practical utility.

### Questions
Methodology

Does incorporating textual reports in pre-training have an element of supervision?

Does the pre-training necessitate diagnostic reports for ECGs or can it also utilize ECGs when the reports are not available?

Are the reports automatically generated or written by cardiologists?

The strength of the self-supervised pretraining approach is learning general features while incorporating textual reports limits the features to the scope of the reports and thus might limit the capabilities for future tasks outside the information provided in the reports. Can the author demonstrate that the learned features are not limited by the scope and bias of the reports?

Does the alignment loss in Equation 1 accommodate the situation where multiple ECGs have similar text reports?

How does random masking differ from random dropout?

Is the performance for other approaches evaluated by the author or the original work since most models require a hyperparameter optimization for best performance?

General comments

Page 1 line 29: rephrase “clinical cardiac conditions classification”.

Page 2 lines (61-72): “Specifically, the ECG signal and …. as follows.” Please rephrase.

Page 2 line 78: What is meant by “which can provide clinical semantics visually”?

Page 2 line 91: “temporal and spatial correlation ship of ECG signals”. to “temporal and spatial correlations of ECG signals”.

Page 2 line 140: Details and references for the text encoder and masking/reconstruction are missing in the methodology section.

Page 4 line (164-194): Please provide references if equations 1 to 5 are derived from existing literature and indicate where there are novel concepts.

Page 4 line (202-207): “We introduced” to “We introduce”

Page 4 line (202-206): “Considering that the textual modality … order to provide more textual features”. Please rephrase to improve clarity and avoid very long sentences.

Page 4 lines (206-208): “After completing …. corresponding report text.” Please rephrase

Page 4 sec 3.2: What is meant by the decoded text and ECGs? Are these the reconstructions of the feature encoding or the corresponding aligned text? If encoding then how is it combined in the mixed-modal representation if the dimensions are different?

Page 7 lines (360-362): “The experimental results …. for classification”. Not clear please rephrase.

Figures: Figure captions need to be improved. 

Figure 1: Please explain the figure adequately in the caption.

Tables: Table captions should include the supervised task and the metric under observation.

Table 7: Please change DERL to DERI.


References:

[1] Che Liu, Zhongwei Wan, Cheng Ouyang, Anand Shah, Wenjia Bai, and Rossella Arcucci. Zero-shot ecg classification with multimodal learning and test-time clinical knowledge enhancement. arXiv preprint arXiv:2403.06659, 2024.

### Soundness
3

### Presentation
2

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
The study introduces DERI (Deep ECG-Report Interaction), a framework designed for cross-modal representation learning from ECG signals and clinical reports to improve the clinical relevance of ECG representations. Traditional ECG self-supervised methods focus on single-modal generative or contrastive learning but fail to capture the deep clinical semantics. DERI addresses these limitations by integrating ECG and report data more deeply.

### Strengths
- Deep Cross-Modal Interaction: Unlike previous methods that use shallow alignment between ECG and report features, DERI implements multiple alignments and feature reconstructions, fostering deeper interactions between ECG signals and report data. This approach strengthens the representation's ability to capture the clinical context, enhancing both accuracy and relevance for diagnosis.
- Potential for Broader Clinical Integration: DERI’s architecture, designed to integrate additional data types like electronic medical records (EMRs), positions it well for broader application in clinical settings. This flexibility could make DERI a powerful tool for multi-modal clinical analysis in the future.

### Weaknesses
In contrast to other modalities such as chest X-rays and pathological diagnoses, electrocardiogram reports have been mainly produced mechanically by diagnostic equipment for many years. Therefore, this study is more likely to be learning of waveform data and its correct labels, rather than two-modal learning of waveform data and its interpretation using natural language. The scope of this study may be narrow than the general interest of ICLR main conference.

### Questions
Is it possible to disclose what the electrocardiogram reports used as training data in this study are specifically like? Was it verified how diverse the content of these reports is in terms of natural language?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes the Deep ECG-Report Interaction (DERI) framework, a novel method for cross-modal representation learning that combines ECG with clinical reports. This paper introduces cross-modal alignment for representation learning and RME module for enhanced ECG learning.

### Strengths
The paper is well-organized and generally easy to follow. The flow from the motivation behind the DERI framework to the detailed explanation of its architecture, followed by experiments and results, is logical and well-structured. The diagrams, particularly those illustrating the DERI architecture and its training process, are helpful in understanding the complex cross-modal interactions.

The technical descriptions, such as the use of multiple alignments, the RME module, and the integration of language models for report generation, are well-explained.

### Weaknesses
The paper shows a lack of understanding of related work, with many previous related articles not cited or discussed. The following articles [1-4] need to be added and discussed in the paper.

Several methods from the referenced articles need to be used as baselines and compared in the experimental section, especially for the ECG report generation part.

There are many similarities between this paper and the article "Zero-Shot ECG Classification with Multimodal Learning and Test-time Clinical Knowledge Enhancement (MERL)," with a lack of innovation.

For instance, two of the losses used in the paper are almost identical to the ones used in MERL (CLIP loss and mask loss); the paper merely describes them in a different way. The report generation method is also quite similar to many multimodal approaches, such as the BLIP method, and does not represent true innovation. Moreover, these papers have not been cited.

The downstream task system is also very similar to MERL, except for report generation. However, many report generation baselines are missing from this paper.

### Questions
Please supplement the references and baseline methods [1-4] in the experiments, and fully discuss and compare their advantages, disadvantages, and innovations in the paper.

Please explain the parts that are overly similar to MERL and highlight the points of technological innovation.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes the Deep ECG-Report Interaction (DERI) framework to address the lack of clinical semantics in ECG representation learning. 
By integrating ECG signals with clinical reports using multi-level alignment strategies, DERI enhances cross-modal learning. It also incorporates a language model for ECG report generation, demonstrating superior performance across multiple datasets.

### Strengths
Align multi-level features using contrastive loss, while also performing cross-modal reconstruction by using ECG signals to reconstruct text and text to reconstruct ECG. This approach enables learning mutual information between the two modalities. The framework is evaluated across multiple datasets and methods for comprehensive assessment. However, the compared baseline methods are limited, and the evaluation metrics are ambiguous.

### Weaknesses
 - The novelty is limited. In Section 3.2, the work uses cross-modal alignment with the original contrastive loss. Section 3.3's approach for cross-modal reconstruction is similar to what was proposed in MRM [1], even though MRM was originally for the image domain. The method in this work closely resembles MRM. Moreover, MRM uses features extracted from masked inputs to reconstruct the other modality, while DERI uses features extracted directly from the original inputs, which reduces the difficulty of the reconstruction task.
- There is a lack of baseline and comparison in the report generation task. In MEIT [2], a comprehensive benchmark for ECG report generation is proposed and implemented on the MIMIC-ECG and PTB-XL datasets, both of which are also used in DERI. However, the authors do not compare DERI against any baseline from MEIT and only use GPT-2 as the text decoder, which is outdated, having been released in 2019.
- The reproducibility issue is further compounded by the authors' apparent reluctance to share their code.
- The report generation task is not implemented on PTB-XL. Since MIMIC-ECG is used for pretraining, evaluating solely on MIMIC-ECG does not sufficiently assess generalizability and robustness, as all the data is seen during pretraining. 
- The evaluation metric for ECG report generation is lacking. The evaluation metric for clinical efficacy is ambiguous.

### Questions
- In Appendix Section D, Table 12, the authors include various text models for report generation, including encoder-only models like MedCPT (desgined for text retrieval task). Using encoder-only models for report generation is questionable, as it conflicts with the mainstream approach seen in works such as MEIT [1] and RGRG [2], which typically utilize encoder-decoder or decoder-only models for text generation tasks. Encoder-only models are not designed for generative tasks like report generation, so their inclusion deviates from standard practices.
 
- Regarding the computation of clinical efficacy in Section 4.2, several aspects need clarification: 
(1) **How is the prompt embedding obtained from the decoder?** If the decoder is used to obtain prompt embeddings, is it based on the representation from the [EOS] token? Clarification is needed on how the embedding is extracted from a decoder-only architecture.
(2) **How is the classification probability for categories computed using a text decoder?** Does this refer to the highest probability assigned to the category name token? Some diseases (e.g., "myocardial infarctions") are tokenized into multiple tokens. If this is the case, how is the classification probability determined for multi-token categories?
(3) **Handling multiple classes in ECGs**: The PTB-XL dataset shows that ECGs can belong to multiple classes simultaneously. If the authors use only the highest probability for classification, they may be reducing the prediction to a single class, which ignores other relevant conditions. Why are additional classes not considered in the evaluation?
(4) **Discrepancy between prompts and generated reports**: The method uses a single-class description as the prompt for classification, whereas the generated report may describe multiple conditions associated with the ECG signal. There is a clear gap between the prompt (single class) and the report (multi-class). How is this gap addressed in the evaluation process?

[1] Wan, Zhongwei, et al. "MEIT: Multi-Modal Electrocardiogram Instruction Tuning on Large Language Models for Report Generation." arXiv preprint arXiv:2403.04945 (2024). Tanida, Tim, et al. "Interactive and explainable region-guided radiology report generation." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

### Soundness
3

### Presentation
3

### Contribution
2
