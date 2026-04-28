# LLMs Boost the Performance of Decision Trees on Tabular Data across Sample Sizes

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
Large language models (LLMs) perform remarkably well on tabular datasets in zero- and few-shot settings, since they can extract meaning from natural language column headers that describe features and labels. In contrast to LLMs, gradient-boosted decision trees (GBDTs) must learn the relationships among columns from scratch, increasing their data requirements. Meanwhile, LLMs are not competitive with GBDTs on medium or large datasets, and their scalability is capped by their limited context lengths. In this paper, we propose LLM-Boost, a simple and lightweight approach for fusing large language models with gradient-boosted decision trees, which enables larger datasets to benefit from the natural language capabilities of LLMs than was previously shown. While matching LLMs at sufficiently small dataset sizes and GBDTs at sufficiently large sizes, LLM-Boost outperforms both standalone models on a wide range of dataset sizes in between. We demonstrate state-of-the-art performance against numerous baselines and ensembling approaches, and we also show how to fuse GBDTs with TabPFN, a recent non-LLM model for in-context learning on tabular data. We find that this combination achieves the best performance on larger datasets. We release our code at https://anonymous.4open.science/r/LLM-Boost-21DD.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the LLM-Boost algorithm, which integrates large language models (LLMs) with gradient-boosted decision trees (GBDTs) to enhance classification performance on tabular datasets. The method involves extracting LLM logits for each row of data and using these predictions to augment the GBDT model, allowing it to learn the residuals to the true labels. The authors demonstrate that LLM-Boost outperforms traditional models and other ensemble techniques across various dataset sizes, showcasing its potential in automating predictive modeling pipelines.

### Strengths
- **Enhanced Performance:** LLM-Boost shows superior classification performance compared to traditional GBDTs and other ensemble methods.
- **Model Agnostic:** The boosting mechanism can be applied to various high-performing tabular architectures beyond LLMs.
- **Efficiency in Training:** Once LLM outputs are pre-computed, the training cost aligns with that of standard GBDT training.

### Weaknesses
 - **Dependence on Interpretability:** The method requires interpretable text descriptors as column headers, which may necessitate prompt engineering for some datasets. This reliance on meaningful column names could limit the applicability of the method to datasets with less structured or less descriptive headers. The performance could degrade significantly if the LLM struggles to extract meaningful information from the column headers, especially in cases where the headers are encoded or anonymized.
- **Pre-computation Costs:** For very large datasets, the initial cost of pre-computing LLM outputs may become significant. This pre-computation step could become a bottleneck, especially if the LLM inference is computationally expensive or requires significant time. The authors should provide a more detailed analysis of the computational cost of the pre-computation step, including the time and resources required for different dataset sizes and LLM models.


### Questions
1. What is the performance with large-sized datasets, instead of small and medium sized datasets?
2. line 201 "weather" -> "whether"
3. Missing inference:
- Iida, Hiroshi, Dung Thai, Varun Manjunatha, and Mohit Iyyer. "Tabbie: Pretrained representations of tabular data." arXiv preprint arXiv:2105.02584 (2021).
- Chen, Pei, Soumajyoti Sarkar, Leonard Lausen, Balasubramaniam Srinivasan, Sheng Zha, Ruihong Huang, and George Karypis. "HYTREL: Hypergraph-enhanced tabular data representation learning." Advances in Neural Information Processing Systems 36 (2024).

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
4

### Summary
This paper combines both LLM and decision trees to do the classification task on the tabular data. The major experiment is to explore how LLM, decision tree and the combined method work across different data sizes.

### Strengths
1. This paper combines LLM and decision trees for tabular classification tasks. It shows certain novelty in the proposed method.

### Weaknesses
1. The major baseline is quite strange. It would be better to separately show how LLM and decision tree work and treat both as the baselines, rather than mix them into one baseline 'Select'.
2. The experiment is not comprehensive. This paper simply lists the performance of different data sizes. It would be better to show some error analysis and cases to indicate when the proposed method can excel.
3. The selection of the LLM (eg, Flan-T5) is not very convincing.

### Questions
1. Can close-sourced LLMs such as GPT-family models perform well on such tasks?
2. What is the rationale for choosing Flan-T5 for the major experiments?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces LLM-Boost, a method that combines large language models (LLMs) and gradient-boosted decision trees (GBDTs) to improve performance on tabular data. The approach leverages LLMs' ability to interpret column headers and GBDTs' efficiency on large datasets. LLMs are used to extract predictions and residuals, which are then refined by GBDT models, leading to improvements, particularly on small to medium-sized datasets.

### Strengths
1. **Novelty.** Demonstrating that combining LLMs with GBDTs for tabular prediction tasks in such a simple manner can be effective is a valuable contribution.

2. **Discussion on limitations and future work.** A thorough discussion of limitations and future work is often overlooked, but it is something researchers reading the paper can greatly appreciate.

### Weaknesses
1. **Computational overhead.** It is unclear how practical it is to use LLM inference for tabular prediction tasks. An alternative use of LLMs in the tabular domain, which arguably is much simpler conceptually, is to use them for automatic feature engineering and training GBDTs on the augmented set of features for prediction [1, 2]. The current approach requires an LLM inference at prediction time, which introduces significant latency and cost, especially when compared to a GBDT model that can be deployed efficiently. The paper does not provide a clear analysis of the trade-offs between accuracy gains and the computational cost of LLM inference. Furthermore, the method's reliance on LLM inference for every prediction makes it less practical for real-time or high-throughput applications.

2. **Missing experiments.** Several crucial baselines, such as comparing LLM-Boost against simply increasing the number of trees in the GBDT, are missing. It is also unclear how the hyperparameters of the GBDT are tuned and if the same tuning procedure is applied to both the standalone GBDT and the LLM-Boost. Additionally, it would be useful to evaluate how the method scales to datasets with significantly larger feature sets, as the LLM context window could become a bottleneck. The paper lacks an analysis of the method's performance on datasets with varying feature set sizes, which is crucial for understanding its applicability in different scenarios.

### Questions
1. How does LLM-Boost perform when column headers are semantically ambiguous or incorrect? Would it still provide performance benefits over standalone GBDTs?

2. Why can’t we simply compare prediction accuracies to evaluate performance?

3. Typos: In Section 3.2, “replacing the first tree int he” → “replacing the first tree in the”.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose LLM-Boost, a fusion of LLM and decision tree algorithms. The main motivation here is the idea that GBDT is known to be the best performing predictive model in the tabular domain, but it cannot handle linguistic context, so it would be useful to be able to inject linguistic context into GBDT.

### Strengths
1. Great motivation. I also agree that injecting linguistic context is important to improve tabular predictive models, and to that end, many researchers are trying to incorporate LLM, which is an important research direction in the tabular learning community.

2. Simple method. If I understood the paper clearly, the main idea of LLM-Boost is to change the first step of GBDT determination to LLM's prediction, which seems really simple and intuitive to me.

3. The authors conducted extensive experiments on a variety of datasets.

### Weaknesses
1. Visualizations for the main results are too difficult to understand.

2. In some cases, the performance improvement is too small or even no improvement. While the authors claim that it is important to integrate LLM and GBDT as the dataset size increases, results such as Table 3 (Appendix) do not support this. When the training set size is at its maximum, the performance of LLM-Boost is almost identical to XGBoost.

3. The scope of the method is unclear. It is not clear if the method is designed for all tabular datasets or only for a specific range of dataset sizes. The authors' claim about the method's strength being in intermediate dataset sizes is vague and needs to be clearly defined.

4. The choice of LLM is questionable. The authors' observation that Llama-3-8B is generally worse to run LLM-Boost on raises concerns about the method's robustness across different LLMs. This suggests a potential limitation in the method's ability to leverage advancements in LLM technology.

### Questions
1. Did the authors try other LLMs, such as Llama 3?

2. Why did the authors use Flan-T5 for the main experiment?

3. Can the proposed LLM-Boost be used with commercial-level LLMs like GPT-4 (which is a black-box API)?

4. Have you tried a dataset with more samples? For example, a dataset with a million samples.

### Soundness
3

### Presentation
2

### Contribution
2
