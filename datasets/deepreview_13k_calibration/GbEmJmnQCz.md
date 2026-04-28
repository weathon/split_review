# Is Memorization Actually Necessary for Generalization?

- Decision: Reject
- Avg Score: 4.40
- Scores: 5, 5, 6, 3, 3

## Abstract
Memorization is the ability of deep models to associate training data with seemingly random labels. Even though memorization may not align with a model's ability to generalize, recent work by~\citet{feldman2020longtail} has demonstrated that memorization is in fact \textit{necessary} for generalization. However, upon closer inspection, we find that their  methodology has three limitations. First, the definition of memorization is imprecise, leading to contradictory results. Second, their proposed algorithm used for \textit{approximating} the leave-one-out test (the gold standard for calculating memorization scores) suffers from a high approximation error. Three, the authors induce a distribution shift when calculating marginal utility, leading to flawed results. Having accounted for these errors, we re-evaluate the role of memorization on generalization. To do so, we track how memorization changes at different levels of generalization (test accuracy). We control model generalization by training 19 different combinations of models, datasets, and training optimizations. We find that memorization and generalization are \textit{strongly} negatively correlated (Pearson -0.997): As one decreases, the other increases. This shows that memorization is not necessary for generalization, as otherwise, the correlation would have been positive. In light of these findings, future researchers are encouraged to design techniques that can accurately approximate memorization scores.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This manuscript reconsiders and critiques the key claim of Feldman and Zhang (2020), hereafter F&Z.  Three arguments are presented concerning methodological issues with F&Z:

(1) the definition of memorization includes an arbitrary threshold parameter, and it turns out that making changes to the parameter affect the conclusions.
(2) F&Z approximate the memorization score defined in (1) and this approximation has a bias that causes memorization to be overestimated.
(3) F&Z estimate the marginal utility of including an instance in the training set by a technique that overestimates the utility.

The authors conduct additional experiments to support their conclusions.

### Strengths
Due to the interest in F&Z---the article currently has 426 citations---undertaking this sort of investigation seems quite worthwhile, and such careful analyses of others' work is sadly uncommon in our field. 

The paper is generally well written and clear.

### Weaknesses
Some claims and conclusions made by the authors either require additional support or are overly strong.

Some details of the work are unclear. Figure 2 took some work to decypher and unclear what threshold is being used.

My major concerns are as follows, with line numbers from the manuscript:

231: "The experiments based on this definition fail the falsifiability test".  This statement seems a bit strong. If one adopts their specific definition of memorization (i.e., a specific threshold), their theory is testable.  It just isn't terribly compelling.  As you argue, showing that the same result holds for a range of thresholds would strengthen the conclusion, even if it held only for that looser notion of threshold.

243: I don't follow your argument about removing memorized points with high vs. low scores.  The notion of changing the threshold (and removing points with scores above the threshold) does not correspond to these two cases, because the low-score case is removing ONLY points with a low score, not all points with a score above a low threshold. I'd suggest clarifying or removing this argument.

265: "subpopulations are most vulnerable to overestimation": This argument needs to be tightened up. If examples are dropped at random, the fraction of instances lying in a small population will be, statistically speaking, the same as the fraction of instances that lie in a large population. Maybe there's a higher variance argument, but I'm not clear. And maybe there's an argument that performance is a sublinear function of the number of members of a population:  the first one is essential, the second one is important, the third one less so, and so forth. If this argument were true, one would need to consider the absolute numbers of instances of a population that remain in the training set, not the fraction.

274: Since when is 88% a 'high test accuracy' for CIFAR10? What architecture were F&Z using?  At very least, shouldn't you acknowledge that they used a more powerful (and presumably closer to SOA) architecture, and the validity and significance of your results is conditioned on this difference.

