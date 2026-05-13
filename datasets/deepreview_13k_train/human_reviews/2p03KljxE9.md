# Language-Assisted Feature Transformation for Anomaly Detection

- Decision: Accept
- Scores: 5, 5, 8, 6

## Abstract
This paper introduces LAFT, a novel feature transformation method designed to incorporate user knowledge and preferences into anomaly detection using natural language. Accurately modeling the boundary of normality is crucial for distinguishing abnormal data, but this is often challenging due to limited data or the presence of nuisance attributes. While unsupervised methods that rely solely on data without user guidance are common, they may fail to detect anomalies of specific interest. To address this limitation, we propose Language-Assisted Feature Transformation (LAFT), which leverages the shared image-text embedding space of vision-language models to transform visual features according to user-defined requirements. Combined with anomaly detection methods, LAFT effectively aligns visual features with user preferences, allowing anomalies of interest to be detected. Extensive experiments on both toy and real-world datasets validate the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a feature transformation method aimed at focusing on specific image attributes guided by language. The approach, termed Language-Assisted Feature Transformation (LAFT), leverages the shared embedding space of vision-language models (specifically CLIP) to modify image features according to user-defined concepts expressed in natural language, enabling enhanced anomaly detection capabilities without additional training.

### Strengths
- The authors explore a valuable research topic that contributes to the current body of knowledge—how to adjust decision boundaries using language to enhance CLIP’s anomaly detection performance. 
- The proposed method stands out due to its training-free nature, which provides flexibility in application across various tasks with limited data.

### Weaknesses
1. Figure 1 is not particularly intuitive or clear, and it is not explained in the text. Specifically, the visual representation of the concept axes and their relationship to the original feature space is unclear. The figure lacks annotations that would help the reader understand how the transformation is achieved. The connection between the 'nuisance' and 'important' attributes and their corresponding prompts is also not visually apparent, making it difficult to grasp the core idea of the methodology.

2. As the exact formulation of prompts is absolutely critical for this methodology, it should have more dedicated explanation in the main text of the paper, not relegated almost entirely to the appendix. The paper should detail the prompt engineering process, including the specific choices of words and phrases used to elicit the desired attribute representations. The lack of this information in the main text makes it difficult to assess the robustness and generalizability of the approach. The reader needs to understand the sensitivity of the method to prompt variations.

3. There are not many baselines, and it would be more convincing if you compare more baselines with and without LAFT transformations. The paper should include comparisons with state-of-the-art anomaly detection methods, both with and without the proposed LAFT transformation. This would provide a clearer picture of the added value of the proposed approach. The current set of baselines is insufficient to demonstrate the superiority of the method.

4. The range of experiments presented are quite restricted. For example with Coloured MNIST, it appears that only one number-colour combination as the normal set was tried. It would be more proper to conduct multiple experiments with different combinations of attributes and show the average result. The same can be said for the other datasets. The lack of diversity in the experimental setup makes it difficult to assess the generalizability of the method. The paper should include experiments with different combinations of normal and anomalous attributes to demonstrate the robustness of the approach.

### Questions
1. What does $c_i$ represent in Equations 5 and 6?
2. For zero-shot anomaly detection, can the transformed image features still match the text features effectively?

### Soundness
3

### Presentation
2

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
The paper introduces Language-Assisted Feature Transformation (LAFT), a novel framework that leverages vision-language models (like CLIP) to enhance anomaly detection. Traditional anomaly detection methods often struggle to capture user-defined nuances of normality, particularly when attributes are entangled or datasets are incomplete. LAFT tackles this by enabling feature transformations guided by natural language prompts. These prompts align visual features with user intent by projecting image features onto specific concept subspaces within a shared embedding space. The paper also proposes LAFT AD, a k-nearest-neighbor (kNN)-based method combining LAFT with anomaly detection, and extends this work into WinCLIP+LAFT, designed for industrial applications. The effectiveness of LAFT is demonstrated across datasets like Colored MNIST, Waterbirds, CelebA, and MVTec AD, showing superior performance in both semantic and industrial anomaly detection.

### Strengths
1. LAFT bridges a gap in anomaly detection by allowing users to express preferences using natural language, providing more control over what is considered "normal."
2. Unlike other feature transformation models, LAFT does not require additional training, making it efficient for settings with scarce data.
3. The experimental results demonstrate that LAFT outperforms state-of-the-art methods, particularly in semantic anomaly detection tasks.

