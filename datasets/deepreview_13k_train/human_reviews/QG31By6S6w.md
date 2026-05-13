# Unleashing the Potential of Vision-Language Pre-Training for 3D Zero-Shot Lesion Segmentation via Mask-Attribute Alignment

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
Recent advancements in medical vision-language pre-training models have driven significant progress in zero-shot disease recognition. However, transferring image-level knowledge to pixel-level tasks, such as lesion segmentation in 3D CT scans, remains a critical challenge. Due to the complexity and variability of pathological visual characteristics, existing methods struggle to align fine-grained lesion features not encountered during training with disease-related textual representations. In this paper, we present {\bf Malenia}, a novel \textbf{m}ulti-sc\textbf{a}le \textbf{le}sio\textbf{n}-level mask-attr\textbf{i}bute \textbf{a}lignment framework, specifically designed for 3D zero-shot lesion segmentation. {\bf Malenia} improves the compatibility between mask representations and their associated elemental attributes, explicitly linking the visual features of unseen lesions with the extensible knowledge learned from previously seen ones. Furthermore, we design a Cross-Modal Knowledge Injection module to enhance both visual and textual features with mutually beneficial information, effectively guiding the generation of segmentation results.
Comprehensive experiments across three datasets and 12 lesion categories validate the superior performance of {\bf Malenia}. Codes will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents a zero-shot medical image semantic segmentation framework that is based on maskformer and attribute-based visual-language feature fusion. To achieve fine-grain alignment between visual and textual concepts, the authors propose to decompose radiological reports into attributes describing lesions of interest, assisted by LLMs and human annotators. The obtained attributes allows fine-grain fusion and alignment between lesion features and textual concepts, yielding improved generalization performance upon unseen lesions. The proposed framework is evaluated on tumor segmentation tasks, and demonstrates improved segmentation results compared with existing zero-shot segmentation approaches on unseen lesions.

### Strengths
The idea of decomposing free-text reports into attributes for fine-grain training and inference is intuitive and feasible. It can significantly reduce the noise and ambiguity associated with unstructured free-text reports and yields improved performance on unseen lesions.

The key components and the detailed implementations are described in good detail. 

The proposed approach demonstrates performance improvements compared with previous zero-shot image segmentation methods.

Detailed ablation studies are presented to verify the effectiveness of key components.

### Weaknesses
Despite stronger segmentation performance, the major framework looks similar to ZePT (Jiang et al., 2024): maskformer backbone + interacting visual and textual features that are obtained from detailed description of the lesions. Therefore, the key take-home message for readers may be a bit unclear: should the readers interpret the key technical contribution as explicitly decomposing textual descriptions/reports into categorized attributes for the ease of learning and inference?

Readers may argue that using GPT-4 for attribute construction from radiological reports is often infeasible in practice due to the privacy and legal concerns. The authors are encouraged to argue if switching to local open-source LLMs would yield a similar level of performance gain. 

The authors may want to decompose some of technical details in Figure 1 into separate figures and move them closer to corresponding paragraphs.

### Questions
Considering the practicality issue, would replacing GPT-4 with an open-source LLM for attribute construction (probably also without human annotators?) reaching a similar level of performance gain (as mentioned above)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces Malenia, a framework for zero-shot lesion segmentation in 3D medical images, aimed at addressing the challenge of transferring image-level knowledge to pixel-level segmentation tasks. Building on advancements in medical vision-language pre-training, Malenia integrates a multi-scale mask-attribute alignment framework and a Cross-Modal Knowledge Injection module to link visual and textual features, enabling the model to handle previously unseen lesions. The authors evaluate Malenia's performance through experiments on three datasets (two public and one private) across 12 lesion categories.

### Strengths
1. The topic on zero-shot lesion segmentation is valuable, as clinical settings often involve diverse, emerging anomalies, and data collection is challenging, increasing the need for models that handle unseen diseases in an open-set context.
2. The authors strengthen their claims with both qualitative and quantitative results, enhancing the credibility of their findings and providing a well-rounded evaluation of the proposed approach.
3. The paper is well-organized, with a clear and logical structure that makes complex concepts accessible and easy to follow for readers.

