# Incremental Causal Effect for Time to Treatment Initialization

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
We consider time to treatment initialization. This can commonly occur in preventive medicine, such as disease screening and vaccination; it can also occur with non-fatal health conditions such as HIV infection without the onset of AIDS; or in tech industry where items wait to be reviewed manually as abusive or not, etc. While traditional causal inference focused on `when to treat' and its effects, including their possible dependence on subject characteristics, we consider the incremental causal effect when the intensity of time to treatment initialization is intervened upon. 
We provide identification of the incremental causal effect without the commonly required positivity assumption, as well as an estimation framework using inverse probability weighting. We illustrate our approach via simulation, and apply it to a rheumatoid arthritis study to evaluate the incremental effect of time to start methotrexate on joint pain.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In many settings, whether or not a subject receives a treatment at any given time point may be a function of their covariates.  In these settings, we can reason about the time to treatment from when an individual becomes treatment-eligible to when they actually receive treatment.  Such a model can allow us to reason about how changes to covariates can affect time to treatment and, through treatment, some relevant outcome.  This model has the benefit of not requiring the positivity assumption.  The authors define this model in terms of hazard functions and provide an estimator.  They then assess their model on both synthetic and empirical data and demonstrate how it can be used to inform policy/medical practice decisions.

### Strengths
While there are some clarity issues with the narrative of the paper, the individual sections and descriptions in the paper are clear and easily readable.  The literature review on incremental causal effects and time to treatment is very thorough, situating the paper nicely in the literature.  The examples chosen, especially the rheumatoid arthritis example, are strong, and the analysis of the rheumatoid arthritis experiment (the reasoning about doubling the hazard decreasing joint pain) is especially compelling and highlights very nicely how this method could be used in practice.

### Weaknesses
The biggest weakness of this paper in my eyes is that the problem being solved is not clearly defined.  Some of this seems to be due to language issues (while the occasional grammatical issue or awkward phrase don't generally impede understanding, there are a few parts where the intended meaning isn't clear), and some of this is due to the lack of a clear motivating example".  Specifically:

- In the introduction, the authors define an incremental intervention as an intervention "that is not pre-specified, but rather a function of the observed treatment distribution."  Without defining what is meant by "the observed treatment distribution", I assume that it means which units in the sample population received treatment and which didn't (P(T)), or maybe the conditional probability distribution in the sample population (P(T|L)).  I'm having a hard time understanding what this means, even after having read the whole paper.  The example in this section, as well as the MTX use case in the experiments, seem to deal with an intervention on treatment (such as being assigned to a behavioral health program or being prescribed MTX) that is, presumably, informed based on the individual's covariate values.  So this is an intervention that is a function of the observed covariates, not "of the observed treatment distribution."  Am I misunderstanding something about your approach here?

The organization of the introduction seems a bit backwards to me.  The example in the third paragraph (probationers being assigned to behavioral health services) is a great motivating example for the general "time to treatment initialization" problem setting.  The first paragraph contains two good examples, but the narrative about "time to treatment" is not made clear.  For example, the first 4 sentences of the paper talk about a tech team struggling to keep up with review requests and asks the reader to consider the effect of doubling the number of reviewers on the processing time of requests.  Coming into this paper with causality in mind, this sounds an awful lot like reasoning about intervening on a treatment (the number of reviewers) and measuring the effect on an outcome (the processing time).  However, as becomes clear later in the paper, the "processing time" is not, in fact, the outcome, but the time until treatment.  And if that's time until treatment, then I suppose treatment = somebody reviewing a request.  But then I'm not sure what the outcome is....backlog size??

If you want to open with that example, you should start by clearing explaining how it maps to your problem. An example flow, assuming I'm understanding the problem correctly: "We're interested in understanding how long it takes people on a tech team to respond to review requests.  The time until review is not static, but depends on many features, such as how many reviewers the help desk has at that time. 
 After a system outage, the number of requests has increased, creating a large backlog.  The scheduler wants to decrease the size of this backlog, which they plan to do by decreasing the time until review.  The number of reviewers has a large effect on the time until review, so the scheduler decides to double the number of reviewers, which then doubles the likelihood of a request being reviewed at any given time, as requests are often selected for review at random.  This process - reasoning about percentage changes to covariates to determine their effect on time to treat and, thus, the effect of treatment - is called "incremental causal effects"."

The second paragraph of the introduction also oddly placed.  Digging into the different types of interventions is interesting, and the distinctions brought up are quite relevant, but without having a clear problem statement yet, it's unclear how to fit your proposed method into that framework.  I think you're missing a paragraph in the introduction where you define (not technically, but in straightforward language) your problem statement. (i.e., the time until treatment for each subject is based on some measured covariates; the outcome is an effect of that treatment and starts be recorded as soon as treatment is applied to that subject; we want to reason about how changes in the probability of treatment function affect outcome).

Section 1.1 is focused on, and named after the positivity assumption, and highlights bypassing the positivity assumption as a key advantage of incremental causal effects.  However, this section, from what I can tell, never actually explains how it bypasses positivity.  (Also, the phrase "avoids the positivity" is weird - reword that) It's only the introduction, so I don't expect an in-depth explanation yet, but given that it's a whole section in the intro about positivity, at least a sentence giving an intuition about why we can ignore positivity would help.  Following on from that about positivity, it looks like it's addressed in the first paragraph of the Related Work section.  However, the explanation in the related work is not very clear or detailed (and again, especially given how prominently positivity was just highlighted in the introduction, I expected a deeper/clearer explanation).

Some terminology explanation is missing.  Line 171 defines $\lambda(t|l)$ and $\Lambda(t|l)$ as just "its hazard function and cumulative hazard function at time t given L = l, respectively."  I assume "its" here refers to T.  However, from what I can see, you never actually define either hazard function, despite them being fairly core to your method.

I like the setups chosen for both the synthetic and empirical experiments, but the lack of a baseline makes interpreting the results near-impossible.  For example, in the simulation results, you say that your results illustrate that the incremental causal effects "perform well with small biases."  I'm struggling to see how you came to that conclusion from Table 1 alone.  Looking at the numbers in the "Bias" row, they look low, but are they actually low for that problem?  Did you use additional visualizations to come to the conclusion that these numbers represent good performance?

Between the clarity issues throughout and the difficulties in interpreting the experimental results, I don't feel comfortable voting for acceptance.  If these issues are adequately addressed, though, I'm open to increasing my score.

### Questions
Can you explain which pieces of this work are novel/provide a contributions list?  From the introduction, it looks like the move to continuous time to treatment is new.  However, the abstract makes it sound like avoiding the positivity assumption is also novel, while the paper makes it seem like that was something that was already shown as a property of incremental causal effects.

I'm not used to seeing L chosen as the variable for covariates/potential confounders. (I've seen W, X, V, C....) It's not a problem, but is the choice of L based on any particular subset of the literature?

As per my confusion in the Weaknesses section, can you clarify what you mean by an incremental intervention being one that is "a function of the observed treatment distribution"?

In the second paragraph of the introduction, you state that, in a static intervention, "the subjects are either all treated or all untreated", in contrast to a dynamic intervention, where treatment could depend on covariates.  This makes it sound like the entire population is either all treated, or all not treated.  This is a valid scenario to consider (e.g., a state government policy that then affects everyone living in that state), but you describe static interventions as being "typically the case when considering an average treatment effect (ATE)", in which case, you typically need examples of both treated and untreated subjects.  I would assume that you meant "each subject is either treated or untreated, assigned independently of their covariates", but that's not particularly close to what you wrote, so I must be misunderstanding something.  Actually, reading the abstract of Bonvini et al (2021), they describe ATE as relating to "the effect of everyone deterministically receiving versus not receiving treatment" - as in, the counterfactual question.  Is that what you're referring to here?

Especially in medical examples (such as the MTX arthritis example), individual covariates can change over time.  Does your model take into account that an individual's covariates L could change over the timesteps before they get treated, which could in turn affect the probability of treatment?

I'm not following the explanation at the beginning of Related Work about how incremental intervention avoids making the positivity assumption.  Summarizing Kennedy (2019), you say that, for subjects with 0 or 1 probability of treatment, we can see positivity as always satisfied "because perturbing the odds does not change their degenerate probabilities".  How does that follow?

In the line before Theorem 1, it says "We prove that ([1]) can be identified".  What is ([1]) referring to here?  Are you referring to Theorem 1?  Assumption 1?  Equation 1?

Are there any baselines you can use for comparison in the experimental results?  Some other effect estimation method, or at the very least some naive baseline that could provide some calibration for the experimental results?

### Soundness
3

### Presentation
1

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
This paper extends INCREMENTAL CAUSAL EFFECT to continuous-time treatment. To this end, the author shows that the target quantity is identifiable under certain assumptions, excluding the well-known positivity assumption. An estimator is then proposed that is consistent. The effectiveness of the estimator has been validated through empirical experiments.

### Strengths
1- The paper addresses an important problem and proposes an algorithm to solve it.

2- The proposed approach has been analyzed both theoretically and empirically.

### Weaknesses
1- Some definitions in Subsection 3.1, such as the hazard function and related concepts, are not clear to the reader. It would be beneficial to provide more detail, as there is still enough space available.


### Questions
1- How is it possible to analyze the estimator with finite sample data? For example, is there a high-probability guarantee for it?

I am not completely familiar with the area covered in the paper, and I’m uncertain about its contribution to the field. I may revise my score after considering the feedback from other reviewers.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies a novel setting in causal inference: incremental causal effect of intervening the continuous time to treatment initiation by shifting the hazard function. It introduces an IPW estimator with proofs of consistency and asymptotic normality. It is also validated through empirical simulations and a real-world study.

### Strengths
1. This paper extends incremental causal effects, which do not rely on the traditional positivity assumption, to a new setting. This advancement allows for new approaches to studying time-to-treatment problems in fields such as public health and policy-making.
2. Theoretical guarantee is provided.
3. The presentation and flow of this paper are clear.

### Weaknesses
1. Additional experiments could provide deeper insights into the behavior and robustness of the proposed approach under different scenarios. For example exploring different shift interventions, hazard functions, and comparative analysis against any alternative estimators.

Minor comments:

2. The clarity of Theorems 2 and 3 could be improved by stating all conditions and notations explicitly.
2. In the simulation, it can be made more clear to state the true effect and whether the outcome is censored in the DGP.
3. Typos: in line 59, line 340, and Theorem 3 proof.

### Questions
1. If there is unmeasured confounding, is it natural to apply sensitivity analysis or proximal causal inference in this setting? How might these approaches integrate with your proposed IPW estimator?
2. Are the regularity conditions outlined in Theorem 2 and Theorem 3 considered trivial or standard in common survival models?
3. Is there any pattern in the estimator performance (bias, variance, or stability) as $\theta$ changes?

### Soundness
3

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
4

### Summary
This paper proposes a novel methodology for estimating incremental causal effects in continuous-time settings, with a specific focus on time-to-treatment initiation. This approach intervenes on the intensity (hazard function) of treatment initiation without relying on the positivity assumption. By shifting the hazard function through a multiplicative factor theta, the authors develop an identification strategy using inverse probability weighting. Theoretical justification, along with both synthetic and real-world experiments, is provided.

### Strengths
1. The paper addresses a gap in causal inference by extending incremental causal effects to continuous time-to-treatment initiation, an area that has not been extensively studied before.
2. The authors provide consistency and asymptotic normality theorems for their estimand, adding theoretical rigor to their approach.
3. The paper is well-written and easy to follow. I particularly like the related work section which offers a comprehensive background that is beneficial for readers.

### Weaknesses
1. A major strength claimed by the authors is that the new estimand avoids the positivity assumption. However, as noted in related work (line 125), "Kennedy (2019) proposed an incremental intervention that fully resolved the positivity issue." Since this paper also focuses on incremental causal effects, this aspect of the contribution may lack novelty.
2. In the synthetic experiment, only a single feature L is used, following a simple uniform distribution. The experiment would be more robust if it included multiple features and more common distributions, such as Gaussian. Additionally, the experiment would benefit from comparisons with other baseline methods, as the paper currently presents only the performance of their model without comparative analysis.
3. In Section 4.2, the authors mention that the decreasing trend in the average number of tenders aligns with findings from a 2002 paper. While it is always impossible to know the true causal evidence in real-world cases, a quantitative comparison of the estimated causal effects with results from other studies would strengthen the paper beyond trend consistency alone.

### Questions
See weaknesses.

1. Line 65: The paper states, "In general, the incremental causal effect has the interpretation of a policy effect on the population, instead of the therapeutic effect on an individual." This reminds me the field of reinforcement learning (RL), which is specifically designed for learning policy rewards. Could there be potential benefits in using RL to learn incremental causal effects?
2. Could you provide a concrete example to illustrate the difference between "time to treatment initiation" and "continuous time to initiating treatment"? These terms appear several times in the paper, but their distinction remains unclear to me. Since this paper focuses on the continuous version, clarifying this difference could help motivate the choice.
3. Line 340: typo 25$ should be 25%.

### Soundness
2

### Presentation
3

### Contribution
2
