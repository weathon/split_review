# Position: Olfaction Standardization is Essential for the Advancement of Embodied Artificial Intelligence

- Decision: Reject
- Scores: 4, 6, 8

## Abstract
Despite extraordinary progress in artificial intelligence, modern systems remain incomplete representations of human cognition. 
Vision, audition, and language have received disproportionate attention due to well-defined benchmarks, standardized datasets, and consensus-driven scientific foundations. In contrast, olfaction—a high-bandwidth, evolutionarily critical sense—has been largely overlooked. This omission presents a foundational gap in the construction of truly embodied and ethically aligned super-human intelligence. We argue that the exclusion of olfactory perception from AI architectures is not due to irrelevance but to structural challenges: unresolved scientific theories of smell, heterogeneous sensor technologies, lack of standardized olfactory datasets, absence of AI-oriented benchmarks, and difficulty in evaluating sub-perceptual signal processing. These obstacles have hindered the development of machine olfaction despite its tight coupling with memory, emotion, and contextual reasoning in biological systems. In this position paper, we assert that meaningful progress toward general and embodied intelligence requires serious investment in olfactory AI research. We call for cross-disciplinary collaboration—spanning neuroscience, robotics, machine learning, and ethics—to formalize olfactory benchmarks, develop multimodal datasets, and define the sensory capabilities necessary for machines to understand, navigate, and act within human environments.  Recognizing olfaction as a core modality is essential not only for scientific completeness, but for building AI systems that are ethically grounded in the full scope of human experience.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
4

### Summary
The paper argues olfaction is a sensory modality neglected by the AI community and calls for an interdisciplinary collaboration to formalize olfactory benchmarks and develop multimodal datasets and more generally dedicate more researcher attention to this area. It also raises interesting ethical considerations around possible privacy violations brought about by the advancement of artificial olfaction.

### Strengths
The subject matter of olfaction that the paper calls attention to is intriguing and the paper provides a nice overview of the space. The paper's call for better olfaction-related data sets and benchmarks seems warranted. The potential ethical / privacy issues due to advancements in artificial olfaction are interesting.

### Weaknesses
- The difference between olfaction as (a) the chemosensory hardware problem (detecting the chemical and issuing a signal to the brain) and (b) the subjective cognitive experience problem (interpreting the signal, predicting how molecule in a given concentration smells to humans) is not clearly discussed. The paper would be stronger if the distinction were clearer - or if the paper re-focused on one of the areas. 
- The paper claims olfaction research is overlooked, but it is unclear if this point is properly supported. E.g., the fact that few papers on the topic are published on arxiv could be simply sociological - this research is more likely to appear in chemistry, electrical engineering, neuroscience journals. It is also not clear how comprehensive semantic scholar source publication set is. How about bioarxiv? On similar point, electric nose research has a very long history and while it is mentioned, it feels like the paper understates the amount of work and findings done in the area - at least, I did not feel I got a comprehensive enough review of it. A cursory look suggests ML in olfaction is also a reasonably active research area: https://www.science.org/doi/10.1126/science.aal2014
- The proposal are vague / lack details.

### Questions
- The chemosensory side of olfaction problem seems to lie substantially in the hardware limitations - it is not easy to detect minuscule concentration of many different chemicals at once. Then, should this paper in the part where it talks about that hardware side of olfaction even be addressed to AI research community? Perhaps, it is better fitted for material scientists or electrical engineers?
- What exactly should the benchmarks and the data sets that you call for look like? Perhaps, you could provide idealized examples?

### Presentation
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This position paper argues that smell is a crucial but overlooked sense for embodied artificial intelligence. It identifies five core obstacles: missing scientific models of odor encoding, absence of data format standards, subjective annotation practices, limited large scale odorant data sets, and a lack of unified evaluation benchmarks. To overcome these challenges the authors propose first defining chemical encoding schemes, next developing rigorous human rater protocols, then assembling open and diverse odor collections and finally creating task driven benchmarks such as odor classification and smell guided navigation that integrate into existing embodied AI platforms. The authors advocate establishing a standards body to coordinate tooling, data sharing, governance and funding. By bringing olfaction into parity with vision and language the paper contends that embodied agents will gain richer more human like perception.

### Strengths
1. By contrasting continuous receptor mappings in vision and audition with the discrete combinatorial coding of odorant molecules the paper highlights a unique challenge and opportunity for AI the need for new data representations and neuromorphic event based processing architectures.

2. The paper uses the coffee example (Figure 3) to show how smell adds critical information when vision alone is insufficient.

3. The paper situates olfaction alongside vision and audition in emerging olfaction vision language models OVLMs emphasizing how chemical sensing can be fused with high fidelity perception and reasoning systems.

4. The paper clearly enumerates five systemic gaps including scientific understanding data standards annotation datasets and benchmarks and proposes a sequential roadmap that defines chemical encodings annotation taxonomies curation of open odorant collections and creation of task driven benchmarks to drive community action.

### Weaknesses
1. The paper asserts that olfaction is essential for embodied AI but does not critically examine scenarios where smell might offer minimal benefit over well-established modalities like vision or audition.

2. The paper outlines data standard definition, annotation protocols, consortium formation and benchmark creation but provides no actionable details such as timelines or milestones; governance models or funding mechanisms for the proposed consortium; or concrete procedures for defining and calibrating annotation taxonomies.

### Questions
1. Which procedures would you recommend for constructing and validating the annotation taxonomy to handle ambiguous or culturally biased descriptors?

2. Can you identify specific embodied-AI tasks where olfaction is likely to provide significant performance improvements over existing modalities?

### Presentation
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper argues that a lack of standardization in olfaction is a significant obstacle to developing truly embodied artificial intelligence (AI). While other senses like vision, audition, and language have well-defined benchmarks and datasets, olfaction has been largely overlooked. The authors identify five key challenges: a lack of scientific consensus on the mechanisms of smell, heterogeneous sensor technologies, a lack of standardized datasets, the absence of AI-specific benchmarks, and the difficulty of objective evaluation. They advocate for a cross-disciplinary effort involving neuroscience, robotics, and machine learning to create olfactory benchmarks and multimodal datasets. The paper asserts that overcoming these challenges is crucial for building AI systems that are both scientifically complete and ethically grounded in the full human experience.

### Strengths
The paper is rich in content, interesting, and makes a very strong case for the development of Olfaction Datasets. 
It's good that Supplementary Material was included.

### Weaknesses
I thought the paper was engaging and interesting. It seems, however, to have been written in a rush. Perhaps something about possible uses of AI with olfaction could be added to the introduction. Also, citation of related work is missing at times, such as in line 168.

There is a space missing in line 114.

Lines 268 to 278 are crucial for the paper and outline the recommendations, but they are under section 2.4 - The Case for Olfaction. Maybe this could be moved so it gets more attention?

### Questions
The paper mentions that the human olfactory system processes information episodically, in "brief, irregular bursts" due to the nature of turbulent plumes. Do you think this should inform the generation/collection of Olfaction Data in any way?

### Presentation
2
