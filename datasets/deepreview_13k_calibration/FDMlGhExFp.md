# TabDPT: Scaling Tabular Foundation Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 5, 5, 8

## Abstract
\looseness=-1
The challenges faced by neural networks on tabular data are well-documented and have hampered the progress of tabular foundation models. Techniques leveraging in-context learning (ICL) have shown promise here, allowing for dynamic adaptation to unseen data. ICL can provide predictions for entirely new datasets without further training or hyperparameter tuning, therefore providing very fast inference when encountering a novel task. However, scaling ICL for tabular data remains an issue: approaches based on large language models cannot efficiently process numeric tables, and tabular-specific techniques have not been able to effectively harness the power of real data to improve performance and generalization. We are able to overcome these challenges by training tabular-specific ICL-based architectures on real data with self-supervised learning and retrieval, combining the best of both worlds. Our resulting model -- the \longname\ (\name) -- achieves state-of-the-art performance on the CC18 (classification) and CTR23 (regression) benchmarks with no task-specific fine-tuning, demonstrating the adapatability and speed of ICL once the model is pre-trained. \name\ also demonstrates strong scaling as both model size and amount of available data increase, pointing towards future improvements simply through the curation of larger tabular pre-training datasets and training larger models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper provides an in-context learning (ICL) scheme TabDPT for neural networks (NNs) on tabular prediction tasks by pre-training a shared Transformer backbone and making predictions with labeled-neighborhood context in a row-based encoding manner across open-domain classification or regression tabular datasets. Specifically, during pre-training approximate retrieval strategy is used to fetch neighbors as the contexts for given data points, self-supervised learning is performed by further dividing them into context and query splits and reconstructing the selected target column features, fitted with randomly shuffled order and masked values of other features. During inference, exact retrieval strategy is used for each query data point to form its labeled-neighbor context for direct prediction. Pre-trained on 123 open-domain datasets (32M rows and 2B cells) from OpenML, the evaluations on two public benchmarks (CC18 for classification and CTR23 for regression) show TabDPT can be comparable to recent supervised tabular NNs and traditional GBDTs, achieved without training on downstream datasets. The scaling behavior of TabDPT in both model parameters and pre-training data size is explored.

### Strengths
**Novel scheme & data scenario combination**: Existing in-context learning (ICL) schemes in tabular prediction community are mostly based on LLM backbones and focus on few-shot or zero-shot data scenarios, while TabDPT is a non-LLM tabular ICL scheme on fully labeled downstream datasets. Principally, TabDPT is pre-trained to learn to predict by comparing with labeled neighbors rather than LLM-based schemes that may rely on world knowledge in the LLMs.

**Robust performance comparison, analysis & ablation**: The authors offer result confidence intervals, win-rate matrix and Elo score analysis on evaluated benchmarks, which give a clear and robust performance comparison between TabDPT and other baselines. The ablation study shows the sources of main bonus in TabDPT scheme.

**Detailed limitation discussion**: The authors sufficiently discuss the limitations of TabDPT caused by its inherent design and the special nature of tabular data features.

### Weaknesses
 **Limited technical novelty & consideration in the field**: To my knowledge, the most technical components in TabDPT scheme is not novel in common tabular data learning community.
- In Sec. 3.1 the authors propose: (1) Row-based encoding strategy (Line 147,155) to reduce memory consumption for in-context training, and do not treat categorical or numerical variables differently (Line 144), while row-based encoding is a common practice in multiple-table prediction or graph-based tabular models (e.g., RDL [1]), and finely distinguishing numerical, categorical, binary and other tabular cells is beneficial [2]. (2) Shared Transformer backbone is a common design choice in cross-table learning that TabDPT is similar to the pre-trained tabular neural networks like TranTab [2] and XTab [3].

- In Sec. 3.2 the authors propose a self-supervised approach to pre-train TabDPT with (1) Random Column as Target prediction and (2) Column Shuffling and Masking inspired by the NLP masked language modeling, **while constructing the random column and masking input columns are old and very common in traditional pre-training objectives for tabular deep learning [4]**. Besides, **both technical components (including column shuffle) are widely used in LLM-based tabular model pre-training** (e.g., TapTap [5], GReaT [6], CM2 [7]).

