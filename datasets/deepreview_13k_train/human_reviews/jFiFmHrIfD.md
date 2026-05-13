# Explorative Latent Self-Supervised Active Search Algorithm (ELSA)

- Decision: Reject
- Scores: 5, 5, 1

## Abstract
In computer vision, attaining exceptional performance often necessitates access to large labeled datasets. The creation of extensive datasets through manual annotation is not only cost-prohibitive but also practically infeasible due to the scarcity of positive samples in imbalanced datasets where negative samples dominate. To tackle this intricate problem, we introduce Efficient Latent Space-based Self-Supervised Active Learning Search (ELSA), an active learning-based labeling assistant. ELSA distinguishes itself from existing interactive annotation methods by focusing exclusively on positive class labeling in massively imbalanced datasets replete with a substantial number of negative samples. Through the automatic exclusion of the majority of negative samples, ELSA achieves a remarkable level of precision and accuracy in its search. This novel framework comprises three fundamental components: a)an iterative Nearest Neighbor Search, b)a Sophisticated Random Sampler, c)a Linear Head powered by Active Learning. Our comprehensive study provides insights into the interplay of these components and their collective impact on search efficiency. Notably, we demonstrate that ELSA achieves orders of magnitude superior performance, in average starting with as little as 5 or less positive samples in ImageNet 1k we managed to detect as much as 80\% of all the examples belonging to that class by only labeling as little as 0.67\% of the entire dataset manually.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a new approach to active learning-based labeling called ELSA, or the Explorative Latent Self-Supervised Active Search Algorithm. ELSA is designed to address the challenges of imbalanced datasets and limited positive samples in computer vision applications. The authors demonstrate that ELSA can achieve high levels of precision and accuracy even with just a few positive samples, making it a cost-effective and practical alternative to manual annotation. The paper also outlines the three fundamental components of ELSA and provides experimental results to support its effectiveness. Overall, the paper's contributions include a novel approach to active learning-based labeling, a detailed description of the ELSA algorithm, and empirical evidence of its effectiveness in computer vision applications.

### Strengths
1. The authors propose a novel active learning-based labeling method which combines a Nearest Neighbour search module, A Random Sampler and a classification head, achieves orders of magnitude superior performance.

2. The authors provide empirical evidence of the effectiveness of ELSA in computer vision applications, using several benchmark datasets and evaluation metrics.

3. The paper also includes a thorough analysis of the results, discussing the strengths and limitations of the approach and comparing it to other state-of-the-art methods.

### Weaknesses
1. Lack of analysis of the impact of hyperparameters such as “a” in the NEAREST NEIGHBOUR SEARCH: The authors do not provide a detailed analysis of the impact of hyperparameters on the performance of ELSA. This is an important aspect of the algorithm, as the choice of hyperparameters can have a significant impact on its effectiveness. A more thorough analysis of the impact of hyperparameters would help to identify the optimal settings for different datasets and applications.

2. The meanings of some symbols such as $L_e$ and $d_r$ in Section3.1 have not been provided with sufficient clarity.

3. The paper could benefit from a clearer structure. For instance, in the beginning of Section 4, the explanation of the algorithm's different components is a bit messy. A suggested improvement is to organize it with Samper first, followed by Random Search, and then NN for better coherence.

4. In Section 4.4, the author could strengthen the explanation of why the algorithm works by referencing previous works or providing experimental proof. To make the argument more convincing, it's suggested to back up claims with references. Also, consider using actual data points instead of Figure 1 for a more persuasive visualization.

5. There are some symbol consistency problems in this paper. For example, in Algorithm 1, $\mathcal M_{ij}$ should be written as $\mathcal M_{ij} = MSE(g(d_i), g(\Lambda_j))$. It's important to use the same symbols for the same concepts, like using $I_i$ in Section 3.1 but $d_i$ in Section 4.1.

6. Although I'm not very familiar with the related works, the discussion of algorithmic time and space complexity in Section 5 may not be crucial for this task.

7. The paper and appendices experiment with hyperparameters and embedding spaces to validate the effectiveness of each component, but it lacks a crucial aspect—a comparison with popular existing methods. It's important to show how the algorithm performs compared to other well-known techniques.

### Questions
1. How sensitive is ELSA to the choice of hyperparameters? Can you provide a more detailed analysis of the impact of hyperparameters on the performance of the algorithm? This would help to identify the optimal settings for different datasets and applications.

2. How might ELSA be extended or modified to address other challenges in active learning-based labeling, such as the presence of noisy or mislabeled data?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an active learning-based labeling assistant algorithm, called ELSA. The author clarifies that ELSA can help reduce the time required to label samples by orders of magnitude compared to manual labeling in large datasets dominated by many negative samples. The paper provides insights into the interplay of these components and their collective impact on search efficiency. Finally, the paper also presents proof-of-concept empirical experiments to corroborate the theoretical results.

### Strengths
Although I haven't thoroughly read most of the technical proofs, the results appear sound and technically correct.

### Weaknesses
The paper is in general easy to follow and well-structured. There are some interesting theoretical guarantees, which seem simple and effective. Nevertheless, I have the following concerns:

1. Not enough empirical evaluations.  it necessary to evaluate other state-of-the-art tabular benchmarks in Table 5. 
2. Novelty and limitations. The theoretical justification is interesting but the novelty in the method itself is slightly incremental, and the proposed algorithm seems based on a simple modification.

The paper has a few English typos in different places. The setting studied in the paper is quite classical. The novelty is harder to judge for me (see my comment in the "weaknesses" above) but the method and algorithm proposed seem quite classical. However, because of my unfamiliarity with the related works, this is a low-confidence review.

I could not find the code to check reproducibility.

### Questions
The paper has a few English typos in different places. The setting studied in the paper is quite classical. The novelty is harder to judge for me (see my comment in the "weaknesses" above) but the method and algorithm proposed seem quite classical. However, because of my unfamiliarity with the related works, this is a low-confidence review.

I could not find the code to check reproducibility.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper discussed an efficient latent space based self-supervised active learning search. Typically, it focuses on positive class labeling. The method includes three components: a)an iterative Nearest Neighbor Search, b)a Sophisticated Random Sampler, c)a Linear Head powered by Active Learning, Some experiments are done to show the method works to some extent.

### Strengths
The paper considers a self-supervised active learning search, which seems to be a potential solution to reduce labeling effort.

### Weaknesses
(1)	The novelty of the work is very small as both active learning and self-supervised learning are well known.
(2)	The solution that this paper takes is quite common, including nearest neighbor search and random sampler.
(3)	It looks like the pape combines several existing methods into one piece without motivating the method well and explaining why they are combined.

(4) The paper is poorly written without an official problem definition.

### Questions
(1) The contribution is not clearly. For instance why nearest neighbor search would be listed as contribution since it is just a common method. Similarly , the random sampling method is also a very routine method. 

(2) The method lacks theoretical support. For instance, what is the error bound ? How does the method perform under noisy setting ?

(3) The experimental evaluations are weak and not sufficient.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor
