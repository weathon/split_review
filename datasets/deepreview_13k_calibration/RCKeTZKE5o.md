# Meta Compression: Learning to compress Deep Neural Networks

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Deploying large pretrained deep learning models is hindered by the limitations of realistic scenarios such as resource constraints on the user/edge devices. Issues such as selecting the right pretrained model, compression method, and compression level to suit a target application and hardware become especially important. We address these challenges using a  novel meta learning framework that can provide high quality recommendations tailored to the specified resource, performance, and efficiency constraints.
For scenarios with limited to no access to unseen samples that resemble the distribution used for pretraining, we invoke diffusion models to improve generalization to test data and thereby demonstrate the promise of augmenting meta-learners with generative models. When learning across several state-of-the-art compression algorithms and DNN architectures trained on the CIFAR10 dataset, our top recommendation shows only 1\% drop in average accuracy loss compared to the optimal compression method. This is in contrast to 25\% average accuracy drop achieved by selecting the single best compression method across all constraints.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a meta learning algorithm which can predict a good compression algorithm for a given compression target.

### Strengths
The idea of using a generative model to generate test data seems like a great solution to the limited data problem. For real-world applications, I think this problem is much less important because new data can always be obtained.

### Weaknesses
1) It was hard to contextualize this work for me. For example, how does this work compare to [1], which uses multi-objective Bayesian optimization to yield an entire Pareto-frontier for architecture + compression algorithm hyperparameters?
2) What is the novelty of this work? Is neither a new meta learning algorithm nor compression algorithm, as far as I can tell. To me, it seems the main novelty is the application of meta learning to model compression. In this case, I would need to see experimental evidence that meta learning for model compression is better than existing approaches using Bayesian optimization [1], DNAS, OFA

### Questions
1) I was confused what exactly is the static erm strategy?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a method utilizing meta learning framework to provide compression methods for any deep learning methods tailoring it for specific resource, performance and efficiency constraints. There main focus is to apply the compression techniques to address the challenges of deploying large models in resource-constrained scenarios.

### Strengths
The authors provide a clear motivation of the problem and is easy to read and follow. The authors also supplement the claims with some proofs and empirical results.

### Weaknesses
One part which is not very clear is around the choice of the accuracy predictor and not very clear how the experiments look like with respect to other design choices around different compression strategies which would make it better to understand the generalizability of the solution. Because of this choice it limits the applicability of the results as they are compared against only one compression constraint.

It is not clear how the research generalized with more recent modeling techniques specifically around transformers, which would help to strengthen the paper and understand the generalizability of the provided approach.

### Questions
1. How would the result and analysis hold against newer architectures specifically around transformers?
2. Do you see limitations of the approach with respect to datasets or architectural choice?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In scenarios where it is vital to make precise choices regarding pretrained models, compression techniques, and compression levels to meet the requirements of a particular application and hardware constraints, this paper introduces a novel approach. The approach utilizes a compression performance predictor to address these challenges, providing customized, high-quality recommendations aligned with specified resource, performance, and efficiency constraints. Additionally, the method incorporates diffusion models to enhance the model's generalization capabilities to test data. To validate the proposed approach, extensive experimentation is conducted, covering a range of state-of-the-art compression algorithms and Deep Neural Network (DNN) architectures trained on the CIFAR-10 dataset.

### Strengths
1. The overall concept is intriguing and holds the potential to evolve into a strong research paper. The aim to develop a compression accuracy predictor that offers compression method recommendations for users is noteworthy. However, the current format lacks effective organization and effective illustration.

2. The research is substantiated with evaluations on a diverse range of architectures, and a large training dataset is created for the compression accuracy predictor.

### Weaknesses
1. It's advisable to include citations in the introduction to enhance the document's comprehensibility. The absence of citations, except in the initial paragraph, can pose challenges for readers in understanding the content. Incorporating citation references in the introduction will provide valuable context and background information.

2. I find that the overall presentation of the work can be somewhat challenging to follow. For instance, in the description of the inner loop of the meta-learning process in Figure 2a, there appears to be a discrepancy where Metadata extraction lacks information from the compressed classifier, which contradicts the description in the main context.

3. The title suggests that the focus of the work is on "learning to compress DNN" implying the main objective is to compress various models with different compression methods using a meta-learner. However, the paper is more like "learning to choose compression methods of DNN" and predominantly centers on training a compression accuracy predictor to predict performance. It then recommends specific compression methods based on different requirements. This deviation from the title's apparent focus may appear inconsistent or confusing to readers.

### Questions
1. The construction process involves numerous architectural considerations and requires training the compressed model as well. While the training cost remains manageable for smaller datasets like CIFAR-10, it's essential to investigate whether this approach introduces excessive overhead when applied to larger datasets such as ImageNet-1000.

2. Could you please offer further elaboration on the "META FEATURES"? Additional details about the specific features used would be beneficial for a clearer understanding.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper addresses the challenges of deploying large pretrained deep learning models in resource-constrained scenarios by introducing a novel meta-learning framework. This framework offers high-quality recommendations for selecting pretrained models, compression methods, and compression levels tailored to specific resource, performance, and efficiency constraints. The proposed approach improves generalization to test data by using diffusion models for limited access to unseen samples.

### Strengths
+ The proposed approach formulates the recommendation for compression methods as an optimization problem, finding the solution via boosted decision trees. This framework can somewhat give a solution when we deal with new data that are not accessible. 
+ The proposed meta-learning framework shows good performance in experiments.
+ This paper provides theoretical proof of the proposed meta learning optimization.

### Weaknesses
 - The novelty of this paper is limited. The proposed method is a simple machine learning problem, which is easy to prove in a certain hypothesis.
- In the actual scenarios, the performance of a certain compression method is highly related to multiple hyper-parameters. This paper does not consider these factors. Specifically, the learning rate, batch size, and number of epochs used during fine-tuning after compression can drastically affect the final performance. The paper only considers the target sparsity and quantization levels, which are insufficient to capture the full complexity of the compression process.
- The pruning and quantization are usually implemented serially in practice. However, the proposed method considers them separately and then merges them together using a simple criterion. This simplification might not reflect the actual interactions between pruning and quantization, where the order of operations and the specific algorithms used can have a significant impact on the final model quality. For example, applying quantization before pruning can lead to different results than the reverse order.
- The quantization and pruning methods tested in this paper are out-of-date. Also, other compression categories like low-rank matrix and tensor decomposition are not considered. The paper should have included more recent and advanced compression techniques such as adaptive quantization, structured pruning, and tensor-train decomposition to make the evaluation more comprehensive and relevant to the current state-of-the-art.
- According to Fig. 7, the proposed method does not work well on large-scale datasets. The performance gap between the proposed method and exhaustive search is significant, indicating a lack of robustness and scalability.
- This paper does not compare with SOTA compression methods (published after 2021) that are directly used to compress models on unseen datasets. The absence of comparison with recent state-of-the-art methods makes it difficult to assess the true value and competitiveness of the proposed approach.
- The training cost is still very high, i.e., 8 days. I don't think the proposed framework can save time a lot as compared to existing SOTA compression methods.

### Questions
This paper uses heuristic information based on existing data. How can you guarantee the existing heuristics work well on another dataset as compared to direct compression and tune on that dataset?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
