# Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
The advancement of large language models (LLMs) prompts the development of multi-modal agents, providing a feasible way to solve practical tasks by using tools. In this paper, we propose a multi-modal agent tuning method that automatically generates multi-modal tool-usage data and tunes a vision-language model (VLM) as the controller for powerful tool-usage reasoning. To preserve the data quality, we prompt the GPT-4o model to separately generate queries, files, and trajectories, followed by a query-file verifier and trajectory verifier. Based on the data synthesis pipeline, we collect the MM-traj dataset with 20k tasks using 10 tools. Then, we build the T3-agent that uses MiniCPM-V as the controller Trajectory Tuning for Tool usage using MM-Traj.  Evaluations on the GTA and GAIA benchmarks show that the T3-agent has achieved remarkable improvements and outperforms GPT-4 driven agents by 10%, showing the effectiveness of the proposed data synthesis pipeline that leads to better reasoning capabilities in tool usage.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method for multi-modal agent tuning for tool usage and presents a dataset designed to train an agent for tool usage. The authors claim that their T3-Agent achieves significant improvements.

### Strengths
1) The idea of using an LLM to separately generate queries, files, and trajectories, followed by a query-file verifier and trajectory verifier is neat.
2) The paper addresses the problem of using the appropriate array of tools corresponding to the information relevant to a query well. 
3) The experiments are thorough.

### Weaknesses
1) Verifying the output of an LLM by the LLM itself does not seem accurate. I am skeptical about the quality of the generated MM-Traj dataset. 
2) You need quantitative verification for the dataset. (It is not clear whether a user study involving a few people on 100 data points out of 15K would provide sufficient confidence.)
3) Experimental results on the GTA benchmark are more promising than those on the GAIA benchmark. However, the overall performance of T3-agent is not superior to that of the other agents in comparison. Specifically, on the GAIA benchmark, the HF agent with GPT-4o performs twice as well as the T3-Agent.
4) If the T3-Agent’s performance were clearly superior, I would be more optimistic about the generated dataset. However, the results seem to support my doubts about the dataset.

### Questions
Please address the concerns raised in the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel approach for multi-modal agent tuning, aimed at enhancing agent performance in complex environments through better utilization of multiple data modalities. The authors propose a tuning framework designed to leverage cross-modal data (e.g., visual and text info) to improve agent task performance, with specific emphasis on tool usage within the agent's capabilities. Their T3 agent is multi-modal agent that can efficiently use tools to solve practical tasks by tuning a VLM as the controller. Evaluations over the various dataset show the significant improvement using their agent with closed as well as open source model. Additionally, they curated dataset using multimodal info having trajectory of various length for broader study. In this work focus is on the correct tool selection and code is given more importance than the widely used JSON schema. In summary, they generate data, tune the VLM and create dataset followed by leverage of tool agent to make use of tool in a better way.

### Strengths
1. Innovation in Multi-Modal Interaction: The approach shows potential in pushing the boundaries of how agents interact with cross-modal data sources. By focusing on practical applications of tool usage, this work could offer useful insights into building agents that understand and respond to complex queries across various media.
2. Comprehensive Methodology: The paper describes a well-structured experimental setup and provides a clear description of the multi-modal tuning process. This includes thoughtful considerations on data processing, model architecture, and task-specific tuning steps, making it easy to follow.
3. Evaluation Metrics: The authors employ a diverse set of metrics to evaluate agent performance. This choice not only validates the model’s accuracy in the tasks but also emphasizes the practical utility of the proposed framework in real-world applications.

### Weaknesses
1. Interpretability: While the approach demonstrates performance gains, the interpretability of results remains limited. Additional analyses, such as ablation studies or attention maps, would be beneficial to understand how each modality contributes to the decision-making process. For example paper first generate queries first without files before relevant queries, what is the impact if we don't do that, or this is based on some past work/observations?

2. Scalability: The paper does not thoroughly address the scalability of the proposed method, particularly as the number of modalities or the dataset size increases. It would be beneficial to test how the method's performance and computational requirements scale with additional modalities or larger datasets. For example, experiments that measure latency, memory usage, and accuracy as more data is introduced could illustrate the framework's robustness and its viability in resource-constrained or high-throughput environments.

3. User Study: To evaluate the practical usability of the framework, a small user study or qualitative feedback from users would provide valuable insights into the query handling experience. Specifically, gathering feedback on aspects like ease of use, perceived accuracy, responsiveness to complex queries, and the intuitiveness of the tool-usage process could highlight areas for refinement in real-world settings.

Minor hints:
1. sec5.6 typo.. "wen based"--> web based.
2. sec 3.4- Author(s) mention details can be found in but missed cross-referencing it.
3. cross reference missing at end of sec 3.4

### Questions
Q: Could you please elaborate on how not using the final answer A aligns with your goal? Specifically, how does this choice benefit your approach to enhancing tool-usage capability?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a new approach for improving tool usage in multi-modal agents by fine-tuning a vision-language model (VLM) controller with synthesized tool-usage data. To overcome the limitations of traditional LLM-driven agents—such as reliance on prompt engineering and limited reasoning for tool usage across modalities—the authors create a three-step data synthesis pipeline. First, *Query Generation* uses GPT-4o mini to generate diverse, tool-aware prompts. Next, *File Generation* retrieves images from similar datasets and creates other files programmatically. Finally, *Trajectory Generation* employs a zero-shot agent using GPT-4o mini to solve tasks, capturing thought processes, code, and observations for each step. Quality is controlled through query-file and trajectory verifiers, also based on GPT-4o mini, producing a dataset called MM-Traj. The resulting agent, T3-Agent, uses the ReAct framework and the MiniCPM-V model trained on MM-Traj, enabling versatile tool usage across categories like web search, visual perception, image editing, and file handling. Benchmarks on GTA and GAIA demonstrate the T3-Agent’s significant improvements in tool usage over both untrained VLMs and other state-of-the-art LLM-driven agents.

### Strengths
- The data synthesis pipeline introduces a scalable, automated approach to generating diverse, complex multi-modal data for tool usage scenarios.
- Verification mechanisms embedded within the pipeline enhance data quality, resulting in a robust, comprehensive dataset.
- With training on the MM-Traj dataset, the T3-Agent demonstrates significant performance gains, surpassing agents built on closed-source models like GPT-4 in certain benchmarks.
- Ablation studies underscore the critical role of data verification in achieving top performance.
- The paper includes detailed visualizations of the T3-Agent’s reasoning process.

### Weaknesses
 - The T3-Agent exhibits a gap in programming capabilities, which leads to lower accuracy in predicted answers compared to GPT-4o. 
- While the paper acknowledges the T3-Agent’s limited programming capabilities, it does not suggest potential improvements or outline future directions to strengthen this aspect.
- The reliance on GPT-4o mini throughout the pipeline raises questions about biases and limitations from this closed-source model. Exploring alternative methods or open-source models could enhance transparency and address these limitations.
- What is $p_i$ in Equation 2?

### Questions
I lean towards acceptance because the paper introduces a promising approach to enhancing the reasoning capabilities of multi-modal agents. The proposed data synthesis pipeline and the resulting MM-Traj dataset are significant contributions to the field, potentially advancing the state of multi-modal learning. However, the paper lacks a discussion on the T3-Agent's robust programming capabilities and does not explore how these might be improved. I would like the authors to comment on this aspect.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work introduces a multi-modal tool-usage data generation pipeline designed to finetune vision-language models (VLMs) for tasks requiring tool-usage reasoning. The pipeline consists of three primary steps. First, a large language model (LLM) is prompted to generate query tasks. Next, relevant images or files are retrieved or generated based on the specified query tasks. Finally, ReAct agents are employed to generate trajectories that address the query task problem, followed by an additional LLM prompt to verify the generated data.

This study also introduces the MM-Traj dataset generated through the proposed scheme and uses it to finetune the MiniCPM-V model to create the T3-agent. The T3-agent's effectiveness is subsequently assessed on the GTA and GAIA benchmarks, showcasing a 20% improvement in performance over untrained VLMs and achieving results comparable to other baseline agents, such as the Lego Agent, Warm-up Act Agent, and HF Agent.

### Strengths
1. The proposed data generation pipeline first generates queries independently of any specific files, followed by producing relevant files to align with these queries. This approach allows the pipeline to create more diverse and expressive tasks, unrestricted by file format or quantity limitations.
2. This work introduces the novel MM-Traj dataset, containing 20k diverse tool-usage data points, supported by a human study to demonstrate dataset quality. 
3. This work also performs an in-depth statistical analysis of the dataset and shows that MM-Traj offers broad coverage across various data modalities and knowledge requirements, as shown in Figure 3.

### Weaknesses
1. In Section 3.3, this work states, “for other needed files, we prompt GPT-4o mini to extend the file content and generate Python code to produce the files.” However, the methodology for file generation remains unclear. For example, if a file is required to be an MP4 video of Taylor Swift’s latest album, it’s uncertain how this content could be generated through Python code alone. Furthermore, if GPT-4o mini generates the Python code to produce such files, it raises concerns about data quality and how the model ensures that the generated content is not hallucinated. The paper does not specify the types of files that can be generated, nor does it provide a clear explanation of the limitations of this generation process, particularly regarding complex multimedia files.
2. While including a human study to assess dataset quality is commendable, having only five experienced raters for a subset of the data may be too limited, potentially introducing biases based on individual preferences. Gathering feedback from a **larger pool of participants**, even with fewer data points per person, could strengthen claims about the dataset's effectiveness. Additionally, comparing MM-Traj to filtered-out data may not yield meaningful insight. Instead, comparisons with other established tool-usage datasets would likely provide more meaningful insights. The study should also include inter-rater reliability metrics to quantify the agreement between raters.
3. The evaluation results in Table 3 reveal mixed outcomes, with the T3-agent performing significantly worse than other methods, such as HF Agent and Sibyl Agent, on the GAIA benchmark. What could lead to this performance discrepancy on the GAIA benchmark? The paper does not provide a clear analysis of the specific challenges posed by the GAIA benchmark that might explain the T3-agent's lower performance. It is also unclear whether the T3-agent's training data adequately covers the types of reasoning required by the GAIA benchmark.

### Questions
1. In Figure 3, the sum of trajectories—214 + 14,273 + 8,740 + 2,520 + 1,242 + 697 + 199 + 202—totals 28,087, which exceeds the stated 20k tasks in the abstract. In addition, the paper mentions that only 15k files remain after passing the query-file and trajectory verifiers. What is the final size of the generated dataset?.
2. Why does GPT-4o mini outperform GPT-4o in Table 2, specifically in the row with HF Agents on AnsACC and CodeExec, given that GPT-4o is expected to be more powerful than GPT-4o mini?

### Soundness
3

### Presentation
3

### Contribution
2
