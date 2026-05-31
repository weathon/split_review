## Human Reviewer 1

### Summary
This work introduces ASpec, a framework that manages the full lifecycle of expert specialist agents by first autonomously discovering specialist archetypes via evolutionary search and then cultivating their expertise through experience. It also introduces "retain-then-escalate", a control policy that, instead of being either fully static or fully dynamic, defaults to retaining a stateful agent team across related queries to leverage expertise and minimize cost, only escalating to architectural resampling when needed. Results show that the proposed approach can lead to substantial performance improvements without sacrificing efficiency.

### Strengths
- The proposed method is novel and well-motivated. It effectively addresses the limitation of prior work, where architectures lack long-term state because they are regenerated or resampled for every query.

- The results in Table 1 show substantial performance improvements, which validate the effectiveness of the proposed method.

### Weaknesses
- I am confused about the transferability results presented in Figure 5 (right). I can't understand this figure and there is no accompanying explanation or analysis. I would like to understand how well the proposed method transfers to different tasks, and a more detailed discussion would be helpful.

### Questions
- I am not very familiar with the related work in this area, so I am unsure whether the selected baselines are the most appropriate for comparison.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
2

---

## Human Reviewer 2

### Summary
ASPEC framework builds evolving teams of specialized agents that can keep improving with experience. It designs specialized agent types through evolutionary search and enables them to improve through practice. Experiments show that this method leads to performance gains.

### Strengths
ASPEC effectively bridges the gap between static task-level designs and per-query adaptive systems.
Achieves top performance on multiple benchmarks—including GPQA and SciCode, surpassing prior frameworks such as AFlow, ADAS, and EvoAgent.
Evaluated across five diverse benchmarks covering reasoning, scientific QA, and coding tasks, demonstrating robust generalization across domains.
The paper explicitly reports that ASPEC achieves higher accuracy than baselines at a fraction of the computational cost. This “Pareto-efficient” behavior is one of its key strengths.

Includes detailed ablation studies quantifying the contribution of each system component—such as specialist operators, the meta-controller, and the architect—to overall performance and efficiency.

### Weaknesses
The meta-agent evaluation process introduces multiple sources of randomness (including LLM output variance, error propagation across chained agents, sampling variability within the meta-agent, and stochastic evaluation outcomes). This leads to higher variability than typical single-LLM evaluations. In addition to averaging results over three runs, reporting variances would help assess and demonstrate the stability of the system’s performance.

The framework’s separation into two discrete stages (specialist discovery and specialist cultivation) appears conceptually convenient but somewhat artificial.

### Questions
How can other long-term memory methods be incorporated into your framework?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper proposes an automated method for generating stateful specifications to improve AI agent performance on complex tasks. By combining formal methods with machine learning, the system automatically extracts state transition rules and constraints from task execution traces. Experiments on various state management tasks show the approach effectively improves task success rates and code quality.

### Strengths
1. **High degree of automation**: Automatically extracts specifications from execution traces with minimal human intervention, enhancing practicality
2. **Methodological innovation**: Combines symbolic reasoning with statistical learning, leveraging advantages of both for complex state spaces
3. **Comprehensive experiments**: Validation across different task types including file system operations, database management, and workflow orchestration
4. **Good interpretability**: Generated state specifications are human-readable, facilitating debugging and understanding of agent behavior
5. **Clear effectiveness**: Experiments show significant improvements in task success rates and code robustness

### Weaknesses
1. **Insufficient formal guarantees**: Despite using formal methods, lacks theoretical guarantees for correctness and completeness of generated specifications. Critical states or constraints may be missed
2. **Questionable scalability**: How does computational complexity scale with state space size? The paper lacks analysis of large-scale scenarios
3. **Data dependency**: Requires sufficiently diverse execution traces to learn complete specifications. Cold start and rare state handling is inadequate
4. **Shallow comparisons**: Limited comparison with pure learning-based or pure formal methods, making it hard to assess true advantages of the hybrid approach
5. **Practical deployment challenges**: How are state specifications continuously updated in dynamic environments? Maintenance issues aren't discussed

### Questions
1. When task definitions change, how efficiently can learned state specifications be updated? Does this require recollecting large amounts of data?
2. For scenarios with concurrent operations, how do you model partial ordering of state transitions?
3. How do you address state explosion? In very complex systems, possible state combinations grow exponentially
4. Compared to manually designed specifications, where are automatically generated ones superior? Have you conducted such comparisons?
5. How transferable is the method across domains? How much domain-specific tuning is required?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper introduces ASPEC, a framework designed to bridge the functional gap in contemporary agent system design between static, task-specific workflows and dynamic, per-query optimizers. It proposes a system of specialized agents capable of accumulating persistent, role-specific expertise over time. The methodology involves an automated lifecycle consisting of evolutionary discovery and experiential cultivation, governed by a cost-aware "retain-then-escalate" control policy. The authors demonstrate measurable performance improvements, notably achieving an accuracy of 62.8% on the GPQA benchmark, and establish competitive cost efficiency relative to approaches that rely on constant architectural resampling.

### Strengths
The proposal to develop adaptive, stateful specialist agents represents a highly appealing and novel direction compared to other current multi-agent system approaches. Furthermore, the empirical results presented are compelling, and the supporting analysis of the system's components and efficiency is sound.

### Weaknesses
The system is inherently complex due to its hierarchical, two-tiered structure. It requires maintaining both a low-level Architect (a large generative LLM used for evolutionary search) and a high-level, trained Meta-Controller (a neural policy). The entire process involves managing an offline two-stage training loop (Discovery and Cultivation), which is more involved than implementing fixed-architecture or simple prompt-optimization methods.

### Questions
Could you elaborate on how the framework determines when a newly discovered specialist's niche is too narrow to be retained, thus avoiding excessive fragmentation?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
3