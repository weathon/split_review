# Learning from Label Proportions: Bootstrapping Supervised Learners via Belief Propagation

- Decision: Accept
- Avg Score: 5.80
- Scores: 5, 8, 5, 6, 5

## Abstract
Learning from Label Proportions (LLP) is a learning problem where only aggregate level labels are available for groups of instances, called bags, during training, and the aim is to get the best performance at the instance-level on the test data. This setting arises in domains like advertising and medicine due to privacy considerations. We propose a novel algorithmic framework for this problem that iteratively performs two main steps. For the first step (Pseudo Labeling) in every iteration, we define a Gibbs distribution over binary instance labels that incorporates a) covariate information through the constraint that instances with similar covariates should have similar labels and b) the bag level aggregated label. We then use Belief Propagation (BP) to marginalize the Gibbs distribution to obtain pseudo labels. In the second step (Embedding Refinement), we use the pseudo labels to provide supervision for a learner that yields a better embedding. Further, we iterate on the two steps again by using the second step's embeddings as new covariates for the next iteration. In the final iteration, a classifier is trained using the pseudo labels. Our algorithm displays strong gains  against several SOTA baselines (upto \textbf{15\%}) for the LLP Binary Classification problem on various dataset types - tabular and Image. We achieve these improvements with minimal computational overhead above standard supervised learning due to Belief Propagation, for large bag sizes, even for a million samples. %

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper provided an algorithm to perform efficient learning from bag-level label proportions. The author utilized Belief Propagation on parity-like constraints derived from covariate information and bag-level constraints to obtain pseudo labels. Next, the Aggregate Embedding loss used instance-wise pseudo labels and bag-level constraints to output a final predictor. In the end, the authors also provided  experimental comparisons against several SOTA baselines across various datasets of different types.

### Strengths
1. Learning from bag-level Label Proportions (LLP)  is an interesting and valuable topic in the learning community. Privacy of data is one crucial consideration in this area.
2. The literature part is clear.
3. The structure of the paper is easy to follow.
4. There is extensive experiment analysis on the algorithm performance.

### Weaknesses
Major
1. In the setup section (section 3, p3), it lack the assumptions and descriptions on the data distribution (x,y), and bag distribution.
1.1 For example, for distributions,  the proposed algorithm may not work and or could not converge
1.2 Without data distribution assumptions, it will limit the guidance for practitioners. 

2. There is no analysis of the theoretical guarantee of the algorithm's performance.

3. The proposed algorithm is much slower than the baseline algorithm, and the running time is about one order slower Table 4. However, the performance of the proposed algorithm in Table 2 and 3 are not significantly better in many setups.

4. The 4 datasets in the experimental analysis are not real data on the bag-level. The bags are manually created.

5. Some notations are not reader-friendly. 
5.1 For example, in formula (2), the meaning of  | | is not defined. 
5.2 3rd line in section 3 of p3, [m] is not defined.

Minor
1. In section 6.1, there is only time for one baseline algorithm, and it lacks time for other algorithms.

2. Near all parameters are tuned. There is no guidance on how to choose them in practice for quick application. For example, there is no guideline for the stopping rule of the algorithm to ensure convergence.

3. In the proposed algorithm, the pair-wise calculation could lead to a high order time complexity. For example, capturing k-nearest neighbors for every point x_i is a very slow process when the data size is large.

### Questions
1. What's the performance of the proposed algorithm on real bag-level data?

2. What's the time performance of other baseline algorithms?

3. Are there any stopping rules to decide when to stop the iteration and ensure the convergence?

4. What's the distribution and bagging assumption required for the proposed algorithm?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel algorithm for supervised learning from label proportions. One first builds a Gibbs measure that enforces the labels proportions within each bag and incentivizes nearby samples to have the same label. Then belief propagation (BP) is run on this measure, obtaining the marginals for each label. The marginals are converted to hard labels via thresholding. These new labels are then used to train a deep neural net. The network is trained on a double objective: one one side fitting the BP generated labels, on the other preserving the actual proportions of the labels in each bag. One of the internal representations of the network is then used as new covariates from which the BP and training are repeated. This algorithm achieves performances which are competitive with or superior to those of competing algorithms.

### Strengths
The paper is well written
The proposed algorithm is interesting and novel. 
The experimental presented experimental evidence appears complete and compelling.
The algorithm achieves a good performance compares to other existing methods.

### Weaknesses
 The proposed algorithm is slower than other algorithms it is comapred to.

### Questions
1. To enforce the label proportions directly in the BP have you tried sending $\lambda_b\to\infty$ and then doing MAP decoding (i.e. instead of thresholding each marginal, you take the configuration of labels that maximizes the BP approximation to the Gibbs measure)?

2. Can you provide some intuition into the architecture of the network g_L? For example what is the function of the average pooling and how it is applied.

3.This is more of a comment: BP is supposed to be more precise on sparse factor graphs. Your factor graph is not sparse due to the term with $\lambda_b$ coupling all the variables within one bag. Do you think there is a way to modify the Gibbs measure to keep the desired properties but having a sparse factor graph?

4. Can you comment on the convergence of the BP iterations? Did BP converge? did the convergence time change with the size of  the training set? Did you use some trick to make it converge?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a method for the problem of Learning from Label Proportions (LLP), where only aggregate level labels are available for groups of instances. The proposed method incorporates both bag-level and instance-level constraints to address the LLP problem. Then, the Belief Propagation (BP) algorithm is utilized to solve the problem. Finally, the authors verify the proposed method for the  LLP Binary Classification problem.

### Strengths
1. The topic of this paper is interesting and important. Learning from Label Proportions (LLP) is a weak-supervised learning paradigm, which is beneficial for privacy protection.
2. The proposed method exhibits good performance on large bag sizes.

### Weaknesses
1. The writing of this paper needs great improvement, e.g., the connection between the LLP problem and the parity checks should be clearly elaborated. The intuition behind this should be clarified. Specifically, the paper needs to explain how the parity check concept, typically used in error correction, directly translates to the constraints imposed on bag-level labels in the LLP setting. The analogy is not immediately obvious, and the paper should provide a more detailed explanation of how enforcing even parity relates to matching aggregate labels.
2. The bag-level and instance-level constraints are commonplace, making the novelty quite limited. While the constraints themselves are not novel, the specific way they are combined and used within the Gibbs distribution framework needs to be more clearly articulated to establish the novelty of the approach. The paper should emphasize the unique aspects of its formulation and how it differs from existing methods that also utilize similar constraints.
3. The experiments were only conducted on Binary Classification problems, while the multi-class classification is a more general case. The lack of experiments on multi-class classification limits the generalizability of the proposed method. The paper should at least discuss the challenges of extending the method to multi-class scenarios and provide some preliminary results or a clear roadmap for future work in this direction.
4. The formulation of the equations should be carefully checked, e.g., in Eq.(1), according to the definition of $y(S_i)$ (the third row in Section 3), the first term equals 0. Besides, the derivation from Eq.(1) to Eq.(2) should be provided for clear understanding. The definition of $y(S_i)$ as the sum of instance labels within bag $S_i$ makes the first term in Eq. (1) zero, which is a critical error. The derivation from Eq. (1) to Eq. (2) is not clear and should be explicitly shown, including the steps taken to simplify the equation and the rationale behind each step. The paper needs to clarify the notation and ensure the equations are mathematically sound.
5. The proposed method performs well on large bag sizes, but the authors do not give explanations why this is the case. The paper should provide a theoretical or empirical analysis of why the proposed method performs better with larger bag sizes. This could involve discussing the properties of the Belief Propagation algorithm or the characteristics of the data that make it more suitable for larger bags. Without this explanation, the results are less convincing.
6. According to the results of Tables 4 and 5, the running time of the proposed method is far more than that of DLLP, besides, the running time of other methods is not reported. The significant increase in running time compared to DLLP raises concerns about the practicality of the method, especially for large datasets. The paper should report the running time of other baseline methods to provide a more comprehensive comparison and justify the computational cost of the proposed method.
7. According to the results of Tables 9-13, the parameters seem to need very careful fine-tuning, and the sensitivity studies of these parameters are missed. The lack of sensitivity analysis for the hyperparameters makes it difficult to assess the robustness of the proposed method. The paper should include experiments that evaluate the performance of the method under different hyperparameter settings to demonstrate its stability and provide guidance on parameter tuning.

### Questions
1. Why do you introduce the Gibbs distribution in the modeling? The reasons should be detailedly clarified.
2. Are the instances in each bag all labeled? If yes, then the bag level counts will equal the size of the bag.
3. Is the size of each bag in this paper equal? What if the sizes of each bag are not equal?
4. In Table 2, why not report the results of large size (512, 1024, 2048) as other tables do?
5. According to the results of Tables 1-3, it is weird that the performance of DLLP(published in 2017) is better than that of GenBags(published in 2022) and EasyLLP(published in 2023). Please explain these.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the setting of learning from label proportions (LLP), where we have access to aggregate labels over bags (i.e., grouped instances). The authors provide an approach that (1) implements belief propagation to assign pseudolabels to similar data points and (2) iteratively trains supervised classifiers with the pseudolabels (and the previous classifiers learned embeddings).

### Strengths
* The authors provide a new scheme (based on Ising models and belief propagation) to propagate pseudolabels across datapoints taking into account bag constraints and covariate similarity.
* They also derive a new architecture and objective during bootstrapping their supervised model on the produced pseudolables. This involves an additional hidden layer that produces soft scores over the bag to maintain correct bag proportions.
* Good experimental gains over existing LLP baselines with large bag sizes.

### Weaknesses
1.  Lack of explanation/intuition about results. Are there any hypotheses as to why the results of your method are worse in cases with small bag sizes but better in cases with large bag sizes?


2. Lack of discussion about work from the field of weak supervision, where there have been similar problems studied in the context of combining weak supervision (labels similar to aggregate labels over bags) and covariate information via clustering [1] and via label propagation [2]. In both cases, a model is trained after pseudolabels are generated (although no iterative refinement is done as these methods start from pretrained representations and supervised models are directly fit on the pseudolabels).


3. A few typos that I noted (that don’t overall affect my score):
* Last line of page 7: “the iteration seem to help improve performance”, should be “iteration seems to help improve performance”
* “Bag constraints” in section 6.1 shouldn’t be capitalized

### Questions
* See first point in the weakness section. Are there any particular intuitions as to why DLLP outperforms your method (somewhat consistently) over small bag sizes?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an effective and efficient approach to the problem of Learning from Label Proportions. The proposed approach has two main steps. In the first step, it uses Belief
Propagation to marginalize the Gibbs distribution to obtain pseudo labels. In the second step, it uses the pseudo labels to provide supervision for a learner. The paper conducted experiments to show the usefulness of the proposed approach.

### Strengths
- The problem of Learning from Label Proportions could be useful. 
- This paper is well structured and easy to follow.
- The proposed approach outperforms state-of-the-art approaches.

### Weaknesses
 - The proposed approach is complex; a simple framework is desirable. The two-step iterative process, involving Belief Propagation and embedding refinement, introduces significant overhead. The reliance on a Gibbs distribution and factor graph further complicates the implementation and understanding of the method.
- The proposed approach assumes the case of disjoint bags; it cannot handle non-disjoint bags. This limits the applicability of the method in real-world scenarios where data points may belong to multiple bags. The inability to handle overlapping bags is a significant constraint.
- The paper lacks theoretical aspects of the proposed approach. Specifically, there is no rigorous analysis of the convergence properties of the iterative algorithm, nor a clear understanding of the impact of the graph structure on the final performance. The absence of theoretical guarantees makes it difficult to assess the reliability of the method.

### Questions
The paper should discuss theoretical aspects of the proposed approach. For example, I am interested in the time and space complexity of the proposed approach since the proposed approach has rather complex framework. What are the computational and memory costs of the proposed approach?

The graph structure has a significant impact on the proposed approach. How do you determine the number of nearest neighbors? Is there any theoretical background to determine the graph structure?

As shown in Algorithm 1, the proposed approach uses the iterative computations. Does the proposed approach have a theoretical property to converge? How do you determine the number of iterations, R?

As shown in Table 1 and 2, for UCI and Criteo datasets, the proposed approach is competitive to the previous approaches. On the other hand, the proposed approach does not work well for CIFAE dataset, as shown in Table 3. Please theoretically justify the experimental results. 

Since the proposed approach uses a k-NN graph, it needs a high computational time to construct the graph. In Section 6.1, the paper shows the processing time of only the proposed approach. Is the proposed approach more efficient than the previous approaches?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
