### Summary

This paper investigates the sparse property of MLP-Mixer. The authors first show that MLP-Mixer can be viewed as a wide MLP with sparse weights. Then, the authors show that the implicit regularization of MLP-Mixer is similar to that of sparse-weight MLP. Finally, the authors demonstrate that the performance of MLP-Mixer is similar to that of unstructured sparse-weight MLP.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. This paper investigates the sparse property of MLP-Mixer, which is an important research problem.
2. The authors provide a theoretical analysis of the sparse property of MLP-Mixer.

### Weaknesses

#### Some Related Works

[1] Monarch: An implicit sparse matrix library for deep learning.

#### comment

1. The authors claim that MLP-Mixer can be viewed as a wide MLP with sparse weights. However, the authors do not provide a quantitative analysis of the sparsity of the weights. The claim of a 'wide' MLP is also not clearly defined, and it's unclear how this relates to the actual width of the network in terms of the number of neurons in the hidden layers. A more precise definition of 'wide' and a quantitative measure of sparsity are needed to support this claim.
2. The authors claim that the implicit regularization of MLP-Mixer is similar to that of sparse-weight MLP. However, the authors do not provide a quantitative comparison of the implicit regularization. The claim of similarity is not supported by any empirical evidence or theoretical analysis. It is unclear what specific aspects of the implicit regularization are being compared and how similarity is measured.
3. The authors claim that the performance of MLP-Mixer is similar to that of unstructured sparse-weight MLP. However, the authors do not provide a quantitative comparison of the performance. The claim of similarity is not supported by any empirical evidence. It is unclear what metrics are used to compare the performance and how the similarity is measured.
4. The authors should compare the performance of MLP-Mixer with other sparse-weight MLPs. The lack of comparison with other sparse-weight MLPs makes it difficult to assess the novelty and effectiveness of the proposed approach. It is important to compare against a range of sparse-weight techniques to understand the relative strengths and weaknesses of MLP-Mixer.
5. The authors should provide a quantitative analysis of the sparsity of the weights in the Monarch matrix. The claim that the Monarch matrix has a similar sparsity pattern to MLP-Mixer needs to be supported by quantitative evidence. The authors should provide metrics such as the percentage of zero weights or the number of non-zero weights to support this claim.
6. The authors should provide a quantitative comparison of the implicit regularization of MLP-Mixer and sparse-weight MLPs. The claim of similarity in implicit regularization needs to be supported by quantitative evidence. The authors should provide metrics such as the norm of the weight matrices or the effective sparsity of the weight matrices to support this claim.
7. The authors should provide a quantitative comparison of the performance of MLP-Mixer and unstructured sparse-weight MLPs. The claim of similar performance needs to be supported by quantitative evidence. The authors should provide metrics such as the top-1 accuracy or the loss to support this claim.

### Suggestions

The paper would benefit significantly from a more rigorous quantitative analysis of the claims made. Specifically, the authors should provide precise definitions for terms like 'wide MLP' and 'sparse weights' and use these definitions to analyze the properties of MLP-Mixer. For example, instead of just stating that MLP-Mixer is a 'wide' MLP, the authors should specify the number of neurons in each layer and compare it to the number of parameters in a dense MLP with a similar number of parameters. Similarly, the authors should provide a quantitative measure of sparsity, such as the percentage of zero weights or the number of non-zero weights, for both the weights of MLP-Mixer and the Monarch matrix. This would allow for a more objective comparison of the sparsity patterns.

Furthermore, the authors need to provide quantitative evidence to support their claims about implicit regularization and performance similarity. For the implicit regularization, the authors should compare the weight matrices of MLP-Mixer and sparse-weight MLPs using metrics such as the norm of the weight matrices or the effective sparsity of the weight matrices. For the performance comparison, the authors should compare the top-1 accuracy or other relevant metrics on standard datasets. The authors should also compare the performance of MLP-Mixer with other sparse-weight MLPs to understand its relative effectiveness. This would help to establish the novelty and practical value of the proposed approach. The authors should also clarify what they mean by 'similarity' in the context of implicit regularization and performance, and provide specific metrics to quantify this similarity.

Finally, the authors should provide more details about the experimental setup and the datasets used. This would allow for a more thorough evaluation of the proposed approach. For example, the authors should specify the datasets used for each experiment, the training procedure, and the hyperparameters used. The authors should also provide a more detailed explanation of the Monarch matrix and its properties. By providing more details and quantitative analysis, the authors can make a stronger case for their claims and contribute more significantly to the field.

### Questions

1. What is the difference between the MLP-Mixer and the MLP with the Monarch matrix?
2. What is the difference between the implicit regularization of MLP-Mixer and that of sparse-weight MLP?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
