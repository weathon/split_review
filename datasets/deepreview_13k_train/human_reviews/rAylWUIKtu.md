# Benchmark Inflation: Revealing LLM Performance Gaps Using Retro-Holdouts

- Decision: Reject
- Scores: 3, 3, 6, 5

## Abstract
The training data for many Large Language Models (LLMs) is contaminated with test data. This means that public benchmarks used to assess LLMs are compromised, suggesting a performance gap between benchmark scores and actual capabilities. Ideally, a private holdout set could be used to accurately verify scores.
Unfortunately, such datasets do not exist for most benchmarks, and post-hoc construction of sufficiently similar datasets is non-trivial. To address these issues, we introduce a systematic methodology for (i) retrospectively constructing a holdout dataset for a target dataset, (ii) demonstrating the statistical indistinguishability of this \emph{retro-holdout} dataset, and (iii) comparing LLMs on the two datasets to quantify the performance gap due to the dataset's public availability. Applying these methods to TruthfulQA, we construct and release 
Retro-Misconceptions,
on which we evaluate twenty LLMs and find that some have inflated scores by as much as 16 percentage points. Our results demonstrate that public benchmark scores do not always accurately assess model properties, and underscore the importance of improved data practices in the field.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduce a criterion to create hold-out set for benchmark data to investigate data contamination issues. They introduce four rigorous tests to validate these retro-holdouts. Applying their method to TruthfulQA, they evaluated 20 LLMs and discovered significant performance gaps, with some models showing score inflation of up to 16 percentage points. This reveals that public benchmark scores often don't accurately reflect real model capabilities.

### Strengths
- There research topic is important for fair evaluation in large language models.
- We need dynamic eval for preventing data contamination.

### Weaknesses
 - The basic logistics require better clarification. While language models trained on next-token prediction are naturally sensitive to different formats (as evidenced by the *reversal curse*), the paper should better distinguish between this inherent next-token prediction capability and true robustness to format perturbations and contamination. Specifically, the paper needs to clarify whether the retro-holdout set is simply a rephrasing of the original dataset or if it involves entirely new questions. If it's the former, the analysis is less compelling due to the known sensitivity of LLMs to even minor phrasing changes. If it's the latter, the methodology for creating these new questions needs to be rigorously detailed, including how they maintain the same level of difficulty and assess the same underlying knowledge as the original questions.

- The four perspectives presented are not all equally justified. There is significant overlap between the first two perspectives, as both rely on model accuracy to assess dataset difficulty. Specifically, the 'Similarity of Difficulty' test and the 'Semantic Embedding Similarity' test both use model performance or model-derived embeddings to determine if the retro-holdout set is similar to the original dataset. This introduces a circularity, as the very models being evaluated are used to validate the evaluation set. Additionally, the human testing perspective, while valuable, is not scalable for wider benchmark applications since it's impractical to recruit human annotators for every hold-out set. Furthermore, the paper does not specify the expertise level of the human annotators, which could significantly impact the reliability of this test.

- The discussion of benchmarks is too narrow, focusing primarily on TruthfulQA. This limited scope may be a consequence of the unscalable human testing requirement in the study design. Furthermore, since TruthfulQA is rarely used in evaluating current frontier LLMs, it would be beneficial to include analyses of additional, more widely-used benchmarks. The paper should also address the potential for the retro-holdout methodology to be applied to other types of benchmarks beyond multiple-choice question answering, such as those involving text generation or reasoning tasks.

- From line 112 to line 113 and line 258, citation format should be changed from \citet to \citep

- Regarding Figure 2, the authors need to specify which example they used in their analysis. Without clear example details, the distribution alone is insufficient to validate their claim. The paper should include specific examples of questions from both the original and the retro-holdout sets to illustrate the differences and similarities, and to allow for a more thorough understanding of the analysis presented in Figure 2.

- The claim on lines 160-161 that benchmark data after a model's cutoff date cannot be contaminated is inaccurate. Benchmarks built from internet sources can still be indirectly contaminated. For example, TruthfulQA, although created after certain model cutoff dates, draws from Wikipedia content. Since proprietary models are often pretrained on Wikipedia, the benchmark could still be contaminated despite its creation date. The paper needs to acknowledge this potential for indirect contamination and discuss how it might affect the validity of the retro-holdout sets.

### Questions
- From line 112 to line 113 and line 258, citation format should be changed from \citet to \citep

- Regarding Figure 2, the authors need to specify which example they used in their analysis. Without clear example details, the distribution alone is insufficient to validate their claim.

- The claim on lines 160-161 that benchmark data after a model's cutoff date cannot be contaminated is inaccurate. Benchmarks built from internet sources can still be indirectly contaminated. For example, TruthfulQA, although created after certain model cutoff dates, draws from Wikipedia content. Since proprietary models are often pretrained on Wikipedia, the benchmark could still be contaminated despite its creation date.

### Soundness
2

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
The paper introduces a retro-holdout framework to assess benchmark reliability for LLMs by retroactively constructing datasets (e.g., Retro-Misconceptions for TruthfulQA) that can reveal evaluation inflation due to data contamination. The study evaluates several LLMs and highlights the importance of reliable data practices in ensuring that benchmark scores reflect real-world model capabilities rather than inflated metrics.

### Strengths
The paper addresses a critical issue in AI evaluation by introducing a new methodology for retro-holdout dataset construction, which could significantly impact LLM benchmark validity. This novel approach to data contamination is a creative response to the challenge of black-box model evaluation, providing a framework that could be applied across different benchmarks. The paper demonstrates thoroughness in validating retro-holdout indistinguishability through multiple statistical tests, contributing meaningfully to ongoing discussions around data integrity in LLMs research.

