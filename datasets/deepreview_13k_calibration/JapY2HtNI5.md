# RNAformer: Axial-Attention For Homology-Aware RNA Secondary Structure Prediction

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 5, 6, 5

## Abstract
Predicting RNA secondary structure is essential for understanding RNA function and developing RNA-based therapeutics. Despite recent advances in deep learning for structural biology, its application to RNA secondary structure prediction remains contentious. A primary concern is the control of homology between training and test data. Moreover, deep learning approaches often incorporate complex multi-model systems, ensemble strategies, or require external data. Here, we present the RNAformer, a scalable axial-attention-based deep learning model designed to predict secondary structure directly from a single RNA sequence without additional requirements. We demonstrate the benefits of this lean architecture by learning an accurate biophysical RNA folding model using synthetic data. Trained on experimental data, our model overcomes previously reported caveats in deep learning approaches with a novel homology-aware data pipeline. The RNAformer achieves state-of-the-art performance on RNA secondary structure prediction, outperforming both traditional non-learning-based methods and existing deep learning approaches, while carefully considering sequence and structure similarities.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces RNAformer, a deep learning model designed for predicting RNA secondary structures from a single sequence without additional requirements like multiple sequence alignments or thermodynamic parameters. The model uses an axial-attention mechanism that is independent of input size, making it suitable for RNA sequences of varying lengths. RNAformer is trained on a homology-aware data pipeline that addresses sequence and structure similarities to ensure a clean split between training and test data.

### Strengths
RNAformer is a single deep learning model that relies solely on RNA sequence input and does not require additional information like multiple sequence alignments (MSAs), embeddings, or ensemble techniques. Also, the Axial-Attention makes the model to be efficient to the length of RNA sequence.

### Weaknesses
The novelty is limited, where the key technique Axial-Attention has already been proposed in 2019. The authors do not appear to have designed the algorithm specifically for RNA data. Rigorous data splitting is too common sense to be a significant contribution to be published at an AI conference. Compared to baselines, it seems to be have weak constraints on RNA secondary structure, such as ES and TP post processing.

### Questions
Q1: How can your algorithm ensure the RNA secondary structure constraints, such as symmetry, no sharp loop within three bases, and so on. Refer to [1].

Q2: Could you compare your algorithm to recent studies[1,2,3]?

Q3: Regarding the Axial-Attention, what you have done to make it spcified to your problem? What is the difference when applying it to image data and RNA data?

Q4: What is the distribution of sequence length? What are the average and maximum lengths?

[1] Tan, Cheng, et al. "Deciphering RNA Secondary Structure Prediction: A Probabilistic K-Rook Matching Perspective." Forty-first International Conference on Machine Learning.

[2] Chen, Xinshi, et al. "RNA secondary structure prediction by learning unrolled algorithms." arXiv preprint arXiv:2002.05810 (2020).

[3] Jung, Andrew J., et al. "RTfold: RNA secondary structure prediction using deep learning with domain inductive bias." The 2022 ICML Workshop on Computational Biology. Baltimore, Maryland, USA. 2022.

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
This paper makes a valuable contribution to RNA secondary structure prediction by introducing RNAformer, an innovative model that leverages axial attention alongside a rigorously curated dataset and evaluation pipeline. The authors carefully address homology concerns, a major problem in previous machine learning models, which significantly enhances the reliability of their findings. The experiments are thorough and demonstrate substantial improvements over existing methods, particularly in generalizing to unseen RNA families. Overall, the combination of a well-designed model and rigorous evaluation positions this work as a strong candidate for acceptance.

### Strengths
* **Rigorous Dataset Construction**: A major strength of this paper is its rigorous approach to dataset construction, addressing an important issue in computational biology that previous models have often overlooked—the need to prevent homologous (highly similar) sequences across training, validation, and test sets to ensure robust evaluations. After assembling the initial dataset, the authors implement a comprehensive three-step data filtering process: (1) they use CD-Hit to remove sequences with over 80% similarity, reducing redundancy; (2) a BLAST search is conducted with a high e-value threshold to further exclude overlaps between training/validation and test sequences; and (3) they build covariance models using tools like LocaRNA-P and Infernal to filter any remaining sequences with structural or sequence similarities, applying a stringent e-value cutoff. This multi-layered filtering pipeline effectively minimizes overlap and ensures that the train/validation and test sets have minimal similarity. Additionally, by defining distinct FT-Homolog and FT-Non-Homolog test sets, the paper provides a structured approach to evaluate the model’s performance across varying levels of similarity, showcasing RNAformer’s generalization capabilities. 

