# Cauchy-Schwarz Fairness Regularizer

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
In this paper, we propose a novel approach to fair machine learning, the Cauchy-Schwarz fairness regularizer, which minimizes the Cauchy-Schwarz divergence between the prediction distribution and sensitive attributes. While existing methods effectively reduce bias as indicated by low values on specific fairness metrics, they frequently struggle to achieve a balanced performance across various fairness definitions. For example, many approaches may successfully attain low demographic parity yet still demonstrate significant disparities in equal opportunity. Theoretical studies have shown that the Cauchy-Schwarz divergence provides a tighter bound compared to the Kullback-Leibler divergence and gap parity, suggesting its potential to improve fairness in machine learning models. Our empirical evaluation, conducted on four tabular datasets and one image dataset, demonstrates that the Cauchy-Schwarz fairness regularizer achieves a more balanced performance across fairness metrics while maintaining satisfactory utility. It outperforms existing fairness approaches, providing a superior trade-off between fairness and utility. In addition, the Cauchy-Schwarz fairness regularizer is a versatile, plug-and-play fairness regularizer that can be easily integrated into various machine learning models to promote fairness.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents a novel fairness regularizer for machine learning models based on the Cauchy-Schwarz divergence. The proposed method aims to address the limitations of existing fairness regularizers by providing a better balance across multiple fairness definitions, including Demographic Parity and Equal Opportunity. Traditional methods often do well in one fairness metric but fail in others; this paper argues that the CS regularizer improves overall fairness performance by minimizing prediction disparities between sensitive attribute groups. The empirical results, validated on four tabular datasets and one image dataset, demonstrate that the CS regularizer achieves a better trade-off between fairness and utility, outperforming state-of-the-art fairness approaches.

### Strengths
1.  Leveraging Cauchy-Schwarz divergence as a fairness regularizer is a contribution with theoretical advantages over traditional metrics like DP, KL, and MMD.

2. The experiments on diverse datasets, including both tabular and image data, strengthen the evidence of the CS regularizer's effectiveness across domains and tasks​​.

3. The evaluation and comparison are comprehensive and convicing.

### Weaknesses
1. The paper begins by highlighting the challenge that many fairness regularizers can achieve DP but fail to address EO effectively. It sets the expectation that the proposed method will tackle this inconsistency between fairness definitions​. However, CS divergence is more naturally aligned with DP rather than EO​. In theory, it is unclear how CS achieves EO​.

2. The theoretical properties and guarantees come from the nature of CS divergence rather than the fair regularizer, making this paper with limited contribution.

3. While the paper explains how CS divergence reduces DP, it does not establish a clear theoretical or empirical link to how CS divergence addresses EO. 

In general, my major concern is the gap between motivation and the proposed method.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors address supervised learning under fairness constraints. The main objective of this paper is to construct a learning algorithm that achieves both demographic parity and equalized odds, two different fairness definitions, simultaneously. To this end, the authors propose using the Cauchy-Schwarz divergence to measure the disparity in the predictor's outputs across groups defined by a sensitive attribute. This measure is incorporated into the objective function of standard supervised learning as a penalty term. Experimental results demonstrate that the proposed method achieves optimal fairness with respect to equalized odds while also maintaining fairness in terms of demographic parity.

### Strengths
This paper addresses the important topic of fairness in supervised learning, which is highly relevant to the conference's focus areas.

The empirical evaluations show that the proposed method achieves superior fairness in terms of equalized odds while simultaneously preserving demographic parity, compared to several existing methods, including FairMixup, MMD, HSIC, and the prejudice remover.

### Weaknesses
The paper omits several significant existing works, leading to some ambiguity in its contributions. First, demographic parity and equalized odds are conflicting fairness definitions, meaning that no predictor with reasonable accuracy can satisfy both demographic parity and equalized odds simultaneously. This issue has been studied in:
- Kleinberg et al., "Inherent Trade-Offs in the Fair Determination of Risk Scores," ITCS'17. 

Building on this, the motivation of the paper is questionable.

While demographic parity and equalized odds are conflicting goals, it may still be valuable to achieve the best possible approximation of both. A recent study develops a fair supervised learning method that optimizes the trade-off among accuracy, approximate demographic parity, and approximate equalized odds:
- Hsu et al., "Pushing the Limits of Fairness Impossibility: Who's the Fairest of Them All?" NeurIPS'22. 

This method appears to achieve a similar goal to the one proposed here, with the added benefit of allowing control over the priority between demographic parity and equalized odds. A comparison with this method is essential to demonstrate the effectiveness of the proposed approach.

Additionally, the paper lacks a clear explanation of how imposing the Cauchy-Schwarz divergence contributes to achieving fairness in terms of equalized odds. The proposed unfairness measure is based on demographic parity, focusing on disparities in the predictor’s output distributions across groups, using a specific choice of divergence to quantify these disparities. While this measure naturally evaluates unfairness in terms of demographic parity, it is less clear how it relates to equalized odds. A more detailed explanation of the mechanism by which the proposed measure influences equalized odds would enhance the reader’s understanding of the method's value.

The theoretical contributions of the paper are limited. Although the authors claim that Proposition 2 demonstrates the tightness of the proposed measure, it merely shows inequalities between the Cauchy-Schwarz and KL divergences. Having a lower value than the KL divergence is not a meaningful property, as it could simply be due to scale differences. For example, several other divergences—including total variation distance, Hellinger distance, and chi-square divergence—also exhibit this property due to Pinsker's inequalities.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose using Cauchy-Schwarz (CS) divergence as a fairness regularizer to achieve balanced fairness across multiple metrics, particularly focusing on demographic parity (DP) and equal opportunity (EO). They highlight a common limitation in fairness approaches, where optimization for one metric often results in poor performance on others. In their experiments, CS divergence not only reduces DP but also minimizes EO disparity, demonstrating superior trade-offs between fairness and utility. The experimental results are extensive, covering different datasets, models, and tasks, and comparing the CS regularizer with existing fairness methods.

### Strengths
- The proposed regularizer achieves lower DP and EO simultaneously, which mostly beats existing methods. Also, the proposed regularizer has minimal sacrifice in terms of utility, such as accuracy and AOC.
- Although CS divergence is a known method for different areas(domain adaptation), it is a novel idea to apply it for fairness. 
- The paper has a comprehensive experimental results section. They do consider several different perspectives, accuracy and fairness metrics, the tradeoff between accuracy and fairness, T-SNE plots, and hyperparameter sensitivity.

### Weaknesses
 - The justification in Section 3.2 is unclear. While the authors argue that CS divergence is more effective for fairness, their supporting points seem to describe general properties of CS divergence rather than directly connecting these to fairness goals like DP and EO. Specifically, the explanation lacks a clear articulation of how the mathematical properties of CS divergence translate to improved performance in reducing disparities in DP and EO. The proof of Proposition 2 is not clear and I think that it misses a few steps. The same proposition exists in [1], it could be just cited.
- The authors focus exclusively on DP and EO in their experiments, despite the abstract implying broader applicability. This might give readers an impression of using more than only these two notions, which could be more accurately scoped in the abstract. The lack of evaluation on other fairness metrics limits the generalizability of the proposed method. For example, it is unclear if the method would be effective for notions like equalized odds or predictive parity.
- The overall structure of Section 3 could benefit from clearer organization. The explanations sometimes feel disjointed, making it challenging to follow the logical progression of arguments. The flow between the theoretical motivation, the mathematical formulation, and the practical application of the CS divergence is not smooth, which hinders the reader's understanding.

### Questions
- Could the authors extend the CS regularizer to support fairness notions beyond demographic parity (DP) and equal opportunity (EO)? For instance, would a CS-based approach also be effective for other fairness definitions, such as equalized odds? Additionally, if the CS regularizer is tuned specifically for EO, does it still achieve significant improvements in DP?
- It is interesting to see that a higher value of $\alpha$(the coefficient in front of the regularizer) causes a higher disparity in Figure 5. Could the authors provide more insights why it happens?
- Have the authors considered using multiple regularizer terms simultaneously, such as combining a DP-based KL divergence regularizer with an EO-based KL divergence regularizer, to achieve lower disparities in both DP and EO? This approach could allow existing methods to balance multiple fairness metrics. If not explored, could the authors provide insight into whether such a combination could improve multiple disparities, or might it lead to conflicts or diminishing returns in fairness and accuracy?

List of typos, and confusions:

- Pg3, Line 119. The sentence discussing the extension of DP and EO to multiple sensitive attributes might fit better after defining EO rather than before.
- Pg3, Line 153. It would improve clarity to switch the order of the phrases "The proof of this..." and "...where $\kappa$...".
- Pg4, Line 178. The parameter is $\lambda$ not $\beta$.

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
4

