Now I have thoroughly analyzed the paper and all reviewer inputs. Here is my consolidated final review:

---

## Summary

PerceptionCLIP proposes a training-free zero-shot classification method that first uses CLIP itself to infer contextual attributes (e.g., background, orientation) from an image and then classifies the object conditioned on those attributes. The core idea—emulating the human visual perception process of understanding context before identifying objects—is cleanly formalized through an attribute-aware CLIP score and conditional probability approximations. Experiments on 11 generalization datasets and two group-robustness benchmarks (Waterbirds, CelebA) show consistent improvements over simple templates and 80-template prompt ensembling.

## Strengths

- **Principled formalization of attribute-aware inference.** Section 3–4 develops a clean probabilistic framework connecting CLIP scores to conditional probabilities via an energy-function analogy, enabling systematic incorporation of contextual attributes into zero-shot inference (Tables 1–2). This formal scaffolding is a genuine contribution that could be extended by future work.

- **Consistent empirical gains across a broad evaluation suite.** The method outperforms both the single-template baseline and 80-template prompt ensembling across all 11 reported datasets (e.g., ~5% absolute gain on EuroSAT). The improvements are directionally consistent, which supports the hypothesis that contextual attribute conditioning is broadly beneficial.

- **Substantial group robustness improvements on Waterbirds and CelebA.** With ViT-L/14, the worst-group accuracy gap is reduced by 19% on Waterbirds and 7% on CelebA (Tables 7–8 in the compiled PDF). This directly demonstrates reduced reliance on spurious correlations, which is the paper's central mechanistic claim.

- **Clean proof-of-concept experiments isolating the causal role of attributes.** Table 3 (verification table) shows that conditioning on ground-truth attributes improves accuracy, while conditioning on wrong or random attributes does not—cleanly separating the effect of correct contextual information from mere prompt enrichment.

- **Insightful connection between the single-step variant and prompt ensembling.** The paper explains that the single-step special case of PerceptionCLIP coincides with prompt ensembling when attributes are randomly selected (Section 5), providing a principled explanation for why ensembling works and situating the method as a generalization of a widely-used technique.

## Weaknesses

### Fatal
None.

### Major

- **Manual construction of contextual attributes limits scalability and reproducibility.** The paper states (Section 6, final paragraph) that it "manually construct[s] essential attributes" for each dataset. This requires dataset-specific expertise to identify generative factors, and there is no systematic or automated procedure for discovering relevant attributes. The method's effectiveness depends directly on the choice of attributes, yet there is no analysis of sensitivity to poor attribute choices or guidance for extending to new datasets. The conclusion acknowledges sensitivity to text descriptions but omits this far more fundamental limitation.

- **Attribute inference accuracy is never validated on the real-world datasets used in the main experiments.** The paper shows CLIP can infer simple binary attributes (orientation, color, shape) on transformed ImageNet with ~74% accuracy (Table 4). However, for Waterbirds (background: land/water/forest) and CelebA (gender, age, race)—where the method's effectiveness depends on accurate attribute inference—the paper never measures how accurately CLIP infers these attributes. Without this validation, the causal chain (inference → conditioning → improvement) remains unsubstantiated. The reader cannot tell whether the method works because of good attribute inference or despite poor inference.

### Minor

- **Limited baseline comparisons.** The paper compares only against the simple template and 80-template prompt ensembling (Radford et al., 2021). Several prior works use LLM-generated class-specific descriptions (Menon et al., 2022; Pratt et al., 2022; Mao et al., 2022; Feng et al., 2023), which the paper cites and distinguishes from its own approach but never empirically compares against. On the group-robustness benchmarks, no comparison to even simple post-hoc debiasing baselines is provided. While these methods differ in scope (class-specific vs. class-independent attributes, training-free vs. training-based), empirical comparisons would substantially strengthen the paper's claims.

- **Interpretability claim is weakly supported.** The paper claims "interpretability" as a benefit but supports it with only two Grad-CAM examples (Figure 3). There is no systematic evaluation, user study, or quantitative analysis of what contextual attributes are inferred or how conditioning changes model focus.

- **No error bars or variance reporting.** All results are reported as single point estimates without standard deviations or confidence intervals. While single-run evaluation is common in this subfield, the method involves stochasticity from sampling description distributions, making variance characterization relevant—especially for small-margin gains (e.g., 0.6% on ImageNet).

### Trivial
None.

## Nice-to-Haves

- Reporting variance (standard deviations over multiple runs) for the key results, particularly for small-margin improvements.
- A comparison to class-specific description methods (Menon et al., Pratt et al., etc.) would strengthen the evaluation, though the difference in approach (class-specific vs. class-independent attributes) makes the absence non-fatal.

## Removed Points

These points are flagged to be removed, treat them with caution:
- The harsh critic's claim that the paper fails to compare to "training-based debiasing methods (LfF, DFR, GroupDRO)" is weakened: PerceptionCLIP is a training-free zero-shot method, and comparing to training-based methods that require in-distribution labeled data is outside the paper's stated scope. The absence is noted but not a valid basis for rejection.
- The criticism that "the distinction between two-step and single-step is partly illusory" misunderstands the paper: the paper clearly acknowledges the relationship and motivates the two-step variant through its advantages (intervention capability, interpretability). This is not a genuine weakness.
- The criticism that "the key assumption that the CLIP score satisfies the ranking inequality in Eq. (4) is asserted as 'not surprising' rather than tested" is partially addressed by the empirical similarity-score evaluations in Figure 1, which show correct pairs scoring higher than mismatched pairs.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not articulate.

## Suggestions

1. **Validate attribute inference accuracy on real-world datasets.** For Waterbirds and CelebA, report CLIP's accuracy in inferring background, gender, age, and race. This would directly substantiate the causal mechanism and help readers interpret the main results.
2. **Add an automated or semi-automated attribute discovery mechanism.** Using an LLM to propose candidate contextual attributes for a given dataset would dramatically improve reproducibility and scalability. Even a simple baseline (e.g., querying GPT for common visual attributes of a domain) would strengthen the paper.
3. **Compare against at least one alternative prompt-based method** (e.g., Menon et al.'s class descriptions) on a subset of the 11 datasets to contextualize the improvements relative to other lines of work.
4. **Provide a sensitivity analysis** showing how performance degrades when irrelevant or poorly chosen attributes are included, to test the robustness of the manual construction strategy.

## Score and Decision

The paper presents a well-motivated idea with a clean formal framework and consistent empirical improvements on standard baselines. However, two significant issues prevent acceptance in its current form: (1) the manual construction of contextual attributes is a structural limitation that is not adequately acknowledged or mitigated, and (2) the core mechanism—attribute inference by CLIP—is never validated on the actual datasets used in the main experiments, leaving the claimed causal chain unsupported. These gaps are substantive but addressable; the underlying idea merits further development.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>