# Multimodal Banking Dataset: Understanding Client Needs through Event Sequences

- Decision: Reject
- Scores: 6, 8, 3, 5

## Abstract
Financial organizations collect a huge amount of data about clients that typically has a temporal (sequential) structure and is collected from various sources (modalities). Due to privacy issues, there are no large-scale open-source multimodal datasets of event sequences, which significantly limits the research in this area.
In this paper, we present the industrial-scale publicly available multimodal banking dataset, MBD, that contains more than 1.5M corporate clients with several modalities: 950M bank transactions, 1B geo position events, 5M embeddings of dialogues with technical support and monthly aggregated purchases of four bank's products. All entries are properly anonymized from real proprietary bank data. Using this dataset, we introduce a novel benchmark with two business tasks: campaigning (purchase prediction in the next month) and matching of clients. We provide numerical results that demonstrate the superiority of our multi-modal baselines over single-modal techniques for each task. As a result, the proposed dataset can open new perspectives and facilitate the future development of practically important large-scale multimodal algorithms for event sequences. 

 HuggingFace Link: \url{https://huggingface

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
1. The paper introduces a new dataset, Multimodal Banking Dataset which integrates multiple modalities for over 2 million corporate clients.
2. The authors highlight the potential applications of this dataset for campaign planning and client behavior analysis, using multimodal benchmarks to demonstrate its value along with baseline model implementation.

### Strengths
1. The work releases a first large scale banking dataset for public availability for financial applications. 
2. The authors present a good benchmark comparing unimodal and multimodal methods across various predictive tasks. The experimental protocol and metrics are clearly laid out as well.

### Weaknesses
1. The authors do not explore or discuss advanced multimodal sequence models or advanced fusion techniques' cross-attention mechanisms as they can better capture interactions across modalities. They mention it at the end as a scope for future work.
2. Though authors discuss using AUC ROC as their metric for mitigating label imbalance issues for example in their campaigning downstream task, they do not discuss or incorporate any additional techniques for handling the label imbalance.
3. Details about anonymization techniques applied are mentioned in the paper but it lacks quantitative evaluation of the impact of these techniques on temporal dependencies within the data.

### Questions
1. Is there a plan to expand the set of downstream tasks in future work? Highlighting a larger application list can increase the dataset's appeal across different financial research areas.

Please look into the weakness section for other questions.

### Soundness
3

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
This is not a research contribution per se but it is a dataset paper.

The paper presents the first large-scale multimodal banking dataset for the user community. It offers a new dataset that has millions of users and millions of transactions that have been suitably anonymized. Moreover, the authors have provided baselines for a few standard tasks. The dataset will be released in order to spur research in the use of machine learning for banking applications.

### Strengths
(1) This will be first and the largest multimodal banking dataset that will be released. This can potentially be tremendously useful to the research community.

(2) The baseline methods and benchmark data for a few problems outlined will also be immensely useful to the research community.

### Weaknesses
(1) The details of the data are somewhat sparse. More details of each type of data will be useful to the reader. Perhaps this article may be useful for improving this aspect of the exposition in the paper:

https://cacm.acm.org/research/datasheets-for-datasets/

(2)  Can some details of the anonymization be provided without compromising on the privacy of the customers? That can help estimate the errors of any model developed using this data.

(3) The data has been collected during the pandemic period? Will it have any effect on any of the conclusions drawn using the data? For examples, could this lead to systemic under-estimation or over-estimation of any phenomenon? Ideally, it would be useful to have another data-set which is outside of the pandemic period - perhaps the second version of this data set? This can serve as a basis for many natural experiments.

### Questions
(1) Will the dataset be openly downloadable or will the authors be controlling the access? Openly downloadable option is obviously preferable.
(2) Will the source code of the bench-marking studies be openly available? 
(3) it will be useful to the community if the set of relevant real-world problems could be articulated that can inspire researchers to work on this dataset. Especially, in order to attract young researchers into the field.

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces a large-scale publicly available multimodal banking dataset (Multimodal Banking Dataset, MBD). The MBD contains data from over 2 million banking customers, covering four different modalities: 9.5 million banking transaction records, 1 billion geographic location data points, 5 million customer interactions with technical support embedded dialogues, and banking product purchase activity over a 12-month period. This dataset provides researchers with a rich resource for analyzing customer behavior dynamics and contributes to the development of large-scale multimodal event sequence algorithms in the future.

### Strengths
1.A large-scale multimodal banking dataset, MBD, is provided. This dataset contains anonymized banking transactions, geographic locations, and technical support dialogues, which contributes to the development of large-scale sequential event tasks in the future.
2.The dataset addresses privacy concerns through effective data anonymization, ensuring that the algorithm's performance is not significantly compromised.
3.The dataset and experimental code are publicly available, promoting transparency and reproducibility in research.

### Weaknesses
1.The dataset's multimodal data includes banking transaction records, geographic locations, dialogue embeddings, and banking product purchase history. However, it appears that many of these modalities are essentially text-based. This differs from typical multimodal datasets, which include modalities such as video, audio, and text. 

2.The main contribution of the paper lies in the introduction of a large-scale dataset, but it lacks innovative methods for addressing related tasks. Additionally, the experimental section presents insufficient comparisons with current state-of-the-art methods. Overall, the paper's innovativeness needs improvement. I suggest that the authors include more experiments involving fully supervised methods [1][2]. Additionally, it would be beneficial to propose a simple and practical innovative approach based on their dataset.

3.This paper contains numerous grammatical and tense issues. Additionally, the expression in the paper is not sufficiently clear, making it difficult for readers to accurately understand certain points and arguments. For example, on page three, phrases like “we selected” and “the dataset was collected”; on page five, “the coordinates were”; line 225 includes “we concentrated,” “whether it was,” and “random noise was added.” Additionally, on line 295, “we propose a downstream task — multimodal matching” (Zong et al., 2023).

### Questions
1. Do you have any specific method to model the different text modalities?
2.The paper contains numerous tense and grammatical errors, which do not meet the standards expected for ICLR.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a new multimodal dataset, MBD, from over 2 million corporate clients, including bank transactions, geo-locations, technical support dialogues, and monthly aggregated purchases of four banking products. The authors also present a benchmark for evaluating models on this dataset and two other financial datasets, focusing on tasks like purchase prediction and multimodal matching.

### Strengths
- Large-scale dataset: The MBD dataset is the largest of its kind, offering a significant amount of data for research purposes.   

- Multimodality: The dataset incorporates various data modalities, providing a more comprehensive view of client behavior.   

- Practical tasks: The benchmark focuses on practically relevant tasks, such as purchase prediction, which can be useful for real-world applications.   

- Anonymization: The authors have taken steps to anonymize the data, protecting client privacy.

### Weaknesses
 - Lack of novelty: The paper primarily focuses on introducing a dataset and benchmark. For ICLR submissions, I'd see more emphasis on novel methods or algorithms. In addition, a careful evaluation of previous models (for example, the MMBench https://arxiv.org/abs/2307.06281) will bring more novelty to the community.

- Missing comparison with LLMs: The paper lacks a comparison with more recent and powerful language models like GPT-4 or BloombergGPT, which have shown strong performance in various financial NLP tasks. For example, can we use prompt engineering to guide the GPT4o to process the transactions and geo-locations. 

- Unclear practical impact of the proposed metric: While the paper mentions that the benchmark can lead to financial benefits, I am curious if real world users care recalls/AUCs, or there are better metrics that map to financial success.

### Questions
-  The paper could be strengthened by exploring more advanced multimodal fusion techniques beyond late fusion.
-  A more detailed analysis of the anonymization process and its potential impact on model performance would be beneficial.
-  The authors could consider expanding the benchmark to include other relevant tasks, such as risk assessment or fraud detection.

Overall, while the MBD dataset and benchmark are valuable contributions, the paper needs significant revisions to address the lack of novelty and provide a more convincing argument for the practical impact of their work.

### Soundness
2

### Presentation
3

### Contribution
2
