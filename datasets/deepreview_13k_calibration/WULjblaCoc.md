# When Can Transformers Count to n?

- Decision: Reject
- Avg Score: 5.60
- Scores: 5, 6, 6, 5, 6

## Abstract
Large language models based on the transformer architecture can solve highly complex tasks. But are there simple tasks that such models cannot solve? Here we focus on very simple counting tasks, that involve counting how many times tokens in the vocabulary appeared in a string. We show that if the dimension of the transformer state is linear in the context length, this task can be solved. However, the solution we propose does not scale beyond this limit, and we 
provide theoretical arguments for why it is likely impossible for a size-limited transformer to implement this task. Our empirical results demonstrate the same phase-transition in performance, as anticipated  by the theoretical argument. Our results demonstrate the importance of understanding how transformers can solve simple tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies an important question on the counting ability of Transformers. An interesting construction is proposed to address the query counting problem using Transformer architecture.

### Strengths
This paper studies an important question on the counting ability of Transformers. An interesting construction is proposed to address the query counting problem using Transformer architecture.

### Weaknesses
Although some theoretical discussion are provided for the proposed construction, the construction itself is only a toy model and may be too simple to reflect the ability of realistic Transformers. Also, the fact that this particular construction cannot achieve certain tasks does not indicate that there does not exist a construction that can. Plus, there are too many loose ends in the proofs (see Questions below).

1. In your examples, you are counting the number of appearance of certain letters instead of tokens. Therefore, tokenization plays an important part in this task. However, tokenization is not discussed in the paper. The paper should address how different tokenization strategies (e.g., byte-pair encoding, word-piece) might affect the counting task, especially when dealing with sub-word units or when the same word is tokenized differently in different contexts.
2. The proposed architecture only considers one single layer with one head without normalization layers. This is not the standard Transformer architecture with MLP and skip connections. The absence of normalization layers (LayerNorm or BatchNorm) and skip connections could significantly impact the model's ability to learn complex patterns and generalize to different counting tasks. The single-head attention mechanism might also limit the model's capacity to capture diverse relationships between tokens.
3. Lines 181-183 argue that replication of the input results in the same output. Is there any theoretical proof? Is this true in practice? The claim that replicating the input sequence does not change the output needs more rigorous justification. This behavior is not necessarily true for all attention mechanisms, especially when positional embeddings are involved. The paper should provide a formal proof or a detailed explanation of why this holds for the specific architecture used.
4. Please elaborate on why the assumption in Eq(1) holds in reality. The assumption in Eq(1) that the input dimension is larger than the dictionary size is not realistic for most practical scenarios where the vocabulary size is much larger than the embedding dimension. The paper should discuss the implications of this assumption and how the results might change when this condition is not met. The paper should also address the more common case where the embedding dimension is much smaller than the vocabulary size.
5. In the entire paper, including the experiment section, the training of the model and the training data are not discussed. Do pre-training, training data, and fine-tuning affect the ability of Transformers? What if a dataset is constructed with (sequence, count) pairs? The paper lacks a detailed discussion of the training process, including the dataset generation, optimization algorithms, and hyperparameter tuning. The paper should explore how different training strategies, such as pre-training on large datasets or fine-tuning on specific counting tasks, affect the model's performance. The impact of using datasets with explicit (sequence, count) pairs should also be investigated.

### Questions
1. In your examples, you are counting the number of appearance of certain letters instead of tokens. Therefore, tokenization plays an important part in this task. However, tokenization is not discussed in the paper.
2. The proposed architecture only considers one single layer with one head without normalization layers. This is not the standard Transformer architecture with MLP and skip connections.
3. Lines 181-183 argue that replication of the input results in the same output. Is there any theoretical proof? Is this true in practice?
4. Please elaborate on why the assumption in Eq(1) holds in reality.
5. In the entire paper, including the experiment section, the training of the model and the training data are not discussed. Do pre-training, training data, and fine-tuning affect the ability of Transformers? What if a dataset is constructed with (sequence, count) pairs?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a theoretical study on how a Transformer can learn the solution of counting. They consider two typical solutions. The first one is a histogram solution that keeps a histogram of the number of different types of tokens, and this requires a dimension linearly scaling with the vocabulary size. The second solution is by first calculating the inverse of the number of times the query tokens appears and then use the MLP to calculate the inverse function. Intriguingly, they show if the feedforward layer is of depth 1, the required width to represent the inverse function scales linearly with the context length.They empirically verified their theory on pretrained LLMs.

