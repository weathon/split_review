# Consistency Checks for Language Model Forecasters

- Decision: Accept
- Avg Score: 7.25
- Scores: 8, 8, 5, 8

## Abstract
Forecasting is a task that is difficult to evaluate: the ground truth can only be known in the future. Recent work showing LLM forecasters rapidly approaching human-level performance begs the question: how can we benchmark and evaluate these forecasters *instantaneously*? Following the consistency check framework, we measure the performance of forecasters in terms of the consistency of their predictions on different logically-related questions. We propose a new, general consistency metric based on *arbitrage*: for example, if a forecasting AI illogically predicts that both the Democratic and Republican parties have 60\% probability of winning the 2024 US presidential election, an arbitrageur could trade against the forecaster's predictions and make a profit. We build an automated evaluation system that generates a set of base questions, instantiates consistency checks from these questions, elicits the predictions of the forecaster, and measures the consistency of the predictions. We then build a standard, proper-scoring-rule forecasting benchmark, and show that our (instantaneous) consistency metrics correlate strongly with LLM forecasters' ground truth Brier scores (which are only known in the future). We also release a consistency benchmark that resolves in 2028, providing a long-term evaluation tool for forecasting.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors expand on forecasting consistency checks pioneered as part of Fluri et al. 2024 (Evaluating Superhuman Models with
Consistency Checks). While that paper presented a proof-of-concept limited set of consistency checks on a single model, this work concretizes these checks into a set of usable metrics and demonstrates some of these metrics' high correlation with forecasting performance (as measured by Brier score).

These metrics include an arbitrage metric, incurring penalties according to how much guaranteed profit an arbitrageur can receive by exploiting the inconsistencies in the probabilities if they were market prices, and a frequentist metric, which uses a hypothesis testing setup to test whether a given forecaster could be sampling from a distribution based on adding noise to a consistent world model. The authors conduct experiments using a new already-resolved test dataset, and release another long-term forecasting dataset to resolve in several years (2028).

### Strengths
- Strong communication of the problem and proposed resolution
- Detailed data generation for both already-resolved experiments and an open-ended future forecasting benchmark
- Extensive discussion of decisions & limitations
- Principled theory and evaluation.
- Correlation plots indicate that the consistency scoring criteria could be used to generally select better forecasters.
- Theoretical and practical method to improve consistency at evaluation time.

### Weaknesses
1. Test-time ArbitrageForecaster does not gain consistency in an emergent set of checks; only those it is specifically designed to address. This reduces the impact of the paper slightly. Specifically, the ArbitrageForecaster appears to be narrowly optimizing for the consistency checks it is trained on, and does not generalize to other forms of consistency, suggesting that the consistency improvements are not indicative of a better world model, but rather an artifact of the optimization process. This raises concerns about the practical utility of the ArbitrageForecaster as a general method for improving forecasting quality.
2. New consistency metrics are rather easily Goodharted; one can imagine training a model on a vast set of synthetic forecasting problems respecting consistency checks in order to gain nearly perfect consistency scores with no improved knowledge of the future. This would limit the long-term efficacy of these metrics as a way to distinguish quality forecasters, unless novel checks are often added (which seems increasingly difficult without dramatically increasing the complexity of new checks). The authors do not address the possibility of models being trained to exploit the specific structure of the consistency checks, rather than learning genuine forecasting ability. For instance, a model could learn to output probabilities that satisfy the consistency checks without actually understanding the underlying relationships between the questions.
3. No comparison with system from Halawi et al. 2024: "Unfortunately, we could not reproduce the system from Halawi et al. (2024) at the time of writing, due to deprecations in the Google News API (we could not obtain access to the alternative Newscatcher API)." It is unclear if this is addressable in the longer term. It seems this comparison would be useful.

Nitpicks (grammar etc.):

- 2536 "with over the discrepancies"
- 2924 " are modifies "
- 184 May want to use P, R here for the input set of questions to distinguish from the output tuple P, Q and the input set of questions P, Q.

