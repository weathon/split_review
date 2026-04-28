# Polynomial-based Self-Attention for Table Representation learning

- Decision: Reject
- Avg Score: 6.33
- Scores: 5, 8, 6

## Abstract
Structured data, which constitutes a significant portion of existing data types, has been a long-standing research topic in the field of machine learning. Various representation learning methods for tabular data have been proposed, ranging from encoder-decoder structures to Transformers. Among these, Transformer-based methods have achieved state-of-the-art performance not only in tabular data but also in various other fields, including computer vision and natural language processing. However, recent studies have revealed that self-attention, a key component of Transformers, can lead to an oversmoothing issue. We show that Transformers for tabular data also face this problem, and to address the problem, we propose a novel matrix polynomial-based self-attention layer as a substitute for the original self-attention layer, which  enhances model scalability. In our experiments with three representative table learning models equipped with our proposed layer, we illustrate that the layer effectively mitigates the oversmoothing problem and enhances the representation performance of the existing methods, outperforming the state-of-the-art table representation methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In order to solve the over smoothing issue caused by the self-attention layer when applying a transformer to tabular data, this paper proposes Chebyshev polynomial-based self-attention. Firstly, inspired by graph signal processing, this paper considers the self-attention mechanism as a graph filter in the form of matrix polynomials and then uses finite degree Chebyshev polynomials to approximate the graph filter based on the PageRank algorithm. Experiments show that the method can effectively improve the performance of the base model without a significant increase in computation, and effectively alleviate the oversmoothing problems.

### Strengths
1)New ideas: This paper introduces the study of self-attention in the field of tabular data, effectively solving the oversmoothing problem.

2)Inspired new approaches: Inspired by graph signal processing and the PageRank algorithm, this paper utilizes matrix polynomials for optimizing the self-attention mechanism and uses Chebyshev polynomials to stabilize the training of coefficients.

3)Better experimental results: Experiments show that the base models, when combined with the approach in this paper, exhibit significant improvements in performance in downstream tasks such as classification and regression.

### Weaknesses
1）The motivation for the paper is not adequately supported by theory. The paper mentions that better flexibility and customization can be achieved by considering the self-attention mechanism as a graph filter in graph signal processing, but does not cite enough papers or theorems to fully convince this point. In addition, when proving that the self-attention matrix conforms to the three properties of the transition matrix required by the convergence of pagerank algorithm, the authors only make a rough qualitative analysis but do not carry out a more sufficient and detailed analysis and relevant theoretical or experimental proof. Specifically, the paper does not rigorously demonstrate that the self-attention matrix, which is dynamically generated during training, consistently maintains the properties of a stochastic matrix necessary for the convergence of the PageRank algorithm. The softmax function ensures non-negativity, but it's not clear if the row-sum to one constraint is always satisfied, especially considering the potential for numerical instability and the dynamic nature of the attention weights. Since the self-attention matrix in the transformer is unpredictable, once it does not meet the corresponding requirements, the self-attention based on matrix polynomials will not be able to approximate the graph filter, and thus will not be able to realize the expected results. Therefore, I suggest the authors to provide more details in this regard.


2）Some experimental data with excessive errors will interfere with the experimental results. In the experimental part, the error range of individual experimental results is too large relative to other data. For example, 70.9±13.90 in Table 2 and 58.1±24.32 in Table 3. When these margins of error are taken into account, it becomes a question which method yields the best experimental results. This may potentially interfere with the fairness of comparisons between different methods, thereby affecting the correctness of experimental results. The high standard deviations suggest that the experimental results may not be reliable, and the reported means may not accurately reflect the typical performance of the methods.


3）The applicability of CheAtt should be further discussed. The paper mentioned that the effect of CheAtt is very dependent on the quality of the base model. As can be seen from Table 1 and Table 4, in TabTransformer and MET, the effect of CheAtt is outstanding, but there is almost no improvement in SAINT. They are all table representation methods based on transformer, and the original performance of SAINT is the best among the three. So what exactly does the "quality of the base model" mentioned in the paper refer to? According to the author's analysis, self-attention based on Chebyshev polynomials can improve the flexibility of the self-attention mechanism. This improvement should not be strongly related to the base model, so do the experimental results mean that CheAtt is not applicable in many situations? I suggest that the authors conduct further analysis in this area.


4）The complexity of CheAtt still needs further discussion. First, the data in Table 5 are all in the range of a few milliseconds, does it refer to the time to generate output after the model training is completed? If so, this does not take into account the large number of matrix multiplication operations required during model training. In addition, it is meaningless to only compare the absolute time difference, and it is more convincing to compare the relative time consumption. It can be seen that in Phishing dataset, the additional time spent can exceed up to 40% of the original, which is a huge and unacceptable increase. Another question is why in the MET+CheAtt method and Phishing dataset, the time after using CheAtt is reduced (from 2.7538 to 2.4625). Is this a clerical error or real experimental data? I recommend the authors to perform a more comprehensive analysis and more realistic experiments in terms of computational complexity.

### Questions
Please refer to the weakness above. I combined my questions with the weakness presentation.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to improve the self-attention module with the matrix polynomial fashion, in order to deal with the over-smoothing issue in Transformer. The improved Transformer shows advantages in the task of understanding tabular data. The proposed polynomial-based layer, namely CheAtt, enables Transformer performs well with good efficiency due to the less-token nature of tabular data.

### Strengths
The paper is well written. The motivation is clear, and the proposed solution is reasonable. The experiments validate the effectiveness. The inherit issue of computational efficiency of polynomial-based layer is avoided in the task of tabular data understanding. Anyway, as far as I know, this is compatible to the current mainstream accelerating techniques.

### Weaknesses
It is better to present more details about the task of tabular data understanding.

### Questions
As I have limited experience in dealing with the tabular data, could the authors provide if any existing method tackling the issue of over-smoothing for this task?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a polynomial-based self-attention layer that enhances the representation performance of existing methods for tabular data. The experiments are thorough and convincing, showing that the proposed layer outperforms state-of-the-art methods. However, the paper lacks a detailed analysis of the computational complexity of the proposed layer and a thorough comparison with other recent approaches. Additionally, it is recommended to improve the presentation of results by adding arrows to the indicators in the charts and to test the scalability of the layer on larger datasets or more complex models.

### Strengths
1.The paper is well-written and the experiments are thorough and convincing.
2.The paper proposes a novel self-attention layer that enhances the representation performance of existing methods for tabular data. The experiments show that the proposed layer outperforms state-of-the-art methods.

### Weaknesses
Lack of detailed analysis of computational complexity. Inadequate comparison with other recent approaches. Presentation of results could be improved. Unclear scalability to larger datasets or more complex models.

### Questions
To further improve the quality of the manuscript, here are several suggestions:

1. The paper does not provide a detailed analysis of the computational complexity of the proposed matrix polynomial-based self-attention layer.
2. The paper does not provide a thorough comparison of the proposed approach to other methods for addressing the over-smoothing issue in Transformer-based methods for tabular data. While the experiments show that the proposed layer outperforms state-of-the-art methods, it is unclear how the proposed approach compares to other recent approaches in the literature.
3. It is recommended to add up or down arrows to the indicators in the chart, such as such as Table 2, Table 3, Table 4, and Table 5.
4. The experiments show that the layer is effective. While data set used in the experiment is small, it is unclear how the layer would scale to larger datasets or more complex models. It is recommended to increase the results of testing on large data sets.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