282: If I understand, you train 20 models and look at the fraction of models that memorize according to some preset threshold. (I'm not clear on what that threshold is for Figure 2.) Doesn't this mean that your LOO estimate is only accurate to increments of 5% (1/20)? Again, I may be confused, but if you find 1 memorization in 20 and the approximation method produces .08, you'd call that an error of (.08-.05)/.05 = 60%. Even if your LOO method had produced 2 memorizations in 20, it would still have an error of 25%. The poor approximation method just can't win using this assessment. Might it not make more sense to look at the approximation error in absolute score, not relative score?  

321: You claim that F&Z's decision to remove all points above a threshold (which must have been done not by accident but because it was too expensive to remove them one at a time, no?) causes a 'complete or near-complete subpopulation purge'. Is this claim based on your outlier scores (lines 300-306)? Whether your answer is yes or no, I would like to see more direct evidence (e.g., removed data points are classified correctly only if one of those removed data points is included in the training set).

399: "for most thresholds, the drop in accuracy is not statistically significant": What test have you done? Simply looking at overlap of +/- 1SD tells you little about significance. I would run an ANOVA to see if there was a main effect of item type removed (random vs. memorized) and an interaction between item type and memorization threshold. My bet is that you'll see an interaction for both CIFAR-10 and CIFAR-100, which indicates that whether or not  V&Z's claim holds true depends on the threshold. I believe that's a conclusion you wouldn't argue with, although it's not as strong as your "memorization is not necessary for generalization" claim (line 419).

Some minor issues:

68: "but due to common ML oversight". Don't you mean due to loss of the subpopulation?  The sentence refers to ML oversight twice.

72: "we disprove the conclusion of the original work..."  Seems fairer to say "we obtain an alternative or weaker conclusion of the original work..."

Figure 1: caption is ungrammatical

Jiang et al. (2021) emphasize the point the authors make about the role of subpopulations of various sizes and might well be cited.  See 
https://proceedings.mlr.press/v139/jiang21k.html

244: "Fix" is a weird paragraph heading. Perhaps "Our solution" or "Our fix"?

251: should be "leave one out (LOO)" the first time you use acronym.

### Questions
Please address the comments I made in the 'weaknesses' section. I am open to raising my score, and I would like to see this work published in some form, but the arguments need to be tighter (or clearer, if it's my misunderstanding). In general, work of this sort requires converging evidence -- multiple experiments/analyses that drive home the same point. Any one bit of evidence may be weak (as I think some of your arguments are), but taken together they become compelling.

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper reexamines the theoretical work of [Feldman, 2020] and [Feldman & Zhang, 2020]. They highlight three issues with the two papers: (i) arbitrary choice of memorization threshold makes certain claim from memorization not fallible at all; (ii) Approximation algorithm for memorization scores has high upward bias; (iii) unintended effect when removing data points.

Sec4, they provide concrete experimental results for the three results cited above.
Sec5, they redo the experiments based on the updated understanding and find the contribution of memorized points to test accuracy is exaggerated in the original paper.

### Strengths
* The experiments are technically solid, with setting and hyperparameters clearly stated.
* Lastly, the practice of revisiting an established paper and pointing technical inadequacy is good for the community.

### Weaknesses
 * It's unclear what's the original contribution to the field the paper has. While pointing out the inadequacy in earlier work, the paper itself doesn't make the case for the role of memorization plays in generalization. It refutes the specific claims made by a particular set of papers, but didn't directly provide evidence if the "necessary condition" holds or not.
* The discussion of related work heavily focuses on the privacy-adjacent domain. There are other showing similar conclusion that does not have the problem mentioned by the author, e.g. [https://proceedings.mlr.press/v178/cheng22a/cheng22a.pdf] shows memorization is necessary for generalization without alluding to most of the concepts in Feldman et al. Similar, [https://proceedings.neurips.cc/paper_files/paper/2023/hash/bf0857cb9a41c73639f028a80301cdf0-Abstract-Conference.html] shows that explicitly enforcing memorization boosts the test time performance in actual experiments.

### Questions
The authors make a good lower-level technical discussion around Feldman et al., but how do those claims shed light into the memorization-generalization dilemma itself? This scientific question is independent of a particular set of papers that claim one way or another. Maybe the authors can discuss how their effort help clarify the underlying scientific question, not just pointing out lower-level technical flaws of earlier papers. I think this is potentially the true contribution of the experiments in the paper could shine.

### Soundness
4

### Presentation
4

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
In this paper the authors examine and challenge the claim presented in Feldman & Zhang (2020) that memorization is necessary for generalization. They conclude that this claim is based on flaws w.r.t. the problem definition of memorization, the practice of estimating its intensity, and the analysis on its marginal utility. The authors further correct the correctable flaws and observe opposite results, concluding that memorization is not required for generalization.

### Strengths
This paper presents a well-supported opinion on the significant issue of memorization vs generalization. It's a solid rebuttal of a previous work. It is self-contained and very well-written.

### Weaknesses
As the authors point out in the paper, both their work and the previous one are basing their studies on the ambiguous and misquantified definition of memorization. Therefore both work suffer from the potential over-simplification and over-generalization of a complicated topic.

### Questions
1. Feldman & Zhang (2020) looks at memorization from the perspective of long tail study. One (my) way of interpreting their work is that memorizing the under-represented training points in a tail sub-population is necessary for the generalization within that sub-population at test time. The empirical study in this work does not disprove such interpretation. It would be interesting to know if the authors are opposing or confirming this particular point conceptually.

2. An alternative, and presumably more quantifiable definition of memorization could help further strengthen the claims in the paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper revisits Feldman and Zhang's (2020) hypothesis that “memorization is necessary for generalization” by re-evaluating key elements in their approach. The authors point out several critical issues in the prior work's definitions of memorization score, the approximation algorithm, and the calculation of marginal utility. By addressing these limitations and introducing a modified experimental setup, this paper shows that memorization does not significantly contribute to generalization. Specifically, it highlights that Feldman and Zhang’s study overlooked the effects of sub-population shifts, which led to misleading conclusions.

### Strengths
- Perspective: The paper brings a valuable critical perspective to existing research, systematically reassessing established assumptions through a new experimental design. Its focus on sub-population shifts and errors in approximation algorithms is not only novel but also practically relevant.

- Empirical Contribution: The authors contribute by carefully analyzing the limitations in Feldman and Zhang’s original methods, particularly through data cleansing and detailed examination of approximation errors. The study effectively uses LOO (Leave-One-Out) experiments to reveal the conditions under which the original approximation algorithm yields incorrect results. While this approach is beneficial, more comprehensive experimental details would further strengthen this contribution.

### Weaknesses
 - Concerns About Reproducibility: Although the paper provides valuable insights into the impact of sub-population shifts, it lacks detailed descriptions of the experimental setup, raising concerns about reproducibility. For instance, details on data set segmentation and specific threshold settings in Figure 2 and Table 1 are insufficiently clear, potentially making it difficult for other researchers to replicate the findings. Specifically, the criteria for selecting the 'influential 500 points' for the Leave-One-Out (LOO) experiments are not well-defined, and it's unclear how these points relate to the overall dataset. The absence of a clear methodology for determining these influential points makes it challenging to validate the results. Furthermore, the paper does not specify the exact method used for calculating influence scores, which is crucial for replicating the selection of these points. 

Presentation: Clearer explanations regarding the differences in the experimental setup in Section 4.2 and prior methods would improve comprehensibility. Demonstrating these differences through specific formulas would also clarify how definitions vary and the extent of the error introduced by each. The current description lacks the necessary mathematical rigor to fully understand the modifications made to the original experimental design. The paper should provide a side-by-side comparison of the equations used in the original work and the modified equations used in this study, highlighting the exact differences and their implications.

### Questions
- Regarding L278: "Since running LOO on the entire dataset is not possible, we only execute it on a set of the influential 500 points." Does this mean that the CIFAR-10 data was limited to 500 points?

- Settings in Figure 2 and Table 1: The description of how the training and test sets are divided in these experiments is unclear. To ensure reproducibility, could you clarify the specific methods of data division and the criteria for selecting data points?

- Accuracy Decline with Lower Memorization Thresholds: In Figure 3 and Table 1, accuracy declines as the memorization value threshold decreases. Could you provide further analysis on this point? Rather than dismissing prior findings outright, highlighting which conditions are significant and why this study clarifies them would enhance the reliability of the conclusions.

#### Additional Comments

- It would be helpful to provide an explanation of "SPP" in L300 for clarity.

- Finally, by sharing the data used for memorization and generalization analyses, this study could further support the research community by enhancing reproducibility and offering a reliable dataset for future work.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper challenges Feldman & Zhang (2020)’s conclusion that memorization is necessary for generalization. The authors argue that there are three issues in Feldman & Zhang (2020)’s experiment design and propose a way to address these issues. They conducted experiments with their proposed changes on CIFAR-10/100 and present empirical results that contradict Feldman & Zhang (2020)’s claim.

### Strengths
The paper raises interesting points that challenge Feldman & Zhang (2020)’s conclusion. The explanations aid intuition, and the authors have also attempted to collect empirical evidence to support their claims. While I believe that rethinking and critically evaluating existing work is essential in the field and should be encouraged, I have a few concerns listed in the following section.

### Weaknesses
1. Lines 307-308 state, “It is clear that these small sub-populations are not memorized and therefore, should not be included in the set of memorized points.” This assertion seems overly confident. Is there rigorous evaluation on the exact number of small sub-population points that are or are not memorized? Are we entirely certain that none are memorized, and what direct evidence supports this? Could it be possible that some are memorized while others are not? Currently, this part lacks rigor. Specifically, the authors should provide a more detailed analysis of the memorization scores within these sub-populations, perhaps showing a distribution of scores rather than making a blanket statement. A more nuanced approach is needed to justify the claim that these points are not memorized, potentially involving a statistical analysis of memorization scores within these groups.

2. The approach for identifying sub-populations also lacks rigor. The concept of a sub-population has no formal definition here, and the exact algorithm is unclear. For example, the phrase “check if multiple memorized points impact the same test set point; if so, they belong to the same sub-population” leaves questions—e.g., what quantitative measure of “impact the same test set point” is used? Additionally, in the second step (visual check), what criteria guide the decision that images belong to the same sub-population, and how do you justify the criteria you used? The granularity of the subgroups may also matter here. It is possible that, although A and B both impact the same test point based on the authors' criterion, their impacts are very different in magnitude—one is relatively large, while the other is small. In this case, removing A alone could significantly affect accuracy, whereas removing B might not. Grouping A and B together and removing both from the memorized set could therefore be problematic. Including a comprehensive list of identified groups in the appendix could be helpful, but more fundamentally, the definition of sub-populations here is highly subjective and does not seem scientific. Using some synthetic data with clear definition of groups or existing datasets with sufficiently fine-grained group annotatations might strengthen the robustness of this analysis. The lack of a clear, quantitative definition for a sub-population makes the analysis difficult to reproduce and interpret. The authors need to provide a precise algorithm for sub-population identification, including the specific metric used to measure the impact on test points and the criteria for visual grouping.

3. You mention that “small” sub-populations should not be identified as memorized. How do you quantify “small”? Specifically, after selecting the sub-populations in your experiments, how do you determine if they are small or large? And on what rationale is the threshold separating small and large based? The authors need to define a clear, quantitative metric for determining the size of a sub-population and provide a justification for the threshold used to classify sub-populations as small or large. This threshold should not be arbitrary but should be based on some statistical or theoretical justification.

4. To support the claim that all small sub-populations are not memorized, it would be beneficial to provide the exact actual memorization scores for all points in the identified sub-populations. This would help confirm that none of them are indeed memorized. Additionally, you should also confirm that their memorization scores are overestimated by the approximation algorithm. Without this, the claim that these points are not memorized remains unsubstantiated. The authors should provide a detailed analysis of the memorization scores for points within these sub-populations, comparing them to the scores of points outside these groups and also to the approximation algorithm's output.

5. For a fair comparison, you could also apply the original method from Feldman & Zhang (2020) to your modified CIFAR-10/100 and demonstrate that their method produces a significant gap between the green and yellow curves. This would support your claim that their method falsely concludes that memorization is necessary. This direct comparison is crucial to demonstrate that the observed differences are due to the proposed modifications and not other factors. The authors should show that the original method, when applied to their modified datasets, produces the same misleading results as reported in the original paper, thus strengthening their critique.

6. How do you ensure that your modified CIFAR-10/100 datasets still follow a long-tailed distribution? Feldman & Zhang (2020) only makes their conclusion within the scope of long-tailed distribution datasets. I’ll expand on this in the next point. The authors should provide a quantitative analysis of the class distribution in their modified datasets to demonstrate that they still exhibit a long-tailed distribution. This analysis should include metrics such as the number of samples per class and the Gini coefficient to confirm the long-tailed nature of the data.

7. Another important point concerns the fundamental conceptual understanding in this paper. Note that the conclusion from Feldman & Zhang (2020) is specifically in the context of long-tailed distributions, where there is a significant fraction of rare and atypical examples. They did not claim that memorization alone, isolated from other factors, is necessary for generalization; instead, they specifically associate their statement with long-tailed distributions. However, in this paper, the frequently used example, the hypothetical cat dataset, does not represent a long-tailed distribution, and using it may be misleading since it is not the scenario Feldman & Zhang (2020) address. A more appropriate example would be, for example, a setup with cats of 100 different colors, where three of the colors have 20 cats each, and the remaining 97 colors have only one or two cats each. In such a setting, it is clear that removing cats from those 97 colors would significantly impact generalization. Not memorizing those data points could be viewed as introducing an incurred or effective distribution shift, which does not contradict Feldman & Zhang (2020)’s conclusion. They did not suggest that the underlying distribution shifts do not contribute to accuracy drop; in fact, this is precisely the point in the context of long-tailed distributions. The authors need to clarify how their analysis aligns with the specific context of long-tailed distributions, as the original work's conclusions are tightly coupled with this data characteristic. The example used should accurately reflect the long-tailed nature of the datasets being analyzed.

### Questions
See the questions raised in the Weaknesses section.

### Soundness
1

### Presentation
2

### Contribution
2