### Strengths
1. The presented theory is very clear. The authors explain their theoretical contribution with very intuitive argument.

2. The theoretical argument that vocabulary size and context length jointly blocks the learning of counting is well supported by empirical experiments.

### Weaknesses
1. The work is mostly constructive so it remains unclear whether Transformers will converge to either of the solution. A mechanistic investigation as mentioned in the conclusion will be a great supplement for the paper.

2. The width bottleneck in the second construction seems to hold only for 1-layer MLP.

3. Technically, the argument that position encoding is necessary only holds for encoder-based model or causal model with 1-layer, a point that should be made clear in the paper.

### Questions
1. If LayerNorm is used in the architecture, could this generate more parameter efficient architecture?

2. Is there a way to investigate what solution Transformers really converge to in training other than probing? For example, will the two construction differs meaningfully on some out of distribution test?

### Soundness
4

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
5

### Summary
This work investigates the ability of LLMs in counting tasks. This paper focuses on two basic tasks, QC and MFE, and demonstrates that the transformers can solve these tasks if the models' size is large enough, but face limitations when the dimension is small. Empirical and theoretical results highlight the importance of understanding these limitations to improve transformer architectures.

### Strengths
1. This work focuses on the counting task for the language models. The authors provide both theoretical and empirical results to demonstrate the limitations of LLMs when the dimension is small.
2. This paper is well-presented and easy for the readers to follow.

### Weaknesses
1. **Lack of Generality:** While the paper focuses on the counting task, its impact on real-world applications is unclear. The conclusions are specific to counting and may not generalize well to broader contexts. Specifically, the paper does not adequately address how the observed limitations in counting tasks translate to more complex scenarios involving sequential data processing, such as natural language understanding or code generation, where counting might be a sub-component but not the primary objective. The study's focus on simple counting tasks, like QC and MFE, may not capture the nuances of real-world problems where counting is intertwined with other cognitive processes.
2. The study primarily analyzes one-layer transformers, leaving the capabilities of multi-layer transformers unexplored. Further **theoretical** investigation is needed to understand how additional layers might influence performance on counting tasks. The paper lacks a detailed analysis of how the depth of the transformer affects its ability to learn counting functions, particularly when the vocabulary size increases. It is unclear if the limitations observed in single-layer models are fundamental or if they can be mitigated by adding more layers, which could potentially allow the model to learn more complex representations of the input sequences.

### Questions
1. How can the conclusions of this paper generalize to real-world tasks, such as math, code, and so on?
2. Do the limitations observed with small dimensions still apply to multi-layer transformers?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Paper investigates the ability of Transformer models to perform simple counting tasks, specifically focusing on counting the occurrences of tokens in a sequence. It explores whether Transformers can count effectively and, if so, under what conditions.

### Strengths
This paper is well-written, presenting a complex topic in a clear and structured manner. the use of well-defined examples, such as the "Query Counting" task and the "Most Frequent Element" problem, aids in illustrating the limitations and possibilities of Transformer architectures in a concrete way.

### Weaknesses
Overall, many of the assumptions in this paper are overly simplistic and do not align well with real-world Transformer design or training outcomes. Based on my experience and prior research on Transformer expressiveness, the findings presented here—particularly those concerning cases where d>m have been hinted at in earlier works and are not surprising, given the simplified single-layer Transformer model used in this study. However, real-world Transformer training is far more complex and has been shown to perform poorly on counting tasks, regardless of dimensionality.
Moreover, the experimental design in this paper is weak, with insufficient results to substantiate the authors' claims. The lack of detailed experimental methodology and the vagueness of the reported results undermine the argument. While I agree with the proposed "ideal case" of a histogram approach to counting, this notion is too trivial to warrant significant mention. Actual Transformer training involves many additional considerations, and practical optimization rarely converges to such an ideal case, as evidenced by many experiments I have done and those of other researchers.
I suggest the authors conduct a deeper exploration into the challenges of counting with Transformers. As it stands, the current version provides limited insights into the expressiveness of Transformers, on top of the existing papers.

