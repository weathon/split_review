# Aarj9MrG8Y — Meta Review

- Model: DeepReviewer 7B
- Decision: Accept
- Rating: 5.5
- Soundness: 3.0
- Presentation: 3.0
- Contribution: 3.0

## Summary

In this paper, I explore the introduction of Adaptive Power Graph Neural Networks (APGNN), which is designed to address the limitations of existing GNN models, particularly in terms of convergence and stability as the network grows deeper. The authors propose a universal learning principle for GNNs, emphasizing the convergence and stability of graph filters and providing a theoretical foundation for the design of infinite-depth GNNs. APGNN is constructed by employing exponentially decaying weights to aggregate information from different orders of neighbors, which is a novel approach that aims to mitigate over-smoothing and over-weighting issues. The paper also includes a theoretical analysis of the generalization ability of APGNN and extensive experimental results that demonstrate its superior performance against state-of-the-art GNN models on both homophilic and heterophilic datasets. Despite these contributions, the paper has several limitations, including the lack of a detailed computational complexity analysis, the absence of a thorough discussion on the model's behavior and limitations on heterophilic graphs, and the need for more rigorous experimental validation. These issues, while not undermining the overall significance of the work, highlight areas for improvement that could enhance the practical applicability and theoretical robustness of APGNN.

## Strengths

I find the paper to be well-written and well-organized, making it easy to follow the proposed methodology and theoretical analysis. The introduction of APGNN is innovative and well-motivated, addressing a critical gap in the literature by providing a principled approach to designing infinite-depth GNNs. The use of exponentially decaying weights to aggregate information from different orders of neighbors is a novel and effective technique that addresses the over-smoothing and over-weighting issues that are common in deep GNNs. The authors provide a clear and concise explanation of the power series expansion and its truncation, which is essential for the practical implementation of APGNN. The theoretical analysis of the generalization ability of APGNN is thorough and provides a solid foundation for understanding the model's performance. The experimental results are extensive and demonstrate the superiority of APGNN over several state-of-the-art GNN models, including DGCNN, SGC, GAT, and APPNP, on both homophilic and heterophilic datasets. The inclusion of a variety of datasets and tasks, such as node classification and link prediction, further strengthens the empirical validation of the proposed method. The paper also includes a detailed comparison with existing GNN models, showing how APGNN can unify and extend these models under the proposed learning principle. Overall, the paper makes a significant contribution to the field of GNNs by providing a principled and effective approach to designing deep and stable GNNs.

## Weaknesses

Despite the paper's strengths, there are several verified limitations that need to be addressed. Firstly, the computational complexity of APGNN is a significant concern. The authors acknowledge the need for truncation of the polynomial expansion to ensure computational feasibility, but they do not provide a detailed analysis of the computational complexity of the algorithm, particularly the time complexity of the matrix multiplications involved in the polynomial expansion. This is crucial because the computational cost scales with the size of the graph and the value of the polynomial order K, which can be a bottleneck for large graphs. The paper lacks a comparison of the computational cost of APGNN with other state-of-the-art GNN models, which is necessary to understand the trade-offs between performance and computational efficiency. This limitation is particularly important for the practical applicability of APGNN, as the computational cost can significantly impact its usability in real-world scenarios (Method, details, 'Polynomial Expansion').

Secondly, the paper does not provide a clear explanation of how the proposed APGNN model can be applied to heterophilic graphs. While the paper includes experiments on heterophilic datasets, the analysis focuses on the general graph filter definition and does not delve into the specific behavior of APGNN on such graphs. The exponentially decaying weights might behave differently in heterophilic graphs, where connected nodes have dissimilar features or labels, and it is not clear how these weights can effectively capture the complex relationships present in these graphs. The paper should include a more in-depth discussion of the potential modifications to the model architecture or training procedure that could improve its performance on heterophilic graphs, such as adaptive weighting schemes or different aggregation functions (Experiments, 'Node Classification Datasets').

Thirdly, the paper lacks a detailed discussion of the limitations of APGNN. The authors mention the truncation of the power series as a way to balance accuracy and computational cost, but they do not explore the potential drawbacks of this approximation or the exponentially decaying weights in detail. For example, the power series expansion might not be suitable for all types of graph structures, and the exponentially decaying weights might not be appropriate for all types of graph data. A clear understanding of these limitations is crucial for readers to properly interpret the results and apply the model in practice. The paper should also provide guidelines for when to use APGNN and when to use other GNN models, based on the characteristics of the graph data and the specific task at hand (Method, details, 'Polynomial Expansion').

