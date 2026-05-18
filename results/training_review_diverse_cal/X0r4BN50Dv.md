I now have a thorough understanding of the paper and can verify the reviewer's claims directly against the text. Let me construct the final review.

---

## Summary

This paper introduces F-Fidelity (FFid), a faithfulness evaluation framework for XAI that addresses the out-of-distribution (OOD) problem in removal-based explanation metrics via (1) explanation-agnostic fine-tuning with random stochastic masks and (2) a bounded removal strategy (Equation 3, truncating removals to at most βtd elements). The paper evaluates FFid against Fidelity, ROAR, and RFid on image (CIFAR, Tiny ImageNet) and time series (PAM, Boiler) data, finding consistent improvements in Spearman rank correlations. It also provides a theoretical result (Theorem 1) showing that under idealized tier-structured assumptions, FFid⁺ can recover the size of the most influential input tier, validated on colored-MNIST.

## Strengths

- **Novel approach to OOD mitigation via random-mask fine-tuning**: The paper identifies a genuine flaw in prior evaluation metrics — that perturbed inputs become OOD for the original classifier — and proposes fine-tuning with explanation-agnostic random masks (Section 3, Eq. 4). This is cleaner than ROAR's retraining per explainer and avoids information leakage. The empirical results consistently show FFid outperforming Fidelity, ROAR, and RFid.

- **Strong empirical ranking recovery across image and time series domains**: On Tiny ImageNet, FFid achieves perfect (−1.00) macro and micro Spearman correlations for both SG-SQ and GradCAM in controlled degradation experiments (Section 4.1). On CIFAR, it achieves perfect macro/micro correlations for SG-SQ and substantially outperforms baselines for GradCAM. Time series results (PAM, Boiler) show consistent improvements in micro ranks and macro correlations (Section 4.2).

- **Rigorous evaluation design**: The controlled degradation framework (adding controlled noise to IG explanations to produce known ground-truth rankings) provides a clean testbed for comparing metrics. The use of both macro (AUC-over-sparsity) and micro (per-sparsity) Spearman correlations gives a more complete picture than single-number summaries.

- **Theoretical connection to explanation size**: Theorem 1 provides a formal argument that under tier-structured assumptions, FFid⁺ changes monotonicity at the boundary of the most influential tier, suggesting the metric can recover explanation size. The colored-MNIST experiments (Section 7) empirically verify this direction-change behavior for known digit sizes.

## Weaknesses

### Major

- **No ablation separating the two proposed components**: FFid combines (i) fine-tuning with random masks and (ii) bounded removal via β truncation (Equation 3). The experiments compare FFid (both components) against RFid (neither component), Fidelity, and ROAR, but never against "RFid + fine-tuning without truncation" or "RFid with truncation but without fine-tuning." This means the reader cannot determine which component drives the reported improvements. If fine-tuning alone accounts for all gains, the bound β is not the claimed separate innovation; conversely, if the bound only helps after fine-tuning, that requires demonstration. This is a central methodological gap that weakens the paper's ability to support its claims about why the method works.

