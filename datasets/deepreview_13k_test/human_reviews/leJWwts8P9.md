# Independence Tests for Language Models

- Decision: Reject
- Scores: 8, 3, 6, 6

## Abstract
We consider the following problem of model provenance: can a third party verify whether two language models are trained independently or not given the weights of both models?  We propose a family of statistical tests for models of any architecture that yield exact p-values with respect to the null hypothesis that the models are trained with independent randomness (e.g., independent random initialization). These p-values are valid regardless of the composition of either model's training data, and we obtain them by simulating independent copies of each model and comparing various measures of similarity in the weights and activations of the original two models to these independent copies. We evaluate the power of these tests on pairs of 21 open-weight models (210 total pairs) and find they reliably identify all 69 pairs of fine-tuned models. Notably, our tests remain effective even after substantial fine-tuning; we accurately detect dependence between Llama 2 and Llemma, even though the latter was fine-tuned on an 750B additional tokens (37.5\% of the original Llama 2 training budget).  Finally, we identify transformations of model weights that break the effectiveness of our tests without altering model outputs, and—motivated by the existence of these evasion attacks—we propose a mechanism for matching hidden activations between the MLP layers of two models that is robust to these transformations. Though we no longer obtain exact p-values from this mechanism, empirically we find it reliably distinguishes fine-tuned models and pruned models of different dimension and is even robust to completely retraining the MLP layers from scratch.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a family of independent tests for assessing whether language models are trained independently, based on a permutation test. Leveraging permutation invariance and equivariance in MLP neurons, it provides exact p-values. Extensive evaluations on 21 open-weight models show that the test performs effectively. Specifically, the framework makes the previously proposed $l_2$ distance more stable. The paper also introduces a robust metric to improve the robustness under adversary, validated using retraining of the MLP.

### Strengths
- The paper is well-written, with clear logic in deriving each component of the test.
- The method is novel and addresses an important question.
- Extensive experiments consistently demonstrate the method's effectiveness across various settings.

### Weaknesses
- The notation of matrices in Algorithm 2 could be improved, as it currently overlaps with the algorithm notation.
- It would be helpful to include an evaluation of the $l_2$, CSU, and CSH tests under adversary, the MLP retraining.

### Questions
- The models examined are standard, trained or fine-tuned dense LLMs. How might the proposed test perform with other architectures, such as mixture-of-experts models? How to properly apply the test when comparing a mixture model and a dense model? If sparsification or pruning methods are applied to create mixtures or sparse models, could that impact the test? Additionally, could an adversary leverage these techniques to circumvent the test?

### Soundness
3

### Presentation
4

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
The paper presents a method to estimate if two LLMs are independent of each other, or if their training procedures had co-dependencies. The high-level idea of the proposed strategy is that, if two sets of LLM weights are independent, then the distribution of differences between arbitrary permutations of their weights is uniform. Otherwise, differences for the same permutation (e.g. original weights), will be significantly smaller than the difference amongst arbitrarily permuted versions of the weights from the two models. Through this principle, the methods computes p-values of the distribution of differences, which reflect the probability of the two models being idependent.

### Strengths
The paper is mathematically thorough and bases its thesis in well formulated assumptions. The idea is interesting and the method relatively simple and inexpensive, which makes it attractive for implementation.

### Weaknesses
1) "Independence" is too loosely defined throughout the paper, and sometimes causes confusion. 

For example, in the introduction, in line 60, the authors state "we do not distinguish whether one is a fine-tune of the other or if the two models share a common ancestor". Firstly, this is in contradiction with the first sentence in the abstract: "We consider the following problem of model provenance: can a third party verify whether two language models are trained independently versus fine-tuned from one another given the weights of both models?"

Secondly, the above leads to think that the method can distinguish if two models are somewhat fine-tuned from each other OR from the same model. However, in section 3.1, the independence of the weights depends on both the training algorithm A and initial weights theta^0, which comprehend many more aspects than just common initialisation/fine-tuning from one another. For example, what is the proposed test's output for two models trained on the same data from random initialisation? In this case A_1 and A_2 are not independent; so this would meant that theta_1 and theta_2 are also not independent? What about smaller details, like simply batch size? This would also be a common characteristic of A_1 and A_2. Are the resulting model's weights independent? The definition of statistical independence of equation 1 is not clear and perhaps not entirely proper; it seems to me that the concept of independence in this context is more continuous and might need to be put in terms of co-correlation or similar.

2) The applicability of the method is too restricted in my opinion, for two reasons: 

First, because of the problem stated in 1 above; If I get a p-value form the proposed method >0.05, what do I know about the two models I tested? Was one fine-tuned initialising from the other? Did they just have identical training procedure with the same data? Was one fine-tuned with the output of the other in a teacher-student manner? Some sources of co-dependence may be problematic, while others may not, so not knowing where the dependence comes from makes the result difficult to use in practical situations.

Second, the method works only if the two models have exactly the same architecture, while there are many situation in which a model of different architecture is derived from another model. In fact, this is the predominant problem with copyright infringement at present; companies owning proprietary LLMs do not have a problem with models being fine-tuned from their ones as initialisation, as they keep them secret. The problem of intellectual property arises when their outputs, which are publicly accessible, are used to fine-tune another model of different architecture. The proposed method cannot detect these cases, even with access to the proprietary model.

UPDATED REVIEW FOLLOWING REPLIES:

Following the replies and discussion, I am fairly certain that the authors are indeed misunderstanding the post-processing theorem and this is causing the basic starting point of their proposed technique to be problematic. I will try to be clearer, starting from my example and the response referencing it from the Authors.

From the authors previous response: "Thus, in your example, the mutual information between $A_1(\theta_1^0)$  and $A_2(\theta_2^0)$ is zero, which is consistent with our claims."

This is not true. The authors are confusing two random variables being the same random variable, in which case the mutual information is indeed 0, with two different random variable having the same value when observed, which is the case in my example, and for which the mutual information is not 0 (or not necessarily). Let me go through the details:

$I(A_1(\theta_1^0), A_2(\theta_2^0)) = H(p(A_1(\theta_1^0), A_2(\theta_2^0))) - H(p(A_1(\theta_1^0), A_2(\theta_2^0)) | p(A_1(\theta_1^0)), p(A_2(\theta_2^0)))$

Going through the components in the equation above:

$p(A_1(\theta_1^0) =  \int p(\theta_0)p(A)p(A_1(\theta_1^0)|A, \theta_0)dAd\theta_0$ - this is the probability to observe the value $A_1(\theta_1^0)$ alone.

$p(A_2(\theta_2^0) =  \int p(\theta_0)p(A)p(A_2(\theta_2^0)|A, \theta_0)dAd\theta_0$ - similarly the probability to observe the value $A_2(\theta_2^0)$ alone.

$p(A_1(\theta_1^0), A_2(\theta_2^0)) = \int p(A, A') p(\theta_0, \theta_0') p(A_1(\theta_1^0), A_2(\theta_2^0)|A, A', \theta_0, \theta_0')$ - this is the joint probability of observing both $A_1(\theta_1^0)$ and $A_2(\theta_2^0)$. 

In my example, I stated that $\theta_1^0 \perp \theta_2^0$, so $p(\theta_0, \theta_0') = p(\theta_0) p(\theta_0')$. However, the mutual information is 0, only if the two As are uncorrelated, i.e., $p(A, A') = p(A) p(A')$, but this is not a given. For example, we could have $p(A, A') = p(A')\delta(A=A')$, which is consistent with my example and for which the mutual information would be positive, unless all $A$ and $A'$ are equal to $A_1$, in which case $p(A')$ is also a delta function (all As in the world are the same A=A_1).

Generalising to the statement of the post-processing inequality, $I(\theta_1^0, \theta_2^0) \geq I(A_1(\theta_1^0), A_2(\theta_2^0))$ only if we know that $A_1$ and $A_2$ are uncorrelated ($p(A, A') = p(A) p(A')$ above), which is an assumption that we cannot make; the two models may have been trained copying each others training procedure or using the same training data, with unknown effects on the correlation of the outcomes.

I apologise for confusing the p-values trend in my final question, but my concern stands; if you are basing the guarantee that your method can detect relation of initialised weights on the inequality $I(\theta_1^0, \theta_1^0) \geq I(A_1(\theta_1^0), A_2(\theta_2^0))$ for any arbitrary two $A_1$ and $A_2$, this is not true in general and does not derive from the post-processing inequality.

I confirm my score, as I believe the paper does contain interesting findings, but bases its theory on an incorrect (or at least still to be proven) assumption, which would need to be addressed specifically through theoretical proof/approximation or extensive experimental evaluation.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

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
The submission presents a statistical test to check whether two language models were independently trained. Notably, the test gives exact p-values. The test involves constructing a set of transforms such that one can generate many independent copies of a model by simply applying randomly sampled transformations. A test statistic can then be applied to the set of transformed models for obtaining a p-value. The submission evaluates a selection of different test-statistics, and some demonstrate very high power.

### Strengths
1.	Submission motivates problem well. It indeed seems important to be able to track provenance of open-weight models. 
2.	Submission is well-written and explains method clearly.
3.	Submission evaluates method on a variety of existing models and models trained for this evaluation.
4.	Proposed method shows a large improvement over existing baselines, and appears to have meaningfully novel contributions.
5.	Submission considers a certain class of adaptive attacks, and introduces a variation of their method to defend against them.

### Weaknesses
1.	Submission does not evaluate methods against "most relevant prior work" (Zeng et al., 2024). Presumably this is because the method is not robust and does not provide exact p-values, however the submission's own methods ($ϕ_{CSU}$ and $ϕ_{CSH}$) are shown to be non-robust, and $ϕ_{JSD}$ does not provide p-values. Yet all three tests are evaluated in Section 4.1. It would strengthen the submission to evaluate against Zeng et al., 2024. 
2.	Submission does not describe cost of algorithms. This seems important given that certain decisions are made based on computation cost (using a lookup table on line 266, and using T=99 on line 419).
3.	More clarity could be provided related to some of the simplifying steps when computing p-values. Specifically, in section 3.2.2 when stating “instead of running PERMTEST itself, in our experiments we convert the output $\hat{p}$ to an approximate p-value $\hat{p}$ using standard lookup tables for Spearman correlation coefficient” Please describe more details on why this is possible. Also, does this relate to why the p-values for the dependent models are all epsilon? It’s surprising that every model that is dependent has such a low p-value. Please provide some additional description or intuition for why that is expected.

### Questions
1.	Suggestion: evaluate against statistic from Zheng et al., 2024, as mentioned above.
2.	Suggestion: give some estimate of the rough cost to run such a test.
3.	Suggestion: If feasible, running $ϕ_{l2}$ with T > 99 would provide a better comparison to the other methods. In particular, $ϕ_{CSU}$ and $ϕ_{CSH}$ have relatively low p-values for xgen-7b-4k-base, while $ϕ_{l2}$ does not, potentially indicating that $ϕ_{l2}$ would be better that the other methods if given a higher T?
4.	Question: Algorithm 3 uses the independence of blocks to increase the power of the submission's proposed tests. If one calculated $ϕ_{l2}$ using the parameters of only a single block, could that use Algorithm 3 as well to increase the power? That might provide a more comparable baseline. If that is the case, I would suggest evaluate against that as well.
5.	Suggestion: In section 4.3.1, highlight that you are evaluating $ϕ^i_{MATCH}$ rather than $ϕ_{MATCH}$.
6.	Question: Why were the other baselines not evaluated in Table 3?
7.	Suggestion: In Figures 4, 5, 6, and 7, it might be helpful to highlight which model pairs are dependent. 
8.	Suggestion: The use of the word 'sequel' (Section 3.2.1 and line 388) is confusing (what is the sequel, and the sequel to what?). I'd suggest clarifying what you mean by sequel or selecting a more appropriate word.

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
This paper explores the challenge of verifying whether two language models were trained independently or if one was fine-tuned from the other. The authors introduce a family of statistical tests to assess model independence by calculating exact p-values based on different measures of similarity in the models' weights and activations. These tests demonstrate robustness, remaining effective despite variations in training data or adversarial transformations that modify weights without affecting model output. Furthermore, the paper emphasizes the resilience of these tests even after substantial fine-tuning, providing a comprehensive evaluation across multiple models and fine-tuning strategies.

### Strengths
1. The paper offers a thorough and insightful examination of the problem, providing a novel approach to verifying model independence.
2. The authors present a rigorous method for testing model independence, incorporating statistical tests that generate valid p-values.
3. The proposed tests have been demonstrated to be effective across a range of models and transformations, exhibiting robustness even in complex scenarios and providing strong results across various experimental conditions.

### Weaknesses
1. Experiments mainly use decoder-only architectures, all around 7B parameters, lacking variation in model types and sizes.

2. Techniques like aligning hidden activations could be computationally expensive for larger or more complex models.

3. The tests focus on specific architectures (Llama-2) without exploring how different hyperparameters (e.g., layers, model size) affect results.

### Questions
1. Whether the proposed framework remains effective for encoder-decoder architectures (e.g., BERT) or encoder-only models? The framework’s validity across these different architectures is not discussed.
2. How sensitive is the framework to larger models beyond the 7B parameter range, or to smaller-scale models such as Phi-3?
3. Since the framework only detects dependence in open-source models, what are its specific real-world applications? Given the freedom and lack of control over open-source models, the framework may be limited to verifying model provenance in research or regulatory contexts.
4. What is the limitation of this framework?

### Soundness
3

### Presentation
2

### Contribution
3
