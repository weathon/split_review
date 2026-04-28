# TimeInf: Time Series Data Contribution via Influence Functions

- Decision: Accept
- Avg Score: 5.80
- Scores: 5, 6, 6, 6, 6

## Abstract
Evaluating the contribution of individual data points to a model's prediction is critical for interpreting model predictions and improving model performance. Existing data contribution methods have been applied to various data types, including tabular data, images, and texts; however, their primary focus has been on i.i.d. settings. Despite the pressing need for principled approaches tailored to time series datasets, the problem of estimating data contribution in such settings remains unexplored, possibly due to challenges associated with handling inherent temporal dependencies. 
This paper introduces \textbf{TimeInf}, a data contribution estimation method for time-series datasets. TimeInf uses influence functions to attribute model predictions to individual time points while preserving temporal structures. Our extensive empirical results demonstrate that TimeInf outperforms state-of-the-art methods in identifying harmful anomalies and helpful time points for forecasting. Additionally, TimeInf offers intuitive and interpretable attributions of data values, allowing us to easily distinguish diverse anomaly patterns through visualizations

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents an interesting approach to time series interpretability research—by using noise perturbations to measure the contribution of data to the model. However, the method designed by the authors is a theoretical extension of existing approaches and lacks more extensive experimental evidence to demonstrate its effectiveness.

### Strengths
The idea of inferring interpretability and anomaly analysis by measuring the contribution of time series data to the model's output is quite novel. The mathematical derivation is well-developed, and the details are thorough.

### Weaknesses
1. Compared to existing methods, the advantages of this approach are not fully emphasized, and the innovative aspects are not clearly defined. The main contribution of the paper can be seen as an extension of existing theory, but the method primarily involves deriving formulas based on Equation (3) and considering the Mixture of \( \delta z^{[m]} \). This operation has limited significance for theoretical extension and does not effectively demonstrate the contribution claimed. I do not believe it addresses the shortcomings of existing methods. Specifically, while the authors derive new formulas, the core mechanism remains rooted in the influence function framework, and the use of a mixture distribution for perturbations, while novel, does not fundamentally alter the underlying limitations of influence functions when applied to complex time series models. The paper needs to more clearly articulate how this approach overcomes the challenges of applying influence functions to time series data, beyond simply extending the equations.

2. The paper conducts experiments on anomaly detection, interpretability, and mislabeled error in datasets. However, the paper does not discuss current state-of-the-art baselines in anomaly detection, such as methods based on LLMs or DCdetector. Moreover, the AUC and F1 results differ significantly from the original work. While the authors' skepticism about dataset quality is commendable, more evidence is needed to support this claim, as only partial visualizations of the data are presented. Additionally, the ablation experiments in the appendix are limited to parameter experiments. Based on my experience, complex theoretical methods often perform unsatisfactorily in neural network training, and more evidence is required to validate the effectiveness of the theory. The lack of comparison with state-of-the-art anomaly detection methods, especially those leveraging deep learning, makes it difficult to assess the practical utility of the proposed method. Furthermore, the limited ablation studies fail to explore the method's robustness across different model architectures and training regimes, which is crucial for establishing its general applicability.

3. Compared to traditional machine learning papers, there is no clear and complete process to present the designed algorithm, such as the input, output, and objective function. The majority of the paper is focused on theoretical formulas and related comparisons, making it difficult to understand. The absence of a clearly defined algorithm, including input data format, output interpretation, and the precise objective function being optimized, hinders the reproducibility and practical implementation of the proposed method. The paper should provide a step-by-step algorithm that clarifies how the theoretical framework translates into a concrete computational procedure.

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a new method for measuring the contribution of different timestamp to the final predictions. The major idea is to leverage influence scores to assign model predictions to individual time points while preserving temporal structures between the time points. Experiments in anomaly detection can verify the effectiveness of the proposed method.

### Strengths
1. The paper is well-written and easy to follow.
2. The presented solution is technically solid.
3. The experiments on anomaly detection can demonstrate the efficacy of the proposed method.

### Weaknesses
1. The relationship between the proposed model and unsupervised anomaly detection is unclear and should be further explained. Specifically, it's not evident how the influence scores derived from the model directly translate to anomaly scores. The paper needs to clarify whether high influence scores indicate anomalies or normal data points, and how a threshold is determined to differentiate between them. The current explanation lacks a clear connection between the model's internal workings and the final anomaly detection results.

2. The model's generalization ability to other time series tasks (e.g., forecasting, imputation) is uncertain. Specifically, how would the contribution score of historical timestamps be measured for future time points? The paper does not address how the proposed method would handle the inherent uncertainty in future time series data when calculating influence scores. It's unclear if the method can be adapted to scenarios where the goal is to predict future values rather than reconstruct past ones. The method's applicability to forecasting and imputation tasks needs more rigorous justification and explanation.

3. There is no discussion on scalability. How does the method perform as the number of historical time points increases? The paper lacks a detailed analysis of the computational cost associated with the proposed method, especially concerning the calculation of influence scores. It's crucial to understand how the method's performance scales with the length of the time series and the dimensionality of the data. The paper should include a discussion on the practical limitations of the method in terms of computational resources and time complexity.

### Questions
Please reply to the above weaknesses if I have any misunderstandings. Thank you.

Another question: Can the proposed model process multivariate time series?

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
4

### Summary
This paper introduces TimeInf, a novel method for estimating data contribution in time series datasets using influence functions. Unlike previous data contribution methods that primarily focus on i.i.d. settings, TimeInf specifically addresses the challenges of temporal dependencies in time series data. The method works by analyzing overlapping blocks of consecutive time points to preserve temporal structure, then uses influence functions to measure how individual time points impact model predictions. TimeInf's key innovation is its ability to integrate data values across consecutive time series observations while accounting for different temporal arrangements of data points. The authors demonstrate TimeInf's effectiveness through extensive experiments on real-world datasets, showing it outperforms existing methods in both identifying harmful anomalies and helpful time points for forecasting. The method is particularly noteworthy for its computational efficiency, interpretable results through visualizations, and strong performance in practical applications, while being theoretically grounded in robust statistics and autoregressive models.

### Strengths
The primary technical strength of TimeInf lies in its novel and theoretically sound approach to data contribution estimation in time series. It successfully extends influence functions to handle temporal dependencies, addressing a significant gap in time series analysis that previous methods overlooked. The method is built on a strong mathematical foundation combining robust statistics with innovative use of overlapping blocks to preserve temporal structure. This theoretical rigor is balanced with practical efficiency, as TimeInf proves to be computationally faster than deep learning alternatives while remaining scalable to large datasets with millions of time points. The method provides clear, quantifiable influence scores and intuitive visualizations that help users understand both anomaly patterns and forecasting behaviors. Its comprehensive evaluation across multiple real-world datasets demonstrates consistent improvement over existing approaches in both effectiveness and efficiency.

### Weaknesses
1. Methodological Limitations:
The paper’s core claim about their “distinctive integration” considering various temporal patterns seems to overlap significantly with existing attention mechanisms, without adequately differentiating itself. The theoretical justification for TimeInf lacks rigorous analysis of its properties, such as consistency or asymptotic behavior. Additionally, the paper doesn’t thoroughly explore the sensitivity of TimeInf to various hyperparameters, like block length or model architecture choices.
	2.	Experimental Issues:
The experimental setup, particularly for anomaly detection tasks, is not clearly described, making result reproduction challenging. The reported results differ significantly from those in original papers for baseline methods, raising questions about comparison fairness. Important baselines in time series anomaly detection such as MTAD-GAT[1], TransAD[2] are missing, limiting the ability to fully assess TimeInf’s performance relative to state-of-the-art methods.  [1] and [2] are using the unspervised learning to learn the distribution and don't use the "clean data assumption" as well. The paper also lacks a comprehensive evaluation of TimeInf’s interpretability claims compared to other approaches.
	3.	Limited Scope and Analysis:
While the paper focuses primarily on anomaly detection tasks, it’s not clear how well TimeInf generalizes to other time series tasks or domains. The computational complexity of TimeInf compared to existing approaches is not thoroughly analyzed, despite mentioning efficiency improvements through conjugate gradient and Hessian-free approaches. The paper lacks a thorough discussion of TimeInf’s limitations or potential failure cases, which is crucial for understanding when and where the method is most applicable. Lastly, the evaluation metrics used are standard (AUC and F1 score), but don’t consider other potentially relevant metrics for time series anomaly detection, such as detection delay or false positive rate at a fixed detection threshold.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents TimeInf, a data contribution estimation model for time series. TimeInf overcomes the traditional i.i.d. setting of influence functions, making it more suitable for time series data. By considering multiple time blocks, TimeInf captures contextual information within time series data. Additionally, its model-agnostic design enhances its versatility and flexibility.

### Strengths
+ TimeInf addresses the gap between existing data contribution methods and the unique requirements of time series data.
+ The proposed influence function is highly versatile, with multiple variants supporting diverse anomaly detection settings. Its model-agnostic nature further enhances its applicability across various models.
+ TimeInf is computationally efficient, leading to significant resource savings.