### Weaknesses
I think the paper faces challenges in terms of interpretability and practicality. The retro-holdout methodology, while innovative, remains a black-box model that relies on side metrics such as similarity and precision, which may not fully establish reliability. Specifically, the reliance on similarity metrics, without a clear explanation of how these metrics are chosen or weighted, makes it difficult to assess the robustness of the retro-holdout construction. It's unclear if the similarity measures capture the nuances of data contamination, or if they are simply identifying superficial similarities. Moreover, the method’s practical relevance is questionable, as it appears computationally intensive and possibly detached from current LLM data contamination mitigation strategies. The computational cost of generating retro-holdout datasets, especially for large benchmarks, is a significant barrier to adoption. Additionally, the lack of comparison with established methods, such as the widely used n-gram approach, leaves readers without a clear sense of this method's relative effectiveness. Without a direct comparison, it's hard to determine if the retro-holdout method provides any significant advantage over simpler, more established techniques.

### Questions
- Could the authors clarify how the retro-holdout's interpretability compares to traditional n-gram methods, and are there plans to benchmark against them?

- Given the computational demands, what practical applications do the authors envision for the retro-holdout framework?

- Would the authors consider publishing their experimental code to support transparency and facilitate reproducibility?

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
4

### Summary
This paper proposed a way to retrospectively create a holdout set for a target dataset to benchmark models more accurately. The authors introduce four statistical tests to ensure the holdout set and the target dataset are sufficiently indistinguishable. They also introduce some tools to help iteratively create the holdout set to pass the statistical tests. With this approach, the authors create a holdout set for the misconceptions category of the TruthfulQA dataset, using it to calculate models' performance gap between evaluating on the original TruthfulQA and on the holdout set. The result shows that most models suffer from benchmark inflation, indicated by a large performance gap, suggesting that the TruthfulQA dataset have been included in the training data to some extent, and highlighting the need of holdout sets.

### Strengths
1. The paper is well written.
2. This paper propose a way to create a holdout set of a target dataset, which is important as many public benchmarks have been included in training data.
3. The proposed holdout set for TruthfulQA could be beneficial for future research to accurately benchmark models.

### Weaknesses
1. The authors did not provide much details about the holdout set for TruthfulQA they created. For example, the size of the holdout set and the number of iterations to pass the four tests. It is unclear how many samples were generated initially, and what the selection process was for the final holdout set. The lack of detail makes it difficult to assess the robustness of the holdout set and the potential for bias in its construction. Specifically, without knowing the number of initial samples and the selection criteria, it's hard to determine if the final set is truly representative of the original dataset's distribution.
2. The authors introduced some tools to help create the holdout set. However, they did not provide empirical evidence to show how these tool work. The description of the tools is vague, and it's unclear how they aid in the iterative process of holdout set creation. For example, it's not clear what specific algorithms or techniques are used in these tools, and how they contribute to satisfying the four statistical tests. Without this information, it's hard to evaluate the effectiveness and necessity of these tools.
3. The authors only demonstrate their approach on a category of TruthfulQA. It is unclear whether the approach can be applied to other datasets. The specific characteristics of the misconceptions category might not be representative of other types of datasets, and the approach might not generalize well to datasets with different structures or distributions. For example, datasets with more complex relationships or different types of questions might require different statistical tests or iterative processes.

### Questions
1. How many iterations does it takes to make the holdout set for the misconceptions category of TruthfulQA pass the four tests?
2. How many samples do you create for the holdout set?
3. Could you provide some examples of data in the holdout set?
4. Different datasets may be created in vary different ways. How can the proposed approach generalize to other datasets?
5. How did you select the four tests? Did you try other criteria?
6. How does the tools help create the holdout set? Did you compare the difference between using and without using those tools?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper highlighted the importance of a holdout set for evaluating LLMs, which inspired the author to propose a method for creating such a set, along with a series of tests to ensure its indistinguishability. An adequately constructed holdout set can help detect whether a benchmark has been contaminated. The experiments demonstrated the effectiveness of their holdout set on TruthfulQA and revealed contamination in 20 popular LLMs.

### Strengths
1. The paper highlighted the importance of a holdout set and introduced an effective method for creating one, along with several testing approaches.
2. The paper presented contamination results for 20 popular LLMs.
3. The testing method for indistinguishability was highly rigorous and comprehensive.

### Weaknesses
1. The experimental dataset is quite limited, consisting only of the truthful QA dataset. It could be expanded to include more diverse and widely-used datasets, such as Open QA, rather than just multiple-choice QA. The current focus on a single multiple-choice dataset limits the generalizability of the findings. The method's effectiveness on other types of QA tasks, such as open-ended question answering or tasks requiring reasoning over multiple documents, remains unclear. This narrow scope also makes it difficult to assess whether the proposed holdout set creation method is robust across different data distributions and task complexities.
2. The method used to create the holdout set is crucial to this paper and should be thoroughly explained in the main section. In its current form, the process isn't clear from the text. I recommend including a diagram or algorithm to better illustrate this process. The current lack of clarity makes it difficult to assess the validity of the holdout set and to reproduce the results. The specific steps involved in generating the indistinguishable holdout set, including any data transformations or selection criteria, need to be explicitly stated in the main body of the paper.
3. The paper "benbench" [1] also evaluates contamination across a wide range of LLMs, and should be referenced in your related works.
4. The paper lacks the meta-evaluation to verify the effectiveness of this method and the compression with other contamination detection methods like MinK [2]. Without a meta-evaluation, it's difficult to determine the reliability of the proposed method in comparison to existing techniques. The paper should include a comparison of the proposed method's performance against other contamination detection methods, such as MinK, using appropriate metrics. This comparison should also consider the computational cost and the sensitivity of the method to different parameters.

### Questions
See weaknesses

### Soundness
3

### Presentation
2

### Contribution
3
