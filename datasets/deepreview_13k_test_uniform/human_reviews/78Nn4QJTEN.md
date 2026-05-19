# When Attention Sink Emerges in Language Models: An Empirical View

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
Language Models (LMs) assign significant attention to the first token, even if it is not semantically important, which is known as **attention sink**. This phenomenon has been widely adopted in applications such as streaming/long context generation, KV cache optimization, inference acceleration, model quantization, and others.  Despite its widespread use, a deep understanding of attention sink in LMs is still lacking. In this work, we first demonstrate that attention sinks exist universally in LMs with various inputs, even in small models. Furthermore, attention sink is observed to emerge during the LM pre-training, motivating us to investigate how *optimization*, *data distribution*, *loss function*, and *model architecture* in LM pre-training influence its emergence. We highlight that attention sink emerges after effective optimization on sufficient training data. The sink position is highly correlated with the loss function and data distribution. Most importantly, we find that attention sink acts more like key biases, *storing extra attention scores*, which could be non-informative and not contribute to the value computation. We also observe that this phenomenon (at least partially) stems from tokens' inner dependence on attention scores as a result of softmax normalization. After relaxing such dependence by replacing softmax attention with other attention operations, such as sigmoid attention without normalization, attention sinks do not emerge in LMs up to 1B parameters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates the phenomenon of attention sink in LMs, where significant attention is allocated to the first token regardless of its semantic importance. Key findings include the correlation of the sink position with the loss function and data distribution, and the behavior of attention sink as key biases storing extra attention without contributing to value computation. The paper also shows that attention sinks do not emerge when softmax attention is replaced with other operations like sigmoid attention without normalization, up to 1B parameters.

### Strengths
- The paper provides a thorough investigation into the attention sink phenomenon, covering various factors that influence its emergence in LMs.
- The findings have practical applications in areas such as streaming/long context generation, KV cache optimization, and model quantization.
- The study considers various model architectures, optimizers, and data distributions, offering a broad perspective on the attention sink phenomenon.

### Weaknesses
- The study notes that attention sink disappears with less training data, suggesting that the models might be overfitting to certain aspects of the training data. It seems that these two factors cannot be decoupled, and it is impossible to explain whether it is over-fit or the amount of data that affects attention-sink.
- The study claims that it focuses on the Language Models. However, this work pay more attention on auto-regressive LMs and may not capture the nuances of other types of encoder-like LMs or Jamba. Does those architecture can solve the attention-sink phenomenon?

### Questions
- How to identify the token where attention-sink occurs? How to determine those locations?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors conduct a comprehensive study of the attention sink problem and present robust empirical results. They discuss and examine the attention sink problem from various perspectives, including optimization, data distribution, loss function, and model architecture. Although the paper does not provide in-depth theoretical analysis, it may inspire further research into the understanding of the attention mechanism, which could, in turn, contribute to the development of stronger generative models. Therefore, I believe this paper would serve as a valuable empirical reference on the attention sink problem for the community and worths of acceptance.

### Strengths
1. The perspectives of studying attention sink problem is diverse and well-motivated. These perspectives are also inspiring to future studies on attention mechanisms.
2. The experiments is very comprehensive and diverse.

### Weaknesses
The primary weakness of this paper is the lack of in-depth analysis. The empirical results come across more as observations rather than as thorough investigations. Including more theoretical analysis or deeper experimental work would strengthen the paper. For instance, in the KV bias section, it would be beneficial to explore how attention variants with and without attention sink are related in formulation.

### Questions
Q1: In Fig. 4 (left), could you provide a performance curve, such as the validation performance of each model against model size? It appears that as the model becomes stronger, attention sink becomes more prominent. Additionally, I am curious about how attention sink correlates with validation loss.

Q2: Fig. 4 (right) shows that a lower learning rate results in a slower increase in attention sink. Is it possible that attention sink occurs simply because the model has not been well-tuned?

Q3: In Table 1, GPT-XL behaves very differently from Llama and Mistral. Do you have any intuition as to why this might be?

Q4: Could you provide some mathematical formulation on how the attention variants (2nd to 4th rows in Table 4) are correlated? Is there an inherent connection among these attention variants that excludes attention sink?

Q5: In Table 6, it appears that the normalizer may impact attention sink. Do you have additional evidence with other types of normalizers?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper studies the phenomenon of "attention sink" in Language Models, where significant attention is disproportionately allocated to the first token in input sequences, without taking into account its semantic importance. The attention sink has practical applications in areas such as streaming generation, KV cache optimization, inference acceleration, and model quantization. 

The authors performed a study across various LM architectures, input types, and training configurations to study the emergence and characteristics of attention sinks.
They found that attention sink happens across different LMs, including smaller models and those trained on random token sequences and that it emerges during optimization with sufficient training data, and its prominence is influenced by learning rates and weight decay.
They also found that attention sink functions similarly to key biases, storing additional attention scores that are largely non-informative and do not contribute to value computations. This behavior is partially attributed to the softmax normalization, which induces inner dependencies among attention scores.

The paper also shows that altering the attention mechanism, such as replacing softmax with sigmoid attention without normalization, can prevent the emergence of attention sinks in LMs up to 1 billion parameters.

### Strengths
- Reproducibily.
- The paper is well written and the experiments set up is soild.
- The paper not only observes the presence of attention sinks but also delves into the mechanistic reasons behind their emergence (also providing insights on the training dynamics that foster attention sinks).
- The paper show that attention sinks persist across various input types, like random token sequences and repeated tokens.

I think that this paper is a valuable step further in understanding the phenomenon of attention sink.

### Weaknesses
- The paper doesn't really take into account the role of attention sink impact on downstream tasks.
- While the paper studies the emergence and immediate characteristics of attention sinks, it does not assess the long-term impacts of attention sinks on model behavior (like stability during fine-tuning, adaptability to new tasks, or resistance to adversarial attacks).

Not really a weakness, but i found the paper a bit difficoult to read because of the unusual aesthetic choices: i think that this style would be great for a blog post where you have more space available to write, but i personally find easier to follow simpler-looking papers.

### Questions
In your paper you study how to mitigate the attention sink, are you sure that we want to mitigate it?

### Soundness
4

### Presentation
3

### Contribution
4
