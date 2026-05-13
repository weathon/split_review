# Contrastive Learners Are Semantic Learners

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
In this work, we explore the definition of semantic equivalence to establish a connection between contrastive tasks and their downstream counterparts. Specifically, we investigate when a contrastive dataset can learn representations that encode formal semantic equivalence relations for a specific downstream task. In our analysis, we recover a surprising hypothesis resembling the distributional one---dubbed distributional alignment hypothesis. Under this assumption, we demonstrate that the optimal model for simple contrastive learning procedure must generate representations that encode formal semantic equivalence relations for the downstream task. Furthermore, we support the theory with a series of experiments designed to test the presented intuitions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper explores the theoretical foundation of contrastive learning, a popular self-supervised technique used to generate high-quality embedding representations across various data modalities (e.g., images, audio, text). While contrastive learning has shown empirical success in encoding semantically similar objects into close embedding representations, a formal understanding of this process is lacking. To address this gap, the authors propose a formalization of semantic equivalence in contrastive learning, inspired by principles from programming language theory. They introduce the distributional alignment hypothesis, which posits that the alignment of distributions in contrastive tasks is essential for effective downstream performance. Through analysis of the SimCLR method, they demonstrate that contrastive learning can inherently encode semantically equivalent symbols in close proximity within the embedding space.

### Strengths
1.The paper provides a theoretical perspective on contrastive learning, bridging the gap between empirical success and formal understanding.

2.Introducing the concept of semantic equivalence in the context of contrastive learning is innovative, borrowing ideas from programming languages to define how two symbols can be considered equivalent in the embedding space.

3.The proposal of the distributional alignment hypothesis offers a new framework for understanding when contrastive tasks are effective for downstream applications, potentially guiding future work in contrastive learning model design.

### Weaknesses
1.While the theoretical findings are compelling, the paper might benefit from empirical experiments to validate the proposed hypotheses, particularly the distributional alignment hypothesis, across different contrastive learning frameworks. As the study is heavily focused on theoretical formalism, which may limit its immediate applicability for practitioners who are looking to implement contrastive learning solutions without deep theoretical knowledge.

2.The paper’s formalism of semantic equivalence is based on an analogy to programming languages, which may not translate perfectly to the nuances of different data modalities (e.g., images vs. text), potentially limiting its generalizability across tasks.

3.There have been a number of analysis to study the effectiveness of contrastive learning, but it is hard to say how the new perspective would help the improvement of contrastive learning method.

### Questions
Please refer to the weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The core argument is that if a pretraining task is "distributionally aligned" with a downstream task, this alignment benefits the downstream task. The concept of distributional alignment relies on "semantic equivalence" -- where 2 features are interchangeable for a prediction task without altering the target label's probability (e.g., synonyms). Two tasks are then distributionally aligned if they share these equivalences; that is, if tokens are semantically equivalent in one task, they remain so in another. The paper suggests that pretraining with a contrastive loss facilitates this by encouraging the model to capture these contextual equivalences on  context prediction task, making it beneficial for downstream tasks (when this alignment holds).

### Strengths
The paper presents an interesting theoretical exploration, backed by set of empirical experiments that, while somewhat limited, suppor t and illustrate the main theoretical arguments. Overall, the paper is clearly written, and the theoretical results, though potentially unsurprising, appear to offer novel insights.

### Weaknesses
Comments

1. This framework seems to have parallels with the learning theory in multitask learning. For instance, Maurer et al. (2016) (multitask subspace learning) argue that multitask learning can be advantageous when task-specific functions can be decomposed into shared and unique components, i.e., f_k = g_k cdot h, where function h is shared across tasks. Drawing on these connections with LT for MTL may be beneifical, and may clarify the novelty. Currently, previous research on MTL is not discussed in the paper.

2. The focus on token representations (word embeddings) as the primary benefit of pretraining is interesting, but it raises a question: could this analysis extend beyond token-level representations to contextualized models as a whole? It would be valuable to explore if and how these insights might generalize. Specifically, the current analysis seems limited to the embedding layer, but the benefits of pretraining may extend to the entire network architecture and the learned contextual representations, not just the initial token embeddings. The paper should discuss whether the notion of distributional alignment can be applied to these contextualized representations.

3. Lastly, the assumption of strict equivalence across all predictions might be too strong. A more nuanced setting, where only some predictions share semantic equivalences with the downstream task, would broaden the applicability. For example, if predicting continuations like "thumbs_up" and "thumbs_down" shares equivalences with a downstream sentiment classification task, but other alternative may not share them, the theory should ideally capture this partial alignment.  The intuition is that probably some of the pretrainintg decision share equivalencess, some unrelated, some require more 'fine-grain' equivalences' or more coarse-ones, this still works.

### Questions
See the three comments above, I'd appreciate authors view on these points.

### Soundness
3

### Presentation
4

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
The paper explores contrastive learning and investigates under which conditions contrastive learning can be effective for downstream tasks. The paper introduced a "distribution alignment hypothesis": if the data distributions used in contrastive learning and downstream tasks are aligned, then contrastive learning will learn semantic representations that good for the task. To support the hypothesis, the paper provides a controlled experiment using a mod-addition task.

### Strengths
At a high level, the work is well motivated: the match between the data used in contrastive learning and final downstream task is crucial for good empirical performance.

### Weaknesses
- The main limitation I see is similar to that the authors identify in Section 7: the alignment hypothesis introduced is very strong and verifying it is not possible in practice. On the other hand, the intuitions that it sheds light on are not novel: despite the claims made, it's been known for a long time that one can learn similarity from this type of data (please see work such word2vec, or subsequent papers such as Levy and Goldberg, showing the relation to the classic distributional semantics work)   
- The paper considers a very specific form of contrastive learning using a specific augmentation function. In general the term contrastive learning is much wider, and the data used varies widely, from data with labels in classification, to question answer pairs in retrieval. I would recommend being much more specific in the claims made.  
- The paper is very loose with the terminology that is at the basis at its main questions and claims, leading to vague or in-accurate statements. For example the answer to RQ2 in intro is clearly yes: we can train embeddings to reflect semantic similarity (see more in suggestions below). Similarly, what is a semantic learner? Semantics is a very wide term (see the field of semantics in linguistics) and yes, speaking in general terms, we already know we can learn meaning from raw data.

### Questions
The paper needs to provide definitions or be very specific about the terms such as "semantic relations". For example in RQ2 (line 47): "can we train embeddings that effectively encode semantical relations?" What do you mean by semantic relations here? And the answer to this question is yes, clearly more than ten years of research in the field of distributional semantics have shown that we can train them to reflect semantic similarity.    
I would also encourage the authors to try and get to core of their findings and explain them better: I struggled to figure out if there is actual content to the definitions and theorem given, or I was simply walked through re-writing of formulas. For this, the paper would benefit from focusing on the actual setup (for example the SimCLR variants used) and less on making wider claims about the findings.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work presents an analysis that contrastive loss (InfoNCE) learns representations that encode semantic relationships effective for downstream tasks. The paper proves that, under certain assumptions, semantically equivalent symbols have the same learned embeddings.

### Strengths
1. The paper borrows frameworks from programming languages to analyze theoretical properties of contrastive embeddings, which is an original and interesting perspective.
2. The paper is written clearly. The exposition is very good for building up reader intuition and the assumptions are clearly stated for each proof.

### Weaknesses
 > Weakness 1. Corollary 4.3 states an **iff** relationship between the alignment of symbols and their respective embeddings. However, the authors only prove the forward direction.

Conditional on Corollary 4.3 being a typo, and only the forward direction holding: $u \doteq_{\mathcal{D}} v \Rightarrow \mathcal{E}^*(u) = \mathcal{E}^*(v)$, why is this conclusion valuable? An encoder that maps every input to 0 also has this property.

> Weakness 2. The assumptions are unrealistic and lead trivially to the Theorems 3.1 and 4.2.

I believe the proof for Theorem 3.1 is a bit obfuscated. The authors essentially make two assumptions:

1.  that contrastive encoders learn the following probability ratio up to a multiplicative constant: $f_i = c \cdot \frac{p(\rho, y \mid \sigma_i)}{p(\rho, y)}$. (taken from van den Oord et al. (2018))
2.  that $p(\rho, y \mid u) = p(\rho, y \mid v)$, which is a trivial result of (1) $u \doteq_{\mathcal{D}} v$, which implies to $p(y \mid u, \rho) = p(y \mid v, \rho)$,  and (2) $p(\rho \mid u) = p(\rho \mid v)$.

Because of Assumption 2, we can immediately conclude that $f_u = f_v$, and use the basis argument to conclude that $u$ and $v$ must have the same embeddings.

The direct assumption that $p(\rho, y \mid u) = p(\rho, y \mid v)$ seems quite strong and substantially simplifies the analysis, as the desired result follows almost immediately from this condition. Also, it is unclear that this result is meaningful in any way for learnability. As stated previously, the encoder that maps every input to 0 also satisfies this property. It is only this property in conjunction with the reverse direction *(that semantically dis-similar symbols are not mapped to the same encoding)* that is interesting. I may be misunderstanding, but I do not see any proof of the reverse direction in the paper.

Theorem 4.2 follows the same basic structure, and the same concerns apply.

 > Weakness 3. Limited experimentation

The ModAdd experiment, while very illustrative of the beneficial properties of contrastive learning, can be solved symbolically. It lacks complexity and noise seen in real data. Simple experiments in language or vision would better illustrate the developed theoretical results. Possibly an evaluation on an MLM task (as shown as an example in Section 2.1)?

### Questions
Mentioned in weaknesses.

Some additional remarks:
1. In Figure 2(a), the semantically equivalent pairs on average converge to a lower euclidean distance compared to non-semantically equivalent pairs. However, it does not converge to 0, as the previously developed theory would suggest. Why is this the case?
 
2. Minor remark: There should be better ways of motivating the assumption $E^*(\rho_i, y_i)$ forms a basis for $\mathbb{R}^d$. There exists prior work on hyper-spherical contrastive learning that proves certain uniformity results that seem related to the author's assumption of uniformity [1]. 

*Minor*
- line 176: mentions "both" but only lists Theorem 3.1.
- line 385: "potetial"
- Appendix A.9 Title: "SLIGTHLY"

---
References:

[1] Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere. Tongzhou Wang, Phillip Isola 2022

### Soundness
2

### Presentation
3

### Contribution
2
