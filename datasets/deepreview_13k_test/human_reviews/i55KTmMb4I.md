# M2rc-Eval: Massively Multilingual Repository-level Code Completion Evaluation

- Decision: Reject
- Scores: 5, 3, 6, 8

## Abstract
Repository-level code completion has drawn great attention in software engineering, and several benchmark datasets have been introduced.
However, existing repository-level code completion benchmarks usually focus on a limited
number of languages ($<$5), which cannot evaluate the general code intelligence abilities across different languages for existing code Large Language Models (LLMs).
Besides,
the existing benchmarks usually report overall average scores of different languages,
where the fine-grained abilities in different completion scenarios are ignored.
Therefore,
to facilitate the research of code LLMs in multilingual scenarios, we propose a massively multilingual repository-level code completion benchmark covering 18 programming languages (called \textbf{\benchmark{}}), 
and two types of fine-grained annotations (i.e., \textbf{bucket-level} and \textbf{semantic-level}) on different completion scenarios are provided,
where we obtain these annotations based on the parsed abstract syntax tree. 
Moreover, we also curate a massively multilingual instruction corpora \textbf{\instruct{}} dataset to improve the repository-level code completion abilities of existing code LLMs. Comprehensive experimental results demonstrate the effectiveness of our \benchmark{} and \instruct{}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces M2rc-Eval, a new benchmarks comprising repository-level code completion tasks in many more languages than current benchmarks. Unique features of this benchmark include fine-grained annotations for different types of completion scenarios. The authors also introduce M2rc-Instruct, which a training dataset to improve performance on M2rc-Eval.

### Strengths
- **Useful contributions.** The idea of having a very-large scale benchmark for repository-aware code completions across 18 programming languages is very useful. This will significantly help researchers improving Code LLMs on low resource languages such as Lua and Scala.
- **Novelty.** The fine-grained breakdown of code completion tasks is novel. However, I am not sure if this is needed or insightful. I would encourage the authors to present more analyses around this.
- **Interesting analyses.** I found the multi-lingual transfer experiment to be quite interesting and would be interested in a language-wise breakdown of this.
- **Paper exposition.** The paper is well-written and the analyses are presented in an easy-to-understand manner.

### Weaknesses
- **Data leakage concerns.** The presented benchmark is collected from The Stack v2 which sources code from public sources such as GitHub. As such it may have significant overlap with the training corpora of the Code LLMs already evaluated in the paper and for future LLMs. As such, this benchmark is not fool-proof from future leakage and the utility of the benchmark for future evaluations is questionable. Further, the authors have evaluated only small models, and evaluations on bigger models ≥ 15B or strong models like GPT-4o or Claude 3.5 Sonnet might reveal the effect of leakage more concretely.
- **Repository-level coding.** While the paper says that the benchmark is for repository-level code completion evaluations, the data collection described in Section 3.1 does not guarantee that the tasks in the benchmark strictly require repository-level contexts.
- **Evaluation metrics.** While EM/ES metrics are being used for evaluations and have been used in several previous works as well, I think it is time that we move on from these inaccurate metrics. We should resort to more robust metrics relying on static or execution analysis such as pass rate [1] or hallucination rate [2] for measuring correctness of code completions.
- **Nitpicks.**
    - The analyses in lines 416-428 are quite obvious, i.e., there is a negative correlation between ES and the number of tokens generated
    - Typos:
        - 047 - “can not” → cannot
        - 261 - textural → textual
        - 401 - shadow → shallow

[1] Chen, Mark, et al. "Evaluating large language models trained on code." *arXiv preprint arXiv:2107.03374* (2021).

[2] Jain, Nihal, et al. "On Mitigating Code LLM Hallucinations with API Documentation." *arXiv preprint arXiv:2407.09726* (2024).

### Questions
See comments above. But framed some concerns in question format below:

1. How do larger or more recent models such as StarCoder2-15B or GPT-4o perform on this benchmark?
2. Can you provide more insights from your multi-lingual transfer experiments? Specifically which languages benefit the most from Python-only fine-tuning? Can we predict such transfer ahead of time?

### Soundness
4

### Presentation
4

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
The paper introduces M$^2$RC-EVAL, a benchmark for repository-level code completion covering 18 programming languages, alongside M$^2$RC-INSTRUCT, a multilingual instruction dataset built in a similar way with M$^2$RC-EVAL. Using The Stack v2 dataset, the authors select repositories with 5+ stars containing 10-50 files, creating a dataset with 50,000 files per language for instruction tuning and 600 files per language for evaluation (w/ random 100 examples for validation and 500 for test). The benchmark introduces two types of annotations: bucket-level, an indicator of the depth of the AST node, and semantic-level, which was split in 11 major categories with language-specific subcategories. The authors benchmarked three major code LLMs (StarCoder-7B, DeepSeekCoder-6.7B, Code Llama-7B) under different settings and provide extensive analysis across multiple dimensions.

### Strengths
- This is the first dataset that covers 18 programming languages in repo-level code completion task
- The dataset Includes both evaluation and instruction tuning datasets
- Authors have conducted various evaluation across multiple dimensions

### Weaknesses
The most critical weakness of this paper is the use of The Stack v2 without addressing data contamination issues. Unlike previous work like Ding et al., 2023 which carefully controlled the date range to avoid overlap with model training data, this work directly uses a widely-used training corpus that contain data that was written many many years back. This fundamentally compromises the benchmark's ability to reflect real-world performance. The authors should either implement temporal splits or explicitly verify and control for overlap with model training data.

Further, the assumption that "we randomly choose a node on the AST as the completion cursor position" (Line 152) is overly restrictive and doesn't reflect real-world scenarios. Code completion can and does occur at any position in practice. A more realistic approach would be to allow arbitrary completion cursor positions while ensuring the completed code forms a valid AST node, similar to previous work cited in the paper.

In addition, the bucket-level annotation scheme appears arbitrary and lacks clear motivation. Dividing ASTs into exactly 10 buckets seems like an artificial constraint when simpler alternatives exist, such as directly using the node's layer number in the AST. It'd be great if authors could justify why this particular granularity was chosen or demonstrate its advantages over simpler approaches.

Finally, despite covering 18 programming languages, there was surprisingly very little discussion of language-specific insights. This is a great opportunity that the authors could seize to analyze how different language features, paradigms, and structures affect completion performance. Such analysis could provide valuable insights for both researchers and practitioners.

### Questions
In addition to the points mentioned in `Weaknesses`, I have a few questions and notes regarding the work:

1. Could the authors elaborate on how was the 5993 repos (line 204) split across eval and instruct?

2. It appears that adding retrieval seems to improve on EM but degrade on ES across models in Table 2. Why would this be expected?

3. On line 445: “StarCoder-7B base model already demonstrates strong coding proficiency, but lacks robust instruction-following capabilities” this is well expected as StarCoder-7B is a base model that has not been instruction tuned?

4. Some plots like Figure 4 look fancy but is conveying only little meaningful information in a readable way. Authors may consider using an alternative way to represent the data, e.g., a simple list or table. Similarly, Figure 5 is barely readable.

### Soundness
2

### Presentation
3

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
The paper releases a cross-file-context repo-level code completion benchmark that tests the fill-in-the-middle (FIM) completion abilities of Code LMs. GitHub repos are collected from Stack V2, and then the files' ASTs are individually processed to create varying categories of FIM holes for completion.

I believe the dataset (especially the instruct split) is a valuable OS contribution. Still, as it joins a whole host of existing benchmarks in this area, it should be fleshed out further regarding research questions.

### Strengths
1. The paper enters a crowded field of repo-level code completion benchmarks but differentiates itself from the pack by the size of the data splits and the number of languages supported.
2. The data collection process is clearly detailed

