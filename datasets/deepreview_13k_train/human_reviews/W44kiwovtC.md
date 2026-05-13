# FastDCFlow: Fast and Diverse Counterfactual Explanations Using Normalizing Flows

- Decision: Reject
- Scores: 3, 3, 5

## Abstract
Machine-learning models, which are known to accurately predict patterns from large datasets, are crucial in decision-making. Consequently, counterfactual explanations-methods explaining predictions by introducing input perturbations-have become prominent. These perturbations often suggest ways to alter predictions, leading to actionable recommendations. However, the current techniques require resolving the optimization problems for each input change, rendering them computationally expensive. In addition, traditional encoding methods inadequately address the perturbations of categorical variables in tabular data. Thus, this study propose "FastDCFlow," an efficient counterfactual explanation method using normalizing flows. The proposed method captures complex data distributions, learns meaningful latent spaces that retain proximity, and improves the predictions. For categorical variables, we employed "TargetEncoding," which respects ordinal relationships and includes perturbation costs. The proposed method outperformed existing methods in multiple metrics, striking a balance between trade-offs for counterfactual explanations.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper lays out a method to obtain counterfactual explanations (CEs) of machine learning (ML) models, employing normalizing flows to generate candidate CEs. Target Encoding (TE) is utilized to maintain some level of ordinality amongst categorical features.

### Strengths
- Results are mostly on par with current state of the art, dependent on the criteria end users are seeking
- CF parameters are analyzed in a useful way
- Besides some typos, the paper is well written, with clear formatting and a logical structure

### Weaknesses
 - The main problem in the paper is its lack of novelty. The two main contributions involve a) using a latent space model and b) converting categorical features to continuous mappings. The first has been proposed many times in the literature, mostly using VAEs. Normalizing flows have also been used before in this context, as the paper references. The transformation of categorical features to continuous features is not new either, and as such, I find the paper's novelty somewhat lacking.
- When considering the usual metrics proximity (P), validity (V) and run time (RT), the proposed method does not perform best across any one metric. The diversity metrics are questionable since they do not appear normalized, thus worse proximity is likely to promote better diversity (see questions).
- The results therefore rely heavily on the proposed metrics, CV and CS, which themselves are left highly unjustified in the text. I do not find these functions particularly compelling, since CS relies on CV, which itself relies on the diversity metrics proposed.

### Questions
1. Based on Table 1, Inner Diversity (ID) and Outer Diversity (OD) compute the average $\ell_2$ differences between CEs for one test point and between CEs across multiple test points. Why was diversity not considered via the angle between CE perturbations rather than the $\ell_2$ norm between raw CEs? Using the $\ell_2$ norm alone means larger diversity can be achieved through CEs with very bad proximity.
2. For the Bank dataset, FastDCFlow achieves proximity an order of magnitude worse than other methods (this is serious), and also achieves worse validity. Yet, FastDCFlow achieves an order of magnitude higher performance on the CS metric which is used for the final assessment of the methods. Proximity and validity are the two fundamental goals of counterfactual explanations, and in this case FastDCFlow fails on both fronts while being pushed as the method with the best overall score. Can the authors please provide further justification of the CS metric (mostly the diversity evaluation in the CV metric) in the context of the above example?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The is paper is concerned with extending the applicability of counterfactual explanation to tabular data, as well as increasing the computational efficiency of producing such explanations.  The authors approach is to propose a normalizing flow along with an ordinal variable encoding to account for cost of perturbations.

### Strengths
- The authors experiments help to identify why standard VAEs fail to produce a good amount of variation in their generated CEs.

### Weaknesses
 - Experimentally, the authors omit a comparison to CeFLow of Duong et al 2023, which is the most natural comparator to their method (being itself a CF model for tabular data based on normalizing flows).  It's notable in its absence, how come?
- The authors explanation of how diversity is to be generated in CEs is too brief.  Section 3.2 very briefly states that the temperature parameter $t$ is used to add noise to the origins of the samples of $\mathbf{z}_{test}$.  But does this offer *more* diversity of valid samples than a method like DiCE, which intentionally penalizes the covariance between sampled points?  It's unsatisfying.
- The first paragraph in section 3 discusses some notation for CE generation, but states that: 
> The aim of CE is to generate perturbed inputs $\mathbf{x}_{cf}$ such that $f(\mathbf{x}_{cf})>f(\mathbf{x})$ for the observed input x.

There are two mistakes here.  First is that  $>$ should be $!=$.  Second, it is far from settled what the benefits of CE are for, and is largely dependent on the person using the tool.  Users will take different insights from CEs than people building models, for example.  My reading of the paper of the paper suggests the authors are intending FastDCFlow to be a user-centric tool, so they should inform their perspective and their experiments accordingly.  Could they do a simulated user study, showing that FastDCFlow helps users make better decisions?  Or could they take an organizational risk perspective, showing that FastDCFlow helps an organization providing a model-based service make better (e.g fairer) decisions?


### Questions
- The second paragraph of the conclusion starts out with 
> In subsequent phases of this study, we are currently integrating TE with a transformation technique that respects the order of categorical variables. 

but section 6.1 suggests that TE was integrated for the experiment in this model, so I'm confused.  Is this just an error in tense?  Or does the present implementation of TE not respect order?  Or something else?
- The same paragraph of the conclusion continues
> Although predicted target values between the ML model evaluations using TE and OHE showed no marked differences, effectively adapting conversion methods for compact datasets remain a challenge.

I believe this statement needs way more unpacking.  If there were “no marked differences” between TE and OHE, I see two important questions that should be asked here:
1. Why is this so?  Is this a consequence of the evaluation criteria for CEs?
2. If OHE and TE don’t show a marked difference, what’s the justification for pursuing the integration of TE?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a methodology for computing counterfactual explanations using normalizing flows.

### Strengths
- Very interesting and novel idea of using normalizing flows
- Paper is well structured and mostly well written -- see Section "Weaknesses" for some criticism

### Weaknesses
 - Experimental results do not look that convincing to me -- often other methods outperform the proposed method. Not sure how much sense the corrected scores make -- I think it would be better to compare different aspects directly, instead of merging them all into a single score
- Training a generation mechanism (e.g. the proposed method) might not be possible or difficult if only very few training samples are available. This might hinder the use of the proposed method in case of high-dimensional data space where only few samples are available
- Access to model internals are needed -- otherwise a gradient-based optimization method can not be applied to the proposed loss function for training the model. To me this looks as a another limitation of the proposed method
-  In general, I miss a discussion of limitations and drawbacks of the proposed method

### Questions
-  I am not sure how fair/appropriate the runtime comparison is: Other methods (non-generative methods) where never designed to be trained on data, so it is somewhat clear that these will not be able to compete with a trained generative method. On the other hand, building/training a generative method requires a lot of training data which poses a major disadvantage compared to other non-generative methods. I think a comparison of these very different methods is challenging -- maybe the authors can elaborate on this a bit more.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
