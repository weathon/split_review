# ControlAgent: Automating Control System Design via Novel Integration of LLM Agents and Domain Expertise

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Control system design is a crucial aspect of modern engineering with far-reaching applications across diverse sectors including aerospace, automotive systems, power grids, and robotics. Despite advances made by Large Language Models (LLMs) in various domains, their application in control system design remains limited due to the complexity and specificity of control theory. To bridge this gap, we introduce \textbf{ControlAgent}, a new paradigm that automates control system design via novel integration of LLM agents and control-oriented domain expertise. ControlAgent encodes expert control knowledge and emulates human iterative design processes by gradually tuning controller parameters to meet user-specified requirements for stability, performance (e.g. settling time), and robustness (e.g., phase margin). Specifically, ControlAgent integrates multiple collaborative LLM agents, including a central agent responsible for task distribution and task-specific agents dedicated to detailed controller design for various types of systems and requirements. In addition to LLM agents, ControlAgent employs a Python computation agent that performs complex control gain calculations and controller evaluations based on standard design information (e.g. crossover frequency, etc) provided by task-specified LLM agents. Combined with a history and feedback module, the task-specific LLM agents iteratively refine controller parameters based on real-time feedback from prior designs. Overall, ControlAgent mimics the design processes used by (human) practicing engineers, but removes all the human efforts and can be run in a fully automated way to give end-to-end solutions for control system design with user-specified requirements. To validate ControlAgent's effectiveness, we develop  \textbf{ControlEval}, an evaluation dataset that comprises 500 control tasks with various specific design goals. The effectiveness of ControlAgent is demonstrated via
extensive comparative evaluations between LLM-based and traditional human-involved toolbox-based baselines.
Our numerical experiments show that ControlAgent can effectively carry out control design tasks, marking a significant step towards fully automated control engineering solutions.git}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces ControlAgent, a framework that automates control system design by integrating large language model (LLM) agents with domain expertise. The framework uses multiple collaborative agents to emulate human iterative design processes, gradually tuning controller parameters to meet user-specified requirements for stability, performance, and robustness. ControlAgent consists of a central agent that analyzes tasks and distributes them to specialized agents, task-specific agents that handle detailed controller design for different system types, a Python computation agent that performs control calculations and evaluations, and a history and feedback module that enables iterative refinement of designs. The system addresses the inherent complexity of control design by breaking down the process into manageable steps and incorporating domain knowledge into the decision-making process. The authors also develop ControlEval, an evaluation benchmark comprising 500 control tasks across various system types including first-order, second-order, systems with delay, and higher-order systems, with different response modes and specific performance criteria. This benchmark serves as a standardized way to evaluate control design workflows.

### Strengths
The core strength of this paper lies in how it successfully addresses the fundamental performance-robustness trade-offs inherent in classical control theory. The framework intelligently uses loop-shaping and PID tuning methodologies, employing settling time and phase margin as key tuning parameters - a sophisticated approach that mirrors established control engineering practices. The iterative design process is noteworthy for its theoretical soundness. Rather than treating controller design as a single-shot optimization problem, ControlAgent mimics the systematic approach used by human experts, progressively refining controller parameters while managing the complex interplay between performance metrics. The empirical results validate this approach, showing success across various system types and complexity levels, with particularly impressive results in handling unstable and higher-order systems. The framework's ability to achieve 100% success rates for first-order and stable second-order systems, while maintaining high performance even for complex higher-order and unstable systems, demonstrates its robust theoretical foundation and practical effectiveness.

### Weaknesses
 - The evaluation methodology raises several concerns. While ControlEval includes 500 control tasks, the paper doesn't clearly justify the distribution of these tasks or demonstrate their representativeness of real-world control problems. The generation process for higher-order systems is particularly problematic - the authors admit to manually designing these cases, which could introduce bias and may not reflect the true complexity of higher-order system control. Specifically, the paper lacks a clear explanation of how the 50 higher-order systems were selected, raising concerns about potential selection bias and whether these systems adequately represent the diversity of challenges encountered in real-world higher-order control problems. The manual design process makes it unclear if the chosen systems are truly representative or if they are skewed towards cases that are easier for the proposed method to handle.
- The comparison with baselines is somewhat limited. The paper primarily compares against relatively simple LLM-based approaches (zero-shot, few-shot) and a single traditional tool (PIDtune). Modern control design often employs more complex methods like robust control, model predictive control, or optimization-based approaches, which are notably absent from the comparison. The performance metrics are also relatively basic, focusing mainly on settling time and phase margin while overlooking other important characteristics like disturbance rejection and noise sensitivity. The absence of comparisons with robust control methods, such as H-infinity or mu-synthesis, is a significant oversight, as these methods are specifically designed to handle model uncertainties and disturbances, which are crucial in real-world applications. Furthermore, the exclusive focus on settling time and phase margin neglects other essential performance metrics such as overshoot, rise time, and steady-state error, which are equally important in assessing the quality of a control system design.
- The iterative design process lacks theoretical guarantees of convergence or optimality. The paper doesn't provide analysis of when or why the iteration process might fail, nor does it establish bounds on the number of iterations needed for convergence. The lack of convergence analysis raises concerns about the reliability of the method, as it is unclear under what conditions the iterative process will converge to a satisfactory solution or if it might oscillate or diverge. The absence of optimality guarantees also leaves open the question of whether the method finds the best possible controller or if it settles for a suboptimal solution. 
- The framework's heavy reliance on proprietary LLM models raises questions about reproducibility and practical deployment. The authors don't thoroughly explore how the system's performance might vary with different base LLMs or how it might degrade with smaller, more practical models. The lack of experiments with different LLM backbones makes it difficult to assess the generalizability of the approach and its sensitivity to the choice of LLM. The reliance on proprietary models also hinders reproducibility, as access to these models may be limited, and their performance may vary over time.

### Questions
- How does ControlAgent handle model uncertainty? While you discuss robustness through phase margin, could you elaborate on whether the framework considers parametric uncertainties or unmodeled dynamics?
- For higher-order systems, you mention manual design of 50 cases. Could you explain your methodology for ensuring these cases are representative and unbiased? What criteria guided your selection?
- For the history and feedback module, how do you handle the context window limitations of LLMs? Could you provide more details about the memory management strategy?
- Could you provide a more detailed analysis of failure cases, particularly for higher-order systems where performance was lower? Understanding these cases would help assess the framework's limitations.

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new paradigm that automates control system design via novel integration of LLM agents and control-oriented domain expertise. However, the writing style is confusing, making it hard to follow their ideas. I suggest the authors improve their academic writing skills by making the abstract more precise and brief, adding the approach section, and reorganizing the corresponding method section. Moreover, I do not know what scenarios the authors implemented or simulated for the experiments. There is no background information or introduction. Generally, this paper needs to improve largely.

### Strengths
This paper proposes a new paradigm that automates control system design via novel integration of LLM agents and control-oriented domain expertise to bridge the the complexity and specificity in control system design.

### Weaknesses
The paper's writing style is confusing, making it hard to follow their ideas. I suggest the authors improve their academic writing skills by making the abstract more precise and brief, adding the approach section, and reorganizing the corresponding method section. Moreover, I do not know what scenarios the authors implemented or simulated for the experiments. There is no background information or introduction. Generally, this paper needs to improve largely.

### Questions
As mentioned above, I suggest the authors improve their academic writing skills and design specific application scenarios, such as robotics and transportation, to verify their framework.

I recommend several papers, as shown below, in which authors can learn how to improve academic writing skills and organize corresponding ideas from them.

1) Yang, Q., & Parasuraman, R. Bayesian strategy networks based soft actor-critic learning. ACM Transactions on Intelligent Systems and Technology (TIST).

2) H. Hamann and H. Wo ̈rn, “A framework of space–time continuous models for algorithm design in swarm robotics,” Swarm Intelligence, vol. 2, no. 2-4, pp. 209–239, 2008.

### Soundness
2

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
This paper describes a composite LLM-based system for control tasks which attempts to design controllers, represented as Python code, for control problems with specific requirements, namely stability, phase margin, and settling time. 

While this paper is decently presented and seems to achieve decent results, I am uncertain about recommending it for ICLR. Primarily, the paper seems highly domain-specific and engineering-focused, rather than more general cutting-edge academic research. Still, it is a good engineering system. Secondly, I am uncertain about the evaluation. 

The proposed method is essentially a domain-specific application of LLM-modulo, e.g. an interative prompt with a verifier and critiques [1].

[1] Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S., ... & Murthy, A. B. Position: LLMs Can’t Plan, But Can Help Planning in LLM-Modulo Frameworks. In Forty-first International Conference on Machine Learning.

### Strengths
This paper addresses the issue of designing controllers using LLMs, in particular with specific stability, phase margin, and settling times. 

The overall system runs in a loop where a the designed controller is run and the system provides feedback based on a history of designs and how well they performed.

### Weaknesses
It seems guarantees would be desirable when working with control systems, and I assume the problem requirements are meant to be guarantees. However, I feel the paper would be made a lot stronger by discussing guarantees at length. 

The evaluation methods seem like they could be improved, in particular I would like the authors to clarify about "a system is considered successfully designed if at least one of the multiple independent trials results in a successful design". It seems this would greatly skew the statistics, since failures are being filtered out. I also don't see reporting of how many samples are taken to achieve the reported success rates. 

Given the unpredictable and error-prone nature of LLMs, I am skeptical that the overall system can work without a human in the loop or method for filtering correct answers. Also, it seems like intermediate mistakes in generation (e.g. a hallucinated constant) would collapse the entire system, so I would expect it to be rather fragile. To the extent that the proposed method works, I am curious what the authors attribute it to?

While the method is interesting, it seems to be an incomplete solution to a highly domain-specific problem, so I'm unsure about the larger impact of the work, e.g. the paper doesn't give much insight into designing general LLM-based systems.

### Questions
How much sampling is done of LLM-generated designs? e.g. is the budget 10 designs?

### Soundness
1

### Presentation
2

### Contribution
1
