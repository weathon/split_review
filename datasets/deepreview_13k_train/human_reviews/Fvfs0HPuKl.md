# fine-tuning with very large dropout

- Decision: Reject
- Scores: 6, 5, 6, 5, 3

## Abstract
It is impossible today to pretend that the practice of machine learning is compatible with the idea that training and testing data follow the same distribution. Several authors have recently used ensemble techniques to show how scenarios involving multiple data distributions are best served by representations that are both richer than those obtained by regularizing for the best in-distribution performance, and richer than those obtained under the influence of the implicit sparsity bias of common stochastic gradient procedures.

This contribution investigates the use of very high dropout rates instead of ensembles to obtain such rich representations. Although training a deep network from scratch using such dropout rates is virtually impossible, fine-tuning a large pre-trained model under such conditions is not only possible but also achieves out-of-distribution performances that exceed those of both ensembles and weight averaging methods such as model soups. 

This result has practical significance because the importance of the fine-tuning scenario has considerably grown in recent years. This result also provides interesting insights on the nature of rich representations and on the intrinsically linear nature of fine-tuning a large network using a comparatively small dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In the paper, the authors propose a novel, effective fine-tuning method to fix reduced performance on out-of-distribution (OOD) data. In essence, they begin with a model pretrained on a larger dataset and then fine-tune it on a significantly smaller set of labelled data. Given the well-known tendency of modern neural networks to perform poorly on OOD samples, the proposed method aims to reduce this performance gap. The approach is straightforward: it fine-tunes the pretrained model with applying dropout (with high dropout rate) to the penultimate layer. This method improves the final model's performance on OOD data across multiple benchmarks (PACS, VLCS, Office Home, Terra Incognita), surpassing popular baselines like model ensembling and weight averaging in classification accuracy. Furthermore, it introduces significantly less computational and memory overhead and enables faster training than conventional ensembles. The proposed approach is also easy to apply across different architectures.

### Strengths
* The paper is clearly written and easy to follow, with an intuitive and easily understandable idea. The related work section provides a sufficient discussion of existing approaches for generating rich feature representations suitable for OOD data.

* The method is straightforward to apply, requiring only a pretrained model and a simple fine-tuning procedure that is easy to implement and computationally efficient. This approach does not change the inference of the final model (compared to vanilla model baseline), making it significantly more computationally efficient than ensembling-based alternatives.

* The method achieves strong results across various classification benchmarks.

### Weaknesses
 * The experiments are limited to classification tasks on fairly standard datasets, leaving it unclear whether this approach with high dropout rates generalizes effectively to other tasks, such as segmentation or even text classification, or to other architectures, like detection models and etc. This raises questions about the scalability and broader applicability of the proposed method beyond image classification. Can other modalities/tasks be added?  

* While the paper offers a high-level explanation of why applying high dropout during fine-tuning could improves generalization (by generating more "weakly relevant" features), it is not entirely clear why this should occur from a formal standpoint. Consequently, the high dropout rate forces the model to distribute information more evenly across dropped features. However, why a more even distribution would result in more "weakly relevant" features remains unclear. A more detailed discussion would be beneficial.

* As shown in Figure 7 of the appendix, the ensembling approach consistently improves performance on in-distribution data, whereas the proposed high-dropout approach does not always yield similar benefits (and sometimes even reduces performance compared to the baseline, which is somewhat expected). It appears that overly aggressive dropout can significantly undermine performance due to excessive randomness. Could more structured methods, such as Masksembles [1], address this issue? Such methods might also overcome the problem of training a model from scratch with high dropout (which often fails to converge due to randomness) by introducing a more structured way to drop features.

### Questions
* Can the proposed high-dropout method generalize to tasks and architectures beyond classification, such as segmentation, text classification, or detection? Can you provide such evaluations?

* Why should evenly distributed information across dropped features lead to “weakly relevant” features? Is further theoretical support available?