Detailed problem: 
1. Counting Problem in Transformers: Previous research has explored the counting problem in Transformers, but this work lacks a comprehensive review of such studies. A notable contribution to this area is the paper "Language Models Need Inductive Biases to Count Inductively", beyond transformer they also study linear attention such as Mamba and RWKV. Additionally, counting on out-of-distribution (OOD) data often requires incremental dictionary size (training to count to n but testing on count to n+k). Several studies, therefore, focus on the "parity" problem in Transformers, where models count the even or odd occurrences of a token, representing an early form of counting research. For instance, "Overcoming a Theoretical Limitation of Self-Attention" proposes a similar approach to counting as your paper, which is not acknowledged here. A recent paper, "Counting Ability of Large Language Models and Impact of Tokenization," provides an extensive overview of counting in Transformers, which could guide a more thorough literature review on counting with Transformer. There are lots of Parity-related theoretical work and experimental work with Transformers, which study counting, they all need to be discussed. 

2. Expressiveness Limitations in Transformers: Prior theoretical and empirical findings suggest that Transformers lack the expressive capacity to act as counter machines. For example, DeepMind's work "Neural Networks and the Chomsky Hierarchy" shows that Transformers struggle even with parity tasks, which are simpler than general counting. Moreover, "Language Models Need Inductive Biases to Count Inductively" and "Overcoming a Theoretical Limitation of Self-Attention" argue that complete Transformer architectures cannot perform counting tasks without specific inductive biases. Common positional encodings (like sinusoidal or absolute encoding) fail in this regard. My own experiments corroborate this—Transformers do not converge to a counting model without cetain biases. This limitation is examined thoroughly in "Overcoming a Theoretical Limitation of Self-Attention," which offers a similar solution to the one proposed in your paper.

3. Limited Theoretical Scope: The theoretical analysis in this paper overlooks several critical components in modern Transformer design that impact expressiveness, such as layer normalization, positional encoding, floating-point precision, residual connections, and advanced activation functions. Many recent studies cover these in greater depth. By simplifying the Transformer to a single attention module, this paper overlooks architectural nuances, which limits the validity of its conclusions. I recommend engaging with recent theoretical work on Transformer expressiveness in light of these elements (matter of fact, many research show that some of the modules here greatly change the theoretical limits of Transformer). The simplified version of your work is similar to MLP, where each node simply connect to every other previous node, and therefore results are trivial. 

4. Precision Considerations: Precision is not adequately addressed here. While the paper mentions the need for 
d>m it omits the scenario where infinite precision enables Turing completeness with finite d. This has been shown in works like "Attention is Turing Complete" and recent chain-of-thought (CoT) research by Tengyu Ma and others. With higher precision, more information can be compressed within floating-point numbers, contrary to this paper's assumption of clear-cut feature vectors.

5.  The counting discussed in this paper is non-inductive, while most modern large language models (LLMs) rely on inductive counting, requiring 
O(N) depth complexity. Both "Language Models Need Inductive Biases to Count Inductively" and "Counting Ability of Large Language Models and Impact of Tokenization" discuss this in detail. This is critical for two reasons: (a) natural language counting often requires sequential comprehension, necessitating a step-by-step approach; and (b) in comparison, recurrent models like RNNs handle counting tasks more naturally than Transformers (almost easily achieve 100\% OOD accuracy according to above papers), highlighting the role of recurrence in inductive counting. Recurrence signals a model’s inductive capacity for counting, suggesting that neural networks generally adopt an inductive counting approach without explicit biases.

6.Prior research shows that positional embedding is crucial for OOD counting. This paper assumes that any positional encoding will equip the model with positional information for counting. However, specific positional encoding designs can distort theoretical assumptions. For example, transformations of values like 1 and 0.5 through positional encoding (either additive in Cosine or geometrical shifting as in ROPE) can cause information loss and lead to unexpected behaviors. These aspects, covered in previous studies, are not discussed here.

