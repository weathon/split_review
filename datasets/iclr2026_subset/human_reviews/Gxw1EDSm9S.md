## Human Reviewer 1

### Summary
This paper presented SWE-Bench Atlas, an automated framework for generating scalable, multilingual software engineering benchmarks from GitHub pull requests. It uses a six-stage pipeline to ensure reproducibility and quality, producing challenging tasks for evaluating LLMs. The tool addressed limitations of manual curation and demonstrates value for both evaluation and model fine-tuning.

### Strengths
+ focus on a practical task
+ the framework is well-structured

### Weaknesses
1. lack of novelty:

The paper’s contributions are primarily integrative rather than innovative. Many of the components, i.e., such as LLM-powered Dockerization, log parsing, and quality scoring, build on existing ideas and tools (e.g., SWE-Agent, SetUpAgent, LLM-as-a-judge). While the combination of these elements is new, the individual techniques are not. 

2.  Overemphasis on engineering:

This work is a strong engineering effort that addresses practical bottlenecks in benchmark creation. However, it does not propose new scientific ideas or evaluation frameworks. It is more akin to a tooling paper or system demo than a core research contribution.

3. Lack data quality assurance:

 SWE-Bench Atlas's automated approach, while scalable, may not fully overcome the fundamental data quality issues that manual curation (like in SWE-bench Verified) was designed to address.

### Questions
1. How to ensure the data quality when using SWE-Bench Atlas to collect new data?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper presents **SWE-Bench Atlas**, a fully automated framework for generating high-fidelity, repository-level coding tasks from open-source GitHub projects. It builds a complete pipeline through six automated modules: the **Sourcing Module**, **Agentic Dockerization System**, **State-Based Test Classification**, **Curation Module**, **Annotation Module**, and **Trajectory Curation System**. Experiments show that its initial validation set contains **5,909 tasks from 3,154 repositories**. On this benchmark, **GPT-5 (2025-08-07)** achieves a **24.34% pass@1**, significantly outperforming other models, demonstrating the benchmark’s difficulty and discriminative power. Fine-tuning experiments on the multilingual SWE-bench benchmark further verify the value of the generated data. Overall, the paper’s objective is practically meaningful; however, it suffers from **limited novelty, missing methodological details, insufficient experimental validation, and noticeable writing quality issues**

### Strengths
1. This paper proposes a practical and fully automated framework for generating high-fidelity, repository-level coding tasks from open-source GitHub projects, addressing key challenges in evaluating large language models for software engineering.

2. In terms of data scale and coverage, it includes **5,909 tasks from 3,154 repositories**, and fine-tuning results demonstrate the value of the generated trajectories.

### Weaknesses
**Low Novelty:** The main improvement of Auto-SWE-Bench lies in automating SWE-Smith’s process, with only minor modifications. The work lacks substantial innovation. 

**Lack of Methodological Details:** The authors did not disclose critical experimental details, such as the prompt templates used at each stage and fine-tuning parameter configurations. 

**Unclear Writing and Presentation:** The paper lacks clear illustrations or diagrams. Some experimental results should be presented in tables for clarity, making the paper difficult to follow. 

**Lack of Baseline and Model Comparison:** In Table 1, the authors did not include systematic comparisons with strong baselines such as SWE-Fixer-72B, SWE-Gym-32B, and SWE-Agent-LM-32B. 

**Lack of Ablation Studies:** The paper does not include systematic ablation experiments, for example, on the *Self-Correcting Iterative Refinement Loop* and related components. 

