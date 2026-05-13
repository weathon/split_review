# Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition

- Decision: Accept
- Scores: 5, 6, 8

## Abstract
Automated mechanistic interpretation research has attracted great interest due to its potential to scale explanations of neural network internals to large models. Existing automated circuit discovery work relies on activation patching or its approximations to identify subgraphs in models for specific tasks~(circuits). They often suffer from slow runtime, approximation errors, and specific requirements of metrics, such as non-zero gradients.
In this work, we introduce contextual decomposition for transformers~(CD-T) to build interpretable circuits in large language models. CD-T can produce circuits of arbitrary level of abstraction, and is the \emph{first} able to produce circuits as fine-grained as attention heads at specific sequence positions \emph{efficiently}.
CD-T is compatible to all transformer types, and requires no training or manually-crafted examples.
CD-T consists of a set of mathematical equations to isolate contribution of model features. Through recursively computing contribution of all nodes in a computational graph of a model using CD-T followed by pruning, we are able to reduce circuit discovery runtime from hours to seconds compared to state-of-the-art baselines.
On three standard circuit evaluation datasets~(indirect object identification, greater-than comparisons, and docstring completion),
we demonstrate that CD-T outperforms ACDC and EAP by better recovering the manual circuits with an average of 97\% ROC AUC under low runtimes.
In addition, we provide evidence that faithfulness of CD-T circuits is not due to random chance by showing our circuits are 80\% more faithful than random circuits of up to 60\% of the original model size. 
Finally, we show CD-T circuits are able to perfectly replicate original models' behavior~(faithfulness $ = 1$) using fewer nodes than the baselines for all tasks.
Our results underscore the great promise of CD-T for efficient automated mechanistic interpretability, paving the way for new insights into the workings of large language models.~\footnote{CD-T will be released as an open-source python package to benefit the wide mechanistic interpretability research community.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel method CD-T that leverages contextual decomposition for mechanistic interpretability in transformers. CD-T's granularity is fine-grained up to attention heads (does not include MLP layers). They report the results of their method (classification metrics and faithfulness of the circuit as compared to randomly sampled circuits) for three tasks, namely indirect object identification, greater-than comparisons, and docstring completion.

### Strengths
1. Motivation, relevant scientific terms and prior works are well-written, making the paper accessible to researchers who are non-experts in this area. 

2. The proposed method can be easily used for all transformer architectures (encoder-decoder and decoder-only, as per line 72). Further, the proposed method significantly reduces the runtime required for inference.

### Weaknesses
1. Manual circuits are not fully explained (definition, how they are computed, cost of computation, etc.) - manual circuits are used as reference during evaluation (line 405), and it is necessary to provide these details regarding them. 

2. It is unclear how CD-T works for inference - is there a distinct circuit discovered for each inference datapoint, or is the circuit found on a broader scale, so as to tradeoff size vs. performance for a larger test set?

3. The authors are encouraged to discuss the practical utility of CD-T. Once their method yields a circuit, could additional analyses, such as on attention heads, be conducted? For instance, are there heads that consistently produce positive or negative outputs across all data points, or do the importance of attention heads vary based on input data characteristics?

4. What transformer architecture is used for the experimental results?

### Questions
Line 20: "CD-T is the first ---?" there seems to be a missing word here

### Soundness
3

### Presentation
3

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
The paper introduces Contextual Decomposition for Transformers (CD-T) for building interpretable circuits in llms for better mechanistic interpretability in transformers efficiently. In contrast to other methods, CD-T employs a mathematical decomposition that isolates the contributions of specific features, allowing CD-T to discover circuits at various levels of granularity. Results show significant improvements in runtime and interpretability over existing methods such as ACDC and EAP on several tasks.

### Strengths
1.	The paper is relatively well presented. It provides a clear description of the method, experiment details, and contribution. 
2.	Using the decomposition approach for designing/scaling LLM models is relatively novel and effective. Results show promising improvements in computational efficiency while maintaining circuit quality, and the method seems to be agnostic to the specific types of transformer models.

### Weaknesses
1.	The paper is relatively well presented. It provides a clear description of the method, experiment details, and contribution. 
2.	Using the decomposition approach for designing/scaling LLM models is relatively novel and effective. Results show promising improvements in computational efficiency while maintaining circuit quality, and the method seems to be agnostic to the specific types of transformer models.

1.	The description of the algorithm can be improved. In particular, the algorithm description is relatively informal and could benefit from more details and formalism. For “Prune nodes from S for which doing so increases the task metric”, how is increasing the task metric evaluated? Specifically, what is the precise mathematical formulation of the task metric, and how is the increase in this metric quantified when a node is removed? Is there a threshold for this increase to be considered significant enough for pruning? Furthermore, the algorithm's dependence on the initial set of nodes 'S' is unclear; how is this set selected, and what impact does its composition have on the final discovered circuit? The paper would benefit from a more rigorous definition of the search space and the pruning criteria.


### Questions
1. See W1; In addition, what’s the computational complexity of the algorithm in terms of the input parameter?
2. How does pruning affect the mechanistic interpretability of the model?

### Soundness
3

### Presentation
3

### Contribution
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
The paper proposes an automatic, mechanistic interpretability approach for finding circuits in transformer models. Their approach propagates backwards from the model output, finding a circuit of nodes most relevant to the given output, and from there the nodes most relevant to those nodes, and so on. These circuits are task-specific subgraphs in the larger model compute graph that are most stimulated (and most relevant) to the input type or task under consideration. 

The authors consider circuit discovery for the attention heads of transformer models, choosing to leave the MLP layers in an attention block for later work. Their linear decomposition model is mechanistic in that it solely depends on the weights and biases of each layer of the network and the relevance metric calculated for the previous layer. It does appear to be data-dependent in that it still relies on a dataset for calculating these relevance metrics. It also relies on precomputed mean activations to do so.

### Strengths
1) The paper's originality is in applying a novel formulation of an existing method - Context Decomposition - to transformer models, albeit to the attention heads of the transformer models. While novel, I am not in the space of circuit discovery in neural networks and unable to judge how novel this is. 
2) The presentation is clear and the limitations in data dependence and precomputation are made clear to the reader in algorithm pseudocode, which is also concise and clear. Experimentation is presented to clearly establish the work's superior performance over the baselines. Notation remains consistent through the paper to my eyes.
3) Significance: The work presents the an automatic circuit discovery approach using CD (extending it as CD-T) in transformer models, and clearly outperforms its chosen baselines. The approach is moreover mechanistic and iterative rather than probabilistic and therefore also comes with a guarantee of circuit discovery given certain assumptions on available data and time.

### Weaknesses
1) I am unsure of the significance of the work due to the iterative nature of the process and the need for data to adequately stimulate different 'tasks' (or behavior modes, perhaps?) and therefore discover circuits in the model. This is to my eyes not clearly explained. The iterative approach, while mechanistic, requires multiple passes through the network, and it's not clear how the number of iterations affects the quality or stability of the discovered circuits. Furthermore, the reliance on a dataset to 'stimulate' different tasks raises questions about the generalizability of the discovered circuits. If the dataset is biased or does not fully represent the model's capabilities, the discovered circuits might be specific to the dataset rather than reflecting the model's true underlying mechanisms.
2) Prior work is noted to have conducted circuit discovery on large language models, and I can't easily find the models used for circuit discovery here. That lack of clarity is concerning, especially when using the manually discovered circuits as a target and prior art as baselines. The specific architectures of the models used for both the target circuits and the baselines are not clearly stated, making it difficult to assess the validity of the comparisons. Without knowing the model sizes, layer configurations, and other architectural details, it's hard to determine if the improvements are due to the method itself or simply differences in model architecture.
3) I am also uncertain of scalability of this approach, considering that the network architectures under evaluation are not clear and that it has been restricted to attention heads rather than MLP layers. I am also uncertain of the effects of sequence length, autoregressive or non-autoregressive decoders. Section 5 does not make these things clear. The restriction to attention heads is a significant limitation, as MLP layers are known to play a crucial role in transformer models. The lack of clarity on the impact of sequence length and decoder type further limits the applicability of the method, as these factors can significantly affect the behavior of transformer models and the resulting circuits.

### Questions
1) I would suggest clearly presenting model architectures under evaluation and assumptions being made on input data for the approach - the mechanistic relevance metrics are ultimately calculated from the outputs derived from input data.
2) How would this scale to large training datasets in LLMs? Is there a minimum dataset required? Can the authors comment on this?
3) What is the effect of autoregressive models and sequence to sequence decoding on this approach? Is there a difference? I don't see a clear analysis in Section 5, and while that is not necessary it would be nice to have the authors comment on this in Section 6.
Questions addressed in comments.

### Soundness
3

### Presentation
4

### Contribution
3
