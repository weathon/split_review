# From Uncontextualized Embeddings to Marginal Feature Effects: Incorporating Intelligibility into Tabular Transformer Networks

- Decision: Reject
- Scores: 5, 8, 5, 3

## Abstract
In recent years, deep neural networks have showcased their predictive power across a variety of tasks. The transformer architecture, originally developed for natural language processing, has also shown great efficiency in handling tabular data, offering a competitive alternative to traditional gradient-boosted decision trees in this domain. However, this predictive power comes at the cost of intelligibility: Marginal feature effects are almost completely lost in the black-box nature of deep tabular transformer networks. Alternative architectures that use the additivity constraints of classical statistical regression models can maintain intelligible marginal feature effects, but often fall short in predictive power compared to their more complex counterparts.   To bridge the gap between intelligibility and performance, we propose an adaptation of tabular transformer networks designed to identify marginal feature effects. We provide theoretical justifications that marginal feature effects can be accurately identified, and our ablation study demonstrates that the proposed model efficiently detects these effects, even amidst complex feature interactions. To demonstrate the model's predictive capabilities, we compare it to several interpretable as well as black-box models and find that it can match black-box performances while maintaining intelligibility. The source code is vailable at https://anonymous.4open.science/r/nmfrmr-B086.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
I do not feel qualified to review this paper as I do not have any experience with tabular machine learning. I would like to ask the ACs to seek an opinion from different reviewers.

### Strengths
n/a

### Weaknesses
 - Discussion of related works is lacking. There is no separate related works section, just some context provided in the introduction, and while a decent selection of related papers are cited, there's little discussion of how the proposed method relates to and differs from existing work. One point I would like to see addressed is whether and how this method improves on methods like integrated gradients, LIME, or SHAP that produce per-feature explanations without requiring model modifications.

- Some theoretical results are given in Section 2.1, but it's not described how the results relate back to the interpretability of the model, and there are some particular issues I wanted to raise:
	- The definition given for $R_{\tilde{w}_{-k}}$ at line number 279 doesn't make sense to me - it could even take the opposite sign of the overall risk \(R\) if the model has a greater loss with just feature $k$ than on average.
	- Equation (7) depends on the assumption that the risk for each single-feature dropout vector is the same and equal to $R(1-p(\tilde{w}_k))$, which seems very unlikely for realistic models or datasets where features have different importances and the model tends to perform better given more features. So I don't see the relevance of this result.
	- My interpretation of the section is that when training with dropout, the performance of individual feature predictors is in some sense bounded by the overall model performance. This makes sense, but it's not clear to me if this indicates anything about the interpretability of the model in terms of the individual feature predictors or what their predictions represent (i.e., do they actually optimize the loss with respect to $\mathbb{E}_{y|x_k}[y|x_k]$, or just something that's not too far from it?).

- Even under the proposed approach, the transformer component itself is somewhat of a black box. This could be tolerable given the improved interpretability of the overall model, but it is a limitation.
	- While thinking through the method, I kept coming back to what the optimal behaviour learned by the transformer and shallow predictors would be. I think it is true that the optimal behaviour at low dropout rates is at least approximately for the transformer to only predict joint effects plus marginal effects that are too complex for the shallow predictors to learn, rather than learning all joint and marginal effects. A proof of this would be useful if possible though.

### Questions
n/a

### Soundness
2

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
This paper proposes a modification to predictive tabular transformer models to make them more interpretable: producing the final output as a sum of the transformer output along with shallow univariate models for each input feature. Dropout is used to encourage the model to optimize its use of each feature independently. The univariate models can then be interpreted as indicating the marginal effect of each feature on the overall output.

### Strengths
- In general, the proposed method makes sense to me and I could see it being used in practice. I've worked with tabular transformers in applied settings and can attest that understandable per-feature explanations are difficult to achieve. This method makes sense to me as a way to get greater interpretability while retaining the performance of tabular transformers, or other deep tabular models.
- As far as I can tell the proposed method is original. It resembles NATT (Thielmann et al. 2024), but I think the design differences are significant in practice and make sense. This method passes all features to the transformer as input, then uses dropout during training to guide the model to a desired behaviour that makes all features interpretable, whereas NATT keeps numeric and categorical features separate and only provides a comparable level of interpretability for numeric features.
- Experimental results are fairly convincing in showing that the proposed method doesn't sacrifice performance.

### Weaknesses
After reading the paper, I still have some questions.
1. In section 2, the encoding of numerical features involves the threshold $b_t$, and the thresholds are from the decision trees. So I wonder how we get these decision trees? Is the marginal effects of the model the same as those decision trees? And what about the performance compared with the decision trees.
2. The method seems too trivial to achieve the expected performance. Only a Linear and dropout can identify the marginal and even enhance the performance.
3. In tabular domain, it seems that 8 datasets in all are not sufficient. This may result in doubt that the datasets used are selected for this task.

In addition to the above questions, I think there are some problems with typography and content。
1. It will be better if there is a section which introduces the related work, e.g. transformers in tabualr, marginal feature effects in tabular or other domains, etc. I think this will help reader better understand the task and your method.
2. It seems that in section Abstract, there is some problem with the spacing between lines.

### Questions
- Could you please clarify the results in Section 2.1, especially how to interpret them with respect to interpretability?
- In practice, how can we be confident that the feature networks have the capacity to fully capture marginal effects? If they can't fully capture them, then part of the marginal effect could be learned by the transformer instead.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work proposed an adaptation of tabular transformer networks designed to identify marginal feature effects, while maintaining the capability of prediction performance at the original level.

### Strengths
From my prospective, the strengths of this paper are as follows:
- Compared to FT-Transformer or GAM, the proposed NAMformer has more interpretability and stronger predictive power, respectively
- There are analysis between contextual and uncontextual embeddings, proving that the uncontextual embedding can represent the original feature
- There are a lot of formula providing theoretical support

### Weaknesses
 - The introduction and methodology sections could benefit significantly from writing improvements and more thorough explanation. In its current form, these sections assume a lot in terms of prior knowledge, e.g. of marginal feature effects, the FT-Transformer architecture, target-aware embeddings, and uncontextualized embeddings. These should be explained, at least at a high-level. Additionally, from Section 2, it is somewhat unclear which parts are inherited from the prior work on FT-Transformer and which parts are new. Particularly, I was confused about the feature encoding part--without referencing the prior work, I cannot easily assess if this part of the work is novel. 
- The authors should include specific use-cases in which the marginal feature effects are useful downstream. Otherwise, it is challenging to assess the significance of the contribution. 
- The paper should have a standalone explanation of the datasets that are being used in evaluation beyond saying that the evaluation is done on four regression and four binary classification datasets---what are these datasets and where do they come from? The authors seem to refer the reader to the appendix for this information, but this is critical for assessing the results. Furthermore, the evaluation should be more thorough than regression and binary classification -- conceivably, the proposed method could become worse than FT-Transformer as the number of classes grows. The authors should include such tasks.

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

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
This work proposes a modification to one of the tabular transformer architectures that enables features to be interpretable. Specifically, the technique proposed in this work, NAMformer, which is built on top of the existing FT-Transformer, enables the identification of "marginal feature effects" which can be used to interpret the final model. NAMformer performs comparably to the original FT-Transformer, while maintaining desirable interpretability properties.

### Strengths
- The claim that the proposed NAMformer is not worse than FT-Transformer in terms of prediction performance seem true on the tasks that were used in the evaluation. 
- The general idea of making tabular transformer architectures interpretable seems like it should be useful for a variety of problems. 
- The inclusion of synthetic evaluations and ablations are useful for understanding the mechanics of the proposed approach.

### Weaknesses
- The introduction and methodology sections could benefit significantly from writing improvements and more thorough explanation. In its current form, these sections assume a lot in terms of prior knowledge, e.g. of marginal feature effects, the FT-Transformer architecture, target-aware embeddings, and uncontextualized embeddings. These should be explained, at least at a high-level. Additionally, from Section 2, it is somewhat unclear which parts are inherited from the prior work on FT-Transformer and which parts are new. Particularly, I was confused about the feature encoding part--without referencing the prior work, I cannot easily assess if this part of the work is novel. 
- The authors should include specific use-cases in which the marginal feature effects are useful downstream. Otherwise, it is challenging to assess the significance of the contribution. 
- The paper should have a standalone explanation of the datasets that are being used in evaluation beyond saying that the evaluation is done on four regression and four binary classification datasets---what are these datasets and where do they come from? The authors seem to refer the reader to the appendix for this information, but this is critical for assessing the results. Furthermore, the evaluation should be more thorough than regression and binary classification -- conceivably, the proposed method could become worse than FT-Transformer as the number of classes grows. The authors should include such tasks.

### Questions
- What are uncontextualized embeddings? As far as I can tell, this is never explained in the paper. 
- What does token identifiability mean? This is also not defined.

### Soundness
2

### Presentation
1

### Contribution
2