**Lack of Task Characteristics and Cost Analysis:** The paper does not report the structural distribution or difficulty characteristics of task instances (e.g., #Lines edited, #Files edited, #Functions edited). It also lacks cost analysis, including the computational resources required at each stage. 

**Writing and Formatting Errors:** There is a typo at line 126, missing citations at lines 298 and 304, and the layout of Table 2 is not well formatted. Also, the titles of paper are inconsistent.

### Questions
1.Could the authors further clarify the conceptual and methodological differences between **SWE-Bench Atlas** and **SWE-Smith**, beyond the automation improvements? 

2.Please provide a detailed **cost analysis** of the entire automation process, including computational resource usage and time overhead at each stage. It is also recommended to include **prompt templates**, parameter configurations.

3.comparisons with baselines such as **SWE-Fixer-72B**, **SWE-Gym-32B**, and **SWE-Agent-LM-32B** to improve clarity and reproducibility. 

4.In **Section 3.1 (Stage 1: Programmatic Sourcing)**, the paper does not explicitly state that candidate tasks should be selected only when the corresponding GitHub issues are resolved **and** the commits modify test files in the repository — which would indicate that the user likely wrote or updated tests to verify the issue’s fix.

5.Could the authors provide more detailed **case studies** and examples of **challenging cases**?

### Soundness
3

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper introduces **SWE-Bench Atlas**, an automated framework for generating large-scale software-engineering benchmarks from open-source repositories. The system integrates six components—sourcing, agentic Dockerization, hybrid log parsing, automatic quality analysis, curation with contextual hints, and trajectory generation. It produces 5.9 K validated tasks from 3 K repositories across seven programming languages and evaluates state-of-the-art models on a 488-task subset. The goal is to provide a scalable, contamination-resistant, and continuously extendable benchmark for AI-based software-engineering agents.

### Strengths
- Addresses an important problem: the lack of scalable, dynamic SWE benchmarks beyond static datasets such as SWE-Bench and SWE-Bench Verified.
- The proposed pipeline is conceptually comprehensive, covering sourcing, environment setup, and trajectory curation.
- The agentic Dockerization and hybrid log-parsing components are practical and potentially reusable by future research.
- The dataset scale and diversity are impressive, and the benchmark results confirm strong task difficulty and clear model separation.

### Weaknesses
- **Presentation quality is poor.**
The paper reads like a technical report rather than a polished conference paper—verbose descriptions, inconsistent formatting, missing figures. This seriously hurts readability.

- **Weak novelty.**
Most components follow existing procedural automation ideas. The “agentic” framing is overstated; the system is largely a scripted pipeline rather than a genuine multi-agent process.

- **Related work gap.** 
The paper overlooks SWE-Flow (ICML 2025), an earlier work with a similar automated SWE data-generation pipeline. This omission undermines the claimed novelty.

### Questions
N/A

### Soundness
3

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
5

---

## Human Reviewer 4

### Summary
This paper introduces SWE-Bench Atlas, an automated framework for the large-scale generation of software engineering benchmark tasks from open-source GitHub projects. The authors claim the framework addresses limitations of existing benchmarks like SWE-bench—namely scalability, data contamination, diversity, and environment reproducibility—through a six-stage automated pipeline. Using this framework, they generated a dataset of 5,909 instances, evaluated leading LLMs on a 488-task subset, and conducted a fine-tuning experiment to show that the generated data improves model performance on other benchmarks.

### Strengths
1. Significance of the Problem: The paper addresses a critical and timely research problem: the scarcity of scalable, high-fidelity, and contamination-free software engineering benchmarks for evaluating the code generation capabilities of Large Language Models.

2. Substantial Engineering Effort: The authors demonstrate considerable technical skill through the development of a complex, multi-stage automated pipeline. The successful integration of diverse components—from data collection and environment creation to automated quality control—represents a significant engineering achievement.

3. Potential Contribution to the Community: The commitment to release a public subset of 488 tasks is a valuable contribution. If realized, this dataset will serve as a novel and important evaluation resource for the research community.

### Weaknesses
Despite its ambitious goals, the paper suffers from severe weaknesses in novelty, experimental validation, and presentation. Its contribution is thus highly limited and falls significantly short of the acceptance standards for a top-tier venue like ICLR.

*   **Significant Lack of Novelty:** The paper's primary contribution is an engineering assembly of existing techniques rather than a fundamental methodological innovation.
    *   **Agentic Dockerization:** The proposed method heavily overlaps with recent work (e.g., *SetUpAgent*) without clearly articulating its unique contributions or substantive advantages.
    *   **LLM Judge:** Using LLMs for quality assessment is now a common paradigm. Its application here is a straightforward extension and lacks methodological novelty.
    *   **Trajectory Curation:** This component appears to be a direct application of an existing tool (*SWE-Agent*) rather than novel research.
    *   **Overall:** The work reads more like a complex engineering report than a research paper with significant scientific insight. It combines modules without demonstrating any synergistic effect ("1+1>2").

*   **Insufficient and Poorly Presented Experiments:** The experimental validation is weak and fails to support the paper's claims.
    *   **Unconvincing Fine-tuning Results:** The key results in Table 1, meant to demonstrate the data's value, show only marginal gains. These improvements are presented without any statistical significance analysis (e.g., confidence intervals or standard deviations), making them unconvincing.
    *   **Superficial Benchmarking:** The results are limited to raw `pass@1` scores. The paper lacks any error analysis, discussion of failure modes, or performance breakdown across different task types, which is essential for a benchmark paper.
    *   **Unsubstantiated Diversity Claims:** The claim of dataset "diversity" is supported only by the number of repositories. Deeper analysis of task complexity, code churn, or problem type distribution is critically missing.

*   **Poor Writing Quality and Lack of Rigor:** The paper is difficult to follow and lacks scientific precision.
    *   **Poor Readability:** The complete absence of figures or diagrams to illustrate the complex six-stage pipeline is unacceptable. It forces readers to guess the system's architecture from dense text.
    *   **Overly Promotional Tone:** The manuscript is filled with grandiose claims ("paradigm shift," "holistic") that are not substantiated by evidence.
    *   **Poor Structure:** Critical information, including the main related work comparison (Table 2) and full leaderboards, is relegated to the appendix. This leaves the core arguments in the main paper incomplete and unsupported.

### Questions
N/A

### Soundness
2

### Presentation
1

### Contribution
1

### Rating
0

### Confidence
5