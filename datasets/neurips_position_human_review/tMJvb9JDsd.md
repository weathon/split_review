# Position:  Stop Overvaluing Multi-Agent Debate—We Must Rethink Evaluation and Embrace Model Heterogeneity

- Decision: Reject
- Scores: 7, 8, 6

## Abstract
Multi-agent debate (MAD) has gained significant attention as a promising line of research to improve the factual accuracy and reasoning capabilities of large language models (LLMs). Despite its conceptual appeal, current MAD research suffers from critical limitations in evaluation practices, including limited benchmark coverage, weak baseline comparisons, and inconsistent setups. This paper presents a systematic evaluation of 5 representative MAD methods across 9 benchmarks using 4 foundational models. Surprisingly, our findings reveal that MAD often fail to outperform simple single-agent baselines such as Chain-of-Thought and Self-Consistency, even when consuming significantly more inference-time computation. To advance MAD research, we further explore the role of model heterogeneity and find it as a universal antidote to consistently improve current MAD frameworks. Based on our findings, we argue that the field must stop overvaluing MAD in its current form; for true advancement, we must critically rethink evaluation paradigms and actively embrace model heterogeneity as a core design principle.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This paper challenges the prevailing optimism around MAD frameworks for LLMs. It presents a systematic evaluation of 5 representative MAD methods across 9 widely-used benchmarks and 4 foundational LLMs. The authors find that, in their current form, MAD methods often fail to outperform simpler single-agent baselines such as CoT and SC, despite incurring greater computational cost. To address this, the paper introduces model heterogeneity, which deploy diverse LLMs within a MAD setup, to consistently improve performance. The paper advocates for rethinking MAD evaluation practices and positions model heterogeneity as a key direction for advancing the field.

### Strengths
1. The position is clear. The central agument is that current MAD methods are overvalued and require more rigorous evaluation. The call to embrace model heterogeneity is well-integrated into the narrative and grounded in the findings.
2. The evaluation of the paper is broad and systematic. The authors evaluate 5 methods, 9 benchmarks, and 4 foundation LLMs. Results are substantiated using detailed tables, figures, and statistical analysis, lending credibility and robustness to the argument.
3. The topic is timely and the contribution is relevant to the community. The area of MAD is rapidly growing and the evaluation of such methods is highly important.
4. The authors provide access to the code, which ensures reproducibility.

### Weaknesses
1. The paper misses some directly relevant citations, such as recent learning-based and uncertainty-aware MAD methods (e.g. ACC-Debate, DebUnc, etc.), which could offer promising alternatives or enhancements to the heterogeneity-focused position.
2. The paper lacks clearly articulated alternative views. While some counter-explanations (e.g. hyperparameters, task categorization, etc.) are mentioned, a dedicated section that explicitly outlines and engages with strong alternative views is lacking. For example, MAD's shortcomings may stem from immature implementations rather than conceptual flaws.

### Questions
1. Results (Table 1, Figure 2) show that current MAD methods often underperform CoT and SC. Could you elaborate on the underlying causes of this outcome? For example, architectural limilations or suboptimal coordination strategies?

2. How feasible is model heterogeneity in practical applications w.r.t. costs, orchestraction overhead, and inconsistencies, particularly under resource-constrained settings?

3. What is MAD's true utility (mentioned in Section 5)? Are there any concrete examples or characteristics of task domains where MAD is likely to be indispensible?

### Presentation
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This position paper argues that the field has been overvaluing multi-agent debate (MAD) methods for improving LLM performance due to fragmented evaluation practices. Through systematic evaluation of 5 MAD methods across 9 benchmarks and 4 models, the authors demonstrate that MAD methods generally fail to outperform simple single-agent baselines like Chain-of-Thought (CoT) and Self-Consistency (SC), despite consuming more computational resources. They propose that model heterogeneity, using diverse models rather than identical agents, can serve as an antidote to improve MAD performance. The paper calls for more rigorous evaluation standards and fundamental rethinking of what effective multi-agent collaboration means.

