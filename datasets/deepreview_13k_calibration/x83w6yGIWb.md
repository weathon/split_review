# Beware of Calibration Data for Pruning Large Language Models

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 5, 8, 3

## Abstract
As large language models (LLMs) are widely applied across various fields, model compression has become increasingly crucial for reducing costs and improving inference efficiency.
Post-training pruning is a promising method that does not require resource-intensive iterative training and only needs a small amount of calibration data to assess the importance of parameters. 
Previous research has primarily focused on designing advanced pruning methods, while different calibration data's impact on pruning performance still lacks systematical exploration. 
We fill this blank and surprisingly observe that the effects of calibration data even value more than designing advanced pruning strategies, especially for high sparsity.
Our preliminary exploration also discloses that using calibration data similar to the training data can yield better performance.
As pre-training data is usually inaccessible for advanced LLMs, we further provide a self-generating calibration data synthesis strategy to construct feasible calibration data.
We conduct experiments on the recent strong open-source LLMs (e.g., DCLM, and LLaMA-3), and the results show that the proposed method outperforms commonly used calibration data and can effectively enhance strong pruning methods (e.g., Wanda, OWL).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the role of calibration data in post-training pruning for large language models (LLMs). The authors find that calibration data similar to the training data yields better performance when pruning LLMs for model compression. As many training datasets for LLMs are inaccessible, the authors propose a strategy to create synthetic calibration data, which outperforms commonly used datasets in experiments. This strategy involves generating synthetic text using the LLM and then filtering out low-quality data. This synthetic data is more similar to the training data and ultimately leads to better performance for pruned LLMs.

### Strengths
The paper effectively challenges the common assumption that post-training pruning methods are robust to the choice of calibration data. Recognizing the challenge of inaccessible training data, the paper introduces a "self-generating then sampling" strategy for constructing suitable calibration data. The paper provides a detailed examination of various aspects related to the self-generating calibration data strategy

### Weaknesses
While the paper shows a correlation between training data similarity and pruning performance, it doesn't explain why this connection exists. The paper's evaluation primarily centers on overall model performance. Investigating how calibration data affects the pruning of individual model components like attention heads or specific layers could be beneficial. This granular analysis would offer a more complete picture of how calibration data impacts different parts of the LLM. Furthermore, the paper lacks a discussion on the computational cost associated with generating synthetic calibration data, which could be a significant factor in practical applications. The study also does not explore the potential for bias amplification when using self-generated data, especially if the model has biases present in its training data.

### Questions
- What are the main differences between this work and the work by [1]?

- The authors say that "We can clearly observe that the self-generated synthetic data has higher Min-50%++ scores than the other calibration data. It indicates that the self-generated synthetic calibration data is indeed similar to the training data, confirming the validity of
using self-generated data as a proxy for the training data.". The conclusion is not entirely clear to me, can you explain how to conclude that synthetic calibration data is similar to the training data in this figure?

- While the paper aims to enhance general capabilities, the impact of using domain-specific calibration data for pruning models intended for specialized tasks remains unclear. do the authors have any intuition for that?

[1] Miles Williams and Nikolaos Aletras. On the impact of calibration data in post-training quantization
and pruning. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar (eds.), Proceedings of the
62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 10100–10118, Bangkok, Thailand, August 2024. Association for Computational Linguistics.
URL https://aclanthology.org/2024.acl-long.544.

### Soundness
3

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
3

### Summary
Large language models with numerous parameters substantially increase deployment and inference complexity and costs. To mitigate this, post-training parameter pruning can be used which exploits the fact that neural networks are often over-parametrized. It operates selectively removing redundant parameters while aiming to preserve performance as measured using a sample of calibration data.
The key contributions of this paper are: (i) a (plausibly) novel data synthesis strategy for calibration data, and (ii) an investigation into the effects of size, quality, and distribution of calibration data, across different pruning hyperparameters.
Additionally, the paper examines major hyperparameter choices within their strategy and perform additional analysis to show that their synthesis method generates data that is distributed similar to the training data.

