# On the (un) interpretability of Ensembles: A Computational Analysis

- Decision: Reject
- Scores: 3, 8, 6, 5, 6

## Abstract
Despite the widespread adoption of ensemble models, it is widely acknowledged within the ML community that they offer limited interpretability. For instance, while a single decision tree is considered interpretable, ensembles of decision trees (e.g., boosted-trees) are usually regarded as black-boxes. Although this reduced interpretability is widely acknowledged, the topic has received only limited attention from a theoretical and mathematical viewpoint.  In this work, we provide an elaborate analysis of the interpretability of ensemble models through the lens of *computational complexity* theory. In a nutshell, we explore different forms of explanations, and analyze whether obtaining explanations for ensembles is strictly computationally less tractable than for their constituent base models. We show that this is indeed the case for ensembles that consist of interpretable models, such as decision trees or linear models; but this is not the case for ensembles consisting of more complex models, such as neural networks. Next, we perform a fine-grained analysis using parameterized complexity to measure the impact of different problem parameters on an ensemble's interpretability. Our findings reveal that even if we shrink the *size* of all base models in an ensemble substantially, the ensemble as a whole remains intractable to interpret. However, an analysis of the *number* of base models yields a surprising dynamic --- while ensembles consisting of a limited number of decision trees can be interpreted efficiently, ensembles that consist of a small (even *constant*) number of linear models are computationally intractable to interpret.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
Authors develop a theoretical basis for evaluation of the interpretability of different ensembles (voting or weighted-voting) with different base models: linear, decision tree and neural network. Authors examine computational complexity of deriving different types of the explanations for ensembles and compare them to single base learners, and provide mathematical guarantees. Authors focus on 3 types of explainability: Sufficient Reason Feature Selection (SRFS), Contrastive Explanations (CF), Shapley Value Feature Attributions (SVFA). Authors analyze a parametrized complexity to show how different parameters such as base-model size, number of base learners affect ensemble interpretability.

### Strengths
- The paper provides computational complexity analysis for ensembles of different type of base models with mathematical guarantees (and proofs).
- Authors reviewed different explainability queries

### Weaknesses
 - Besides mathematical proofs and guarantees, the contribution of the paper is very questionable. The conclusions authors made are well-known. For example, weighted voting of neural networks can be expressed as a bigger neural network with another linear layer, which is still a neural network, therefore, complexity gap should not be high (if any). Similarly, ensembles with a constant number of linear models can be shown (for specific ensemble type) as a neural network of two layers with non-linear activation (for classification), which is for interpretable.
- In my opinion, the most interesting part of the paper is hidden in the appendix part and needs restructuring.
- A key concern lies in the definition and assumptions around interpretability. The authors acknowledge that interpretability is a long-studied and not well-defined concept. While they propose their own definition, it is neither widely accepted nor practically relevant. The paper assumes there is a common agreement around interpretability criteria that does not exist. For example, the authors claim that Shapley values are "commonly recognized" as an interpretability metric, yet these values are widely criticized in the field.
- The structure of the paper is another significant issue. At 60 pages, including the appendix, it is overly dense and challenging to go through. Frequent references to material in the appendix make the paper even harder to follow. For a conference submission, the work would benefit from being split into several smaller, focused papers with clearer organization and presentation.
- Some of the conclusions drawn in the paper are trivial or widely known. For instance, the discussion in lines 78–92 simply reiterates the well-established fact that ensembles are not interpretable. Insights derived from the authors’ formulation add little practical value for the machine learning community, limiting the paper’s broader impact.
- There are also technical inaccuracies that require attention. For example, the authors discuss decision trees without specifying that they are axis-aligned, which is an important distinction since oblique decision trees (with linear splits) also exist. Additionally, the treatment of MCR (also known as counterfactual explanations) in Table 1 as a novel contribution is misleading, as its NP-completeness is already well known.
- A broader concern is the disconnect between the theoretical results presented and the practical needs in machine learning. The authors focus on binary inputs, yet most practical ML systems handle continuous data naturally. While it is possible to discretize continuous inputs, such an approach is rarely necessary in practice and limits the relevance of the proposed methods.

### Questions
N/A

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
2

### Summary
The paper presents an expanded framework for analyzing the complexity of interpreting ensemble models in comparison to their constituent base models and to each other. The authors investigate three broad categories of base models—FBDDs (generalized trees), linear models, and multilayer perceptrons (MLPs)—alongside three families of interpretability metrics (referred to as 'explainability queries'): Sufficient Reasons, Contrastive Reasons, and SHAP values. This framework encompasses a wide range of interpretability approaches commonly used in machine learning. The authors provide an in-depth computational analysis of interpretability for these models, demonstrating that the computational costs differ significantly when comparing base models with ensembles, particularly in the cases of linear models and tree ensembles.

To extend this analysis, the authors apply parameterized complexity techniques to explore how model size and the number of base models affect the computational complexity. One key insight from this parametric perspective is that, while increasing the number of models in a linear model ensemble does not impact interpretability tractability, limiting the number of trees in a tree ensemble can render interpretation computationally feasible.

### Strengths
* The authors offer a well-rounded perspective that reflects a wide range of approaches used in the field. They introduce a comprehensive and formal framework for analysing interpretability complexity across different model types and interpretability metrics.
 This makes the work broadly applicable and useful for various ML subfields, especially formal analysis on interpretability methods.
* The use of parameterized complexity to analyze the effect of model size and the number of base models adds depth to the analysis. This aspect of the work allows for a nuanced view of interpretability that reveals under what conditions interpretability is tractable, which is particularly innovative and sheds more insight on formal complexity of interpretability in ensembles of different classes.
* The paper is well-structured, coherent, and logically organized. The authors thoughtfully delegate details to Appendices, where they provide comprehensive and easy to follow proofs. Furthermore, including proof sketches in the main text is an excellent choice, as it allows readers to understand the core ideas without extensive back-and-forth with the Appendices.

### Weaknesses
While there are no major weaknesses in the scope, there is always room for expansion. For instance, discussing the interpretability of regression models versus classifiers more extensively, exploring continuous domains and fundamental differences (which is actaully touched on in an Appendix), and extending metrics to observational SHAP and other interpretability metrics. However, the current scope is already comprehensive, and these suggestions could serve as directions for future work. To be fair, extending it in any above-mentioned directions could end up costing the clarity.

### Questions
Given the assumption of feature independence for Shap values, is the work still includes methods like interventional TreeSHAP, which are proved to be computing SHAP values under the same assumption [1], while leveraging the tree structures in the ensemble rather than computing the intractable original SHAP formula? Is such methods that are computing exact SHAP values not directly from the original SHAP formula something to be considered in your work?

[1] Laberge, Gabriel, and Yann Pequignot. "Understanding interventional treeshap: How and why it works." arXiv preprint arXiv:2209.15123 (2022).

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper theoretically studies the class of ensemble models from an interpretability perspective. Specifically, the paper discusses the computational complexity associated with different kinds of "interpretability queries" (i.e. SHAP, counterfactuals) and different kind of ensemble models (deep ensembles, tree ensembles, etc.). The paper finds evidence that ensembles are in fact less interpretable than base models. This is substantiated by an extensive list of theoretical results.

### Strengths
- The subject matter is an important research area within machine learning, making this research highly relevant. The focus aligns well with ongoing discussions and research questions (TreeSHAP + Tree vs. TreeSHAP + Forest). The paper adds a good contribution to explainability and theoretical foundations in AI. 
- A clear strengths of this paper are the theoretical contributions, of which there are many. While I have problems with the presentation of the results, they are very interesting and like the authors say "give theoretical merit to the folklore saying that ensembles are less interpretable than base models". I do very much like the paper because of this. I particularly like the additional results for the decision tree classes (FBDDs) and the non-SHAP related explanation queries.
- All in all, while the paper is very technical, the writing is strong and precise.

### Weaknesses
 - **The paper is too technical**, which could lead to the ICLR audience might missing the core contributions. It contains many acronyms that are not generally known, making it difficult for readers to follow along. Furthermore, one theoretical result follows another without putting the results well into context or grounding it. At the moment the paper contains 8 Theorems and 8 propositions making it 16 theoretical results on 6 pages. Lines 246-258 are just a proof sketch right where the central part of the paper could be. This may hinder the audience from fully appreciating the significance and implications of each result within the broader field. The appendix is quite long (44 pages give or take) and contains a lot of details missing in the main text. This reinforces the impression that the contribution may not be well suited to a conference paper and would maybe better fit a journal like JMLR.
