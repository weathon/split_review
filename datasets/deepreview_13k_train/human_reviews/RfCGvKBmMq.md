# Representation Matching Information Bottleneck for Text Matching in Asymmetrical Domains

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
Recent studies have shown that the domain matching of text representations will help improve the generalization ability of asymmetrical domains text matching tasks. This requires that the distribution of text representations should be as similar as possible, similar to matching with heterogeneous data domains, in order to make the data after feature extraction indistinguishable. However, how to align the distribution of text representations remains an open question, and the role of text representations distribution alignment is still unclear. In this work, we explicitly narrow the distribution of text representations by aligning them with the same prior distribution. We theoretically prove that narrowing the distribution of text representations in asymmetrical domains text matching is equivalent to optimizing the information bottleneck (IB). Since the interaction between text representations plays an important role in asymmetrical domains text matching, IB does not restrict the interaction between text representations.  Therefore, we propose the adequacy of interaction and the incompleteness of a single text representation on the basis of IB and obtain the representation matching information bottleneck (RMIB). We theoretically prove that the constraints on text representations in RMIB is equivalent to maximizing the mutual information between text representations on the premise that the task information is given. On four text matching models and five text matching datasets, we verify that RMIB can improve the performance of asymmetrical domains text matching.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors apply information bottleneck theory in asymmetric text matching to improve latent text code quality. The challenge in asymmetric text matching is finding the mapping from two distinct text distributions (e.g. questions and answers) to a common latent vector space.

### Strengths
Clear experiments and results.

### Weaknesses
weaknesses are adequately discussed by the authors.

### Questions
In the Interaction, we maximize I(z1;z2). This makes sense for positive and negative examples, but do we want to maximize I(z1;z2|Y=neutral)?

### Soundness
3 good

### Presentation
3 good

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
In this paper, the authors propose to align representations of texts from asymmetric domains for better matching performance. Specifically, the authors leverage the information theory to show the alignment solution is not only narrowing the distributions, but also equivalent to optimizing the information bottleneck.  Several proofs are also given to support the proposed ideas. Experiments on several benchmark datasets demonstrate that the proposed method outperforms the previous work DDR-MATCH. An ablation study also shows that it is beneficial to add both interaction and inadequacy to information bottleneck.

### Strengths
* S1: The paper has strong theoretical supports by having proofs from the view of information theory.
* S2: Experiments demonstrate the significant gains over the baseline with different embedding models.

### Weaknesses
 * W1: While most of the method descriptions are in the form of information theory, the actual model architecture deployed in the experiment should be also clarified. Some comparisons to baseline methods should be also conducted, otherwise we might not know if the gain is from the proposed idea or simply because of other factors like more model parameters. Specifically, the paper lacks details on how the information bottleneck is implemented within the model architecture. It's unclear how the interaction and inadequacy terms are incorporated into the loss function and how they affect the model's training dynamics. Without this level of detail, it is hard to assess if the performance gains are from the proposed information-theoretic approach or from other architectural choices or training strategies. Furthermore, the paper should include a comparison with baseline models that have a similar number of parameters, to ensure that the performance gains are not simply due to increased model capacity.
* W2: Lack of comparisons to other representation alignment methods, such as [a,b,c,d]
* W3: With the same encoder, the representations are to some degree still in the same domain. The real asymmetric setup (like [d]) with different encoders or even different data types should be considered in the experiments.

### Questions
* Q1: Many gains are huge in terms of values. I wonder if the authors conduct significance tests to have verification.
* Q2: Following W2, I wonder if the authors can compare with more representation alignment methods during the author feedback period.
* Q3: Following W3, the proposed method actually does not use any property about text, so theoretically it can be applied in representations of arbitrary data formats. I wonder if there could be some experiments on multi-modal settings.
* Q4: In Table 1, it is interesting that the proposed method improves a lot in `SICK`, but also significantly underperform DDR-Match in `SNLI`. I wonder if the authors have conducted analysis to research this phenomenon.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates text-matching tasks in asymmetrical domains from the perspective of information bottleneck theory. It demonstrates that narrowing the distribution of text representations in asymmetrical domains text matching is equivalent to optimizing the information bottleneck. Furthermore, it extends the conventional information bottleneck approach to a novel framework called Representation Matching Information Bottleneck (RMIB). The theoretical justification of the proposed RMIB method is provided, and empirical evidence is presented to show its effectiveness in improving model performance for text retrieval and matching tasks.

