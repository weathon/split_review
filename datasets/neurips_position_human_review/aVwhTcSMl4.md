# World Models Should Prioritize the Unification of Physical and Social Dynamics

- Decision: Accept
- Scores: 6, 6, 7

## Abstract
World models, which explicitly learn environmental dynamics to lay the foundation for planning, reasoning, and decision-making, are rapidly advancing in predicting both physical dynamics and aspects of social behavior, yet predominantly in separate silos. This division results in a systemic failure to model the crucial interplay between physical environments and social constructs, rendering current models fundamentally incapable of adequately addressing the true complexity of real-world systems where physical and social realities are inextricably intertwined. This position paper argues that the systematic, bidirectional unification of physical and social predictive capabilities is the next crucial frontier for world model development. We contend that comprehensive world models must holistically integrate objective physical laws with the subjective, evolving, and context-dependent nature of social dynamics. Such unification is paramount for AI to robustly navigate complex real-world challenges and achieve more generalizable intelligence. This paper substantiates this imperative by analyzing core impediments to integration, proposing foundational guiding principles (ACE Principles), and outlining a conceptual framework alongside a research roadmap towards truly holistic world models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- this paper proposes theoretical guidelines/principles on designing intelligent systems that integrates physical and social dynamics, rather than building world models that consider only one of the two dimensions. The principles are briefly discussed and a framework definition is proposed that creates joint physical and social states.

### Strengths
- it tackles a well-known limitation of current intelligent agents' world models which is of interest of the NeurIPS community
- the proposed framework is clearly presented and supported by most up-to-date related approaches
- it provides a long list categorizing existing world model methods into physical and social

### Weaknesses
- this work does not mention digital twins which increasingly have been modelling physical and social dimensions together
- limitations of existing approaches are not discussed in depth (simulated environments with traditional text-based LLMs)
- more discussion on multimodality and its limitations compared to the proposed framework

### Questions
- which are the current benchmarks or tasks that could show that current models fail to integrate social-physical aspects? 
- the example provided: "A purely physical model might predict a ball’s trajectory if thrown, but ... its physical characteristics." -> If context (video) is provided to a multimodal model, won't it be able to say the intent of throwing a ball? 
- how does your proposal compares to social digital twins? (https://www.mdpi.com/2624-6511/8/1/23)
- there is some work on multiagent environment that integrates social and physical aspects (https://arxiv.org/abs/2506.12331v1) and also
- project Sid hasn't been discussed where multi agent Minecraft simulations with thousands of agents simulate physical and social interactions to build civilizations (https://arxiv.org/html/2411.00114v1). Despite not having joint states, what are the limitations of these simulated environments? 
- physical and social dimensions are not already implicitly embedded in multimodal systems such as Veo3 or even OpenAI o3? What would be the advantage of creating physical-social states instead of simply use multimodality? Aren't those states already capturing physical and social dynamics (among other dimensions)?

### Presentation
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This position paper argues that the next major step for world model development is the bidirectional unification of physical and social dynamics. Current models are siloed, either on physical prediction (e.g., reinforcement learning, intuitive physics) or social modeling (e.g., preferences, Theory of Mind), which limits their applicability in complex real-world scenarios where these dimensions interact. The paper reviews the limitations of both paradigms, proposes the ACE Principles (Abstraction, Contingent causality, Entangled emergence) for guiding integrated modeling, and introduces a conceptual framework (WMP-S) that treats the physical-social world state as a coupled system. The authors advocate for this unified modeling as essential for building robust, generalizable AI systems capable of interacting meaningfully in human-centric environments.

### Strengths
The paper presents a novel, forward-looking position rooted in theoretical rigor and empirical insight. It provides a comprehensive analysis of the limitations of current physical and social world models, synthesizes interdisciplinary knowledge, and proposes actionable principles (ACE) for future research. Its conceptual framework (WMP-S) offers a clear path forward. The writing is clear, the motivation is well-articulated, and the topic is of high relevance to NeurIPS and broader AI research.

### Weaknesses
The proposal is largely conceptual and could be further strengthened by empirical case studies or concrete prototype implementations. While the unification argument is compelling, more detail on how to resolve practical issues like data alignment, computational scalability, and evaluation of integrated models would be valuable. The ACE Principles are sound but might benefit from comparative examples or counterpoints. There is also limited discussion of how this integration might be applied across diverse cultural or ethical contexts.

### Questions
- How might the proposed WMP-S framework be evaluated in practice? Are there benchmark environments where physical and social dynamics are sufficiently represented?
- What are the most critical technical barriers to implementing the ACE principles at scale?
- How might this framework account for culture-specific social dynamics that don’t generalize easily?

### Presentation
2

---

## Human Reviewer 3

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This position paper argues that the next major leap for AI world models lies in the deep, bidirectional unification of physical and social predictive capabilities. The authors point out that current research largely develops models for physical dynamics (e.g., model-based RL, video prediction) and social dynamics (e.g., preference modeling, Theory of Mind, LLM-based agents) in isolation, resulting in incomplete representations of real-world complexity. They analyze the limitations of this separation, survey the state of the art in both dimensions, and propose the ACE Principles as guiding tenets for future work: Abstraction of social complexity and heterogeneity, Capturing contingent causality, and Enabling entangled system emergence and co-evolution. They further provide a conceptual framework (WMP-S) and research roadmap for developing holistic world models that integrate both physical and social domains. The paper's central position is that such unification is essential for robust, generalizable, and socially-aware AI systems capable of navigating the full complexity of real-world environments.

### Strengths
1. Clear and timely position: The paper identifies a critical bottleneck in world model research and argues convincingly for its resolution.

2. Comprehensive literature review: Both physical and social world modeling paradigms are reviewed, making the gap and integration challenges concrete.

3. Conceptual innovation: The ACE Principles provide a useful intellectual framework that could guide future work.

### Weaknesses
1. Lack of concrete implementation or case studies: The framework is conceptual; no empirical demonstration or detailed implementation proposal is given, which may limit immediate practical uptake.

2. Evaluation and benchmarking: The paper does not propose specific evaluation metrics or benchmarks for integrated physical-social world models.

3. Scalability and data availability: While challenges such as data scarcity and complexity are acknowledged, more concrete strategies for addressing these (e.g., multi-modal data collection, transfer learning) would strengthen the roadmap.

### Questions
1. How might the field begin to build and benchmark the first integrated physical-social world models? Are there specific domains or simulation environments you recommend as testbeds?

2. Do you envision this integration as a monolithic architecture, or a modular combination of physical and social modules with shared representations?

### Presentation
3
