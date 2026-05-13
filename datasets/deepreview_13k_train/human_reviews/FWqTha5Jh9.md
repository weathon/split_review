# DA-Bench: Benchmarking Unsupervised Domain Adaptation Methods with Realistic Validation On Diverse Modalities

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Unsupervised Domain Adaptation (DA) consists of adapting a model trained on a labeled source domain to perform well on an unlabeled target domain with some data distribution shift.
While many methods have been proposed in the literature, fair and realistic evaluation remains an open question, particularly due to methodological difficulties in selecting hyperparameters in the unsupervised setting.
With DA-Bench, we propose a framework to evaluate DA methods on diverse modalities, beyond computer vision task that have been largely explored in the literature. We present a complete and fair evaluation of existing shallow algorithms, including reweighting, mapping, and subspace alignment.
Realistic hyperparameter selection is performed with nested cross-validation and various unsupervised model selection scores, on both simulated datasets with controlled shifts and real-world datasets across diverse modalities, such as images, text, biomedical, and tabular data.
Our benchmark highlights the importance of realistic validation and provides practical guidance for real-life applications, with key insights into the choice and impact of model selection approaches.
DA-Bench is open-source, reproducible, and can be easily extended with novel DA methods, datasets, and model selection criteria without requiring re-evaluating competitors.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces DA-Bench, a benchmark for evaluating unsupervised domain adaptation (DA) methods across diverse data modalities with realistic validation techniques. Unlike existing benchmarks, DA-Bench uses unsupervised model selection scores and nested cross-validation to better reflect real-world settings where labeled target data is unavailable. Key contributions include:
- A comprehensive benchmark framework spanning multiple data types (e.g., computer vision, NLP, tabular, biosignals) with 20 shallow and 3 deep DA methods.
- Realistic evaluation protocols that avoid overestimating performance by selecting hyperparameters without target labels, using methods like Importance Weighted (IW) and Circular Validation (CircV) scores.
- Practical guidance and open-source code for DA model selection, offering insights on method and scorer effectiveness under different shift types.

DA-Bench represents a valuable resource for researchers and practitioners by setting a realistic standard for evaluating DA methods and by supporting the field’s advancement through rigorous, reproducible benchmarking.

### Strengths
- The paper is well-organized, with clear explanations of DA methods, evaluation metrics, and data shifts. Effective use of tables and visuals enhances clarity and enables easy interpretation of results.
- DA-Bench is a benchmark that addresses a gap in UDA across multiple data modalities, such as NLP, tabular, and biosignals; multiple DA methods such as 20 shallow and 3 deep DA methods; and multiple model selection strategies. 
- The paper is open-sourced and provides a useful resource for researchers and practitioners to conduct rigorous, reproducible benchmarking.

### Weaknesses
1.  Lack of Clarity in Figure 1
  - Interpretability Issues: Figure 1 is difficult to interpret, particularly in terms of what each shift type represents. For instance, it’s unclear what each color indicates; if colors represent different classes, why are there multiple clusters for each class?
  - Subspace Shift Classification: Subspace Shift is more accurately described as a methodology for handling other types of shifts—primarily Covariate or Conditional Shifts—by finding a common subspace where distributions align. It may be misleading to categorize Subspace Shift as a standalone shift type. The description lacks clarity on how this subspace is identified or why it is invariant to the shift.
  - Suggestion: A clearer, more detailed illustration is needed to make Figure 1 more intuitive and to accurately represent the nature of each shift type. The figure should explicitly show how the data distributions change under each shift, and the subspace shift should be presented as a transformation rather than a shift type itself.
2. Limited Analysis of Dataset and Shift Impact
- Shift Types in Existing Benchmarks: While the benchmark covers method performance across various datasets, it lacks an analysis of the types of shifts present in commonly used benchmarks. Understanding the specific types of shifts (e.g., Covariate, Target, Conditional) in datasets like Office-31, Office-Home, and MNIST/USPS would provide valuable insights. It is not sufficient to state that real-world shifts are complex; the paper should at least attempt to characterize the dominant shifts in these datasets.
- Impact on Method Performance: It would also be helpful to examine how specific shift types influence the performance of different DA methods. This analysis would allow researchers and practitioners to make more informed choices when selecting methods for datasets with specific types of shifts. The paper should provide a more detailed analysis of which methods are robust to which types of shifts.
3. Limited Evaluation of Deep DA Methods
- Missing Methods: The benchmark currently omits certain popular deep domain adaptation techniques, such as pseudo-labeling methods, which are widely used and impactful. For example, pseudo-labeling approaches like MIC (Masked Image Consistency). The inclusion of DeepJDOT is not sufficient to represent the breadth of pseudo-labeling techniques. The benchmark should include a wider range of deep learning methods, especially those that have shown strong empirical performance.
4. Lack of Clarity on Scorer Variability within the Same Method
- Table 2 Confusion: In Table 2, different DA methods with varying model selection techniques are compared, which makes interpretation challenging. A clearer comparison would involve analyzing the same DA method across different model selection approaches to understand the variability introduced by model selection. This would make it easier to interpret the effectiveness of each scorer within a consistent method framework. The paper should focus on isolating the impact of the scorer by keeping the DA method constant.

