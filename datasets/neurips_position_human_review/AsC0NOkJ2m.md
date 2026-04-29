# Position: Out of Control - Why Alignment Needs Formal Control Theory

- Decision: Reject
- Scores: 7, 5, 9

## Abstract
This position paper argues that formal optimal control theory should be central to AI alignment research, offering a distinct perspective from prevailing existing AI safety and security approaches. While recent work in AI safety and mechanistic interpretability has advanced formal methods for alignment, they often fall short of the generalisation required of other control frameworks required of other technologies. There is also a lack of research into how to render different alignment/control protocols interoperable. We argue that by recasting alignment through principles of formal optimal control and framing alignment in terms of hierarchical stack from physical to sociotechnical layers according to which controls may be applied we can develop a better understanding of the potential and limitations for controlling frontier models and agentic AI systems. To this end, we introduce an \textit{Alignment Control Stack} and formal methods to address these challenges and demonstrate their utility in simulated experiments. We argue that such analysis is also key to the assurances that will be needed by governments and regulators in order to see AI technologies sustainability benefit the community. Our position is that doing so will bridge the well-established and empirically validated methods of optimal control with practical deployment considerations to create a more comprehensive alignment framework, enhancing how we approach safety and reliability for advanced AI systems.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The position paper argues that AI alignment research would benefit from formally adopting principles and tools from formal control theory. The authors identify two gaps in current alignment work: the formalization problem, where empirical or heuristic methods lack generalizable, rigorous guarantees; and the coordination problem, where alignment techniques across technical and socio-technical layers are developed in isolation. To address these, the authors propose the Alignment Control Stack (ACS), a ten-layer hierarchical taxonomy (from physical hardware up to societal governance) that specifies where control theory can be applied. The authors illustrate how formal control methods (e.g. Kalman filtering, stochastic optimal control, and game-theoretic formulations) can be mapped onto existing AI safety protocols, including auditing untrusted models and modeling adversarial subversion. Through toy simulations, they demonstrate deriving optimal adversary strategies, conducting sensitivity analyses, and framing adaptive deployment as POMDPs. The paper calls for integrating formal control frameworks with alignment methods to provide robust, interoperable guarantees essential for trustworthy AI deployment.

### Strengths
1. Clear Position & Motivation: The paper succinctly motivates why formal control theory’s emphasis on stability analysis, robust synthesis, and stochastic modeling complements existing alignment research.

2. Novel Taxonomy: The Alignment Control Stack provides a structured lens for organizing and comparing control interventions across layers, fostering clarity and interoperability.

3. Concrete Illustrations: By recasting recent AI safety protocols (e.g., auditing strategies, subversion games, adaptive deployment) in control-theoretic terms and showing toy simulations, the authors convincingly demonstrate how optimal control and game theory yield principled parameter choices and sensitivity insights.

4. Relevance & Impact: The call to bridge optimal control theory with AI alignment is timely for the NeurIPS community, given the increasing complexity of frontier models and the need for rigorous safety guarantees in high-stakes applications.

### Weaknesses
Though Section 5 discusses objections (complexity science, mechanistic interpretability, empirical iterative methods), the treatment is brief. For instance, more discussion of how white-box interpretability techniques could concretely feed into control models would strengthen interoperability claims.
The paper lacks experiments on realistic, high-dimensional models (e.g. large language models). The experiments focus on the variety of toy demonstrations of the Alignment Control Stack, but they do not yet overcome the core concerns about scalability to high-dimensional, real-world systems or about integrating human-in-the-loop dynamics and governance layers. The paper would still benefit from larger-scale case studies or at least mid-scale neural network experiments that validate tractability and human-agent coordination.

### Questions
How do you envision constructing tractable state-space models for large language models in Layers 5–7? Can you outline a concrete pipeline for extracting state variables (e.g., via probes or interpretability circuits) to feed into a stochastic control framework?

Have you evaluated approximate control methods (e.g., model predictive control with limited horizons) on mid-scale neural networks? What performance-safety trade-offs emerged?

Answering these questions would strengthen the argument made by the paper.

### Presentation
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper posits that formal optimal control theory should be central to AI alignment research, offering a distinct perspective from existing AI safety/security approaches. It identifies lack of formalisation and coordination as the two main challenges of alignments which can be addressed by control theory. To this end, the paper suggests Alignment Control Stack, a ten-layer hierarchical model spanning from physical hardware to socio-technical governance.

### Strengths
- The paper provides extensive reasoning for why formal control theory is necessary for alignment research which is quite relevant and topical.

- The hierarchal Alignment Control Stack helped ground the discussion on where to include control theory at every stage. 

- The alternative views are well argumented.

- Connecting to governments and policy making is quite relevant and important.

### Weaknesses
- My biggest concern is which definition of mis-alignment was used? There are different definitions and they can be addressed with different methodologies. I suppose the paper wants to propose control theory to avoid misalignment in FM, but what are the misalignments that the authors are concerned with?

- Many examples use linear-Gaussian surrogates but these are quite different from the true nonlinear, high-dimensional, partially observable dynamics of frontier LLMs. Potentially these methods aren't easily applicable.

- There exists papers on aligment formalisation which the paper doesnt really discuss or acknowledge -  "Value alignment: a formal approach", "Artificial intelligence, values, and alignment"

### Questions
- I am not an expert in control theory, but do you think we can a hybrid approach with some methods from empirical research along with control theory can be realistically used. At what stack level which methods should be prioritised?

### Presentation
2

---

## Human Reviewer 3

### Rating
9

### Rating Number
9

### Confidence
4

### Summary
The paper argues that AI alignment research should integrate formal optimal control theory to address two issues:
(1) the formalisation problem: a lack of mathematical frameworks to generalize results and compare alignment methods
(2) the coordination problem: absence of a structured taxonomy for where in the AI system stack alignment interventions are applied.

It presents the Alignment Control Stack (ACS), a 10-layer hierarchical model from physical hardware to socio-technical governance. The authors demonstrate how formal control methods can enhance current AI safety protocols by providing provable guarantees, robustness against adversarial strategies, and principled trade-off analysis.

The position advocated is that bridging current empirically-driven AI safety methods with control theory’s proven mathematical frameworks will result in more generalizable, and trustworthy alignment strategies for advanced and agentic AI systems. The Alignment Control Stack’s layered-control approach appears to be a new contribution to the AI safety literature.

### Strengths
- The paper argues its position clearly and discusses the alternative views in detail.
- The paper presents a clear, well-structured Alignment Control Stack that organizes alignment interventions across ten hierarchical layers from hardware to socio-technical governance.
- The inclusion of simulated case studies strengthens its claims by showing how tools of control theory can provide strategic insights and formal guarantees.
- The paper is well-written, and the appendix provided more details into the stack.

### Weaknesses
- The paper lacks real-world empirical validation of the Alignment Control Stack beyond toy simulations.
- It provides limited implementation details on how to practically integrate control-theoretic methods into existing AI development pipelines.

Minor:
- There is no need for subsection 1.1 if it is only one sub-section
- There are a few typos in the paper, I suggest revising.

### Questions
- How feasible is constructing tractable formal models for high-dimensional complex AI systems like LLMs or agentic AI where internal dynamics are only partially understood and change with fine-tuning or external tool calling? 

- In the Alignment Control Stack, how would you manage interactions across layers when control resources are limited, and could your framework quantify the balance or trade-off between acting at lower (technical) versus higher (socio-technical) layers?

### Presentation
4