6. Experiment lacking specifications. Your experiment does not say how in-distribution training and out of distribution testing is done. Within DIstritbuion, the counting behaves different than OOD, as shown by above mentioned papers. 


7. The experimental section lacks clarity regarding in-distribution (ID) training and OOD testing. Counting behaves differently in ID versus OOD contexts, as shown in the referenced papers. Providing explicit details on the data split methodology would strengthen the validity of the results.

8. LLM-Based Counting: Counting in LLMs presents unique challenges. Not only does it involve inductive methods, but factors like tokenization and chain-of-thought (CoT) prompting also affect the theoretical counting capacity of the Transformer architecture. Studies by Tengyu Ma and others in "Counting Ability of Large Language Models and Impact of Tokenization" delve into these factors. The absence of these considerations in your experiments reduces the credibility of the findings. CoT prompting can unexpectedly enhance the expressiveness of Transformers by mimicking recurrent behaviors similar to RNNs. Although the paper discusses LLMs, it does not mention use of CoT and its effect, which is worth addressing given its relevance to theoretical expressiveness.

9 Gap Between Theory and Practice: The theoretical proofs claim the existence of a Transformer capable of counting, albeit simplified. However, existence does not guarantee practical trainability. As previously mentioned, Transformers rarely converge to this type of behavior in practice without specific biases. Floating-point representations of features can also complicate interpretation, indicating a substantial gap between theoretical assertions and empirical outcomes. More experimental evidence is needed to substantiate the theoretical claims made in this paper.

### Questions
To clarify the unique contributions of your work compared to "Overcoming a Theoretical Limitation of Self-Attention," it would be beneficial to highlight additional perspectives or distinct aspects that differentiate your approach.  As they propose nearly identical Transformer design in counting but with more in-depth experimental analysis.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies transformers' counting capability, focusing on two counting tasks, i.e., QC and MFE. 
For analysis, the paper considers transformers' expressive power. The paper shows two possible
solutions for QC, i.e., Histogram and CountAttend, and highlights the relations between the embedding dimension, the model size, the dictionary size, and the sequence length in the two solutions, respectively. For MFE, the paper further 
proves bounds on the size of the embedding compared to the size of the dictionary. Experiments evaluate the dependence between the transformer model size and its ability to perform counting tasks both models trained from scratch and a pretrain LLM.

### Strengths
1. The paper analyzes the capability of transformers by considering simple yet representative counting problems, which is an interesting perspective.
2. In counting tasks, the paper highlights the relations between the embedding dimension, the model size, the dictionary size, and the sequence length theoretically. These results present an architectural limitation of the transformer and provide insights on how to overcome the issues.

### Weaknesses
1. The theoretical analysis is restricted to the expressive power of the transformer. It is unclear whether the proposed solutions for the counting tasks are learnable. Specifically, while the paper shows that certain architectures *can* represent the required counting functions, it does not address whether standard training procedures would converge to these solutions, or if the optimization landscape is conducive to finding them. The analysis lacks consideration of the inductive biases introduced by the training process, which could significantly impact the practical learnability of the proposed counting mechanisms.
2. While the theoretical analysis shows two possible solutions for QC, the experiments do not demonstrate the mechanisms of the transformer to perform the task. The experiments primarily focus on the scaling behavior of transformers with respect to counting accuracy, but they do not provide insights into how the transformer internally represents and manipulates the information to achieve counting. It remains unclear whether the transformer is actually implementing the proposed Histogram or CountAttend solutions, or if it is relying on alternative, potentially less robust, strategies.

### Questions
1. Do the constructions require infinite precision or only log precision? 
2. For QC, which are the mechanisms of the transformer to perform the task in practice?
3. The lower bounds in Lemma 4.4 and Theorem 5.1 are proved with constant-depth models. 
Do the lower bounds hold for deep models (up to poly(n) depth)? If not, do the lower bounds hold for constant-depth models with CoT?

### Soundness
3

### Presentation
2

### Contribution
3
