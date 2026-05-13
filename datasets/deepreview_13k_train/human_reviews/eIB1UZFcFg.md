# Look Before You Leap: Universal Emergent Mechanism for Retrieval in Language Models

- Decision: Accept
- Scores: 8, 6, 5, 6

## Abstract
When solving challenging problems, language models (LMs) are able to identify relevant information from long and complicated contexts. To study how LMs solve retrieval tasks in diverse situations, we introduce ORION, a collection of structured retrieval tasks spanning six domains, from text understanding to coding. Each task in ORION can be represented abstractly by a request (e.g. a question) that retrieves an attribute (e.g. the character name) from a context (e.g. a story). We apply causal analysis on 18 open-source language models with sizes ranging from 125 million to 70 billion parameters. We find that LMs internally decompose retrieval tasks in a modular way: middle layers at the last token position process the request, while late layers retrieve the correct entity from the context. After causally enforcing this decomposition, models are still able to solve the original task, preserving 70% of the original correct token probability in 98 of the 106 studied model-task pairs. We connect our macroscopic decomposition with a microscopic description by performing a fine-grained case study of a question-answering task on Pythia-2.8b. Building on our high-level understanding, we demonstrate a proof of concept application for scalable internal oversight of LMs to mitigate prompt-injection while requiring human supervision on only a single input. Our solution improves accuracy drastically (from 15.5% to 97.5% on Pythia-12b). This work presents evidence of a universal emergent modular processing of tasks across varied domains and models and is a pioneering effort in applying interpretability for scalable internal oversight of LMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies how LLMs internally solve retrieval tasks. To do this, they introduce ORION, a collection of 15 datasets and apply causal analysis to 18 LLMs. To solve the tasks in ORION, the LM has to combine information from the question and context into the last token position. The authors use residual stream patching on this last token to investigate how the LM decomposes and combines the information. They need 2 prompts for this; prompt1 = R1C1 and prompt2 = R2C2; R stands for Request (question) and C for context. They observe that depending on the layer where they do the patching, the model may output R1(C1) (answer to question 1 from context 1), R2(C2), or R1(C2). This means that the patching is intervening the model’s computation and combining high-level information from 2 prompts. With this, it is possible to supervise the internal process of the models and for example, make the model more robust to prompt injection.

### Strengths
* Extensive experiments on 18 LMs from 125M to 70B parameters on 15 datasets.
* Empirical evidence of internal decomposition of retrieval tasks. This can be very useful of the community to better understand the internal behavior of the models and improve their interpretability.
* Application to mitigate prompt injection

### Weaknesses
 * It remains unclear to me how to operationalize the request patching to mitigate prompt injection. It seems it requires a trusted input although lines 420 seem to indicate it doesn't. See more details on the question below.

 * in lines 450-451, it is written that you perform residual stream patching from the trusted input to an untrusted input. However, I couldn't understand how you obtain the trusted input. My understanding is that we only have an untrusted input in a real-world scenario, so this method is difficult to use. Line 420 says that you designed the application so that it doesn't require access to ground-truth labels, but isn't the trusted input the ground-truth label? To organize my questions a bit more:
   * What is this "trusted input" and how it differs from the ground-truth input?
   * How do you obtain the "trusted input"?

I still believe the application of this is limited to very specific scenarios with somewhat predefined inputs and vulnerable to prompt injections. Is my understanding correct? (regardless of the application, the knowledge about the internal workings of the LLM learned from this paper is valuable IMHO)

### Questions
* in lines 450-451, it is written that you perform residual stream patching from the trusted input to an untrusted input. However, I couldn't understand how you obtain the trusted input. My understanding is that we only have an untrusted input in a real-world scenario, so this method is difficult to use. Line 420 says that you designed the application so that it doesn't require access to ground-truth labels, but isn't the trusted input the ground-truth label? To organize my questions a bit more:
   * What is this "trusted input" and how it differs from the ground-truth input?
   * How do you obtain the "trusted input"?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces ORION, a diverse set of structured retrieval tasks designed to study how language models (LMs) handle complex information retrieval across six different domains. The authors conduct a comprehensive analysis on 18 open-source LMs with varying sizes and find that these models internally decompose retrieval tasks in a modular fashion. Specifically, middle layers process the request (e.g., a question), while later layers retrieve the relevant entity from the context. Through causal analysis, they demonstrate that enforcing this modular decomposition preserves a significant portion of the model's performance. Additionally, the paper presents a fine-grained case study and proposes a scalable method for internal oversight of LMs to mitigate prompt-injection attacks, significantly improving accuracy with minimal human supervision. This work provides insights into the universal modular processing of tasks in LMs and pioneers the application of interpretability for enhancing model oversight.

