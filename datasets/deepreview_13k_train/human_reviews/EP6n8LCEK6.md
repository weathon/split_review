# Understanding Prejudice and Fidelity of Diverge-to-Converge Multi-Agent Systems

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Large language model (LLM) agents have demonstrated substantial potential across various tasks, particularly in multi-agent systems. Among these, \textit{Diverge-to-Converge} (D2C) frameworks stand out for their ability to iteratively diversify and converge intermediate thoughts to improve problem-solving. In this paper, we conduct a comprehensive study on the \textit{\textbf{prejudice}} and \textit{\textbf{fidelity}} of typical D2C frameworks, including both model-level and society-level frameworks. 
\ding{182} In the \textit{prejudice} section, we uncover an inherent \textit{confirmation bias} in D2C systems, which not only leads to suboptimal performance, but also amplifies social biases, such as gender discrimination and political partisanship. Surprisingly, we find that by reframing open-ended problems into controlled initialized problems, this bias can be leveraged to foster more equitable and effective agent interactions, ultimately improving performance.
\ding{183} In the \textit{fidelity} section, we explore the scaling laws of D2C frameworks at different granularities, revealing that increasing the number of agents enhances performance only when the system is not yet saturated---such as in complex tasks or with weaker agents. In saturated scenarios, however, adding more agents can degrade performance. 
To facilitate further study, we develop \texttt{APF-Bench}, a benchmark specifically designed to evaluate such inherent weaknesses of D2C frameworks. 
We hope our findings offer instructional insights into the strengths and limitations of D2C multi-agent systems, offering guidance for developing more robust and effective collaborative AI systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper examines the limitations of Diverge-to-Converge (D2C) frameworks in large language model (LLM) agents, focusing on prejudice and fidelity. It reveals a confirmation bias in D2C systems that hampers performance and amplifies social biases, but reframing open-ended problems as binary questions mitigates these effects. The study also shows that increasing the number of agents only improves performance under unsaturated conditions. Additionally, the authors introduce APF-Bench, a benchmark to evaluate these weaknesses, providing insights for building better collaborative AI systems.

### Strengths
1. It uncovers and addresses *confirmation bias* in D2C frameworks, providing practical solutions to mitigate performance issues and social biases.
2. The study examines both*prejudice* and *fidelity*, offering a detailed understanding of D2C frameworks across multiple levels.
3. By demonstrating how reframing problems into binary questions improves fairness and effectiveness, the research has real-world applicability.
4. The development of *APF-Bench* as a dedicated tool for evaluating D2C systems is a valuable resource for future research.
5. The analysis of scaling laws provides essential guidelines for optimizing agent collaboration in different task scenarios.

### Weaknesses
1. Limited Real-World Testing: The findings might lack generalizability if not tested in diverse, real-world multi-agent scenarios.
2. Potential Oversimplification: Reframing problems as binary questions may oversimplify complex tasks, possibly limiting the depth of solutions.
3. Scalability Constraints: The performance degradation observed in saturated systems indicates a limitation in scaling D2C frameworks effectively.
4. Bias Mitigation Trade-offs: While the approach reduces biases, it may inadvertently introduce new limitations or biases in certain contexts.

### Questions
* Why do you study D2C frameworks rather than other MAS frameworks? Is D2C a typical and widely adopted MAS framework? What are the incentives behind this choice?
* What is the main *contribution in scientificity* that the paper claims? This paper does a lot of evaluation and analysis on different LLMs, but they are the existing ones. Could you provide insights into designing LLMs that can inherently avoid or mitigate confirmation bias? Or, can you give a discussion on the underlying causes of such bias, which could possibly arise at the data level or the pre-training/fine-tuning level instead of solely empirical discovery? 
* See also Weaknesses for other questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors investigate reasoning pathologies of a certain class of multi-agent LLM systems, Diverge-to-Converge (D2C) frameworks, both at the model- and society-level. The authors identify an inherent confirmation bias in D2C systems but results in social biases and task underperformance which can be alleviated if open-ended questions are re-phrased as binary. The authors then study the scaling laws of D2C frameworks, finding that more agents does only result in performance improvements if the system is not yet saturated but can otherwise even degrade performance. The authors suggest remedies for both these pathologies and release APF-Bench to specifically evaluate these weaknesses.

### Strengths
* Very timely and can provoke thought - e.g. trade-off bias/compute
* Robust evaluation across multiple datasets
* the idea to use reframing to tackle biases seems novel

### Weaknesses
 * Could have discussed a greater variety of biases other than confirmation bias
* It isn't clear how questions of real-world importance that are open-ended can always be brought into binary form.
* conceptual advances are limited - scaling laws / reframing techniques themselves feel rather incremental

line 216 "menifest"

### Questions
* How do you prevent bias in the debate judgements?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper conducts a study on confirmation bias from initial responses in different multi-agent LLM setups and comes up with a technique to prevent this bias (and thus improve benchmark performance) by changing the framing of questions. It then presents very initial work on how multi-agent system performance scales with the number of agents and tokens.

### Strengths
- The paper presents a very comprehensive review of existing multi-agent LLM research and fits in prejudice and fidelity quite well in these settings. This provides useful context to understand the paper’s key contributions.

- The problem reframing method is reasonably novel and the experimental evaluations are comprehensive enough to demonstrate improvements with this method.

- It presents initial interesting results around differences in scaling the number of agents/LLM calls versus the number of tokens per generation. This could allow for a lot more future work in multi-agent LLM research.

- APF-Bench encompasses other benchmarks and can act as a useful starting point for similar research directions.

### Weaknesses
 - The paper explores only problem reframing as a bias mitigation strategy. However, not every problem can be converted into a binary problem, and other strategies are not explored at all.

- The paper does not perform evaluations on any open source models.

- The refinement strategy for datasets could introduce selection bias and skew results. I would be interested in seeing results across a random subset of the test set on the benchmarks used.

- The paper spends its first 5.5 pages providing a background on the problem and multi-agent LLM settings. This takes away from its key contributions, which are limited to the problem reframing strategy and very introductory work on scaling laws around fidelity. Section 6.2 is extremely limited and does not back up its claims with linked experiments.

- The appendix presents examples of model outputs, however it does not provide examples of inputs to the models (especially in the problem reframing setting). I’ve posed questions around these examples in Questions section of my review.

### Questions
- Page 18, Case 2, GSM8k: Could the authors provide complete inputs to the models and their outputs for each iteration?

- Is there a hypothesis around why the results hold and such biases occur in language models? Are there reasonable tests that can be conducted around this?

- Could there exist better reframing techniques? Why was the binary reframing technique selected? Will it work for all tasks?

Update - these questions have been answered by the authors.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the Diverge-to-Converge (D2C) frameworks and highlights the challenges of prejudice and fidelity in D2C frameworks. The authors define prejudice and fidelity as the performance variation under changed conditions and scaling laws, respectively. To evaluate prejudice and fidelity, this paper introduces APF-Bench using the proposed Dataset Refinement. The results confirm the findings.

### Strengths
1. The paper is well-structured and easy to follow. The inclusion of informative figures and tables enhances clarity.
2. This paper reveals two key challenges: the impact of initial conditions and the number of agents on the final performance.
3. The experiments span many task-domains and multiple models.

### Weaknesses
1. This paper mainly proposes a benchmark to test and validate these challenges rather than further addressing them.
2. In more complex scenarios, problem reframing is difficult.

### Questions
Minor comments:
1. In Figure 1, should the question be "A ship travels 80 miles east/west and 150 miles north. How far is the ship from its starting point?".
2. D2C instead of C2D, e.g. Section 5 Debatepedia, Dataset Problem Reframing, etc.
3. Inconsistent symbol representation. In Section 3, C stands for the total number of calls, whereas in Section 4, C stands for Agent Count.

### Soundness
3

### Presentation
3

### Contribution
2
