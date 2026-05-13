# URLOST: Unsupervised Representation Learning without Stationarity or Topology

- Decision: Reject
- Scores: 6, 5, 6

## Abstract
Unsupervised representation learning has seen tremendous progress but is constrained by its reliance on data modality-specific stationarity and topology, a limitation not found in biological intelligence systems. For instance, human vision processes visual signals derived from irregular and non-stationary sampling lattices yet accurately perceives the geometry of the world. We introduce a novel framework that learns from high-dimensional data lacking stationarity and topology. Our model combines a learnable self-organizing layer, density adjusted spectral clustering, and masked autoencoders. We evaluate its effectiveness on simulated biological vision data, neural recordings from the primary visual cortex, and gene expression datasets. Compared to state-of-the-art unsupervised learning methods like SimCLR and MAE, our model excels at learning meaningful representations across diverse modalities without depending on stationarity or topology. It also outperforms other methods not dependent on these factors, setting a new benchmark in the field. This work represents a step toward unsupervised learning methods that can generalize across diverse high-dimensional data modalities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose to extend the utility of unsupervised representation learning under the relaxation of conventional assumptions related to stationarity and topology. They are inspired by biological visualization systems and assert that the existing ansatz are not sufficiently inclusive of general high-dimensional data.

### Strengths
The authors ground their approach in a concrete example that is returned to throughout thereby helping the reader to build a stronger understanding and intuition for the work.

Method is demonstrated for multiple modalities suggesting its broader utility. The method seems to possess impactful new capabilities.

Figures and result tables are clear with reasonably informative captions-- something that is not always the case and greatly appreciated.

### Weaknesses
The core findings and impact to the field are not clearly identified in the introduction. They include the questions they aim to answer and a high-level description of their approach but concrete claims or impact are omitted. While the reviewer was very intrigued by the paper, the primary weakness was the lack of a clear statement of the "so what?"

While helpful for building intuition, the classification accuracy studies are less compelling as they feel more contrived yet they get the bulk of the attention. From this viewer's perspective, the presented method's potential to be able to infer the permutation or inform about the topology or stationarity of data is the more novel component. Although it may just be a personal preference, I think highlighting and demonstrating those unique abilities would emphasize the novelty and utility of the method. 

Results tables should include confidence intervals. 

In this reviewer's estimation there is insufficient information available for reproducibility within the main body of the paper.

### Questions
What are the top three claims or novel contributions of the work from the authors' perspective? 

What can the proposed approach tell you about the stationarity and topology of the data it is provided?

Are there connections between this work and encryption/decryption?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
The paper introduces a novel method for unsupervised representation learning which can handle signals lacking an explicit topology. The method is then evaluated on synthetic biological vision datasets,

### Strengths
The problem considered by the author seems relevant and their method intriguing, but I do not have enough experience in the field to give a proper judgement of the strengths.

### Weaknesses
See above. Additionally, some concepts introduced in the text are poorly defined and impossible to understand for a non-expert.

1. In section 2.2, what are the 'dimensions' i and j? What is the manifold M? How do you define a Laplacian based on A? The description of how the affinity matrix A is constructed is missing, making it difficult to understand how the Laplacian is derived. Specifically, it's unclear what features are used to compute the affinity between data points, and how the affinity values are determined. Without this, the Laplacian construction is ambiguous.
2. After equation 1, what density does p(x) represent? The role of p(x) is not clear in the context of the overall method. It's unclear how this density function relates to the data or the problem being addressed.
3. Section 2.3, the intended meaning of alignment is not clear to me. The idea of directly solving the alignment problem with low-level statistics is completely obscure: What is the alignment problem? It's unclear why a self-organization layer is necessary, and how it relates to the spectral clustering performed earlier. The connection between the low-level statistics and the alignment is not well established.
4. What are the metrics used for evaluation in Table 1?

### Questions
see above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a framework for unsupervised representation learning that overcomes the limitations of stationarity and topology. It combines a learnable self-organizing layer, density adjusted spectral clustering, and masked autoencoders to learn representations from high-dimensional data without relying on stationarity or topology. The model is evaluated on various datasets, including simulated biological vision data, neural recordings from the primary visual cortex, and gene expression datasets. Results show that the proposed method works well. The approach demonstrates promise for building unsupervised representations across high-dimensional data modalities, including modalities in natural sciences like chemistry, biology, and neuroscience.

### Strengths
- The paper is well-written. A clear structure can enhance the readability and understanding of a paper. However, the decision to reuse a large Figure 1 from multiple papers raises questions about the originality and visual presentation of the work. Creating a unique figure would enhance the paper's credibility and make it more visually cohesive.

- The underlying idea is recognized as interesting and well-motivated. The paper successfully conveys the rationale behind each stage of the proposed method.

- The paper conducts various experiments on different datasets, including simulated biological vision data, neural recordings, and gene expression datasets. This demonstrates the versatility and applicability of the proposed method across different modalities.

### Weaknesses
 - The paper is well-written. A clear structure can enhance the readability and understanding of a paper. However, the decision to reuse a large Figure 1 from multiple papers raises questions about the originality and visual presentation of the work. Creating a unique figure would enhance the paper's credibility and make it more visually cohesive.

- The underlying idea is recognized as interesting and well-motivated. The paper successfully conveys the rationale behind each stage of the proposed method.

- The paper conducts various experiments on different datasets, including simulated biological vision data, neural recordings, and gene expression datasets. This demonstrates the versatility and applicability of the proposed method across different modalities.

 - The combination of well-known techniques in a pipeline is noted as a potential limitation. The lack of an end-to-end deep learning architecture is highlighted, questioning the level of innovation in the proposed method.

- The absence of information on seed-related results makes it challenging to fully interpret and reproduce the reported results. More comprehensive reporting of experimental methodologies would strengthen the paper's scientific rigor. More transparency in the experimental methodology and inclusion of uncertainty statistics would enhance the robustness of the reported results.

- The real-world dataset results are currently unconvincing. The reported accuracy metrics are comparable, and the absence of uncertainty statistics diminishes the robustness of the claims. More detailed analysis and statistical measures are needed to support the performance claims on real-world datasets.

### Questions
Refer to the comments above.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair
