# FairlyUncertain: A Comprehensive Benchmark of Uncertainty in Algorithmic Fairness

- Decision: Reject
- Scores: 5, 6, 6, 6, 5

## Abstract
Fair predictive algorithms hinge on both equality and trust, yet inherent uncertainty in real-world data challenges our ability to make consistent, fair, and calibrated decisions. While fairly managing predictive \textit{error} has been extensively explored, some recent work has begun to address the challenge of fairly accounting for irreducible prediction \textit{uncertainty}. However, a clear taxonomy and well-specified objectives for integrating uncertainty into fairness remains undefined. We address this gap by introducing \FU, an axiomatic benchmark for evaluating uncertainty estimates in fairness. Our benchmark posits that fair predictive uncertainty estimates should be \textit{consistent} across learning pipelines and \textit{calibrated} to observed randomness. Through extensive experiments on ten popular fairness datasets, our evaluation reveals: (1) A theoretically justified and simple method for estimating uncertainty in binary settings is more consistent and calibrated than prior work; (2) Abstaining from binary predictions, even with improved uncertainty estimates, reduces error but does not alleviate outcome imbalances between demographic groups; (3) Incorporating consistent and calibrated uncertainty estimates in regression tasks improves fairness without any explicit fairness interventions. Additionally, our benchmark package is designed to be extensible and open-source, to grow with the field. By providing a standardized framework for assessing the interplay between uncertainty and fairness, \FU paves the way for more equitable and trustworthy machine learning practices.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces FairlyUncertain, a Python package designed to evaluate uncertainty in fairness for machine learning algorithms. The package proposes methods and standards to incorporate uncertainty estimation into fairness evaluations in predictive models.

### Strengths
1. The paper identifies and addresses the underexplored intersection of fairness and uncertainty in predictive modeling.
2. The study spans multiple datasets and predictive tasks, enhancing the benchmark's relevance and applicability.
3. Designing the benchmark as an open-source tool encourages ongoing development and community contributions.

### Weaknesses
1. The paper targets uncertainty as a critical factor in predictive fairness, given the real-world impact of machine learning decisions. However, it does not adequately justify the importance of the consistency and calibration axioms themselves within this context. Specifically, while uncertainty is broadly recognized as significant for transparent AI, the paper could strengthen its justification by explaining why consistency and calibration specifically matter for fair uncertainty estimation. For example, the paper could discuss scenarios where inconsistent uncertainty estimates across similar model architectures or training runs could lead to unfair outcomes, or where miscalibrated uncertainty estimates systematically disadvantage certain demographic groups.

2. Although the paper targets "fair uncertainty," the fairness component feels less integrated with uncertainty until Section 5, where it discusses the abstention framework and Uncertainty-Aware Statistical Parity. The paper could benefit from introducing the importance of fairness alongside uncertainty earlier, so readers understand the relationship between these two aims from the outset. For instance, the introduction could include a motivating example where a model's uncertainty estimates are well-calibrated overall but are systematically less accurate for a specific protected group, leading to unfair decision-making.

3. This paper is largely an implementation paper, presenting a framework and accompanying package for uncertainty-fairness evaluation rather than introducing fundamentally new theoretical insights into either fairness or uncertainty estimation. Its main contribution lies in providing a package that can support standardized evaluations of uncertainty estimation methods within fairness contexts. Therefore, it may be better suited for a benchmark track or tools/package track than a general research track.

### Questions
None

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
The paper introduces FairlyUncertain, a benchmark designed to assess the integration of uncertainty into fairness contexts within machine learning. Addressing the inherent prediction uncertainty challenge for fairness, the paper emphasizes that uncertainty estimates should ideally be consistent across similar models and calibrated to observed randomness. Through experiments across 10 datasets, including binary classification and regression tasks, the authors evaluate various methods for uncertainty estimation and introduce a new fairness metric, Uncertainty-Aware Statistical Parity (UA-SP), tailored for regression tasks. FairlyUncertain provides a structured benchmark to explore the nuanced relationship between uncertainty and fairness, specifically examining the effects of abstention and confidence thresholds.

### Strengths
1- FairlyUncertain introduces a standardized benchmark that is both theoretically grounded and practical, which allows researchers to evaluate how uncertainty affects fairness and vice versa. This is timely, given the increasing need for fair AI applications under uncertainty.

2- The paper defines fairness-focused axioms: Consistency (Axiom 2.3) and Calibration (Axiom 2.4), which set criteria for reliable uncertainty estimates. These axioms are clear and can be used for the practical goal of having fair predictive models that remain robust even under model variations.

3- The authors provide extensive evaluations of consistency and calibration across datasets and methods. They cover both abstention and confidence thresholding. The benchmark’s focus on these uncertainty handling methods, without endorsing one as definitive, offers a structured way to assess their impact on fairness. 

4- The benchmark is open-source which could be used in future research.

5- The benchmark’s use of consistency as a measure for similar pipelines indirectly addresses concerns about model multiplicity. FairlyUncertain's evaluation across slight hyperparameter changes serves as a practical check for this multiplicity effect.

### Weaknesses
1- Axiom 2.3 suggests that small changes in hyperparameters should not significantly impact uncertainty estimates. While this is a reasonable assumption, it would benefit from explicit clarification on the stability limits of uncertainty under various hyperparameter changes to avoid overgeneralization.

2- Although the benchmark evaluates abstention as a fairness strategy, abstention does not reduce demographic disparities in binary classification tasks. Addressing why abstention fails to impact fairness in this context could inform potential adjustments to the benchmark. Also, given that abstention was shown not to reduce demographic disparities, the paper could address situations where abstention might inadvertently introduce biases. For example, explaining conditions under which abstention could be counterproductive would deepen the understanding of its impact on fairness.

3- While tables like Table 2 and Table 4 capture calibration and consistency scores, the paper could strengthen its analysis by discussing why certain methods perform better/worse across different datasets. Additionally, the appendix includes valuable demographic-specific breakdowns that could be better integrated into the main analysis to improve understanding of method reliability and demographic-specific impacts.

4- While XGBoost is effective for tabular data, expanding to deep learning models like MLPs, or transformers would align with recent trends in fairness research and test FairlyUncertain’s utility on more complex architectures. Reproducibility might vary across model architectures, especially complex ones, due to the implicit assumption of consistency under slight hyperparameter variations. While the benchmark is robust as presented, extending it to a broader model set might require tuning and validation.

### Questions
1- How does this work compare with existing research on fairness evaluation (beyond Section 6.1)? i.e., to what extent does the authors' focus on uncertainty help the practical selection of fairness measures and mitigation strategies?

2- Could this framework be adapted for more complex models or architectures and extended to additional fairness notions, such as intrinsic fairness? If so, how?

3- What are the societal implications of incorporating uncertainty in the selection of fair models? Could the authors expand on the strengths of their approach relative to existing methods, providing examples to illustrate the impact beyond simple numerical metrics? Existing literature on model multiplicity highlights the uncertainty involved and explores its societal, legal, and philosophical implications (there are many papers out there on this topic). I am wondering, what new insights does this paper contribute to these ongoing discussions?

### Soundness
3

### Presentation
3

### Contribution
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
The paper introduces "FairlyUncertain", a benchmark to evaluate predictive uncertainty in fairness contexts. It emphasizes the need for consistency and calibration of uncertainty estimates across learning pipelines. Experiments on ten datasets reveal that a simple uncertainty estimation method outperforms prior work, that abstaining from uncertain binary predictions reduces errors but not demographic imbalances, and that incorporating calibrated uncertainty in regression improves fairness. The benchmark is extensible and aims to standardize fairness assessments involving uncertainty, promoting equitable and trustworthy machine learning practices.

### Strengths
- Originality: Introduces FairlyUncertain, a novel benchmark for integrating uncertainty into fairness.

- Quality: Validated through extensive experiments across ten datasets; open-source and extensible.

- Clarity: Clear motivation, methodology, and presentation.

- Significance: Provides a foundational, scalable framework for enhancing fairness in machine learning.

### Weaknesses
 - Findings on reducing errors but not outcome imbalances could be expanded with deeper insights or additional benchmarks.

- The paper does not fully explore variations in models, parameters, or datasets, which limits its generalizability and insights into broader use cases.

### Questions
- Are there plans to include additional fairness interventions?
- Which new calibration metrics could enhance FairlyUncertain?
- Why does regression improve fairness without explicit interventions?
- How generalizable are the results beyond the ten datasets used?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce FairlyUncertain, an axiomatic benchmark for evaluating uncertainty estimates in fairness. The benchmark posits that fair predictive uncertainty estimates should be consistent across learning pipelines and calibrated to observed randomness. FairlyUncertain suggests that: In the binary setting, natural uncertainty estimates beat complex ensemble-based approaches and abstaining improves error but not imbalance between demographic groups. In the regression setting, consistent and calibrated uncertainty methods can reduce distributional imbalance without any explicit fairness intervention.

### Strengths
1. The organization and writing are fairly clear, and the structure of the paper is sound.

2. The motivation is clear, and the background as well as the related works are well explained.

3. The paper shows enough originality and novelty, by providing a novel framework for fairness and uncertainty.
 
4. The experiments are extensive, comparing the performances on various datasets and different prediction tasks.

