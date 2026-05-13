# A SYSTEMATIC STUDY ON EARLY STOPPING CRITERIA IN HPO AND THE IMPLICATIONS OF UNCERTAINTY

- Decision: Reject
- Scores: 3, 8, 3

## Abstract
The development of hyperparameter optimization (HPO) algorithms constitutes a key concern within the machine learning domain. While numerous strategies employing early stopping mechanisms have been proposed to bolster HPO efficiency, there remains a notable deficiency in understanding how the selection of early stopping criteria influences the reliability of early stopping decisions and, by extension, the broader outcomes of HPO endeavors. This paper undertakes a systematic exploration of the impact of criterion selection on the effectiveness of early stopping-based HPO. Specifically, we introduce a set of criteria that incorporate uncertainty and highlight their practical significance in enhancing the reliability of early stopping decisions. Through a series of empirical experiments conducted on HPO and NAS benchmarks, we substantiate the critical role of criterion selection, while shedding light on the potential implications of integrating uncertainty as a criterion. This research furnishes empirical insights that serve as a compass for the selection and formulation of criteria, thereby contributing to a more profound comprehension of mechanisms underpinning early stopping-based HPO.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper offers an analysis of the implications that arise from using different metrics for decision making in multi-fidelity HPO. It offers several insights, including that sometimes using training performance for decision making is better than using validation performance and also offers some explanations for this and remedies that reduce the risk of using the wrong variables for decision making in pratcice.

### Strengths
I think the paper addresses a potentially interesting question and also employs some formal rigor in the analysis. It is mostly clearly written and also coherent in the steps taken.

### Weaknesses
I have to admit that I am a bit confused about the contribution and relevance of the paper, and also, in parts, about some of its technical aspects.

Before going into the details, I would like to make a subtle remark on the terminology. The paper consistently talks about early stopping, but there is some recent effort to distinguish this type of stopping (early *discarding*) from simple early stopping, which is the classical case in GradientBoosting or neural networks, i.e., to stop learning as soon as the *learning curve* is stall, independently of performances observed for other learners. This paper uses the term early stopping for both simultaneously. A detailed explanation of this can be found in [1]. The usage of the term "early stopping" is particularly confusing in the context of Hyperband, because literally in the classical sense this has nothing to do with early stopping but re-evaluating (re-training) the model on different budgets. I nthe context of the paper, since neural networks are considered, one can think of Hyperband a bit like a freeze-thaw mechanism, but still this is early discarding and not early stopping, the latter of which would only examine learning curves in isolation.

At a high level, I am missing a clear contribution in this paper and also a red path. The paper reads a bit like a collection of experiments that somebody conducted to study different aspects of uncertainty in HPO but also to analyze certain methods. Most of the insights are very intuitive and would not even require a detailed study. So I guess I also miss some rigor in the paper and do not have a clear takeaway. It is strange, because the paper is not technically poor, and also the topic itself is interesting. Still I feel like I did not learn anything particularly useful reading the paper. Also, the paper is somewhere between an insight paper and proposing certain techniques to improve a situation. For an insight paper, the data basis is too small and the insights are much too vague. For a technical contribution paper, the comparison is lacking. I was very much reminded of one very successful insight paper submitted to this very venue on the effect of the batch size on overfitting [2]. The paper is not related topic-wise but provides a very nice technical explanation on a rather surprising phenomenon, while what we see in this paper is mostly not surprising but very expected. This does not mean that the topic is not interesting, but I think it needs to be exposed in a different way.

here are some detailed remarks on some parts of the paper.


1. I do not really understand Section 2. The authors suggest that the evaluation criterion could be a choice of the HPO tool for early discarding, but this is often not really a choice but a requirement imposed by the use case. While it is true that in NNs one often has both accuracy and loss, it is not really clear to me what the authors here see as the decision variable. Also, I think that "performance metric" or "performance measure" could be a more reasonable term than "criterion", because criteria often suggests also aspects different to performance such as runtime. As a matter of fact, the term "criterion" is used later in the paper to refer to other concepts (Sec. 4). I presume that they want to say something like "it is not clear whether the best metric for stopping is the loss that is being optimized or an external metric such as accuracy and whether one should use the training performance or validation performance". This would then motivate the four cases they look at, but the author's don't phrase it like this, so I am not even sure whether I understood the motivation right.

