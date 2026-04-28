# Mixup Your Own Pairs

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 8, 6, 3

## Abstract
In representation learning, regression has traditionally received less attention than classification. Directly applying representation learning techniques designed for classification to regression often results in fragmented representations in the latent space, yielding sub-optimal performance. In this paper, we argue that the potential of contrastive learning for regression has been overshadowed due to the neglect of two crucial aspects: \emph{ordinality-awareness} and \emph{hardness}. To address these challenges, we advocate ``mixup your own contrastive pairs for supervised contrastive regression", instead of relying solely on real/augmented samples. Specifically, we propose \emph{\textbf{Sup}ervised Contrastive Learning for \textbf{Re}gression with \textbf{Mix}up (\textbf{SupReMix})}. It takes \textit{anchor-inclusive} mixtures (mixup of the anchor and a distinct negative sample) as hard negative pairs and \textit{anchor-exclusive} mixtures (mixup of two distinct negative samples) as hard positive pairs at the embedding level. This strategy formulates harder contrastive pairs by integrating richer ordinal information. Through extensive experiments on six regression datasets including 2D images, volumetric images, text, tabular data, and time-series signals, coupled with theoretical analysis, we demonstrate that \textbf{SupReMix} pre-training fosters continuous ordered representations of regression data, resulting in significant improvement in regression performance. Furthermore, SupReMix is superior to other approaches in a range of regression challenges including transfer learning, imbalanced training data, and scenarios with fewer training samples.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper argues that the neglect of ordinality-awareness and hardness causes the sub-optimal performances of contrastive learning for regression. Specifically, the authors propose hard sample mining with mixup augmentations for contrastive learning in regression tasks, dubbed SupReMix, which takes anchor-inclusive mixtures as hard negative pairs and anchor-exclusive mixtures as hard positive pairs. Empirical and theoretic analyses are provided to demonstrate the effectiveness. Extensive experiments on various modalities show the performance gains of the proposed SupReMix over the Vanilla baseline and existing contrastive-based regression methods.

### Strengths
(**S1**) The proposed method is well-motivated to tackle the hard sample mining problem for regression tasks and achieves significant performance gains upon Vanilla.
(**S2**) The authors provide various interesting empirical studies of regression tasks, e.g., visualizations of logit distribution and latent space. These findings are supportive of the proposed method and might be inspiring for designing better algorithms for regression tasks.
(**S3**) The overall representations of the manuscript are well-ranged and easy to follow, which provides empirical analysis and theoretic explanations.

### Weaknesses
 (**W1**) Lack of novelty compared to existing methods. The studied problem and proposed method are not novel enough. As known to all, the hard sample mining problem has been explored since 2020, there are also some relevant methods for regression methods (SupCon, SupCR, Decoupled CL [1]). Meanwhile, the proposed SupReMix utilizes similar strategies to design hard samples as MoCHi [2] and i-Mix [3] for contrastive pre-training and uses similar anchor and sample selection strategies as C-Mixup [4].

(**W2**) Weak experiments. Despite the authors providing extensive comparison results with two directly relevant contrastive learning methods, more related baselines should be compared in various experimental settings. Firstly, the authors adopt the implementation from C-Mixup [4] while not comparing it with it. I suggest the authors add more comparison experiments with existing mixup methods for regression (e.g., Vanilla Mixup, C-Mixup [4], ManifoldMix [5], etc) and general hard sample mining contrastive pre-training methods with mixup augmentations (e.g., MoCHi [2] and i-Mix [3]). Secondly, the authors should not only evaluate on self-supervised pre-training and fine-tuning setting but should conduct the practical training-from-scratch setting as well.

(**W3**) Usage of hyper-parameters. Firstly, many hyper-parameters are used in SupReMix compared to SupCon and mixups for regression tasks. The most widely used mixup augmentations are 

(**W4**) Overlook of some related works. As mentioned above, some general and relevant mixup augmentations [3, 5, 6, 7] should be included as background knowledge. Meanwhile, relevant hard sample mining techniques [2, 5, 7] in contrastive learning should be included and discussed in the related work section.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies representation learning in the context of regression, which is a problem that has received relatively lesser attention in literature. Motivated by the fact that typical objectives for representation learning often introduce unwanted inductive biases into the learning, the paper argues for two key objectives to consider when setting up the represnetation learning : (a) ordinality-awareness, i.e., the latent space must reflect or be sensitive to the ordinality of the output and (b) hardness, i.e., choosing the right level of hardness in choosing negatives and positives within a contrastive training setup.

Ordinality is enforced by choosing negatives from an ordered set of samples according to the function value, such that samples in a level set (same value) are mixed up with samples with different labels.

Hard positives are chosen by mixing up samples that have function value above and below the anchor's function value, where the mixup coefficient is chosen such that the linear combination in the output equals the anchor's actual function value. 

Experiments on a number of different regression benchmarks show improvements over related baselines.

### Strengths
* The paper addresses an important problem on improving representation learning for regression, a domain to which a lot of our insights and beliefs from classification may not generalize.
* I think formulation is intuitive and clever, exploiting the ordinality and mixup in choosing hard positives and negatives makes sense and appears to help. 
* Importantly, the proposed approach -- SupReMix leverages these without leveraging augmenting functions, which is standard in most representation learning to obtain different views of a sample. This is significant since its non-trivial to choose augmentations in regression or for time series data. 
* SupReMix shows superior performance across all baselines considered on all or most of the benchmarks which is encouraging.

### Weaknesses
 * I think the biggest weakness is the lack of comparisons with related works in regression -- most notably C-Mixup (Yao et al., NeurIPS 2022) -- and vanilla mixup as well, as it has been shown to be a competitive baseline even on regression. I think they may be better than the ERM (vanilla) baseline in the experiments. Besides, the C-mixup method is also closely related in the sense that they choose mixup pairs that are close in function value (albeit without considering ordinality) so its worth a deeper comparison even methodologically. It might provide some insights into the strengths of SupReMix.  For example, does adding ordinality with vanilla mixup or C-mixup boost performance of each method? 
* The framework fundamentally relies on ordering the training data according to function value -- how is this implemented in practice? Is the ordering done on each mini batch? 
* Are the backbone networks trained from scratch or do you use pre-trained variants followed by fine-tuning?
* A limitation that is unaddressed here, is that the current method does not generalize to even simpler regression problems where the output function has dimensionality $>1$. 
* Finally, I find the notational style in the paper is a bit confusing and not easy to read. It may help the reader to simplify or modify the notation to benefit legibility .. for e.g. indices, function values, embeddings are all in italics which is not typical and hard to distinguish. Please fix these. 
* Figures 1 A and B, do not convey the message of the method clearly.. and is a bit confusing. I think this can be improved to make the proposed method more explicit.

### Questions
please see questions above.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors study how contrastive representation learning can be improved, specifically for regression problems.

They propose Supervised Contrastive Learning for Regression with Mixup (SupReMix). This entails utilizing mixup in the feature embedding space, to create harder positive and negative contrastive pairs. Hard negatives are created by mixing the anchor with a normal negative example. Hard positives are created by mixing two normal negative examples, such that if the corresponding regression targets are mixed in the same manner, this equals the target of the anchor.

The proposed method is applied to six datasets with different input modalities, with age, text similarity score or sound pressure level as the regression targets. Their method consistently outperforms the vanilla regression baseline, and mostly also other baselines for supervised contrastive learning.

### Strengths
I definitely agree with the authors that representation learning for _regression problems_ has received less attention than for classification. This is an important and interesting problem that I think should be studied more.

The overall proposed method makes intuitive sense, it seems like a reasonable approach.

The proposed method is shown to consistently improve the vanilla regression baseline across a quite wide range of applications.

### Weaknesses
The paper could be a bit more well-written overall. For example:
- Section 2 seems somewhat out-of-place. To me, it doesn't quite follow naturally from Section 1, and it is not entirely clear what the main takeaway should be or how it connects to the rest of the paper. The motivation for this section is not clear; it's unclear why analyzing the behavior of contrastive learning with permuted labels is relevant, and the connection to the proposed method is not explicitly stated. The section lacks a clear explanation of how the observed deficiencies of standard contrastive learning motivate the specific design choices in SupReMix.
- Equation (1) and (3) are difficult to read/parse. They are quite "dense". The notation is not immediately intuitive, and the lack of clear definitions for each term within the equations makes them hard to follow. The reader must spend significant time deciphering the meaning of each symbol and how they relate to each other.
- It is not clear what the theoretical results in Section 3.4 are supposed to tell me, what should be my main takeaway? The theorems and lemmas are presented without clear explanations of their practical implications. It is not obvious how these theoretical findings translate into concrete benefits for the proposed method or how they justify the specific design of the loss function. The connection between the theoretical results and the empirical performance is not well-established.