### Weaknesses
1. The connection between "Fairness" and "Consistency/Calibration" is not so clear: in the description of consistency/calibration metrics, the sensitive attributes don't seem to be included and discussed. For example, for consistency, all the metrics (SD or p-values) are computed over different ensembles, but how is it related to fairness? For calibration, it says "We identify groups of individuals with similar uncertainty estimates and empirically evaluate the standard deviation of the residual difference between the observed and predicted outcomes", but in the previous definition of calibration (Axiom 2.4), the group should be defined by sensitive attributes. The relationships between fairness and consistency/calibration should be further explained.

2. The methodology is limited to ensemble methods: the consistency/calibration metrics discussed in the paper all focus on ensemble methods (i.e., XGBoost), how can this be generalized to a wider class of ML methods (e.g., neural networks with stochastic optimizers)?

3. The experiments on fairness interventions are not very convincing: in section 5, the authors show that "abstaining from binary predictions, even with improved uncertainty estimates, reduces error but does not alleviate outcome imbalances between demographic groups", can the authors provide more insights into this phenomenon? This point is linked to my previous request for more explanation on the connection between fairness and uncertainty estimates.

### Questions
1. Is there more discussion on the connection between fairness and consistency/calibration? For example, how does the standard deviation across different hyper-parameters (which don't take sensitive attributes into account) help mitigate bias towards certain groups (which need information on sensitive attributes)?

2. Can this definition of consistency/calibration be generalized to other ML methods other than ensembles?

I would like to raise my score if these weaknesses/questions can be addressed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents the FairlyUncertain benchmark, which is aimed at measuring the fairness properties of model uncertainty estimates. They focus on two metrics which are called consistency and calibration, and explore the results on these metrics across several algorithms and several datasets, concluding that probabilistically-grounded methods tend to return the best results. They explore the ramifications of abstention on fairness metrics, and propose a new uncertainty-aware form of statistical parity.

### Strengths
- this is an important topic for which there are no currently existing benchmarks that I’m aware of, I think this could be useful for people
- good level of thoroughness here exploring the various different metrics across datasets
- abstention experiments are interesting - surprising to me that abstention doesn’t improve most fairness metrics
- uncertainty-aware Statistical Parity is a good idea - incorporating the uncertainty estimate into a CDF-based metric makes sense

### Weaknesses
 - I’m not sure I agree with the characterization (around L90) of A/B types as unmeasurable and C/D/E types as estimatable from a fixed sample. I think both of these statements are conditional on various distributional assumptions - for instance, you can measure individual variance if you assume you know the mean (or its parametric form and inputs). I think explicating the underlying data generating process would make this whole contribution more substantial
- A couple issues with formalisms in Section 2: 1. I don’t understand Def 2.2 - “differ only in hyperparameter settings” and “there is some j…” seem to say different things: the first implies P and P’ are in some shared “pipeline class” parametrized by different hyperparameters, the second implies that just one hyperparameter differs. 2. On Line 127, f(P) is used - this seems wrong to me, as on L117, f is named as the *output* of P, not a function of it
- I’m not sure I agree with the given definition of consistency as a useful fairness axiom - it seems like more of a Lipschitz condition over what a well-parametrized pipeline might look like. My impression of a fairness axiom of this type might be of the flavor that uncertainty estimates should be as invariant as possible to hyperparameter choices (I’m not sure this is a good axiom either but it seems more fairness-related).
- there is a rich literature on calibration metrics which is not connected to at all in this paper - it would be good to get a better understanding of how those relate to the chosen metrics
- L287 and elsewhere: for consistency, it seems like a non-robust choice to output a maximum std. Dev over individuals - I’m wondering if like a 90th percentile might be a better choice
- L391 - it seems odd to optimize an objective function that mixes statistical parity and equalized odds. Usually, one or the other is picked, since they are very different objectives
- Def 6.2 - it seems overly specific to me to assume that the model outputs are parametrizing a normal distribution. In particular, I don’t think this makes sense in the binary Y case - and the end of the definition (CDF comparison for all outcomes y \in Y) I think doesn’t make sense in the binary y case either (rather you want this to be true at all points in the range)

Small points:
- L142: “a model that always returns 0 is consistent” - by the previous definition this is not true, as the definition of consistency applies to a pipeline class, rather than the model which is outputted. Such a pipeline may output a constant-0 model for some set of hyperparameters, but not others.
- how is clustering done for calibration? I don’t think this is discussed
- Table 4: not sure how Disp. Impact is defined

### Questions
- I’m not sure the framework in Table 1 does a ton for me - doesn’t really connect to the rest of the paper at the moment so tightly and I’m not sure what the takeaways are. I would be interested to see a clearer explication of how these types of uncertainty connect to epistemic/aleatoric
- would like to see a more fleshed out argument for the consistency axiom
- would be interested to know more about connections to current calibration literature
- how much do results change if each fairness metric is optimized for individually (in combination with error)
- is there a more general version of the UA-SP definition?

### Soundness
2

### Presentation
3

### Contribution
3
