# Sometimes I am a Tree: Data Drives Unstable Hierarchical Generalization

- Decision: Reject
- Scores: 5, 8, 3

## Abstract
Neural networks often favor shortcut heuristics based on surface-level patterns.
As one example, language models (LMs) behave like n-gram models early in training. 
However, to correctly apply grammatical rules, LMs must rely on hierarchical syntactic representations instead of n-grams.
In this work, we use cases studies of English grammar to explore how latent structure in training data drives models toward improved out-of-distribution (OOD) generalization. 
We then investigate how data composition can lead to inconsistent OOD behavior across random seeds and to unstable training dynamics. Our results show that models stabilize in their OOD behavior only when they fully commit to either a surface-level linear rule or a hierarchical rule. The hierarchical rule, furthermore, is induced by grammatically complex sequences with deep embedding structures, whereas the linear rule is induced by simpler sequences. 
When the data contains a mix of simple and complex examples, potential rules compete; each independent training run either stabilizes by committing to a single rule or remains unstable in its OOD behavior. These conditions lead `stable seeds' to cluster around simple rules, forming bimodal performance distributions across seeds. We also identify an exception to the relationship between stability and generalization: models which memorize patterns from low-diversity training data can overfit stably, with different rules for memorized and unmemorized patterns.
Our findings emphasize the critical role of training data in shaping generalization patterns and how competition between data subsets contributes to inconsistent generalization outcomes across random seeds.git}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study analyzes the role of the syntactic complexity in language models’ acquisition of hierarchical inductive biases. Specifically, by generating sentences with varying syntax tree depths and of varying structures (some with mixed scoping and others with forward scoping), the features that lead to linear or hierarchical generalization are isolated. Additionally, by mixing these types of data, the authors conduct a grokking-style analysis of when stable, unstable, hierarchical, linear, or mixed generalizations are likely to be learned. 

It is found that including sentences with a syntactic tree depth of at least 3 is required for hierarchical generalizations to be stably acquired, and that mixing depths in the training data can lead to unstable generalizations. It is also found that if the data is not sufficiently diverse, memorization (rather than any consistent generalization) is the preferred strategy.

### Strengths
* The paper adds to a rich literature on directly evaluating the inductive biases of language models. This paper approaches it from a grokking perspective, which, to my knowledge, has not been done before.
* In Fig. 4, it is interesting that such a small variety of syntactic structures in the declaratives would lead to hierarchical generalization. I had assumed that a more naturalistic and varied distribution would be necessary to prevent memorization.
* Thorough analysis of variation across many random seeds.

### Weaknesses
1. The findings could be much better contextualized with related work throughout the paper. For example, at L150: this is not the first work to analyze the effect of data on syntactic generalization. Mueller et al. (2023) (who are currently cited only in the Appendix) do a similar analysis, finding that simpler corpora lead to syntactic generalization with less data. Additionally, when referring to the syntactic transformations task setup at L144, Frank & Mathis (2007) [1] is the correct citation. At L154-161 (and App. F): it would be nice to contextualize this with analyses from McCoy et al. (2020) on instability across random seeds. In Sec. 4.3, these findings are very related to those of Papadimitriou & Jurafsky (2023) [2] (who are not cited) on training with recursive and/or cross-serial dependencies.
2. The findings are somewhat obvious in light of the above citations, and in light of grokking work (which, by the way, should also be better cited and discussed; see [3,4,5]). Data determines generalization because neural networks are a statistical approach to learning. There are probably new insights to be gleaned from this new task setting compared to past grokking work, and it could be nice to explicitly enumerate these in the paper.
3. L212-215: It is not clear why these hyperparameters were chosen, and why different hyperparameters were used for the two tasks.
4. Related to the first point (but more minor), the decision of what to include in the main paper vs. the appendix Related Work sections currently feels arbitrary.

### Questions
Questions
===
1. Where did the hyperparameters in L212-215 come from? Was there some tuning involved, and if so, would it be possible to show results for other tested hyperparameters?
2. By syntactic complexity, do you generally mean syntactic tree depth? The rarity/difficulty for humans in processing of particular structures? Number of edges in the tree (which could correlate with sentence length, even if the maximum depth of the tree were low)? I assume the first given the analyses in Sec. 4, but would be nice to explicitly define the term.
3. L420: which studies?
4. At first glance, Fig. 4 and Sec. 6 feel contradictory. There is some interesting nuance here that could be interesting to explore: diversity is necessary to prevent memorization, but at the same time, including a diverse mixture of complex and simple sentences leads to *worse* generalization than simply using more complex sentences. Why is this?

Suggestions/Typos
===
* L182: there are *at least* two strategies. The model could rely on other heuristics, such as always moving the affirmative verb in QF as opposed to the main or first verb (as attested in Mueller et al., 2024).
* Table 1 caption: by “left” and “right”, do you mean “top” and “bottom”?
* L113: two periods

References
===
[1] Robert Frank & Donald Mathis (2007). “Transformational networks.” Models of Human Language Acquisition. https://bpb-us-e2.wpmucdn.com/websites.umass.edu/dist/a/27637/files/2017/06/cogsci-2007.pdf

[2] Isabel Papadimitriou & Dan Jurafsky (2023). “Injecting structural hints: Using language models to study inductive biases in language learning.” Findings of EMNLP. https://aclanthology.org/2023.findings-emnlp.563/

[3] Yifei Huang et al. (2024). “Unified View of Grokking, Double Descent and Emergent Abilities: A Perspective from Circuits Competition.” COLM. https://arxiv.org/abs/2402.15175

[4] Vikrant Varma et al. (2023). “Explaining grokking through circuit efficiency.” https://arxiv.org/abs/2309.02390

[5] Ziming Liu, Eric J. Michaud, & Max Tegmark (2023). “Omnigrok: Grokking Beyond Algorithmic Data.” ICLR. https://arxiv.org/abs/2210.01117

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates the influence of training data composition on the generalization behaviors of language models, focusing on their ability to learn hierarchical syntactic representations versus relying on surface-level heuristics such as n-gram models. Through case studies involving English grammar tasks (specifically question formation and tense inflection) the authors show that the complexity and diversity of training data play pivotal roles in determining if models adopt hierarchical rules or simpler linear heuristics. 
Interesting findings of the paper: 
i) Adding sentences with deep syntactic trees in the training data encourages models to develop hierarchical syntactic representations  (and this seems to enable out of distribution generalization).
ii) When the training dataset have a mix of simple and complex grammatical structures, models show unstable training dynamics and inconsistent rule commitments across different random seeds (this aligns with findings by McCoy et al. (2018, 2020))
iii) In case of low data diversity, models tend to memorize patterns without learning robust hierarchical or linear rules, resulting in poor generalization.

I think the main message of this paper is the relevance of training data features in shaping the inductive biases of neural networks.

### Strengths
- Interesting analysis of the mechanisms of rule commitment.
- The identification of a memorization regime, where models stabilize without learning either hierarchical or linear rules.
- The findings are replicated across two distinct grammatical tasks, and backed up by linguistics theroies.

### Weaknesses
- The experiments utilize relatively small transformer models trained on synthetic datasets with 100K samples (it doesn't make the study less valid, but larger models may exhibit different inductive biases and learning dynamics that are not captured by smaller-scale experiments).
- The authors use a fixed set of hyperparameters (learning rate of 1e-4, Adam optimizer, specific layer configurations) across all experiments, without addressing how variations in hyperparameters might influence the model's ability to learn hierarchical rules or affect training stability.

### Questions
- It might be worthy study how other objectives (like MLM) interact with data composition to affect rule learning. 
- Have you considered how the role of data composition might vary with languages that have different syntactic structures?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigate generalization of LMs.  Specilically, data composition significantly influences a model's out-of-distribution (OOD) generalization.  Insufficient data diversity can lead models to rely on memorization rather than achieving true generalization. They primarily validate these observations through learning on grammatical tasks.

model: 12M  decoder-only Transformer.
tasks: question formation, tense inflection.

### Strengths
The paper is well-written, with comprehensive visuals and thorough experimental results.

### Weaknesses
1. The conclusion in this paper have many overlaps with previous studies[1],[2],[3]; please specifiy your difference and contribution detailed.
2. The experiments only contain two dataset: question formation and tense inflection. This limited validation is insufficient to support the overall conclusions of the paper, generally speaking.  More tasks and models are needed.  Suggest tasks: language modeling, mathematics reasoning … …
3. The authors present only the experimental observation that "lower diversity data tends to promote memorization, while higher diversity data encourages generalization." These are  obvious conclusions compared with previous papers. Are there any new insights offering deeper theoretical reasoning or more controlled experiments to support these findings? or fuerther verfiication on LLMs, e.g. 7B ?

### Grammar

Line 113: “. . “

Line 119: multiple abbreviation definitions

Table 1: revise “Left” and “right” to “Top” and “Bottom”

[1] Liu Z, Michaud E J, Tegmark M. Omnigrok: Grokking beyond algorithmic data[C]//The Eleventh International Conference on Learning Representations. 2022.

[2] Zhu X, Fu Y, Zhou B, et al. Critical data size of language models from a grokking perspective[J]. arXiv preprint arXiv:2401.10463, 2024.

[3] Wang B, Yue X, Su Y, et al. Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization[J]. arXiv preprint arXiv:2405.15071, 2024.

### Questions
See in Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1
