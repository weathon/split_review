# Deep Incomplete Multi-view Learning via Cyclic Permutation of VAEs

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 5, 6, 6

## Abstract
Multi-View Representation Learning (MVRL) aims to derive a unified representation from multi-view data by leveraging shared and complementary information across views. However, when views are irregularly missing, the incomplete data can lead to representations that lack sufficiency and consistency. To address this, we propose Multi-View Permutation of Variational Auto-Encoders (MVP), which excavates invariant relationships between views in incomplete data. MVP establishes inter-view correspondences in the latent space of Variational Auto-Encoders, enabling the inference of missing views and the aggregation of more sufficient information. To derive a valid Evidence Lower Bound (ELBO) for learning, we apply permutations to randomly reorder variables for cross-view generation and then partition them by views to maintain invariant meanings under permutations. Additionally, we enhance consistency by introducing an informational prior with cyclic permutations of posteriors, which turns the regularization term into a similarity measure across distributions. We demonstrate the effectiveness of our approach on seven diverse datasets with varying missing ratios, achieving superior performance in multi-view clustering and generation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a novel model, Multi-View Permutation of Variational Autoencoders (MVP), designed to address incomplete multi-view data by establishing robust inter-view relationships through cyclic permutations within the VAE latent space. MVP uniquely integrates cyclic permutations and latent variable partitions to encode both shared and view-specific information, enabling inference for missing views without sacrificing inter-view coherence. By incorporating an informational prior through cyclic permutations, MVP transforms the regularization term into a similarity measure, enhancing the consistency and sufficiency of representations across views. Experimental results on seven benchmark datasets demonstrate that MVP outperforms existing IMVRL methods in clustering and generation tasks, showcasing its ability to generate coherent and robust representations even with high missing-view rates.

### Strengths
The application of cyclic permutations in the VAE latent space presents a unique and innovative approach to modeling inter-view relationships. This method appears more robust than prior approaches, effectively capturing and maintaining consistency across incomplete multi-view data.

MVP is rigorously tested across multiple datasets under varying missing rates, demonstrating strong adaptability and consistently superior performance over previous methods in both partially and fully observed data settings. The results confirm MVP’s effectiveness in handling diverse levels of data incompleteness.

The paper includes thorough experiments and analyses, such as ablation studies and additional tests on relatedness, offering comprehensive insights into MVP’s performance. The authors strengthen their findings by running models multiple times with different random seeds and presenting deviations on the plots, adding credibility to the robustness and reliability of their results.

### Weaknesses
Although the paper centers on incomplete multi-view learning, much of the processing related to incomplete data, such as section C1, is relegated to the appendix. This structure may hinder readability and comprehension. A more detailed description of the incomplete data processing steps in the main text would improve accessibility and clarity for readers.

While the proposed method’s effectiveness in handling random arrangements of latent variables is supported by experiments, it also introduces additional computational complexity, particularly in the cumulative computation of the multi-view variational lower bound function. MVP’s complexity seems closer to that of MMVAE and notably higher than MVAE and MVTCAE. A detailed analysis of this computational cost would be beneficial, as it has important implications for scalability in multi-view applications. Specifically, the paper lacks a clear breakdown of the computational cost associated with the cyclic permutation operation, which involves generating and applying $(V-1)!$ permutations, where $V$ is the number of views. This operation, while innovative, could become a bottleneck for datasets with a large number of views, and the paper should provide a more thorough analysis of its impact on overall runtime and memory usage.

### Questions
Did the authors employ an analytical form or a sample-based estimation for the KL divergence terms in the ELBO computation?

How does the computational complexity of MVP scale with dataset size, and are there specific optimizations implemented to mitigate the computational overhead introduced by cyclic permutations?

### Soundness
4

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
4

### Summary
This paper introduces the MVP framework named of Multi-View Permutation of Variational Auto-Encoders, which focuses on a practical problem for incomplete multi-view learning. MVP can use MVAEs to establish view relationships in the latent space, thereby aggregating more comprehensive information while inferring missing views. Compared with the existing methods, the authors arrange and partition the variables and use a circular permutation approach to transform regularization into a measure of distribution similarity, thereby enhancing the consistency between different perspectives. The experimental results on several real-world datasets demonstrate the effectiveness of the proposed model.

### Strengths
1. This paper is well-motivated since missing is a common and significant problem in real-world multi-view learning. The modelling of the missing problem in this paper is very well designed and the method of applying permutations and segmentations in the latent space is very novel.
2. The paper provides a well-structured overview that is easy for the reader to understand. In addition, implementation details of the selected technology are presented in detail.
3. The paper provides comprehensive experimental results to validate the effectiveness of the proposed method. The model is tested on seven different datasets and compared with several SOTA methods to demonstrate its usefulness and robustness

### Weaknesses
1. The complexity of the proposed method is not adequately discussed. It would be helpful to compare the computation cost of the proposed method to the baselines, specifically detailing the time and space complexity of each stage (encoding, transformation, decoding) and how these scale with the number of views and latent dimensions. A more granular analysis, perhaps including FLOPs, would be beneficial.
2. This paper assumes that the first k dimensions of z capture information common to all views, so how is it set on different datasets? The justification for this assumption is not clear, and the paper should provide a more rigorous explanation of why the initial dimensions are suitable for capturing shared information. Furthermore, the method's sensitivity to the choice of k needs more investigation, including how performance varies with different values of k across diverse datasets, and whether there's a principled way to select k rather than relying on heuristics.
3. This paper only shows the results generated on the PolyMNIST and MVShapeNet datasets, where the views are all RGB type. How are the results generated on datasets with other types of views, such as the CUB Dataset, which includes both image and text modalities? The paper needs to demonstrate the generalizability of the method to non-image data and discuss any modifications or considerations required for handling different data types. The current results are limited to a specific type of data, which raises concerns about the method's applicability in more diverse scenarios.
4. For the experimental results, why are the experimental results you provided lower than the original papers? For example, DVIMC on the Scene 15 dataset with missing rates η=0.1 is lower than the published papers. In addition, how were the experimental results of Completer obtained? The original Completer is proposed for two view data which cannot be applied on the datasets you exploited in the paper directly. The paper needs to clarify the implementation details of the baselines, especially how they were adapted to the multi-view setting, and provide a more thorough explanation of any discrepancies in performance compared to the original publications. This is crucial for ensuring the reproducibility and validity of the experimental results.
5. The convergence analysis can be added in the experiment, which can be adopted to better the loss function. The paper lacks a detailed analysis of the convergence behavior of the proposed method. It would be beneficial to include convergence curves for the loss function and its components, as well as visualizations of the latent space evolution during training. This would provide insights into the stability and effectiveness of the optimization process.

### Questions
None

### Soundness
2

### Presentation
2

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
In this paper, the authors design a multi-view permutation of variational auto-ecoders for incomplete multi-view clustering, which termed MVP. The variational auto-encoder is used for extracting the invariant features.  Randomly reoder variables are used for cross-view generation.

### Strengths
1. Extensive experiments have demonstrated the effectiveness of the methodology designed in the paper.

2. The paper is well-organized.

3. The motivation is clearly described.

### Weaknesses
1. The use of VAE for invariant feature learning has been extensively studied [1,2,3, 4]. Please analyze the differences.

2. The paper does not provide the code, yet the results in Table 2 show significant performance of the proposed method. The authenticity and fairness of the experiments are questionable. Therefore, please release the code during the rebuttal process, as this will be a key criterion in my evaluation.

3. The construction details of the PolyMNIST and MVShapeNet datasets in line 406 are unclear. Is using new datasets to test previous methods fair?

4. How can the impact of randomness introduced by random padding, as mentioned in line 20, be mitigated?


5. The novelty needs to be further clarified. The use of Variational Autoencoders and ELBO has been widely studied in the IMVC field.

### Questions
Please see weakness.

### Soundness
3

### Presentation
3

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
This paper introduces the Multi-View Permutation of Variational Autoencoders (MVP) for incomplete multi-view representation learning. By leveraging cyclic permutations of posteriors, MVP enhances inter-view consistency and infers missing views effectively. Key elements include partitioning variables for view invariance, deriving an Evidence Lower Bound (ELBO) for optimization, and implementing an informational prior through cyclic permutation to align distributions across views. Experimental validation across multiple datasets and missing data scenarios shows MVP’s superiority over existing methods in clustering and generation tasks, particularly under high missing rates.

### Strengths
- MVP introduces a cyclic permutation approach to VAEs, leveraging view-invariant transformations in the latent space to address the challenges posed by incomplete multi-view data. This method successfully captures inter-view relationships by modeling correspondences and creating a more robust latent space, which significantly enhances the ability to infer missing views and aggregate information effectively.
- The paper provides rigorous theoretical analysis and proofs.
-  The extensive experiments, particularly in scenarios with high missing data ratios, provides compelling evidence of MVP’s ability to handle incomplete data effectively. The authors not only validate the approach across different missing ratios but also include quantitative metrics and visualizations to showcase MVP’s advantage over competing models.

### Weaknesses
##### Major

- "Even if we reorder the variables within each column of Z0, as demonstrated in the transition from Z0 to Z1in Figure 1, the underlying semantic information remains invariant"? The explanation of “underlying semantic information” remains unclear. A detailed clarification on what specific semantic information remains invariant during these transformations would strengthen the paper. For example, does this invariance hold for any arbitrary permutation, or is it constrained by the structure of the latent space? Furthermore, how is this semantic invariance quantitatively measured or verified, beyond qualitative observation?
- MVP’s performance could be sensitive to cyclic permutation settings and regularization parameters, as they directly influence view consistency and the similarity measure. A deeper sensitivity analysis of these parameters would provide insight into MVP’s stability and adaptability. Specifically, the paper should explore how different permutation strategies (e.g., random permutations vs. cyclic permutations with varying cycle lengths) impact the learned representations and downstream task performance. Additionally, the effect of different regularization strengths on the latent space structure and the resulting view consistency should be investigated.
- The cyclic permutation technique appears conceptually similar to disturbance and re-alignment strategies as proposed in *Partially View-Aligned Clustering* (NeurIPS ’20). A discussion of distinctions and similarities between MVP and this approach would benefit readers. It is crucial to clarify how MVP's approach differs in terms of the optimization process, the nature of the transformations applied, and the specific problem it addresses compared to *Partially View-Aligned Clustering*.
- Network architectures used for MVP are not fully detailed in the paper, limiting reproducibility and making it challenging for readers to understand the baseline structures supporting MVP’s performance. The paper should provide specific details on the number of layers, the types of activation functions, the dimensionality of the hidden layers, and the specific configurations used for both the encoders and decoders. This level of detail is essential for other researchers to replicate the results.

##### Minor

- Highlighting the Single-view Partition and Complete-view Partition in Figure 1 would improve clarity.
- The transition from Z_0 to Z_1 in Figure 1 is difficult to follow; linking this to Section A.2 might assist readers.
- It is not easy to distinguish the views with the samples in Fig.1b. It would be better to use different number of views and samples.
- The reference to “The second term” in Line 303 would be clearer if accompanied by Equation 1.

### Questions
See Major problems in Weaknesses

### Soundness
3

### Presentation
2

### Contribution
3
