# Mambular: A Sequential Model for Tabular Deep Learning

- Decision: Reject
- Scores: 3, 3, 8, 3

## Abstract
The analysis of tabular data has traditionally been dominated by gradient-boosted decision trees (GBDTs), known for their proficiency with mixed categorical and numerical features. However, recent deep learning innovations are challenging this dominance. We introduce Mambular, an adaptation of the Mamba architecture optimized for tabular data. We extensively benchmark Mambular against state-of-the-art models, including neural networks and tree-based methods, and demonstrate its competitive performance across diverse datasets.
Additionally, we explore various adaptations of Mambular to understand its effectiveness for tabular data. We investigate different pooling strategies, feature interaction mechanisms, and bi-directional processing. Our analysis shows that interpreting features as a sequence and passing them through Mamba layers results in surprisingly performant models.  The results highlight Mambular’s potential as a versatile and powerful architecture for tabular data analysis, expanding the scope of deep learning applications in this domain.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose Mambular, an adaption of the Mamba architecture for tabular data. The authors compare Mambular against various well-known model families in the tabular domain, in both regression and classification tasks, showcasing the competitive performance of the proposed method. The authors additionally perform a series of ablations to provide insights on several design choices.

### Strengths
- The work is well written.
- The work ablates several design choices of the proposed method.
- The proposed method achieves competitive performance compared to the considered baselines. 
- The work considers both regression and classification tasks.

### Weaknesses
 - The related work section misses core references and can be further strengthened. [1][2]
- Line 279, I would rather the authors advocated that the results are not significant, rather than considering a 10% significance level. The standard is a 5% significance level.
- The authors do not perform hyperparameter tuning.
- It is not clear how the set of defaults for all methods is devised.
- The number of datasets considered is limited. Additionally, the authors do not use well-established benchmarks from the community. [3][4]
- A detailed analysis regarding time is not provided to have a clear understanding of the pros and cons of different methods.

### Questions
- Line 47, missing related work [1].
- Line 252, missing related work [2].
- Line 264, how was the set of defaults devised? Do the authors use the defaults of the baselines from the corresponding papers? 
- Line 271, how were the datasets selected?
- In terms of baselines, why was CatBoost not included? Given that it handles categorical variables natively? It is additionally among the best performing methods from the gradient-boosted decision tree family.
- Could the authors apply significance tests over the entire suite of datasets and not on a per-dataset basis? The mean value could be used to aggregate the multiple runs on a single dataset. Additionally, could all of the methods be considered and a critical difference diagram be provided?
- Line 297, the results do not align with the referenced work, in particular in [3], (Table 1, Table 2, Figure 3) the FT-Transformer architecture lags behind the ResNet architecture in terms of performance. Additionally, as I previously mentioned, CatBoost is the top performing method, which the authors do not include in the comparisons.
- A comparison with TabPFN for datasets that fit the limitations of the method would be interesting.
- What is the runtime of the proposed method compared to the baselines? What about the inference time?

[1] Kadra, A., Lindauer, M., Hutter, F., & Grabocka, J. (2021). Well-tuned simple nets excel on tabular datasets. Advances in neural information processing systems, 34, 23928-23941.

[2] Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018). CatBoost: unbiased boosting with categorical features. Advances in neural information processing systems, 31.

[3] McElfresh, D., Khandagale, S., Valverde, J., Prasad C, V., Ramakrishnan, G., Goldblum, M., & White, C. (2024). When do neural nets outperform boosted trees on tabular data?. Advances in Neural Information Processing Systems, 36.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors introduced Mamba architecture to solve the problems of tabular data. They showed the effectiveness of the proposed method by comparing its performance with neural networks-based algorithms and tree-based methods. And they confirmed the superiority of a sequence and passing method by comparing various pooling methods.

### Strengths
The authors proposed the Mamba architecture to solve tabular problems. It showed good performance overall, especially in classification performance.

### Weaknesses
The proposed method seems to be nothing more than using the Mamba structure on tabular data. Although there are some structural suggestions, it is difficult to say that the idea is novel overall.
And when I check the experimental results, it seems difficult to say that the performance has been greatly improved. Additional discussions and experiments are needed to see what advantages can be taken advantage of by applying the Mamba structure to tabular data, what differential performance improvements can be made compared to existing methods, and what can be considered if a Mamba structure or a new structure based on Mamba is proposed in the future.

### Questions
Please check the above weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents Mambular, a sequential deep learning model based on the Mamba architecture, designed for tabular data tasks. The authors evaluate Mambular against state-of-the-art neural and (ensemble) tree-based models, showing that it performs as well as or better than these models across different datasets.

### Strengths
- A novel sequential approach to tabular data, treating features as ordered sequences to capture feature interactions. 

- Solid benchmarks against state-of-the-art models confirm its competitive performance across diverse datasets.

- Paper is clearly written and easy to follow,  the model and its components are clearly explained, and the comprehensive ablation study provides insight into the impact of different architectural choices.

### Weaknesses
 - The paper would benefit from a more extensive comparison with recent deep learning baselines for tabular data. While it presents strong benchmarks, adding models like TabPFN and GANDALF could enhance the evaluation, giving a clearer picture of Mambular’s performance against the latest advancements.
- Additionally, thorough hyperparameter tuning is necessary for many tabular learning models to ensure fair and optimal comparisons. Please refer to Questions.

- Hyperparameter Tuning and Model Performance: In Section 5, the authors claim that hyperparameter tuning does not significantly impact model ranking, citing Grinsztajn et al. (2022) and Gorishniy et al. (2021). I find this very questionable, especially given that Table 3 shows Random Forest outperforming XGBoost, which is typically strong for tabular data (Also, see Appendix tables here [1]).  
Additionally, the model’s sensitivity to kernel size in permutation experiments suggests that hyperparameter choices affect performance significantly. To address this, I suggest comparing models using an established benchmark such as TabZilla [2], which offers a diverse suite of datasets for evaluating tabular models. 

- The Mambular model’s sequential structure makes it highly sensitive to feature order, which impacts performance under certain hyperparameter settings. Although feature order dependency is a known issue in tabular data models, I recommend that the authors conduct an experiment with random feature permutations (see Definition 2 in [3]). This could enable Mambular to emphasize dependencies rather than sequence, potentially improving model's robustness.

### Questions
- Hyperparameter Tuning and Model Performance: In Section 5, the authors claim that hyperparameter tuning does not significantly impact model ranking, citing Grinsztajn et al. (2022) and Gorishniy et al. (2021). I find this very questionable, especially given that Table 3 shows Random Forest outperforming XGBoost, which is typically strong for tabular data (Also, see Appendix tables here [1]).  
Additionally, the model’s sensitivity to kernel size in permutation experiments suggests that hyperparameter choices affect performance significantly. To address this, I suggest comparing models using an established benchmark such as TabZilla [2], which offers a diverse suite of datasets for evaluating tabular models. 

- The Mambular model’s sequential structure makes it highly sensitive to feature order, which impacts performance under certain hyperparameter settings. Although feature order dependency is a known issue in tabular data models, I recommend that the authors conduct an experiment with random feature permutations (see Definition 2 in [3]). This could enable Mambular to emphasize dependencies rather than sequence, potentially improving model's robustness.



[1] https://arxiv.org/abs/2305.13072

[2] https://github.com/naszilla/tabzilla

[3] Borisov, V., Seßler, K., Leemann, T., Pawelczyk, M., & Kasneci, G. (2022). "Language models are realistic tabular data generators." arXiv preprint arXiv:2210.06280.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Mambular, an adaptation of the Mamba architecture specifically designed for tabular data problems. The authors claim that their model leverages a sequential interpretation of tabular data, similar to its successful application in other domains such as text, vision, and time series. The proposed architecture incorporates pooling strategies and feature interaction mechanisms to enhance performance. The paper provides experimental results on various datasets, comparing Mambular with state-of-the-art models such as FT-Transformer, TabTransformer, XGBoost, and LightGBM. According to the authors, Mambular achieves competitive results, highlighting the feasibility of applying sequential models to tabular data.

### Strengths
The paper explores the application of the Mamba architecture to tabular data, leveraging lessons from its success in handling other data types like text and time series. While not entirely novel, this extension demonstrates an attempt to generalize Mamba to a new domain.

The authors present experimental results comparing Mambular with a limited selection of state-of-the-art models, such as FT-Transformer, TabTransformer, XGBoost, and LightGBM. While the comparisons are not exhaustive, these initial results provide some insight into the model’s potential.

The architecture incorporates feature interaction mechanisms and various pooling strategies, potentially providing flexibility to handle different types of tabular data characteristics.

### Weaknesses
 - Lack of novelty: One of the main weaknesses is the lack of significant novelty. The concept of adapting Mamba for tabular data is not substantially different from previously proposed models like MambaTab [1]. The minor modifications presented in Mambular mainly involve hyperparameter tuning and slight architectural changes, which do not justify the need for a new model.

 - Misalignment with tabular data characteristics: The paper fails to convincingly justify why treating tabular data as sequential offers any distinct advantage. Unlike sequential data such as text or time series, tabular data lacks a natural ordering of features. The authors did not provide clear evidence or theoretical grounding for why a sequence-based model should work better in this context.

 - Limited scope of experiments: The experimental results are based on only 12 datasets, and the comparison to state-of-the-art algorithms is not comprehensive. Given the varied nature of tabular data, a broader set of datasets and comparisons to more established tabular models would have strengthened the claims.

 - Inconsistent Performance: Despite the claims of Mambular’s superiority, the reported results do not consistently show a significant performance improvement over existing methods, such as XGBoost or LightGBM.

### Questions
What is the rationale behind interpreting tabular data as sequences? Could the authors provide a theoretical explanation or empirical evidence showing that treating features as a sequence offers a distinct advantage?

How do the authors address the lack of consistency in performance improvements across the datasets? Were any specific types of datasets or characteristics where Mambular performed particularly well?

Could the authors explain why comparisons were not made with a wider range of established tabular models, such as TabR[2], T2G-Former[3], and SAINT[4]?
[2] TabR: Unlocking the Power of Retrieval-Augmented Tabular Deep Learning, 2023
[3] T2G-Former: Organizing Tabular Features into Relation Graphs Promotes Heterogeneous Feature Interaction, 2023
[4] SAINT: Improved Neural Networks for Tabular Data via Row Attention and Contrastive Pre-Training, 2021

### Soundness
1

### Presentation
2

### Contribution
1
