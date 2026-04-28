# DEPT: Decoupled Embeddings for Pre-training Language Models

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8

## Abstract
Language model pre-training benefits from diverse data to enhance performance across domains and languages. However, training on such heterogeneous corpora requires extensive and costly efforts. Since these data sources vary lexically, syntactically, and semantically, they cause \textit{negative interference} or the ``\textit{curse of multilinguality}''.  We propose a novel pre-training framework to alleviate this curse. Our method, \dept, decouples embeddings from the transformer body while simultaneously training the latter in multiple contexts. \dept enable training without a shared global vocabulary and: (1) can train robustly and effectively under significant data heterogeneity, (2) reduces token embedding parameters by up to \textbf{80\%} and the communication costs by $\mathbf{675 \times}$ for billion-scale models, (3) enhances model generalization and plasticity in adapting to new languages and domains, and (4) permits training with custom optimized vocabularies per data source. We demonstrate \dept's potential via the first vocabulary-agnostic federated multilingual pre-training of a $\mathbf{1.3}$ \textbf{billion}-parameter model, limiting its embedding size to $\mathbf{102.4}$ million instead of $\mathbf{512}$ million.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce the method DEPT, “Decoupled Embeddings for Pre-trained Language models,” an algorithm that trains a transformer model on heterogeneous datasets such as domains or languages individually and subsequently aggregates the parameters by averaging them. They introduce three variants where increasingly less embedding information is shared. DEPT achieves lower perplexity than baselines.

### Strengths
1. The authors tackle an important problem. The usage of data mixtures during pre-training is not well understood but is an essential part of modern foundation models.
2. While the idea of using model averaging after an inner loop of training on dedicated subsets of data is not particularly novel, it might have a big impact on pre-training, given the encouraging results.

### Weaknesses
1. Writing can be improved or misses important information. For example, for the experimental setup, I struggle to understand L205-311, and information on software/hardware, such as how many FLOPS  or hours training took, is missing.
2. Some claims are overstated: M-T outperforms DEPT in 5/11 datasets in Table 2. I am not convinced that Trim and Glob perform identically (L377).
3. An important additional baseline would be models trained on individual data sets. This would give insights into the advantages/disadvantages of model averaging.

### Questions
1. How would the model DEPT-SPEC be used for inference? Would there first be a need to determine the used domain / language as tokenizers are separate (L129)?
2. The GLOB model seems to work best. Is there any hypothesis why this is the case? What is the implication of this fact?
3. The mentioned “Performance metrics” in all captions is always perplexity?
4. Based on which estimation is communication cost 675x lower?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this work, the authors propose to train Language Models with multiple independent tokenizer and language modeling heads (one per language or data source) but with a single Transformer backbone. One touted advantage of this approach is that each source can train on its own GPU node, with a reduced need for cross-node communications (since a significant share of the weights does not need to be replicated across them). Another touted advantage is that forcing one model to work with multiple tokenization schemes makes the model more adaptable to new languages and domains post-training, similar to how "embedding reinitialization during the training" was found to have a similar effect (at a cost that however did not warrant its use when training large models, unlike the proposed methodology that does not requiring wasting training cycles).

### Strengths
- The setup proposed in this paper looks very satisfying, and it seems to solve several problems both in the industry and in research labs.
- The value proposition seems clear to me.
- The deployed methodology appears novel.
- The literature research looks satisfactory to me, given the scope of the paper.

### Weaknesses
 - The paper's form is well below the required writing standards. To address this, I'd suggest specific improvements, such as:
  - Standardizing method names throughout the paper and tables (SPED vs SPEC, GlOB vs GLOB vs Glob, ...)
  - Clearly defining the performance metrics used and specifying explicitly whether lower or higher values are better
  - Adding a reference to Table 1 in the main text
  - Improving table readability by adding summary statistics (averages...), using bold or color highlighting, or splitting into multiple tables (moving some languages to an Appendix).
- Not enough arguments are brought forward to justify the issue with diverging models during training. I have myself never experienced this phenomenon in similar setups. As such, it's difficult to rule out that it might be the result of bugs in the training code or poor hyperparameter choices, rather a general phenomenon. 
  - A better description of the exact training methodology and the hyperparameter search would help alleviate concerns, here.
  - An ablation study or an explanatory paragraph isolating factors that contribute to divergence would also help.
- The lack of comparisons with baselines not trained by the authors is worrying. 
  - I would prefer for external baselines to be added, even if some added context is necessary to explain away unfair comparisons (could be an appendix).
- Without devising a clear methodology to perform inference on SPEC-type models, the paper feels a bit incomplete. 
  - I'd suggest to the authors to briefly outline a proposed inference methodology for SPEC models, and to discuss the challenges and potential approaches for inference with these models in more detail.

### Questions
- [addressed] Is there any comparable experiment whose results you can compare your models against?
- [addressed] How did you perform hyperparameter search?
- [addressed] Did you perform scaling experiments?

[addressed] More than answering questions, I expect the authors to do a significant effort during the rebuttal to improve the paper's form. I would downgrade my rating if this does not happen. (I prefer to give authors a chance to amend, because I think the paper is otherwise interesting if you can get past the shortcomings of the writing.)

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a pre-training framework DEPT which allows the model to train without being bound to a shared global vocabulary. Three variants are introduced: Glob, Trim, and Spec. Although each pipeline has the same setting for the transformer block, the difference lies in how they deal with the embeddings. Among the three, Glob is close to the standard pre-training: a single global embedding matrix is used. Trim keeps a local embedding matrix for each data source, and each token in the matrix is also contained in the global vocabulary. With the federated learning framework, the updates of a specific token are then aggregated to the same token in the global embedding matrix. Spec is a fully decoupled version where there is a non-sharing local embedding matrix for each data source. The authors evaluate the DEPT by investigating the efficiency, generalization as well as plasticity.

### Strengths
- The paper is well-written and easy to follow.

- The idea of decoupling embedding matrix and transformer block in pre-training within the federated learning framework is novel.

- The authors answer the raised research questions with meaningful and extensive experiments.

- The results generally confirm that DEPT can improve the generalization and plasticity of the models.

### Weaknesses
 - The data sources are not always clear given a dataset. The proposed pipeline only works if the domains are known. Otherwise, some manual or automatic clustering has to be used to create different sets of data.

- The multi-domain data is almost only in English. But for the multilingual data, the data of each language should also contain various domains. Therefore there are confounding variables. A natural question would be whether the model can generalize to the same domains across different languages.

- No downstream tasks in natural language understanding or generation are evaluated on the resulting models. But such further evaluation is important.

- abstract: I believe "negative interference" and "curse of multilingual" are not parallel concepts. Curse of multilingual is a special type of interference because of the training data containing many languages. 

- I don't find the authors clearly stating the "performance metrics" in Tables 1, 2, 3, 4.

- The authors are suggested to have aggregated statistics for Tables 1, 2, 3, and 4 (e.g., average) so that the authors can have a better understanding of which model generally performs the best. Additionally, the authors can bold the best number in each column.

- line 278: 50,257 instead of 50257.0

- Line 341 (b) tn the ?

### Questions
- abstract: I believe "negative interference" and "curse of multilingual" are not parallel concepts. Curse of multilingual is a special type of interference because of the training data containing many languages. 

- I don't find the authors clearly stating the "performance metrics" in Tables 1, 2, 3, 4.

- The authors are suggested to have aggregated statistics for Tables 1, 2, 3, and 4 (e.g., average) so that the authors can have a better understanding of which model generally performs the best. Additionally, the authors can bold the best number in each column.

- line 278: 50,257 instead of 50257.0

- Line 341 (b) tn the ?

### Soundness
3

### Presentation
3

### Contribution
4