### Weaknesses
1. The Zero-Shot Inference section lacks sufficient detail on how the model handles test CT images containing unseen tumor types. For instance, if a test image includes both a kidney tumor and a gallbladder tumor, it is unclear how the model predicts these different tumors within the same image. Additionally, the phrase “we obtain the class information for each predicted lesion mask by referencing a clinical knowledge table” is ambiguous. Further clarification is needed on what this clinical knowledge table entails, specifically its structure and content, and how it is used in the inference process to disambiguate between different lesion types when multiple are present in a single image. The description should also clarify if the model predicts all possible lesions simultaneously or sequentially, and how the model handles overlapping or adjacent lesions of different types.
2. The comparisons in Table 1 and Table 2 may not be entirely fair. The authors introduce additional ATTRIBUTE DESCRIPTIONS annotations, which provide extra information not available to baseline methods like TransUNet, nnUNet, and Swin UNETR. These baselines rely solely on image data, while the proposed approach leverages attribute annotations, giving it an advantage in performance comparisons. The paper needs to clarify how the attribute descriptions are encoded and integrated into the model architecture, and whether this integration is a simple concatenation or a more complex fusion mechanism. The ablation study should also include a comparison of the proposed method with and without attribute descriptions to quantify the contribution of these descriptions to the overall performance.
3. The fully-supervised performance of baseline methods reported in Table 2 appears unusually low. For instance, in the official nnUNet paper, liver tumor segmentation achieved a Dice score of 76 on the test set, whereas the presented result here is only 61.33. Similarly, lung tumor segmentation originally reported a Dice score of 74, but this paper reports 54.44. This discrepancy raises concerns about the reproducibility and fairness of the comparisons. The authors should provide a detailed explanation of the experimental setup used to reproduce the baseline results, including specific preprocessing steps, hyperparameter settings, and training protocols. A direct comparison with the reported results in the original papers is necessary to ensure the validity of the comparison.
4. In Table 7, the authors compare their method to existing vision-language pretraining strategies, but it is unclear how these methods were reproduced. Most vision-language pretraining approaches require access to diagnostic reports, which are not included in the public MSD and KiTS23 datasets. It would be helpful to understand how the authors conducted these comparisons without complete diagnostic reports. Furthermore, the paper should specify the exact pretraining datasets and training procedures used for the compared models. Additionally, the absence of comparisons with important pretraining models like CT-CLIP weakens the evaluation, as CT-CLIP is a widely used model in medical vision-language tasks.
5. Scalability of the proposed method is questionable due to its reliance on ATTRIBUTE DESCRIPTIONS. For practical clinical applications, this approach would require physicians to provide additional lesion descriptions across eight visual attribute aspects, which may not be feasible in all settings. This dependency could limit the method’s applicability in diverse clinical environments. The paper should discuss alternative approaches to obtain attribute descriptions, such as using natural language processing techniques to extract them from radiology reports or exploring methods to reduce the number of required attributes.

### Questions
please refer to Weaknesses

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces "Malenia," a framework for zero-shot 3D lesion segmentation using vision-language pre-training methods. This framework aligns multi-scale mask representations of lesions with textual embeddings of disease attributes, which facilitates the segmentation of unseen lesion types in medical imaging.

### Strengths
1. This study bridges the gap between mask representations and textual disease attributes for zero-shot lesion segmentation.
2. The empirical validation includes comprehensive experiments across multiple datasets and lesion types, demonstrating the robustness and effectiveness of Malenia.

### Weaknesses
1. While the paper effectively addresses 3D CT scans, it does not discuss the applicability of the Malenia framework to other imaging modalities like X-ray.
2. The paper does not discuss how the framework handles ambiguous or borderline cases where lesion boundaries are not well-defined or where lesions exhibit highly atypical appearances.
3. There is no thorough discussion on the limitations or failures of the proposed model.

