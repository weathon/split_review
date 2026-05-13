# Towards a Complete Logical Framework for GNN Expressiveness

- Decision: Accept
- Scores: 8, 8, 8

## Abstract
Designing expressive Graph neural networks (GNNs) is an important topic in graph machine learning fields. Traditionally, the Weisfeiler-Lehman (WL) test has been the primary measure for evaluating GNN expressiveness. However, high-order WL tests can be obscure, making it challenging to discern the specific graph patterns captured by them. Given the connection between WL tests and first-order logic, some have explored the logical expressiveness of Message Passing Neural Networks. This paper aims to establish a comprehensive and systematic relationship between GNNs and logic. We propose a framework for identifying the equivalent logical formulas for arbitrary GNN architectures, which not only explains existing models, but also provides inspiration for future research. As case studies, we analyze multiple classes of prominent GNNs within this framework, unifying different subareas of the field. Additionally, we conduct a detailed examination of homomorphism expressivity from a logical perspective and present a general method for determining the homomorphism expressivity of arbitrary GNN models, as well as addressing several open problems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a novel framework aimed at systematically assessing the logical expressiveness of GNNs. It proposes a comprehensive relationship between GNNs and logic, offering a method to construct logical formulas equivalent to arbitrary GNN architectures. The paper also discusses the implications of this framework for understanding existing models, comparing expressiveness across models, and estimating WL test bounds.

### Strengths
**Solid Theory**: The paper constructs a solid theoretical foundation through extensive mathematical proofs and derivations.

**Unified Framework**: By establishing a connection between GNNs and first-order logic, the paper proposes a theoretical framework that can unify different GNN models. This framework allows for a systematic comparison of the expressiveness of different GNN models.

**Novel Perspective**: The paper analyzes and explains the expressiveness of GNN models from the perspective of first-order logic, providing a new perspective for understanding these models.

### Weaknesses
 **Limited Comparison and Analysis**: The paper does not specifically analyze what each operation in first-order logic implies about what the model has learned, nor does it directly compare with other existing expressiveness assessment frameworks, such as the work mentioned by Zhang et al.

**Practical Guidance for Model Development**: Although the paper provides an assessment framework, it lacks specific guidance on how to use this framework to guide the development of high-expressiveness GNN models.

**Insufficient Experimental Validation (Not necessarily a con)**: The paper lacks an experimental section to validate the effectiveness, rationality, and correctness of its framework.

### Questions
1. Early work also explained the expressiveness of GNNs from a logical perspective. What new contributions have your contributions made compared to their work? Specifically, what are the differences between the second-order logic they used and the first-order logic used in your work? What are the respective advantages and disadvantages?

2. Please further elaborate and supplement what each operation in first-order logic specifically corresponds to in terms of what the model learns from the graph?

3. Zhang et al. proposed a refined framework for assessing the expressiveness of GNNs in "Beyond Weisfeiler-Lehman: A Quantitative Framework for GNN Expressiveness." Compared to the assessment method proposed in the paper, what are the respective strengths and weaknesses? Could you provide a detailed comparative analysis?

4. The paper compares several typical GNN models using a unified framework. Could you further explain how the differences in logical expressions of different GNN models correspond to the actual capabilities of the models in practice?

5. Please supplement experiments to prove the completeness, rationality, and correctness of the theoretical aspects of the paper. This would be very helpful for understanding the differences between models and selecting models suitable for specific tasks.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors introduce a framework to assess the logical expressivity of Graph Neural Network (GNN) models by analyzing their underlying combination and aggregation operations. By constructing sets of logical formulas that each GNN model can capture, this method provides insights into the types of logical properties these models can represent and distinguish. Intuitively, a GNN captures a formula $\phi$ in FO if, for any graph G, the results of $\phi$ applied on G are fully reproduced by the representations computed by the GNN.
By mapping GNN operations to logical formulas, the framework identifies the set of logical statements a GNN can inherently represent. This is a more fine-grained approach to understanding the expressivity of GNNs compared to the WL hierarchy. The paper explores GNN expressivity across different prediction tasks—graph-level, node-level, and link-level—highlighting the logical distinctions between models when applied to tasks at each of these levels.

### Strengths
- A new theoretical framework for assessing the expressive power of GNNs by relating it to fragments of FO
- Classification of existing MPNNs, subgraph GNNs
- Ability to assess the expressive power wrt to the ability to capture certain substructures (motifs) in graphs
- Affirms conjecture from prior work

### Weaknesses
 - The presentation could be improved in several places. For instance, there could be more illustrations and examples throughout the paper. 
- Nitpick: I would refrain from assigning very positive attributes, "simple," "elegant," etc., to your own results and proofs.


### Questions
- There should be a limitations section. For instance, do these results apply to graphs with node attributes as well? What other limitations has the proposed framework for assessing expressiveness of GNNs? What could be future work?

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper first proposes GACNNs, a generalisation of several GNN architectures, using sequences of combination and aggregation functions over node tuples. This allows them to subsume several existing GNNs models. They then prove the logical expressivity of GACNNs and apply those results to find the equivalent logic sets for 8 GNN variants. Finally, they show how the logical expressivity can be used to also find the homomorphism expressivity and k-WL expressivity of the model.

