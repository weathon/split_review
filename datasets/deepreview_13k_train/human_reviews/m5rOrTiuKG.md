# ExploraCoder: Advancing code generation for multiple unseen APIs via planning and chained exploration

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
Through training on publicly available source code libraries, large language models (LLMs) can invoke multiple encapsulated APIs to solve complex programming problems.
However, existing models inherently cannot generalize to use APIs that are unseen in their training corpora. As libraries continuously evolve, it becomes impractical to exhaustively retrain LLMs with new API knowledge. This limitation hampers LLMs from solving problems which require newly introduced or privately maintained libraries. 
Human programmers often explore unfamiliar APIs by writing experimental code before invoking them for a more complex problem. 
Inspired by this behavior, we propose \textbf{ExploraCoder}, a training-free framework that empowers LLMs to invoke multiple unseen APIs in code solution by (1) planning a complex problem into several API invocation subtasks, and (2) exploring correct API usage through a novel chain-of-API-exploration.
Concretely,  ExploraCoder guides the LLM to iteratively generate several experimental API invocations for each simple subtask, where the promising execution experience are exploited by subsequent subtasks. This forms a chained exploration trace that ultimately guides LLM in generating the final solution.
We evaluate ExploraCoder on Torchdata-Github benchmark as well as a newly constructed benchmark that involves more complex API interactions.
Experimental results demonstrate that ExploraCoder significantly improves performance for models lacking prior API knowledge, achieving an absolute increase of 11.24\% over naive RAG approaches and 14.07\% over pretraining methods in pass@10. Moreover, the integration of a self-debug mechanism further boosts ExploraCoder's performance on more challenging tasks. Comprehensive ablation and case studies provide further insights into the effectiveness of ExploraCoder.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces ExploraCoder, a training-free framework designed for large language models (LLMs) to utilize unseen APIs to perform code generation (library-oriented code generation), enabling LLMs’ capabilities to adapt to new or private libraries without retraining. 
ExploraCoder decomposes a complex programming task into simpler subtasks, employing a chain-of-API-exploration (CoAE) method that iteratively generates, executes, and refines code snippets for specific API calls for each subtask. 
By doing so, ExploraCoder builds an experience trace, ultimately guiding the generation of correct final code.
The paper demonstrates improved performance in handling unseen APIs on the Torchdata-based benchmarks compared to other training-free methods, achieving competitive Pass@k and Success@k rates.

### Strengths
1. The problem of adapting LLMs to work with new APIs is a timely and important as it reflects the real-world need for adaptability in code generation, especially in environments with dynamic or proprietary libraries. Chain of API Exploration is innovative in the context of LLMs.
2. The framework for handling new APIs -- divide-and-conquer framework combined with iterative API exploration which mimics a human programmer’s exploratory approach is solid and well-supported. Interestingly, the self-debugging mechanism is well-integrated within CoAE.
3. The experimental design appears thorough, incorporating both existing and newly developed benchmarks to assess performance across tasks of varying complexity. The benchmarks are carefully constructed to highlight the challenges of multi-API invocation.
4. Results are clearly presented, with ablation studies and comparisons to relevant baselines (e.g., naive RAG, Self-Repair) supporting claims of improved performance

### Weaknesses
1. The use of similarity-based retrieval strategy for identifying appropriate APIs for subtasks may not be effective in case APIs are similar in functionality functionally  but syntactically different (e.g., APIs that share functionalities across domains or are named differently). This inherits the retrieval bias, which may hinder the subtask performance.

2. ExploraCoder may be sensitive to effective task segmentation, or selecting the optimal granularity for subtasks, where over- or under-decomposition may lead to errors or inefficiencies. The paper lacks a proper discussion and evaluation of how accurately they achieve optimal granularity.

* Furthermore, the paper does not specify how the model handles cascading errors in multi-API tasks, especially for the 
iterative CoAE mechanism and self-debugging.

3. While the paper sometimes implies that ExploraCoder can generalize across various API types, the benchmarks are limited to the Torchdata library, which may not fully represent and generalize to APIs in other domains. 

