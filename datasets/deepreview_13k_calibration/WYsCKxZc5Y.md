# Contextually Guided Transformers via Low-Rank Adaptation

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3

## Abstract
Large Language Models (LLMs) based on Transformers excel at text processing, but their reliance on prompts for specialized behavior introduces computational overhead. We propose a modification to a Transformer architecture that eliminates the need for explicit prompts by learning to encode context into the model's weights. Our Contextually Guided Transformer (CGT) model maintains a contextual summary at each sequence position, allowing it to update the weights on the fly based on the preceding context. This approach enables the model to self-specialize, effectively creating a tailored model for processing information following a given prefix. We demonstrate the effectiveness of our method on synthetic in-context learning tasks and language modeling benchmarks. Furthermore, we introduce techniques for enhancing the interpretability of the learned contextual representations, drawing connections to Variational Autoencoders and promoting smoother, more consistent context encoding. This work offers a novel direction for efficient and adaptable language modeling by integrating context directly into the model's architecture.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The Contextually Guided Transformer (CGT) paper introduces a novel Transformer model that incorporates context adaptation directly into its architecture. Unlike traditional Transformers that rely on prompts or fine-tuning to adapt to new tasks or contexts, CGT dynamically adjusts its processing based on a context summary that evolves as the model reads through the input sequence.

### Strengths
The CGT introduces a unique approach to embedding context into the Transformer’s architecture. By using y-components (context summaries) to dynamically modulate the model, CGT offers an innovative solution to integrate context without the need for explicit prompting at every layer.


The auxiliary loss is a thoughtful addition, penalizing large changes in the context summary to encourage smooth, interpretable, and stable evolution of the y-components. This loss term is well-conceived.


CGT holds promise for applications requiring efficient, context-specific adjustments to input sequences, potentially reducing the need for resource-intensive prompt processing in context-sensitive tasks.

### Weaknesses
The paper’s explanation of core concepts, especially around the auxiliary loss, low-rank transformation of y-components, and the role of x- and y-components, is highly technical but but lacks clarity. The separation of x- and y-components and the exact mechanism of context modulation are only partly clear after multiple readings and external clarifications.
In particular, sections describing the technical architecture, auxiliary loss, and low-rank transformations should be simplified, with more intuitive explanations.

The experiments in the paper are insufficient to support the claims made about CGT’s adaptability and efficiency. The limited range of benchmarks leaves questions regarding CGT’s real-world performance on common language tasks (e.g., machine translation, text classification, etc.).

