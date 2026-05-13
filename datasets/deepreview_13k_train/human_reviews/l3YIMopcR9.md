# VersiCode: Towards Version-controllable Code Generation

- Decision: Reject
- Scores: 6, 5, 6, 6, 3

## Abstract
Large Language Models (LLMs) have made tremendous strides in code generation, but existing research fails to account for the dynamic nature of software development, marked by frequent library updates. 
This gap significantly limits LLMs' deployment in realistic settings. 
In this paper, we propose two novel tasks aimed at bridging this gap: version-specific code completion (VSCC) and version-aware code migration (VACM). 
In conjunction, we introduce VersiCode, a comprehensive Python dataset specifically designed to evaluate LLMs on these two tasks, together with a novel evaluation metric, Critical Diff Check (CDC@1), which assesses code generation against evolving API requirements. 
We conduct an extensive evaluation on VersiCode, which reveals that version-controllable code generation is indeed a significant challenge, even for GPT-4o and other strong frontier models. 
We believe the novel tasks, dataset and metric open up a new, important research direction that will further enhance LLMs' real-world applicability. 
The code and resources can be found at
\url{https://wutong8023.site/VersiCode/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Despite current LLMs' remarkable advances in code generation tasks, they are typically trained and evaluated using static benchmarks such as HumanEval and MBPP. However, real-world software development is dynamic, with frequent library updates and API changes that require version-specific code compatibility. Current benchmarks do not address these challenges, highlighting a gap between LLM evaluations and practical development needs. To bridge this gap, the paper proposes two new tasks: (i) version-specific code completion (VSCC) and version-aware code migration (VACM)—and introduce VersiCode, a comprehensive dataset covering over 300 Python libraries and 2,000 versions. Additionally, the authors present a new metric, Critical Diff Check (CDC),  to better assess LLMs' ability to handle version-specific code generation.

### Strengths
- The paper addresses a real-world software development challenge, which is largely ignored by LLM4Code literature, where frequent updates to libraries and APIs require code to be compatible with specific versions.

- It introduces two new tasks focused on code evolution: code completion and version-aware code migration. These tasks are common in real-world development, and the paper provides detailed, separate approaches for each.

- The paper presents VersiCode, a large, high-quality dataset that includes data from over 300 Python libraries across over 2,000 versions over nine years.

- The new CDC metric improves on standard code similarity checks by including essential details like API usage, parameter handling, and managing deprecated features.

### Weaknesses
 - While dealing with API evolution, the paper did not deal with more complex changes involving updates of API parameters or behaviors over time.  

- The proposed VersiCode dataset requires regular updates to remain relevant, and handling thousands of library versions could become difficult as libraries continue to evolve, which may limit long-term usefulness.

### Questions
Your work provides valuable advancements for version-aware code generation. However, handling complex API changes—such as alterations in method behaviors, parameter types, or the introduction of new functionalities—can significantly impact code compatibility and functionality. How do you plan to address these more intricate API modifications in future iterations of VersiCode and CDC? 

Additionally, what strategies are you considering to ensure that VersiCode remains up-to-date and scalable as libraries continue to evolve rapidly across different programming languages and ecosystems?

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
4

### Summary
The paper introduces VersiCode, a benchmark aimed at addressing the challenges faced by LLMs in generating version-specific code generation. It proposes two tasks: version-specific code completion (VSCC) and version-aware code migration (VACM). These tasks simulate real-world scenarios where deprecated API invocations must be updated to a newer version. The study includes a novel metric, Critical Diff Check (CDC@1), to access the code generation's adherence to version-specific requirements.

### Strengths
- Strong Insight. Capturing version dynamics is essential for effectively handling version-specific dependencies in practical software development.
- Comprehensive dataset. VersiCode covers 300 libraries over nine years, offering extensive coverage for version-specific testing and paving the way for future research in version-specific code generation and automated code migration.
- Novel metric. The CDC@k metric employs a set of hand-crafted rules to assess the similarity between API usages across different versions, enabling a more detailed, execution-free evaluation of version-specific code generation.

### Weaknesses
 - Lack of in-depth analysis. As noted in subsection 4.2, the performance of GPT-4o drops significantly without import statements, suggesting that the evaluation is heavily influenced by prompt design and provided context. A more thorough analysis on how context information, such as documentation related to added or deprecated APIs, affects performance would be beneficial. Specifically, the analysis should explore the impact of different types of contextual information, such as API documentation, code examples, and usage patterns, on the model's ability to generate version-specific code. The current evaluation seems to conflate the model's ability to leverage provided context with its inherent knowledge of API versioning.
- Misleading analysis. In subsection 5.2, the claim that "The context code in another version is still helpful, but its benefits are limited" is difficult to corroborate based on Table 1 and Table 2, as block-level code migration details are not sufficiently presented. Additionally, the statement, "There is a significant improvement across most models, except for LLaMA3-70B and GPT-4o, detailed in Appendix D.3," is puzzling, as Appendix D.3 focuses on grammar verification impacts. Clarification is needed to confirm if there was an error or oversight. The analysis lacks a clear explanation of how the different models perform on specific types of API changes (e.g., additions, deprecations, modifications). The results should be broken down by the nature of the API change to provide a more nuanced understanding of the models' capabilities and limitations.

### Questions
See above.

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
The VersiCode paper addresses the crucial gap in current LLM capabilities by focusing on version-controllable code generation, a requirement in real-world software development due to frequent updates in third-party libraries. The authors introduce two novel tasks, version-specific code completion (VSCC) and version-aware code migration (VACM), to evaluate models on handling evolving software dependencies. A new dataset, VersiCode, consisting of over 300 Python libraries and 2,000 versions, enables comprehensive testing. They also propose the Critical Diff Check (CDC) metric, which enhances traditional metrics by evaluating version-specific aspects such as API usage and parameter handling. Through testing on models like GPT-4 and LLaMA, the study reveals significant challenges in version-sensitive code generation, underscoring the need for targeted pretraining, continual learning, and refined evaluation methods to improve LLM adaptability to evolving software versions.

### Strengths
Major Strengths

1. Comprehensive Dataset and Benchmark for Version-Specific Tasks: VersiCode is an important contribution as it directly addresses the under-explored area of version-specific code generation. By including metadata such as function descriptions, code snippets, and version numbers, it enables realistic evaluations of LLM capabilities in scenarios that require adherence to specific library versions. As shown in Figure 2, VersiCode’s metadata is utilized to create multi-granularity completion tasks, demonstrating the paper’s methodological depth in representing version-sensitive contexts.

2. Introduction of the CDC Metric: The Critical Diff Check (CDC) metric provides a more detailed assessment of LLM performance by focusing on crucial factors like API usage and parameter handling. This is particularly useful for evaluating tasks where syntax alone does not suffice. Table 1 presents a comparison of CDC and other metrics across different test cases, demonstrating its close alignment with the Pass@1 score, which highlights CDC’s effectiveness as a reliable proxy for assessing version-specific correctness.

3. Insightful Evaluation on Diverse Models and Detailed Error Analysis: The authors evaluate a wide range of models, including GPT-4o and StarCoder, revealing notable performance differences across version migration scenarios. For instance, in Table 2, models are evaluated across major and minor version changes, highlighting the difficulties that LLMs face in backward compatibility. This comprehensive analysis provides valuable insights into model limitations and suggests paths for improvement.

Minor Strengths

1. Detailed Task Decomposition with Multi-Level Completion: The dataset’s structure supports token, line, and block-level completion, making VersiCode versatile and relevant for different development use cases. Figure 3 compares model performance on token-level code completion across various data sources, showcasing the dataset’s capability to test LLM adaptability to different levels of code.

2. Rigorous Evaluation Methodology: The experimental setup is clearly defined, with the authors selecting 2,000 test instances for token-level completion (Section 3.1). This careful setup enhances the credibility of the results, providing a consistent baseline against well-known datasets like HumanEval[1] and MBPP[2].

[1] Chen M, Tworek J, Jun H, et al. Evaluating large language models trained on code[J]. arXiv preprint arXiv:2107.03374, 2021.

[2] Austin J, Odena A, Nye M, et al. Program synthesis with large language models[J]. arXiv preprint arXiv:2108.07732, 2021.

### Weaknesses
Major Weaknesses

1. Lack of Implementation of Retrieval-Augmented Generation (RAG): Although the authors acknowledge the potential of RAG techniques, there is no exploration of its integration, which could have significantly enhanced LLM performance in this context. RAG could assist in real-time access to documentation or version-specific information, potentially improving accuracy on challenging cases (see Section 5.2 for model limitations in handling context). Incorporating recent works in RAG-based methodologies for code tasks, such as those explored in [1], could inspire potential enhancements.

2. Absence of Evaluation Metrics for High-Level Reasoning: While CDC is effective for syntactic and structural validation, it doesn’t capture the semantic reasoning required to fully assess code functionality in context. Including metrics that evaluate semantic coherence or logical consistency could provide a more rounded view of LLM limitations, similar to the approaches suggested in studies like [2] which focus on code understanding and error detection.

Minor Weaknesses

1. Potential Bias in Model Evaluation Sampling: Although VersiCode’s dataset is extensive, the paper does not clarify how test samples were selected, which could impact the generalizability of findings. Describing the selection process, such as prioritizing recent or frequently updated APIs, would improve the robustness of conclusions (Section 2).

2. Limited Generalization to Languages Beyond Python: VersiCode primarily targets Python libraries, despite the widespread use of other languages in development. Expanding the dataset to include JavaScript or Java, for example, could enhance the benchmark’s applicability across diverse development environments, as is common in industry setting.

### Questions
The paper makes a significant contribution to understanding the performance of LLMs on version-specific code tasks, yet certain design choices would benefit from further clarification. The following questions aim to probe areas where additional context could strengthen the work:

1. Could the authors elaborate on the rationale behind the specific criteria used for sampling instances in model evaluations?

2. Did the team consider incorporating any RAG-based methods in future work to enhance the model’s access to relevant version documentation?

3. Are there plans to extend VersiCode to support other programming languages, given the diverse needs in software development?

### Soundness
4

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
4

### Summary
The authors find that code generated by LLMs needs to target specific library versions, and this problem was ignored in previous work. They propose two new tasks, version-specific code completion, and version-aware code migration, to evaluate LLMs’ ability in version-controllable code generation. They construct a Python dataset, VersiCode, to evaluate LLMs on these two tasks. They also propose a new evaluation metric, Critical Diff Check (CDC), to assess code migration results. Evaluation results show that version-controllable code generation is a significant challenge, even for extremely powerful LLMs.

Contributions:

- They propose two novel important tasks, i.e. version-specific code completion and version-aware code migration.

- They construct a versioned dataset, VersiCode.

- They introduce a new metric, Critical Diff Check.

- Their experiments provide valuable insights and directions for future research.

### Strengths
Originality: The problem of version-controllable code generation is pretty novel. Previous research in code generation ignores that the libraries and APIs used by the generated code can evolve.

Quality: The paper constructs the first versioned code generation dataset, including version-specific code completion and version-aware code migration tasks. The authors evaluate many popular LLMs on the dataset and give valuable insights about their ability to generate version-controlled code.

Clarity: The paper clearly states the problem of version-controllable code generation, including the motivation and how existing benchmarks fail to address the challenge.

Significance: Version-controllable code generation is very important in practice. The generated code is used with specific library versions, so the code generation process must consider the library versions.

### Weaknesses
1. The only metric used in the version-aware code migration is CDC, a metric just proposed in this paper. Although in section 4, the CDC@1 is stated to align closely with pass@1, it is hard to say this new metric can serve as the only metric in code migration. The reliance on a single, novel metric, especially one not yet widely adopted or validated in the community, makes it difficult to benchmark the results against existing literature. The lack of comparison with established metrics like pass@1 raises questions about the practical significance of the reported CDC scores. It would be beneficial to see how the proposed approach performs when evaluated using more conventional metrics.

2. The paper uses “Exact Match” to mean the specified API is used in the generated code. This practice is inconsistent with other papers, where “exact match” means the generated code is the same as the oracle. This discrepancy in the definition of “Exact Match” can lead to confusion and misinterpretation of the results. The authors should clarify the definition of this metric and consider using a more appropriate term to avoid ambiguity. The current usage of “Exact Match” deviates from the standard practice in code generation literature, potentially hindering the comparability of the results.

### Questions
1. Is it possible to use more familiar and possibly more reliable metrics, like pass@1, to evaluate code migration results?

2. The paper uses “Exact Match” to mean the specified API is used in the generated code. This practice is inconsistent with other papers, where “exact match” means the generated code is the same as the oracle. I hope the authors can change the name of this metric to a more appropriate one.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work introduces a benchmark for measuring the ability of LLMs trained on code to condition their predictions on API versions. It measures both code completion and code migration performance of a wide range of models across deprecated, newly added, and consistently available API methods across a large set of projects in a new benchmark called VersiCode. It also introduces a new accuracy metric based on static analysis. Results show that more capable LLMs generally fair worse on newly added and deprecated methods than on ones that have consistently been present, while smaller models show the reverse pattern. All models show a decrease in performance for newer APIs. Most models struggle especially with code migration across major version changes.

### Strengths
This work provides a dataset that fills an important gap in code evaluations specifically, measuring the effect of API changes. The dataset it contributes is quite large and contains useful data from a variety of sources. It provides some of the first large-scale empirical evidence that LLMs perform differently on certain types of APIs, including more recent releases and deprecated ones. It presents a wide range of results.

### Weaknesses
My main concerns are around the interpretation (and significance) of the results, the clarity and soundness of the methodology, and the relevance of the contributions to this venue. I'll address these in order, followed by a list of minor issues.

**Results:** the interpretation of the results involves questionable claims in a number of places. Some of these are perhaps mostly clarity issues, while a few others seem more foundational.

An example of the latter is the comparison with HumanEval and MBPP in Fig. 3, which shows, in Fig. 3.a1, that completion accuracy is far lower on VersiCode than on the aforementioned benchmarks. The text argues that this shows "the difficulty in disambiguating and recalling version-specific library usage" (L209)  and that LLMs "struggle to deliver satisfactory results" (L232). However, self-contained functions are not a good basis of comparison for examples of real API usage. It is well-established that completing real-world code, especially function calls, is harder than code in self-contained function with detailed specifications. That is not to mention the extensive leakage concerns around the baseline, benchmark programs.

This work doesn't offer a baseline of version-agnostic API completion to compare the results on version-sensitive API completion with. The closest is the comparison in Fig. 3.b, which compares the completion quality on methods that are deprecated/added vs. ones that stay the same ("general") in the particular version used in a sample's prompt. Since unchanging APIs make up more than half the total volume of API calls (Fig. 4), it stands to reason that many of these are consistent across most/all versions of their libraries, making the "general" performance a rough approximation of the performance of models on API call completion disregarding versions. The gap between these and version-sensitive API calls is considerably smaller for the large models in this subfigure, and even inverted for the smaller ones (the explanation for which, on L248, is a bit unsatisfying as it would seem to apply to large models equally). That is, version-sensitive API calls are only slightly harder to complete (for large models) than ones that stay the same.

This combined with Fig. 4's trends suggests that the "real" effect is mostly one of frequency: older APIs and ones that do not get deprecated are used more often in typical training sets, which tend to go back to GitHub's inception, and are therefore more accurately completed. Whether there is an actual difference in performance between these three types of methods is questionable. Figure 4 shows almost indistinguishable curves for each model over time between the subfigures, although separating out "general" might show a more clear contrast. This raises strong concerns around whether there is a difference at all, or whether the differences observed in Fig. 3.b are actually caused by confounds related to statistical frequency over time.

It is also not quite clear why performance on deprecated methods is measured by prompting with the version right before the method is being deprecated. At least, that is implied by L134 ("the last usable version") -- L129 contradicts itself by referring to the lifespan of a method as both $s \leq m \leq e$ and $[s, e)$, making it unclear whether version $e$ is included. If the prompt asks to complete a method that is about to be deprecated in the next version, I assume the goal is to find cases where the models might incorrectly assume that the method is already deprecated? If so, are the samples constructed so that there is a new, valid completion in the exact same context in the subsequent version? If not, the models almost "have no choice" but to complete the soon-to-be-deprecated version for snippets that use an idiomatic style that is made obsolete by the deprecation. Similarly, was there a check that the models aren't simpy using an alternative, valid API? Replacement APIs are often introduced before deprecating older versions.

There are a number of other, mostly minor, questionable claims about the performance as well, including:

L242: why does "excelling in handling downstream applications [...] increase the likelihood of models memorizing specific content"? Is the causal statement meant to be reversed, viz. models memorizing the content increases the likelihood of excelling in downstream applications? That would make more sense, but it would need some empirical evidence to back up that: the smaller models are not memorizing content, the patterns included here show up in the training data, and larger models aren't simply better at pattern matching.

L249: "However, most models struggle with reasoning and adapting to intermediate versions." -- does "intermediate" refer to added/deprecated ones here? If so, Fig. 3b shows that "most models" do relatively better on those than on unchanged ones.

L416: the description of GPT-4o's performance here seems off: its major->major performance is worse than on any other task. Relatedly, it was not clear to me what the sentence on L417/418 meant. Also, the use of "major->minor" and similar syntax is a bit confusing. Typically, we only distinguish between a major or minor version change. This paper seems to use the word "major" to refer just to the first version of a major release in order to distinguish between cases such as the first version of one major change to another vs. jumping from a given minor change within a major release to the start of the next major release. It is unclear why performance on the latter is so much higher than on major->major changes, or even on minor->minor changes, which ought to be much easier.


**Methodology:** as evidenced by some of the questions/concerns above (e.g. the lack of a solid baseline, the definition of deprecation), there are multiple concerns with the details of the approach. These often stem from a lack of clarity in the text, including in the appendix. An example of this is the definition of code migration: the example in Fig. 2 shows a case where the same description applies to two subsequent API versions and the code differs by just the API version. However, the way descriptions are generated (L863) doesn't guarantee that equivalent code snippets in successive versions would get the exact same description. Were the migration pairs collected from cases that happened to have an identical description? Was any manual validation applied to this process to capture the rate of false positives (and ideally FNs, but those would be harder to measure)?

The concern around the lack of manual validation applies to a number of other methodological decisions, such as scraping code from scientific papers. While a convenient dataset for this task, scientific code has a less than stellar reputation for quality. Was any filtering applied to confirm that this code was not using deprecated methods? Many of the results rely on the evaluation samples being unambiguous, in the sense that there is exactly one valid completion, but there is little evidence in the methodology or results that confirms that this has been guaranteed by this benchmark.

The definition of the "CDC" metric also raises some concerns. It appears that "exact match" as used in this paper does not refer to a true (semantic) match between programs, but rather to an identifier ("core token", L1025) match. The CDC metric expands on this with a few additional heuristic checks, such as comparing the number of arguments (but not their exact values) and the presence of a `with` statement. Per Tab. 11, these added heuristics have an almost imperceptible (and perhaps not statistically significant) impact on the correlation between CDC and pass@1 ranking. The main evidence for its usefulness comes from it yielding values closer to those from pass@1 than EM in Tab. 1, at the line and block level and the more noticeably higher Pearson correlation compared to EM at the block level. While that is useful, the lower values may well be in part due to the introduction of false negatives (e.g. matching keyword arguments is not necessarily a prerequisite for correctness) and there is still a considerable gap at the block level. Overall, I find it questionable to define "exact match" as something quite far from a true, semantic match, and the additional heuristics in CDC clearly leave a sizable gap with the actual target metric. I would strongly encourage the benchmark to focus on execution correctness over heuristic match, even if that shrinks the set of usable examples substantially.

**Relevance:** on a slightly less pressing note, this work seems only partially relevant to this venue. While the dataset it contributes shows useful limitations of LLMs, it does not offer proven insights into where these limitations originate and how they can be addressed. It makes a number of claims about why these limitations exist, some of which I identify as dubious above, but it does not support these claims with explorations of the models' training data or learned representations. Without a clear relation between how the models are actually built and the observed effects, any explanations feel rather speculative. That leaves the main contribution in the domain of code evaluation data, rather than representation learning. It may be more suitable for a venue dedicated to code-specific learning.

**Minor Issues:**

- L93: nit: inverted final quote
- L143: no need to use double equals
- L412: please add a mention that Tab. 2 has the results.
- L431: missing "more"?

### Questions
Regarding the concerns around the (interpretation of the) results, I strongly suggest removing the comparison with HumanEval and MBPP in favor of an analysis that separates out API completion performance on methods that are (almost) never changed vs. ones that are, to better isolate the existence and magnitude of the effect of versioning on API completion specifically. On this note, please try to answer:

Is the difference in performance statistically significant when controlling for time? E.g. in Fig. 4, is there a consistent difference when comparing datapoints for the same year between APIs that don't change (ideally ones that never change, but "general" is fine too) and ones that are added/deprecated for any of these models? Reverse trends for addition vs. deprecation are interesting too.

Please address the questions in the discussion about the definition and evaluation of deprecated methods and on the other methodological concerns above.

What degree of manual validation was used to ensure that the underlying snippets are valid? How were code migration pairs constructed exactly?

Is there a need for the CDC metric compared to pass@1 if the latter can be applied to a sufficiently large set of samples already? How do you address the concerns around the metric's potential for false negatives and the relatively slim difference compared to "Exact Match" (and the concerns with that nomenclature)?

Answers to all other questions in the "Weaknesses" section would be appreciated.

### Soundness
2

### Presentation
2

### Contribution
2