Lastly, the experimental validation could be more rigorous. While the paper includes a variety of datasets and tasks, the scope of the experiments is limited in some aspects. The paper should conduct more experiments to demonstrate the advantages of APGNN, particularly in terms of its robustness and generalizability. The current experiments, while extensive, do not provide sufficient evidence to support the claim that APGNN is effective in scenarios with high polynomial orders or large graphs. Additionally, the paper should include a wider range of baselines and a more detailed statistical significance testing to ensure the reliability of the results (Experiments, 'Node Classification Datasets'). These weaknesses, while not undermining the overall significance of the work, highlight areas for improvement that could enhance the practical applicability and theoretical robustness of APGNN.

## Suggestions

To address the identified limitations, I recommend several concrete and actionable improvements. Firstly, the authors should provide a more thorough investigation into the computational aspects of APGNN. This should include a detailed analysis of the time complexity for each step of the algorithm, particularly the matrix multiplications involved in the polynomial expansion. The analysis should consider how the computational cost scales with the size of the graph and the value of the polynomial order K. Additionally, the authors should explore and discuss potential optimization techniques, such as sparse matrix operations or low-rank approximations, to reduce the computational burden. A comparison of the computational cost of APGNN with other state-of-the-art GNN models would also be valuable to provide a clear understanding of the trade-offs involved (Method, details, 'Polynomial Expansion').

Secondly, the authors should conduct a more in-depth analysis of how APGNN performs on heterophilic graphs. This should include experiments on benchmark datasets that exhibit heterophily, such as social networks or knowledge graphs. The authors should discuss the potential modifications to the model architecture or training procedure that could improve its performance on heterophilic graphs. For example, they could explore adaptive weighting schemes that take into account the similarity between connected nodes, or investigate different aggregation functions that are more suitable for heterophilic settings. The theoretical implications of using exponentially decaying weights in heterophilic graphs should also be discussed, and whether these weights can effectively capture the complex relationships present in such graphs (Experiments, 'Node Classification Datasets').

Thirdly, the paper should include a more detailed discussion of the limitations of APGNN. The authors should clearly state the assumptions made by the model and the conditions under which these assumptions might not hold. For example, the limitations of the power series expansion used in APGNN and the exponentially decaying weights should be discussed in detail. The paper should also provide guidelines for when to use APGNN and when to use other GNN models, based on the characteristics of the graph data and the specific task at hand. This discussion should include a clear understanding of the scenarios where APGNN might not be the most appropriate choice and the potential directions for future research (Method, details, 'Polynomial Expansion').

Finally, the authors should conduct more experiments to demonstrate the advantages of APGNN. This should include a wider range of datasets, tasks, and baselines to provide a comprehensive evaluation of the model's robustness and generalizability. The experimental setup should be more rigorous, with a clear description of hyperparameter tuning and statistical significance testing. For instance, the authors should report the mean and standard deviation of the performance metrics over multiple runs to ensure the reliability of the results. The paper should also explore the sensitivity of APGNN to different hyperparameter settings and provide guidelines for selecting appropriate values. These improvements would strengthen the empirical validation of APGNN and provide a more robust foundation for its practical application (Experiments, 'Node Classification Datasets').

## Questions

1. How does the proposed APGNN model perform on heterophilic graphs, and what are the specific challenges and potential solutions for addressing these challenges? The current analysis focuses on homophilic graphs, but many real-world graphs exhibit heterophily, where connected nodes have dissimilar features or labels. A deeper understanding of APGNN's behavior on heterophilic graphs is crucial for its practical applicability.

2. What are the potential strategies to reduce the computational cost of APGNN, especially for large graphs and high polynomial orders? The paper acknowledges the need for truncation to ensure computational feasibility, but a more detailed analysis of the computational complexity and potential optimization techniques is needed. This should include a discussion of sparse matrix operations, low-rank approximations, and other methods that could reduce the computational burden.

3. How does the proposed APGNN model unify existing GNN models, and what are the specific steps or transformations that can achieve this unification? The paper provides a theoretical analysis of the unification, but a more detailed and explicit demonstration of how APGNN can be seen as a general framework for existing GNN models would strengthen the paper's claims.

4. What are the limitations of the power series expansion used in APGNN, and how do these limitations affect the model's performance on different types of graph structures? The paper mentions the truncation of the power series, but a more thorough discussion of the potential drawbacks and the conditions under which these approximations might not hold is necessary.

5. How does the exponentially decaying weight parameter α affect the performance of APGNN, and what guidelines can be provided for selecting appropriate values for this parameter? The paper includes an ablation study on α, but a more comprehensive analysis of its impact on different graph sizes and complexities would be beneficial. This should include a discussion of the trade-offs between performance and computational cost when choosing different values of α.

