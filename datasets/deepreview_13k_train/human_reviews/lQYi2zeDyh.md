# Demystifying amortized causal discovery with transformers

- Decision: Reject
- Scores: 6, 3, 5, 6

## Abstract
\looseness-1 Supervised learning approaches for causal discovery from observational data often achieve competitive performance despite seemingly avoiding explicit assumptions that traditional methods make for identifiability. In this work, we investigate CSIvA \citep{ke2023learning}, a transformer-based model promising to train on synthetic data and transfer to real data. First, we bridge the gap with existing identifiability theory and show that constraints on the training data distribution implicitly define a prior on the test observations. Consistent with classical approaches, good performance is achieved when we have a good prior on the test data, and the underlying model is identifiable. At the same time, we find new trade-offs. Training on datasets generated from different classes of causal models, unambiguously identifiable in isolation, improves the test generalization. Performance is still guaranteed, as the ambiguous cases resulting from the mixture of identifiable causal models are unlikely to occur (which we formally prove). 
Overall, our study finds that amortized causal discovery still needs to obey identifiability theory, but it also differs from classical methods in how the assumptions are formulated, trading more reliance on assumptions on the noise type for fewer hypotheses on the mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper analyzes amortized causal discovery, where synthetic data allows supervised learning of causal discovery. The investigation focuses on whether learning-based methods can overcome traditional identifiability constraints in causal discovery. Extensive out-of-distribution experiments in a bivariate setting with a CSIvA transformer demonstrate that the method cannot generalize well to unseen mechanisms or noise families. This finding establishes an important link to traditional causal discovery literature, revealing how identifiability assumptions are transferred from algorithm design to training data selection. The work further demonstrates empirically that model generalization can be significantly improved by training on diverse families of mechanisms and noise distributions. A theoretical justification for this approach is provided by proving that the set of non-identifiable structures arising from such unions is negligible, particularly extending known results to post-additive noise models.

### Strengths
- Establishes a clear connection between how assumptions in classical causal discovery are translated to training data assumptions in amortized approaches.
- Provides strong empirical validation and theoretical justification of generalization in amortized learning improves with mixed training, something that previously has not been studied to this extent, providing an important result and discussion point that will benefit the causal discovery community. 
- Establishes a testing methodology for amortized causal discovery that if adopted stands to benefit the field in improving the methods.

### Weaknesses
 - Limited Scope:
  - Analysis restricted to bivariate cases
  - Not clear how well the results extend to more complex graphs, nor is there a clear path for extending results to larger graphs
  - Doesn't address practical challenges like confounding or selection bias
- Experimental Limitations:
  - Only evaluated on purely synthetic data
  - Limited exploration of how results scale with dataset size

### Questions
- Have you explored how your results might extend to larger graphs? What are the main challenges you foresee?
- Can you provide more concrete guidance on choosing optimal ratios when mixing different types of causal models during training?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper tries to analysis the CSIvA model on bivariate causal models. The authors proposed an hypothesis to attempt to bridge the gap between model free (i.e. end-to-end learning without given knowledge of causal generating process) causal discovery algorithms and the identifiability theory, but only use some examples, without a proper proof.

### Strengths
The problem that the authors are trying to attack is actually important. Identifiability is central to causal discovery because it determines whether the true causal structure can be uniquely recovered from the data. Without identifiability, any conclusions about causality are inherently uncertain, making the validation and application of causal models problematic. Meanwhile, models such as CSIvA does not provide any identifiability results, but achieves good performance in practice. Thus to ensure the reliability of such models, identifiability results would be required.

### Weaknesses
1. The hypothesis in the paper is not proved.
2. Actually, for a causal discovery algorithm, if it is differentiable at each steps, then it would be trivial to use a RNN to mimic  the action of the algorithm exactly. Then a large enough transformer can be used to fit the RNN easily. Thus it would be trivial that a transformer would perform good in identifiable causal discovery cases if such algorithm exists, For example, for linear gaussian with equal variance, each steps of NOTEARS is differentiable if the objective is differentiable. Thus we can use a differentiable neural network to mimic NOTEARS. In other cases, such explanation may also holds.

3. The experimental on 2-variables dataset are too simple. The identifiability results may hold for 2 variables, but the optimization landscape for 2 variables is significantly different from higher dimensions. The search space grows exponentially with the number of variables, and it is not clear that the proposed approach will scale well. The current experiments do not provide sufficient evidence to support the claim that the method can handle more complex, real-world scenarios with higher dimensionality.

