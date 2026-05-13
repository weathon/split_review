# From Tokens to Lattices: Emergent Lattice Structures in Language Models

- Decision: Accept
- Scores: 1, 6, 6, 8, 6

## Abstract
Pretrained masked language models (MLMs) have demonstrated an impressive capability to comprehend and encode conceptual knowledge, revealing a lattice structure among concepts. This raises a critical question: how does this conceptualization emerge from MLM pretraining? In this paper, we explore this problem from the perspective of Formal Concept Analysis (FCA), a mathematical framework that derives concept lattices from the observations of object-attribute relationships. We show that the MLM's objective implicitly learns a formal context that describes objects, attributes, and their dependencies, which enables the reconstruction of a concept lattice through FCA. We propose a novel framework for concept lattice construction from pretrained MLMs and investigate the origin of the inductive biases of MLMs in lattice structure learning. Our framework differs from previous work because it does not rely on human-defined concepts and allows for discovering "latent" concepts that extend beyond human definitions. We create three datasets for evaluation, and the empirical results verify our hypothesis.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The work focuses on generating concept lattices from masked language models such as BERT, RoBERTA, etc. The idea is to utilize the information contained in these models for generating a partial ordering of the concepts instead of learning the concepts from textual information.

### Strengths
--> Concept lattices are directly constructed from masked language models.

### Weaknesses
--> It should be made clear in the paper if the authors are directly constructing the concept lattice or the formal context first and then generating the lattice. This makes a difference since generating concept lattices starting from a formal context is computationally expensive.
--> The contributions/research questions of the paper should be explicitly mentioned in the introduction.
--> Why not using Large Language Models for constructing lattice and comparing it to masked language models since the masked language models are not fine-tuned they are rather used by masking the tokens.
--> The broader applicability of these lattices is a bit unclear, where would these lattices be used? If the objective is to classify the terms into the classes then this can be done without passing through the concept lattice generation phase. i understand that there is a partial ordering between the concepts but there is a concept of hierarchical classification.
--> Introduction should have a clear example/scenario for motivating the objectives of this work.

### Questions
--> Are authors directly generating a concept lattice or generating a formal context? 
--> What is the computational complexity of generating the context and then the lattice?
--> What is the broader applicability on where these lattices can be used for solving which tasks? 
--> Why not prompt Large Language Models which contain much more information?

### Soundness
2

### Presentation
2

### Contribution
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
The authors propose a framework that uses Formal Concept Analysis (FCA), to explore the conceptual understanding of an MLM (Masked Language Model) and their hierarchical relationships. 
FCA is a well-known mathematical framework researched in the early 2000's or so. FCA aims to uncover concept lattices from attribute-value data. 
MLM are trained neural networks that aim to predict a masked token in a sentence given its context. They are known to be capable of contextual understanding that can be used as pre-training in various NLP tasks. 
The big question the authors pose is: how does conceptualization emerge from pre-training an MLM?
The authors hypothesize that MLMs learn the conditional dependencies between objects and attributes under certain patterns. Then they propose a framework to probe MLMs through the use of FCA to construct a lattice of latent concepts without relying on human-defined ontologies. Their empirical evaluation, using three datasets they developed, showed that conditional probabilities in MLM can help recover formal contexts and construct concept lattices.

### Strengths
+ Bridging the gap between FCA and MLM is a good idea that shows that old and new AI can work in tandem, especially when it comes to the interpretability of black-box models and their usefulness in subsequent tasks. Using FCA could be a nice step in this direction. 

+ Paper well-written in general, appropriate citations.

+ The formalization seems appropriate. 

+ The ability to uncover latent concepts without human ontologies gives a chance to non predefined concepts to emerge and hence has the potential to increase our knowledge in the domain.

### Weaknesses
 - There is a lack of general motivation on why it is important to uncover the lattice of the concepts embedded in an MLM and how it will be used. If the goal is XAI, the authors should highlight it. Specifically, the paper does not articulate the downstream benefits of understanding the conceptual organization within an MLM. It is unclear how this lattice structure would be used to improve model performance, interpret predictions, or gain new insights into language understanding.

-  The scalability of the framework to multi-relation is unclear and using one single relation seems quite limiting. While it is mentioned by the authors as a limitation, a discussion about how limiting the lattice to one relation can miss patterns would be good. The authors could discuss the challenges that might arise when tackling multi-relations. This might include the complexity of the lattice itself. The paper does not explore the potential for the lattice to become exponentially complex with the inclusion of multiple relations, and how this would impact the computational feasibility of the approach. The authors should also discuss how the choice of relation affects the resulting lattice and whether some relations are more informative than others.

- The experimental section is limited in the number and choice of the datasets. The datasets used are not standard benchmarks, making it difficult to compare the results with other methods. The paper would benefit from a more thorough evaluation using a wider range of datasets, including those with more complex relationships and larger vocabularies. The authors should also justify the choice of datasets and discuss their limitations.

### Questions
1-  How can the lattice of concepts be leveraged in NLP tasks?
2-  Does using only one relation mean that FCA does not allow capturing the full extent of the conceptual understanding the MLM is capable of?
3- How are the uncovered concepts labeled?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In the paper “From Tokens to Lattices: Emergent Lattice Structures in Language Models” submitted to ICLR 2025, the authors answer the question whether Formal Concept Analysis  concept lattices can be extracted in a meaningful way from an MLM, such as BERT. They answer this question positively, which is demonstrated by a dedicated experiment.

