# Position: Toward a Theory of Agents as Tool-Use Decision-Makers

- Decision: Reject
- Scores: 7, 5, 7

## Abstract
As Large Language Models (LLMs) evolve into increasingly autonomous agents, fundamental questions about their epistemic foundations remain unresolved: What defines an agent? How should it make decisions? And what objectives should guide its behavior? In this position paper, we argue that true autonomy requires agents to be grounded in a coherent epistemic framework that governs what they know, what they need to know, and how to acquire that knowledge efficiently. We propose a unified theory that treats internal reasoning and external actions as equivalent epistemic tools, enabling agents to systematically coordinate introspection and interaction. Building on this framework, we advocate for aligning an agent’s tool use decision-making boundary with its knowledge boundary, thereby minimizing unnecessary tool use and maximizing epistemic efficiency. This perspective shifts the design of agents from mere action executors to knowledge-driven intelligence systems, offering a principled path toward building foundation agents capable of adaptive, efficient, and goal-directed behavior.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This paper proposes a very very interesting epistemic action theory - basically see tool-use LM agents are epistemic actors who iterate between using internal cognitive tools for reasoning and external physical tools for knowledge towards a goal. Thus, at each step, the agent must choose whether to think internally or interact externally based on what it already knows versus what it still needs to learn.

Consequently, the authors build 2 theory constructs: 1) the notion of knowledge boundary, that what agent already knows and 2) decision boundary that the agent chooses to reason internally or seek for external tools. Thus optimal behavior—the Decision-Knowledge Alignment Principle—occurs when these boundaries coincide: the agent reasons internally when the answer lies within its parameters and invokes external tools only when necessary, minimizing hallucinations, wasted calls, and over-thinking. This is a very very interesting idea.

### Strengths
1) This paper provides a cohesive epistemic theory for agent behavior. I think this is a very impressive work given the theory-lack nature of computer science & engineering. 
2) The idea of knowledge-decision-alignment is very interesting and indeed actionable and testable. Therefore, this is a theory that's useful for guiding research endeavors.

### Weaknesses
In general, the words and theory terms in this paper is actually a bit confusing. I feel like the authors are trying to use some of the more philosophical or theory-laden terms. But actually it's not necessary. 

For example, the term metacognitive has tons of meaning and theories already associated with it. I think there is no points that the authors need to evoke those terms and cause further confusions. Usually, metacognition is related conscious introspection and tons of debates are happening in that realm of philosophy of mind. Another term is the use of the term "theory of mind" and "theory of agents". There is no points jumping into that debate since then the theory here presented is trivialized by trying to defend some of the term uses. 

I think the theory here itself is already very good. Don't need to seek references to older more history-complicated terms. Usually, when the authors want to propose a new theory, use simple terms and the terms that people have never used before is actually easier to get the idea straight.

### Questions
One small technical question: when external tools differ sharply in latency, cost, and risk, how should the alignment objective be reformulated to balance “minimal tool calls” against real-world utility?

### Presentation
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper views internal reasoning and external actions as equivalent tools for knowledge acquisition, and argues that an optimal agent should align its tool-use decision boundary with its knowledge boundary. The paper then provides a formal framework for defining tools, agents, optimal behavior, and operationalizes these via meta-cognition and the minimization of unnecessary tool use.

### Strengths
1. Interesting idea: The paper presents a clear and principled unification of internal reasoning and external actions as epistemic tools, and proposes adaptive knowledge-decision alignment.
2. Insights for achieving agent optimality in terms of agentic pretraining, SFT and RL.

### Weaknesses
1. Lack of mention and discussion of related work on improving reasoning or decision-making efficiency [1]. 
2. No discussion of practical challenges in reliably estimating knowledge boundaries, calibrating meta-cognition, or measuring and minimizing unnecessary tool use in real-world agent training and deployment.
3. The paper focuses on knowledge-driven efficiency as the primary metric but does not consider alternative metrics such as prioritizing user satisfaction, safety, or robustness in unstructured environments, which may require different decision-making trade-offs.
4. No alternative viewpoints proposed and addressed.

References:

[1] Sui, Yang et al. “Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models.” ArXiv abs/2503.16419 (2025).

### Questions
1. To what extent do existing approaches to improving reasoning and decision-making efficiency address the position in this paper?
2. How to estimate or calibrate agent's own knowledge boundaries in practice, especially as models and tasks evolve? Are there specific mechanisms or proxies for real-time boundary detection?
3. Better to have ablation studies comparing agents with and without decision-knowledge boundary alignment when solving complex tasks. What practical metrics can be helpful, and what challenges can occur?
4. In scenarios where minimizing tool use might conflict with other priorities (e.g., user trust, interpretability, or safety via additional checks), how to balance such trade-offs?

### Presentation
3

---

## Human Reviewer 3

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This position paper presents a unified theory for autonomous agents, framing them as knowledge-based decision-makers. The central point is that internal reasoning and external actions (tool use) should be considered equivalent epistemic tools for knowledge acquisition. The authors formalize the concepts of a "knowledge boundary" (the limit of an agent's internal knowledge) and a "decision boundary" (the choice between using an internal or external tool). The central position is the "Decision-Knowledge Alignment Principle," which posits that optimal agent behavior is achieved when the decision boundary is aligned with the knowledge boundary. This means that an agent should use internal reasoning for knowledge it possesses and external tools for knowledge it lacks, thereby minimizing unnecessary actions and maximizing epistemic efficiency.

### Strengths
The article presents a clear, coherent, and powerful conceptual framework for analyzing agent behavior. The fundamental concepts of "knowledge boundary," "decision boundary," and their proposed alignment provide an intuitive and orderly abstraction for reasoning about critical agent issues such as efficiency, resource management, and hallucination. The topic is exceptionally timely and relevant to the NeurIPS community.

### Weaknesses
The main weakness lies in the difficulty of measuring fundamental concepts. The "knowledge frontier" is an abstract and elusive boundary, a point the authors acknowledge. While the article proposes minimizing the use of external tools as a practical indicator, this could oversimplify the problem. 

The concept of "epistemic equivalence" between reasoning and action also minimizes crucial non-epistemic factors such as API costs, latency, and the reliability of external systems, which are often dominant considerations in real-world applications.

### Questions
1. Your framework's advocates for using external tools only when knowledge is outside the internal boundary. How do you account for cases where an external tool is preferable for non-epistemic reasons, such as superior precision (e.g., a calculator API vs. internal arithmetic), higher reliability, or for verification of the model's own internal knowledge?
2. The knowledge boundary is represented as a sharp line. Might a probabilistic perspective, where the agent has varying degrees of confidence in his or her internal knowledge, be more accurate? How could this "epistemic uncertainty" be used directly as a signal to modulate the decision boundary at the time of inference? I imagine a scenario where I have multiple agents making decisions on the same topic, but each with a different degree of confidence in their knowledge.

### Presentation
3
