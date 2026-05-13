# On Information-Theoretic Measures of Predictive Uncertainty

- Decision: Reject
- Scores: 5, 3, 3, 1, 3

## Abstract
Reliable estimation of predictive uncertainty is crucial for machine learning applications, particularly in high-stakes scenarios where hedging against risks is essential.
    Despite its significance, a consensus on the correct measurement of predictive uncertainty remains elusive.
    In this work, we return to first principles to develop a fundamental framework of information-theoretic predictive uncertainty measures.
    Our proposed framework categorizes predictive uncertainty measures according to two factors: \textbf{(I)} The predicting model \textbf{(II)} The approximation of the true predictive distribution.
    Examining all possible combinations of these two factors, we derive a set of predictive uncertainty measures that includes both known and newly introduced ones.
    We empirically evaluate these measures in typical uncertainty estimation settings, such as misclassification detection, selective prediction, and out-of-distribution detection.
    The results show that no single measure is universal, but the effectiveness depends on the specific setting. 
    Thus, our work provides clarity about the suitability of predictive uncertainty measures by clarifying their implicit assumptions and relationships.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a framework of predictive uncertainty measures by categorizing them as cross entropy between different pairs of predictive and (approximations of) true models. This encapsulates several known uncertainty measures as well as derives new ones. The authors show that the aleatoric (irreducible) and epistemic (reducible) components of uncertainty can be represented as conditional entropy and KL divergence respectively, as current uncertainty measures traditionally use both of these quantities, or expectations of these quantities, the authors explain the relationship between their uncertainty quantification and other methods. They then demonstrate their method of quantifying predictive uncertainty over 3 potential model setups: a preset model, a Bayesian average, and over all possible models. Experiments show that the efficacy of uncertainty measures depends heavily on the task, chosen model, and posterior sampling method.

### Strengths
The authors clearly show how each uncertainty quantification measure can be related back to cross entropy. This provides a clear categorization and interpretation of existing measures based on different choices of true and predictive models. Making these assumptions explicit is valuable for users to benchmark and choose the appropriate methods.

The paper is also easy to follow with a clear summary in Table 1.

### Weaknesses
The main contribution of the paper seems to be the theoretical framework categorizing uncertainty quantification measures based on cross entropy, but much of the experiments focus on evaluating the effects of different posterior sampling methods. It is unclear why these methods specifically were significant for the comparison, and if there are any theoretical relationships between different posterior sampling choices and uncertainty measures. Moreover, the main theoretical contribution is not quite significant considering that many existing works already classify their measures as being cross entropy between predicting and true models, which breaks down into a sum of aleatoric and epistemic uncertainty (e.g. Schweighofer et al., 2023b)

In breaking down the total uncertainty into aleatoric and epistemic uncertainty, the authors use aleatoric uncertainty to mean the uncertainty arising from using the selected predictive model, rather than the standard definition in the literature about inherent uncertainty in the true distribution. This seems counterintuitive to me and could be a potential source of confusion for many readers. For example, if the predictive model perfectly matches the true distribution, the aleatoric uncertainty would be zero under the standard definition, but not under the authors' definition. This discrepancy needs to be addressed more clearly.

I could not really see some of the claims made by the authors about the empirical results, although it may be because the figures are very small and many points/plots overlap. For example, in Section 5.3 Figure 4, the results seem mixed to suggest that “TU (A3) performs best”. The performance differences between the uncertainty measures are not clearly visible, making it difficult to validate the claims made in the text. Furthermore, the lack of statistical significance testing makes it difficult to determine whether the observed differences are meaningful or simply due to random variation.

### Questions
In the cases with the same choices for the predicting model and the (approximate) true model (A1, B2, C3), it was not clear how the predicting model differs at all with the approximation of the true predictive distribution, because the model is often learned to best fit the true distribution. 

The experiments focused on comparing posterior sampling methods felt very unexpected after almost no mention of them in the main Section 3. I think discussing their significance earlier, as well as any categorization of implicit assumptions they make similar to that of uncertainty measures, would really strengthen the paper. 