Next, in the same section, the author's talk about reliability of criteria. What is this now supposed to mean? Implicitly, it gets clear later in 2.2 that the authors refer to test performance as some kind of ground truth and the question is whether the measures used for decision making are faithful in the sense that they do not discard the candidate with the eventually best test performance. At least to me, it is not clear why test accuracy is the eventual objective. This is not necessarily so (accuracy is a non-continuous metric, so one could at least argue for log-loss or Brier score), and in these cases one could also uses these as a loss. Btw. what did the authors use as a loss? I presume its cross-entropy loss, i.e., log-loss, which would make it even less clear why the objective should be test accuracy.

I also do not understand the selection of results for Fig. 1. It seems it is the NAS201 datasets + 2 from LCBench. Is this right? Why do you clip away 4 of the LCBench datasets?

2. In the theoretical part, I see several issues. First, the section lacks a bit clarity on whether D refers to the training data or validation data. Apparently this precisely depends, because D is the data used to estimate \hat f^t, and this can be either training or validation data, depending on whether one computes training/validation accuracy/loss. More importantly, there is a logical mistake. You cannot argue that tighter bounds on the regret imply lower regrets (this is only a conjecture), because the regrets can easily move always in the same range, and only in one case you have higher slacks to the bounds. Personally, I also find the statements a bit contradictory to the observations in Sec. 2, because on the "complex" tasks like CIFAR and ImageNet, not only the training data is bigger but also the validation fold should be much bigger than on the smaller datasets, so one would expect that the validation performance is also more reliable as a criterion. Apparently this is not the case, but I do not currently see how Sec. 3 resolves these doubts.

3. I think that the complexities of the networks in NAS201 and LCBench is inherently very different, which adds a confounding factor to the whole setup. I presume that the variability in NAS201 is much higher than in LCBench, which only has funnel-shaped networks.

4. The experiments conducted in 4.2.1 remain largely unclear to me. I mean, I understand what the authors want to demonstrate, but a lot of technical details are missing so that I it is hard to interpret the results.

### Questions
What did you use as the loss in the neural networks? Cross entropy?

In the theoretical part, shouldn't we expect better decision making precisely for large datasets, i.e. isn't this contrary to the findings in Sec. 2? I guess it can next be explained by |D| not being the only factor but also the model complexity, which induces higher variance if |D| is large and the model is flexible. Would you agree?

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper  systematically examines various early stopping criteria in HPO and proposes effective uncertainty-driven criteria .

### Strengths
The insights and conclusions look reasonable and well-supported. 

Well-organised and quite easy to follow the logic.

### Weaknesses
The significant differences among different criteria from section 2.2 would be expected as claimed in the paper; 

Including brief introduction about the 9 HPO tasks would be better for readers to understand the problem.

Figure 4 could be improved. I suppose Figure 4(a) and 4(c) are for three tasks of various datasets. The meaning of Figure 4(b), as indicated from the paragraph below, the three curves are for three training settings. If this is the case, I am wondering which task/dataset it is from.

### Questions
see above Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a study on early stopping criteria in hyperparameter optimization (HPO), first empirically studying the effects of budget constraints and filtering ratios on the popular Hyperband algorithm to evaluate the reliability of early stopping, and then studying the effects of model uncertainty on early stopping.

### Strengths
The effects of budget constraints and filtering ratios on the popular Hyperband algorithm were studied empirically using two benchmarks of varying scales, LCBench and Nas-Bench-201.

### Weaknesses
1.	More descriptions should be provided for the three fundamental questions to be studied in this paper. To be specific, in the absence of a description of what reliability and model uncertainty are in this paper, the motivation for this paper to evaluate the reliability of early stopping and study the model uncertainty is unclear and confusing. The second question uses words like the nature of early stopping that are not well defined, making it difficult to understand.
2.	Only the Hyperband algorithm, which was published six years ago, was examined in evaluating the utility of early stopping criteria in hyperparameter optimization. More state-of-the-art early stopping criteria should be investigated and analyzed to draw a convincing conclusion.
3.	The word gaps in Insight 2 should be described clearly.
4.	What is the fraction of budget shown in the figures? What is its relation with the filtering ratios?

### Questions
What are the answers to the three fundamental questions given in the Introduction?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor
