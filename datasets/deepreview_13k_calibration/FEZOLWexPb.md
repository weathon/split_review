# MAESTRO: Masked Encoding Set Transformer with Self-Distillation

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
The interrogation of cellular states and interactions in immunology research is an ever-evolving task, requiring adaptation to the current levels of high dimensionality. Cytometry enables high-dimensional profiling of immune cells, but its analysis is hindered by the complexity and variability of the data. We present MAESTRO, a self-supervised set representation learning model that generates vector representations of set-structured data, which we apply to learn immune profiles from cytometry data. Unlike previous studies only learn cell-level representations, whereas MAESTRO uses all of a sample's cells to learn a set representation. MAESTRO leverages specialized attention mechanisms to handle sets of variable number of cells and ensure permutation invariance, coupled with an online tokenizer by self-distillation framework. We benchmarked our model against existing cytometry approaches and other existing machine learning methods that have never been applied in cytometry. Our model outperforms existing approaches in retrieving cell-type proportions and capturing clinically relevant features for downstream tasks such as disease diagnosis and immune cell profiling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents MAESTRO, a self-supervised learning method tailored to learn representations of high-throughput cytometry data. The complexity and variability of the data makes it impossible to directly apply many of the previously developed techniques, so the authors come up with a new method using the existing teacher-student architecture to learn representations of immune profiles. The authors present evidence of effective data reconstruction, probe representations in predicting sample diagnosis and cell type proportion, and demonstrate superior performance to existing techniques. In addition, the authors report results of the ablation study to justify the design of MAESTRO.

### Strengths
- I appreciated the detailed and comprehensive method description. Clearly structured and explained in sufficient detail. Although many of the blocks are not novel, such a presentation helps understanding the work.
- The contribution of the work looks solid, as demonstrated in the experiments. The design of the proposed method is justified with an ablation study. The performance appears superior to previously proposed methods.
- Arguably, there exist few solutions capable of handling high-throughput cytometry data to this day. MAESTRO seems to make a significant contribution in the domain by tackling this challenge effectively.

