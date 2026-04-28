# StarCraft II Arena: Evaluating LLMs in Strategic Planning, Real-Time Decision Making, and Adaptability

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3

## Abstract
StarCraft II plays an important role in developing AI agents for real-time strategic reasoning due to its complex nature. However, people usually draw conclusions of how competent their agents are according to the level of the built-in agents in StarCraft II which they can win in terms of the final success rate. Little intermediate quantitative information is considered while human-in-the-loop analysis is time inefficient, which results in inadequate reflection of the true strategic reasoning ability. In this work, we propose StarCraft II Arena, a well-designed benchmark for evaluating the strategic planning, real-time decision-making, and adaptability capabilities of large language models (LLMs) agents. We introduce using fine-grained capability metrics, allowing for targeted capture and analysis of specific capability, and further propose a detailed decision trace to enhance the understanding of LLM behavior. We demonstrate the utility of such a benchmark by evaluating several state-of-the-art LLMs in various setups. Our results reveal distinct performances in long-term strategy development, real-time decision-making, and adapting to environmental changes. Such results show that the StarCraft II Arena offers a deeper insight into the decision-making process of LLMs and has the potential to become a challenging and comprehensive benchmark for strategic reasoning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents StarCraft II as a benchmark for evaluating reasoning capabilities of LLMs. The paper also presents a set of metrics for evaluating these models, which are based on the domain itself (e.g., amount of resources the play collects). Finally, the paper presents results of several LLMs on this benchmark.

### Strengths
The idea of having a challenging benchmark for reasoning with LLMs is interesting and appealing. I also think that computer games can be a good benchmark for this type of evaluation. The choice of a real-time strategy game is particularly good, given the response latency of these systems.

### Weaknesses
Overall, the paper lacks clarity and depth in describing both the technical implementation and practical contributions.

1. Unclear contribution: The paper does not effectively justify why this benchmark must exist as a standalone contribution rather than an addition to existing Starcraft II resources. The contribution seems limited to a collection of scripts and metrics, which could likely be integrated into the existing environment without creating a separate benchmark.

2. Lack of implementation details: Key technical aspects of the implementation are insufficiently described, making it hard to understand the benchmark's novelty and how it's technically realized. Several things are not clear, such as:
   - Integration: How are LLM agents integrated with StarCraft II? How can users use the benchmark? Does the benchmark use a custom API or an interface for this?
   - Decision Tracking: How is decision-making tracked and analyzed? While Table 3 provides a decision trajectory, details of how this is analyzed and used are missing.
   - Computational Requirements: What hardware/software is necessary to run this benchmark effectively? This information is critical for usability but is absent.
   - Opponents: Are the LLMs evaluated with built-in agents or newly introduced opponents? The fact that agents are evaluated against built-in agents in Starcraft II is mentioned as a limitation, but it is unclear whether the authors change this in their benchmark.

3. Incomplete metric information: The metrics lack context. For instance, while Appendix A.1 outlines the metrics, there are no defined ranges, leaving the reader unsure of how to interpret scores. For example, how should a Real-Time Decision score of 21.12 versus 37.51 in Table 4 be interpreted? Similarly, terms such as “effective” actions in EPM or “collected vespene” are not unexplained, reducing the metrics’ interpretability (how do we know that these are the right metrics to assess decision-making and planning?).
 
4. Missing benchmark discussion and limitations: A discussion about future development and limitations of the benchmark is missing, which limits the reader's understanding of the benchmark's intended scope and future extensions.

5. Figure 2 indicates a large variance. Why are there no error bars in the tables?
6. It's important to have the prompt included in the appendix or supplement. Was it possibly in a supplement that I cannot access?



### Questions
Please see the questions in the "high-level concerns" section above.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents StarCraft II Arena as a benchmark for evaluating LLMs in strategic planning and decision-making capabilities. While it introduces fine-grained metrics and decision tracking mechanisms, the paper needs substantial clarification on its novel contributions and experimental methodology.