Comparisons are mostly against standard Transformers, which do not offer context adaptation; comparisons with strong baselines in adaptive transformer architectures, such as [Dynamic Evaluation (DE)](https://proceedings.mlr.press/v80/krause18a.html) and other [Test-Time Training]() methods, are necessary to verify if CGT’s approach is truly advantageous.

The paper claims that CGT is a flexible, context-adaptive model, yet the provided experimental results do not provide convincing evidence of this. The model’s claimed efficiency and ability to improve over static Transformer architectures are not well-validated.
Moreover, the choice of synthetic tasks and limited application domains makes it difficult to gauge how well CGT would perform in more complex or real-world tasks. A more robust evaluation on diverse benchmarks would provide stronger empirical support for CGT’s effectiveness.

### Questions
Will the code be open-sourced for this work?

### Soundness
3

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
4

### Summary
This paper proposes a modified Transformer model called the Contextually Guided Transformer (CGT). To achieve self-modulation, it uses a context summary embedding at each layer to update subsequent layers’ weights by balancing the original task cross-entropy loss with a context auxiliary loss. CGT shows good performance in specialized tasks, especially in initial context-critical tasks, and is more efficient than current methods, which often rely on repeated attention-guiding prompts or an additional model to guide the main Transformer’s weight updates. To improve interpretability of the context representation, the paper also introduces element-wise regularization by viewing the Transformer as a Variational Autoencoder (VAE), ensuring the context summary embedding evolves gradually.

### Strengths
1.This paper introduces an innovative architecture that enhances Transformer behavior on more specialized tasks. Instead of using repetitive prompts or training an additional model—which increases computation cost and complexity—it introduces self-specialization by exploring the different potential between global context and local context of embeddings.
2. They introduce a simple regularization scheme by viewing the transformer as VAE.
3.The design of the loss function and regularization function is elegant and well-explained, contributing to clearer demonstrations and results.

### Weaknesses
1.The experiments only compare CGT with a traditional autoregressive causal Transformer as a baseline across limited datasets (types of tasks). The results would be more persuasive if other modified Transformers for specialized purposes were included in the comparison. Specifically, the paper lacks comparison to models that incorporate mechanisms for context adaptation or task-specific specialization, such as those employing dynamic parameter generation or hypernetworks. The absence of these comparisons makes it difficult to assess the true novelty and effectiveness of CGT relative to existing approaches designed for similar goals. For instance, comparing against models that use attention mechanisms to dynamically condition on context would provide a more rigorous evaluation.
2.The paper finds that consecutive tokens in the context summary embedding do not behave smoothly, contrary to expectations. An explanation of why this phenomenon occurs would improve the paper. The lack of smoothness in the context summary embedding raises questions about the interpretability and stability of the learned representation. It is unclear whether this behavior is a fundamental limitation of the proposed approach or an artifact of the training process. Further investigation is needed to understand the underlying causes and potential implications for model performance.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes an alternative to using explicit prompts for specializing LLMs. The authors introduce a method called Contextually Guided Transformer. This method processes the context text with a lighter-weight model and generates weight adaptation for the full model. Furthermore, to improve computation efficiency, the authors introduced auxiliary loss, smoothness prior, and VAE to allow the model to keep the weight adaptation fixed in the full model. The authors perform experiments on two synthetic toy tasks and one language modeling task and support the results with various analyses.

### Strengths
* This paper proposed an innovative solution to an interesting problem, leveraging thoughts from various research directions, such as adapter/lora, low-rank decomposition, VAE, and hyper tuning.

* The authors have performed a plethora of different experiments and analyses. These results help reveal how the method works.

### Weaknesses
 * The datasets used in this work have limited information. But, to answer whether we can encode context into weight adaptation, we need tasks like reading comprehension. More specifically, in the synthetic dataset, the model only needs to encode two numbers from the context; in the linear regression dataset, the model needs to encode 16 numbers; finally, in language modeling, the benefit can be mostly captured by simply encoding the topic (there are eight in total), as partially suggested in the t-SNE analysis. The synthetic and regression tasks are too simplistic to demonstrate the method's ability to capture complex contextual information. The language modeling task, while using a more realistic dataset, appears to be heavily influenced by topic rather than nuanced contextual understanding.

* Writing is relatively unclear. There are multiple places where the method or experiment setting is ambiguous. (see the questions for details)

* Limited successes in experiments. Although there are encouraging results in the toy datasets, in language modeling, the effect is not (potentially due to undesirable experiment setting rather than shortcomings of the method). The gains observed in the toy datasets do not translate to the language modeling task, suggesting a potential limitation in the method's scalability or applicability to more complex scenarios. The lack of substantial improvement in language modeling raises concerns about the practical relevance of the proposed approach.

* Although saving the cost of explicit prompting is a main objective, this paper does not compare costs either theoretically or empirically. Ideally, we should compare (i) not fixed (ii) fixed (iii) baseline (iv) baseline with cached kv from context.

### Questions
* I need some help understanding the experiment setting. In the three datasets, which part of the text is treated as y, and which part is treated as x? Could you provide some examples in the rebuttal?

* I didn't manage to understand the model's architecture. How is the representation of x and y produced from the GPT-2 model? When we change the x and y dimensions, does that also affect the model's hidden dim? And how do we use different x and y

* In the language modeling experiment, I don't understand the reason for cutting and concatenating two text samples. I would expect using a single example as the more logical choice for measuring the model's ability to use context. If the text comprises two independent and incomplete sentences, the model benefits less from short-term context (it can break up at any point) or long-term context (the early tokens may belong to an irrelevant example).

* Line 337 whcih -> which

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a modification to the Transformer architecture that integrates prompt context into the model's weights and activations. This integration enables the model to perform in-context learning without relying on preceding examples. To enhance the learned weights, the paper introduces an auxiliary loss and regularization techniques, resulting in smoother and more consistent results. To validate the effectiveness and interpretability of this approach, the paper conducts a series of experiments.

### Strengths
1. The presentation of the method is clear, providing a comprehensive introduction to its intricacies and implementation.
2. The theoretical support provided is convincing, extending across multiple research fields to demonstrate its validity in diverse contexts.
3. The experiments conducted are substantial and demonstrate the interpretability aspect of the method through multiple tests and analyses.

### Weaknesses
1. The proposed method needs to train from scratch for each distinct task, which is not a efficient way.
2. The quantitative results presented in Table 1 exhibit significant interval overlap, thereby reducing their statistical significance.
3. The applicability of the method remains uncertain due to its development on synthetic datasets and the necessity of training from scratch, as opposed to utilizing real-world datasets and adapting pretrained models.

### Questions
1.	If the model necessitates training from scratch for each distinct task, it would become prohibitively expensive. Consequently, one might consider training a LoRA module as a more efficient alternative. Please provide further elaboration on the motivations.
2.	How much time can be saved by eliminating the examples, compared with the time required to train the model?

### Soundness
3

### Presentation
3

### Contribution
2
