# Fairness-enhancing mixed effects deep learning improves fairness on in- and out-of-distribution clustered (non-iid) data

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Traditional deep learning (DL) models have two ubiquitous limitations. First, they assume training samples are independent and identically distributed (i.i.d), an assumption often violated in real-world datasets where samples are grouped by shared measurements (e.g., participants or cells). This leads to performance degradation, limited generalization, and covariate confounding, which induces Type 1 and Type 2 errors. Second, DL models typically prioritize overall accuracy, favoring accuracy on the majority, while sacrificing performance for underrepresented subpopulations, leading to unfair, biased models. This is critical to remediate, particularly in models influencing decisions regarding loan approvals and healthcare. To address these issues, we propose the Fair Mixed Effects Deep Learning (Fair MEDL) framework. This framework quantifies cluster-invariant fixed effects (FE) and cluster-specific random effects (RE) through: 1) a cluster adversary for learning invariant FE, 2) a Bayesian neural network for RE, and 3) a mixing function combining FE and RE for final predictions. Fairness is enhanced through the architectural and loss function changes introduced by an adversarial debiasing network. We formally define and demonstrate improved fairness across three metrics on both classification and regression tasks: equalized odds, demographic parity, and counterfactual fairness. Our method also identifies and de-weights confounded covariates, mitigating Type 1 and 2 errors. The framework is comprehensively evaluated across three datasets spanning two industries, including finance and healthcare. The Fair MEDL framework improves fairness by 86.4\% for \textit{Age}, 64.9\% for \textit{Race}, 57.8\% for \textit{Sex}, and 36.2\% for \textit{Marital status}, while maintaining robust predictive performance. Our implementation is publicly available on GitHub.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors build on prior work defining mixed effects to provide fair and robust predictors (ARMED). They add a debiasing term to ensure fairness in the fixed-effect part and demonstrate how their method improves on the ARMED baseline in terms of fairness using 3 datasets.

### Strengths
**Originality**:  the authors propose amending the ARMED framework to include a fairness regularizer. The combination of mixed effects (as defined by the authors) and fairness is novel.

**Quality**: the authors include multiple datasets and investigate many different attributes, not restricting themselves to binary classification and binary attributes.

**Clarity**: overall the paper is clear, although the RE part of the network could be explained a bit more.

### Weaknesses
 **Originality**: this feels like a minor modification of the ARMED framework, especially as the $L_{CCE}(S,S')$ is the same as the loss on Z.

**Quality**: I believe important baselines are missing, as well as a proper discussion. For instance, the `fairness under distribution shift' is an important related field that is not cited here. Baselines from this field could be implemented, including some that include adversarial losses [1]. From my understanding, there isn't any baseline implemented outside of ARMED, even though Yang et al., 2023 is referenced.

In terms of the motivation of the method, I have major concerns:
- the fairness loss is on the FE part of the network. What prevents the RE part of the network from inducing bias? This is actually suggested by the better fairness results from the FE network compared to its ME counterpart.
- the authors mention that they enforce ‘equality of odds’, but they actually enforce that the model is not able to ‘encode’ the sensitive attribute. These are different criteria, and it is possible for models to encode a signal at the same level but display very different equalized odds [2].

**Significance**: the results seem quite variable (looking at the 95% CI), with obvious overlaps between multiple methods especially when considering unseen clusters. Can the authors discuss the additional complexity of ARMED compared to its variance, and benefit? It would also be good to mention how statistical significance is established (which test, n, and correction for multiple comparison). In addition, please see my question on optimization below.

### Questions
Scalability: the authors investigate different numbers of samples, but the number of features remain small (max 19). Can the authors comment on the implications of e.g. using images?

Optimization: the loss term includes multiple adversaries, mixes of loss types (e.g. cross-entropy with MSE), each with their own parameter. This seems like a difficult function to optimize, as even one term with an adversary can be challenging to converge. Can the authors comment on this?

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This   paper   introduces   a   novel   Fairness-Enhancing   Mixed   Effects   Deep   Learning (MEDL)   framework   that   addresses   two primary   issues   in   traditional   deep   learning (DL):   the   failure   to   account   for   non-independent   and   identically   distributed   (iid) training   samples   in   clustered   data,   and   biases   toward   the   majority   group   in   the training   data,   which   can   have significant   repercussions   in   fields   like   finance   and healthcare.   The   framework   aims   to   enhance   fairness   while   maintaining   prediction performance and interpretability.
The   authors   propose   the   full   fairness-enhancing   ARMED   framework,   which   adds additional   adversarial   debiasing   subnetwork   to   the   original  ARMED   framework   for fairness-promoting.   Authors   claim   that   the   combination   of   ARMED   and   domain adversarial   debiasing   method   significantly   boosts   the   fairness   of   the   model,   and shows   the   consistent  
improvements   of   the   new   framework   across   three   distinct datasets adopted in this study

### Strengths
1. The proposed framework is commendable for its innovative integration of cluster adversary, Bayesian neural networks, and a mixing function, enabling the distinction between cluster-invariant fixed effects (FE) and cluster-specific random effects (RE).
2.   The   robust   empirical   testing   across   diverse   datasets   (census/finance   and healthcare) and task types (classification and regression) validates the framework's applicability and effectiveness.
3.  The   significant   improvements   in   fairness   (up   to   86%   in   some   variables)   without substantial   loss   in   accuracy   is   a   remarkable   achievement,   showcasing   the framework's potential to balance fairness and performance effectively.

### Weaknesses
1. The Results section of the paper mainly explains the improvement of fairness of the   new   framework.   There   is   a   limited   explanation   of   “preserve   interpretability advantages” in the paper, which is mentioned in the abstract. The authors claim that their method preserves interpretability by maintaining the ability to distinguish between cluster-specific and cluster-invariant effects, however, this is not explicitly demonstrated through any specific analysis or example. The paper lacks a concrete example showing how the learned fixed effects (FE) and random effects (RE) can be separately interpreted in the context of the datasets used, and how this interpretability is preserved when fairness-enhancing modifications are applied. For instance, a detailed analysis of how specific features contribute to FE and RE, and how these contributions change with the fairness modifications, would be necessary to support the claim.
2. In section 3.1, the authors state that “while both Domain Adversarial Debiased (fair DA   adv.   deb.)   and   Domain   Adversarial   with   absolute   correlation   (fair   DA   ACL) enhance fairness, fair DA adv. deb. exhibits a more consistent fairness improvement across all sensitive variables.” Given the results in Table 1, it is difficult to see that fair DA  adv.  deb.  exhibits  a  more  consistent  fairness  improvement.  For  many  sensitive variables, the TPR or FPR standard deviation of fair DA ACL is smaller than fair DA adv.   deb..   Especially   for   the   Marital-status   feature   on   occupations   seen   during training and Sex feature on occupations unseen during training, fair DA ACL has both TPR   and   FPR   standard   deviation   smaller   than   fair   DA  adv.   deb.,   which   indicates
better fairness according to the paper. Authors then state that “Moreover, fair DA adv. deb. enhances fairness with minimal
reduction   in   balanced   accuracy   compared   with  fair   DA ACL—1%   vs   1.6%.   Given these   findings,   we   chose   to   incorporate   fair   DA   adv.   deb.   into   the   ARMED framework”.   The   balanced   accuracy   between   fair   DA ACL   and   fair   DA  adv.   deb. seems to be quite small and does not give a convincing reason for choosing fair DA adv. deb. over fair DA ACL. The difference in balanced accuracy is marginal, and the standard deviation of TPR and FPR, which the authors use to measure fairness, is often lower for fair DA ACL. A more rigorous justification is needed for selecting fair DA adv. deb., possibly by considering other evaluation metrics or providing a more detailed analysis of the trade-offs.
3: I would like to congratulate the authors on publishing their paper on TPAMI, however, ICLR is a decent venue for machine learning too. Advertising ARMED (Sec 2.2) can hardly be part of "Methods" as it is not an innovation/contribution in this paper. Note that unlike many conferences in signal processing, conference papers in top ML venues are not shortened versions of journal papers. You need to be substantially different and innovative from earlier works. Besides, the purpose of double blind is to remove the selection bias in favor of big names. As a reviewer for ICLR, knowing you have a TPAMI paper will not really affect my rating.

### Questions
There are too few baselines to conclude that the experiments are comprehensive enough to demonstrate its fairness. 
The   authors   incorporate   fair   DA  adv.   deb.   instead   of   fair   DA ACL  into   the  ARMED framework based on their findings of the ablation study in section 3.1. But the reason for choosing fair DA adv. deb. over fair DA ACL is somehow not very convincing.
Authors can try to use the absolute correlation loss mentioned in fair DA ACL for the full fairness-enhancing ARMED framework, then make a comparison with the original proposed full fairness-enhancing ARMED.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The research paper presents an enhancement to the ARMED framework, aiming to improve fairness concerning fairness-sensitive variables like age, sex, and race. Although the original ARMED framework provided commendable generalization for out-of-distribution (OOD) data, it suffered from biases towards predominant groups. To address this, the authors incorporated adversarial debiasing (adv. deb.) and absolute correlation loss (ACL) into the existing domain adversarial (DA) model, a component of the ARMED framework.

Three distinct models were compared: the DA model, the fair DA adv. deb. model, and the DA ACL model. Among these, the fair DA adv. deb. model consistently exhibited enhanced fairness. Consequently, by integrating these modifications for both fixed and mixed effects, the authors devised a Fairness-enhancing ARMED framework. This refined model not only maintained a similar accuracy to the existing ARMED baseline but also exhibited considerable fairness improvements for classification tasks and better mixed effects fairness predictions in regression.

The study further showcased the model's efficacy using three datasets: the ADULT dataset, IPUMS dataset, and Heritage Health dataset. When pitted against existing neural networks, the "Fair" model, which synergized components from both the DA and ARMED models, produced superior fairness predictions across nearly every fairness-sensitive variable.

A significant contribution highlighted in the paper is the inclusion of sub-networks, specifically the Adversarial Classifier A_F and the Adversarial Classifier A_m, to the ARMED framework. The paper's findings serve as foundational work, promoting enhanced fairness and reliability in machine learning outputs, particularly in handling OOD data and emphasizing mixed effects fairness predictions in regression scenarios.

### Strengths
Originality: The paper addresses the pressing issue of bias in deep learning models, especially when it comes to fairness-sensitive variables. By melding the ARMED framework with domain adversarial techniques, the research manages to elevate both fairness and reliability in its predictions.

Quality: A prominent improvement is evident through a significant reduction in standard deviation , reflecting the enhanced quality of the model. The proposed model, which synergizes ARMED and DA techniques, exhibits superior performance when dealing with out-of-distribution data and fairness-sensitive variables.

Clarity: The research offers insights into the application and outcomes of various methods. 

Significance: Manage the challenge of out-of-distribution data in deep learning, while ensuring fairness, accentuates its pivotal role in the advancement of the field.

### Weaknesses
Originality:
- The paper seems to predominantly enhance the existing ARMED model by integrating two adversarial debasing components. The modification, while valuable, might not be perceived as groundbreaking, especially when viewed against the backdrop of the existing literature.
- The work appears to be an iteration of the ARMED model rather than a transformative leap, raising concerns about the overall novelty and the magnitude of the paper's impact.

Clarity:
- Several figures and illustrations used in the paper closely resemble those from the original ARMED paper. This reuse of content, without adequate new context, can create confusion.
- Some terms, which although might be secondary in the context of this paper, are left undefined. Terms like "h", "𝛽", and "m", for instance, need clear explanations or references, even if briefly, to maintain reader continuity.
- The introduction contains superfluous discussions on traditional deep learning's weaknesses and excessive literature references with insufficient explanations. This can dilute the paper's main message and confuse readers.
- Explanations on the merging of the ARMED and Domain Adversarial models, particularly in Figure 1, are vague. A detailed breakdown or a supplementary diagram could enhance clarity.

Quality:
- The paper seems to underemphasize the importance of well-established fairness criteria. Metrics like equalized odds or demographic parity should be discussed more prominently, rather than lesser-known metrics such as TPR stdev or FPR stdev's mean and CI.
- Although the results are analyzed thoroughly, the overall experimental setup and methodology appear to lack depth. Without a comprehensive understanding of the experiment's design and employed metrics, the derived results might seem less credible.
- There's an observable absence of detailed visualizations in the experimental sections, reducing the impact and clarity of results presented.
- Explanations for certain core concepts like Fixed effect, Random effect, and Mixed effect are either missing or insufficiently highlighted. Such crucial components warrant a dedicated section, possibly in the introduction or an appendix.

Significance:
- While performance improvements are highlighted, the paper could benefit from a more persuasive argument showcasing how significant these improvements are in the larger context.
- Drawing direct visual and textual comparisons to the older ARMED model, without differentiating the advancements made in the current paper, might diminish its perceived value.

### Questions
- How does the addition of two adversarial debasing components differentiate your work from the original ARMED model substantially? Could you elaborate on the unique challenges and solutions introduced in this iteration?
- In the figures that resemble those from the original ARMED paper, are there any significant alterations or modifications that readers should be aware of? If so, could these be highlighted or differentiated more clearly?
- What led to the decision to focus on metrics like TPR stdev or FPR stdev's mean and CI instead of the more conventionally used fairness metrics such as equalized odds or demographic parity? How do the chosen metrics enhance the study's objectives?
- Is it possible to incorporate more detailed visualizations in the experimental sections to enhance clarity and understanding of the results? (I've seen curves which includes two axes - performance and fairness)
- Given the stated performance improvements, could you contextualize them more persuasively? How do these improvements translate to real-world applications or the larger academic context?
- There seems to be a strong emphasis on the paper's results. Could you provide more comprehensive background on the relevance and significance of these results in the context of existing research or practical applications?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper extends the previous ARMED framework with adversarial neural networks to enhance fairness. It shows improvements in fairness across sensitive variables in various datasets.

### Strengths
1. The paper has tested the proposed method on a diverse set of real-world datasets from finance and medicine, showing improvements in fairness.

### Weaknesses
1. The paper is very poorly written. The structure is not well-presented, and there are many grammar errors.
2. The fairness issue is addressed with domain adversarial neural networks, which is common.
3. The mathematical definitions are unclear. Only several losses are introduced without any detailed interpretation. 
4. It's unclear how the proposed method identifies new unseen clusters with an adversarial classifier.
5. There is no justification for why the proposed method can improve equality-of-odds fairness.

### Questions
Please see the previous section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
