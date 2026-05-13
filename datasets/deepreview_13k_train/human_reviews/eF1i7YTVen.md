# COPU: Recognizing Time Series' Heterogeneity In Stacked Neural Network

- Decision: Reject
- Scores: 6, 6, 3, 6

## Abstract
Neural networks (NNs) have been widely studied in complex fields due to their remarkable capacity for nonlinear modeling. 
However, in the realm of time series analysis, researches indicate that merely stacking NNs does not yield promising nonlinear modeling outputs and hinders model performance. Conventional NN architectures overemphasize homogeneous feature extraction, impeding the learning of diverse features and diminishing their nonlinear modeling capability. To address this gap, we propose the $\textbf{C}$ross-correlation Enhanced Approximated $\textbf{O}$rthogonal $\textbf{P}$rojection $\textbf{U}$nit (COPU) to quantify and augment the NN's nonlinear modeling capacity. COPU efficiently computes the local cross-correlation characteristics between features, amplifying heterogeneous components while compressing homogeneous ones. By reducing redundant information, COPU facilitates the learning of unique and independent features, thereby enhancing nonlinear modeling capability. Extensive experiments demonstrate that our method achieves superior performance across two real-world regression applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper, titled COPU: Recognizing Time Series' Heterogeneity in Stacked Neural Network, addresses limitations in traditional neural network (NN) architectures when applied to time series data. The authors propose the COPU (Cross-correlation Enhanced Approximated Orthogonal Projection Unit), a new framework designed to enhance the NN's nonlinear modeling capabilities by emphasizing heterogeneous features. Traditional NN structures often focus on homogeneous feature extraction, which limits their performance on time series data where diverse feature extraction is essential. The COPU framework uses the Rank Ratio (RR) metric to measure the model's ability to capture unique information, enhancing heterogeneous components while compressing homogeneous ones. Experimental results demonstrate that COPU significantly outperforms existing NN structures in capturing nonlinear patterns, especially in time series datasets like SRU.

### Strengths
Timely and Novel Research Direction: In time series forecasting research, most studies have traditionally focused on increasing model capacity. This paper takes a novel approach by addressing time series analysis from a fresh perspective that emphasizes data-specific structural improvements. This unique angle offers high novelty by shifting from merely increasing the capacity of NNs to a more data-driven design that aligns closely with the characteristics of time series data.

Innovative Methodology: COPU stands out for emphasizing heterogeneous over homogeneous elements in the data, which is well-suited to the nature of time series data. Unlike previous studies that focus on extracting homogeneous features, this paper proposes the Cross-correlation Enhanced Perceptron (CEP) to align features based on their correlations, suppressing redundant homogeneous information while amplifying unique features. This approach enhances the NN's ability to capture nonlinear aspects effectively, making it highly suitable for time series analysis.

Performance and Stability: COPU demonstrates superior performance compared to traditional NN structures, especially in terms of capturing diverse features without overfitting. This model excels in real-world scenarios by effectively learning complex and varied representations in time series data, showcasing both stability and robustness.

### Weaknesses
Limited Applicability: COPU is specifically designed for time series data, which could restrict its application across different data types, such as image or text data. Although the focus on time series data is intentional, this may limit its adaptability to more general purposes. The lack of exploration into how the core concepts of COPU, such as the Rank Ratio (RR) metric and the Cross-correlation Enhanced Perceptron (CEP), might be adapted or extended to other data modalities is a significant limitation. For instance, the time-frequency conversion inherent in CEP might not be directly applicable to non-sequential data, and the RR metric's effectiveness in measuring the heterogeneity of features in other domains is unclear.

Model Complexity: The architecture of COPU, particularly with CEP integration, is relatively complex, potentially requiring more computational resources than conventional NN models. This complexity could present challenges for implementation, especially for large-scale datasets or real-time applications. The paper does not provide a detailed analysis of the computational overhead introduced by the CEP, making it difficult to assess the practical feasibility of the model in resource-constrained environments. Furthermore, the optimization of the model's hyperparameters, especially those related to the CEP, could be more challenging due to the increased complexity, potentially leading to longer training times and higher computational costs.



### Questions
Generalizability of the RR Metric: The paper shows that RR is effective for assessing nonlinear modeling capabilities in time series data, but it is unclear if RR can be reliably applied to other data types (e.g., continuous vs. discrete time series, multimodal data).

