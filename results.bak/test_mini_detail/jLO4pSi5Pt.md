Now I have all the information I need. Let me produce the consolidated final review.

## Summary

This paper studies test-time adaptation (TTA) for vision-language models (VLMs) under long-tailed test distributions — a realistic but previously unstudied setting. It identifies two failure modes unique to this setting (text-induced tail erosion and modality-bias amplification) and proposes L-TTA with three co-designed components: Synergistic Prototypes (SyPs) with Deterministic and Exclusionary prototypes to enrich tail-class representations, Rebalancing Shortcuts (RSs) with a class re-allocation loss for dynamic feature clustering, and Balanced Entropy Minimization (BEM), a tailored variant of entropy minimization that penalizes overconfident head-class predictions with theoretical justification. Experiments across 15 datasets under three imbalance ratios (10, 20, 50) show consistent improvements over 11 baselines in both accuracy and macro-F1, with competitive computational cost.

## Strengths

- **First systematic study of VLM TTA under long-tailed test distributions.** The paper identifies two failure modes (text-induced tail erosion and modality-bias amplification) that are specific to the VLM + long-tailed TTA intersection and have not been addressed by prior balanced-set TTA methods. The three components (SyPs, RSs, BEM) are directly motivated by these failure modes and work synergistically.

- **Consistent and extensive empirical validation.** Across 15 datasets spanning OOD, cross-domain, and corruption benchmarks, with three imbalance ratios (10, 20, 50), L-TTA consistently outperforms 11 prior VLM TTA methods. The improvements are especially clear in macro-F1 (the key metric for class balancing), with gains of 1.5–2.6% over the next best method on the OOD average and corruption benchmarks. These results are supported by ablation studies (Table 6) confirming that each component contributes, and robustness experiments (Table 7) showing stability under dynamic head/tail stream orders.

- **Competitive efficiency.** Table 4 shows L-TTA achieves the best harmonic mean of accuracy and macro-F1 on both benchmarks while requiring only 1.45 hours and 1.89 GB memory — substantially less than methods like RLCF (18.30 h) and WATT (27.70 h). This demonstrates the practical viability of the approach.

- **Component-wise necessity is cleanly demonstrated.** Ablations in Table 6 show that removing DPs, EPs, RSs, or BEM all cause noticeable degradation, with the full combination always best (e.g., ViT-B/16 macro-F1 drops from 65.83 to 63.40 with only DPs, and to 62.20 with only EPs). The synergistic design is empirically validated.

- **Generalization across backbone scales.** Results on four additional backbones (ViT-L/14, ViT-H/14, SigLIP-L/16, MetaCLIP-BigG) in Table 5 show consistent gains (~1.5% Acc / 1.8% Mac.), confirming the approach's broad applicability.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No statistical significance reported despite 5 runs.** The paper states it conducts 5 runs for each experiment, but no standard deviations, confidence intervals, or error bars are provided in any table or figure. Given that per-dataset gains are often 1–2% in accuracy (e.g., Table 2: Aircraft 25.49 vs. 24.32; Caltech101 95.26 vs. 94.85), it is not possible to determine whether these improvements are statistically reliable or within run-to-run noise. Reporting variance would substantially strengthen the evidence, especially since the trend is consistent across many datasets.

- **Exclusionary Prototype update rule has unresolved multi-view ambiguity.** Equation (5) updates EPs with a per-view EMA-like formula. The paper states "for each view... we update EPs of all classes," implying Q sequential updates per image (Q=15 augmented views). However, the update counter N_{c,s}^{EP} is described as increasing by 1 "at each step," which could be interpreted as per-image rather than per-view. The distinction matters because it affects how aggressively tail-class prototypes are updated relative to head-class ones. A pseudocode block or explicit statement about update frequency would resolve this.

- **The quantification of the two failure modes relies on visual figures.** The paper's motivating claims about text-induced tail erosion and modality-bias amplification reference Figure 1(b) but do not provide quantitative per-class accuracy breakdowns in the main text (deferred to Appendix C). Since these failure modes are central to motivating the method, including a simple quantitative demonstration (e.g., a bar chart of head vs. tail accuracy for an existing method) in the main paper would make the motivation more concrete.

- **The claim that unimodal LT-TTA methods (SAR, DELTA, LAME) cause modality-bias amplification when applied to VLMs is asserted but not experimentally verified against the proposed method.** The paper mentions them in related work and references Figure 1(b.2) to claim they fail on VLMs, but does not include them as baselines in any experiment. While the paper's primary contribution is a VLM-specific method and the comparison is against 11 VLM TTA methods, a single quantitative demonstration of this claim (e.g., SAR applied to CLIP in one benchmark) would strengthen the paper's narrative arc from problem identification to solution.

### Trivial

- Table 4 reports "1.45h" with inconsistent spacing in the time column. Minor formatting issue.

## Nice-to-Haves

- **Include a proof sketch for Propositions 1 and 2 in the main text.** The propositions are stated clearly, but a 2–3 line sketch of why the inequalities hold (even with a reference to the appendix for the full proof) would help readers assess the theoretical grounding without leaving the main paper. Currently the reader must take the propositions on faith or skip to the appendix.
- **Compare BEM against a simpler LT-adapted baseline** such as entropy minimization with logit adjustment or a class-prior-weighted EM loss. This would isolate the benefit of BEM's confidence-weighted penalty term over a straightforward reweighting scheme.

## Removed Points

*The following points from the inputs were removed per the filtering rules:*

- **Criticism about proofs being relegated to the appendix.** The parser strips appendix content from all papers; proofs exist in the original submission. Per the hard rules, this is not a valid weakness.
- **Criticism about missing code/supplementary material.** The paper provides a GitHub link; reproducibility concerns about what cannot be examined in the review packet are removed per the hard rules.
- **Criticism about HM metric not being standard.** The harmonic mean is a well-established combined metric in imbalanced learning.
- **Criticism about gains being "modest" as a standalone weakness.** Gains of 1–3% are typical for TTA papers; the consistency across 15 datasets and 3 imbalance ratios makes this a pattern, not a weakness. The more specific concern about statistical significance is retained above.
- **"Major clarity issues in method description — reproducibility is in question."** The equation (5) is explicitly stated with all terms defined. While there is a multi-view ambiguity (retained as a minor weakness), the claim that the method is "non-reproducible without extensive guessing" overstates the issue given that the full update formula, normalization, and counter mechanism are all written out.
- **Strength Finder's generic strengths.** Removed generic statements about "addressing an important problem" or "targeting an interesting question" that lacked specific evidence or conflicted with verified weaknesses.

## Novel Insights

The interplay between the harmonic mean of performance and efficiency (Table 4) offers an interesting perspective: prototype-based methods (TDA, DPE) are efficient but degrade on corrupted data, whereas L-TTA maintains both efficiency and corruption robustness through the synergy of EPs (which are updated for all classes per sample, not just the predicted class) and RSs (which operate without gradient flow through the backbone). This design principle — decoupling representation enrichment (prototypes) from dynamic adaptation (shortcuts with lightweight cross-attention) — is a concrete takeaway that could inform future TTA methods beyond the long-tailed setting.

## Suggestions

1. Add standard deviations or confidence intervals to all main tables (Tables 1–3) using the 5 runs already conducted. This is a low-effort change that would meaningfully strengthen the evidence.
2. Clarify the EP update procedure: explicitly state whether all Q views update prototypes sequentially per step or are aggregated before a single update, and define how N_{c,s}^{EP} increments.
3. Include a small quantitative demonstration of the two failure modes (e.g., head vs. tail accuracy of a baseline method like TPT on a long-tailed variant of ImageNet) in the main paper rather than deferring to the appendix.
4. Add a brief proof sketch (2–3 sentences) for Proposition 2 in the main text to help readers follow the theoretical motivation without needing the appendix.

## Score and Decision

**Round-1 bracket: between 4 and 7.** The weak anchors (avg 2.5) were withdrawn/rejected papers with major flaws — clearly weaker than the current paper. The middle anchors (4.67–6.67) included one withdrawn paper (ROSITA, 4.67), two draws (TIPPLE 5.50, PEL 5.25), and three accepted posters (Multi-label BEM 6.25, C-TPT 6.0, RLCF 6.67). The strong anchors (all 8.0) were papers with significantly stronger theoretical depth or broader scope — the current paper does not match that bar.

**Round-2 narrowing (targeting the 5.5–7.5 and 4.5–6.5 bands).** Papers read in full:

- **PEL (avg 5.25, reject):** PEL applies existing PEFT to long-tailed recognition — incremental contribution, rejected. The current paper has stronger novelty (identifies failure modes, designs three co-designed components) and tackles a harder problem (TTA vs. fine-tuning with labeled data). **Current paper is stronger.**

- **C-TPT (avg 6.0, accept poster):** Simple calibration-focused regularization for TTA. Good motivation but limited scope (applied only to TPT). Current paper has more components, more extensive experiments, and addresses a less-explored setting. **Current paper is somewhat stronger.**

- **Multi-label BEM (avg 6.25, accept poster):** Similar conceptual contribution (modified EM for a non-standard TTA setting). Comparable experimental thoroughness within its domain (3 datasets vs. 15). **Current paper is comparable to slightly stronger.**

- **RLCF (avg 6.67, accept poster):** Novel RL-with-CLIP-feedback framework applied across three tasks (classification, retrieval, captioning). Broader impact but similar evaluation depth per task. **Current paper is comparable.**

- **DeYO (avg 7.0, accept spotlight):** Stronger theoretical analysis of entropy limitations, novel PLPD metric, very thorough experiments. The current paper has comparable experimental scope but weaker theoretical development (propositions stated without proof sketches). **Current paper is slightly weaker.**

Based on this calibration, the paper is clearly above the 5.25–6.0 reject/borderline papers and sits comfortably in the 6.0–6.5 range. It is comparable to accepted posters at ICLR (multi-label BEM at 6.25, C-TPT at 6.0, RLCF at 6.67) but does not reach the spotlight-level quality of DeYO (7.0).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>