### Strengths
1. The proposed RMIB method offers a reasonable improvement to the information bottleneck approach by considering the practical aspects of text-matching tasks. It captures unique factors within text-matching tasks, such as the interaction between text representations and the limitations of a single text representation. These ideas demonstrate a certain level of innovation.
2. The methods presented in the paper are accompanied by clear theoretical proofs.
3. Building on the theoretical analysis, the effectiveness of RMIB is further validated through empirical experiments. Special cases in the experiments are also analyzed and explained.
4. The paper exhibits a well-structured hierarchy and a clear line of thought, making it highly readable.

### Weaknesses
1. The paper contains errors in the tables presenting experimental results. While the experiments are described as "F1 values on SICK," the tables do not include the F1 metric for SICK. Additionally, based on the information provided in "3.1 DATESET AND METRIC," it seems that the dataset metrics don't mention the F1 score.
2. The proof for Proposition 4 in the paper is somewhat perplexing, and the meaning and proof process for Theorem 4 are not well understood. Moreover, there is an error in Equation (67) within the proof of Proposition 4.
3. The method needs to set three hyperparameters, which could be limiting in practical applications. The author acknowledges this limitation in the paper.

### Questions
1. According to "3.1 DATASET AND METRIC," why do SICK and SciTail have F1 metrics, and why do the tables of experimental results not align with the F1 metric as described in the experiments?
2. Regarding the proof of Theorem 4: Can we directly derive equation (68) based on a Markov chain, and why are equations (66) and (67) necessary? My knowledge in this field is limited, so I seek your understanding if I have misunderstood.
3. How does equation (68) directly lead to the conclusion, and can this step be explained in more detail?
4. I'm not quite sure how to implement the objective function using code. How do I calculate the KL divergence between a Gaussian distribution and the distribution of text representations?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the issue of aligning text representations in asymmetrical domains to improve text matching performance. It introduces RMIB framework, which narrows the distribution of text representations and emphasizes the importance of interaction between text representations. The paper theoretically proves that optimizing the RMIB is equivalent to maximizing the mutual information between text representations given the task information. The contributions include proposing RMIB, providing its theoretical foundation, and demonstrating its effectiveness on various text matching models and datasets.

### Strengths
The paper presents an extensive experimental evaluation, including detailed results across various datasets, demonstrating the significant improvements achieved through the RMIB framework. The inclusion of a range of evaluation metrics adds robustness to the assessment of the RMIB framework's performance in diffferent text matching tasks. The paper offers a strong theoretical foundation, showcasing the equivalence between text representation distribution narrowing and information bottleneck optimization, thereby reinforcing the validity and relevance of the proposed RMIB framework.

### Weaknesses
How the authors performed statistical significant test for Table 2? The analysis primarily focuses on scenarios with limited data availability, and the paper lacks a comprehensive exploration of the RMIB framework's effectiveness in highly heterogeneous data matching scenarios. Specifically, the paper does not address the potential for the RMIB framework to overfit to the specific characteristics of the datasets used, especially given the relatively small size of some of the datasets. Furthermore, the need for manual hyperparameter tuning within the RMIB optimization process might restrict its applicability to diverse text matching tasks. The paper does not provide a clear methodology for selecting optimal hyperparameters, and the sensitivity of the framework to different hyperparameter settings is not thoroughly investigated. Future research should aim to automate the hyperparameter selection process to enhance the framework's adaptability and scalability. While the results demonstrate the effectiveness of the RMIB framework, further comparisons with state-of-the-art models on a broader set of text matching tasks, including those with more substantial data and greater domain diversity, would strengthen the paper's conclusions and provide a more comprehensive understanding of the framework's capabilities and limitations.

### Questions
How the authors performed statistical significant test for Table 2?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
