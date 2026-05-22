Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces L-TTA, the first test-time adaptation method designed for vision-language models (VLMs) under long-tailed test distributions. The method comprises three co-designed components: Synergistic Prototypes (combining Deterministic and Exclusionary Prototypes to enrich tail-class representations), Rebalancing Shortcuts (learnable attention-based modules with a class re-allocation loss), and Balanced Entropy Minimization (a modified entropy loss with a confidence-weighted penalty term, supported by theoretical propositions). Experiments across 15 datasets, three benchmarks (OOD, cross-domain, corruption), multiple imbalance ratios (10/20/50), and four additional backbones show consistent improvements over 12 existing TTA baselines, with particularly notable gains in macro-F1.

## Strengths

- **First targeted study of LT-TTA for VLMs.** The paper identifies and formalizes two failure mechanisms — Text-induced Tail Erosion and Modality-bias Amplification — that are specific to the VLM setting (Section 1, Figure 1). While the evidence for these mechanisms is conceptual, the framing correctly identifies that prior TTA methods for VLMs were designed for balanced test sets and degrade under long-tailed distributions (Figure 2, Tables 1-3 empirically confirm this degradation).

- **Exclusionary Prototypes with all-class update.** EP update (Eq. 5) differs from prior prototype-caching methods (e.g., TDA's negative cache) by using every incoming view to update prototypes of *all* classes, weighted by the inverse prediction probability. This design enriches tail-class representations and provides a technical differentiator from existing VLM TTA approaches. The ablation (Table 6) confirms that removing EPs causes a ~3-4% macro-F1 drop.

- **Rebalancing Shortcuts with CRA loss.** RS introduces learnable attention-based shortcuts over prototypes, optimized with a load-balancing-inspired class re-allocation loss (Eq. 7, explicitly citing inspiration from MoE literature (Qiu et al., 2025)). The ablation in Figure 4b shows the CRA loss provides ~1.64% macro-F1 gain over using entropy minimization alone, and Table 6 shows RS consistently improves over base prototypes.

- **Balanced Entropy Minimization with theoretical grounding.** BEM (Eq. 9) adds a confidence-weighted penalty term to standard EM. Propositions 1 and 2 (Section 3.2) formalize why standard EM biases head classes and why BEM reduces this gap — providing theoretical motivation uncommon in this area. Figure 4d shows BEM yields up to 0.85% macro-F1 improvement over alternative penalty strengths.

- **Comprehensive and rigorous evaluation.** 15 datasets across three benchmarks, three imbalance ratios (10/20/50), comparison against 12 prior methods, four additional backbones (ViT-L/14, ViT-H/14, SigLIP-L/16, MetaCLIP-BigG), and reporting both accuracy and macro-F1. The consistent pattern — e.g., +2.20% macro-F1 on LT-CDB (Table 2), +2.64% on LT-CB (Table 3), and stable gains across all backbones (Table 5) — constitutes strong evidence that L-TTA delivers on its rebalancing claims.

## Weaknesses

### Major

- **Failure-mode claims are asserted without quantitative evidence.** The paper motivates its entire approach by claiming two VLM-specific failure modes, but these are illustrated only conceptually in Figure 1. The text states "Figure 1(b.2) shows that adapting the unimodal SAR method on a VLM backbone results in a significant performance drop and instability" — yet no quantitative results (per-class accuracy, accuracy gap before/after adaptation, or any numerical comparison of SAR on a vision backbone vs. VLM) are provided anywhere in the paper. The concept of "rich classes" is introduced but never measured or exploited. This is a significant evidential gap because the narrative that VLM-specific challenges *require* the proposed novel mechanisms (rather than simply porting existing LT-TTA ideas) is left untested. The paper would benefit from a small experiment showing, e.g., per-class accuracy of a vanilla VLM TTA method broken down by head/tail/rich classes, or the actual degradation of a unimodal LT-TTA method when applied to a VLM.

### Minor

- **Ablation does not cleanly isolate the contribution of BEM without prototypes.** Table 6 ablates prototype variants and RS, but BEM is only tested on top of the full SyP+RS pipeline. The standalone contribution of the BEM loss (applied to base CLIP logits without any prototype-based modifications) is not measured. Similarly, "RS alone" is not meaningful without prototypes by design, but comparing RS against a simpler learnable alternative (e.g., a learned linear projection on the same prototypes) would sharpen the attribution. The current ablation shows components are synergistic but cannot quantify each component's independent contribution.

- **Equation 6 notation is ambiguous.** The formula `v_c ← Attn([v_c, t_c], q_j)q_j + v_c` omits the summation over all hyper-class vectors `j` that the surrounding text describes. A reader would reasonably interpret this as a single projection rather than a weighted sum over `K` vectors. While a specialist can infer the intended meaning, this hinders reproducibility from the main text.

- **Test-set construction is described imprecisely.** The paper states classes are subsampled to follow an "exponentially decayed curve," with the caveat "if the calculated cardinality is less than the class cardinality itself, we simply keep that class unchanged" (Section 4). This means classes that already have fewer samples than the target cardinality are not adjusted, potentially breaking the intended imbalance ratio. The exact algorithm should be specified, and the impact of this approximation on the reported ratios should be discussed.

- **Efficiency claim is slightly overstated.** L-TTA's 1.45h on ImageNet with imb=10 is slower than DPE (1.38h) and TDA (0.91h) — the two fastest prototype-based methods. The paper's claim that L-TTA "only incurs minor computation overhead" (Section 4.1) is accurate relative to the mean of all 12 methods but should be qualified against the most efficient competitors.

### Trivial

- The notation in Eq. 9 could clarify that `(1 - ˜P)^β` operates element-wise on the prediction vector, and `log(π / Σ_i π_i)` is element-wise log of the normalized prior.

- The update rule for threshold `θ` (Eq. 4, "following the above EMA manner") is described textually but the explicit EMA formula is not provided.

## Nice-to-Haves

- Adapting vision-only LT-TTA methods (DELTA, SAR) to the VLM setting and comparing them would strengthen the paper's argument that VLM-specific designs are necessary. This is not a structural flaw — the paper already compares against 12 VLM TTA baselines — but it would directly test the paper's key motivation. The paper's claim that SAR fails on VLMs (Figure 1b.2) should be backed by actual numbers.

- Testing BEM applied to base CLIP predictions (without prototypes) would cleanly isolate its standalone contribution.

- A more stressful robustness test — e.g., a non-stationary data stream where label distribution shifts over time (head-heavy → tail-heavy) — would strengthen the practical claims beyond the current epsilon variation experiment (Table 7).

## Removed Points

*These points from the source reviews are removed or demoted for the following reasons:*

1. **"Omission of DELTA/SAR baselines is a structural failure."** — The paper compares against 12 VLM TTA baselines that are direct competitors. Adapting vision-only LT-TTA methods (DELTA, SAR) to VLMs is a non-trivial extension that goes beyond the paper's stated scope. The paper acknowledges these methods in Related Work and explains they focus on different challenges. While this comparison would strengthen the motivational narrative, its absence does not constitute a structural flaw. Demoted to Nice-to-Have.

2. **"CRA loss is presented as novel without acknowledging MoE work."** — The paper explicitly writes "Gaining inspiration from the Load Balancing Loss (LBL) of mixture-of-experts in LLMs (Qiu et al., 2025)" at line 129. The inspiration is properly cited. Removing this criticism.

3. **"L-TTA is actually slower than DPE and TDA."** — The paper claims "minor computation overhead" in context of all methods; L-TTA is faster than 8 of 12 methods and much faster than the heaviest (RLCF: 18.30h, WATT: 27.70h). This is a minor overstatement that does not misrepresent the overall efficiency profile.

4. **"Table 7 shows only marginal variation."** — The experiment is designed to test *robustness* to ordering, not sensitivity; small variation demonstrates robustness. A non-stationary stream test would be a nice addition but is not a flaw in the current design.

5. **"Dynamic head/tail shifts experiment is not stressful."** — The experiment varies sampling probability for tail-class samples; this is a reasonable perturbation. Critics suggesting non-stationary shifts are proposing an additional experiment, not identifying a flaw in the existing one.

6. **"Missing related works" and "paper should cite X"** — Removed per policy (no external verification of missing citations).

7. **Various formatting, appendix-deferred content, and reproducibility nitpicks about missing hyperparameters.** — These reflect parser-stripped content or are trivial implementation details standard for this community.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel analytical perspective that the paper itself does not already articulate. The critiques are largely about missing evidence (failure-mode quantification, ablation isolation) rather than revealing a new interpretation of the method or results.

## Suggestions

1. Add a small quantitative experiment in the Introduction or Section 4 showing per-class accuracy before/after standard VLM TTA, disaggregated by head/tail/rich classes, and/or the actual performance of a unimodal LT-TTA method (e.g., SAR) applied to a VLM. This would directly validate the claimed failure modes that motivate the entire paper.

2. Add an ablation variant "BEM on base CLIP (no prototypes)" to Table 6 to show BEM's standalone contribution independent of the prototype machinery.

3. Clarify the notation in Eq. 6 (add the summation over `j`) and Eq. 9 (explicitly indicate element-wise operations).

4. Provide the exact subsampling algorithm for constructing long-tailed test sets, and discuss how the "keep unchanged" caveat affects the realized imbalance ratio.

## Score and Decision

The paper tackles a novel and practically relevant problem (first LT-TTA for VLMs), proposes a well-designed method with three co-designed components, and backs it with extensive experiments (15 datasets, 12 baselines, multiple backbones and imbalance ratios). The consistent macro-F1 gains across all settings constitute genuine evidence of rebalancing capability. The main weaknesses are: (1) the claimed failure modes that motivate the paper are presented without quantitative evidence, weakening the motivational narrative; (2) the ablation does not fully isolate BEM's independent contribution. These are real but not fatal — they do not invalidate the method's demonstrated performance. The paper makes a solid contribution to the field.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>