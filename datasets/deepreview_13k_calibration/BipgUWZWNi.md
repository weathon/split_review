# Controlling Information Leakage in Concept Bottleneck Models with Trees

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
As AI models grow larger, the demand for accountability and interpretability has become increasingly critical for understanding their decision-making processes. Concept Bottleneck Models (CBMs) have gained attention for enhancing interpretability by mapping inputs to intermediate concepts before making final predictions. However, CBMs often suffer from information leakage, where additional input data, not captured by the concepts, is used to improve task performance, complicating the interpretation of downstream predictions. In this paper, we introduce a novel approach for training both joint and sequential CBMs that allows us to identify and control leakage using decision trees. Our method quantifies leakage by comparing the decision paths of hard CBMs with their soft, leaky counterparts. Specifically, we show that soft leaky CBMs extend the decision paths of hard CBMs, particularly in cases where concept information is incomplete. Using this insight, we develop a technique to better inspect and manage leakage, isolating the subsets of data  most affected by this. Through synthetic and real-world experiments, we demonstrate that controlling leakage in this way not only improves task accuracy but also yields more informative and transparent explanations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Concept-bottleneck Models (CBM) suffer from information leakage, where the model exploits information in the soft concept scores with unintended consequences towards interpretability.
The paper addresses the leakage issue by fitting constrained decision trees on top of the concept scores.
They quantify information leakage with a mutual information measure and propose a three-step procedure for modeling.
The paper argues that their technique yields better explanations even when the concept set is incomplete, and guides the developer to concept sets that needs expansion.

I found the idea neat and the presentation clear but found empirical validation underwhelming.

### Strengths
- The paper is well motivated and the presentation is clean. They argued their modeling choices well. 
- Mixed-CBM idea is intuitive, and follows from their mutual information measure of (4).

### Weaknesses
 **Empirical Validation**

The results in Table 1 and Table 2 indicate that MCBM-* (their method) has similar task accuracy to Sequential/Joint with vanilla decision trees.
MCBM-*, however, allows for leakage inspection as remarked in Table 1 or in Section 5.3.
I too see MCBM-*'s major contribution is with leakage inspection, but the paper makes only a sparing evaluation of the same.
I expect to see stronger evaluation of MCBM's utility for information leakage, and their implications in improving task accuracy or explanation quality.
Perhaps through human-studies or mining new concepts on one of the tasks such as CUB.

From Table 2, I do not see how MCBM-* is better. It has worser task accuracy than EntropyNet, but perhaps lower leakage? (which is not apparent).
Given that their method has advantages when the number of concepts is small, their evaluation too should bring out more readily.

Overall, I did not find the evaluation convincing on (a) the promise and implications of MCBM-*'s leakage inspection, (b) MCBM's merits over decision trees or any other baselines.

### Questions
1. Please explain the metrics at length. Concept accuracy, fidelity and explanation accuracy. I believe explanation accuracy is mentioned but never used (in which case it can be dropped).
2. From the argument in L460-462, decision trees with soft concept scores must have led to more leakage (or poor fidelity?), but that's not the case in Table 1. Please explain.
3. When the concept scores are mixed, I do not see why only the concepts on the path are softened. What happens when all the concepts are softened (when expanding the tree) or only the leaf concept is softened.
4. Please comment on the choice of hyperparam. Table 2 lists out numbers for various hparam $\lambda_C$, but how is it picked? 
5. (Comment) A picture or description of Morpho-MNIST can be handy.

### Soundness
3

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
4

### Summary
This work introduces Mixed Concept Bottleneck Models (MCBMs), a predictive model and an inspection tool that uses decision trees to analyze and control information leakage in traditional Concept Bottleneck Models (CBMs). By exploiting a hard independent CBM whose label predictor is a decision tree, this model constructs a CBM by expanding each of the original decision tree’s leaf nodes using new sub-trees that operate on soft concept representations for the concepts that are used to reach that node. This allows MCBMs to properly quantify leakage across each decision path and rule, producing group-based explanations. This paper evaluates MCBMs across three datasets and shows that they may lead to high-fidelity and interpretable explanations whilst performing similarly to equivalent hard, independently trained CBMs.

### Strengths
Thank you so much for submitting this work! I enjoyed reading this paper and learned a lot while reading it. Below are what I believe are this paper’s main strengths:

1. **[Originality] (Critical)** Introducing decision trees to capture, disambiguate, and control leakage in vanilla CBMs is, to the best of my knowledge, certainly novel. I like the general idea and believe others may also find it interesting and new.
2. **[Significance] (Major)** If shown to lead to actionable conclusions, I do believe that MCBM may have some impact as an analysis tool (more so than as a predictive model; see weaknesses below). Moreover, the simple yet useful formalization of information leakage (i.e., equation (4)), which MCBMs can very easily estimate, is a helpful step towards better understanding and studying information leakage. Therefore, this approach may be useful to others working in this space, particularly those interested in leakage. As such, I believe both of these contributions are potentially useful for the overall XAI community. 
3. **[Quality] (Minor)** This work is well-placed within the concept-based XAI literature and does a good job of connecting MCBMs to existing work outside of this paper.
4. **[Clarity] (Major)** The paper is very well-written, easy to follow, and full of visual aids that truly help with its understanding.

### Weaknesses
In contrast, I believe the following are some of this work’s limitations:

1. **[Significance] (Critical)** I can see how the proposed approach may be useful for studying leakage in vanilla CBMs. However, I think a very strong case can be built against using MCBMs as a model for prediction in real-world cases, given their significant drops in performance compared to existing even simple baselines (e.g., joint CBMs). A case can be built to use a model that offers more interpretability (however one defines that) if the hit on performance is not very significant. In this case, however, the presented evidence suggests this hit can indeed be quite significant. Moreover, it is unclear how MCBMs compare to and how they could be used to analyze much more modern approaches (e.g., Post-hoc CBMs, CEMs, ProbCBMs, Energy-free CBMs,  etc.), all of which are much better than vanilla CBMs. As such, I have some doubts about the potential impact of this work without further evidence or contributions showing their use for modern baselines/pipelines/frameworks. See below for further questions on this particular topic, as this is my biggest concern/hesitation regarding this work.
2. **[Significance] (Critical)** Related to my concern above, although MCBM is claimed to be helpful not just as a model but also as an analysis tool, the current experiments fail to provide evidence that any conclusions extracted by analyzing MCBM’s outputs do indeed lead to actionable changes that improve the analyzed model. My current concern is that this work presents MCBM as both (1) a model and (2) an analysis tool, without providing sufficient evidence, in my opinion, that it leads to actionable significant improvements in either of those two directions.
3. **[Significance/Quality] (Major)** Concept interventions, a standard evaluation procedure for CBM-like models, are not evaluated anywhere in this work. As such, it is hard to fully understand the benefits of MCBMs over other existing baselines in this field.
4. **[Quality] (Major)** Against common good practices, no error bars are provided for any of the results. This makes it very difficult to judge for significance, and it is particularly important here as some of the gains are small enough that they could just be from noise.
5. **[Quality/Clarity] (Minor)** It is unclear how some of the key hyperparameters (e.g., $\texttt{msl}$) were selected for the different tasks. Given how sensitive MCBMs are shown to be to this hyperparameter (in the appendix), it is very important to verify that this hyperparameter was properly selected without accidental test-set leakage.

### Questions
**[Post rebuttal update: Changed my score to a *5: marginally below the acceptance threshold*]**

Currently, given some of my concerns with this work's framing and evaluation, and considering them w.r.t. the strengths I listed above, I am leaning towards rejecting this paper. However, I am absolutely happy to be convinced that some or all of my conclusions are wrong and to change my recommendation based on a discussion with the authors. For this, the following questions could help clarify/question some of my concerns:

1. **(Critical)** I understand that “trustworthy”/leakage-free explanations are always better. However, in the case where the concept set is incomplete (which is likely to be the case for any real-world dataset), what is the argument for using something like MCBM over any of the baselines that can achieve high accuracy in these setups (e.g., joint logit CBMs, Hybrid CBMs, Hybrid Post-hoc CBMs, CEMs, etc)? The performance difference between MCBM-Seq and joint CBMs, arguably a weak baseline for incompleteness compared to more recent approaches, seems to be large enough that one could construct a very convincing argument that any gains in reductions in concept leakage are not worth it in practice  (e.g.,  up to 25% absolute drop in task accuracy in CUB according to Table 2). This is my largest concern with this work. Am I misunderstanding something here? If not, what is the case for using something like an MCBM over any other existing approaches in practical scenarios where concepts are almost certainly bound to be incomplete? The reason why I am fixating on this is that there are several claims in the paper (e.g., “these tree-based approaches …achieve better accuracy on datasets with incomplete concept information” in Section 6) that do not appear to be backed by the same evidence presented in this paper. As such, assuming I correctly understand this work (happy to be convinced that I do not), I think these claims should be revised to represent better what the evidence shows.
2. **(Critical)** Related to the question above, if the interest is to use MCBM as a predictive model, do you have a sense of how MCBMs perform against any (not necessarily all) of the many high-performing modern baselines (CEMs/Post-hoc CBMs/ProbCBMs/Energy-based CBMs/etc)?
3. **(Critical)** If the argument to be built is that MCBMs are better for post-hoc analysis than prediction, then I would say the paper should focus more on the analysis part and show how MCBMs can be used to lead to actionable changes/edits/insights that improve the underlying model somehow. Section 5.3 shows some of this but falls short in that it does not convincingly show that some of the conclusions made from the MCBM’s analysis can lead to changes to the underlying model that indeed improve it under some intended metric. Therefore, do you have any empirical evidence of actionable changes derived from insights from MCBM that led to a model’s update improving its performance under a reasonable metric? Could these sorts of studies be extended to more modern architectures like those discussed above?
4. **(Critical)** Could you please provide error bars for the results in all of the presented Tables? This would enable one to determine the significance of any deviations from a baseline. This is particularly important here as some of the gains presented (e.g., in Table 2) are small enough that they could be attributed to noise.
5. **(Critical)** The use of bold in Table 1 is very confusing and seems to follow an unconventional use. Is it the case that only the best scores for each metric are in bold as it is traditionally done? If so, then why are there no entries in bold for the Task accuracy (where MCBM underperforms), and why are certain MCBM results bolded when, in fact, they are worse than competing baselines (e.g., “explanation” for CUB and MIMIC-II)? I think it is absolutely okay to use bolding for any purpose as long as it is made clear to the readers. In the absence of an explanation for it, however, I would say the common assumption is that bold fonts indicate the best-performing baseline (which does not appear to be the case here).
6. **(Critical)** In Section 1, it is claimed that information leakage may affect the ability to intervene on CBMs (a statement I agree with for vanilla CBMs but seems to not be the case for other sorts of CBM-like models as recent evidence suggests [1]). Is it the case that interventions in MCBMs lead to higher accuracies than in their CBM counterparts? Given the importance that interventions have for CBMs (and the way they serve as a verification of their interpretability across the literature), it would be extremely helpful to understand what they look like for MCBMs.
7. **(Major)** The appendices show that the hyperparameter $\texttt{msl}$ has a significant effect on the performance and interpretability of the resulting MCBM. How was this selected for the results shown in Section 5? How would one select this argument in practice?
8. **(Minor)** It is claimed that the method “does not introduce any computational overhead compared to a Sequential CBM with a single decision tree as label predictor”. This is true from an asymptotic complexity point of view, but it may not necessarily be true from a practical point of view (asymptotic analysis does not consider the average instance and ignores potentially large constants, which may have non-trivial effects in the "small n" limit). In practice, what is the observed overhead in training an MCBM vs a CBM as the number of samples or concepts varies?
9. **(Minor)** If my understanding is correct, from Algorithm 1 and Section 4.1’s description, the concept predictor’s outputs are used during test time in both the global and the specialized decision trees. If that is true, then Figure 2 is a nice addition but may be a bit misleading as it appears to indicate that some of the concepts don’t come from the concept predictor, but instead, they come from some oracle/ground truth source. Is my understanding of how this method operates correct? If so, then why are there no connections/edges from the concept predictor to the hard CBM part (LHS) of Figure 2?
10. **(Minor)** How are the 45 concepts for CUB chosen? I can see the list of selected concepts in the Appendix, but it is unclear why these were selected over the rest.
11. **(Minor)** Out of curiosity, in case this has already been tried, if one does leaf-node specialization based on the **concept** **logits** rather than the probabilities, do you get better performance on incomplete datasets? If so, then why would this not be a better path than using the probabilities? Logits can also be calibrated and interpreted as probabilities, and they may enable more leakage that can benefit the downstream task.

### Minor Suggestions and Typos

Whilst reading this work, I found the following potential minor issues/typos which may be helpful when preparing a new version of this manuscript:

1. **(Potential Typo)** In line 80, “… the purpose of this work is provide …” should probably be “… the purpose of this work is to provide…”
2. **(Potential Typo, nitpicking)** In line 135, should “categorical vector” be “binary vector” instead for the concept vector $c$?
3. **(Potential Typo)** In line 141, “e.g” should probably be “e.g.”
4. **(Potential Typo)** In line 214, the citation to Platt is accidentally all upper-cased.
5. **(Formatting)** When using the opening quotations (”) in Latex, I would suggest using `` rather than ". Otherwise, the left quotation symbol is reversed (see Section 5.1 for examples).

## References

- [1] Zarlenga et al. "Learning to Receive Help: Intervention-Aware Concept Embedding Models." NeurIPS (2023).

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Concept bottleneck models (CBMs) is a valuable technique for enhancing the interpretability and explainability of deep learning models; however, they have recently been shown to suffer from information leakage issues. This work proposes a new decision tree-based method to address the leakage issue. Unlike the original CBM which used a small network (e.g. a linear model) to predict the label Y from the (soft or hard) concept representation C, this work uses a decision tree as the predictor. The authors smartly show that by comparing the cases when  soft concepts and hard concepts are used to construct the tree, it is possible to inspect and control information leakage corresponding to specific configurations of concepts. The method is evaluated on several standard datasets.

### Strengths
- The paper introduces a new decision tree-based method for quantifying and controlling information leakage in CBMs, which to the best of my knowledge is very novel. I personally think that the use of tree-based model in CBMs itself may already be a good contribution before its applications in addressing information leakage.
- The writing is mostly clear and easy to follow. I especially appreciate Figure 1 which helps readers to intuitive understand the main idea and pipeline of the proposed methodology;
- To the best of my knowledge, this is the first work to formulate information leakage issues in CBMs. For this purpose, the authors propose a general, information-theoretic metric (Definition 3.1). The applicability of this metric is well beyond the specific method considered in this paper (tree-based CBMs);
- The work also offers a new method for inspecting how information is leaked and used in a more fine-grained and interpretable manner. By inspecting each path in the decision tree, practitioner can understand how hard concepts are insufficient for accurate predictions and how additional information could enhance these predictions (thereby leads to information leakage). This interpretability, facilitated by the use of decision tree, is a notable innovation over existing methods;
- Reproducibility: the authors have provided certain implementation details as well as offering anonymous code repo.

### Weaknesses
 - (Major) There might be, in my opinion, a potential discrepancy between the information leakage metric defined (Definition 3.1) and the actual tree-based implementation for computing this information leakage. Specifically, the defined metric appears to consider the mutual information between the predicted concepts and the target variable conditioned on the true concepts, i.e., I(Ĉ; Y|C), where both Ĉ and C are random variables. However, the tree-based implementation seems to compute this information gain conditioned on specific configurations of the hard concepts at each leaf node, i.e., I(Ĉ; Y|C=c_k), where c_k represents a specific constant vector of hard concepts. This discrepancy raises concerns about whether the tree-based method is truly capturing the intended notion of information leakage as defined by the general metric.
- (Major) Related to the above point, it seems that the information leakage problem addressed in this paper differs slightly from that studied in existing works. Specifically, this work appears to focus on computing information leakage corresponding to specific configurations of hard concepts $C$ i.e. $I(\hat{C}; Y|C=const)$ (where $C$ equals to some constant) rather than calculating $I(\hat{C}; Y|C)$ (where both $\hat{C}$ and $C$ are random variables). This distinction is crucial because it implies that the method may not be measuring the overall information leakage but rather a localized version of it, potentially missing the broader picture of how information is leaked across different concept configurations.
- (Major) While the insights and ideas presented are highly novel, the proposed three-phase method also seems more complex than existing approaches aiming to address information leakage [1, 2, 3]. The method involves training a global decision tree, followed by training individual sub-trees for each leaf node, and an independently trained concept predictor. This multi-stage process introduces additional complexity and computational overhead, which may not be justified without a clear demonstration of superior performance compared to simpler alternatives.
- (Minor) The work has not been compared to state-of-the-art methods for addressing information leakage, such as CEM [1], PCBM [2] and [3]. This lack of empirical comparison makes it difficult to assess the practical advantages of the proposed method over existing techniques. Without such comparisons, it remains unclear whether the added complexity of the tree-based approach translates into tangible improvements in controlling information leakage.

### Questions
- The information gain you computed in eq.(5) seems to condition on a particular configuration of the hard concepts (e.g. ck = [0, 1, 0]) corresponding to the leaf node. Is this correct?
- How is the calibration process described in lines 211-241 actually performed? It may not be immediately clear to those who are unfamiliar with the specific calibration technique mentioned. The author could consider to include a short description of these processes in future refinement.
- The work has not been compared to other methods for addressing information leakage in CBMs e.g. [1, 2, 3]. Could the authors provide a justification for this omission?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors study a particular form of information leakage in decision-tree CBMs. They introduce a metric and method to quantify this information leakage by comparing the decision-tree paths of hard CBMs with their soft counterparts. Their method induces little to no drops in task / concept accuracy.

### Strengths
- the authors study the interesting and important problem of how to build trustworthy CBMs
- the authors perform experiments on diverse datasets

### Weaknesses
 - the main issue seems to be a lack of rationale for definition 3.1, which forms the basis for the paper. The authors quantify *information leakage* as the amount of “unintended information” that is used to predict the label with soft concepts that is not present in hard representation. Why captures whether this information is “unintended”. It seems to me that the author’s information measure needlessly penalizes soft concepts that provide extra, intended information. For example, in Morpho-MNIST, continuous features  (i.e. thickness, area, length, width, height, and slant of digits) are binned and then used for prediction. Soft concepts may improve the model by removing the binning, making these features more reliable.
- It is also unclear how quantifying this information leakage is useful. It would be nice to see whether this information could be used, e.g. to improve concepts for a downstream task or in a human user study where concepts are shown to be more understandable. This is especially important seeing as the introduced method seems to slightly decrease some desirable metrics (Table 1)
- why do the authors focus on decision trees (e.g. as opposed to a linear model CBM)? The paper only compares against Entropy Net & a black-box baseline
- minutia
    - line 141 “linear layer decision trees” - do the authors mean “linear layer or decision trees”
    - line 144 “networks f and g” - is g a network? line 141 would suggest it is not
    - why is this a reasonable definition?
    - line 189 “as the trees be incomparable”

### Questions
- why do the authors focus on decision trees (e.g. as opposed to a linear model CBM)? The paper only compares against Entropy Net & a black-box baseline
- minutia
    - line 141 “linear layer decision trees” - do the authors mean “linear layer or decision trees”
    - line 144 “networks f and g” - is g a network? line 141 would suggest it is not
    - why is this a reasonable definition?
    - line 189 “as the trees be incomparable”

### Soundness
3

### Presentation
2

### Contribution
2
