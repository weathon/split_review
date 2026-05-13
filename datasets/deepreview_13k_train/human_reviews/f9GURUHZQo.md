# Large Language Models as Realistic Microservice Trace Generators

- Decision: Reject
- Scores: 6, 3, 6, 8

## Abstract
Computer system workload traces, which record hardware or software events during application execution, are essential for understanding the behavior of complex systems and managing their processing and memory resources. However, obtaining real-world traces can be challenging due to the significant collection overheads in performance and privacy concerns that arise in proprietary systems. As a result, synthetic trace generation is considered a promising alternative to using traces collected in real-world production deployments. This paper proposes to train a large language model (LLM) to generate synthetic workload traces, specifically microservice call graphs. To capture complex and arbitrary hierarchical structures and implicit constraints in such traces, we fine-tune LLMs to generate each layer recursively, making call graph generation a sequence of easier steps. To further enforce learning constraints in traces and generate uncommon situations, we apply additional instruction tuning steps to align our model with the desired trace features. Our evaluation results show that our model can generate diverse realistic traces under various conditions and outperform existing methods in accuracy and validity. We show that our synthetically generated traces can effectively substitute real-world data in optimizing or tuning systems management tasks. We also show that our model can be adapted to perform key downstream trace-related tasks, specifically, predicting key trace features and infilling missing data given partial traces.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a novel approach to generate synthetic workload traces, specifically microservice call graphs using LLMs. The authors fine-tune LLMs to generate each layer recursively to make this generation a sequence of easy steps and finally apply instruction tuning to align the model with desired features. The authors evaluate their approach on Alibaba v2022 dataseta across many key dimensions and report significant gains.

### Strengths
1. The paper is well-written.
2. The authors solve an important problem of generating data for micros-service calls which might be difficult to acquire because of privacy and performance constraints. 
3. This is an interesting domain of generating structured data.

### Weaknesses
1. The model evaluation is done for just one data, so the results might not be that generalizable to different datasets of varied characterisitics.
2. The model shows results for LLaMa-2-7B, but it does not evaluate for larger models. Will the proposed approach be as useful as the model scales.?
3. The model might overfit to certain structures if the training data does not capture diversity.

### Questions
1. Can you share the numbers of some other datasets>
2. Have you observed any pattern in the evaluation results as you scale the model?

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
This paper introduces a method for generating synthetic microservice call graphs using large language models (LLMs). It attempts to address the difficulty of obtaining real-world traces by training LLMs to produce hierarchical and constraint-abiding call graphs recursively, breaking down the complex task into simpler sub-tasks. The authors also employ instruction tuning to align model outputs with specific trace features, in order to enhance the model's ability to generate valid and realistic traces. The paper evaluates the proposed approach by substituting for real-world data in system management tasks and adapt to downstream tasks like predicting trace features and infilling missing data.

### Strengths
The paper introduces an approach to generating synthetic microservice call graphs using large language models (LLMs), which is an interesting idea for system workload tracing. It attempts  to handle complex and arbitrary hierarchical structures and implicit constraints within microservice call graphs through a recursive generation method. The paper highlights the potential of synthetic traces to replace real-world data in optimizing and tuning system management tasks, offering significant advantages in terms of privacy and data availability. The method of this paper is of a certain level of innovation and practical value.

### Weaknesses
1. I have serious doubts about the motivation of this paper: Do we really need synthetic traces in the microservices trace domain?
    1）None of the three "synthetic trace generation" methods mentioned by the authors are for generating microservices traces: (Bergsma et al., 2021) is for generating cloud workloads, and (Jiang et al., 2023; Yin et al., 2022) are for producing network traces.

   2）The authors only made a brief statement about the motivation, "Obtaining real-world traces is often hindered by privacy concerns and their general unavailability," without providing any arguments or details. Moreover, the authors' method also requires "1.36 million microservice call graph samples" for training and validation, which is contradictory.

   3）In fact, in enterprises with microservices as the basic architecture, trace data is abundant and easily obtainable. There is no issue of insufficient data. If privacy prevents the use of this data, then the authors' method would also be inoperable.

   4）Furthermore, there are many microservices simulation systems, such as TrainTicket (X. Zhou, X. Peng et al., “Fault analysis and debugging of microservice systems: Industrial survey, benchmark system, and empirical study,” TSE’18, 2018). These systems also consume far less resources than the "4xA100" used in this paper.

2. The authors' experiments are insufficient and fail to prove the effectiveness.
    1) As a key metric for measuring the quality of generated traces, "Accuracy," the authors did not elaborate on its definition or how to count the "valid following the initial instructions." The authors also did not introduce the "initial instructions."

    2) We know that the calling relationships between microservices in real environments are very complex, so to verify the accuracy of the generated traces, many aspects need to be validated, not just "Distribution of Popular Calls" and "Heavy-hitter Prediction." For example: response delays of instances, branching of traces, etc.

   3) Figure 3 shows that only when the number of edges is less than 5 or the depth is less than 2 can the accuracy of the generated traces be guaranteed to be high. Otherwise, a certain proportion of inaccurate data will appear. I doult that if this inaccurate data is used as training data for anomaly detection or root cause analysis, it will severely affect the model's performance. For example, for anomaly detection, the authors only mentioned that TraceVAE performs similarly with real and synthetic data, suggesting that the authors provide more experimental details (such as whether the test sets are the same) and compare more algorithms.

   4) When comparing effects, it is not very meaningful for the authors to always compare with untrained LLMs. It is recommended to add comparisons with existing trace generation methods. For example, which has a greater overhead and better effect between the TrainTicket simulation system and this paper's generation method.

### Questions
1. The authors should further elaborate the necessity of synthetic trace generation in the microservices domain, especially when ample tracking data is typically available in microservices-based architectures? Additionally, if privacy concerns limit the use of real-world tracking data, why your synthetic trace generation method still need real-world data for training?

2. It is recommended that the authors compare the proposed method with existing trace generation methods or simulation systems, such as TrainTicket, particularly in terms of resource consumption and effectiveness, to demonstrate the advantages or unique features of their approach.

3. The authors are suggested to define the "accuracy" metric used in their experiments and explain how "valid following the initial instructions" is quantified. Furthermore, it is suggested to include additional validation metrics that capture the complexity of microservice interactions, such as instance response times and trace branching.

4.The authors are advised to provide more experimental details, including whether the test sets used for comparing real and synthetic data are the same, and whether the inaccurate data is include for training TraceVAE. Additionally, it is recommended to include comparative experiments with existing trace generation methods to prove the effectiveness of the proposed method.

5.Please add more experiments about, what are the implications that accuracy declines when the number of edges exceeds 5 or the depth exceeds 2? For example, given the presence of a certain proportion of inaccurate data in the generated traces, the authors should discuss how to manage these data, especially when using them as training data for anomaly detection or root cause analysis, to avoid affecting model performance.

### Soundness
1

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
3

### Summary
The paper proposes to use LLMs for the generation of synthetic micro-services call-graph traces with the aim of providing richer datasets for downstream tasks in the microservice management domain while overcoming the privacy concerns of service providers. To enhance the quality of generated call graphs, authors rely on two key ideas. First, they generate call graphs using a tabular representation, i.e., a table with each row being an edge with given features such as source, destination, type, start time, end time, encoded in a subject-predicate structure similar to the concept used by the GreaT tabular data generator and include a series of preconditions. Second, they generate the call graph in a recursive top-down manner with intermediate instructions, which helps the model to generate edges satisfying consistency constraints, e.g., end time not later than the overall call graph end time. Using these, they fine-tune a Llama2 8b model and evaluate the synthesized call graphs both in terms of statistical similarities with respect to the training data and of utility in downstream tasks, i.e., when used to train other machine learning models also compared to vanilla LLM and prior art trace generators.

### Strengths
+ The data synthesized by the proposed generator based on fine-tuned LLM with the use of recursive call graph generation is able to match the performance of real data traces when used to train ML models.
+ The LLM is able to incorporate specifications from users.
+ Ablation study to evaluate the impact of recursive generation and intermediate instructions

### Weaknesses
 - One of the motivations for using synthetic data is to preserve privacy, but how much LLMs can or can not leak private information is still an open research question.
- Since the paper aims to generate (call) graphs, it would have been nice to include as a baseline a generator for attributed graphs.
- While authors use three baselines (TVAE and GreaT and a probabilistic model) when studying and comparing the distribution similarity between real and synthetic traces, the results on downstream utility are only performed against real traces. Moreover, here, the results are not very different from the ones obtained by GreaT.

Minor:
Figure 4a is a bit hard to read; I suggest plotting the data differently.
It would be nice to include confidence intervals in the plots of Figure 3.

### Questions
Please consider adding a baseline from the field of graph generators such as DiGress or similar and extending the result from Section 4.3 to the (at least a couple of the better performing) baselines.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a method for generating synthetic microservice workload traces by fine-tuning large language models (LLMs) to replicate complex, hierarchical microservice call graphs. Using a recursive generation approach, the model creates layers of the graph step-by-step, preserving structural constraints to ensure realistic trace outputs. Additional instruction tuning enhances the model's ability to follow specific trace requirements and generate uncommon scenarios, making the synthetic traces suitable as substitutes for real-world data in downstream tasks like anomaly detection. The method is shown to outperform existing generative approaches, offering a promising solution for environments where real trace data is limited or privacy-sensitive.

### Strengths
Innovative Use of LLMs for Trace Generation: The proposed use of large language models (LLMs) for generating realistic microservice workload traces, specifically microservice call graphs, is promising, leveraging recent advancements in language models to solve challenges related to data availability and privacy in system performance analysis.