- While the paper is sound and provides a plethora of proofs, I am **missing** some **empirical validation** or at least **illustrative examples**. The work stays very abstract. I acknowledge that computational complexity results do not necessarily need "experiments", however they do help a lot in grounding the theoretical results for practitioners or uncover edge cases.
- The paper does not contain a limitations section.

### Questions
- How can you make the paper more approachable provided an additional page?
- I highly suggest, you move technical proof sketches out of the main paper and put the results better into context and tell the reader why result X is meaningful for model class B. You may further streamline the paper by moving more minor results into the appendix all together.

### Soundness
3

### Presentation
1

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper provides an analysis of the computational complexity of ensemble models’ interpretability. The authors investigate whether explaining ensemble models is inherently more computationally demanding than explaining individual models. The authors find that explaining ensembles made of interpretable base models, e.g., decision trees, is computationally more expensive than the base models. However, there is no gap in the computational complexity between explaining expressive, uninterpretable models, e.g., neural networks, and their ensembles.

The paper also studies the parameterized complexity of explaining ensembles, examining how specific factors, e.g., the size or the number of base models, affect interpretability. The results show that reducing the size of the base models in the ensemble does not make the ensemble interpretable. The effect of the number of base models on the interpretability depends on their type, i.e., linear models or decision trees. Ensembles with a small number of decision trees can be interpreted efficiently, while a small number of linear models in an ensemble makes it computationally intractable to interpret.

### Strengths
1- The manuscript provides original work based on a theoretical foundation.

2- The paper shows differences between linear model ensembles and decision tree ensembles in parameterized complexity results, which reveals that not all ensembles are equally hard to interpret.

### Weaknesses
1- The paper’s contribution is marginal and provides evidence for the already-known un-interpretability of ensemble models, as the authors mention in line 530: “Our work provides mathematical evidence for the folklore belief: “ensembles are not interpretable”.” However, the paper succeeds in showing that not all ensembles are equally hard to interpret.

2- The paper lacks motivation for the targeted problem and why the contribution can be significant. It can be helpful if the introduction is expanded to include examples of how the findings can impact research or practice in explainable AI.

3- The authors claim that the main focus of the paper was on understanding the complexity of ensemble models and their impact on model interpretability. However, the explanations of the compared models were not evaluated or compared using explainability-related metrics, e.g., fidelity, robustness, or using a user-based evaluation. Therefore, it can be helpful to clarify explicitly that the focus is on the theoretical computational complexity of explanations, not an evaluation of interpretability in general.

### Questions
Why can the findings of this work be significant to researchers in the domain of interpretability and explainable AI if the findings are already “folklore belief”?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies the computational complexity of computing explanations of ensembles.

### Strengths
The paper is mostly well written and easy to follow even if you do not have a strong background in computational complexity theory -- the last time I had to deal with this was when I was a student. Given that, I would not consider myself as an expert in this area -- i.e. you should take all my comments with a pinch of salt.

However, checking the proofs for correctness is beyond my level of expertise.

### Weaknesses
Given that the paper is purely theoretical, I think it would be nice to highlight the consequences/recommendations for practitioners—e.g., limiting the number of models or the size of the base models, etc. Also, I would be interested in having an algorithm (even a naive one) that can be applied to ensembles for which the stated properties are fulfilled—although this might be too much for a conference paper.


Minor:
"while ensembles consisting of a limited number of decision trees can be interpreted efficiently, ensembles that consist of a small (even constant) number of linear models are computationally intractable to interpret" -- when first reading this (abstract) I had trouble understanding the difference between "limited number" vs. "small". Eventually it became clear throughout the paper -- I think rephrasing this statement would make it more clear for the average reader (e.g. "... , but limiting the number of linear models does not make the problem tractable" or smth. similar).

### Questions
What do you consider the major takeaway or recommendation for practitioners?

### Soundness
3

### Presentation
3

### Contribution
3
