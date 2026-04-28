# To Err is Machine: Vulnerability Detection Challenges LLM Reasoning

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 6

## Abstract
In this paper, we present a challenging code reasoning task: vulnerability detection.
Large Language Models (LLMs) have shown promising results in natural-language
and math reasoning, but state-of-the-art (SOTA) models reported only 54.5%
Balanced Accuracy in our vulnerability detection evaluation, even those models
pre-trained on large amounts of source code. Our error analysis on LLM responses
shows that the models struggle to reason about the code semantics relevant to
identifying vulnerabilities, especially subtle semantic differences caused by small
textual changes. We explored prominent models and training settings to understand
their effects on vulnerability detection performance — including better prompts,
larger models, more pre-training data, and fine-tuning — but none led to significant
improvements. This raises the question of whether simply scaling training data and
model size will allow us to “solve” complex code reasoning tasks like vulnerability
detection, or if a fundamental shift in modeling and training techniques is required.
We also explored adding domain knowledge to prompts; although it helped certain
models understand some code semantics, vulnerability detection requires multi-
step reasoning, and these models still failed in steps, such as reasoning about
variable relations. Our results suggest that new models, new training methods, or
more execution-specific pretraining data may be needed to conquer vulnerability
detection. We speculate that auto-regressive pre-training on source code may not
effectively extract code semantics, especially on the current pretraining mixtures,
in which execution data is scarce. Success on vulnerability detection as a code
reasoning task can benefit many areas of software engineering such as debugging,
test input generation, and program repair. Our code and data are available at
https://figshare.com/s/78fe02e56e09ec49300b.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper evaluates LLMs capability in detecting Vulnerabilities in Code. It evaluates LLMs capabilities from various aspects, for example studying whether the LLM size and training process has any effect on its capability in detecting vulnerable code patterns.

### Strengths
- The paper is targeting an important problem. With LLMs being readily available for various AI for Code scenarios, whether they are a good tool to use for vulnerability detection is an important problem.
- The paper targets a reasonable number of LLMs for evaluation.
- The paper first establishes that LLMs are not good at vulnerability detection, then it tries to understand where the LLMS fail, whether its localization or reasoning. 
- The paper also analyzes whether the LLM size and training routine, as well as giving additional information from static analyzers matters in vulnerability detection.

### Weaknesses
 - The paper concludes that LLMs are not great at vulnerability detection based on a study on SVEN, targeting C/C++ issues. While C/C++ is one of the important languages when it comes to vulnerability detection, previous research shows that even in code generation tasks LLMs perform better in more common languages such as python and javascript than C/C++. I'm not sure that for us to claim that LLMs are  in capable of detecting vulnerabilities, is it enough to look into C/C++ only. I expect that LLMs would perform better in easier to interpret languages such as JavaScript or on vulnerability patterns that are easier to catch such as "Hardcoded credentials.". Overall, a more fine-grained breakdown on the language and type of vulnerability is needed to better understand where the LLMs can be helpful and where they cannot be helpful.
- While I find the comprehensive study on different LLMs ability to find vulnerabilities insightful, none of the follow up experiments where able to point to a particular aspect that would explain why LLMs may not perform well on detecting certain vulnerabilities. It would be great to have some suggestions/insights on training routines, fine-tuning datasets, etc that can help improve LLMs performance.

### Questions
- Do the authors have a breakdown of their results in terms of vulnerability type?
- Have they repeated this experiment on newer LLMs such as Sonnet 3.5, o1, and gpt4o? If they have seen reasoning issues it would be interesting to see o1 and sonnet 3.5 results in particular.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper provides an in-depth analysis of LLMs' limitations in vulnerability detection, identifying the complexity of the task and the need for future work to enhance LLM’s code reasoning abilities. It further demonstrates that common strategies for enhancing LLM performance—like increasing model size, expanding training data, fine-tuning, and leveraging domain knowledge —do not significantly improve their vulnerability detection capabilities.

### Strengths
- The paper studies an interesting problem and pinpoints a critical challenge with great potential.
- It provides a comprehensive analysis based on the recent LLM families and demonstrates that common strategies don’t enhance LLM performance.

### Weaknesses
 - To my understanding, the paper pinpoints the challenge of vulnerability detection across LLMs but doesn’t clearly articulate how future work could leverage the findings presented here to further improve its performance. The main contributions aren’t clearly specified.