### Strengths
1. The contribution is significant and will be of interest to the ICLR community. It unifies existing work on logical expressivity of GNNs, as well as showing the consequences that this has for two other important methods of analysing GNN expressivity.
2. The paper makes good use of space, sticking to the recommended 9 pages and rarely making redundant statements.
3. The quality of the work appears to be good, although I haven't been able to properly verify the soundness of the proofs.
4. The authors have made it clear where their work fits into the existing literature, and what their contribution is.

### Weaknesses
Major:
1. The main section of the paper lacks intuitions as to why the theorems are true, as well as proof sketches. These would greatly benefit the reader, particularly for a central result such as Theorem 3. For example, the proof of Theorem 3 relies on constructing a logic formula that captures the behaviour of a GACNN, but it's not clear how this construction works, or why it's guaranteed to exist for all GACNNs. A high-level overview of the proof strategy would be beneficial.
2. Due to a mixture of typos and imprecision, it is sometimes unclear what the authors are intending to stay from a technical perspective. This is particularly problematic in a paper that consists solely of theory. For example: on L262, the "logic sets at the bottom" have so far only been presented to be able to be atp(u), so what else could this refer to? And on L171, what does 'u' refer to? One might reasonably assume a node, but further down it also appears to refer to node tuples. The lack of clear definitions and consistent notation makes it difficult to follow the technical arguments.
3. I have many other smaller concerns with the paper, which altogether come together into a major concern.

Medium:
1. L187 the example is far too simple and doesn't do enough to explain the idea of having a sequence of operations within each layer. It is not obvious how other real GNNs can be made from these building blocks. Using a more complex example like Local 2-GNN would be more beneficial. The example given only shows a single aggregation and combination step, which doesn't illustrate the full power of the proposed framework.
2. In Theorem 3, equivalent logic sets are being used for each x_i, but they have so far only been defined for GNNs, not these building blocks. A more general definition of equivalent logic sets is needed. It's unclear how the notion of equivalent logic sets extends to the individual combination and aggregation functions that make up a GACNN layer.
3. L327 "auxiliary logic set". One might assume that this relates to global readouts, given that these greek letters were just used above. However, that interpretation does not seem to fit with the proposition. It is not clear, and should be stated explicitly what this logic set is for, as well as using different notation to separate it from global readouts if that is not what it intends to represent. The purpose and definition of this auxiliary logic set is unclear and needs more explanation.
4. L331 the jump from the GNN models to their expressivity is not clear. It would be helpful to see an example of the whole pipeline in effect: GNN model -> GACNN -> equivalent logic -> simplification of the logic. A concrete example that demonstrates how a specific GNN model is translated into a GACNN, then into an equivalent logic formula, and finally how that logic formula is simplified would greatly enhance the paper's clarity.
5. L406 the construction is presented in a somewhat clunky manner, and would benefit from being both more precise and concise. E.g. the enumeration (a-c) is just the definition of a graph that can be done inline

Minor:
1. L35 "many studies" needs a citation
2. L38 it is unclear why k-WL lacks interpretability
3. L49 "although provides"
4. L55 MPNNs are already a generalisation of several GNNs models, so it is misleading to say they analyse different GNN models separately.
5. L76 "is denoted"
6. L97 "leave"
7. L105 "predicate", "corresponds"
8. In section 3.1, GNNs are referred to without having been defined yet.
9. L140 "district"
10. L152 "the elements" -> "each element"
11. L166 no need for "etc", since you already said "including"
12. L172 should be clearer that it's a sequence of two operations, not just two operations
13. L182 "variants", but only one is described
14. L187 the appendix should be referenced here for the construction of the other GNN models within this framework
15. L254 "existed"
16. L255 "edges" -> "neighbourhoods", since we're generalising to node tuples
17. L270 "function", "Similar as previous"
18. L281 "is" = "are"
19. L298 "its layers" -> "a layer", since all layers have been assumed to have the same structure
20. L309 "provides"
21. L323 "prediction"
22. L365 "although computes"
23. L376 "tasks"
24. L392 should this not be "homomorphism expressivity"? Homogenous has other connotations. Also "beautiful" is emotive language and should be avoided
25. L404 full stop should not be there
26. L464 - 466 is a bit verbose, and restating the obvious

### Questions
1. L134 the GNN outputs "true" for a node. Does this mean that GNNs are restricted to those that do binary classification on nodes? If so, this is not stated explicitly anywhere.
2. L140 why are logic sets "quantitative" but k-WL or homomorphism tests are not?
3. L171 - what does "u" refer to? This needs to be more explicit.
4. L179 I find it strange that the computation counts down (from K + 1) within a GACNN layer, but at the layer level it counts up from 0. Is there a good reason for this?
5. L180 "generalised neighbour" has not been defined. What does this precisely refer to?
6. L196 why not use an example of an existing GNN model here?
7. L262 "logic sets at the bottom" have so far only been presented to be able to be atp(u), so what else could this refer to?
8. L351 "more general v". In what sense is it more general? And why is it obviously more powerful?
9. L450 how useful is the construction, given its recursive nature?
10. L472 why is the WL bound on SEAL so weak, given proposition 9? Shouldn’t we be able to exactly specify it’s WL expressivity?
11. Is the paper claiming to have generalised all GNNs? L482 seems to suggest so.

### Soundness
3

### Presentation
3

### Contribution
4
