# Embracing Contradiction: Theoretical Inconsistency Will Not Impede the Road of Building Responsible AI Systems

- Decision: Accept
- Scores: 8, 5, 6

## Abstract
This position paper argues that the theoretical inconsistency often observed among Responsible AI (RAI) metrics, such as differing fairness definitions or trade-offs between accuracy and privacy, should be embraced as a valuable feature rather than a flaw to be eliminated. We contend that navigating these inconsistencies, by treating metrics as divergent objectives, yields three key benefits: (1) Normative Pluralism: maintaining a full suite of potentially contradictory metrics ensures that the diverse moral stances and stakeholder values inherent in RAI are adequately represented; (2) Epistemological Completeness: using multiple, sometimes conflicting, metrics captures multifaceted ethical concepts more fully and preserves greater informational fidelity than any single, simplified definition; (3) Implicit Regularization: jointly optimizing for theoretically conflicting objectives discourages overfitting to any one metric, steering models toward solutions with better generalization and robustness under real-world complexities. In contrast, enforcing theoretical consistency by simplifying or pruning metrics risks narrowing value diversity, losing conceptual depth, and degrading model performance. We therefore advocate a shift in RAI theory and practice: from getting trapped by metric inconsistencies to establishing practice-focused theories, documenting the normative provenance and inconsistency levels of inconsistent metrics, and elucidating the mechanisms that permit robust, approximated consistency in practice.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The machine learning community is in conflict over which metrics to prioritize during training; oftentimes, optimizing along multiple axes requires sacrificing performance along a single axis. The authors argue that this behavior is a feature rather than a bug. The inconsistencies in these objectives is useful for ensuring that machine learning systems can engage with stakeholders with different values and also acts as an implicit regularizer to prevent overfitting to a single metric. The authors combine concepts from diverse perspectives on semantic regularization, Rashomon sets, and block shortcut features. The authors close by introducing future directions.

### Strengths
- The authors craft excellent arguments with almost every claim either supported by relevant literature or logical arguments
- The writing is super engaging that would encourage lots of reflection in RAI research 
- I really appreciate how the authors engage with multiple RAI communities and illustrate how these diverse viewpoints converge in this framework

### Weaknesses
- I would have liked to see more references to the empirical evidence like user studies or retrospective analyses (if they exist) of the downstream effects of pluralist ML systems vs singular objective systems
- I would love more guidance on how to use these objectives in practice: what considerations and trade-offs should a researcher make in deciding what to do?

### Questions
- There exists interpretability work clarifying when there may exist an interpretability vs accuracy tradeoff, specifically sourcing from label noise [1]. Do you have a sense of when such a trade-off might exist with plurality/inconsistencies?
- Are there ever any cases where plurality hurts (e.g., low stakes decisions like predicting existence of a cup)? How should a researcher decide what metrics to use and when is too much inconsistency too much?



[1] https://proceedings.neurips.cc/paper_files/paper/2023/file/0a49935d2b3d3342ca08d6db0adcfa34-Paper-Conference.pdf

### Presentation
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper focuses on the tradeoffs and competitions between various trustworthy/ responsible AI metrics. The authors argue that this competition between different metrics is not a problem to be solved. The authors argue that representing diverse moral values and stakeholder priorities. They formalise two types of inconsistencies: intra-concept and inter-concept, and outline why they are valuable. The authors recommend practice-driven theory for such tradeoff balancing.

### Strengths
- The topic is quite important for responsible AI and for different optimization strategies for such metrics.

- Maintaining Pareto front of different metrics is a valid suggestion and a very practical solution when many methodologies for maintaining tradeoffs fail.

- The paper is well structure and intuitive to follow.

### Weaknesses
- Would have appreciated some guidance on what acceptable inconsistency thresholds were for some of the tradeoffs, more practically? 

- Some methods have been able to mitigate tradeoffs between conflicting metrics. The paper doesn't recognise or discuss them.

- The formulation could be naive since it misses out on some aspects of responsible ai, such as explainability, accountability or adversarial attack, where the user's intent is malicious.

### Questions
- What framework do the authors envision can help decide the tolerance band?

- Are there certain levels or types of inconsistency that should always be considered unacceptable? For instance, is a model that is equitable for one group but grossly inequitable for another still within the bounds of "acceptable inconsistency"?

- How would this be applied to different aspects of responsible ai?

### Presentation
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper argues that theoretical inconsistencies among Responsible AI (RAI) metrics (such as conflicting fairness definitions or trade-offs between accuracy and privacy) should be embraced rather than eliminated. The authors propose that such inconsistencies preserve value pluralism, capture richer conceptual information, and act as implicit regularizers that improve model robustness. They recommend shifting from eliminating inconsistency to defining acceptable inconsistency thresholds, documenting normative assumptions, and designing pluralistic evaluation tools.

### Strengths
The paper presents a clear conceptual framework distinguishing between intra-concept and inter-concept inconsistencies. It offers a multi-dimensional argumentation for retaining metric inconsistency. The use of concrete examples from fairness, political neutrality, and accuracy–privacy trade-offs makes the argument accessible and grounded. Recommendations are actionable, covering theoretical development, stakeholder engagement, and transparency documentation.

### Weaknesses
The paper’s emphasis on embracing inconsistency could benefit from more detailed risk analysis of when inconsistencies may harm stakeholder trust or decision clarity. While mechanisms for leveraging inconsistency are explained, there is limited discussion on the computational and operational costs of implementing multi-metric optimization. The argument sometimes leans on philosophical justification without equally rigorous empirical evidence across diverse deployment contexts. The proposal for “Metric Provenance Sheets” is promising but lacks concrete implementation guidelines or evaluation results.

### Questions
1. One can also say that we should not evaluate the ethics of a machine learning model with metrics at all. What would the authors responed to this?
2. How should practitioners determine the optimal “acceptable inconsistency threshold” for high-stakes applications?
3. What governance structures or oversight bodies could ensure multi-metric evaluations remain transparent and accountable?
4. Are there domains or contexts where metric inconsistency might systematically disadvantage certain stakeholders?
5. How might the proposed pluralistic evaluation approach integrate with existing regulatory frameworks that currently rely on single-metric compliance?

### Presentation
4
