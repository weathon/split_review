# When Prompt Engineering Meets Software Engineering: CNL-P as Natural and Robust "APIs'' for Human-AI Interaction

- Decision: Accept
- Avg Score: 6.33
- Scores: 6, 8, 5

## Abstract
As large language models (LLMs) gain increasing capabilities, they are being widely applied in areas such as intelligent customer service, code generation, and knowledge management. Prompts written in natural language (NL) serve as the "APIs'' for human-LLM interaction. To enhance prompt quality, best practices for prompt engineering (PE) have been established, along with writing guidelines and templates. However, due to the inherent ambiguity of natural language, even prompts that strictly follow these guidelines often fail to trigger LLM to consistently output high quality responses, particularly for complex tasks. To address this issue, this paper proposes a Controlled Natural Language for Prompt (CNL-P) which incorporates best practices in PE. To overcome the NL's ambiguity, CNL-P introduces precise grammar structures and strict semantic norms, enabling a declarative but structured and accurate representation of user intent. This helps LLMs better understand and execute CNL-P, leading to higher quality responses. To lower the learning curve of CNL-P, we introduce an automatic NL2CNL-P conversion agent based on LLMs, which allow users to describe prompts in NL from which the NL2CNL-P agent generates CNL-P compliant prompts guided by CNL-P grammar. We further develop a linting tool for CNL-P, including syntactic and semantic checks, making static analysis techniques applicable to natural language for the first time. CNL-P’s design not only integrates best practices in PE but also adopts key principles from software engineering (SE). Extensive experiments show that CNL-P can improve the quality of LLM's responses through the novel and organic synergy of PE and SE. We envision that CNL-P has the potential to bridge the gap between emergent PE and traditional SE, paving the way for a new natural language centric programming paradigm.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
- This paper proposes the use of Controlled Natural Language (CNL) by framing prompts as a form of API, which allows users to harness AI model capabilities without needing in-depth technical knowledge.
- This work applies software engineering (SE) principles such as modularity, abstraction, and encapsulation to Controlled Natural Language (CNL), offering a structure that decouples prompts from code
- The authors conducted experiments to evaluate how effectively CNL-P adheres to design principles and whether CNL-P or template methods improve the quality of LLM responses.

### Strengths
- Clearly motivated framing of prompting as an API, enabling users to leverage AI model capabilities without extensive technical expertise.
- Strong connection to first principles in SE, providing a foundation to address challenges in complex NL-PL conversion and prompt-code coupling. This approach is particularly beneficial for language experts and non-technical users by effectively decoupling prompts from code.
- Dimensions to assess NL-to-CNL-P conversion quality are well-designed, covering diverse quality aspects.

### Weaknesses
 - The specific aims of the work remain unclear; while high-level challenges and design considerations are presented, the precise goals are hard to identify.
- Experiment setup in RQ1 lacks clarity on how the five dimensions are measured and how the 93 prompt instances were chosen. There are also no human validation results presented, even as partial samples.
- RQ1 primarily assesses design considerations, while RQ2 focuses on accuracy. Given the current setup and task scope in RQ2, the advantages of CNL-P are not fully apparent, as other models also perform well.
- For a more robust finding that CNL-P is better suited for weaker models, it would be beneficial to include additional experiments with weaker models beyond GPT-4-o mini.

### Questions
- Considering the setup and the consistency of output generation with single-turn GPT-4-o prompting, what advantages does CNL-P offer over single-turn generation with GPT-4-o?
- Given the broad goals of this work and the multi-faceted design of CNL-P, what rationale led the authors to focus on these three specific research questions?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces Controlled Natural Language for Prompt (CNL-P), a novel framework that bridges prompt engineering (PE) and software engineering (SE) principles to enhance the clarity, predictability, and effectiveness of prompts for large language models (LLMs). CNL-P addresses inherent ambiguities in natural language prompts by formalizing grammar structures and semantic norms. The work's primary theoretical contribution is the formalization of prompt engineering through SE principles, supported by a novel static analysis approach for natural language prompts and empirical validation across multiple LLM architectures.

### Strengths
Theoretical Innovation:
- Novel synthesis of SE principles with PE practices
- Comprehensive formal grammar for controlled natural language
- Innovative application of static analysis theory to natural language

Technical Contribution
- Formal specification of the CNL-P grammar
- Theoretical framework for prompt verification
- Rigorous performance analysis across LLM architectures
- Novel approach to static analysis of natural language

