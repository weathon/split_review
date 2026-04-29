# Unlocking the Full Potential of Data Science Requires Tabular Foundation Models, Agents, and Humans

- Decision: Reject
- Scores: 8, 5, 4

## Abstract
Despite its vast potential, data science remains constrained by manual workflows and fragmented tools. Meanwhile, foundation models have transformed natural language and computer vision — and are beginning to bring similar breakthroughs to structured data, particularly the ubiquitous tabular data central to data science.
At the same time, there are strong claims that fully autonomous agentic data science systems will emerge. 
We argue that, rather than replacing data scientists, the future of data science lies in a new paradigm that amplifies their impact: collaborative systems that tightly integrate agents and tabular foundation models (TFMs) with human experts.
In this paper, we discuss the potential and challenges of navigating the interplay between these three and present a research agenda to guide this disruption toward a more accessible, robust, and human-centered data science.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper argues that realizing the full societal and scientific potential of AI requires moving beyond purely performance-driven research metrics toward a “holistic AI evaluation” framework. This framework should integrate considerations such as fairness, interpretability, robustness, energy efficiency, data governance and human-AI collaboration outcomes into mainstream evaluation protocols.

### Strengths
As per my assessment, the strengths of the paper are as follows - 

* It clearly diagnoses a key misalignment in AI research incentives.
* It advances a balanced treatment of technical and societal dimensions.
* It has a strong engagement with prior literature - especially from responsible AI and meta-benchmarking communities.
* It advances feasible adoption mechanisms through existing research structures (funding, competitions, peer review).
* The multi-layered evaluation concept is innovative and adaptable to different subfields.

### Weaknesses
More concrete implementation pilots or case studies (e.g., leaderboard redesigns, journal pilot programs) would strengthen feasibility claims.
An expanded discussion of potential resistance from researchers and industry stakeholders due to cost/time burdens. The proposed audit layer could benefit from clearer delineation of responsibility (who audits, with what authority?).

### Questions
An interesting question which emerges is - Could you present a detailed mock-up of a leaderboard or evaluation sheet that includes all three proposed layers?

### Presentation
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
The paper argues that end-to-end, human-absent automation is the wrong target for tabular data science. Instead, it proposes a collaborative paradigm that tightly integrates tabular foundation models (TFMs), LLM-based agents, and human experts. It surveys the limits of TFMs (narrow task coverage), agents (insufficient rigor on tables), and humans (limited bandwidth), and contends that only their combination can deliver robust, explainable, and scalable data science. The authors sketch a workflow (problem formulation → data ops → modeling → validation) with explicit human checkpoints, discuss risks (automation bias, leakage, privacy, security, sustainability), and outline a research agenda (stronger TFMs, safer/structured agents, realistic benchmarks, end-to-end verifiability, deployment).

### Strengths
1.	Timely and coherent position. The triad (TFMs + agents + humans) is clearly motivated and well argued for tabular work where provenance, rigor, and context matter.
	2.	Well-structured survey + design blueprint. The paper crisply contrasts capabilities/limits (e.g., TFMs’ structure awareness vs. agents’ tool use vs. human judgment) and offers a workflow with clear human intervention points; this is useful to practitioners and researchers alike.
	3.	Balanced treatment of risks. The section on automation bias, leakage, privacy/memorization, execution risk, and compute/energy cost shows practical awareness beyond benchmarks.

### Weaknesses
1.	As a position piece it’s acceptable, but even a small case study (e.g., TFM-equipped agent on a realistic, multi-table task) would substantiate the claims and clarify trade-offs in accuracy, latency, and cost.
	2.	The paper could more sharply differentiate its blueprint from AutoML, program-aided LMs, graph-RAG, DSPy-style pipelines, and existing data-science agents (what’s truly new beyond integration + emphasis on tabular?).
	3.	How to choose between TFMs vs. LLM tools, how to constrain agent action spaces in “high-risk” steps, how to select/validate structures and resolve conflicts (e.g., contradictory intermediate results) remain underspecified.
	4.	The desiderata (explainability, completeness, etc.) lack concrete metrics/protocols (e.g., trace coverage/faithfulness, cross-table consistency checks, cost/energy accounting, human-in-the-loop efficacy).
	5.	The paper argues humans are indispensable, but provides few patterns for when and how to re-insert experts (triggers, escalation criteria, UI/UX primitives), or how to elicit and encode institutional knowledge.

### Questions
•	What are the minimal new mechanisms that distinguish your system from RAG + schema-enforced extraction + tool-calling agents?
	•	How is structure/tool selection automated? When does the agent invoke a TFM vs. write code vs. defer to a human?
	•	What guardrails do you envision for causal/biased analyses (e.g., primitives that make target-leakage or non-IID assumptions explicit and checkable)?
	•	Can you share a cost/latency analysis for multi-stage, human-in-the-loop pipelines, and any caching/reuse strategies?
	•	What is the verifiability artifact (e.g., provenance graph + scored checkpoints) you expect reviewers/users to inspect?

### Presentation
3

---

## Human Reviewer 3

### Rating
4

### Rating Number
4

### Confidence
3

### Summary
The paper argues that the future of data science lies in collaborative new systems that integrate human experts, agents and tabular foundational models instead of autonomous data science agents. The authors compare the strengths of human experts with TFMs and LLM agents, and call for research in scalable, context-aware TFMs, human-agent collaboration, realistic benchmarks, and verifiable systems.

### Strengths
1. The paper is quite well-written and easy to understand. 
2. It is also well-structured: to support their position, the authors first lay out current challenges in data science, then discuss the strengths and limitations in tabular foundational models, LLM agents and human experts. The paper then suggests the collaborative paradigm, potential risks and future research directions. 
3. The authors also discussed with details and examples on the unique capabilities of human experts - domain knowledge that are not easily accessible for model training, contextual understanding of data science, and alignment with the final goal of doing data science.
4. The authors discussed thoroughly on the potential risks in AI centered data science.

### Weaknesses
The paper can benefit from the following discussions:
1. The paper's core position, that AI needs human experts for goal alignment and domain knowledge, doesn't seem particularly novel. It's described as a "deeply integrated" collaboration, but the workflow presented just looks like the standard process of humans formulating problems and then validating the AI's solutions in each step.
2. The argument for why a tabular foundational model is the right choice isn't backed by strong empirical or theoretical evidence. The reasoning rests on general LLM limitations like hallucinations and poor reasoning, but this overlooks the incredibly rapid progress made to solve these deficiencies in frontier models.
3. A major piece of the data science process, data ETL and processing, is missing from the discussion. This seems like a critical omission, especially since LLMs are promising for automating these tasks.

### Questions
1. I wonder if it would be more effective to discuss the three layers of data science as human supervision, agents, and models? We've seen from frontier lab demos that AI agents can now use tools like Python to create simple data science models or use existing models for problems that don't involve TFMs, maybe instead of arguing for tabular foundational models, just general machine learning models for data science?
2. The paper mentions a “dynamically orchestrated workflow,” but it’s not clear what this means concretely. Could you elaborate on what this looks like in practice? The figure that illustrates the workflow with AI and human seems like a typical work process with human review in the loop.

### Presentation
3
