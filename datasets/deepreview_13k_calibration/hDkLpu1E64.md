# FEABench: Evaluating Language Models on Real World Physics Reasoning Ability

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
Building precise simulations of the real world and invoking numerical solvers to answer quantitative problems is an essential requirement in engineering and science. We present FEABench, a benchmark to evaluate the ability of large language models (LLMs) and LLM agents to simulate and solve physics, mathematics and engineering problems using finite element analysis (FEA). We introduce a multipronged evaluation scheme to investigate the ability of LLMs to solve these problems by reasoning over natural language problem descriptions and operating COMSOL Multiphysics$^\textregistered$, an FEA software, to compute the answers. In addition to testing state-of-the art-LLMs, we further design a language model agent equipped with the ability to interact with the software through its Application Programming Interface (API), examine its outputs and use tools to improve its solutions over multiple iterations. Our best performing strategy generates executable API calls 88\% of the time. However, this benchmark still proves to be challenging enough that the LLMs and agents we tested were not able to completely and correctly solve any problem. LLMs that can successfully interact with and operate FEA software to solve problems such as those in our benchmark would significantly push the frontiers of their utility. Acquiring this capability would augment LLMs' reasoning skills with the precision of numerical solvers and advance the development of autonomous systems that can tackle complex problems in the real world.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces FEABench, a benchmark for evaluating large language models (LLMs) in physics, mathematics, and engineering tasks via finite element analysis (FEA), with COMSOL Multiphysics as the selected software. The authors point to limited research on LLMs handling complex numerical simulations crucial in these fields.

FEABench includes two datasets: 
- FEABench Gold with 15 human-verified problems offering quantitative targets, and 
- FEABench Large with 200 parsed problems from COMSOL tutorials, which often require plot generation or multi-value computations rather than single, verifiable outcomes.

The study observes that while LLMs generate executable code, they face challenges like selecting appropriate physics interfaces and avoiding inaccuracies. To address this, the authors designed a multi-turn LLM agent system to iteratively refine solutions via COMSOL API interactions, feedback, and specialized sub-agents. This agent includes: an algorithmic call sequence to reduce errors, combined LLM and API feedback for consistency checks, and methods to sustain correction attempts despite tool call failures. The agent system consists of sub-agents, such as a Controller for solution generation, an Evaluator for feedback, a Corrector for solution adjustments, and a Tool Lookup Agent for retrieving information.

Despite significant progress in execution accuracy, complete and correct solutions to benchmark problems are still to be achieved.

### Strengths
- Challenging Benchmark: FEABench introduces a novel and complex benchmark for assessing LLMs in physics, mathematics, and engineering tasks using FEA software, offering a way to evaluate these models in real-world problem-solving scenarios.
- Evaluation: FEABench goes beyond correctness checks by employing a multi-dimensional evaluation strategy, providing a more detailed view of LLM capabilities.
- Agent-Based Framework: The multi-turn agent approach illustrates the potential of combining LLMs with feedback systems and tool integration to tackle complex, iterative tasks more effectively. The agent reaches an executability score of 0.88 (88% of the generated code lines are executable). This is considerably higher than the single-shot approaches. The agent shows substantial improvements in interface factuality, interface recall, and feature recall, indicating a better understanding and use of physics concepts in the code. The agent successfully computes a "Valid Target" in two out of fifteen problems.

### Weaknesses
 - Limited Success: While the agent framework in FEABench improves code executability, this is not sufficient for overall benchmark success. While the agent computes valid target values in two problems, only one of those values falls within 10% of the ground truth answer. This is a crucial metric for determining true problem-solving success. Table 5 shows that the agent-based approach does not lead to significant improvements in code similarity compared to single-shot prompts. The agent showed only modest improvement in accurately setting properties of physics features, and it failed to fully solve any FEABench problem. This raises questions about whether the agent's search strategy is well-suited for tackling the benchmark's challenges.
- Absence of Agent Baselines: Although the paper proposes an agent-based approach, it does not provide a comparative analysis against existing (rich set of) LLM agent frameworks, making it difficult to assess improvements in code generation or overall performance. As a result, the primary contribution seems to be limited to the introduction of the FEABench dataset.
- The iterative nature of the agent-based approach involves multiple cycles of code generation, execution, feedback analysis, and code correction. This process can be computationally expensive, particularly when dealing with complex FEA problems that require significant computational resources for simulation.

### Questions
I would appreciate if the authors could elaborate on the novelty of their agent design, especially in comparison to the extensive existing literature on LLM agent development. Specifically, clarifying how their approach differs in structure, feedback mechanisms, or task handling would help understand the potential algorithmic advancements introduced in this work.

### Soundness
2

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
The FEABENCH paper measures how well an LLM can solve a problem that requires doing “FEA = finite element analysis” by creating a dataset of problems to solve. Solving an FEA problem requires calling a tool through a series of API calls to describe the problem, the COMSOL Multiphysics tool is used in this paper and the tool does the numerical computation to solve the problem described to it through the API calls. The LLM must map an english problem description to a series of API calls to be processed/executed by the COMSOL Multiphysics tool to produce the solution. The paper measures the accuracy of a solution across many different metrics like the executability of the API calls produced, the correctness of the model tree produced, and the correctness of the target value returned.

