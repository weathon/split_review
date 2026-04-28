# On the Inadequacy of Similarity-based Privacy Metrics: Reconstruction Attacks against ``Truly Anonymous Synthetic Data''

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 8, 6, 3, 5

## Abstract
Training generative models to produce synthetic data is meant to provide a privacy-friendly approach to data release.
However, we get robust guarantees only when models are trained to satisfy Differential Privacy (DP).
Alas, this is not the standard in industry as many companies use ad-hoc strategies to empirically evaluate privacy based on the statistical {\em similarity} between synthetic and real data.

In this paper, we review the privacy metrics offered by leading companies in this space and shed light on a few critical flaws in reasoning about privacy entirely via empirical evaluations.
We analyze the undesirable properties of the metrics and filters they use and demonstrate their unreliability and inconsistency through counter-examples.
We then present a reconstruction attack, \emph{ReconSyn}, which successfully recovers (i.e., leaks all the attributes of) at least 78\% of the low-density train records (or outliers) with only black-box access to a single fitted generative model and the privacy metrics.
Finally, we show that applying DP or using generators with low utility does not successfully mitigate \emph{ReconSyn} as the privacy leakage still comes from access to the metrics.
Overall, our work serves as a warning to practitioners not to deviate from established privacy-preserving mechanisms.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper challenges the effectiveness of similarity-based privacy metrics currently used by start-ups to validate the privacy guarantees of synthetic data. The authors provide a thorough review of these metrics and provide counter-examples where a metric would declare synthetic data to be safe even though it isn’t. The authors then propose a threat model for attacking synthetic data as typically provided by a start-up, where the adversary has unlimited query access to the generative model and the ability to recompute the privacy metrics over arbitrary datasets. They develop a reconstruction attack and demonstrate on several datasets that the attack succeeds in reconstructing a large fraction of outliers in the datasets. Finally, they show that even when the generative model is DP, reconstruction still succeeds better than expected due to leakage in the privacy metrics.

### Strengths
- 1) The question being studied is timely and of great practical importance. There are many start-ups in the synthetic data space making broad claims about the privacy of synthetic data and there is not enough scientific scrutiny of these claims. 
- 2) Solid review of the privacy metrics used to validate the privacy of synthetic data.
- 3) Provides counter-examples for all of the metrics where the metric would declare the synthetic data to be safe even though it isn’t.
- 4) Proposes and evaluates the first record-level reconstruction attack against synthetic data.
- 5) The attack results are very strong as a large fraction of outliers can be correctly reconstructed.

### Weaknesses
 - 1) The attack results are contingent on the definition of outliers. Both the targets of the attack (outliers) and the test records (over which the attack success rate is computed) are constructed using similar clustering methods. This may lead to over-optimistic results. The use of clustering to define outliers is a potential weakness, as the attack may be exploiting the specific characteristics of the clustering algorithm rather than inherent vulnerabilities of the synthetic data generation process. The authors should consider using a more robust, model-agnostic definition of outliers, perhaps based on density estimation or distance-based methods, to ensure the attack's generalizability. Have the authors considered (1) evaluating their attack on a dataset that has not been pre-processed by them to add outliers or (2) identifying outliers (to be used as the test records) with a state-of-the-art approach such as https://arxiv.org/abs/2306.10308?
- 2) It’s unclear which of the similarity-based metrics is used in the empirical evaluation. The paper mentions several metrics (IMS, DCR, NNDR), but it is not specified which one is used in the attack. This lack of clarity makes it difficult to interpret the results and understand the effectiveness of the attack in relation to specific metrics. The authors should explicitly state which metric is used or, if multiple metrics are used, how they are combined or compared.
- 3) Missing method description in the main paper and insufficient method description in the Appendix. In the main paper, the authors should clearly explain the difference between SampleAttack and SearchAttack (without which interpreting the results is very difficult). In the Appendix, to ensure reproducibility, the authors should precisely describe steps 18-32 of Alg. 1. The current textual descriptions are too informal/imprecise. The description of the attack is particularly vague regarding the iterative refinement process. It is unclear how the candidate records are modified and filtered at each step. The authors should provide a detailed, step-by-step description of the algorithm, including the specific operations performed on the candidate records, the criteria for selecting the most likely records, and the stopping condition for the iterative process.

### Questions
- 1) Is it possible, using the authors' method, to assign a confidence or likelihood to each reconstructed record?
- 2) Why do the authors focus on outliers only? Intuitively, an average record is more likely to be generated by the synthetic data model than an outlier record. The other leading reconstruction method based on repeated dataset generation, developed by Dick et al. against aggregate statistics, doesn’t explicitly target outliers. 
- 3) What do the authors mean by “all three tests pass” (relating to the metrics)?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the use of similarity-based metrics as a privacy tool.
Recently, certain companies have developed heuristics to determine when a synthetic dataset is private.
These heuristics have no theoretical backing and are, ironically, a huge privacy leak as they contain deterministic information about the inclusion or exclusion of training samples.
The paper points out a number of issues with these approaches as well as various ways to fool the metrics/inconsistencies in them.
They then develop two variants of an attack that can reconstruct the training data with access to these privacy metrics.
They show that outliers can be reconstructed with high accuracy, and thus, these metrics do not ensure data releases that satisfy GDPR.

