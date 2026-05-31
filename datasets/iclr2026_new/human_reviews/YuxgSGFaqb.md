## Human Reviewer 1

### Summary
The paper introduces SWINGARENA, a CI-faithful, adversarial code-evaluation arena where an LLM “Submitter” proposes patches and an LLM (or human) “Reviewer” writes tests to break them; the roles can switch across rounds. It ships (i) a rigorously curated multi-language dataset with runnable CI, (ii) a Retrieval-Augmented Code Generation (RACG) pipeline to find relevant files and synthesize fixes, and (iii) arena metrics (e.g., Win Rate, SPR/RPR) to quantify progress. Experiments on real repositories show the arena surfaces harder, more realistic failure modes than static benchmarks and that better retrieval/testing policies materially improve pass rates.

### Strengths
1. The adversarial submitter-reviewer paradigm with role-switching is creative and mirrors real-world collaboration better than static benchmarks.
2. Rigorous data curation: Three-stage filtering with human expert validation is commendable.
3. Well-oraganized writing, easy to understand.

### Weaknesses
1) **Limited novelty / “integration over invention.”**  
   The work skillfully engineers an end-to-end pipeline for realistic SE evaluation, but core techniques (retrieval, ranking, CI emulation, multi-turn prompting) largely reuse known components. 
2) **Under-granular ablations for RACG.**  
   Current ablations are mostly on/off toggles or coarse retrieval settings, leaving it unclear which sub-module drives gains.
   - **Actionable:** Provide per-component ablations on (i) chunk size & overlap, (ii) reranker family (bi-encoder vs. cross-encoder), (iii) proximity/structure priors (same-dir, same-package), (iv) adaptive Top-k vs. fixed, (v) failure-triggered expansion rules; add mediation analysis to quantify each component’s indirect effect on final win rate.
3) **Language & ecosystem coverage is narrow.**  
   Results cover C++/Python/Rust/Go but omit **Java/JS/TS** and build systems (**Maven/Gradle**, **pnpm/yarn/monorepo**). This limits external validity for common enterprise stacks.

### Questions
1) **Causal attribution:** How do you isolate the gain from the *adversarial, role-switching* protocol itself (vs. model scale, retrieval strength, prompt length)? Can you run controlled A/Bs holding RACG constant while removing role-switching, and report mediation analysis?

2) **Real-world parity:** How closely do local CI runs match upstream (e.g., GitHub Actions) on pass/fail and runtime? Please provide a paired evaluation with agreement statistics and discuss observed drift.

3) **Gaming & robustness:** Are there “score-hacking” strategies (e.g., submitter creates trivially detectable but non-critical faults; reviewer overfits to diffs)? What constraints or equilibrium analyses prevent metric inflation?

4) **Scaling laws:** As model size, number of rounds, and repo size (files, dependency depth) grow, do we observe consistent scaling behavior? Which has higher marginal return: **more rounds** or **stronger/adaptive retrieval**?

5) **Granular failure taxonomy:** What are the dominant failure modes per language (retrieval miss, build failure, semantic error)? Please add an error decomposition table linking failure modes to specific RACG sub-modules.

6) **Cross-ecosystem generalization:** What minimal changes are needed to support Java (Maven/Gradle) and JS/TS monorepos? Any zero-/few-shot transfer experiments showing the framework’s portability?

7) **Contamination audits:** How did you detect/prevent training–evaluation overlap for both LLMs and the reranker? 

8) **Metric resolution:** Beyond overall win rate, can you report **defect-type × difficulty** strata (and CIs) to demonstrate the framework discriminates hard cases rather than being dominated by easy issues?

9) **Adaptive retrieval policy:** Can RACG expand beyond fixed Top-k after early failures? Please report the success-latency trade-off and whether adaptive policies change conclusions.

10) **Cost & reproducibility:** What is the typical wall-clock time and token usage per match under your default settings? Could you provide scripts and a “minimal slice” that reproduces headline results on modest compute?

> If the above analyses (especially #1, #2, #4, #7) are addressed, I would likely raise my overall score.

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper introduces an adversarial evaluation framework for LLMs in software engineering, arguing that existing benchmarks like HumanEval are too simplistic by focusing only on single-function unit tests. SwingArena aims to model real-world workflows by using actual long-context GitHub issues, executing generated patches against the full CI pipeline, and implementing an adversarial battle protocol. In this protocol, one LLM acts as a Submitter generating a patch, while another acts as a Reviewer generating new tests specifically to break the submitted patch. The authors find that evaluating models in this dynamic, CI-driven arena reveals nuanced model "personalities" (e.g., "aggressive patchers" v.s. "reliable coders") and surfaces important failure modes (like cross-file consistency errors) that static benchmarks overlook.

### Strengths
- The paper is well-motivated, addressing a clear gap in existing research. It convincingly argues that the field must move beyond simple unit test success and instead evaluate models on their ability to produce code that is "valid, compliant, and able to pass a full CI pipeline and peer review."
- A core contribution is the new dataset of over 2300 real-world GitHub issues across four languages (C++, Python, Rust, Go). Each problem is CI-grounded, meaning the original human solution was verified to pass the full CI pipeline, ensuring a high-quality, realistic testbed.
- The adversarial framework successfully reveals behavioral tendencies that static tests can't. For example, the paper found that GPT-4o acts as an "aggressive patcher" (achieving high win rates), whereas DeepSeek and Gemini "prioritize correctness and CI stability" (scoring higher on CI pass rates).

### Weaknesses
- It's hard to interpret the primary "Win Rate" metric given its adversarial nature. A model's success depends on the relative weakness of its opponent (the reviewer model). This makes it difficult to assess the absolute quality and correctness of a solution based on this metric alone.

### Questions
- Continuous Integration pipelines can be computationally expensive to run repeatedly. Given that the reviewer agent analyzes the submitter's patch and generates targeted tests, could this reviewer component potentially be leveraged to reduce the cost of CI runs needed in an evaluation? For instance, could the reviewer's analysis provide a strong signal for early rejection of clearly incorrect patches before running the full CI, or could it intelligently select a subset of critical tests to run instead of the entire suite?
- You mentioned that the quality gates for the reviewer-generated tests are crucial for preventing exploitative behavior and ensuring test validity. Could you provide more detail on how strictly these were enforced during the evaluations? For example, what was the approximate rejection rate for reviewer-generated tests that failed these gates, and what were the common reasons for rejection (e.g., failing against the golden patch, modifying production code, style violations)?

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper introduces SWINGARENA, a framework for evaluating LLMs on software development tasks. Unlike static benchmarks, SWINGARENA simulates a collaborative workflow by pairing LLMs into "submitter" (patch generator) and "reviewer" (test case generator) roles. The evaluation is grounded in real-world GitHub issues and utilizes repository-native CI pipelines for verification. To manage the long-context nature of large codebases, the framework includes an RACG module.

### Strengths
present a new dataset of 2,300 CI-filtered issues across C++, Python, Rust, and Go, and provide experimental results for several proprietary and open-source models.

### Weaknesses
1. The paper's main "battle" metric, the Win Rate, is severely confounded. The "Win Rate" is defined as the submitter's patch passing all CI checks, including the reviewer's generated test. As the authors correctly note, "higher values may also indicate weaker reviewer tests". This confounding variable makes it impossible to draw clear conclusions about a submitter's absolute capabilities.

2. The paper introduces a complex, multi-stage RACG module but explicitly states it is a "baseline rather than a standalone algorithmic contribution". The ablation study in Table 3  fails to justify its necessity.

### Questions
1. The results for GPT-4o seem contradictory. The text claims it has "relatively lower RPR/SPR scores", but also a "dominance in producing adversarially-strong patches" based on high win rates ($\ge0.90$). Why a model have a low SPR but a high Win Rate?

2. Given that the "Win Rate" metric is confounded by the reviewer's strength, would it not be more sound to evaluate the submitter's patch directly against the golden patch and the full, human-written test suite?

3. In the RACG ablation (Table 3), what does the "Top-k Related" retrieval baseline consist of?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes SWINGARENA, a dynamic adversarial evaluation framework for real software engineering tasks that pairs LLMs as submitters and reviewers who generate and test patches, respectively, through a continuous integration (CI) pipeline. SWINGARENA also leverages retrieval augmentation to retrieve the most relevant context from code bases for a variety of languages (C++, Python, Rust, and Go), spanning 400 issues and surfacing new problems, and also showing behavioral differences in models as patch generators and validators.

### Strengths
1. Introduces iterative and adversarial evaluation that incorporates software engineering in CI development scenarios and goes beyond mere unit tests.
2. Propose a multi-language long context retrieval (RACG) pipeline for fetching relevant code context that combines syntax-aware chunking, dense reranking, and token-budget–aware packing across C++, Python, Rust, and Go.
3. A dataset of 2300 real GitHub issues with 400 high-quality issues (100 per language) selected for evaluation.
4. Benchmarking of several state-of-the-art open and closed-source LLMs.

### Weaknesses
1. The win rates of all models are very close to each other (almost every model gets 0.9 or above), which makes me question the utility of this benchmark in terms of model selection.
2. Best@k values for all the models are also very close to each other, which makes it hard to judge which model is better. 
3. Retriever doesn’t seem to boost performance much in Table 3, especially for Best@3 for Python and C++. The authors also acknowledge a weakness in how many relevant files can be included (only 5 files) and that context retrieval leads to the most failures (26% according to Appendix C1). This makes the benchmark less reliable since the LLMs cannot perform optimally under these limitations. 
4. Missing citations for some relevant work, like CodeRAGBench [1], CrossCodeEval [2], and RepoCoder [3].

[1] Wang, Zora Zhiruo, et al. "Coderag-bench: Can retrieval augment code generation?." arXiv preprint arXiv:2406.14497 (2024).  
[2] Ding, Yangruibo, et al. "Crosscodeeval: A diverse and multilingual benchmark for cross-file code completion." Advances in Neural Information Processing Systems 36 (2023): 46701-46723.  
[3] Zhang, Fengji, et al. "Repocoder: Repository-level code completion through iterative retrieval and generation." arXiv preprint arXiv:2303.12570 (2023).

### Questions
What does “PK-style dual-role evaluation” on line 78 mean?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
6

### Confidence
4