### Weaknesses
1. For a benchmark paper, it is a bit light on details of env setup, tooling and sandboxing
2. The evaluation is still based on surface form metrics like exact-match, which can be very noisy, especially for FIM settings. Scaling execution tests can be hard, but existing benchmarks like EvoCodeBench [1] and BigCodeBench [2] have done so using a combination of model generation and human validation.
3. Several very strong recent code model releases, such as Yi-Coder [3], Llama-3.1 [4], and Qwen-2.5-coder [5], are missing from the evals. This is pertinent due to their longer context support (up to 128k tokens), allowing for a much more interesting baseline than the paper currently uses (just the individual file in question). A very interesting evaluation of the paper is missing: how well the benchmark can be solved if the model just placed all the most pertinent files in context instead of just retrieving a few short snippets. Similarly, how would the various in-repo file ordering schemes previously explored by StarCoder-2 [6] and DeepSeek-Coder [7] affect this?

[1] https://arxiv.org/abs/2404.00599
[2] https://arxiv.org/abs/2406.15877
[3] https://arxiv.org/abs/2403.04652
[4] https://arxiv.org/abs/2407.21783
[5] https://arxiv.org/abs/2409.12186
[6] https://arxiv.org/abs/2402.19173
[7] https://arxiv.org/abs/2401.14196

### Questions
1. The cross-lingual transfer benchmarks may not be properly baseline. The paper uses StarCoder-1, a multi-PL pre-trained model that is continually pre-trained on Python code. This is a rather non-standard setting and would be fairer (across langs) if it were started from StarCoder-1-Base.
2. It would be interesting to explore the effect of various code retrievers instead of just Jaccard-Similarity in retrieving snippets in-context.

### Soundness
3

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
3

### Summary
This paper introduces M2RC-EVAL, a new benchmark designed to assess repo-level code completion performance across 18 programming languages. The benchmark uses two types of fine-grained annotations: bucket-level, based on the depth of abstract syntax trees, and semantic-level, which focuses on code semantics.  Additionally, the paper presents a multilingual instruction corpus, M2RC-INSTRUCT, to improve code completion models.

### Strengths
**Massive multilingual benchmark**: The paper introduces a novel multilingual benchmark that supports 18 programming languages, which is a significant expansion over existing benchmarks that only handle a limited number of languages.

**Quality control**: The dataset construction is considered thorough, with a robust collection process from github repos and clear quality control measures. 

**Clear writings**: This paper is well-organized, with clear explanations of how the benchmark and instruction dataset were constructed and evaluated. The use of tables and figures aids in understanding the experimental results.

Overall, this benchmark contributes to address the growing need for multilingual evaluation in code completion. The fine-grained annotation methodology also provides useful insights into the challenges faced by models in many programming scenarios.

### Weaknesses
**Evaluation Metrics:** While the paper mainly uses exact match and edit similarity metrics, these may not fully capture the functional correctness of the generated code. I acknowledge that implementing an execution-based evaluation across such a massive multilingual benchmark poses considerable challenges, and this is more of a broader limitation within the field rather than a direct weakness of this particular work. I do appreciate the authors’ inclusion of CodeBLEU, which offers another perspective by considering syntactic and semantic aspects of code generation. Still, it would be more insightful to explore whether there is any correlation between CodeBLEU scores and the more traditional EM and ES metrics.

### Questions
Apart from the point in the 'Weaknesses' section, I have the following questions and suggestions:

**Proprietary Model Comparison**: Do the authors plan to include a comparison with advanced proprietary models, even on a smaller subset of the benchmark? This could offer insights into how fine-tuned open-source models compare against the leading commercial solutions.

**Qualitative Error Analysis (Suggestion):** It would be insightful to provide a more detailed qualitative error analysis to highlight where current code LLMs encounter the most difficulty across different languages. This could help pinpoint areas for further improvement.

**Figure Clarity (Suggestion):** While the visualizations are nicely presented, some figures (e.g., Figures 4 and 14) have very small fonts, making it difficult to read the details. Increasing the font size in these visualizations would enhance clarity and accessibility for readers.

### Soundness
3

### Presentation
4

### Contribution
4
