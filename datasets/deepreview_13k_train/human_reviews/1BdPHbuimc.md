# Chain-of-Action: Faithful and Multimodal Question Answering through Large Language Models

- Decision: Accept
- Scores: 8, 8, 5

## Abstract
We present a Chain-of-Action (CoA) framework for multimodal and retrieval-augmented Question-Answering (QA). Compared to the literature, CoA overcomes two major challenges of current QA applications: (i) unfaithful hallucination that is inconsistent with real-time or domain facts and (ii) weak reasoning performance over compositional information. Our key contribution is a novel reasoning-retrieval mechanism that decomposes a complex question into a reasoning chain via systematic prompting and pre-designed actions.  Methodologically, we propose three types of domain-adaptable `Plug-and-Play'  actions for retrieving real-time information from heterogeneous sources. We also propose a multi-reference faith score to verify conflicts in the answers.
In addition, our system demonstrates that detecting the knowledge boundaries of LLMs can significantly reduce both LLM interaction frequency and tokens usage in QA tasks. Empirically, we exploit both public benchmarks and a Web3 case study to demonstrate the capability of CoA over other methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces the Chain-of-Action (CoA) framework, a novel approach to multimodal and retrieval-augmented question answering that enhances the faithfulness and reasoning quality of large language models (LLMs). CoA addresses key challenges in QA, such as unfaithful responses and weak reasoning, by decomposing questions into a series of reasoning steps or actions that systematically retrieve and verify information from various sources. The framework introduces three "Plug-and-Play" actions—web querying, knowledge encoding, and data analyzing—that support multimodal data integration. Additionally, a multi-reference faith score (MRFS) is proposed to resolve inconsistencies and improve response accuracy. Experimental results demonstrate CoA’s effectiveness in handling complex questions across QA benchmarks and in real-world applications, particularly in the Web3 domain.

### Strengths
1. This study introduces a framework embodying the divide-and-conquer approach, effectively breaking down complex tasks into manageable components that are tackled sequentially. This structure enhances the model's ability to handle multifaceted queries with improved precision.

2. The empirical results demonstrate notable improvements in both performance and efficiency, as reflected in reduced API calls and token usage compared to prior methods. These gains underscore the framework’s effectiveness and potential for cost-saving in real-world applications.

3. The introduction of the multi-reference faith score (MRFS) is a contribution, which effectively identifies and mitigates information conflicts, and improves answer reliability and trustworthiness in real-time applications.

### Weaknesses
1. The paper’s primary weakness lies in how it presents its key concepts and narrative. Many claims, such as "multimodal," "plug-and-play," and "action-based" elements, lack direct evidence or clear definitions, making it challenging to follow the core contributions. Though the pipeline is straightforward, understanding the study's actual workflow is hindered by (1) inaccurate terminology, (2) loosely connected methodology descriptions, and (3) a mix of abstract workflows and technical details.

2. Certain terms are uncommon or seem misapplied, which leads to confusion. For example, terms like "multimodal" (when referring to text and tabular data), "chain-of-action" (more of a "chain-of-data-collection-and-verification"), "actions design" (data collection), "actions workflow" (data verification), "node" (sub-question), and "knowledge boundary" (what a model actually knows) lack clarity and could benefit from more precise definitions or alternatives.

3. Question decomposition appears critical to this framework, yet there is limited discussion on decomposition strategies or comparisons with existing baselines. Further elaboration here would strengthen the paper's contributions.

4. The "plug-and-play" feature is presented as a low-cost prompting strategy; however, integrating retrieval for each data type (e.g., web, internal knowledge) may not be straightforward. It may be worth reconsidering or refining this claim to better reflect its implementation complexity.

5. The paper’s claim of multimodal data handling is unclear. If the input consists of real-time information, domain knowledge, and tabular data, it may be more accurately described as handling heterogeneous data rather than multimodal data. Additionally, if tabular data is linearized as text for LLM input, the fundamental multimodal claim weakens.

6. The study does not include ablations to show the specific contribution of tabular data. Providing such analyses could clarify its impact on the framework's performance.

7. Section 3.2 mentions expert evaluation on a 1 to 3 scale based on three criteria, but it lacks details on the expert recruitment process, qualifications, and any inter-rater reliability metrics. Adding these details would increase the transparency and credibility of the evaluation process.

### Questions
1. Could you clarify what “imputation” refers to in Table 2? Are there results available for CoA without MRFS, and what does “w/ ROUGE” mean? My understanding was that ROUGE is used only in ASQA.

2. In Table 3, could you provide separate statistics for input and output tokens, as well as the average token usage per action? This would help readers better understand the specific cost details.

3. Could you elaborate on what is meant by the term “knowledge boundary”?

4. Are the results of the Chain-of-Action framework directly comparable to previous studies? I noticed that this study used GPT-4, while DSP and SearchChain relied on older-generation LLMs (text-davinci-002 and gpt-3.5-turbo, respectively).

5. Would it be fair and perhaps clearer to rename Sections 2.2.1 and 2.2.2 as "Data Collection" and "Data Verification," instead of “Actions Design” and “Actions Workflow”? These alternative terms seem easier to understand and align well with the content of the corresponding subsections.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a new QA retrieval mechanism called Chain of Action(CoA). When a question is asked to an LLM, there is a prompt which generates a list of actions the LLM needs to take first to effectively answer the questions. They introduce a Plug and Play approach where in case of Multimodal LLMs, the actions taken can be integrated into the application. The actions can be web query or data analysis. The paper integrates 3 such actions. The LLM then performs each of the individual action generated and then there is another query which combines information from all the actions. The LLM then gives an answer based on the newly injected information

### Strengths
1. The authors utilize newer multimodal LLM abilities to perform actions such as web query and data analysis. The authors come up with a new QA mechanism for LLMs which uses the actions The method is called Chain of Action(CoA).
2. The authors demonstrate that this method significantly outperforms other reasoning and QA methods on many QA datasets. 
3. The improvement of using actions over thoughts does seem to be the natural way of solving a question. This approach has significant potential for improving QA capabilities of LLMs.

### Weaknesses
1. Based on the number of actions to be taken and what kind of "plug" is used for the action, the time taken to finish all actions and send out an answer might become significant. It would have been good to see the study on latency(eg. average response time) of the system because of the new method.
2. It would be helpful to conduct an ablation study when you remove specific action types to isolate their impact on performance. This would provide clearer insights on how much this method relies on additional capabilities. Specifically, it would be beneficial to see the performance when only web search is removed, and when only local knowledge base search is removed.
3. Comparing CoA with and without the ability to perform additional "plugs" across different types of questions can be useful in understanding the impact of this method. It is important to understand how much the performance gain is because of the external tools and how much is because of the new framework.

### Questions
1. Can you elaborate on the key differences between "thoughts" in CoT and "actions" in CoA? How does this change improve the overall performance? It would also be helpful if you can discuss the limitations and trade-offs between them.
2. If the system doesn't have the ability to add additional actions like web query, does CoA still perform better than CoT. 
3. Does CoA add significant latency to QA process?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents the Chain-of-Action (CoA) framework designed to improve large language models' (LLMs) performance in multimodal and retrieval-augmented question-answering (QA). CoA addresses challenges such as hallucination and weak compositional reasoning by decomposing questions into reasoning chains. This method incorporates plug-and-play actions for retrieving diverse data sources and uses a novel multi-reference faith score for verification. Empirical results show CoA outperforms other methods in public benchmarks and real-world applications.

### Strengths
- **Innovative Framework**: The CoA's structured decomposition into sub-questions and its use of domain-adaptable plug-and-play actions represent a significant advancement in enhancing the faithfulness and accuracy of LLM responses.
- **Empirical Validation**: Demonstrated strong performance on benchmarks and real-world applications, notably outperforming existing baselines in multimodal QA tasks.
- **Verification Mechanism**: The multi-reference faith score is an effective metric for cross-validating LLM-generated answers against external sources, enhancing reliability.
- **Practical Impact**: Real-world implementation in a Web3 QA system showed increased user engagement and positive feedback, validating the method's applicability.

### Weaknesses
 - While the CoA approach shows strong empirical performance, its adaptability to more diverse or unstructured data modalities beyond text and tabular data remains to be proven. Specifically, the framework's ability to handle modalities such as audio, video, or complex sensor data is unclear, and the mechanisms for integrating these diverse data types into the reasoning chain are not well-defined.
- The scalability and efficiency when integrating more complex or real-time data sources require further exploration, especially in scenarios with rapidly changing information. The paper does not address the computational overhead of the proposed approach when dealing with large volumes of data or high-velocity data streams, which could be a significant limitation in practical applications. Furthermore, the latency introduced by the multi-step reasoning process and the retrieval of external sources is not thoroughly analyzed.
- The approach, despite its modular design, may face challenges in tasks involving higher-order reasoning or complex multi-step dependencies that are not purely fact-based. The framework's ability to handle tasks requiring abstract reasoning, counterfactual analysis, or intricate logical inferences is not demonstrated, and it is unclear how the system would manage scenarios where the reasoning path is not straightforward or requires recursive logic.

### Questions
1. Can the authors provide more details on how the CoA framework could be adapted for tasks involving visual or mixed data modalities?
2. How does the framework handle discrepancies or conflicts when sources provide contradictory information?
3. Are there plans to explore CoA's performance in real-time, fast-evolving information retrieval scenarios where data may change rapidly (e.g., live news events)?
4. Could the use of CoA extend to tasks requiring intricate reasoning paths that involve recursive or nested logic?

### Soundness
3

### Presentation
4

### Contribution
3
