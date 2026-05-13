# Circuit Transformer: A Transformer That Preserves Logical Equivalence

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Implementing Boolean functions with circuits consisting of logic gates is fundamental in digital computer design. However, the implemented circuit must be exactly equivalent, which hinders generative neural approaches on this task due to their occasionally wrong predictions. In this study, we introduce a generative neural model, the “Circuit Transformer”, which eliminates such wrong predictions and produces logic circuits strictly equivalent to given Boolean functions. The main idea is a carefully designed decoding mechanism that builds a circuit step-by-step by generating tokens, which has beneficial “cutoff properties” that block a candidate token once it invalidate equivalence. In such a way, the proposed model works similar to typical LLMs while logical equivalence is strictly preserved. A Markov decision process formulation is also proposed for optimizing certain objectives of circuits. Experimentally, we trained an 88-million-parameter Circuit Transformer to generate equivalent yet more compact forms of input circuits, outperforming existing neural approaches on both synthetic and real world benchmarks, without any violation of equivalence constraints.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Summary:
This paper introduces an approach called "Circuit Transformer" for generating logically equivalent circuits while preserving strict equivalence constraints. Existing neural approaches often make occasional errors, violating the equivalence.

### Strengths
a.	A decoding mechanism that builds circuits step-by-step using tokens with "cutoff properties" to block invalid tokens. 
b.	A "Circuit Transformer" model incorporates this mechanism as a masking layer. 
c.	Formulation of equivalence-preserving circuit optimization as a Markov decision process

### Weaknesses
1.  It is not clear why we need circuit transformer. What does this approach buy compared to existing commercial tools for performing logic synthesis from truth tables? There are methods like the Quine-McCluskey method and its many optimized variants built into commercial logic synthesis tools that can handle Boolean functions of a much larger scale than what this paper proposes. Without a comparative analysis with logic synthesis, this paper's motivation is unclear.
2.	Scalability: While the paper demonstrates effectiveness on 8-input, 2-output circuits, it's unclear how well the approach scales to much larger circuits with hundreds or thousands of inputs/outputs. In any modern digital design, there are likely to be billions of logic gates. What is the point of illustrating on an 8-input 2-output circuit?
3.	Computational: The paper does not provide a detailed analysis of the computational complexity of the proposed approach, especially for larger circuits. This information would be valuable for assessing practical applicability.

### Questions
Please address the weaknesses highlighted.

### Soundness
2

### Presentation
2

### Contribution
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
This paper presents a generative model to produce circuits while ensuring logical equivalence with the given Boolean function. The key innovation is the "Circuit Transformer", which utilizes a novel decoding mechanism based on cutoff properties that enable token generation in a way that prevents logical errors. This ensures each generated circuit is logically equivalent to its Boolean function. The Circuit Transformer was tested against existing tasks and achieved good performance in terms of both success rate and circuit size.

### Strengths
- A novel transformer-based method to generate a circuit while preserving the semantics of the original Boolean function.
- Experiments show good performance compared with other methods.

### Weaknesses
 - The motivation and intuition behind the proposed method are not immediately clear. Including a concrete illustrative example or practical application would significantly aid in understanding the approach.
- The authors provide an example illustrating how a feasible circuit can be constructed using the proposed method, but the process for selecting each token $s_i$ is not explicitly explained in the example. This leaves ambiguity about whether the selection is deterministic or nondeterministic, as I could not locate specific instructions for this process in the paper. More details would be beneficial to help understand the cutoff-property-based method.
- The set $S_i$ is central to ensure the equivalence between Boolean functions and generated circuits, as it necessitates checking that $F(\cdot)$ holds (essentially a semi-equivalence SAT check) after each token selection (line 3 in Alg.1). Given the top-down mechanism, I guess it will become increasingly non-trivial? It is also unclear how this "semi-equivalence checking" is guaranteed within the Transformer model, particularly in terms of maintaining the inference efficiency. Additionally, Table 2 does not include training and inference time, which would provide valuable insight into efficiency.
- Given that the benchmark circuits involve 8-input and 2-output nodes, it seems feasible to represent such boolean functions using a more compact form, such as Binary Decision Diagram (BDD). Existing methods for converting BDDs into circuits while preserving Boolean function semantics could serve as a viable alternative approach. Why were these methods not considered in your comparative experiments?

### Questions
Please address the weakness raised in **Weaknesses**.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a generative neural model (based on Transformers), which generates Boolean circuits equivalent to the model’s input. The primary contribution is a novel circuit representation coupled with a decoding mechanism that guarantees logical equivalence.

The sequential representation of circuits is based on a three-valued logic (true, false, unknown) and follows specific characteristics (Inheritability, Incrementality, Backtrack Elimination, Completeness). These characteristics ensure that 1) the model can build circuits incrementally while logical equivalence (under the tree-valued logic) is preserved in each step, and 2) no backtracking is necessary, which is on par with the generative properties of the Transformer. 

A standard Transformer model is trained in a supervised manner to convert randomly constructed circuits to smaller but equivalent circuits (ground truth created by an existing tool). During inference, tokens that would invalidate the circuits (i.e., invalidate equivalence under three-valued logic) are masked and, hence, cannot be predicted. Consequently, every step of the generation produces a circuit equivalent to the input circuit under the three-valued logic, and every generated circuit that does not contain wild-card nodes (“unknown”) is equivalent to the input under boolean logic. 

In addition to greedy decoding, the authors introduce a Monte-Carlo Tree Search (MCTS) to prefer circuits with fewer gates. The MCTS utilizes the next token probabilities of the Transformer and a reward function based on the number of gates in the circuit's DAG representation. 