* The underperformance of ensembles is somewhat surprising. A potentially useful baseline could involve training ensembles with a shared classification head, where all layers except the final one remain distinct for each model in the ensemble. This setup would encourage the ensemble to generate features from the same domain, allowing for feature averaging, which could improve OOD performance. Would that resolve the underperformance issue? 

* Could structured dropout methods, such as Masksembles, help address the issue of aggressive dropout leading to worse performance on in-distribution data? Could it help train models from scratch with high dropout rates without compromising generalization?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The submission proposes a technique for fine-tuning pre-trained networks: apply a very large dropout rate (90%) on the penultimate layer of residual networks. This approach is shown to be effective at making fine-tuned networks more robust to an OOD dataset, when compared to two existing approaches.

### Strengths
Originality: Very high dropout rates have not been explored because they tend not to work well when training from scratch. Exploring it in the context of modern residual networks and fine-tuning with an emphasis on evaluating OOD robustness is original, to my knowledge.

Clarity: The paper is very clearly written, and is easy to follow.

Quality: The ideas are more or less technically sound, building on previous observations. The experiments are adequate to support the claims made — high dropout is more effective for OOD generalization for a fine-tuned model relative to related ensemble methods. 

Significance: The results appear to be consistent, though marginal most often, improvements over the selected baselines. Given that the proposed method is simple and lightweight makes it practically interesting.

### Weaknesses
While the intuitions motivating the method are interesting and seem to play the role of establishing weight-averaging and ensemble as the natural baselines, it is not very clear that these intuitions are sufficient to narrow the scope of comparison to only the selected baselines.

It seems that performance is somewhat sensitive to the precise value of the dropout rate — 90%. It is not clear that this rate was chosen without looking at test-time performance. 

It is not fully clear to me why applying large dropout only to the penultimate layer is necessarily the best implementation, given the motivation. Does performance suffer if such dropout is applied everywhere, and not in a “dimension-aligned” fashion?

L296-298 says “the i.i.d. performance of the large dropout method lags behind that of ensembles, revealing that the o.o.d. performance improvement is not a secondary effect of some i.i.d. performance improvement (i.e. the o.o.d. performance gaps in o.o.d. Figure 1 do not come from i.i.d. overfitting/underfitting.).” In general, one wishes to retain good IID performance while also improving upon OOD numbers. On balance, might a practitioner prefer one of the baselines?

Minor:

L150-L153 says: `We focus on residual networks because fine-tuning has been found to hardly change the inner layers of non-residual networks (Raghu et al., 2019, fig 2). In contrast, skip connections in residual networks expose the inner block features in such a manner that the fine-tuning process can utilize these features in a near-linear way (Evci et al., 2022).` The first citation seems to be about MAML, which is a specific setting and likely does not extend to all fine-tuning settings. The point in that work seems to be more about what meta-learning does in terms of feature reuse and does not make generic observations about fine-tuning in non-residual networks. The second citation doesn’t seem to make any claims about the usefulness of intermediate features being specific to models using skip connections. ResNets and ViTs are top classifiers currently, so it might not be necessary to motivate the choice of models here anyway.

L319-L321 says `When the fine-tuning dataset size approaches the pre-training dataset size, the difference between fine-tuning and training from scratch becomes less clear, the linear connectivity property disappears, the linear approximation perspective on fine-tuning no longer holds, and the optimal dropout rate falls sharply.` Has it been demonstrated in prior work that the linear connectivity property disappears when the dataset sizes get close (i.e. is there a citation for this claim)?

L447 says `Despite all this technology, advanced fine-tuning of a pretrained RESNET #1 (2nd column) barely matches the performance of naive fine-tuning on RESNET #2 (3rd column).` Just a nit, but usually one does not say “A barely matches B” when A > B.

Typos:

L129: “setup is a commonly used” —> drop “a”

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work the authors make one simple observation: when fine-tuning in o.o.d. setups, using a very high dropout can yield surprisingly good performance. The evaluation is performed on popular downstream datasets and common architectures.

### Strengths
- The quantitative evaluation (for obtaining the main results) is quite comprehensive.
- The message is delivered clearly.
- The empirical result is quite surprising.

### Weaknesses
 - There is a gap from the expected theory. In the limit of large sampling, there should not be any difference in terms of performance when varying the dropout probability (a-priori, large dropout should make convergence harder, when untouching the learning rate). The empirical observation in the specific setup chosen is interesting, but right now, considering it is the only contribution, it is felt there is a lack of grounding to allow practitioners to employ this solution without running an extensive grid search. Specifically, the paper does not sufficiently explore the interaction between dropout rate and other hyperparameters, such as learning rate and batch size, which could significantly impact the observed performance gains. The lack of theoretical justification makes it difficult to predict when and why this high dropout approach will work, limiting its practical applicability without extensive experimentation.
- It seems that there is a lot of engineered choices related to learning rate scaling at layer's scale, dropout etc. The paper lacks a clear explanation of how these choices were made and their impact on the results. The specific learning rate scaling method used is not justified, and it's unclear whether the observed benefits are specific to this particular scaling or a more general phenomenon. The interaction between the learning rate scaling and the high dropout is not well understood, and it is possible that the results are highly sensitive to this specific configuration.
- Some statements are overly (and maybe, unnecessarily) strong. For example, "It is impossible today to pretend that the practice of machine learning is compatible with the idea that training and testing data follow the same distribution": there are many cases in which inference happens in distribution. While the point about OOD generalization is valid, the statement is too broad and does not acknowledge the many real-world scenarios where in-distribution testing is the norm.

### Questions
- How is the proposed idea performing on more efficient architectures, like MobileNet?
- Is the same approach valid for non CV-based tasks, like NLP? It is felt the high dropout is successful where architectures are notoriously over-parametrized (as it is for CV).
- How are the learning hyper-parameters found? Has a validation set been used?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
To improve the ensembling performance of weight averaging, the paper proposes to employ a large dropout rate at the penultimate layer to obtain rich representations with better OOD performance.

### Strengths
1. The training scheme of a large dropout is interesting.
2. The proposed large dropout obtains superior performance than previous methods.

### Weaknesses
1. The main problem of the paper does not provide a deep analysis of why large dropout is helpful. It simply provides some comparing experiments to demonstrate its effectiveness. The authors should provide a formal definition of the achieved "richer representation" (i.e., quantitative comparisons). Also, some visualizations also can be provided for a better analysis.
2. Since the experiments of the proposed method are conducted on the DomainBed, comparing them to the existing methods is also required.
3. The deep analysis of different behaviors of Weight Averaging, Deep Ensemble, and the proposed method on the ID and OOD performance is required for Figure 7.
4. Why not adopt the large dropout in the deeper layers?
5. The number of ensembling members is provided (1296? which seems too large for the practice). The influence of the number should also be considered.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The current manuscript challenges the traditional assumption that training and testing data share the same distribution, which is increasingly unrealistic in real-world applications. To handle diverse data distributions, recent work has used ensemble methods to create richer, more robust representations than those optimized for single-distribution performance. Instead, the authors propose fine-tuning large pre-trained models with large dropout rates, achieving better performance on OOD tasks. They compare the effective of their method with ensembles and weight-averaging methods.

### Strengths
This paper argues that the traditional assumption in ml—that training and testing data come from the same distribution—is no longer realistic. To handle real-world scenarios involving multiple, shifting data distributions, recent studies have highlighted the need for representations that are "richer" than those optimized for single-distribution performance.  and they suggest fine-tuning a large trained model via large dropout rates.

### Weaknesses
 **w1: novelty**: my major concern is the limited novelty of the proposed approach, as it closely resembles existing methods without introducing substantial new concepts or techniques.

**w2:limited experiments and results:** even the experimental setup is minimal, with limited datasets and benchmarks, which weakens the generalizability and impact of the findings. Expanding the experiments to include a broader range of datasets and baselines would strengthen the evaluation.

**w3:Lack of theoretical discussion:** the paper lacks a theoretical foundation or in-depth discussion that could clarify the underlying mechanisms or justify the observed empirical results.

### Questions
Please see the above weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
1