- **Distribution mismatch between fine-tuning masks and evaluation masks**: During fine-tuning (Section 3), the stochastic mask generator P_β selects βtd *random* input elements to remove. During evaluation, FFid⁺ removes a fraction of the *top-s scoring* elements (structured by the explainer's importance ranking) and FFid⁻ removes the lowest-scoring elements. The paper claims evaluation inputs are "in-distribution with respect to the masks used in the fine-tuning step" (Section 3). This would only be approximately true if the evaluation removal patterns were also random, but they are deliberately structured by the explainer. The paper never addresses this distributional gap, which undermines the theoretical grounding of the OOD mitigation claim. The empirical success might derive from fine-tuning making the classifier more uniformly robust to any perturbation, rather than from the specific distribution-matching rationale.

- **Theoretical result validated only on a dataset designed to match its assumptions**: Theorem 1 rests on restrictive assumptions (fixed-size influence tiers, classification probability depending only on unmasked counts per tier, Shapley-value-based explainers). The empirical validation (Section 7) uses colored-MNIST with two known tiers (digit vs. background) of controlled sizes — precisely the assumed structure. The paper claims this shows "our metric can infer the underlying discrete structure of the ground truth explanations" (Section 6), but the evidence only demonstrates a consistency check on a synthetic setup. Without validation on at least one realistic dataset where ground-truth explanation sizes can be determined by an independent procedure, the third contribution (explanation size recovery) remains an isolated theoretical curiosity rather than a practically useful result.

### Minor

- **Conversion from continuous attribution scores to binary masks is never specified**: Explainers like SmoothGrad Squared and GradCAM produce continuous importance scores. To compute FFid⁺ at sparsity level s (5%–95%), the paper must produce binary masks of exactly s non-zero entries. The method for this conversion (thresholding at the s-th percentile? top-s entries?) is never stated. This is a basic reproducibility gap that introduces an uncontrolled degree of freedom into all experimental results.

- **Missing experimental details**: The time series experiments (Section 4.2) specify α⁺=α⁻=0.5 for RFid and FFid, but the β value used for FFid's truncation bound (Equation 3) is not reported. Without β, the comparison is not fully interpretable. Similarly, the macro correlation definition (Section 4) says AUCs "are calculated using these AUC values" without specifying how — the reader can infer a Spearman correlation between AUC values and GT rankings, but the paper should state this unambiguously.

- **No experimental comparison to ROAD**: The paper cites ROAD (Rong et al., 2022) in Related Work and correctly notes that ROAD also addresses information leakage and OOD issues in removal-based metrics. Yet ROAD is not included in the experiments. A comparison would strengthen the claim that FFid improves upon prior evaluation metrics; its omission leaves the most directly related competitive method unbenchmarked.

### Trivial

- The macro correlation definition (Section 4, bullet 1) states that AUCs are computed per explainer and then "macro correlations are then calculated using these AUC values," followed by citing references. The exact computation (presumably Spearman correlation between AUCs and GT ranks) should be stated explicitly for self-containedness.

## Nice-to-Haves

- The authors could add ablation experiments separating fine-tuning from bounded removal, as described above. This is the single most impactful improvement the paper could make.
- For the explanation-size recovery claim, validating on a dataset where ground-truth explanation sizes can be independently determined (e.g., a tampered-image dataset with known inserted object size, or a sentiment dataset with known rationale lengths) would substantially strengthen the third contribution.
- A comparison to ROAD would be informative, though not strictly required given the existing baseline set.

## Removed Points

- **NLP experiments absent from main text**: The reviewer noted that NLP experiments are claimed in the abstract and contributions but do not appear in the main body's experimental sections. Per the hard rules, content from the appendix (stripped by the parser) is assumed to exist in the original submission; the parser removed all appendix material, which may contain the NLP results. This point is removed as a weakness, though the authors should consider ensuring the main body at least references the appendix for NLP results if they exist there.
- **Fine-tuning hyperparameters not reported**: The reviewer asks for number of epochs, learning rate, etc. These are standard implementation details that belong in the appendix (stripped). Not penalized.
- **"ROAD also uses random masking during evaluation"**: The reviewer claims ROAD uses random masking during evaluation as a point of comparison, but this does not invalidate the paper's claims or constitute a confirmed weakness beyond the missing experimental comparison already listed above.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the method or its implications that the paper itself does not already articulate.

## Suggestions

1. **Add ablation experiments** comparing: (a) RFid with fine-tuning (no truncation), (b) RFid with truncation (no fine-tuning), (c) FFid (both). This will reveal which component drives improvements and whether the bounded removal (Equation 3) is a genuinely separate contribution or is dominated by fine-tuning alone.

2. **Address the distribution mismatch** between random training masks and structured evaluation masks. Either provide analysis showing the evaluation removals approximately follow the same distribution, or adjust the fine-tuning procedure to match evaluation conditions (e.g., use importance-weighted or top-k stochastic masks during training).

3. **Specify the masking procedure** for continuous attribution scores: state explicitly that for sparsity s, the binary mask selects the s elements with the highest attribution scores (top-s selection).

4. **Report β values** used in time series experiments and any other missing hyperparameters relevant to reproducibility.

5. **Validate the explanation-size recovery claim** on at least one non-synthetic dataset with independently determinable explanation sizes to support the claim's generality.

6. **Clarify the macro correlation computation** explicitly in the main text.

## Score and Decision

The paper proposes a genuinely useful framework (FFid) for XAI faithfulness evaluation, with a well-motivated design and strong empirical results across multiple domains. The core claim — that FFid outperforms existing metrics in recovering ground-truth explainer rankings — is supported by the experiments. However, the paper suffers from three major weaknesses: the lack of ablation to isolate the contribution of its two components, the unaddressed distribution mismatch between training and evaluation masks, and the limited validation of the explanation-size recovery claim on only a synthetic dataset. These do not invalidate the paper's contributions but significantly limit the depth of understanding about why the method works and the scope of the claims that can be made. The paper would be substantially stronger if these gaps were addressed.

**Overall assessment**: This is a borderline-to-accept paper with real contributions that need additional experimental support to be fully convincing. I recommend acceptance with the expectation that the authors address the major weaknesses in a revision.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>