### Questions
1. Can you report confidence interval for the Brier score of a new model based on its consistency scores (so long as it is not Goodharted on consistency?) - e.g. with Fisher's z transformation?
2. Can one report, in addition to the correlation between Brier and each consistency metric, a ranking metric on the models' Brier performance based on the consistency ranking? It seems that selecting the best model/few models based on consistency scores is a critical use case.
3. Is there any way to ensure contamination-free or low-contamination consistency checking? Can we design an arbitrary search space for consistency checks that is large enough to not be saturated trivially by consistency training (see weakness 2).

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a novel approach to evaluating language model (LLM) forecasters, given the challenge of evaluating predictions with unknown future outcomes. The authors propose a consistency check framework that uses arbitrage and hypothesis testing as a metric, measuring logical inconsistencies across different, related forecasting questions. They build an automated system for generating forecasting questions, applying consistency metrics, and demonstrate that consistency scores correlate well with forecasting accuracy as measured by Brier scores.

### Strengths
* The manuscript is well-written, and the ideas are easy to follow.
* The paper effectively addresses the challenge of evaluating LLM forecasters by proposing new metrics based on arbitrage and hypothesis testing.
* It provides a thorough derivation and demonstrates a statistically significant correlation between the metrics proposed and Brier score.
* The authors also curated a dataset of forecasting questions, enhancing the evaluation for the future works.

### Weaknesses
 * The ArbitrageForecaster section would benefit from additional practical details, including parameter tuning, framework specifications, and methods for applying adjustments across various LLM models. Adding a framework visualization could further enhance clarity.


### Questions
* I wonder what's the performance for o1-mini for the negation and paraphrase experiment in Figure 3? Or is there any reason why the authors decided to evalute GPT4o instead of o1-mini?
* Given that the long-horizon benchmark evaluates consistency without ground truth, how do authors see the questions without ground truth being indicative of forecasting ability? Are there specific applications where such consistency checks alone could be considered sufficient?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies forecasting binary events using LLMs. They make numerous contributions involving consistency violations of binary forecasts. They introduce consistency metrics, propose an evaluation pipeline including the creation of two forecasting datasets, analyze correlation between consistency violations and the quality of the forecasts as gauged by the Brier scoring rule, a proposed forecaster to reduce violations, and a new benchmark where events are resolved in 2028.

### Strengths
This paper explores the important subject of using LLMs to forecast future events. Clearly a lot of effort has gone into the work, from the data generation aspects formalizing and running the evaluation pipeline. 

Another strength of the paper, at least from what I understand, is that the authors have tried to avoid data contamination issues that are prevalent in the literature involving the use of LLMs. They have also created a new benchmark for events resolving in 2028, which could be beneficial to the community.

### Weaknesses
I’m a bit confused by the focus of the study itself, which is to use logical consistency to evaluate a forecaster before resolution of the events themselves; presumably, the point of this is to evaluate forecasts sooner. But what is the value of using consistency as an early marker? There are likely confounding factors at play here that determine a model's affect on both forecasting consistency and the performance on the task. For instance, maybe a certain class of models (perhaps larger or trained in certain ways) are better forecasters – and many of these features are observable anyway, so why not just use these instead of consistency? I don’t understand why the authors have gone down this path and would like to know more about what motivated this line of work. Also, the observed correlation in the two instances doesn’t provide too much evidence for the claims, in my view, so I wonder about the generalizability of the claims. Frankly, I do not fully see the merits yet but I’m open to changing my mind. 

In my opinion, way too much (important) information is in the Appendix. I appreciate the space limitations, but I feel a lot of important material is missing from the main text, such as details about the frequentist metrics and details about the datasets. I did not get a chance to look closely at various parts of the Appendix.

The metrics themselves seem overly and possibly unnecessarily complicated. The rationale for these were also not provided clearly. What about something simpler, such as distances between scores that involve S? Perhaps I’m not understanding the complexity of scoring when arbitrary predicates are used for consistency. For example, it is unclear how the proposed metrics handle cases where the logical relationships are complex, involving multiple conditional probabilities or nested logical operators. The paper does not provide sufficient justification for the specific mathematical forms chosen for the consistency metrics, nor does it explore simpler alternatives that might be more interpretable and easier to implement. A more thorough analysis of the properties of the proposed metrics, including their sensitivity to different types of inconsistencies, would be beneficial.

