# Positional Attention: Out-of-Distribution Generalization and Expressivity for Neural Algorithmic Reasoning

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5

## Abstract
\noindent There has been a growing interest in the ability of neural networks to solve algorithmic tasks, such as arithmetic, summary statistics, and sorting. While state-of-the-art models like Transformers have demonstrated good generalization performance on in-distribution tasks, their out-of-distribution (OOD) performance is poor when trained end-to-end. In this paper, we focus on value generalization, a common instance of OOD generalization where the test distribution has the same input sequence length as the training distribution, but the value ranges in the training and test distributions do not necessarily overlap. We propose that using fixed positional encodings to determine attention weights -- referred to as positional attention -- enhances empirical OOD performance while maintaining expressivity. We support our claim about expressivity by proving that Transformers with positional attention can simulate parallel algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes that using fixed attention patterns with only positional information (positional transformers) can enhance transformer capabilities for tasks such as sorting and minsum. The authors explain this phenomenon by demonstrating that positional transformers can effectively implement any algorithm defined in a parallel computation model (PCOC), and use experiments to valid their findings.

### Strengths
The paper demonstrates both experimentally and theoretically that attention mechanisms utilizing only positional information possess significant expressive power, presenting interesting implications for future research directions.

### Weaknesses
While the paper effectively demonstrates the expressive power of positional transformers, I have two main concerns:

1. Regarding the theoretical analysis of positional transformers' expressive power (Section 5):
The argument that positional transformers can simulate PCOC seems somewhat not surprising, given that MPC can simulate PCOC (with more rounds), PCOC can be considered a special case of MPC. While Lines 123-129 argue that "MPC requires input data to specify destinations for communication," these destinations are not truly "specified by input," as each destination is computed from the source with detail-designed mlp[1]. Since (one-hot) positional information can easily implement any fixed attention pattern, this theoretical contribution seems limited, especially considering that [1] achieved similar results without utilizing positional information.

2. Regarding the experimental validation (Section 6):
The experimental setup may not adequately demonstrate positional transformers' superiority over vanilla transformers in these tasks. The input data for vanilla transformers are sequences of scalar numbers, and adding absolute positional information to these scalars significantly impacts the original data. This naturally disadvantages vanilla transformers, as they must simultaneously process both the original data (for value/output) and positional information (for attention) by their sum. Maybe some additional experiments, such as use *nonparallel* vectors to denote each (integer) number and let model predict target label y one by one, would be more convincing.

### Questions
Please refer to the weaknesses section.

### Soundness
3

### Presentation
3

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
This paper proposes decoupling the query and key vectors from the value vectors, and making them global for every layer. 
This results in a transformer structure that is learned but fixed at every layer.
The authors demonstrate on some simple synthetic tasks that the model still can perform these tasks, and that they generalise on size and values.

### Strengths
Generally, decoupling structure and computation might have some positive effects, depending on the task. 
By having a separate key query decided at the start of the forward pass can achieve this decoupling, and depending on how they are computed, can help in generalisation.
The paper shows some tasks in which this is possible without explicit position embeddings and layer dependent attention routing, which may hold some promise for graph structured tasks and transformers (e.g. molecule-related)

### Weaknesses
The perspective of Transformers as a graph convolution network with a learned attention mask is [not new](https://thegradient.pub/transformers-are-graph-neural-networks/). Further, the decoupling of structure and layer-input is also [not novel](https://aclanthology.org/2022.acl-long.327.pdf). The overall contribution of this paper is minimal, and I would suggest focusing on parameterisations of P, particularly task-specific, for this type of model. The write-up on PCOC is also strongly reminiscent of message-passing in graphical models, so I'm not sure what this perspective contributes, though I may be missing something here.

### Questions
- Can you plot accuracy on the tasks you’ve benchmarked on? MSE doesn’t really seem informative here.
- Could you have more information / variants of how you compute P? This seems to be the most crucial element of the structure, now that it’s been decoupled from each layer’s input. What tasks work with just an embedding table? What tasks would require some prior processing from another Transformer model? etc.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores the enhancement of out-of-distribution (OOD) generalization in Transformers for algorithmic tasks by proposing the positional attention mechanism. Unlike standard self-attention, this approach calculates attention weights solely based on fixed positional encodings, maintaining expressivity. Through theoretical and empirical evidence, the authors demonstrate that positional Transformers can simulate parallel algorithms, achieving significant improvements in OOD value generalization over standard Transformers.

### Strengths
1. The methodology is well-explained, with diagrams and equations aiding in understanding the architecture and theoretical claims.

2. The paper includes a theoretical analysis that establishes the expressive power of positional Transformers by linking them to the Parallel Computation with the Oracle Communication (PCOC) model.

### Weaknesses
1. The model’s OOD generalization appears to primarily rely on two factors: (1) the independence of the attention matrix from the input $X$, and (2) the absence of one-hot encoding for the input. For example, in the cumulative sum task, positional attention only needs to equally weight the first $i$ tokens onto the  $i$-th token, which allows the output to approximately scale by the same factor as the input within a certain range. However, this design introduces notable limitations: first, positional attention is unable to model relative relationships between different inputs $X$, limiting its applicability to tasks that require more complex relative positioning. Second, this model appears suitable primarily for tasks involving numeric values that do not require one-hot encoding, constraining its utility in a broader range of applications.

2. Several minor typos and formatting inconsistencies were observed, such as missing periods on lines 156, 356, and 364. Addressing these issues would improve the manuscript’s professionalism and readability.

### Questions
In my view, the proposed architecture resembles a learnable adjacency matrix version of a Graph Neural Network (GNN), even with the explicit incorporation of positional information. Could the authors compare the results with those achieved by a GNN under the same sentence length? It would be interesting to see if the proposed method significantly outperforms GNNs, as such a comparison could highlight the unique advantages of this approach.

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
4

### Summary
The paper focuses on the task of improving the performance of Transformer models on arithmetic tasks. In particular, the authors focus on “value generalisation”, that is “where the test distribution has the same input sequence length as the training distribution, but the value ranges in the training and test distributions do not necessarily overlap”. Stemming from the observation that the steps executed by many basic array algorithms (sum, sort, min, max) are independent of the underlying values, the authors propose to fix the attention matrix of each layer, and make it independent of the provided input.

### Strengths
The paper impresses with the following points:

S1. The paper is very-well written, with the exposition, background material, definitions, methods and results being very clearly presented and easy to follow, with extensive details.

S2. The paper offers a thorough theoretical explanation of how the proposed positional transformers can simulate any algorithm falling under the Parallel Computation with Oracle Communication (PCOC) model.

### Weaknesses
W1. Section 5 of the paper focuses offers a theoretical explanation of why the proposed positional transformers can simulate any algorithm falling under the Parallel Computation with Oracle Communication (PCOC) model. While it is indeed quite interesting that there is a rich class of computation that can be approximated with fixed attention, it is not clear how this theory ties in with the rest of the paper. Most critically, how does this theory explain the observation that fixed attention result in __better__ empirical performance? Doesn’t the referenced work of Sanford et al. imply that transformers with dynamic attention should also be able to approximate algorithms from the same class?

W2. The paper’s main thesis is that _“positional attention enhances empirical OOD performance”_, however it does not propose a hypothesis explaining as to why that might be the case. I find this conclusion of the paper to be surprising and difficult to believe without further details. The authors construct a _strictly less expressive_ architecture that has _better_ performance. While that can be due to appropriate inductive biases, the classic transformer should be able to learn these tasks too. If the positional embeddings of the classic transformer are learnable and concatenated to the inputs, then isn’t it possible to show that for every positional Transformer, one can construct a classic transformer that is functionally equivalent to it? Furthermore, as the authors also discuss in their related work section, we know that the classic transformer is a universal approximator for continuous and discrete functions, as well as Turing-complete. Hence, the classic transformer should also  be able to solve the tasks considered in the paper. I am also concerned with the authors mentioning that 

> In particular, the weights can be very sensitive to the scale of input values. We observe a dramatic change in attention weights as soon as we give the model the same input but scaled so that the values lie outside the domain of the training data.

Perhaps I am missing something, but shouldn’t scaling the input by $\lambda$ scale all elements of the pre-softmax attention matrix by $\lambda^2$. And as scaling the pre-softmax activations is equivalent to adjusting the temperature of the softmax, isn't this difference in attention predictable and expected?

All that makes me think that the reported results might be caused by technical details in the implementation of the experiments, rather than due to positional attention being fundamentally better for some reason.

W3. Improving the ability of a Transformer to solve algorithms in isolation seems unnecessary: the example tasks used in the paper can be solved exactly with just a couple of lines of code. There would be value if the model uses these tasks as a subroutine of more complex tasks, e.g., given a natural text description of purchases, group them by type and compute commulative sums for each group. However, the paper does not study whether the proposed positional encodings work for more general data distributions, e.g., NLP tasks, different formatting of the same tasks, non-PCOC tasks, or mixtures of tasks. My intuition is that the ridgidity of the attention mechanism that improves the performance on the tasks considered in the paper, would be detrimental to the performance on such tasks that require flexibility, nuance, and robustness. And as LLMs are useful precisely for these less-structured tasks —for the structured ones, one is better off writing a Python script— I feel that the paper has failed to propose a modification of the transformer architecture that would result in improved performance in any realistic case. As such, the paper would likely be of limited value to the community.

Overall, despite the clear writing and good presentation, the paper has major conceptual and methodological flaws. The restricted architecture that is proposed could work well for the small task set the paper considers, but is unlikely to work well in practical settings where flexibility, nuance, and robustness matter. Moreover, the paper does not hypothesise or explain why the prosed restricted architecture would perform better than the more general classical transformer that subsumes it. This question is also not addressed by the theoretical analysis of the paper. The leaves the central claim that “positional attention enhances empirical OOD performance” not well-substantiated.

### Questions
Minor question:

Q1. Why are you parametrising the fixed attention matrices $A$ by the $W_q$ and $W_k$ matrices instead of directly parameterising $A$ (in Eq. 2)? Is it to reduce the model size? How would your results change if you parametrise $A$ directly?

### Soundness
2

### Presentation
4

### Contribution
2
