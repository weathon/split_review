# Conformal Prediction Sets Can Cause Disparate Impact

- Decision: Accept
- Scores: 5, 8, 8, 8

## Abstract
Although conformal prediction is a promising method for quantifying the uncertainty of machine learning models, the prediction sets it outputs are not inherently actionable. Many applications require a single output to act on, not several. To overcome this, prediction sets can be provided to a human who then makes an informed decision. In any such system it is crucial to ensure the fairness of outcomes across protected groups, and researchers have proposed that Equalized Coverage be used as the standard for fairness. By conducting experiments with human participants, we demonstrate that providing prediction sets can increase the unfairness of their decisions. Disquietingly, we find that providing sets that satisfy Equalized Coverage actually increases unfairness compared to marginal coverage. Instead of equalizing coverage, we propose to equalize set sizes across groups which empirically leads to more fair outcomes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work is motivated by the well-known problem of group-conditional coverage in conformal prediction: when an underlying predictive model is more inaccurate on some subgroups than others, achieving equalized coverage over subgroups requires providing prediction sets that vary in size across subgroups. The work conducts a human study in which human decision-makers are presented with prediction sets as a decision aid; the study suggests that their accuracy improves at different rates across subgroups.

### Strengths
The authors rightly identify "equal coverage" as a limited notion of fairness for prediction sets, in the sense that the end-goal of providing prediction sets is ultimately to improve a downstream task -- i.e., equalized coverage in itself ought to be desirable only to the extent that it improves the utility of predictions in general. Evaluation via human study is also an important perspective; I see this work as playing a similar role as the work that conducted human evaluations of explainability methods. I also appreciate that authors mention (non conformal) methods for providing prediction sets.

### Weaknesses
* The main weakness of this work to me is that its hypotheses are a priori unsurprising. If some subgroup A requires larger set sizes for the same coverage level, it is tautologically true that there is higher uncertainty for subgroup A and that any class in the prediction set is less likely to be the ground-truth label. Even if a person relied 100% on the prediction set and simply picked uniformly at random among the predictions, one would expect performance to be worse on groups with bigger set sizes. This is a fundamental property of prediction sets and not necessarily a novel finding about human behavior. The paper doesn't sufficiently address why this is a surprising or important result.
* Therefore, I find the results to be less 'disquieting' than the work seems to suggest. Over the baseline of no assistance, it seems that all methods approximately improve accuracy, and I don't really see why it's a bad thing that some groups benefit more; the paper does not make a case _against_ using conditional CP methods for bias reasons. (That is, why artificially reduce accuracy, i.e. worsen outcomes, for the easier subgroups? It's not clear to me how that would be normatively defensible, e.g. in a high stakes medical task, and I would push back on the language of "increases unfairness".) It would certainly be a bad thing if conditional CP somehow made human prediction worse than marginal CP; a different question that could/would have been interesting to ask is not whether max disparity increases, but rather whether accuracy actually improves from seeing conditional prediction sets or not. That is, something like H0: for all subgroups, accuracy using marginal and accuracy using conditional prediction sets is the same; H1: for at least some subgroups accuracy increases or decreases. The paper focuses too heavily on disparate impact without considering the overall utility of the prediction sets.
* It is also surprising to me that the baseline is no assistance rather than providing a point (top-1) prediction; the latter seems like the more natural comparison for a prediction set and could potentially illustrate more significant per-subgroup disparities, especially with more variation in top-1 accuracy. The current baseline makes it difficult to assess the true value added by the prediction sets.
* Finally, minor comment on experimental design - I should preface this comment by saying I'm not an expert in this kind of study design (though I am familiar with other approaches to randomized experiments and hypothesis testing). However, I am not confident that the numerical results (i.e. those summarized in Table 2) lend themselves to clear statistical interpretations - e.g., given the computed point-estimate ORs, how are we meant to interpret (max) ROR, and where does that uncertainty propagate? How are significance thresholds computed? This is especially concerning given that for FACET, the only dataset where set sizes differ by more than 1, all the ORs themselves essentially all hover around 1/ just barely at significance. That said, I think the primary value of this work is the high level characterization of how humans use and interpret prediction sets (as opposed to applications of RCTs in econ/medicine/etc, where precise interpretations and therefore rigorous experimental design are more consequential).

======

Minor presentation notes:

* Exchangeability - should probably be formally defined. Saying that it is "realistic in practice" (086) is a pretty strong statement, in my opinion. I personally consider the exchangeability/iid distinction to be more formal than practical - I've very rarely seen practical applications that are exchangeable but not iid. This is not central to the claims of the paper and I'm not necessarily counting it as a weakness; I just found that statement to be distracting.
* Eq 8 - assuming `Cov` means `Coverage` but would probably be nice to define it formally first
* L241 - minor typo in this sentence I think.

### Questions
* Fig 1: what is the x-axis? 
* Table 1: is the "coverage" column for the conditional method computed on average? 
* Table 2: significance levels are for the null of OR = 1?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors design a randomized trial to study the impact of utilizing conformal prediction (CP) sets in machine learning decision pipelines with a human in the loop. They find that utilizing a "fair" notion of CP (a notion which ensures coverage for each sensitive group) can actually exacerbate disparate impacts in the pipeline.

### Strengths
* The background on conformal prediction provided by the authors is well written, as are the justifications for the models picked at inference time.
* The authors pre-registered the hypothesis they tested
* I think the findings are generally novel and interesting. As figure 5 indicates, the fact that utilizing Mondrian CP can reduce accuracy for on certain groups has important implications for fairness practices when prediction sets are required.
* Generally, this feels like a paper that could spark some new work on fairness in CP, so I believe it will be of interest to the ICLR community.

### Weaknesses
 * The authors primary focus is to study disparate impact as measured by improvement *gain* from a given CP treatment (as compared to a control). This is fine, but I would argue that if a CP treatment improves accuracy on each sub-group (even if at a different amount) then this isn't necessarily a bad thing, for example the minimax fairness would be improved. In this sense, I actually found figure 5 the most interesting observation, as it indicates how Mondrian CP can actually leave the worst-case groups, off worse. In general I would suggest more discussion on the trade-offs of the specific fairness definitions the authors use.

### Questions
* Could the authors provide further discussion on the implication of using conformal set size as a proxy for difficulty? I believe this is a reasonable proxy for difficulty but obviously it is also related to the treatment, does this have any effect on the analysis?
* A clarification question on equation 9. Does trial j refer to an entire task (e.g. text classification) or one sample from an entire task?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper study conformal prediction setup, and want to ensure group fairness in outcome, as measured by disparate impact (final decision made). They study via human experiments, how two different fairness metrics on the prediction sets (fairness on the coverage or of the size) and show that i) the former worsens the actual fairness of the outcome and ii) the latter does improve it.

While I was not familiar with the conformal  prediction setup, I found the paper easy to read and it sparked my curiosity. From the research perspective, I believe that this paper is extremel valuabley to ensure that metrics are well grounded in actual outcomes.

### Strengths
As mentioned, I find that such connection between metrics on the set and end-behavior are needed. Paper is quite easy and claims are well supported by evidence.

### Weaknesses
Abstract could be a bit clearer, in particular for people less familiar with the subject.

### Questions
I am curious about the relationship between the Fairness in Conformal predictions and Fairness in Classifiers. Let's imagine a 3rd experiment, where the base classifier is fair and the conformal prediction setup is applied without any fairness constraint. What would the results look like>?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a user study highlighting concerns regarding conformal prediction (CP) in practice. The authors show that $(i)$ CP can exacerbate fairness concerns when humans make decisions; $(ii)$ using equalized sets rather than equalized coverage (as previously proposed) leads to fairer outcomes in practice.

### Strengths
The main strengths of the paper are:

S1) the empirical evaluation is strong enough, involving different data types and settings;

S2) the proposed user study sheds light on some of the limitations of conformal prediction and provides an interesting counter-example to traditional approaches mitigating unfairness in conformal prediction;

S3) the work is overall well-written and easy to follow.

### Weaknesses
I do not have significant concerns regarding the work. I list here a few comments/suggestions regarding a few potential limitations worth discussing in the current version of the paper:

1) When considering selective prediction (see e.g., [1] for a survey), Bondi et al., (2022) [2] show that human performance is affected by how and which information is passed to them. Their experiments consider different settings and show that human performance increases when humans receive only the " deferral " information, and the ML model is good at solving the task. Similar considerations could also be taken into account in this setting.

2) As noted in De Toni et al. (2024), conformal prediction is mainly beneficial when the classification task regards several classes. When the task is binary, most methods fail to provide useful sets, as when both classes are returned, this does not help humans. I wonder whether this consideration might hinder the external validity of the paper's findings, as the current experiments concern only multiclass settings ($m\geq8$ for all three datasets).

3) I would be more cautious regarding lines 477-479. Ruggieri et al. (2023) [3] show that performing conditional corrections at the group level does not ensure an overall improvement in terms of fairness due to the Yule Effect. If my understanding is correct, generating more singletons per each protected group is equivalent to performing "conditional corrections"; hence, the Yule Effect might still occur. This means equalizing the number of singletons across groups might not always be the right solution.

### Questions
I have a couple of questions for the authors:

q1) in the background section, I think the definition of conformal and non-conformal set predictors can coincide, depending on how $s()$, $f()$ and the relative quantiles are defined. Am I correct?

q2) regarding the previously highlighted shortcomings, can the authors elaborate on W1, W2 and W3?

### Soundness
3

### Presentation
3

### Contribution
3
