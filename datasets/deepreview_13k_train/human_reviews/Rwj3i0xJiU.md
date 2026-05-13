# Libra: Leveraging Temporal Images for Biomedical Radiology Analysis

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Radiology report generation (RRG) is a challenging task, as it requires a thorough understanding of medical images, integration of multiple temporal inputs, and accurate report generation. Effective interpretation of medical images, such as chest X-rays (CXRs), demands sophisticated visual-language reasoning to map visual findings to structured reports. Recent studies have shown that multimodal large language models (MLLMs) can acquire multimodal capabilities by aligning with pre-trained vision encoders. However, current approaches predominantly focus on single-image analysis or utilise rule-based symbolic processing to handle multiple images, thereby overlooking the essential temporal information derived from comparing current images with prior ones. To overcome this critical limitation, we introduce Libra, a temporal-aware MLLM tailored for CXR report generation using temporal images. \textbf{Libra} integrates a radiology-specific image encoder with a MLLM and utilises a novel Temporal Alignment Connector to capture and synthesise temporal information of images across different time points with unprecedented precision. Extensive experiments show that Libra achieves new state-of-the-art performance among the same parameter scale MLLMs for RRG tasks on the MIMIC-CXR. Specifically, Libra improves the RadCliQ metric by 12.}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a method that generates chest X-ray reports from temporal inputs. The method combines a radiology-specific image encoder with a VLM and introduces a Temporal Alignment Connector (TAC) to capture and synthesize temporal information from images taken at different times. Experiments demonstrate that the method achieves good performance among other vision language models on the MIMIC-CXR dataset.

### Strengths
1- The clinical problem statement is fair and important
2- The evaluation is good and comprehensive and ablation studies showed how the method behaves in difference scenarios 
3- The authors introduced an interesting technical local and global learning mechanism

### Weaknesses
1- The main claim of the paper is that it is the first to introduce a VLM for automatic report generation that utilizes temporal scans to ensure more realistic reports that learn from multiple scans acquired at different time points. Regardless of whether it is a VLM or other types of encoder/decoder nets, this claim is not true because multiple works have been published to address this problem. For instance, 

-https://aclanthology.org/2023.findings-emnlp.325/
-https://aclanthology.org/2023.findings-emnlp.140/
- https://arxiv.org/abs/2403.13343
- https://arxiv.org/pdf/2301.04558 (which you already cite but don't compare with).

2- It is not clear whether the method is capable of handling one previous scan or multiple

3- In Figure 1, the effect of Rad-Dino is not clear. What if it is replaced with a classical pre-trained image encoder?

### Questions
Please respond to the three points in the weaknesses.

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
3

### Summary
This paper introduces Libra, a vision-language model designed for radiology report generation based on chest X-rays. Libra integrates temporal information across images taken at different time points through a Temporal Alignment Connector (TAC), enabling the model to capture temporal changes effectively. The model leverages a pre-trained RAD-DINO image encoder and a specialized medical language model, Meditron, to generate high-quality radiology reports. Experiments demonstrate that Libra outperforms existing VLM methods on the MIMIC-CXR dataset.

### Strengths
* Innovative temporal processing. The TAC module is a novel addition that allows Libra to capture and utilize temporal changes in medical images effectively, enhancing the model's clinical applicability.
* Comprehensive ablation studies. The ablation experiments clarify the importance of each submodule (TFM, LFE, and PIPB), reinforcing the credibility of the design choices.
* Comprehensive appendix. The appendix is highly commendable, providing detailed descriptions of the datasets, training configurations, and additional experimental results. This thorough documentation enhances the paper’s transparency and reproducibility, offering valuable insights that complement the main text and support further exploration by readers.

### Weaknesses
Despite the paper's clarity, several imprecise arguments and overstatements necessitate revision and clarification:
* Incomplete framework representation. TFM is a crucial component of the core TAC, but the framework diagram omits the illustration of the $MLP_{final}$ part within TFM. This omission may lead to ambiguity regarding the final processing steps, making it more difficult for readers to fully understand how all modules are integrated within the model. It is recommended that the authors update the framework diagram to include this component and provide a detailed explanation of its role, which would enhance the overall clarity of the model architecture.
* Insufficient detail on RAD-DINO. The description of RAD-DINO in the model architecture section is too brief, lacking the depth necessary for readers to fully understand its role and integration within the model. It is suggested that the authors provide a more comprehensive explanation, including details about its architecture, pre-training process, and specific contributions to the model’s performance in radiology tasks. This would improve both the clarity and the completeness of the proposed framework.
* Over-reliance on prior images. Although the paper introduces the Prior Image Prefix Bias to address the absence of prior images, the model still faces challenges during generation when prior images are unavailable. This suggests that the current solution may not fully resolve issues related to temporal information gaps, potentially affecting the model’s robustness in real-world clinical scenarios. The authors are encouraged to conduct further analysis of the model’s performance without prior images and explore potential strategies to enhance robustness under limited temporal information.
* Lack of clear novelty in vision-language alignment. The proposed vision-language alignment mechanism lacks distinct novelty when compared to existing methodologies in this domain. Similar cross-modal attention mechanisms have been extensively explored in prior studies. The authors are advised to conduct a detailed comparison between their approach and previous works, specifically highlighting any improvements or innovations that set their model apart in the context of radiology report generation tasks.
* Insufficient acknowledgment of prior work. The paper lacks a thorough review of relevant prior work, especially recent advancements in vision-language models for medical image interpretation. This omission makes it challenging to contextualize the model's contributions. The authors should provide an in-depth discussion of related works to clearly establish how Libra advances the state of the art and addresses specific gaps in the literature.
* 	Limited dataset and evaluation metrics. The experimental evaluation relies solely on the MIMIC-CXR dataset, which raises concerns about the model's generalizability. Additionally, some evaluation metrics are insufficiently explained. It is recommended that the authors include experiments on other datasets, such as CheXpert, and offer more detailed explanations of the evaluation metrics to strengthen the model's validation and applicability.