### Strengths
- It is very important to show that these attempts at privacy-preserving synthetic data do not work (even if obvious to experts) as there are companies using these approaches. I particularly like how it shows an explicit GDPR violation, which will make companies take this more seriously.
- The list of issues is well-written and contains many good points.

### Weaknesses
## Paper Structure/ Understanding ReconSyn
Without reading the appendix, I had little to no idea about how the attack works. Then I read the appendix, and I found it still to be rather unclear (although I get the general idea).
1) The attack needs to be described in the main paper. One suggestion to make room for this could be to cut the incredibly verbose evaluation section down to summarize the key points over all datasets with a few interesting anomalies. As the paper is currently written, we read the evaluation with little idea of what is being evaluated.
2) The algorithm needs to be described more formally as to the exact set operation that takes place during filtering and the exact branching conditions based on the metrics.

## How practical is the attack?
While I was convinced that the similarity metrics are a bad idea without the attack, I think the attack is not as practical as it is portrayed.
1) Assuming the adversary can query any dataset with the metric seems far-fetched. Although the paper argues this is the case in practice, it would be easy for companies to restrict this.
2) In Section 5, it seemed the attack was adaptive (The search attack is deployed based on the performance of the Sample attack). However it was not clear how the attack could know the reconstruction rate of the previous component without access to the training data.
3) It would be helpful to list the number of queries to the metric oracles/the effect that a rate-limiting defence would have on attack success.
4) While the attack is useful for a proof of concept, it doesn't have any merit in the case that the privacy metrics are not leaked. Thus, the argument that it outperforms related work in terms of its lack of assumptions is a little misleading.

## DP argument
The section about the effect of DP is somewhat a moot point as it can not be DP while allowing unperturbed queries about the training dataset (the metrics). I somewhat get the idea to show that even if they decided to use DP on the generator, it still wouldn't be enough with the metrics being present. Perhaps more interesting would be to show what happens if the metrics are released with DP (an actual defence). Although epsilon already gives an indicator of how private the synthetic data is, the best defence would be removing the metrics entirely.

