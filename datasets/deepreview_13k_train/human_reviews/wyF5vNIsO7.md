# Scalable Universal T-Cell Receptor Embeddings from Adaptive Immune Repertoires

- Decision: Accept
- Scores: 5, 8, 8, 6

## Abstract
T cells are a key component of the adaptive immune system, targeting infections, cancers, and allergens with specificity encoded by their T cell receptors (TCRs), and retaining a memory of their targets. High-throughput TCR repertoire sequencing captures a cross-section of TCRs that encode the immune history of any subject, though the data are heterogeneous, high dimensional, sparse, and mostly unlabeled. 
Sets of TCRs responding to the same antigen, *i.e.*, a protein fragment, co-occur in subjects sharing immune genetics and exposure history. Here, we leverage TCR co-occurrence across a large set of TCR repertoires and employ the GloVe (Pennington et al., 2014)  algorithm to derive low-dimensional, dense vector representations (embeddings) of TCRs. We then aggregate these TCR embeddings to generate subject-level embeddings based on observed *subject-specific* TCR subsets. Further, we leverage random projection theory to improve GloVe's computational efficiency in terms of memory usage and training time. Extensive experimental results show that TCR embeddings targeting the same pathogen have high cosine similarity, and subject-level embeddings encode both immune genetics and pathogenic exposure history.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this study, the authors developed a method to derive low-dimensional representations of T cell receptors and subject-level repertoires in feature space. To enhance computational efficiency, the method employs random projection theory.

### Strengths
The paper is well-organized and clearly written.

The proposed method is technically sound.

The application of random projection theory to enhance computational efficiency, particularly regarding memory usage and training time, is noteworthy.

### Weaknesses
The biological definitions presented in the study are somewhat unclear. For instance, when the authors refer to TCR embedding, it is important to specify whether they mean both the TCR alpha and beta full chains, the CDR3 regions of both chains, or only the CDR3 region of the TCR beta chain. Additionally, do the authors take into account V(D)J gene information when using the CDR3 region?

Given that TCRs are highly cross-reactive, the authors need to provide further explanation on why using co-occurrence information alone is effective for TCR embedding.

The repertoires of different subjects contain varying numbers of TCRs. How do the authors address this variability when representing them with a matrix of the same TCR dimensionality?

Considering the high cross-reactivity of TCRs, how do the authors define the TCR-level ground truth without relying on wet-lab-based experiments?

When discussing classification tasks, it would be helpful to clarify whether the focus is on receptor-level classification or repertoire-level classification. Furthermore, given different receptors have clone frequencies within the repertoire, it appears that the authors do not consider clone frequency in their repertoire-level embedding.

The interpretation of deep learning models is crucial for clinical applications; however, the authors have provided limited results in this area.

Lastly, there is a noticeable lack of comprehensive comparisons with state-of-the-art works such as DeepTCR, TCRAI, DeepAIR, and DeepRC, which should be addressed.

### Questions
In the weaknesses section, it would be beneficial to provide further illustrations regarding the biological background, the methodology employed, and a detailed explanation of why the model is effective.

Moreover, in addition to reporting AUC and sensitivity, the authors should also include other relevant metrics such as specificity, positive predictive value (PPV), negative predictive value (NPV), and overall accuracy. It is important for the authors to clarify how the cut-off points for these metrics were determined, as this information is crucial for understanding the model's performance and its clinical applicability.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors present JL-GLOVE, a scalable algorithm for generating low-dimensional embeddings for T cell receptors (TCRs) and TCR repertoires using TCR co-occurrence data. The main idea is to leverage the co-occurrence patterns of TCRs that target the same antigen to learn meaningful representations. To address the computational challenges of large-scale TCR data, the authors introduce the JL-GLOVE method, which combines GloVe with random projection theory. This approach improves memory efficiency and speeds up the training process. They then aggregate these TCR embeddings to generate subject-level embeddings, providing a low-dimensional representation of an individual's immune history. The embeddings show that TCRs targeting the same antigen exhibit high cosine similarity, and aggregated repertoire embeddings correlate with immune profiles, supporting disease prediction and HLA inference tasks. Results demonstrate the utility of these embeddings for predictive modeling and potential applications in personalized medicine by integrating them with other data modalities.