### Strengths
The paper productively expands on prior work to answer unanswered follow up questions related to the influence of calibration data on pruning and delivers insightful findings through a set of reliable experiments.
It proposes a novel and intuitive approach for the synthesis of calibration data and evaluates it empirically and theoretically while experimentally justifying major hyperparameter choices. They show that the approach can improve by up to 2.6% over using an out-of-distribution calibration dataset.
The paper also clearly describes background, relevant pruning approaches, the problem statement and proposed approach for calibration data synthesis as well as experimental results.

### Weaknesses
The main results are not so well represented. In Table 2, the proposed calibration data synthesis approach frequently falls behind other sources of calibration data. It’s not highlighted in the table (e.g., using colors or otherwise) whether each source was present in the training set of the evaluated LLM. That is, it makes sense to have separate comparisons for the proposed approach with each of (i), data the model was not trained on and (ii), data the model was trained on, but these seem to be mixed up in one table making it hard to interpret the quality of the results by looking at the table. The statement “Overall, our self-generated synthetic calibration data outperforms other baseline calibration data in language modeling and commonsense reasoning tasks and…” is not well justified because the remaining of the paragraph focuses on Wikipedia and C4 and its not obvious from the table that it outperforms all sources consistently over all tasks. 

The paper involves some redundancies. For instance, the introduction as well as background seem to closely repeat the literature review. The questions are mentioned in the introduction then later again in section 3. Moreover, the choice of words in some of the sentences used is inadequate. For instance, the use of “value more” in “We fill this blank and surprisingly observe that the effects of calibration data even value more than designing advanced pruning strategies.” Take note as well that the paper does not convey that this “values more” than designing more advanced pruning strategies and that’s nontrivial to prove. Constructs such as “while different calibration data’s impact on pruning performance still lacks systematical exploration.” also make the abstract harder to read compared to if it was something like “while the impact of calibration data used has been…”.

### Questions
Suggestion (I): decompose or improve the table to highlight matching or exceeding the performance of using calibration data from the actual training set and exceeding the performance compared to calibration datasets belonging to other distributions. 

Suggestion (II): avoid redundancy in repeating the literature review and possibly summarize the questions in the introduction. In the literature review, the name of the technique corresponding to each citation could be mentioned as well.
Suggestion (III): improve the abstract to better reflect the outcomes of the paper and be easier to read.
Suggestion (IV): Mention somewhere that the paper will first proceed by answering the calibration data related questions and then propose a new a novel technique for its generations. Typically, one expects the main novel contribution to come first.

### Soundness
3

### Presentation
2

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
This paper studies the impact of calibration data in the post-training pruning of LLMs, which shows that calibration data significantly affects pruned model performance as pruning difficulty increases, surpassing the improvements from advanced pruning algorithms. The authors also find that using training data or data similar to it as calibration data significantly boosts pruned model performance. Since pre-training data is often unavailable for advanced LLMs, the paper proposes a strategy for self-generating calibration data. Extensive experiments on multiple LLMs and pruning methods confirm the effectiveness of the proposed synthetic calibration data.

### Strengths
1. This paper introduces a criterion and construction strategy for choosing calibration data in post-training pruning, supported by extensive experimental validation.
2. The authors conduct experiments on various LLMs and pruning methods, with multiple repetitions, to eliminate the effects of randomness.
3. The paper is well-organized, clearly presenting the empirical studies, methodology, experiments, and results, making it easy for readers to follow the authors' arguments.

### Weaknesses
1. This paper only conducts experiments on unstructured and semi-structured pruning settings and does not validate the effectiveness of synthetic calibration data in more practical structured pruning.
2. The synthetic calibration data is not a method first proposed by the authors. A recent work by Shin et al.[1] also proposed synthetic calibration data. However, the authors do not discuss the differences between that work and the others.
3. This paper only uses data from Wikipedia to generate synthetic data. Why do you not validate the effectiveness of synthetic data generated from other sources?

