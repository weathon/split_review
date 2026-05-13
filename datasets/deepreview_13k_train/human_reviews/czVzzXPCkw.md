# ON EXTRAPOLATION IN MATERIAL PROPERTY REGRESSION

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
Deep learning methods have yielded exceptional performances in material property regression (MPR). However, most existing methods operate under the assumption that the training and test are independent and identically distributed (i.i.d.). This overlooks the importance of extrapolation - predicting material properties beyond the range of training data - which is essential for advanced material discovery, as researchers strive to identify materials with exceptional properties that exceed current capabilities. In this paper, we address this gap by introducing a comprehensive benchmark comprising seven tasks specifically designed to evaluate extrapolation in MPR. We critically evaluate existing methods including deep imbalanced regression (DIR) and regression data augmentation (DA) methods, and reveal their limitations in extrapolation tasks. To address these issues, we propose the Matching-based EXtrapolation (MEX) framework, which reframes MPR as a material-property matching problem to alleviate the inherent complexity of the direct material-to-label mapping paradigm for better extrapolation. Our experimental results show that MEX outperforms all existing methods on our benchmark and demonstrates exceptional capability in identifying promising materials, underscoring its potential for advancing material discovery.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
(Note: The reviewer does not have a background in material property prediction; thus, this review is based on informed estimates. The reviewer welcomes discussions and is open to adjusting scores or comments based on feedback from the authors and other reviewers.) 

The paper introduces a novel approach that reframes material-property regression (MPR) as a material-property matching problem, aiming to simplify target function complexity. This reframing addresses the difficulty neural networks face in capturing complex non-linearity beyond the training data, improving model extrapolation.

The core idea is that focusing on the proximity between material and property representations, rather than on precise value predictions, reduces learning difficulty and enhances extrapolation. The authors propose two objectives for learning aligned feature spaces for material-property representation matching. First, they use absolute matching optimization with a negative cosine similarity loss to pull paired material and label representations closer together. Second, the method employs Noise Contrastive Estimation (NCE) to help the model distinguish target from noisy labels, thereby capturing fine-grained relative matching relationships.

Within these well-aligned latent spaces, the proposed method (MEX) predicts by optimizing for the nearest target value for a given sample. Experiments demonstrate that MEX not only performs best on the benchmark but also shows strong detection capabilities for promising materials, underscoring its extrapolation potential and suitability for robust material discovery.

------
While reading this paper, I hypothesized that the label encoder could easily overfit to the training data, effectively reducing it to a look-up table and thereby losing any extrapolation capability. However, this risk may be mitigated by the inclusion of a noisy label component, which introduces stochasticity to the model, reducing its tendency to overfit. And the Gaussian applied to the label likely encourages continuity in the label space, which could help to foster the model’s extrapolation abilities.

### Strengths
•	The approach addresses a significant problem in material property prediction.

•	The results look promising

### Weaknesses
•	Dataset Limitations: The dataset is small and simplistic, limiting the evaluation of the method's effectiveness. The number of samples (ranging from 4,764 to 18,982) is limited, and details about the dimensionality of data points are not provided. Additionally, the design of y target $y_{\text{target}}$, as described in section 3.1, seems unrealistic since the training and target data are entirely disjoint. This choice could disadvantage baseline methods.

•	Baseline Choice: The Deep Imbalanced Regression (DIR) technique is designed for handling imbalanced data distributions with underrepresented target values. However, the proposed dataset’s disjoint target-training setup may hinder DIR’s performance. DIR methods are not specifically tailored for extrapolation, which is central to this work, making it challenging to evaluate against MEX.

### Questions
1.	Could the authors clarify the Geometric Mean metric to aid readers unfamiliar with it?
2.	In Figure 6, the performance seems to decrease as $\lambda$ increases, suggesting that NCE might negatively impact results. Could the authors explain this trend?
3.	The authors claim that the matching-based approach enhances extrapolation, but how does this method handle out-of-distribution data or outliers? Can contrastive learning effectively handle these cases? 
4.	Could the authors consider an additional setting where the target and training data overlap slightly, such as by adding extreme high or low values to the training set, to simulate an imbalanced distribution?
5.	How well does the method scale with higher-dimensional targets?
6.	Is there a threshold in the matching function M(x, y) to determine when a match is strong enough?
7.	How does the model avoid overfitting in the label encoder, potentially transforming it into a look-up table? Does the noise component mitigate this risk, supporting extrapolation?
8.	While $y^*$ is estimated via Monte Carlo sampling, could gradient-based methods be viable for this estimation? 
9.	What is the dimensionality of the input data sample x?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the challenge of extrapolation in material property regression. Existing deep learning models for MPR assume that the training and test data follow similar distributions, thus limiting their ability to make predictions beyond the known range. To address this issue, the authors introduce the Matching-based Extrapolation (MEX) framework that reframes MPR as a material-attribute matching problem.MEX employs both absolute and relative matching objectives to optimize the consistency of the material and attribute representations, thereby facilitating better extrapolation of material property predictions. The authors also develop a new benchmark.

### Strengths
- Originality:
  - Novel perspective of material property prediction. Reframe the task as a material property matching problem.
- Quality:
  - A new benchmark is constructed and a new framework is proposed to address the critical problem of out-of-domain material property prediction.
- Clarity:
  - Most of the paper is clearly presented, with some details that should be explained more clearly. The section on noise contrastive estimation-based optimization.
- Significance:
  - The problem is critical for new material discovery. The benchmark provides an important validation of the OOD material property prediction problem.

### Weaknesses
 - Limited novelty in method.
  - The key components, NCE, and cosine similarity-based matching are well-known techniques.
- scalability and computational complexity
  - The MEX framework’s inference requires iterative candidate label refinement, which introduces considerable computational overhead compared to traditional regression methods.
- Experiments
  - Traditional methods, like DFT, are supposed to be compared to find the gap between DL-based extrapolation and traditional methods.
  - More DL-based methods should be compared to provide evidence that previous works lack the generalization of OOD properties.

### Questions
- Dataset
  - The diversity of the dataset, for example, the distribution of atom numbers and the lattice constants, etc.
- Matching choice
  - Are there any insights into adapting Noise Contrastive Estimation (NCE) instead of other methods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The author addresses the issue of material property regression, focusing specifically on regression problems where the feature values lie outside the boundaries of the training set.
The author performs the regression task using two encoder models: (1) an encoder for material properties and (2) an encoder for target values.
Finally, using Monte Carlo sampling, the model outputs target values that can yield features most similar to the object properties within the given boundary.
The author structured the dataset using Matminer ensuring that the target values in the training and evaluation environments do not overlap.
The proposed method achieved a high level of performance compared to other methods.

### Strengths
The problem setting proposed by the author is, to some extent, justifiable, and within this setting, the author presents a state-of-the-art algorithm.

### Weaknesses
(1) Narrowly defined problem:
The experimental setting proposed by the author is highly narrow in scope.
An algorithm that performs well only within the proposed setting does not provide insight into whether it effectively considers material properties within the boundaries of the training data.
Furthermore, the experimental setting proposed by the author appears highly challenging, and the actual MAE values are relatively large compared to the target values.
Therefore, it is difficult to conclude that the author has sufficiently demonstrated the practicality of the proposed method.

(2) Main method which lacks novelty and analysis:
Specifically, it is challenging to discern any reasonable approach proposed by the author for addressing extrapolation.
The two matching optimizations proposed by the author are both methods aimed at accurately predicting the given labels in the training set.
The author utilizes MC sampling to identify target values outside the range of the training set; however, it is unclear whether the encoding of target values beyond the training range has been effectively learned.
This suggests that the algorithm "may" achieve high performance if there is significant variance in the value encoder, hyperparameters, and other factors.
Therefore, to verify the extrapolation performance of the proposed method, the author should present additional ablation studies.

(3) Lack of fairness:
First, there is a question regarding the author’s validation setting.
It is unclear why the target value range is the same in both the test and validation environments.
Second, the author is aware of the lower and upper bounds of the label range but does not address the issue of setting these bounds beyond the range of the test set.
This strongly conflicts with the motivation for extrapolation that the author discusses.
Lastly, the author does not provide the hyperparameter search space for the comparative methods.
These are details that should be explicitly documented if new training was conducted on a new dataset.

### Questions
The first question concerns whether the practicality of the author’s method can be extended.
Naturally, defining the boundary of target values in the training set is highly unnatural.
It is natural for materials with target values similar to those of a new material to be sparsely represented.
This implies that the author’s algorithm should also be capable of addressing imbalanced regression problems.
Can the author demonstrate the effectiveness of this algorithm on established imbalanced regression benchmarks or in environments where labels are sparsely shared between the training and evaluation sets?
If feasible, the author should suggest providing a rigorous comparison framework to ensure fairness, as discussed in the weaknesses section.

The second question is whether the author can explain how the method intuitively aligns with the concept of extrapolation.
Whether through theoretical or experimental approaches, it is essential to establish confidence that this method genuinely addresses the MPR problem with consideration for extrapolation.

### Soundness
2

### Presentation
2

### Contribution
1
