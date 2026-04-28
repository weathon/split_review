# Rule-Based Rating and Selection of LLM Training Data

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
The quality of training data is crucial for the performance of large language models (LLMs). There are recent studies utilizing LLMs to rate and select data based on scores from a small set of human-designed metrics (rules). However, existing rule-based methods often overly rely on human heuristics, lack robust metrics for rule evaluation, and exhibit limited adaptability to new tasks. In our work, we propose a novel rule-based framework that leverages the orthogonality of score vectors corresponding to rules as a unique metric for rule evaluation. Our method employs an automated pipeline that first uses LLMs to generate a diverse set of rules, covering a wide range of rating aspects. It then rates a batch of data according to these rules and applies the determinantal point process (DPP) from random matrix theory to select the most orthogonal score vectors,  effectively isolating a subset of independent rules. Then these rules are applied to rate all data and samples with the highest average scores are selected for further downstream tasks such as LLM training. We validate our method through two experimental setups: 1) comparison against ground truth ratings and 2) benchmarking LLMs trained with the selected data. Our extensive experiments span various settings, including general pre-training and domain-specific fine-tuning in fields such as IMDB, Medical, Math, and Code. The results show that our DPP rule-based rating method consistently outperforms other methods, such as rating without rules, uniform sampling, importance resampling, and QuRating, in terms of both rating accuracy and model performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a rule-based framework to rate and select samples for LLM training. The framework first generates a set of rules using GPT-4. Then, it uses the determinant point process (DPP) to select the most diverse subset from the previous set of rules based on the score vectors of a batch of randomly samples data. The selected rules are then used to rate and select data for LLM training. Experiments show the effectiveness of the proposed framework to some extent.

### Strengths
1. The authors are the first to introduce the mathematical rule evaluation metric, which is interesting and novel.
2. The motivation of  exploring DPP sampling for rules selection is technical sound.
3. The authors provide extensive experiments span various settings, including general pre-training and domain-specific fine-tuning in fields such as IMDB, Medical, Math, and Code
4. The paper is well-written and easy to follow.

### Weaknesses
1. The necessity of using an automated method to select some rules from the rule set is questionable, especially when the total number of rules is not large (N=50) and each rule is not long (see Tables 4, 5, and 13-16). In this case, the cost of manual rule selection is totally acceptable and manual selection is more reliable than automatic methods.
2. According to the experimental results in Table 1-3, the performance improvement achieved through DPP sampling appears to be somewhat limited. The authors may want to report the mean and standard deviation of the performance of different methods in multiple runs, and also provide a significance test.
3. Some important baselines are missing, such as LESS (ICML 2024) [1], IFD (ACL 2023) [2], SelectIT [3], DiverseEvol [4], ZIP [5], and InsTa [6]. The author should select as least two of latest data selection methods for comparison.
4. In Section A.6.6, the authors generate 10 uncorrelated rules using GPT-4 for Code and Math domains. I would like to suggest the author to add “GPT 10 Uncorrelated Rules” as a baseline in experiments in Section 5 to see the performance of models based on “GPT 10 Uncorrelated Rules”.
5. Some important analysis that could provide better insight to readers is missing as follows. (1) Why does “All 50 Rules” underperforms “DPP 10 Rules”? As claimed in Lines 489-493, the diversity in the data rating step can improve the model performance. According to this claim, the performance of “All 50 Rules” should exceed that of “DPP 10 Rules”, as the diversity of all 50 rules is obviously greater than that of the 10 selected rules. (2) What are the differences in the distribution of samples selected based on the selected rules?

### Questions
Please see the weaknesses for the details.
Overall, it is a good paper with some flaws. I will consider raising my score if the authors can effectively address my concerns.

### Soundness
2

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
4

### Summary
This paper introduces an automated method to improve the quality of training data for large language models (LLMs). Instead of relying on human-made rules, the authors use GPT-4 to automatically generate a wide range of data quality rules based on the specific task and dataset. They then apply Determinantal Point Processes (DPP) from random matrix theory to select a diverse and uncorrelated subset of these rules, reducing redundancy. By rating data samples according to these selected rules and choosing the best ones for training, they enhance the performance of LLMs across various tasks, such as sentiment analysis, medical knowledge, mathematics, and code generation. The method is fully automated, reduces human bias, and is adaptable to different domains, leading to better-trained models without manual intervention.

### Strengths
•	The authors use DPP to select rules that aren’t too similar, enhancing rule diversity. This approach enables the rules to assess data from different perspectives, improving data selection and ultimately boosting model performance.

•	They show that rule correlation value has a positive Pearson correlation with MSE, supporting the value of diverse rule selection. Furthermore, by comparing the results to randomly selected rules, they demonstrate that DPP can effectively identify these diverse rules, resulting in improved MSE.

•	The models trained with their selected data outperformed those trained with data chosen by other methods, such as DSIR, QuRating, and Random 10 Rules generated by GPT, demonstrating the effectiveness of their approach and using DPP for rule selection.

•	Their method is fully automated, removing the need for human-made rules, which makes it adaptable to various tasks. This automation allows it to be easily applied across different situations and domains, providing a flexible approach to data selection.

### Weaknesses
•	The reliance on LLMs like GPT for rule generation raises concerns about potential selection biases. Biases in the generated rules could lead to an overrepresentation or underrepresentation of certain types of data, which may impact the fairness and effectiveness of the data selection process. The authors should clarify how they are measuring the overlap between rule clusters produced by GPT and Claude, and provide additional details on the metrics or methods used to support their conclusion that there is no clear separation between the clusters.

