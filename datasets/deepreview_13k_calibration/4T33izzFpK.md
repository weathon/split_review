# metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Large Language Models (LLMs) vary in their abilities on a range of tasks. Initiatives such as the $\texttt{Open LLM Leaderboard}$ aim to quantify these differences with several large benchmarks (sets of test items to which an LLM can respond either correctly or incorrectly).
   However, high correlations within and between benchmark scores suggest that (1) there exists a small set of common underlying abilities that these benchmarks measure, and (2) items tap into redundant information and the benchmarks may thus be considerably compressed.
   We use data from $n > 5000$ LLMs to identify the most informative items of six benchmarks, $\texttt{ARC}, \texttt{GSM8K}, \texttt{HellaSwag}, \texttt{MMLU}, \texttt{TruthfulQA}$ and $\texttt{WinoGrande}$ (with $d=28,632$ items in total). From them we distill a sparse benchmark, \texttt{metabench}, that has less than $3\%$ of the original size of all six benchmarks combined. This new sparse benchmark goes beyond point scores by yielding estimators of the underlying benchmark-specific abilities.
   We show that these estimators (1) can be used to reconstruct each original \textit{individual} benchmark score with, on average, $1.24\%$ root mean square error (RMSE), (2) reconstruct the original \textit{total} score with $0.58\%$ RMSE, and (3) have a single underlying common factor whose Spearman correlation with the total score is $r = 0.94$.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper considers the six LLM benchmarks included in the Open LLM Leaderboard (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, and WinoGrande) and seeks to create a much smaller benchmark that is predictive of the original suite by subselecting items. This is done using data from more than 5000 LLMs included in the leaderboard and a pyschometric method called item response theory (IRT) which in essence fits a model that estimates the item's difficulty and how well the item discrimates between models whose "abilities" are close to the item's difficulty. (Note this model ability is also fit by the method in an alternating fashion.) The presented method results in a benchmark that is only 3% the size of the original benchmark but is able to effectively reconstruct both the original individual benchmark scores and the joint score. Finally, using factor analysis, the authors demonstate that a single latent is predictive of all 6 benchmarks.

### Strengths
The paper is well-written and clearly communicates its ideas and methods. In the choice of the IRT, multiple models and methods for estimating the ability are explored. The method proposed produces a much smaller benchmark which the authors demonstrate has better predictive power than randomly subsampling items (Figure 1B). Careful consideration is given to potential limitations of the method, including assumptions about the conditional independence of the LLMs used for the study. The work also considers the interesting idea of a benchmark that performs adaptive testing in which items are selected sequentially based on a current estimate of the model's ability.

Overall I think the paper makes meaningful contributions to studying LLM benchmarks and making model evaluation more efficient, and I thus lean towards acceptance. However, I do think the benchmarks considered are missing some of the abilities that people seek to measure in LLMs (e.g. coding), somewhat limiting the work's impact. I seek to provide concrete suggestions regarding this in the next section.

### Weaknesses
My comments in this section are not intended to be required changes to the paper but rather a discussion of what I think the authors could add to have more significant impact.

Currently the main output of the paper is a much smaller benchmark that can be used to efficiently rank models on the six benchmarks as well as evidence from factor analysis that all six benchmarks are measuring a single latent ability. However, across the broader field of LLM benchmarks, it is generally assumed that there are multiple latent dimensions to the abilities of LLMs. For example, if a code benchmark was added into the set, I would assume this would require another latent dimension to fit model performance, and it would be intriguing if this was not true! Also I would be curious if a larger fraction of the test items is required to reconstruct the scores when the set of included benchmarks require multiple latent ability dimensions to represent.

In essence, the most interesting direction I see for this work is to apply the methods to a more comprehensive set of benchmarks to try to discover latent ability dimensions that might be interpretable as what we think of as LLM capabilities. This should then also provide a characterization of which of these abilities each benchmark measures.

### Questions
For quite a few models on the leaderboard, the MMLU score will be random chance (~25%, which you can see in Figure 1). Would it be a useful preprocessing step to subtract out random chance from the score and renormalize? E.g. take (score - 0.25) / (1 - 0.25).

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces metabench, a sparse benchmark distilled from six prominent benchmarks (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, and WinoGrande). Simple criteria, cross-validated subsampling, and information-based filtering are used to reduce the size of the benchmark. Original scores are reconstructed in a cross-validated manner.

### Strengths
1. This paper distills six prominent LLM benchmarks into a much smaller one with less than 3% of the size, which enables more streamlined and cost-effective evaluation methods;
2. The new sparse benchmark yields estimators able to reconstruct the original benchmark score.

### Weaknesses
As mentioned in the limitations section, a smaller benchmark has the risk of being memorized.

### Questions
Will a small benchmark lead to a large variance in evaluation?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Metabench, a sparse benchmarking method designed to evaluate large language models (LLMs) with minimal redundancy and resource demands. By analyzing data from over 5000 LLMs across six benchmarks (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, and WinoGrande), Metabench distills these into a much smaller subset, reducing the combined item count by over 97%. Using psychometric techniques such as Item Response Theory (IRT), Metabench selects the most informative items, facilitating efficient and accurate evaluation while maintaining the integrity of the original benchmarks. The sparse benchmark achieves impressive fidelity, reconstructing original scores with less than 1.24% RMSE on average, and identifying a single common latent factor strongly correlating with general model ability.

### Strengths
1. The paper’s technical approach is methodologically sound, with robust use of IRT and statistical modeling to identify informative items.
2. It is well-organized, with a clear explanation of Metabench’s goals and psychometric techniques.
3. It makes a substantial contribution to LLM evaluation, providing a novel, efficient, and scalable benchmarking solution.

### Weaknesses
1. The framework currently focuses on six benchmarks; additional work could explore its applicability across a broader range of LLM tasks or domains. Specifically, the current selection of benchmarks, while diverse, is heavily focused on question-answering and reasoning tasks. The method's effectiveness on tasks requiring more complex language generation, such as summarization or translation, remains unclear. Furthermore, the reliance on multiple-choice formats might limit its applicability to benchmarks that use free-form text generation or other non-classification based evaluation metrics.
2. Metabench’s dependence on psychometric models, especially IRT, could be limiting if these models do not fully capture the complexities of LLM behavior, as they were traditionally designed for human subjects. The assumption that LLM performance can be adequately modeled by a single latent trait, as is often the case in IRT, may be overly simplistic. LLMs might exhibit multiple, potentially uncorrelated, abilities that are not captured by a single latent factor. This could lead to an incomplete or even misleading assessment of their true capabilities. The use of IRT also assumes that item difficulty is stable across different LLMs, which might not hold if certain models are specifically trained or optimized for particular types of questions.

### Questions
1. Could authors elaborate on potential limitations when applying Metabench to other domains?
2. How might Metabench handle scenarios where specific benchmarks assess unique skills not captured by a general latent factor?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes metabench, a compressed version of six popular LLM benchmarks (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, and WinoGrande) that achieves comparable evaluation capability while using less than 3% of the original items. The authors leverage psychometric techniques, particularly Item Response Theory (IRT), to identify the most informative test items and estimate latent abilities that can reconstruct original benchmark scores with high accuracy.

### Strengths
1. Novel application of psychometric methods to LLM evaluation
2. Impressive compression ratio (<3% of original size) while maintaining accuracy. Low reconstruction error (1.24% RMSE for individual benchmarks, 0.58% for total score).
3. Comprehensive ablation studies and baseline comparisons. Thorough investigation of factor structure across benchmarks.

### Weaknesses
1. Memorization risks: 
    (1) Smaller benchmark size increases memorization vulnerability
    (2) Proposed mitigation strategies need further validation
2. Theoretical Assumptions:
    (1) IRT assumptions about LLMs need more justification
    (2) Independence assumptions between models may be violated due to shared architectures/training data

### Questions
1. Could alternative item selection methods (beyond Fisher information) yield better results?
2. How stable are the results across different random seeds and model subsets?

### Soundness
2

### Presentation
2

### Contribution
2
