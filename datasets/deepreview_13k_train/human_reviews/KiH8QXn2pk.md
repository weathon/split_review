# PPTSER: A Plug-and-Play Tag-guided Method for Few-shot Semantic Entity Recognition on Visually-rich Documents

- Decision: Reject
- Scores: 6, 8, 3

## Abstract
Visually-rich document information extraction (VIE) is a vital aspect of document understanding, wherein Semantic Entity Recognition (SER) plays a significant role. However, the study of few-shot SER on visually-rich documents remains largely unexplored despite its considerable potential for practical applications. To address this issue, we propose a simple yet effective Plug-and-Play Tag-guided method for few-shot Semantic Entity Recognition (PPTSER) on visually-rich documents. PPTSER is a pluggable method building upon off-the-shelf multi-modal pre-trained models. It leverages the semantics of the tags to guide the SER task. In essence, PPTSER reformulates SER into entity typing and span detection, handling both tasks simultaneously via cross-attention. Experimental results illustrate that PPTSER outperforms fine-tuning baseline and existing few-shot methods, especially in low-data regimes. With full training data, PPTSER achieves comparable or superior performance to fine-tuning baseline. Specifically, on the FUNSD benchmark, our method improves the performance of LayoutLMv3 in 1-shot, 3-shot and 5-shot scenarios by 15.61%, 2.13%, and 2.01%, respectively. On the XFUND-zh benchmark, it improves the performance of LayoutLMv3 by 3.73%, 6.16%, and 4.01%, respectively. Overall, PPTSER demonstrates promising generalizability, effectiveness, and plug-and-play nature for few-shot SER on visually-rich documents. The codes will be available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents PPTSER, a few-shot method for semantic entity recognition on visually-rich documents. In PPTSER, SER tags are concatenated with the document tokens to serve as the input, and the class-wise logits are extracted from the last self-attention layers for few-shot learning and inference. The authors decouple the SER task into entity typing and span detection, and perform classifications on the two sub-tasks via extracting attention on two set of tags. PPTSER shows consistent improvements in few-shot settings on a range of datasets.

### Strengths
- PPTSER shows strong improvements in few-shot SER.
- The architecture can be applied into all kinds of transformer-based multi-modality model.
- The method's presentation is clear and well-structured, with a transparent design and motivations.
- The rationality is verified by careful analysis, strengthening the credibility of the proposed approach.

### Weaknesses
The paper acknowledges that using NER tags as prompts has been explored in text-based NER. This diminishes the novelty of the paper and raises concerns about its contribution in comparison to existing work.

### Questions
The paper mentions text-based few-shot NER frameworks in the Related Work. It would be valuable to clarify if these frameworks can be directly applied to SER on visually-rich documents with minimal or no significant modifications. If yes, a comparison with PPTSER would provide insights into its advantages and novelty.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To address few-shot Semantic Entity Recognition (SER) in visually-rich documents, the authors introduce PPTSER, a pluggable approach to existing multimodal pre-trained models. PPTSER reframes SER into two sub-tasks: entity typing, which assigns entity types to each token in the document, and span detection, which determines whether tokens are at the beginning or middle of an entity span. The core of PPTSER involves (1) using SER tags as a prompt, concatenating them with the document’s tokens, and inputting them into a multimodal pre-trained model, and (2) using the attention weight from the last attention block between the tag-related prompt and the document’s tokens as the probability of tokens belonging to each tag. Consequently, PPTSER eliminates the need for a classifier layer, reducing the total number of parameters. Experimental results on widely used SER benchmarks demonstrate that PPTSER outperforms both traditional fine-tuning methods and few-shot methods in both few-shot and full-data scenarios. The authors also conduct additional analyses of PPTSER to validate its effectiveness.

### Strengths
PPTSER can be considered an original and significant contribution to the field. This is the first method that leverages cross-attention between tokens and tags to predict entities for SER tasks. Experimental results demonstrate that PPTSER significantly outperforms other models  in both few-shot and full-training-set scenarios. In addition, the model can be plugged to any pre-trained model, providing a versatile approach. The paper is overall clear and well-written.

### Weaknesses
Section 3.2 could be made clearer by using a more formal formulation of the model -- rather than giving the building blocks of the neural architecture. There are many complexities introduced because of this low level description.

In section 3.2 also, It would be good also to provide an example of an input sequence augmented with a tag-related prompt would improve comprehension.

No experimental details are given in section 4 (reproducibility issues).

### Questions
In section 3.2.1, could you clarify the last paragraph. Why the special "-1" is needed? It might be easier to just ignore the $\tilde c$ in the span detection loss.

In eq. (2), how are the matrices $Q$ and $K$ determined?

In section 4, the experimental protocol is not described (and no information in appendix on this side):

- Please give details (training details)
- In section 4.3, could you explain how PPTSER was trained?

In section 5 “Analysis”, could you specify the proportion of unrelated words added to the prompt?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a plug-like label-guided method for few-shot entity recognition in visually rich documents. The approach leverages the semantics of tags to guide the SER task, resulting in good performance even with limited data. The method surpasses fine-tuned baselines and existing few-shot methods on various few-shot benchmarks.

### Strengths
1.	The proposed method demonstrates effectiveness in few-shot VRD entity recognition tasks. 

2.	The approach is intriguing as it utilizes the semantics of tags to guide the SER task. 

3.	The experimental results showcase that the proposed method outperforms fine-tuning baselines and other existing few-shot SER methods, particularly on the FUNSD and XFUND-zh benchmarks.

### Weaknesses
1.  The novelty is needed to be justified just as the motivation is not clear given the proposed architecture utilizing cross-attention has been widely discussed in NER for pure text.

2.  Does the issue of label leakage exist in the current training and testing scheme? Whether the prompts are also used again in testing?  

3.  The figures in the paper exhibit a significant amount of overlap and difficult to understand. The presentation way needs to improve.

### Questions
1.	While the author claims to have addressed the challenge of the “In-Label-Space setting for few-shot SER,” this challenge is not adequately introduced in this paper. Furthermore, it is crucial to acknowledge that the In-Label-Space setting may deviate from the real-world challenges encountered in few-shot/zero-shot/meta-learning scenarios. In most cases, our primary interest in this field lies in enabling machines to learn novel entity types rather than knowing “B-XX” to infer “I-XX”.

2.	Since Figure 2 appears to be less informative on its own, a better approach would indeed be to combine Figure 1(b) and Figure 2. This combination would provide a clearer representation of the reputation within the context of these two figures.

3.	Regarding LayoutLMs and aligning multimodal inputs, it is important to consider how spatial/visual embeddings are handled for tag-related prompt tokens. 

4.	In Figure 2, there are two parts labeled as “other embeddings.” It would be helpful to understand the distinction between these two parts.

5.	The datasets used in this study, such as FUNSD and XFUND-zh, are indeed relatively small and contain only a few entity types (e.g., only 3 in FUNSD). This limitation makes it challenging to fully assess the effectiveness of the In-Label-Space setting for few-shot SER on these specific datasets. Using CORD is suitable, but not enough.

6.	The paper mentions that “words related to SER tags are used as a prompt,” but it is not adequately explained what the tag-related prompt actually contains or how it is constructed. It would be beneficial for the author to provide some examples or utilize a running example prompt to illustrate the training process more clearly. This would help readers better understand what occurs during training and how the tag-related prompt influences the model’s performance.

7.	Table 1 shows marginal improvements when using the full data but significant improvement when using only a few instances. However, for CORD, the improvement is not as significant. The reason behind this discrepancy is unclear and requires further investigation.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
