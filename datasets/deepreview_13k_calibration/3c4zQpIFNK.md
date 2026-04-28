# LIME: LESS IS MORE FOR MLLM EVALUATION

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8, 6

## Abstract
Multimodal Large Language Models (MLLMs) are measured on numerous benchmarks like image captioning, visual question answer, and reasoning. However, these benchmarks often include overly simple or uninformative samples, making it difficult to effectively distinguish the performance of different MLLMs. Additionally, evaluating models across many benchmarks creates a significant computational burden. To address these issues, we propose LIME (Less Is More for MLLM Evaluation), a refined and efficient benchmark curated using a semi-automated pipeline. This pipeline filters out uninformative samples and eliminates answer leakage by focusing on tasks that require image-based understanding. Our experiments show that LIME reduces the number of samples by 76\% and evaluation time by 77\%, while it can more effectively distinguish different models' abilities. Notably, we find that traditional automatic metrics like CIDEr are insufficient for evaluating MLLMs’ captioning performance, and excluding the caption task score yields a more accurate reflection of overall model performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces LIME (Less Is More for MLLM Evaluation), a refined benchmark for evaluating Multimodal Large Language Models (MLLMs). The authors propose a semi-automated pipeline to curate a more efficient and discriminative evaluation dataset by filtering out uninformative samples and eliminating answer leakage. The resulting benchmark reduces the number of evaluation samples by 76% and evaluation time by 77% while maintaining or improving the ability to distinguish between different models' capabilities. Key findings include the inadequacy of traditional automatic metrics for captioning tasks and the importance of excluding caption task scores for more accurate overall performance assessment.

### Strengths
* Originality: 
   * Novel approach to benchmark curation that focuses on quality over quantity. 
   * Creative use of MLLMs themselves as judges for data filtering. 
   * Innovative three-stage filtering pipeline (model judgment, semi-automated screening, leakage elimination)
* Clarity:
   * Well-structured presentation of the methodology 
   * Clear visualization of data statistics and filtering results
* Quality:
   * Comprehensive empirical validation across multiple models and benchmarks
   * Thorough analysis of the correlation between different subtasks

### Weaknesses
 - The filtering pipeline heavily relies on existing MLLMs as judges, which could potentially introduce biases from these models into the benchmark. While the authors attempt to mitigate this by using multiple models, a more thorough analysis of potential inherited biases would strengthen the work.
- The paper does not fully explore whether the reduced dataset size might affect the statistical significance of evaluation results. While efficiency gains are clear, more discussion of the tradeoffs between dataset size and evaluation reliability would be valuable
- The choice of tasks and task weightings in the final benchmark appears somewhat arbitrary. A more systematic approach to determining which tasks are most important for evaluating MLLMs would strengthen the methodology.

### Questions
1. How sensitive is the filtering pipeline to the choice of judge models? Would using different combinations of models as judges result in significantly different benchmark compositions?
2. How do you ensure that the filtering process doesn't inadvertently favor certain types of model architectures or training approaches?
3. Have you explored whether the reduced dataset size affects the statistical significance of model comparisons? What is the minimum number of samples needed for reliable evaluation?
4. (Minor) If the benchmark is accepted, what will the authors do to let the community buy the idea using your combined filtered benchmark instead of the existing ones? While I believe the benchmark is useful. One concern from my side is that people may still stick to the individual raw datasets.

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
Existing MLLM benchmarks often include overly simple or uninformative samples, making it difficult to effectively distinguish the performance of different MLLMs. This work proposes LIME , a refined and efficient benchmark curated using a semi-automated pipeline.
This pipeline filters out uninformative samples and eliminates answer leakage by focusing on tasks that require image-based understanding.  The experiments show that LIME reduces the number of samples by 76% and evaluation time by 77%, while it seems promising to be more effective for distinguishing different models’ abilities.

### Strengths
The problem is important and interesting to the community. Evaluation is an important part for multimodal LLM. This work dives deep into existing benchmarks and conducts comprehensive analysis to study the specific questions in those benchmarks. The motivation of Figure 1 and 2 is clear and important.

### Weaknesses
1. My biggest concern is that the approach only filter the samples from the existing benchmarks, do we need to consider adding other metrics/domains to evaluate MLLMs? 
2. Another interesting thing is that sometimes MLLM may not "read" image but directly answer the questions based on the knowledge from LLM, do we need to consider adding this into the benchmark?

### Questions
See weakness.

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
4

### Summary
The paper proposes the LIME, a refined and efficient benchmark for MLLM evaluation. The paper first shows that existing benchmarks contain a large proportion of easy or noise samples that cannot reflect the actual capabilities of MLLM. Then, the paper proposes a three-stage pipeline to filter the existing 10 benchmarks across 6 types. The easy samples, wrong-labeled samples, and answer-leakage samples are removed during this process. The refined benchmark can provide a more rigorous evaluation of the existing MLLMs.

### Strengths
1. This paper uncovers the problem of existing benchmarks and the proposed filter method is reasonable and meaningful. 
2. The filter benchmark provides a more rigorous evaluation of the existing MLLMs and will have practical significance for future MLLM evaluations.
3. The experiment results are comprehensive and insightful.

### Weaknesses
 1. Do not compare with other general MLLM benchmarks like MMMU or MMBench. I would also like to see whether the easy samples or answer-leakage samples exist in these benchmarks.


### Questions
1. In Line 036, the author mentions 'How many chairs in the image'. Does it mean all existing MLLMs' counting capabilities are not satisfactory?
2. In Line 156, 'The model has encountered a specific question during training'. Does the term 'model' here refer to LLM or MLLMs?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents a refined and efficient MLLM benchmark called LIME, which enhances the quality of existing benchmarks through semi-automatic refinement. LIME consists of 9,400 evaluation samples across six types of tasks and ten different benchmark datasets. The authors evaluated over 30 models and provided some analyses based on the results.

### Strengths
1. The removal of easy samples and meaningless or erroneous data from the dataset is crucial for more efficient and reasonable evaluation of MLLMs. The authors utilize GPT-4V and human annotators to fillter out those illogical and meaningless questions, which seems to have been overlooked in previous benchmarks.
2. The authors evaluate over 30 baseline models and provide an analysis of MLLM performance based on the evaluation results, which clearly represents a significant amount of work.
3. The authors also construct a similarity search system for investigating the gap between LIME and real-world users’ queries, which shows that the current benchmark does not fully cover the instruction requirements of real-world scenarios.

### Weaknesses
1. The proposed benchmark, LME, integrates existing benchmarks and adopts their evaluation metrics, which have been previously criticized in earlier works (specifically designed for evaluating MLLMs) [1, 2] as being unsuitable for assessing open-form outputs of MLLMs. For instance, the authors mention, “for tasks such as AI2D, ScienceQA, OCRBench, and POPE, we calculate the accuracy of the extracted responses.” In these benchmarks, if the correct answer is "bike" but the model outputs "bicycle," it is considered incorrect, which is an unreasonable approach. The authors should employ more appropriate evaluation metrics, such as multiple-choice questions, true/false questions, or scoring by GPT.
2. To eliminate answer leakage, such as when a model has seen the questions during training, the authors conduct a text-only check using pure text LLMs. Based on the responses from these LLMs, they remove samples that can be directly answered without using the image. However, this approach is unreasonable because these multimodal questions would only appear in the training of MLLMs. Therefore, the authors should use MLLMs to filter out such questions instead of relying on LLMs.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