### Strengths
1. Well-structured evaluation framework with fine-grained metrics
2. Comprehensive testing across multiple LLM models
3. Interesting decision tracking system for behavior analysis

### Weaknesses
1. Insufficient experimental details:
- Build-in AI difficulty level not specified
- Race and map selection criteria not documented
- Limited experimental scope (10 games per model)
2. Theoretical foundation needs strengthening:
- Limited discussion of why LLMs are suitable for StarCraft II
- Insufficient comparison between LLM agents and traditional RL agents
- Unclear theoretical justification for chosen metrics
3. Literature positioning:
- Need more thorough comparison with existing StarCraft II benchmarks
- Better contextualization of contributions needed
- Clearer differentiation from existing approaches required

### Questions
1. Can you elaborate on the key differences between this work and existing StarCraft II benchmarks, particularly "Large Language Models Play StarCraft II"? What are the novel contributions that advance the field?
2. The paper would benefit from a deeper discussion of why LLMs are suitable for StarCraft II:
- What unique capabilities do LLMs bring compared to traditional RL approaches?
- How does the decision-making process differ between LLM agents and RL agents?
- What insights have you gained about LLM capabilities through this work?
3. Experimental details requiring clarification:
- What was the difficulty level of the built-in AI?
- How were races and maps selected?
- Why was 10 games chosen as the sample size? Why not do more experiments and test open-soruce model
- What statistical analyses support the conclusions?
4. Theoretical foundation:
- How do the proposed metrics relate to fundamental LLM capabilities?
- What theoretical guarantees or limitations exist for the evaluation framework?
- How generalizable is this benchmark to other strategic decision-making tasks?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a benchmark called Starcraft II Arena, which aims to evaluate the decision-making, planning, and adaptability of large language models (LLMs) within a strategic gaming environment. While traditional benchmarks for Starcraft II assess agents based on a single overall metric—win rates against built-in opponents—the authors argue that a more detailed analysis of LLM performance is necessary. The main contribution of this paper is a methodology designed for an in-depth evaluation of the capabilities of LLM agents.

### Strengths
The key idea of this paper, introducing a benchmark for a more in-depth multi-agent evaluation of LLMs, is significant and useful.

### Weaknesses
Overall, the paper lacks clarity and depth in describing both the technical implementation and practical contributions.

### **Major comments**

1. Unclear contribution: The paper does not effectively justify why this benchmark must exist as a standalone contribution rather than an addition to existing Starcraft II resources. The contribution seems limited to a collection of scripts and metrics, which could likely be integrated into the existing environment without creating a separate benchmark.

2. Lack of implementation details: Key technical aspects of the implementation are insufficiently described, making it hard to understand the benchmark's novelty and how it's technically realized. Several things are not clear, such as:
   - Integration: How are LLM agents integrated with StarCraft II? How can users use the benchmark? Does the benchmark use a custom API or an interface for this?
   - Decision Tracking: How is decision-making tracked and analyzed? While Table 3 provides a decision trajectory, details of how this is analyzed and used are missing.
   - Computational Requirements: What hardware/software is necessary to run this benchmark effectively? This information is critical for usability but is absent.
   - Opponents: Are the LLMs evaluated with built-in agents or newly introduced opponents? The fact that agents are evaluated against built-in agents in Starcraft II is mentioned as a limitation, but it is unclear whether the authors change this in their benchmark.

3. Incomplete metric information: The metrics lack context. For instance, while Appendix A.1 outlines the metrics, there are no defined ranges, leaving the reader unsure of how to interpret scores. For example, how should a Real-Time Decision score of 21.12 versus 37.51 in Table 4 be interpreted? Similarly, terms such as “effective” actions in EPM or “collected vespene” are not unexplained, reducing the metrics’ interpretability (how do we know that these are the right metrics to assess decision-making and planning?).
 