### Questions
Please refer to the weakness.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes DA-Bench, a comprehensive benchmark for evaluating unsupervised domain adaptation (DA) methods across diverse modalities such as computer vision, natural language processing, tabular data, and biosignals. The benchmark includes a set of simulated and real-world datasets with different types of distribution shifts, a wide range of shallow DA methods designed to handle these shifts, and an evaluation of deep DA methods. A nested cross-validation procedure with multiple unsupervised scorers is used for realistic hyperparameter selection. The results show that few shallow DA methods consistently perform well, and model selection scorers significantly influence their effectiveness. Deep DA methods, while promising, require extensive hyperparameter tuning and often fail to outperform shallow methods in low-data regim

### Strengths
1. Comprehensive benchmark: The benchmark covers a wide range of DA methods and datasets with diverse modalities and distribution shifts, providing a more realistic evaluation of DA techniques.
2. Realistic model selection: The use of nested cross-validation with unsupervised scorers for hyperparameter selection addresses the challenge of lacking target labels in practical DA scenarios.

### Weaknesses
1. The paper mainly focuses on empirical results and benchmarking, without providing deep theoretical insights into why certain methods perform better or worse under different domain adaptation scenarios. Incorporating more theoretical analysis could help in understanding the underlying principles of domain adaptation and guide the development of new methods.

2. While the paper includes a variety of domain adaptation methods in its benchmarks, some of the baseline methods are relatively outdated or not state-of-the-art. Including more recent and advanced baseline methods would provide a more accurate assessment of the performance of new domain adaptation techniques.

3. The paper uses accuracy as the primary evaluation metric for the benchmarks. While accuracy is a common metric for classification tasks, it may not be sufficient to fully capture the performance of domain adaptation methods in all scenarios. Considering additional evaluation metrics such as ECE, Brier Score, F1-score, or even domain-specific metrics could provide a more comprehensive evaluation.

### Questions
See weaknesses.

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
3

### Summary
This paper introduces DA-Bench, a framework for evaluating Unsupervised Domain Adaptation methods across diverse modalities beyond computer vision. Through realistic assessments and nested cross-validation, it comprehensively evaluates shallow algorithms like reweighting and mapping. The study emphasizes the importance of realistic validation, offering insights into model selection approaches.

### Strengths
1.	The paper is well-written and easily comprehensible.
2.	The proposed benchmark is comprehensive and straightforward.
3.	The motivation for validating the parameters of the methods, such as unsupervised scorers that do not rely on target labels, is commendable.
4.	Extensive experiments across multiple datasets are adequate.

### Weaknesses
1. Figure 1 is far from self-contained. Could you explain the detailed relationships and distinctions among these four shifts according to the Figure? Also, in this figure, it appears to represent a binary classification task. Do these four shifts generally exist in other tasks as well?
2. This paper evaluated three outdated deep DA methods. Could you provide the latest deep DA methods for evaluation, such as [1] and [2]?
3. In Table 3, accuracy scores for deep methods are only presented for selected real-life datasets. Could you provide the scores for simulated datasets and conduct the relevant comparisons?
4. In line 217，this paper claims that the supervised scorer cannot be used in practice.  Does this imply that the scorer is meaningless in practice? In other words, how can we evaluate DA methods in practice when target labels are completely absent?

### Questions
Please address the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces DA-Bench, a framework for evaluating unsupervised domain adaptation (DA) methods across diverse modalities, such as images, text, biomedical, and tabular data. It emphasizes fair and realistic hyperparameter selection using nested cross-validation and unsupervised model selection metrics.

### Strengths
DA-Bench provides a relatively comprehensive evaluation of existing shallow algorithms and offers practical insights for real-life applications. It is open-source, reproducible, and easily extendable with new DA methods, datasets, and model selection criteria.

### Weaknesses
The paper has the following shortcomings. First, the methods tested are outdated, lacking work from the past three years. Second, the correlation between different modalities is weak, casting doubt on whether transferability can be achieved. Lastly, the paper does not propose any new theories.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
3
