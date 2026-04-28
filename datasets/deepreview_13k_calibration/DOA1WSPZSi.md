# Can Knowledge Graphs Make Large Language Models More Trustworthy? An Empirical Study over Open-ended Question Answering

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5

## Abstract
Recent works integrating Knowledge Graphs (KGs) have led to promising improvements in enhancing reasoning accuracy of Large Language Models (LLMs).
However, current benchmarks mainly focus on closed tasks, leaving a gap in the assessment of more complex, real-world scenarios. This gap has also obscured the evaluation of KGs' potential to mitigate the problem of hallucination in LLMs.
To fill the gap, we introduce \ours{}, a new benchmark specifically designed to assess LLMs enhanced with KGs under open-ended, real-world question answering scenarios.
\ours{} is designed to closely reflect the complexities of practical applications using questions from different types, and incorporates specific metrics to measure both the reduction in hallucinations and the enhancement in reasoning capabilities.
To consider the scenario in which KGs may have varying levels of mistakes, we further propose another experiment setting \oursp{} to assess model performance when the semantics and structure of KGs are deliberately perturbed and contaminated.
\ours{} aims to (1) explore whether KGs can make LLMs more trustworthy in an open-ended setting, and (2) conduct a comparative analysis to shed light on methods and future directions for leveraging KGs to reduce LLMs' hallucination.
We believe that this study can facilitate a more complete performance comparison and encourage continuous improvement in integrating KGs with LLMs. The code of this paper is released at \codelink{}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces OKGQA, a benchmark designed to assess the trustworthiness of LLMs augmented with KGs in open-ended QA scenarios. It also includes a perturbed version (OKGQA-P) with various KG perturbations to test the resilience of LLMs against 
inaccuracies in KG knowledge. The proposed methodology expands RAG and integrates two main processes: G-retrieval and G-generator, for utilizing KG knowledge in different forms (like triplets, paths, or subgraphs).  The study tests these models across 850 queries spanning 10 categories, utilizing metrics like FActScore and SAFE to gauge the reduction of hallucinations in model outputs.

### Strengths
1. The introduction of OKGQA as a novel benchmark can address a current research gap in assessing LLMs in open-ended, real-world scenarios.
2. The perturbed benchmark, OKGQA-P, allows for the evaluation of LLM robustness in response to inaccuracies or noises in KGs.  
3. The comprehensive and well-organized experimental results across different forms of information and different types of queries show the effectiveness of the proposed methods and can provide valuable insights for future researchers.

### Weaknesses
1. The proposed methodology of G-retrieval and G-generator is similar to the existing line of work on RAG and KG-augmented generation [1]. However, there is a lack of comparison to demonstrate how these proposed methods fundamentally differ from previous methods applied to closed-end QA. Specifically, the paper does not adequately articulate the novel aspects of their approach beyond standard RAG techniques, particularly in how they handle the complexities of open-ended question answering with knowledge graphs.
2. The queries are generated using predefined templates with LLMs, which raises concerns about their ability to authentically represent the distribution and complexity of real-world questions. The reliance on templates may result in a dataset that lacks the nuances and variability found in natural human queries, potentially limiting the benchmark's applicability to real-world scenarios.
3. The proposed OKGQA-P supports only four types of perturbation heuristics, which require further explanation on how they sufficiently cover the inaccuracies in knowledge graphs for real-world applications. The chosen perturbations, while relevant, may not capture the full spectrum of errors present in real-world KGs, such as entity mislinking or attribute inaccuracies, which could affect the robustness evaluation.
4. Lack of evaluation on how improvements in reducing hallucination relate to the retrieved KG knowledge. The study does not provide a clear analysis of how specific pieces of retrieved knowledge contribute to the reduction of hallucinations, making it difficult to understand the mechanisms by which the proposed methods achieve their results.

### Questions
1. How representative are the synthesized queries of actual real-world questions? What methods were employed to ensure that their complexity and distribution are realistic?

2. How many evaluators participated in the manual assessment of query naturalness, and what criteria were used for this human evaluation to ensure a standardized evaluation?

3. What is the correlation between the LLM's automatic evaluations and human judgments of query quality? How were discrepancies between the automatic scores (s_auto) and manual scores (s_human) addressed during the evaluation process?

4. Were different values of 'k' for hops around question entities considered to test the robustness of model responses in relation to variations in graph size and structure?

5. Can the authors provide a more detailed breakdown of performance across the different query types, specifically how various perturbation methods affected certain query types?

6. In section 4.2, it is unclear how the retrieved structured knowledge is integrated into the PLM. In particular, what are the differences in final sequence length across different forms of information (this can be essential for managing the LLM inference costs)?

7. Please explain why, in certain query categories (such as "evaluation and reflection"), the knowledge-augmented methods result in degraded performance compared to the baseline.

### Soundness
3

### Presentation
2

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
The key innovation is the introduction of benchmarks, OKGQA, for evaluating LLMs augmented with KGs in real-world QA scenarios. The second experiment, designated OKGQA-P, is intended to assess the efficacy of the model in the context of a scenario wherein the semantics and structure of the knowledge graph are disrupted and compromised.

### Strengths
1. The effectiveness of different retrieval methods in conjunction with LLMs is analyzed in experiments that provide insights into the combination of KGs and LLMs.

### Weaknesses
1. The unique contributions of the OKGQA benchmark are insufficiently defined, and the distinctions between OKGQA and existing benchmarks are not clearly articulated.
2. While the paper references several closed-ended elements from related literature, it lacks a thorough discussion of limitations and practical implications.
3. The question of whether KGs can reduce hallucinations in LLMs is widely recognized as affirmative, given the effectiveness of RAG techniques in mitigating hallucination issues.  However, what is pertinent to this paper is an exploration of whether KGs can further reduce hallucinations in scenarios with open-endedness.

### Questions
In section 3.2, the paper mentions that ''…we introduce perturbations to edges in the KG to degrade the quality of the KGs, diminishing human comprehensibility.'', why human comprehensibility is diminished?

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
This paper focuses on testing whether the knowledge graph make large language models more trustworthy，which is an important in KG and LLM area. This paper does a empirical study over open-ended question answering task to evaluate above issues.
 The strength of this paper are as follows: 
This paper addresses a significant research question of whether knowledge graphs (KGs) can make large language models (LLMs) more reliable in open-ended question answering. This paper  designed a new benchmark, OKGQA, specifically for assessing LLMs enhanced with KGs in open-ended, real-world question answering scenarios.
By proposing the OKGQA-P experimental setup, this paper considers scenarios where KGs may have varying levels of errors, further simulating real-world situations where KGs' quality can be inconsistent
This paper conducted a series of experiments on OKGQA and OKGQA-P, analyzing the effectiveness of various retrieval methods and LLMs of different scales.
The weakness of this paper are as follows:
While OKGQA-P considers errors in KGs, further exploration of the generalizability of these findings to a broader range of real-world applications may be necessary.
Although the authors present experimental results, a more in-depth analysis and discussion on why certain methods outperform others and the potential limitations of these methods could be provided.

### Strengths
This paper addresses a significant research question of whether knowledge graphs (KGs) can make large language models (LLMs) more reliable in open-ended question answering. This paper  designed a new benchmark, OKGQA, specifically for assessing LLMs enhanced with KGs in open-ended, real-world question answering scenarios.
By proposing the OKGQA-P experimental setup, this paper considers scenarios where KGs may have varying levels of errors, further simulating real-world situations where KGs' quality can be inconsistent
This paper conducted a series of experiments on OKGQA and OKGQA-P, analyzing the effectiveness of various retrieval methods and LLMs of different scales.

### Weaknesses
While OKGQA-P considers errors in KGs, further exploration of the generalizability of these findings to a broader range of real-world applications may be necessary.
Although the authors present experimental results, a more in-depth analysis and discussion on why certain methods outperform others and the potential limitations of these methods could be provided.

### Questions
nan

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
This paper proposes OKGQA to evaluate LLMs enhanced with KGs under open-ended, real-world question-answering scenarios. The authors also implement the OKGQA-P experimental setting to assess model performance when KGs are perturbed by real-world contamination. A series of experiments conducted on both OKGQA and OKGQA-P demonstrate that integrating KGs with LLMs can effectively mitigate hallucinations in LLMs, even when KGs are contaminated.

### Strengths
1. The authors elaborate on the necessity of evaluating LLMs under open-ended QA scenarios in detail.

2. The OKGQA-P setting to assess KG-augmented LLMs when KGs are contaminated is intuitive and reasonable.

3. The perturbation results in Figures 4 and 5 are very interesting.

### Weaknesses
1. The observation (2) in line 76 that CoT and SC may cause bias and hallucination is confusing. The results (Llama3.1 8B) in Table 1 show that the integration of CoT and SC helps improve quality and factuality.

2. The authors may want to provide more statistical details including the involved people's educational background, and the final score distribution agreement between the people and LLMs in "The human-in-the-loop process in Line 186". Specifically, inter-rater reliability metrics such as Cohen's Kappa coefficient should be included to assess the consistency of human evaluations.

3. The authors may need to do more kinds of perturbation methods including node deletion to mimic scenarios when a query cannot be retrieved from a KG. Furthermore, the perturbation methods should also consider real-world scenarios such as entity ambiguity, which can arise from misspellings or the use of synonyms.

4. The authors may want to discuss and summarize more RAG methods for open-ended QA settings including [A, B, C].

### Questions
1. The authors may want to provide more details of the metrics used in Lines 292 to 295.

2. The results in Figures 4 and 5 are interesting. Does that mean that even incorporating a  severely perturbed KG (e.g., perturbation level=1.0 in Figures 5 (a), (b), and (c)), FS-SG can still help LLMs in reducing hallucination?

### Soundness
3

### Presentation
2

### Contribution
2