•	The authors are encouraged to test their framework on larger models within the same family, such as LLaMA2-7B and LLaMA2-13B, to provide further evidence of its scalability and effectiveness. While the correlation between rule correlation and MSE is positive, it is not as high as the 0.6 mentioned in the paper, suggesting that the relationship might not be as strong as implied.

•	There are no experiments that single out DPP's effectiveness, leaving it unclear how much of the performance can be attributed to the LLM's capabilities versus DPP's role. The approach taken to compare against GPT-generated rules does not fully align with the proposed method. A more direct comparison would involve using GPT-4 to replicate DPP's role by adding a refinement step where GPT-4 filters and selects a subset of rules that are both highly relevant to the task and diverse. Without a baseline comparison using only GPT-4 for rule generation, the specific contribution of DPP remains uncertain, making it difficult to gauge its true impact within the framework.

•	To better understand the data distribution, the authors should analyze the distribution of the original dataset and the distribution of selected samples resulting from different selection methods, including DPP. Metrics such as the length of training samples, cross-entropy loss before fine-tuning, and cyclomatic complexity for coding datasets could provide insights.

### Questions
•	The authors should address potential selection biases introduced by GPT in rule generation, as biases in the generated rules could lead to an overrepresentation or underrepresentation of certain types of data. One way to assess this is by comparing the distribution of data selected using their method with the original data distribution. Additionally, comparing this distribution with that of baseline methods would provide insights into how their approach stands out in terms of bias mitigation.

•	The authors could consider using GPT-4 to perform DPP’s role by adding a refinement step that prompts GPT-4 to filter out and select a subset of r rules that are both highly relevant to the task and diverse, using a well-constructed prompt to achieve this. This refined subset could serve as a baseline for evaluating the effectiveness of the DPP alone. If the authors have already explored a similar approach, it would be helpful to clarify this and provide any reasons for choosing not to pursue it.

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
4

### Summary
The paper introduces an automated rule-based framework for selecting high-quality training data for large language models (LLMs) without human intervention. The framework utilizes LLMs to generate a diverse set of rules for data evaluation, addressing limitations in existing methods that rely on human-designed heuristics. It employs a determinantal point process (DPP) to select a subset of rules that are orthogonal, effectively reducing redundancy and bias in data selection. This method aims to improve data quality by rating and selecting data samples with the highest average scores, making it versatile across pre-training, fine-tuning, and RLHF tasks. The paper validates this approach through two evaluations: comparison with ground-truth ratings and performance assessment of LLMs trained with selected data, across domains like IMDB, Medical, Math, and Code. The results show that the DPP rule-based rating outperforms other methods, confirming its effectiveness in enhancing both rating accuracy and model performance.

### Strengths
1. The paper presents an automated rule-based framework for selecting high-quality LLM training data without human intervention. The model generates diverse rules for data evaluation, effectively eliminating human bias.
2. The method is flexible across various scenarios, including pre-training, SFT, and RLHF, and can be adapted to specific domains by modifying rule-generation prompts.
3. Extensive experiments covering different downstream tasks validate the approach. The detailed appendices further enhance the reliability of the results.
4. The rule evaluation metric focuses on score similarity rather than direct scoring, enabling measurement of rule diversity and adaptability to multiple domains and tasks.

### Weaknesses
1. Although the paper verifies the method’s effectiveness through extensive experiments, the proposed approach lacks significant innovation. Diversity-based selection and DPP for data selection are relatively common in prior work [1]. This paper’s difference lies in selecting rules rather than data directly. Citing related work and clearly distinguishing this approach from previous studies would strengthen the paper’s contribution.

2. The approach requires manual adjustment of prompts for different tasks and datasets, meaning that the effectiveness of the rules is limited by the accuracy of the prompts. It is also unclear how the descriptions of data and downstream tasks are generated. Additionally, the value of hyperparameter r is constrained by the value of R, and the paper does not clarify how to choose the optimal r. 

3. Rule quality is evaluated only by orthogonality/correlation, with no evidence that unrelated rule combinations are the most effective. Additional metrics would offer a more comprehensive assessment.

### Questions
None

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper solves the problem of choosing a subset of training data with better quality that can help in better finetuning or pre-training of the LLMs. The paper removes the need for human intervention in rule generation by automatically generating the rules using the LLM model itself. It also proposes a method to filter out rules from a large rule set to obtain diverse and independent set of rules. Overall it provides an automated solution to obtain a subset of training data for better training without any human in the loop.

### Strengths
1. The paper reduces the cost by removing the human experts for the creation of rules.

2. Paper has good amount of experiments that support the claims made in the paper.

3. The paper also introduces a robust rule-evaluation metric that promotes diverse and independent set of rules.

### Weaknesses
1. The paper is quite complex and might take some amount of effort to correctly implement. 

2. It depends heavily on LLMs such as GPT-4 which might not be an efficient approach for the resource constraint scenarios and require huge computational costs.

3. The cost of human in the loop is replaced by the cost of performing inference on the LLMs such as GPT-4 that should be considered, this is one major drawback of the paper and there should be an ablation study over that. There is a trade-off between cost of human in the loop and the cost of executing an LLM that needs to be explored.

### Questions
**See weaknesses.**

### Soundness
3

### Presentation
3

### Contribution
3