4. Missing benchmark discussion and limitations: A discussion about future development and limitations of the benchmark is missing, which limits the reader's understanding of the benchmark's intended scope and future extensions.

5. Figure 2 indicates a large variance. Why are there no error bars in the tables?
6. It's important to have the prompt included in the appendix or supplement. Was it possibly in a supplement that I cannot access?

### **Minor comments** (These did not affect my score)
- Abstract: Lines 016-019 are a bit difficult to understand; consider rephrasing
- Figure 2: It’s unclear what this Figure is meant to convey, and the Figure lacks labeled y-axes.
- In Section 4.3, line 367 states "Definitions and methods for these metrics will be further detailed in the figure 4.3." This seems to refer to a table, possibly Table 3, rather than a figure. 
- In Table 3, "OBSERVERtgreater" should probably be "OBSERVER."
- Lines 323 + 350 state that screenshots illustrating decision traces will be provided in the appendix, but these are not included
- I don't understand what is meant when the authors state that civilization and the other games are not "strategic and tactical" in Table 1. Additionally, Werewolf is clearly an imperfect information game. The authors should reconsider this table because I believe many of the entries are inaccurate.
- Why is the score in Table 4 unnormalized? It's an incomprehensible number as it stands.

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
summary: The paper presents StarCraft II Arena as a benchmark for evaluating LLMs in strategic planning and decision-making capabilities. While it introduces fine-grained metrics and decision tracking mechanisms, the work needs substantial clarification regarding its novel contributions, metric selection justification, and experimental methodology.

### Strengths
1. Well-structured evaluation framework with proposed fine-grained metrics
2. Comprehensive testing across multiple LLM models
3. Detailed decision tracking system for behavior analysis
4. Clear visualization of experimental results
5. Systematic approach to evaluating different aspects of LLM capabilities

### Weaknesses
1. Metric Selection and Justification:
- APM/EPM metrics appear borrowed from traditional StarCraft II evaluation without clear justification of their relevance to LLM agents
- No discussion of how these metrics specifically reflect LLM decision-making capabilities
- Missing analysis of whether traditional StarCraft II performance metrics are appropriate for language models
2. Experimental Design Limitations:
- Build-in AI difficulty level not specified
- Race and map selection criteria not documented
- Limited experimental scope (10 games per model)
- Absence of LLM vs LLM experiments
- No evaluation against human players
- Limited testing of open-source models, reducing reproducibility
3. Theoretical Foundation and Novelty:
- Limited discussion of why LLMs are suitable for StarCraft II
- Insufficient comparison between LLM agents and traditional RL agents
- Evaluation metrics show significant overlap with existing work
- Need clearer articulation of novel contributions
- Better contextualization within existing literature required

### Questions
1. Evaluation Metrics:
- How do APM and EPM meaningfully evaluate LLM agent performance when their decision-making process is fundamentally different from traditional agents?
- What is the relationship between these metrics and LLM reasoning capabilities?
- Have you considered developing metrics specifically designed for language model evaluation?
2. Comparative Analysis:
- Could you clarify the key methodological differences between your work and "Large Language Models Play StarCraft II"?
- What novel insights does your evaluation framework provide that weren't captured in previous work?
- How does your fine-grained capability analysis advance the field beyond existing benchmarks?
3. Experimental Design:
- Why weren't LLM vs LLM experiments included in the evaluation?
- What prevented the inclusion of human player comparisons?
- Could you explain the decision to limit testing of open-source models?
- How would the results differ with head-to-head language model competitions?
4. Implementation Details:
- How are LLM actions translated into game commands?
- What are the time constraints for model inference?
- What specific prompt engineering techniques were used?
- What is the role of temperature and other sampling parameters?
5. Theoretical Framework:
- How does the decision tracking system account for the unique characteristics of language model reasoning?
- What theoretical justification supports the choice of strategic planning metrics?
- How do you ensure the evaluation framework captures the full range of LLM capabilities?

### Soundness
1

### Presentation
2

### Contribution
1
