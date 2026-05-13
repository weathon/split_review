# Planning in Strawberry Fields: Evaluating and Improving the Planning and Scheduling Capabilities of LRM o1

- Decision: Reject
- Scores: 1, 5, 3, 3

## Abstract
The ability to plan a course of action that achieves a desired state of affairs has long been considered a core competence of intelligent agents and has been an integral part of AI research since its inception. With the advent of large language models (LLMs), there has been considerable interest in the question of whether or not they possess such planning abilities, but--despite the slew of new private and open source LLMs since GPT3--progress has remained slow. OpenAI claims that their recent o1 (Strawberry) model has been specifically constructed and trained to escape the normal limitations of autoregressive LLMs--making it a new kind of model: a Large Reasoning Model (LRM). In this paper, we evaluate the planning capabilities of two LRMs (o1-preview and o1-mini) on both planning and scheduling benchmarks. We see that while o1 does seem to offer significant improvements over autoregressive LLMs, this comes at a steep inference cost, while still failing to provide any guarantees over what it generates. We also show that combining o1 models with external verifiers--in a so-called LRM-Modulo system--guarantees the correctness of the combined system's output while further improving performance.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper evaluates the planning capabilities of OpenAI's latest o1 series models on the PlanBench and TravelPlanner benchmarks, and proposes the use of external verifiers to assist the models in planning.

### Strengths
The paper is highly timely and helps readers understand the specific performance of the o1 series models on the two benchmarks.

### Weaknesses
The paper's contribution to the community is relatively limited, as it does not provide any new insights.

The first key observation ``while o1 does seem to offer significant improvements over autoregressive
LLMs, this comes at a steep inference cost'' is already highlighted in OpenAI's official post (https://openai.com/index/learning-to-reason-with-llms/). The specific magnitude of this cost, while perhaps not explicitly quantified in the OpenAI post, is a predictable consequence of the increased model complexity and the iterative nature of the o1 architecture. The paper does not offer a novel analysis of this cost beyond what is generally understood about such models.

The second key contribution in Section 4 — that ``combining o1 models with external verifiers–in a so-called LRM-Modulo system–guarantees the correctness of the combined system’s output while further improving performance.'' — is also not new; it simply tests o1 models within the established LLM-Modulo Frameworks [1], without providing any new insights. The application of this framework to a new model, while useful, does not constitute a significant contribution if the results are predictable and do not reveal any unexpected behavior or insights.

### Questions
No questions.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
OpenAI's o1 (Strawberry) represents a shift from traditional LLMs to Large Reasoning Models (LRMs). The paper evaluates the o1 family (including o1-preview and o1-mini) on planning and scheduling capabilities using established benchmarks like PlanBench, TravelPlanner, and graph coloring problems. The study shows that while o1 models outperform previous LLMs, they result in higher inference costs and lack guarantees for output accuracy. The study also explores methods to enhance reliability through integration with RM-Modulo framework as external verification.

### Strengths
- The paper focuses on important practical considerations such as reliability and efficiency of LRMs
- The paper utilizes established benchmarks while extending them for more rigorous testing and takes a systematic approach to evaluating both basic and complex planning scenarios. The paper presents a thorough evaluation with performance metrics, such as accuracy and inference time clearly reported and supported with comparative data.
- Proposed the integration of LRM-Modulo framework for enhanced reliability and potentially efficiency when coupled with the mini version

### Weaknesses
 - The reliability of the proposed LLM-Modulo integration when paired with the o1-mini model is unclear to me. While we can observe improved o1-mini performance, in cases such as Blockworld (hard), Sokoban, Trip Planning, o1-mini still significantly lags behind o1 performance. As the inference efficiency is an important consideration, it is unclear whether the LLM-Modulo can reliably deliver better efficiency while preserving the quality of the response.
- The studied problem is important but the novelty of the paper's proposed solution is limited.

### Questions
- Can the authors please explain the applicability and scalability of LLM-Modulo outside of the tested benchmarks, e.g., for practical usage? What is the minimum requirement of a task for the LLM-Modulo integration to be implemented?
- What are the potential ways to make the high inference cost of o1 more manageable in practical settings, besides using o1-mini as a replacement?

### Soundness
2

### Presentation
2

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
The paper examines the capabilities of large reasoning models (LRMs) for planning and scheduling tasks.  It evaluates two LRMs, o1-preview and o1-mini, on benchmarks (for example PlanBench, Natural Plan benchmark and Travel Planning benchmark) and compares their performance to previous results.  The paper also notes the steep inference cost of LRMs and discusses the tradeoffs between using LLMs versus LRMs, arguing that in some cases an LLM-Modulo approach may be significantly cheaper than o1 models for comparative performance, and with guarantees.

### Strengths
+ The paper demonstrates strong integration with existing framework (LLM-Modulo), leading to cost reductions in the evaluation process.
+ The authors provide thorough documentation of the prompts and their design.
+ The research contributes to our understanding of model capabilities and limitations, which is important for the field’s development and for improving model robustness.

### Weaknesses
The paper’s introduction could benefit from a clearer motivation. The decision to produce a new benchmark evaluation for each model release raises a question: does this paper bring a unique perspective to the evaluation landscape, or could the model creators be responsible for performance assessments of "established" benchmarks? Given that no new methodology or dataset is introduced, the contribution could appear limited to evaluating 1-2 additional models.

- Structural and Organizational Observations

The structure of the paper could be improved for clarity. For example, the results are presented as early as the related work section and continue sporadically throughout, which may make it challenging for readers to follow the flow of the argument. Additionally, the section on related work doesn’t provide a comprehensive view of the current state of the field, which might leave readers without a solid foundation in the broader research context.

Some terms, like "IPC," are introduced in the introduction but explained only in later sections. Defining these terms earlier could help readers understand the content more easily. Additionally, while the appendix includes sample prompts, adding a detailed example or task illustration in the main text could make the methodology and objectives clearer to readers.

- Evaluation and Methodological Details

The evaluation process might benefit from further clarification, especially concerning the assessment of LL(R)M solutions. For instance, it’s not entirely clear whether the evaluation is based on finding an optimal solution path or whether any correct path is acceptable, and if only one solution path is considered correct per example. Further qualitative analysis of the model’s errors would also be helpful—such as identifying if mistakes are common at the start of a task, or more likely toward the end. Discussing typical solution lengths would add another informative layer to the evaluation.

The evaluation protocols could be explained in more detail. The authors mention using a fixed temperature of 1 (this is fixed temperature for o1 models), but it would still help to run each instance multiple times (e.g., 3-5 runs) to check for any variation in results. This approach would make the findings more reliable. Given the focus on evaluation costs, applying this method to a smaller subset could balance accuracy with resource use.

- Contributions and Added Insights

The paper’s introduction suggests new metrics will be introduced, but no specific metrics are proposed. While the authors argue that “new approaches to measuring LRM reasoning capabilities must consider efficiency, cost, and guarantees,” this point is broadly applicable to all LLMs rather than being specific to LRMs

In the section evaluating Sokoban, some additional details could improve transparency. For instance, providing information about the board distributions (e.g., sizes and number of boxes) and specific results across different board configurations could give readers a clearer picture of the model’s performance. The authors report that o1-mini achieved a 10.9% success rate on Sokoban, while Llama3.1-405B achieved 0%; however, further analysis on this performance gap would be helpful.

- Style and Presentation Suggestions

The paper’s tone in certain sections could be more formal. Phrasing that is occasionally colloquial, along with exclamation marks, can detract from the overall scientific rigor expected in research papers. Additionally, consistency in the figures could improve readability—specifically, in Figure 1, the lines on the left plot are hard to see, and the color scheme is inconsistent between plots, which may make interpretation challenging.

Currently, the absence of code limits the ability of readers to reproduce the findings. Additionally, a discussion on limitations and broader impacts would provide helpful context regarding the scope and implications of the results.

- Cost Analysis Considerations

The cost analysis presented in Table 4 could be better suited to the appendix. Since model costs can vary over time, the information may quickly become outdated.

### Questions
Q1. How is the solution generated by the LLM evaluated? Is it based on finding the optimal path, or is any correct path acceptable? Also, is there only one correct solution path for each example?

Q2. Is there any qualitative analysis of errors? For instance, when does the model typically make mistakes? Does it struggle to begin tasks correctly, or do errors occur more frequently toward the end of the solution? Additionally, what is the average length of the solutions?

Q3. Could you provide more detail on the evaluation protocols? The paper mentions a temperature setting of 1, but was any sampling used, given the non-deterministic nature of results? For example, was each instance evaluated multiple times (e.g., 3-5 runs) to capture potential variance? 

Q4. Could you clarify the distribution details for the Sokoban tasks? Specifically, what are the board sizes and the number of boxes used, and are there specific results for each configuration?

Q5. The paper reports that on Sokoban, o1-mini achieved a 10.9% success rate, while Llama3.1 (405B) achieved 0%. Could you provide some analysis or discussion on why there is such a difference in performance?

Q6. For Gemini 1.5 Pro, were the parameters regarding safety settings configured correctly to produce reasonable answers?

Q7. Could you define "gaslighting" in this context? Are there relevant citations or sources that you could provide on this topic?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors benchmarked the performance of the newly released o1-preview and o1-mini on a few planning and scheduling datasets, and further evaluate how o1 models can be combined with LLM-Modulo system to enhance the guarantees of the correctness.

### Strengths
- The paper is overall well-written and easy to follow.
- The paper tests the state-of-the-art model, the o1 series, and studies their performance on complex reasoning tasks, including planning and scheduling problems.

### Weaknesses
 - While it is definitely important to understand the actual performance of the newly released o1 models not from the OpenAI team as an advertisement, the contribution seems limited. This paper does not propose a new dataset or a new method. The conclusion is also not surprising given the extremely large amount of work on LLM for planning that has already been published and even cited in the paper  [1, 2, 3]. And the new argument on the cost side seems obvious given the price already released by OpenAI.
- While the overall writing is easy to follow, the style does not follow the typical academic paper but is more like a blog post. Many non-declarative sentences are used.
- The paper does not follow the ICLR template format right now.

### Questions
Can you explain the significance of this paper? What is the main contribution besides evaluating a new series of models?

### Soundness
3

### Presentation
3

### Contribution
1
