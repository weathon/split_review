# Feature Matching Intervention: Leveraging Observational Data for Causal Representation Learning

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 3, 6

## Abstract
A major challenge in causal inference from observational data is the absence of perfect interventions, making it difficult to distinguish causal features from spurious ones. We propose an innovative approach, Feature Matching Intervention (FMI), which uses a matching procedure to mimic perfect interventions. We define causal latent graphs, extending structural causal models to latent feature space, providing a framework that connects FMI with causal graph learning. Our feature matching procedure emulates perfect interventions within these causal latent graphs. Theoretical results demonstrate that FMI exhibits strong out-of-distribution (OOD) generalizability. Experiments further highlight FMI's superior performance in effectively identifying causal features solely from observational data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies settings where images are created from spurious and true features, the true features being invariant across environments. Using a single environment, and under the assumption that _only_ the spurious feature is used for minimising the risk, the authors propose a scheme to create a new dataset (or batch) that simulates interventions on the spurious features. Another model can be trained on this dataset (batch) that then is independent of the spurious feature and only uses the true feature for the task at hand. The authors also introduce a test for the assumption that only the spurious features are used for the task.

### Strengths
Overall the idea is a simple one and quite interesting. I do have some issues with the experiments and the test for the assumptions. I think these points could be a lot stronger and should clearly show when the FMI method works and when it doesn't.

- The method is simple and sound when the assumptions of the method hold. The assumptions are _mostly_ clear.
- The paper is mostly clear, although certain areas could be improved (see below)

### Weaknesses
The main weakness of the work is that it only works if the model only uses the spurious feature in the training environment. This is quite a strong assumption and thus should be main and centre in the work. In my opinion, in most cases, it seems likely that a model trained on a single environment in this setting will learn from a _mixture_ of spurious and true features (with varying strengths). In this case, applying FMI can also _hurt_ performance as the signal from the true feature can be lost in the matching process. Furthermore, I'm not sure if the test in Section 5.2 will pick up this case, as Y|Z may differ in the validation environment even in the case that both spurious and true features are used. A thorough analysis of this case will greatly improve the work. It would be of interest to see how sensitive the test is and how much performance is lost if the training results in a mixture of true and spurious features. I would encourage the authors to discuss if this is the case, and include experiments that show if performance drops or not (for example when colour noise in Section 6.2 is higher than the label noise), and to show how trustworthy their proposed test is at finding these cases.

A second weakness is that the procedure requires training a neural network to convergence at every training step.



### Questions
- What is the resultant added cost in your experiments as you require training a network to convergence at every step?
- Is it not possible to just train two neural networks to convergence instead of training a new one to convergence at every training step?
- L312: I'm not sure how Assumption 3 implies that Zspu is the feature learned in the training environment? Surely this depends on how correlated the spurious feature is with the label in the training environment? As far as I can tell, there is no assumption about the training environment at all.
- L345: Related to the first weakness: This property may still hold if _both_ the spurious feature and the true feature are used. I think it may be more correct to say that if Y|Ze and Y|Ze0 are the same then you can be sure that Z is the true feature.
- The experiments in 6.1 an 6.3 are not very informative. There is no clear information from what I can see about the level of correlations between the spurious features and labels.
- Section 6.2: The Colored MNIST setting does not read clearly to me at all. I have a few questions about this:
- There are 3 environments (0.1, 0.2, 0.9) it sounds like two are used as the training environment and one is used as a testing environment. Are the two that are used as a training environment mixed? If so, why is this done? Why not train on 0.1 and then test on 0.9 and so on? This is not commented on at all. This seems like an odd choice and makes the experiment quite unclear.
- It seems that the 0.1 and 0.9 setting are the same (as they have the same correlation between label and spurious feature), is this correct?
- The performance drop when 0.1 is the test environment is a bit worrying. I completely see why training on (mixture of) 0.1 and 0.2 would result in the spurious feature being used, and the performance on the 0.9 environment improves when FMI is used. I'm not sure I believe the claim in L418 that the performance drop in the 0.1 env is due to subsampling. It seems that an equally reasonable explanation could be that training on 0.9 and 0.2 together results in a classifier that uses _both_ Ztrue and Zspu. Matching would thus result in a drop in performance. This should be tested thoroughly to see if this is the case, and to see if the test (Section 5.2) actually spots when this is the case.
- The plot in figure 5 is unclear to me. What is environment 0 and environment 1? Why are there two plots given that you are testing how similar Y|f are in two different environments?

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
This paper is concerned with representation learning with the aim of finding invariant representations that provide good out of distribution behavior (and can be considered causal under suitable definitions). To achieve this the authors provide a matching scheme which matches on the prognostic score. The authors provide an intuitive and simple realization of the approach, adapting the standard minibatch learning scheme with a subsampling procedure that aims to provide balance and, as a result, control for unobserved confounding. A set of experimental results is provided demonstrating the relative performance of the proposed approach with respect to variants of empirical and invariant risk minimization.

