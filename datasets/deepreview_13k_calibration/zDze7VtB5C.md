# A Little Depth Goes a Long Way: the Expressive Power of Log-Depth Transformers

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 3, 5, 6

## Abstract
Most analysis of transformer expressivity treats the depth (number of layers) of a model as a fixed constant, and analyzes the kinds of problems such models can solve across inputs of unbounded length. In practice, however, the context length of a trained transformer model is bounded. Thus, a more pragmatic question is: *What kinds of computation can a transformer perform on inputs of bounded length?* We formalize this by studying highly uniform transformers where the depth can grow minimally with context length. In this regime, we show that transformers with depth $O(\log C)$ can, in fact, compute solutions to two important problems for inputs bounded by some max context length $C$, namely *simulating finite automata*, which relates to the ability to track state, and *graph connectivity*, which underlies multi-step reasoning. Notably, both of these problems have previously been proven to be asymptotically beyond the reach of fixed depth transformers under standard complexity conjectures, yet empirically transformer models can successfully track state and perform multi-hop reasoning on short contexts. Our novel analysis thus explains how transformer models may rely on depth to feasibly solve problems up to bounded context that they cannot solve over long contexts. It makes actionable suggestions for practitioners as to how to minimally scale the depth of a transformer to support reasoning over long contexts, and also argues for dynamically unrolling depth as a more effective way of adding compute compared to increasing model dimension or adding a short chain of thought.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper explores the computational expressivity of transformers when their depth scales logarithmically with input context length. Prior analyses typically assume a fixed transformer depth, which limits the model’s ability to solve certain tasks as context length increases. This work, however, argues that transformers can still solve certain problems up to a bounded input length, even if they cannot handle them for arbitrarily large inputs. By scaling depth logarithmically with the input length, transformers can effectively simulate finite automata and solve graph connectivity problems, which are critical for tasks involving multi-step reasoning and state tracking. These findings suggest that only a modest, logarithmic increase in depth is required to address such tasks, offering a path for efficient model scaling and highlighting the benefits of dynamic depth adjustments over simply expanding model width or employing chain-of-thought reasoning.

### Strengths
1. **Innovative Depth Scaling Insight**: This paper shifts the focus from fixed-depth transformers to a dynamic, log-depth scaling, addressing some limitations of traditional models in handling extended contexts. This perspective broadens our understanding of transformers’ potential expressivity.

2. **Rigorous Theoretical Foundation**: The paper provides clear mathematical proofs and complexity analyses that validate the advantages of log-depth scaling for specific tasks, particularly regular language recognition and graph connectivity. This rigor strengthens the work’s contributions to understanding transformers’ computational capacity.

3. **Comprehensive Comparison with Other Scaling Approaches**: The authors examine depth scaling in comparison to width scaling and chain-of-thought methods, demonstrating that logarithmic depth growth is more computationally efficient and effective for reasoning tasks, especially for state tracking and pathfinding in bounded contexts.

### Weaknesses
1. **Limited Consideration of Complementary Methods**: The paper promotes depth scaling over width or chain-of-thought expansion but could benefit from a more nuanced discussion of scenarios where those methods may still offer advantages or may complement log-depth scaling. For example, while log-depth scaling may be efficient for state tracking, it's unclear how it compares to width scaling for tasks requiring large parallel searches or knowledge-intensive operations. The paper should also address the practical trade-offs, such as the potential increase in training time associated with deeper networks compared to wider ones, which could be a significant factor in real-world applications.

2.  **Lack of Experimental Validation**: Although the theoretical findings are compelling, the paper would be stronger with empirical experiments demonstrating the practical performance of log-depth transformers on real-world tasks and quantitatively comparing their efficiency and effectiveness with other models. The theoretical claims about the relationship between depth and effective context length for state tracking, for instance, should be verified through controlled experiments. Without such validation, the practical applicability of the proposed scaling method remains uncertain.

### Questions
1. Are there specific conditions or types of tasks where width expansion or chain-of-thought reasoning may still be advantageous compared to log-depth scaling?

2. Do you have plans to empirically validate these theoretical results on real-world datasets? If so, what metrics or benchmarks would you prioritize to assess the practical benefits of log-depth scaling?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The work shows that two reasoning problems where standard transformer struggled to solve can be solved by a looped transformer. The work also shows that modular arithmetic with small modulus can be solved with the same architecture. Authors finally showed that scaling depth is more efficient than width or adding CoT intermediate steps.

### Strengths
S1. Authors showed that looped transformer (non-constant depth architecture) can solve problems more efficiently than CoT or adding width. This is quite interesting for theoretical transformer foundation, although the impact is pretty limited for current constant-depth architecture, given it's not clear and easy to scale large training for looped transformer. 

