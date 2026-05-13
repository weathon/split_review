# Beyond Sequence: Impact of Geometric Context for RNA Property Prediction

- Decision: Accept
- Scores: 6, 5, 8

## Abstract
Accurate prediction of RNA properties, such as stability and interactions, is crucial for advancing our understanding of biological processes and developing RNA-based therapeutics. RNA structures can be represented as 1D sequences, 2D topological graphs, or 3D all-atom models, each offering different insights into its function. Existing works predominantly focus on 1D sequence-based models, which overlook the geometric context provided by 2D and 3D geometries. This study presents the first systematic evaluation of incorporating explicit 2D and 3D geometric information into RNA property prediction, considering not only performance but also real-world challenges such as limited data availability, partial labeling, sequencing noise, and computational efficiency. To this end, we introduce a newly curated set of RNA datasets with enhanced 2D and 3D structural annotations, providing a resource for model evaluation on RNA data. Our findings reveal that models with explicit geometry encoding generally outperform sequence-based models, with an average prediction RMSE reduction of around 12\%\ across all various RNA tasks and excelling in low-data and partial labeling regimes, underscoring the value of explicitly incorporating geometric context. On the other hand, geometry-unaware sequence-based models are more robust under sequencing noise but often require around $2-5\times$ training data to match the performance of geometry-aware models. Our study offers further insights into the trade-offs between different RNA representations in practical applications and addresses a significant gap in evaluating deep learning models for RNA tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduce a newly curated set of RNA datasets with enhanced 2D and 3D structural annotations, providing a resource for model evaluation on RNA data. The paper reveals that models with explicit geometry encoding generally outperform sequence-based models, and geometry-unaware sequence-based models are more robust under sequencing noise but often require around 2 − 5× training data to match the performance of geometry-aware models. The authors conducted thorough and detailed experiments to support their proposed arguments.

### Strengths
1. The authors investigated the enhancement of RNA property prediction through the utilization of both 2D and 3D data, and explored the performance degradation of corresponding models under various influencing factors, including noisy data and partial label.

2. The authors collected a substantial amount of RNA sequence data across a wide range of nucleotide count intervals, ensuring comprehensive coverage.

3. The authors conducted extensive experiments using various models on the dataset to support their proposed arguments.

Originality, quality, clarity, and significance:

The paper is original and provides a comprehensive exploration of the impact of different types of input data on RNA property prediction capabilities for the first time. The writing is clear, and the overall quality is marginally acceptable. This research makes a contribution to the exploration of RNA property prediction.

### Weaknesses
1. The authors utilized a limited number of 3D models for geometric structure modeling, most of which are relatively early models, and neither of the two models (EGNN and SchNet) is specifically designed for 3D RNA structure modeling. Therefore, I believe their performance does not fully reflect the potential improvements offered by geometric information across various datasets. The authors are supposed to validate models specifically designed for RNA 3D structure modeling, such as ARES [1] and PaxNet [2], as well as some classic models in the protein domain (like GVP [3], GearNet [4], and MEAN [5]).

2. The pooling strategy is difficult to classify as an innovative contribution from the authors, as it is relatively simple. Thus, the models employed in the paper are essentially existing models, and the authors have not proposed their own model. Since 3D data encompasses more information than 1D and 2D data, the authors should reflect on how to better utilize 3D information to enhance model performance.

3. As noted in the paper, "all-atom SchNET and EGNN rely on a limited local neighborhood of adjacent atoms, limiting their receptive fields and preventing them from capturing long-range dependencies", full-atom modeling indeed incurs a significant computational burden. The authors could consider adopting the approach from methods like MEAN [5], treating each nucleotide as a node in a graph, which would allow for the expansion of local neighborhood relationships. Alternatively, the strategy used in PaxNet [2] could be employed to model the long-range and short-range interactions.

4. The analysis in section 4.2 lacks insights. Some conclusions are quite obvious, such as the enhancement of performance due to increased training data, which is even more pronounced in transformer-like structures. Moreover, the inferior performance of 3D models compared to 2D models can be attributed to the significantly lower prediction accuracy of existing methods for 3D structures compared to 2D structures.

