# Asynchronous Factorization for Multi-Agent Reinforcement Learning

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 3, 5

## Abstract
Value factorization is widely used to design high-quality, scalable multi-agent reinforcement learning algorithms. However, current methods typically assume agents execute synchronous, 1-step *primitive actions*, failing to capture the typical nature of multi-agent systems. In reality, agents are asynchronous and execute *macro-actions*---extended actions of variable and unknown duration---making decisions at different times. This paper proposes value factorization for asynchronous agents. First, we formalize the requirements for consistency between centralized and decentralized macro-action selection, proving they generalize the primitive case. We then propose update schemes to enable factorization architectures to support macro-actions. We evaluate these asynchronous factorization algorithms on standard macro-action benchmarks, showing they scale and perform well on complex coordination tasks where their synchronous counterparts fail.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method to effectively handle macro-actions in multi-agent reinforcement learning (MARL) through an asynchronous learning structure. To address the inefficiencies and temporal inconsistencies that arise when agents have different action durations in synchronous learning frameworks, the paper introduces the Asynchronous Value Factorization (AVF) method. This approach allows agents to update independently in environments involving macro-actions, improving learning efficiency and scalability. The paper provides theoretical foundations through the concepts of Macro-IGM and MacAdv-IGM, demonstrating that macro-action-based learning has a broader expressiveness compared to traditional single-action methods. Experimental validation shows that AVF outperforms synchronous methods in various macro-action scenarios, achieving superior performance in asynchronous policy learning.

### Strengths
- Solving practical issues. The paper introduces an asynchronous learning structure that addresses the temporal inconsistencies and update delays inherent in synchronous approaches. This enables agents to update independently, significantly improving learning efficiency and environmental adaptability. This design effectively reflects the real-world asynchronous nature of multi-agent systems, solving practical issues.
- Theoretical Extensibility: The concept of Macro-IGM provides greater representational power for handling macro-actions, ensuring that local agent actions remain consistent with the global policy. This allows for stable policy optimization even in asynchronous settings, demonstrating an expanded expressiveness and applicability beyond traditional methods.
- Compatible with Existing Algorithms: The proposed asynchronous update mechanism can be integrated with existing algorithms like QMIX and QPLEX, enhancing their performance by addressing temporal inconsistencies and improving efficiency. This compatibility allows the AVF method to be applied broadly across various MARL frameworks, increasing its practical utility.

### Weaknesses
 - Theoretical Analysis Limitations: Although the paper presents theoretical propositions such as Macro-IGM and MacAdv-IGM, their practical relevance to the proposed AVF algorithm is limited. The theoretical framework is broad and lacks direct applicability, as it does not clearly define or demonstrate how the function class  F  satisfying these conditions is implemented within the algorithm. Additionally, the propositions do not significantly bridge the gap between theoretical findings and practical performance, raising questions about the real impact of these proofs on the algorithm’s effectiveness. Specifically, the paper does not detail how the conditional value function predictions, which are crucial for the theoretical framework, are explicitly incorporated into the update rules of algorithms like QMIX and QPLEX. This lack of clarity makes it difficult to assess whether the theoretical guarantees of Macro-IGM and MacAdv-IGM are actually realized in the practical implementation of AVF. For instance, the paper does not explain how the conditional operator is implemented within the neural network architecture, nor how it ensures that agents do not prematurely sample new high-level behaviors before completing their current macro-actions.
- The paper’s asynchronous learning structure and handling of macro-actions, while effective, are relatively straightforward and have been explored in MARL research before. This makes the contribution seem incremental rather than a significant innovation, potentially limiting its perceived impact in advancing the field.

### Questions
Could you explain how the theoretical propositions, specifically Macro-IGM and MacAdv-IGM, concretely impact the learning performance and stability of the AVF algorithm? I would like clarification on how these theoretical proofs contribute directly to the design and performance improvement of the algorithm.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies temporal abstraction in MARL, focusing on Asynchronous Value Factorization (AVF). It adjusts the IGM consistency and common value factorization methods to the AVF setting, where agent utilities with ongoing macro-actions are excluded from the gradient calculation. The approaches are evaluated on some small benchmark domains.

### Strengths
- Studies a well-motivated but somewhat neglected problem
- Well-written and easy to understand
- The limitations and broader impact are clearly stated

