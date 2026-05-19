# Evaluating Diversity of LLM-generated Datasets: A Classification Perspective

- Decision: Reject
- Scores: 5, 3, 5, 3, 5

## Abstract
LLM-generated datasets have been recently leveraged as training data to mitigate data scarcity in specific domains. However, these LLM-generated datasets exhibit limitations on training models due to a lack of diversity, which underscores the need for effective diversity evaluation. Despite the growing demand, the diversity evaluation of LLM-generated datasets remains under-explored. To this end, we propose a diversity evaluation method for LLM-generated datasets from a classification perspective, namely, DCScore. Specifically, DCScore treats the diversity evaluation as a sample classification task, considering mutual relationships among samples. We further provide theoretical verification of the diversity-related axioms satisfied by DCScore, demonstrating it as a principled diversity evaluation method. Additionally, we show that existing methods can be incorporated into our proposed method in a unified manner. Meanwhile, DCScore enjoys much lower computational costs compared to existing methods. Finally, we conduct experiments on LLM-generated datasets to validate the effectiveness of DCScore. The experimental results indicate that DCScore correlates better with various diversity pseudo-truths of evaluated datasets, thereby verifying its effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work propose a new metric, DCScore that measures the diversity of generated datasets. DCScores formulate the evaluation as a classification tasks and consists of three stages: text representation, pairwise similarity and diversity summarization to measure the dataset diversity. Experiments demonstrate DCScore outperforms other baselines, including Distinct-n, K-means inertia and VendiScore.

### Strengths
- The manuscript is logically organized and easy to follow. The main method is clearly explained with illustration figures.
- Several ablation studies are conducted, helping to understand the effectiveness of the proposed methods.
- Both empirical and theoretical justification are conducted to evaluate DCScore.

### Weaknesses
- For the goal of holistic analysis, DCScore involves pairwise similarity comparison, which is quadratic complexity as the number of samples, making it hard to scaling for large datasets, e.g., million-level samples, even billion level samples. In Line 63, previous methods struggles to offer a holistic evaluation of a dataset due to its reliance on pairwise similarity while DCScore seems also suffers to this issue.
- The improvements in Table 2 is modest. And it wound be better to analysis whether larger DCScore brings better performance when the models are optimized on the corresponding datasets.
- Section 4.3 can be simplified, most of the content are introducing some details about baseline method, which is not the contribution of this work.
- Seems like the main different between DCScore and VendiScore is the diversity summarization where VendiScore involves the eigenvalue computation, and DCScore use a more efficient softmax operation. More insights about why the eigenvalue computation is redundant wound further enhance the quality of this work.

### Questions
Please refer to the weaknesses part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new metric DCScore to measure the diversity of the generated dataset. Specifically, it first calculates a similarity matrix and using a softmax like function to convert the similarity matrix to represent the diversity. The final score will be the trace of the diversity summarization matrix.

### Strengths
The proposed metric is simple and easy to implement. It achieves comparable performance as other methods while shows slightly computation benefit when the dataset is small. The paper provides good proof of that DCScore satisfies several axioms defined for a principled diversity metric.

### Weaknesses
The paper claims DCScore has lower computational expense compared to other baseline methods. The theoretical analysis is questionable. In line 482, it says that the DCScore has a complexity of $O(n^2)$, which is incorrect, considering the calculation of the Kernel matrix, the computational complexity is at least $O(n^2d)$, where d is the dimension of the feature. The paper claims that the VendiScore has a computational complexity of $O(n^3)$, which also not true. VendiScore calculates the sum of the eigenvalues of the Kernal matrix, however, the sum of the eigenvalues of the Kernel matrix is equivalent to the sum of the eigenvalues of the covariance matrix, which makes the computation complexity to be $O(d^2n)$ instead of O$(n^3)$, as mentioned in section 3.2 of the VendiScore paper. Considering in real problem, n is always much larger than d, otherwise we shouldn’t care too much of the computation. In the computation cost experiment, the paper only compares the computation for a dataset with at most 4,000 samples, which is unfair for VendiScore. 

Performance-wise, from table 2, I also cannot see DCScore is  better than VendiScore. VendiScore is slightly better than DCScore in zero-shot case while DCScore is slightly better in few-shot setting. However, the difference is very minor. 

It’s a bit unclear to me the motivation of the classifier-based method, and why it’s better. VendiScore has the same properties of DCScore as well as performance. As I mentioned in the computation complexity part, DCScore may be not have lower computational cost as well.

### Questions
It would be very helpful if authors can help clarify the computation cost and help me better understand the motivation of using a classifier based method.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, the authors proposed a classification-based diversity evaluation method for LLM-generated datasets called DCScore, which treats diversity evaluation as a sample classification task and captures mutual relationships among samples. The authors provided theoretical verification that DCScore satisfies four axioms, including effective number, identical samples, symmetry, and monotonicity. Experiments show that DCScore exhibits a correlation with diversity parameters and human judgment compared to baseline metrics.

### Strengths
1. The authors proposed an LLM-generated dataset diversity evaluation method from a classification perspective called DCScore, which treats the evaluation of each sample in the LLM-generated dataset as a distinct classification task.

2. The authors provided theoretical verification that DCScore satisfies four axioms, including effective number, identical samples, symmetry, and monotonicity.

### Weaknesses
The paper has several weaknesses:

1. **Lack of Purpose and Application**: The significance of studying LLM-generated data diversity is unclear. The authors should clarify whether this research can aid smaller LLM training or accelerate LLMs' overall training, as well as the practical applications of diversity evaluation.

2. **Unclear Novelty of DCScore**: It is unclear whether DCScore is a new method or a simplified version of existing approaches. The paper should better highlight its novelty and contribution to the field.

3. **Unexplained Correlation Investigation**: The objective of investigating the correlation between DCScore and diversity pseudo-truth is not well explained. The authors should clarify how this experiment supports the overall thesis of the paper.

4. **Weak Performance and Experimental Design**: DCScore performs poorly in the zero-shot setting (Table 2), but no explanation is provided. Additionally, the rationale behind using Text Classification and Story Completion tasks needs to be better justified.

### Questions
Here are a few questions I would like to ask the authors:

1. Large Language Model (LLM)-generated datasets have found widespread applications, but what is the purpose or significance of studying the diversity of LLM-generated data? For instance, can research on the diversity of LLM-generated data contribute to training smaller LLMs or accelerate LLM training? Additionally, what are the potential application scenarios for investigating the diversity of LLM-generated data? I would appreciate it if the authors could provide further clarification on this point.

2. In Method 4.3, is DCScore a fusion or a simplified version of existing methods? What is the significance of the discussion in this section?

3. In the experiments, the objective of “investigating the correlation between the diversity evaluation of DCScore and the diversity pseudo-truth” is unclear. Could the authors elaborate on this goal and relate it to the central premise of the paper?

4. In Table 2 of the experiments, under the zero-shot setting, the performance of DCScore is not very strong. Could the authors provide an explanation for this? What is the rationale behind conducting experiments under the Text Classification and Story Completion settings?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents DCScore, a computationally efficient method for evaluating the diversity of LLM-generated datasets by framing diversity assessment as a sample classification task.

### Strengths
- This paper studies an underexplored problem, i.e., evaluating the diversity of LLM-generated datasets.
- The proposed method is simple and computation-efficient, and it does not need any model training.
- Experiments show that the proposed evaluation metric aligns with human judgments, highlighting its effectiveness.

### Weaknesses
1.	The method proposed in this paper seems to have a weak connection with classification, as it merely applies a softmax function based on a sample similarity matrix, which resembles instance discrimination in contrastive learning. The reviewer believes it is a stretch to interpret this as a classification problem.
2.	The method in this article is highly similar to VandiScore, except that it replaces the entropy of eigenvalues of the similarity matrix with matrix trace, yet the results in Table 2 show that both methods are very close.
3.	In addition to assessing dataset diversity, the reviewer suggests that a sample selection method should be proposed to eliminate redundant samples, thereby achieving a dataset with higher diversity and effectively reducing the overhead of data generation.
4.	The writing of this article needs further improvement; for instance, $\widetilde{T}$ is not clearly defined in the text; also, the description of the classifier $f$ and its referred softmax function are inconsistent and need to be adjusted.
5.	The method uses a sentence transformer to extract embeddings, and thus its effectiveness heavily relies on the generalization ability of the sentence transformer. It should be compared with other embedding models; additionally, there are many types of kernel functions, which were not considered in this paper.

### Questions
1. Does the size of the generated datasets affect the diversity score?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes DCScore to evaluate the diversity of LLM-generated datasets.DCScore treats the diversity evaluation as a sample classification task, considering mutual relationships among samples. The proposed method is somewhat novel to me.

### Strengths
The proposed method can be used to evaluate the diversity of LLM-generated datasets and capture the mutual relationships among samples.
Extensive experiments show that DCScore exhibits a stronger correlation with diversity parameters and human judgment than baseline metrics.
The authors evaluate both the performance and efficiency of DCScore, highlighting its effectiveness.

### Weaknesses
1. Some related works [1,2] evaluate the quality of augmented data from the data augmentation perspective. They also involve diversity-related metrics. It is suggested that authors discuss and compare with them.
[1] Gontijo-Lopes, Raphael, et al. "Affinity and diversity: Quantifying mechanisms of data augmentation." arXiv preprint arXiv:2002.08973 (2020).
[2] Yang, Suorong, et al. "Investigating the effectiveness of data augmentation from similarity and diversity: An empirical study." Pattern Recognition 148 (2024): 110204.
2. The diversity-sensitive components are important for DCScore calculations. How are these components computed? Since this is one of the most critical parts of the proposed method,  more specific details are needed.
3. I got a little confused about the definition and properties of DCScore. If I understand correctly, in the probability matrix P, P[i,i] denotes the probability of classifying T_i into class I. 1. What is the meaning of categories in the classification function? 2. If all samples are identical, what does the DCScore equal? If this is 1, the probability is one-hot and contracts to softmax calculations. If not, then the DCScore does not equal 1. The same is true for cases where all samples are distinct. More clarifications are needed.
4. On page 8, evaluation of existing datasets. How can we evaluate the effectiveness of different metrics? Are some datasets more diverse than others, and can the proposed metrics reflect this trend?
5. Is the diversity the higher, the better?  Can authors provide some takeaway conclusions for readers?
I will increase my score based on the authors' responses.

### Questions
Please see the weakness.

### Soundness
2

### Presentation
3

### Contribution
3