* **Well-Designed Experiments with Superior Performance over Baselines**: The experimental design of this paper is well-conceived, with RNAformer consistently outperforming baseline methods in a rigorous experimental setting. The authors conduct two complementary experiments to highlight the model's capabilities. First, they evaluate on synthetic data, comparing RNAformer to the current state-of-the-art RNA 3D structure prediction model, AlphaFold 3 (AF3), demonstrating RNAformer’s superior performance. Second, they evaluate on experimental data with strict homology control, providing a thorough assessment of generalization. Even though baseline methods often use less stringent data splits or rely on additional information, RNAformer achieves better results. Together, these two experiments effectively underscore RNAformer’s superiority. 

* **Model Simplicity**: Another commendable aspect of this paper is the simplicity of the RNAformer model. By avoiding reliance on multiple sequence alignments (MSAs) and additional complex features, RNAformer achieves high performance with a streamlined architecture. This simplicity reduces computational overhead and enhances the model’s generalizability, making RNAformer a practical and effective alternative to more complex methods in RNA secondary structure prediction.

### Weaknesses
 * **Lack of Explanation for Column and Row Axial Attention**: One limitation of the paper is the insufficient discussion or justification for using column and row axial attention in RNAformer. This attention mechanism is applied in each RNAformer block to process the 2D latent representation of the RNA sequence. In certain models, such as MSA Transformer (https://www.biorxiv.org/content/10.1101/2021.02.12.430858v3), row and column attention is intuitive due to the distinct structural roles of rows and columns in the input data. However, in RNAformer, there is no inherent difference between rows and columns, as the input is a single RNA sequence without a natural row-column structure. Additionally, the output contact map is a symmetric \( L \times L \) matrix, where rows and columns are effectively equivalent. The authors may want to clarify why this architecture was chosen and how it specifically benefits the model in this context. While the authors mention the need to handle variable lengths, it is unclear why axial attention is superior to standard attention mechanisms for this task, especially given that the input is a single sequence, not an MSA. The use of axial attention seems like an unnecessary architectural choice that requires further justification, particularly when compared to standard attention mechanisms that have been successfully applied to similar sequence-to-contact map prediction tasks.

* **Insufficient Discussion of Sparse Adjacency Loss**: While the paper introduces a specially designed sparse adjacency loss, the discussion surrounding its design and impact on model performance is limited. Sparse adjacency loss is an important component, especially given the sparsity of RNA contact maps. Understanding how this loss function influences the model's predictions could provide valuable insights. The authors could expand on why this specific loss was chosen, its advantages over standard loss functions, and its contribution to handling sparse data effectively. The paper should provide more detail on how the loss function is calculated, including the specific criteria used to select paired and unpaired bases, and how the ratio of paired to unpaired positions is determined. A more thorough explanation of the loss function's design choices and their impact on the model's learning process is needed.

* **Need for Additional Baselines on Synthetic Data**: When comparing results on synthetic data, the paper only uses one baseline method, AlphaFold 3 (AF3), a 3D structure prediction model. In this comparison, the authors first predict the tertiary structure with AF3 and then extract the secondary structure, which may not provide an entirely adequate baseline. Although AF3 is considered state-of-the-art for 3D structure prediction, this does not necessarily imply it is optimal for secondary structure prediction, as the paper only claims AF3’s superiority in 3D tasks. Including additional commonly used secondary structure prediction models as baselines would strengthen the evaluation and provide a more comprehensive comparison. The authors should include comparisons with models specifically designed for RNA secondary structure prediction, rather than relying solely on a 3D structure prediction model. This would provide a more direct and relevant comparison of the model's performance.

### Questions
I have no question.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
I will cut directly into strength/weakness/questions.

### Strengths
- The proposed data preparation pipeline, which emphasizes a homology-aware train/validation/test split, addresses a critical need in this research community. Given the limited availability of RNA structural data, large deep learning models trained on random splits are at heightened risk of overfitting. 
- I like this idea about validating deep learning models through alignment to biophysical techniques such as RNAfold. 
- These experimental results are useful. It is good to see in table 3 that careful data preparation has brought deep learning models to a more realistic and often comparable level of performance to thermodynamic models like RNAfold and Linearfold.

### Weaknesses
 - The machine learning component of this paper is a bit limited in terms of novelty. The axial attention (mainly comprising of row-wise and column-wise self attention) is indeed quite similar to those that have been used in alphafold2 and MSA transformer. A lot of techniques have also been adopted from other works, for example the pretraining-finetuning training process which was initially used by spotrna.
- Between certain non-coding RNA families, there can be substantial sequence/secondary structure similarity, so the the synthetic dataset generated in section 3.1 may be flawed in theory. I think this is something worth checking out.


### Questions
- The covariance models e-value cutoff at 0.1, how do you come to this value (empirically or theoretically) and is it effective?
- Data splitting subsection on page 6 is a bit confusing. So essentially, you created two types of dataset, one effectively removing homology information (TS-Hard and FT-Non-Homolog, for test and finetuning), ther other one only accounting for sequence similarity (TS-PDB and FT-homology) so that the comparison to prior baselines is fair. 
- Why is e2efold missing from Table 3? It could probably serve as a valuable cautionary example.
- In section 4.2.1, although the sectio is called "Impact of homology on prediction quality", I don't really see how the content of that section alone is relevant for this topic, since it was mainly about comparing to alphafold 3.
- The linear scaling behaviour shown in section 4.2 may benefit from some comparisons to some other deep learning baselines.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces RNAformer, a transformer-based model that utilizes axial attention for RNA secondary structure prediction, relying solely on a single RNA sequence as input without requiring multiple sequence alignment (MSA) data. It also introduces a data preprocessing pipeline for constructing homology-aware RNA datasets.

### Strengths
1. The proposed methods work reasonably well.
2. The paper provides experimental validation of the model’s performance and scalability.
3. The code is available.

### Weaknesses
1. I think the authors should clarify why they chose to input the single RNA sequence into the model while using axial attention. Typically, axial attention is designed to handle both row and column interactions—where row attention captures sequence-specific information and column attention enables the model to consider homologous relationships across multiple sequences, such as in multiple sequence alignments (MSAs).  In RNAformer, however, axial attention is applied solely to the single sequence, instead of the MSA input.  Understanding the motivation for this choice is essential, as it diverges from the usual application of axial attention in models that integrate homologous data.  The authors could explain how this approach benefits RNA secondary structure prediction and whether it offers advantages in terms of computational efficiency, interpretability, or applicability to cases where MSA data is unavailable.

2. The paper lacks unique contributions to RNA secondary structure prediction, particularly regarding its axial attention module. What is the specific difference between RNAformer’s axial attention module and those in Evoformer in [1] or [2]?

3. The methodology for preparing homology-aware RNA datasets needs further clarification. In lines 269–273, how were the "50 random PDB samples" and the "TS-Hard" set selected? How were the data split across the four test sets and three validation sets? What is meant by “we gather TS1, TS2, and TS3 into the test set, TS-PDB, containing 125 samples”? Does “Rfam TS” in Table 1 refer to a combination of TS1, TS2, and TS3? Also, do the "FT-Homolog" and "FT-Non-Homolog" sets overlap with the Rfam training, validation, and test sets? In line 291, what does “2) only for TS-PDB” mean?

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces RNAformer, a deep learning model that predicts RNA secondary structures from sequences using axial-attention mechanisms. It achieves state-of-the-art performance and overcomes previous limitations by employing a homology-aware data pipeline, making it superior to traditional and existing deep learning methods.

