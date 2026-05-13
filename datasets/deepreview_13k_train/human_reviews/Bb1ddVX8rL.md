# Legendre-KAN : High Accuracy KA Network Based on Legendre Polynomials

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
Recently, the Kolmogorov-Arnold Network (KAN) has been proposed,
   significantly outperforming MLP in terms of interpretability and symbolic representation.
   In practice, KANs are required to fit data to extremely high precision.
   For instance, in typical applications of KAN like inferring precise equations from data and serving as solvers for partial differential equations,
   high accuracy is an intrinsic requirement.
   In the current architecture of KAN,
   cubic B-spline basis functions were selected as the approximate tools.
   However, the inflexibility of fixed degree and knots in B-splines restricts
   the adaptability of the activation functions.
   Due to these inherent limitations of B-spline functions,
   especially low-order and homogeneity, KAN still has room for improvement in accuracy.
   In this paper, we propose the Legendre-KAN that can enhance the
   degrees of freedom of the basis functions in the KAN.
   Compared to the traditional Spline-KAN,
   Legendre-KAN utilizes parameterized Legendre basis functions and
   normalization layers at the edges of the KAN.
   Benefiting from higher-order orthogonal polynomials,
   Legendre-KAN significantly outperforms the Spline-KAN in terms of accuracy.
   Extensive experiments demonstrate that Legendre-KAN achieves higher accuracy
   and parameter efficiency, of which accuracy reaches 10-100 times that of Spline-KAN in some cases.
   For those functions which can be symbolized,
   this leads to more correct results as opposed to Spline-KAN.
   Our approach effectively improves the accuracy of the mathematical relationships
   in KANs, providing a better solution for approximating and analyzing complex nonlinear functions.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors introduce a new network called Legendre-KAN, which combines Legendre polynomials with the Kolmogorov-Arnold (KA) theorem. The motivation behind this development is that the standard Kolmogorov-Arnold Network (KAN), due to the inherent limitations of B-splines, cannot sufficiently reduce training error for complex tasks such as solving partial differential equations. The authors conduct a series of experiments in the field of symbolic regression to demonstrate that their approach outperforms both KAN and MLP in terms of test loss when fitting the equations.

### Strengths
- The Legendre-KAN achieves lower test set losses on a set of symbolic expressions compared to the standard KAN.
- The authors provide an extensive overview of the method.

### Weaknesses
 - The current results are limited to only a small set of equations. In the field of symbolic regression, there are well-established benchmarks, such as SRBench and SRSD, on which novel approaches are typically tested. The authors should test on these benchmarks.
- No analysis with noise is performed.
- It is unclear what scientific contribution this approach brings. If the authors present this work as a contribution to symbolic regression, they should test it against strong and well-established baselines (such as Operon, DSR, and Neural Symbolic Regressors) rather than only KAN. Alternatively, if the authors are focusing solely on the KAN comparison, they should explain why they chose the symbolic regression task and what better performance on this task implies.

### Questions
- Do you have any performance improvements in non-symbolic regression tasks compared to KAN? For example, in the abstract, you mention solving partial differential equations, and in your related work, you mention approaches where KAN has been used in the context of Graph Neural Networks and Transformers. Did you test your approach on these tasks and settings?
- What do the terms “time ratio,” “Equal params,” “best k/grid,” and “best k” mean in the tables?

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes a new variant of the Kolmogorov-Arnold Network (KAN) called Legendre-KAN, designed to improve the accuracy of symbolic representation and function approximation. The main advancement here is the replacement of the traditional B-spline basis functions in KANs with parameterized Legendre polynomials, which offer higher degrees of freedom and are known for their global approximation capabilities and numerical stability.

### Strengths
The shift from B-splines to Legendre polynomials appears well-motivated, and the results convincingly show an increase in accuracy for small problems.

### Weaknesses
1. There have been several KAN alternatives proposed at this point -- Fourier KANs, Wavelet KANs, RBF KANs, etc. There are no comparisons to those alternatives.
2. The paper starts with mention of areas which require high accuracy and precision, however the target experiments are extremely small scale. Even the "complex" nonlinear functions are simple polynomials where no-one uses neural networks for approximation.

### Questions
See limitations for the main issues with the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes Legendre-KAN, a variant of the Kolmogorov-Arnold Network (KAN) that integrates Legendre polynomials into the activation functions to improve performance. By utilizing Legendre basis functions, along with skills such as normalization and reduced initialization parameters, the authors aim to enhance the accuracy and parameter efficiency of KAN in symbolic representation tasks. Empirical evaluations demonstrate that Legendre-KAN achieves better fitting accuracy compared to the standard KAN.

### Strengths
•	Incorporating Legendre basis functions into KAN is a novel approach that appears to contribute positively to the network's performance.
•	The empirical results seem to show that Legendre-KAN results in improved fitting accuracy.

### Weaknesses
•	The paper lacks a theoretical analysis to substantiate why Legendre polynomials outperform B-spline functions. The choice of Legendre polynomials appears somewhat arbitrary without a deeper justification of their suitability for this task compared to other basis functions. A more rigorous analysis, perhaps involving a comparison of their approximation properties or convergence rates in the context of KANs, would strengthen the paper.
•	There are grammatical errors and incomplete sentences in the manuscript, notably in Section 3.1, which impede comprehension. The lack of clarity in the writing makes it difficult to fully grasp the nuances of the proposed method and its implementation. This issue needs to be addressed to ensure the paper is accessible and understandable to the broader research community.
•	The evaluation is confined to symbolic representation tasks. While recent study shows that KAN is found to be better than MLP only in symbolic formula representation, but still inferior to MLP on other tasks such as machine learning, CV, NLP and audio processing. It would be more convincing if the proposed method with KAN and MLP could be tested on tasks other than symbolic representation. The paper should explore the performance of Legendre-KAN on more diverse tasks to demonstrate its general applicability and robustness.
•	The structure of the paper is somewhat disorganized, with experimental results appearing in sections typically reserved for background and methodology. This makes it difficult to follow the logical flow of the paper and understand the motivation behind the experiments. A clearer separation of methodology and results would improve the readability of the paper.

### Questions
•	A deeper theoretical comparison of Legendre polynomials and B-spline functions is necessary to strengthen the argument for the proposed method.
•	Test the proposed method on additional tasks beyond symbolic representation to demonstrate its effectiveness in other domains and strengthen the overall claims.
•	Improve the clarity and grammatical correctness of the writing to better convey the proposed method's details and implications.
•	Enhance the descriptions in figure captions for clearer understanding.
•	Enhance the clarity of the figures, especially Figure 6, and ensure that all labels and legends are accurate. For instance, the labels in Figure 4b appear to be reversed.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The Kolmogorov-Arnold Network (KAN) has been proposed as a significant improvement over MLPs in terms of interpretability and symbolic representation. However, in this paper, researchers have identified issues with the cubic B-spline basis functions used in KAN, specifically their inflexibility due to fixed degrees and knots. As a result, KAN struggles to reduce training error to the precision required for scientific research, leading to mathematical expressions that differ greatly from the true function, thereby limiting its practical applications.

To increase the flexibility of the basis functions in KAN, this paper introduces Legendre-KAN, which employs parameterized Legendre basis functions and normalization layers at KAN's edges. Extensive experiments show that Legendre-KAN achieves 10-100 times greater accuracy than KAN in symbolic representation tasks and in fitting complex nonlinear functions that cannot be easily symbolized. This improvement enhances the accuracy of mathematical relationships within KANs, offering a more effective solution for approximating and analyzing complex nonlinear functions.

### Strengths
1. Researchers replaced the B-spline basis functions with Legendre polynomials in KAN, introducing Legendre-KAN. They highlight several benefits of using Legendre polynomials: (1) Legendre polynomials have a global polynomial function approximation space; (2) With higher order, Legendre polynomials can capture more complex patterns and relationships within the data; (3) By applying appropriate orthogonalization, Legendre polynomials are numerical stable.
2. Two technique trick to improve network: (1) Add a normalization layer to normalize the input activation values of each layer to interval $[0,1]$, which unifies the form of each layer's basis function. (2) Use smaller initialization parameters in order to solve the problem of gradient explosion.
3. Experiments in both symbolic representation tasks and fitting complex nonlinear functions that cannot be easily symbolized shows that Legendre-KAN outperforms KAN with 10-100 times greater accuracy.

### Weaknesses
1. Lack of detailed and reasonable explanations in section 2.2 "B-spline functions and its fitting characteristic". 
	(1) In line 196, figure 3 and figure 4 are used to support the claim "spline functions perform well in smooth regions but may introduce significant errors in certain areas". However, there are two questions. First, figure 3 and figure 4 contradict each other in multiple places: in figure 3(b), Legendre polynomials fits better than B-spline, while in figure 4(b) it is the opposite; in figure 3(c), B-spline fits well, which is inconsistent with figure 4(c). Second, the term "certain areas" is vague, leading to confusion about attributing "significant errors" to the localized fitting caused by piecewise spline functions in the following sentences. The inconsistency between figures and the vague description of "certain areas" undermines the argument about B-spline limitations. The analysis lacks a clear definition of the specific characteristics of these "certain areas" where B-splines fail, making it difficult to understand the core issue.
	(2) This part identifies the main drawback that the spline function is localized and piecewise polynomials. However, it is summarized as "the activation functions with lower degrees of freedom prevents Spline-KAN from producing accurate results" in line 254. The conception of "degrees of freedom" and the relationship among "local/global", "order of polynomials" and "degrees of freedom" are confusing. The paper does not clearly explain how the localized nature of B-splines directly translates to a lower degree of freedom in the context of function approximation. The connection between these concepts needs to be more rigorously established, as simply stating a lower degree of freedom is insufficient without explaining its implications on the approximation space.
2. Architecture of Legendre-KAN is missing some key information. It is not clearly specified which module is inherited from KAN and which is modified, or which settings follow KAN and which changes. For instance, in line 352, it is mentioned that "we also combined the best-performing $b(x) = SILU (x)$ with the Legendre basis to enhance the smoothness of the high-order polynomial fitting results." However, it is not clarified the use of SiLU function has already been in the KAN. The paper should explicitly state which components of the original KAN architecture are retained and which are replaced or modified in Legendre-KAN. The lack of clarity makes it difficult to understand the precise architectural differences and the specific contributions of the proposed modifications. Furthermore, the role of the SiLU activation within the original KAN needs to be clarified to understand the novelty of its combination with Legendre basis.
3. Some irregularities in the paper writing.
	(1) Lack of definition or repeated definition for the symbols used in the paper. In line 113, a theorem is quoted, but none of the symbol is defined. Meanwhile, same symbols are used in section 3.2 of totally different meanings. Also, in figure 2(a), symbol $B$ with subscript is never defined in the paper. The inconsistent use and lack of definitions for mathematical symbols throughout the paper creates ambiguity and makes it difficult to follow the technical arguments. The paper needs a consistent notation system and clear definitions for all symbols, especially when they are used in different contexts.
	(2) Figures and tables lack brief explanations typically provided below them to aid understanding. The absence of captions or brief explanations for figures and tables makes it challenging for the reader to quickly grasp the key information being presented. Each visual element should be accompanied by a concise description of its purpose and the main insights it conveys.
	(3) Some writing details such as spelling and punctuation errors. For example, "worse" is spelled as "wrose" in line 257 and a sentence ends with a comma in line 274.

### Questions
See Weakness

### Soundness
2

### Presentation
1

### Contribution
3
