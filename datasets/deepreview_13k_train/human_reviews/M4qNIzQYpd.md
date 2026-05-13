# OpenRCA: Can Large Language Models Locate the Root Cause of Software Failures?

- Decision: Accept
- Scores: 8, 6, 8, 5

## Abstract
Large language models (LLMs) are driving substantial advancements in software engineering, with successful applications like Copilot and Cursor transforming real-world development practices. However, current research predominantly focuses on the early stages of development, such as code generation, while overlooking the post-development phases that are crucial to user experience. To explore the potential of LLMs in this direction, we propose OpenRCA, a benchmark dataset and evaluation framework for assessing LLMs’ ability to identify the root cause of software failures. OpenRCA includes 335 failures from three enterprise software systems, along with over 68 GB of telemetry data (logs, metrics, and traces). Given a failure case and its associated telemetry, the LLM is tasked to identify the root cause that triggered the failure, requiring comprehension of software dependencies and reasoning over heterogeneous, long-context telemetry data. Our results show substantial room for improvement, as current models can only handle the simplest cases. Even with the specially designed RCA-agent, the best-performing model, Claude 3.5, solved only 11.34% failure cases. Our work paves the way for future research in this direction.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces OpenRCA, a novel benchmark and evaluation framework aimed at assessing the ability of large language models (LLMs) to perform root cause analysis (RCA) in real-world software systems, specifically focusing on the post-development phase, which has been largely overlooked in current research. The benchmark consists of 335 failure cases from three enterprise software systems, accompanied by over 68 GB of telemetry data (logs, metrics, and traces), challenging LLMs to identify the root causes of software failures by reasoning across complex, multi-modal data. The paper also proposes RCA-agent, a specialized tool to help LLMs process large volumes of telemetry data. The evaluation results show that current models, even with RCA-agent, struggle to handle these tasks effectively, with the best-performing model (Claude 3.5) solving only 11.34% of the failure cases. This paper makes a valuable contribution by highlighting the challenges and potential of LLMs in post-deployment software maintenance and lays a foundation for future research in automated root cause analysis.

### Strengths
The paper demonstrates several key strengths. First, it offers a clear and detailed evaluation, presenting comprehensive results that highlight how different models perform on the OpenRCA benchmark. The inclusion of various methods, such as RCA-agent and different sampling techniques, alongside a breakdown of performance by system complexity and task difficulty, provides valuable insights. Second, the model comparison between proprietary and open-source LLMs is highly informative, showcasing the limitations of current open-source models like Llama 3.1 compared to more advanced proprietary models like Claude 3.5 and GPT-4o, effectively setting the stage for future improvements. The paper also includes a strong task complexity and system analysis, showing how model performance correlates with system complexity and the number of root cause elements, offering practical insights for future research. The reasoning length and error tolerance analysis provides an interesting perspective on how LLMs' performance can be improved with longer reasoning and better error handling. Finally, the real-world applicability is demonstrated through a detailed case study, illustrating how the OpenRCA benchmark can be used in practice to solve root cause analysis tasks, thus bridging the gap between theory and real-world challenges.

### Weaknesses
Insufficient Contextualization of Problem Importance:
Lack of Quantitative Evidence: The paper mentions that software failures cost "billions of dollars," but does not provide specific references or data to substantiate this claim. For instance, Figure 1 cites the financial impact without attributing it to any source.

Actionable Insight: Provide concrete data and citations from industry reports or academic studies that quantify the financial and operational impact of software failures. For example, referencing studies from Gartner or IEEE could strengthen the argument and give readers a clearer understanding of the problem's magnitude.

Inadequate Literature Review on Existing RCA Benchmarks:
Questionable Claim in Section 2.2: The assertion that "RCA is a critical step in the software development lifecycle but often lacks practical benchmarks" may not fully reflect the current state of research. There are existing benchmarks and tools for RCA in software engineering.

Actionable Insight: Expand the literature review to include a comprehensive analysis of existing RCA benchmarks and tools. Discuss works like the MIMIC dataset in healthcare analytics or other RCA frameworks in software engineering to highlight how OpenRCA differentiates itself and fills existing gaps.

Limited Discussion on Broader Impact and Applications:
Underdeveloped Broader Impact Section: The paper does not sufficiently elaborate on how OpenRCA can improve software maintenance, quality assurance, or developer workflows.

Superficial Analysis of Low Model Performance:
Lack of Deep Dive into Results: The observation that "current models can only handle the simplest cases" lacks a thorough analysis. The paper does not explore why models performed poorly—whether it's due to limitations in model architecture, data complexity, or other factors.
Actionable Insight: Conduct a detailed error analysis to identify the root causes of low model performance. Discuss whether issues stem from the models' inability to process long-context data, difficulties in reasoning over heterogeneous data types, or shortcomings in handling complex software dependencies. Providing specific examples where models failed can offer valuable insights.

Overreliance on Synthetic Queries and Lack of Real-World Data:
Synthetic Nature of Failure Reports: The queries are synthesized based on common failure reports, which may not capture the complexity and nuances of real-world scenarios.

Complex Tables and Figures Without Adequate Explanation: Some tables (e.g., Table 2) and figures (e.g., Figure 5) are dense and may be difficult to interpret without additional context. References to Appendix A suggest that crucial information is relegated to the appendices.

Limited Diversity of the Dataset:
Narrow Focus on Distributed Systems: The dataset comprises failures from only three enterprise distributed software systems, potentially limiting the applicability of the benchmark to other system architectures like monolithic or embedded systems.

Absence of Ethical Considerations and Potential Risks:
No Discussion on Ethical Implications: The paper does not address potential ethical concerns, such as the consequences of incorrect root cause identification in critical systems, which could lead to misdiagnosis and exacerbate issues.

### Questions
Can you provide more details on the selection process for the failure cases in OpenRCA?

Clarification Needed: The paper mentions 335 failure cases from three enterprise systems but does not describe how these cases were selected. Were they chosen based on frequency, severity, or another criterion?
Suggestion: Please clarify the criteria used to select these cases and explain how representative they are of real-world failure patterns.

What are the specific challenges faced by models when handling multiple root cause elements?

Clarification Needed: The paper observes a significant drop in accuracy as the number of required root cause elements increases. Is this due to limitations in context window size, inability to handle heterogeneous data, or something else?
Suggestion: A more detailed explanation of the challenges could help readers understand the underlying issues and suggest pathways for improvement.

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
The paper introduces OpenRCA, an innovative benchmark designed to evaluate large language models in identifying root causes of software failures using diverse, long-context telemetry data. The authors evaluate state-of-the-art LLMs on this benchmark, offering a high-level analysis of their performance. The authors also introduce RCA-Agent as a tailored solution for OpenRCA task. The findings suggest significant room for enhancing LLM capabilities in solving real-world service reliable problems.

### Strengths
- OpenRCA pioneers the application of LLMs in the post-development phase of the software life-cycle, highlighting a new direction to use LLMs for identifying and analyzing real-world software issues.

- The authors’ rigorous data-cleaning process in building OpenRCA is valuable, involving system selection, data balancing, data calibration and query synthesis.

- The goal-driven task design covers various aspects of RCA tasks, framing them in a generalized, natural-language query format.

- The authors conduct a comprehensive experiments of popular closed and open LLMs with different strategies (Balanced Sampling, Oracle Sampling and RCA-Agent). And the authors also provide high-level comparative analysis for each setting based on experiment results.

### Weaknesses
 - OpenRCA includes only three distributed software systems, which is small and may limit the benchmark’s generalizability. As noted by the authors, accuracy appears to correlate with system complexity, and the telemetry distribution varies across systems. Although OpenRCA provides 335 failure cases, the limited number of software systems could introduce significant variance. The variance is concerning because the performance of models may be overly influenced by the specific characteristics of these three systems, rather than demonstrating a general ability to identify root causes across diverse software environments. The limited number of systems also makes it difficult to assess how well the benchmark generalizes to different types of software architectures and failure modes.

- The benchmark does not fully disentangle the capabilities of long-input retrieval, non-natural language understanding, and software problem identifying. The long, complex, non-natural language input introduces additional difficulty for LLMs, potentially limiting performance beyond the task of software failure identifying. The complex input format, consisting of logs, traces, and metrics, requires LLMs to possess specialized domain knowledge and the ability to process heterogeneous data types, which makes it difficult to isolate the specific challenges of software failure identification. Adding an ablation study could help isolate the challenges introduced by long, non-natural language input. For example, it would be beneficial to evaluate the models on a simplified version of the input data, such as using only logs or traces, to determine the impact of each data type on performance.

- The data collection approach seems to highly reliant on human effort, which may cause difficulty in updating and scaling. Collecting software telemetry and manually annotating Oracle sampling seems to be labor-intensive. Actually, frequent updates are crucial for keeping LLM benchmarks quality, particularly in consideration of potential data leakage. The manual annotation process is not only time-consuming but also prone to human error, which could introduce inconsistencies in the benchmark data. A more automated approach to data collection and annotation would be necessary to ensure the long-term viability and reliability of the benchmark. Furthermore, the lack of a clear data update strategy may lead to the benchmark becoming outdated quickly, especially given the rapid pace of software evolution.

- As the authors note, the current benchmark includes only distributed systems. Expanding the benchmark to incorporate systems from other domains would provide a broader evaluation of LLM capabilities. The focus on distributed systems limits the applicability of the benchmark to other types of software, such as embedded systems or desktop applications. Including a more diverse range of systems would provide a more comprehensive assessment of LLMs' ability to identify root causes in different software environments.

- Typo: In line 035, "post-development phrases" --> "post-development phases."

### Questions
- The authors categorize tasks into three levels: Easy, Mid, and Hard, based on the number of elements. Given that system complexity varies among repositories (for instance, Telecom has the smallest telemetry volume), could the authors further explain on why element count was chosen as the primary criterion for task difficulty? How did the authors account for the impact of system complexity on task difficulty?

- The authors state in Line 363 that "models generally follow the same trend: accuracy increases with more reasoning steps." However, Figure 6 does not appear to strongly support this, as accuracy varies significantly across different models and lengths. Could the authors provide further clarification or evidence on how this conclusion was reached?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper provides OpenRCA, a benchmark set for root cause analysis for software systems. The benchmark set is composed of 335 failures and the task is to identify the timing of the failure along with the component that failed and its reason. The paper also proposed RCA-agent, a multi-agent approach that utilizes a coe execution environment to effectively utilize telemetry data. While the best performing LLM was able to solve 6% of failure cases, RCA-agent increased it 11%.

### Strengths
The paper introduces a novel benchmark dataset for root cause analysis. The benchmark set is carefully designed with emphasis on consistency and quality. This in my opinion is a significant contribution as it can likely help advance the field, motivating further contributions utilizing this dataset. The second contribution on RCA-agent is limited in its originality as multi-agent systems utilizing code execution are widely available. Nevertheless, showcasing the increase in accuracy through an agentic approach motivates further research on this. The paper is very well written and organized.

### Weaknesses
The paper puts emphasis on creating a high quality dataset and one of the processing steps was the removal of failure records where the root cause cannot be identified using the given telemetry. Envisioning a system which acts based on the analysis from automated root cause analysis, it is vital to be able to flag if the root cause cannot be identified from given data. Therefore, the benchmark set should reflect that in my opinion. 

Due to the highly stochastic nature of agentic systems as well as LLMs, I think evaluations would be stronger if authors can provide error bars. Specifically, reporting median values without any measure of variance makes it difficult to assess the robustness of the results. The lack of error bars obscures the consistency of the performance across different runs, which is particularly important given the inherent randomness in both LLM outputs and agent-based execution environments. 

As the paper focuses on root cause analysis for distributed systems, one insight that would make the paper stronger is how LLMs and the proposed RCA-agent perform as the scale of the system increases. That would help the readers understand limitations and applicability of such approaches. The current evaluation does not explore how the performance of the proposed method scales with the complexity of the distributed system, which is a critical factor in real-world deployment scenarios.

### Questions
- The comparative analysis of LLMs are interesting but given the rather low performance of individual LLM’s, I’m curious to see if one would get any additional boost in performance when they are used in an ensemble fashion. This also helps to understand if the LLMs considered identify similar failures or not.
- Table 3. For the hard category, all LLM’s even in the agent setting gets 0. I’m guessing maybe identifying the reason is harder than identifying the timing of the issue. Following this intuition, I’m wondering if there is a task that is difficult across the board?  
- Figure 5. The accuracy distribution for RCA-agent is completely different than the sampling based ones. For instance, using GPT-4o, we see that the accuracy is reduced for Telecom and bank datasets but increased for Market dataset. Similarly, using Llama3.1, we see that the accuracy is similar for Telecom and Bank but reduced for the Market dataset. I’d love to hear more insights on these behaviors.
- Could you clarify which model size you used for Llama3.1-instruct?
- Nit: Table 4. Explain what drop ratio is in the title.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper preposes OpenRCA, a benchmark for root cause analysis that requires models to extract potential root cause from large quantities of telemetry data, logs and traces. The paper also proposes RCAagent as a potential method to solve this root cause analysis problem since vanilla models struggle. The paper uses three SOTA closed-source models and three open-source models for the evaluation on OpenRCA.

### Strengths
- RCA remains an important problem in realistic scenarios.
- Good paper structure, explains the key problem, terminologies, and ideas very clearly.
- Clean and good dataset with clear structures, etc.
- A realistic RCA benchmark, with huge effort made towards ensuring fairness and denoising.

### Weaknesses
### Major
- The “golden set” identified in the oracle sampling might be not realistic enough. In real-life tasks, it is also one of the key challenge for the model to understand and select the correct KPI in order to diagnose the problem.
- Using agent has been a widely adopted method in other research fields. This paper fails to provide any insight into the nature of the problem and merely uses a general planner-executor agent framework almost without applying any domain knowledge. The only domain knowledge is a 42-line long rule given to the planner, which basically outlines all the things that the LLM should do. As a result the agent part seems really redundant and unnecessary. The same argument applies to the case study.
- There is no point trying vanilla LLM on this task. The author acknowledges in the paper that it is virtually impossible to give the telemetry data to the LLM, which is why they adopt the sampling method. There are two flaws in this: 1. LLM is not designed to process huge amount of data, so an agent evaluation/previous baseline evaluation should be more proper, and 2. There is no tell that if the performance of the LLM is bounded by the sampling.

### Misc
- Some apparent spelling mistakes, like “Partitial” in table 2, or “Accuray” in table 3
- The instruction given to the baseline in the artifact is far less comprehensive than the one given to the agent. Maybe fairer to give more domain knowledge to the baseline models?
- The CSV file for the record in the artifact is confusing and consists lots of excess newlines?
- Rather than reducing the size of the benchmark, why don’t do a success rate calculation on each system first and then compute the final score on the three success rates?

### Questions
- Does oracle sample generalize to general RCA tasks? Is it a realistic baseline?
- Does the 42-line rule in the system prompt given to the planner LLM generalize to other cases as well? What is the insight in designing an agent this way specifically for this task?
- Is the benchmark intended for LLM or agents? Why wasn't other more specialized tools/agents from previous work tested and reported on the benchmark? 
It would also be great for the authors to address the misc weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