### Weaknesses
 
**Limitation**

- The paper assumes macro-actions to be pre-defined but realistically this does not seem feasible to me: Since macro-actions consist of primitive actions, the macro-action space scales exponentially w.r.t. time, which makes a manual definition of adequate (or even optimal) macro-actions prohibitive. This is a significant limitation, as the performance of the proposed method is highly dependent on the quality of these pre-defined macro-actions. The paper does not address how to select or design these macro-actions, which is a crucial aspect for practical applications.

**Significance**

- I am sceptical about the optimality claim regarding Macro-Dec-POMDPs, which depends on the actual macro-action definition. E.g., considering Dec-Tiger, one could define a macro-action that only consists of Listening actions (without opening a door), which would never yield the optimal reward - regardless of what the other agents does. The paper does not adequately discuss the limitations of this optimality claim, especially in scenarios where macro-actions are not well-designed.
- As far as I understood, the most significant technical contribution is only to exclude the agent utilities of ongoing macro-actions from the gradient calculation, e.g., using masking. While technically sound, this seems like a relatively minor modification to existing value factorization methods, and the paper does not provide sufficient evidence to demonstrate its novelty or impact.
- The experimental is mainly a self-comparison, i.e., ablations, without including any baseline known from hierarchical MARL [1] or temporal abstraction in MARL [2], which also consider macro-action-based value factorization. The lack of comparison with established methods makes it difficult to assess the true performance and contribution of the proposed approach.

**Presentation**

- In Section 4, the first and second paragraph overlap visually which looks weird.
- The labels of Figures 3, 4, 5, 6, and 8 are too small (they are unreadable when printed). Even worse, the plots Figures 5, 6, 7, and 8 pixelate when zooming in, which does not help readability either. Thus, I am uncertain about the significance and quality of the results.

**Literature**

[1] Xu et al, "HAVEN: Hierarchical Cooperative Multi-Agent Reinforcement Learning with Dual Coordination Mechanism", AAAI 2023

[2] Tang et al., "Hierarchical Deep Multiagent Reinforcement Learning with Temporal Abstraction", 2018

### Questions
None

### Soundness
2

### Presentation
2

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
This paper investigates an asynchronous multi-agent setting, extending value factorization methods to this context. It introduces Macro-Action-Based IGM and applies relevant value factorization methods within the macro-action framework. The experimental results demonstrate the effectiveness of the proposed methods on macro-action benchmarks.

### Strengths
1. The paper addresses an intriguing and underexplored area by applying value factorization methods to agents utilizing macro-actions.

2. The methodology is clearly articulated, supported by figures that enhance understanding.

3. The experimental results show notable improvements on benchmarks.

### Weaknesses
 - The current method appears straightforward; a deeper exploration is warranted. For instance, the proposed MAC-IGM and MacAdv-IGM lack insights into algorithm design. Since MAC-IGM encompasses a broader class of functions over the primitive IGM, it would be beneficial to investigate more effective factorization or simple modifications tailored for asynchronous tasks rather than merely applying previous methods. As it stands, the current variant of IGM serves mainly as a verification of existing value factorization methods, diminishing its contribution.

- Asynchronous updates require further examination:
  - Why must agents with ongoing macro-actions be masked?
  - Using 0 as the masked value in D2 seems problematic; if all rewards and Q-functions are negative, more agents with ongoing macro-actions would lead to lower rewards assigned for others.
  - For QPLEX, since its mixing network also requires actions as input, will this be masked in D1 and D2?
  
A more principled approach to determining asynchronous updates, potentially aligned with the MAC-IGM definition, should be considered.

- The environmental results are unclear:
  - The comparisons in Section 5.1 between D0, D1, D2, w/ and w/o MS are hard to discern from Figure 6.
  - The comparison of AVF to prior methods is vague; using the best performance among VDN, QMIX, QPLEX, and all update and macro-state variants seems unfair.
  - Since the proposed method is value-based, incorporating baselines like IQL with macro-actions would be beneficial.
  - The figures are unclear, and error bars are missing. Utilizing vector graphics instead of raster graphics is recommended, as the latter become blurry when enlarged.
  - How many seeds were used for each experiment?

### Questions
Refer to the weaknesses mentioned above.

### Soundness
3

### Presentation
3

### Contribution
2