**Typos and Minor Errors**:
   - Page 1, Abstract: "niave" should be "naive."
   - Page 2, Section 1: "self-debug" is not consistently hyphenated throughout the paper.
   - Terms like "experience exploitation" and "trace" are not defined until later sections, which could confuse readers initially.

### Questions
1. How does the framework handle APIs with similar functionality but different syntax? How robust is the similarity-based retrieval in this setting?
2. Have you evaluated different segmentation strategies, and how did they affect model performance?
3. How often the framework must retry or debug when errors accumulate across tasks?

### Soundness
3

### Presentation
2

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
This paper introduces ExploraCoder, a framework for code generation that enables large language models to handle tasks involving multiple, previously unseen APIs. Traditional code generation models, even with RAG or API-pretrained knowledge, often struggle with complex tasks that require multiple API interactions due to limitations in retrieving and integrating diverse APIs effectively. Experiments demonstrate that ExploraCoder significantly outperforms traditional methods.

### Strengths
1.The results demonstrate significant improvements, and the experiments are thorough, covering comparisons with RAG frameworks and API-pretrained models across challenging benchmarks.

2.ExploraCoder operates without additional training, making it resource-efficient and easier to deploy, which is advantageous for real-world applications.

3.Clear and Well-Written Presentation: The paper is well-structured and clearly written, making the concepts and experimental setup easy to understand.

### Weaknesses
1.The iterative API exploration and self-debugging processes increase computational costs, especially for tasks with complex requirements and multiple APIs. While the framework is training-free, the runtime cost for each exploration cycle could be considerable, impacting scalability for larger applications (eg. repo-level?). The computational overhead, particularly the number of model calls and token consumption, needs to be thoroughly analyzed, especially as the number of API interactions increases. The paper should include a detailed analysis of how these costs scale with task complexity and the number of APIs involved, providing a clearer picture of the method's practical limitations.

2.I understand that creating datasets is expensive, but I am still concerned about the effectiveness of this method on other libraries. Although the paper demonstrates strong results on the Torchdata-Github and Torchdata-Manual benchmarks, without testing on a more diverse set of libraries, the robustness of ExploraCoder in real-world code generation tasks remains uncertain. The choice of Torchdata, while having some desirable properties, might not fully represent the diversity of real-world API usage patterns. The paper should address the potential for overfitting to the specific characteristics of Torchdata and discuss how the method would generalize to libraries with different structures and documentation styles.

3.ExploraCoder relies on timely execution feedback to guide subsequent steps in the API exploration chain. If execution feedback is delayed or unavailable, as might be the case in certain API-limited or high-latency environments, the framework’s performance could be negatively affected. The paper should discuss the implications of unreliable execution feedback and how the framework might handle such scenarios, including potential fallback mechanisms or error handling strategies.

4.The framework is designed to handle multiple unseen APIs, but it does not address how it would adapt to changes in APIs over time. As APIs evolve (e.g., deprecations, new parameters, or altered behavior), the effectiveness of previously explored solutions may degrade. Without dynamic updating, ExploraCoder could struggle with outdated API knowledge. The paper should discuss the need for a mechanism to update the API pool and how the framework would adapt to API changes, including the potential for automated updates or manual intervention.

5.The framework’s iterative exploration and debugging processes may produce opaque reasoning steps, making it difficult to understand or verify why certain API calls were chosen. This could hinder debugging or modifying generated solutions manually, which may be problematic for developers aiming to understand the rationale behind each API invocation in the final solution. The paper should provide more insight into the interpretability of the exploration process, perhaps by visualizing the decision-making steps or providing detailed logs of the API exploration process.

6.As mentioned in the paper, if an LLM has already learned new APIs, it would be highly competitive. How can you justify that this method remains competitive when compared to knowledge-update approaches? The paper should provide a more thorough comparison against models that have been updated with the target API knowledge, analyzing the trade-offs between the proposed method and knowledge-updated models, particularly in terms of performance, resource consumption, and adaptability.

7.(minor point) Naive RAG seems like a relatively weak baseline for complex multi-API tasks. Is there no better option to demonstrate that the method in this paper is powerful?

