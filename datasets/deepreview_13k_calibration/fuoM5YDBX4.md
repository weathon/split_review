# Transformer Learns Optimal Variable Selection in Group-Sparse Classification

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Transformers have demonstrated remarkable success across various applications. However, the success of transformers have not been understood in theory. In this work, we give a case study of how transformers can be trained to learn a classic statistical model with "group sparsity", where the input variables form multiple groups, and the label only depends on the variables from one of the groups. We theoretically demonstrate that, a one-layer transformer trained by gradient descent can correctly leverage the attention mechanism to select variables, disregarding irrelevant ones and focusing on those beneficial for classification. We also demonstrate that a well-pretrained one-layer transformer can be adapted to new downstream tasks to achieve good prediction accuracy with a limited number of samples. Our study sheds light on how transformers effectively learn structured data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates one-layer transformers trained on specific dataset, where the input variables are generated from multiple groups, while the true label of this input is determined by variables from a single group. Based on these simplifications and assumptions, it theoretically demonstrates that the one-layer transformers can almost attend to the variables from the label-relevant group. Moreover, it provides a tight lower and upper bound for the population cross-entropy loss of a one-layer transformer trained by gradient descent. It also shows that the well pre-trained one-layer transformers can be efficiently transferred to a downstream task sharing a similar “group-sparse” structure and further provides an improved generalization error bound for one-layer transformers fine-tuned by SGD, which surpasses that of linear logistic regression applied to vectorized features. The numerical experiment observations support the theoretical findings.

### Strengths
The paper is well written and easy to follow. 

The theoretical analysis is thorough and the results align with the group sparsity assumption, although I did not check all the math and proof in detail.

In a sense, it provides new insights into sparsity analysis on the workings of attention based models.

### Weaknesses
(1) too much data assumption and model simplification. According to Definition 3.1, each patch x_j is i.i.d from Gaussian, and its label is determined from a given v (which can be learned from samples later). These data assumptions make group attention trivial. The assumption that each patch is drawn independently from a Gaussian distribution, combined with the label being determined by a single group, significantly simplifies the learning problem. This setup bypasses the complexities of real-world data where features are often correlated and labels are influenced by multiple factors. The independence of the input features makes it easier for the model to identify the relevant group, thus potentially overestimating the capabilities of the transformer in more complex scenarios.

(2) And the model is one-layer transformers, which may cannot capture attention-based models to a sufficiently satisfactory extent. With these simplifications, the contribution of this paper is limited, especially considering the pre-work from Jelassi et al. (2022). The use of a one-layer transformer, while simplifying analysis, does not fully capture the behavior of deeper, more complex transformer architectures. The interactions and hierarchical feature learning that occur in multi-layer transformers are not addressed, limiting the generalizability of the findings. The comparison to the work of Jelassi et al. (2022) highlights the incremental nature of this contribution, as it builds upon existing theoretical frameworks with a simplified model.

### Questions
the input x_j is concatenated with position encoding, does Theorem 3.2 still hold if using addition instead of concatenation?

### Soundness
3

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
This paper analyzes the variable selection of the Transformer theoretically.

### Strengths
The author presented a novel theoretical analysis on how the transformer can learn to select variables for the group sparse classification, which is interesting and novel.

### Weaknesses
1. Given your previous definition of the notations, pls define $\Theta$ in advance （otherwise people would get confused about this common notation.What is the 'variable' in the paper? Are they some features or some attributes of the data that define the label? What is the $v_1$ in the Thereom 3.2-2？ The weight corresponding to the label 1 or the value vector (output from value matrix in Transformer)？
2. The proof stretch should be placed in the Supplementary instead of the main paper. 
3. The experiments are conducted on synthetic data, however, in the higher dimensional images (e.g. 3*224*224), things would change. I have concerns on these too simple experiments. 
4. The Lemma 5.1, I do not see why the $W^{(T^*)}_{1,2}$ holds and $W$ is diagonal. In NLP, it seems that the feature is correlated to its position and would correspond to the output, is that a too strong assumption?
5. Can you show a more detailed demonstration on why the inequality of $\alpha^(T^*)$ holds (or is just a definition?) and why Lemma5.2 can be incorporated into Lemma 5.3? Also, I do not think Lemma 5.2. holds as the underlying assumption is the Transformer is naturally with low error. Lemma 5.2 is more like a strong assumption and definition to me. 
6. How you define the group sparse? What is this different from the standard classification?

### Questions
See weakness

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
3

### Summary
This paper investigates the theoretical understanding of transformers, which have shown success in various applications but lack a clear theoretical foundation. The study focuses on how transformers can learn a statistical model with group sparsity, where only a subset of input variables (groups) influences the label. The research shows that a one-layer transformer can use attention mechanisms to select relevant variables and ignore irrelevant ones for classification. Additionally, it demonstrates that a well-pretrained one-layer transformer can adapt to new tasks with limited samples and achieve good accuracy. This study provides insights into how transformers learn structured data effectively.

### Strengths
1. This paper investigates the theoretical understanding of transformers, an important and interesting problem that may greatly benefit the deep learning community.
2. This paper is well-written and has a good motivation.
3. The conclusion that a one-layer transformer can use attention mechanisms to select relevant variables and ignore irrelevant ones for classification makes sense to me.

### Weaknesses
1. Though the problem is interesting, the conclusion, a one-layer transformer can use attention mechanisms to select relevant variables and ignore irrelevant ones for classification, seems to be well-known in the deep learning community and has already been verified by the original paper (Attention Is All You Need).
2. The theoretical understanding of transformers given by this paper mainly focuses on the well-pretrained one-layer transformer. However, it will be much more interesting to study the multi-layer transformer since the scaling law shows that the loss of transformer scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude. 
3. The study focuses on how transformers can learn a statistical model with group sparsity, where only a subset of input variables (groups) influences the label. However, the concept of group sparse is not properly defined, making me confused to fully understand it. Further, what is a similar “group-sparse” structure as mentioned in the Introduction section? What kind of “group-sparse” inputs are similar?

### Questions
Please refer to the weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
3
