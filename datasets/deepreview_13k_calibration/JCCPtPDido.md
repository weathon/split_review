# Jet Expansions of Residual Computation

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
We introduce a framework for expanding residual computational graphs using \textit{jets}, operators that generalize truncated Taylor series.
Our method provides a systematic approach to disentangle contributions of different computational paths to model predictions.
In contrast to existing techniques such as distillation, probing, or early decoding, our expansions rely solely on the model itself and requires no data, training, or sampling from the model.
We demonstrate how our framework grounds and subsumes \textit{logit lens},
reveals a (super-)exponential path structure in the recursive residual depth and opens up several applications. 
These include sketching a transformer large language model with $n$-gram statistics extracted from its computations, and indexing the models' levels of toxicity knowledge.
Our approach enables \textit{data-free} analysis of residual computation for model interpretability, development, and evaluation. The project website can be found \href{https://yihong-chen.io/jet_expand/}{here}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a method for expanding residual networks, such as Transformers, using jets—operators that generalize truncated Taylor series. This approach aims to disentangle the contributions of individual computational paths to model predictions. The authors claim that their method subsumes the Logit Lens and demonstrate its ability to extract n-gram statistics from intermediate model layers, also enabling a data-free approach to detoxification.

### Strengths
Well-written and theoretically well-developed, with content that is thorough yet not overwhelming.

### Weaknesses
I find the theoretical foundation to be solid, but my main concerns lie with the experimental approach.

The experiments may be overly empirical and lack statistical rigor. For instance, in Section 5.1, only a handful of jet paths corresponding to specific linguistic functions are selected to demonstrate intervention effects. A more systematic approach is needed to demonstrate that the jet lens is more effective than the logit lens.

While the paper primarily offers an analytical framework, it lacks actionable insights for model steering. For example, could it be demonstrated that the bi-gram statistics can be leveraged to guide more efficient pre-training or improve RLHF techniques for reducing toxicity?

### Questions
I have mostly raised them in the weakness section.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors develop a method that expands a residual network into the sum of an exponential number of jets (roughly, taylor expansions of different components). Each term is a "path" information takes as it traverses the network. They apply this to interperability,

### Strengths
The method itself is very interesting; thinking of a network as a sum-of-paths is very natural and the jet formalism seems to capture it in a nice way.

The authors show that this generalizes  prior work such as the logit lens.

Since the top network architectures are residual, this is applicable to the most common model types.

Interpereting parts of the network is an important and relevant topic.

### Weaknesses
 - The primary issue is confusing exposition and incomplete details. These make the contributions difficult to asses. I enumerated specifics in the "questions" section.
- The exponential expansion factor means that to analyze a model like LLaMa 405b, one would have 2^118 terms which seems a bit unwieldy
- Presumably, you need ways of computing k-th order jets for network components (the authors don't seem to discuss this), which makes implementation difficult.

- Paragraph after eq (9): what is gamma_3? it is not defined or used in the figure. This seems important. Is it a hypothetical 3rd block? 
- Lemma 1: Unclear where w comes from. I have 3 hypotheses: (1) w is arbitrary and changes which member of the equivalence class you have (2) there is a specific value of w needed ("there exists a w...") (3) there's a typo and the LHS should be a weighted sum of x. This needs to be explicit.
- What is the point of tthe if l < L in Algorithm 1? Isn't this always true? In the else, how can there be a gamma_{L+1} if there are L layers? where does w come from? 

line 264: "For example, bi-grams statistics related to Pq (z2|z1, . . . ) can be computed
by evaluating bi-gram paths, which we can obtain by expanding the LLM with Algorithm 2 and
filtering out all paths that involve self-attention modules."

If you filter out all self-attention paths, aren't the bigrams z1, z2 independent? this needs to be true because self-attention is the only mechanism for a transformer to route information amongst tokens.

How are you optimizing the jet weights? This seems to be very important as you show the weights in Figure 2, but you only briefly mention that it is "done cheaply" without any details. Do you need specific datasets? do you use SGD? How do you actually compute the residual in a way that can be optimized?

How do you represent (computationally) and evaluate the jets? The paper presents them abstractly, which is fine, but in order to compute anything you need to be able to evaluate the k-th order jet for an MLP or self-attention layer.


Minor comments:

In eq (7), I found the notation `J^k f(x) = f(x) + ...` to be a bit confusing; suggest `(J^k f) x = y \mapsto ...`

### Questions
- Paragraph after eq (9): what is gamma_3? it is not defined or used in the figure. This seems important. Is it a hypothetical 3rd block? 
- Lemma 1: Unclear where w comes from. I have 3 hypotheses: (1) w is arbitrary and changes which member of the equivalence class you have (2) there is a specific value of w needed ("there exists a w...") (3) there's a typo and the LHS should be a weighted sum of x. This needs to be explicit.
- What is the point of tthe if l < L in Algorithm 1? Isn't this always true? In the else, how can there be a gamma_{L+1} if there are L layers? where does w come from? 

line 264: "For example, bi-grams statistics related to Pq (z2|z1, . . . ) can be computed
by evaluating bi-gram paths, which we can obtain by expanding the LLM with Algorithm 2 and
filtering out all paths that involve self-attention modules."

If you filter out all self-attention paths, aren't the bigrams z1, z2 independent? this needs to be true because self-attention is the only mechanism for a transformer to route information amongst tokens.

How are you optimizing the jet weights? This seems to be very important as you show the weights in Figure 2, but you only briefly mention that it is "done cheaply" without any details. Do you need specific datasets? do you use SGD? How do you actually compute the residual in a way that can be optimized?

How do you represent (computationally) and evaluate the jets? The paper presents them abstractly, which is fine, but in order to compute anything you need to be able to evaluate the k-th order jet for an MLP or self-attention layer.


Minor comments:

In eq (7), I found the notation `J^k f(x) = f(x) + ...` to be a bit confusing; suggest `(J^k f) x = y \mapsto ...`

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors rewrite a model with skip connections as a composition of many Taylor series, evaluated at various points that are related to intermediate activations, promising data-independent global interpretability. The approach is demonstrated on LLMs and conceptually compared to related methods such as LogitLens.

### Strengths
- The mathematical exposition is clear.
- The authors acknowledge the limitation of their method in capturing the nonlinear model exactly.
- The applicability of the proposed method for evaluating models globally is interesting and promising. In particular, the model diffing experiments provide the potential of useful metrics for assessing the effectiveness of a specific fine-tuning method, the rate of model improvement and saturation, and the potential for certain emergent properties from n-gram statistics.

### Weaknesses
 - The first four sections contain clear mathematical expressions. The remaining sections do not use any of these notations which makes it very hard to digest what the figures are measuring in the context of the proposed method. I’d encourage the authors to improve the clarity of the figures and the captions. At the moment, they are very unclear.
- One way to address the first weakness would be to add a new section, between the theoretical section and the empirical section, which explains in the greatest detail possible what exactly is going to be measured empirically. This section should explicitly link the mathematical formalism to the experimental setup, defining all relevant quantities and how they are computed.
- The authors claim that their method provides global interpretability but it is unclear how their method is able to provide insights without evaluating the Jacobians at specific points. The method seems to rely on local expansions, so it's not clear how these local views can be combined to form a global picture of the model's behavior. Specifically, the paper does not explain how the method avoids the need to evaluate Jacobians at specific input points to achieve global interpretability.
- Is the proof of Lemma 1 a novel contribution or is it a well-known result? It is not clear whether this result is a novel finding or a standard mathematical technique.
- The proof of Lemma 1 (in the Appendix) is not clear. The steps in the proof are not sufficiently detailed, making it difficult to follow the logic and verify the correctness of the result.
- Before Equation 9, you state “x_{empty set} = eta”. The notation $x_set$ wasn’t previously defined and is therefore unclear. The introduction of this notation without prior definition makes it difficult to understand the subsequent equations and the overall flow of the argument.
- Could the authors expand on the algorithm bubble? At the moment, the steps are not very clear. The descriptions of the algorithms are too high-level, lacking the necessary detail for a reader to understand the implementation.
- It is unclear from the paper how the jet expansion relates to n-grams. The connection between the mathematical framework and the concept of n-grams is not clearly established, making it difficult to understand the practical implications of the method.
- The relation between LogitLens and the proposed method should be made more explicit. While LogitLens is mentioned, the precise relationship and differences between it and the proposed method are not clearly defined.
- Superposition is mentioned multiple times throughout the paper. The relation with the jet expansion is not clear. The paper discusses superposition but does not explain how the jet expansion method can be used to analyze or understand it.
- "filtering out all paths that involve self-attention modules" — why is this necessary or reasonable? The rationale behind excluding self-attention modules from the analysis is not provided, raising questions about the completeness of the method.
- Figure 2
    - How is the top table related to the bottom figures? The connection between the top table and the bottom figures is not explained, making it difficult to interpret the results.
    - Is it necessary to put all this information in a single figure? The figure is too dense, making it hard to understand the individual components and their relationships.
    - Why should we measure the “cosine similarities between original and jet logits of joint (left) and iterative (right) lenses”? What do we learn from measuring it? The motivation for using cosine similarity as a metric and its interpretation are not clearly explained.
    - How do we see evidence for superposition or neuron polysemy in this figure? The figure does not provide clear evidence or explanation of how superposition or neuron polysemy are being analyzed.
    - Is a simpler method like LogitLens capable of identifying similar patterns?  Is there some simpler baseline you could compare your method to? The paper does not compare the method to simpler baselines to demonstrate its advantages.
- Tables 1 and 2
    - "∆ logit after intervention" — what is the exact definition? unclear what this means. The definition of this metric is not provided, making it difficult to understand the results.
    - What's the order of the expansion? The order of the Taylor expansion used in the experiments is not specified.
    - Is a simpler method like LogitLens capable of identifying similar patterns? Is there some simpler baseline you could compare your method to? The paper does not compare the method to simpler baselines to demonstrate its advantages.
- "One-to-one bi-grams like" and “Many-to-many bi-grams” — unclear what does this mean. The definitions of these terms are not provided, making it difficult to understand the analysis.
- Figure 4
    - What’s the definition of a "hit ratio"? The definition of the hit ratio metric is not provided, making it difficult to interpret the results.
    - What’s the definition of "total mass"? The definition of total mass is not provided, making it difficult to understand the results.
    - How do I see double descent or grokking in this figure? The connection between the figure and the concepts of double descent or grokking is not clearly explained.
- What’s the definition of “diffing jet bi-grams”? The definition of this term is not provided, making it difficult to understand the analysis.
- "small change in mass" — what’s the definition of “mass”? The definition of mass is not provided, making it difficult to understand the analysis.

### Questions
- "filtering out all paths that involve self-attention modules" — why is this necessary or reasonable?
- Figure 2
    - How is the top table related to the bottom figures?
    - Is it necessary to put all this information in a single figure?
    - Why should we measure the “cosine similarities between original and jet logits of joint (left) and iterative (right) lenses”? What do we learn from measuring it?
    - How do we see evidence for superposition or neuron polysemy in this figure?
    - Is a simpler method like LogitLens capable of identifying similar patterns?  Is there some simpler baseline you could compare your method to?
- Tables 1 and 2
    - "∆ logit after intervention" — what is the exact definition? unclear what this means.
    - What's the order of the expansion?
    - Is a simpler method like LogitLens capable of identifying similar patterns? Is there some simpler baseline you could compare your method to?
- "One-to-one bi-grams like" and “Many-to-many bi-grams” — unclear what does this mean.
- Figure 4
    - What’s the definition of a "hit ratio"?
    - What’s the definition of "total mass"?
    - How do I see double descent or grokking in this figure?
- What’s the definition of “diffing jet bi-grams”?
- "small change in mass" — what’s the definition of “mass”?

### Soundness
4

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
2

### Summary
This paper utilizes a convex combination of Taylor expansions to rewrite residual networks up to a nonlinear residual term. Crucially, these expansions are such that the contributions from different combinations of network subunits can be studied separately. This results in a data-independent interpretation tool for understanding black-box residual networks. The authors use this developed tool to study the functionality of subunits, pretraining dynamics, and finetuning in the context of language models.

### Strengths
The proposed approach is principled, intuitive and unifies certain prior works. As shown by experiments, it can identify the linguistic functionality of various computational subunits in language models.

### Weaknesses
Overall, the approximation quality of the jet expansions is not guaranteed, and hence faithfulness to the actual network and its behavior is unclear. This is acknowledged by the authors, and the approximation quality does not necessarily improve with scaling k (as seen from the experiments). Therefore, experimental explorations with jet expansions are only indicative without any confidence. The lack of guaranteed approximation quality is a significant limitation, especially when the method is used to interpret complex models. The method's reliance on Taylor expansions, which are local approximations, means that the insights gained might not generalize well to the entire input space. The experiments show that increasing k does not consistently improve the approximation, suggesting that higher-order terms may not always capture the network's behavior more accurately, and may even diverge from the true function. This raises concerns about the reliability of the interpretations derived from these expansions, as they might be misleading if the approximation error is high. Furthermore, the method's effectiveness is highly dependent on the choice of expansion centers, and the paper does not provide a clear strategy for selecting these centers, which could lead to inconsistent results.

### Questions
In Figure 2, the truthfulness of jet logits decay when $k=2$. Could you comment about scaling with respect to $k$? Do you expect it to improve the quality of the expansions?

Can you explain how to obtain bi-gram and skip-n-gram expansions? Overall, I think these two paragraphs (L259 "Jet bi-grams and skip-n-grams statistics") could be a bit more detailed for comprehension of the reader.

### Soundness
3

### Presentation
3

### Contribution
3