The proposed method is only applied to regression problems with 1D targets. It is not clear to me whether or not it could be extended. The method's applicability to multi-dimensional regression targets is not discussed, leaving a gap in understanding its broader potential. This limitation restricts the scope of the method and raises questions about its generalizability to other regression tasks.

The proposed method is only applied to datasets where the regression targets take on a relatively small set of different values (see Table 12), for example age in the interval [0, 100] with a bin size of 1. It is not entirely clear to me whether or not the method is somehow limited to such regression problems. The experiments do not explore the behavior of the method with truly continuous regression targets, where the target space is not discretized into a small number of bins. This raises concerns about the method's performance in scenarios with high target variability and its sensitivity to the bin size chosen for the target values.

### Questions
1. Could the proposed method be extended also to regression problems where the targets are multi-dimensional?

2. Is the proposed method somehow limited to regression problems such as age estimation, in which the targets take on a relatively small discrete set of values? Could it be applied also to problems with "truly continuous" regression targets? What happens if, within a given batch, it is not possible to find examples with exactly the same regression target as the anchor?


Minor things:
- Section 4, Evaluation Schemes: The linear probing protocol is used for 4 out of 6 datasets. Any particular reason why? Why not for all 6? Or, why do you finetune the whole network for those 2 particular datasets?
- Table 9 and 10 are interesting results, but for which dataset(s) are these results?
- Section 1, "its dependency on data augmentation restricts its applicability to domains where effective augmentation techniques are lacking": I think this should be the other way around, the applicability is restricted to domains where effective augmentation methods do exist?
- Figure 1 caption, "encodes input to embeddings": input --> inputs?
- Section 3, "which encodes input to embeddings": input --> inputs?
- Personally, I would probably consider modifying the title, making it a bit more descriptive (the current title gives no clear clue that the paper studies the important problem of representation learning for regression).

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper discusses the neglect of contrastive learning for regression tasks. To tackle this issue, the paper introduces "Supervised Contrastive Learning for Regression with Mixup" (SupReMix). In particular, anchor-inclusive mixtures and anchor-exclusive mixtures are proposed. Evaluations are conducted on regression datasets, including 2D images, volumetric images, text, tabular data, and
time-series signals.

### Strengths
This paper is clearly written and organized. The idea of applying contrastive learning to regression is interesting.

### Weaknesses
 * a) No sufficient comparisons are made to demonstrate the solidness of this work. Since this paper proposed a data augmentation method based on mixup, the performance of SupReMix should be compared with other mixup approaches and not just the baseline SupCon. Besides regular Mixup and manifold Mixup, there are many, many other mixup approaches, for instance, C-Mixup [1], local-Mixup [2], and manifold intrusion [3]. The paper lacks a thorough ablation study to justify the specific choices made in the proposed mixup strategy. For example, the impact of different mixing ratios and the choice of anchor samples (both inclusive and exclusive) should be investigated more rigorously. The current comparisons only show that SupReMix is better than SupCon, but it's unclear if the improvement comes from the mixup strategy itself or other factors. A more detailed analysis of the contribution of each component is needed.

* b) Since the idea of contrastive learning is towards the clustering effect. One would naturally think that applying contrastive learning to regression is not viable. Then it would only make sense to compare SuperReMix to regression frameworks without contrative learning, for example, Moving Window Regression [4]. The paper does not adequately address the fundamental question of why contrastive learning, which is inherently designed for discrimination and clustering, is suitable for regression tasks. The authors should provide a more in-depth discussion on the theoretical justification for using contrastive learning in a regression setting. Furthermore, the paper should compare the proposed method with established regression techniques that do not rely on contrastive learning, such as Gaussian Process Regression or Support Vector Regression, to demonstrate its effectiveness in comparison to traditional approaches.

* c) Results in Tab. 1-6 show incremental improvement over the baseline. However, the gain is provided but is w.r.t to vanilla, not second best.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair
