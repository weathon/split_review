# Stable Anisotropic Regularization

- Decision: Accept
- Scores: 8, 8, 3

## Abstract
Given the success of Large Language Models (LLMs), there has been considerable interest in studying the properties of model activations. The literature overwhelmingly agrees that LLM representations are dominated by a few ``outlier dimensions'' with exceedingly high variance and magnitude. Several studies in Natural Language Processing (NLP) have sought to mitigate the impact of such outlier dimensions and force LLMs to be isotropic (i.e., have uniform variance across all dimensions in embedding space). Isotropy is thought to be a desirable property for LLMs that improves model performance and more closely aligns textual representations with human intuition. However, many claims regarding isotropy in NLP have been based on the average cosine similarity of embeddings, which has recently been shown to be a flawed measure of isotropy. In this paper, we propose I-STAR: IsoScore$^{\star}$-based STable Anisotropic Regularization, a novel regularization method that can increase or decrease levels of isotropy in embedding space during training. I-STAR uses IsoScore$^{\star}$, the first accurate measure of isotropy that is both differentiable and stable on mini-batch computations. In contrast to several previous works, we find that \textit{decreasing} isotropy in contextualized embeddings improves performance on most tasks and models considered in this paper.git}}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study investigates the connection between isotropy and model performance by employing 3 distinct LLMs and 9 fine-tuning tasks. It introduces I-STAR, a method for adjusting model isotropy based on a novel differentiable metric called IsoScore*.

Surprisingly, the study's findings contradict the prevailing notion in NLP literature. That is, it demonstrates experimentally that discouraging isotropy leads to better performance across the different models and downstream tasks.

### Strengths
This paper challenges the dominant belief in NLP literature showing that anisotropy is beneficial. Its findings have the potential to significantly influence future research directions in the field.

It also introduces new way to compute the Isotropy in models. The authors conducted a set of experiments to show its efficiency comparing it to CosReg.

### Weaknesses
If we see a trend in Figure 3 on how higher IsoScore* leads to lower accuracy, some correlation and significance score should be added to support this claim.

### Questions
Could you add in the Appendix the same experiments done in Figure 3 but for CosReg and also the same in Figure 4 but for IsoScore*? This will give a better intuition of how these 2 different methods work.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This submission proposes a new method for measuring isotropy in neural models, improving over previous proposals and leading to a new regularization technique I-STAR. They show that LLMs actually seem to benefit from less isotropic internal representations, contrary to previous claims in the NLP literature.

### Strengths
The paper is well written and clear. The proposed improvement of IsoScore into IsoScore* is fairly straightforward. The fact that it is a more accurate and more convenient estimate of isotropy in LLMs is argued very well and supported by some empirical results.

The paper convincingly argues that isotropy and its impact on performance are not properly understood in NLP, which is a very significant contribution.

Experimental results mostly support the arguments in the paper (more comments below).

### Weaknesses
* There is no significance testing on the results (Table 1) but there are error bars (good!) — these seem to indicate that most differences outlined are hardly significant (e.g. RTE, 72.56+/-1.29 vs 71.34+/-0.91). This makes it difficult to get a clear picture of the resulting effect of decreasing isotropy.
* Similarly Fig. 3 is difficult to interpret — there are clear decreasing trends in some plots, not so much in most of them.

### Questions
* p.4: Presumably all norms in steps 6 and 7 of Algorithm 1 are 2-norms?
* p.4: Is RDA "regularized discriminant analysis"? It is only introduced on p.5.
* p.4: As \Sigma_S is computed from a large number of tokens and re-estimated after each epoch, this is presumably quite costly computationally. Could you comment on that? As you are computing these anyway, why not use that directly to estimate isotropy? This would essentially correspond to \zeta=1, which is not tested here as far as I can tell.
* p.6: "Section F" -- do you mean Section D?
* p.7: I do not clearly see Fig. 4 as supporting the claim that CosReg only alters the mean of activations (all means seem to be ~zero on the plots, with one outlier). Maybe a plot of the distribution would support this claim better?
* p.9: Why are -1 and +1 lambdas excluded from Fig. 5? -1 seems the most popular choice in Fig. 2.
* Regularization to a manifold in parameter space is well studied in Machine Learning, and indeed supports the argument that anisotropy may benefit performance. This is also linked to the idea that there is the level of representativity in the model that must match the intrinsic dimension or complexity in the data. Fig. 5 actually seems to show roughly consistent intrinsic dimensions for the three models used here. Is there a way you could put this in perspective with e.g. model size? Showing for exemple how anisotropy favors a roughly stable internal dimensionality in parameter space as model size increases?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors improved upon IsoScore, a measure for the isotropy of point clouds (Findings of ACL'22), and proposed the IsoScore* as a measure of **an**isotropy. IsoScore* employs PCA (as a natural method for estimating the covariance matrix) and utilizes shrinkage estimation, making it a differentiable measure that operates robustly even with small data sizes. In experiments, IsoScore* was used as a regularization term when fine-tuning masked language models. As a result, under optimal hyperparameters, performance improvements were observed across multiple downstream tasks.

### Strengths
- In the NLP field, the isotropy of internal representations was believed to be the key to model success. The message of this paper, suggesting that the **an**isotropy of internal representations might be the key to performance improvement, will likely resonate intriguingly with many readers.
- The paper comprehensively covers a collection of works related to the isotropy of NLP models, making it a highly self-contained piece for readers.

### Weaknesses
### 1. The reasons for contradictions with prior research are unclear, weakening the persuasiveness of the main claim.
The authors' main claim that "**an**isotropy is the key to model performance improvement" isn't reconciled with prior research which posits that "isotropy is the key to model performance improvement". While the authors suggest that the discrepancy arises from the evaluation metrics used (as stated “previous studies have made claims using “flawed” measures of isotropy,” on page 7), both this work and prior studies differ *not* only in metrics but also in tasks (GLUE tasks vs. word similarity tasks). Therefore, it's not an apple-to-apple comparison. If there's an inverse correlation between anisotropy and performance in word similarity tasks, it becomes challenging to coherently explain the overall results. This issue might possibly be resolved if there were experiments or comprehensive discussions specifically for the word similarity tasks.

### 2. The claim that the proposed method improves performance on downstream tasks seems a bit overstretched.
Even when choosing the best settings across multiple hyperparameters, the performance improvement is modest (as seen in Table 1). Moreover, performance can deteriorate compared to the baseline depending on hyperparameter choices (as shown in Figure 3). Furthermore, adopting the proposed method incurs an additional cost of hyperparameter selection. Therefore, for practitioners aiming to employ IsoScore* for their problems, it's hard to advocate for the use of the proposed method. Of course, submissions to ICLR shouldn't be evaluated solely on empirical performance. However, in this paper, improving performance on downstream tasks is one of the main contributions; thus the lack of compelling experimental results will inevitably impact the paper's peer-review evaluation.

### Questions
- If anisotropy is a natural consequence of SDG, what is the significance of deliberately adding anisotropy as a regularization term? The computational cost increases slightly, and the disadvantage of increased hyperparameter tuning cost needs to be offset by some substantial benefits. If there are such advantages, the appeal of the proposed method would be enhanced.
- What is the significance of adjusting the hyperparameter $\zeta$ for shrinkage estimation when using IsoScore* as a regularization term? Even if the value of IsoScore is estimated to be on the lower side (Figure 2), if the estimated value has a monotonic relationship with the true value, wouldn't there be no issue in regularization? If the goal is to ensure differentiability, couldn't we just fix it at an appropriate value?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