### Summary
This paper presents an in-processing fairness methodology, a *Cauchy-Schwarz Fairness Regularizer.* The authors consider two popular group fairness metrics in the binary classification setting: *Statistical Parity* and *Equalized Odds.* The proposed method optimizes for standard classification accuracy (through binary cross-entropy loss) while tacking on a regularizer that measures the "Cauchy-Schwarz Divergence" between two distributions: $\mathrm{Pr}(\hat{Y} \mid S = 0)$ and $\mathrm{Pr}(\hat{Y} \mid S = 1)$, the distributions of the classifier conditional on the sensitive attribute applying or not applying ($\hat{Y} \in \{0, 1\}$ is the output of the classifier, supposedly on a given example, and $S \in \{0, 1\}$ is the sensitive attribute). The authors claim that the Cauchy-Schwarz divergence give a couple of intuitive explanations for why this regularizer might be better than existing regularizers based on known divergence measures such as KL divergence, maximum mean discrepancy, and simply regularizing based on mean demographic parity rates. Then, they conduct a suite of experiments and show that the Cauchy-Schwarz Fairness Regularizer consistently achieves good simultaneous Equalized Odds and Demographic Parity, with small sacrifices to accuracy, compared to the other baseline fairness regularizers based on discrepancy measures.

### Strengths
**Originality:** The paper does present a new (to my knowledge) idea in using a Cauchy-Schwarz divergence to regularize their fairness objective. However, I believe that the extent of the original contribution is the use of a different divergence metric to simply regularize binary cross-entropy loss, providing yet another in-processing fairness method based on a simple and standard modification to incentivize the classifier's prediction distributions to be similar across sensitive attributes. The authors also don't provide much past a couple of surface-level remarks comparing their choice of discrepancy ("Cauchy-Schwarz divergence") to other standard divergences. For example, it is unclear whether *Proposition 2* even means anything salient in the context of this study. The authors claim that the CS divergence has "tighter error bound" than KL divergence and proceed to justify this (without any further explanation) by referencing the fact that the CS divergence between two Gaussians is always smaller than the KL divergence between two Gaussians. It is unclear to me why this would be an attractive property past the fact that the units representing the divergence between two distributions is simply smaller than the units with KL divergence, as the authors use the CS divergence to measure discrepancy between the two distributions directly. More on this in *Weaknesses.*

**Quality:** The authors present a comprehensive suite of experiments on popular fairness datasets. The Experiments section is relatively well-organized, and the results seem significant, at least in relation to the chosen baselines (although it isn't clear to me that these are the right baselines, see *Weaknesses*). The quality of the experimental results, overall, seem promising when taken at face value, but it is unclear to me whether the presented baselines are sufficient. 

**Clarity:** The paper's presentation is generally clear and well-written, at least in organization. The sections flow in a readable way, and the authors take care in presenting their results in an interpretable manner. However, (see *Weaknesses*) there are numerous typos that overall obscure the clarity in the more technical statements, particularly in Section 3. Of particular note is Section 3.2, where the authors present some relatively hand-wavy "reasons" why the CS divergence measure might be a better choice than other divergence measures. In these sections, I found that the explanations from the authors were often lacking in rigor or depth. The Experiments section and the accompanying Appendix for the experimental details, however, seemed well-written and clear, at the least.

**Significance:** As stated above, I don't find this technique particularly novel past the use of simply adjusting a measure of distance in the regularizer for a standard binary classification objective. To make this a stronger paper, I believe that Section 3 should be substantially stronger, and sharper proofs and theorems should be given to compare the CS divergence measure to existing divergence measure, and, perhaps, prove some theorems that state its properties either in-sample or out-of-sample. However, these details are missing from the current state of the paper.

### Weaknesses
I have pointed out several weaknesses in the *Strengths* section. Overall, I don't believe this paper is in the state to be published, for several reasons. I believe there are serious limitations to consider and revisions to be made to the paper, and the it is unclear to me whether the main result is at all significant. To elaborate further:

**Typographical or clarity confusion.** Although the paper is overall clear and well-written, there are numerous flaws in the presentation of many of the technical statements in the paper. I would suggest in some of the more technical portions:

- In Equations 1 and 2, it should be mentioned that these notions maintain *in expectation* over all of the input space. That is, $P(\hat{Y} = 1 \mid S = 0)$, for example, holds in expectation over all $X$. In fact, it is slightly unclear that your random variable $\hat{Y}$ subsumes the dependence on $X$. I would either add that to the notation as well, to indicate dependence on the input. This is especially important in your later exposition, when you define probability densities over the input space that depend on the predictions $\hat{Y}$.
- On that above point, it might be helpful in general to have a separate "Notations" section to get this stuff straightened out.
- Equation 5 should have the two losses depend on the parameter $\theta$. This is a nitpick, but writing a minimization problem over a parameter when your functions don't depend on a parameter isn't quite clear.
- Nitpick: You say, "the parameter $\beta$" when it should (I think) be $\lambda$.
- Equation 6: The notation here is unclear --- you say that $p$ and $q$ are densities, so $p(\mathbf{x}_i)$ and $q(\mathbf{x}_j)$. Densities are zero on points, so $DP(p;q)$ is always zero. Perhaps you mean to write this with indicators on $\mathbf{x}_i^p$ and $\mathbf{x}_i^q$?
- Remark 1: While the proof in the Appendix seems correct, this seems to be a bit of a non sequitur. How are we meant to interpret this random factoid? Plus, $\mathbf{mu}_p$ and $\mathbf{mu}_q$ are undefined in this remark.
- In the HSIC, $L$ is defined and never used; perhaps in Equation 9 you mean to use $L$ instead of $Q$?
- Equation 11: I believe this would be much clearer if you introduced the dependence on $\mathbf{x}$. Written in Equation 11, $\mathbb{P}$ and $\mathbb{Q}$ seem to be just numbers (you present these distributions as average rates over for the classifier over $S = 0$ and $S = 1$).
- Equation 12: the dependence on $\theta$ should be made explicit (every term should depend on $\theta$).
- Table 1 and Experimental Results: The definition of each baseline should be included in the main body, not the appendix.

**Section 3: Insufficient rigor in justifying the CS divergence.** Overall, I found Section 3 seriously lacking in rigor or depth, particularly in the presentation of the "three key reasons" in Section 3.2. For the first reason, it is unclear without a rigorous statement what the authors mean by "closed-form solution for the mixture of Gaussians." The authors just state this without providing further rigorous justification or explanation, and then they simply cite a couple of additional references without any further justification of why this might be particularly helpful in this application.  For the second reason, it is unclear why the divergence from CS being smaller than KL provides any particular advantage at all, as the authors are just using it as a regularizer. Why would this scale matter at all in the regularization? What do the authors mean by "tighter error bound?" Why does the justification with Gaussian data have any bearing on the experimental results? These questions all should be answered in a revision, as they are unclear to me. The third reason is doesn't give any references and provides a non-rigorous, vague explanation comparing CS divergence to MMD and DP as divergences. I found this explanation particularly "hand-wavy," as it relies on no mathematical justification or experimental backing. Overall, the explanation behind the mechanism of the CS regularizer is unclear, and I did not gain any insight from its comparison to other divergence measures in Section 3. I believe that, if the CS divergence really is a worthwhile object of study, there should be much more rigorous justification of its properties in Section 3.

**Section 4: Insufficient suite of experiments.** Although it makes sense to compare to other inprocessing techniques for fairness, it would be helpful to also compare these baselines to other fairness techniques at other stages of the pipeline, particularly preprocessing and postprocessing. In particular, I believe that this would provide a more comprehensive suite of experimental results especially because the authors make no theoretical connections between the objective and the out-of-sample performance.

### Questions
The main question I am still confused above from this work that was not addressed was how these results are compatible with the classic "Impossibility Theorem" of Fair ML. In particular, it is well-known (see, e.g. Kleinberg, Mullainathan, Raghavan 2016) that it is impossible to achieve simultaneous Statistical Parity and Equalized Odds under relatively mild conditions on the binary classification problem. However, this is exactly what the authors of this paper seek to achieve with the CS regularizer, and one of their main stated contributions is a *simultaneous* control of both. However, this classic impossibility result is not cited in the paper. In light of this result, it seems to me that another plausible explanation of the experimental results isn't that it can "improve fairness for both DP and EO" as Section 4.3 suggests, but, rather, that it is just a good regularizer for EO proper. 

My main question is: how does the CS regularizer stand in light of the impossibility result? Of course, I believe that the impossibility result applies to DP = 0 and EO = 0, but I believe that it throws one of the contributions and motivations of this paper into question.

Along with this question, several others (also raised in the above sections) are:
- How does this method fare in comparison to preprocessing and postprocessing methods?
- Are there more rigorous justifications for the CS regularizer than the ones mentioned in Section 3?

### Soundness
1

### Presentation
2

### Contribution
1
