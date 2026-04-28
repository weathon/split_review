# Plan-RAG: Planning-guided Retrieval Augmented Generation

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6

## Abstract
We introduce Planning-guided Retrieval Augmented Generation (\ours), a novel framework that augments the \emph{retrieve-then-reason} paradigm of existing RAG frameworks to \emph{plan-then-retrieve}. \ours formulates a reasoning plan as a directed acyclic graph (DAG), decomposing queries into interrelated atomic sub-queries. Answer generation follows the  DAG structure, allowing significant gains in efficiency through parallelized retrieval and generation. While state-of-the-art RAG solutions require extensive data generation and fine-tuning of language models (LMs), \ours incorporates frozen LMs as plug-and-play experts to generate high-quality answers. Compared to existing RAG solutions, \ours demonstrates significant improvements in reducing hallucinations and bolstering attribution due to its structured sub-query decomposition. Overall, \ours offers a new perspective on integrating external knowledge in LMs while ensuring attribution by design, contributing towards more reliable  LM-based systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces an approach that enhances RAG by shifting from a retrieve-then-reason to a plan-then-retrieve paradigm, which improves efficiency and accuracy in handling complex queries through structured query decomposition. Contributions include:

- A directed acyclic graph (DAG) structure for decomposing complex queries into interrelated sub-queries, enabling information sharing and parallelized generation.
- Integration of "plug-and-play" experts, such as relevance and critic experts, to dynamically assess and refine retrievals without fine-tuning language models, reducing hallucinations.
- Improved attribution by design, as the DAG structure allows clear tracing of generated answers back to specific retrieved documents.

### Strengths
* Originality: The paper introduces a new plan-then-retrieve approach, which is a novel method of structuring complex queries by breaking them into smaller, linked parts using a DAG. This allows the model to handle parts of the query in parallel, speeding up response time and reducing errors. The addition of modular "plug-and-play" components, like relevance and critic experts, makes the framework adaptable to different models without retraining.
* Quality: The work is properly evaluated, with tests on multiple QA datasets that show Plan-RAG outperforms other RAG models in accuracy and relevance. Detailed experiments also demonstrate how each component (like the relevance and critic experts) contributes to the overall performance.
* Clarity: The authors explain the motivation behind their approach, and the experimental setup and findings are presented clearly.
* Significance: Plan-RAG could have an impact on how we use retrieval-augmented models, especially in fields where accuracy and traceability are crucial, like healthcare or financial services. The DAG structure could also inspire more structured reasoning approaches in other AI research areas.

### Weaknesses
1. The presentation of the overall framework is confusing. In Figure 2, there seems to be 7 agents, but only 4 out of them are explained in Section 3.2. It would be much clearer to present each of the components in parallel and to include an easy example to explain how each component works.

2. Comparison between the proposed method against Self-RAG and RQ-RAG is not fair. “We use the officially released code and associated models for both of these methods.” (L341) It does not make sense to “use the associated models for these methods”. To compare the RAG framework, the backbone models should be consistent. But Plan-RAG leverages Llama3-8b-Instruct, which is itself much stronger than Llama-2-7b and Llama-2-13b, used by the other two RAG baselines. Moreover, Plan-RAG utilizes GPT4o to generate the DAG, which is an essential step for the success of the entire framework.

3. While the modular "plug-and-play" experts add flexibility, they also introduce additional processing steps that require multiple LLM calls and make the overall system slower than single retrieval-then-reason paradigm, especially for real-time applications. The framework’s reliance on multiple experts could make it less suitable for time-sensitive tasks. To address this, the authors could evaluate the system’s runtime in more detail and consider simplifying the expert system or limiting the experts used per task, which would maintain performance without adding significant delays.

4. Plan-RAG’s DAG-based decomposition seems unnecessary for straightforward RAG use cases where queries are single-hop or require less complex reasoning. The paper could be strengthened by identifying specific types of tasks or scenarios where Plan-RAG’s complexity is justified. For broader usability, the authors could explore a simplified, “light” version of the framework that omits some complexity for single-hop or low-complexity queries.

5. The overall effectiveness heavily relies on constructing an accurate DAG that correctly represents the query’s reasoning process. However, creating such a structure automatically, especially for diverse or ambiguous queries, seems itself a challenging task. More experiments or analysis on the reliability and feasibility of automated DAG generation should be included, as would suggestions for how to handle or correct inaccurate DAGs. The authors could consider discussing potential fallback strategies when the DAG construction fails or is incorrect, or they could investigate ways to make the DAG-building process more robust.

### Questions
Why does the ablation study only focus on two experts? What about the importance of other experts?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a plan-based RAG model, called Plan-RAG, which decomposes a query into multiple subqueries and constructs a directed acyclic graph (DAG) based on the subqueries' hierarchy. The RAG system, using multiple LLM experts, traverses the graph to respond to the original query. Empirical experiments demonstrate that the proposed approach achieves competitive performance compared to other state-of-the-art models.

### Strengths
- The paper proposes a systematic approach to decomposing queries to address problems requiring multi-hop reasoning, enhancing the system's trustworthiness and interpretability.
 
- The proposed approach employs multiple LLM experts to make the system more efficient and effective.

### Weaknesses
 - Although the system applies DAG, the proposed approach doesn’t seem to offer a novel idea compared to other query decomposition methods (such as RQ-RAG and RA-ISF); it feels more like an incremental engineering effort.

- The experiments are not conducted thoroughly:
  - The authors use up-to-date LLMs, such as GPT-4 and LLaMA 3, to implement Plan-RAG, while using LLaMA 2 for other models (Self-RAG, RQ-RAG), which significantly hinders a fair comparison. Therefore, it would be beneficial to evaluate the comparative approaches using the same base models as those employed by Plan-RAG.
  - Since there are no comparative evaluations of Attribution, it is difficult to assess the performance of the proposed Plan-RAG. It would be desirable to compare Plan-RAG’s performance with other approaches in terms of Attribution.
  - Although the Critic Expert reduces the number of retrievals, the resulting performance is not promising. Additional analysis may be needed to assess how effectively the reduced retrievals provide context.


Typos and presentation errors:
- Line 238: q —> q ̃
- Line 279: retrieval(s) might be confusing.
- Line 314: There should be a space before ‘More’.
- Table 6 is only referenced in the appendix and not in the main pages.

### Questions
What is the reason the authors use different base LLMs to compare the proposed Plan-RAG with other state-of-the-art models, such as Self-RAG and RQ-RAG?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Plan-RAG, a *plan-then-retrieve* RAG framework that models the RAG process as a DAG, decomposing queries into subqueries and uses various expert llms to decide whether to retrieve and ensure the relevance of the retrieved documents.

In experiments, the paper compares the performance of Plan-RAG with recent SOTA methods, Self-RAG and RQ-RAG, on four QA datasets. The results demonstrate the effectiveness of the proposed method to some extent. In the ablation study, the paper emphasizes the importance of the critic and relevance expert designed in the Plan-RAG framework.

### Strengths
- The motivation of the paper is clear and the framework is easy to understand.
- The proposed framework can achieve superior performance compared to various baselines without fine-tuning the LLM.

### Weaknesses
1. There are some inconsistencies in the equations and symbols in this paper. For example, the symbol $v$ in eq (1) and on line 211 is not defined; the author might have meant $q$ instead? Also, on line 238, should $q$ be $\tilde{q}$?
2. The novelty of this paper needs further verification. Firstly, the "plan-then-retrieve" framework is not introduced for the first time in this paper; a very similar work can be found in [1]. Additionally, this paper's approach shares similarities with methods based on tool planning (viewing retrieval as a tool) and the multi-agent RAG framework. Moreover, methods related to query rewrite [2][3] and document relevance judgment [4] exist.

3. There are unfair settings in the baselines of Table 3. (1) In Plan-RAG, the most challenging planning process for llm is generated by GPT-4o, which is unfair for the standard RAG baseline. How would it be if planning were generated by Llama-8b or if GPT-4o were used as the model for standard RAG? (2) The baselines in the vanilla LLM are relatively weak; testing the effects of stronger models like GPT-4 or GPT-4o or Claude-3 would be more persuasive.

4. The performance of this framework on single-hop data seems unsatisfactory.

5. Two important benefits of Plan-RAG are efficiency and debuggability. However, the paper lacks relevant experiments to prove these points, and there seems to be no manifestation of debuggability in the methods section.

### Questions
1. Why does Plan-RAG perform poorly on single-hop tasks?
2. A term that consistently appears in this paper is "attribution," which is not explained in the paper in the context of the RAG system. How should this term be understood? I can only roughly infer its relevance to the granularity of subqueries from line 400. Is this understanding correct?
3. All steps of planning in this paper seem to be generated in a one-pass manner. In fact, another paradigm for planning involves iterative generation at each step (e.g. ReAct). How should these two paradigms be viewed in terms of the advantages and disadvantages for planning effectiveness?

### Soundness
2

### Presentation
3

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
The paper introduces Plan-RAG, a framework that shifts from the traditional “retrieve-then-reason” paradigm used to a plan-then-retrieve paradigm. Plan-RAG decomposes queries into atomic sub-queries using a reasoning Directed Acyclic Graph, which allows parallelized retrieval and generation. The system utilizes frozen language models as plug-and-play experts to guide retrieval and generation. This approach significantly reduces hallucinations, improves attribution, and enhances efficiency, especially for multi-hop reasoning tasks.

### Strengths
1. Plan-RAG offers a novel “plan-then-retrieve” paradigm with a reasoning DAG, providing a new way to handle complex queries in retrieval-augmented generation.
2. The framework is technically sound and evaluated across multiple datasets, demonstrating improvements in efficiency, hallucination reduction, and attribution.
3. The key concepts, particularly the reasoning DAG and plug-and-play expert system, are clearly presented with helpful examples and diagrams.
4. Plan-RAG addresses important challenges in hallucination and attribution, offering a scalable solution that works with frozen language models.

### Weaknesses
1. This paper lacks of the analysis on the DAG generation part. It remains unclear how does DAG performs vs. a plan without DAG structure. You could conduct an ablation study comparing Plan-RAG with and without the DAG structure.
2. This paper lacks of the error analysis about the results. For example, which module leads to the most errors and has the greatest impact on the model results. You could provide a breakdown of errors by different experts and to quantify the impact of each expert on overall performance. 
3. The paper only does experiments on an 8B model, which lacks of generalization experiments on different sizes models. How does the performance and efficiency of Plan-RAG scale with model size (e.g., GPT-4)?

### Questions
Due to the application of multiple experts, you may provide concrete latency measurements comparing Plan-RAG to baseline methods for an analysis of how latency scales with query complexity. It would be better if the authors could discuss potential optimizations to reduce overhead in real-world deployments.

### Soundness
3

### Presentation
2

### Contribution
3
