# Re-Evaluating the Impact of Unseen-Class Unlabeled Data on Semi-Supervised Learning Model

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Semi-supervised learning (SSL) effectively leverages unlabeled data and has been proven successful across various fields. Current safe SSL methods believe that unseen classes in unlabeled data harm the performance of SSL models. However, previous methods for assessing the impact of unseen classes on SSL model performance are flawed. They fix the size of the unlabeled dataset and adjust the proportion of unseen classes within the unlabeled data to assess the impact. This process contravenes the principle of controlling variables. Adjusting the proportion of unseen classes in unlabeled data alters the proportion of seen classes, meaning the decreased classification performance of seen classes may not be due to an increase in unseen class samples in the unlabeled data, but rather a decrease in seen class samples. Thus, the prior flawed assessment standard that "unseen classes in unlabeled data can damage SSL model performance" may not always hold true. This paper strictly adheres to the principle of controlling variables, maintaining the proportion of seen classes in unlabeled data while only changing the unseen classes across five critical dimensions, to investigate their impact on SSL models from global robustness and local robustness. Experiments demonstrate that unseen classes in unlabeled data do not necessarily impair the performance of SSL models; in fact, under certain conditions, unseen classes may even enhance them.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates the impact of unseen classes in unlabeled data on the performance of semi-supervised learning (SSL) models. It challenges the prevailing assumption that unseen classes are detrimental to SSL performance, highlighting flaws in previous assessment methods that altered the proportion of unseen and seen classes simultaneously. This paper adheres to the principle of controlling variables by keeping the proportion of seen classes constant while varying unseen classes across five dimensions. Through rigorous experimentation, the authors demonstrate that unseen classes do not inherently degrade SSL model performance; in some scenarios, they may even enhance it. The findings suggest a reevaluation of the role of unseen classes in SSL, emphasizing that their effects are more nuanced than previously thought.

### Strengths
1. This paper effectively identifies a flaw in previous methods for assessing the impact of unseen classes on SSL model performance. By fixing the size of the unlabeled dataset and adjusting the proportion of unseen classes, earlier approaches fail to control for variables appropriately. This adjustment alters the proportion of seen classes, meaning that any decrease in classification performance for seen classes may not be solely due to an increase in unseen class samples, but rather to a decrease in seen class samples. This clarification helps refine our understanding of how unseen classes affect SSL model performance.
2. The experiments presented in this paper are thorough, as the authors control various variables to validate their claims from different perspectives. This comprehensive approach strengthens the credibility of their findings.
3. The writing in this paper is clear and easy to understand, making it accessible to readers.

### Weaknesses
1. In the proposed five metrics, some formulas are not clearly defined. For instance, the meaning of \(\hat{ACC}\) in Eq. 1 and \(\bar{ACC}\) in Eq. 2 is not explicitly explained. Providing clearer definitions for these terms would enhance the understanding of the metrics and their implications in the context of the research. Specifically, it's unclear whether \(\hat{ACC}\) refers to the accuracy on the entire test set or a subset corresponding to a specific value of 'r'. Similarly, the calculation of \(\bar{ACC}\) needs more detail: is it a simple average across all 'r' values, or is it weighted in some way? The lack of clarity makes it difficult to fully grasp the nuances of the proposed metrics and their ability to capture the impact of unseen classes.
2. In the tables, it would be helpful to use bold text or dashed lines to highlight specific data points, emphasizing the advantages of certain algorithms under particular settings. For example, if a particular algorithm consistently outperforms others under specific conditions (e.g., high proportion of unseen classes), highlighting these instances would make the results more accessible and impactful. The current presentation requires the reader to manually scan the tables to identify such patterns, which is not ideal.

### Questions
See Weaknesses

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
This paper studies the problem of safe semi-supervised learning. It found that the previous works are based on flawed evaluations, which did not adhere to the principle of controlling variables. They fixed the size of unlabeled data but change the proportion of unseen classes, which would also affect the proportion of seen classes. To deal with this problem, the paper proposes a re-evaluation framework to keep the proportion of seen classes unchanged and adjust the proportion of unseen classes. Furthermore, the paper also propose five metrics to comprehensively evaluate the impact of unseen classes. Based on the proposed framework, extensive experiments are performed to evaluate the impact of unseen classes on various SSL models.

### Strengths
1. The paper does not provide any new method. It gives an insightful perspective on the previous studies and finds that these methods have issues accurately assessing the impact of unseen classes. The motivation is very clear and seems to be reasonable. 

2. Based on the above motivation, the paper proposes to re-evaluate previous safe SSL models by fixing the proportion of seen classes. Furthermore, the paper proposes five evaluation metrics to access the impact of unseen classes on SSL models.

3. Extensive experiments based on the proposed framework are performed with various safe SSL methods. These results provide a comprehensive and fair comparison among existing methods.

### Weaknesses
The main contribution of this paper lies in proposing a more reasonable experimental setup; however, its major issue is the credibility of the experiments. The experiments are conducted solely on CIFAR-10 and CIFAR-100, which makes the results unconvincing. While I understand that past studies has primarily been conducted on these two datasets, given that this paper aims to make innovations from an experimental perspective, it should propose more practical experimental setups and conduct experiments on more realistic datasets.

### Questions
There are five evaluation metrics. Which one is the most important?

### Soundness
2

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
4

### Summary
The paper proposes an evaluation framework and then evaluates whether unlabeled samples from unseen classes deteriorate the performance of semi-supervised learning methods on seen classes.

### Strengths
**S1.** The motivation of the paper is valid and interesting.

