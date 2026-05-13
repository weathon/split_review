# TENSORIZED ATTENTION MODEL

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
In recent years, attention mechanisms have played a crucial role in the
success of Transformer models, as seen in platforms like OpenAI's
ChatGPT. However, these models often struggle to compute attention
weights across various object types, such as 'comments,' 'replies,' and
specific 'subjects,' which naturally express relationships in many
real-world scenarios. This limitation can potentially impact prediction
accuracy.
To overcome this limitation, we introduce the Tensorized Attention Model
(TAM). By leveraging Tucker decomposition, TAM calculates attention
weights across a diverse array of objects and seamlessly integrates them
into Transformer outputs. 
We have implemented TAM within the Transformer encoder and have
showcased its effectiveness in response selection tasks. Our model takes
into account relationships based on 'the current context in the
dialogue', 'the entire dialogue history', and 'the subject matter of the
dialogue'. Evaluation using the Reddit dataset across a wide variety of
topics indicates that TAM significantly outperforms existing
Transformer-based methods in terms of accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studies the problem of modelling multi-object relationships for attention mechanisms. For this problem, they focus on incorporating object types into attention via proposing tensorized attention which uses Tucker decomposition to acquire attention weights across object types. Experiments on the Reddit dataset verifies the effectiveness.

### Strengths
The paper exhibits several strengths:

- The methodology section is clearly written with transparent details.

- In overall, the paper is well-written with few technical errors.

### Weaknesses
However, there are some small but significant drawbacks in the paper:

- The logic of the motivation seems confusing. E.g., the authors claim that computing transformer output from attention weights is not suitable for transforming from source object to different target object, but we can calculate multiple attentions for different source-target object pairs via using co-attention [1].

- The argument that BTD leads to overfitting because it uses more than two core tensors seems ad-hoc. It is similar to the argument because previous methods use more parameters, they suffer from overfitting.

- The experiments are incomprehensive. Executing the method on only one dataset is insufficient to assess its effectiveness.

[1] Actbert: Learning global-local video-text representations, CVPR 2020.

### Questions
Do you evaluate TAM on other datasets than the Reddit dataset?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The article presents a new attention mechanism for transformer architectures based on a tensor framework. The proposed tensor based method can incorporate multi-object relationships using Tucker decomposition. In particular, for the attention layer, along with the query Q and memory (key) K embeddings, a semantics embedding S is considered, and the attention mechanism is defined through a Tucker decomposition with a trainable core tensor G. Then an aggregation layer is used to convert the multi-dimensional attention tensor into a 2D matrix by summing up along the semantics axis. Several numerical results are presented an a Reddit dataset to illustrate the performance of the method compared to the standard attention and an alternate tensor attention mechanisms.

### Strengths
Strengths:
1. A new tensor based attention mechanism is proposed that can incorporate side information such as semantics and multi-wise interactions into the attention layers.
2. Tensor algebra is a natural approach to define multidimensional interactions and the proposed method modifies existing method to handle multi-way relations.
3. Numerical results show that the method yields promising results and outperforms previous methods.

### Weaknesses
Weakness:
1. Intuition behind the use of semantics in the attention layer is not clear.
2. Numerical results are on a single dataset.
3. The method might be incremental.

### Questions
The paper presents a tensor approach, that extends the previous work to account for multi-way interactions, and introduces semantics dimension to attention. This might be interesting in applications where there is natural multi-dimensional correlations such as videos, genetics and others.

I have the following comments about the paper:

1.  The intuition behind introducing the semantics information when defining attention, and what information does the 3rd order tensor capture are not very clear. There does not seem to be any activation function (say softmax) used after the Tucker product. Typically, the attention mechanism tries to capture key token to token interactions. Here, it is not clear that does the attention layer learn.


2. The paper presents interesting numerical results. However, there are few questions here. 
First, the exposition seems limited as only one dataset is considered with just 2 types of semantics. Are there other datasets or settings/applications where there might be natural multi-dimensional objects.
Second, the evaluation metric considered seems slightly different from other attention based papers,  where typically accuracy is considered. Perhaps R_{10}@1 is similar. Is there a reason why R_{10}@k is considered?
Next, in the results presented, it appears TAM has more #params than the standard BERT. Perhaps the performance gain is due to this. It would be interesting to see if standard attention would come close to TAM if similar #params are used. 
Lastly, why does TAM without semantics information perform better than standard BERT or tensorized attention?


Minor Comment:
i. Use \citep to get the standard citation form. Otherwise it results in double parentheses if (\cite{}) is used.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the Tensorized Attention Model (TAM), which leverages Tucker decomposition to calculate attention weights across various object types and seamlessly integrates them into the Transformer encoder. The authors evaluate TAM using the Reddit dataset and demonstrate that it significantly outperforms existing Transformer-based methods in terms of accuracy in response selection tasks.

### Strengths
1. The introduction of the Tensorized Attention Model (TAM) is a novel extension to the Transformer model that incorporates multi-dimensional attention mechanisms, enriching attention outputs by considering relationships across three or more distinct object types.

2. TAM innovates the tensorized transformer framework by employing Tucker decomposition for multi-object attention, enhancing accuracy through query-length-aligned tensor decomposition of key and value components, and reducing memory usage and overfitting through iterative averaging while maintaining accuracy.

3. The paper provides empirical validation of TAM's effectiveness by integrating it into a Transformer encoder and evaluating its performance in response selection tasks.

### Weaknesses
1. The paper focuses on measuring the impact of TAM's multi-dimensional attention within the encoder model, although TAM could theoretically be applied to both encoder and decoder models.

2. The paper does not provide a detailed comparison of TAM with other state-of-the-art methods in the field, which could help to better understand the advantages and limitations of the proposed approach.

3. The paper does not explicitly mention the application of TAM to other Transformer-based models, such as decoders.

### Questions
1. How does TAM compare to other state-of-the-art methods in terms of computational efficiency and memory usage?

2. Are there any potential applications of TAM in other natural language processing tasks, such as machine translation or question-answering?

3. Can TAM be applied to both encoder and decoder models in Transformer-based architectures?

4. What is the potential for scaling up the architecture to larger parameter sizes?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