### Strengths
The paper's primary strength lies in its comprehensive and systematic experimental evaluation that challenges prevailing assumptions with solid empirical evidence. The scope of evaluation (5 methods × 9 benchmarks × 4 models) is impressive and provides robust statistical foundation. The introduction of model heterogeneity as a solution demonstrates constructive contribution beyond criticism. The clear articulation of future research directions provides valuable guidance for the community. The work has immediate practical implications for researchers and practitioners working with multi-agent systems.

### Weaknesses
* **Shallow Theoretical Analysis of MAD Underperformance:** The paper could benefit from deeper theoretical analysis of why MAD methods underperform, the current explanations remain somewhat surface-level. The authors don't explore whether the problem lies in the debate mechanisms themselves, the consensus algorithms, or the assumption that multiple identical agents can generate meaningful diversity.

* **Simplistic Model Heterogeneity:** The Heter-MAD design, randomly mixing GPT-4o-mini and LLaMA 3.1, lacks principled motivation. It ignores task-model compatibility, complementary strengths, or dynamic assignment strategies. Additionally, the paper could provide a more detailed analysis of the trade-offs involved with the proposed model heterogeneity, especially concerning the computational overhead of using multiple different LLMs.

* **Model Heterogeneity Analysis Lacks Depth:** While Table 2 shows consistent improvements from Heter-MAD, the analysis of why this works is superficial. Figure 4's categorization (CC, CW, WC, WW) is helpful but incomplete, it doesn't explain the mechanisms by which heterogeneous models achieve better consensus.

### Questions
* What specific benchmark characteristics do you think would better showcase MAD advantages, and how might the field develop more appropriate evaluation scenarios that require true multi-agent collaboration?
* Given your findings about model heterogeneity, how do you envision this scaling with even more diverse model pools, and what are the practical constraints for implementing this in real-world applications?

### Presentation
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This position paper critically examines the state of multi-agent debate (MAD) research for large language models (LLMs), highlighting major gaps in current evaluation practices such as limited benchmarks, inconsistent and weak baselines, and a lack of systematic comparison among approaches. The authors conduct a comprehensive experimental study, evaluating five representative MAD methods across nine widely-used benchmarks and four foundational LLMs. Surprisingly, the results indicate that MAD frameworks often fail to outperform simple, established single-agent baselines such as Chain-of-Thought (CoT) and Self-Consistency (SC), even when consuming markedly more inference-time resources. The study further reveals that introducing model heterogeneity—i.e., using diverse foundation models as agents—leads to robust gains across frameworks, suggesting a need for the MAD community to rethink core design assumptions and evaluation methodologies.

### Strengths
- Comprehensive evaluation: The study systematically benchmarks five leading MAD methods (SoM, Multi-Persona, Exchange-of-Thoughts, AgentVerse, and ChatEval) on nine prominent datasets (spanning general knowledge, mathematical reasoning, and programming) using four distinct LLMs. This broad coverage, clearly presented in Table 1 (Page 5) and Figure 2 (Page 2), is a considerable strength, providing an unusually robust empirical foundation for the field.
- Valuable evaluation results: The main finding—that MAD frameworks generally do not outperform CoT/SC—directly challenges prevailing assumptions in the area. This is well-illustrated in Table 1 and further supported by the aggregated win/tie/lose statistics in Figure 2, making a compelling case for skepticism about current MAD narratives.
- Important suggestions: The discussion (Section 5) outlines not only pitfalls in the current literature but also articulates concrete, forward-looking research directions: optimizing for heterogeneity, enhancing intra-agent reasoning, and developing benchmarks revealing true utility for multi-agent collaboration.

### Weaknesses
- Dependence on Limited Set of LLMs: The core empirical results depend on a pool of four LLMs (e.g., GPT-4o-mini, Claude-3.5-haiku, Llama3.1:8b/70b). It is unclear how generalizable these findings are to proprietary models or to non-English or lower-resource settings. This limits the universality of the conclusions, and no discussion is provided regarding the selection criteria or potential advantages and disadvantages of the chosen models.

### Questions
- Besides enriching the type of tasks in the benchmark for MAD evaluation, are there any new auxiliary metrics could be suggested to identify when single agent LLM is sufficient or MAD is preferred.

### Presentation
3
