# Simulating Society Requires Simulating Thought

- Decision: Accept
- Scores: 7, 9, 6

## Abstract
Simulating society with large language models (LLMs), we argue, requires more than generating plausible behavior; it demands cognitively grounded reasoning that is structured, revisable, and traceable. LLM-based agents are increasingly used to emulate individual and group behavior, primarily through prompting and supervised fine-tuning. Yet current simulations remain grounded in a behaviorist “demographics in, behavior out” paradigm, focusing on surface-level plausibility. As a result, they often lack internal coherence, causal reasoning, and belief traceability, which makes them unreliable for modeling how people reason, deliberate, and respond to interventions.

To address this, we present a conceptual modeling paradigm, Generative Minds (GenMinds), which draws from cognitive science to support structured belief representations in generative agents. To evaluate such agents, we introduce the RECAP (REconstructing CAusal Paths) framework, a benchmark designed to assess reasoning fidelity via causal traceability, demographic grounding, and intervention consistency. These contributions advance a broader shift: from surface-level mimicry to generative agents that simulate thought—not just language—for social simulations.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
3

### Summary
This position paper argues that the recent development of simulating a society with LLMs requires the simulation of thought. That is, it must be grounded reasoning, structured, revisable and traceable.
In essence, this means that we must focus on structuring their reasoning, rather than relying on just their outputs.
The position argues for constructing reasoning graphs via semi-structured interviews that LLM agents should utilise in social simulations to mitigate issues regarding diversity, fidelity, and traceability.

### Strengths
This paper provides solid evidence and is well embedded in the (cognitive science) literature for the proposed requirements; in particular, the motivating and illustrative examples are helpful. The responses to the alternative views are well-grounded in literature and examples.

### Weaknesses
The key concern regarding this position is that some of this seems to be in the works already. Reasoning LLMs can self-correct by simulating their thinking for a given problem when they find contradictions. While the presented framework concretises beliefs, and the current reasoning LLMs are susceptible to the issues the paper mentions, it seems already quite effective.

The other concern is that using Q&A-style interviews to structure reasoning and simulate thought could ultimately still have issues like hallucinations. I feel this could have been addressed more strongly in the alternative view regarding traceability. It is possible that I don't fully appreciate the position this paper proposes. However, it seems that such reasoning graphs, as in my previous example, could still easily capture errors that the framework attempts to mitigate.
Still, I think this position could spark a debate that pushes for better reasoning models.

### Questions
How does this position fit with the current advancements in reasoning LLMs that already implement a kind of thought simulation?

### Presentation
3

---

## Human Reviewer 2

### Rating
9

### Rating Number
9

### Confidence
4

### Summary
This paper is on simulating society with large language models (LLMs). Rather than generating plausible behaviour, cognitively grounded reasoning is suggested that is structured, revisable, and traceable. Although these language models can be improved through prompt engineering, fine-tuning, and other techniques, they lack internal coherence and causal reasoning. Belief traceability also needs to be constructed such that how people reason, deliberate, or respond to interventions should also be taken into consideration. Hereby the authors present two contributions: 1) A Conceptual Modelling Paradigm, called Generative Minds, that support structured belief representations for agents. 2) RECAP (REconstructing CAusal Path), a benchmark that assesses reasoning fidelity through causal traceability, demographic grounding, and intervention scenarios. The authors posit that we must concentrate on simulating thought patterns, rather than focussing on predicting next tokens, the approach resorted to by LLMs. From real-world, semi-structured interviews, how people explain and revise their beliefs can be captured, leveraging belief graph networks. RECAP can be used as a replicable schema for reasoning evaluation, not as a static dataset only.

### Strengths
The paper is very well-written, well-structured, and clear. What they suggest have potential in principle and practice to be implemented. The authors exemplify what they posit and their arguments are solid. They argue their opinions clearly in detailed and comprehensible manner. All the arguments they suggest are supported with reasoning and evidence. The topic is very relevant and important to the NeurIPS community. What they posit would have a large societal impact on LLMs and AI, since the current language models mostly concentrate on generating fluent texts, lacking coherent belief systems. Only focussing on predicting the next token sensibly might not be called real intelligence as also covered by the authors. Leveraging conceptual belief models and updating them consistently may be what society really needs as an evolving "entity", also caring about the diversity and different ideologies of individual persons. Once we simulate real thinking processes as mentioned in the paper, we can contribute to humanity overall in a more effective and practical manner.

### Weaknesses
The paper only has several weaknesses as I stated below: 

1) Maybe some more details on constructing alternative conceptual belief networks along with their implementation difficulties could be mentioned. For example, different cultures and domains might need varying conceptual belief networks; in this case human in the loop processes could be incorporated in addition to the semi-structured approaches handled by LLMs as well, and it might be a bit labourious, based on such different scenarios.
2) Apart from the use of the em-dash character frequently that is also stated to be widely produced by AI tools (e.g., ChatGPT) a lot, the following typos and format issues had better be addressed as well:

i) Page 1. Line 18: .In the field of -> . In the field of (A white space to be added after the dot.)
ii) Page 8. Line 382: Design Principles. -> Please, move it to the next page so that the list header aligns better with the items

### Questions
1) As mentioned in the weaknesses part, could we incorporate human in the loop processes per different culture, ideology, etc. in a more effective manner and create different belief models, for example, per country or nation / religion, etc.? For example, some concepts can connote different meanings and polarities for various cultures, religions, and ideologies. If implementing all of these be considered to be labourious (not only using LLMs for semi-structured data), what approaches can be followed? 
2) Can we leverage some already-existing ontology or conceptual models, such as ConceptNet 5, to make the process easier by updating these a bit? There are some similar studies in the literature and on-going projects being conducted by mostly top-tier companies, such as OpenAI, Google, and Meta.

### Presentation
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Generative Minds (GenMinds), a cognitively grounded framework for modeling structured and traceable reasoning in LLM-based agents. To evaluate such agents, the authors propose RECAP, a benchmark assessing causal traceability, demographic grounding, and intervention consistency—advancing social simulation beyond surface-level behavior to deeper cognitive fidelity.

### Strengths
1. Clear Problem Identification with Practical Relevance
The paper clearly identifies the limitations of current LLM-based social simulations—such as shallow reasoning, hallucinations, and lack of interpretability—and frames these as critical issues in real-world applications like policymaking and stakeholder modeling.

2. Innovative Shift from Behavioral Mimicry to Cognitive Modeling
It proposes a compelling conceptual shift from surface-level behavior mimicry to cognitively grounded reasoning using Theory of Mind and modular reasoning traces. This shows originality and strong theoretical grounding.

3. Emphasis on Interpretability and Causal Traceability
The argument for modeling reasoning fidelity—including causal, compositional, and revisable belief structures—addresses a major gap in the field, potentially improving both trust and utility in high-stakes decision-making scenarios.

### Weaknesses
1. Lack of Concrete Implementation or Empirical Evidence in Introduction
While the ideas are conceptually strong, the introduction doesn't clearly state whether these frameworks (e.g., modular reasoning motifs, symbolic-neural models) are implemented or just proposed. It risks remaining at a theoretical level without demonstrated feasibility.

2. Ambiguity Around Scalability and Practical Deployment
Although the proposed approach claims better efficiency and generalization, it’s unclear how well this symbolic-neural framework scales to large, real-world datasets or complex simulations involving many stakeholders.

3. Limited Discussion of Limitations or Potential Pitfalls
The introduction does not preemptively address potential challenges, such as how modular reasoning would handle ambiguity in natural language or conflicting stakeholder beliefs, which are common in social contexts.

### Questions
See 'Weakness'

### Presentation
3
