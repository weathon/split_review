Now I have a clear picture of where this paper stands relative to the anchor papers. Let me now synthesize the final review.

## Summary

This paper identifies and formalizes the "copy-paste artifact" in identity-consistent image generation — where models over-replicate the reference face rather than synthesizing the identity with natural variation. To address this, the authors construct MultiID-2M (a 500k-image paired multi-person dataset with diverse references per identity), design MultiID-Bench (a benchmark with a novel copy-paste metric that quantifies reference bias), and propose WithAnyone, a FLUX-based model trained with paired data, contrastive identity losses, and GT-aligned supervision. The central claim is that WithAnyone breaks the fidelity–copy-paste trade-off exhibited by prior methods.

## Strengths

- **Novel formalization of a genuine failure mode**: The copy-paste metric M_CP (Eq. 2) captures the relative bias of generated faces toward the reference vs. the ground truth using angular distances in ArcFace embedding space. This formalizes a previously qualitative observation about over-rigid identity adherence. Figure 5 demonstrates that all prior methods cluster along a regression curve trading Sim(GT) against CP, validating the metric's diagnostic power.

- **Large-scale paired dataset enables non-reconstruction training**: MultiID-2M provides ~500k paired multi-ID images with multiple reference images per identity across diverse poses, expressions, and viewpoints. This is a genuine enabler — the ablation (Table 3) confirms that removing the paired-tuning phase (Phase 3) raises copy-paste from 0.161 to 0.239, directly demonstrating that reconstruction-only training drives the artifact.

- **Convincing quantitative case for trade-off breaking**: On MultiID-Bench (Table 1), WithAnyone achieves Sim(GT)=0.460 with CP=0.144, compared to InstantID's Sim(GT)=0.464 with CP=0.337. The model thus reaches near-identical identity fidelity while reducing copy-paste by more than half. This result is supported across both single-person and multi-person subsets (Tables 1–2), and the scatter plots (Fig. 5) visually reinforce that WithAnyone sits off the regression curve of all other methods.

- **Well-designed benchmark with GT-oriented evaluation**: MultiID-Bench evaluates Sim(GT) rather than Sim(Ref), which is a genuine improvement — prior works' reliance on Sim(Ref) inadvertently rewards copy-paste. The benchmark uses 435 test cases with rare, long-tail identities having no overlap with training data, and provides standardized evaluation across 12 state-of-the-art models.

- **Thorough ablations isolating each component's contribution**: Table 3 cleanly separates the effects of paired training, GT-aligned ID loss, extended negatives, and dataset quality. Figure 7 provides detailed evidence that GT-aligned landmarks yield lower and more consistent ID loss across noise levels compared to prediction-aligned landmarks.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Training–evaluation metric coupling**: The GT-aligned ID loss (Eq. 4) directly minimizes `1 – cos(g, t)`, which is the complement of Sim(GT), the primary evaluation metric. While the test identities are held out (the benchmark samples identities with no training overlap), the objective and metric share the same functional form using the same ArcFace embedding model. The ablation shows that removing GT-Align reduces Sim(G) from 0.405 to 0.385 (Table 3), indicating the loss contributes meaningfully to the metric. Reporting an alternative identity metric (e.g., a different face-recognition backbone not used in training) would make the trade-off-breaking claim more robust.

- **Copy-paste metric can conflate weak identity with low reference bias**: The ablation without extended negatives (Table 3) yields CP=0.074 — the lowest in the table — but Sim(G) drops to 0.368, indicating the model generates faces equidistant from both GT and reference rather than close to GT but far from reference. The paper does not discuss this limitation of the CP metric, which matters for interpreting whether low CP always indicates desirable behavior.

- **Controllability evidence beyond copy-paste is primarily qualitative**: While the paper's title and framing emphasize "controllable" generation, the quantitative evidence centers on copy-paste reduction. The CLIP-T score of WithAnyone (0.313) trails several general-purpose baselines (OmniGen2: 0.331, InfU: 0.328), and attributes like expression, pose, and lighting changes are demonstrated through cherry-picked examples (Fig. 6) rather than quantitative breakdowns. The user study (Fig. 8) supports the claims but uses only 10 participants without reported variance or significance testing.

- **CP ranking threshold lacks justification**: Table 1 restricts CP ranking to cases with Sim(GT) > 0.40, and Table 2 uses Sim(GT) > 0.35. The choice of these thresholds is not explained, and sensitivity to alternative thresholds is not analyzed. A brief justification or sensitivity analysis would strengthen confidence in the reported rankings.

### Trivial

- Architecture details for the SigLip branch and face-embedding injection into DiT blocks appear only in Figure 4's caption and are deferred to Appendix E (stripped in review copies), leaving a readability gap in the main text (Section 5).

- The regression lines in Figure 5 are drawn without methodological details (fitting procedure, whether they exclude the proposed method), making the "off-curve" claim partly a visual impression.

- Table metrics are reported as point estimates without standard deviations or confidence intervals.

## Nice-to-Haves

