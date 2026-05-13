# AutoGeTS: Automated Generation of Text Synthetics for Improving Text Classification

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
When developing text classification models for real world applications, one major challenge is the difficulty to collect sufficient data for all text classes. In this work, we address this challenge by utilizing large language models (LLMs) to generate synthetic data and using such data to improve the performance of the models without waiting for more real data to be collected and labelled. As an LLM generates different synthetic data in response to different input examples, we formulate an automated workflow, which searches for input examples that lead to more "effective'' synthetic data for improving the model concerned. We study three search strategies with an extensive set of experiments, and use experiment results to inform an ensemble algorithm that selects a search strategy according to the characteristics of a class. Our further experiments demonstrate that this ensemble approach is more effective than each individual strategy in our automated workflow for improving classification models using LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the use of synthetic generations for retraining classification models with augmented data. The authors’ main contribution is through a selection pipeline for examples from the training set to be used in synthetic augmentation. They demonstrate their methodology through controlled experiments on class imbalanced settings.

### Strengths
- The paper demonstrates a good level of technical descriptions for experiments, definitions and results.
- Experiment setups are elaborate and controlled across different aspects of the selection methodology and throughout the retraining pipeline.
- Elaborate presentation of overall and class-specific performance results.
- The appendix is appreciated, especially the inclusion of baseline results and PCA experiments for synthetic correctness.

### Weaknesses
 - A major issue for me is the lack of detail about synthetic generation in the main paper, this is an integral part of your contribution and yet it seems to be lacking in experimentation and presentation. 
- There seems to be a major focus on the selection process but not as much exploration for the improvement of generation prompts/pipelines given these selections, in fact, according to the appendix, the synthetic generation prompt seems to be very vanilla, with little prompt engineering or any measures to maintain diversity or even any experimentation on the later. The lack of entropy injection or verification in the prompt could present an issue with generalizability and scale, these issues need to be addressed as part of synthetic pipelines not only with post-hoc checks.
- Section 5.2 could use further detail on how you obtain the order of classes optimized for R1 and R2 measures as well as relevant classes for ICs in R3, this is a difficult and important part of the problem and it would’ve been helpful if it was discussed further in the main paper.

### Questions
- Have you experimented with more models for generation?
- Have you performed any human annotations on a sample of your synthetic data in order to identify potential issues with diversity and correctness (is new data in fact in line with prompt examples)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the text classification task by exploring text data synthesis, which is especially useful to solve the data scarcity issue for long-tail classes. This paper specifically studies how to select demonstrations for generating synthetic data. Three approaches are proposed to select examples from a embedding space of existing data samples, including a naive traversal of embedding space with static sliding windows, hierarchical top-down search, and a generic algorithm to iteratively update the selection. Experiments results mainly shows that the data synthesis method can significantly improve model performance on the infrequent classes.

### Strengths
- This paper proposes three alternative methods for example selection from an embedding space to synthesize text data. Experiments compare these methods and their combinations to show their strength
- The proposed data synthesis method significantly improves classification performance on small-size classes, which shows the motivation of the paper
- Comprehensive experiments are conducted to compare the proposed three alternative methods and their combinations on different types of classes
- The paper overall is clearly written and easy to follow

### Weaknesses
 - Only one dataset with skewed distributed classes are used. More datasets could be beneficial to show the generalizability of the method
- In the experiments, the proposed data synthesis methods are only compared with the baseline classifier. However, there should be a baseline with a "naive" example selection method such as random or using local density. I expect such a method is also effective to improve performance on rare classes and the performance increment of the proposed method may be marginal.
- The presentation of experiment results is hard to read. The numbers are too compact and hard to directly see the comparison. The figures have too many small fonts and cannot easily see the content. Some major revision here should be necessary.

### Questions
See the first two weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a framework for using synthetic data generated by LLMs to improve text classification tasks, particularly for low-frequency classes, without the need for human intervention. They address the challenges of limited data for underrepresented classes with the framework of automatic selection. They explored three methods for selecting inputs, which are sliding window (SW), hierarchical sliding window (HSW), and genetic algorithm (GA). The methods target specific objectives, for example, class recall, class-based balanced accuracy, overall balanced accuracy, or F1-score. Experimental results showed that HSW is effective for larger classes and GA performs well for smaller and mid-sized classes. They also proposed an ensemble algorithm that combines these methods to further improve performance.

### Strengths
- The paper introduces a framework that addresses the real-world challenges of class imbalance in text classification, a common issue in industrial applications, by leveraging synthetic data from LLMs to improve performance in low-frequency classes. The framework automates the selection of inputs for synthetic data generation, reducing the need for domain expertise.

- The paper tested three different strategies to gain insights into which methods work well under various conditions. Also, they considered ensemble algorithm for further improving performance.

### Weaknesses
 - The paper evaluates their proposed framework on only a single dataset, which limits the demonstration of AutoGets's effectiveness in other domains.  Additionally, the absences of baseline comparisons, for example, traditional data augmentation techniques, makes it challenging to fully understand the advantages of AutoGeTs. While HSW and GA methods are intended to reduce computation costs, further analysis is needed to determine how computational demands scale with larger datasets, as real-world industrial applications typically involve substantial data volumes.

### Questions
.

### Soundness
3

### Presentation
2

### Contribution
3
