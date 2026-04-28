# Test-Time Alignment via Hypothesis Reweighting

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
Large pretrained models often struggle with underspecified tasks---situations where the training data does not fully define the desired behavior. For example, chatbots must handle diverse and often conflicting user preferences, requiring adaptability to various user needs. We propose a novel framework to address the general challenge of aligning models to test-time user intent, which is rarely fully specified during training. Our approach involves training an efficient ensemble, i.e., a single neural network with multiple prediction heads, each representing a different function consistent with the training data. Our main contribution is HyRe, a simple adaptation technique that dynamically reweights ensemble members at test time using a small set of labeled examples from the target distribution, which can be labeled in advance or actively queried from a larger unlabeled pool. By leveraging recent advances in scalable ensemble training, our method scales to large pretrained models, with computational costs comparable to fine-tuning a single model. We empirically validate HyRe in several underspecified scenarios, including personalization tasks and settings with distribution shifts. Additionally, with just five preference pairs from each target distribution, the same ensemble adapted via HyRe outperforms the prior state-of-the-art 2B-parameter reward model accuracy across 18 evaluation distributions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes HYRE, dynamically reweights ensemble models at test time based on a few labeled examples from the target distribution, allowing the model to better align with specific user intent or task requirements. HYRE applies generalized Bayesian inference, updating ensemble member weights using non-differentiable performance metrics. Empirical results show HYRE’s robustness across multiple distribution shifts, personalization tasks, and preference alignment scenarios, achieving improved accuracy with minimal additional data.

### Strengths
-The use of ensemble reweighting for test-time alignment is a novel solution to the underspecified task problem, offering quick adaptation without additional training.

- HYRE leverages scalable ensemble architectures, making it feasible to apply this approach to large-scale, pretrained models.

-The method is validated across varied tasks, including preference personalization, distribution shifts, and safety benchmarks, showing consistent improvements.

-HYRE’s adaptation requires only a few labeled examples, reducing computational costs compared to conventional fine-tuning and aligning with practical constraints.

### Weaknesses
 -Although the active learning setup is mentioned, the paper lacks detailed analysis on how different active learning criteria (entropy, BALD, variance) affect performance across tasks.

- The empirical studies are concentrated on well-known datasets, but the paper could benefit from evaluating HYRE on additional real-world datasets, especially those with more nuanced or complex underspecification.

- HYRE is compared against fine-tuning and other ensemble-based models but lacks direct comparisons with recent advances in task alignment or ensemble calibration methods.

 The results show that HYRE outperforms conventional ensemble approaches. Could the authors clarify how HYRE compares with models explicitly trained for task alignment, particularly in settings where task ambiguity is less pronounced?

### Questions
The paper suggests that HYRE performs well with only a few adaptation samples. Could the authors elaborate on how performance scales as the number of adaptation examples increases, and how the results compare with methods like fine-tuning under such conditions?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes Hypothesis Reweighting (HYRE), a framework for test-time model adaptation to address task underspecification in large pretrained models. The authors introduce an ensemble method that dynamically reweights individual ensemble heads at test time based on a small number of labeled examples from the target distribution. The authors state that the method outperforms traditional methods such as fine-tuning in low-data scenarios and adapts quickly without modifying the model parameters.

### Strengths
1. The paper is content-rich and centers on test-time adaptation, which is practical.

---
2. The paper features extensive analytical experiments supported by a variety of figures and tables, which enhance the clarity and depth of the presented results.

---
3. The  understanding of method from the perspective of Bayesian inference is insightful.

### Weaknesses
 1. Your motivation, the claim that "the best single model (A) can substantially outperform the ensemble average (B)" does not directly lead to the conclusion that "it is more advantageous to view the ensemble as representing a set of candidate models (C) rather than aiming for a single 'best' function through uniform averaging (D)". The relationship between A, B, C, and D needs clearer justification. Are B and D describing the same approach? This logical connection requires more elaboration to be convincing.

---
2. Your method is based on **Strong Assumptions**. It relies on training multiple heads  as the basis for test-time adaptation, which implies:
     - You assume that test tasks can be represented by a **limited set** of basis functions, which may not hold true in many real-world applications.
     - You also assume that test tasks are **linear combinations** of these basis functions, another strong assumption that is often unrealistic.

---
3. Your method has **Dependence on Labeled Test Data**. The requirement for a small set of labeled examples from the target distribution is a significant limitation, while standard test-time adaptation scenarios typically allow access only to unlabeled test data.
     - This constraint makes your method unusable in conventional **zero-shot** scenarios.
     - The labeled examples need to be **independent and identically** distributed (i.i.d.) from the test distribution, which limits applicability in non-i.i.d. environments.
     - Your method is unsuitable for **continuous or single-sample** adaptation settings where labeled data may not be readily available.

---
4.  Even if we assume your theoretical framework holds, practical implementation poses challenges. For instance, how do you acquire data from different domains to train the basis heads? The quality and distinctiveness of this data directly impact the method’s effectiveness in real-world test scenarios.

---
5.  You need to compare your method with more alignment baselines such as CPO, KTO, SimPO, etc. Additionally, using established alignment evaluation benchmarks like the Open LLM leaderboard would strengthen your results and demonstrate broader applicability.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
### 

- Motivated from the observation that a single model can, under some circumstances, achieve better performance than a naive ensemble, the paper proposes to use a combination of efficient ensemble learning algorithm (from previous work) and a fast ensemble weight learning algorithm to dynamically weigh the different members of the ensemble. They demonstrate on a range of tasks, regression in UCI datasets, vision datasets with distribution shifts like WILDS, and preference modeling with LLMs. Although the improvements are less noticeable in the regression problems, they illustrate consistent gains from their method in the vision and language domains.
- Despite these results, a few important analyses are missing
    - Comparisons to prior work on dynamically learning weights for ensembles (e.g., [1], [2], [3])
    - Analysis of how much improvement comes from the efficient ensemble learning vs. weight learning
    - How the improvement in the rewards for the LLM preference modeling tasks actually translates to performance in head-to-head comparisons of the generations

[1] Ruan, Yangjun, et al. "Weighted ensemble self-supervised learning." arXiv preprint arXiv:2211.09981 (2022).

[2] Jiménez, Daniel. "Dynamically weighted ensemble neural networks for classification." 1998 IEEE International Joint Conference on Neural Networks Proceedings. IEEE World Congress on Computational Intelligence (Cat. No. 98CH36227). Vol. 1. IEEE, 1998.

[3] Shahhosseini, Mohsen, Guiping Hu, and Hieu Pham. "Optimizing ensemble weights and hyperparameters of machine learning models for regression problems." Machine Learning with Applications 7 (2022): 100251.

### Strengths
- The paper begins with a crisp motivation that a single model can at times outperform a naive ensemble of models. Overall, it is very clearly written and easy to read, and the contribution is very well-scoped.
- The paper presents comprehensive results across a range of tasks, from regression tasks in UCI, distribution shifts in vision, and preference modeling in language.

### Weaknesses
 - The preference model experiments with LLMs show consistent results across the different benchmarks, but ideally it would be good to see GPT4-based evaluations [1] to see whether this increase in the reward by 0.03 in Anthropic HH is perhaps meaningful difference at all.
- The novelty of this paper lies in the insight that in task underspecification settings, a single model can outperform an ensemble of models and that HyRE’s fast ensembling reweighting mechanism can indeed learn a good weighting. However, the paper lacks comparisons against other basic baselines of works that have proposed methods [2, 3, 4] to re-weight ensembles at inference-time. Despite the time constraint, some preliminary experiments comparing against these would be very helpful and I would be more keen to raise my score.
- Some further analysis seems warranted to see how much improvement is coming from the efficient ensemble learning method vs the ensemble weighting learning algorithm. The delta from the ensemble weighting learning algorithm is at least clear from the different results/tables.

### Questions
- The authors’ main argument / hypothesis is that given task underspecification, a single model can outperform a naive ensemble. Can the authors also provide how the performance of a single model fares compared to an ensemble + HyRE — beyond the toy experiment in Figure 3? Essentially, it would be good to quantify if HyRE is able to learn the “optimal” weighting? If the authors could provide some additional results on perhaps the language model or vision (WILDS) experiments.
- Also, what is also the entropy of the learned weights over the members of the ensembles? Do the authors observe that it collapses onto a single model, if the hypothesis is indeed true that a single model can outperform all others in task underspecification settings?
- As for the fast ensemble reweighting method, for the personalization of LLMs, is it possible to directly leverage the reward models’ scores in order to learn the weighting instead of using negative log likelihood?
- The reviewer acknowledges that running scaling experiments may be difficult given the time constraint, but an obvious argument against this ensemble approach would be that it then takes up to K times the amount of training compute to train K models. How does this fare against training 1 larger model in the paper’s experiments?
- In Table 2, what are the numbers in the parantheses?
- How were the samples for tuning the ensemble weights selected? Random? If so, can the authors report the standard deviation across using different sets of random samples?

### Soundness
3

### Presentation
3

### Contribution
2