### Strengths
RNAformer stands out for its scalability, efficiency with varying sequence lengths, and a robust homology-aware approach to data curation. It simplifies the prediction process without additional data requirements and offers linear scaling capabilities, outperforming other models in accuracy and generalization.

### Weaknesses
1. In the introduction, why is it stated that AlphaFold 3 struggles to capture RNA topologies and secondary structure features? The article should provide a more detailed explanation. Since structural information is more conserved, why can't we solely use structure information for training and test data splitting?

2. What is meant by "row- and column-wise embedding" on page 4? According to the mathematical expression, $L^{(0)}$ is a 3D matrix; why is it described as being in a 2D latent space? The mathematical representation and textual explanation in this section are quite confusing, making it difficult for readers to understand. Specifically, the description of the embedding process lacks clarity. It's unclear how the one-hot encoded sequence is transformed into row and column embeddings, and how these are combined to form the 3D matrix $L^{(0)}$. The text should explicitly state the operations involved, including any weight matrices and their dimensions.

3. From lines 156, 174, 179, and line 188, it appears that the strategies used in this article are derived from existing literature. Therefore, this work seems to be incremental in the context of RNA structure prediction. Where does the unique innovation of this article lie? The use of axial attention and convolutional layers, while effective, is not novel in itself. The paper needs to clearly articulate what specific combination or adaptation of these techniques constitutes a unique contribution.

4. From a methodological standpoint, how does the author emphasize the issue of homology in data splitting? The description of the data splitting process is somewhat vague. While the use of CD-HIT-EST and BLAST-N is mentioned, the specific parameters and thresholds used for these tools are not clearly defined. Furthermore, the rationale behind using a combination of sequence and structure-based methods for homology detection needs to be more thoroughly explained. The paper should provide a detailed justification for each step in the data splitting pipeline, including the specific e-values and sequence similarity cutoffs used.

5. The code repository provided in the article is inaccessible. Could the authors please provide an updated link for the code and data, so that readers can review and reproduce the results?

6. The deduplication tools should be CD-HIT-EST and BLAST-N.

7. Add the evaluation results for the INF (Interaction Network Fidelity) metric. Reference for INF: Parisien et al. RNA (2009), 15:1875–1885.

8. Why was the RNAFold-generated structure chosen as the true label for the synthetic dataset? According to later test results, there are other energy minimization-based prediction methods (e.g., MXfold2) that perform better.

### Questions
See "Weaknesses".

### Soundness
3

### Presentation
3

### Contribution
2
