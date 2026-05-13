# EEG-Language Pretraining for Highly Label-Efficient Pathology Detection

- Decision: Reject
- Scores: 5, 6, 8, 5

## Abstract
Multimodal language modeling constitutes a recent breakthrough which leverages advances in large language models to pretrain capable multimodal models. The integration of natural language during pretraining has been shown to significantly improve learned representations, particularly in computer vision. However, the efficacy of multimodal language modeling in the realm of functional brain data, specifically for advancing pathology detection, remains unexplored. This study pioneers EEG-language models (ELMs) trained on clinical reports and 15000 EEGs. We propose to combine multimodal alignment in this novel domain with timeseries cropping and text segmentation. This also enables an extension based on multiple instance learning to alleviate misalignment between irrelevant EEG or text segments. Our results indicate that models learn richer representations from being exposed to a variety of report segments, including the patient's clinical history, description of the EEG, and the physician's interpretation. Compared to models exposed to narrower clinical text information, we find such models to retrieve EEGs based on clinical reports (and vice versa) with substantially higher accuracy. Particularly in regimes with few annotations, we observe that ELMs can significantly improve pathology detection compared to EEG-only models, as demonstrated by both zero-shot classification and linear probes. The integration of multiple instance learning further improves performance across tasks. In sum, these results highlight the potential of integrating brain activity data with clinical text, suggesting that ELMs represent significant progress for clinical applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method for training EEG-language model for pathology detection with EEG data. It leverages the success of multimodal language modeling in other domains, aiming to learn richer representations by aligning EEG time series with reports. Furthermore, the paper introduces sub-unit alignment using time series cropping and text segmentation to address the length discrepancy between modalities. It also propose a MIL extension to EEG and text data to handle inconsistencies in relevance and explore different text segmentation strategies based on report content.

### Strengths
- Applying multimodal language modeling to EEG and clinical text reports is a promising and much needed approach for zero-shot evaluation.
- Addresses the challenges posed by the length and heterogeneity of EEG and clinical text data through sub-unit alignment and MIL.
- Strong empirical results, especially in low-label regimes.
- Paper shows comprehensive ablation studies and analysis of different components.

### Weaknesses
- Limited evaluation on only one corpus (TUEG/TUAB). It would be interesting to see how the model generalizes/transfer to other datasets collected in a different setup/environment.
- Pretraining dataset with 15144 files are also relatively small compared to other domains. However, this issue is not related to the paper but more to lack of availability of high-quality large-scale EEG-Text data.
- The model performance seems highly sensitive to text segmentation and the type of text input (e.g., LLM summaries). This sensitivity raises concerns about the robustness of the approach and its applicability to other clinical settings.
- The comparison to EEG-only SSL methods is valuable, comparing the proposed model to fully supervised methods (when sufficient labeled data is available) is crucial for assessing the practical utility of the approach. I also see lack of comparison with other EEG-only self-supervised methods.

### Questions
- While the results show improved performance, the paper lacks a deeper discussion of the clinical implications of the learned representations. What kind of insights do ELMs offer for understanding EEG pathologies?
- I am wondering how does the proposed sub-unit alignment affect the temporal dependencies in EEG data? does it miss important segments relating to some specific conditions?
- Regarding the normalization by number of crops in MIL loss. Is this appropriately addressing the varying amount of information in different-length crops and text segments?
- I also have reservations over the procedure of selecting optimal value for temperature parameter. Why a separate held-out validation data is not used?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This article explores a multimodal model that integrates natural language with EEG brain data, introducing EEG-Language Models (ELMs) trained on clinical reports and EEG data. By using time-series cropping and text segmentation, the model better aligns EEG and text data, showing significant advantages in pathology detection, especially when data is limited. The study demonstrates that this combined approach improves detection accuracy and presents new possibilities for medical applications.

### Strengths
1. Richer Representation Learning: Through time-series cropping and text segmentation, this method increases the number of samples, allowing the model to learn richer and more diverse representations. This improved data variety helps the model capture complex patterns in EEG and clinical text, enhancing performance in pathology detection tasks and making it more adaptable to different clinical scenarios.