Around line 110: “the entropy of the posterior predictive distribution has been found to be inadequate…criticised on grounds of not fulfulling certain expected theoretical properties”. Could the authors clarify specifically what made them inadequate and how this work addresses it?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper considers the uncertainty quantification problem for a machine learning model; it aims to develop an uncertainty measure that captures the uncertainty of an ML model on predicting one data sample. It proposes a set of uncertainty measures and compares their performances on selective prediction and mistakes/OOD detections.

### Strengths
The paper provides a good description of the two types of uncertainty, and this gives a good account for the existing literature on uncertainty measures.

### Weaknesses
My main concern is that the paper looks more like an experiment report rather than a research paper:

First, I agree that the proposed cross-entropy loss (5) is a reasonable uncertainty measure. However, there are several issues:
- It assumes there exists a true parameter that governs the generation of the data samples, which can be easily violated and hard to verify for a specific dataset. This assumption is particularly problematic in real-world scenarios where data distributions are complex and may not adhere to a simple parametric model. The lack of robustness to deviations from this assumption severely limits the practical applicability of the proposed measure.
- All the newly proposed uncertainty measures in this paper serve as an approximation of (5). There is no principled way to know if these approximations are better than the existing ones. For a dataset at hand, one could use validation data to choose the proper uncertainty measure; there is no evidence that the proposed measures in Table 1 is better than the other existing ones for sure. The paper does not offer any theoretical justification for why these specific approximations should be preferred over others, nor does it provide a comparative analysis against a broader range of existing uncertainty measures.
- The paper has its title as "information-theoretic" but the proposed measure (5) and those in Table 1 have no theoretical guarantee. The connection to information theory is tenuous at best, and the lack of theoretical grounding undermines the claim of an information-theoretic approach.

Second, all the proposed measures seem very natural; they don't provide new insights for people working on uncertainty quantification. As I mentioned above, when you have a new dataset at hand, you still have to run all the uncertainty measure and use the validation data to pick one. The measures lack novelty and do not offer a significant advancement over existing methods. The paper does not provide any compelling reason to adopt these measures over existing, well-established techniques.

Third, the proposed framework doesn't account for the uncertainty calibration procedure which is commonly used in the existing practice of uncertainty quantification. Specifically, we can think it in this way: the proposed measures are all zero-shot in that it relies solely on the trained ML model, but the uncertainty calibration can utilize the validation data (or a reserved dataset unseen during the training) to refine the uncertainty estimate. This omission is a significant oversight, as calibration is crucial for ensuring that uncertainty estimates are reliable and can be used for decision-making.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a framework for categorizing information-theoretic measures of predictive uncertainty. It addresses the need for reliable uncertainty quantification in machine learning, especially in high-stakes applications where accurate prediction of uncertainty is crucial. By categorizing these measures based on assumptions about the predicting model and how the true predictive distribution is approximated, the authors unify existing measures and introduce new ones. They identify the cross-entropy between the predicting model and the true model as a fundamental uncertainty measure, though generally intractable. Empirical evaluations demonstrate that no single measure is universally best, as effectiveness depends on the specific application and sampling method used. The work clarifies relationships among measures, guiding more informed choices in uncertainty quantification.

### Strengths
- Introduces a comprehensive framework for predictive uncertainty based on cross-entropy between the predicting and true models, adding a novel, theoretical foundation to uncertainty quantification.

 - Expands on existing information-theoretic measures by categorizing them under a unified approach, highlighting relationships and assumptions that were not fully articulated in prior works.

 - Derives the framework from first principles, establishing robustness in theoretical grounding.

### Weaknesses
In my opinion, the paper fails to explain how the presented framework can be of help to better understand the different information-theoretic measures that can be derived from it. I am mostly critical about the analysis given in the experimental section. I was expecting, for example, a more insightful discussion about which are the limitations for properly quantifying uncertainty of the different approximation approaches of the true predictive distribution. However, Section 5 provides a  lot of experimental data, but there are not useful insights connecting this experimental data with the presented framework. In consequence, the paper does not enhance the understanding of when and how different uncertainty measures perform effectively. The experimental section lacks a clear methodology for evaluating the uncertainty measures. It is not clear how the different approximation methods are compared, and what metrics are used to assess the quality of the uncertainty quantification. The discussion does not delve into the practical implications of the observed results, leaving the reader without a clear understanding of the trade-offs between different measures in real-world scenarios. For instance, the paper does not discuss the computational cost of each measure, which is a critical factor in practical applications.