### Weaknesses
 + Some key mathematical terms in the paper could benefit from clearer explanations, such as $\delta_{x}[m]$ and $z^{[m]}$. Specifically, while $z^{[m]}$ is described as a block of m consecutive time points, the paper does not explicitly state whether this is a vector, a matrix, or a tensor, and what the dimensions represent. For $\delta_{x}[m]$, it is unclear what the notation implies about the distribution of the time block. Is it a Dirac delta function, and if so, what is the implication of using this in the context of time series data? The lack of clarity makes it difficult to fully grasp the mathematical formulation.
+ The paper lacks a clear mathematical definition of the task, especially regarding the tasks targeted by the variants of TimeInf, which could cause confusion. While the paper mentions anomaly detection, it does not formally define the objective function or the optimization problem being solved. Furthermore, it is unclear how the different variants of TimeInf are adapted for different tasks, and what specific mathematical modifications are required for each task.
+ Although the authors describe TimeInf as a data contribution estimation method, its task definition and benchmark choices make it appear primarily as an anomaly detection model. While data pruning experiments are provided in Appendix Section E, more direct evidence would help demonstrate that TimeInf goes beyond anomaly detection. The current experiments do not sufficiently demonstrate the method's ability to identify influential time points for tasks other than anomaly detection. The data pruning experiments, while suggestive, lack a direct connection to a clearly defined task beyond anomaly detection.
+ The comparisons would benefit from including more advanced anomaly detection algorithms [1], [2], [3]. The current benchmark set is not comprehensive enough to fully assess the performance of TimeInf against state-of-the-art methods. Specifically, the absence of recent deep learning-based anomaly detection methods limits the scope of the evaluation.
+ In Section 4.3, the authors attribute TimeInf's relatively poor performance in Table 4 to mislabeled ground truth annotations. However, they need to clarify why other benchmark models are unaffected by these mislabeled annotations. Demonstrating that other models do adhere to potentially mislabeled annotations would help validate this claim. It is not sufficient to simply state that the ground truth is mislabeled; a more rigorous analysis is needed to show that other models are indeed learning from these incorrect labels.

### Questions
+ Experimentally, TimeInf can effectively identify anomalies in time series. However, in the Data Pruning experiment, the authors claim that TimeInf can identify the most influential time patterns, which appears different from detecting anomalies (removing anomalies should not necessarily lead to a significant drop in model performance). Why is TimeInf able to identify influential time patterns at times, while it detects anomalies at other times? This seems somewhat contradictory.

[1]. Tuli S, Casale G, Jennings N R. TranAD: deep transformer networks for anomaly detection in multivariate time series data[J]. Proceedings of the VLDB Endowment, 2022, 15(6): 1201-1214.

[2]. Xiao C, Gou Z, Tai W, et al. Imputation-based time-series anomaly detection with conditional weight-incremental diffusion models[C]//Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 2023: 2742-2751.

[3]. Xu H, Wang Y, Jian S, et al. Calibrated one-class classification for unsupervised time series anomaly detection[J]. IEEE Transactions on Knowledge and Data Engineering, 2024.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces TimeInf, a model-agnostic data contribution estimation method for time-series datasets. It uses influence scores to attribute predictions to individual time points, preserving temporal dependencies. TimeInf shows effectiveness in detecting anomalies, providing interpretable attributions, and identifying mislabeled anomalies in ground truth.

### Strengths
The paper is well-organized with clear problem formulation and concise visualization. It effectively demonstrates the utility of TimeInf across multiple tasks, providing robust results on time-series datasets.

### Weaknesses
1.	My main concern is that while TimeInf is presented as a general model-agnostic method, the experiments in the main text focus solely on anomaly detection. It would be better to include more different tasks to support the advantage of this general method rather than only elaborate on one task. Specifically, the paper lacks a demonstration of TimeInf's applicability to tasks like time-series forecasting or classification, which are common in the field. The current focus on anomaly detection, while valuable, does not fully justify the claim of broad applicability. A more diverse set of experiments would strengthen the paper's claims.
2.	Table 2 contains misformatted bold values that do not reflect the best performance (UCR and SMAP’s F1).
3.	The data pruning experiments use non-standard time-series forecasting metrics; it will be better if more common metrics like RMSE and MAE can be considered. The current metrics make it difficult to compare the results with existing literature and to understand the practical implications of the data pruning method.

### Questions
1.	Can you elaborate on how TimeInf extends beyond the local historical context to capture a more global perspective as mentioned in Section 3?
2.	Following Q1, regarding Table 3, can you provide baseline comparisons to show the model’s advantages in capturing long-term dependencies?

### Soundness
3

### Presentation
2

### Contribution
2