The literature review seems too sparse. For instance, there are several papers on consistency in general, and probably many others on forecasting with LLMs. I will not point them out specifically but it is relatively easy to find more work. Perhaps the authors can consider expanding the related work section.

Section 5 came across as somewhat rushed, perhaps as it is somewhat preliminary and the results are not too promising, from what I understand.

### Questions
Here are some further questions and suggestions:

How large are the datasets created? Could the authors elaborate? I probably missed this information.

How can one be assured that the data contamination issue is not a problem for forecasting? I understand the authors have mentioned that they try to build a dataset that avoids this issue through time stamps – could they confirm if they are sure that there is no data contamination, in that the training data does not directly include information about the forecasted events? 

I noted several typos and related issues in the manuscript. Here are a few (most after resolution):

Line 82: “analyses can extend to …”

Line 107: should Forecast be in [0,1] rather than equal to the range? I’m not sure about this one.

Line 161 (footnote 1): “Manifold Markets use …”

Line 148-152: This choice seems arbitrary and merely pointing to an example with the sum of probabilities being 1.1 is not helping.

Line 169: “individual step …”

Line 242: what is “sensical”? Do you mean “sensible”?

Figure 1: The description mentions 3 metrics. Should there be 3 panels? Also, there is a space before a period in the caption.

Figure 2: What is COND? What is CONDCOND? It seems like some information is missing.

Line 324: “a proxy …”

Note that there are some citation style issues in Section 6.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes to evaluate large language model (LLM) forecasters by assessing the consistency of their predictions through a "consistency check", since ground truth is often unavailable about the future – we have to live and see!). Thus, the paper proposes an arbitrage-based and a frequentist metrics to detect logical inconsistencies. It finds good correlations between these consistency metrics and forecasting performance metrics (such as Brier score) tested on events that have already happened from a datasets established by this paper (one from prediction markets and one synthetically generated from news articles).

### Strengths
TLDR: This paper takes on a massive challenge and delivers as much as imaginable in such a hard setting.

**S1. Novel evaluation approach with a lot of effort and care to do things right:** The authors cleverly circumvent the need for ground truth in long-term forecasts by developing consistency metrics, validated by correlation measures and by carefully gathering datasets with events that resolved “between May 1, 2024, and August 15, 2024.”, so after the knowledge cutoff of the models. The consistency checks are clever and make predictions more interpretable, since they appeal to logic. Also, the paper includes many and diverse LLMs into testing. Well done!

**S2. Useful artefacts:** The paper creates a long-horizon consistency benchmark for forecasts resolving in 2028. This adds a massive a practical tool for future benchmarking, especially of more advanced LLMs that are yet to come.

**S3. Lots of details for reproducibility:** The paper provides a solid appendix with comprehensive documentation, including forecasting question structures, pipeline details, and explicit consistency conditions. This enhances reproducibility, makes the paper experimental design and choices easy to follow, and can make the potential applicability across related forecasting tasks real, by enabling other researchers to implement this on their own domain.

**S4. The paper’s writing is excellent.** Otherworldly.

### Weaknesses
 **Minor:** Limited breadth of data domains: Dependency on NewsAPI and Manifold and Metaculus for some forecast questions, while practical, may limit the breadth of testing topics and introduce data biases. But this is a minor issue, since the challenge taken on by this paper is massive, and the experiments were conducted with a lot of care, and the methodology presented in this paper can be extended to as many domains as possible (S3).


### Questions
Since the correlation between consistency metrics and forecasting performance metrics is conducted on events that have already concluded, is it not possible that the LLMs already know that, thus they are more accurate and more consistent in their predictions? I would assume that you chose events that resolved “between May 1, 2024, and August 15, 2024.” (L203), because that would be after the knowledge cutoff, right. But are we absolutely 100 percent sure that we know the actual knowledge cutoff of these models (since OpenAI loves switching things behind the scenes in the API without letting users know?)

L134, the phrase "We set V(F(x1), . . . F(xn)) to be the maximum such 'minimum profit'" could benefit from a rephrasing – "We define V(F(x1), . . . F(xn)) as the maximum achievable minimum profit from the arbitrageur…"

### Soundness
4

### Presentation
4

### Contribution
4