### Strengths
1. ORION represents a novel data-centric approach, facilitating a comparative study across 18 models and 6 diverse domains, enhancing the scope and depth of retrieval task analysis.
2. The fine-grained case study on Pythia-2.8b effectively bridges macroscopic and microscopic descriptions, adding a layer of detailed validation to the findings.
3. The insights gained from this study significantly contribute to the broader understanding of LM internals, influencing future design and optimization strategies.

### Weaknesses
1. Limited Generalizability Beyond ORION Tasks: While the study provides valuable insights into modular decomposition within the specific tasks included in ORION, there may be limitations in generalizing these findings to other types of tasks or real-world scenarios that are not represented in the ORION collection. The focus on single-token retrieval tasks, while simplifying analysis, may not fully capture the complexities of multi-token generation or tasks requiring more intricate reasoning. For instance, tasks involving complex question answering, summarization, or translation might exhibit different modularity patterns, which are not explored in this work. The study's conclusions about modular processing might not directly apply to these more complex scenarios.

2. Dependency on Specific Models and Versions: The analysis is based on a specific set of 18 open-source language models with varying sizes, which may not fully represent the behavior of all existing LMs or future iterations of these models. Additionally, focusing on specific versions (e.g., Pythia-2.8b) might introduce limitations related to the unique characteristics or limitations of those versions. The observed modularity could be an artifact of the training data or architectural choices of these specific models, and might not be a universal property of all language models. Furthermore, the fine-grained analysis on Pythia-2.8b, while insightful, may not be representative of the broader landscape of language models, limiting the generalizability of the micro-level findings.

### Questions
See the above weaknesses.

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
4

### Summary
The paper introduces ORION, a structured collection of retrieval tasks aimed at studying how language models (LMs) handle retrieval in various contexts. The research investigates 18 models, applying causal analysis to show that LMs use a modular approach to process retrieval tasks, with middle layers focusing on the request and late layers on retrieving context. The concept of request-patching is introduced to improve model oversight and counteract prompt injections.

### Strengths
- **Innovative Dataset**: ORION serves as a unique, structured dataset collection that enables comparative analysis across multiple models and retrieval scenarios.
- **Causal Analysis**: The study's use of causal interventions provides valuable insights into model behavior, highlighting a modular structure in how LMs process retrieval.
- **Proof of Concept**: Demonstrates a practical application for mitigating prompt injections using request-patching, enhancing model robustness in certain cases.
- **Thorough Evaluation**: The research assesses models across a range of sizes and tasks, reinforcing the applicability of findings.

### Weaknesses
 - The methodology focuses heavily on retrieval tasks and may not be immediately applicable to more complex scenarios involving multi-step reasoning or decision-making. The current scope limits the analysis to single-turn retrieval, neglecting the iterative nature of many real-world tasks where information is gathered and refined over multiple steps. This raises concerns about the generalizability of the findings to more dynamic and interactive contexts.
- Although insightful, the microscopic component analysis indicates that variability in task-solving components remains complex and less well-explained by the macro-level findings. The study identifies a modular structure, but the specific mechanisms within these modules and their interactions are not fully elucidated. This lack of fine-grained understanding limits the ability to predict model behavior in novel situations or to develop targeted interventions.
- The proof of concept for oversight is limited to retrieval tasks with single attributes, raising questions about scalability to broader, real-world applications. The request-patching technique is demonstrated in a controlled setting with simple queries, but it is unclear how it would perform with more complex, multi-faceted requests or in the presence of adversarial inputs. The practical utility of the approach remains uncertain without further validation.
- Further exploration of how these findings apply to closed-source models or those with different architectures would strengthen the paper’s generalizability. The current analysis is primarily focused on open-source Transformer models, leaving open the question of whether the observed modularity and request-patching effectiveness hold for proprietary models or those employing alternative architectures such as state space models.

### Questions
1. Can the authors discuss potential extensions of ORION to handle multi-attribute or more complex reasoning tasks?
2. How might the request-patching approach be adapted or extended for use in real-world, multi-step tasks?
3. Did the analysis include any comparisons between models fine-tuned with instruction-following data and those that are not?
4. Are there potential limitations or risks in applying request-patching to models with different architectures or training methods?

