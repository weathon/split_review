# Beyond Monoliths: Expert Orchestration for More Capable, Democratic, and Safe Large Language Models

- Decision: Reject
- Scores: 3, 3, 6

## Abstract
This position paper argues that the prevailing trajectory toward ever larger, more expensive generalist foundation models controlled by a handful of big companies limits innovation and constrains progress. 
We challenge this approach by advocating for an “Expert Orchestration" architecture as a superior alternative that democratizes LLM advancement. 
Our proposed architecture intelligently selects from thousands of existing models based on query requirements and decomposition, focusing on identifying what models do well rather than how they work internally. 
Independent “judge" models assess various models' capabilities across dimensions that matter to users, while “router" systems direct queries to the most appropriate specialists within an approved set. 
This approach delivers superior performance by leveraging targeted expertize rather than forcing costly generalist models to address all user requirements. 
The expert orchestration paradigm represents a significant advancement in LLM capability by enhancing transparency, control, alignment, and safety through model selection while fostering a more democratic ecosystem.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper argues for an "Expert Orchestration" framework as an alternative to the prevalent monolithic approach brought about by the development of LLMs by large corporations, which have the resources to train frontier LLMs that are general and good enough for multiple (all) tasks. The authors first provide critique about concentrating resources and models, focusing on the (i) monopolistic market dynamics brought about by the dominance of a few big companies (leading to more bias, speed to gain market share and less concerns about safety, fairness, societal equity) and the (ii) technical difficulties of building a know-it-all general monolithic model with add-ons tools such as RLHF, prompt engineering, with less understanding on how they work and "think" and control on their outputs. The authors then build an argument for expert orchestration from diverse fields (economics, organizational theory, cognitive science, biology) as well as democracy, alignment and safety aspects. The framework has two important roles: Judges (evaluator of experts wrt queries) and Routers (route queries to experts) and can lead to superior performance and provide benefits such as higher transparency, alignment, control, more competitive markets.

### Strengths
The topic that the authors have chosen to address is an important one and with the advent of LLMs that are owned and trained by large corporations and the community in general would prefer a more transparent and reproducible approach. The expert orchestration framework is presented as such and the authors use the pattern of specialization in other diverse fields such as market economics, knowledge distribution, organizational theory, cognitive science to support the need for an expert orchestration framework with diverse experts specializing in their fields over a single generalist model which can perform many tasks. The framework is straightforward with judges to provide evaluation scores across different metrics (which each judge is a specialist in) and routers to choose experts to address user queries.

### Weaknesses
1. The definition of the expert models is not clear in the paper. Are they just the judges and routers or task-specific? Expert or specialist models can be derived from LLMs using 'fixes' claimed by the authors, such as prompt engineering, RLHF. In this case, the development of LLMs and expert models are dependent and not mutually exclusive. The authors acknowledge this but claimed that "expert orchestration enables the full value of foundation models to be realized through selective specialization, fine-tuning, and deployment" and these are enabled by "fixes" that have been claimed to be detrimental.
2. The use of diverse fields to support the need for expert orchestration while interesting, may not fully reflect how foundational LLMs are trained and how human experts are developed. LLMs are trained with as much data (breadth and depth) as possible and experts LLMs (more depth with same breadth), compared to a human generalist (breadth) individuals and a human expert (depth with certain breadth). As such, what may work for other fields may not work for LLMs.
3. The idea of routing is not exclusive to expert orchestration and has already been used in training LLMs. It is not clear what is the value-add over current methods.

### Questions
1. Can you elaborate on how Figure 1 explains decomposition and routing? It is very abstract to me.
2. The figures are not referred in the text and seems to be arbitrarily placed. 
3. How is the expert orchestration framework different from the agentic AI framework, which is also pushed by big corporations building LLMs? Is there any reason why it is not considered in the paper?
4. Are the benefits in Section 5 only achievable using the expert orchestration framework?
5. Will a hybrid approach work? Monolithic LLMs development with expert orchestration to improve them?

### Presentation
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
This paper considers that prevailing trajectory toward ever larger, more expensive generalist foundation models controlled by a handful of big companies limits innovation and constrains progress. 

To argue this, they propose using an expert orchestration framework as an alternative approach to help research and development for LLMs.

### Strengths
The proposed framework is interesting. 

The paper addresses important problems and highlights the benefits of using specialized models in integrated framework. It aggregates a wide spectrum of recent research (routing, MoE, continual learning, safety, bias) and even foundational economic/ethical texts.

Each identified challenge is paired with concrete, actionable strategies (e.g., cost‑aware routers for inference, balanced fine‑tuning to curb forgetting).

The paper also presents an interdisciplinary lens incorporating economic and ethical frameworks (e.g., Smith, Ricardo, Wu) frames technical choices within broader societal implications, encouraging responsible AI deployment.

### Weaknesses
The motivation of the paper is interesting. However, it should be considered the large scale foundation models and the proposed distributed orchestrated frameworks of smaller expert models have been both utilized by different companies, labs., researchers etc. for different tasks. 

Therefore, it is not  clear how the proposed framework will lead a paradigm shift.

The manuscript focuses on benefits but does not discuss downsides (e.g., increased maintenance for routing, complexity of MoE gating). Practical concerns such as heterogeneous hardware, latency budgets, and regulatory compliance are omitted. That is, it is not clear how small research labs or individual researchers will be able to develop and employ this framework resolving the limitations imposed by the aforementioned big companies.

### Questions
What are the main downsides you anticipate for each recommendation (e.g., increased maintenance for routers, potential loss in robustness with MoE gating)?

Do you have any guidance on when a particular approach might be overkill for smaller deployments versus large‑scale production systems?

How do you foresee routing and MoE architectures performing on edge devices or heterogeneous hardware environments (e.g., GPU vs. TPU)?

Are there regulatory considerations (GDPR, HIPAA) that influence your choice of routing strategies or model partitioning?

Can you elaborate on the coordination logic between multiple specialized models in your proposed compound system?

### Presentation
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper analyzes the technical and structural problems of the mainstream monolithic LLM paradigm and proposes an alternative framework called Expert Orchestration. The authors argue that competition centered on large corporations not only limits innovation but also risks concentrating AI power. They further note the inherent weaknesses of single models. The proposed framework consists of two core components. First, independent Judge models evaluate LLM outputs using multi-dimensional criteria such as legality and ethics. Second, Router integrates these evaluations with user requirements to direct queries to the most suitable expert model. The authors claim this approach enhances performance, cost-efficiency, safety, and transparency.

### Strengths
- This is a very well-written paper and highly suitable for a position paper. It has a clear problem statement, justification, and future direction.

- Directly challenges the dominant monolithic LLM paradigm and proposes the concrete alternative of Expert Orchestration.

- It moves beyond simple critique by proposing specific components, such as 'Judge models' and 'Routers,' and provides a clear roadmap for the research community through its discussion of open research questions (Section 6).

- Grounded in reality by referencing existing technologies (e.g., Mixture-of-Experts, FrugalGPT), which supports feasibility.

### Weaknesses
- While the vision of a system where numerous models are fairly evaluated and seamlessly connected by objective 'Judge' models is compelling, it is also highly idealistic. The success of the entire framework could become critically dependent on the performance and objectivity of these Judge models.

- Implementation raises major engineering challenges, including API standardization, version control, and maintaining large-scale reliability.

### Questions
- How can the objectivity and reliability of Judge models be secured and validated?
- How can "expertise" be formally defined and measured to ensure that the Router makes optimal decisions when selecting among specialist models?

### Presentation
4
