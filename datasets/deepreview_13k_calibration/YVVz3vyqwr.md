# GENRAD: Genomics and Radiomics Heterogeneous Graph Neural Network for Graph-Level Classification in Alzheimer's Disease

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
Alzheimer’s Disease (AD) poses multifaceted challenges due to its neurodegenerative nature driven by complex genomic, radiomic, and structural interactions. Understanding these complex relationships is pivotal for advancing diagnostic and therapeutic approaches. Current models struggle to effectively integrate multimodal data for AD, limiting their predictive accuracy and biological interpretability. Thus, there is a pressing need for models that can seamlessly fuse genomic and radiomic data to provide a holistic understanding of AD pathology. We introduce GENRAD, a novel heterogeneous graph neural network (GNN) that integrates multimodal genomic and radiomic data for graph-level classification in AD by representing patients, genes, and brain structures as distinct nodes and implementing advanced message-passing techniques. The benefits of GENRAD are fourfold: (1) It enables multimodal fusion of genomic and radiomic data, uncovering biologically meaningful insights missed by single-modality models. (2) Its adaptive multi-scale graph representations model interactions at various biological scales, capturing complex relationships essential for understanding AD pathology. (3) GENRAD incorporates explainable AI techniques, providing detailed analysis of key genomic markers and brain regions associated with AD. (4) GENRAD performs unsupervised clustering of genes, allowing the identification of functionally related biological pathways, thus empowering clinicians with actionable insights for personalized treatment strategies. GENRAD demonstrates superior classification accuracy in identifying AD-related patterns compared to existing machine and deep learning models, achieving an accuracy of 91.70%.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces GENRAD, a heterogeneous graph neural network (GNN) designed for Alzheimer’s Disease (AD) classification through the integration of genomic and radiomic data. This model represents patients, genes, and brain structures as nodes, allowing complex interactions to be analyzed using advanced message-passing techniques.

### Strengths
1. The model’s use of multi-scale graph representations captures local and global biological interactions, providing a holistic understanding of AD pathology.
2. The unsupervised clustering of genes within the model facilitates the identification of functional biological pathways, which could aid in personalized treatment strategies.

### Weaknesses
1.  The paper lacks a thorough discussion of related interpretable GNNs specifically designed for AD. Many studies have developed explainable GNNs for AD, such as those in [1, 2, 3, 4]. A comparison of these models with GENRAD in terms of both design and interpretability effectiveness is necessary to justify the interpretability of the proposed model.

2. While the paper claims computational efficiency, it does not provide theoretical or experimental evidence to substantiate this claim. A computational analysis section, including runtime comparisons, would justify the argument.

3. The paper does not provide a clear problem definition, which makes it hard to follow.

4. The mathematical equations contain typos and undefined symbols. For example, there is a mathematical symbol error in Equation (3) $\mathcal{N} _{\phi}\left( i \right)$ and undefined dimensions for variables.

5. From the Table 1, the performance of proposed methods is limited compared with other baselines, such as FGCNN, especially no standard deviation are provided.

### Questions
1. How does GENRAD compare in interpretability and model design with other interpretable GNNs?

2. Could the author analyse the interpretable experimental results in medical domain perspective?

3. Could the author provide a detailed computational efficiency analysis, both theoretical and experimental, to support the efficiency claims?

### Soundness
3

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
5

### Summary
This paper introduces GENRAD, a heterogeneous graph neural network designed to integrate genomic and radiomic data for Alzheimer’s Disease (AD) classification. GENRAD is structured to handle multimodal data, representing patients, genes, and brain structures as distinct nodes and using advanced message-passing techniques. It claims four major contributions: enhancing multimodal data fusion, creating adaptive multi-scale graph representations, improving explainability, and enabling unsupervised clustering of genes to identify biologically relevant pathways. The model demonstrates superior accuracy compared to other methods in classifying AD.

### Strengths
1. The paper is well-structured and easy to understand.
2. The paper provides visualization results that highlight key genomic markers and brain regions associated with Alzheimer’s Disease (AD).

