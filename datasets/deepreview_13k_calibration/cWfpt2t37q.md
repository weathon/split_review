# From Risk to Uncertainty: Generating Predictive Uncertainty Measures via Bayesian Estimation

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
There are various measures of predictive uncertainty in the literature, but their relationships to each other remain unclear. This paper uses a decomposition of statistical pointwise risk into components associated with different sources of predictive uncertainty: namely, aleatoric uncertainty (inherent data variability) and epistemic uncertainty (model-related uncertainty). Together with Bayesian methods applied as approximations, we build a framework that allows one to generate different predictive uncertainty measures.

We validate measures, derived from our framework on image datasets by evaluating its performance in detecting out-of-distribution and misclassified instances using the AUROC metric. The experimental results confirm that the measures derived from our framework are useful for the considered downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce a framework for quantifying uncertainty by decomposing it into aleatoric and epistemic. The authors use Bayesian methods to approximate and derive a unified framework for generating uncertainty measures. The framework is validated through experiments on classification tasks for image datasets, specifically on out-of-distribution detection.

### Strengths
1. The paper is well written and clear.
2. The paper presents a solid theoretical contribution by unifying different predictive uncertainty measures under a Bayesian risk decomposition framework. It connects well-known uncertainty quantification methods (e.g., Mutual Information, Expected Pairwise KL Divergence) with a common theoretical foundation, which adds clarity and depth to the topic.

### Weaknesses
### 1. Limited Scope of Experimental Section

The paper's experimental section only considers image classification tasks, which have been extensively researched in the uncertainty community. It could be strengthened by:

   - **Broadening the task domain**: The paper could provide results on regression tasks to bolster the experimental validation. Specifically, the framework should be tested on datasets with varying noise levels and complexities to assess its robustness in different scenarios. This would also help to clarify how the proposed uncertainty measures behave in non-classification settings.
   - **Exploring state-of-the-art methods**: Consideration of more cutting-edge methods, such as generative models for uncertainty quantification, could enhance the experimental insights. For instance, comparing the proposed framework with methods that use normalizing flows or variational autoencoders for uncertainty estimation could provide a more comprehensive evaluation.

### 2. Redundant Conclusions

Given the lack of novelty in experimental design (see 1), the conclusions drawn in the experimental section are similar to those in previous works [1, 2], which limits the novelty of the paper’s contributions to the literature. Specifically, the observation that excess risk is a suitable measure for soft out-of-distribution detection, while it may not be as effective for hard out-of-distribution detection, is not a novel finding. This is a well-established limitation of methods that rely on the predictive distribution.

### 3. Assumption of Well-Approximated Data Distributions

The framework relies on the decomposition of total risk into Bayes risk and excess risk, which assumes that the underlying true data distribution can be well approximated. In practice, this assumption may not hold in many real-world scenarios, especially with complex, high-dimensional data. The paper does not adequately address the potential impact of model misspecification on the derived uncertainty measures. It is crucial to investigate how the framework behaves when the model's assumptions about the data distribution are violated.

### 4. Lack of Baseline Comparisons

The paper appears to lack comparison to strong baselines. While the authors state:

> "We emphasize that the goal of our experimental evaluation is not to provide new state-of-the-art measures or compete with other known approaches for uncertainty quantification."

They also mention:

> "Instead, we aim to verify whether different uncertainty estimates are indeed related to specific types of uncertainty."

However, the paper fails to provide comparisons to modern estimates of uncertainty such as [3, 4], which could help contextualize their findings and strengthen the evaluation. Without these comparisons, it is difficult to assess the practical utility and relative performance of the proposed framework.

### 5. Lack of training details

The authors appear to have omitted important training details in Appendix H. Specifically, it is unclear:

   - What loss function was used to train the models? It is important to clarify whether the loss function used for training was the same as the one used for uncertainty quantification, and if not, what the implications of this choice are.
   - How were the ensembles trained? Were they trained as completely independent networks, or did they share components? The training procedure for the ensembles needs to be clearly specified, including whether any regularization techniques were used to ensure diversity among the ensemble members.

Providing these details is crucial for reproducibility and understanding how the proposed framework was implemented.


### Questions
Does the loss function to quantify uncertainty and the training loss function need to be the same?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a generalized framework from which common measures of aleatoric and epistemic uncertainty can be obtained. This is done through Proper Scoring rules and the notion of risk. The framework assumes Bayes (aleatoric) and Excess (epistemic) risk, and explains that the risk may be estimated differently with different ways to approximate the true function and the learned function. Following this they observe which proper scoring rule tends to perform well, and when aleatoric/epistemic uncertainty performs well for a certain task. Lastly, they briefly describe energy based measures.

### Strengths
- The paper clearly outlines its contribution. By offering a better theoretical understanding of the commonly used uncertainty measures we may progress the field of disentanglement. 
- The paper covers a lot of ground in a limited span, discussing risk, proper scoring rules, different ways for risk estimation, and a substantial amount of experimental results. Overall I think the paper provides a nice overview of different uncertainty measures and how they relate.

### Weaknesses
 - While the paper unifies various results into a shared formulation, parts of this are not entirely novel and the paper is not clear about this. For example, Schweighofer et al. (2023a)[2] already describe EPKL as a deviation from Mutual Information that does not assume the BMA to be the true model. They also discuss the relation to the reverse Mutual Information. This disagrees with the problem statement on Line 45 which suggests that it is not clear how these measures relate to each other. Similarly, results similar to Table 1 are already given by Hofman et al. [1] (see questions). Consider explicitly showing which parts of the generalization are novel, and which relationships are established (for example by [1] and [2]). 
- The current work fails to assert the usefulness of the proposed generalization. I would expect a strong evaluation to create hypotheses that follow from the generalization, and validate those experimentally. Only experiments 6.2 and 6.3 come with a hypothesis, but those hypotheses generally apply to uncertainty quantification and not the proposed generalization. This severely limits the impact of the paper. 
- At various locations the authors discuss that aleatoric and/or epistemic uncertainty are vaguely defined, but they do not try to maintain a precise definition following the literature. For example, they argue that epistemic uncertainty is the lack of knowledge of the right model parameters, but this would ignore model misspecification, which is accepted as a source of epistemic uncertainty. Similarly, on Line 36 authors say that aleatoric uncertainty is ambiguity in the label distribution, which ignores uncertainty in the inputs or an otherwise stochastic relationship between the features and the labels. I encourage the authors to attempt to use a more consistent and complete definition of aleatoric and epistemic uncertainty as a starting point. This is particularly relevant because the Pointwise Risk perspective seems to try to give an alternative precise definition. Consider for a source [3], Section 2.4.1.
- It is unclear why the energy-based models are discussed, as they seem to have little relevance. Please clarify the relevance or remove this section. 

- In Section 6.4 it would be good to clearly point to where we can find evidence for which claim (table, row and column). This mainly applies to Lines 477-482. I cannot find the results that show R_exc(3,1) is better than both energy-based methods for misclassification detection, nor that R_Exc(3,1) is preferred over energy based measures for Soft-OOD. 
- Line 456 seems overstated “all instances of excess risk should perform worse [than Bayes/Total risk on misclassification detection]”. This is true if there is more (separable) aleatoric uncertainty than epistemic uncertainty, but this is not true in general. For example in low data or high dimensional problems, this might not hold. Adding the word “typically” or “usually” could be sufficient. 
- Lines 104-107 are repetitive with Lines 36-38. 
- The whole paper assumes Deep Ensembles as the BNN, but different behavior may be observed with different models. It could be good to show behavior with MC-Dropout or Flipout.
- Table 5 mentioned on Line 475 is actually in the appendix, but the text presents it as part of the main body. 
- In the tables it should be clear whether the plus-minus indicates standard deviation, variance or standard error. If appropriate, it may be helpful to indicate the which parts of the tables relate to conclusions drawn (highlighting in bold may be useful). 
- The notation of e.g. R_Exc^{(1, 3)} is hard to keep track of as a reader. Would it be acceptable to rename “Excess” risk to epistemic risk, or Bayes risk to Aleatoric Risk? Perhaps the indices may also be substituted with abbreviations so the connection to the approximations is clear?

### Questions
- Previous work by Hofman et al [1] seems to be related and at least partially overlapping, but not cited. For parts of Table 1 it seems Hofman et al. give a similar result also based on proper scoring rules. From this it seems that a general framework for uncertainty measures already exists. Can the authors clarify how their proposed framework extends beyond this?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a family of uncertainty measures based on point-wise risks which allows to decompose the uncertainty into aleatoric (Bayes risk) and epistemic (Excess risk) parts. Plugging-in proper scoring rules into the derived uncertainty measures, they obtain expressions for computing the Bayes and Excess risk for the specific case of proper scoring rules. Finally, the authors compare three different methods for estimating the risks based on the Bayesian formulation, which they allows to derive many of the existing uncertainty measures as special cases.

