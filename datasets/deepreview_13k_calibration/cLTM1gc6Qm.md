# Mockingbird: Platform for Adapting LLMs to General Machine Learning Tasks

- Decision: Reject
- Avg Score: 6.00
- Scores: 10, 3, 5

## Abstract
Large language models (LLMs) are now being used with increasing frequency as chat bots, tasked with the summarizing information or generating text and code in accordance with user instructions.
The rapid increase in reasoning capabilities and inference speed of LLMs has revealed their remarkable potential for applications extending beyond the domain of chat bots.
However, there is a paucity of research exploring the integration of LLMs into a broader range of intelligent software systems.
In this research, we propose a paradigm for leveraging LLMs as mock functions to adapt LLMs to general machine learning tasks.
Furthermore, we present an implementation of this paradigm, entitled the Mockingbird platform.
In this paradigm, users define mock functions which are defined solely by method signature and documentation. Unlike LLM-based code completion tools, this platform does not generate code at compile time; instead, it instructs the LLM to role-play these mock functions at runtime.
Based on the feedback from users or error from software systems, this platform will instruct the LLM to conduct chains of thoughts to reflect on its previous output, thereby enabling it to perform reinforcement learning.
This paradigm fully exploits the intrinsic knowledge and in-context learning ability of LLMs.
In comparison to conventional machine learning methods, following distinctive advantages are offered: 
(a) Its intrinsic knowledge enables it to perform well in a wide range of zero-shot scenarios. 
(b) Its flexibility allows it to adapt to random increases or decreases of data fields.
(c) It can utilize tools and extract information from sources that are inaccessible to conventional machine learning methods, such as the Internet.
Finally, we evaluated its performance and demonstrated the previously mentioned benefits using several datasets from Kaggle. Our results indicate that this paradigm is highly competitive.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
The paper introduces *Mockingbird*, a platform designed to adapt large language models (LLMs) for a variety of general machine learning tasks. The approach leverages LLMs' reasoning and in-context learning abilities through "mock functions," which enable LLMs to role-play predefined functions without needing traditional code implementations. This setup allows for interactive machine learning by transforming LLMs into flexible, general-purpose functions that adapt based on user feedback and system errors.

Mockingbird is distinctive in that it operates mock functions at runtime, bypassing compile-time code generation. Users interact with mock functions as they would with conventional functions, while the system dynamically manages function calls, converts data between formats, and validates outputs. The platform includes modules for "reflection" (learning from errors), "memory compression" (optimizing memory usage), and "substitution scripts" (code generation after adequate training), which enhance the robustness and efficiency of LLM-driven machine learning tasks.

Mockingbird demonstrates notable advantages: strong zero-shot and few-shot performance due to LLMs’ intrinsic knowledge, flexibility in handling incomplete data, and the capability to integrate tools unavailable to traditional methods. Evaluations on various machine learning tasks (e.g., classification, regression) suggest competitive performance, often surpassing human scores on some datasets. However, the paper identifies limitations, including LLMs' difficulties in self-correcting without feedback and challenges with tasks of higher complexity.

Overall, Mockingbird provides a paradigm shift for using LLMs in machine learning, focusing on efficiency, adaptability, and leveraging LLMs’ unique capabilities in broader intelligent systems.

### Strengths
The paper presents several notable strengths across originality, quality, clarity, and significance, offering a comprehensive approach to adapting LLMs for general machine learning tasks through the innovative *Mockingbird* platform. Below is an assessment of each dimension.

### Originality
Mockingbird introduces a unique paradigm that leverages LLMs’ capabilities beyond language processing, adapting them to various machine learning tasks by implementing mock functions that operate at runtime. This approach diverges from conventional methods of LLM utilization by bypassing compile-time code generation in favor of dynamic role-playing, which broadens the application potential of LLMs to areas previously inaccessible. The authors' incorporation of *reflection mechanisms*, which allow LLMs to learn from errors and refine responses over time, adds further originality, as this functionality is typically limited in standard machine learning frameworks. The use of LLMs as flexible, adaptive function substitutes demonstrates a creative synthesis of existing concepts, empowering LLMs to perform tasks traditionally assigned to symbolic or rule-based systems.

