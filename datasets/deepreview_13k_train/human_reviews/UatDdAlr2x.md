# Counting in small transformers: The delicate interplay between attention and feed-forward layers

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
How do different architectural design choices influence the space of solutions that a transformer can implement and learn? How do different components interact with each other to shape the model's hypothesis space? We investigate these questions by characterizing the solutions simple transformer blocks can implement when challenged to solve the histogram task -- counting the occurrences of each item in an input sequence from a fixed vocabulary. Despite its apparent simplicity, this task exhibits a rich phenomenology: our analysis reveals a strong inter-dependence between the model's predictive performance and the vocabulary and embedding sizes, the token-mixing mechanism and the capacity of the feed-forward block. In this work, we characterize two different counting strategies that small transformers can implement theoretically: relation-based and inventory-based counting, the latter being less efficient in computation and memory. The emergence of either strategy is heavily influenced by subtle synergies among hyperparameters and components, and depends on seemingly minor architectural tweaks like the inclusion of softmax in the attention mechanism. By introspecting models \textit{trained} on the histogram task, we verify the formation of both mechanisms in practice. Our findings highlight that even in simple settings, slight variations in model design can cause significant changes to the solutions a transformer learns.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the author studied the relationship between attention and the feedforward layer through the task of histogram task.

### Strengths
The author studied an interesting topic about the relationship between the attention and the feedforward layer.

### Weaknesses
1. The paper’s narrative could use some improvement for better clarity and flow.

2. This paper studies the relationships among components in transformers within the context of histogram tasks. However, there isn’t enough evidence to show that this empirical study on histograms alone can adequately represent the properties of transformers in general. The cited work, Thinking like Transformers, also uses histograms but includes reverse sorting and other tasks to provide a broader context.

3. Another concern is the significance of these findings—why are they important, and do they provide meaningful insights?

4. There’s little discussion on how these findings could guide the adjustment or application of transformer structures in practical contexts.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper explores the performance of small Transformer models in performing counting tasks (specifically histogram tasks), analyzing how the collaboration of different components in the model architecture affects the final solution.
The authors found that in the histogram task, the predictive performance of the model is closely related to the vocabulary size, embedding dimension, token mixing mechanism and the capacity of the feed-forward block. Small Transformers can implement two counting strategies, the choice of which is influenced by hyperparameters and synergies between components. Even small architectural adjustments can lead to significant changes in the solutions learned by the model.

### Strengths
1. This paper demonstrates how various components of the transformer affect the model's learning ability, which can help understand the internal mechanisms of  transformer

2. The authors provide a simple yet effective testing environment, making it possible to evaluate the impact of the model architecture on solutions more clearly.

3. The visualizations are well done, making it easier to understand.

### Weaknesses
1. The paper analyzes only a simple single-layer transformer structure, while scaled-up models in real applications may exhibit different behaviors. Additionally, this paper overlooks the impact of the autoregressive mechanism and positional encoding. Specifically, the single-layer architecture limits the model's ability to capture hierarchical relationships within the data, which are often crucial in complex counting tasks. The absence of an autoregressive mechanism means the model cannot leverage sequential dependencies, which could be important for more nuanced counting scenarios. Furthermore, the lack of positional encodings means the model treats all tokens as unordered, potentially hindering its ability to distinguish between tokens based on their position in the input sequence.

2. Although the paper reveals the impact of architectural details on model performance, it lacks clear guidance for practical applications. For instance, it analyzes how relation-based counting, inventory-based counting, and softmax significantly influence the model's learning strategies and performance. However, I find it challenging to relate these methods to transformer models in real-world applications. I believe that adjustments in model design often need to be validated in practical settings, yet the paper does not provide specific application examples or optimization suggestions. The analysis of counting strategies, while interesting, remains somewhat abstract without concrete examples of how these strategies manifest in practical scenarios, such as natural language processing or time-series analysis. The paper does not offer specific recommendations on how to translate these findings into actionable design choices for real-world transformer applications.

### Questions
Could you explain in detail what the "online learning setting" in Line 153 means?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work investigates how different components of transformer architectures contribute to solving the counting task (creating a histogram of token occurrences in a sequence). The key research question is: how do architectural choices like embedding dimension, hidden layer size, and mixing mechanism (dot product attention vs linear) affect the solutions a transformer can learn? The authors discover and theoretically back up two distinct strategies transformers can use: (1) relation-based counting (which is more efficient but requires specific architectural features) and (2) inventory-based counting (which requires more parameters but is more flexible) - and show how seemingly minor architectural choices like including softmax in attention can dramatically affect which strategy emerges. They map out exactly what parameter regimes allow each strategy to work, including surprising findings about how transformers can still function even when the embedding dimension is smaller than the vocabulary size.

### Strengths
* The paper is well-written, easy to follow, and provides sufficient analysis for its claims.
* Discovers and Discusses two strategies which 1-layer transformers can use to perform the counting task (i.e., relation-based and inventory-based) and in doing so considers a range of possible hyperparameter selections that affect this strategic choice.
* During its analysis further studies the role of BoS token showing that together with softmax in the counting task, can help models with smaller p and d sizes to still reach perfect accuracy.

### Weaknesses
 * Limited scope and applicability, specifically: (1) Only examines single-layer transformers, (2)Focuses on just one task (histogram counting)
* No clear path to extending insights to more complicated settings more specifically multi-layer transformers
* Lack of practical impact in the sense that it is hard to find a direct translation from this paper findings to real-world transformer design for real-world tasks

### Questions
Have you done any analysis or insight you can share on: 
1. what behaviour can we expect in terms of the same hyperparameter choices (embedding dimension, Hidden Layer Size, and Vocab Size) whether as a  2 or 3 layer blackbox and/or an isolation of one of the transformer layers in a multi-layer setting?
2. Have you done any initial analysis to share about whether the same relationships for parameters and potential solving strategies hold for other tasks (such as the sorting or lookup problems you referred to or any other tasks)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In an attempt to improve the interpretability of different elements of transformers, the authors use transformers to solve a histogram task. They incorporate two different counting strategies (relation-based and inventory-based), and replace different components of transformers in a controlled setting to study the relative role of each component. They find that both the attention mechanism (without applying softmax) and a sufficiently large FFN are capable of solving the histogram task. They also find that this task is sensitive to hyperparameters.

### Strengths
- The explanations, logic and experiments are sound

### Weaknesses
 - If I understood correctly, the main contributions are that for the histogram test: 1. using the attention mechanism but without the softmax step (relation-based counting) is capable of high accuracy, and 2. Using learnable-matrix multiplication instead of attention (inventory-based counting) is not capable of high accuracy, but using a FFN can mitigate this by acting as a lookup table. It would be helpful if the authors would elaborate on why these findings are important.
- It would also be helpful if the authors provide some intuition on why they chose the histogram test. To be specific, transformers are designed for prediction and regression tasks. It's not clear why the authors chose to study a task that diverge from conventional transformer use cases. Perhaps there are interesting theoretical or practical insights that motivated this direction?

### Questions
- In your opinion, what do these findings tell us about the hypothesis space of transformers?

### Soundness
3

### Presentation
3

### Contribution
2