### Strengths
Many parts of the work have appeared in some form before, but combining them is a novel idea. For example, generating the uncertainty measure from the point-wise risks has been explored in [1] and [2] as the authors note, but also in [3]. Proper scoring rules were explored in the context of the uncertainty quantification in [4]. Finally, the various Bayesian risk estimation techniques have existed in the literature for a long time. However, the authors do a good job connecting these pieces and showing how various uncertainty measures naturally arise and correspond to different ways of estimating the risk for a proper scoring rule. The authors supplement this with a deeper investigation of the relationships between the estimates and exploring which estimates are better under specific conditions. 

[1] Kotelevskii, Nikita, et al. "Nonparametric uncertainty quantification for single deterministic neural network." Advances in Neural Information Processing Systems 35 (2022): 36308-36323.
[2] Lahlou, Salem, et al. "Deup: Direct epistemic uncertainty prediction." Transactions on Machine Learning (2021).
[3] Liu, Jeremiah, et al. "Accurate uncertainty estimation and decomposition in ensemble learning." Advances in neural information processing systems 32 (2019).
[4] Gruber, Sebastian, and Florian Buettner. "Better uncertainty calibration via proper scores for classification and beyond." Advances in Neural Information Processing Systems 35 (2022): 8618-8632.

### Weaknesses
While the work as a whole appears sound, I have a few concerns:
1. How are the proposed risks affected by the model misspecification, e.g., prior misspecification of $p(\theta)$? I think since the method is Bayesian in nature, it's important to outline the assumptions and highlight possible shortcomings. Specifically, the impact of using an overly informative prior, which could lead to underestimation of epistemic uncertainty, needs to be addressed. The authors should discuss how the choice of prior influences the posterior, especially when data is limited, and how this affects the derived uncertainty measures.
2. No simulations. Assuming, we know the true $\eta$, it would be interesting to see how the different estimators of the risk fare under (1) various distribution shapes (2) misspecification (of prior) (3) error from approximate posterior (if full posterior is not available). The lack of simulation results makes it difficult to assess the practical behavior of the proposed estimators under controlled conditions. For example, how do the estimators behave when the posterior is highly non-Gaussian or multi-modal, and how sensitive are they to errors introduced by approximate inference techniques?
3. Experimental section is narrowly focused and not well-motivated. The authors devote their experiments to testing whether the aleotoric and epistemic uncertainties are captured well. For this, the authors compute the proposed Total, Bayes, and Excess risks and classify the samples into out-of-distribution and misclassified based on these values. They then test the accuracy of this classification. Since Excess risk is connected to the epistemic uncertainty that is connected to the out-of-distribution classification, the out-of-distribution classification accuracy must be better based on the Excess risk. Similarly for the Bayes risk and the accuracy of identifying misclassification, both of which are connected to the aleatoric uncertainty. First, these experiments hinge on the assumption that indeed the misclassification and out-of-distribution are related to the aleatoric and epistemic uncertainties -- a largely untestable assumption. Second, from the tables, I see very little difference between using the Total, Bayes, and Excess risks across all datasets and tasks: the differences while being statistically significant appear almost negligible, which raises questions whether the suggested measures and/or experiments are meaningful. It is unclear if the observed performance differences are practically significant, and the experiments do not provide a strong justification for the proposed decomposition.
4. No comparison with other UQ measures. The authors do not compare their proposed UQ measures with the existing approaches, which leaves the question of why they should be used in practice. Without a comparison to existing uncertainty quantification methods, it is difficult to assess the relative advantages and disadvantages of the proposed approach. The authors should clarify how their method improves upon or differs from existing techniques.
5. (Minor gripe)  Limited practical utility. It appears to compute any of the proposed uncertainty measures, one needs an access to the posterior $p(\theta|X,Y)$. Ultimately, this limits the set of methods to which the proposed approach could be applied. The requirement of having access to the full posterior distribution limits the applicability of the proposed method to Bayesian models, and the authors should discuss the implications of this limitation and potential ways to address it.