### Strengths
I find the paper interesting to read. It studies a sound problem about an ability of LLMs to perform Symbolic AI tasks.

### Weaknesses
Definition 5 is vogue, it is more like an intuition rather than definition.

In L (line) 263, it is said that data generation (i.e., Abstraction 1) is an inherently noisy process. However, I do not see anything noisy in Abstraction 1, everything is nice and clean. What is meant by noisy here?

In L 253, Animal-behaviour dataset is presented. But where does the data come from? Is it just the authors’ beliefs and nothing more?

In L 374, it is said “We formalize the problem as a recommendation system problem”. But this is not clear at all without further details, and so the essence of the first experiment is not clear for me.

In the introduction and the conclusion, it is emphasised that the suggested method does not depend on predefined human concepts and ontologies. However, it is misleading: it clearly depends on humans, who have to provide patterns B.

Minor:
L 53: extra whitespace after “possible”
L 99: D should be \mathcal D and p_\theta should be defined
L 125: Do not start a sentence with a math symbol, especially if the previous one ends with such a symbol
L 211: Start the definition with “Given a pattern b”
L 237: b \in B should be in the subscript
L 243: g, m should be in the subscript
L 268: it should be defined what is the distance in this context
L 275, 278: bf w should be just w
L 285: hypothesis
L 290: standard notation F: D \to I says that F is a function with domain D and range I. This is clearly not what you want to say here. Also, D should be \mathcal D.

### Questions
Every comment in the weakness section, except the list of minor corrections, is essentially a question.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper explores how masked language models (MLMs) like BERT inherently learn conceptual relationships by organising knowledge into "concept lattices" through a framework called Formal Concept Analysis (FCA). The authors demonstrate that through this framework MLMs can reconstruct concept relations directly from language patterns in an more effective and explainable way.

### Strengths
- This work introduces a well-structured FCA-based probing framework that translates MLM logits to formal contexts, allowing for insightful analysis.
- The constructed concept lattices effectively recover and represent conceptual knowledge that MLMs encode.
- The framework also ensures efficient construction of concept lattices.

### Weaknesses
 - The baseline models only consider naive BERT embeddings, omitting a range of established probing techniques known for their effectiveness, such as prompt-based probing in natural language inference (NLI) formats. Incorporating these methods would provide a stronger basis for claiming that this FCA-based framework is more effective in extracting knowledge from MLMs.

- The evaluation is limited to "single-token" named entities, which may restrict dataset coverage. While the `[MASK]` token only predicts one token at a time, several methods exist to approximate multi-token predictions.

- A minor point concerns the definition of MLM. In practice, not every token in a sequence is masked, so it would be more accurate to define MLMs with respect to a set of sampled masked tokens.

### Questions
- Have you considered the issue of potential ill-formed entity or relation names fitting into the template, which might introduce bias into evaluation?

- A minor point concerns the definition of MLM. In practice, not every token in a sequence is masked, so it would be more accurate to define MLMs with respect to a set of sampled masked tokens.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores how masked language models (MLMs) like BERT implicitly capture conceptual knowledge and organize it into lattice structures. The authors employ Formal Concept Analysis (FCA) to illustrate that MLMs' training objectives inherently form a "formal context" that can be mapped into a lattice framework. The paper diverges from traditional approaches by not relying on human-defined concepts, instead proposing that MLMs capture "latent" or unspoken concepts beyond human ontologies. The author examines this approach in three datasets: region-language, animal-behavior and disease-symptom, and concludes that MLMs are efficient in modeling the concept hierarchies in probabilistic terms.

### Strengths
1. The innovative application of FCA enables the reconstruction of concept lattices without relying on human-defined concepts and ontologies, allowing for the discovery of latent concepts that traditional methods might overlook.

2. The paper includes a variety of visualizations that effectively illustrate key concepts, enhancing clarity and engagement.

3. The proposed method is computationally efficient, making it practical for implementation without requiring additional training or significant resources.

4. The paper offers a thorough empirical analysis across diverse domains, which supports the validity of its claims that MLMs can generate meaningful concept lattices.

### Weaknesses
1. The study relies on carefully curated datasets that may not capture the complexity or variability of real-world language use. Expanding the dataset to include a broader range of contexts and ambiguities would enhance the framework’s robustness and applicability.

2. While concept lattices offer a structured hierarchy, they are currently limited to modeling simple object-attribute relationships. Incorporating more nuanced or multi-relational knowledge types would broaden the framework’s applicability.

3. The paper’s presentation could be significantly improved. Simplifying the exposition and emphasizing intuitive explanations would make the work more accessible and engaging.

### Questions
1. Can this framework be applied to autoregressive language models (e.g., GPT series) instead of masked language models?

2. How are concept patterns selected for this framework? Are they designed empirically by humans, and to what extent could different patterns impact the results?

3. How might this framework perform on larger, more complex datasets with more ambiguous or polysemous relationships?

### Soundness
2

### Presentation
2

### Contribution
2