### Questions
I have found Section 3.1 a bit hard to follow. Consider the use of acronyms instead of number of letters to refer to the different options

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
In the paper, authors introduce a framework that allows for derivations of different measures of predictive uncertainty quantification. For this, authors suggest Cross-Entropy between predicted and true distributions as a measure of total (predictive) uncertainty. Using this as a starting point, they, following prior work, derive the framework.
Authors evaluate resulting measures of uncertainty in different downstream tasks.

### Strengths
While the paper is overall well-written and easy to follow, it has significant weaknesses (see below).

### Weaknesses
I see two major drawbacks in the paper under review, both of which are significant enough that addressing them properly would fundamentally alter the paper's selling point. Specifically, these are:

1. The proposal of Cross-Entropy (CE) between the predicted distribution and the true distribution as a measure of total uncertainty, leading to new definitions of aleatoric uncertainty (AU) and epistemic uncertainty (EU).

2. The relation to prior work and the correct positioning of the paper within the existing literature.

----

## Cross-Entropy and the definitions of AU and EU

One of the paper's main selling points, as mentioned in the abstract, is "returning to first principles to develop a fundamental framework of information-theoretic predictive uncertainty measures." This is an excellent motivation. However, what are these first principles?

The most important equation in the paper, and seemingly the "first principle" referred to, is Equation 5. In this equation, the authors consider the CE between the predicted distribution and the true distribution as a measure of total (predictive) uncertainty. Since CE is not a symmetric function, the order of arguments is crucial—a point I want to emphasize.

In the literature, there are papers (cited in the work under review but not properly discussed) that derive the reverse order of arguments, i.e., CE between the true and predicted distributions, and use it as a measure of total (predictive) uncertainty. In those papers [discussed below], this order was indeed derived from first principles. Specifically, they introduce a general notion of error via statistical risk, consider a specific class of loss functions, and then derive CE as a measure of total uncertainty—with the reverse order of arguments compared to the paper under review. It can be shown that CE with that (reverse) order of arguments can be decomposed into components that align with conventional definitions of AU and EU: AU is irreducible and depends solely on the true $p(y \mid x)$, while EU is reducible, given a more accurate model.

Therefore, the order of arguments presented by the authors is conceptually different and should be well-motivated. However, the entire motivation provided boils down to a sentence in lines 121-122: "We *propose* to measure predictive uncertainty with the cross-entropy between the predictive distributions of a selected predicting model and the true model." The authors do not derive it from first principles, as mentioned in the abstract, but rather propose it as a heuristic. It's acceptable to propose a heuristic if it's useful and doesn't contradict prior work.

This proposed order of arguments leads to the decomposition in Equation 5. **In this decomposition, AU is defined as fundamentally reducible** (it depends solely on the estimate or model, not the true distribution), which contradicts a substantial body of research and acknowledged papers. It even contradicts the sentence in lines 71-74 of the current paper.

From a common-sense perspective, it's unclear why these newly proposed definitions are acceptable. By these definitions, AU and EU are fundamentally interrelated, and changing the selected model **will change the true AU**. To me, this makes no sense. Changing a predictive model can change only our estimate of the true AU, not the true AU itself.

The authors attempt to provide motivation for this controversial redefinition in a dedicated paragraph (lines 142-149). To support their claims, they refer to three papers: Apostolakis (1990) and Helton (1993; 1997).

However, a closer consideration of these papers does not support the authors' claims. None of these papers state that the true aleatoric uncertainty is the reducible uncertainty.

Specifically:

> Helton 1993 follows the conventional definitions of AU and EU (referred to as uncertainty of type A and type B, respectively). In Section "X. Discussion," they refer to prior work and align the definitions of uncertainties with their equations: "The IAEA report defines type A uncertainty to be stochastic variation; as such, this uncertainty corresponds to the frequency-based probability of Kaplan and Garrick and the $pE_i$ of Eq. (1). Type B uncertainty is defined to be uncertainty that is due to lack of knowledge about fixed quantities; thus, this uncertainty corresponds to the subjective probability of Kaplan and Garrick and the distributions indicated in Eq. (6)."

> Helton 1997 (same author) follows the conventional definitions: "Alternate names include aleatory, type A, irreducible and variability as substitutes for the designation stochastic, and epistemic, type B, reducible and state of knowledge as substitutes for the designation subjective." Moreover, Helton et al. emphasize the importance of correctly distinguishing between these sources: "When an appropriate separation between stochastic and subjective uncertainty is not maintained, rational assessments of system behavior become difficult, if not impossible..."

> Apostolakis (1990) distinguishes between "State-of-Knowledge Uncertainties" (uncertainty in the parameters of the model, hence epistemic) and "Uncertainties in the Model of the World" (e.g., even with perfect knowledge of parameters, we still cannot predict certain events, hence aleatoric).
For practitioners, it might not be crucial to distinguish between AU and EU; rather, it's useful to know the "total" uncertainty: "The distinction between the conditional model-of-the-world probabilities [results in AU]... and the probabilities for the parameter [results in EU]... in the same example is merely for our convenience in investigating complex phenomena."

Therefore, in none of these papers do the authors define or consider true AU as something reducible. Given this, proposing the CE between predicted and true distributions as a measure of total (predictive) uncertainty is not well-motivated. It appears to be a heuristic that leads to definitions of uncertainties contradicting prior work.

Therefore, there is no contribution in this regard.

----

## Relation to Prior Work and Correct Positioning of the Paper

Another main contribution of the paper, as stated by the authors, is the "introduction of a unifying framework to categorize measures of predictive uncertainty according to assumptions about the predicting model and how the true model is approximated." However, a framework leading to exactly the same results has already been introduced.

Specifically, there are two papers—Kotelevskii and Panov (2024) (first published on arXiv in February 2024) and Hofman et al. (2024) (first published on arXiv in April 2024)—that provide a framework for generating uncertainty measures leading to the very same formulas presented in this paper (apart from the point estimate of a model, which is simply a special case of the previously introduced framework if a degenerate posterior is considered). There is nothing new in terms of uncertainty measures that can be derived from the paper under review.

What the authors of the paper under review do is start from the opposite order CE and then follow exactly the same methodology proposed in the prior work, without correctly referencing them. Since ultimately one needs to approximate the true distribution, it's not surprising that the authors arrived at the same equations as in the prior works. But the authors do not discuss this.

Specific Concerns:

- Lines 39-43:

The authors state:

"Despite its widespread use, this measure has drawn criticism (...), prompting the proposal of alternative information-theoretic measures (... Kotelevskii and Panov, 2024; Hofman et al., 2024b). The relationship between those measures is still not well understood, although their similarities suggest that they are special cases of a more general formulation."

The very same question was raised and addressed in the paper by Kotelevskii and Panov (2024):

"It is not clear how all these measures of uncertainty are related to each other. Do they complement or contradict each other? Are they special cases of some general class of measures?"

Both prior works show the answer to this question, demonstrating that many known measures of predictive uncertainty are special Bayesian approximations and are interrelated in this sense. Given this, it's unclear what the novelty of the present work is. Claims such as "Our framework includes existing measures, introduces new ones, and clarifies the relationship between these measures" are not supported.

- Lines 113-115:

The authors state:

"In response, alternative information-theoretic measures have been introduced (... Kotelevskii and Panov, 2024; Hofman et al., 2024b). Although the relationship between these measures is not well understood, their structure is similar to Eq. 4, suggesting a connection between them. We next propose a fundamental, though generally intractable, predictive uncertainty measure, where all of these measures are special cases under specific assumptions."

Again, the central point of the works by Kotelevskii and Panov (2024) and Hofman et al. (2024) was to elucidate these relationships and connections. In these prior works, it was already shown how these similarities to Eq. 4 are employed.

- Lines 243-245:

The authors claim:

"Furthermore, Kotelevskii and Panov (2024) discussed measures (B2), (B3), (C2), and (C3) as Bayesian approximations under the log score."