### Questions
1. In Section 4.1 and Appendix E, the authors arrive at the conclusion that choosing the best estimate is often impossible in practice. namely, in Section 4.1, the authors say that exact relationship of the central estimate, $r(\bar\eta)$ with the other ones is not known so it's not clear which choice of the estimate for Bayes risk is best; while in Appendix E, the authors conclude that knowing which estimate to choose for the Excess is impossible to know apriori. Similarly, there is little guidance on the choice of the proper scoring rules. Overall, this leaves me with a 4 (proper scoring rules) * 9 (estimates) possible ways to get the Excess risk. Similarly, for the Bayes risk, we have another 12 possible choices. Are there any general or maybe domain-specific advice on how to choose the best UQ measure from among the proposed ones? Is it possible to have results on the error rate of each estimate for some common distribution families? In Appendix E, the authors note that none of the estimated yield a lower / upper on the Excess risk, which raises a question if it's possible to derive such an estimated bound? 
2. I think there are important points missing from the experiments description (Section 6). For example, how are the UQ measures computed given the outputs of the deep ensemble model? And more generally, given a model that only allows access samples from the posterior, are we resorting to a regular Monte Carlo? 
3. In Section 6, what is meant by 5 groups of ensembles? Do all of them have the same architecture? I think the wording here is confusing.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors use a decomposition of statistical pointwise risk into components, associated with aleatoric and epistemic uncertainties. Together with Bayesian methods, applied as an approximation, they build a framework that allows to generate different predictive uncertainty measures. Experiments are shown that support the theoretical claims.

### Strengths
This is a nice and interesting paper that addresses a cogent problem in the literature, that is, the existence of many aleatoric and epistemic uncertainty measures based on the total risk decomposition, and how they're related to one another.

### Weaknesses
Taking a Bayesian route has a fundamental drawback, that was highlighted e.g. by Hullermeier and Waegeman (2021, already cited in the paper) and Caprio et al. (2024, Credal Bayesian Deep Learning). Consider the *posterior predictive distribution*, 

$$p(\tilde y \mid \tilde x , D)=\int_\Theta p(\tilde y \mid \tilde x, \theta) p(\theta \mid D) \text{d}\theta = \mathbb{E}_{\theta \sim p(\theta \mid D)} [p(\tilde y \mid \tilde x, \theta)],$$

where $p(\tilde y \mid \tilde x, \theta)$ is the model distribution, and $p(\theta \mid D)$ is the parameter posterior. Posterior predictive $p(\tilde y \mid \tilde x , D)$ tells us "how likely" output $\tilde y$ is to be the "correct one" for input $\tilde x$, given the knowledge encapsulated in the data $D$ we collected, which enters the computation via the posterior probability $p(\theta \mid D)$. Oftentimes, scholars claim that, in a Bayesian setting, the distribution on the parameters $\theta$ captures (or is linked to) the epistemic uncertainty (EU) faced by the agent. This is a somehow agreeable premise, akin to a second-order distribution reasoning. If we accept this assertion, though, we see how EU at the predictive level is not quantifiable any more, since it gets washed away by taking the expectation $\mathbb{E}_{\theta \sim p(\theta \mid D)} [\cdot ]$. 

This conceptual problem is relevant for this paper, especially because it is related to the ideas of Bayesian averaging of risk and Central label. I'd like the authors to add a discussion on this matter.

Also, I think there's a typo in line 198: shouldn't it be $\eta_{\theta \mid D_{tr}}$ instead of $\eta_{\theta}\mid D_{tr}$?

### Questions
See Weaknesses. The authors should cite https://arxiv.org/abs/2302.09656 and https://link.springer.com/chapter/10.1007/978-3-031-57963-9_1#:~:text=In%20their%20seminal%201990%20paper,bound%20to%20hold%20with%20equality when discussing about the mentioned problem (and possibly in the related work section). They may also cite other approaches that may be considered in the future, such as credal sets ones, studied by Yusuf Sale, Eyke Hülleremeier, Paul Hofman, Michele Caprio, Viktor Bengs, Sebastien Desterke, Fabio Cuzzolin, Thierry Denoeux, Alessio Benavoli, and Cassio de Campos.

Also, I think there's a typo in line 198: shouldn't it be $\eta_{\theta \mid D_{tr}}$ instead of $\eta_{\theta}\mid D_{tr}$?

### Soundness
3

### Presentation
3

### Contribution
3