Recursive Generation of Complex Graph Structures: The proposed method addresses the hierarchical and recursive nature of call graphs, which many synthetic data generation techniques struggle to capture. By breaking down call graph generation into recursive layers, the model can better manage complexity and maintain structural constraints, which is essential for realistic trace generation.

Instruction Tuning for Enhanced Trace Validity: The authors incorporate instruction tuning, adding intermediate reasoning steps that enforce trace constraints. This strengthens the model's ability to follow user specifications and generate traces that respect the structural dependencies within microservice architectures, such as start and finish times in hierarchical call graphs.

Demonstrated Practical Application: The paper shows that synthetically generated traces can effectively replace real traces in downstream tasks, including microservice management tasks like critical component extraction and anomaly detection. This is a valuable contribution, as it shows that synthetic data can potentially reduce reliance on sensitive real-world data while still maintaining performance.

Comprehensive Evaluation and Benchmarks: The authors conduct thorough experiments that compare the recursive and instruction-tuned model against baselines, such as probabilistic models and other generative methods like GANs and VAEs. They provide performance metrics across various tasks (e.g., trace generation, infilling, and downstream prediction tasks), giving a clear view of the model's strengths and limitations.

### Weaknesses
Limited Exploration of Long-Term Dependencies: While the recursive approach is effective in handling hierarchical structures, it does not retain previously generated layers or edges in memory. This may limit the model's ability to capture long-term dependencies or sequential behaviors across more complex, larger traces, which could be important in certain applications involving extensive trace histories. Specifically, the model might struggle to generate traces where the behavior of a service in a deep layer is influenced by the state of a service in a much earlier layer, potentially leading to unrealistic or inconsistent trace patterns.

Reliance on Manually Constructed Instruction Templates: The use of hand-crafted templates for instruction tuning may restrict the model’s adaptability and efficiency. Generating diverse instruction formats, possibly with automated methods, might improve the model’s generalization and reduce the manual effort required to customize instructions for different scenarios. The current approach may not effectively capture the full range of possible trace variations, particularly those that deviate from the predefined templates.

Performance Trade-Offs in High Complexity Scenarios: The model demonstrates a drop in accuracy with increasing complexity, particularly with greater numbers of edges and layers in the call graphs. Although the recursive approach and instruction tuning mitigate some of this complexity, the performance could suffer in very large or deeply nested call graphs, limiting its effectiveness for the most demanding or detailed traces. This is especially concerning for production systems with intricate service interactions, where the model’s accuracy may degrade significantly.

Synthetic Data Quality Compared to Real Data: Despite the high accuracy and validity of synthetic traces for downstream tasks, the paper notes a slight performance drop when using synthetic traces compared to real data in certain tasks. This suggests that, while synthetic traces are a viable alternative, they may still not fully replicate the nuances of real-world data. The subtle differences between synthetic and real traces could impact the performance of anomaly detection or other sensitive tasks.

Lack of Real-World Deployment Evidence: While the model is tested in a simulated environment and evaluated on trace data from a known dataset (Alibaba v2022), there is limited evidence of its performance in a live production environment. Real-world deployment could reveal additional challenges or performance limitations, especially under more varied or unforeseen conditions. The model's robustness to noisy or unexpected events in a live system remains uncertain.

Potential Privacy Risks with Instruction-Tuned Models: The instruction tuning approach, while effective, could raise privacy concerns if used with highly specific instructions or in contexts where sensitive information may inadvertently be reflected in the generation outputs. The model might inadvertently learn and reproduce patterns that reveal sensitive information about the underlying system or user behavior.

### Questions
Given that the recursive approach discards previously generated layers, how does this affect the model's performance in scenarios where long-term dependencies across multiple layers are critical? Could the authors provide additional insights or results on the effects of layer depth and sequence length on trace validity?

The paper mentions the use of hand-crafted templates for instruction tuning. Have the authors considered experimenting with automatically generated or dynamically adapted instructions to better match a broader range of conditions? Could this approach improve model generalization?

Have the authors considered or conducted tests of the model in real-world environments? While the model performs well on simulated data, deploying it in live production systems might reveal additional insights about practical constraints, resource usage, and unexpected errors.

The results suggest a performance drop with increased trace complexity. Can the authors clarify the main factors contributing to this decline? Is it due to limited model capacity, recursive generation limitations, or instruction tuning?

Instruction tuning, especially with user-specific attributes, might raise concerns about inadvertently learning or generating sensitive patterns. Did the authors take any measures to ensure privacy during training? Are there risks of exposing specific information, especially if used in sensitive environments?

The paper focuses on microservice call graphs, but this method may be adaptable to other hierarchical data. Do the authors foresee limitations in applying this approach to other domains, such as healthcare workflows or complex IoT interactions?

### Soundness
3

### Presentation
3

### Contribution
4
