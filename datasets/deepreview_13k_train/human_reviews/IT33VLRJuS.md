# Recovering Time-Varying Networks From Single-Cell Data

- Decision: Reject
- Scores: 3, 8, 3, 3

## Abstract
Gene regulation is a dynamic process that underlies all aspects of human development, disease response, and other key biological processes. The reconstruction of temporal gene regulatory networks has conventionally relied on regression analysis, graphical models, or other types of relevance networks. With the large increase in time series single-cell data, new approaches are needed to address the unique scale and nature of this data for reconstructing such networks. Here, we develop a deep neural network, Marlene, to infer dynamic graphs from time series single-cell gene expression data. Marlene constructs directed gene networks using a self-attention mechanism where the weights evolve over time using recurrent units. By employing meta learning, the model is able to recover accurate temporal networks even for rare cell types. In addition, Marlene can identify gene interactions relevant to specific biological responses, including COVID-19 immune response, fibrosis, and aging.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper aims to predict a series of graphs describing gene expression regulation by transcription factors from a series of single-cell gene expression data. The method uses attention-based architecture within each time point, with a recurrent component linking the time points.

### Strengths
The paper focuses on an important, though well-studied task of regulatory gene network inference. It focuses on time-series, single-cell data, an increasing available, more detailed view of gene expression. 

The approach goes beyond simple application of existing deep learning models by using an architecture in which the projection matrices for calculating attention are evolve as part of an RNN.

### Weaknesses
The architecture relies on interpreting the attention matrix A generated within the model as the adjacency matrix of the regulatory network, with the model itself being trained on a surrogate task of predicting cell type (y). The assumption that A, used in this surrogate task, will capture direct regulatory interactions is not very well justified in the manuscript. Would using a matrix with different dimensionality (e.g. having #columns the same, to match # of TFs, but with different number of rows), result in similar performance on the surrogate task? If yes, what beyond shape leads to the interpretation of A as the adjacency matrix? For example, is there a reason to apply softmax to rows of the matrix?

The experimental results are missing key details relating to the performance on regulatory network inference. Key statistics related to network-wide performance in discovering edges are not reported: it would be helpful to see AUROC and AUPR values. The justification for not reporting these metrics, based on the small size of the ground truth, is not convincing; these metrics are standard and should be reported, even if the ground truth is limited. Furthermore, the lack of comparison to other methods for regulatory network inference makes it difficult to assess the relative performance of the proposed approach.

### Questions
The model is aimed at time series, but the experimental data very few data points. If the method was applied to each time point separately (as just the first time point, eliminating the recurrent part), would the performance be affected substantially?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces an attention and graph based approach called Marlene, to infer dynamic GRN from time series (longitudinal) single cell RNA sequencing data. The author provided an in-depth overview of the GRN inference field and explained the need of developing novel methods to capture the time-varying gene networks. 

Marlene starts with a pooling by multihead attention (PMA) layer which transform gene expression profiles at multiple time points to gene feature matrix at multiple time points. Then self attention are applied on each of these gene embeddings and the adjacency matrix is calculated based on the learned transformation. The weights of the self attention module are connected with GRU units so that information could be shared across time points. Finally, the extracted GRN are used to regenerate the expressed data, and the generated features are used to predict the cell type label. The entire model is trained to predict cell type. 

In term of experiment, the author managed to squeeze results from 3 experiments into this paper. These 3 cases are SARS-CoV-2 Vaccination, Aging and Lung, and fibrosis a mouse lung injure model. All 3 experiments are solid and supporting the claim.

### Strengths
This is a very solid piece of research. The motivation is well explained and attractive. The idea is novel and has potential to be practically useful. The description of the method is very clear and the logic flows very well. The experiment part is comprehensive. 

In terms of the method itself, using PMA or Set transformer to convert the expression to gene feature matrix eliminate the axis of cells so downstream analysis could focus on the attentions on genes. The use of GRU in the next step is not so intuitive but seems to have literature support. The task of predicting cell labels is also very clever in this case because single cell data is noisy and complete reconstruction is more prone to error. Also, control the sparsities of the adjacency matrix by using the top k edges is also very inspiring.

### Weaknesses
1. I would like to see a more clear explanation on Equation 3-6. What exactly are the rational of using GRU here beyond it was used in EvolveGCN? Do we have any physical meaning on this operation on Equation 3-6? Specifically, it's unclear how the GRU's hidden state is initialized and how the temporal dependencies are captured by updating the self-attention weights, rather than the gene embeddings themselves. The connection to EvolveGCN is mentioned, but a deeper explanation of why this approach is suitable for dynamic GRN inference is needed. It is not clear if the GRU is capturing meaningful temporal dynamics or simply acting as a complex weight update mechanism.
2. Algorithm stability is a key metric in BEELINE. Could you comment on the stability of Marlene? It would be helpful to see some quantitative analysis of the variability in the inferred GRNs across multiple runs with different initializations. Are the top k edges consistent across runs, or do they vary significantly? This is crucial for the reliability of the method.
3. The output of Equation 6 is the adjacency matrix at timepoint t. Then, at least for the evaluation you have performed in this study, you must have transformed multiple At into one At. Could you explain in detail how you did that? It is not clear how the multiple adjacency matrices are combined to produce a single network for downstream analysis or visualization. The paper needs to specify if this is a simple average, or if more complex methods are used to combine the adjacency matrices.

### Questions
1. BEELINE does have a few dataset that has multiple time points (For example, hESC). I wonder how Marlene perform on those datasets in BEELINE. You can use the non-chipseq ground truth, which is very similar with the method I use. It would be great if you can use their metric (EPR/AUPRR etc)

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a novel deep learning framework called Marlene for reconstructing dynamic gene regulatory networks (GRNs) from time-series single-cell RNA sequencing (scRNA-seq) data. The authors aim to address the challenges of modeling the temporal evolution of GRNs using the increasingly available scRNA-seq data, which existing network inference methods are not well-equipped to handle.

Problem Significance: 
Studying the dynamic regulation of biological processes is crucial for understanding the mechanisms driving responses such as development, disease progression, and treatment outcomes. Reconstructing accurate temporal models of GRNs can provide key insights to identify potential interventions and treatments. However, the increasing scale of scRNA-seq data and the presence of multiple cells profiled per time point pose challenges for traditional GRN inference approaches. The development of Marlene tackles an important open problem in the field.

Model Input/Output: 
The input to Marlene is a time series of gene expression matrices {X^1, ..., X^T}, where each matrix X^t has dimensions (cells x genes) for a given time point t. The number of cells may vary per time point.
The output is a series of directed weighted graphs {G^1, ..., G^T} representing the GRN at each time point. The nodes are genes (assumed to be the same across time) and the edges capture regulatory relationships between transcription factors (TFs) and target genes. The graphs are characterized by adjacency matrices {A^1, ..., A^T}.
For evaluation, Marlene's inferred networks are benchmarked against curated TF-gene interaction databases (TRRUST and RegNetwork) using Fisher's exact test to assess overlap significance. The dynamics captured between time points are analyzed by computing intersection-over-union (IoU) scores.

### Strengths
Strengths:
* Marlene effectively leverages recent advances in deep learning, such as self-attention mechanisms and recurrent units, to model dynamic GRNs from scRNA-seq data. The approach uses set-based architectures to handle multiple cells per time point.
* Employing meta-learning (MAML) enables Marlene to reconstruct accurate networks even for rare cell types by treating cell types as tasks. This enhances the model's ability to handle heterogeneous cell populations.
* The model demonstrates strong empirical results on three diverse datasets, outperforming several static and temporal baselines in recovering known regulatory interactions and identifying relevant biological processes.

### Weaknesses
Weaknesses:
* The paper primarily evaluates using overlap analysis with existing incomplete databases of static interactions. More direct experimental validation of novel predicted regulatory links would strengthen the findings. Specifically, the authors should consider validating a subset of the predicted time-varying interactions using techniques such as targeted CRISPRi/a screens or perturbation assays followed by single-cell RNA-seq. This would provide stronger evidence for the biological relevance of the inferred dynamic networks.
* Potential limitations in scaling Marlene to a very large number of genes are not thoroughly discussed. In experiments, the quadratic memory usage from adjacency matrices led to gene filtering. The authors should provide a more detailed analysis of the computational complexity of their method, including memory and time requirements as a function of the number of genes, cells, and time points. This analysis should also consider the impact of using different hardware configurations (e.g., GPUs with varying memory capacities).
* The model currently lacks the ability to predict the effects of perturbations like TF knockouts, which could enhance its utility for causal inference and treatment design. The authors should discuss how their model could be extended to incorporate interventional data or how the inferred networks could be used to simulate the effects of perturbations. This could involve integrating techniques from causal inference or developing a module that predicts the downstream effects of TF perturbations.
* The usefulness of time-varying GRNs is not discussed. The authors should provide concrete examples of how the inferred dynamic networks can be used to gain biological insights. For instance, they could discuss how the identified changes in regulatory interactions can be linked to specific biological processes or how the model can be used to identify potential drug targets.

### Questions
1	How sensitive is Marlene to the choice of hyperparameters, such as the number of attention heads, hidden units, or depth of the neural network layers?
Explanation: The performance of deep learning models often depends on selecting hyperparameters. The paper does not provide a comprehensive analysis of how different hyperparameter settings affect Marlene's ability to recover accurate GRNs. Understanding the model's sensitivity to these choices is important for assessing its robustness and guiding practical applications.

	2	Can Marlene effectively handle datasets with a large number of time points or with irregular time intervals between samples?
Explanation: The study's datasets contain a relatively small number of time points (3-7). It is unclear how well the model would scale to longer time series, which are common in many biological processes. Additionally, the paper does not discuss how Marlene would handle irregularly sampled data, where the time intervals between consecutive points vary. Addressing these scenarios is crucial for the model's general applicability.

	3	How does the model's performance change when dealing with datasets of different sizes, both in terms of the number of cells and the number of genes?
Explanation: The paper reports results on three specific datasets but does not provide a systematic analysis of how the model's performance scales with the size of the input data. Understanding Marlene's data efficiency and ability to handle datasets of varying sizes is important for assessing its practical utility and guiding data collection efforts.

	4	How does Marlene handle technical noise and batch effects that are common in scRNA-seq data?
Explanation: Single-cell RNA sequencing data often contains technical noise and batch effects that can confound the analysis of biological variation. The paper does not explicitly discuss how Marlene deals with these issues or if any preprocessing steps (e.g., normalization, batch correction) were applied to the input data. Clarifying the model's robustness to these factors is vital for its reliable application to diverse datasets.

	5	Can the model provide insights into the strength and directionality of the inferred regulatory interactions?
Explanation: While Marlene outputs weighted directed graphs, the paper focuses primarily on evaluating the presence or absence of edges against existing interaction databases. It does not delve into how well the model captures the strength and directionality of the regulatory relationships. Providing a more detailed analysis of these aspects could enhance the interpretability and biological relevance of the inferred networks.

6    What are the downstream applications of time-varying GRNs? Currently, the authors evaluate according to the recovery of (static) curated interactions. How can the method be evaluated in a way that evaluates its utility for real downstream applications?

7   The paper shows an extremely large difference between Marlene and alternative methods. This is surprising because all methods perform largely the same tasks with only minor methodological tweaks. What can explain the large differences between models?

### Soundness
2

### Presentation
4

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
The paper titled "Recovering Time-Varying Networks from Single-Cell Data" introduces Marlene, a deep neural network designed to infer dynamic gene regulatory networks from time series single-cell gene expression data. The authors propose a model that employs self-attention mechanisms and recurrent units to construct directed gene networks, with weights that evolve over time. A significant contribution is the integration of meta-learning to enable accurate recovery of temporal networks, even for rare cell types. The study demonstrates Marlene's effectiveness in identifying gene interactions relevant to specific biological responses across multiple datasets, showcasing the potential of deep learning in unraveling the dynamics of gene regulation and its implications for understanding complex biological processes.

### Strengths
1. propose a novel deep learning framework that employs self-attention mechanisms and GRUs to model the dynamics of gene regulatory networks.
2. The method is tested across three diverse datasets, which demonstrate the generalization ability of the model.

### Weaknesses
1. While the paper presents a technical approach, it could benefit from a deeper discussion on the biological implications of the findings and how they align with or differ from current scientific understanding. Specifically, the paper lacks a detailed analysis of how the inferred time-varying networks relate to known biological pathways or regulatory mechanisms. The discussion should move beyond simply stating that the model recovers known interactions and delve into the functional consequences of the identified dynamic changes in gene regulation.

2. In the experimental phase, mainly presents results based on metrics, demonstrating that it outperforms other methods. However, for solving a specific GRN problem, we are more concerned with whether the inferred GRN can identify some key genes or transcription factors (TFs) that can be further analyzed downstream. For a biological problem, merely comparing metrics does not adequately demonstrate the model’s performance. The paper should include an analysis of the specific genes and TFs identified by the model, and how these relate to the biological processes under study. For example, are the identified TFs known regulators of the biological response, and are the predicted target genes consistent with known regulatory relationships?

3. The paper emphasizes using GRU to capture the temporal dynamics of the GRN. However, there are already many studies on dynamic GRNs, such as Dictys: dynamic gene regulatory network dissects developmental continuum with single-cell multiomics. I believe it would be more convincing to compare with these dynamic methods. The paper should explicitly compare the performance of Marlene with other state-of-the-art dynamic GRN inference methods, especially those that also use time-series single-cell data. A comparison with methods that use different modeling approaches, such as ordinary differential equations or Bayesian networks, would also be beneficial.

4. In GRN inference problems, perturbation experiments for some key genes are also an important downstream analysis. Including some perturbation experiments could help validate the accuracy of the inferred GRN. The paper should discuss the possibility of using perturbation data to validate the inferred GRNs. This could involve comparing the predicted effects of gene perturbations with experimental observations, which would provide a more direct assessment of the model's accuracy.

### Questions
1. While the paper presents a technical approach, it could benefit from a deeper discussion on the biological implications of the findings and how they align with or differ from current scientific understanding.
2. In the experimental phase, mainly presents results based on metrics, demonstrating that it outperforms other methods. However, for solving a specific GRN problem, we are more concerned with whether the inferred GRN can identify some key genes or transcription factors (TFs) that can be further analyzed downstream. For a biological problem, merely comparing metrics does not adequately demonstrate the model’s performance.
3. The paper emphasizes using GRU to capture the temporal dynamics of the GRN. However, there are already many studies on dynamic GRNs, such as Dictys: dynamic gene regulatory network dissects developmental continuum with single-cell multiomics. I believe it would be more convincing to compare with these dynamic methods.
4. In GRN inference problems, perturbation experiments for some key genes are also an important downstream analysis. Including some perturbation experiments could help validate the accuracy of the inferred GRN.

### Soundness
3

### Presentation
2

### Contribution
3