### Strengths
* The authors examine an interesting and compelling problem. 
* The proposed solution is simple and intuitive; the idea of using matching for this problem holds appeal given both it's relative simplicity and robustness against a broad array of underlying data generating processes.
* Empirical results indicate the proposed approach holds promise.

### Weaknesses
While a reader well familiar with this area understands the connections between distribution shift, invariance, and causal inference, it is not made clear within the introduction and problem setting. I would strongly suggest that the authors rewrite these sections making each connection much more explicit. In particular, it should be very explicit what the definition of a causal feature is in this work.

The proposed method, as I understand it is more akin to matching on the prognostic score (Hansen, 2008), rather than more standard matching (e.g., the Stuart paper cited), in that matches are constructed using the _outcomes_ rather than matching covariates with respect to _treatment status_. This should be clarified in the paper. Toward this end, in the problem setup it is stated that these results easily extend to additional outcome types, however it is not immediately clear to me that this should be the case since matching on real valued and multi-valued treatments entails a more nuanced procedure.

Subsampling to make proportions match is reasonable, but also likely introduces issues when there is large distribution skew. Specifically, if the predicted probabilities are highly skewed, the subsampling procedure will result in very small effective sample sizes for the minority class, potentially leading to unstable estimates and high variance. This is a critical issue that needs to be addressed, especially in the context of real-world datasets where class imbalances are common.

It's not clear to me how equation 5 achieves balance, or why we should think of this as matching in the standard set? Typically we would find matched pairs where $\hat{f}$ is as close as possible, while this doesn't seem to be doing any explicit matching? The current description lacks a clear explanation of how the subsampling procedure in equation 5 directly leads to balance in the feature space. It is not obvious that forcing the conditional probabilities to be equal will result in the desired balance, especially when the predicted probabilities are not well-calibrated.

Assumption three is incredibly strong, and it is not clear to me how likely this is to hold for any realistic dataset (see below for  a question regarding this). Toward that end, it's not clear to me how substantial the theory is that is provided here. If we are placing strong, and difficult to meet, assumptions on the available data the risk here is that the results serve more as a proof of existence, rather than a general theorem that can be leaned upon in practice. The assumption requires interventions on all variables at all levels, which is a very strong requirement that is unlikely to be met in practice. The authors need to provide a more thorough discussion of the implications of this assumption and how it limits the applicability of their theoretical results.

The highlighting scheme in the results table is confusing. I think the authors meant to bold the best performing method in each setting, rather than just the settings where the algorithm performs well?

Ben B. Hansen, The prognostic analogue of the propensity score, Biometrika, Volume 95, Issue 2, June 2008, Pages 481–488, https://doi.org/10.1093/biomet/asn004

### Questions
Can the authors explain how equation 5 is achieving balance here? It's not clear to me that the procedure as described would appropriately control for confounding.

Why is the matching done with respect to batches? It would seem that this would result in poor entailed balance properties? 

