### Summary

This paper studies the problem of semi-supervised node classification, where the number of labeled nodes is extremely small and the labeled nodes are not provided on a per-class basis. To address this problem, the authors propose a framework called ELI (Estimating Label Information) to estimate label information and enhance reformulations of well-known semi-supervised learning frameworks. The proposed framework is evaluated on several datasets and shows significant improvements over baselines.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The problem studied in this paper is interesting and important.
2. The proposed framework is well-motivated and easy to understand.
3. The experimental results show that the proposed framework can improve the performance of baselines.

### Weaknesses

#### Some Related Works

[1] Graph neural networks with structural and positional representation.
[2] Dropedge: Towards removing noisy edges for graph neural networks training.
[3] Dropmessage: Unifying random dropping for graph neural networks.

#### comment

1. The novelty of this paper is limited. The proposed framework is similar to the existing methods [1,2,3]. The authors should discuss the differences between their proposed method and these existing methods. Specifically, the paper lacks a detailed comparison of how the proposed ELI framework differs from methods that incorporate structural and positional information into GNNs, or those that use edge dropping techniques. The paper needs to clarify the specific mechanisms by which ELI's label information estimation provides an advantage over these existing approaches, particularly in scenarios with extremely limited labeled data.

2. The authors claim that the proposed method can enhance the performance of GNNs in the SLNC task. However, the experimental results do not support this claim. The authors only compare their method with the original GNNs, and the performance improvement is marginal. The authors should compare their method with more advanced GNNs, such as GPRGNN [4] and GPSGNN [5], which have demonstrated superior performance on graph datasets. The current comparison is insufficient to demonstrate the practical significance of the proposed method, as it does not show improvement over state-of-the-art GNN architectures.

3. The authors should conduct experiments on more datasets. The datasets used in the experiments are relatively small, and the authors should consider using larger datasets to evaluate the scalability of their method. The current datasets may not be representative of real-world scenarios, and the lack of experiments on larger, more complex datasets limits the generalizability of the findings.

4. The authors should compare their method with the existing methods in the literature. The paper lacks a comprehensive comparison with relevant methods, making it difficult to assess the relative performance of the proposed approach. The authors should include a more thorough literature review and compare their method against a wider range of state-of-the-art techniques for semi-supervised node classification.

5. The authors should provide more details on the experimental settings. The paper lacks sufficient details on the hyperparameter settings, the training procedures, and the computational resources used. This makes it difficult to reproduce the results and to assess the validity of the experimental evaluation.

### Suggestions

The paper needs to significantly strengthen its novelty claims by providing a more detailed comparison with existing methods that incorporate structural and positional information, as well as edge dropping techniques. The authors should clearly articulate how the ELI framework's label information estimation differs from these approaches and why it is particularly effective in the SLNC setting. A more rigorous theoretical analysis of the proposed method would also be beneficial, providing insights into its convergence properties and generalization capabilities. Furthermore, the experimental section needs to be significantly expanded to include comparisons with state-of-the-art GNN architectures, such as GPRGNN and GPSGNN, to demonstrate the practical significance of the proposed method. The authors should also conduct experiments on larger and more diverse datasets to evaluate the scalability and generalizability of their approach. This would provide a more comprehensive evaluation of the proposed method and its potential for real-world applications.

To address the lack of detailed experimental settings, the authors should provide a comprehensive description of all hyperparameters used in their experiments, including the learning rate, batch size, number of epochs, and any other relevant parameters. They should also specify the exact training procedures used, including the optimization algorithm, any regularization techniques, and the hardware used for the experiments. This level of detail is crucial for ensuring the reproducibility of the results. Furthermore, the authors should consider releasing their code and datasets to the community to facilitate further research in this area. This would allow other researchers to verify their findings and build upon their work. The authors should also include ablation studies to analyze the impact of different components of their framework on the overall performance.

Finally, the authors should provide a more thorough literature review and compare their method against a wider range of state-of-the-art techniques for semi-supervised node classification. This would help to contextualize their contribution and demonstrate its significance within the broader research landscape. The authors should also discuss the limitations of their proposed method and suggest potential directions for future research. This would provide a more balanced and nuanced view of their work and its potential impact. The authors should also consider exploring the use of different label information estimation techniques and analyze their impact on the performance of the proposed framework.

### Questions

Please refer to the Weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
