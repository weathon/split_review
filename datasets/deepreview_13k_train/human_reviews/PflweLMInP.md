# Complete multi-modal metric learning for multi-modal sarcasm detection

- Decision: Reject
- Scores: 5, 3, 3, 10

## Abstract
Multi-modal sarcasm detection identifies sarcasm from text-image pairs, an essential technology for accurately understanding the user's real attitude.
Most research extracted the incongruity of text-image pairs as sarcasm information. However, these methods neglected inter-modal or intra-modal incongruities in fact and sentiment perspectives, leading to incomplete sarcasm information and biased performance.
To address the above issues, this paper proposes a complete multi-modal metric learning network (CMML-Net) for multi-modal sarcasm detection tasks.
Specifically, CMML-Net utilizes a fact-sentiment multi-task representation learning module to produce refined fact and sentiment text-image representation pairs.
It then designs a complete multi-modal metric learning to iteratively calculate inter-modal and intra-modal incongruities in a unified space (e.g., fact and sentiment metric space), efficiently capturing complete multi-modal incongruities.
CMML-Net performs well in explicitly capturing comprehensive sarcasm information and obtaining discriminative performance via deep metric learning.
The state-of-the-art performance on the widely-used dataset demonstrates CMML-Net's effectiveness in multi-modal sarcasm detection.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a novel framework called the Complete Multi-Modal Metric Learning Network (CMML-Net) designed for multi-modal sarcasm detection, leveraging both text and image data. This task is complex due to sarcasm's reliance on implicit contrasts, often between literal meanings and actual sentiments or facts. The CMML-Net improves sarcasm detection by identifying these contrasts through inter-modal (between text and image) and intra-modal (within each modality) incongruities, enhancing sarcasm recognition accuracy. In general, the CMML-Net demonstrates a significant advancement in multi-modal sarcasm detection, providing a repeatable and well-organized structure for detecting sarcasm with high accuracy. The model’s design effectively captures multi-dimensional incongruities, though its computational demands and current scope might limit broader real-time and cross-modal applications.

### Strengths
1. The modular structure of CMML-Net enables clear, systematic analysis of sarcasm, making the model robust and extensible for future research. The dual-stream network is meticulously designed to assess sarcasm through both fact and sentiment incongruities, improving detection accuracy.

2. By building upon existing work and leveraging well-established models, the CMML-Net is highly repeatable, with well-documented performance on benchmark datasets.

### Weaknesses
1. The paper lacks clarity due to some undefined symbols and terms. For instance, the architecture is based on "units" in section 3.2 that are repeatedly referenced as learnable, but their exact nature is not defined. It is unclear whether these units are neuron clusters, specific network layers, or memory mechanisms designed to integrate multiple modalities. Additionally, other symbols, such as the capital "S" and "F," are not explicitly defined. While "S" seems to represent sentiment-related information, the meaning of "F" is ambiguous and should be clarified. Could you please clarify those terms where they are firstly introduced?

2.  The paper’s focus on multi-modal sarcasm detection is narrow, limiting its potential impact and relevance for the broader machine learning community. Could you please give some potential broader implications or applications of their work beyond sarcasm detection. 
3.  The framework is built largely on existing approaches, enhancing its reproducibility. However, this reliance on established methodologies limits its originality, as there is a lack of significant methodological contribution. This may affect its impact within the research community, which typically values innovation in addition to reproducibility.

### Questions
See in weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel network, CMML-Net, designed for detecting sarcasm in text-image pairs. The network addresses the limitations of previous methods that focused solely on inter-modal incongruities, neglecting intra-modal incongruities. CMML-Net employs a fact-sentiment multi-task representation learning module to generate refined representations and a complete multi-modal metric learning approach to iteratively calculate inter-modal and intra-modal incongruities in both fact and sentiment metric spaces. The model demonstrates state-of-the-art performance on the Multimodal Sarcasm Detection (MSD) dataset, outperforming existing methods by capturing more comprehensive sarcasm information.

### Strengths
1.	This paper is well-written with a clear and concise expression.
2.	The authors have conducted a thorough set of experiments, which is a significant strength of the paper.