2. Data Preprocessing and Noise Filtering: The method employs careful data preprocessing and cropping to remove irrelevant noise, focusing on the most important EEG signals. This improves the efficiency of training and inference by ensuring the model works with high-quality, meaningful data, leading to more accurate and reliable performance in clinical settings.

### Weaknesses
1. Limited Dataset Scale: Despite the demonstrated potential of multimodal pretraining in medical EEG analysis, the model remains significantly constrained by the limited availability of clinical EEG data and corresponding textual reports. The scarcity of such data hinders the model's generalization capability, particularly when dealing with unseen pathological cases, where performance may degrade substantially. Additionally, the small dataset size increases the risk of overfitting to specific pathological patterns, reducing the model’s robustness and applicability across diverse clinical settings. This limitation also raises concerns about the model’s transferability and consistency when deployed in different hospitals or patient populations.

2. Potential Bias Risks: The method's reliance on pretrained language models and text summarization introduces the possibility of inherited biases or inaccuracies from the original language models, which are often trained on general, non-medical data. These biases may be exacerbated or propagated in the EEG representations and subsequent clinical decision-making. For instance, if the pretrained model exhibits particular biases toward certain symptoms or pathologies, it could result in unbalanced predictions during EEG analysis. Moreover, the text summarization process might oversimplify or misrepresent critical information, further amplifying bias effects. Combined with the framework’s lack of innovation—relying on basic contrastive learning mechanisms—this approach may be insufficiently adaptable for more complex or dynamic clinical scenarios.

3. Alignment Instability: Although the implementation of a multiple-instance learning strategy helps mitigate some of the alignment issues between EEG data and text segments, it does not fully resolve the challenges posed by mismatched or weakly correlated data. In practice, clinical reports and EEG signals may contain partially irrelevant or loosely related information. For instance, certain report sections might include background details unrelated to the EEG signals, or critical EEG features may not be explicitly referenced in the text. Such discrepancies can lead to unstable multimodal alignment, reducing the model’s accuracy and robustness in pathology detection tasks. Consequently, the model's reliability and practical utility in real-world clinical environments may be compromised due to suboptimal alignment performance.

### Questions
1. Considering the inherent differences between EEG and fMRI, could you elaborate on the decision to use EEG data for this study? fMRI provides high spatial resolution and detailed information about brain regions involved in specific tasks or conditions, which could offer a more comprehensive and fine-grained understanding when aligned with clinical text. How might the use of fMRI improve the quality of alignment or representation learning in comparison to EEG, and what trade-offs would this involve in terms of data availability, preprocessing complexity, and computational demands?
2. EEG data is known for being highly susceptible to various forms of noise and artifacts, such as muscle activity, eye movements, and environmental interference. Effective preprocessing is crucial for ensuring the quality and reliability of the data used in model training. Could you specify the techniques employed for noise reduction and artifact removal? Additionally, what measures were taken to standardize and segment the EEG signals to make them suitable for training, and how were these techniques validated to ensure they do not compromise important neural information?
3. The current analysis mainly features cross-sectional comparisons between different methods. Would it be possible to add more thorough comparative experiments, perhaps including longitudinal analyses or additional baselines, to provide a more complete understanding of the model's performance and robustness?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents EEG-Language Models (ELMs) pretrained jointly on clinical reports and EEG data using a multiple instance learning (MIL) variant of contrastive learning (MIL-NCE). The authors evaluate these models on downstream tasks, including retrieval analysis and pathology classification. Pathology classification is performed using both zero-shot and fine-tuning approaches. The model’s performance is compared against EEG-only pretraining methods, which serve as the main baseline, and demonstrates significant improvements across all evaluations. The paper also explores various ELM configurations and finds that their ELM-MIL variant achieves the best overall performance.

### Strengths
- While multiple instance learning and contrastive learning are not novel in isolation, the paper adapts these techniques to the novel domain of brain activity signals and demonstrates substantial benefits over using EEG-only pretraining methods. The results show that exposing the model to a variety of report segments enables the learning of richer representations.

- The paper includes thorough ablation studies that explore various design choices, such as the integration of multiple instance learning and different segments of clinical text. The model is also compared against various comparable baseline approaches, including BYOL and ContraWR, with standard deviations reported over multiple runs to indicate the confidence level of their results.

