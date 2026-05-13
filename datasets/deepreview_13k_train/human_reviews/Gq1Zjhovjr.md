# Consistency Regularization for Domain Generalization with Logit Attribution Matching

- Decision: Reject
- Scores: 5, 3, 3, 6, 6

## Abstract
\vspace{-2mm}
Domain generalization (DG) is about training models that generalize well under domain shift. Previous research on DG has been conducted mostly in single-source or multi-source settings. In this paper, we consider a third, lesser-known setting where a training domain is endowed with a collection of pairs of examples that share the same semantic information.
Such semantic sharing (SS) pairs can be created via data augmentation and then utilized for consistency regularization (CR). We present a theory showing CR is conducive to DG and propose a novel CR method called Logit Attribution Matching (LAM). We conduct experiments on five DG benchmarks and four pretrained models with SS pairs created by both generic and targeted data augmentation methods. LAM outperforms representative single/multi-source DG methods and various CR methods that leverage SS pairs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to enhance the consistency regularization method for domain generalization by incorporating a logit attribution matching approach.
The authors first revisit the domain generalization (DG) problem through the causal latent decomposition (CLD) model. This model indicates that DG adheres to the concept of causal-invariant prediction, wherein the predicted labels for a semantic sharing pair remain consistent with diverse non-core factors, as long as the core factors remain unchanged. They then introduce a theorem of Conditions for Optimal DG and unveil consistency regularization as a potential optimal solution for DG, subject to certain assumptions. Existing methods, such as probability matching, logit matching, and feature matching, can all be treated as special cases of this optimal solution. The authors then develop the Logit Attribution Matching (LAM) regularizer, building upon the feature matching method. This approach introduces weights on each dimension of the features, corresponding to each label y. It is hoped that this design allows the model to pay more attention to core factors than non-core factors and improve OOD performance.

### Strengths
1. The writing of this paper is clear and the idea is easy to follow.
2. It is interesting to revisit domain generalization from a causal latent decomposition perspective and highlight the core and non-core factors that are not considered in previous works.
3. It is also interesting to utilize the Optimal DG theorem to summarize the existing consistency regularization methods into a general framework.
4. A thorough experiment is conducted in the main paper content as well as the appendix to evaluate and analyze the proposed methods.

### Weaknesses
1. The contributions may not be very significant because consistency regularization for DG has already been extensively studied in previous research and the proposed method only makes simple modifications to the existing feature matching method. Several concepts in this paper are borrowed from previous ideas, such as targeted augmentation and causal-invariant prediction.

2. The theorem does not serve as a supporting foundation for the proposed logit attribution matching method. It seems that the theorem and the techniques are divided and tell two different stories. Concretely, the theorem just reveals that consistency regularization can be an optimal solution for DG. It is not connected to why logit attribution matching is needed to deal with core and non-core factors. Before this paper can be accepted, it is necessary that it undergoes revision to ensure a clear and concise explanation of how the theorem serves as a driving force behind the techniques employed.

### Questions
Is it possible to build logit attribution matching upon probability matching or logit matching models?
Are they better or worse than building upon a feature matching model? 
Can the authors provide more analysis and explanations of why you just choosing feature matching methods?

### Soundness
3 good

### Presentation
3 good

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
Models can be trained to generalize to new domains (called domain generalization) through augmenting training data. Another approach to domain generalization is through consistency regularization, which enforces that the model should make similar predictions on similar inputs.  This paper proposes using consistency regularization on top of data augmentation; that is, enforcing similarities (at the logit, output, embedding level) on pairs of unaugmented and augmented samples. The paper provides a theoretical result stating that a model that is causal invariant (E.g. $\hat{P}(Y | x) = \hat{P}(Y | \tilde{x})$) and minimizes loss in-distribution will also minimize out-of-distribution loss. The paper finally proposes a new form of consistency regularization, called logit attribution matching (LAM), which encourages feature matching on features that are strongly associated with the true label; this is more granular than previous approaches. The performance of consistency regularization on top of targeted data augmentation is compared to using standard data augmentation to expand the training dataset, and LAM is compared against other consistency regularization methods.