### Weaknesses
1.	The summary of related work is incomplete.
2.	The authors mention that previous work neglected the importance of intra-modal incongruity in sarcasm detection, leading to incomplete incongruities and biased performance, but do not provide reasons why intra-modal incongruity is useful for sarcasm. It is suggested to use examples in the Introduction section to intuitively demonstrate this.
3.	The authors mention two innovative points in the Introduction section, but these two points essentially seem to be the same.
4.	The authors explain that "Fact incongruity means sarcasm occurs when the literal meaning and the observed facts unexpectedly contrast." Additionally, in the method design, both the FISN and SISN modules take the combined results of image and text as input. This indicates that the work primarily focuses on addressing inter-modal incongruities. However, the authors describe the FISN and SISN as aiming to capture both intra-modal and inter-modal incongruities (Sections 3.2.1 and 3.2.2). Where is the intra-modal incongruity reflected?
5.	Only one dataset is considered in the experiments, such as MMSD2.0 and MSTI, which are not included, and the generalizability of the method cannot be demonstrated.
6.	The Main Result lacks significance analysis.
7.	In Section 4.6, the authors analyze the YOLO-task representation, but is it possible to replace it with other models to achieve multimodal sarcasm detection results based on different backbones?

### Questions
Please see the Weaknesses.

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
5

### Summary
This work focus on multimodal sarcasm detection task. As existing works neglected inter-modal or intra-modal incongruities in fact and sentiment perspectives, their performance exist a bias. To achieve this, this paper proposes a complete multi-modal metric learning network (CMML-Net) for multi-modal sarcasm detection tasks. Extensive experiments demonstrates the effectiveness and the scalability of the proposed CMML-Net.

### Strengths
1.	The proposed CMML-Net model achieves the state-of-the-art performance on different datsets.
2.	Ablation studies validate the necessity of each component. Visualizations provide intuitive understanding.
3.	The related literatures are well covered.
4.	This work provides code for reproduce.

### Weaknesses
1.	Lack of insights in the proposed approach. Motivation of the proposed module in the overall framework is unclear in this paper.
2.	The method of this paper exhibits limited novelty. In my opinion, introducing the Yolo task, the face stream aims to find the image-based incongruity. However, the image-based incongruity have been discussed in existing works. And they proposed many effectiveness approach to solve this problem.[1,2,3,4]
3.	There is unclear motivation of why this paper introduces deep metric learning. And what’s it’s advantage compared to traditional deep learning in existing works?
4.	This paper highlights the incongruity from two perspective: fact and sentiment. The sentiment aspect is easy to understand. However, there lacks more discussion on why the fact aspect is important for multimodal sarcasm detection in introduction section.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
This paper proposes a complete multi-modal metric learning network (CMML-Net) for multi-modal sarcasm detection tasks. Specifically, CMML-Net utilizes a fact-sentiment multi-task representation learning module to produce refined fact and sentiment text-image representation pairs. It then designs a complete multi-modal metric learning to iteratively calculate inter-modal and intra-modal incongruities in fact and sentiment metric spaces, explicitly capturing complete multi-modal incongruities. CMML-Net performs well in explicitly capturing comprehensive sarcasm information and obtaining discriminative performance via deep metric learning. The state-of-the-art performance on the widely-used dataset demonstrates CMML-Net's effectiveness in multi-modal sarcasm detection.

### Strengths
1.The authors use the method of metric learning to study multimodal sarcasm detection, which is innovative.

2.The authors provide a detailed analysis of the effectiveness of each module.

3.The author makes a detailed analysis of the inconsistencies of multimodal irony in images and texts.

### Weaknesses
1.Metrics Learning Related Work: This paper is inspired by metrics learning, but lacks work on metrics learning.

2.Typographical errors: There are errors in some of the corner marks in the text, e.g. line 140. Some punctuation errors, such as line 148. Some sentences are redundant, such as lines 165 to 167.

3.Row 153: What is the size of the target range k and whether it will affect the module.

4.Inadequate experimentation: It is not enough to adopt only one dataset, more datasets including MMSD2.0 [1], DMSD [2], RedEval [3] verification model need to be adopted.

5.Supplemental baseline: Comparisons of relevant sarcasm detection work are missing, and it is recommended to add, e.g., G2SAM[4], DynRT-Net[5], DMSD-CL[2].

### Questions
None

### Soundness
4

### Presentation
3

### Contribution
4
