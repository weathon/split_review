# LLM-Assisted Static Analysis for Detecting Security Vulnerabilities

- Decision: Accept
- Scores: 3, 6, 6, 8

## Abstract
Software is prone to security vulnerabilities. 
Program analysis tools to detect them have limited effectiveness in practice due to their reliance on human labeled specifications. 
Large language models (or LLMs) have shown impressive code generation capabilities but they cannot do complex reasoning over code to detect such vulnerabilities especially since this task requires whole-repository analysis.
We propose \tool, a neuro-symbolic approach that systematically combines LLMs with static analysis to perform whole-repository reasoning for security vulnerability detection.
Specifically, \tool leverages LLMs to infer taint specifications and perform contextual analysis, alleviating needs for human specifications and inspection.
For evaluation, we curate a new dataset, \benchmark, comprising 120 manually validated security vulnerabilities in real-world Java projects.
A state-of-the-art static analysis tool CodeQL detects only 27 of these vulnerabilities whereas \tool with GPT-4 detects 55 ($+28$) and improves upon CodeQL's average false discovery rate by 5\% points.
Furthermore, IRIS identifies 6 previously unknown vulnerabilities which cannot be found by existing tools.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a hybrid approach that combines static analysis (CodeQL) with LLMs to detect vulnerabilities. Specifically, IRIS uses LLMs to find taint specification of external APIs and use CodeQL to compute paths as context and feed into the prompts to LLMs. The authors evaluated their work on 120 manually  validated Java vulnerabilities. The results show that their approach can detect 56 vulnerabilities, 28 more than the ones reported by CodeQL

### Strengths
+ IRIS demonstrated the improved results over CodeQL 
+ IRIS found unknown vulnerabilities 
+ This paper is well written and contains details.
+ It's interesting to learn that the LLMs can infer taint specifications with 70% accuracy

### Weaknesses
Soundness:
This paper contains a problematic evaluation:
- The authors curated 120 examples. All of them are vulnerable labels. The results focus on vulnerabilities detected. The false positive rates are not evaluated?
- There are many vulnerability datasets available, such as PrimeVul, Sven datasets. Why do you not run your tool on other datasets?
- The baselines of CodeQL (QL), Infer (Infer), Spotbugs (SB), and Snyk are all static analysis tools?  Should you also compare any AI based approaches? e.g., what about feeding the entire function into a prompt and see how LLMs perform?
- only 5 models are experimented

Presentation:
- How subset of paths are selected when paths are too long for the prompt? It's not clearly presented
- We typically don't call such an approach neural-symbolic

Contribution:
- This paper makes incremental contributions
(1) Using LLMs for getting taint information. Typically in static analysis, we provide a list of taint APIs, it can be done precisely by the domain experts.
(2) Using paths reported by CodeQL as context when prompting LLM. There have been work that uses output of the static analysis tools like infer as prompts

### Questions
-  How are the subset of paths selected when paths are too long?
-  There are many vulnerability datasets available, such as PrimeVul, Sven datasets. Why do you not run your tool on these datasets?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposed IRIS, a neuro-symbolic approach that leverages LLMs to infer taint specifications and perform contextual analysis for security vulnerability detection in combination with static analysis tools like CodeQL. The evaluation comes with a newly curated dataset CWE-Bench-Java, comprising 120 manually validated security vulnerabilities in real-world Java projects. The experiment result shows that IRIS with GPT-4 detects 28 more vulnerabilities than CodeQL alone.

### Strengths
1. Originality: The paper proposed a new method that combined LLM with static analysis tool CodeQL to infer taint specifications and perform contextual analysis.
2. Quality: The experiment shows huge improvement on bug detection effectiveness
3. Clarity: The paper is well-written and implementation details like prompts and QL scripts are provided in appendix.
4. Significance: The paper addressed challenges of static taint analysis like false negatives due to missing taint specifications, contributing to the field in the long term.

### Weaknesses
1. The paper doesn't address potential data leakage and memorization by LLMs, since they are asked to infer sources/taints purely based on method name and signature instead of implementation. The method may work well for projects where the APIs (sources and taints) are already publicly known, but not for private projects or less well-known projects. 
2. The comparison with baseline CodeQL may not be fair enough as the LLM-based method will always have advantages on bug detection numbers due to more source/sinks. It might be more convincing if LLM-based approach can be compared with heuristics shown in prompts like "Taint source APIs usually return strings or custom object types." to see that LLM's advantage against heuristics like name and signature type matching.

### Questions
1. As mentioned in the limitation section, "IRIS makes numerous calls to LLMs for specification inference and filtering false positives, increasing the potential cost of analysis" I would like to know the actual cost of LLM call for IRIS on CWE-Bench-Java in total and on average.

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
This paper proposes using a neuro-symbolic approach, combining LLM and static taint analysis tool CodeQL, for whole-repository level, Java vulnerability detection. The authors curate CWE-Bench-Java, a vulnerability dataset of Java projects. Evaluation results show that IRIS is able to detect significantly more vulnerabilities compared with the baselines and are able to uncover previously unknown vulnerabilities.

### Strengths
- IRIS includes a LLM filtering step via contextual analysis, as the use of LLM for sources and sinks predictions may incur many spurious alerts. The ablation study shows that this step can greatly improve Avg F1 score for larger models.
- IRIS significantly outperforms prior methods in terms of the number of vulnerabilities detected and is able to uncover previously unknown vulnerability.

- IRIS focus on project-level vulnerability detection on CWE-Bench-Java, which is inherently a challenging task as the projects are of large sizes.

### Weaknesses
 - The false discovery rate of IRIS is very high (~90%) and the F1 score is low (around 0.1). The Avg FDR and Avg F1 scores for IRIS + GPT-3.5 / Lamma-3 / DeepSeekCoder are either worse or comparable to the CodeQL baseline.
  - What are the causes of the undetected vulnerabilities (among the 120)?
- A more rigorous discussion or evaluation should be conducted beyond random sampling of 50 alarms to argue that the actual false discovery rate should be much lower (line 397-399).
- Models other than GPT-4 are over-approximating the specifications (Figure 7). The paper would benefit more from method designs to improve LLM-inferred specifications to lower the false discovery rate to save manual efforts of triaging through the alerts.

- Presentation
  - Line 377: "IRIS's superior performance compared to CodeQL:" Should be more careful with the language here, as Table 1 doesn't show its superiority on Avg FDR and F1 metrics.

### Questions
1. Can you add related works where the vulnerability is considered detected when the vulnerable path passes through some crucial program points (line 297-298)?
2. Can you explain the design choices in Section 3? It seems to me that these may affect LLM's taints specification inference and predictions of false positives.
   1. Few-shot (3-shot) for external APIs and zero-shot for internal APIs: does the number of shots affect the precision of LLM-inferred specifications?
   2. $\pm$ 5 lines surrounding the source and sink location (line 261), 
   3. A subset of nodes (line 263 - 264): how are they selected?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper claims to be the first work to combine LLMs with static analysis to detect application-level security vulnerability via whole-project analysis. They propose a contextual analysis technique with LLMs that reduces false positive alarms and minimizes the triaging effort for developers. Their insight is that encoding the code context and path-sensitive information in the prompt elicits more reliable reasoning from LLMs. They curated a benchmarking dataset of real-world JAVA programs that contain 120 security vulnerabilities. They evaluate IRIS on the Java dataset using eight diverse open- and closed-source LLMs. Doing an extensive evaluation, they show that their method IRIS obtains the best results by detecting 55 vulnerabilities, which is 28 (103.7%) more than CodeQL, the existing best-performing static analyzer.

### Strengths
1. The paper addresses the long-standing security problem of decreasing the false positive rate of vulnerability detection while maintaining high enough accuracy.
2. They have done a thorough evaluation using both open—and close-source LLMs and different static analysis baselines, such as Facebook Infer, SpotBugs, and Snyk.
3. They introduced a new dataset with important characteristics such as containing vulnerability metadata, being compilable, demonstrating real work, and being validated.

### Weaknesses
1. Tested only on Java codebase.
2. They have excluded code written in other languages that may flow to the Java components in the project during runtime or via compilation.
3. An evaluation of how many detection misses were due to CodeQL's fault and how many were due to LLM's incorrect specification or filtering fault.

### Questions
1. They hypothesize that since LLMs are pre-trained on internet-scale data, they know about the behavior of widely used libraries and their APIs. So, can any new package or Java module not processed by the LLMs cause detection or specification generation issues?
2. I want more details on the specification tuples, such as what are all the possible values for the type of node to match in G and what is the upper bound for N from the N-tuple of F?
3. The authors mentioned including ±5 lines surrounding the exact source and sink location and the enclosing function and class. How did they come up with the "5" value? Can it be arbitrarily large, bounded by the LLM's token limitation?
4. I would like to know if, in the event that CodeQL does not detect a vulnerability even with correctly labeled specifications,will it be marked as negative? Can you give me any statistics on how many such instances there are? If I understand correctly, CodeQL is still a critical part of the vulnerability detection pipeline. LLM just ensures that the data fed into the static analyzer is of quality, and once detection is made, LLM helps weed out false positives?
5. Has it ever happened that LLM made a mistake and marked a positive case as negative even after the positive detection of a vulnerable path by CodeQL? I am trying to understand how accurate the LLM-based filtering method is and how drastic the change in explanation for detection will be based on the different specifications provided.

### Soundness
3

### Presentation
3

### Contribution
3