### Weaknesses
1. It seems that the work addresses an existing task and tackles it by integrating existing concepts and approaches into a new framework. Therefore, the novelty of this work appears limited and must be further clarified by the authors. The core idea of using a teacher-student architecture for self-supervised learning is not new, and the specific implementation details, while well-presented, do not introduce a fundamentally novel approach to representation learning. The use of attention mechanisms for set-based data is also established, raising questions about the incremental contribution of this work.
2. Evaluation is done on a single dataset, which is generally not enough to showcase the effectiveness and robustness of the newly presented method. The cited DeepCyTOF, for example, employed five collections of FCM datasets from FlowCAP-I and three additional collections of CyTOF datasets. The lack of evaluation across diverse datasets limits the generalizability claims and makes it difficult to assess the method's performance under varying experimental conditions and data distributions. The single dataset, even if large, may not capture the full spectrum of variability present in cytometry data.
3. Data and code availability are not discussed. For a method paper, an anonymized repository must be provided for reviewers to verify the soundness and validity of the approach. Without access to the code and data, it is impossible to reproduce the results and assess the implementation details, which is crucial for a method-focused paper.
4. The authors cite the paper of [cyMAE](https://www.biorxiv.org/content/10.1101/2024.02.13.580114v2) to claim that manual gating remains state of the art, while this very method was introduced at the NeurIPS 2023 Workshop AI4Science as the first effort to achieve (and, arguably, surpass) this state-of-the-art performance. Comparison to cyMAE is neither presented, nor discussed, which is a questionable choice of the study design. The lack of comparison to a method that claims to surpass manual gating, especially when that method is directly relevant to the data type, is a significant oversight.
5. Only a few concluding remarks are dedicated to the limitations of the approach. More discussion points could follow from the additional evaluations that are currently missing. A more thorough discussion of the limitations, including potential biases, computational costs, and sensitivity to hyperparameters, is needed to provide a balanced perspective on the method's applicability.
6. References look limited suggesting the authors might not be aware of the other important works in the field. Also, some statements are missing citations (e.g., lines 83-92), which complicates validity assessment. The lack of citations for specific claims makes it difficult to assess the validity of the statements and the context of the work within the broader literature. The limited references suggest a potential lack of awareness of relevant prior work.
7. Minor flaws:
- line 296: missing bracket typo
- line 313: double-quote typo
- line 317: “Algorithm 0” typo

### Questions
__Contributions__

1. Is MAESTRO tailored to the analysis of immune profiles? How well can it generalize beyond that? What would be the evidence of that? If there are no additional experimental results, please discuss potential applications of MAESTRO to set-structured data outside of immunology, and what modifications, if any, might be needed for such applications.
2. What is the strongest argument to defend the novelty of this work?

__Figure 3b__

3. How do you explain values for Sepsis, Vasculitis, and two types of COVID?

__Table 1__

4. If manual gating performs so poorly, why is it called the golden standard? Please discuss reasons it remains widely used despite the emergence of more accurate computational methods and consider abstaining from calling it a gold standard.
5. The table includes 2 methods that are supervised. However, the [cyMAE paper](https://www.biorxiv.org/content/10.1101/2024.02.13.580114v2)  suggests that it is gradient boosting decision trees (GBDT) that achieve top performance among the supervised learning algorithms. Why is there no comparison to GBDT?
6. Is a single linear probing task enough to evaluate the discriminative power of the learned representations? Is it possible they are biased towards sample diagnosis? Please include other evaluation tasks to provide a more comprehensive assessment of the learned representations.

__Evaluations__

7. Some other methods have been included for comparison despite the fact that they are incapable of handling large datasets. To make it possible, the authors sampled 10k cells for each sample ranging from 11k to 1386k cells in total. How fair and informative is that comparison? Were the other methods optimized to achieve their top performance under such conditions? Is it possible to compare MAESTRO to the other methods on a subset of the large dataset under entirely identical conditions? Please provide a more detailed justification for the comparison methodology.

### Soundness
3

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
3

### Summary
The authors developed a method called MAESTRO (Masked Encoding Set Transformer with Self-Distillation) to effectively capture and summarize the diverse characteristics of immune cells from cytometry data. MAESTRO leverages a specialized attention mechanism and a self-distillation framework within a self-supervised learning setup, enabling it to handle large datasets without information loss. The model generates sample-level representations from the data. The authors evaluated MAESTRO’s embeddings to determine whether they can support downstream diagnostic classification, and enable cell-type proportion prediction.

### Strengths
The manuscript is well-written and easy to follow. The proposed method is effectively designed to handle large datasets without losing sample information. Additionally, the model addresses permutation invariance by using specialized attention blocks that omit positional encodings. This design enables MAESTRO to generate robust, representative embeddings for diagnostic classification and cell-type proportion prediction.

### Weaknesses
(1) The model was evaluated only on datasets from similar experimental settings, which contain minimal batch effects. It is unclear how the method handles batch effects or how the resulting embeddings may be influenced by such variations. Specifically, the lack of evaluation on datasets with known, significant batch effects raises concerns about the generalizability of the method. The authors should consider evaluating the model on datasets with more pronounced batch effects to demonstrate its robustness in real-world scenarios. (2) According to the description, the detected proteins could be different between cells. Currently, the authors select and focus only on the shared detected proteins across all the samples. This approach may discard valuable information present in non-overlapping protein markers. The authors should explore methods to incorporate data from all detected proteins, potentially using techniques like masking or imputation for missing values. (3) Additionally, the model primarily generates sample-level embeddings, whereas producing cell-level (for each cell) and feature-specific (for each feature) embeddings could be valuable for downstream comparisons. The current focus on sample-level embeddings limits the granularity of analysis. Cell-level embeddings could enable more detailed investigations of cellular heterogeneity, while feature-specific embeddings could reveal important patterns in protein marker expression. (4) Further details on the method's runtime, robustness, and memory usage would also be beneficial. The absence of this information makes it difficult to assess the practical applicability of the method, especially for large-scale datasets.

### Questions
See the weakness section.

### Soundness
3

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
In the paper, the authors proposed MAESTRO, a set-transformer-based method that design for generate the sample embeddings and cell embedding for the cytometry data. The authors compared several baseline method, conducted ablation studies, and further checked the effectiveness of the sample/cell embeddings on sample classification/cell type proportion retrieval.

### Strengths
The paper is generally well written and easy to follow.

The authors considered the specific needs for the cytometry data, such as variable set size, large data scale, and the permutation-invariant problem and designed their model, which is great and add a layer of novelty.

### Weaknesses
The downstream experiments presented in sections 4.3 and 4.4 of the manuscript, which focus on sample classification, are adequately performed. However, the section 4.5 dealing with cell type distribution retrieval does not meet the same standard. The rationale behind fine-tuning the embedding for this task is unclear, given the variability and sample-dependence of cell type distributions. This approach lacks the robustness required for generalization across different datasets.

Furthermore, the manuscript does not convincingly demonstrate the utility of the proposed embeddings in broader cytometry tasks. Downstream applications such as zero-shot cell classification, zero-shot sample characterization beyond disease/health state, and protein representation are notably absent. Incorporating these biologically meaningful experiments would significantly enhance the value and applicability of the research. More rigorous and diverse testing of the embeddings on a range of cytometry tasks is essential to establish their effectiveness and relevance in the field.

I did not get the biological importance on the permutation-invariant module. Any downstream tasks to show the effectiveness of the module?

### Questions
See weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
MAESTRO introduces a self-supervised set transformer framework for analyzing cytometry data, which is known to be challenging due to its high dimensionality, permutation invariance, and variable sample sizes. Using masked encoding and a self-distillation approach, the model generates vector representations of immune profiles by leveraging attention mechanisms to handle set-structured data. MAESTRO performs better cell-type proportion retrieval and disease phenotype classification than state of the art techniques, improving single-cell analysis in immunology research.
Since cytometry datasets contain millions of cells per sample, MAESTRO proposes a three -fold strategy :
- A SSL set representation approach with a permutation-invariant attention mechanisms (using __ISAB, PMA, SAB__); 
- A masked encoder (__NRBM__) that enables to process large cytometry datasets efficiently;
- A teacher-student model for self-distillation via __EMA__.

Thus, MAESTRO learns holistic representations of entire cell sets, capturing both global (sample-level) and local (cell-type) information.

### Strengths
- __Originality__: The paper presents a novel idea to deal with million-row size cytometry dataset, as single cells ones are, providing a model, MAESTRO, that can capture sample membership information without losing cell population-level interactions rather than uniquely focusing on individual cells. 
- __Quality__: The manuscript clearly explains how to face the challenges of large single-cell cytometry datasets exploiting and combining previous-field ideas not deeply applied by compared models yet.
- __Clarity__: The paper is quite well written, with no major typos or incomprehension.
- __Significance__: The manuscript, presents a novel idea to face a common problem in a large cytometry dataset, and may well-impacts research due to its:           
     - __SSL__ module that doesn’t require any label-acquisition process for training, which is particularly costly for these datasets;
     - ISAB, PMA, and SAB (__Eqs. 5-7__) that are finely tuned to maintain permutation invariance, a critical feature for handling unordered sets like these; 
     - NRBM (__Alg.1__) rather than random masking to contain cell-populations level information.

### Weaknesses
 - **Patient-batch limitations:**  
   - The manuscript doesn’t address the problem of patient-normalization in scenarios where the model may have to deal with a heterogeneous cohort of patients. Cytometry patients' samples may vary a lot in a heterogenous cohort, and further studies on this generalization process could extend MAESTRO applicability (e.g. https://pubmed.ncbi.nlm.nih.gov/31633883/). For example, authors could specify whether would make sense to __inject__  __patient-level__ information as __prior knowledge__ during the pre-training phase.

-  **Scalability concerns with self-distillation on larger datasets and different batch sizes:**  
   - This approach may become less effective as datasets start spanning over large patient cohorts since MAESTRO  has been pre-trained on four GPUs at a time, with corresponding  __batch_size=1__, meaning four samples at once have been processed. Under extremely large datasets, feeding the teacher model with complete sets can lead to substantial memory requirements. The current implementation, with a batch size of 1, raises concerns about the model's ability to generalize across diverse patient populations, as it might be learning specific patient characteristics rather than generalizable biological patterns. Furthermore, the computational cost of processing each sample individually during self-distillation could become prohibitive for larger datasets.

-  **Dealing with noisy input:**
   - It’s not explicitly addressed the robustness of MAESTRO when dealing with noisy inputs, such as debris, dead cells that may be inherited from other cytometry datasets (e.g. flow cytometry ones), and whether this could or couldn’t be taken into account in the SSL strategy. The lack of discussion on how the model handles such artifacts is a significant gap, as these are common in real-world cytometry data and can affect the reliability of the learned representations. The model's performance could be significantly impacted by the presence of these noisy elements, leading to inaccurate downstream analysis.

### Questions
Authors, in addition to the __above__ cited __perplexities__, may illustrate whether they have plans for exploring the following points:
   1. How does the __choice of protein markers__ affect MAESTRO’s performance and generalizability;
   2. How MAESTRO would perform on __multi-modal__ data types like epigenomic data, e.g. __ATAC-seq__;
   3. How MAESTRO’s embedding can support unsupervised tasks like __clustering__ or anomaly (__blast__ population) __detection__, in a potential __diagnosis__ scenario.

### Soundness
3

### Presentation
3

### Contribution
4