### Questions
1. Could the authors provide insights on the computational efficiency of their framework?
2. This work and its motivation are similar to the previous works [1-2], please describe the differences between them.
[1] Li, Z., Li, Y., Li, Q., Wang, P., Guo, D., Lu, L., ... & Hong, Q. (2023). Lvit: language meets vision transformer in medical image segmentation. IEEE transactions on medical imaging.
[2] Huang, X., Li, H., Cao, M., Chen, L., You, C., & An, D. (2024). Cross-Modal Conditioned Reconstruction for Language-guided Medical Image Segmentation. arXiv preprint arXiv:2404.02845.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Malenia, a novel framework specifically designed for 3D zero-shot lesion segmentation in medical images. The authors aim to address the challenges of transferring image-level knowledge to pixel-level tasks—such as lesion segmentation—by proposing a multi-scale lesion-level mask-attribute alignment approach. Malenia improves the alignment between the visual features of unseen lesions with textual representations, leveraging Cross-Modal Knowledge Injection (CMKI) to enhance both visual and textual embeddings. Experimental results across three datasets demonstrate that Malenia outperforms state-of-the-art (SOTA) methods in zero-shot lesion segmentation.

### Strengths
1. The proposed Malenia framework is novel, particularly in its use of multi-scale mask-attribute alignment for 3D lesion segmentation. This is a meaningful extension of zero-shot segmentation methods to the medical domain, where unseen lesion categories are common (e.g., "hepatocellular carcinoma," mentioned in Sec. 1).
2. The CMKI module is a strong contribution because it combines visual and textual embeddings, enriching the segmentation prediction with complementary information from both modalities. This is a novel approach that enhances the zero-shot capability of the model.
3. The paper introduces a multi-positive contrastive loss to fine-tune the alignment between lesion masks and textual attributes. This approach allows the model to generalize better to unseen lesions by learning from shared visual attributes, which distinguishes it from prior works like SAM (Kirillov et al., 2023).

### Weaknesses
1. The method relies on transforming patient reports into structured descriptions of eight visual attributes, which requires expert radiologist involvement. This process may not be scalable or practical in real-world applications where such annotations are not readily available. The reliance on expert-defined attributes introduces a potential bottleneck, as the quality and consistency of these attributes directly impact the model's performance. Furthermore, the process of extracting these attributes from patient reports is not automated, making it difficult to apply the method to large datasets without significant manual effort.
2. As noted in Appendix D, the model performs less effectively on attributes requiring complex visual semantic understanding, such as "Surface Characteristics" and "Specific Features". This suggests a potential limitation in capturing intricate visual patterns. The model's difficulty with these attributes highlights a gap in its ability to understand subtle visual cues, which are often crucial for accurate lesion segmentation. For instance, the distinction between a smooth and irregular surface or the identification of specific, rare features can be highly dependent on contextual information and fine-grained visual analysis, which the model seems to struggle with.
3. While the model shows strong performance on 12 lesion categories, the diversity of lesions in clinical practice is vast. The ability of Malenia to generalize to a wider range of unseen lesions without additional training remains uncertain. The evaluation, while promising, is limited by the number of lesion categories used. The model's performance on a broader range of lesion types, including those with more complex or atypical visual characteristics, needs to be assessed to fully understand its generalization capabilities. The current evaluation does not fully address the challenge of real-world clinical variability.

### Questions
1. In Section 3.1, the authors employ the Multi-Positive InfoNCE (MP-NCE) loss for aligning mask embeddings with multiple attribute embeddings. Could the authors provide more details on how the MP-NCE loss is computed and how it facilitates learning with multiple positive pairs? Specifically, how are the positive and negative pairs defined in the context of multiple attributes?
   Could the authors explain how this formulation effectively handles multiple positive pairs for each mask token?
2. The model uses a fixed number of mask tokens ($N=16$) and defines $R=8$ attribute aspects. Have the authors conducted any experiments to assess how varying $N$ or the number of attributes affects the model's performance? An ablation study on these hyperparameters could provide insights into the model's sensitivity and optimal settings.
3. As noted in Appendix D, the model performs less well on attributes like "Surface Characteristics" and "Specific Features". What are the potential reasons for this lower performance? Could incorporating additional contextual information or advanced features help the model better capture complex visual semantics?

### Soundness
2

### Presentation
2

### Contribution
2
