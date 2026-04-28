# Learning Diagrams: A Graphical Language for Compositional Training Regimes

- Decision: Accept
- Avg Score: 5.67
- Scores: 3, 8, 6

## Abstract
Motivated by deep learning regimes with multiple interacting yet distinct model components, we introduce learning diagrams, graphical depictions of training setups that capture parameterized learning as data rather than code. A learning diagram compiles to a unique loss function on which component models are trained. The result of training on this loss is a collection of models whose predictions ``agree" with one another. We show that a number of popular learning setups such as few-shot multi-task learning, knowledge distillation, and multi-modal learning can be depicted as learning diagrams. We further implement learning diagrams in a library that allows users to build diagrams of PyTorch and Flux.jl models. By implementing some classic machine learning use cases, we demonstrate how learning diagrams allow practitioners to build complicated models as compositions of smaller components, identify relationships between workflows, and manipulate models during or after training. Leveraging a category theoretic framework, we introduce a rigorous semantics for learning diagrams that puts such operations on a firm mathematical foundation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work formalizes machine learning training using learning diagrams.
A learning diagram is defined as a directed graph that allows the composition of learning components, models, and loss functions.
The work uses a colimit construction for building training pipelines as diagrams which consist of sub-diagrams. Finally, a softwware library, DiagrammaticLearning.jl, implements the provided formulation.

### Strengths
1. This work presents an elegant mathematical notation and formulation of automated machine learning (AutoML) based on directed graphs consisting of machine learning primitives and losses. The work formalizes the creation of machine learning pipelines.

2. A software library is presented that implements this formulation.

### Weaknesses
1. It is unclear what advantage this framework provides over previous work on automated machine learning, specifically AutoML systems based on directed graphs of machine learning components, or machine learning pipelines.

2. The empirical performance improvement over trivial baselines, as described in Tables 2 and 3, is not significant: 1-3% compared to a weak baseline.

3. The work lacks novelty with respect to the broad field of AutoML, which consists of machine learning primitives, automated machine learning systems, and user interfaces, developed over the past decade:

a. See for example derivatives of the D3M project.

b. A book on AutoML: Automated Machine Learning, Hutter, Kotthoff, and Vanschoren, Springer Nature, 2019

c. AutoML systems:
Auto-sklearn, Google Cloud AutoML, H2O AutoML, AlphaD3M, Auto-Keras, AutoGluon, to name a few,

d. Ignoring an entire field of work presented in AutoML conferences and workshops since 2016.

### Questions
What capability does this formalism provide that is unavailable in existing AutoML systems?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new approach to managing complex ML training setups called learning diagrams. It offers a new, more structured, way of looking at compositionality and interaction between different components (like data and different models) in composite learning settings. More specifically, in the learning diagrams framework nodes represent objects within a training regime, which can be data spaces, intermediate representations or parameter spaces. Each node, representing these spaces, is also associated with a distance measure -- a loss function. The edges represent transformations between two spaces (can be a learnable function represented with a neural net). Learning amounts to finding parallel passes that connect the same start and end nodes, and using their composite loss for learning. Composite loss is the sum of all pairwise losses of the parallel paths through a learning diagram. 

The proposed concept of learning diagrams is rigorously grounded in the category theory. Additionally, the paper introduces a software framework that enables the specification of learning diagrams as a Python data structure.

### Strengths
**Originality**:
The ideas presented in this work appear to be original in several ways. The paper applies category theory to create a formal framework that generalizes to different common training setups in ML. It proposes a way to automatically find parallel passes that enable the calculation of the composite loss used for training. Additionally, the paper proposes to view a training setup as a manipulable graphical object with adjustable and replaceable components (as data rather than code). I think this idea is original and leads to a nice generalization of many existing training regimes potentially opening doors for new interesting training setups.

**Quality&Clarity**: The paper appeared very well structured to me. The clarity of exposition is generally very good.

**Significance**: the significance of the work lies in providing a theoretical and software framework for designing multi-component learning systems. It facilitates compositionally in ML system design, which can lead to more maintainable and efficient model development (subparts can be easily replaced with new ones). It also facilitates collaborative model development through the integration of a plethora of independently trained models available online. The idea of representing training frameworks as a data structure (rather than code) can be impactful by increasing the transparency and interpretability of different complex training setups. It can help gain insights into relationships between different training regimes.

### Weaknesses
Learning diagrams provide a unified framework that encompasses many different setups, and this is demonstrated in this work by representing several training settings as in the language of learning diagrams. 

However, I think this paper could benefit from some concrete demonstrations of the advantages of learning diagrams over conventional methods in terms of performance, interpretability, training efficiency, revealing unknown connections between existing training setups etc..

### Questions
- can the framework presented here be used to enable a type of modularity where at each intermediate "layer" of a modular learner a routing decision has to be made (similar to MoEs/MoErging methods https://www.arxiv.org/pdf/2408.07057 )? i.e. here intermediate modules do not necessarily produce outputs that are in the label space of the underlying data

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the problem of formally describing training protocols. For this purpose, they introduce a graphical formalisation called *learning diagrams*. First, they motivate their proposal by providing a series of examples of how common training paradigms can be accurately and concisely described via learning diagrams (namely image captioning, knowledge distillation, and few-shot learning). Then, they introduce a library called DiagrammaticLearning, that provides an interface for describing and building training setups. Finally, they formalise the process of describing models and data and compiling them into loss functions using category theory. 

The library, called *DiagrammaticLearning.jl*, provides an interface to describe learning diagrams as labeled directed graph. Intuitively, vertices describe data sources and losses, and edges represent models, which in turn are functions applied to the data. The library then detects and sums over parallel paths to determine a single loss function. Finally, the library can convert the learning diagram into an implementation using a deep learning framework (e.g. PyTorch). Thus, the library is an intermediate language to describe training protocols and converting them into actual implementations.

### Strengths
- Communicating training setups used is often a significant challenge and can lead to miscommunication, especially in scenarios where multiple models interact with each other. Formally specifying training setups provides an opportunity to address this problem.
- The series of continuously more complex examples makes it easy to follow the ideas behind learning diagrams. 
- The authors evaluate their framework against the original implementations of the selected examples and demonstrate that it achieves similar performance.

### Weaknesses
 - Despite using an intuitive graphical representation, the code in listing 1 is hard to read and not particularly intuitive. 
- Section 3 contains little details about the actual implementation. 
- While the authors mention that they have removed the code for the double blind review process, I would have appreciated anonymised code in the supplementary material considering that the framework is the main contribution. This would have allowed the reviewers to interact with the framework, provide more detailed feedback regarding functionality and usability, and see whether it actually supports development in the ways described in the paper.

### Questions
- Could you elaborate on the role of DiagrammaticLearning as a compiler (Section 3.3)? How exactly does it compile the graph into e.g. PyTorch training code? 
- Is the framework compatible with common PyTorch frameworks, e.g. HuggingFace?

### Soundness
3

### Presentation
2

### Contribution
2
