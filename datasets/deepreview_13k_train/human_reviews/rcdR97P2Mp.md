# Towards continuous machine learning on periodic crystals by ultra-fast invariants

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
Periodic point sets model all solid crystalline materials (crystals) whose atoms can be considered zero-sized points with or without atomic types.

This paper addresses the fundamental problem of checking whether claimed crystals are novel, not noisy perturbations of known materials obtained by unrealistic atomic replacements. Such near-duplicates have already skewed ground truth because past comparisons relied on discontinuous cells and symmetries.  
 
The proposed Lipschitz continuity under noise is a new essential requirement for machine learning on any data objects that have ambiguous representations and live in continuous spaces. 

For periodic point sets under isometry (any distance-preserving transformation), we designed the invariants that distinguish all known counter-examples to the completeness of past descriptors and detect thousands of (near-)duplicates in the world's five largest databases in a few minutes on a modest desktop computer.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This is a new method for searching crystals. Multiple databases were used for evaluation.

The authors claim large improvements from years to hours.

The paper does make some large claims. For example, in the abstract there is a free standing claim saying
"The proposed Lipschitz continuity under noise is a new essential requirement for machine learning on any
data objects that have ambiguous representations and live in continuous spaces." This is for some types of
neural networks not for all algorithms. Correct? Please clarify by providing evidence or citations supporting the claim that this is an "essential requirement" for all ML on ambiguous data in continuous spaces. Alternatively, please clarify if this applies only to certain types of ML algorithms. 

The paper is written for an extremely specialized and narrowly focused domain and not for the general 
ML crowds found in ICLR.

The authors will need to add more explanations for general purpose ICLR audience. Otherwise this paper should be submitted to a Crystallography journal.

The main contribution is that the authors can  convert any PDD{h} into a fixed-size matrix,
which can be flattened into a vector for easy comparisons, while keeping the continuity and almost
all invariant data.

The authors also directly talk to the reviewers which is unexpected. For example, "We thank all reviewers for supporting scientific integrity, now guaranteed by the proposed invariants." or "Thank you for reading all the proofs!". Such claims are informal and not relevant for a publication in ICLR.

### Strengths
This works showcases large speedups in comparing crystalline structures.
The works extends Widdowson & Kurlin, 2022.
The paper shows and extensive amount of proofs and theorems.

### Weaknesses
This is a new method for searching crystals. Multiple databases were used for evaluation.

The authors claim large improvements from years to hours.

The paper does make some large claims. For example, in the abstract there is a free standing claim saying
"The proposed Lipschitz continuity under noise is a new essential requirement for machine learning on any
data objects that have ambiguous representations and live in continuous spaces." This is for some types of
neural networks not for all algorithms. Correct? Please clarify by providing evidence or citations supporting the claim that this is an "essential requirement" for all ML on ambiguous data in continuous spaces. Alternatively, please clarify if this applies only to certain types of ML algorithms.

The paper is written for an extremely specialized and narrowly focused domain and not for the general 
ML crowds found in ICLR.

The authors will need to add more explanations for general purpose ICLR audience. Otherwise this paper should be submitted to a Crystallography journal.

The main contribution is that the authors can  convert any PDD{h} into a fixed-size matrix,
which can be flattened into a vector for easy comparisons, while keeping the continuity and almost
all invariant data.

The authors also directly talk to the reviewers which is unexpected. For example, "We thank all reviewers for supporting scientific integrity, now guaranteed by the proposed invariants." or "Thank you for reading all the proofs!". Such claims are informal and not relevant for a publication in ICLR.

The work is unnecessarily theoretical.  Giving the impression that there is not much novelty.

The title says "Towards continuous machine learning .. " but no ML example has been provided. Only similarity metrics.

### Questions
It is not clear what is the theoretical vs algorithmic contribution of the work. Please explain.

It is not clear what is the difference with the paper Widdowson & Kurlin, 2022. Please explain.

It is not clear what is the underlying representation that allows for the acceleration. Please provide a detailed explanation of the data structure you use, and how it enables faster computations compared to previous methods.

It is not clear what is the relationship with other existing machine learning methods. Please explain.
For example, can you compare your method to particular ML techniques used in materials science or crystal structure analysis. Can this method be integrated with graph neural networks or other ML models used for predicting crystal properties? Such as resistance to temperature changes?

### Soundness
1

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The work presents a novel representation for periodic crystals that allows for efficient and effective identification of de-facto duplicates in current crystal databases. In particular the representation is Lipschitz-continuous under noise, i.e., tiny variations of crystal structures, e.g. caused by measurement noise, only yield tiny distances in representation space. The representation allows the efficient identification of duplicates or (noisy) near-duplicates in databases by pairwise comparisons in databases with in total almost two million entries, thus revealing a large number of previously unknown duplicates as well as labelling errors (same structure with different chemical composition, which is infeasible) in the databases. Last but not least, the proposed approach is able to distinguish all known counter-examples, i.e. examples indistinguishable by some previous representations.

