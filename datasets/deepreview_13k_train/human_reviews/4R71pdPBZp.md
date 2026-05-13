# Self-Evolving Multi-Agent Networks for Software Development

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
LLM-driven multi-agent collaboration (MAC) systems have demonstrated impressive capabilities in automatic software development at the function level. However, their heavy reliance on human design limits their adaptability to the diverse demands of real-world software development.
To address this limitation, we introduce EvoMAC, a novel self-evolving paradigm for MAC networks. Inspired by traditional neural network training, EvoMAC obtains text-based environmental feedback by verifying the MAC network's output against a target proxy and leverages a novel textual backpropagation to update the network.
To extend coding capabilities beyond function-level tasks to more challenging software-level development, we further propose rSDE-Bench, a requirement-oriented software development benchmark, which features complex and diverse software requirements along with automatic evaluation of requirement correctness.
Our experiments show that:
i) The automatic requirement-aware evaluation in rSDE-Bench closely aligns with human evaluations, validating its reliability as a software-level coding benchmark.
ii) EvoMAC outperforms previous SOTA methods on both the software-level rSDE-Bench and the function-level HumanEval benchmarks, reflecting its superior coding capabilities. The benchmark can be downloaded at \href{https://yuzhu-cai.io/rSDE-Bench/}{https://yuzhu-cai.io/rSDE-Bench/}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a multi-agent collaboration approach to address software development problems. EvoMAC obtains text-based environmental feedback by verifying the match between the MAC network's output and the target proxy, and it updates the network using a novel textual backpropagation technique, thereby achieving the final development outcome. Additionally, this paper introduces a software development benchmark called RSD-Bench, which provides more detailed and structured software requirements for documenting user needs compared to previous benchmarks. The final experimental results show that the proposed EvoMAC outperforms other single-agent and multi-agent methods on both RSD-Bench and HumanEval.

### Strengths
1. This paper proposes a multi-agent collaboration approach to address software development problems.
2. This paper introduces a software development benchmark called RSD-Bench, which provides more detailed and structured software requirements for documenting user needs compared to previous benchmarks.
3. Extensive experiments demonstrate that EvoMAC outperforms other single-agent and multi-agent methods on both RSD-Bench and HumanEval.

### Weaknesses
1. The benchmark proposed in this paper lacks data analysis and some basic statistical information, such as prompt length, the number of final generated files/functions, and the distribution of code length. Without these details, it's difficult to assess the complexity and diversity of the benchmark tasks. For instance, knowing the variance in prompt lengths would indicate the range of requirements the model is expected to handle, and the distribution of code length would help understand the scale of the generated code.
2. The benchmark proposed in this paper is relatively easy, with the EvoMAC method already achieving around 90% accuracy. This raises concerns about the benchmark's ability to effectively differentiate between various methods and its overall usefulness for pushing the boundaries of software development models. The high accuracy suggests that the benchmark may not be sufficiently challenging to expose the limitations of current approaches.


### Questions
1. Are there any issues with the citation format in the paper?
2. Does the paper lack an appendix?
3. In Table 2, there is no comparison of results with environment tools but without evolving. This should be added.

### Soundness
3

### Presentation
4

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
The paper introduces a novel framework called EvoMAC, aimed at enhancing the capabilities of LLM-driven multi-agent collaboration (MAC) systems in software development. The authors argue that traditional MAC systems are heavily reliant on human-designed workflows, which limits their adaptability and performance in real-world scenarios. EvoMAC seeks to overcome these limitations by enabling self-evolution of agents and their connections during task execution.

### Strengths
- This self-evolving paradigm allows MAC networks to adapt iteratively based on environmental feedback. The framework employs a mechanism similar to neural network backpropagation, where the output of the MAC network is verified against a target proxy, facilitating continuous learning and improvement.
- The RSD-Bench provides a structured benchmark for software-level coding tasks, focusing on comprehensive requirements rather than isolated functions.
- By incorporating unit tests and compilers as feedback mechanisms, EvoMAC reduces subjectivity and provides reliable feedback, which is critical for verifying the correctness of generated code. The objective environment-based feedback is an effective alternative to critique agents, which can introduce bias and hallucinations.

### Weaknesses
 - The EvoMAC framework introduces significant complexity with its multi-agent setup, dynamic adjustments, and textual backpropagation mechanism. This complexity may limit the framework's accessibility and implementation ease for real-world adoption outside of specialized research contexts. The intricate interplay of multiple agents, coupled with the dynamic adjustment of their roles and connections, presents a substantial hurdle for practical deployment. The textual backpropagation, while innovative, adds another layer of complexity that requires careful management and interpretation, potentially hindering its adoption in less specialized environments.
- Although EvoMAC performs well with large models like GPT-4o-Mini, its performance with smaller or less capable models is unclear. This reliance may restrict its applicability, particularly in environments with limited computational resources. The paper does not provide sufficient evidence that EvoMAC can maintain its performance with smaller models, which raises concerns about its practicality in resource-constrained settings. The lack of data on how the framework scales with different model sizes is a significant limitation.
- RSD-Bench focuses on website and game software types, which may not comprehensively represent the diversity of real-world software development tasks. Expanding the evaluation to include other domains, such as enterprise applications or data processing software, would enhance the generalizability of the results. The current benchmark is limited in scope, focusing primarily on web and game development. This narrow focus does not adequately capture the breadth of challenges encountered in real-world software development, such as enterprise systems, data processing pipelines, or embedded systems.

### Questions
1. How sensitive is EvoMAC to the quality and specificity of feedback from unit tests? If the unit tests are incomplete or overly general, would EvoMAC still produce reliable code, or would it require stricter validation criteria?
2. Can EvoMAC work effectively with models of different sizes, or does it rely on the power of high-capacity LLMs? Would it perform satisfactorily with smaller models that might be more efficient in constrained environments?
3. Can the self-evolving mechanism be applied to other domains outside software development? If yes, how?
4. Given EvoMAC’s iterative approach, how would it handle larger software projects with thousands of lines of code and extensive requirements? Are there specific design considerations for scaling it to more extensive projects?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents EvoMAC, a self-evolving multi-agent collaboration (MAC) network designed to advance LLM-based multi-agent systems beyond function-level tasks to software-level coding tasks. EvoMAC employs a unique textual backpropagation mechanism to iteratively update agents and their connections in response to text-based environmental feedback, effectively enhancing task completion without human intervention. By formulating the evolving process to analogize neural network training, EvoMAC provides a clear structure for defining and extracting improvements. This approach underscores the significance of iterative refinement in the software generation process, enabling continuous improvement and adaptability in complex coding tasks. 

To evaluate EvoMAC, the authors introduce RSD-Bench, a novel benchmark with complex and diverse software requirements that includes automated requirement verification. EvoMAC demonstrates superior performance on RSD-Bench and the HumanEval function-level benchmark, outperforming state-of-the-art methods and showcasing its robustness and adaptability across various evolving iterations and LLM configurations.

### Strengths
- Effectively demonstrates EvoMAC's evolution process as analogous to neural network training, establishing a reliable target proxy for evaluation and constructing a clear objective.

-  The paper is well-structured and easy to follow, with thorough explanations of EvoMAC’s self-evolving process,the design of the RSD-Bench, and detailed descriptions of experimental procedures. Figures and benchmarks illustrate the methodology effectively, aiding comprehension.

- By addressing limitations in traditional MAC systems and demonstrating EvoMAC’s efficacy on challenging software-level tasks, this work sets a promising precedent for adaptive agent frameworks in automated software development, making it valuable for both research and practical applications.

- The RSD-Bench is more practical in software generation evalaution, as it aligns closely with real-world software development process. By incorporating unit tests at both the task and function levels, it establishes a rigorous and precise mechanism for evaluating software generation quality. Additionally, RSD-Bench demonstrates strong human alignment (0.9922), providing a reliable evaluation metric. This paper also conducts analysis the reasonality of RSD-Bench in comparison to existing benchmarks, demonstrates its necessity. 

- This paper provides thorough experiments and analyses that robustly demonstrate EvoMAC’s effectiveness and performance. EvoMAC’s strong performance on both the RSD-Bench and HumanEval benchmarks highlights its high quality and efficacy in handling complex coding tasks.

### Weaknesses
 - Existing studies, such as [1-4] have also explored automation in LLM-based multi-agent collaboration. Please compare the differences between EvoMAC and these works.

- EvoMAC's updating process includes removing agents that have completed their tasks. Can the entire agentic workflow be replayed once a task is finished, or is the removed agent permanently excluded from further iterations?

- Given that EvoMAC includes multiple evolutionary iterations, direct comparisons with standard multi-agent frameworks may not be entirely fair. Could you also provide the number of LLM calls for tasks in RSD-Bench? This metric would offer a more clearer understanding of EvoMAC’s performance.

-  EvoMAC primarily focuses on models like GPT-4, Claude 3.5, and Gemini, but it is unclear if the framework can adapt to less powerful models, such as GPT-3.5 or open-source options like DeepSeek. Presenting results across a broader range of LLMs would support EvoMAC’s claims of robustness and adaptability.

- Can the authors provide additional examples of the unit tests designed within RSD-Bench?

- The Testing Team’s performance significantly impacts the Coding Team's potential, particularly in the HumanEval benchmark. How is the Testing Team’s performance evaluated to ensure alignment with target performance objectives and to prevent divergence? Additionally, how is the Testing Team’s performance quantified within RSD-Bench? 

-  The paper does not specify the stopping criteria for EvoMAC’s iterative evolution process. Could the authors provide details on the stopping mechanism or criteria? 

- The paper lacks specific settings for the Coding Team in both the HumanEval and RSD-Bench benchmarks. Please provide these details to improve clarity on the experimental configuration and consistency across benchmarks.

- Could the authors showcase additional examples of the textual gradient analysis and the updating process during the evolution for HumanEval and RSD-Bench?

### Questions
Please refer to the questions in Weaknesses.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors provide a paper with twofold contribution: i) a new approach to developing multi-agent collaboration systems for software development and ii) a benchmark to compare their approach with existing approaches to solving the same problem.
Regarding (i), their approach (called EvoMAC) intends to overcome the limitations of similar multi-agent collaboration systems development workflows, mainly on adaptability and generalization. EvoMAC was designed to mimic standard neural network development, meaning that the errors are "backpropagated" throughout the agents, creating a self-adaptive multi-agent network.
Regarding (ii), the benchmark dataset RSD-bench was created based on the requirements of the software being developed, in contrast to the existing ones, which are usually based on the functionality of the generated code/software (i.e., unit tests).
The paper's results show that the EvoMAC approach outperforms other approaches when applying the RSD-Bench to adapted versions of standard benchmark datasets like HumanEval.