Experimentally, the authors’ approach outperforms Transformer models on other sequential and non-sequential representations of circuits. Using MCTS during inference also produces smaller circuits than the symbolical tool Resyn2 used for training data.

### Strengths
Representing circuits sequentially with cutoff properties is novel and integrates well with sequential generative methods such as Transformers. Formally guaranteeing the correctness of a generative solution is immensely important for circuit design. The authors show that an inherently sound generative process is beneficial compared to validating solutions past generation. 

Integrating symbolic methods into the generative process not only gives formal guarantees on the result but also improves performance, which is an exciting finding and a strength of the paper.

The authors evaluate in-distribution on random circuits and out-of-distribution on circuits extracted from IWLS 2023 benchmarks, showing that their approach is robust.

### Weaknesses
## Related Work

I believe the related work (line 155ff, Schmitt et al. d’Ascoli et al.) is relevant because of the similarity in the domains and the usage of Transformers. While I agree that feasibility guarantees are important for tasks requiring correctness, it may be challenging to attribute the failure cases in related works solely to their absence, given the differences in task complexities. Both related works target very different tasks than this work. Because of the incomparability of the tasks and their complexity, it is unclear whether the failure cases are attributed to missing feasibility guarantees (as claimed by the authors) or the different tasks and complexities.

__Q1:__ Since the authors claim that the related work would benefit from feasibility guarantees, it would be interesting to see whether they think their approach also applies to the work of Schmitt et al. and d’Ascoli et al.

## Markov Decision Process and Monte Carlo Tree Search

The explanation of the generation using a Markov Decision Process (MDP) and Monte Carlo Tree Search (MCTS) should be expanded for clarity. Crucial details on how the trained Transformer model interacts with the Monte Carlo Tree Search are left in the Appendix (Algorithm 3). I recommend including MCTS in Section 3.5 and explaining how the Reward, the MCTS, and the Transformer model interact. 

Additionally, algorithm 3 in the appendix could be more precise. E.g., When creating child nodes, the authors refer to $P(s_t|s_1, …, s_{t-1})$; however, $s_1$ to $s_{t-1}$ should be indexed by the MCTS nodes (line 878). Otherwise, P would be constant. Furthermore, the authors should clarify how “visited” and “total value” are updated (line 881). $s_a$ (line 870) has the same notation as a token, although it is a rational number. 

## Experiments

It is noteworthy that an out-of-distribution real-world dataset has been evaluated. The experiments with different representations (Boolean Chain, AIGER, w/o TPE) show rigor in the evaluations. Providing details on the model’s runtime and scalability would add depth to the empirical results, particularly in comparison to Resyn2. These additions would provide a more comprehensive view of the method's practical implications, although they may not impact the current findings directly.

__Q2:__ The authors only report on average circuit sizes, but it would also be interesting to report the standard deviation. What percentage of circuits is smaller than the ground truth reference?

__Q3:__ How long does inference of the model take? If I understood correctly, the MCTS makes at least K independent calls to the model. Furthermore, how computationally expensive is the token masking in each step? Am I right that it is exponential in the number of inputs, as mentioned in Appendix 2? Generally, some time measurements of the approach would be interesting, especially in comparison with Resyn2. 

__Q4:__ The approach can handle circuits with at most eight inputs and two outputs. Can the authors argue whether this is representative of the problem area? How many inputs/outputs does the IWLS benchmark (before extracting) have? __Q5__: Would the approach scale to larger circuits? 

The following two questions did not affect my review but would be an interesting addition to the experiment section: 
 
__Q6:__ It would be interesting to know how well the Circuit Transformer performs without next-token masking. This would singularize whether performance improvement is mainly based on the representation, the symbolic next-token masking, or the MCTS. 

__Q7:__ The authors compare with other representations and apply beam search in those experiments. The authors acknowledge that this leads to a performance boost. Why is beam search not used in combination with the Circuit Transformer model?

## Presentation:

Although the paper is well-structured overall, several presentation adjustments could enhance readability, particularly in the methods section. Introducing symbols closer to their relevant subsections, providing an introductory paragraph for Section 3, and clarifying Figure 3 would help guide the reader. Such refinements would further support the clarity of the contributions. However, most of these issues are easy to fix and did not impact my assessment of the technical contribution and its soundness. 
 - Most symbols are defined in the paper's first paragraph. Personally, I would use this space to motivate the paper rather than introduce formal definitions. I recommend moving symbol definitions closer to where they are used in the methods section so the reader does not have to search for those definitions. 
 - An introduction before the first subsection of the method section would clarify the structure and guide the reader through the different subsections.
 - I’m not sure if the eight-queen-puzzle example as a vessel to explain cutoff properties is the right fit, as the reader expects circuits to be the domain of the paper. If the authors think introducing the eight-queen-puzzle is necessary, I would inform the reader before the subsection with a quick introduction that the puzzle is only an illustration to explain constrained sequence generation and that the sequential representation of circuits will follow in 3.2.
 - Figure 3 needs more explanation for easier understanding. That includes an intuitive explanation of $S_t$ and $s_t$. Furthermore, at this point, it is unclear to the reader why the unknowns are explored in this order, as it will be introduced later in 3.4. A note to this fact would help. 
 - Section 3.3 starts with “in the last section”, but this is not the last section.
 - Important information (such as the loss function) is only mentioned in the caption of Figure 5. I recommend moving this to the main text.

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
3