As I mentioned above Assumption three is incredibly strong, and it is not clear to me how likely this is to hold for any realistic dataset (unless I am misreading it. To be clear, all variables are intervened at all levels? Only one intervention has to be present for each variable? Are they perfect interventions? 

Is assumption 4 the observed support?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Feature Matching Intervention (FMI), an approach for mitigating spurious correlations using a feature-matching procedure to mimic perfect interventions on spurious features. The authors provide theoretical guarantees for the proposed method's out-of-distribution (OOD) generalization under specific assumptions and propose a validation approach to assess whether spurious features are being learned in the training environment. Experimental results on synthetic and semi-synthetic datasets, including Colored MNIST and WaterBirds, demonstrate that the proposed method outperforms baseline methods, especially in scenarios with strong spurious correlations in the training data.

### Strengths
1. The theoretical analysis of the OOD generalizability of the proposed method is rigorous, and the derivation procedure is clear and easy to follow.

2. The experiments demonstrate that the proposed method outperforms baselines in identifying causal features, especially in the presence of spurious correlations.

### Weaknesses
1. __Single Environment Claim__: Although the authors claim that the proposed method can mitigate spurious correlations using data from a single training environment, Assumptions 2 and 3 appear to imply the need for multiple environments when deriving the theoretical guarantees. Additionally, the empirical studies on Colored MNIST utilize two training environments, which seems inconsistent with this claim. It would be beneficial for the authors to conduct experiments using a single training environment and evaluate the method's performance on both synthetic and semi-synthetic datasets.

2. Assumption 1 appears to be more of an intuitive conjecture, lacking formal theoretical support. The assumption that the best feature learned from the training environment is either the true causal feature or a spurious feature seems overly simplistic. In many real-world scenarios, the learned feature might be a complex combination of both causal and spurious elements, which this assumption does not account for. Furthermore, the reliance on a statistical test based on a validation environment to determine the nature of the learned feature introduces additional complexities and potential for error.

3. __Missing Related Work__: Some relevant related works have been omitted. First, the concept of reweighting to mimic perfect interventions on spurious features for improving distributional robustness has been discussed in [1] and [2]. Additionally, there is a body of work focused on improving group distributional robustness based on the understanding that ERM tends to learn spurious correlations ([3], [4], [5]). The proposed method seems to share similarities with these works. It would be helpful if the authors could discuss the novelty of their approach and how it fills a gap compared to these existing works.

4. __Subsampling and Overfitting Concerns__: The authors use subsampling to remove the dependence between the label and spurious features. However, spurious correlations often occur in highly imbalanced data distributions, and subsampling in such cases could lead to dropping a substantial portion of the data from majority groups. This may increase the risk of overfitting, especially if the remaining dataset is small. It would be great if the authors could address how they mitigate the risk of overfitting in this scenario.

5. __Validation Environment Concerns__: When assessing whether spurious features are learned in the training environment, the authors propose using a validation environment. This appears to contradict the single-training-environment assumption. One of the benefits of the single-environment setting is the reduced requirement for environment labels or predefined environment divisions. However, if a validation environment is required, this benefit is lost. Furthermore, the validity of the test may depend on the level of distributional shift between the training and validation environments. If the shift is minimal, the test might incorrectly conclude that ERM has learned the causal feature. Clarification on these points would be great.

6. __Experimental Setup for WaterBirds Dataset__: Could the authors provide more details regarding the experimental setup for the WaterBirds dataset?

7. __Discussion on Poor Performance in Heterogeneous Training Environments__: The experimental results on Colored MNIST indicate that FMI performs poorly when the training environments are highly heterogeneous. Specifically, when training environments are (0.2, 0.9) or (0.1, 0.9) and the test environment is (0.1) or (0.2), the performance degrades. A detailed discussion on the reasons behind this poor performance and potential ways to address it would be helpful.

8. Minor typo: in line 245, $i, j \in \{1,2\}$ should be $i, j \in \{0,1\}$?

### Questions
Please see the questions in Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors propose Feature Matching Intervention (FMI), which uses a matching procedure to mimic perfect interventions. They define causal latent graphs, extending structural causal models to latent feature space, providing a framework that connects FMI with causal graph learning.

### Strengths
The procedure emulates perfect interventions within causal latent graphs. Theoretical results demonstrate that FMI exhibits strong out-of-distribution (OOD) generalizability. Experiments further highlight FMI’s superior performance in effectively identifying causal features solely from observational data.

### Weaknesses
Please refer to questions.

page 3, line 147. ''Thus, identifiability becomes an issue here. However, since our goal is to learn $f\phi$, this concern is not relevant.'' Is the goal to identify $\phi$ here?

### Questions
page 3, line 147. ''Thus, identifiability becomes an issue here. However, since our goal is to learn $f\phi$, this concern is not relevant.'' Is the goal to identify $\phi$ here?

### Soundness
3

### Presentation
3

### Contribution
3
