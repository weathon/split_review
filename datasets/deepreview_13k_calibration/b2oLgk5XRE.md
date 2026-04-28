# Context-Driven Missing Data Imputation via Large Language Model

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5

## Abstract
Missing data poses significant challenges for machine learning and deep learning algorithms. In this paper, we aim to enhance post-imputation performance, measured by machine learning utility (MLu). We introduce a nearest-neighbor-based imputation method, DrIM, designed for heterogeneous tabular datasets. However, calculating similarity in the data space becomes challenging due to the varying presence of missing entries across different columns. To address this issue, we leverage the representation learning capabilities of language models. By transforming the tabular dataset into a text-format dataset and replacing the missing entries with mask (or unk) tokens, we extract representations that capture contextual information. This mapping to a continuous representation space enables the use of well-defined similarity measurements. Additionally, we incorporate a contrastive learning framework to refine the representations, ensuring that the representations of observations with similar information in the observed columns, regardless of the missingness patterns, are closely aligned. To validate our proposed model, we evaluate its performance in missing data imputation across 10 real-world tabular datasets, demonstrating its ability to produce a Complete dataset having high MLu.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses missing data challenges for tabular data to enhance post-imputation performance, i.e., machine learning utility. Specifically, it proposes a nearest-neighbor-based imputation method for heterogeneous tabular data. The method leverages LLMs to learn the representations of tabular data and incorporate a contrastive learning framework to refine the representations. The experimental results on 10 dataset demonstrate the effectiveness of the proposed method for imputation with high machine learning utility.

### Strengths
1. The paper is well-written and easy to follow.
2. The idea of using LLMs for missing value imputation is interesting. Learning representations with LLMs could benefit to capture contextual information for missing values and is helpful for resolving heterogeneous problem.
3. The results on 10 datasets show that the proposed methods achieve better perfomrnace than the SOTA baselines.

### Weaknesses
1. Though the idea of leveraging LLMs for imputation is interesting, some studies have proposed similar ideas to this work. It would be more appropriate to incorporate them and discuss both the differences and advantages of the proposed method in relation to them.

    a. CLAIM Your Data: Enhancing Imputation Accuracy with Contextual Large Language Models

    b. LLM-Forest for Health Tabular Data Imputation

2. The proposed method employed BERT as the language model for learning sample representations. However, BERT cannot be considered a large language model (LLM) given that it has a relatively small number of parameters when compared to typical LLMs.
3. For the sensitivity analysis, it can be observed that the two proposed methods experience a greater decline compared to the baselines in terms of the feature selection metric. More detailed analysis ought to be provided.
4. Again, Remasker exhibits greater stability than DrIM_base when it comes to the F_1 metric. Moreover, it appears to outperform DrIM_Fine in the aspect of model selection. However, the current analysis is rather limited in scope, making it insufficient to conduct a comprehensive and in-depth analysis. Table 1 presents the experimental findings at a missingness level of 0.3. Nevertheless, the results are not as satisfactory at other levels of missingness.
5. In the related work section, it is necessary to clarify the position of this paper within the literature. By doing so, the contributions can be highlighted more effectively.
6. It would be better to include other pretrained language models (or even LLMs) for comparison.

### Questions
1. It would be better to include more recent related studies and discuss the advantages of this paper.
2. Why do you choose the missingness level of 0.3 to report in Table 1? Are the results consistent as the missingness level varies?

### Soundness
2

### Presentation
3

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
This paper introduces DrIM, a nearest-neighbor-based imputation method for heterogeneous tabular datasets. It utilizes Large Language Models (LLMs) to transform tabular data into text format, enabling better similarity measurements. By replacing missing entries with mask tokens, it captures contextual information. DrIM shows promising results in imputing missing data across various real-world datasets, enhancing machine learning utility (MLu) effectively.

### Strengths
- **Research Topic.** The studied problem is interesting and practically important for tabular datasets.

- **Experiments.** Experiments are carried out on 10 datasets with 14 baseline methods, which is quite convincing.

### Weaknesses
 - **Lack of Novelty.** The LLM part of the paper is merely used for similarity computation. And the contrastive learning part of the paper is also very simple.

- **Confusing Title.** LLM is commonly associated with models such as ChatGPT among current readers, a term that in conjunction with BERT at least appears to deviate from readers' expectations.

- **Article Structure.** The relatively simple method introductions and experimental charts in this article resulting in a limited depth of experimental analysis with just three short paragraphs. I believe this is not reasonable and changes need to be made.

- **Experiments Analysis.** For feature selection task, the performance of the proposed methods drops quickly when missingness rate reaches 0.8, which needs more discussion and explanation. This is just an example, apart from it, more discussion is needed in the experimental section as well.

### Questions
- **Experiments.** The author only conducts experiments using BERT. Comparing the results obtained using BERT with those from models like ChatGPT would be valuable and further enhance the contribution of the paper.

### Soundness
2

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
4

### Summary
In this manuscript, the authors propose the use of language models to encode tabular data and further employ representations in the semantic space to identify similar data for the purpose of data imputation. Additionally, the authors introduce contrastive learning to enhance the expressiveness of the language models. Extensive experiments are conducted, demonstrating the robust performance of the proposed method.

### Strengths
1. This manuscript addresses an important issue: the presence of numerous missing values in tabular data, which is often heterogeneous, thereby complicating the challenge of data representation.
2. This manuscript conducts extensive experiments, and statistical analyses of the results indicate that the proposed method exhibits superior performance."
3. The manuscript is well-written, and the proposed idea is clearly explained, making it easy to follow.

### Weaknesses
1. The experimental results presented in the manuscript suggest that the proposed use of textual space to represent tabular data is promising. However, this is concerning because a substantial body of existing work [1,2,3] indicates that language models exhibit insufficient representational capacity for tabular data, particularly for numerical tabular data, especially in settings without fine-tuning. The manuscript employs an approach that contradicts the conclusions of existing studies, which raises my concerns.
2. Despite the extensive experimental results, the authors lack further analysis and discussion of these findings. In fact, the authors have ample text space available for a more in-depth analysis.
3. The authors suggest that the interpretability of the introduced contrastive learning deserves further investigation, which is puzzling. From my perspective, the incorporation of contrastive learning into the BERT model represents merely a straightforward data injection, with the performance improvements being quite evident. If the authors believe that further interpretive analysis is necessary, they should consider integrating techniques such as SFT (supervised fine-tuning) to explore the effectiveness of various data injection methods.
4. The construction of positive example pairs in contrastive learning can be problematic. In  essence, the authors assume missing at random (MAR). However, the MAR assumption might not be satisfied in many domains, i.e., the missing of values in tabular can be not random. For example, in medical domain, the missing value of some medical measurement is the result of medical experts’ judgement. The value is missing because the medical expert think it is unnecessary for some patient to do the test.
5. The authors need to pay attention to the formatting of different citations. For example, citations in lines 36 and 37 of the manuscript should be presented without parentheses.

### Questions
Please address the comments in weaknesses.

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
3

### Summary
This paper introduces a context-driven missing imputation method via large language models, termed DrIM. It represents missing values as mask tokens and then maps both continuous and categorical columns into a continuous representation space in a nearest-neighbor-based manner. To find suitable neighbors, this paper incorporates a contrastive framework to refine the representations on the heterogeneous tabular datasets. Experiments show the effectiveness.

### Strengths
Tabular data is one of the most used formats in current machine learning studies. It is interesting to construct contextual imputations for missing values with the modern language models. The experiments and attached code were well prepared.

### Weaknesses
 - The selection of language models: Are there particular factors to consider when selecting BERT-based models? Does it truly represent the current landscape of large language models?

- I recognize that including more mathematical content and pages can enhance reader comprehension. However, I found this paper somewhat lengthy, featuring several meaningless formulas that represent basic knowledge instead of things like theoretical proofs and bounds, such as cosine similarities in Section 3.2.

### Questions
I wonder whether it could be applied to multiple-table data or not, like relational databases. I noticed recent efforts that apply machine learning models to many tasks on relational datasets. If not, considering there existed many Missing Data Imputation methods, the use of such manner might be quite limited.

### Soundness
3

### Presentation
3

### Contribution
3
