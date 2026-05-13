# Fairness Through Matching for better group fairness

- Decision: Reject
- Scores: 6, 5, 6

## Abstract
Group unfairness, which refers to socially unacceptable bias favoring certain groups (e.g., white, male), is frequently observed ethical concern in AI.
Various algorithms have been developed to mitigate such group unfairness in trained models.
However, a significant limitation of existing algorithms for group fairness is that trained group-fair models can discriminate against specific subsets or not be fair for individuals in the same sensitive group.
The primary goal of this research is to develop a method to find a good group-fair model in the sense that it discriminates less against subsets and treats individuals in the same sensitive group more fairly.
For this purpose, we introduce a new measure of group fairness called Matched Demographic Parity (MDP). 
An interesting feature of MDP is that it corresponds a matching function (a function matching two individuals from two different sensitive groups) to each group-fair model. 
Then, we propose a learning algorithm to seek a group-fair model whose corresponding matching function matches similar individuals well.
Theoretical justifications are fully provided, and experiments are conducted to illustrate the superiority of the proposed algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors raise a concern that existing group fairness notions do not protect against unwarranted within-group performance disparities. The authors propose a new Matched Demographic Parity (MDP) fairness measure and accompanying learning approach — Fairness Through Matching — which is designed to improve within group fairness. The authors justify their approach theoretically and via experiments on several benchmark datasets.

### Strengths
This work provides a novel Matched Demographic Parity fairness measure and establishes connections with existing measures such as strong demographic parity. Matching for improved group fairness is an interesting and under explored area, and the authors develop a technically sound framework that demonstrates promising empirical performance. I also appreciated the ablation of different matching approaches in the experiments section.

### Weaknesses
Weaknesses (ordered by importance):
- Given the focus of this work, I would expect a more granular comparison against existing multi-calibration fairness notions and leaning algorithms. The stated goal of this work — to “find group-fair model that discriminates less between subsets or individuals in the same sensitive group” — bears strong resemblance to muliccalibration, which provides a guarantee that holds across many overlapping subsets of a protected group. Indeed, the authors’ definition of “subset fairness” is very similar to the formal definition of multi-calibration (the specified definition seems to specify a maximum violation over subsets rather than specifying a constraint that holds over all intersectional subgroups). A direct comparison against multi-calibrated predictors (theoretically and in experiments) is needed. If this is not the case, I encourage the authors to clearly differentiate early on in the work, as other readers are likely to have similar questions. Specifically, the work should be compared against approaches that provide fairness guarantees over a collection of subgroups, such as those described in Kearns et al. (2018). While the authors draw connections to this work in the appendix, they state that their problem is different because they do not know the collection of subsets in advance. However, it is not clear that this is a key differentiating factor, and a direct comparison in the experiments is needed to justify this claim.

- I also have concerns regarding the scalability and robustness of the proposed approach in real-world settings of interest. It seems that a matching style approach would be challenging when subgroups are highly imbalanced, and that performing matching across multiple intersectional subgroups would also be challenging. 

- There is an opportunity to strengthen the motivation of the work. I appreciate the authors’ approach of providing a toy example to highlight issues with group-fair models. However, Fig 1, speaks to similar known issues with intersectionality in fairness. It would be helpful to illustrate the intuition as to why matching is a useful approach for addressing this problem. 

- Benchmarking fairness approaches via the COMPAS dataset has several known limitations. I don’t have an issue with using this dataset in this work given the technical focus of the paper, but do think that an explicit disclaimer acknowledging these issues is warranted in the experiments section.

### Questions
Please see points raised in the weaknesses section above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce an algorithm to find models which satisfy both group fairness and within-group fairness called FTM or fairness through matching. This algorithm uses a new group fairness measure called MDP or matched demographic parity. They provide theoretical justification as well as some empirical results.

### Strengths
The authors provide good theoretical justification for their algorithm.
The authors provide some empirical results that show better performance to other similar methods - with fewer outliers when looking at subset fairness (or group fairness).

### Weaknesses
 The language in the paper is hard to follow. Both grammatically as well as inconsistencies in terms used throughout the paper. The authors should be sure to update grammar throughout the paper (for example "a group fair model that less discriminates subsets or individuals in the same sensitive group" -> a group fairness model that discriminates less between subsets or individuals in the same sensitive group), as well as making sure their terminology throughout the paper is consistent (example: group fairness, subset fairness).

Unless I missed it in the proofs of the appendix, it is not made clear why MDP is necessary, and why total variation, strong demographic parity, or 1-Wasserstein distances should not be used. The authors provide the similarity between the measures but do not clearly state why MDP is important.

The authors make the claim that one of their contributions is the new group fairness measure MDP, but state in section 3.4 that Black et al. (2020) employs the MDP constraint. Could the authors please clarify if and how their MDP definition is different from the earlier paper.

The plots in the paper are not at all readable with very small text.

This paper seems incremental in nature, being very close to FRL, Gorsaliza et al, and pulls together techniques from other areas.

Minor nits:
It would be good to include the accuracy table in the main paper.

### Questions
Please see the questions associated with "Weaknesses" above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a refined group fairness regularization through matchings. Specifically, they introduce matched demographic parity, which treats individuals in the same demographic group more fairly.

### Strengths
The authors present a novel method, which is interesting and performs well. In addition, they propose a sound and detailed theoretical analysis of the methods.

### Weaknesses
Two main limitations of the proposed work and presentation stand out:
- Regarding the motivation. Subgroup discrimination is indeed a problem of Group-Fairness approaches. However, since you do not require any specific structure of the matching, it seems that you also enforce non-discrimination against features for which we want to discriminate. Take for example $X=[gender, race, skill]$ is a job application. If I apply matched group fairness on gender, then I agree that this should not lead to discrimination against e.g. african american woman. However, I am very happy with discriminating agains unskilled workers. Could you please explain how your approach would work in this case?
- While motivated from the side of group fairness, your approach has many relations to individual fairness. Specifically, (Step 1) identifies "similar" individuals while (Step 2) requires the "similar individuals" to be treated similarly by the classifier. I see that the "similar individuals" in step 2 are synthetic, but I still believe that the relation to individual fairness ought to be discussed.

### Questions
Some questions and comments in the order they appear in the paper:
- In the first paragraph of section 3.2, you use $\|\cdot\|^2$ to find the OT map. Which distance do you choose, and how is the performance influenced by (a) the distance and (b) the preprocessing? (no need to run experiments, I would just like to understand it better)
- Figure 4 is quite small. If you find some space increasing the size would be nice

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
