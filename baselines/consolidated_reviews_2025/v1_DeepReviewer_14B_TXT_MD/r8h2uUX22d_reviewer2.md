### Summary

The paper provides a new perspective on the MLP-Mixer architecture, a variant of MLPs that has recently gained attention in the vision domain. The authors show that the mixing layers of MLP-Mixer can be interpreted as an extremely wide MLP with a sparse weight matrix, achieved through the Kronecker product. This observation leads to the understanding that the MLP-Mixer implicitly incorporates sparsity, a concept widely studied in deep learning. The authors further demonstrate that the implicit regularization of the MLP-Mixer is related to the L1-norm of the weights. They also establish a connection between the MLP-Mixer and Monarch matrices, another form of sparse parameterization. Through empirical evaluations, the authors show that MLP-Mixer exhibits similar performance trends to unstructured sparse-weight MLPs when increasing sparsity (equivalent to widening) while keeping the number of connections fixed. They also propose a new family of MLP-Mixer-like architectures called the PK family, which generalizes the MLP-Mixer. The paper concludes by highlighting the importance of sparsity in the success of the MLP-Mixer and suggesting future research directions.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper provides a novel perspective on the MLP-Mixer architecture by showing its equivalence to a wider MLP with a sparse weight matrix. This connection sheds light on the internal mechanisms of MLP-Mixer and provides a deeper understanding of its behavior.
- The authors demonstrate that the implicit regularization of the MLP-Mixer is related to the L1-norm of the weights. This finding connects the MLP-Mixer to the concept of sparsity, which has been extensively studied in deep learning.
- The paper establishes a connection between the MLP-Mixer and Monarch matrices, another form of sparse parameterization. This connection further strengthens the understanding of the MLP-Mixer and its relationship to other sparse architectures.
- The authors conduct extensive empirical evaluations to support their claims. They show that the MLP-Mixer exhibits similar performance trends to unstructured sparse-weight MLPs when increasing sparsity while keeping the number of connections fixed. This finding suggests that sparsity is a key factor in the success of the MLP-Mixer.
- The paper is well-written and easy to follow. The authors provide clear explanations of their ideas and present their results in a concise and organized manner.

### Weaknesses

#### Some Related Works


#### comment

 - The paper focuses primarily on the theoretical analysis of the MLP-Mixer architecture. While the theoretical results are interesting, the paper could benefit from more extensive empirical evaluations to validate the proposed ideas. Specifically, the experiments could explore a wider range of datasets and hyperparameter settings to ensure the robustness of the findings. The current empirical analysis, while supportive, feels somewhat limited in scope.
- The paper could provide more insights into the practical implications of the proposed ideas. For example, how can the understanding of the MLP-Mixer as a wide and sparse MLP be used to design more efficient and effective architectures? The paper does not offer concrete guidance on how to leverage the sparsity insights for practical architecture design beyond the proposed PK family. It would be beneficial to explore specific architectural modifications or training strategies that directly exploit the identified sparsity patterns.
- The paper could discuss the limitations of the proposed ideas and potential directions for future research. For example, how does the proposed interpretation of the MLP-Mixer extend to other types of neural networks? The discussion of limitations is somewhat brief. A more in-depth analysis of the assumptions made in the theoretical analysis and how they might affect the conclusions would be valuable. Furthermore, the paper could explore the potential challenges in applying the proposed interpretation to other architectures, such as recurrent neural networks or graph neural networks.

### Suggestions

The paper makes a compelling theoretical connection between MLP-Mixer layers and sparse, wide MLPs, but the empirical validation could be significantly strengthened. The authors should consider expanding their experiments to include a more diverse set of datasets, beyond those typically used for image classification. For instance, exploring datasets with different modalities (e.g., text, audio) or varying degrees of complexity could provide a more comprehensive understanding of the generalizability of their findings. Furthermore, a more systematic exploration of hyperparameter space, such as varying the degree of sparsity, the width of the equivalent MLP, and the number of layers, would be beneficial. This would help to identify the optimal configurations for different tasks and provide a more robust validation of the theoretical claims. The authors could also consider comparing their approach with other sparse neural network techniques, such as pruning or regularization-based methods, to better understand the advantages and disadvantages of their proposed interpretation.

To enhance the practical impact of the work, the authors should provide more concrete guidance on how the insights gained from their analysis can be used to design more efficient and effective architectures. While the PK family is a good starting point, the paper could explore specific architectural modifications or training strategies that directly exploit the identified sparsity patterns. For example, the authors could investigate the use of structured sparsity, where entire filters or channels are removed, rather than just unstructured sparsity. This could lead to more computationally efficient models that are easier to implement on hardware. Additionally, the authors could explore the possibility of using the sparsity patterns to guide the design of custom hardware accelerators, which could further improve the efficiency of the proposed architectures. The paper could also benefit from a discussion on the trade-offs between sparsity, accuracy, and computational cost, providing practical guidelines for practitioners.

Finally, the paper should delve deeper into the limitations of the proposed interpretation and discuss potential avenues for future research. The authors should explicitly state the assumptions made in their theoretical analysis and discuss how these assumptions might affect the conclusions. For example, the analysis might be limited to linear activation functions or specific types of weight matrices. It would be valuable to explore how the interpretation extends to more complex scenarios, such as non-linear activations or different forms of weight initialization. Furthermore, the authors should discuss the challenges in applying their interpretation to other types of neural networks, such as recurrent neural networks or graph neural networks. This would help to identify the limitations of the current approach and guide future research in this area. The paper could also explore the potential for using the proposed interpretation to develop new regularization techniques or optimization algorithms that are specifically tailored to sparse neural networks.

### Questions

- Could you provide more details on the experimental setup used in the empirical evaluations? For example, what datasets were used, what metrics were used to evaluate the performance, and what were the hyperparameter settings?
- How does the proposed interpretation of the MLP-Mixer extend to other types of neural networks? Are there similar interpretations for other popular architectures, such as convolutional neural networks or recurrent neural networks?
- What are the potential applications of the proposed ideas beyond image classification? Could the understanding of the MLP-Mixer as a wide and sparse MLP be used to design more efficient and effective architectures for other tasks, such as natural language processing or speech recognition?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