### Strengths
- The use of the JL transform significantly improves the computational efficiency of the GloVe algorithm, enabling the analysis of large datasets containing millions of TCRs. The authors demonstrate that JL-GLOVE achieves good performance using only a fraction of the co-occurrence data, making it suitable for handling the increasing scale of TCR repertoire sequencing data.

- The embeddings produced not only capture the co-occurrence patterns among TCRs but also demonstrate clustering by antigen specificity and HLA association. This biologically meaningful structure aligns with immune response patterns and enhances the interpretability of the embeddings, which is valuable for immunological research and practical applications like personalized medicine.

- The paper rigorously validates the embeddings’ effectiveness through multiple downstream tasks, including disease classification and HLA inference. The experiments demonstrate the robustness of the embeddings to scale, supporting their utility in predicting immune response profiles across various pathogens, and showcasing meaningful performance improvements with larger datasets.

### Weaknesses
 - The authors compare JL-GLOVE to protein sequence-based embeddings (e.g., ESM-2 and TCRdist), which are structurally different from co-occurrence embeddings. While this comparison is useful, the paper could benefit from a broader comparison with other immunology-focused embedding techniques, such as contrastive learning methods or graph-based embeddings, which may capture additional biological context. Specifically, methods that explicitly model the relationships between TCRs and antigens, or those that incorporate known biological pathways, could provide a more relevant benchmark. For instance, comparing against methods that use attention mechanisms to learn contextualized TCR representations could highlight the specific advantages and disadvantages of the co-occurrence approach.

- The paper relies primarily on a mean pooling approach for aggregating TCR embeddings at the repertoire level, which, while straightforward, may be overly simplistic. This method is prone to noise, especially as the number of TCRs (K) increases, potentially limiting classification performance for diseases with more subtle immune signatures. The mean pooling approach treats all TCRs equally, ignoring the fact that some TCRs may be more informative than others for a given disease or immune state. More sophisticated aggregation techniques, such as weighted averaging based on TCR frequency or attention-based pooling that learns to focus on the most relevant TCRs, could potentially improve the quality of the repertoire embeddings.

### Questions
- The paper benchmarks JL-GLOVE against ESLG and AIRIVA for disease classification tasks. The authors can include a more comprehensive comparison with other deep learning models specifically designed for TCR repertoire analysis (DeepTCR, DeepID etc).

- The authors observe that the disease classification performance is sensitive to the embedding dimension (d) and the number of TCRs (K). A more systematic exploration of the impact of these parameters can be done A more detailed analysis of the impact of different embedding dimensions across various dataset sizes would be valuable.This would aid other researchers in configuring JL-GLOVE for datasets of different sizes or resolutions, thereby increasing the framework’s accessibility and practical utility.

- Presenting one or two practical case studies where JL-GLOVE embeddings provide actionable insights in a real-world immunological context (e.g., identifying rare disease signatures) would further emphasize the method’s applicability.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper develops JL-GLOVE, a method for creating vector representations/embeddings of T-cell receptors (TCRs) and immune repertoires that capture meaningful biological relationships. The method leverages TCR co-occurrence across patient repertoires, adapting the GloVe algorithm from natural language processing while incorporating the Johnson-Lindenstrauss transform for computational efficiency. TCRs are embedded such that those targeting the same pathogen have similar vector representations, and patient repertoires are represented by averaging their constituent TCR embeddings. The resulting embeddings successfully encode both immune genetics (HLA types) and pathogen exposure history, improving as more data is added, and outperform baseline methods on disease prediction tasks. The authors demonstrate their method's scalability and interpretability, showing it can process millions of TCRs while maintaining performance, though they note that the simple averaging approach for patient-level representations could be improved. By creating these biologically meaningful representations, the work provides a foundation for quantifying immune system similarity between individuals and could assist in personalized medicine applications.

### Strengths
- Originality: the development of TCR embeddings and immune repertoire representations is original and an under studied area in the representation learning community. The application of Glove algorithm here fits nicely and works. 
- Quality: the produced results are of high quality and provide a significant impact to the field
- Clarity: the paper is very clear to read and understand. The authors give the right amount of biological/immunological background to understand the paper and why it is important. 
- Significance: this is a very significant and meaningful contribution to the field of personalized medicine. The application of representation learning for TCRs and immune repertoires is a great step towards better medicine.

### Weaknesses
 - The novelties of the paper are not the representation learning method itself. The paper applies Glove algorithm with a few modifications that help it work better, but are not necessarily innovations in of themselves. 
- As stated, the immune repertoire method of taking the average, is nice and works, it could be further developed by other methods.

### Questions
- I believe this paper should be in the topic area of applications to physical sciences (biology / immunology) rather than unsupervised, self-supervised, semi-supervised, and supervised representation learning. There are few novelties in terms of methods development, but the application of these methods are extremely impactful and a nice way to show the power of representation learning. 
- You mention other methods for set level representations, why not use those? Average is nice in it's simplicity, but does this simplicity cost performance? Would be nice to see a benchmark against set representation methods. You may also be interested in OTKE method for set level representation.

### Soundness
4

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
4

### Summary
This paper introduces a scalable approach to generating T-cell receptor (TCR) embeddings by leveraging the GloVe algorithm, adapted with the Johnson-Lindenstrauss (JL) transform for improved computational efficiency. The approach aims to create subject-level embeddings of TCR repertoires, which capture immune genetics and pathogenic exposure history. It employs a co-occurrence-based model to detect immune-related patterns and provides an aggregation of TCR embeddings at the subject level, which the authors claim could serve in predicting diseases and HLA types.

### Strengths
- The approach is somewhat novel in applying co-occurrence modeling, inspired by NLP, to TCR data. Leveraging random projection (JL transform) to enhance GloVe's performance also demonstrates creativity in handling large datasets.
- The paper is well-organized with clear methodological sections, providing figures and tables to explain the model architecture and performance comparisons.

### Weaknesses
 - While the method adapts the GloVe and JL transform for TCR analysis, there is limited advancement in the biological interpretability of embeddings over existing approaches.
- The paper lacks rigorous benchmarks against established methods beyond simple logistic regression. Disease and HLA classification tasks do not adequately demonstrate the model’s robustness, especially with limited sensitivity for certain conditions (e.g., HSV) at larger embedding scales. The choice of logistic regression as the sole benchmark is concerning, as it may not fully capture the potential of the embeddings. More sophisticated classifiers, such as support vector machines or gradient boosting methods, should be explored to provide a more comprehensive evaluation of the embedding quality. The limited sensitivity for conditions like HSV, even at larger embedding scales, suggests that the model may not be capturing the nuances of complex immune responses, particularly when dealing with closely related pathogens.
- While clustering by disease and antigen provides some interpretative insight, the embeddings’ clinical relevance is unclear. The clustering analysis, while visually appealing, lacks a clear connection to clinical utility. It is not evident how these clusters translate into actionable insights for disease diagnosis or treatment strategies. The absence of a clear clinical application limits the practical impact of the proposed method.
- Despite using the JL transform to improve scalability, the computational requirements for large-scale TCR data (e.g., 4 million TCRs) are still high, limiting the practical applicability of this approach in settings with constrained computational resources. The claim of improved scalability through the JL transform needs further clarification. The paper should provide a more detailed analysis of the computational resources required for different dataset sizes, including memory usage and training time. This would allow researchers to better assess the practical feasibility of the approach.
- The method relies heavily on co-occurrence patterns, which may not fully account for complex immunological interactions, such as those involving low-frequency, yet clinically relevant, TCRs. Moreover, the assumption that TCRs responding to the same antigen will necessarily co-occur in similar contexts lacks validation and may oversimplify TCR functional diversity. The reliance on co-occurrence patterns may lead to a bias towards frequently observed TCRs, potentially overlooking the importance of rare but functionally significant TCRs. The assumption that co-occurrence implies functional similarity needs more rigorous validation, as TCRs responding to the same antigen might not always be present in the same contexts.

### Questions
- How does the model handle rare but potentially significant TCRs? Given the emphasis on co-occurrence, it is unclear how rare TCRs are represented, as these could provide unique insights in immune responses but may not frequently co-occur with other TCRs.
- The current validation relies primarily on logistic regression without exploring other classifiers or model interpretability techniques, which would strengthen the paper’s claims on model generalizability and utility.
- How does the embedding perform across other immunological datasets?
- Additional clarity on computational scaling challenges would be helpful, especially given the potential high-dimensional space of TCR repertoires.
- What additional features could improve biological relevance?

### Soundness
3

### Presentation
3

### Contribution
3
