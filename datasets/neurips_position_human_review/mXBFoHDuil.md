# Statistically Valid Post-Deployment Monitoring Should Be Standard for AI-Based Digital Health

- Decision: Accept
- Scores: 7, 7, 6

## Abstract
This position paper argues that post-deployment monitoring in clinical AI is underdeveloped and proposes statistically valid and label-efficient testing frameworks as a principled foundation for ensuring reliability and safety in real-world deployment. A recent review found that only 9\% of FDA-registered AI-based healthcare tools include a post-deployment surveillance plan. Existing monitoring approaches are often manual, sporadic, and reactive, making them ill-suited for the dynamic environments in which clinical models operate. We contend that post-deployment monitoring should be grounded in label-efficient and statistically valid testing frameworks, offering a principled alternative to current practices. We use the term "statistically valid" to refer to methods that provide explicit guarantees on error rates (e.g., Type I/II error), enable formal inference under pre-defined assumptions, and support reproducibility—features that align with regulatory requirements. Specifically, we propose that the detection of changes in the data and model performance degradation should be framed as distinct statistical hypothesis testing problems. Grounding monitoring in statistical rigor ensures a reproducible and scientifically sound basis for maintaining the reliability of clinical AI systems. Importantly, it also opens new research directions for the technical community---spanning theory, methods, and tools for statistically principled detection, attribution, and mitigation of post-deployment model failures in real-world settings.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The paper argues that post-deployment monitoring of clinical AI systems is critically underdeveloped and advocates for a shift toward statistically valid, label-efficient hypothesis testing frameworks. It highlights that despite clinical AI tools’ susceptibility to performance degradation due to factors like covariate shift and concept drift, only 9% of FDA-registered models include surveillance plans. The authors propose formalizing monitoring as two-sample hypothesis tests, encompassing both data shift detection and performance monitoring, with rigorous statistical guarantees. They present detailed formulations for detecting changes in distribution and performance, introduce open challenges such as label scarcity and subgroup identification, and contrast their approach against alternatives like continual learning, Bayesian change-point detection, and conformal methods, ultimately positioning hypothesis testing as the most robust, interpretable, and regulator-aligned method.

### Strengths
* The paper is well-motivated, grounded in regulatory context, and presents a principled, formal approach to a neglected yet critical problem in clinical AI. Its framing of monitoring as hypothesis testing is both rigorous and elegant, offering statistical guarantees often missing in heuristic-based MLOps
* The treatment of label scarcity, through surrogate labeling and active learning, adds practical depth, and the discussion of subgroup-specific degradation addresses fairness and transparency
* I think the paper is well written all around

### Weaknesses
* the paper leans heavily on assumptions like i.i.d. sampling and known pre-deployment distributions, which may not hold in real-world hospital systems
* the authors acknowledge the high dimensionality of clinical data, practical strategies for selecting and validating appropriate test statistics in such settings are underexplored. The reliance on statistical tests may also struggle with the complexity and multimodality of clinical feature spaces, especially when concept drift and covariate shift co-occur.

### Questions
* How would this framework generalize to multi-modal clinical data, such as image-plus-text inputs, where joint distributions are even more complex? I ask this because your title contains Digital Health but multimodality is not considered in the works.
* how does the framework handle confounding variables or unobserved shifts in label semantics

### Presentation
4

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The manuscript argues for statistically grounded post-deployment validation of medical devices. Two types performance degradations are distinguished: 

(1) covariate shift - changes in input patterns
(2) concept drift - changes in relationships between features and labels 

Accurate and timely “catching” of these errors will prevent patient harm associated with incorrect AI decision-making. 

In particular, the manuscript highlights the value of detecting performance degradations using hypothesis testing, and discusses the pros and cons of the proposed method compared to other techniques. Finally, a thorough survey of techniques for conducting the associated tests and comparing distributions is provided.

### Strengths
The manuscript is well written, clearly describes related work, and offers a wealth of information regarding how to test for performance drift using hypothesis tests.

### Weaknesses
I found Figure 1 difficult to understand. In particular, I didn’t understand how the colors corresponded to covariate drift/concept shift, and how model recalibration fixed the problem.

In addition, while it is helpful to have such a detailed summary of tests, are some techniques more commonly used than others? It would be helpful to have more guidance regarding which methods are standard for ease of comparison.

### Questions
Does the variability in patients/clinical readers impact degradation performance testing? In particular, how challenging is it to modify any of the offered tests to success criteria that depends on 95% confidence intervals as opposed to point estimates? 

In model performance monitoring (and perhaps elsewhere in the manuscript), the hypothesis test is defined with respect to a positive difference (tau). However, this may not be needed/feasible. In particular, it would be valuable to distinguish super-superiority, superiority, and non-inferiority as potential outcomes of the hypothesis tests.

### Presentation
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
The authors argue that statistically valid, label-efficient post-deployment monitoring should be standard practice for clinical AI systems. The paper outlines why monitoring is essential for safety and describes common targets such as covariate shift, concept drift and performance degradation. The authors highlight regulatory expectations and identify key challenges, including costly labelling and operational constraints in healthcare settings.

### Strengths
1. The authors have a clear position “statistically valid, label-efficient post-deployment monitoring should be standard in clinical AI”), which is well-defined, tied to FDA/NIST guidance and immediately relevant to the healthcare ML community
2. Makes use of formal statistical testing frameworks (e.g., two-sample tests, sequential analysis, bootstrap) and applies them to operational ML in a clinical context which is something ML research and deployment (surprisingly) often lacks
3. I like how it balances theory with realities such as label cost, clinician alert fatigue and healthcare workflow limitations, which makes the recommendations credible

### Weaknesses
1. While individual concepts are well-described the paper often lists methods and open questions without deeply integrating them into a coherent positional narrative. This makes the argument less direct and those parts read more like a survey/review paper
2. The argument would be stronger with an end-to-end clinical example showing how the proposed principles translate into thresholds, alerting protocols and decision-making under uncertainty, i.e. case studies 
3. The regulatory and statistical references are strong but I feel the paper under-cites recent advances in ML-specific drift detection (e.g., distribution-free detectors, adaptive control of false alarms) that could strengthen or challenge its stance. However this isn't a critical issue
4. The emphasis on i.i.d.-style statistical tests and straightforward two-sample testing glosses over the complexity of temporally correlated irregular and nonstationary clinical data
5. The framing risks implying that a method is either “valid” or “invalid” without acknowledging spectrum-of-validity trade-offs. I wonder if there is an angle here to relate this to the question of fairness vs accuracy, e.g. Kleinberg et al. Inherent trade-offs in the fair determination of risk scores (2017)

### Questions
1. If statistical validity, label efficiency, and subgroup monitoring cannot all be fully satisfied due to operational constraints, how would the authors prioritise among these goals, and what criteria would they use to decide?
2. Once a statistically valid alert is triggered, what is the authors’ view on how that should feed back into model improvement or retraining workflows without compromising future validity checks? Should the model be pulled? Or does the backup then become part of the equation?
3. Could the authors comment on whether monitoring systems should also track downstream clinical impact metrics (e.g., changes in treatment patterns, patient outcomes) alongside statistical drift metrics, and how that would fit in their framework?

### Presentation
3
