# M$^3$-Impute: Mask-guided Representation Learning for Missing Value Imputation

- Decision: Reject
- Scores: 6, 5, 3

## Abstract
Missing values are a common problem that poses significant challenges to data analysis and machine learning. This problem necessitates the development of an effective imputation method to fill in the missing values accurately, thereby enhancing the overall quality and utility of the datasets. Existing imputation methods, however, fall short of explicitly considering the `missingness' information in the data during the embedding initialization stage and modeling the entangled feature and sample correlations during the learning process, thus leading to inferior performance. We propose \n{}, which aims to explicitly leverage the missingness information and such correlations with novel masking schemes. \n{} first models the data as a bipartite graph and uses a graph neural network to learn node embeddings, where the refined embedding initialization process directly incorporates the missingness information. They are then optimized through \n{}'s novel feature correlation unit (\FRU) and sample correlation unit (\SRU) that effectively captures feature and sample correlations for imputation. Experiment results on 25 benchmark datasets under three different missingness settings show the effectiveness of \n{} by achieving 20 best and 4 second-best MAE scores on average.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel grpah neural network-based approach to address the problem of missing value imputation. The proposed method explicitly uses the missingness information with correlations between features and samples. With 25 benchmark datasets, authors demonstrated its superiority compared to recent missing value imputation methods.

### Strengths
- Clear statement and approach: This paper clearly states the limitations of existing methods and thereby why the proposed method is necessary.

- Novel approach: Combination of feature correlation, sample correlation, and missingness information is fair separately and concurrently.

- Comprehensive experiments: This paper conducted comprehensive experiments with 25 benchmark datasets and 3 missingness patterns. This is the most broad experimental result among studies on missing value imputation.

- Detailed description: Authors provided detailed explanation for each module in the proposed method.

### Weaknesses
Complexity issue: The proposed method is much more complex than other methods, including its predecessor GRAPE. Although the authors already provided the computing time at test phase, but I am curious about how long the training phase takes.

Limitations in comparative analysis: While the authors conducted comprehensive experiments, but the improvements are mostly marginal, making it difficult to assess whether the improvements are significant or not. The authors should consider ways to present in a more compelling manner to highlight their significance.

### Questions
1. Is there any additional analysis regarding the computational complexity during the training phase?

2. Is there any analysis when the proposed method significantly outperforms and when does not. In practicality, it is helpful to know when the proposed method is powerful since it entails more complexity. If the improvement is marginal, GRAPE can be a good alternative.

3. How did you tune the proposed method? Information about baselines are attached in Appendix but I cannot see about the proposed method. Also, some ablation study only presents marginal changes, so it is difficult to get insights from them. Is there any different results about them?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces $M^3$-Impute, a novel method for missing value imputation that leverages mask-guided representation learning to address the challenge of accurately imputing missing data. M3-Impute incorporates missingness information and captures feature and sample correlations through innovative masking schemes, offering a significant advancement in the field. The method's key contributions include a refined embedding initialization process that integrates missingness information, the introduction of feature correlation unit (FCU) and sample correlation unit (SCU) to effectively model feature-wise and sample-wise correlations, and extensive experiments on 25 datasets demonstrating M3-Impute's superior performance over existing methods under various missing data patterns. By jointly modeling feature and sample correlations with missingness information, M3-Impute leads to improved accuracy in imputing missing values.

### Strengths
1.$M^3$-Impute demonstrates a high level of originality, with significant contributions including an innovative embedding initialization process that incorporates missingness information, which is uncommon in previous studies and offers a new perspective for the field of missing data imputation. 

2.The introduction of feature and sample correlation unit (FCU and SCU) is innovative as they explicitly model feature and sample correlations through a soft masking mechanism, marking a novel approach in existing missing data imputation methods. 

3.Extensive experiments on 25 datasets demonstrating $M^3$-Impute's superior performance over existing methods under different missing data patterns.

### Weaknesses
1. To strengthen the paper, it would benefit from comparing $M^3$-Impute against the most recent state-of-the-art methods in missing value imputation, highlighting its unique advantages over the latest techniques.

2. The paper should include a detailed examination of $M^3$-Impute's performance with large-scale datasets to assess its scalability and efficiency as data volumes expand. 

3. Adding a section on the model's interpretability would enhance the paper, as it is vital to understand the model's predictions for trust and application in critical fields like healthcare and finance.

4. The paper should delve into $M^3$-Impute's computational efficiency, including memory usage and optimization, to address resource limitations in practical applications.

### Questions
1.The experiments, although extensive, are primarily conducted on a set of datasets that may not fully represent the diversity of real-world data. It would be beneficial to include more datasets with varying characteristics, such as different domains and levels of missingness (eg: a certain type of severe deficiency), to more comprehensively evaluate the robustness and generalizability of $M^3$-Impute.

2.The paper notes that $M^3$-Impute struggles with datasets where data points have low dependencies, as FCU and SCU rely on data similarity. This can lead to sparse or inadequate graph formation and poor model performance. Can we employ strategies such as enhancing data representation and refining graph construction techniques to tackle these challenges?

3.Reference [1] also engages in graph construction and employs graph representation learning for missing value imputation. However, the approach to graph construction varies between the two methods. Has the author conducted a comparative analysis? Is there a correlation between the efficiency of missing value imputation and the method of graph construction? Which approach proves to be more effective?

[1] Jiaxuan You, Xiaobai Ma, Daisy Yi Ding, Mykel J. Kochenderfer, and Jure Leskovec. Handling missing data with graph representation learning. Advances in Neural Information Processing Systems 33: Annual Conference on Neural Information Processing Systems 2020, NeurIPS 2020.

### Soundness
3

### Presentation
3

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
Missing values challenge data analysis and machine learning, requiring effective imputation to enhance dataset quality. The authors claim that current methods often ignore missingness information and correlations among features and samples, reducing accuracy. M3-Impute addresses this by modeling data as a bipartite graph and using a graph neural network that incorporates missingness in initialization. Its feature and sample correlation units (FCU and SCU) capture essential correlations for improved imputation. Testing on 25 benchmark datasets under three missingness settings shows M3-Impute’s superior performance, achieving top MAE scores in most cases.

### Strengths
Originality: M3-Impute introduces a novel approach to missing value imputation by leveraging a mask-guided representation learning method. Unlike conventional methods, it incorporates both sample-feature relationships and missingness information in embedding initialization. The development of the feature correlation unit (FCU) and sample correlation unit (SCU) further distinguishes this method, providing unique mechanisms to explicitly model feature- and sample-wise correlations.

Quality: The proposed methodology demonstrates a well-structured integration of graph representation learning with innovative imputation techniques. M3-Impute’s use of bipartite graph modeling, along with the FCU and SCU units, reflects a robust design that balances theory and practical application, enhancing the overall quality and rigor of the imputation process.

Clarity: The paper clearly outlines each component of M3-Impute, detailing the step-by-step process of embedding initialization, feature- and sample-wise correlation modeling, and final imputation integration. This level of clarity provides readers with a clear understanding of the method’s architecture and functionality.

Significance: By directly addressing gaps in current imputation methods, M3-Impute holds significant potential to advance the field. Its effective incorporation of missingness information and explicit correlation modeling not only improves imputation accuracy but also sets a foundation for more sophisticated data analysis in complex datasets, impacting fields reliant on high-quality data imputation.

### Weaknesses
There are several major limitations.

First, the discussion of missing data mechanisms is incomplete. The literature on different missing data mechanisms—such as Missing Completely at Random (MCAR), Missing at Random (MAR), and Missing Not at Random (MNAR)—is extensive. Please refer to:

Ibrahim, J. G., Chen, M. H., Lipsitz, S. R., & Herring, A. H. (2005). Missing-data methods for generalized linear models: A comparative review. Journal of the American Statistical Association, 100(469), 332-346.
Kim, J.K. and Shao, J. (2021). Statistical methods for handling incomplete data. Chapman and Hall/CRC.
This paper, however, is limited to addressing only MCAR.

Second, the graph-based missing data method proposed by You et al. (2020) faces significant issues. In particular, it does not scale well to large datasets, as its efficiency depends heavily on both sample size and the number of variables.

Third, some concepts similar to the feature correlation unit (FCU) and sample correlation unit (SCU) have been previously explored in the following references:

Zhong, J., Gui, N., & Ye, W. (2023). "Data Imputation with Iterative Graph Reconstruction." Proceedings of the AAAI Conference on Artificial Intelligence, 37(9), 11399-11407.
 Jarrett, Daniel, et al. "HyperImpute: Generalized Iterative Imputation with Automatic Model Selection" ICML 2022.
 Gupta, Shubham, et al. "GRAFENNE: learning on graphs with heterogeneous and dynamic feature sets." International Conference on Machine Learning. PMLR, 2023.
 Qiao, Lishan, et al. "Estimating functional brain networks by incorporating a modularity prior." Neuroimage 141 (2016): 399-407.
 Um, Daeho, et al. "Confidence-Based Feature Imputation for Graphs with Partially Known Features." The Eleventh International Conference on Learning Representations.

### Questions
While Graph Neural Networks (GNNs) are valuable for capturing the intrinsic structure of feature and sample correlations, the M3 method, along with similar approaches, falls short in modeling the underlying missing data mechanisms. Additionally, most machine learning tasks increasingly emphasize causal inference to ensure robust and interpretable outcomes. However, your current method overlooks causal inference considerations, which could limit its application to settings where understanding causal relationships is critical.

### Soundness
2

### Presentation
3

### Contribution
2