### Soundness
3

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
This paper investigates how language models (LMs) solve retrieval tasks across diverse situations. The authors introduce ORION, a collection of structured retrieval tasks spanning six domains, from text understanding to coding. They apply causal analysis on ORION for 18 open-source language models ranging from 125 million to 70 billion parameters. The study reveals that LMs internally decompose retrieval tasks in a modular way: middle layers at the last token position process the request, while late layers retrieve the correct entity from the context. The authors demonstrate a proof-of-concept application for scalable internal oversight of LMs to mitigate prompt injection while requiring human supervision on only a single input.

### Strengths
1. The introduction of ORION provides a valuable resource for studying LM behavior across a wide range of retrieval tasks. By creating a structured dataset with consistent abstract representations, the authors enable systematic comparisons across different models and task types. This data-centric approach is particularly useful as it allows for scalable analysis of LM behavior.

2. The discovery of a universal emergent mechanism for retrieval tasks across different model sizes and architectures is a decent contribution. The authors' finding that middle layers process the request while late layers perform retrieval suggests a fundamental organizing principle in LMs that was previously unknown. This insight could have far-reaching implications for our understanding of LM capabilities and limitations.

3. The paper demonstrates a compelling link between theoretical understanding and practical application. By leveraging their insights into the internal workings of LMs, the authors develop a proof-of-concept for mitigating prompt injection attacks. This application showcases the potential real-world impact of mechanistic interpretability research.

4. The study's comprehensive scope, covering 18 different models across various scales, adds robustness to its findings. This breadth allows the authors to identify patterns that persist across different architectures and training regimes, strengthening the generalizability of their conclusions.

### Weaknesses
1. While the paper identifies the modular decomposition of retrieval tasks, it lacks a deep exploration of why this decomposition emerges. The authors could strengthen their analysis by investigating how this modularity relates to the training process or architectural choices in LMs. For instance, they could examine whether the observed layerwise specialization correlates with specific attention patterns or activation distributions, and whether this specialization is a result of pre-training data biases or inherent architectural constraints. A more detailed analysis of the information flow across layers, including the specific computations performed at each stage, would be beneficial.

2. The study focuses primarily on retrieval tasks with single-attribute requests. This limitation raises questions about how well the findings generalize to more complex retrieval scenarios involving multiple attributes or nested queries. Expanding the analysis to include such tasks, for example, by examining how models handle conjunctions or disjunctions in queries, or how they manage nested dependencies, could provide a more comprehensive understanding of LM retrieval capabilities. Specifically, the study should investigate if the observed modularity holds when the model needs to integrate information from multiple sources or perform iterative retrieval steps.

3. The paper's case study on Pythia-2.8b reveals inconsistencies between macro-level modularity and micro-level component behavior. This discrepancy is not fully resolved, leaving open questions about how emergent behaviors arise from the interactions of individual components. A more in-depth analysis of this phenomenon, perhaps by examining the specific attention heads and their activation patterns, could provide valuable insights into the nature of computation in LMs. It is crucial to understand whether the observed micro-level variability is a form of redundancy or if each component plays a unique role that contributes to the overall modular behavior.

4. The authors' proof-of-concept for mitigating prompt injection is limited in scope. The experiment focuses on a narrow range of distractor types and only two model sizes. A more comprehensive evaluation, including a wider variety of adversarial inputs such as code injection or more sophisticated semantic manipulations, and a broader range of model architectures and sizes, would strengthen the claims about the method's effectiveness and generalizability. Furthermore, the study should investigate the method's robustness against adaptive attacks, where the adversary is aware of the defense mechanism.

5. The paper does not adequately address the potential limitations of the residual stream patching technique. For instance, it's unclear how sensitive the results are to the choice of patching layers or whether the observed effects could be artifacts of the intervention method itself. A more thorough discussion of these methodological considerations, including a sensitivity analysis of the patching parameters and a comparison with other intervention techniques, would enhance the robustness of the study's conclusions.

### Questions
1. How does the emergent modularity in retrieval task processing relate to the pre-training objectives or architectures of the studied LMs? Are there specific design choices that might promote or hinder the development of this modular structure?

2. Your analysis focuses on single-attribute retrieval tasks. How do you expect the observed mechanisms to generalize to more complex queries involving multiple attributes or nested retrieval operations? Have you conducted any preliminary investigations in this direction?

3. The case study on Pythia-2.8b reveals that individual components behave differently depending on superficial input features. How do you reconcile this micro-level variability with the macro-level modularity observed across tasks and models? What implications does this have for our understanding of emergent behaviors in LMs?

4. Your proof-of-concept for mitigating prompt injection shows promising results. Have you explored how this technique might scale to more diverse types of adversarial inputs or larger language models? What challenges do you anticipate in applying this method to real-world deployment scenarios?

### Soundness
4

### Presentation
3

### Contribution
3
