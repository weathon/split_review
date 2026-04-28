# Linear Relational Decoding of Morphological Relations in Language Models

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
The recent success of transformer language models owes much to their conversational fluency and productivity in linguistic and morphological aspects. An affine Taylor approximation has been found to be a good approximation for transformer computations over certain factual and encyclopedic relations. We show that the truly linear approximation $W\textbf{s}$, where $\textbf{s}$ is a middle layer representation of the base form and $W$ is a local model derivative, is necessary and sufficient to approximate morphological derivations. This approach achieves above 80\% faithfulness across most morphological tasks in the Bigger Analogy Test Set, and is successful across language models and typological categories. We propose that morphological relationships in transformer models are likely to be linearly encoded, with implications for how entities are represented in latent space.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work (building off Hernandez et al) shows that linear approximations are sufficient to encode morphological relations from an object to subject state. The authors find strong evidence that the Jacobian works for morphological relations, but performs worse than the LRE for other kinds of relations. 

They further characterize the roles of Jacobian and bias (in relation to LRE), and help define structures behind output generation in LLMs better.  The paper performs these experiments on a novel adaptation of the Bigger Analogy Test Set, wherein forty distinct relations are represented.

### Strengths
* The experiments are very thorough and well done. The authors spend a lot of effort trying to understand latent justifications to the results they obtain. The mathematical justifications of the research are well motivated, with a good set of references to back the claims.
* This is an important area of research in latent understanding of LLMs.

### Weaknesses
* There seem to be multiple contributions of the paper, some being less important than others. This makes it hard to clearly understand 1-2 important takeaways from the work. As examples, these takeaways can be Jacobian approximations, and role of bias and Jacobian in LRE. The rest should be condensed into a single para and maybe kept as smaller side-contributions.
* The methodology of adaptation of Bigger Analogy Test Set should be clearly explained. I am assuming this is an important aspect of the work?
* Is there any reason the authors didn’t try experiments with larger models (greater than 10B params)? Learnings might be significantly different.
* The presentation and in general, representations of facts isn’t done in an ideal manner. 
    * Fig 3 and 4 are not interpretable. Please enlarge the image, or in general, feel free to just present the most relevant facts.
    * A lot of the abbreviations like LRE and BATS are not defined. It’s clear what they represent if you read the paper properly, but a definition is warranted.

### Questions
See weaknesses,

### Soundness
3

### Presentation
2

### Contribution
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
The paper explores how transformer-based language models approximate morphological transformations using linear transformations. The study finds that for morphological relations, a simple Jacobian (linear) transformation effectively captures the relationship between base and derived word forms (e.g., noun to plural, verb to noun). This linear approximation achieves high accuracy on morphological tasks from the Bigger Analogy Test Set and shows consistency across different language models, suggesting that morphology is encoded in transformers as a linear transformation.

### Strengths
- Demonstrates that morphological relations in language models are highly linearly approximable, providing insights into model structure and interpretability.
- Validates findings across different language models, indicating robustness of the method.
- Uses the Bigger Analogy Test Set, covering a wide range of morphological and linguistic relations for validation across a range of morphological paradigms.

### Weaknesses
- The method's reliance on linear transformations is highly likely to be limited to English, a fusional-analytic language. Most language are highly non-linear in morphological transformations and thus paper has to state its linguistic limitations and scope before claiming a general theory of any kind.

### Questions
-

### Soundness
2

### Presentation
3

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
The paper uses that morphological relations exist in a linear subspace after looking at a Taylor-expansion of the neural network. (I am not entirely sure which Taylor expansion; see below). The claim to novelty of the paper is that linear relationships have been tested for other types of linguistic relations, but for morphological. So, as an example, if I have the complex word "uncomputable" I want to break it down into "un"-"compute"-"able" and show that each piece, when encoded as a real vector, is something I can sum to get the entire word. The experimental results focus on translation of morphologically complex words.

### Strengths
The strength of the paper stems from its focus on a less well-reached topic. I appreciated an interpretability paper that focuses on morphology. I think if the method were explained better, it would be a very interesting paper.

### Weaknesses
The primary weakness of the paper is its poor technical exposition. I've phrased most of this as questions below. Another weakness is the poor rendering of the plots. It's very hard to read the plots in Figure 5. Also, many of the equations are not labeled making them hard to reference in the review. The background section, 2.1. is also hard to read.

### Questions
Most of the questions are about section 2.
* What is F? To talk about Jacobians, I imagine it has to be a vector-to-vector map.
* At what point is the Jacobian computed? W is defined as a function, but treated as a matrix?
* What do the authors deal with tokenization?
* What are the examples talked about in section 2.4?
* Is unbolded o the same as bolded o? It sort of looks like it

### Soundness
3

### Presentation
2

### Contribution
3