S2. The findings could inform more efficient model scaling strategies, maybe combining the effect of CoT with log n depth.

S3. The paper is well written and all relevant lemmas are well explained.

### Weaknesses
W1. Major weakness is that the theoretical results lack experimental validation on the tasks author suggested, limiting real world applicability. Also, dismissing CoT with a couple of lines seems unfair, given the potential showed by CoT on arithmetic and graph related problems, above all.

W2. Given the memory management issue, implementing dynamical depth is not clear and also it's not clear if a looped transformer can be indeed __trained__ to solve the two mentioned problems. 

W3. The paper is very intricate and a bit more explanation may be needed to understand this work. Also the work is not really self contained. 

W4. Although theorem 3 and 4 are the core part of the authors work, they are not well justified.

### Questions
Q1. Given the two differences from the standard transformer architecture and the fact that Lemma 1 holds because of the masked pre-norm, do you think that the results hold for standard transformer architecture? 

Q2. Would it be possible to add a more informal introduction to let other people read and fully understand the work without looking at prior work? 

Q3. Did you also see a similar law for other architectures (like https://arxiv.org/abs/2405.06394 or other constant transformer-like model)?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper addresses the expressive capacities of transformers where 
the depth grows logarithmically with the length of the inputs. Specifically, the paper seeks to 
contribute to three questions:
- Can fixed-depth transformers handle "hard" problems when restricted to bounded input lengths?
- Does logarithmic depth scaling offer greater expressive abilities compared to a fixed depth?
- What practical advantages do log-depth transformers or input-dependent depth offer?

Informally, the paper's primary theoretical contributions regarding the "universal transformer" model, 
which is characterised by a basic encoder architecture with certain layers repeated a number of times 
dependent on the input length, are as follows:
- (Theorem 1) For each regular language $L$, there exists a universal transformer, with logarithmic repetition, 
that recognises $L$.
- (Theorem 2) There exists a universal transformer, with logarithmic repetition, that decides whether, 
given a graph $G$ and vertices $s$ and $t$, there is a path from $s$ to $t$.
- (Theorems 3 & 4) Placing different classes of transformers (fixed depth or CoT) in $\text{TC}^0$.

### Strengths
- The three areas that the paper aims to contribute to are both relevant and intriguing. Particularly, 
the assumption of bounded input lengths, which is closer to practical settings, deserves thorough investigation.
- Setting aside the notational and definitional ambiguities discussed below, the paper supports all 
theoretical claims with proofs, which appear to be sufficient.
- The related work, specifically regarding the expressive capabilities of different transformer models, 
is well chosen. I concur that this paper contributes significantly to these domains.

### Weaknesses
To begin, I will summarize the main issue I encounter with this paper. 
As mentioned earlier, the contributions the paper aims to provide are intriguing, and I also think they are partially achieved. 
However, the current form of the paper makes it challenging to grasp the significance of these contributions and how they compare to existing results. This difficulty arises primarily from a lack of clear definitions, confusing informal statements, and a disconnect between the theoretical contributions and their proposed implications. 

I will go into detail below, loosely ordering the weaknesses from most to least significant:
- I am not convinced that the paper sufficiently addresses the first and third contributions it aims to make. The main results focus on transformers with dynamic depth, leaving me unclear about the implications for fixed-depth models. Lines 76 to 83 seem to mention this in the context of an experiment, but it is only briefly referenced and lacks further development throughout the paper. Additionally, the explanation of the third contribution in Lines 86 to 9, which states, "scaling depth logarithmically as a computational resource more efficiently expands the expressive power of transformers compared to scaling width...", appears to be an overinterpretation based solely on the results of Theorems 1 & 2 versus Theorem 3. If this claim is to be maintained, the paper needs to provide more detailed justification for such a bold statement, which is currently absent.
- The definition of the (s, r, t)-universal transformer model lacks clarity and detail. While I understand the authors' intent to be succinct, even those familiar with related research might struggle to comprehend the model's specifics. A thorough understanding is crucial for comparing the expressiveness of different transformer models. Here are some points related to the definition in Section 2:
    - There seems to be a confusion in terminology regarding the "semantics" of universal transformers, which are described as sequence-to-value functions. However, on line 103, they are referred to as a decoder, which is typically associated with sequence-to-sequence transformations.
    - The definition of masking within this model is unclear. The phrase "... add a learned mask vector that can select specific dimensions of the residual stream ..." is ambiguous and needs clarification. This issue is particularly important because, for example, in Lemma 1, the term "...causally masked attention..." is mentioned, but its meaning is not well defined.
    - The notation $L^l$ is ambiguous. Does it signify layer $l$ or the function it performs? Additionally, the notation $r$-layer $(l-s) \mod r$ is not defined
    - The definition of averaging-hard attention using a limits construction and an exponential function diverges from the common use of hardmax in related works cited within the paper. Are there differences that justify this choice?
    - Section 2.2 appears disjointed and complicates the definition. The first sentence raises multiple questions, particularly on the necessity of "memory management."
- The presentation of Theorem 2 is somewhat misleading. The problem addressed is not the "connectivity problem" in the traditional sense, which involves deciding whether all nodes are interconnected by some path. Instead, it is the "reachability problem," which focuses on deciding if there is a path connecting specific nodes.
- The role of Theorem 4 is not clearly articulated. The theorem is referenced with 
(Anonymous, p.c.), which is somewhat unconventional. Is this result established within this paper? 
It seems there is a proof provided in the appendix, so the rationale for this citation is unclear. 
If the theorem is not original to this work, clarification is necessary regarding its inclusion.
- The abstract begins with the statement: "Most analysis of transformer expressivity treats the depth (number of layers) of a model 
as a fixed constant, ...". I find this statement problematic. It seems that the authors are referring to research focusing on formal language theory, which aims to understand which classes of languages specific classes of transformers can recognize. 
While individual transformer models have a fixed depth, this is right, the class of models does not need to be constrained in this way. This is an example of an informal assertion that leads to confusion. 
- Lines 44 to 46 include the statement, "This is analogous to how regular expressions cannot express all context-free languages, but one can write regular expressions that capture fragments of a context-free language." The paper uses this analogy to imply that transformers generally perform effectively on shorter input lengths. This statement is somewhat perplexing because the point about regular expressions is quite basic; if there is additional nuance or significance, such statements require further clarification.



### Questions
I would appreciate it if you could address the weaknesses I highlighted earlier. Specifically, I am interested in the following:

- Could you provide additional clarification on your contributions regarding the first question, particularly on how you contribute to understanding the limits of the expressiveness of fixed-depth transformers with bounded inputs?
- Could you offer a more detailed and rigorous explanation of the concepts discussed in Section 2.2?
- Am I correct in identifying a potential confusion between decoder-only and encoder-only models, or is there a detail I might have overlooked?
- What is the precise method of masking you employ within your model?

I'm keen to resolve these issues as I believe your work holds significant value. However, the points mentioned above currently obscure its impact.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates log-depth Transformers, demonstrating that their capabilities exceed those of constant-depth Transformers ($\mathsf{TC}^0$) and constant-depth Transformers with $O(\log n)$ chain-of-thought steps. Through theoretical constructions, the authors show that a log-depth Transformer can effectively solve the regular language recognition problem and the graph connectivity problem, both of which fall outside the expressive power of constant-depth Transformers with polynomial size.

### Strengths
The authors utilize saturated attention rather than hard attention, aligning more closely with practical applications. Additionally, they consider the effects of layer normalization.

### Weaknesses
1. The motivation for log-depth Transformers lacks sufficient conviction. Given the bounded context assumption in line 50, it would be more appropriate to treat all elements as constant. If bounded context and model sizes are to be discussed carefully, as indicated in lines 76-78 regarding the maximum problem size of graph connectivity with fixed depth $d$, the coefficient is crucial, while the result of $2^{O(d)}$ remains unclear.

2. The results presented lack clarity. In the main theorems (Theorems 1 and 2), only the model depth of $O(\log n)$ is specified, omitting other critical configurations such as the required model width and the number of attention heads.

3. Additional clarification is needed regarding the results in relation to prior work. Specifically, Lemma 3 of [1] demonstrates that a Transformer with depth $2d$ maps $\langle C,x\rangle$ to the circuit value $C(x)$, where $C$ is a threshold circuit with depth $d$. Since regular language recognition and the graph connectivity problem both belong to $\mathsf{TC}^1$, this lemma could already suggest comparable results in this paper.

4. The absence of experimental results to validate the theoretical findings is a significant gap. Empirical verification of the solid lines in Figure 1 is also essential.

### Questions
1. What are the other configurations (e.g., model width, maximum number of attention heads, etc.) for the Transformers in the main theorems, specifically Theorems 1 and 2? 

2. Can you provide more clarification of your results in relation to prior work, such as [1]? (Refer to weakness 3)

3. Can you conduct experiments on the two tasks considered in the paper, varying the model depth, model width, and the number of attention heads to empirically evaluate how these factors affect performance?

[1] William Merrill and Ashish Sabharwal. The parallelism tradeoff: Limitations of log-precision transformers. https://arxiv.org/abs/2207.00729.

### Soundness
2

### Presentation
2

### Contribution
2
