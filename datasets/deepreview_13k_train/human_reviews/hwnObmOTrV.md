# Modeling Complex System Dynamics with Flow Matching Across Time and Conditions

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Modeling the dynamics of complex real-world systems from temporal snapshot data is crucial for understanding phenomena such as gene regulation, climate change, and financial market fluctuations. Researchers have recently proposed a few methods based either on the Schroedinger Bridge or Flow Matching to tackle this problem, but these approaches remain limited in their ability to effectively combine data from multiple time points and different experimental settings. This integration is essential in real-world scenarios where observations from certain combinations of time points and experimental conditions are missing, either because of experimental costs or sensory failure. To address this challenge, we propose a novel method named Multi-Marginal Flow Matching (MMFM). MMFM first constructs a flow using smooth spline-based interpolation across time points and conditions and regresses it with a neural network using the classifier-free guided Flow Matching framework. This framework allows for the sharing of contextual information about the dynamics across multiple trajectories. We demonstrate the effectiveness of our method on both synthetic and real-world datasets, including a recent single-cell genomics data set with around a hundred chemical perturbations across time points. Our results show that MMFM significantly outperforms existing methods at imputing data at missing time points.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper aims to model the dynamics of complex real-world systems across time and conditions using flow matching. Current methods, such as Flow Matching, remain limited by the inability to effectively capture information across multiple time points and experimental conditions. This paper aims to alleviate these limitations with a novel method they refer to as  Multi-Marginal Flow Matching, which leverages the Flow Matching framework and optimal transport theory to train a neural network to regress onto the flow. The authors evaluate the method’s effectiveness on synthetic and real-world data, demonstrating superior performance to existing baselines, measured by qualitative and quantitative metrics.

### Strengths
This paper introduces a novel method which expands on previous methodology in a parsimonious manner.
The work is relevant to the research community, addressing the problem of modeling complex system dynamics. 
The approach is simple and intuitive, with sound theoretical backing. The empirical evidence they provide is strong but limited. 
The experiments are well-designed and include sufficient baselines. The authors appear to know the literature very well and do a good job providing citations throughout. 
The paper is well-written and organized and easy to follow. I particularly appreciate how the authors clearly provide the minimally sufficient information in the main body of the paper and detail the appendix to complement.

### Weaknesses
The authors rigorously compare their method to multiple existing methods. However, they only do so on one real-world rna-seq dataset and one synthetic dataset. In the introduction of the paper, the authors give a multitude of real-world settings where their method may be considered useful. While the authors clearly motivate their method, I am concerned by the rigor with which they evaluate their method empirically. Are there additional datasets that could further demonstrate the effectiveness of the method, such as some of the genomics datasets used in Tong et al. (2024)? If so, inclusion would greatly increase this paper's contribution. The authors address this weakness in their rebuttal, providing additional experiments supporting their method's usefulness in practice.

In the proof of proposition 1, the final (*), I am confused how Fubini’s theorem applies here to switch the order of the inner product and integral. 
I may have a misunderstanding: is it necessary for conditions {c} to be given by the data. If they are missing, how may one proceed? In many real word systems, for example, conditions or categories may be latent and unobserved.

### Questions
In the proof of proposition 1, the final (*), I am confused how Fubini’s theorem applies here to switch the order of the inner product and integral. 
I may have a misunderstanding: is it necessary for conditions {c} to be given by the data. If they are missing, how may one proceed? In many real word systems, for example, conditions or categories may be latent and unobserved.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Multi-Marginal Flow Matching (MMFM), a method for modeling the dynamics of biological single-cell time series data. The proposed approach extends the Flow Matching (FM) framework by incorporating multiple time points and conditions, thereby learning the transport of probability distributions for cellular states across these different scenarios. MMFM leverages techniques like smooth spline-based interpolation and neural networks with classifier-free guidance to model changes over time and conditions. Through experiments on synthetic and single-cell RNA-seq datasets, the authors show MMFM's superior performance in imputing missing time points compared to other baseline methods.

### Strengths
- The motivation for using MMFM to model cell population dynamics across multiple steps and conditions is well-founded, as it directly addresses challenges inherent in biological experiments, such as fragmented and incomplete data. The multi-step transport approach is impressive in efficiently capturing the system's temporal and conditional complexities.

- The method extends (Conditional) Flow Matching (FM) to the *Multi-Marginal** setting, which is a natural and well-justified progression for addressing biological systems that require modeling across multiple time points. This approach enables the framework to leverage inter-dependencies across multiple conditions, significantly enhancing generalizability.

 - The use of **optimal transport** and **Schrödinger Bridge** for improving the integration of multiple marginals is insightful, resulting in improved model robustness. Compared to **piece-wise linear interpolation**, the introduction of cubic splines for smoother interpolation significantly boosts the performance and efficiency of the model, which is well demonstrated in their experiments.

### Weaknesses
 - The title, **"Modeling Complex System Dynamics,"** might be an over-claim relative to the paper's focus, which is primarily on **biological single-cell dynamics**. Typically, "Complex System Dynamics" also refers to broader scenarios, such as physical phenomena in fluid dynamics, climate systems, or even economic time series. Since the proposed method appears promising and generalizable, demonstrating its applicability to tasks in broader domains would further strengthen this claim.

- In the Multi-Marginal Conditional Flow Matching (MMCF), the authors pre-compute the solution for the multi-marginal optimal transport, which can be time-consuming. While they mention that **mini-batches** can be used to handle large datasets, further discussion on the **scalability** of the approach would be valuable. In particular, it would help if the authors could expand on the tradeoff between the **performance** and **efficiency** when comparing **L-MMFM** and **MMCF**, as OT solvers tend to become computationally expensive with increased dimensionality.

- Although MMFM is demonstrated effectively on biological single-cell data, there is no extensive discussion about its generalization capabilities in handling diverse temporal datasets beyond biology. Considering the potential to model other types of time series (e.g., physical or environmental data), the paper would benefit from a discussion about such possible applications and any inherent limitations.

### Questions
- Some generative models designed for imputation task can be also adapted for extrapolation/forecasting, such as CSDI[1]. Can the MMFM or CSD method be extended to handle **extrapolation** for sequences beyond the given time points?

- The current model appears to rely on temporal snapshots at specific intervals. Can **MMFM** handle **non-uniformly sampled** time points? If so, how is this addressed within the interpolation or flow matching framework?

[1]: Tashiro, Yusuke, et al. "Csdi: Conditional score-based diffusion models for probabilistic time series imputation." Advances in Neural Information Processing Systems 34 (2021): 24804-24816.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a Multi-Marginal Flow Matching (MMFM) method to model the dynamics of complex systems from fragmented temporal snapshot data. MMFM constructs a flow using smooth spline-based interpolation across time points and experimental conditions, and regresses this flow with a neural network using a classifier-free guided flow matching framework. The paper demonstrates the effectiveness of MMFM on both synthetic and real-world datasets, including a single-cell genomics dataset with around a hundred chemical perturbations, showing the MMFM’s power in imputing data at missing time points.

### Strengths
-The use of smooth spline-based interpolation is a plausible approach for constructing the flow across different time points.
-The authors evaluate MMFM on a real-world dataset involving cellular responses to drugs, demonstrating the method's applicability to practical problems in biology and medicine.

### Weaknesses
Lack of Clear Problem Definition: The paper lacks a clear and concise problem definition. There is no centralized notation or formal problem statement, making it difficult to follow the methodology and understand the specific goals of the research. The absence of a formal problem statement makes it challenging to assess the novelty and significance of the proposed method.
Incomplete Methodological Details: The method section is incomplete and lacks crucial details. For example, the loss function used for training is not fully explained, and key components such as mean and variance formulas are missing. Specifically, the paper does not clearly specify how the derivatives of the mean and variance functions are computed, which are essential for the flow matching objective. Additionally, the specific implementation of optimal transport is not described, leaving readers uncertain about how the method works in practice. The description of the multi-marginal optimal transport is vague, and it is unclear how the joint distribution is constructed from pairwise couplings.
Unclear Experimental Setup: The experimental setup is poorly documented. The origin of the formulas used in the synthetic dataset is not explained, and the y-axis labels in Figure 2 are missing, making it difficult to interpret the results. For the real-world dataset on cellular responses to drugs, the criteria for evaluating performance are not clearly defined, making it hard to assess the effectiveness of MMFM. The paper does not specify the metrics used to evaluate the imputation performance on the real-world dataset, making it difficult to reproduce the results.
Limited Baseline Comparisons: The performance comparison with baseline methods is inadequate. The paper mentions that MMFM outperforms existing methods but does not provide detailed comparisons or statistical significance tests, which are necessary to validate the claims. The lack of quantitative comparison with established methods makes it difficult to assess the practical value of the proposed approach.

### Questions
Why is the condition c multiplied by a scalar in Eq.(11) possible, as c is only the identifier of the condition?
What does the y-axis represent in Figure 2?
How is optimal transport specifically implemented in MMFM?
The MMFM loss function (7) and the CFM loss function (3) seem to be the same, what is the purpose of introducing the MMFM loss function?
From which literature do the formulas used in the synthetic dataset originate, What is the purpose of studying this synthetic dataset?
What is the exact definition of c_{\phi}?
What is the exact definition of \mu_{t}^{‘}(x) and \sigma_{t}^{‘}(x)?
What is the exact network architecture of \bar{v}_t(.)?

### Soundness
2

### Presentation
1

### Contribution
2