### Strengths
The work presents novel representations for periodic crystals that allows for efficient and effective identification of (near-)duplicates in existing databases. Thus the work does not only yield highly relevant practical findings, but also prevents "adversarial attacks" via claimed-new "discoveries" of materials which are however de facto already known and were only possible by exploiting deficiencies of previously proposed representations.

### Weaknesses
The authors proposes a procedurally constructed representation, and "machine learning" in their work is limited to pairwise distance computation. In this regard, having "machine lerning" in the title is somewhat misleading. The contribution may be well suited also to be placed in a more application-oriented publication venue (Science?). However, it is clear that a representation (albeit engineered) with the stated properties that, furthermore, allows very fast distance computation is also highly relevant for any kind of machine learning on crystal structures, as manifested by the fact that previous works the authors build upon have appeared at NeurIPS and CVPR.

Note, I revised my score from 8 to 5 after contemplating the other Reviews and discussing with CLkj; see comment further down for details

### Questions
-- In Problem 1.2, I assume (c) (2) should be symmetry, i.e., I guess d(b,c) is a typo and should be d(b,a)?

-- In 1.2. (d), lambda is not defined

-- p.2 l. 93f "gigantic loophole": It would be helpful to the reader if you could again cite the relevant reference (given earlier in the introduction)

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses identifying near duplicate crystal, using invariants computed from point distance distributions PDD. Apparently the authors found a fast method for detecting and describing near duplicate crystals, tested on retrieval experiments with several crystal databases.

### Strengths
The development of invariants to rapidly identify near duplicate structures is interesting.

### Weaknesses
This paper seems to use a lot of language, assumptions references only clear to those studying crystal structures, and thus it is unclear if or how it links to the broader machine learning community. For example, "points" are discussed throughout the paper, it’s only in discussion where it is mentioned these points are in 3D space. There is no mention of other work using point distance distributions PDDs, e.g. distance transforms in classic computer vision, invariants such as the scale invariant feature transform SIFT used to identify near duplicate photos on a repeating pixel lattice.

No discussion of other invariants, e.g. 3D SIFT used to characterize and detecting near duplicates based on non-repeating structures in human brain images, which would seem to work quite well in the case of redundant crystal structures, using precisely the same KD search tree structure mentioned in this work, however appear unknown to the authors, e.g.
[a] Chauvin, Laurent, et al. "Neuroimage signature from salient keypoints is highly specific to individuals and shared by close relatives." NeuroImage 204 (2020): 116208.

### Questions
Why is there no mention of invariants from well-known work outside of work repeating crystal structures? Particularly given identical technologies used for retrieval, e.g. KD-tree search trees, using invariants derived from non-repeating structures (e.g. human body anatomy) which would appear to be a more difficult problem? If these are irrelevant, it would be good to know why.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper presents a novel approach to periodic crystal representation by addressing limitations in existing methods for distinguishing unique crystalline structures. The authors propose a new invariant for periodic point sets, which is designed to improve the identification of unique crystals. This invariant provides a systematic approach to eliminating near-duplicate entries in material databases.

### Strengths
The paper seems to offer a substantial contribution to evaluating novelty in crystalline materials, presenting a practical and (as far as i can tell) theoretically sound method for ensuring data quality in large-scale material databases. This seems to address an important challenge in materials science research.

### Weaknesses
The relevance to ICLR is not particularly clear, as the work does not introduce a new ML method or focus on representations of ML models in the typical sense. The authors should address the relevance for iclr or machine learning in general to improve understanding by the ml community. A less technical introduction would also benefit understanding and readability. Overall, the paper may be better suited for a more specialized audience or a theory-focused computer science conference.

The paper is dense with technical details; consider moving some to the appendix (e.g. some examples) to allow more space for intuitive explanations and discussion.

Invest more effort in improving the illustrations, particularly graphs. Figure 6’s text is small; consider adjusting the color scheme in Figure 1 to make it clearer and remove some of the elements to make it less crowded.

The work may be suitable for a theory-focused ml conference, as it introduces a well-justified quality metric for material datasets rather than a new ML method.

The language at times seems overly opinionated, with phrases like “notoriously hard problem” and “avoid such embarrassment.” These could be rephrased to maintain a more objective tone.

### Questions
- Consider rephrasing or omitting the last sentence of the discussion, as it seems somewhat out of place.
- The paper is dense with technical details; consider moving some to the appendix (e.g. some examples) to allow more space for intuitive explanations and discussion.
- Invest more effort in improving the illustrations, particularly graphs. Figure 6’s text is small; consider adjusting the color scheme in Figure 1 to make it clearer and remove some of the elements to make it less crowded.
- The work may be suitable for a theory-focused ml conference, as it introduces a well-justified quality metric for material datasets rather than a new ML method.
- The language at times seems overly opinionated, with phrases like “notoriously hard problem” and “avoid such embarrassment.” These could be rephrased to maintain a more objective tone.

### Soundness
3

### Presentation
3

### Contribution
2
