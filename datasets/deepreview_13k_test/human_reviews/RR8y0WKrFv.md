# Ensemble Distillation for Unsupervised Constituency Parsing

- Decision: Accept
- Scores: 8, 3, 8, 8, 6

## Abstract
We investigate the unsupervised constituency parsing task, which organizes words and phrases of a sentence into a hierarchical structure without using linguistically annotated data. We observe that existing unsupervised parsers capture different aspects of parsing structures, which can be leveraged to enhance unsupervised parsing performance.
To this end, we propose a notion of ``tree averaging,'' based on which we further propose a novel ensemble method for unsupervised parsing.
To improve inference efficiency, we further distill the ensemble knowledge into a student model; such an ensemble-then-distill process is an effective approach to mitigate the over-smoothing problem existing in common multi-teacher distilling methods.
Experiments show that our method surpasses all previous approaches, consistently demonstrating its effectiveness and robustness across various runs, with different ensemble components, and under domain-shift conditions

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a method for combining the outputs from unsupervised parsers in the manner similar to MBR decoding, but different in considering all possible trees. The proposed method simply assigns score to every span, a hit count that is the number of constituency appearing in outputs from multiple unsupervised parser. Then, it runs CKY to derive the maximum scored tree using the hit count score. Experiments on PTB and SUSANNE presents gains over SOTA baselines.

### Strengths
- The proposed method is very simple to combine multiple outputs from unsupervised parsing, and the method might have an impact to other system combination method, e.g., NER with CRF. The ensemble by hit-count is sound and the merit is proved effective in the experiments especially when comparing MBR which can consider only spans in the multiple system outputs.

- Experiments are well designed and the effect of the proposed method is proved empirically. This work also presents knowledge distillation using RNNG and URNNG so that it might have a potential for a practical application. Analysis is also convincing by comparing multiple diverse systems.

### Weaknesses
- It is comparing only for English, and it would be better to compare the model with other languages, e.g., Chinese, for further strengthening this submission.

### Questions
- I'd like to know the impact of length of inputs, e.g., whether the proposed method is better in lengthy input or not.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel strategy following an ensemble-then-distill paradigm to deal with the unsupervised constituency parsing task that aims to hierarchically structure sentences without relying on linguistically annotated data. The proposed approach firstly ensembles existing unsupervised parsers based on the notion of “tree averaging” and then conducts distillation to create a student model. This technique efficiently alleviates the over-smoothing issue that frequently arises in multi-teacher distillation. Experimental results indicate that such an ensemble-then-distill method outperforms existing approaches with superior effectiveness and robustness.

### Strengths
The major contributions include:

1.      A new notion of tree averaging and the corresponding search algorithm: CYK variant

2.      Ensemble-then-distill approach that trains a student parser from an ensemble of teachers.

3.      The inference time of the student model is 18x faster than the ensemble method.

4.      A hypothesis that different unsupervised parsers capture different aspects of the language structures and the verification with experiments.

### Weaknesses
1. Lack of clarification regarding the methodology design.

- The averaging tree is derived with the highest total F1 score compared with different teachers. Have the authors tried other methods of calculating the similarities between trees? Perhaps a fair comparison is needed to further indicate the effectiveness of the proposed tree averaging method.
- The authors did not provide a detailed explanation for choosing the seven unsupervised parsers introduced in Section 3.2 as teacher models. For instance, why did the authors select ContextDistort as one of the teachers despite its relatively inferior performance and inference efficiency?

2. The authors state in Introduction that combining the different parsers may leverage their different expertise. The authors attempt to verify this statement in Section 3.4 by comparing two settings: the ensemble of three runs of the same model and that of three heterogeneous models. I wonder if it is more appropriate to choose the model with highest performance in the former setting so that it can be further validated there exists additional boost due to different expertise (e.g., Neural PCFG for Group 2).
3. The writing can be improved. There are some typos and unclear descriptions. Please refer to comments for detail.


Comments

1. Minor comments on writing:
(1)	Paragraph #1 in Introduction: ...to explore unsupervised methods as it eliminates... -> ...to explore unsupervised methods as they eliminate...
(2)	Paragraph #1 in Section 3.1: ... on the widely used the Penn Treebank -> ... on the widely-used Penn Treebank

### Questions
Despite these merits, there are some points which need further clarification, and some suggestions.

1.      The ensemble method demonstrates its effectiveness on PTB. However, in 2020, the F1 score of CRF parser on PTB variants had already been above 90 (Zhang et al., 2020). There is indeed a performance boost in comparison to oracle score (the highest possible F1 score of binarize groundtruth trees). But it is not appropriate to claim that “largly bridging the gap between supervised and unsupervised constituency parsing” on Page 6.

2.      In Results on SUSANNE, the authors claim that “This is a realistic experiment to examine the models’ performance in an unseen low-resource domain.” However, SUSANNE is an English dataset. In CoNLL Shared task, there are tree-banks on low-resource languages (Zeman et al., 2017). It’s better that the authors can demonstrate the effectiveness of the approach on some of these low-resource language datasets.

References:

Zeman, D., Popel, M., Straka, M., Hajic, J., Nivre, J., Ginter, F., Luotolahti, J., Pyysalo, S., Petrov, S., Potthast, M., Tyers, F., Badmaeva, E., Gokirmak, M., Nedoluzhko, A., Cinkova, S., Hajic Jr., J., Hlavacova, J., Kettnerová, V., Uresova, Z., … Li, J. (2017). CoNLL 2017 Shared Task: Multilingual Parsing from Raw Text to Universal Dependencies. Proceedings of the CoNLL 2017 Shared Task: Multilingual Parsing from           Raw Text to Universal Dependencies, 1–19. https://doi.org/10.18653/v1/K17-3001

Zhang, Y., Zhou, H., & Li, Z. (2020). Fast and Accurate Neural CRF Constituency Parsing. Proceedings of the Twenty-Ninth International Joint Conference on Artificial Intelligence, 4046–4053. https://doi.org/10.24963/ijcai.2020/560

3.      In Table 3 on Page 7, PTB-supervised model is used for comparison. Which PTB-supervised model is used?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an ensembling approach for the task of unsupervised constituency parsing. Having trained a group of various prior models, they use a dynamic program to find the “average tree” of their predictions. While this approach works well, it can then be further used for distillation into an RNNG which works more efficiently and in some settings more accurately. They also analyze to what extent the improvements in performance from ensembling are down to smoothing vs. combining expertise.

### Strengths
- The insight that different models are weakly correlated despite similar F1 is interesting and well motivates the approach
- The proposed dynamic program is intuitive and well explained
- Experiments are strong and thorough
- The analysis of gains from denoising vs. difference in expertise is well conducted

### Weaknesses
- The fact that the F1 gains from distillation do not carry over to the out of domain setting is a drawback and somewhat underexplored
- There is a lack of qualitative analysis of the types of behaviors that different model types exhibit, and how ensembling actually combines those. Some of this is done in the Appendix but it would be nice to see specific examples in the main paper, especially since that analysis is wrt constituency labels which the model isn’t actually being evaluated on.

### Questions
- How does regular RNNG perform, and why not use it as a teacher?
- Regarding the experiment in Figure 1, do you see similar results if you measure the gains from the *distilled* ensemble? That would be useful to see alongside

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a consistency-based decoding method for unsupervised constituency parsing, which can also be formulated as minimum Bayes risk decoding.
Experiments demonstrate significant improvement over existing methods.

### Strengths
- Significant contribution to unsupervised constituency parsing, including a generative MBR process and consistently improved results.

- Comprehensive analyses are carefully conducted and presented.

- The paper is very well written and easy to follow.

I also wanted to note the statements and conclusions in this paper are remarkably honest. 
Most of the claims are very well supported by related work and experimental results. 
While this is generally not considered as a strength, such a presentation style should be commended and encouraged in recent years.

### Weaknesses
- MBR-style or consistency-based methods have also been applied to parsing for decoding or model selection, but the authors failed to recognize and discuss them. To name a few, [Smith and Smith, 2007](https://aclanthology.org/D07-1014.pdf) and [Zhang et al., 2020](https://aclanthology.org/2020.acl-main.302.pdf) used MBR-decoding to improve dependency parsing; [Shi et al., 2019](https://aclanthology.org/P19-1180.pdf) adapted an agreement-based model selection process for distantly supervised constituency parsing.

- The motivation is not completely convincing. Recent trends in NLP demonstrate that explicit parses might not be crucial or even necessary to many user-facing applications (e.g., GPT models do not really use explicit language structures), which contradicts the first sentence in this paper (*Constituency parsing is a core task in natural language processing*). Traditionally, such structures served as a backbone for many NLP models, and the prediction of them was therefore referred to as *core NLP*. I am not sure if the parsing is as important as what I receive from this paper. Please consider revising or including more justification. 


**Minor points on weaknesses**

- The references in this paper, especially to conventional linguistic literature, need some work:
    - Section 1: Carnie (2007) and Fromkin et al. (2003) are introductory books. Both should be changed to Chomsky (1957). Syntactic Structures.
    - [Spitkovsky et al. (2013)](https://aclanthology.org/D13-1204.pdf) is worth a mention in the related work section.

- Page 1: low correlation among different unsupervised parsers: [Williams et al. (2018)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00019/43445/Do-latent-tree-learning-models-identify-meaningful) discovered a similar issue within the same model architectures (Table 1, right settings).
This is worth a discussion.

- Not really a weakness for a machine learning conference submission: since the topic of this paper is highly linguistic, I am willing to see a detailed analysis of what patterns are fixed. For example, do NPs/PPs with rare words receive more fixes than those with frequent words, or the opposite, or not significant? Do VPs with transitive verb heads receive more fixes than those with intransitive verb heads, or the opposite, or insignificant? Does the student extract any constituent that does not receive any vote from teacher models, due to fixes on shorter spans and CYK?

I am being conservative in my initial evaluation and am happy to increase my rating if most of the above issues are fixed.

### Questions
- Which split of PTB did you use to generate the statistics in Table 1?
- Table 2: why are the +RNNG/+URNNG oracle performance different from the basic one (83.3)?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers ensembling unsupervised (unlabled binary) constituency parsers. The main technical piece is an MBR decoding algorithm that finds the highest-F1 tree with respect to a set of candidate trees. Experiments show that this ensembling method is more effective than simply selecting a max-intra-F1 candidate tree or training a student model on the union of candidate trees (union distillation).

### Strengths
- Simple but insightful observation that it is possible to "generate" a tree from candidate trees
- Derivation of the hit-count maximization algorithm 
- Strong results

### Weaknesses
- Somewhat narrow scope (ensembling constituency trees)
- Some details missing (see the questions)

### Questions
Would "Our ensemble (X teacher across runs)" in Table 2 use candidate trees from different models, or do they all end up from the same model (e.g., ConTest for X="best")? It's good to know the answer to this question because one of the main claims of the paper is that it's important to exploit the large qualitative differences between different methods (Table 1). The fact that we get the best result by just using outputs from the same model seems to refute that claim (i.e., it's all variance reduction).

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
