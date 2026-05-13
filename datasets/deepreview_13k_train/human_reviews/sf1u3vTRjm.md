# ML-Bench: Evaluating Large Language Models for Code Generation in Repository-Level Machine Learning Tasks

- Decision: Reject
- Scores: 8, 6, 3, 6

## Abstract
Despite Large Language Models (LLMs) achieving impressive results in code generation, significant challenges remain in automated ML development, particularly in utilizing existing ML repositories effectively.
Also, recently, people have developed LLM agents that attempt to interact with repository code (e.g., resolving issues), prompting the need for end-to-end evaluations starting from environment setup to deploying the repository rather than merely generating code in already-configured environments. 
These two gaps have motivated our development of ML-Bench, a benchmark rooted in real-world ML applications that leverage existing code repositories. 
ML-Bench encompasses annotated 9,641 examples across 18 GitHub repositories, challenging LLMs to accommodate user-specified arguments and documentation intricacies effectively.
To evaluate both LLMs and agents, two setups are employed: 
ML-Bench-L for assessing LLMs' text-to-code conversion within a predefined deployment environment, and ML-Bench-A for testing autonomous agents in an end-to-end task execution within a Linux sandbox environment. 
Our findings indicate that while GPT-4o leads with a Pass@5 rate surpassing 50%, there remains significant scope for improvement, highlighted by issues such as hallucinated outputs and difficulties with bash script generation. 
Notably, in the more demanding ML-Agent-Bench, GPT-4o achieves a 76.47% success rate, reflecting the efficacy of iterative action and feedback in complex task resolution. 
Our resources, including code, data, and models, are available at \url{https://anonymous.4open.science/r/ML-Bench}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces ML-BENCH, a benchmark designed to evaluate the performance of LLMs and agents on machine learning tasks at the repository level. The benchmark addresses two key gaps: LLMs' struggle with repository-scale code understanding and the need for end-to-end evaluations from environment setup to deployment. ML-BENCH includes 9,641 examples across 18 GitHub repositories, challenging LLMs to handle user-specified arguments and documents effectively.

### Strengths
1. Comprehensive Benchmarks: The paper presents ML-BENCH, which offers a comprehensive set of benchmarks that cover a wide range of tasks from different GitHub repositories. This comprehensiveness is crucial as it allows for the evaluation of LLMs and agents across various real-world scenarios, providing a more accurate assessment of their capabilities.

2. Thorough Experimental Analysis: The paper includes a thorough experimental analysis with two main setups—ML-LLM-BENCH and ML-AGENT-BENCH—that test different aspects of LLMs and agents. The detailed analysis and the use of various models to assess performance provide a robust understanding of the current state and limitations of LLMs in handling complex repository-level tasks.

3. Reproducibility and Sandbox Environment: The paper offers a reproducible sandbox environment, which is essential for the research community. By providing a secure Linux sandbox environment where agents can execute commands and code blocks, the paper enables other researchers to replicate the experiments and build upon the findings. This not only aids in verifying the results but also in extending the research to explore new models and potential improvements.

Consequently, this paper is of high quality and would be interesting to appear in a top-tier conference.

### Weaknesses
1. Data Leakage Concerns: Although the paper addresses the data leakage issue in Section 5.1, their efforts to verify the type and parameters of the generated results against user instructions do not fully mitigate this problem. Given that this benchmark is based on repositories from GitHub, and considering that nearly all large language models (LLMs) utilize data from GitHub, the static nature of these benchmarks may render this work less effective in the future. Since the paper has already implemented a sandbox environment for executing these repositories, a suggestion is to make the benchmark dynamic, similar to what LiveCodeBench has done. This could be achieved by regularly updating the benchmark with new repositories, thereby mitigating data leakage issues more effectively.

2. Enhanced Experimental Settings: To provide a clearer experimental analysis, it would be beneficial to include two additional experimental settings. In Table 4, the paper compares different levels of context for generation, similar to the approach in RepoBench. To enhance this analysis, experiments should be conducted with a more advanced retriever, such as UniXCoder, and without any extra context. The first addition would help determine whether a better retriever can lead to improved performance, while the second would allow for a deeper analysis of data leakage issues.

3. Table 4 lacks the latest SOTA LLMs, such as Claude-3.5-Sonnet and CodeQwen2.5. These models have demonstrated superior coding capabilities, both in closed and open-source environments. It would be insightful to evaluate whether these advanced LLMs could achieve superior performance on this benchmark.

### Questions
Check Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
ML-BENCH introduces a novel benchmark for evaluating LLMs and AI agents on repository-level machine learning tasks. Unlike previous benchmarks focused on function-level code generation, ML-BENCH tests models' ability to understand entire codebases and execute end-to-end ML workflows. The benchmark comprises two components: ML-LLM-BENCH for evaluating code generation in pre-configured environments, and ML-AGENT-BENCH for testing end-to-end task execution including environment setup. The evaluation covered 9,641 examples across 18 repositories, with GPT-4o achieving the best performance.

### Strengths
1. The paper presents a comprehensive dataset comprising 9,641 examples with meticulous manual annotations, accompanied by details of annotation process.
2. Unlike many benchmark papers, ML-BENCH also provides training data.
3. The experiments are generally solid, with good analysis.

### Weaknesses
- The model selection is my first concern, particularly the absence of Claude-3.5 (which I think was available for ICLR's timeline), while including numerous smaller open-source models that are less interesting (though I know authors want to include fine-tuning) - as a benchmark paper, I think authors should prioritize showcasing the performance gap between the best available open-source and closed-source models.
- The limitation to "README-documented tasks" potentially undermines the paper's claimed contribution to "repository-code understanding," raising questions about whether the benchmark truly tests code comprehension capabilities. The tasks might be solvable by simply following instructions in the README without requiring a deeper understanding of the codebase's architecture, dependencies, or complex logic.
- The benchmark seems heavily skewed towards bash script tasks, which sounds a imbalance for me. This over-reliance on bash scripts might not fully capture the complexities of machine learning workflows, which often involve intricate Python code, custom data loaders, and model-specific configurations. It raises concerns about the benchmark's ability to evaluate models on core ML tasks.
- While the authors acknowledge data leakage issues, the discussion is really short - I do not really understand the authors' solution. The paper lacks a detailed explanation of how the benchmark mitigates data leakage, especially given that many models are pre-trained on vast amounts of code data. The absence of a clear methodology for preventing memorization of repository-specific information is a significant concern.

### Questions
- What's the performance of Llama-3.1 (70B, 405B), Deepseek-v2, etc..?
- What proportion of tasks truly require deep code understanding versus simple README/Document comprehension? 
- How exactly does the proposed method address data leakage issues?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
ML-Bench introduces a benchmark in two parts for evaluating language models' ability to work with machine learning repositories: ML-LLM-Bench and ML-Agent-Bench. ML-LLM-Bench assesses LLMs' capability to generate executable commands with appropriate arguments by understanding repository-wide context, documentation, and cross-file dependencies within a pre-configured environment. ML-Agent-Bench goes further by evaluating autonomous agents on end-to-end ML (machine learning) tasks, requiring them to perform environment setup, dependency management, and dataset preparation before executing the desired ML commands. The benchmarks highlight the importance of comprehensive repo understanding and environment management in realistic ML scenarios.

### Strengths
- The full end-to-end task shows promise and contains novel elements, though current agent performance appears quite strong already.
- The dataset components and analyses across different settings have potential value, but their presentation lacks clarity in illuminating task challenges and model behavior patterns.

### Weaknesses
 - The ML-Agent-Bench sub-task name is nearly indistinguishable from MLAgentBench, a well-known work in the same field. This creates unnecessary confusion and should be reconsidered.
- The first novelty claim (line 90) appears inaccurate. Both RepoBench and SWE-bench already provide similar repository-level coding evaluations, which have become common since these benchmarks were released last year. While this may be a feature of the benchmark, it does not constitute a novel contribution. Specifically, the claim of evaluating end-to-end ML workflows is not entirely novel, as existing benchmarks also involve multi-step processes, albeit perhaps with less emphasis on environment setup. The distinction needs to be more clearly articulated.
- The anonymized repository and supplementary materials lack a complete dataset. For instance, the specified Hugging Face dataset "XXXX-1/ml-bench" is not accessible, preventing thorough dataset inspection. This lack of access hinders the ability to verify the dataset's quality and the claims made about it.
- The paper's methodology and analysis suffer from significant presentation issues. Many sections are difficult to follow and require excessive effort to comprehend. The organization needs substantial improvement for clarity. Additionally, several paragraphs contain unnecessary details that detract from the main text. For example, the file and code symbol notations introduced in Section 2.1 are never used beyond their initial definition. The description of the error analysis is also vague, lacking sufficient detail on how errors are categorized and quantified.


### Questions
- If I understand correctly, there are 9 core tasks per repo on average (with templates / argument selection expanding this for diversity). Then please clarify: does the test-train split differentiate between tasks, or is it sampled randomly and uniformly? If uniformly, wouldn't test instances closely mirror training instances? This raises questions about why fine-tuned models show such similar performance across ID and OOD test splits.
- Section 5.1's description of data leakage mitigation needs clarification. The current explanation doesn't adequately explain how data leakage is measured or mitigated.
- The methodology behind the Error Analysis requires clarification. If it was conducted using an LM, please provide details about the model and prompts used.
- Am I mistaken or does Figure 5 appear to show an agent's execution log rather than an evaluation runtime as suggested by the caption?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents ML-Bench as a new repository-level software engineering benchmark that targets ML applications. One could see ML-Bench as an ML counterpart for SWE-Bench. For example, ML-Bench provides two interfaces for both LLM-based text-to-code evaluation (ML-LLM-Bench) and sandboxes (ML-Agent-Bench) that can provide feedback for agent frameworks to evaluate their real-world problem-solving abilities.

### Strengths
1. The writing is easy to follow with self-explanatory illustrations. 
2. One difference between setting agents for ML applications and general software applications is that ML applications usually require comprehensive dependencies and dataset preparation; ML-Bench puts some effort into this part to highlight the necessity to build benchmarks towards ML applications. 
3. According to L264 to L269, ML-Bench has in-distribution (ID) and out-of-distributions (OOD) evaluation cases. The results show that even ID fine-tuning can not bring statistically obvious improvement for some models.

### Weaknesses
1. Missing details about Success Rate evaluation in ML-Agent-Bench. I understand it should be up to the specific agent framework to evaluate whether an instance is solved, but how do you define if an agent execution fulfills user requirements, especially for ML applications? Unlike the general SWE domain, ML repositories are usually not accompanied by heavy unit tests, and even if they do, due to the stochastic nature of ML applications, it's hard to say an instance is not solved merely because the final output does not match the pre-defined results.

2. I see the authors have extensively discussed the difference between SWE-Bench and ML-Bench. Still, I do not agree with some of the claims in Appendix B.1. For example, the c) claims repository understanding, which is also the focus of SWE-Bench. e) It claims SWE-Bench does not "explicitly" address the documentation utilization, where I consider documentation to be easily considered pure-text code files in both agent and agent-less solutions.

### Questions
Refer to the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3
