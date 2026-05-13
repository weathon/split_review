# A Principled Evaluation Framework for Neuron Explanations

- Decision: Reject
- Scores: 5, 5, 3, 6, 6, 5

## Abstract
Understanding the function of individual units in a neural network is an important building block for mechanistic interpretability. This is often done by generating a simple text explanation of the behavior of individual neurons or units. However, for these explanations to be useful, we must understand how reliable and truthful they are. In this work we unify many existing explanation evaluation methods under one mathematical framework. This allows us to compare and contrast existing evaluation metrics and understand the evaluation pipeline with increased clarity. We propose two simple sanity checks on the evaluation metrics and show that many commonly used metrics fail these tests and do not change their score after massive changes to the concept labels. Based on our experimental and theoretical results, we propose guidelines that future evaluations should follow and identify good evaluation metrics such as correlation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The existing methods often use completely different metrics to evaluate how good their descriptions are, but it is not clear how they compare to each other. This paper unifies many existing explanation evaluation methods under one mathematical framework. This paper proposes two simple sanity checks on the evaluation metrics and shows that many commonly used metrics fail these tests and do not change their score after massive changes to the concept labels. Finally, this paper proposes guidelines that future evaluations should follow and identifies good evaluation metrics such as correlation.

### Strengths
- This paper provides a detailed summary of existing work and unifies them under a mathematical framework.
    - The experimental results of this paper reveal shortcomings in the majority of existing evaluation metrics.

### Weaknesses
 - The clarity of this paper could be improved. It is necessary in Equation (1) to present the form of function $\mathcal{G}$ and samples from the probing dataset $\mathcal{D}$ to help readers understand the process of neuron explanation.
    - More information is necessary to explain how the results in the table in Figure 2 were computed. The author did not specify which images in Figure 2 represent the ground truth, which were used for generating prediction results.
    - It is essential to provide additional details on how the results in the table in Figure 2 are computed. The author does not clarify which images in Figure 2 are used to generate prediction results and how these concepts are determined. For example, Equation (10) states $M(a_k,c_t)={B(a_k)}_i$, and at line 331, ${B(a_k)}_{i}=1$, so why does the precision for "Animal" equal 0.5 instead of 0?

### Questions
- Equation (1). Why consider layer $l$ after specifying target neuron $k$ ?
    - Equation (1). Is $t_k$ a textual description of neuron function or a one-hot vector based on concepts?
    - Equation (1). What is the process for generating explanation $t$ ?
    - Section 4.1. In general machine learning, it is common to comprehensively consider recall, precision, and F1 score. Could you explain the connection between individually assessing precision or recall and the more prevalent approach of evaluating all three metrics together?

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
3

### Summary
The paper introduces a unified mathematical framework for evaluating neuron explanations and proposes two new sanity checks to assess the reliability of these evaluation metrics. The work highlights the shortcomings of many current metrics and recommends correlation (with uniform sampling) as the most reliable metric. Through theoretical analysis and comprehensive experiments, the paper provides insights into the biases of common metrics and emphasizes the importance of unbiased sampling.

### Strengths
This paper is well-written and adress an important problem to the field of explainability:

1. **Unified Framework**: The paper effectively consolidates various existing evaluation metrics under one theoretical umbrella, making it easier to compare and contrast them. This is a valuable step toward standardizing neuron explanation evaluations.
2. **Introduction of Sanity Checks**: The proposed "Missing Labels" and "Extra Labels" tests are innovative and help identify metrics that may produce unreliable results. These tests are practical tools for researchers aiming to choose or develop more robust evaluation metrics.

### Weaknesses
Nevertheless, this paper has issues, some more significant than others. I will categorize these into **major problems (M)** and **minor problems (m)**. It is important to emphasize that all these issues are addressable and do not undermine the overall quality of the paper.

**M.1.** Related Work Insufficiency: the related work section is lacking for an ICLR-level submission, citing only 25 references. The paper overlooks key literature on concept extraction, concept importance estimation, and human-centered evaluations of neurons and concepts—some of which directly relate to the challenges discussed in the paper.

**M.3.** Limited Discussion on Metric Limitations: while correlation is presented as the most reliable metric, the paper does not thoroughly explore its potential limitations or scenarios where it may fall short! A more balanced discussion that addresses these limitations would enrich the analysis.

**M.5** Focus on Final Layer Neurons: the experiments are predominantly focused on final layer neurons, which might not represent the complexity found in intermediate layers. Including analyses of hidden layers would provide a more comprehensive evaluation of the framework's applicability across the entire network.

**Minor Problems (m)**:

**m1.** Impact of Hyperparameter α: the paper does not discuss the effect of the α parameter on the results. Is there an optimal α that depends on the specific metric used? A brief analysis would be helpful.

**m.2** Lengthy Recap of Basic Metric Definitions: the paper devotes two pages to revisiting standard classification metrics such as precision, F1-score, AUC, and cosine similarity. For an ICLR audience, this level of detail is unnecessary and could be condensed or omitted.

**m.3.** Redundant Explanations of Failure Cases: what the paper describes as "Failure cases of recall" and "Failure cases of precision" are related to standard type I and type II errors in statistics. Entire paragraphs dedicated to these concepts are redundant and could be streamlined.

**m.4** Model-wise Table Splits Without Aggregate Analysis: the tables present results model-wise but do not offer aggregate data. Including aggregated results could provide a clearer overall picture of the metric performance.

### Questions
- Have you considered applying the proposed sanity checks to evaluation metrics in other domains, such as NLP or multimodal systems? This could demonstrate the broader applicability of your framework.

- Would an analysis that incorporates feature visualization methods alter or reinforce your conclusions about the reliability of different metrics?

- Extend your analysis to include neurons from intermediate layers and various model architectures to assess the framework's robustness across different scenarios.

- Incorporate qualitative analyses or practical case studies or concept-based dataset ?

**Overall, this paper is a notable contribution to the evaluation of neuron explanations. However, there are some major limitations and a major rewrite would further strengthen its overall impact on the field.**

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
5

### Summary
This paper focuses on the evaluation of explanation methods for neurons in DNNs. The authors first formalize the evaluation task in a unified framework. Then, they identify the theoretical flaws of existing evaluation metrics, and further propose two sanity checks for evaluation methods. In experiments, they find that most evaluation methods cannot pass the sanity check, while the correlation metric and cosine similarity exhibited good performance.

### Strengths
1. The authors focus on an important topic of the evaluation of explanation methods.
2. The authors compare many different evaluation metrics in experiments.

### Weaknesses
1. This paper is only limited to explanation methods based on simple concepts. Specifically, the explanation in this paper only refers to whether a neuron represents a specific concept, where the concept is simplified as the class label or superclass labels. However, the explanation for a neuron is much more complex and not limited to representing a single concept, such as the receptive filed of a neuron or saliency map. The proposed evaluation principles cannot be scaled to other explanation methods.
2. The proposed method is ad-hoc. Why do you only adjust the concept label for testing? Why not try to adjust neural activations? The theoretical guarantee for the completeness of the proposed method is needed.
3. The mathematical formulation of the explanation $t_k$ is unclear. Does it represent a scalar, a vector, or a text description?
4. All the metrics and sanity checks seem to be limited to the explanation for a neuron. How do you compute these evaluation metrics and sanity check if the explanation is based on linear combination of neurons? Many papers have claimed a concept is usually jointly represented by the combination of multiple neurons, rather than a single neuron.
5. The completeness of sanity checks in the paper is not guaranteed. In other words, even if an evaluation metric passes two sanity checks, it still cannot grauantee this metric to be a faithful metric. The limitation of the evaluation method needs to be formulated in mathematics.
6. All experiments in the paper are conducted using class labels or superclass labels as the concept. If the concepts are more fine-grained attributes like stripe or wings, is the proposed method powerful enough to still identify the difference between different evaluation metrics?

### Questions
Please refer to the weakness part.

### Soundness
2

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
4

### Summary
The paper addresses a critical issue in neuron explanation methods: the works of neuron explanation methods often use completely different metrics to evaluate how good their explanations are. It proposes a unified mathematical framework to unify existing evaluation metrices. 

Furthermore, the paper introduces two sanity checks for evaluation metrics: the Missing Labels test and the Extra Labels test. These tests are designed to assess the robustness of commonly used metrics. The findings reveal that many of these metrics fail to pass at least one of these fundamental tests. A key outcome of the research is the identification of Correlation as the most effective overall evaluation metric.

### Strengths
1. The study tackles an important research question in XAI by aiming to compare and contrast existing evaluation metrics for neuron explanation methods and understand the evaluation pipeline with increased clarity.

2. The definitions and explanations related to the mathematical framework are well articulated.

3. The introduction of two sanity checks based on the mathematical framework seems sensible. These checks provide practical tools for assessing the robustness of the evaluation metrics.

4. The findings effectively highlight the shortcomings of existing evaluation methods and underscore crucial considerations for designing robust evaluation metrics. This enhances our understanding of how to measure the effectiveness of neuron explanations accurately.

### Weaknesses
1.	Ambiguity in Parameter Selection: The paper does not provide a clear rationale for the choice of threshold hyperparameters in equations (5) and (6), nor for the value of \alpha in the second experimental setting, or the ratios 0.5/2 in the first and second sanity checks. It remains unclear how these values were determined and whether different values might impact the results. Specifically, for equation (5), the choice of \(b_\alpha\) is not well-motivated, and it's unclear how sensitive the results are to this threshold. Similarly, for equation (6), while 0.5 is a common cutoff for binary classification, its appropriateness in this specific context needs further justification. The lack of a clear methodology for selecting \(\alpha\) in the second experimental setting raises concerns about the robustness of the findings. Furthermore, the arbitrary selection of 0.5 and 2 as ratios in the sanity checks lacks a principled basis and could potentially bias the results. A more thorough exploration of the parameter space and sensitivity analysis is needed to establish the reliability of the conclusions.

2.	While I understand that the paper focuses on evaluating Function 1, considering the title “A Principled Evaluation Framework for Neuron Explanations,” it would be beneficial to discuss the relationship between evaluating Function 1 and Function 2 more thoroughly. It would be advantageous to demonstrate whether the current evaluation framework could be adapted to evaluate Function 2 with some modifications. If this is not feasible, I would suggest that the authors narrow their claims prior to Section 2.3 to better reflect the specific focus of the framework. The paper's title suggests a broader scope than what is actually covered, and a more explicit discussion of the limitations regarding Function 2 is warranted. The current framework focuses solely on the input-to-activation mapping (Function 1), while the activation-to-output mapping (Function 2) is equally important for a comprehensive understanding of neuron behavior. The paper should either expand its scope to include Function 2 or clearly state that it is outside the scope of this work and discuss the implications of this limitation.

3.	In Setup 4 of Table 7, all methods fail to achieve high accuracy. Could the authors explain why this is the case or why this setup is particularly more challenging? In this scenario, even the best method achieved less than 80% accuracy. Does this indicate that the current best evaluation methods are still not perfect? The consistently low performance across all methods in Setup 4 suggests that there might be inherent limitations in the evaluation setup or the pseudo-labels used. It is crucial to understand why this particular setup is so challenging and whether the current evaluation metrics are adequate for capturing the nuances of neuron behavior in this scenario. The paper should provide a more detailed analysis of the factors contributing to the low accuracy and discuss the implications for the generalizability of the findings.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the problem of evaluating neuron explanations. Specifically, it proposes a unification of some of the metrics used for neuron explanations and two sanity checks that a good metric needs to pass. The sanity checks work by replacing the class labels associated with the data points in the probing dataset. While the first check removes half of the labels for a given class, the second doubles their count. The idea is to use such labels as a concept, keep the explanations associated with the neurons the same, and check the sensitivity of the metrics to the change. To compute the ground truth explanations (which will be kept fixed), the authors consider the output neurons of vision models where the ground truth is the label to be predicted and the class that optimizes the overlap between firing rate and class samples for a hidden layer. The authors claim that good metrics should exhibit a large change in the scores and, based on such claims, identify and claim the best metric among the tested ones as the one where the gap is the largest.

**EDIT AFTER REBUTTAL**: Given the current changes to the manuscript and the promised ones (please refer to my Summary of Review After Rebuttal and the authors' response for a detailed explanation), most of my concerns have been or will be addressed. The only remaining issue is related to the significance of the tests in Section 5. However, considering the improvements in all other areas, I am leaning towards acceptance.

### Strengths
- Evaluating the quality of explanations and addressing the fragmentation of the metrics is arguably the most important problem in the field of explainable artificial intelligence. The field needs more papers in this direction.

- The development of more sanity checks for explanations is important and would be a good contribution


- The pure results in the tables (without the analysis and claims - see weaknesses and questions), are significant and important to the field and can raise awareness about the weaknesses of metrics used for evaluating explanations.

### Weaknesses
 - The most significant weakness relates to the claims and analysis of the results. **There is a mismatch between what the authors claim,** (assess which metric is the best one to evaluate explanations) **and what the results and the sanity check support** (asses which metric is the most sensitive to the concept label noise in a probing dataset -  i.e., the (non-) robustness of metrics in the presence of concept label noise). In a few words, claiming that the best metric to evaluate explanations is one that exhibits the largest sensitivity to label noise is misleading and not conceptually precise. I would suggest maintaining all the experiments and changing the narrative and the analysis to better reflect the results of the experiments (for example moving the focus from "finding the best metric for evaluating neuron explanations" to "benchmarking metrics in the presence of label noise"). 


This first point requires a detailed description, provided below. The authors are encouraged to provide further clarification or supporting evidence or adapt the narrative and claims of the paper to the raised concern:

Consider the setup of the output neurons considered by the authors. In this case, the tests:
- do not change the input (so the concepts are still included or not included in the input), 
- do not change the explanation (which is truthful as claimed by the authors to be the ground truth), and
- do not change the neuron’s behavior. 

This setup means that the explanation is still the right one because it reflects what the neuron actually learned and its behavior. Therefore, in an ideal (and unrealistic) scenario, a perfect metric should still assign a high score with the explanation associated with the neuron both before and after the tests based on the semantics of the input and the behavior of the neuron and ignoring the label associated with the input. 

Conversely, *what the tests are doing is **introducing label noise** into the probing dataset.*
The problem of label noise is well-studied and well-known in binary classification setups. Ideally, a perfect metric should be immune to label noise, as stated before. However, such a metric is unrealistic, and at the practical level, f1 or AUC are the best and standard de facto metric. Analyzing the results in the table, the best metrics identified by the authors are more sensitive to label noise than these standard metrics for binary classification problems. It is not clear why a metric should be more sensitive to label noise than these latter metrics. This is a good sign that the claim of the authors about the criteria to establish the best metric could be misleading and needs to be reconsidered or further assessed. Again, there is nothing wrong with the experiments or the sanity checks; they could be a wonderful resource against adversarial attacks or to check robustness against label noise. **However, I argue these tests should not be used to identify the best metric to evaluate the quality of explanations.**

- **There is a mismatch between the generality of the claims (best metrics for neural explanations) and the specific settings analyzed**. Given the scope and the expected impact of the paper, it is essential to be rigorous and to state explicitly at the beginning of the paper (alongside the claims) what are the assumptions and settings where this behavior has been observed and holds true. Currently, these must be inferred implicitly from the paper. In the current state, the experiments focus only on (i) the vision domain (ii), models trained on ImageNet, (iii) settings where the concepts correspond to the classes on which the model was trained on, and (iv) concepts are identified by their binary presence. Several of these assumptions are not standards (e.g., (iii) (iv)). The authors should provide more evidence of the generality of their claims in different domains (e.g., nlp), models (trained on different datasets and not trained on the concepts), and setups (e.g., non-binary concepts) claims and explicitly state these assumptions.

- The organization of the paper could be slightly improved. For example, the metrics evaluated in this paper are presented only as equations in the main text. There is no textual description of them. Since they are the main focus of the paper, they deserve more attention.  It is unclear what these metrics measure, why they were proposed, and what their strengths and weaknesses are. Some details, such as the setup where they were proposed (e.g., domain, granularity) and ranges, are included in tables and the appendix, but these are not sufficient to fully understand the metrics. To save space, certain sections that are not the main focus of the paper do not need detailed descriptions in the main text (e.g., function 2 in Section 2.3 and associated discussions, or even the generation part of Section 2.2).

- It is unclear what rationale and process were used to select the metrics analyzed. As with the previous points, since the claims involve identifying the best metric to use in future work, it is important to adopt a clear rationale and adhere to it.  Some metrics included in the analysis have been used only in one paper (or at least it seems so by looking at the table references), so popularity does not seem to be the criterion. Meanwhile, metrics used in other papers are missing from the analysis. Adopting a rigorous strategy (e.g. popularity, publication venues, date of publication, compatibility with the proposed unification, etc.) and explicitly stating the procedure used to select the metrics would strengthen the paper.

### Questions
All the weaknesses listed above are indirect questions for the authors. Therefore, please consider them as points to discuss. The score should be considered a placeholder. I will significantly revise it if the authors provide further clarification or supporting evidence or adapt the narrative and claims of the paper to the raised concerns.

All the following questions did not affect my evaluation but I would appreciate a clarification:
- What is the rationale for assigning citations to the metrics in Table 1? Some of the metrics have been used in multiple papers, but only one of them is reported (e.g. WPMI)
- There are some simplifications in the setup and definitions of the tested metrics and the way these metrics have been used in the original papers (e.g., correlation score or IoU). Is this correct or are they the same? If the answer is negative, is there a mathematical proof ensuring that the results for the simplified and unified versions hold for the settings tested by the original papers? If so, please include this information in the appendix.
- It is not clear why some metrics, like the Cosine cubed, are included. They have been used only as an optimization metric for CBMs and not strictly for comparing and evaluating neuron explanations (even if the target is related). If the authors prefer to include this kind of metrics, there are many other similar optimization metrics in the CBM research area that should be included.
- The motivation for considering correlation a better choice than cosine similarity seems quite weak as reported in the paper (just one sentence vs better results overall!). Can authors provide an example of “significant errors when explaining neurons whose average activation is different from zero”?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper unifies various metrics used for evaluating mechanistic interpretability tasks into a single unified framework. It then introduces a series of "sanity checks" to assess the reliability of these metrics, demonstrating how some existing metrics fail these tests. Through experiments where the "ground truth" of a concept is known, the authors conclude that the "correlation" metric with uniform sampling yields the most accurate results.

### Strengths
1. A unifying framework for various metrics appears to be beneficial for researchers in this field.

2. The "sanity checks" conducted could provide valuable insights for those studying the topic.

3. The paper is thoughtfully and clearly written.

4. The paper combines both a "formal" aspect that unifies the definitions and practical experiments.

### Weaknesses
1. The primary contribution of this paper is in unifying various metric frameworks within mechanistic interpretability. However, this approach appears relatively "straightforward" and doesn’t seem to involve any technically complex process (the authors may clarify if they disagree). In traditional XAI, for instance, numerous papers propose unifying different notations, yet these often entail either technical or mathematical complexities ("demonstrating that X fits within this category is technically challenging because...") or yield unexpected insights ("it's surprising that X can also be captured under our framework because..."). This framework does not seem to meet those criteria.

2. I'm not sure why the "sanity checks" are regarded as a reliable evaluation framework for the metrics. Why should we trust the assurances provided by these "sanity checks" but not the guarantees offered by the metrics themselves?

3. The choice of the "correlation" metric appears somewhat rigid. Are there any potential issues with using this metric, even though it performed best in the experiments section?

### Questions
1. Are there any technical or conceptual challenges in constructing the underlying uniform framework? Does it reveal any non-trivial or surprising relationships, such as the unexpected categorization of certain metrics within this framework?

2. See other comments in the weaknesses section

3. It would be helpful if the authors could discuss the limitations of their unifying framework, the sanity checks performed, or aspects of the experiments section. Could the authors elaborate on some of the constraints or limitations of their work?

### Soundness
2

### Presentation
3

### Contribution
2
