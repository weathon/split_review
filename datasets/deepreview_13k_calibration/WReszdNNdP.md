# BOWLL: A DECEPTIVELY SIMPLE OPEN WORLD LIFELONG LEARNER

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
The quest to improve scalar performance numbers on predetermined benchmarks seems to be deeply engraved in deep learning. However, the real world is seldom carefully curated and applications are seldom limited to excelling on test sets. A practical system is generally required to recognize novel concepts, refrain from actively including uninformative data, and retain previously acquired knowledge throughout its lifetime. Despite these key elements being rigorously researched individually, the study of their conjunction, open world lifelong learning, is only a recent trend. To accelerate this multifaceted field's exploration, we introduce its first monolithic and much-needed baseline. Leveraging the ubiquitous use of batch normalization across deep neural networks, we propose a deceptively simple yet highly effective way to repurpose standard models for open world lifelong learning. Through extensive empirical evaluation, we highlight why our approach should serve as a future standard for models that are able to effectively maintain their knowledge, selectively focus on informative data, and accelerate future learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce the first monolithic baseline for open world lifelong learning, which remedies the lack of well suited baselines for evaluation. Particularly, the simple batch normalization technique is repurposed for 3 subtasks in lifelong learning: open-set recognition, active learning and continual learning. Through extensive empirical evaluation, the resulting approach proves simple yet highly effective to maintain past knowledge, selectively focus on informative data, and accelerate future learning. The proposed method also compares favorably to other related baselines.

### Strengths
- A simple and reliable baseline is always valuable, especially for the less-studied open world lifelong learning area. The method seems competitive on the benchmarked datasets.
- The unified use of the batch norm statistics for the 3 components in lifelong learning is interesting and promising. The ablation in Table 3 of the appendix is nice, indicating the involved components are indispensable.

### Weaknesses
 - One main concern of this paper is the missing analysis for some components of the proposed lifelong learner (see questions below).

 - The image synthesis method based on Deep Inversion seems interesting. All it's doing is to generate class-conditioned pseudo-images using past representations (the running mean and variance from the batch normalization layers). How much cost will such image synthesis incur? How faithful are the generated images? Why not opt for feature synthesis which seems natural and efficient given the maintained feature mean and variance?
- For active query, the acquisition function is designed using entropy weighted with sample similarity. How important is such weighting? Is this the best way to strike a good tradeoff between exploration and similarity? Any other formulations for ablation/comparison?

### Questions
- The image synthesis method based on Deep Inversion seems interesting. All it's doing is to generate class-conditioned pseudo-images using past representations (the running mean and variance from the batch normalization layers). How much cost will such image synthesis incur? How faithful are the generated images? Why not opt for feature synthesis which seems natural and efficient given the maintained feature mean and variance?
- For active query, the acquisition function is designed using entropy weighted with sample similarity. How important is such weighting? Is this the best way to strike a good tradeoff between exploration and similarity? Any other formulations for ablation/comparison?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a baseline method for open-world lifelong methods that relies on the idea of batch normalization. The method relies on three important components: 1) detection of out-of-distribution examples using batch-norm statistics, 2) active querying of remaining examples by using batch-norm statistics, 3) continual training using both example replay and generated pseudo-examples that also rely on information coming from batch-norm statistics. Experiments are run on three benchmark datasets, and compared to strategies such as joint learning, funetuning and GDUMB, using metrics such as backward transfer and accuracy.

### Strengths
- The paper intends to tackle the very important problem of open-world lifelong learning by exploiting a simple yet effective strategy of batch-normalization statistics. These statistics are exploited in several parts of the learning process, including discarding OOD examples, actively selecting most effective examples, and actually learning from these selected examples in a continual learning setting. 
- Experiments show that the proposed baseline is quite competitive, in particular in terms of backward transfer (Table 2)
- The paper is well-written and easy to follow. The components of the solution are clearly explained, and the diagram in Fig. 1 is very self-explanatory.

### Weaknesses
 - The main weakness that I see in the paper is the limitation of the experiments. I would have expected more robust experiments in more varied datasets, and a larger number of datasets and tasks. 
- Similarly, I would have expected more comparisons with other SOTA methods that, although not originally open-world learning, perhaps could be slightly modified for the sake of comparison.

### Questions
- Table 2 shows quite a remarkable good performance of the proposed method in the case of backward transfer, which is a very challenging problem in continual learning, and is difficult to achieve. Could you provide more insights as to why this would be the case?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses open-world continual learning, an emerging research area, and suggests leveraging Bayesian Network statistics to enhance various phases of open-world learning.

