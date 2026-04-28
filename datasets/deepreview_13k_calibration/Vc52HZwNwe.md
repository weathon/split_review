# Gradient-free Proxy for Efficient Language Model Search

- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 5, 8, 5

## Abstract
The rising demand for efficient natural language processing (NLP) systems has underscored the significance of developing lightweight language models. However, prevailing approaches to neural architecture search (NAS) often confront issues such as biased evaluation metrics and computational inefficiencies. This paper introduces weight-weighted PCA (W-PCA), a novel zero-shot NAS method specifically tailored for lightweight language models. Our approach leverages two evaluation proxies, namely parameter count and principal component analysis (PCA) value of the feed-forward neural (FFN) layer, to provide a comprehensive and unbiased assessment. Additionally, by eliminating the need for gradient computations, we optimize the evaluation time, thereby enhancing the efficiency of designing and evaluating lightweight language models. Comparative analysis on the GLUE and SQuAD datasets demonstrates that our approach not only significantly reduces training time compared to one-shot NAS methods but also achieves higher scores in the testing phase compared to previous state-of-the-art training-based methods. Furthermore, ranking evaluations on a dataset sampled from the FlexiBERT search space reveal that our approach exhibits superior ranking correlation and further reduces solving time compared to other zero-shot NAS methods that require gradient computation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
As the model size of large language models continues to increase, the development of lightweight language models becomes increasingly significant. While neural architecture search (NAS) is commonly used for this purpose, it often encounters biased metrics and inefficiencies. This paper introduces two evaluation proxies, specifically parameter count and principal component analysis (PCA) value, which eliminate the need for gradients and enhance efficiency. Experiments conducted on GLUE and SQuAD demonstrate the effectiveness of this approach.

### Strengths
1. The proposed algorithm significantly enhances the search efficiency of NAS.
2. The models discovered through this method outperform other baseline methods in GLUE and SQuAD benchmarks.
3. The visualization of the correlation between principal component analysis (PCA) and the number of parameters (#params) rankings helps interpret the effectiveness of the paper.

### Weaknesses
1. The paper primarily focuses on experiments with the BERT model, and it would be beneficial to conduct more experiments on other types of language models, such as generative models or larger-sized models, to ascertain the method's applicability. Specifically, the method's effectiveness on models with significantly different architectures and training procedures, such as those used in large language models, remains unclear. The current scope limits the generalizability of the findings.
2. A more in-depth discussion of the proposed method is needed. It would be beneficial to conduct ablation studies to assess the impact of each loss term, considering that multiple loss terms are included in the fine-tuning process. The paper lacks a detailed analysis of how each component of the W-PCA contributes to the overall performance. It is unclear whether the parameter count or the PCA value is more important, or if their combination is crucial. A more granular analysis is required to understand the method's inner workings.
3. The differences in training datasets and objectives compared to previous works make it unclear whether the improvement stems from the searched architecture or other factors. The paper does not adequately control for these differences, making it difficult to isolate the impact of the proposed architecture search method. It is essential to compare the performance of the searched architecture with other architectures trained on the same datasets and with the same objectives to ensure a fair comparison.
4. The improvement observed in GLUE and SQuAD is described as marginal. The reported gains are not substantial enough to justify the complexity of the proposed method. The paper needs to provide a more compelling argument for the practical significance of the achieved improvements, especially considering the computational overhead of the search process.
5. This article requires significant improvement in writing and formatting. The misplaced tables contribute to a lack of clarity in the paper's presentation, such as in section 6.3. The overall presentation of the paper is disorganized, making it difficult to follow the arguments and understand the results. The tables are not well-integrated into the text, and the figures are not always clear.

### Questions
1. Could you provide information regarding the zero-shot performance of the searched model? Additionally, I'm interested in learning about the performance of architectures discovered using W-PCA with different parameters.
2. Have you conducted experiments with multiple shots and employed an iterative searching strategy for multiple shots searching?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a zero-shot neural architecture search method for selecting lightweight language models. The method involves leveraging two evaluation proxies - parameter dimension and eigen/spectral values. This methodology enables faster throughput of evaluating and selecting lightweight language models via gradient free computations. Evaluation on the GLUE benchmark shows higher scores as compared to previous state-of-the-art methods.

### Strengths
1. Zero-shot NAS enables faster searching of the models 0.5d as compared to > 50d using other approaches.
    
2. Competitive results against multiple baselines.

### Weaknesses
1. The paper is convoluted and difficult to understand. Multiple sections need to be written again. Kindly see Questions/Comments.
    
2. Table 5 results are close to each other. Thereby showing that the weight-weighted version might not improve the results too much as compared to Vanilla. A deeper qualitative analysis is required to establish the usage which is missing in the current version of this work.

### Questions
1. The first two lines of the abstract are not well connected. Kindly reframe the abstract to highlight the motivation and contribution better
    
2. Abstract: Unbiased assessment of what?
    
3. Section 1. 3rd last paragraph - “potentiallly overlooking important characteristics”. What are these important characteristics?
    
4. Section 2.2 mentions primitive operators - What are these?
    
5. Section 2.3: Include year with the citations.
    
6. Section 2.3: Inconsistent notations throughout this section - N is parameters, as well as batch size in this section. This section needs to be written better to make the reader understand the motivation for using each of the metrics, instead of just writing the formulation.
    
7. Section 3: Kindly mention how PCA_dim is calculated using equations, and how the threshold serves as the lower/upper limit for deciding the principal components. Explicitly call out hidden_dim = dimension of the hidden layer after before applying FFN.
    
8. Why is the scaling of hidden_dim needed ?
    
9. Equation 4: Notation writeup should be improved currently it looks like PCA(X) subtracted from W.
    
10. Section 5.1: Kindly include the details of the appendix section of Serianni & Kalita. Each paper should be a standalone read.
    
11. Section 6.2.1: Details of the genetic algorithm being used is missing here. Kindly include it here or the appendix.
    
12. Section 6.2.3: KD Loss - $\mathcal{L}^i_{attn} = \text{MSE}(\mathbb{A}^{S}*i\mathbb{W}a, \mathbb{A}^T*j).
    
13. Section 6.2.3: KD Loss - “jth teacher model layer corresponds to ith student model layer” - How do we get this correspondence?
    
14. Conclusion: Kindly mention some quantitative metrics here. In the current version it looks like a paraphrase of the abstract.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors aim to address these limitations and improve the applicability of zero-shot NAS. As prevailing approaches to NAS often confront issues such as biased evaluation metrics and computational inefficiencies, the authors proposed w-PCA (given an observed strong correlation in ranking between PCA and the # of parameters (#params), with their product demonstrating even better performance) to better and more inclusively consider both the model parameters count and PCA values. Combining these two aspects, w-PCA shows significantly smaller training time compared to 1-shot NAS, while achieving higher scores in the testing phase compared to previous SOTA training-based methods.

### Strengths
1. The proposed method (w-PCA) achieved significantly smaller training time compared to 1-shot NAS
2. w-PCA achieving higher scores in the testing phase compared to previous SOTA training-based methods on GLUE and SQuAD datasets
3. Concluding experiments on two widely used NLU datasets & detailed analyses of the results are provided
4. First work that applies 0-shot NAS to NLU tasks
5. Details of the implementation (in the main text and appendix A), making comprehension easier, and reproducibility as well

### Weaknesses
1. The method struggled in performance on the GLUE & SQuAD datasets (e.g. BERT-base* performed the best, even if it is by a 2-point margin). Do you have any idea why?

2. Does the work scale? It would have been nice to discuss the limitations of this approach. For instance, I see this approach to be useful in resource constraint settings e.g. low-resource scenarios but the datasets used cover very few to none of such languages. It would be great to have it included to see to which extent this could benefit extremely constrained environments

3. What should be the trade-off between training time, the weight of the obtained model, and the performance? i.e. how much decrease (worse case) in performance could we "sacrifice" for how many # of parameters and how much time should/could?

4. Not related to the PCA necessarily but to the idea of reduction - have you tried or explored working in latent space?

### Questions
See Weaknesses

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work introduces a novel zero-shot NAS method, called as weight-weighted PCA (W-PCA), designed to efficiently explore lightweight language models within a teacher-student network for knowledge distillation. The method harnesses the parameter counts and principal component analysis (PCA) values of the feed-forward neural (FFN) layer, instead of relying on gradient metrics, to offer a comprehensive and impartial evaluation. In experimental trials, this approach demonstrates the ability to significantly reduce training time when compared to previous one-shot NAS methods.

### Strengths
This work presents a zero-shot NAS method that:
1. Identifies significant dimensions that contribute to the performance.
2. Reduces the need for extensive backpropagation and derivative calculations and requires only forward propagation during the evaluation of candidate architectures.

### Weaknesses
 1. The novelty may be limited, as the proposed method has not provided a comprehensive and robust architectural design guideline or led to the discovery of an efficient and universally applicable architecture. The use of PCA on FFN layers, while offering a different perspective, doesn't inherently guarantee the discovery of novel architectural insights beyond what is already achievable with existing NAS methods. The method's reliance on parameter counts and PCA values, instead of gradient-based metrics, might overlook crucial performance factors that are captured by backpropagation, such as the interplay between different layers and the impact of activation functions.
2. Tables 2 and 3 demonstrate only modest performance improvements with W-PCA in comparison to baseline methods, with exceptions on a few datasets. This might raise questions about the overall effectiveness of the proposed method. The reported gains are not consistently significant across all datasets, suggesting that the method's effectiveness may be highly dependent on specific dataset characteristics or model configurations. The lack of substantial improvements, coupled with the absence of a clear theoretical justification for using PCA in this context, makes it difficult to ascertain the practical utility of the proposed approach.

### Questions
1. “By considering the PCA values, we can identify dimensions that contribute the most to the architecture’s performance, allowing for informed decision-making during architecture search.” How will the dimensions benefit the architecture search?
2. Are there any particularities of the architectures searched by your method?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
