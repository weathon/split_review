## Human Reviewer 1

### Summary
This paper proposes ARENABENCHER, a framework for automatic benchmark evolution using multi-model feedback. The idea is to iteratively generate new test cases while preserving the core ability of each item and selecting those that degrade performance across several models. The authors claim that the method improves difficulty, fairness, and separability of existing benchmarks such as GSM8K, CSQA, and harmful behavior datasets.

### Strengths
1. The paper tackles an important problem: benchmark contamination and stagnation under rapid LLM progress.

2. The multi-model feedback mechanism is conceptually interesting and potentially more robust than single-model adversarial rewriting.

3. The framework is clearly modular and described in a step-by-step manner.

### Weaknesses
1. Major claims are not empirically justified. Many statements in Sections 1–3 are presented as facts without direct supporting evidence. For example, the claim that multi-model feedback “mitigates bias” is not demonstrated beyond intuition.

2. Experimental definitions are unclear or inconsistent. Key metrics such as fairness are vaguely defined in prose but not rigorously formalized in Section 4. In Table 2, fairness is said to represent “how evenly the performance drop is distributed,” but if so, the original dataset should always be 100% fair by definition, which contradicts reported values (e.g., 84.8 or 82.9). I could not understand what a fairness value of 85 actually means.

3. Evaluation is incomplete. There is no ablation for critical design choices (e.g., the number of sampled models, verifier quality, or extraction accuracy). Moreover, the paper lacks qualitative analysis of failure cases until very late (Figure 2), and even there the discussion remains superficial.

### Questions
1. Please provide a precise mathematical definition of fairness and clarify why original datasets do not reach 100 under your metric.

2. Can you provide evidence that multi-model feedback truly outperforms single-model-guided rewrites, beyond performance drop magnitude?At present, I believe that the paired trends in Table 1 alone are not sufficient to draw such a conclusion

3. How sensitive is your framework to incorrect ability extraction or verifier mistakes? Can you quantify this?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
5

---

## Human Reviewer 2

### Summary
ArenaBencher is a framework for automatic benchmark evolution that addresses data contamination in LLM evaluation. The system extracts test objectives, generates candidate questions, verifies them with LLM-as-a-judge, and uses multi-model feedback (sampling √K models) to select variants that consistently degrade performance across models. It includes iterative refinement using successful candidates as in-context demonstrations. The framework is evaluated on GSM8K (math), Harmful Behaviors (safety), and CommonsenseQA (reasoning) using 6 open-source models.

### Strengths
1. The design avoids creating model-specific adversarial examples that may be trivial for some models, helping ensure that updated benchmarks reflect shared weaknesses across diverse architectures rather than exploiting idiosyncrasies of particular systems.
2. The four desiderata (difficulty, separability, fairness, alignment) provide a principled way to assess benchmark quality.
3. Testing across math, safety, and reasoning domains demonstrates generalizability.
4. 95% alignment and 96% correctness on 100 GSM8K samples provides high alignemnt evidence of the augmented data.

### Weaknesses
Though the paper is well-written, there are two fundamental weaknesses I have to bring out:
1. The paper's core motivation is to reduce data contamination's impact on benchmark validity, yet the evaluation metrics do not directly demonstrate reduced contamination or improved prediction of true model capabilities on unseen data by the four metrics (Difficulty, Separability, Fairness, Alignment). The paper needs real-world data validation such as temporal splits or naturally occurring unseen data. For example, GitHub PRs after model training cutoffs provide natural test cases for SWE-bench contamination evaluation (if there is any). The evaluation should test whether ArenaBencher augmentation on augmented SWE-bench better predicts performance on post-cutoff PRs compared to other baselines. Without this validation, it remains unclear whether ArenaBencher actually solves data contamination or merely creates harder variants.
2. The paper provides no comparative evaluation with baseline methods, making it impossible to assess how good the proposed method is. Two critical types of comparisons are missing. First, the paper does not compare multi-model feedback against single-model augmentation to establish cost-effectiveness, leaving unclear whether sampling multiple models provides proportional improvement over using just one model given the additional API costs. Second, there is no comparison with other multi-model collaboration approaches or simpler augmentation methods such as paraphrasing or rule-based perturbations.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper introduces a model-agnostic framework designed to automatically evolve benchmarks to counteract the problem of data contamination in large language model (LLM) pretraining corpora.

The ArenaBencher pipeline operates in four main stages. The authors apply this framework to benchmarks in three domains: mathematical reasoning (GSM8K), commonsense reasoning (CommonsenseQA), and safety (AdvBench Harmful Behaviors). 

The results demonstrate that the evolved benchmarks are more difficult for a range of open-source models, improve the separability, and distribute performance drops fairly across the model pool, all while maintaining alignment with the original task objectives as verified by both automated metrics and human evaluation.

### Strengths
This paper is easy to follow. It tackles the urgent and widely recognized problem of benchmark contamination and the resulting inflation of LLM performance metrics. I think the proposed direction of creating dynamic, evolving benchmarks is valuable.

The authors have conducted comprehensive experiments to validate their points. The framework is tested across three distinct and important domains (mathematical reasoning, commonsense reasoning, and safety), with LLAMA3, Qwen3, and Mistral. 

Difficulty, Separability, Fairness, and Alignment are measured. The inclusion of a human evaluation study to validate alignment and correctness further strengthens the empirical results.

### Weaknesses
I think the framework lacks a mechanism to balance the competing goals of difficulty and separability. The results in Table 2 also partly show this. The current selection mechanism, which selects candidates with the highest aggregated loss, may favor test cases that are simply too hard for all models, causing their scores to cluster near zero and reducing the benchmark's ability to distinguish between them. A truly discriminative benchmark should maximize the variance in performance across models.

The design choice of sampling $m = \lceil\sqrt{K}\rceil$ models for feedback should be better justified. Although the paper cites "classical ensemble heuristics" from Random Forests and XGBoost, ArenaBencher's objective is different. There is no guarantee that a heuristic designed for decorrelating learners by subsampling features would be optimal for estimating a population statistic by subsampling models.

The entire framework is dependent on a single proprietary model (GPT-4). The authors commendably include a failure case analysis for the generator (Figure 2), but do not discuss or analyze the robustness of the verifier/judge. A systematic bias or blind spot in the judge model could silently poison the entire evolved benchmark.

### Questions
While the related work section effectively contrasts the approach with single-model adversarial attacks, it could be improved by including more literature on dynamic benchmark generation.

The authors could provide ablation studies or theoretical arguments to support the $m = \lceil\sqrt{K}\rceil$ choice over alternatives.

Could the authors provide an analysis of the computational cost of this process? How does the cost scale with the benchmark size $N$, the model pool size $K$, and the number of refinement rounds $R$?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
4