5. The analysis in section 4.3 presents similar issues. Since the authors introduced sequencing noise, this error accumulates greater noise in both 2D and 3D data as a result of using 2D and 3D predictive tools. Therefore, it is expected that the transformer1D, which directly models 1D sequence data, would exhibit stronger performance.

### Questions
1. Predicting the 3D structure of models directly from 1D sequence data can indeed introduce noise, affecting model performance. Have the authors considered finding a 3D RNA dataset, such as the RNAsolo [1]?

2. This paper primarily focuses on predicting RNA properties and utilizes the MCRMSE metric. I would like to know what specific properties are being referred to, and what are the units for the predicted values?

[1] Rnasolo: a repository of cleaned pdb-derived rna 3d structures, Bioinformatics 2022.

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
4

### Summary
The paper provides a curated set of RNA datasets with annotated 2D and 3D structures and investigates RNA property prediction using various deep learning models, focusing on 1D (nucleotide sequences), 2D (graph representations), and 3D (atomic structures) approaches. Key findings reveal that 2D models generally outperform 1D models, while 3D models excel in noise-free scenarios but are sensitive to noise. In contrast, 1D models show greater robustness in noisy and OOD conditions. The authors emphasize the trade-offs of each approach and advocate for future research to integrate the strengths of all models.

### Strengths
1. This study provides a thorough comparison of 1D, 2D, and 3D models, showcasing their respective strengths and weaknesses in handling RNA data.
2. This study provides a comprehensive analysis of various deep learning models, assessing their performance under different conditions, including limited data and labels, different types of sequencing errors, and out-of-distribution scenarios, which is crucial for real-world applications.
3. The commitment to transparency and reproducibility by making methodologies, datasets, and code publicly available promotes collaborative progress in the field.

### Weaknesses
1. The article lacks methodological innovation, missing deep improvements on existing technologies and novel algorithm designs.
2. The article merely compares various metrics, and the key points are not sufficiently emphasized.
3. Both the secondary and tertiary structures are predicted using software, particularly the tertiary structure, which is not very accurate. This can lead to significant uncertainties in further property predictions.

### Questions
1. In recent years, many RNA language models have been proposed, applicable to various downstream tasks. Compared to these models, what are the advantages and disadvantages of the methods mentioned in the article?
2. What are the criteria for selecting secondary structure prediction tools, and is there a detailed analysis and further experimentation?
3. Please explain the motivation behind the five task settings, as these experiments may make the article appear cumbersome and the key points unclear.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a systematic evaluation of incorporating explicit geometric information into RNA property prediction, considering not only performance but also real-world challenges such as limited data availability, partial labeling, sequencing noise, and computational efficiency. To this end, authors introduce a newly curated set of RNA datasets with enhanced 2D and 3D structural annotations, providing a resource for model evaluation on RNA data.

### Strengths
For the field of AI for Science, high-quality datasets are very important assistants. This article integrates four datasets, which contain a large number of data samples of various types.

### Weaknesses
> **W1. Lack of explanation for RNA's uniqueness.**

In section 3, it seems that a task of general sequence molecules is defined, and it is not specifically for RNA. Is there any fundamental difference in methodology between them and other sequenced molecules (such as proteins and DNA), except that the molecular composition may be slightly different?

> **W2. The method used is relatively old.**

There are many new works for 1D sequences and 2D topological graphs, which are not elaborated here. As for 3D geometric graph neural networks, many latest works are not included in the comparison. In fact, the EGNN used has been pointed out by some literature to have form capacity limitations [a], which makes the conclusions drawn in the article unreliable. More and stronger baselines should be added. You can refer to these surveys [b,c,d], and add baselines such as SaVeNet [e], LEFTNET [f], FAENet [g], TFN [h], NequIP [i], MACE [j], EquiformerV2 [k], EPT [l], MEAN [m], dyMEAN [n], etc.

### Questions
See Weakness.

### Soundness
3

### Presentation
3

### Contribution
3