### Questions
1. Where does Figure 6 reflect the results of magnitude-based pruning?
2. Are the conclusions and method presented in this paper applicable to LLM quantization?

### Soundness
4

### Presentation
3

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
This paper investigates the impact of calibration data in the pruning of large language models (LLMs). This work mainly repeats some work that has been done by Williams & Altetras (EMNLP2024), which investigates the impact of calibration data in the pruning and quantization of large language models. The authors present evidence that the quality and type of calibration data can impact pruning performance, at times more so than advanced pruning methods themselves, reflecting the results done by Williams & Altetras (EMNLP2024). They propose a self-generating calibration data synthesis strategy to create effective calibration datasets when access to training data is limited.

### Strengths
1. **Originality:** In addition to the models included by Williams & Altetras (EMNLP2024), the authors also tested with DCLM-7B. This model is designed to showcase the effectiveness of systematic data curation. They propose a self-generating calibration data synthesis strategy. 
2. **Quality:** The paper provides a systematic exploration, supported by experimental results demonstrating how different calibration datasets affect the performance of pruned models.
3. **Clarity:** The writing is reasonably clear and easy to follow. The objective is straightforward. 
4. **Significance:** The findings have significant implications for practitioners in the field, although it has been highlighted by previous work already.

### Weaknesses
1. **Lack of Novel Contribution:** The study builds on important findings by Williams & Aletras (EMNLP2024), and the findings are already been proven and previous work has done further comparing quantization and pruning. The core idea of using calibration data to guide pruning, and the observation that the quality of this data impacts performance, is not new. The authors' proposed self-generating calibration data synthesis strategy, while a practical contribution, is not fundamentally novel, as similar approaches have been explored in the context of data augmentation and synthetic data generation for other tasks. The incremental nature of the contribution diminishes its overall impact.
2. **Lack of downstream tasks experiments:** the authors only consider pruning performance and it does not necessarily reflect the downstream tasks. Previous work done by Williams & Altetras (EMNLP2024) has done a much more comprehensive evaluation of a wide range of downstream tasks. The paper's evaluation is limited to a narrow set of tasks, and it is unclear if the observed trends in pruning performance will generalize to other downstream tasks, especially those that require different types of reasoning or knowledge.
3. **No explanation on pruning performance:** The paper primarily evaluates "pruning performance," but fails to provide a clear explanation of this metric. It's unclear whether this refers to pruning error, signal-to-noise ratio (SNR), or another measure. The authors neither explain their calculation method nor cite a source for this metric. This lack of clarity makes it difficult to interpret the results and compare them with other pruning methods.
4. **Experimentation with Diverse Datasets:** The experiments predominantly focus on a narrow range of calibration datasets and models. Including a broader set of datasets, especially those with different characteristics (e.g., domain-specific data, data with different levels of noise), could provide more generalizable results and strengthen the conclusions drawn about the effectiveness of their proposed methods. The current selection of datasets may not fully capture the complexities of real-world scenarios.
5. **Validation or discussion of choices in methods:** There are some variables actually can be potentially impact the results, such as why 5000 samples from the Wikipedia data for generation, and why eliminate the top 20%. The paper lacks a thorough discussion of the rationale behind the specific choices made in the experimental setup. For example, the number of samples used for calibration data generation (5000) and the threshold for filtering out high perplexity samples (top 20%) are not justified with empirical evidence or theoretical arguments. This lack of validation raises concerns about the robustness and generalizability of the findings.

### Questions
Could the authors provide further clarification on how efficient their proposed calibration data synthesis method is, e.g., what are the minimum data points it needs to generate for calibration?

### Soundness
2

### Presentation
3

### Contribution
1