### Weaknesses
1. While LAFT demonstrates significant improvements in controlled environments, such as the Colored MNIST dataset, its performance gains appear less pronounced when applied to complex real-world datasets. This discrepancy suggests that the model may struggle to maintain robustness across multiple intricate attributes, highlighting the need for further refinement in handling multi-attribute scenarios.
2. The experimental setup lacks comprehensive comparisons, particularly between language-assisted and vision-assisted approaches. For instance, incorporating image guidance by utilizing related reference normal images (e.g., normal digits in various colors) or color-augmentation for kNN baseline could provide valuable insights. A thorough examination of both language-based and vision-based assistance would strengthen the evaluation of LAFT's efficacy.
3. The impact of the number of PCA components, which is the sole hyperparameter in LAFT, is not adequately investigated. Given that this parameter influences the model's performance, it is crucial to explore its effect across different datasets. Specifically, an analysis of whether a larger number of components may be beneficial for more complex datasets would provide valuable insights into optimizing the model’s performance.

### Questions
1. In Table 8, the header refers to "bird," which is inconsistent with the title of the Colored MNIST dataset mentioned (maybe a typo). Could the authors clarify this discrepancy?
2. What are the sizes of the training sets for each dataset used in the experiments? Given that these samples serve as candidates for kNN search, how might the number of training samples affect the final performance of the model?
3. The experimental results on the MVTec AD dataset in Table 3 suggest that InCTRL might outperform WinCLIP+LAFT when considering deviation, especially when the number of shots exceeds 2. Could the authors provide detailed experimental results for each of the five different reference sample sets?

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
3

### Summary
This paper proposes a feature transformation methodology using concept axes, which are the principal components of the difference vectors between text embeddings of prompts specially designed to ignore nuisance attributes/highlight important attributes for anomaly detection.

### Strengths
The methodology is interesting and a solid contribution to this direction of research in vision-language modelling for anomaly detection.

The results appear to be promising in the experiments presented, although a wider range of experimental setups would be more convincing (see weakness) 

The ablation study is comprehensive.

### Weaknesses
1. Figure 1 is not particularly intuitive or clear, and it is not explained in the text. 

2. As the exact formulation of prompts is absolutely critical for this methodology, it should have more dedicated explanation in the main text of the paper, not relegated almost entirely to the appendix. 

3. There are not many baselines, and it would have been more convincing if you compare more baselines with and without LAFT transformations. 

4. The range of experiments presented are quite restricted. For example with Coloured MNIST, it appears that only one number-colour combination as the normal set was tried. It would be more proper to conduct multiple experiments with different combinations of attributes and show the average result. The same can be said for the other datasets.

### Questions
Please address the points raised in the Weakness section. Also:

1. What is the purpose of including Aux. prompts? 

2. How does different CLIP architecture and also different VLMs affect performance?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
On the basis of existing anomaly detection methods based on visual language alignment, this paper proposes using task related languages for task oriented feature information screening and transformation to improve the model's anomaly detection capability. The experiment was conducted on multiple datasets and demonstrated better performance compared with existing methods.

### Strengths
1. This paper is with clear motivation.
2. This paper is well-organized and easy to follow.

### Weaknesses
1. The criteria for selecting text prompts are ambiguous. Some datasets utilize the category names of the samples, while others employ diverse descriptions. These approaches rest on the critical assumption that anomalies are distinctly defined, exemplified by MNIST, where anomalies arise from differences in numerals rather than variations in handwriting styles or colors. Should the actual anomalies diverge from these presuppositions, might the proposed model's performance diminish relative to methods devoid of textual guidance? In other words, could the model forfeit its capacity to detect all possible anomalies?

2. In the MVTec dataset experiment, the author opted not to employ the concise anomaly descriptions provided by the dataset itself for text prompts, instead relying solely on item categories, mirroring the approach of WinCLIP. What rationale informed this decision?

3. The proposed model is an extension of WinCLIP, yet it appears to forgo the anomaly segmentation functionality inherent to WinCLIP. Is this omission attributable to certain design elements that potentially diminish the model's anomaly localization capabilities?

4. Experiments have been conducted on synthetic datasets like MNIST and CelebA by altering the original datasets. While I acknowledge the challenge of selecting appropriate text prompts for real-world datasets such as MVTec, the author should endeavor to incorporate more authentic datasets into their study, such as the VisA dataset utilized in WinCLIP or the medical AD benchmark employed in MVFA [a].

[a] Adapting Visual-Language Models for Generalizable Anomaly Detection in Medical Images. CVPR 2024.

### Questions
See the weakness.

### Soundness
3

### Presentation
3

### Contribution
3