- The additional value of breaking down different vulnerability issues into three stages is somewhat unclear and lacks evaluation. And also why do LLMs perform notably worse on tasks involving NULL checks compared to other scenarios? Offering specific suggestions for overcoming these limitations would strengthen the paper.
- The paper can benefit from extending its fine-tuning experiments beyond StarCoder2, especially by fine-tuning the SVEN and PrimeVul datasets with a broader range of LLMs.

### Questions
1. Can you expand on the evaluation section as discussed above?
2. How does this work compare with other recent studies on vulnerability detection, such as Steenhoek et al. (2024)?

[1] Benjamin Steenhoek and Md Mahbubur Rahman and Monoshi Kumar Roy and Mirza Sanjida Alam and Earl T. Barr and Wei Le: A Comprehensive Study of the Capabilities of Large Language Models for Vulnerability Detection,CoRR, 2024


Minor comments:
Can you expand on the experimental setup in the Secion 3? It isn’t clear to me the evaluation methods for evaluating understanding and localizing errors.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the limitations of large language models (LLMs) in performing vulnerability detection tasks, highlighting the distinct reasoning and code understanding required for effective identification of vulnerabilities. By evaluating 14 state-of-the-art LLMs across various prompt strategies on the SVEN dataset, the authors demonstrate that LLMs generally underperform in this area, particularly with tasks requiring deep code semantics, such as handling pointer operations and bounds checks. The paper offers a comprehensive breakdown of the common failure patterns observed, emphasizing the challenges LLMs face in reliably detecting code vulnerabilities and identifying specific reasoning deficiencies in current models.

### Strengths
Major Strengths

1. Solid study on vulnerability detection limitations in LLMs: This paper presents a rigorous analysis of LLM performance in vulnerability detection, specifically on tasks requiring nuanced code reasoning. It identifies critical failure modes, such as incorrect handling of bounds checks and null-pointer dereferences. The authors highlight these challenges through detailed case studies, including examples like the pointer dereference and buffer overflow vulnerabilities, where models fail to correctly interpret safety checks or arithmetic constraints (e.g., the issues shown in Figures 1A and 1B).

2. Comprehensive evaluation on LLM-based vulnerability detection: The paper evaluates 14 models on the SVEN dataset[1], comparing baseline and advanced prompts like Chain-of-Thought from CVE (CoT-CVE) and static analysis-derived prompts (CoT-StaticAnalysis). The extensive prompt strategy testing, including contrastive pairs and static analysis paths, shows the impacts of these prompts on model performance. Despite attempts with diverse prompts, none of the strategies led to significant improvements beyond the random-guessing baseline, reinforcing the paper’s argument that current LLM capabilities are inadequate for complex vulnerability reasoning

3. Insightful analysis of failure patterns: The paper categorizes and quantifies specific recurring errors, including failures in bounds checks (50% of bounds-related errors) and misinterpretations of pointer or arithmetic operations. This error breakdown, as detailed in Table 3, clarifies the specific reasoning steps where models consistently fail, such as misunderstanding variable constraints and execution order. These insights offer concrete areas for improvement, particularly in recognizing key programming structures relevant to security​.

Minor Strengths

1. Excellent paper presentation: The paper is organized with logical sections and visual aids, including error distribution charts (Figure 3) and model performance comparisons (Figure 2), that help to convey complex results clearly. The figures, such as those highlighting prompt performance and specific error categories, provide readers with a quick understanding of each model’s strengths and weaknesses on vulnerability tasks​.

2. Methodical approach to prompt strategy comparisons: By systematically testing and comparing various prompt designs—including zero-shot, n-shot, CoT-CVE, and CoT-StaticAnalysis—the paper provides a nuanced view of how different prompt styles affect vulnerability detection performance. This comparison offers valuable insights into prompt engineering, especially as it reveals that even advanced prompts based on structured data (e.g., static analysis proofs) fail to achieve consistent improvements​.

3. Detailed manual inspection of model errors: The paper’s manual review of 300 LLM-generated responses allowed for a deeper understanding of specific errors that automated metrics might miss. This qualitative analysis shows that LLMs frequently misinterpret pointer safety and logical implications across multiple steps of reasoning. The authors provide concrete examples of where models misjudge safe versus vulnerable code (such as failing to recognize bounds checks on pointer dereferences), giving a more rounded view of LLM limitations in this domain
 
[1] He J, Vechev M. Large language models for code: Security hardening and adversarial testing[C]//Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security. 2023: 1865-1879.

### Weaknesses
Major Weaknesses

1. Oversimplified in-context learning: Although the authors assess several in-context learning techniques, they do not fully explore the design rationales for each prompt or the limitations that different choices present. For example, in the CoT-StaticAnalysis prompt, the inclusion of static analysis paths from the D2A dataset was intended to help models follow logical steps, but it lacks a discussion on why certain paths were prioritized over others. Adding such detail would clarify prompt-specific limitations and help in identifying where these prompts fell short for vulnerability detection. The paper also does not discuss the impact of different example selection strategies, such as using more diverse examples or examples that specifically target the identified failure modes of the LLMs.

2. Limited exploration of RAG-based systems for code-specific semantics: While the paper mentions that Retrieval-Augmented Generation (RAG) systems could benefit vulnerability detection, it does not explore how RAG might be applied to enhance the model’s understanding of complex code reasoning tasks. Incorporating RAG systems could allow models to retrieve relevant code snippets or documentation, potentially aiding in cases where semantic context (e.g., specific variable usage patterns or documentation on safe handling of pointers) is essential for accurate reasoning[1-2]. Exploring this could offer a deeper understanding of model limitations and point to meaningful directions for future work​.

Minor Weaknesses

1. Sampling may be biased: The manual inspection of 300 samples may introduce bias, as the authors do not fully detail the criteria used to select these samples or ensure diversity. Explaining how they selected these samples (e.g., random selection, specific focus on certain vulnerability types) would strengthen the credibility of their findings and ensure that the review represents the dataset as a whole.

2. Vulnerability types are limited: The study primarily examines vulnerabilities related to bounds checks, null pointers, and pointer handling, which limits the generalizability of the findings. Including additional vulnerability types, such as integer overflow (as shown in the simple example from CWE in Figure 10), would provide a broader view of LLM limitations in software security tasks.

3. Absence of advanced evaluation metrics: While the Balanced Accuracy metric is helpful in assessing basic performance, it does not capture important aspects like semantic accuracy or reasoning consistency. Introducing metrics that focus on these qualities would provide a more comprehensive evaluation of model performance on tasks requiring deep semantic understanding, such as detecting specific security flaws in code​.

### Questions
Overall, this work demonstrates a professional understanding of LLM research for vulnerability detection, offering meaningful insights into the limitations of current models and practical implications for their use in code security. I am ready to defend my assessment and may consider increasing my score depending on responses to the following questions.

1. Could the authors provide further justification for their chosen in-context learning design, including any tuning or design choices made for specific prompts?

2. What limitations did the authors encounter when expanding the scope of vulnerabilities? How could future work address this limitation?

3. Did the authors consider additional metrics for evaluating semantic accuracy or reasoning consistency in model responses?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors performed an empirical study of using LLMs for software vulnerability detection. The authors formulated vulnerability detection in 3 steps: locating potentially vulnerable statements, understanding vulnerability-related features, and predict the final vulnerability label with multi-step reasoning. The authors conducted experiments on the SVEN vulnerability dataset with LLMs under basic and COT prompts. From the results, the authors find that existing LLMs cannot effectively detect vulnerabilities, achieving results similar to random guesses. Moreover, scaling up model parameters, fine-tuning with domain-specific data, and COT prompting do not significantly improve model performances.

### Strengths
+: The paper points out that vulnerability detection is a challenging task for LLMs and has not been successfully addressed by existing models. This introduces new research opportunities in both software engineering and LLM.

+: The authors defined a three-step reasoning framework for better analysis in LLMs for vulnerability detection.

### Weaknesses
 -: In section 2, the authors adopted the BigVul and D2A datasets for building prompts. However, due to a previous study [1], these datasets have high noise rates. The authors should ensure the correctness of these generated prompts.

-: The experiments should contain some of the newest LLMs, e.g., GPT-4o-mini and Llama 3.1.

-: The authors pointed out the difficulties of vulnerability detection using LLMs. Perhaps it is also better to discuss possible solutions to these difficulties.

### Questions
- The authors mentioned the newest PrimeVul dataset, and used it for fine-tuning. So why do the authors used the SVEN dataset for evaluation instead?

- In section 3, how are the 300 manually inspected samples selected?

- In section 3.3, the authors used the COT-annotation prompts (with static analysis) to provide additional knowledge. How is the COT-annotation prompt different from other prompts in section 2, especially the COT-StaticAnalysis prompt?

### Soundness
2

### Presentation
3

### Contribution
2