Balancing Homogeneous and Heterogeneous Elements: While the approach of suppressing homogeneous features and amplifying heterogeneous ones is innovative, the paper does not detail how the balance between these elements impacts performance. More insight into how this balance can be adjusted and its effect on model performance would be valuable.

Effect of Stack Depth on COPU’s Performance: Although increasing the depth of COPU stacks improves performance, the model exhibits diminishing returns at higher depths. It would be helpful to have guidelines on optimizing stack depth for this model.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new neural network component, called the cross-correlation Enhanced Perceptron (CEP), to solve the difficult problem of nonlinear modeling in time series analysis. CEP facilitates the learning of unique features by performing alignment and cross-correlation calculations on input features in a single step to distinguish and amplify different features while suppressing the influence of similar features. To further improve the model performance, the authors integrate CEP into the approximate orthogonal projection unit (AOPU) to form the COPU framework. COPU uses CEP to enhance nonlinear modeling capabilities and solves the limitations of AOPU in computational accuracy and expressiveness. The experimental results show that COPU is significantly superior to the existing methods in several real regression tasks. The contribution of this paper is to develop a CEP component specially used in time series analysis, which provides a new idea for feature modeling in a specific domain. At the same time, the authors also focus on an evaluation metric Rank Ratio (RR), because it can be interpreted as the proportion of linear dependencies that are translated into independence by neural networks.

### Strengths
1. The author clearly demonstrates the problem that this paper aims to solve: that complex networks can effectively solve problems related to computer vision and natural language processing; But its ability to solve the problem of time series analysis is insufficient.
2. The author proposes a CEP scheme, which quantifies the similarity between features through Cross-correlation to ensure alignment without directly ignoring differences in time, which is quite innovative.
3. The author summarized relevant literature, explained the characteristics of time series analysis problems, and proposed that RR index has a good evaluation significance in measuring time series analysis problems, and this index can be relatively convincing in the subsequent research
4. The author cited sufficient literature to demonstrate the point of view, and designed ablation experiments to enhance feasibility.

### Weaknesses
1. The advantages of indicator RR compared with other common indicators are not fully elaborated. While the paper introduces RR as a metric that reflects the proportion of linear dependencies transformed into independence, it does not sufficiently justify why this is a superior measure compared to established metrics like Mean Squared Error (MSE), Mean Absolute Error (MAE), or even metrics specific to time series forecasting such as Root Mean Squared Error (RMSE) or dynamic time warping (DTW). A more rigorous comparison, including a discussion of the limitations of these other metrics in the context of the specific problem, is needed to fully justify the choice of RR.
2. The relationship between CEP and COPU is not clearly stated, and it should be explained in detail how to achieve it. The paper describes CEP as a component that enhances feature learning through alignment and cross-correlation, and COPU as an integration of CEP into the AOPU framework. However, the precise mechanism of this integration is not clearly articulated. It is unclear how the cross-correlation outputs of CEP are used within the AOPU framework, and how this integration specifically addresses the limitations of AOPU. A more detailed explanation of the data flow and mathematical operations involved in the integration of CEP into AOPU is needed.
3. The datasets used in the experimental design are insufficient, and more datasets are recommended to be added for verification. The paper's experimental validation is limited to a small number of datasets, which may not be representative of the broader range of time series analysis problems. To demonstrate the generalizability of the proposed COPU framework, it is necessary to evaluate its performance on a more diverse set of datasets, including those with different characteristics (e.g., varying lengths, noise levels, and underlying patterns).
4. In terms of experimental Settings, the author should provide setting parameters of different networks to compare the results more reasonably. The paper mentions that the hyperparameter settings of comparative models are consistent with COPU, but does not provide the specific values of these parameters. Without this information, it is difficult to assess whether the comparison is fair and whether the performance differences are due to the proposed method or simply to differences in hyperparameter tuning. The paper should include a table or appendix detailing the specific hyperparameter settings used for each model.

### Questions
1. In the design process of CEP, why may the c value be negative? Why is it feasible to use sigmoid to force a negative number to be positive?
2. Does the CEP module have to be fixed with your network structure or can it be embedded in other models as well?
3. Will the paper provide code? I want to know about the implementation of CEP and COPU.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper think that conventional NN architectures overemphasize homogeneous feature extraction, impeding the learning of diverse features and diminishing their nonlinear modeling capability. To address this gap, they propose the Cross-correlation Enhanced Approximated Orthogonal Projection Unit (COPU) to quantify and augment the NN’s nonlinear modeling capacity.

### Strengths
They introduced RR as a metric to quantify the proportion of linear dependencies transformed into independence by the network. Performing a comprehensive exploration of NN’s nonlinear modeling capability.  This paper proposes a new NN component termed CEP that has strong nonlinear representation performance in time series analysis and serves as the foundation for developing the COPU framework.

### Weaknesses
1.  In page 1, the author said :  For these methods to be effectively applied in this field, it is
essential to recognize that time series has more ambiguous discriminative patterns than other forms
like images and text (Alec et al., 2021). Such ambiguity hinders the model’s ability to extract diverse
features from the input, obstructing its capacity for nonlinear modeling.

Then you give simple explanation, but the problem is you explanation is wrong. You classify original text and image data, while you do convoltuion on timeseries dat, and then you said "it is more challenging to discern the effect of two input sequences on the output
of a system". That is not resonable.


2. Some sentence is hard to understand like:
Page 7: This offers a novel perspective that elucidates the underlying efficacy of residual connections in NNs beyond the kernel (Duvenaud et al., 2014) and gradient (Kaiming et al., 2016) explanations.

3. In Figure 7, except for layer 7, it is hard for me to find difference CEP and other method, and I think with the iteration, the CEP curve will  close to other curve in the end.

4. You need to add explanation to different lines in Figure 8.

5. Last and most important Problem:
You propose a new method to solve the problem in time series prediction, but you did not conduct experiments on popular dataset and compare with some current SOTA models, like you refered in your paper : Are transformers effective for time series forecasting?

### Questions
The same to Weaknesses

### Soundness
2

### Presentation
2

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
In this paper, the authors present an approach called Cross-correlation Enhanced Approximated Orthogonal Projection Unit (COPU) to quantify and augment a neural network’s (NN’s) nonlinear modeling capacity. The authors motivate their approach based on the observed inability of NNs to learn diverse features and effectively perform nonlinear modeling. The proposed method amplifies heterogeneous components and reduces homogeneous ones, enabling the learning of unique and independent features, thereby enhancing the NN's nonlinear modeling capability.

### Strengths
- The authors motivate the proposed approach using realistic examples.

- They propose using rank ratio as a metric for measuring nonlinear modeling capability.

- Experiments conducted on real world datasets.

### Weaknesses
 - The presentation of the paper is quite confusing. There are several mistakes, such as Eq. (6) not being referenced anywhere, and in line 251, the notation "x \in \mathbb{R}^{d,b}" is unclear. Additionally, there are several sentences that are difficult to follow.
For example: 

- "This process enables the differentiation between redundant information and innovation, further suppressing homogeneous information among features while amplifying their differences"
what innovation means here?

- "while the augmentation modular focuses on diverse and informative feature extraction"
module?

- "We implement this approach by  employing dictionary lookup Ashish et al. (2017) to achieve feature mapping."
wrong reference type.

- Using scientific notation for MAPE (which is typically presented as percentage) is also confusing.	

- S4 acronym not introduced.

These are just a few examples, but there are numerous similar presentation issues throughout the paper, making it very difficult to follow. This is a significant shortcoming in itself, bringing the paper below ICLR  standards.

- Results on standardized and well-known datasets are expected to support the authors' claims and facilitate the reproduction of the presented results.

- In many cases, an MLP performs similarly to (or better than) the proposed approach, raising questions about the actual difficulty of the datasets used in the evaluation and whether the results truly support the authors' claims. The authors should also provide the results of a linear model to highlight the necessity of modeling non-linear components.

### Questions
Overall, the paper is not yet ready for publication. Significant improvements are required in both the presentation and the experimental setup and evaluation in order to adequately support authors' claims. While the authors are welcome to respond to these shortcomings, I believe the issues are too fundamental to be addressed through a rebuttal alone and will likely require a major revision of the paper.

### Soundness
2

### Presentation
1

### Contribution
2