8.(minor point) The method appears straightforward and intuitive, but such process-oriented approaches seem to lack transparency, leading to potential uncontrollable risks in intermediate steps. How do you ensure that the intermediate outputs are reasonable?

### Questions
1.Given that iterative API exploration and self-debugging increase computational costs, how does this framework handle large-scale tasks, such as those at the repository level? Have you conducted any efficiency tests or optimizations for such large-scale applications?

2.While the method performs well on the Torchdata benchmarks, how confident are you in its effectiveness for other libraries or domains?

3.If an LLM has already been updated to include new API knowledge, it would naturally perform well. Can you elaborate on how ExploraCoder remains competitive against knowledge-updated models and whether it provides any unique advantages?

4.Are there more suitable baselines that could demonstrate the strengths of ExploraCoder more effectively?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces ExploraCoder, a framework that enables Large Language Models (LLMs) to generate code involving multiple unseen APIs through planning and exploration. The framework breaks down complex programming tasks into simpler subtasks, explores API usage through experimental code generation and execution, and leverages successful experiences to guide final solution generation. The authors curated two benchmarks: Torchdata-Github and the more chanllenging Torchdata-Manual. Authors evaluate their approach on two benchmarks, demonstrating significant improvements over baseline methods and conducting comprehensive ablation studies to validate their design choices.

### Strengths
- The problem was formulated clearly as a practical challenge in code generation
- The authors explain their proposed method clearly 
- Experiments show improvement over baseline models that the authors opt to compare against
- Various ablations especially on how different components contribute to the system's performance

### Weaknesses
The most significant concern I have is the limited novelty of this paper. The proposed ExploraCoder framework seems closely resembling existing code agent frameworks that can perform operations that cover what has been discussed in the paper, e.g., planning, reading code and code documentation, chain/tree-of-thought reasoing, and code execution, and iterations of all above. The core components of the proposed method, e.g., task planning, API recommendation, Chain of API Exploration, solution generator, etc. are methodologically similar to existing approaches in code agents. The paper does not sufficiently demonstrate how its approach fundamentally differs from or improves upon these existing methods, beyond applying similar techniques to the specific domain of unseen API usage.

A related weakness is the paper's related work. The authors have notably omitted discussion of recent advances in code agents, e.g., from swe-agent to AutoCodeRover to the leading ones on swebench. Without comparing against these relevant approaches, it's difficult to assess the true contribution of ExploraCoder to the field. 

Further, the comparison in experiments setting might not be fair. the proposed method requires significantly more model calls than the baseline approaches noted in the paper, as it involves multiple rounds of code generation, execution, and debugging for each subtask. However, this aspect is neither analyzed nor discussed in the paper. The authors should provide a detailed and transparent analysis of the computational overhead.

Finally, both benchmarks mentioned in the paper (Torchdata-Github and Torchdata-Manual) contain only 50 problems each, which is relatively small for drawing statistically significant conclusions. While the problems themselves may be complex and requires multiple API usage, the robustness and generalizability of the results are debatable given the small size of the benchmark and domain.

### Questions
See weaknesses above for the most critical ones on novelty, comparison of baseline methods, fairness in benchmarking, and scalability of the dataset.

In addition,

- Could the authors provide qualititive examples on 1) the benchmarks and 2) where the proposed method demonstrate improvements over baselines?

- On the dataset curation part (Line 843 onwards in A.5): could you elaboreate on 1) how the example programming tasks was created, and 2) how the expert review was done?

- A lot of useful content has been presented in appendix only. This creates troubles in the flow of the presentation. Please consider re-arrange the paper to make sure that the most critical and logically important topics are presented in the main content without the need of frequently referring to the Appendix.

- nit: there are some typos throughout the paper. Please fix them in next iteration. Some examples: 1) L30 niave->naive 2) L116 the citation should be We et al. 2022 instead of 2024. 3) L397: abosolue->absolute 4) L524 performe->perform 5) L922 sematics->sematics

### Soundness
2

### Presentation
2

### Contribution
1