- Overall, the paper is well-written and provides robust baseline comparisons, detailed ablations of design choices, and a strong justification for incorporating text into the pretraining of EEG foundation models.

### Weaknesses
- While the paper focuses on pretraining strategies, the results would be more robust if a supervised baseline were included in Table 2. For example, training a neural network to classify pathology directly from raw EEG signal space could provide a useful comparison. Ideally, this supervised model should use the same architecture as the EEG encoder employed by the authors.

- The impact of the temperature parameter on performance, as shown in Figure 3, is not entirely clear. Including performance results for more temperature parameter values could provide better insight into its effect on the model.

- The tasks used to evaluate the models are relatively narrow and not very challenging. Although the paper demonstrates performance improvements over the baseline on these benchmarks, it is difficult to conclude the method’s overall efficacy without evaluating on more complex tasks. However, it is important to recognize the difficulty in obtaining EEG-report datasets. One suggestion is to explore sleep databases for potential paired EEG and report data, which might include sleep apnea or sleep stage annotations. These annotations could be converted into brief report summaries based on the severity of apnea, for instance.

### Questions
- Why is there no supervised baseline for pathology classification?

- The temperature ablation (Figure 3) is somewhat unclear. Including results for additional temperature values could enhance the clarity of the plot.

- Where do the authors see this approach being most useful? What other types of tasks could benefit from this method compared to baseline approaches?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents an EEG pretraining LLM for disease detection, introducing a novel method that integrates multimodal alignment with EEG time series cropping and text segmentation. The experimental results demonstrate the superior performance of the proposed method compared to existing approaches. Additionally, the paper is well organized, and the references to recent works are comprehensive.

### Strengths
1.	The aligning of EEG crops and the text segments is quiet good idea.
2.	The proposed method seems to achieve superior performance of the proposed method compared to existing approaches.
3.	This paper is well organized and with clear presentation.

### Weaknesses
1.	Classifying EEG signals into [normal] or [abnormal] is relatively straightforward, even with traditional (non-large) models. Using such high-resource cost model to do such a simple work is nor enough.
2.	The authors rely on a pretrained language model for the text encoder without fine-tuning it on specialized medical data. This approach may hinder performance in the medical domain, as the pretrained model likely lacks the necessary medical knowledge and context.
3.	While the authors employ a Multiple Instance Learning (MIL) approach to align EEG segments with text, the generality of the provided text segments (e.g., "clinical history," "medications") raises questions. Specific text segments may not be accurately aligned with corresponding EEG segments, potentially undermining the effectiveness of the alignment strategy.

### Questions
1. The authors state, “As paired medical EEG data and clinical reports are scarce, training the text encoder function fl from scratch is unlikely to be successful… To prevent resulting information loss, we follow the recommendations by Liu et al. (2023a) to use a pretrained language model for fl and freeze its weights during training.” However, I believe that the scarcity of medical reports actually suggests the need to fine-tune the text encoder. The data used to pretrain large language models likely consists of general dialogue, lacking specialized medical knowledge and explanations. Without fine-tuning on medical data, the model’s performance in this domain may be suboptimal.
2. The use of MIL to align EEG segments with corresponding text segments is an interesting approach. The paper states: “While previous approaches aim to align text and EEG crops uniformly, certain text segments likely describe specific EEG sections more accurately than others.” Can I interpret this with the following example:
•	Clinical Text: “One segment of the EEG data indicates deep sleep, while another shows the patient gradually waking up.”
•	EEG: One crop represents deep sleep; the other represents waking up.
Therefore, are the authors aligning the first EEG crop with the “deep sleep” text and the second with the “waking up” text? If so, why are the text segments provided in the Figure 1 more general, such as "clinical history," "medications," and "description of EEG," which seem to describe the EEG comprehensively rather than specific segments?
3. Classifying EEG signals into [normal] or [abnormal] is relatively straightforward, even with traditional (non-large) models. Are the results in Table 3 quite low? Have the authors compared their performance with other large models or traditional models?
4. Given the high cost of training such a large model, I believe it’s important to set higher expectations for its capabilities. Have the authors considered multi-disease recognition or generating other types of medical records?

### Soundness
3

### Presentation
3

### Contribution
2