Research Impact:
- Opens new theoretical directions in prompt engineering
- Bridges formal methods and LLM interaction
- Provides a foundation for analyzing prompt properties
- Advances understanding of structured approaches to PE

### Weaknesses
Theoretical Limitations:
- Formal analysis of expressive power could be stronger. Specifically, the paper does not delve into the formal limits of the proposed grammar, such as whether it can express all computable functions relevant to prompt engineering or if there are inherent limitations in its descriptive capacity. A more rigorous treatment of the grammar's expressive power, perhaps using concepts from formal language theory, would be beneficial.
- Completeness properties of the static analysis need more discussion. The paper does not fully address the completeness of the static analysis approach. It is unclear whether the proposed static analysis can detect all possible errors or inconsistencies within CNL-P prompts, or if there are specific classes of errors that it cannot identify. A discussion of the limitations and potential blind spots of the static analysis is needed.
- Edge cases in the formal grammar require deeper analysis. The paper does not explore potential edge cases in the formal grammar, such as complex nested structures or ambiguous interpretations of keywords. A more thorough analysis of these edge cases is necessary to ensure the robustness and reliability of the grammar.
- Theoretical bounds need more rigorous treatment. The paper lacks a rigorous treatment of the theoretical bounds of the proposed approach. For example, it does not discuss the computational complexity of parsing or analyzing CNL-P prompts, or the scalability of the approach to large and complex prompts.

Methodological Concerns:
- Formal comparison with other structured approaches could be deeper. The paper does not provide a deep formal comparison with other structured approaches to prompt engineering. A more detailed comparison, perhaps using formal metrics or benchmarks, would be beneficial to understand the relative strengths and weaknesses of CNL-P.
- Statistical analysis could be more comprehensive. The statistical analysis of the experimental results could be more comprehensive. For example, the paper does not report confidence intervals or p-values, making it difficult to assess the statistical significance of the reported improvements. A more rigorous statistical analysis is needed to support the claims of the paper.
- Theoretical justification for design choices needs elaboration. The theoretical justification for some of the design choices in CNL-P is not fully elaborated. For example, the paper does not provide a clear rationale for the specific set of keywords or the structure of the grammar. A more detailed discussion of the theoretical basis for these design choices is needed.
- Formal properties of the conversion process require more analysis. The formal properties of the conversion process from natural language to CNL-P are not fully analyzed. It is unclear whether the conversion process is deterministic, reversible, or if it introduces any loss of information. A more detailed analysis of the formal properties of the conversion process is needed.

Validation Gaps:
Limited formal analysis of grammar properties.
Statistical significance analysis could be more rigorous.
Theoretical comparison with other formal methods needed.
Completeness of the static analysis approach not fully addressed.

### Questions
Comparative Evaluation: Could you provide a more detailed comparison of CNL-P’s functionality and usability versus DSPy, LangChain, and Semantic Kernel? Specifically, how does CNL-P’s approach to modularity and state management differ in terms of user accessibility and technical demands?

Advantages and Trade-offs: While CNL-P is designed to decouple prompts from code for accessibility, frameworks like DSPy offer robust control through tight integration with programming language abstractions. Could you discuss specific scenarios where CNL-P might outperform DSPy or vice versa, especially in terms of prompt complexity and user involvement?

Non-Technical Accessibility: CNL-P is described as more accessible to non-technical users than PL-based methods like DSPy and LangChain. Could you elaborate on any studies, tests, or qualitative comparisons you conducted to evaluate this claim? This would clarify the extent to which CNL-P lowers the barrier for non-programmers.

Performance in Practical Applications: Do you have insights or preliminary results comparing the performance and user experience of CNL-P with DSPy, LangChain, and Semantic Kernel in specific application areas (e.g., dynamic prompt generation or complex workflow management)? Real-world examples could strengthen the practical context of CNL-P’s advantages.

Future Integration with PL-Based Methods: Given that DSPy and other PL-based frameworks emphasize structured programming benefits, do you foresee potential for CNL-P to integrate with or complement these frameworks? A discussion on interoperability could highlight pathways for combining strengths across approaches.

Scoring and Evaluation: Can you elaborate on the specific criteria used to assign scores across the five evaluation dimensions (Adherence to Original Intent, Modularity, Extensibility and Maintainability, Readability and Structural Clarity, and Process Rigor)? Was there a weighting system applied to these dimensions, or were they treated as equally important?

Interpretability of Results: The table of results is challenging to interpret due to its minimal contextual information. Could you provide a more detailed breakdown or rubric that explains how scores were derived, potentially with examples of how different prompt types scored across specific dimensions?

Comparative Analysis: Did you consider using statistical measures to compare the performance of CNL-P, RISEN, and RODES across evaluation metrics? This could strengthen the validity of the reported improvements.

Presentation Improvements: The experimental results could benefit from a more visual presentation format, such as radar charts or bar graphs, for easier comparison across dimensions. Would you consider updating the results presentation in a revised version?

Completeness of Scoring Process: Did you perform any error analysis or additional validation to understand how CNL-P performs in specific scenarios where RISEN or RODES may excel, or vice versa? This would provide insight into potential edge cases for CNL-P.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Controlled Natural Language for Prompt (CNL-P), a novel prompt language to elicit high-quality responses from large language models (LLMs). CNL-P combines principles from software engineering with prompt engineering to create structured, accurate natural language prompts for interacting with LLMs. By defining clear syntax and components such as Persona, Constraints, Variables, and Workflow, CNL-P reduces natural language ambiguity and increases response consistency. Its structured, modular format allows for more reliable, maintainable, and interpretable prompts, acting as a natural “API” that makes human-AI interaction accessible and robust. In addition, the author proposed an NL2CNL-P agent to convert natural language prompts into CNL-P format allowing users to write prompts in natural language without expertise in learning syntax of CNL-P. A linting tool is proposed to check the syntactic and semantics of CNL-P. The experiments demonstrate the effectiveness of CNL-P in improving the consistency of LLM responses across various tasks.

### Strengths
1. The paper effectively combines prompt engineering and software engineering to introduce CNL-P as a structured, precise language for prompt design.
2. CNL-P’s modular design enables independent development, testing, and maintenance.
3. Its linting tool supports syntactic and semantic checks, which enables static analysis techniques for natural language.

### Weaknesses
I have several concerns regarding the evaluation section:
1. For RQ1, the authors asked ChatGPT-4o to assess the quality of conversions from natural language prompts to CNL-P or NL style guides based on five criteria. However, the reliability of this evaluation is not properly validated:
    - The authors did not provide evidence of how the evaluation results correlate with actual human evaluations, which would strengthen their claims.
    - There is no guideline detailing how the scale for each category is defined, which makes it difficult to interpret the numbers in Table 1.
2. For RQ2, the experiment lacks comprehensiveness:
    - Diversity of tasks: Currently, all tasks fall under the classification category. It would be beneficial to include more complex tasks, such as reasoning and coding, to better demonstrate the effectiveness of CNL-P. The classification tasks used, while diverse in subject matter, do not fully explore the potential of CNL-P in more complex scenarios.
    - The authors should conduct a more thorough evaluation across a broader range of both open-source and closed-source LLMs to validate the effectiveness of CNL-P. The current evaluation is limited to a small set of models, which may not generalize to other architectures or model sizes. Furthermore, the lack of ablation studies on specific CNL-P components makes it difficult to assess their individual contributions to the overall performance.
    - Insufficient error analysis of CNL-P across various LLMs and tasks: The performance of CNL-P varies among different models/tasks. The claim that weaker models benefit more from CNL-P lacks thorough discussion and validation. A comprehensive analysis should include task difficulty, the quality of natural language prompts, the quality of CNL-P, and their relationship to the task performance. The analysis should also consider the types of errors made by different models when using CNL-P versus natural language prompts.
3. Generalization of CNL-P:  
    - As all the tasks in the experiment are classification tasks, the natural language prompts should not be overly complex (correct me if I am wrong). Consequently, the paper does not sufficiently address how CNL-P performs with very large and complex prompts. It also fails to clarify whether the linting tool can handle such complex CNL-P. The lack of experiments with nested or recursive CNL-P structures also limits the understanding of its scalability.
4. In lines 789-799, the natural language prompt appears well-organized and detailed. I would like to ask:
    - For an effective CNL-P prompt, is such a level of detail and organization required from the human input?
    - How does the organization of the natural language prompt impact the quality of the converted CNL-P prompt?
    - Does the CNL-P prompt still outperform a well-organized natural language prompt?
5. The plots and figures for result analysis should be integrated into the relevant pages or paragraphs; otherwise, it is hard to follow the discussion and analysis.

### Questions
1. Which Llama model was used in your experiment?

### Soundness
3

### Presentation
2

### Contribution
2
