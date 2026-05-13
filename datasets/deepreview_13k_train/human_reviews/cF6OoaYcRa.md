# Calibrated Physics-Informed Uncertainty Quantification

- Decision: Reject
- Scores: 6, 3, 3, 6

## Abstract
Neural PDEs have emerged as inexpensive surrogate models for numerical PDE solvers. While they offer efficient approximations, they often lack robust uncertainty quantification (UQ), limiting their practical utility. Existing UQ methods for these models typically have high computational demands and lack guarantees. We introduce a novel framework for calibrated physics-informed uncertainty quantification to address these limitations. Our approach leverages physics residual errors as a nonconformity score within a conformal prediction (CP) framework. This enables data-free, model-agnostic, and statistically guaranteed uncertainty estimates. Our framework utilises convolutional layers as finite difference stencils for gradient estimation, our framework provides inexpensive coverage bounds for the violation of conservation laws within model predictions. In our experiments, we utilise CP to obtain marginal coverage for each cell and joint coverage over the entire prediction domain of various PDEs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a data-free conformal prediction approach for uncertainty quantification in neural PDE solvers, which does not require additional true PDE solutions to evaluate nonconformity scores. This data-free capability is achieved by assessing physics residual errors (PRE), or violations of conservation laws, for each prediction. PRE-CP provides both marginal (dimension-wise) and joint (domain-wide) coverage, enabling statistically sound conformal bounds for predictions. Additionally, the authors employ convolutional layers as finite difference stencils for faster and more accurate gradient estimation, as well as a rejection sampling method that uses CP-based criteria to reject predictions with a predetermined probability.

### Strengths
•	Very interesting and important topic for SciML community and very well written

•	Strong motivation

•	Complete experiments and discussion with strong empirical results

•	Methods are clearly written and are easy to follow

### Weaknesses
I have some question regarding how will PRE-CP behave when the neural model fails to predict PDE solution, or generating consistently high physical residual errors.

### Questions
Krishnapriyan et al. [1] show that it is highly likely for PINNs to fail in predicting PDE solutions when the PDE coefficients are high, which can lead to consistently high residual errors across almost the entire PDE domain. I am curious whether PRE-CP would generate very wide conformal bounds that still provide relatively high coverage of these residual errors, potentially underestimating the poor performance of the neural solver.

[1] Krishnapriyan, Aditi, et al. "Characterizing possible failure modes in physics-informed neural networks." Advances in neural information processing systems 34 (2021): 26548-26560.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposed to use a conformal prediction (CP) framework to estimate uncertainty in neural PDEs. The main proposal of the paper is the utilisation of physics residual errors as nonconformity scores within a CP framework. The main goal of the paper is to provide a fast uncertainty quantification framework for neural PDEs. The proposed method is illustrated on several toys examples.

### Strengths
If demonstrated more extensively through additional experiments and theoretical results, the paper potentially provides a computationally cheap uncertainty quantification framework for neural PDEs.

### Weaknesses
 - At the current moment, the paper provides only a minor extension of the CP framework to the context of neural PDEs.
- There are no theoretical results in the paper supporting claims about bounds and statistical guarantees. 
- The experiments are limited to several toy problems with only illustrative examples (and no simulation study with diverse/relevant evaluation metrics, such as l2 measure for the solution, coverage for the quality of CI, etc.). 
- There is no comparison to any other uncertainty quantification methods.

- The statement regarding Bayesian methods lacks specific details about their limitations. The authors should clarify what specific guarantees these methods fail to provide that conformal prediction does offer, particularly in the context of neural PDE solvers.
- The paper does not adequately distinguish between epistemic and aleatoric uncertainties, and it needs to be more precise about the type of uncertainty being quantified. The current discussion is vague and does not provide a clear understanding of the nature of the uncertainty being addressed.
- The claim on line 155, stating the introduction of a novel data-free nonconformity score for CP to obtain statistically valid and guaranteed error bounds, lacks theoretical support. The paper needs to provide a rigorous mathematical justification for this claim.
- Figures 4 and 5 show confidence intervals that appear too large for 95% coverage, and the marginal CP coverage is difficult to assess visually. The paper should include quantitative metrics to properly evaluate the coverage and calibration of the method, rather than relying solely on visual inspection.
- The paper presents only single illustrative examples in Figures 4 and 5, rather than a Monte Carlo study, which is needed to properly demonstrate the calibration and coverage of the method. Given the claim of computational efficiency, more extensive results are expected.
- The absence of comparisons to other uncertainty quantification methods makes it difficult to assess the relative performance and advantages of the proposed approach.

### Questions
1)“The majority of literature in UQ for neural PDE solvers has been looking at Bayesian
methods, such as dropout, Bayesian neural networks and Monte Carlo methods (Geneva & Zabaras, 2020; Zou et al., 2024; Psaros et al., 2023), which lack guarantees or are computationally expensive.”  
This statement is rather high-level. The authors should specify what guarantees these methods do not provide which conformal prediction does provide. 
2) The paper does not distinguish between epistemic and aleatoric uncertainties and should be more explicit and precise about what type of uncertainty quantification it provides. 
3) On line 155 there is a claim: “We introduce a novel data-free nonconformity score for Conformal Prediction (CP) to obtain statistically valid and guaranteed error bounds for neural PDE solvers.”
Theoretical support should be provided to this claim. 
4) Both Figure 4 and Figure 5 illustrate very large confidence intervals for joint CP which would not correspond to 95% coverage. For marginal CP, it is hard to visually tell what coverage is. The same holds for the later figures. The paper should provide additional metrics to evaluate the results quantitatively. 
5) Figure 4 and 5 provide a single illustrative example and not a proper Monte Carlo study to illustrate the calibration and coverage of the method. Considering that the paper suggests the method is computationally cheap, there is no reason to not provide more extensive results supporting the paper's claims. 
6) There is no comparison to any other uncertainty quantification methods.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper uses physics residual errors as nonconformity scores within a conformal prediction framework for efficient and calibrated uncertainty quantification in neural PDEs.

### Strengths
The paper is clearly written and easy to understand.

### Weaknesses
1. The proposed method appears relatively simple and lacks novelty. Using the Physics Residual Error as a nonconformity score for conformal prediction seems to be a minor contribution.
2. The paper lacks a comparison with other uncertainty quantification (UQ) methods. I think various UQ methods could be applied based on the point-wise PDE residuals.
3. Additional analytical experiments are necessary to gain a deeper understanding of the proposed method. Could you conduct some tests in real-world scenarios?
4. The numerical PDE residual shows considerable numerical error due to discretization issues, particularly in 2D+time PDEs. How is the time derivative calculated over a 20-frame sequence? Please provide further clarification.

### Questions
See Weaknesses

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a method to quantify the prediction uncertainty of a data-driven neural PDE solver using conformal prediction. This technique leverages the assumption that the physical residual operator, which defines the PDE dynamics, is known. By using a discretized version of this operator, the method assesses whether the neural solver’s predictions are consistent with the expected dynamics.

### Strengths
- The paper introduces a novel approach that integrates a physical prior with uncertainty quantification techniques to evaluate the performance of purely data-driven neural PDE solvers.
- The idea is presented with clear details and supported by experiments on diverse equations. The authors effectively illustrate how this helps assess and improve the reliability of the neural PDE predictions.

### Weaknesses
 - My primary concern is about the choice to use only the physical residual for PRE non-conformity. Since most neural PDE solvers for temporal dynamics aim to solve an Initial-Boundary Value Problem (IBVP), it's essential not only to consider the differential operator but also to account for how the solution aligns with the imposed initial and boundary conditions. The authors may need to address this aspect of the problem and explore how incorporating these constraints could enhance the conformity assessment.


### Questions
I suggest that the authors provide a more intuitive explanation of how the conformal prediction techniques applied in the paper work. Offering clearer insights into these methods could help a broader audience better understand the concepts and their relevance to the study.

### Soundness
3

### Presentation
2

### Contribution
2