## Full Content

## Summary:

In this paper, I explore the introduction of Adaptive Power Graph Neural Networks (APGNN), which is designed to address the limitations of existing GNN models, particularly in terms of convergence and stability as the network grows deeper. The authors propose a universal learning principle for GNNs, emphasizing the convergence and stability of graph filters and providing a theoretical foundation for the design of infinite-depth GNNs. APGNN is constructed by employing exponentially decaying weights to aggregate information from different orders of neighbors, which is a novel approach that aims to mitigate over-smoothing and over-weighting issues. The paper also includes a theoretical analysis of the generalization ability of APGNN and extensive experimental results that demonstrate its superior performance against state-of-the-art GNN models on both homophilic and heterophilic datasets. Despite these contributions, the paper has several limitations, including the lack of a detailed computational complexity analysis, the absence of a thorough discussion on the model's behavior and limitations on heterophilic graphs, and the need for more rigorous experimental validation. These issues, while not undermining the overall significance of the work, highlight areas for improvement that could enhance the practical applicability and theoretical robustness of APGNN.


## Soundness:

3.0


## Presentation:

3.0


## Contribution:

3.0


## Strengths:

I find the paper to be well-written and well-organized, making it easy to follow the proposed methodology and theoretical analysis. The introduction of APGNN is innovative and well-motivated, addressing a critical gap in the literature by providing a principled approach to designing infinite-depth GNNs. The use of exponentially decaying weights to aggregate information from different orders of neighbors is a novel and effective technique that addresses the over-smoothing and over-weighting issues that are common in deep GNNs. The authors provide a clear and concise explanation of the power series expansion and its truncation, which is essential for the practical implementation of APGNN. The theoretical analysis of the generalization ability of APGNN is thorough and provides a solid foundation for understanding the model's performance. The experimental results are extensive and demonstrate the superiority of APGNN over several state-of-the-art GNN models, including DGCNN, SGC, GAT, and APPNP, on both homophilic and heterophilic datasets. The inclusion of a variety of datasets and tasks, such as node classification and link prediction, further strengthens the empirical validation of the proposed method. The paper also includes a detailed comparison with existing GNN models, showing how APGNN can unify and extend these models under the proposed learning principle. Overall, the paper makes a significant contribution to the field of GNNs by providing a principled and effective approach to designing deep and stable GNNs.


## Weaknesses:

Despite the paper's strengths, there are several verified limitations that need to be addressed. Firstly, the computational complexity of APGNN is a significant concern. The authors acknowledge the need for truncation of the polynomial expansion to ensure computational feasibility, but they do not provide a detailed analysis of the computational complexity of the algorithm, particularly the time complexity of the matrix multiplications involved in the polynomial expansion. This is crucial because the computational cost scales with the size of the graph and the value of the polynomial order K, which can be a bottleneck for large graphs. The paper lacks a comparison of the computational cost of APGNN with other state-of-the-art GNN models, which is necessary to understand the trade-offs between performance and computational efficiency. This limitation is particularly important for the practical applicability of APGNN, as the computational cost can significantly impact its usability in real-world scenarios (Method, details, 'Polynomial Expansion').

Secondly, the paper does not provide a clear explanation of how the proposed APGNN model can be applied to heterophilic graphs. While the paper includes experiments on heterophilic datasets, the analysis focuses on the general graph filter definition and does not delve into the specific behavior of APGNN on such graphs. The exponentially decaying weights might behave differently in heterophilic graphs, where connected nodes have dissimilar features or labels, and it is not clear how these weights can effectively capture the complex relationships present in these graphs. The paper should include a more in-depth discussion of the potential modifications to the model architecture or training procedure that could improve its performance on heterophilic graphs, such as adaptive weighting schemes or different aggregation functions (Experiments, 'Node Classification Datasets').

Thirdly, the paper lacks a detailed discussion of the limitations of APGNN. The authors mention the truncation of the power series as a way to balance accuracy and computational cost, but they do not explore the potential drawbacks of this approximation or the exponentially decaying weights in detail. For example, the power series expansion might not be suitable for all types of graph structures, and the exponentially decaying weights might not be appropriate for all types of graph data. A clear understanding of these limitations is crucial for readers to properly interpret the results and apply the model in practice. The paper should also provide guidelines for when to use APGNN and when to use other GNN models, based on the characteristics of the graph data and the specific task at hand (Method, details, 'Polynomial Expansion').

Lastly, the experimental validation could be more rigorous. While the paper includes a variety of datasets and tasks, the scope of the experiments is limited in some aspects. The paper should conduct more experiments to demonstrate the advantages of APGNN, particularly in terms of its robustness and generalizability. The current experiments, while extensive, do not provide sufficient evidence to support the claim that APGNN is effective in scenarios with high polynomial orders or large graphs. Additionally, the paper should include a wider range of baselines and a more detailed statistical significance testing to ensure the reliability of the results (Experiments, 'Node Classification Datasets'). These weaknesses, while not undermining the overall significance of the work, highlight areas for improvement that could enhance the practical applicability and theoretical robustness of APGNN.


## Suggestions:

To address the identified limitations, I recommend several concrete and actionable improvements. Firstly, the authors should provide a more thorough investigation into the computational aspects of APGNN. This should include a detailed analysis of the time complexity for each step of the algorithm, particularly the matrix multiplications involved in the polynomial expansion. The analysis should consider how the computational cost scales with the size of the graph and the value of the polynomial order K. Additionally, the authors should explore and discuss potential optimization techniques, such as sparse matrix operations or low-rank approximations, to reduce the computational burden. A comparison of the computational cost of APGNN with other state-of-the-art GNN models would also be valuable to provide a clear understanding of the trade-offs involved (Method, details, 'Polynomial Expansion').

Secondly, the authors should conduct a more in-depth analysis of how APGNN performs on heterophilic graphs. This should include experiments on benchmark datasets that exhibit heterophily, such as social networks or knowledge graphs. The authors should discuss the potential modifications to the model architecture or training procedure that could improve its performance on heterophilic graphs. For example, they could explore adaptive weighting schemes that take into account the similarity between connected nodes, or investigate different aggregation functions that are more suitable for heterophilic settings. The theoretical implications of using exponentially decaying weights in heterophilic graphs should also be discussed, and whether these weights can effectively capture the complex relationships present in such graphs (Experiments, 'Node Classification Datasets').

Thirdly, the paper should include a more detailed discussion of the limitations of APGNN. The authors should clearly state the assumptions made by the model and the conditions under which these assumptions might not hold. For example, the limitations of the power series expansion used in APGNN and the exponentially decaying weights should be discussed in detail. The paper should also provide guidelines for when to use APGNN and when to use other GNN models, based on the characteristics of the graph data and the specific task at hand. This discussion should include a clear understanding of the scenarios where APGNN might not be the most appropriate choice and the potential directions for future research (Method, details, 'Polynomial Expansion').

Finally, the authors should conduct more experiments to demonstrate the advantages of APGNN. This should include a wider range of datasets, tasks, and baselines to provide a comprehensive evaluation of the model's robustness and generalizability. The experimental setup should be more rigorous, with a clear description of hyperparameter tuning and statistical significance testing. For instance, the authors should report the mean and standard deviation of the performance metrics over multiple runs to ensure the reliability of the results. The paper should also explore the sensitivity of APGNN to different hyperparameter settings and provide guidelines for selecting appropriate values. These improvements would strengthen the empirical validation of APGNN and provide a more robust foundation for its practical application (Experiments, 'Node Classification Datasets').


## Questions:

1. How does the proposed APGNN model perform on heterophilic graphs, and what are the specific challenges and potential solutions for addressing these challenges? The current analysis focuses on homophilic graphs, but many real-world graphs exhibit heterophily, where connected nodes have dissimilar features or labels. A deeper understanding of APGNN's behavior on heterophilic graphs is crucial for its practical applicability.

2. What are the potential strategies to reduce the computational cost of APGNN, especially for large graphs and high polynomial orders? The paper acknowledges the need for truncation to ensure computational feasibility, but a more detailed analysis of the computational complexity and potential optimization techniques is needed. This should include a discussion of sparse matrix operations, low-rank approximations, and other methods that could reduce the computational burden.

3. How does the proposed APGNN model unify existing GNN models, and what are the specific steps or transformations that can achieve this unification? The paper provides a theoretical analysis of the unification, but a more detailed and explicit demonstration of how APGNN can be seen as a general framework for existing GNN models would strengthen the paper's claims.

4. What are the limitations of the power series expansion used in APGNN, and how do these limitations affect the model's performance on different types of graph structures? The paper mentions the truncation of the power series, but a more thorough discussion of the potential drawbacks and the conditions under which these approximations might not hold is necessary.

5. How does the exponentially decaying weight parameter α affect the performance of APGNN, and what guidelines can be provided for selecting appropriate values for this parameter? The paper includes an ablation study on α, but a more comprehensive analysis of its impact on different graph sizes and complexities would be beneficial. This should include a discussion of the trade-offs between performance and computational cost when choosing different values of α.


## Rating:

5.5


## Confidence:

3.25


## Decision:

Accept