### Quality
The paper demonstrates a high standard of quality in both design and evaluation. The *Mockingbird* platform is well thought out, with clear specifications for mock functions, mock trainers, memory management, and substitution scripts. These components reflect careful consideration of performance, accuracy, and computational efficiency, addressing the key challenges that come with deploying LLMs in real-world intelligent systems. The authors provide rigorous empirical validation across multiple datasets from Kaggle, comparing *Mockingbird*’s performance against human benchmarks and conventional methods. The results are promising, showing that *Mockingbird* can often outperform human scores and exhibit robust zero-shot and few-shot capabilities, underscoring the quality and practical relevance of the platform.

### Clarity
The paper is clearly written and logically organized, making the technical details accessible and the platform’s contributions easy to understand. Complex concepts such as *mock functions* and the reflection mechanism are explained thoroughly, and the inclusion of high-level workflow diagrams enhances clarity by offering a visual breakdown of the system. Additionally, the authors carefully define the terms and structure of the mock functions, ensuring that readers unfamiliar with this kind of LLM application can grasp the framework and its potential. The clarity extends to the evaluation section, where performance metrics and dataset descriptions are presented in an easily interpretable manner.

### Significance
Mockingbird’s approach has significant implications for the field of machine learning and intelligent systems. By adapting LLMs to function as mock functions for general machine learning tasks, the authors demonstrate a novel way to harness the latent capabilities of LLMs, which can impact fields requiring flexibility, adaptability, and minimal data-dependency. This paradigm could serve as a foundational model for future systems that aim to integrate LLMs across diverse applications, especially where real-time adaptability and rapid learning from limited data are crucial. Furthermore, by proposing a method that requires minimal fine-tuning or data preprocessing, *Mockingbird* positions itself as a viable solution for practical deployment, potentially reducing the resource costs associated with traditional machine learning pipelines. 

In summary, *Mockingbird* presents a significant, original, and high-quality contribution to the application of LLMs in machine learning, broadening their scope and utility with a well-designed, clear, and adaptable framework. This platform has the potential to inspire further research and development in leveraging LLMs for non-linguistic tasks across a wide range of intelligent systems.

### Weaknesses
 While *Mockingbird* is a promising and innovative platform for adapting LLMs to general machine learning tasks, several weaknesses could be addressed to strengthen the work further.

### Limited Exploration of Baseline Comparisons
One notable limitation is the lack of detailed comparison with baseline machine learning models or alternative LLM-driven methods in more depth. While the authors compare *Mockingbird* to human competitors on several Kaggle tasks, a more rigorous analysis could involve benchmarks with established machine learning frameworks, such as scikit-learn, or even fine-tuned LLMs on the same tasks using standard training procedures. This would not only provide a clearer picture of *Mockingbird*'s performance relative to existing solutions but also highlight specific areas where the platform excels or falls short. Including performance benchmarks against these baselines on more complex, real-world datasets (such as those requiring deeper reasoning or specialized knowledge), particularly those with established benchmarks, would provide actionable insights into *Mockingbird*'s strengths and limitations.

### Scalability and Efficiency Concerns
Although the authors mention *Mockingbird*'s ability to reduce inference costs through substitution scripts, there is limited discussion on the scalability of this platform for larger datasets or environments where memory and computational resources are constrained. For instance, the current reflection and mock memory mechanisms may lead to substantial memory consumption and processing time as the number of invocations grows, particularly with longer reasoning chains. Further exploration of memory management techniques, such as more advanced context compression strategies, like those used in transformer models, or selective pruning of reflection notes based on their impact on performance, could enhance scalability, making the platform more viable in low-resource or high-throughput settings. A more comprehensive assessment of time and memory consumption across different LLMs, including smaller, more efficient models, would provide valuable guidance for deploying *Mockingbird* in various real-world contexts.

### Ambiguities in the Reflection Mechanism
While the reflection mechanism adds a unique learning dimension, the paper lacks clarity on how effectively this mechanism generalizes across diverse types of errors and tasks. For example, the platform could struggle with more nuanced errors, particularly in cases where initial invocations are flawed due to incorrect initial assumptions or where errors are complex and multilayered, such as in multi-step reasoning tasks requiring backtracking. Additional experiments that specifically measure how the reflection mechanism handles errors of different complexities, including those arising from logical inconsistencies or incorrect attribute assignments, and across a range of machine learning tasks could help delineate its robustness. Moreover, exploring alternative self-correction or meta-learning techniques, possibly by incorporating user feedback or additional task-specific criteria, might enhance the flexibility and reliability of the reflection process, especially in cases where the LLM's initial reasoning is significantly off-target.

### Limited Domain Exploration and Specificity
The paper evaluates *Mockingbird* on a relatively limited set of datasets from Kaggle, which may not fully capture the platform's potential across varied or specialized domains. This limitation is especially relevant given *Mockingbird*’s stated goal of general applicability. Incorporating datasets from more specialized fields (e.g., biomedical, financial, or scientific data), which often have unique data structures and require specific domain knowledge, would provide clearer insights into the platform's effectiveness and adaptability in specific, high-stakes applications. By demonstrating *Mockingbird*'s utility in niche or technically challenging tasks, the authors could better validate the generality and practical impact of their approach.

### Lack of Error Analysis and Interpretability
Currently, the paper lacks a robust error analysis to explain cases where *Mockingbird* performs suboptimally, particularly in tasks like the Horse Health Outcome Prediction. Understanding why the platform fails on certain tasks, potentially due to intrinsic biases or limitations in LLM reasoning, such as an over-reliance on specific features or a misunderstanding of domain-specific relationships, would yield actionable insights for further improvement. Additionally, including an interpretability component could help users understand *Mockingbird*'s predictions and errors, improving trust and usability. The authors could consider incorporating explainability methods (e.g., output sensitivity to input variations or traceability of the reasoning chain in reflection notes), which would help address the challenges users might face in interpreting model outputs, especially in complex tasks.

### Practical Constraints and Implementation Details
While *Mockingbird* presents a flexible and promising framework, the practical challenges of implementing it remain underexplored. Real-world deployment details, such as the costs associated with using commercial LLMs, latency issues, and hardware requirements, are not fully discussed. For instance, clarifying how *Mockingbird* performs under constraints like low latency or limited budgets, especially when using larger models, would add significant value for practitioners. Further discussion on potential optimizations or variations in LLM setups (such as use cases where smaller, more cost-effective models could be used or where model quantization techniques could reduce memory footprint) would also enhance the work’s applicability.

### Actionable Improvements
To address these weaknesses, the authors could:
1. Expand on baseline comparisons with existing ML and LLM-driven methods on complex tasks.
2. Provide an in-depth scalability analysis, especially focusing on memory and inference cost management.
3. Clarify and test the robustness of the reflection mechanism across diverse error types and complex reasoning tasks.
4. Demonstrate the platform's adaptability in specialized and domain-specific datasets.
5. Conduct a detailed error analysis and explore interpretability mechanisms to increase user trust.
6. Address practical constraints related to real-world deployment, potentially offering guidance on optimizing LLM configurations under resource constraints.

### Questions
1. **Clarification on Reflection Mechanism Robustness**
   - Could you provide more detail on how the reflection mechanism adapts to different types of errors across varied tasks? Specifically, does the mechanism struggle with more complex or multi-step reasoning errors? Additional information on whether the reflection process performs differently for tasks with high levels of complexity would clarify the flexibility and potential limitations of this component.

2. **Baseline Comparisons with Alternative Machine Learning Models**
   - To better assess *Mockingbird*'s advantages and limitations, could you expand on the rationale for selecting the current benchmarks? Would you consider adding direct comparisons with other machine learning models or frameworks, such as fine-tuned models, to give a fuller picture of the platform’s relative performance? Clarifying this would strengthen the validity of the claims regarding *Mockingbird*'s competitive advantages.

3. **Scalability and Memory Management in High-Throughput Settings**
   - What strategies do you envision for managing memory and scaling *Mockingbird* in high-throughput or resource-constrained environments? Since the reflection and memory mechanisms could become resource-intensive as the number of invocations grows, an explanation of any built-in controls or suggestions for extending *Mockingbird* in real-world applications with limited memory or computational power would be valuable.

4. **Error Analysis and Interpretability**
   - The paper could benefit from a more in-depth error analysis to explain cases of suboptimal performance, such as the Horse Health Outcome Prediction task. Could you provide more details on how intrinsic biases or model limitations might affect *Mockingbird*'s outcomes in these scenarios? Additionally, would you consider incorporating interpretability tools to aid users in understanding and trusting the model's outputs?

5. **Applicability to Specialized Domains**
   - Could you elaborate on how *Mockingbird* would perform in highly specialized domains, such as biomedical or financial datasets, where domain-specific knowledge or more complex reasoning may be required? Testing on such datasets would help validate *Mockingbird*'s versatility and potential for generalization, particularly in fields where accuracy and reliability are critical.

6. **Detailed Analysis of Inference Costs and Deployment Feasibility**
   - Real-world implementation details such as the costs associated with using commercial LLMs, latency issues, and hardware requirements are not fully addressed in the paper. Could you provide an estimate or guidance on the practical costs, especially for larger models in commercial settings? A discussion of potential cost-effective alternatives or guidance on deploying smaller LLM configurations would help practitioners consider *Mockingbird*’s feasibility in production environments.

7. **Plans for Future Work and Domain Expansion**
   - The conclusion suggests potential future directions for *Mockingbird*, particularly regarding real-time LLM inference. Could you elaborate on any specific domains or additional types of machine learning tasks you believe would be particularly well-suited for future implementations of *Mockingbird*? Expanding on this would help readers understand where the paradigm might have the most immediate impact or unique advantages.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores the possibility of using LLMs as mock-function-implementors focusing on machine learning tasks. It pits this idea against conventional machine learning methods and offers advantages such as (a) "intrinsic knowledge for free" (b) flexibility in terms of inputs and (c) potential to use agentic behavior to access external resources based on context. The paper describes the workflow of using the Mockingbird platform which involves users writing a mock function (function signature and docs describing the behavior) and an optional training phase where users can give a training set to the platform, which can use a reflection-style process to curate "few shot examples" for runtime usage. The platform takes care of prompting the LLM with function inputs and deserializing the LLM's outputs while providing schema-adherence (either using the LLM provider's built-in support, or reprompting the LLM if response does not adhere to the defined schema). The platform can also support plugging in different memory compression techniques to manage context length.

The paper evaluates the performance of GPT4o plugged with this platform on a few different Kaggle competitions (for classification and regression tasks) and finds that on 3 of them the platform achieves SOTA or competitive scores (while severely underperforming on some other contests).

### Strengths
The idea of using LLMs to implement mock functions is interesting.

### Weaknesses
1. The paper introduces a lot of ideas but does not substantiate them leaving the reader confused as to how exactly the idea might be implemented (even conceptually).
    - E.g., the entire bit about branching in mock memory is unexplained -- how are the branches used? Does the user of the mockingbird library/platform have to do something explicitly to use these branches? What purpose do they serve? Are they effective at whatever they are supposed to do (no evaluation)?
    - The idea of substitution script is not evaluated
    - Is reflection really effective? How well does Mockingbird perform when you just feed the training examples in a few-shot manner, without any "remarks" field?

2. Since the paper is trying to position itself as defining a new paradigm, it's important to explore the different design choices which the paper does not do at all. I do not think page limit is an issue because sections 1 and 2 have a lot of overlaps and a bit of rewriting could easily give some space for more thorough evaluation. Similarly, some parts in 3.2 could also be cut down (e.g., "Why cannot LLMs be “a good veterinarian”?").

3. The figures and descriptions are quite confusing.
    - E.g. I do not understand how the arrows work in Figure 1, and what is the "reasoning" component there, why it is separate from the LLM, what is the real-time information from external sources etc. 
    - E.g., "Based on the feedback from users or error from software systems, this platform will instruct the LLM to conduct chains of thoughts to reflect on its previous output" -- feedback from users/software systems? How that works is not explained in the paper, as the paper seems to position this platform as taking in a training dataset and using reflection style prompting to build a version of the "Mock Memory", which likely happens not at runtime but in training phase?

4. Some of the claims are not really valid. E.g., " Overall, it achieves very competitive scores " is not accurate when the method achieves 6 and 18 percentiles on two (binary?) classification datasets. "However, there is a paucity of research exploring the integration of LLMs into a broader range of intelligent software systems" is also not true (but that's not too concerning to me as that's not central to the paper).

### Questions
My main question to the authors is what are the advantages of using Mockingbird over directly prompting the LLM with examples? Given that LLM providers are already providing schema-adhering-responses as an option, the only two benefits I see are: (a) reflection setup for free (b) slightly more convenient interface because of integrating LLMs via mock functions. Is this sufficiently different than calling LLMs directly that we can call it a new paradigm?

I would in fact be quite happy with a library/framework that would let me write mock functions and let LLMs implement them _as long as_ there are sufficiently useful guarantees provided by the library, more than what I would get by raw prompting the LLM. E.g., automatically improving performance (as the authors are trying to do with reflection, but do not really evaluate it thoroughly), mocking stateful objects (it's unclear if the Mock Memory is meant for this also, or just for storing the few shot examples) etc. But these features would have to be evaluated meaningfully.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This research paper proposes a new paradigm called Mockingbird, which leverages large language models (LLMs) as "mock functions" to adapt them to general machine learning tasks. Mockingbird allows users to define mock functions, which are functions without code bodies but only with method signatures and documentation. At runtime, Mockingbird instructs the LLM to "role-play" these mock functions, enabling LLMs to perform tasks beyond traditional chatbot interactions. The paper discusses how this paradigm offers advantages over conventional machine learning methods, including handling zero-shot scenarios, adapting to fluctuating data fields, and utilizing external sources like the internet. The authors present an open-source platform implementing Mockingbird and evaluate its performance on various datasets from Kaggle, demonstrating its competitive capabilities.

### Strengths
This is a framework paper with good intuition.
1. The authors effectively use figures to illustrate key concepts, such as the Mockingbird workflow and memory management features. It demonstrates a good system design.
2. The paper demonstrates a good understanding of related work in LLMs, in-context learning, and code generation, with a comprehensive list of references.
3. The authors provide sufficient detail about the implementation, including system prompt construction and JSON schema validation.
4. The branch control feature of mock memories is fascinating. This LLM agent's memory update feature could also be applied to other memory-based agent frameworks to enhance consistency and coherence.

### Weaknesses
This paper has several weaknesses regarding the description of its methodologies and the scope of experiments conducted.
1. The author did not explain several key components regarding the memory systems and final execution.
    - The description of Section 2.4 is hard to follow. From the first paragraph, I can read about the intuition behind compressing and replacing memory, but how to conduct that memory compression is undefined. It would be helpful to provide a detailed description of your implemented memory compression algorithm or to include pseudocode for their approach, as the current description sounds more like a survey and compilation of different methods without a specific implementation. The current explanation lacks specifics on how the LLM is prompted to summarize reflection notes and what specific summarization techniques are employed.
    - If possible, the authors could create another figure to show how a substitution script is generated. I am extremely interested in what type of substitution script looks like. Is it a rule-based decision system with if-else statements? Experiments of the drop in accuracy after the translation are necessary, even if the authors believe this step is optional. The paper does not specify the exact structure of the generated code, nor does it provide any examples of how the substitution script is created, making it difficult to assess its impact.
    - If all the problems are binary classification and regression containing a single answer, why is JSON schema output necessary? I am not saying there are specific drawbacks, but introducing JSON schema for this simple scenario is confusing. Why don’t we just prompt the LLM as a multi-choice QA? The necessity of using JSON schema for simple tasks is not justified and seems like an unnecessary complexity, especially when simpler methods could be used.
2. Some of the claims in Section 3.2 Discussion do not convince me. The limited scope of the experiments conducted also raises some concerns.
    - All experiments are conducted within small Kaggle datasets. Several experiments showed poor performance against humans. We should either improve the performance to a reasonable point or include a more in-depth analysis of why MockingBird fails. The experiments lack sufficient scale and fail to demonstrate the robustness of the proposed approach. The poor performance against humans also raises concerns about the practicality of the method.
    - No comparisons of different base models are included. The authors recommend that the user fine-tune self-host LLMs, but it seems they were not responsible for this claim. If all the tasks are binary classification or regression, it would not be difficult to finetune an LLaMA-3 8B model to generate reasonable feedback. For example, experiments for closed-source models (i.e., GPT-4o-mini, Claude-3.5-Sonnet) and open-source models (i.e., Qwen-1.5,  LLaMA-3, Deepseek, and Mistral) would be helpful. Some models on Together AI do support JSON mode. The lack of evaluation across different LLMs is a significant oversight, especially given the recommendation to fine-tune self-hosted models. The paper does not explore how model selection impacts the performance of Mockingbird.
    - Longer context is not all you need. This analysis should not be drawn from your experiment results. The discovery, however, seems to be interesting, as a conclusion might be drawn from the intrinsic properties of these Kaggle tasks. One or two concrete examples from each experiment should be added to assist the analysis. It should be the properties of the tasks that lead to this phenomenon, not the phenomenon itself (i.e., longer context degrades performance in some tasks) that lead to this phenomenon. For example, illustrations of how LLM missed correct information among longer in-context examples may help. The analysis of context length is not well-supported by concrete examples, and the reasons for performance degradation with longer contexts are not well-explained.
    - Why Cannot LLMs Be 'a Good Veterinarian'? The reasoning is somewhat unclear, and the ideas jump between. 
      - The paper suggests that the higher number of data fields in the "Horses" task contributes to the difficulty. Explain why this might be the case. Could it be related to the increased complexity of relationships between variables, the potential for more missing data, or the increased difficulty in identifying relevant features?  You could explore the relationship between the number of data fields and task difficulty and provide concrete examples of how the "guessing trap" manifests in this task. This will be clearer if a trend of increased difficulty with more data fields is observed (i.e., a plot showing the decrease in performance). The paper does not provide a clear explanation of why increased data fields cause difficulty, and it lacks a concrete analysis of the "guessing trap" phenomenon.
      - The explanation of the "guessing trap" is too abstract. Use concrete examples from the "Horses" task to illustrate how the LLM might be making incorrect assumptions about its errors and how those incorrect assumptions lead to a lack of improvement. For example, you might outline the steps of their reasoning, supported by specific observations from your experiments on the "Horses" task. The "guessing trap" explanation lacks concrete examples, and the paper does not provide a detailed analysis of how the LLM's reasoning process fails.
3. A cost analysis is necessary for each task run. It seems to be extremely expensive to run one experiment with Mockingbird. Factors such as GPU hours, number of API calls (if using a commercial LLM service), and estimated financial cost will be helpful. The paper lacks a cost analysis, which is essential for assessing the practicality of the proposed approach. The lack of analysis of computational and financial costs makes it difficult to evaluate the real-world applicability of the method.
4. More ablation studies regarding each component of MockingBird are helpful. For example, could using serializers for both input and output boost performance? How and what information should be compressed within the memory compression steps? Or should we use a monkey patch substitution script directly generated by LLM in the training loop? Making two tables with suboptimal results is never enough for an ICLR-level publication. The paper does not include sufficient ablation studies to justify the design choices. The lack of analysis of individual components makes it difficult to understand their contributions to overall performance.

### Questions
In Section 2.4 Memory Replacing and Compression, should I interpret $mn^2 + 0.5mn$ as $\frac{1}{2}mn(n+1)$? I did not get why we have a $0.5mn$ term.

The ideology of treating LLM call as a function is not new [1].

From the supplementary material, is the original code for execution not included?

More works adapt LLMs to machine-learning tasks [2, 3, 4, 5], though not all are relevant to Kaggle competitions.

[1] Lin, C., Han, Z., Zhang, C., Yang, Y., Yang, F., Chen, C., \& Qiu, L. (2024, July). Parrot: Efficient serving of LLM-based applications with semantic variables. Presented at the 18th USENIX Symposium on Operating Systems Design and Implementation (OSDI 24), Santa Clara, CA. USENIX Association.

[2] Guo, S., Deng, C., Wen, Y., Chen, H., Chang, Y., \& Wang, J. DS-Agent: Automated Data Science by Empowering Large Language Models with Case-Based Reasoning. In Forty-first International Conference on Machine Learning.

[3] Liu, Y., Tang, X., Cai, Z., Lu, J., Zhang, Y., Shao, Y., ... \& Gerstein, M. (2023). ML-Bench: Large Language Models Leverage Open-source Libraries for Machine Learning Tasks. arXiv e-prints, arXiv-2311.

[4] Huang, Q., Vora, J., Liang, P., \& Leskovec, J. (2023). Benchmarking Large Language Models as AI Research Agents. In NeurIPS 2023 Foundation Models for Decision Making Workshop.

[5] Hollmann, N., Müller, S., \& Hutter, F. (2024). Large Language Models for Automated Data Science: Introducing CAFFE for Context-Aware Automated Feature Engineering. Advances in Neural Information Processing Systems, 36.

### Soundness
2

### Presentation
2

### Contribution
2
