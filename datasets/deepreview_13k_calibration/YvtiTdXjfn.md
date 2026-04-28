# Scalable Ensemble Diversification for OOD Generalization and Detection

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
Training a diverse ensemble of models has several practical applications such as providing candidates for model selection with better out-of-distribution (OOD) generalization, and enabling the detection of OOD samples via Bayesian principles.
An existing approach to diverse ensemble training encourages the models to disagree on provided OOD samples.

However, the approach is computationally expensive and it requires well-separated ID and OOD examples, such that it has only been demonstrated in small-scale settings.

\textbf{Method.}
This work presents a method for Scalable Ensemble Diversification (\ourmethodname)
applicable to large-scale settings (e.g.\ ImageNet)
that does not require OOD samples.
Instead, \ourmethodname{} identifies hard training samples on the fly
and encourages the ensemble members to disagree on these.
To improve scaling, we show how to avoid the expensive computations in existing methods of exhaustive pairwise disagreements across models.

\textbf{Results.}
We evaluate the benefits of diversification with experiments on ImageNet.
First, for OOD generalization, we observe large benefits from the diversification in multiple settings including output-space (classical) ensembles and weight-space ensembles (model soups).
Second, for OOD detection, we turn the diversity of ensemble hypotheses into a novel uncertainty score estimator that surpasses a large number of OOD detection baselines.
\footnote{Code available at \codeurl{}.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a way to train an ensemble of models on OoD without access to Out-of-distribution data. Their proposed approach relies on determining hard samples from the training data and steering an ensemble of models to disagree on these samples. Authors claim this approach to be better for large-scale training. Randomness and last-layer training make their method efficient.

### Strengths
The paper is well-written and easy to follow. I especially like abstract. The method is quite efficient, especially as it requires training two models on each batch.

### Weaknesses
The novel contribution of the paper is not significant. It is not clear how the proposed hardness measure is useful for OoD. I have asked several questions below which will resolve my concerns.

Authors argue:
>> With no OOD data, it is difficult to apply disagreement methods since the main training objective encourages all models to fit the training examples, hence to agree on all available data.

but then uses hard examples as a proxy for OoD data. Why would it make sense to replace OoD data with hard examples? Hard examples.

The authors use 2 models per batch for an ensemble of 50 models. This is quite interesting but requires more explanation as one would expect a number higher than 2 for effective diversification.

The main contribution of the paper is the introduction of a Hardness measure based on cross-entropy loss. However, there is no mention of previous works that have explored this direction (e.g., hard example mining is one direction that comes to mind). It would be interesting to mention previous works and explain how this work is different\new.

For OoD generalization, I am not sure how the proposed training makes a significant difference. Specifically, the results are quite close to a single model. But I am not sure what would be considered a significant improvement.


Another similar work that has explored Out-of-distribution generalization and an ensemble of models is the following: ZooD: Exploiting Model Zoo for Out-of-Distribution Generalization. Although this is in a different context.

Would it make sense to repeat some of the experiments on DomainNet (or a similar OoD dataset)?

### Questions
Authors argue:
>> With no OOD data, it is difficult to apply disagreement methods since the main training objective encourages all models to fit the training examples, hence to agree on all available data.

but then uses hard examples as a proxy for OoD data. Why would it make sense to replace OoD data with hard examples? Hard examples.


The authors use 2 models per batch for an ensemble of 50 models. This is quite interesting but requires more explanation as one would expect a number higher than 2 for effective diversification.


The main contribution of the paper is the introduction of a Hardness measure based on cross-entropy loss. However, there is no mention of previous works that have explored this direction (e.g., hard example mining is one direction that comes to mind). It would be interesting to mention previous works and explain how this work is different\new.

For OoD generalization, I am not sure how the proposed training makes a significant difference. Specifically, the results are quite close to a single model. But I am not sure what would be considered a significant improvement. 


Another similar work that has explored Out-of-distribution generalization and an ensemble of models is the following: ZooD: Exploiting Model Zoo for Out-of-Distribution Generalization. Although this is in a different context.

Would it make sense to repeat some of the experiments on DomainNet (or a similar OoD dataset)?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tackles the out-of-distribution (OOD) generalization and detection via the ensemble diversification approach. Specifically, the authors propose the Hardness-based Diversification Regularizer (HDR) to identify OOD samples from the training data and make disagreement between the members of the ensemble, which is different from existing methods requiring additional unlabeled OOD data. Furthermore, this paper proposes a new OOD measure called Predictive Diversity Score (PDS) which outperforms the existing bayesian Model Averaging (BMA). Experimental results across large-scale benchmarks (e.g., ImageNet) show the efficacy of the proposed framework.

### Strengths
- The research direction is promising, aiming to scale the current approach for large-scale data use while minimizing dependence on external OOD data.

- The analysis justifying the adaptive weights in Section 2.2 and quantifying diversity in Table 1 is well-executed.

- Additionally proposed components such as PDS, stochastic sum and shallow disagreement seem practical.

### Weaknesses
 - In the proposed framework, each OOD sample is individually labeled during training. The reviewer’s main concern lies in conflicts within the ensemble, where simultaneous agreement (cross-entropy supervision) and disagreement arise over the same OOD data point. For instance, the same data can involve both agreement and disagreement terms during training.  Although the method beneficially induces OOD data from the training set, I would like to understand the authors' reasoning for this design choice, especially regarding the fluctuating membership status (ID or OOD) of the same data and why this approach may yield improvements over existing methods.

- According to the proposed framework, the membership status (i.e., ID or OOD) of each training data point may fluctuate throughout training, potentially even at each epoch. I believe analyzing this dynamic would enhance the manuscript, as it would be insightful to observe which data points are identified as hard samples (i.e., OOD data) by the trained models and how this impacts quantitative performance. For instance, an additional analysis could address how fluctuations in the amount of OOD data and the frequency of membership shifts for individual samples influence performance metrics at different stages. Furthermore, observing the characteristics of samples that consistently remain OOD or alternate between ID and OOD membership would provide valuable insights.

- The performance gains are modest compared to the baseline methods.

- The paper is a bit unkind; please clarify the meaning of "Div HPs" in the captions of the relevant tables, even though it is explained in the main text. Additionally, in Table 2, the amount by which the weight is raised is missing. Beyond listing the applied weight values, the reviewer suggests an ablation study to explore how varying weights impact quantitative performance, along with relevant discussions on the corresponding results.

### Questions
- As mentioned, the research direction is promising. However, obtaining unlabeled data, particularly for natural scene images (e.g., through web-crawling or platforms like YouTube), does not seem overly challenging. What distinguishes the proposed method from existing approaches that rely on explicit OOD data? For instance, the reviewer suggests including additional experiments in domains where obtaining suitable unlabeled OOD data is challenging, such as the medical field, to better demonstrate the advantages of the proposed framework over current methods.

- Is there a specific reason for omitting the results of “DivDis,” a fundamental baseline method, from Table 1?

- Why are the results from baseline methods, namely DivDis and A2D, missing in both the 5th and 6th rows of Table 2?

- The authors of DivDis have already demonstrated the viability of their method through parallel computation for diversification. What distinct advantages do stochastic sum and shallow disagreement offer over this approach?

- Please see the items in Weaknesses.

### Soundness
3

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
3

### Summary
This paper proposes a new ensemble framework where model prediction diversity is encouraged on only hard samples. They also propose a new diversity measurement for OOD detection. The experiments show that the proposed method can effectively enforce the prediction diversity of the ensembled models, which lead to a better OOD performance.

### Strengths
1) The paper gives a reasonable and easy-to-understand motivation to encourage diversity on hard samples for single domain generalization. 
 2) Extensive experiments on 2 different tasks are conducted to demonstrate the effectiveness of the proposed method.

### Weaknesses
1) It would be better to see some performance results on more widely used public benchmark datasets for single domain generalization, such as PACS, DomainNet, so that the proposed method can be compared with more baseline methods. 
2) The overall performance improvement of the proposed method seems to be marginal on 3 out of 5 of the domains in Table 2. Can you provide more analysis on the reason behind these results?

### Questions
Please refer to the Weakness section.

### Soundness
3

### Presentation
3

### Contribution
3
