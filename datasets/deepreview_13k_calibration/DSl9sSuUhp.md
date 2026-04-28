# Attic: A New Architecture for Tabular In-Context Learning Transformers

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Tabular In-Context Learning (ICL) transformers, such as TabPFN and TabForestPFN, have shown strong performance on tabular classification tasks. In this paper, we introduce Attic, a new architecture for ICL-transformers. Unlike TabPFN and TabForestPFN, where one token represents all features of one observation, Attic assigns one token to each feature of every observation. This simple architectural change results in a significant performance boost. As a result, we can confidently say that neural networks outperform tree-based methods like XGBoost.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Attic, a novel transformer architecture for tabular in-context learning that uses cell tokens instead of observation tokens. The work demonstrates significant empirical improvements over existing methods and makes a meaningful contribution to the field.

### Strengths
* The architectural modification from observation tokens to cell tokens is simple yet effective, showing substantial performance gains across multiple benchmarks
* Thorough empirical evaluation on two major benchmarks (WhyTrees and TabZilla) with comprehensive comparisons against state-of-the-art methods
* Technical contribution backed by clear motivation and intuitive explanations for why cell tokens may work better than observation tokens
* Impressive results showing Attic outperforming tree-based methods and ensemble approaches like AutoGluon on several datasets
* Detailed ablation studies and analysis of computational requirements and decision boundaries

### Weaknesses
1. Limited theoretical analysis or formal justification for why cell tokens perform better.
2. The authors note that Attic is significantly slower and more memory-intensive than TabForestPFN for datasets with many features. This scalability issue could limit Attic's practical applicability to large, high-dimensional datasets.
3. Mixed precision training issues are not fully resolved, with float16 training instability remaining unexplained.
4. Initial regression results feel preliminary and could be expanded. 
5. More detailed analysis of failure cases where tree-based methods outperform Attic. Why, in datasets with less than 500 observations, does Attic underperform?
6. The paper does not thoroughly explore potential limitations or failure cases of Attic, which would provide a more balanced view of the method's capabilities.

### Questions
1. Any potential approaches to reduce memory and computational requirements of Attic?
2. How does Attic handle missing data or categorical variables? Are there any special preprocessing steps required?
3. Can you elaborate on Attic's performance in regression tasks compared to classification?

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
The authors propose a new tabular in-context learning algorithm. They introduce a new dimension in the model input by modeling each feature as one token rather than each sample. This allows for feature order invariance at the cost of extra computation. The proposed model, ATTIC, makes substantial performance gains.

### Strengths
- The experimental results of the method is really exciting. As someone very familiar with the baselines, ATTIC seems to address a major performance bottleneck in tabular in-context learning.

- The authors provide an simple intuitive approach, encode each feature seperately to overcome feature order invariance instead of using ensembling, which provides large performance improvements.

- The authors provide results on several hard benchmarks and achieve performance with no hyperparameter tuning. The decision boundaries results provide further evidence for ATTIC's efficacy.

- The authors provide a detailed comparison of Attic compared to TabForestPFN for easy reproducibility.

### Weaknesses
Overall, I think some more in-depth analysis into the runtime and memory tradeoffs Attic makes to achieve its superior performance can greatly benefit the paper.

- Because Attic introduces a new dimension over the feature counts, I imagine the runtime costs greatly increase. How much does this increase with respect to the number of features?

- Similar to the previous question. How does the memory costs of Attic rise with respect tothe number of features?

- My understanding is TabPFN overcomes feature order invariance through ensembling across multiple feature shufflings. Could you discuss the tradeoff between using larger TabPFN ensembles and Attic, as both incur additional runtime costs?

- Intuitively, I feel larger feature count datasets would benefit the most from Attic. Empirically, are there trends on what specific datasets Attic most improves upon baseline algorithms?

### Questions
See Weaknesses.

Will you open-source your code?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper is on in context learning (ICL) for tabular prediction problems.
Essentially the complete tabular training data is placed in context and predictions are performed on test data. The main difference to existing work is that in the proposed approach each cell value is represented individually as compared to an entire row.
The approach is evaluated on both classification and regression problems and compared to existing ICL approaches as well as standard ML models such as gradient boosted trees.

### Strengths
In theory the idea of representing feature values individually seems very reasonable to me since it is allows a richer representation of the data. They also show that extending the existing architectures (TabPFN/TabForestPFN) accordingly can be performed pretty smoothly (Figure 1). 

The evaluation is performed on more than 100 benchmarks and the authors consider both classification and regression problems.

The performance on classification problems (see Table 2 and Table3) seems to outperform a wide range of existing approaches.

Section 4.6 and 4.7 provide interesting insights into the decision boundaries obtained by the proposed models as well as some indication on which kind of benchmarks the approach does not work so well.

### Weaknesses
First, to me there are the following limitations of the proposed approach:
1. Representing each value is sensible, but it does come at a substantial computational cost. The growth is in the number of columns and there are data sets with more than a thousand columns. Now, one can argue that for the ICL setting there will always be limitations (e.g., 1 billion rows and 1k columns is unlikely to happen). However, when looking at Table 2 TabForestPFN is only marginally worse than Attic (ZeroShot) but much more cost effective due to the more abstract representation. 
2. On regression tasks (Figure 6) the performance is by far not as good. And that is actually interesting and not necessarily something negative about this approach. While in theory classification and regression are the same, it does seem to pose issues especially for DL approaches in general and not just the approach presented here.


Moreover, there are some points in the paper that are unclear to me.
For instance, in Section 4.2 it states that 94 out of 176 benchmarks are used from TabZilla.
One question is how those were selected, but to me the more important question is how they are split up into classification and regression tasks (this is explained for the WhyTrees benchmarks but not TabZilla).
Looking at Table 2, it seems that there only 28 classification tasks.This number of benchmarks weakens the results in my opinion - especially given that on regression it is known not to work as well.

In terms of hyper-parameter optimization - what was the experimental setup? For instance, was there a split of train/validation to perform  HPO and then the evaluation on test? To me this is not stated clearly in the paper.
One could also pick a bit more sophisticated HPO approach (e.g., https://github.com/hyperopt/hyperopt-sklearn ), but at least random search is used (and not grid search).

At the end of Section 3 it is stated: "We believe that this dependency on feature order leads to training inefficiencies. The cell-token
ICL-transformer treats each feature the same and learns how to construct relationships between features." 
And while I agree with this intuition, why not perform an ablation study on it (e.g., shuffling columns and see if it impacts the performance)?

Similarly, it would be useful to try to explain the results in Table 3 a bit more - is it that the model needs the fine-tuning to embed the categorical values appropriately? The gap between fine-tuned and zero-shot is very large and it would be great to understand the reason for it better.

### Questions
In addition to the above questions:

Is it possible to show if the differences in performances shown in Table 2 are statistically significant?

Figure 4 is interesting - but isn't it the case that as the decision boundaries become more and more detailed, the generalization capability of the approach is reduced at the same time?

In terms of computational complexity is there a way to show computational cost (e.g., as a new column in Table 2)?
The question here is of course what the metric in this context could be - maybe the combination of runtime/memory usage/GPU requirement (for GPU use: number of input/output tokens) would already be insightful.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Traditional ICL transformers like TabPFN and TabForestPFN use observation tokens, which can be influenced by the order of these features. To overcome these challenges, this paper introduces Attic, which employs cell tokens to represent individual observations x features, allowing the model to handle features without being affected by their order. As a result, the authors claim that Attic significantly outperforms traditional methods like XGBoost, CatBoost, and TabPFN in benchmark tests from WhyTables and Tabzilla. These findings suggest that Attic is a strong candidate, given its superior accuracy on various datasets.

### Strengths
- The motivation is clear and well-founded. I like the idea of removing the feature order importance that is placed on classic ICL transformers. This is a nice thing to focus on and is a strength of this paper. 
- I appreciate the author’s writing style and delivery of the material. The paper reads well and the authors provide a nice, logical flow for their arguments. (See below for some suggestions for additional details which will improve the paper even more!)
- The authors’ results are promising and they certainly show their motivation and technical solution (observation x feature tokens) is a promising research direction!
- Evaluating their method against existing benchmarks (Tabzilla and WhyTables) is a very important and necessary step for any new method in the tabular data space. I appreciate the authors' care and consideration here.

### Weaknesses
 - More details are needed throughout the paper. For example, can the authors provide values instead of variables for architecture details: 
    - Token dictionary size, what is the value of $L$, dimension sizes, what values of $k$ did you test?etc
    - How is the tokenization performed for each observation x feature?
    - What are the model sizes for the -M and -L versions of TabForestPFN?
- You claim in L153: “We changed this because we believe this formulation is more natural, but performance-wise, it has little impact.” Please provide an ablation describing and proving this claim. 
- The authors need to highlight more clearly for the reader that this work and its findings are limited to datasets with 10 or fewer classes. 
- Do the authors re-run TabPFN for the Tabzilla benchmark? or do they take the TabPFN results from the Tabzilla paper/results?
- What model is being reported in Tables 6 and 7 for TabForestPFN when you describe at least 3 different versions you use in your main paper? This actually is an important question/distinction the authors need to make through the paper. It is very hard to evaluate the paper without knowing this since the 3 versions of TabForestPFN are so different and the evaluation of the paper rests on understanding which version is being discussed in each results section. With further clarity, I’ll be able to update my score accordingly. 
- Can the authors confirm the train/val/test splits they use are consistent with what the authors used in WhyTress and Tabzilla? My concern here is that tabular data use cases are not limited in the ways the authors may have selected their subset of Tabzilla. Tabzilla, which quickly has become a gold-standard benchmark in tabular data evaluations, is vast and captures a lot of nuance in the tabular community and use cases. I’m concerned the author’s down-selecting is increasing hiding some flaws of the approach. 
- Can the authors please describe why they omit about half of the Tabzilla benchmark? 
- Can the authors provide details on the computation resources? They provide comparisons to TabForestPFN primarily, but they should also provide comparisons to TabPFN and CatBoost at least — preferably more. Computational complexity is one of the main downsides of this approach, so the authors need to provide more care here for us to evaluate the work appropriately.



### Questions
See Weaknesses. I am certain that with satisfying clarifications on the questions above, I will happily raise my score.

Also, a minor typos:
- L221: “Additionally, pretraining Attic on smaller datasets than TabForestPFN favors TabForestPFN”. This typo makes the entirely of the paragraph of L219 hard to comprehend.

### Soundness
3

### Presentation
3

### Contribution
3
