# The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction

- Decision: Accept
- Scores: 1, 3, 8

## Abstract
Transformer-based Large Language Models (LLMs) have become a fixture in modern machine learning.
Correspondingly, significant resources are allocated towards research that aims to further advance this technology, typically resulting in models of increasing size that are trained on increasing amounts of data. 
This work, however, demonstrates the surprising result that it is often possible to significantly improve the performance of LLMs by selectively removing higher-order components\footnote{Higher-order components are singular vectors with smaller singular values.} of their %
weight matrices. This simple intervention, which we call LAyer-SElective Rank reduction ($\intervention$), can be done on a model after training has completed, and requires no additional parameters or data. We show extensive experiments demonstrating the generality of this finding across language models and datasets, and provide in-depth analyses offering insights into both when $\intervention$ is effective and the mechanism by which it operates\footnote{Code and website: \href{https://pratyushasharma.io/laser/}{https://pratyushasharma.io/laser/}}.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
LLMs are usually considered “the larger the better”, but this paper presents a surprising result: it is often possible to improve the performance of LLMs by simply removing higher-order components of their constituent weight matrices in the MLP layers. This paper presents this rank reduction method, LASER, that removes the components in the {Q,K,V,O} matrices that have smaller singular values (i.e., those higher-order components).

This paper finds that the effects of reduction is not uniform across layers. The performance degradation can be found by reducing early layers, while significant performance benefits are available, often by pruning the later layers. This effect is the most obvious in the MLP output, and is also observable in the k, q, v matrices.

This paper further dives into studying what types of facts are recovered by rank reduction, and finds that the facts recovered on rank reduction are most likely those infrequently present in the data. 

Why are the higher-ordered components noisy? And what are the higher-ordered components computing? This paper approximates the final weight matrix using its higher-ordered components, and analyze how the model’s behavior changes on the datapoints that GPT-J’s lower-order components lead to incorrect outputs. They find that the model predicts incorrect entities of the same semantic type as the correct answer. As more lower-ordered components are included, the output changes to predicting common word tokens.

With additional experiments (on text domains including QA and non-text-domains including learning policies, images), this paper studies the generalizability of the findings.

### Strengths
- This paper is well-written and easy to read.
- The experiments are designed thoughtfully, and nicely supports the hypothesis.
- The findings are important for both the understanding and the developments of better models in the future.

### Weaknesses
I do not see obvious weaknesses in this paper. There is a typo: Table 3 needs a horizontal line at the bottom.

### Questions
Seems like the MLP layers are the key components in storing the noise vs storing the “useful inductive biases”. I wonder if some structural choices (e.g., different position embedding methods, different activation functions, number of heads, etc.) can affect Transformer’s low-rank vs high-rank component behavior as well.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work discussed a traditional idea, i.e. the low-rank approximation using SVD, for language model compression. Its major observation is that using a low-rank approximation on the MLP layer of transformers can even improve the downstream performance.
This observation is verified across different tasks and different transformer models.

### Strengths
-The use of low-rank approximation should be an effective and general way to allow the models to obtain more robust generalization abilities, while being more computationally efficient in the inference.
-The authors tried very hard to demonstrate the major observation by showing the results across different transformer models, which are actually not even for language modeling tasks.

### Weaknesses
Albeit the strengths above, I would like to say the major weakness of this work is that it draws its conclusion not very rigorously:
-Current LLMs are often evaluated from multiple aspects including their reasoning abilities such as commonsense reasoning, world knowledge, reading comprehension etc, as well as their language generation abilities such as multilingual ability etc. And each aspect contains well-known benchmark datasets for the evaluation, such as MNLU, AGIEval and BBH. However, this work uses none of them. Therefore, I am not convinced that this robust performance can be achieved across all the above-mentioned aspects.
-The authors do not provide the final search results of rank reduction, i.e. the layers selected for compressing and the reduced rank, in the final performance in Table1, 2 & 3. It is very important to provide these results to show that the selected model is indeed in a reduced rank.

### Questions
I find that the dimension of GPTJ is 4096, which should be $d$ in your notation. So in Fig2, what is the rank of Reduction 99.5%/99.75% and others with .5%? (4096*0.0025=10.24, not an integer?)

The used CounterFact is very similar to the table-to-text generation task (but for a qa task), which is not a frequently used dataset to test even the QA and factual/world-knowledge reasoning performance of LLM. Any reason for choosing the dataset?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a layer-selective rank-reduction method called LASER. The authors demonstrate that the performance in open-ended question answering is improved when rank-reduction is applied to the specific weight matrix. Moreover, they confirm consistent performance enhancements in tasks on non-text domains such as policy learning and image classification. Additionally, through analysis, it has been observed that high-order components contain factually incorrect knowledge which degrades question answering performance.

### Strengths
- The authors conduct extensive experiments with respect to layer number, parameter type, and rate reduction to identify setups that lead to performance improvement.
- The authors provide interesting observations such as a correlation between rank reduction and question answering accuracy.
- The authors demonstrate that the proposed method can also be applied to various domains such as image classification.

### Weaknesses
- Analysis on other text domain tasks such as reading comprehension could provide further insights.

### Questions
- In Figure 3(c), what is the number of originally correct and answer-corrected datapoints?
- It appears that there is a significant improvement in overall performance with GPT-J compared to LLama2 or Roberta. What could be the underlying cause of the result?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