### Strengths
1. Applying BN statistics for OOD detection, active learning, and continual learning is a novel and unified approach.
2. The significance of the problem is notable.
3. It surpasses a strong baseline, GDUMB.

### Weaknesses
I believe this paper might overstate its contributions for the following reasons:

1. It seems to focus solely on the class-incremental learning scenario in continual learning, despite claiming to address various types of continual learning settings. How about, for example, Task-incremental learning [1]? The paper does not provide sufficient justification for why other continual learning scenarios, such as task-incremental learning, are not considered, especially given the claim of addressing general continual learning problems. This narrow focus limits the generalizability of the proposed method.

2. The paper claims that BOWLL can achieve OOD detection, active learning, and continual learning, but I only see a comparison in final and LCA performance in table 2. This falls short of adequately demonstrating the model's superiority in all three objectives. The experiments do not isolate and evaluate the performance of each component (OOD detection, active learning, and continual learning) independently. The paper needs to provide more comprehensive experiments and metrics to support its claims.

### Questions
See above

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript delineates a simple method, termed as BOWLL, which is devised as a baseline for the evaluation of open world lifelong learning - a conjunction of open-set recognition, active learning, and continual learning. The BOWLL exhibits an innovative usage of the Batch Normalization layer - a commonly-used component of neural networks,  along with Out-of-Distribution Detection module, Active Query module, Memory Buffer, and Pseudo Data that endow the proposed method with competitive performance for open world lifelong learning.

### Strengths
S1. The paper's significance is underscored by its motivation to facilitate future research in this domain.

S2. The BOWLL model's novelty is encapsulated in its innovative usage of the Batch Normalization layer, along with Out-of-Distribution Detection module, Active Query module, Memory Buffer, and Pseudo Data.

S3. The evaluation is comprehensive, with comparisons to baseline methods and ablation study providing a compelling demonstration of the promising performance of the BOWLL method.

S4. The clarity of the manuscript enhances accessibility for readers, facilitating a straightforward understanding of the proposed approach.

### Weaknesses
W1.  Although the paper provides a comprehensive explanation of the methodology, further technical insights regarding the implementation and each module within the BOWLL method would be beneficial. Specifically, the paper lacks detailed explanations of the inner workings of the Out-of-Distribution Detection module, the Active Query module, and the specifics of how the Batch Normalization layer is utilized in this context beyond a high-level description. The exact algorithms, parameters, and design choices for these components are not sufficiently elaborated, making it difficult to reproduce or fully understand the method.

W2. The paper falls short in providing a detailed analysis of the limitations of the proposed BOWLL, a factor which could be significant for future research and practical applications. The discussion of limitations is crucial for understanding the scope and applicability of the method. For example, under what conditions might the method fail, and what are the potential biases or assumptions that could affect its performance? A more thorough analysis of these aspects is needed.

W3. The computational complexity of the BOWLL algorithm, especially for those selection and replacement strategies, which could be a concern for large-scale datasets or practical applications, is not discussed in the manuscript. The paper should include a discussion of the time and space complexity of the algorithm, particularly focusing on the most computationally intensive parts, such as the active query and pseudo-data generation. This analysis is essential for assessing the scalability of the method.

W4.  Although the paper employs sound-good methodology and achieves competitive performance,  further efforts regarding the technical innovation and methodological novelty would be beneficial. While the combination of existing techniques is effective, the paper could benefit from a more in-depth discussion of the specific novel contributions beyond simply combining these modules. What are the unique insights or novel approaches that BOWLL brings to the field?

W5. The manuscript could delve deeper into the Continual Train Step, a factor which could be pivotal for understanding the pipeline of open-world lifelong learning. The paper does not provide enough detail on the optimization process, the learning rate schedules, or the specific loss functions used during the continual training phase. A more detailed explanation of these aspects would be beneficial.

W6. A more detailed exposition of the datasets used in the evaluation, including their characteristics and potential biases, would enrich the manuscript. The paper should provide more information about the size, class distribution, and any potential biases present in the datasets used for evaluation. This information is crucial for interpreting the results and understanding the generalizability of the method.

### Questions
C1. How does the method balance the data in the memory buffer and pseudo-images?

C2. What is the formulation of $R_{TV}()$ and $R_{l_2}()$ respectively in Eq. (7)?

C3. What is the meaning of $\beta$ in the evaluation metric LCA?

C4. Haven't the model used those discarded data?

C5. What is the relationship between open-world learning and open-world lifelong learning?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