### Strengths
Solving difficult FEA problems is an interesting and challenging domain for an LLM to master, it’s good to keep pushing LLMs to more difficult problems and see where they break, and what are the limits.

### Weaknesses
W0: Having to get a COMSOL Multiphysics R license to run the benchmarks sounded quite expensive and problematic for folks to get that expense approved in most schools and companies, so that is why I said poor for Contribution because I think students/researchers will pick other benchmarks that are cheaper to work on improving, with easier more direct solutions to measure against. I feel like a very niche set of folks would want to bite into this benchmark, with the cost to buy the tool, and the python wrapper complexities and tedious boiler plate interface to describe problems.

W1: It feels like this is a bit of niche problem domain, so the general Web data a model is trained on wouldn’t help prepare the model super well to use the FEA tool and call it with the appropriate sequence of API calls to get the correct answer.  But if the model was fine tuned on a bunch of problems/answers then maybe it could do a ton better. Would be interesting to know if finetuning on more real or synthetic data would help, or how using many more few shot examples in the prompt would help. It wasn’t clear to me how much documentation and examples the LLM was given to solve each problem - I thought it said 1 shot.

W2: The benchmark is so difficult that no LLMs can solve any of the problems completely. It seems to me the benchmark should include some super easy problems so something is solvable. But I guess that is what all the other metrics provide to some extent.

W3: I’m not an FEA expert but it feels like problems in the FEA domain are rather difficult and it feels like the ability to score well on this benchmark requires the model to do well in understanding the physics of the problem, and then also the LLM’s ability to program to the FEA solver’s API to describe the problem properly requires a lot of ugly boilerplate code it appears. So it feel like it would be hard to see clearly where the model was messing up, in understanding the physics or in understanding how to turn the physics into code that reflects the LLM’s understanding.

### Questions
About how much did it cost in LLM $$$ to run the evaluations across the different LLM models and how long did it take the LLMs?  Of the run time was the FEA software run time significant in the Golden dataset?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper titled **"FEABench: Evaluating Language Models on Real World Physics Reasoning Ability"** introduces a novel benchmark for assessing the capability of large language models (LLMs) and LLM-based agents to perform finite element analysis (FEA) tasks. FEA is essential in many engineering domains for solving complex physical problems using numerical solvers. The paper tests LLMs' ability to read problem descriptions, reason over them, and interact with FEA software (COMSOL Multiphysics). It presents a benchmark called FEABench Gold, consisting of 15 manually verified FEA problems, and evaluates the performance of various state-of-the-art LLMs, such as Claude-3.5, GPT-4, and Gemini-1.5, in solving these tasks. The best strategy involved LLM agents capable of generating executable API calls for COMSOL. However, even the best-performing models struggled to solve any of the benchmark problems completely and correctly.

### Strengths
- The paper presents a novel benchmark focused on a crucial real-world domain (FEA) that has been underexplored in LLM evaluation. By requiring end-to-end reasoning from natural language to executable code for complex physics simulations, FEABench pushes the boundaries of what is currently possible with LLMs.

- The authors have taken care to ensure the problems are solvable, self-contained, and quantitatively verifiable. The evaluation framework is comprehensive, with multiple metrics capturing different aspects of solution quality.
- The inclusion of concrete examples (e.g., problem descriptions, code snippets) aids understanding.

- FEABench addresses an important gap in LLM evaluation by focusing on complex engineering problems that require both high-level reasoning and low-level code generation. Success on this benchmark could have major implications for automating engineering workflows. The multi-turn agent design also provides a valuable template for future work on LLM-based problem-solving systems.

### Weaknesses
 - **Lack of Comparison with Human Performance**: Including a baseline comparison of human performance on these FEA tasks would significantly strengthen the evaluation. This comparison should involve both novice and expert COMSOL users to provide a spectrum of human capabilities.  Expert evaluation is particularly crucial to validate task difficulty,  establish performance benchmarks, assess solution quality and check benchmark integrity. Specifically, the absence of human performance baselines makes it difficult to gauge the true difficulty of the FEA problems and whether the observed LLM limitations are inherent to the task or specific to current model architectures. The lack of human baselines also makes it difficult to determine if the benchmark is appropriately challenging, or if it is too difficult even for expert users, which would limit its utility.

- **Limited Success of LLMs**: Despite the interesting problem posed, none of the LLMs tested were able to solve the benchmark problems completely and correctly. A detailed examination of where and why LLMs fail could provide valuable insights, potentially revealing common patterns in errors across different models or problem types. It would be beneficial to discuss how current LLM architectures might be fundamentally limited for these tasks and whether specialized components for mathematical reasoning or code generation could improve performance. For example, are the failures primarily due to incorrect API calls, flawed physical reasoning, or an inability to translate the problem description into a coherent sequence of steps? A more granular error analysis is needed to pinpoint the specific bottlenecks.