### Questions
Generalizability. How would the model perform on other datasets or in different clinical settings?

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
4

### Summary
This paper introduces Libra, a novel Visual-Language Model (VLM) designed for radiology report generation (RRG) that leverages temporal imaging data to improve report accuracy. To address disease progression in radiology, Libra integrates a radiology-specific image encoder with a medical language model and introduces a Temporal Alignment Connector (TAC). This connector comprises a Layerwise Feature Extractor (LFE) to capture high-granularity imaging features and a Temporal Fusion Module (TFM) for synthesizing temporal references.

### Strengths
1. The paper presents an innovative approach for handling prior study citations across various time points in report generation tasks.

2. The development of the Temporal Alignment Connector showcases a sophisticated method for capturing and integrating temporal information across multiple images.

3. A comprehensive experimental analysis, including ablation studies and qualitative comparisons, is provided to validate the effectiveness of the proposed methods.

### Weaknesses
1. Comparative Results: The comparative results do not convincingly demonstrate Libra's superiority. Although MIMIC-Diff-VQA is derived from MIMIC-CXR, the comparison seems unbalanced, as Libra was trained on both MIMIC-CXR and MIMIC-Diff-VQA, while the other model was only trained on MIMIC-CXR.

2. Effectiveness of the Temporal Alignment Connector: The authors overstate the effectiveness of the Temporal Alignment Connector (e.g., "significant enhancements across all metrics" in line 398). While the Temporal Fusion Module aims to provide temporal-aware representations, the ablation results in Table 3 (using dummy images) yield comparable results, with the exception of the F1 score. If Libra effectively perceives and utilizes temporal information, it would be beneficial to explain why incorporating true prior images results in only marginal improvement.

3. Experimental Settings: Some experimental settings deviate from standard practices. For instance, in Q2 of Section 4, the encoder and LLM should align with those used in Libra (i.e., RAD-DINO and Meditron).

4. Clarity in Table 5: Table 5 lacks clarity. Notably, using only Findings in Stage 1 yields better performance in Clinical Efficacy. One would intuitively expect the VQA dataset, which emphasizes detailed symptom descriptions, to enhance Clinical Efficacy, yet the results in Table 3 show a decrease.

5. Explanation of Figure 5: Provide more detailed explanations for Figure 5 in the Appendix, where the heatmap indicates that the Prior LFE shows more focused attention.

### Questions
See the Weaknesses part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This submission tackles the challenge of automated radiology report generation. Specifically, the authors aim to generate a radiology report’s Findings section given a current and (optionally) past radiology image of a patient. The paper proposes a method consisting of a pretrained image encoder, a new convolutional module designed to compress image features from the image encoder (termed “LFE”), an attention-based module designed to integrate information from two radiology images (termed “TFM”), and a pretrained language decoder. The main contributions are the two connecting modules, the “LFM” and “TFM”. Empirically, the method is shown to outperform baselines.

### Strengths
-	The need to integrate information from multiple images in generating a report is a real and well-motivated problem. The modules the authors propose are an interesting approach to doing so, and it seems this approach does improve the models’ ability to make past/present comparisons.
-	The authors propose a number of other changes in their radiology report pipeline, including an additional feature transformation module on top of the pretrained image encoder as well as a particular training scheme and prompt. The authors present a thorough ablation section to show each change improves performance. Empirically, the model is shown to outperform reasonable baselines.

### Weaknesses
-	The proposed approach is brittle regarding how many images can be input. With the current model, two scans are required to be input. Thus, when a patient does not have a prior scan, the authors propose using the current scan as a “dummy” prior scan instead. While many patients do not have previous scans, others often have multiple previous scans. Extending the proposed framework to account for multiple prior scans would increase computational complexity in the cross-attention head and I believe would require multiple “dummy” prior scans to be input for any patient who does not have the maximum number of scans. This inflexibility makes the proposed method less attractive for solving the posed problem of “temporally aware report generation” compared to methods that are more flexible with regard to number of input images.     
-	The framing of the paper could be improved. The paper is pitched as a temporal alignment paper in the Abstract and Introduction, however it seems that most of the improvement in the paper come from a constellation of other changes made to the report generation pipeline. Specifically, the empirical evidence supporting their approach to using past+present images is not particularly strong. Most standard evaluation metrics only change 1-2% when using the past image. In contrast, it seems the additional complexity introduced by the LFE module (which integrates features from a pretrained image encoder), the additional layers in the TFM module, and other changes made to the training pipeline (the prompt, the use of VQA, etc.) impact performance more significantly, impacting performance metrics by 5-10%. Given the relative improvements of the authors’ contributions, I think the framing of the paper could be revised.
-	The paper’s writing could be improved to be more concise and clear; I found many sections overly wordy and others lacking detail.

### Questions
-	How long does inference take for a single study take, and on what hardware?
-	Is the choice to use features from throughout the image encoder ablated? This is proposed as one of two main contributions of the paper in the Introduction, however I do not see that choice evaluated anywhere. I see the ablations on the LFE, however you could ablate the use of multi-layer features from the encoder without removing the LFE.
-	A Limitations and Future Work section would be helpful additions. For example, the same approach could be used to integrate info from multiple imaging modalities, which could be an interesting avenue for future exploration.

### Soundness
3

### Presentation
2

### Contribution
2