### Weaknesses
1. Limited Technical Contribution. To handle the multi-modality data integrating genomic and radiomic information, this paper employs a message-passing technique originally proposed in [1] on a heterogeneous graph that models patients, genes, and brain structures with both local and global interactions. This existing approach constitutes the paper’s major and only technical contribution, making the overall contribution marginal.

2. Incomplete Literature Review. This paper lacks a comprehensive overview of existing multimodal data fusion methods, making it unclear how GENRAD specifically advances this field. The following papers are highly relevant to this study.

[2] Gaiteri, C., Ding, Y., French, B., Tseng, G. C. and Sibille, E., 2014. Beyond modules and hubs: the potential of gene coexpression networks for investigating molecular mechanisms of complex brain disorders. Genes, brain and behavior, 13(1), pp.13-24.

[3] Gaiteri, C., Mostafavi, S., Honey, C. J., De Jager, P. L. and Bennett, D. A., 2016. Genetic variants in Alzheimer disease—molecular and brain network approaches. Nature Reviews Neurology, 12(7), pp.413-427.

[4] Bodalal, Z., Trebeschi, S., Nguyen-Kim, T. D. L., Schats, W. and Beets-Tan, R., 2019. Radiogenomics: bridging imaging and genomics. Abdominal radiology, 44(6), pp.1960-1984.

[5] Li, S. and Zhou, B., 2022. A review of radiomics and genomics applications in cancers: the way towards precision medicine. Radiation Oncology, 17(1), p.217.

[6] Wang, M., Roussos, P., McKenzie, A., Zhou, X., Kajiwara, Y., Brennand, K. J. and Zhang, B., 2016. Integrative network analysis of nineteen brain regions identifies molecular signatures and networks underlying selective regional vulnerability to Alzheimer’s disease. Genome medicine, 8, 1-21.

[7] Singh, G., Manjila, S., Sakla, N., True, A., Wardeh, A. H., Beig, N. and Spektor, V., 2021. Radiomics and radiogenomics in gliomas: a contemporary update. British journal of cancer, 125(5), pp.641-657.

3. Lack of Justification for Methodological Choices. The rationale behind certain technical decisions—such as using the SAGEConv layer for message-passing—lacks detailed justification specific to the properties of the multimodal data. Furthermore, the reasons for employing the GeneMANIA method to obtain co-expression scores and for defining edges between brain structures based on 3D Euclidean distance remain unclear.

4. Insufficient Evidence and Contextual Interpretation. On page 7, it is stated that GENRAD incorporates explainable AI techniques, such as GNNExplainer, alongside biological interpretability frameworks to make predictions that are not only accurate but also clinically meaningful. However, GNNExplainer is neither discussed in the methodology section nor tailored to the specific properties of multimodal data, which leaves the AI techniques used insufficiently explained. Additionally, while visualizations of gene interactions and brain regions affected by Alzheimer’s Disease (AD) are provided, they lack biological context and supporting evidence, raising questions about the relevance of the identified biomarkers and brain regions and their alignment with established neuroscience findings.

5. Limited Dataset. The model evaluation uses a single dataset (ANMerge), limiting the generalizability of the results. Moreover, the dataset details, including size and data distribution, are not fully described.

6. Comparative Analysis with Broader Baselines. To validate GENRAD’s performance further, comparisons with a more comprehensive set of baselines, particularly from recent transformer-based approaches, would strengthen the findings.

7. Marginal Performance Improvement. The classification results in Table 1 show that the proposed GENRAD achieves only a slight improvement over the follow-up methods and, in some cases, performs even worse.

8. Unclear Presentation. Numerous abbreviations are used without providing their full terms, and Figure 2 lacks a caption, affecting overall clarity.

### Questions
1. Could the authors elaborate on why SAGEConv was chosen over other potential GNN architectures? How does it specifically benefit the integration of genomic and radiomic data?

2. Given the single dataset used, how do the authors view GENRAD’s applicability to other AD datasets, and are there plans for further validation with more diverse data sources?

3. While explainable AI techniques are included, how do the authors envision clinicians using these insights in real-world applications? Providing case studies or examples could be beneficial.

### Soundness
1

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
This paper introduces GENRAD, a novel heterogeneous graph neural network that improves Alzheimer's Disease classification by integrating genomic and radiomics data through a graph structure representing patients, genes, and brain regions as nodes. The model achieves 91.70% classification accuracy while providing interpretable insights about disease pathology through explainable AI techniques and unsupervised gene clustering, advancing both diagnostic capabilities and potential treatment strategies.

### Strengths
Building heterogeneous graph from radiomic and genomic information is novel, based on the reviewer's knowledge.

The paper is clear and easy to follow.

Thorough ablation study has been provided.

Potentially new findings can be found from the interpretations.

### Weaknesses
The comparisons in Table 1 are not convincing. For example, to demonstrate that GENRAD could outperform Zheng et al (2018) and Maddalena et al (2022), the baseline models should be retrained on the ANMerge. It is not fair to just put their results on ADNI in the table.

It is not clear how authors defined the edge between patient node and structure/gene node. And why there is no direct interaction between structure and gene node? This is important for AD for several reasons, like the amyloid and tau can be accumulated in different regions with different extents. Besides, the structure-structure edges were built based on 3D Euclidean distance between different regions. Is this better than other ways like covariance matrix from cortical thickness, or the correlation between node of brain regions, etc?

Why SAGEConv was chosen? There are many, many other message passing layers out there that are feasible, which should be compared with.

Neither code nor data is provided, make it hard to evaluate the reproducibility. It could be beneficial for the cummunity if they can be shared, though it is not necessary at this stage.

Minor: Missing index and caption for figure 2.

### Questions
Please refer to the weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a heterogeneous GNN that integrates multimodal genomic and radiomic data for graph-level classification in Alzheimer’s Disease. The method represents patients, genes, and brain structures as distinct nodes and employs advanced message-passing techniques to improve classification performance.

### Strengths
1. The idea of incorporating neuroimaging data with demographic and genetic information is well-founded and addresses a relevant need in AD research.
2. The experimental results are impressive, showing strong performance on ANMerge dataset.

### Weaknesses
1. **Questionable Radiomic Feature Construction**: The choice of radiomic feature construction remains unclear and is a significant weakness. While the authors use a segmentation model, they fail to justify why they did not leverage established brain atlases, both anatomical [1] and functional [2], which are widely used in neuroscience and GNN research [3, 4] for constructing brain networks. These atlases provide a biologically grounded parcellation of the brain into regions of interest (ROIs), which are then used to define network nodes. The use of 3D Euclidean distance to construct structure-structure edges is particularly problematic. Physical proximity does not equate to functional connectivity or similar activity patterns. Functional brain networks are typically constructed using correlation metrics, such as Pearson correlation or partial correlation, derived from time-series data, which capture statistical dependencies between brain regions, not just spatial proximity. The authors should provide a more compelling rationale for their approach, especially given the availability of well-validated alternatives. 

2. **Limited Literature Discussion**: The paper still lacks a comprehensive discussion of prior work that integrates MRI and demographic data using GNNs. Several existing studies [5-8] have explored similar data modalities and network construction techniques. These works should be acknowledged and incorporated into both the discussion and experimental comparisons to properly contextualize the contribution of the proposed method. A thorough literature review is essential to demonstrate the novelty and significance of the proposed approach relative to the existing state-of-the-art.

3. **Missing Data Statistics**: Key data statistics, such as the number of patients, the distribution of classes, age and gender are still missing from the main text. This information is crucial for transparency and reproducibility and should be included in the paper, not just referenced as a public dataset. The lack of these details hinders the ability of other researchers to understand the experimental setup and replicate the results.

4. **Presentation Issues**: The presentation could be improved for better clarity:
   - (1) The figure on page 5 lacks a caption.
   - (2) In the first sentence of Section 3.2.3, "Figure 2b" should refer to "Figure 2a."
   - (3) The text and edges in Figure 3 are difficult to read and should be made clearer.
   - (4) I suggest revising Table 2 by separating binary classification results from multi-class classification results, as these settings are not directly comparable.

### Questions
Please refer to weaknesses

### Soundness
1

### Presentation
2

### Contribution
2