- **Lack of LLMs Candidates**: To provide a more comprehensive evaluation of current LLM capabilities, it would be beneficial to expand the range of models tested. This should include open-source model families such as LLaMA, Mistral, and Qwen. Testing multiple scales within each model family could reveal how model size affects performance on FEABench.  If possible, evaluating domain-specific models trained on scientific or engineering corpora would add further depth to the analysis. This broader evaluation would provide a more complete picture of the current state of LLM capabilities on FEA tasks and could uncover interesting differences in how various model architectures and training approaches handle these challenges. The current selection of models is limited and does not fully represent the diversity of available LLMs.

- **Complexity of Task**: The paper could explore more how different levels of task complexity (e.g., simpler geometry or fewer physics variables) influence LLM performance. Additionally, the role of visual information from GUI could be better integrated into the evaluation process. The current benchmark does not adequately explore the impact of task complexity on LLM performance, making it difficult to understand the limitations of LLMs in handling varying levels of difficulty. The lack of integration of visual information also limits the evaluation to text-based problem descriptions, which may not fully capture the complexity of real-world FEA tasks.

- **Not So Good Presentation**: The paper's presentation and structure could be improved to enhance clarity and readability.

  - As a benchmark paper, it fails to provide a clear, concise overview of the datasets' composition and size. The distinction between FEABench Gold and FEABench Large is not well explained, leaving readers confused about the exact number of problems in each dataset and the rationale behind this split. A clear statement of the dataset sizes (15 problems in FEABench Gold and 120 in FEABench Large) early in the paper, along with a brief explanation of why two separate datasets were created, would significantly improve understanding.

  - The evaluation metrics section is another area that lacks clarity. Some metrics, such as the Code Similarity Score, are introduced without sufficient justification or explanation of their relevance. The paper acknowledges that "two different code blocks could generate equivalent model subtrees," which raises questions about the utility of this metric in evaluating solution quality. The authors should either provide a stronger rationale for including this metric or consider removing it if it doesn't contribute meaningfully to the evaluation. Furthermore, the paper fails to effectively communicate the motivation behind introducing domain-specific metrics. While these metrics may be crucial for evaluating FEA solutions, the paper doesn't clearly articulate why existing general code evaluation metrics are insufficient and how the new metrics address these shortcomings. A more detailed explanation of how these domain-specific metrics capture important aspects of FEA problem-solving that general metrics miss would strengthen the paper's contribution.

### Questions
- Exploring the impact of training data and fine-tuning strategies is crucial. Current LLMs may not have adequate coverage of FEA-related knowledge in their training data, and domain-specific fine-tuning or data augmentation could potentially yield significant improvements. Additionally, discussing the potential of hybrid approaches that combine LLMs with other AI techniques, such as symbolic reasoning systems or neural-symbolic methods, could provide valuable insights into addressing the observed limitations.

- Could the authors clarify the main factors that contributed to the models’ failure to solve any benchmark problems completely? Was it primarily API interaction errors, poor physical reasoning, or something else?
- Have any attempts been made to include human feedback in the agent loops (e.g., human-in-the-loop evaluation)? If so, how does that impact the success of the LLM agents?
- Given the difficulty of the FEA tasks, what improvements to LLM architectures or agent designs do the authors suggest to improve their performance in future iterations?
- Could the authors include specific examples from the FEABench dataset to enhance the clarity and understanding of the benchmark? Providing concrete problem examples, along with their corresponding model specifications and expected outputs, would offer valuable insight into the types of tasks the LLMs are expected to handle.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces FEABench for evaluating LLMs ability on solving physics, mathematics and engineering problems using finite element analysis software. The authors evaluate 3 LLMs on this benchmark and also develop a multi-turn LLM agent that can interact with the FEA software API to iteratively improve its solutions. Experimental results demonstrate that this benchmark is challenging.

### Strengths
To the best of my knowledge, this is the first systematic work on large language models manipulating complex computer software.
The benchmark is challenging.

### Weaknesses
1. The FEABench Gold dataset is relatively too small, with only 15 problems. Is it comprehensive? Please compare with other relevant datasets to show whether your dataset is relatively too small, e,g, SWEBench[1] (Agent Dataset), OSWorld[2] (Software Agent Dataset).
2. The work is not particularly outstanding in the context of LLM-Agent research and lacks sufficient references to related work in this area. Although the narrative is from a physics perspective, the overall approach is closely related to LLM Agent research.
3. The experimental evaluation is not comprehensive enough. It only explores 3 closed-source models. Other models, including many open-source ones, e.g., Llama, were not tested.
4. The study only considers one software, COMSOL Multiphysics, which may not fully capture the "REAL WORLD PHYSICS REASONING ABILITY" claimed in the title, e.g. ANSYS.
5. The paper does not consider the graphical user interface of COMSOL Multiphysics, which is crucial for using this software, as is shown in Figure 5 in your paper.

### Questions
Same as Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