### Strengths
Quality:
- Theoretical results motivate why causal invariant property is important for domain generalization.
- LAM outperforms both DG methods and CR methods 

Clarity:
- Toy illustration in figure 1 made theoretical result and setup more clear. 

Significance:
- Handling OOD settings is an important problem in machine learning.

### Weaknesses
Quality:
- Theory is not connected to LAM. Since the condition is $\hat{P}(y | x) = \hat{P}(y | \tilde{x})$, why does probability matching not work well? Why does LAM work better? The theoretical result provides a high-level condition for domain generalization, but it does not explain why matching probabilities or features across all classes is suboptimal in practice. The paper lacks a clear explanation of how the theoretical causal invariance relates to the specific design of LAM, which only matches features relevant to the true label. The paper needs to clarify the practical differences between the theoretical ideal and the actual implementation.
- The theoretical model's connection to data augmentation is also rather weak. Can you show that your choice of data augmentation is retaining $x^c$ and changing $x^n$? The paper argues that data augmentation retains core features ($x^c$) while changing non-core features ($x^n$), but this is not rigorously demonstrated. The paper needs to provide a more concrete justification for how the chosen augmentation strategies specifically achieve this separation of core and non-core features. For example, how do the augmentations ensure that the background is changed while preserving the object's identity?

Originality:
- Having trouble understanding why CR on top of DA is a contribution. In the related work you say that CR can use different data augmentation strategies as well as alternate ways to pair up samples. The paper combines consistency regularization (CR) and data augmentation (DA), but it is not clear what the novel contribution is. The paper needs to clearly articulate the novelty of combining these two well-studied ideas, especially since the related work already discusses the use of different data augmentation strategies within CR. The paper needs to highlight what is unique about their approach compared to existing methods.
- This paper combines two well-studied ideas into one with a new theoretical result and a new consistency regularization term, but the theory and the new term could be more motivated. The theoretical result and the new consistency regularization term, LAM, are not sufficiently motivated. The paper needs to provide a more compelling argument for why these specific choices were made and how they address the limitations of existing methods. The connection between the theory, the data augmentation, and the LAM regularization is not clearly established.

Clarity:
- Minor nit: this paper has many abbreviations (DG, DA, OOD, CR, CLD). I found that use of DG and DA were a bit confusing the first time I read the paper, and would prefer having more sentences with the full words, at least in the introduction.
- Unclear how contributions in the introduction are related. It reads like a list of ways to improve performance but don't feel well-motivated.

### Questions
- Theory is not connected to LAM. Since the condition is $\hat{P}(y | x) = \hat{P}(y | \tilde{x})$, why does probability matching not work well? Why does LAM work better?
- The theoretical model's connection to data augmentation is also rather weak. Can you show that your choice of data augmentation is retaining $x^c$ and changing $x^n$?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the problem of domain generalization. It creates a theoretical model prescribing the relationship between the source and target domain, for which they argue the benefit of consistency regularization. The paper further presents a new consistency regularization scheme, referred to as Logit Attribution Matching (LAM). The key idea there is the match the logits of a pair of related examples while incorporating label information. Experimental study demonstrate performance improvements.

### Strengths
The main novelty of the paper are theoretical argument justifying the benefit of the consistency regularization and the proposal of the LAM, which take label information into account.  But to this reviewer, the novelty on both sides is thin. Theorem 1 holds nearly trivially; the LAM idea is also straight-forward.

### Weaknesses
1. Theorem 1 contains the very strong assumption that the target distribution of $X^c$ lies within the support of corresponding source distribution (Assumption 3) of the theorem. It is highly suspicious if in reality such a condition would hold true in conjunction with the first two assumptions. Cross-domain learnability also depends on the choice of hypothesis class, constructed (in part) from prior knowledge. The difference between source and target distributions on $X$ should be measured with respect to the hypothesis class. For example, a popular measure is ${\cal H}\Delta{\cal H}$ divergence as in Ben-David & Blitzer. It is possible that the target distribution is supported outside of the source distribution and yet the two distributions have small ${\cal H}\Delta{\cal H}$ divergence, providing learnability.

2. In the description of LAM, it is not clear to me if the weights $\{w_{uy_k}\}$ are hyperparameters or if they are learned during training. If they are hyperparameters, how are they decided? and why not set them to 1 for each $(u, y_k)$?. If they are learned, what mechanism would force them to satisfy the two conditions listed on page 6 (lines 8 and 9)? Note that these weights and $f_\phi$ are learned together.

### Questions
See weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a novel method called logit attribution matching (LAM) for improving domain generalization. Compared to existing consistency regularization methods (probability matching, logit matching, feature matching etc), the proposed method further adds class label information into the regularization term across semantic sharing pairs during data augmentation.

Experiments on a wide set of datasets show that LAM outperforms existing consistency regularization methods, and outperform domain adaptation approaches as well.

### Strengths
- The proposed idea is fairly simple by introducing an additional weight term over each feature unit and class label. Yet this simple weight term seems to be rather useful in improving the OOD performance over a wide set of image datasets.

- The authors did a fairly comprehensive set of experiments over 5 image datasets to demonstrate the superiority of the proposed method.

### Weaknesses
 - Over the five datasets experimented, the augmentation is handpicked based on the characteristics of each dataset. This might make the disentanglement of causal/non-causal features relatively easier (i.e., the SS pairs better fit into this paper's motivation on $X^c$ and $X^n$). I wonder how the proposed approach works when the augmentation is agnostic to the datasets, i.e., what if you apply one of RandAugment / CutMix / AugMix to all the datasets as augmentation, and use LAM for regularization? How would the performance change?

### Questions
- Can the authors show how LAM works when the augmentation applied is dataset-agnostic? e.g., using augmentation methods like RandAugment / CutMix / AugMix for all the datasets?

### Soundness
3 good

### Presentation
3 good

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
This paper studies the magic of consistency regularization in domain generalization. First, authors claim that CR remains effective for DG and there are a few of existing approaches. Then, they study the theory behind the combination of CR and targeted augmentation. Finally, authors design their own approach called logit attribution matching to simply match the logits to further improve the performance. Experiments have shown its effectiveness.

------Post rebuttal

The response addressed my concerns and I increased the score to 6.

### Strengths
1. The paper presents a nice analysis of the consistency regularization in domain generalization, with interesting theoretical support.
2. Based on their theoretical analysis, the LAM approach is proposed which combines the existing targeted augmentation approach to further enhance the performance of CR-based DG.
3. Extensive experiments on several benchmark datasets have shown that the method brings improvements over ERM.

### Weaknesses
1. While I’m not an expert in causality, I hold doubt about the assumption in Figure 1, i.e., the data generation process. We certainly know that such generation process is an assumption, and other causality researchers can draw a completely different causal graph. Therefore, how can authors justify that this figure is practical and can be trusted? This is important since all analysis is based on this basic assumption. Specifically, the assumption that the label Y is solely determined by Xc while ignoring the influence of Xn seems overly simplistic. In real-world scenarios, it's plausible that both core (Xc) and non-core (Xn) factors contribute to the label, albeit perhaps with varying degrees of influence. This oversimplification could limit the applicability of the theoretical analysis.
2. I admire the effort to combine targeted augmentation with CR. But I do not think targeted augmentation is algorithmically novel since this is not general and hard to generalize to other datasets, given the wide popularity of DG in different applications. Therefore, the introduction of targeted augmentation is not efficient or general. This makes LAM deeply rely on the effectiveness of TA. I would like to know how can LAM be applied to other new domains where targeted augmentation is not realistic. The reliance on targeted augmentation is a significant limitation. The paper does not adequately address the scenario where such augmentations are not readily available or are difficult to define. This raises concerns about the practical applicability of the proposed method in diverse real-world settings.
3. In the experiment section, I did not see any comparison with existing CR-based baselines, but only ERM variants. Did I miss anything?

### Questions
See the weakness. I'm extremely curious about the practical usage of LAM without the help from TA.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
