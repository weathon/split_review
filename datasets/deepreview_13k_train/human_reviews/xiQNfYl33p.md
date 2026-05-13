# A Generic Framework for Conformal Fairness

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Conformal Prediction (CP) is a popular method for uncertainty quantification with machine learning models. While the method provides probabilistic guarantees regarding the coverage of the true label, these guarantees are agnostic to the presence of sensitive attributes within the dataset. In this work, we formalize \textit{Conformal Fairness}, a notion of fairness using conformal predictors, and provide a theoretically well-founded algorithm and associated framework to control for the gaps in coverage between different sensitive groups. Our framework leverages the exchangeability assumption (implicit to CP) rather than the typical IID assumption, allowing us to apply the notion of Conformal Fairness to data types and tasks that are not IID, such as graph data. Experiments were conducted on graph and tabular datasets to demonstrate that the algorithm can control fairness-related gaps in addition to coverage aligned with theoretical expectations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript introduces and studies a general-purpose conformal fairness framework. It consists of an algorithm that can enforce various notions of fairness (such as demographic parity, equalized odds, predictive parity, and several others contained in the ML fairness literature) on the coverage of prediction sets, in the sense of satisfying appropriate conformal guarantees on expected coverage conditional on sensitive labels/attributes. To demonstrate practical performance of the framework given the various fairness notions, experimental evaluation is provided on a variety of supervised learning tasks; besides the standard setting, graph conformal prediction with fairness constraints is also demonstrated in experiments.

### Strengths
The paper's main asset is a reasonably broad evaluation of the proposed methods on a variety of datasets where fairness concerns may necessitate using one of the tabulated conformal fairness metrics. Compared to prior works the experimental section appears more extensive, both in terms of metrics and datasets. Moreover, conformal fairness guarantees were displayed on graph data in addition to the standard supervised tasks. The results indicate that explicitly enforcing fairness according to any of the tabulated fairness criteria is in fact often necessary, as evidenced by vanilla methods not satisfying non-enforced fairness coverage constraints. Furthermore, no drastic deterioration in efficiency guarantees is observed, indicating that the price to pay for fairness conditional coverage may often be acceptable.

### Weaknesses
--- The main weakness and bottleneck at this point is the writing of the manuscript. In particular, the writing of Section 3, which introduces the objectives, the general algorithm, and the analysis, is currently not acceptable. Indeed, lots of key notions and terms, both on the fairness side and on the conformal side, are not properly and unambiguously introduced and/or are discussed in arbitrary order.
(Fairness: groups/group collections are never formally defined, nor are requirements on them specified (e.g. non-intersectionality etc); "filters" and "filter functions" are simply thrown into the presentation. No background on the fairness measures, no elaboration on how they are transformed into conformal analogues compared to original notions, except for an incoherent sentence starting with "Essentially achieved..." in line 130. Conformal prediction: auxiliary notions like "interval widths", "label miscoverages" appear right away in the pseudocode, which also uses clunky notation and for which the textual explanation is as confusing as the pseudocode notation.) This is not to say that one cannot fill in many of the details with enough imagination and enough expertise, but at the moment the writing is hardly structured and accessible enough.

--- The theoretical/methodological side does not offer strong novel contributions; for the most part it simply wraps class-conditional and group-conditional conformal methodology into fairness-specific terminology --- and is currently doing it in a somewhat confusing way, given the currently unsatisfactory presentation as stated above.

--- In addition, the literature background review, where it's claimed that there are "very few prior efforts" on fairness and conformal prediction, misses an established line of work on group-conditional fairness guarantees; these works study the enforcement of coverage guarantees (usually of both upper and lower bounds) on rich classes of subpopulations given by possibly arbitrarily overlapping groups.

R. Barber et al: The limits of distribution-free conditional predictive inference [Journal of IMA 2020]
C. Jung et al: Batch Multivalid Conformal Prediction [ICLR 2023]
Z. Deng et al: Happymap: A generalized multi-calibration method [ITCS 2023]
O. Bastani et al: Practical adversarial multivalid conformal prediction [NeurIPS 2022]
I. Gibbs et al: Conformal Prediction with Conditional Guarantees [2023]

### Questions
The main desideratum is a substantial overhaul of the paper's writing, especially as it pertains to the methodology Section 3. 

There are other minor concerns, such as the exact conformal methods that the current proposed method is tested against. For instance, APS has been superseded in the literature by RAPS, so that should be included in the comparison. Also, importantly, at least a couple of the many recently appearing class-conditional and local conformal methods should also be included in the comparison for the sake of fairness; indeed, these methods are designed to be able to empirically attain partial versions of conditional coverage without receiving explicit constraints (such as fairness ones) as input, so they should provide a stronger baseline than methods like APS.

----------------------------------------------------------------------------------

UPDATE: The rebuttal, and the post-rebuttal manuscript update, address the immediate concern of improving the presentation of key terms/concepts in Section 3 and beyond. Other improvements such as updates to the experimental section were also made. Given these, I have raised my overall score to 6.

### Soundness
3

### Presentation
2

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
The paper introduces "Conformal Fairness," a framework that extends Conformal Prediction (CP) to ensure fairness across sensitive groups. The authors develop a theoretically grounded algorithm to control gaps in coverage between these groups, leveraging the exchangeability assumption instead of the typical IID assumption. This allows the framework to be applied to non-IID data types, including graph data. Experiments on both graph and tabular datasets show that the framework can effectively control fairness gaps while maintaining coverage guarantees.

### Strengths
- Originality: Introduces "Conformal Fairness," extending Conformal Prediction (CP) to address fairness in uncertainty quantification, especially for non-IID data.
- Quality: Provides strong theoretical backing with rigorous proofs and effective validation through experiments on graph and tabular datasets.
- Clarity: Clearly defined theoretical concepts and a stepwise algorithm description make the methodology accessible to those with relevant background knowledge. Providing additional background information on key concepts would help readers who are less familiar with the topics to follow more easily
- Significance: Tackles an important gap by combining fairness with uncertainty quantification. Adaptable to multiple fairness metrics and data types, making it broadly applicable in ethical AI contexts.

### Weaknesses
 - The paper lacks a detailed discussion of the fairness-efficiency trade-off. Quantifying acceptable efficiency losses when fairness is improved would make the results more actionable for practitioners balancing both aspects.

- The extension of the exchangeability assumption to real-world data may not always hold. Adding empirical evidence or discussion on when this assumption is valid in practice would make the claims more robust.

-Lack of comparison with all existing fairness-aware methods limits benchmarking. Adding baselines would clarify the framework's effectiveness.

### Questions
- How does the framework handle scalability with multiple sensitive attributes, especially computationally?

- Why were existing fairness-aware methods not used as baselines for comparison?

- How practical is the exchangeability assumption for real-world graph data? Any empirical evidence?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a framework to check and find the suitable threshold for conformal learning. Further, the framework can be easily extended to some constraints, like fairness constraints. The authors specifically studied achieving fairness properties for graph models. Further, the authors studied how to use their framework to check the fairness property of a model. The authors' algorithm first find the right use inverse quantile to check whether a threshold is good.

### Strengths
Conformal prediction is a very interesting area and there are many interesting works in this area. It is a natural question to ask how to achieve fairness for models in this setting. The authors provide a very general framework that can achieve many different definitions of algorithmic fairness. The paper also did many interesting experiments in graph datasets.

### Weaknesses
I personally think the author does not elaborate enough on why they chose this algorithm design. The writing of this paper could be improved.

### Questions
I think it would be very helpful for the authors to explain more about their design choices. For example, why choose inverse quantile for miscoverage level? Explain a bit more about the intuitions behind lemma 3.1 and 3.2 would really help the readers.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a notion of fairness, named $\textit{conformal fairness}$. In contrast with standard fairness notions (e.g. demographic parity), this notion significantly applies conformal mapping, which the authors clearly defined. The authors developed an algorithm to achieve this type of fairness on graph datas and confirmed with experiments.

### Strengths
1. This paper is well-written with a clear structure.

2. The notion of conformal prediction is common, while its application on fairness is not widely studied to the best of my knowledge. The novelty of this notion is well justified.

3. The conformal fairness metrics in Table 1 are intuitive and well-founded.

### Weaknesses
1. Although the conformal fairness metrics are well-defined in Table 1, they were not carefully discussed in later results (Theorem 3.4). Specifically, Theorem 3.4 states that "the coverage difference for Predictive Parity is satisfied". In Table 1, the definition of Predictive Parity relies on a conformal prediction $\mathcal{C}$, but the specific mapping/quantification is not discussed in the theorem statement. The theorem should explicitly state how the conformal prediction set $\mathcal{C}$ is constructed and how it relates to the coverage difference being satisfied. For instance, is the coverage difference measured in terms of the size of the prediction sets or the probability mass contained within them, and how does this relate to the $\alpha$ parameter used in the conformal prediction framework?

2. This is a continuation of the previous point. Suppose there is a conformal prediction in Theorem 3.4, how good is it, i.e. what shall the value of $\alpha$ be, as in Equation 1? The paper does not provide guidance on how to choose the $\alpha$ parameter, which is crucial for the practical application of conformal prediction. The choice of $\alpha$ directly impacts the size and validity of the prediction sets, and thus the fairness guarantees. A discussion on the trade-offs associated with different $\alpha$ values and how they relate to the specific fairness metrics would be beneficial.

### Questions
Please see the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2