### Questions
See above weakness.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work explores supervised learning for causal discovery, a promising direction to potentially replace traditional score-based or constraint-based methods. However, many gaps remain unclear when considering the supervised learning paradigm for this task. To clarify these gaps, we conduct extensive experiments using a specialized method, CSIvA, on a variety of synthetic datasets. The results of these experiments are presented, along with a detailed discussion of their implications.

### Strengths
Some insights from the experiments are provided.


1) For in-distribution generalization, CSIvA effectively generalizes to unseen samples from the training distribution.

2) For out-of-distribution generalization, it is unsurprising that CSIvA performs poorly.

3) CSIvA's performance depends on whether the data is sampled from an identifiable SCM.

4) Training CSIvA on mixtures of SCMs leads to improved generalization.

### Weaknesses
I am generally open to, encouraging, and expecting new paradigms that go beyond traditional score-based or constraint-based methods for causal discovery. However, this work raises several key concerns, prompting me to review this draft with caution.

1) As an experimental paper, it is expected to provide a wide range of existing methods applied to various datasets, not just simulated data. However, the experimental settings in this work are relatively simple and do not appear to be robust enough for a comprehensive experimental study.

2) The insights from the experiments do not yield particularly exciting results and seem somewhat predictable. I would expect a deeper discussion of these experiments or even some theoretical progress. For example, it would be helpful to explore why training data sampled from identifiable SCMs performs well or how the learned model (e.g., a transformer) leverages this information. Additionally, while the learned model may not explicitly satisfy identifiable conditions (such as those in linear non-Gaussian additive noise models), it would be interesting to investigate whether the model implicitly learns such information.

3) For data sampled from a non-identifiable SCM, there may be multiple graphs within a single Markov equivalence class. In this case, do supervised learning paradigms truly offer no advantage? For instance, could we apply a Bayesian approach to the model to yield the most probable result? Additionally, given the existence of multiple possible graphs, could we frame this as a one-to-many problem, perhaps using techniques like Mixture Density Networks?

### Questions
See above.

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
3

### Summary
The paper presents a comprehensive analysis of CSIvA in the context of bivariate causal models. The authors first demonstrate that while CSIvA generalizes well in distribution, it fails to generalize out-of-distribution, regardless of changes in mechanisms or noise distributions. By hypothesizing that CSIvA can identify the SCM underlying the data generation process, the authors challenge the previous claim that “supervised learning methods can address complex data generation and reduce the need for explicit assumptions.” Additionally, the paper takes an empirical step forward by showing that CSIvA has the potential to capture multiple identifiable causal structures within a single network, supported by theoretical claims that post-ANM models are generally identifiable.

### Strengths
The paper is well-organized and clearly presented. The authors articulate their points effectively, with implications interwoven throughout the sections and the corresponding background provided in the appendix. The experiments on synthetic datasets are comprehensive, demonstrating that the performance of CSIvA is non-trivial. The empirical results support the proposed hypothesis. The experiment demonstrates that CSIvA’s generalization ability can be significantly enhanced by incorporating multiple distributions into the training dataset. 

This paper potentially addresses the limitations of supervised learning in causal discovery, particularly the challenge of applying pre-trained models to datasets that may be out-of-distribution. Specifically,  the highlight of this paper is that it offers a possible way to make supervised learning-based causal discovery practical: if the training dataset is sufficiently comprehensive, the model’s predictions are somewhat reliable.

### Weaknesses
In my view, the largest weakness is the lack of evaluation on real-world datasets. Since the experiments already demonstrate the potential of achieving a relatively robust predictor by incorporating multiple distributions in the training dataset, an investigation and comparison with traditional methods on any real-world datasets would be valuable and appreciated. For example, https://www.cmu.edu/dietrich/causality/projects/causal_learn_benchmarks/. This is just an example, the author does not need to be constrained by this and can use any dataset that is valid for causal discovery. If there are any reasons why experiments on real-world datasets may not be feasible or practical, I would be very interested in hearing them and would welcome the explanation with an open mind.



Another limitation, which is also discussed by the authors, is the scope of analysis is rather limited in a bivariate model without considering intervention.

### Questions
I would appreciate clarification on how the method handles independent variable pairs. Does it require a training dataset of independent variables, or is it primarily designed to identify a DAG from the Markov equivalent class, meaning independent cases don't need to be considered? Addressing this point explicitly could be helpful for readers with varying levels of expertise in the field.

### Soundness
3

### Presentation
3

### Contribution
3