I find this statement very misleading. One of the primary contributions of Kotelevskii and Panov (2024) and Hofman et al. (2024) is the establishment of a general framework that contains not only log score-based measures but many others. Moreover, the authors of the paper under review consider exactly the same set of instantiations as in the prior work. Surprisingly, only the consideration of log score measures is mentioned in the main part of the paper when prior works are discussed. In the very next sentence, the authors contrast their work by saying "Our work thus generalizes and gives a new perspective on those measures," which seems like an intentional undervaluation of prior work and overselling of the present work.

- Lines 464-466:

The authors state:

"The results are shown in Fig. 5. We observe that throughout all measures, the total and the aleatoric components perform much better than the epistemic components, which is contrary to assumptions commonly formulated in the literature (Mukhoti et al., 2023; Kotelevskii and Panov, 2024)."

This is again misleading. Kotelevskii and Panov (2024) explicitly investigated this question in their experimental section:

"Is Excess risk always better than Bayes risk for out-of-distribution detection?"

where "Excess risk" represents epistemic uncertainty and "Bayes risk" represents aleatoric uncertainty in their notation. Their findings showed that for hard out-of-distribution data, aleatoric (and total) uncertainty outperforms epistemic uncertainty estimates. Therefore, the remark is not correct.

- Lines 812-838:

In this section, the authors derive, in the partial case of the log score, the general relationship presented in Kotelevskii and Panov (2024), specifically that:

$R_{\text{exc}}^{(1,1)} = R_{\text{exc}}^{(2,1)} + R_{\text{exc}}^{(1,2)}$
 
This is redundant, as the general case has already been shown in prior work. Moreover, this particular relationship (in the case of the log score) was already derived in [1].

[1] Malinin, Andrey, and Mark Gales. "Uncertainty estimation in autoregressive structured prediction." arXiv preprint arXiv:2002.07650 (2020).


Therefore, the second contribution claimed by the authors—the introduction of the framework for uncertainty measures—is essentially overselling, given that prior work already introduces this framework.

In the paper, there are two sections in the Appendix, specifically A.4 and A.5 (which are never referenced), where the authors briefly mention that other concrete measures were introduced in the prior work. Nevertheless, the discussed relationship is incomplete; it only mentions that some measures of uncertainty were introduced in previous works but never acknowledges the existence of the framework that leads to the same equations. Additionally, it is not clear why this very important (but very tiny though) discussion is hidden in Appendix and never referenced to.

----

## Conclusion

In this review, I have discussed the contributions claimed by the authors: (1) the consideration of CE between predicted and true distributions as a measure of uncertainty, and (2) the introduction of a framework for new uncertainty measures.

The heuristic with the order of arguments in CE seems unjustified and, in my understanding, is incorrect, as it leads to conceptually flawed definition of AU. The introduction of the framework is not novel, as it was already done in prior work but not properly referenced.

Therefore, I believe this paper should be rejected.

### Questions
1. Why it is never mentioned in the paper, that there are papers, that lead to exactly the same framework, and allow for the generation of new measures of predictive uncertainty?

2. Why this definition of the true AU is introduced?

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a unified framework for information-theoretic measures of predictive uncertainty, integrating various approaches under a comprehensive structure. The framework accommodates different assumptions about the predictive model and its approximation of the true model, consolidating nine distinct uncertainty measures. The authors explore the interrelations among these measures, categorizing prior work within the framework’s defined measures. To validate its effectiveness, the paper evaluates the proposed measures across diverse experimental scenarios involving uncertainty-based tasks, such as misclassification detection, selective prediction, and out-of-distribution (OOD) detection.

### Strengths
This paper is well-crafted, presenting a unified framework for information-based uncertainty measures and offering a thorough analysis of each measure's interpretation and distinctions. The authors clearly outline how each scenario within the framework aligns with existing work in the literature, providing valuable context and insight.

### Weaknesses
I understand that the primary contribution of the paper is the general framework presented by the authors. However, in practical applications, testing each measure can be computationally intensive and potentially infeasible. The community would greatly benefit from theoretical insights into specific scenarios, such as identifying which measure is optimal for OOD detection under some assumptions.

### Questions
I believe uncertainty estimation is of broad interest to the machine learning community, making it particularly valuable if the authors could provide theoretical guarantees across different scenarios, in addition to the empirical studies.

### Soundness
3

### Presentation
3

### Contribution
2