## Minor comments
- Consider using parenthesis around citations, as some sentences are hard to parse when filled with citations that are not distinguished from normal text.
- 2D gauss was missing from Table 1 despite section 5.1.1 referring to it.
- No mention of how the ground truth outliers are computed in the evaluation.
- Figure 5 is very hard to read. The shading is subtle and changes the colour to make it even more confusing. Perhaps shapes for eachepsilon and make them shaded or hollow for the two attacks?
- $1/n$ is too large for a delta parameter. It technically allows a trivial mechanism that publishes a single record of the database. The general rule of thumb is that $\delta << 1/n$ [Dwork & Roth](https://www.nowpublishers.com/article/Details/TCS-042)

### Questions
I think most of my concerns could be addressed by clarifying the attack and its purpose as a proof of concept (not a general reconstruction attack).

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores problems with privacy metrics used to evaluate synthetic data (generated without differential privacy). The paper demonstrates the undesirable properties of these metrics and shows the viability of a reconstruction attack. The paper suggests a need to move away from ad hoc approaches to privacy . Extensive experiments are conducted demonstrating the viability of the attack on real synthetic data under a reasonable threat model.

### Strengths
The paper is well motivated, the false promise of synthetic data generation (without DP) is a very important message. The overview of existing metrics for evaluating synthetic data alongside their weaknesses is a very clearly presented and a valuable contribution in its own right.

 The experiments are thorough and extensive detailed is given in the appendix. 

Overall the conclusion of the paper that effective attacks on synthetic data exist seems well supported by the experimental results, assuming the presentation can be improved.

### Weaknesses
A thorough description of the attack is lacking in section 4 which significantly weakens the comprehensiveness of the paper in my view. I understand why the full Algorithm was relegated to the appendix but a paragraph explain the logic of the attack and where the information is being extracted would significantly improve the paper. Given the vulnerability of models trained with DP to this attack, the information is presumably coming from the metrics but an intuitive explanation of how that occurs is missing.

Figure 2 should be presented in a way where it is possible to distinguish between the different training algorithms and datasets. I would suggest enlarging the figure despite the constrain on space since it is a key result for the paper. I find it more useful that FIgure 4, which is given much more space.

I do not entirely understand what the takeaway is from Figure 3. The figure is referred to only in passing and never explained. More generally 
the description of the results would benefit from more thorough explanation.

As far as I can tell, 'outliers' is never clearly defined but it is the denominator for all success rates reported and so it is important to explain what this set of data points is and how much of the training data they make up.

Stating that the attack works on models trained with DP in the abstract/intro is true in a literal sense but I feel somewhat disingenous since as noted later in the paper, the information is come from the statistics released without DP. Any model regarded as formally satisfying DP would never be able to look directly at the private data in this way.

Overall, I believe the paper has a strong attack but these results could be better presented to really hammer the point to ensure the key message of this paper reaches the synthetic data community. Ideally there could be a figure that made it impossible to ignore the weaknesses of the synthetic data generation but the current figures are overly information loaded causing the key takeaway to be lost.

### Questions
Can you report the privacy metrics with DP or would your recommendation be to not report distance metrics? 

How do you define an outlier? As far as I can tell, 'outliers' is never clearly defined but it is the denominator for all success rates reported and so it is important to explain what this set of data points is and how much of the training data they make up.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The use of synthetic datasets generated from real datasets is common in industrial applications. One of its main applications is to comply with privacy regulations when real datasets are sensitive and cannot be used directly. To assess their privacy before its release, a synthetic dataset is evaluated it by the use of privacy metrics. The main metrics that are used in practice are Identical Match Share (IMS), Distance to Closest Records (DCR) and Nearest Neighbor Distance Ratio (NNDR). However, they evaluate privacy via heuristics that do not provide strong guarantees.  

The contribution show that IMS, DCR and NNDR are not good metrics for privacy. They do so by (i) exposing major flaws in the design with respect to standard privacy and security guidelines  (ii) illustrating contradictions in the privacy assessment of the metrics by the use of counter examples and (iii) providing a data reconstruction attack that is able to recover a substantial amount of dataset outliers by having black-box access to the synthetic data generators and the output of the privacy metrics.

### Strengths
The paper clearly presents and treats an important problem in the study of privacy preserving applications. It is key to understand the privacy threats posed by the extensive use of synthetic data. 

Section 3 and Appendix E show fundamental flaws in the use of IMS, DCR and NNDR as meaningful metrics. Section 3 outlines key aspects of the design of privacy preserving mechanisms which are not present these metrics. Appendix E provides counter examples that illustrate how substantial sensitive data can be revealed even if privacy metrics give a good score to the released data.

### Weaknesses
As said, early sections of the paper successfully identify important design flaws in the assessment of the privacy provided by synthetic data. However, the arguments provided by the main contribution, which is the ReconSyn the attack, are not sufficiently solid. 

The main objective of the paper is to show that IMS, DCR and NNDR are inadequate as privacy metrics. This essentially means that these metrics fail to assess how much sensitive information is leaked by sharing a synthetic dataset. To do that, the contribution presents an attack that attempts to recover the original data points from the synthetic data generator. However, the attack proposed by the protocol (ReconSyn) seems to have a major flaw: it success does not rely on the sensitive information released by synthetic data, which is only used marginally. The attack heavily relies on the ability to query privacy metrics an arbitrary amount of times. These queries provide a *huge* amount of information: the distance to real data points (given by DCR and NNDR) and the amount of synthetic data points that match the real ones (given by IMS). It is not surprising that one could successfully reconstruct outlier data points with arbitrary access to that information. 

The above is confirmed from the results of Section 5.2 which show that the attack performs well regardless of the quality of the synthetic data and even when data is generated with strong DP guarantees (see Section 5.2.3). 

My impression over the main take-away of the paper is that revealing the privacy metrics is dangerous. Therefore, the impact of the contribution seems low: it does not provide a compelling argument against the release of synthetic data itself when its IMS, DCR and NNDR scores are not revealed (even if the synthetic data has been evaluated with these metrics). 

In addition, I do not think that the evaluation of the attack against differentially private techniques of generation is well addressed. In the current setting, the attacker has the possibility to access information that is not differentially private (i.e the privacy metrics) and has unlimited queries to the privacy mechanism. It is well known that epsilon and delta DP parameters degrade after each query to the mechanism.

### Questions
Please elaborate on the weaknesses outlined above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this work authors empirically demonstrate the insufficiency of the existing privacy metrics when applied to synthetically generated data. In addition, authors also propose a novel data reconstruction attack to highlight the vulnerabilities in generative models.

### Strengths
The problem authors address is very important and their work is rather timely. 

One particular thing I really like in this work is that this is yet another case, where academia identifies a critical issue, where industry does not, except that this time, it is an issue that directly affects industry and cannot be easily ignored, making this work’s conclusions incredibly relevant to the community.

The experimental setting makes sense to me and I agree that the threat model can represent a valid real-world deployment.

### Weaknesses
I do have some concerns, however.

While the numerical results that authors demonstrate are very impressive, their choice of datasets is rather limited: in many cases, this is just a limitation/future work area, however, in this work, i argue this is a major flaw. These datasets were commonly known as the relatively ‘trivial’ ML tasks, mainly because of how simple they are. Therefore, reconstructing this data (as shown in works such as [1,2,3,4]) is A) relatively straightforward even with simple inversion attacks and B) is very often due to a very limited reconstruction space that the adversary is present with (i.e. there are many ways to define a valid number in MNIST, for instance). So while these results demonstrate that the metrics are indeed poorly performing on these specific datasets, I am not convinced this is the case for more complex settings, where the reconstruction space is much larger (e.g. even in CIFAR10). Therefore, I would like to see similar results being presented on non-trivial tasks to show that the proposed flaws do affect more realistic settings too. 

