# Simple yet Effective Incomplete Multi-view Clustering: Similarity-level Imputation and Intra-view Hybrid-group Prototype Construction

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Most of incomplete multi-view clustering (IMVC) methods typically choose to ignore the missing samples and only utilize observed unpaired samples to construct  bipartite similarity. Moreover, they employ a single quantity of prototypes to extract the information of $\textbf{all}$ views.   To eliminate these drawbacks, we present a simple yet effective IMVC approach, SIIHPC, in this work. It firstly transforms partial bipartition learning into original sample form by virtue of   reconstruction concept to split out of observed similarity, and then loosens traditional non-negative constraints via regularizing samples to more freely characterize the similarity.  Subsequently, it learns to recover the incomplete parts by utilizing the connection built between the similarity exclusive on respective view and the consensus graph shared for all views. On this foundation,  it further introduces a group of hybrid prototype quantities for each individual view to flexibly extract the data features   belonging to each view itself.  Accordingly, the resulting graphs are with various scales and  describe the overall similarity more comprehensively. It is worth mentioning that these all are optimized in one unified learning framework, 
which makes it possible for them to  reciprocally promote. Then, to effectively solve the formulated optimization problem, we design an ingenious auxiliary function that is with theoretically proven monotonic-increasing properties.  Finally, the clustering results are obtained by implementing spectral grouping action on the eigenvectors  of stacked multi-scale consensus similarity.  Numerous experimental results demonstrate that even under diverse missing proportions, the proposed SIIHPC  is still able to provide a preferable clustering performance compared to multiple prominent IMVC methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces SIIHPC, an incomplete multi-view clustering method that bypasses traditional missing view recovery by directly imputing similarities. SIIHPC replaces single prototype construction with hybrid-group prototypes, allowing each view to capture unique features within a unified framework. This framework is optimized through a well-designed iterative algorithm with convergence guarantees, ensuring robust and effective clustering.

### Strengths
The paper presents a novel approach SIIHPC to incomplete multi-view clustering through similarity-level imputation, which diverges from conventional methods that focus on reconstructing missing samples or features. This approach serves as an efficient alternative to traditional recovery-based techniques. By addressing incomplete multi-view clustering without explicit missing view imputation, SIIHPC reduces computational overhead and allows clustering methods to function effectively without relying on fully complete data structures.

A key innovation of the paper is the introduction of hybrid-group prototype construction, which replaces single prototypes with a more flexible model that enables each view to capture unique features. This enhances the model’s adaptability to heterogeneous data views, improving clustering performance across diverse datasets and scenarios.

Extensive experimental evaluations on multiple datasets with varying missing ratios highlight the robustness and effectiveness of SIIHPC. The inclusion of ablation studies further enriches the assessment, providing valuable insights into the contribution of each component to the model's overall performance and validating the framework’s design choices.

### Weaknesses
The terminology introduced in the paper is unclear; for instance, terms like T-PBL, SLI, IVHGP, and MSVSG are not properly explained in the captions of Figure 1, making it difficult for readers to follow the framework without additional context.

The overall process of the proposed clustering algorithm lacks clarity. Specifically, the final steps for obtaining clustering results and the initialization settings for relevant parameters should be clearly defined to improve the reader's understanding of the algorithm’s workflow.

While the paper provides strong experimental results, the interpretability of the clustering outputs and the practical implications of hybrid-group prototypes could be explored further. It would be helpful for the authors to discuss how the clustering results or prototype structures might be interpreted in real-world applications, providing insights into the method's broader utility.

### Questions
Can the authors clarify the terms used in Figure 1, such as T-PBL, SLI, IVHGP, and MSVSG, and ensure that these terms are defined either in the figure caption or in the text to improve readability?

Could the authors provide a more detailed explanation of the overall process of the clustering algorithm, particularly the final steps for obtaining clustering results and the initial parameter settings?

Given that the method relies on similarity-level imputation rather than missing view recovery, how sensitive is the model's performance to the quality of the imputed similarities? Could the authors discuss any potential limitations in scenarios with high levels of data incompleteness?

To better assess the stability and reliability of SIIHPC’s performance, could the authors provide standard deviation metrics for their experimental results? Including this information would help illustrate the consistency of the method across different runs and give a clearer view of its robustness under varying data conditions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this manuscript, the authors address the challenge of incompleteness due to missing samples by restoring the missing data at the similarity level. They propose a method that employs a hybrid approach to extract data representations, utilizing multiple quantities of prototypes for each individual view rather than relying on a single quantity across all views. This approach effectively resolves the misalignment of observed samples and incorporates potentially useful information from the missing samples into the bipartition similarity. Additionally, the authors balance contributions from different views while defining overall similarity based on the intrinsic characteristics of each view. These goals are effectively realized within a cohesive learning framework. The proposed method's effectiveness is convincingly demonstrated through experimental results on six public datasets with varying missing ratios.

### Strengths
1. The manuscript presents a logically structured approach, with Figure 1 providing a clear and intuitive overview of the framework.

2.  The authors utilize a variety of missing ratios and metrics in their experiments to evaluate clustering performance effectively.

3. The proposed SIIHPC demonstrates favorable memory and computational efficiency.

### Weaknesses
1. There is an issue with the manuscript's organization where the title of Section 5.5 is found to be identical to that of Section G in the Appendix.

2.  Experiments exhibit that some comparison methods do not function properly on VGGFACEHUND, YOUTUBEFACE and FASHMINST. However, there is a lack of theoretical explanations to substantiate these observations. Specifically, the manuscript does not delve into why methods based on matrix factorization, tensor decomposition, or graph learning encounter difficulties with these datasets, particularly when the datasets are not exceptionally large. A more thorough discussion of the computational bottlenecks or algorithmic limitations of these methods when applied to these specific datasets is needed.

3. The space complexity of Algorithm 2 is not described enough. The analysis should include a more detailed breakdown of the memory requirements for each variable, considering the dimensions of the matrices and tensors involved. It is crucial to understand how the memory scales with the number of samples, views, and prototypes.

4. The manuscript lacks definitions or explanations for certain notations used throughout the text. For instance, the notation $()_{+}$ in (11), N/A in Table 2 and Table 3  are not clarified. This lack of clarity hinders the reproducibility and understanding of the proposed method.

### Questions
1. Is the auxiliary function $g$ influenced by the percentage of missing samples?  Both $\mathbf{L} _{v}$ and $\mathbf{P} _{v,s}$ incorporate the missing percentage, which raises the question of how this affects the function.

2. According to the dataset descriptions in Table 1, FASHMINST has more samples than YOUTUBEFACE. However, the results in Table 3 indicate that SIIHPC incurs a higher memory overhead on YOUTUBEFACE compared to FASHMINST. What factors contribute to this discrepancy?

3. As indicated in Table 3, GSRIMC is limited to operating on only two small-sized datasets and exhibits higher consumption of running time and memory overhead. In comparison with SIIHPC, what is the theoretical complexity of GSRIMC?

4. Beyond the comparison with graph or tensor-based methods, how does SIIHPC fare when compared to deep learning approaches?

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
5

### Summary
This paper proposes a new incomplete multi-view clustering method, which reconstructs similarity relationships through the original sample form to capture the intrinsic information of all views. By relaxing traditional non-negative constraints, the method enables more flexible similarity characterizations. Additionally, a hybrid prototype set is introduced for each view, facilitating view-specific feature extraction and contributing to a comprehensive consensus graph. An innovative auxiliary function with monotonic properties is designed to solve the optimization problem effectively. Experimental results on various incomplete multi-view datasets demonstrate the robust clustering performance of SIIHPC.

### Strengths
Paper Strengths
1.The paper is well-organized and easy to follow. The intuition is clearly discussed in the Introduction.
2.The proposed method performs exhaustive experimental analyses, comparing a wide array of clustering algorithms, thereby strengthening the credibility of the results.

### Weaknesses
Paper Weaknesses
1.The process for constructing the consensus graph $G$ is not clearly explained, particularly in relation to $G_s$. The description lacks detail on how the individual view similarities are aggregated or reconciled to form the final consensus graph. It's unclear how the method ensures that $G$ effectively captures the shared information across all views, especially given the potential for noise or inconsistencies in individual view similarities.
2.Does the dataset include both images and text? Please specify the composition of each view within the dataset. The current description of the datasets is insufficient to understand the nature of the multi-view data. For example, if images are used, what are the specific image features extracted? If text is used, what preprocessing steps are applied? This lack of detail makes it difficult to assess the generalizability of the proposed method.
3.It would be helpful to discuss how Similarity Level Imputation and Hybrid-group Prototypes specifically contribute to improving clustering performance in Ablation section. The ablation study should provide a more granular analysis of the contribution of these components. It is not sufficient to simply state that they improve performance; the mechanism by which they do so needs to be clearly articulated. For example, does similarity level imputation primarily improve performance on datasets with high levels of missing data? How does the number of hybrid prototypes affect the final clustering result?

### Questions
1.The experimental setup lacks sufficient detail, particularly regarding the range and selection criteria of hyperparameters.
2.The Symbol Summary in the Appendix does not cover all symbols used throughout the paper, which may hinder clarity for readers. It is recommended to include all symbols and provide detailed explanations for each variable to improve readability and understanding of the methodology.

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
5

### Summary
This paper presents an incomplete multi-view clustering (IMVC) algorithm, SIIHPC. To utilize the latent valuable information of incomplete samples, it successfully separates out the observed parts via bipartition learning transformation and relaxes traditional non-negative constraints via sample regularization. It introduces the learnable consensus graphs to provide unified structure, and based on the relationship between consensus graphs and exclusive similarities it imputes the incomplete part at the similarity level. To get rid of the limitations of single prototype quantity, it assigns a group of hybrid prototype quantities for each view, and performs spectral grouping on the resulting multi-scale graphs to generate the cluster labels. Afterwards, it gives a four-step updating scheme to minimize the formulated objective. Overall, the overall organization of this manuscript is clear and easy to follow.

### Strengths
1. The motivation is good. Incorporating incomplete samples into the construction of bipartite similarity enhances the representation of relationships between different entities.   Diverse prototype quantities facilitate the accurate characterization of different views.

2. The designed auxiliary function is interesting. It equivalently solves one quadratic programming problem with orthogonal constraints and meanwhile is demonstrated to be with monotonic-increasing properties.

### Weaknesses
1. In the paper, the hyper-parameters $\lambda$ and $\beta$ are adjusted in $[10^{-7}, 10^{-6}, \cdots, 10^{-2} ]$  and $[10^{2}, 10^{3}, \cdots, 10^{7} ]$ respectively. The reasons for setting parameters are not given. 

2. Similar to the analysis about Table 3, some reasons for the sub-optimal results in Table 2 should be added. 

3. Descriptions about the theoretical space overhead should be more in-depth.

### Questions
1. As descripted, PSIMVC is also based on prototype, what are the differences between the proposed SIIHPC and PSIMVC? Specially, combined with Table 3, PSIMVC can consume less time and/or memory.  

2. Figure 4 show that at each iteration of Algorithm 2, the objective of function $g$ is increasing while at different iterations of Algorithm 2, it doesn't seem like this, such as at the $3$-th, $4$-th, $5$-th iteration respectively. 

3. After transformation, why is the complexity about $\mathbf{H}_{v,s}$ reduced from square to linear?

4. When adopting the prototypes constructed by elicitation sampling, what is the performance of SIIHPC?

### Soundness
4

### Presentation
4

### Contribution
3