- A targeted controllability evaluation — e.g., test cases where the prompt specifies a clear attribute change (smiling, head turn, glasses) and measuring whether the generated face exhibits that attribute — would directly support the "controllable" framing.
- Ablation on the size of the paired dataset to demonstrate how performance scales with data volume would strengthen the claim that MultiID-2M is a critical enabler.
- Reporting Sim(GT) and CP with error bars across test cases or runs would let readers assess the reliability of the rankings in Tables 1–3.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *Harsh Critic: "The introduction could better acknowledge that some prior methods (e.g., PuLID) already incorporate identity losses beyond simple reconstruction."* — **REMOVED**: The paper does reference PuLID and discusses its FLUX implementation; the related work section (Section 2) covers prior identity losses. This is a presentation nitpick, not a substantive gap.

- *Harsh Critic: "The dataset's reliance on publicly known celebrities raises questions about implicit memorization by large models."* — **REMOVED**: The ethics statement explicitly discusses data sourcing from CC-licensed images of public figures and anonymization procedures. The concern about implicit memorization by large models is speculative and not tied to any specific evidence in the paper.

- *Harsh Critic: "No ablation is provided on the size of the paired dataset or the number of negatives in the contrastive loss."* — **DEMOTED to Nice-to-Have**: This is a worthwhile addition but not a weakness — the existing ablations already demonstrate the value of paired data and extended negatives.

- *Strength Finder: "GT-aligned ID loss enables effective identity supervision at all noise levels"* — **RETAINED** (merged into the ablation strength), as Fig. 7 provides clear evidence.

- *Strength Finder: "Human study confirms perceptual advantages"* — **DOWNWEIGHTED**: The user study is noted but with appropriate caveats about sample size.

## Novel Insights

The paper's most novel observation is the formalization of copy-paste as a metric (Eq. 2) using normalized angular distances between generated, reference, and GT embeddings. By showing that all existing models lie on a trade-off curve where higher Sim(GT) co-occurs with higher CP (Fig. 5), the paper provides quantitative evidence that reconstruction-based training systematically conflates identity fidelity with reference replication. The paired-training strategy then demonstrates that this trade-off is not inherent — it can be substantially mitigated with appropriate data and objectives. This framing, where the evaluation metric itself (Sim(GT) vs. Sim(Ref)) is part of the diagnosis, is a useful template for other conditional generation tasks where training and evaluation regimes may inadvertently reward degenerate solutions.

## Suggestions

- Add a sensitivity analysis for the CP ranking threshold (Sim(GT) > 0.40 / 0.35) to show that the relative ordering of methods is not an artifact of this choice.
- Report an alternative identity metric (e.g., AdaFace or a different face-recognition backbone) on the benchmark to demonstrate that WithAnyone's identity advantage is not coupled to the ArcFace embedding used in training.
- Clarify in the main text, even if briefly, how the SigLip branch and face embeddings are injected into the DiT backbone, rather than relying entirely on Figure 4 and the appendix.
- Discuss the CP metric's limitation revealed by the "w/o Ext. Neg." ablation: that CP can be artificially low when identity is weak, and how this should qualify interpretation of the metric.

## Score and Decision

**Round-1 bracket**: Based on comparison with anchors in the 3.0–10.0 range, WithAnyone is clearly stronger than RetriBooru (4.5, similar problem but weaker execution) and UIFace (6.0, narrower scope), placing it above 6.0. It appears below CADS (8.0, more theoretically grounded and broadly applicable) and IC-Light (10.0, fundamentally novel physical constraints). **Initial bracket: 6.5–8.0**.

**Round-2 narrowing**: Compared against InstantPortrait (6.67) — WithAnyone offers more comprehensive contributions (dataset + benchmark + model vs. single model), broader scope (multi-ID generation vs. style-only editing), and fewer methodological gaps. Compared against Superposition of Diffusion Models (7.33) — scope is different (systems contribution vs. theoretical framework), but both are well-executed. WithAnyone is comparable to or slightly stronger than Superposition in empirical depth.

**Anchor comparison summary**:
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| ID-Booth (NWvsm2VxAM) | 3.00 | 1 | Weaker — narrower problem, less comprehensive evaluation |
| RetriBooru (IjVCcykKdr) | 4.50 | 1 | Weaker — similar problem but anime-only, less convincing results |
| UIFace (riieAeQBJm) | 6.00 | 1 | Weaker — narrower scope (synthetic FR data), less thorough evaluation |
| InstantPortrait (ZkFMe3OPfw) | 6.67 | 2 | Weaker — style-only editing, more methodological gaps noted by reviewers |
| ClassDiffusion (iTm4H6N4aG) | 6.25 | 2 | Weaker — more focused method, less comprehensive contribution |
| Superposition (2o58Mbqkd2) | 7.33 | 2 | Comparable — different type (theoretical), both well-executed |
| CADS (zMoNrajk2X) | 8.00 | 2 | Stronger — cleaner theoretical contribution, broader applicability |
| REPA (DJSZGGZYVi) | 9.00 | 1 | Stronger — fundamental training insight with broader impact |

WithAnyone sits between Superposition (7.33) and CADS (8.00). It is closer to Superposition in overall contribution quality, but benefits from delivering a complete ecosystem (dataset + benchmark + model) with strong empirical validation. I assign it **7.5**.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>