**S2.** The proposed evaluation framework follows the principle of controlling variables by fixing the confounding factor, i.e. the proportion of unlabeled samples from visible classes. So, the proposed evaluation framework overcomes the shortcomings of current evaluation schemes.

**S3.** The influence of unlabeled samples from unseen classes is evaluated from five perspectives and five evaluation indices.

**S4.** Some representative methods are chosen for experiment and the experiment results can provide some guidance for understanding the working mechanism of existing methods and designing new ones.

### Weaknesses
In order to more clearly present the findings of the paper, the presentation needs to be further improved, specifically.

**W1.** Since $r$ (or $r_u$) is recorded in the tables in the experiment section, there is a precise definition for $r$. To reduce ambiguity, the formal definition of $r$ should be given based on the symbol system in Section 2. The current description lacks a clear mathematical definition, making it difficult to understand how the ratio is precisely calculated and applied within the experimental setup. For instance, it is unclear whether $r$ refers to a proportion of the total unlabeled data or a proportion of the unseen class data, and how this relates to the number of samples actually used in the experiments.

**W2.** It is necessary to provide a table or brief description for each indicator, showing its range, interpretation of positive/negative values, and how it relates to model performance. Without this, it is hard to interpret the results. For example, while $R_{slope}$ is mentioned, the reader needs to know what a positive or negative slope implies about the model's robustness. Similarly, the practical implications of high or low values for GM, WAD, BAD, and $P_{AD \geq 0}$ are not immediately clear and require a more detailed explanation.

**W3.** To facilitate readers to intuitively assess the degree of impact and facilitate cross dataset comparisons, the evaluation indicators in formulas (1)-(5) should to be normalized if possible. The current metrics, such as the slope of accuracy change ($R_{slope}$), are not normalized, making it difficult to compare results across different datasets or experimental settings. Normalization would allow for a more standardized interpretation of the impact of unseen classes on model performance, enabling a more direct comparison of the robustness of different methods.

**W4.** More experiment details should be recorded, such as the names of seen and unseen classes, the number of labeled samples for each class, and the number of unlabeled samples for each class. If there is not enough space, put it in the appendix. Furthermore, the authors should provide a link to their code or dataset splits, if possible, to further enhance reproducibility. The current description of the experimental setup lacks crucial details for reproducibility. Specifically, the exact classes used for seen and unseen categories, the number of labeled and unlabeled samples per class, and the specific data splits are not provided. This lack of detail makes it difficult to replicate the experiments and verify the findings. A link to the code and dataset splits would be essential.

**W5.** In addition, some clerical errors need to be corrected, specifically.

    a. In line 072, ”unseen classes in ---> “unseen classes in.

    b. In line 141, Fig.2(b) ---> FIg.2(a).

    c. In line 480-481, the table’s title should be above the table.

    d. In the experiment, how are the integrals in formulas (1) and (2) calculated? It seems that the integral operation should be the accumulation operation.

    e. In line 190, how can we obtain the “the expected accuracy”? In my opinion, it should be “the mean of ....”.

### Questions
I hope the authors can clarify the following question.

**Q1.**  As mentioned in line 269-299, there are three experiments (generated by three random seeds) for each kind of dataset construction. So, the experiment results given in the paper are still with high randomness. So, it is difficult to accept these conclusions derived from these experiment results. In order to dispel this doubt, the authors should strengthen the experiment from the following aspects.

    a. The number of datasets should be increased, e.g., 10 or more.

    b. The diversity of datasets should also be increased, rather than being limited to image datasets.

    c. For each dataset construction (labeled and unlabeled samples setting),  more experiments should be carried out, e.g., 10 times or more.

    d. Some statistical significance tests should be introduced.

**NOTE: I am willing to increase my rating to a 6 or 8, if the authors can dispel my doubts through more adequate experiments.**

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an evaluation framework for safe semi-supervised learning (SSL) with unseen class data. The paper observes that previous works fix the total number of seen and unseen class data, which may not reflect the true influence of unseen class data. Therefore, they fix the number of seen class data and change a number of quantities of unseen class data to investigate their influence. Extensive experiments are performed with much analysis.

### Strengths
- The shortcomings of previous evaluation approaches are new to the SSL field.
- Many experiments are performed, providing a solid and comprehensive evaluation for robust SSL.
- The experimental analysis is also very comprehensive.
- The paper is well written and easy to understand.

### Weaknesses
 - My main concern is the practicality of the framework. The main purpose of the paper is to test the influence of *increasing numbers* of unseen class data on the classification performance on seen class data. The proposed metrics are mainly *one-order statistics* of the classification performance, which show the change in performance with more unseen class data. However, the main interest of SSL with unseen class data in real-world applications may not be focused on one-order statistics. In real-world applications, we only care about the performance of a certain number of unseen class data instead of the performance change with more data, although many papers provide the figures with different numbers of unseen class data. Therefore, although the framework is valid for different sizes of unseen class data, the practicability for real applications may be limited.
- Only CIFAR datasets were used for experiments. Since previous SSL benchmarks provide more datasets from different modalities, such as text or tabular data, it is beneficial to consider more text and tabular datasets.
- The standard deviations of the experimental results should also be included.
- Some typos should be checked. For example, in Eq. (1), it should be argmin. In Line 431, it should be Table 5.

### Questions
- Are the experimental results in tables the average accuracies with multiple seeds?
- Is $C_{ib}$ the ratio between unseen and seen data?
- Is each entry in Table 6 the mean of several $C$, i.e. the mean of each row?

### Soundness
3

### Presentation
3

### Contribution
3
