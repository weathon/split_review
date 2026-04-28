# CoRNStack: High-Quality Contrastive Data for Better Code Retrieval and Reranking

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Effective code retrieval plays a crucial role in advancing code generation, bug fixing, and software maintenance, particularly as software systems increase in complexity. While current code embedding models have demonstrated promise in retrieving code snippets for small-scale, well-defined tasks, they often underperform in more demanding real-world applications such as bug localization within GitHub repositories. We hypothesize that a key issue is their reliance on noisy and inconsistent datasets for training, which impedes their ability to generalize to more complex retrieval scenarios. To address these limitations, we introduce CoRNStack, a large-scale, high-quality contrastive training dataset for code that spans multiple programming languages. This dataset is curated using consistency filtering to eliminate noisy positives and is further enriched with mined hard negatives, thereby facilitating more effective learning. We demonstrate that contrastive training of embedding models using CoRNStack leads to state-of-the-art performance across a variety of code retrieval tasks. Furthermore, the dataset can be leveraged for training code reranking models, a largely underexplored area compared to text reranking. Our finetuned code reranking model significantly improves the ranking quality over the retrieved results. Finally, by employing our code retriever and reranker together, we demonstrate significant improvements in function localization for GitHub issues, an important
component of real-world software development.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new dataset CoRNSTACK for code retrieval tasks. Different from previous datasets, this dataset is a large-scale and high-quality dataset that contains hard negative samples. Trained with CoRNSTACK, the performance of models on code retrieval tasks and code reranking tasks has significantly increased. Besides, the authors also demonstrate the effectiveness of training with the proposed dataset in a real-world application (addressing GitHub issues).

### Strengths
1. According to my knowledge, the problems in previous code retrieval datasets discussed by the authors truly exist and the proposed dataset addresses these problems well. This proposed high-quality dataset will benefit research in code retrieval tasks and real-world retrieval applications.
2. The idea of fine-tuning LLMs as code rerankers is interesting and effective.
3. The authors not only evaluate code retrieval tasks, but also demonstrate the effectiveness of training with CoRNSTACK in addressing real-world GitHub issues.

### Weaknesses
Overall, I think this paper is good and should be accepted. All of the following weaknesses are minor problems.
1. There is no analysis of the reason for the improved performance of code rerankers. I guess this is also due to the hard negative samples?
2. As stated by the authors, one of the motivations for constructing this dataset is that existing datasets contain many false negative samples. In [1], the authors also discussed this problem and proposed methods to address the problem during model fine-tuning, which I think should also be discussed in the paper.
3. Although the authors discussed the problems of existing datasets in the introduction and some preliminaries of code retrieval in the paper, I still think it is better to write a related work section to make them clearer. Since code retrieval is not an extremely hot topic, many readers may not know many details of previous works in this area.
4. Typo in Line 272, 'high-qualit,y'

### Questions
1. Why do you use pre-trained text embedding models for dual consistency filtering? What about using pre-trained code retrieval models pre-trained on previous code retrieval datasets?
2. Fine-tuning models with contrastive learning is a common and traditional method for code retrieval tasks. Recently, there has been a new paradigm named Generation-Augmented Retrieval (GAR) framework proposed for code retrieval tasks as well [1, 2]. I think this framework makes the fine-tuning of code retrieval models somewhat unnecessary. What's your opinion on the necessity of fine-tuning code retrieval models? (Also, I think discuss this point in the paper will be better)


[1] Haochen Li, Xin Zhou, and Zhiqi Shen. 2024. Rewriting the Code: A Simple Method for Large Language Model Augmented Code Search. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1371–1389, Bangkok, Thailand. Association for Computational Linguistics.

[2] "Generation-Augmented Query Expansion For Code Retrieval." arXiv preprint arXiv:2212.10692 (2022).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a dataset built upon The Stack V2 dataset, proposing a high-quality contrastive training dataset called CoRNStack, which consists of (text, code) pairs. This dataset uses dual consistency filtering to eliminate noisy positives and is further enriched with mined hard negatives. The effectiveness of the proposed dataset is demonstrated through downstream code tasks, including code retrieval and re-ranking tasks.

### Strengths
A new dataset has been established on existing code datasets by filtering and selecting positive and negative samples.

### Weaknesses
 The process of handling negative samples in Figure 1 needs to be explained in more detail and more directly.

### Questions
1. The quality of the new dataset needs to be explained, especially how accurate the pairings are between text queries and code.  
2. It should also be clarified whether the code data in the dataset has been checked manually or tested with examples, as this is important for the quality of the code retrieval tasks.  
3. Additionally, it would be helpful to include information about the variety of code tasks in the new dataset, particularly how simple and complex scenarios are distributed.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper constructs a dataset containing high-quality positive and negative samples for contrastive learning, thereby achieving better retrieval and reranking performance. They ensure a strong semantic correlation between the positive samples and queries in the dataset through filtering, and they obtain high-quality and diverse negative samples through hard negative mining. The model trained on this dataset achieves generally excellent retrieval performance across different benchmarks and retrieval tasks. Additionally, they further extend this dataset to build an ordered dataset for training the reranker, which also yields good results. Finally, they combine the retriever and reranker to achieve effective function localization for GitHub issues.

### Strengths
1. The paper is easy to follow

2. Motivation is clear

3. The model achieves effective results, showing significant improvements in various scenarios, including retrieval, reranking, and function localization.

### Weaknesses
There are some minor flaws in the experimental section that could be further improved:

1.The motivation for selecting Arctic-Embed-M as the initial encoder for training, instead of other models, is not clearly explained.

2.The setup in section 4.2.1 lacks clarity. For example, the statement “a sampling strategy with varying window sizes (between 3 to 10) and random shuffling leads to 250k training instances” could be elaborated more for better clarity.

3.In training the reranker, the authors used the QWen 32B model as a teacher to annotate data. It might be beneficial to include the teacher model’s performance in Table 6, allowing us to see if the model approaches the teacher’s performance on this task.

4.In section 2.3, the authors mentioned using a softmax-based sampling strategy instead of directly adopting top-k sampling for better diversity of negative samples. Including an ablation study for this strategy in the experimental section could more clearly validate the effectiveness of your approach.

### Questions
Refer to weakness 2. What's your motivation to select Arctic-Embed-M as your initial encoder rather than other models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The article introduces CORNSTACK, a novel, high-quality dataset for contrastive code retrieval and reranking training. The primary motivation is to address the limitations in existing code embedding models, which struggle with complex, real-world software development tasks due to the noisy and inconsistent nature of current datasets. These models, crucial for bug localization and retrieval-augmented code generation, often fail to generalize beyond small, controlled tasks. The effectiveness of the dataset was demonstrated through the training of the retriever and reranker models.

### Strengths
1. The authors try to filter the high-quality code retrieval dataset from the stack dataset to solve the noise problem existing in the current code retrieval dataset.
2. The authors train both retriever and reranker models, and the final experimental results prove the effectiveness of the authors' method and achieve state-of-the-art results. 
3. The authors evaluate the code retrieval dataset and also try to evaluate the code retrieval model for the error localization dataset.

### Weaknesses
1. This paper's contribution is mainly incremental. It improves data quality through filtering and negative sample mining methods on the Stack V2 dataset, which has been extensively explored in previous research work [1,2]. This paper only makes minor improvements based on these papers. 
2. The paper lacks a more detailed comparison and analysis between the final obtained and original datasets beyond just quantity (such as case studies and other statistical conclusions). 
3. In the writing of the paper, the construction of the dataset and the harmful sample mining methods (especially the curriculum learning technique, which is not model-independent) are coupled. In my opinion, these are two parts: one part is the construction of the dataset, and the other part is the harmful sample mining method designed by the author. I believe these two parts should be more clearly distinguished in the writing. 
4. For the codet5+ model, the results reported in the paper seem to differ from those presented in the original text. Could the author add more detailed experimental settings?

### Questions
Please refer to Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2
