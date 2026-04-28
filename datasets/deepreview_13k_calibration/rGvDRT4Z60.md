# FairPATE: Exposing the Pareto Frontier of Fairness, Privacy, Accuracy, and Coverage

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3

## Abstract
Deploying machine learning (ML) models often requires both fairness and privacy guarantees. In this work, we study the challenges of integrating group fairness interventions into the Private Aggregation of Teacher Ensemble (PATE) framework. We show that in the joint fairness-privacy setting, the placement of the fairness intervention before, or after PATE’s noisy aggregation mechanism (which ensures its differential privacy guarantees) leads to excessive fairness violations, or inefficient privacy budgeting, respectively. With this in mind, we present FairPATE which adds a rejection mechanism due to fairness violations. Through careful adjustment of PATE’s privacy accounting, we match the DP-SGD-based state-of-the-art privacy-fairness-accuracy trade-offs (Lowy et al., 2023) in demographic parity, and improve on them for equality of odds with 2% lower disparity at similar accuracy levels and privacy budgets. We also evaluate FairPATE in the setting where exact fairness guarantees need to be enforced by refusing to provide algorithmic decisions at inference-time (for instance, in a human-in-the-loop setting) thus trading off fairness with coverage. Based on our FairPATE, we provide, for the first time, empirical Pareto frontiers for fairness, privacy, accuracy, and coverage on a range of privacy and fairness benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The proposes a framework to integrate fairness into PATE. The proposed method is a simple adaptation of PATE which incorporates fairness constraints into the model's query rejection mechanism.

### Strengths
- The paper tackles a highly relevant issue in ML, addressing both theoretical and practical implications of fairness and privacy.
- The proposed framework is a simple adaptation of the existing PATE. Simplicity is a plus in my book.

### Weaknesses
 - Fairness is "enforced" by adding parity constraint within the aggregator which acts as a rejection sampling step on the basis of fairness. The general idea was proposed in several other works in the past, including the ones cited by the authors and against which the authors compare. It is thus difficult to understand what is new in the proposed framework. An explicit mention would help.
- A discussion on when to use the proposed framework in contrast to other frameworks is absent (see also my questions below).
- The experimental analysis should be improved. Some figures are misleading, e.g., same colors used for different algorithms (see questions below).
- The experimental results are not consistent across datasets. For example, the trends shown in the main paper do not hold for other datasets reported in the appendix, e.g., DP-Fermi produces better tradeoffs than FairPATE on the Adult dataset. This inconsistency is not discussed in the main paper, which could lead to a misleading interpretation of the method's performance. The paper should provide a more thorough discussion of the factors that cause these differences in performance across datasets.

### Questions
- I can't judge what is the impact of IPP (the rejection step added at inference time) on the overall results. Can you provide some ablation study showing how the framework performs on various datasets with different majority/minority distributions with and without IPP? 
- How does the framework work in case of some distribution shift? This is especially important in the context of my question above. 
- For the other datasets reported in the appendix the trends shown reverts, e.g., DP-Fermi produces better tradeoffs than FairPATE. Can you discuss why? What feature of the dataset makes this possible?
- Fig. 2 and 3 use orange colors for two different algorithms (Tran et al (Fig 2) and Jagielski et al. (Fig 3)). The authors should report all algorithms in all figures or justify their absence.
- Why Tran et and Jagielski et al. are not reported for the UTK-dataset experiment? 
- Paper [Learning with Impartiality to Walk on the Pareto Frontier of Fairness, Privacy, and Utility](https://arxiv.org/pdf/2302.09183.pdf) discusses a similar topic (although the contributions from this work are different) and it could be added to your Related work section.

Minor comments:

A lot of the cited papers have appeared in conferences. But the authors cite their arxiv version. I suggest to update the references accordingly.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work considers the inclusion of fairness constraints into a method for differentially private
(DP) training (or data generation from private data) based on transfer learning. The paper argues
that in this "PATE" approach which accounts of privacy concerns using DP, there is only one
sensible place to incorporate fairness using an intervention (i.e. adjusting what/whether) data
proceeds to subsequent PATE steps. This step is the point after the transfer from an ensemble of
teachers is made. The paper puts a mechanism there that will reject some queries/instances if they
result in violations of fairness which is a function of all of the prior decisions of the
mechanism. The work evaluates this approach relative to 2 other DP-based systems that incorporate
fairness showing mostly preferable trade-offs between fairness, accuracy, and privacy; though this
benefit is small.

### Strengths
+ Fairly well written and easy to follow.

+ The points of intervention discussions give a nice overview of the PATE approach and ways in
  which additional mechanisms can be independently injected. Note, however, the independent
  intervention assumption is a weakness below.

+ Rejection for fairness does give additional options for achieving fairness though this too comes
  with a weakness below.

### Weaknesses
 - The implications of rejecting for fairness are not considered. Rejection for privacy has
  implications in terms of privacy budget and likewise rejections for fairness come with
  implications and ignoring them might be responsible for the observed gains on the Pareto
  frontier. Consider the noted rejection example:

    "If at inference-time a decision cannot be made without violating a pre-specified fairness
     metric, then the model can refuse to answer, at which point that decision could be relegated
     to a human judge"

  The important implication here is that there will still be a judgement; it is just that the model
  will not be making it. Regardless of whether the result of the human judgement will produce fair
  or unfair overall statistics (that consider ultimate judgement whether by model or human), those
  decisions need to be incorporated into subsequent fairness calculus. Even if a query is rejected
  due to privacy, and if a decision is made for it subsequently, it would need to be accounted for
  in subsequent fairness decisions.

  Suggestion: incorporate ultimate decisions, whether by model or human, into the rejection
  mechanism; i.e. update counts m(z, k) based on human decisions. Given that humans might put the
  group counts into already violating territory, it may be necessary to rewrite Line 7 of Algorithm
  1 to check whether the fairness criterion is improving or not due to the decision and allow
  queries that improve statistics even though those statistics already violate γ threshold.
  Handling rejection in experiments will also need to be done but unsure what the best approach
  there would be. Perhaps a random human decision maker?

- In arguments for intervention points, assumptions are made which preclude solutions. They assume
  the intervention need to be made independent of other mechanisms in PATE. That is, they cannot
  consider information internal to decision making that is not described by Figure 1 like
  individual teacher outputs. This leaves the possibility that some fairness methods might be able
  to integrated with PATE in a closer manner than the options described. One example is that they
  might include the teacher outputs instead of operating on the overall predicted class like
  Algorithm 1 assumes presently. C3 in particular suggests that some interventions will not account
  for privacy budget correctly due to special circumstances and suggests at Point 4, they can be
  budgeting can be handled correctly. Nothing is stopping a design from refunding privacy budget if
  a query is rejected subsequently to an intervention point.

  Suggestion: rephrase arguments for why some intervention points are bad to make sure they don't
  also make assumptions about how the interventions are made and whether they can interact with
  privacy budget.

- Results in the Pareto frontier show small improvements, no improvements, and in some cases worse
  results than prior baselines.

  Suggestion: Include more experimental samples in the results to make sure the statistical
  validity of any improvement claims is good. This may require larger datasets. Related, the
  experiments show error bars but how they are derived is not explained.

- Comparisons against methods in which rejection due to fairness is not an option may not be fair.

  Suggestion: either integrate suggestion regarding accounting for rejection above, or incorporate
  some form of rejection (or simulate it) in the existing methods being compared to. It may be that
  the best methodology is not FairPATE but some existing baselines if adjusted to include fairness
  rejection option.

Smaller things:

- Rejection rate is not shown in any experiments. One could view a misclassification as a
  rejection, however. Please include rejection rates or view them as misclassifications in the
  results.

- The distribution whose fairness need to be protected is left to be guessed by the reader. For
  privacy, it is more clear that it is the private data that is sensitive and thus privacy
  budgeting is done when accessing that private data as opposed to the public data. For fairness,
  the impact on individuals in the private dataset seems to be non-existent as the decisions for
  them are never made, released, or implemented in some downstream outcome. I presume, then, it is
  the fairness needs to be respected on the public data.

  Algorithm 1 and several points throughout the work hint at this. However, there is also the
  consideration of intervention points 1,2,3 which seem odd as they points seen before any
  individual for whom fairness is considered is seen. That is, fairness about public individuals
  cannot be made there, independent of any other issues such as privacy budgeting. Further, Theorem
  1 discusses a demographic parity pre-processor which achieves demographic parity on private data
  which I presume is irrelevant.

- The statement

    "PATE relies on unlabeled public data, which lacks the ground truth labels Y"

  is a bit confusing unless one has already understood that fairness is with respect to public
  data. PATE also relies on private labeled data to create the teachers.

- The Privacy Analysis paragraph could be greatly simplified to just the last sentence regarding
  post-processing.

Smallest things:

- Double "violations" near "violations of demographic disparity violations".

- The statement "DP that only protects privacy of a given sensitive feature" might be
  mischaracterizing DP. It is not focused on features or even data but rather the impact of
  *individuals* on visible results.

### Questions
Question A: Is reasonable to ignore downstream decisions from queries rejected due to fairness
  (i.e. contrary to my suggestion in the weaknesses above)?

Question B: C1 makes a point that adding privacy after fairness may break fairness. What about in
  expectation? Were one to view the demographic statistics defining fairness measures in
  expectations, wouldn't they remain fair?

Question C: Theorem 1 makes a statement about a pre-processor inducing privacy parameter
  degradation but FairPATE (or PATE) appears to fit the definition of a pre-processor. If the point
  of the Theorem is to argue against pre-processors, isn't it also arguing against PATE/FairPATE?
  Unrelated, what is "ordering defined over the input space X" and why is it necessary?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discusses the problem of interactions between fairness, privacy, and accuracy constraints for PATE (Private Aggregation of Teacher Ensembles) type algorithms for differentially private learning. PATE style of algorithms first uses the private data (partitioned into several small partitions) to train base classifiers (teachers). Then, the algorithm uses these teachers to label some public data in a privacy preserving way. In particular, it cleverly chooses which points it can label without sacrificing too much privacy. Then another classifier (student) is trained on this newly privately labelled dataset, which is then released to the user. In this paper, this labelling step is used to also incorporate privacy constraints. Finally, the paper uses empirical evidence to suggest that their algorithm achieves a better privacy fairness accuracy trade-off than Loewy et. al. 2023.

### Strengths
* The paper is written quite clearly and is easily readable. The arguments of the authors come out clearly without ambiguity and the reader can easily follow the train-of-thought. I appreciated that very much.
* I also found the main algorithmic idea of this paper quite nice. The idea of that the algorithm chooses which points to label not only on the bassi of the privacy constraint but also the fairness constraint is quite neat and could be useful in other contexts. I appreciated this.

### Weaknesses
Despite the interesting idea of the paper, I am unable to support this paper for acceptance. The four main reasons are as follows (in decreasing order of severity).

1. __W1__ Significance: The paper aims to convey the significance of its contribution through experimental results (and I don't think there is anything wrong with it and in general support extensive empirical results), but the experiments present a rather bleak picture of the advantages of FairPATE.
    * **Minimal improvements** Most importantly, there are rarely any results where the improvements of PATE over baselines is larger than 1\%. For example in 1. Credit card dataset and 2. parkinson's dataset, there results differ by less than $1\%$.
    * **Several examples of underperformance** Several examples also show that FairPATE performs significantly worse than competitor. Examples include Demographic Parity for Adult dataset and UTK Face ($\epsilon=5$).
    * **Misleading regarding diversity of experiments** In the introduction, the paper sells itself regarding performing a wide range of experiments but results on nearly half of these datasets are hidden away in the appendix without any mention in the main text and without comparisons. Experiments on **CheXpert, CelebA, FairFace, and Retired-Adults** are not available in the main text and it is very hard to interpret the results presented for this in the appendix.  In fact, there are **no results of FAIR-PATE on CheXpert** in the paper
    * Please show comparison on these for demographic parity and equalized odds (similar to Figure 2,3 with comparison to Loewe et. al.'s algorithm) on these four datasets. In addition, there are results in the literature that run DP algorithms on CelebA and CheXpert. Comparisons should be made to them to show what is the sacrifice being made compared to state-of-the-art.

2. __ W2__ **Wrong Conclusion from Theorem 2** I did not go through the detail of Theorem 1 but I assume it is correct and follows from Group privacy arguments. However, the sentence above Theorem 1 (Point C2) claims that the result proves that  " pre-processing ... will necesarrily degrade the guarantee of the .... private learning mechanism". How ever this is not what the Theorem shows. The theorem only proves a privacy guarantee of $M\odot P_{\text{pre}}$ not that this is the tightest privacy guarantee possible for the composed mechanism. Am I missing something ?

3. __W3__ **Abstaining from prediction for fairness reasons** The introduction justifies this as _"if a decision cannot be made without violating a pre-specified fairness metric, then the model can refuse to answer at which point the decision can be relegated to a human judge"_. If I have understood this correctly, this is a flawed argument. For example, consider the situation where there are group of data points from the majority group, on which if the algorithm predicts correctly the fairness will be violated and hence the algorithm abstains. Nevertheless, the prediction is easy for this group and the judge nevertheless predicts on them correctly and the overall fairness is still violated. Isn't this pointless then to relegate this to the judge ? Intuitively, it appears that any problem can be made fair this way by simply refusing to predict on certain majority groups thereby artificially boosting the fairness of the algorithm. The correct fairness solution should aim to improve performance on the minority group instead.


4. __W4__  **Unfair Comparisons** Fair-PATE  and Loewy et. al's algorithm do not work under the same restrictions of differential privacy. Specifically, Fair-PATE uses public unlabelled data and Loewy et. al doesn't and we know that (even a small amount of) public data can severely help in improving accuracy of DP models (perhaps fairness too). Hence, it appears to me that Loewy et. al. uses a significantly stricter notion of privacy and achieves nearly comparable result and in some cases even better (for tabular datasets, there are no comparison on vision datasets with Loewy et. al.).

### Questions
* **Motivation** I understand that there are several works showing that privacy incurs a sacrifice in fairness. However, one possible approach to this problem is simply improving the accuracy and perhaps the resultant accuracy also leads to high fairness. In fact Berrada et. al. (2023) makes this argument with some experiments in their paper. I did not see an argument in this paper why this approach is not expected to solve all problems. Why should there be a trade-off between privacy and fairness ? Is it known in the literature and are there theoretical studies arguing about the necessity of a trade-off ?

* **Missing baselines** Why is there no comparison with the algorithm of Zhang et. al. (2021), Kulynuych et. al. (2022) and Berrada et. al. (2023) ? They are mentioned in one or two sentences at the very end of the paper but without any comprehensive empirical comparison.
* **FairDP-SGD" What is FairDP-SGD ? It doesn't seem to have been defined anywhere ? Is it an existing work ? Where is FAIR-PATE's result on CheXpert ?

* In addition to this, please also also address __W1,W2,W3,W4__.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