### Strengths
The paper is very well written and clearly explained. The two proposed contributions (the EVoMAC approach and RSD-Bench dataset) are consistent with the objective expressed in the introduction.
Altough the problem of how to (self-)organize multi-agents is not exactly a new problem, the rise of agentic approaches using LLMs brought new traction to this challenge, and the authors addressed a pain point on these approaches when dealing with complex software development. Indeed, most solutions rely only on function-level and ignore the requirements engineering perspective, which ultimately leads the developers to half-baked solutions. This is not the case with the proposed EvoMAC. It takes account of the particularities of user requirements when organizing the agents initially and also considers the evaluation of the generated code against initial requirements.
Their inspiration for neural network algorithms is broad. However, it is also a clever idea that sounds original and demonstrates a creative adaptation of backpropagation principles to multi-agent collaboration.
The authors also provide sound experimentation on how they implement their approach and when comparing with similar solutions.
Together with the approach, the authors provided a well-defined benchmark to overcome the limitations of the existing ones. A more detailed description of the RSD-bench could indeed compose a contribution per se.
The RSD bench is tailored to requirements engineering, which could address common limitations in agent-based collaboration research by bridging functionality-based assessments with requirement-based evaluations.

### Weaknesses
Most of the paper's weaknesses are minor problems that can improve its quality, even though I don't consider them mandatory.
- I truly believe that the mathematical explanation of the problem (mainly between lines 169-184) is unnecessary, even though I see that this somehow facilitates some later explanations. Altough it provides some kind of generalization, the approach still relies on LLMs that are probabilistic by nature and then are not mathematically generalizable (i.e., the function $\phi(\cdot,\cdot)$ is essentially a message sent to an LLM, so it does not behave exactly as a mathematical generic function as the authors may want to demonstrate). I advise the removal of the mathematical explanation. It can help sometimes but does not add value to the paper.
- The paper lacks an actual example/use case in the opposite (or complementary, if the authors decide to keep it) of the mathematical explanation. The authors use this type of explanation in lines 270-271. This kind of example can be used as a running example throughout the paper.
- Minor problems:
	- Typo on the Figure 3 caption. "indrection"
	- Figures 6 and 8 can be improved to ensure legibility and accessibility, maybe by adjusting font size and contrast.
	- Figure 1 is a bit confusing. I think it can be split into 3 different figures or be better explained in the paper. If kept as is, I suggest adding brief explanations of the arrows, such as "add," "revise," and "remove."
	- Figure 5 can be rethought with a better color choice, especially considering the accessibility of the paper.

### Questions
- When explaining their approach (section 3.1), the authors did not mention problems regarding the context window of most LLMs. Since requirements can contain quite a large amount of textual data, is the approach capable of dealing with it without extra techniques (e.g., RAG)? If not, even though the authors did not highlight it as a problem, the context window limitations should be mentioned.

### Soundness
3

### Presentation
4

### Contribution
3