- In Sec. 3.3 the authors propose retrieval-based strategy for pre-training TabDPT, sharing a similar training strategy as retrieval-based tabular models (e.g., RETRO or TabR [8] as mentioned in Line 211), though using ICL prediction manner, the core difference of TabDPT is solely substituting kNN search with more memory-efficient retrieval algorithm used in [9], which is not novel as well.

In summary, from technical novelty perspective, TabDPT seems to be a combination of existing works in tabular learning community, with the similar overall framework in other LLM-based tabular ICL papers, which weaken the original contributions of the paper.

**Insignificant performance promotion**: TabDPT performed heavy pre-training on 123 datasets (2B cells) and also requires fully labeled training data to form neighborhoods' contexts to conduct ICL-based prediction for a given data point, its main performances in Table 1 seem not significantly different from supervisedly tuned baselines like recent retrieval-based deep learning method (i.e., TabR) and classical tree-based models, the performances are so close that may be changed by selecting proper random seeds, raising a question of whether it is necessary to adopt ICL-based scheme under such fully labeled tabular data scenarios.

**Unreasonable computational budget comparison**: In Sec. 5.3 the authors discuss the training and inference time of TabDPT and other supervisedly tuned baselines (see Fig. 4a). There seem to be two perspectives to reflect the partially unreasonable analysis here: (1) In real-world practice, for a tuned supervised baseline, inference time is the most important efficiency metric since a model is only tuned once but used to predict in the long term, thus a direct comparison just using inference time of TabDPT and other baselines is more convincing and practical. (2) If the authors want to compare the development time of TabDPT and others, the pre-training time may need to be recorded and considered since this part is also the training budget of TabDPT, comparing only inference time of TabDPT with training (HPO) + inference time of others may hinder the real computational requirement comparison. **In summary, from any perspectives above, the computational budget analysis may be not reasonable enough**. Besides, the authors compared convergence speed of TabDPT and PFN++ using a fixed training epoch, while the trend may be affected by hyperparameter settings, and comparing under a fixed training time may be more rigorous.

**Limitations from pre-fixed maximum feature amount and class number**: As discussed in Sec. 3.4 and Sec. 6, TabDPT has pre-fixed maximum feature amount and class number to process, which inherently limit its efficiency and effectiveness in long tables (commonly seen in recommendation field) or large class number. For long tables, dimensionality reduction techniques should be applied to inevitably protect the input features. For large class number, multiple forward time is required which further add inference budget and may be hard to fit.

**Uneconomical inference strategy**: Compared to the traditional supervisedly tuned baselines (i.e., tree models, deep learning models), the retrieval-based nature of TabDPT may hurt its real practicality in industrial tabular data scenario where the labeled data scale is extremely large (in both sample and feature amounts) and online real-time application is required.

### Questions
Honestly, it is interesting to see ICL-based inference scheme can be comparable to traditional supervised scheme with prompt-tuning-like pre-training and sufficient neighbor contexts. I would like to improve my score according to the response of the following questions and comments from other reviewers.

(1) Since a 78M TabDPT pre-trained on 2B cells is used for the main results, and the author claimed there is no single gold standard benchmark in the paper, could you further evaluate on the following datasets: (a) the ones in the paper of FT-Transformer [1] (7 classification & 4 regression datasets), (b) several datasets from "Categorical classification" & "Categorical regression" in Appendix A.1 of [2]. I would be more familiar with these deep-model- or tree-model-favored datasets (including large feature and class amounts). The results of TabDPT are enough, and add the total or per-sample inference time if possible.

(2) Since different tabular datasets may vary in feature ranges, is there any consideration or experiment to reflect TabDPT is able to handle datasets in various feature ranges? (e.g., a table with feature value range from 1\~10 and another from 1,000\~100,000 in a single batch)

(3) Does TabDPT design considered the semantics of column names? What about its performances in OOD (out-of-domain) downstream datasets (i.e., the results on the datasets which domain is not pre-trained)?

(4) According to Fig. 4b, the performance of TabDPT is heavily rely on the neighbor retrieval during inference, forming a similar mechanism of kNN. Is it possible to substitute TabDPT with the kNN having a learnable neural kernel?

(5) Could you provide a comparison of inference time per 1000 samples for TabDPT and other baselines (i.e., only record inference time for others in Fig. 4a)?

(6) Since ICL-based outputs are affected by contexts, i.e., retrieved neighbors in TabDPT, is there any consideration to keep the stable prediction (especially regression tasks), or will the results be hugely changed with different random seeds?


**Reference**

[1] Revisiting Deep Learning Models for Tabular Data, NeurIPS 2021.

[2] Why do tree-based models still outperform deep learning on tabular data? NeurIPS 2022.

### Soundness
3

### Presentation
2

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
The article introduces TabDPT, a Tabular Discriminative Pre-trained Transformer, designed for tabular data through in-context learning combined with retrieval-based self-supervised pre-training. TabDPT aims to leverage real tabular data rather than synthetic data. The authors demonstrate TabDPT’s state-of-the-art performance on the OpenML-CC18 and OpenML-CTR23 benchmarks for classification and regression tasks.

### Strengths
1. This paper is well-organized and clearly written, making it easy for readers to understand the design and details of TabDPT.
2. TabDPT demonstrates scalability with both model size and data size, showcasing the ICL-based model as a foundation model for large-scale tabular pre-training.
3. TabDPT achieves better performance on benchmark datasets like OpenML-CC18 and OpenML-CTR23 while also offering significantly faster inference.
4. The authors openly discuss challenges and "bitter lessons" learned during model development, providing valuable insights and guidance for future researchers in this domain.

### Weaknesses
1. The authors present only the direct inference performance of TabDPT. In practical applications, fine-tuning is a reasonable way to enhance performance. It would have been beneficial to compare TabDPT with existing approaches that improve upon TabPFN, such as Tune Tables [1], TabForestPFN [2], MixturePFN  [3], and LocalPFN [4].
2. The novelty of TabDPT appears limited, as it mainly relies on pre-training with real data and adopts the column-as-target approach, a key technique from prior works like STUNT [5], P2T [6], and the KNN-based retrieval strategy used in LocalPFN [4].
3. TabDPT retains certain limitations of TabPFN, such as fixed maximum class and feature counts and a lack of dedicated processing for categorical and textual features. While these issues could be mitigated with conventional methods such as PCA, the authors should provide dedicated evaluations of TabDPT’s performance on datasets with class counts above 10, feature counts exceeding 100, and purely categorical features.

### Questions
1. See weaknesses
2. I’m curious whether the authors could provide a breakdown of TabDPT's performance across different dataset sizes by categorizing datasets into size bins. This would highlight how TabDPT compares with other models at varying dataset scales.
3. TabPFN (subsample) version can efficiently ensemble by sharing context, so a comparison between this method and TabDPT’s retrieval-based strategy in terms of efficiency and effectiveness would be informative.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims at presenting an approach which trains tabular-specific In Context Learning -based architectures on real data with self-supervised learning and retrieval. The model is: Tabular Discriminative Pre-trained Transformer (TabDPT). The work is on

### Strengths
Efficiency: The model provides fast inference on new tasks due to its ICL capabilities, eliminating the need for task-specific training.

Scalability: TabDPT demonstrates strong scaling with both model size and data quantity, suggesting potential for future improvements.

Generalization: The model generalizes well across tasks without additional fine-tuning, a significant advantage over traditional tree-based models.

Comprehensive Evaluation: The model is thoroughly evaluated against competitive baselines, showing strong performance across various metrics.

### Weaknesses
Feature and Class Limitations: The model has predefined limits on the number of features and classes, requiring additional techniques to handle larger datasets. Specifically, the reliance on PCA for feature reduction, while practical, may lead to information loss, particularly in datasets where the original feature space is highly informative and non-redundant. The method's approach of breaking down multi-class problems into a series of binary classifications, while addressing the class limitation, could introduce error propagation and may not be as efficient as methods designed to handle multi-class problems directly.

Textual Information: The current model cannot utilize textual information, which could limit its applicability in certain domains. This is a significant limitation as many real-world tabular datasets include textual descriptions or labels that can be highly informative. The inability to leverage this information means the model is potentially missing out on valuable contextual cues that could improve performance.

Pre-training Cost: While inference is fast, the pre-training process is time and resource-intensive. The high computational cost of pre-training makes the model less accessible to researchers and practitioners with limited resources. This could hinder the widespread adoption of the model, despite its potential benefits.

Evaluation: I would have expected a larger scale evaluation on tabular data. While the current evaluation is comprehensive, it would be beneficial to see the model's performance on a wider range of datasets, particularly those with varying characteristics such as high dimensionality, imbalanced classes, and different data distributions. This would provide a more robust understanding of the model's strengths and weaknesses.

### Questions
1/ How does the model handle datasets with significant missing data, and how does this impact performance?
2/ What are the specific challenges in extending the model to handle textual information, and how might these be addressed?
3/ How does the model's performance compare on datasets with varying levels of feature heterogeneity?
4/ What are the potential applications or domains where TabDPT's approach might be particularly beneficial or limited?
5/ How does the model's performance scale with even larger datasets beyond those tested in the paper?

### Soundness
2

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
This paper proposes TabDPT, a scaled-up version of TabPFN. To achieve this, the authors collect a large number of datasets and then train it by generating a large number of input-output pairs with random columns as outputs. TabDPT outperforms the traditional GBDT on the CC18 and CTR23 benchmarks.

### Strengths
1. TabDPT has state-of-the-art performance on both classification and regression tasks. While the previous TabPFN was not applicable to regression tasks, TabDPT proved that this kind of ICL transformer is also suitable for tabular regression tasks, which I think should be appreciated.

2. Using random columns as a useful target feature is a great way to enrich the training dataset.

3. TabDPT's inference time is very efficient because it requires no additional training time.

4. The authors evaluated TabDPT's performance on a variety of datasets to make their results more reliable.

5. It seems reasonable to me to use search for better performance than TabPFN.

### Weaknesses
1. While the performance of TabDPT is impressive, the novelty of TabDPT is quite curious. I still think it's a great contribution to the Tabular Learning community, but I think it would be better to emphasize the novelty along with the scale-up part.

2. Some citations are missing. Using random columns as a useful objective feature is similar to masked value prediction in the image or language domains (as the authors say), but it is also a widely used concept in the tabular domain. For example, STUNT [1] and P2T [2] also use this concept to achieve the desired performance on the considered tasks.

### Questions
1. I would like to know how TabDPT compares to XTFormer [1], even if the training sets are of different sizes.

2. From what I understand, ICL transformers like TabPFN perform better when the dataset size is small (i.e. a few-shot setup). Can you provide a rejection study related to the size of the dataset? Also, it would be great to see a comparison with modern few-shot learning methods like STUNT [2] or FeatLLM [3].

3. I'm also curious about the fine-tuning performance of the model. It is already known that fine-tuning TabPFN can give better results. I wonder if the same phenomenon is true for TabDPT.

----
[1] Chen et al., Cross-Table Pretraining towards a Universal Function Space for Heterogeneous Tabular Data, ArXiv 2024

[2] Nam et al., Few-shot Tabular Learning with Self-generated Tasks from Unlabeled Tables, ICLR 2023

[3] Han et al., Large Language Models Can Automatically Engineer Features for Few-Shot Tabular Learning, ICML 2024

----
Overall, I think this paper will make a high contribution to the ICLR community, and while I still give it an acceptance grade, I am prepared to raise it again if the authors address the concerns noted in the weaknesses and questions.

### Soundness
3

### Presentation
3

### Contribution
4
