# Inductive Transformers: How Large Language Models Form Concepts, And How to Make Them Even Better At It

- Decision: Reject
- Scores: 5, 1, 3, 3

## Abstract
We present a new approach to designing additional inductive bias into transformers to enable tighter conceptual organization, greater conceptual control, and higher levels of conceptual abstraction. This is a paper for those who would like to understand why transformers are structured the way they are and how new versions could be designed for ``neuro-diversity'' -- to learn differently from the same data.  This family of inductive bias requires only modest modifications to transformer activation functions. We explain the approach and give an illustrative example simulation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a way of incorporating inductive biases into the design of a vanilla transformer in a minimally invasive way: in the form of the activation functions and connections in the model. This is motivated by drawing comparisons with how humans are able to learn controllable abstract organised concepts and perform causal reasoning as a result. Successful variants of such a model might pave the way forward for models that are smaller and more capable than existing general models trained with large amounts of data and using massive computational resources.

### Strengths
- In my opinion, the key strength of the paper is the contribution of a straightforward model whose motivation is to achieve improved causal reasoning, iterative experimentation, long-range planning, and other cognitive abilities in language models, which are active research areas.
- The illustrative example is intuitive and helpful to get a sense of all the advantages of the inductive transformer elicited in the paper.
- The definitions for key ideas like identifiability, controllability are clear, increasing the readability of the paper.

### Weaknesses
 - While the paper provides an illustrative example to demonstrate the inductive transformer's potential, it lacks empirical evaluation with large-scale experiments and/or diverse datasets, which reduces its impact in my opinion. A more comprehensive evaluation would provide a clearer understanding of its capabilities and limitations. Specifically, the paper does not explore how the proposed architecture performs on standard benchmark datasets used for evaluating language models, making it difficult to compare its performance with existing models. The illustrative example, while helpful, is insufficient to demonstrate the model's generalizability and robustness.
- The introduction of additional inductive biases could potentially result in an increased model complexity and training cost. It would be helpful to discuss the trade-offs between model performance and computational resources, as well as practical scalability issues that may arise. The paper does not provide a detailed analysis of the computational overhead introduced by the proposed inductive biases, nor does it discuss how these biases might affect training time and memory requirements, especially when scaling up to larger models and datasets. A thorough analysis of these trade-offs is crucial for assessing the practical viability of the proposed approach.
- The paper focuses on concept learning, but does not discuss in detail the interpretability and explainability of the inductive transformer. Understanding how this model forms concepts and making its decision-making processes more interpretable is important in assessing its utility. While the paper mentions identifiability and controllability, it does not delve into specific techniques for visualizing or analyzing the learned representations. A more detailed discussion of how to interpret the model's internal states and decision-making processes would be beneficial.

### Questions
- If we agree with the premise that inductive transformers enable learning of abstract concepts, how would we go about generalising these concepts to a wide range of tasks and domains? Each task/domain might warrant different inductive biases being incorporated into the model architecture, resulting in a complete loss of generality from one task to another. Would that be the case?
- Could you discuss a potential merge of base models that have been trained to perform next token prediction and the minimal architectural changes to the transformer that result in the inductive transformer? Or would the proposed architecture entail completely getting rid of base models?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
I had a hard time understanding the core contribution of the paper. As far as I can tell, the architecture is a sort of "parallel grammar" where abstract productions are learned and used to generate concrete tokens, in the same way that a PCFG might generate terminal symbols along with a complete abstract structure supporting it.  The vanilla transformer is viewed as the marginalization of this model. The hope is that by incorporating / learning abstract structure along with concrete productions, the model will have a more powerful inductive bias.

### Strengths
The high-level goal of the paper, which is to create transformers with strong, hierarchical and compositional inductive biases, is a great research direction.

The idea that vanilla transformers can be interpreted as the marginalization of a structured probabilistic model is intriguing; similar work has been done by Patel et al on CNNs.

### Weaknesses
While the high-level goals are laudable, the paper suffers from several weaknesses:

- The paper does a poor job of explaining its ideas. While the introduction is reasonably accessible, I struggled to understand the probabilistic model, the production system, and the need for Bernoulli/categorical variables. I feel like this could have been framed much more clearly using terminology / frameworks that are more common in the machine learning community.  For example, this could have been framed in terms of probabilistic graphical models, or graph grammars, etc.

- The empirical results were unconvincing. The training set was too simplistic, and the simple lesion done does not confirm the hypothesis of structured / compositional knowledge.

### Questions
none

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper present a new approach to inject additional inductive bias into transformers to enable tighter conceptual organization, greater conceptual control, and higher levels of conceptual abstraction. The approach is given an illustrative example simulation.

### Strengths
The paper propose a generative statistical model such that recursive marginalization of athe model is in tight equivalence with the calculations performed by inference in a vanilla transformer. This idea can provide a foundation for the design of new inductive bias into transformers, which is inductive transformers.

### Weaknesses
It's very hard to understand the equivalence between the proposed generative model and the vanilla transformer.



### Questions
1. It's difficult to understand the equivalence between the generative model and vanilla transformer, is there more formal way to prove the equivalence?
2. Can you provide more explanations on the "concept" meaning in both the generative model and vanilla transformer.
3. What's the time complexity of the propose generative model's training/inference process?
4. Is it possible to apply the proposed generative model on large scale dataset?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work provides a re-interpretation of transformers as a probabilistic generative model of concepts and presents a new architecture, inductive transformers, that enables a stronger inductive bias towards more structured concepts. Tokens are encoded into latent variables with their own hierarchies/relations with other latent variables, and a decoder maps these latent variables back into tokens. Much machinery of the model is the same as vanilla transformers, but the operations are cleverly recast into this probabilistic framework, but there are also many additions are made to the model to accommodate this probabilistic framework. They trained their model on a toy dataset with two-token pairs and show that it can learn abstract concepts like modifiers ("big cat" or "big dog"), puts abstract concepts consistently in the same location within the model, and exhibits controlability in being able to delete concepts. This shows a potential improvement to transformers in terms of interpretability.

### Strengths
* The re-casting of transformers into a probabilistic framework is interesting and clever. 

* The toy experiments shows the model has interesting properties (controllability, etc.) that can improve transformers more. 

* They tackle a well-motivated problem in how to build structured concepts into transformer networks.

### Weaknesses
 * The paper is severely lacking clarity. Most of the details needed to understand the model are hidden in the appendix. Its not at all clear how this model works without digging through the appendix, and even then it takes a long time to figure out how the different components come together. This is especially puzzling given that the authors have so much extra space left in the main paper. The introduction, I feel, can be condensed a lot and the content in the supplement should be moved into the main paper such that readers of the main paper should understand how this architecture is implemented. 

 * The model is only implemented on a very simple toy dataset (two word sentences). It would be better to see how this model can be used on a larger dataset that is more on the level of what transformers are trained on.

### Questions
* A lot of components of the model seem highly similar to clone structured cognitive graphs (George et al. 2021). What are the similarities/differences to their work?

References:

George, D., Rikhye, R. V., Gothoskar, N., Guntupalli, J. S., Dedieu, A., & Lázaro-Gredilla, M. (2021). Clone-structured graph representations enable flexible learning and vicarious evaluation of cognitive maps. Nature communications, 12(1), 2392.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