One fundamental concern of mine related to this is that this attack may require human supervision: from section 5, it reads that even for cases as simple as MNIST, the adversary needs to ‘strategically’ perform some sort of reconstruction guidance (e.g. excluding certain pixels). I would argue that this, in part, violates your threat model and really harms the applicability of your method to real-world imaging tasks. Because in order to know which pixels need removal, the attacker needs to have some sort of prior on the images: sure it is trivial with handwritten digits what pixels to remove, but what about skin pathology imaging? The images are much more identifiable if one knows attributes associated with individuals in the dataset, but also require much more expertise to know how to interpret them and what to keep/remove. 

Additionally, while the authors claim that the models they attack are SotA, I am not fully certain that this is indeed the case. It was previously shown that models such as DPGAN, for instance, are not particularly great at generating meaningful datasets when there are outliers which need to be represented (which is, again, poorly captured in datasets such as MNIST).

Some of the issues with the SBPM metrics are valid, but rather inflated. In particular, I agree that issue 4 correctly identifies the issues when adversarial samples are present - but this is also an assumption applicable to almost all ML settings too? Same for issue 5: while I agree that it is often easy to misinterpret what SPBM mean numerically, the same can be said about DP (which given issue 1 is ‘supposed to be’ an alternative to SPBMs as it gives you objective guarantees), which has a privacy parameter often poorly interpreted and contextualised. So yes, this is an issue, but it is not specific to SPBMs and I would go as far as arguing that it is not fully fair to associate these issues with every single SPBM method: in my view, IMS is extremely easy to interpret, and this is precisely why its problematic (i.e. its interpretation is easy, but the score itself is unrepresentative, causing its misuse).  

My concrete suggestion here would be to tone down some of the issues (and maybe consider if all of them are really relevant to these specific methods you present) and then use the space that you gained to include more information on how the attack works in the main body. I understand that the algorithm itself is in the appendix, but there is nothing in the main body at all that helps the reader understand how this attack actually functions. All we have is a threat model and assumptions. The reason I find this important is because you are able to leverage these privacy violations primarily because you were able to present a novel data reconstruction attack, which is the core contribution of this work, but you are really not presenting this main contribution at all (except for the appendix).

### Questions
Could you also, perhaps, clarify how exactly was DP training performed? From my understanding, construction of privacy filters requires you to derive information from the private data: hence it is unclear to me how this was handled and accounted for in terms of the privacy budget? This might be related to the leakage comes from the privacy metrics; as they require access to the train data and are deterministic: does this mean that your empirical evaluation is done in this manner and hence uses unaccounted private information? If so, you are leaking information, thereby completely invalidating your DP. Could you clarify this in detail, as DP is a large section of your work and your conclusions strongly suggest that DP cannot mitigate your attack. Also: it seemed to me that all of your algorithms except for CT-GAN used DP already, why a separate section?

Additionally: I would like you to present the SearchAttack in more detail: it is unclear what ‘history of records from the first pass’ is. 

Overall, I am really on the fence about this work. The conclusions and empirical examples can be incredibly useful for the ML community as a whole, but the results themselves are not particularly representative and the DP section is very unclear (and can potentially be very misleading). I would like the authors to address the issues I outlined above, in which case I will be willing to increase my score.

[1] - Geiping, Jonas, et al. "Inverting gradients-how easy is it to break privacy in federated learning?." Advances in Neural Information Processing Systems 33 (2020): 16937-16947.
[2] - Zhu, Ligeng, Zhijian Liu, and Song Han. "Deep leakage from gradients." Advances in neural information processing systems 32 (2019).
[3] - Usynin, Dmitrii, et al. "Zen and the art of model adaptation: Low-utility-cost attack mitigations in collaborative machine learning." Proc. Priv. Enhancing Technol. 2022.1 (2022): 274-290.
[4] - Zhang, Yuheng, et al. "The secret revealer: Generative model-inversion attacks against deep neural networks." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2020.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair
