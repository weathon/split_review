Now I have all the calibration data I need. Let me write the final review.

## Summary

This paper introduces and formalizes a previously overlooked dimension in machine unlearning: the decoupling of class labels from target concepts. The authors identify four scenarios (all-matched, target mismatch, model mismatch, data mismatch) defined by the relationships among the label domains of forgetting data, model output, and target concept. They provide a theoretical analysis (Theorem 3.2, "representation gravity") showing that forgetting dynamics at the representation level explain why existing methods fail in mismatch settings. Based on this, they propose TARF (TARget-aware Forgetting), a framework combining annealed gradient ascent on forgetting data with target-aware gradient descent on identified hard-to-affect retaining data. Experiments on CIFAR-10, CIFAR-100, and ImageNet-1k show TARF achieves near order-of-magnitude improvements in Gap over the best baselines on target and data mismatch settings, while remaining competitive in conventional settings.

## Strengths

1. **Principled taxonomy of label-domain mismatch scenarios**: Section 3.1 and Figure 1 formalize four distinct forgetting tasks by introducing relations (L1=L2, L1≺L2) among the label domains. This provides a structured vocabulary for unlearning problems where the class label and target concept diverge, which prior work (Warnecke et al., 2023; Golatkar et al., 2020; Chen et al., 2023) did not model.

2. **Theoretical link between representation distance and forgetting dynamics**: Theorem 3.2 proves that the loss-change gap during gradient ascent is bounded by a term proportional to the representation distance d_h(x1,x2), formally connecting latent space geometry to unlearning behavior. This provides theoretical grounding absent from prior class-wise unlearning methods such as FT, GA, BS, and L1-sparse, which operate without an explicit representation-level analysis.

3. **Systematic outperformance across all four mismatched tasks on standard benchmarks**: In Table 3, TARF achieves the lowest Gap on all four tasks for both CIFAR-10 and CIFAR-100. For example, on target-mismatch CIFAR-100, TARF's Gap=0.21 versus the next-best (GA, 8.86); on data-mismatch CIFAR-100, TARF's Gap=1.17 versus next-best (GA, 2.43). No other method achieves competitive performance across all three mismatched settings simultaneously.

4. **Scalability to ImageNet-1k with consistent gains**: Table 4 shows TARF achieves the best Gap across all four tasks on ImageNet-1k (All matched: 3.66, Target mismatch: 3.97, Model mismatch: 5.92, Data mismatch: 4.17), demonstrating the approach does not degrade on large-scale, high-resolution data, unlike some baselines (e.g., GA collapses on target mismatch with Gap=47.17).

5. **Target-identification mechanism validated empirically**: The accuracy-drop-based identification procedure (Phase I) is validated in Figure 5(a), showing target-concept classes experience significantly larger accuracy drops after gradient ascent than remaining classes. This provides an operationalization of the "representation gravity" concept that prior methods lack.

6. **Ablation study isolating the annealed-gradient-ascent design choice**: Figure 7 directly compares constant, linearly-increasing, and linearly-decreasing (annealed) schedules for k(t) on model-mismatch forgetting, showing why the specific annealing design matters.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **Framing-evaluation tension for target/data mismatch**: The paper introduces target mismatch forgetting as "unlearn 'people'" (Figure 1b, line 33) and uses intuitive examples suggesting the goal is to forget the entire target concept. However, the retrained reference (against which all methods are evaluated) is trained on D_r = D \ D_f (line 61). Since D_f is only a subset of the target concept (e.g., {boy, girl} ⊆ people), the retrained model has *not* forgotten "people" — it has forgotten only {boy, girl} while retaining knowledge of {man, woman, baby}. The evaluation measures approximation of this retrained model, not forgetting of the full target concept. The paper is internally consistent about what it evaluates, but the framing in Figure 1, the introduction, and Section 3.1 suggests a stronger claim. The authors should either (a) sharpen the language to clarify that the evaluation target is forgetting only the given subset D_f, or (b) add evaluation metrics that directly measure target-concept forgetting (e.g., accuracy on D_fr).

2. **Unclear Gap values for the Retrained reference row in Table 3**: The Gap is defined as (1/4)∑|R_Retain − R_Opt| (line 194), measuring deviation from the Retrained model. However, the Retrained row in Table 3 shows Gap = 4.33 (CIFAR-10 all-matched) and 1.47 (CIFAR-100 all-matched). A reference compared against itself should yield Gap = 0. These values are confusing and need clarification or correction (set to "N/A" or 0). Note: this does not affect relative comparisons since all methods use the same reference, but it obscures the presentation.

3. **Assumption that the number of target-concept classes is known**: The paper states "we assume that the number of classes in D_un belonging to the target concept is known" (line 61) for Phase I identification. While a threshold-based approach (top-10% rank ordering, line 152) is mentioned that partially mitigates this, the sensitivity of TARF to misspecification of this threshold/assumption is deferred to the appendix. Since this assumption directly affects practical applicability, an explicit sensitivity analysis in the main text (or a clear statement that the thresholding approach eliminates the need for knowing the count) would strengthen the paper.

4. **LLM/TOFU experiments underreported**: Table 5 is difficult to parse — metric abbreviations ("QA Prob on F.", "QA Prob on R.") are unexplained, and the distinction between "TARF (GA)" and "TARF (NPO)" is not described. The accompanying text is minimal (lines 327-329). For a paper claiming general applicability beyond image classification, this section needs a proper setup description, metric definitions, and interpretable results.

5. **Two TARF rows in Table 2 without clear differentiation**: In the CIFAR-100 section of Table 2 (lines 267-268), two TARF rows are listed with different values but identical labels. It is unclear which corresponds to which configuration.

### Trivial
None.

## Nice-to-Haves
- Adding standard deviations or significance indicators for the all-matched setting where TARF's Gap (1.01) is very close to SCRUB's (1.03) on CIFAR-10, and for the model-mismatch setting where the improvements are smaller. (The paper states results are in Appendix F.7.)
- A brief empirical demonstration in the main text showing how the threshold-based identification (top-10%) performs compared to the "known count" assumption.

## Removed Points
**From Harsh Critic:**
- Point about "multiple-run statistics deferred to appendix" — Standard practice in page-limited venues; the appendix exists in the original submission. The Gap differences in the key mismatched settings are large enough that std values would not change the conclusions.
- Point about "Table 2 confusing layout" — Partially addressed in Minor weakness 5 (the two TARF rows), but the general "layout is confusing" critique lacks a concrete actionable anchor.
- Point about "the Gap for Retrained reference is confusing" — Retained as Minor weakness 2.
- Point about "missing standard deviations for small differences" — Placed in Nice-to-Haves.

**From Strength Finder:**
- None removed — all six strengths are concrete, specific, and evidence-backed.

## Novel Insights
None beyond the paper's own contributions. The paper itself introduces several novel concepts (the taxonomy of label-domain mismatch, representation gravity, TARF framework) and the reviews do not surface genuinely new observations beyond what the paper provides.

## Suggestions
1. Clarify in Section 3.1 that in target/data mismatch, the retrained reference is trained on D\D_f (which still contains false retaining data). Explicitly state what the evaluation does and does not measure. Adjust the "unlearn 'people'" framing or add direct metrics on D_fr.
2. Set the Retrained Gap values to "N/A" or "—" in Table 3, or explain what these numbers represent if intentional.
3. Expand the LLM/TOFU experiment section with clear metric definitions and an explanation of what distinguishes TARF(GA) from TARF(NPO).
4. Disambiguate the two TARF rows in Table 2 with descriptive labels or a footnote.
5. Add a brief sensitivity study on the threshold parameter β (or the known-class-count assumption) to the main text.

---

**Calibration Anchors:**

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| UGradSL (hwXUmwJAq5) | 3.00 | R1-low | Much weaker; simple gradient-based approach, limited novelty |
| PPU (Xagys9QD3T) | 3.00 | R1-low | Much weaker; simple probability-replacement method |
| MASIMU (BJfIDS5LsS) | 2.50 | R1-low | Much weaker; complex multi-agent approach, poor clarity |
| Deep Unlearning (pUOesbrlw4) | 5.25 | R2-middle | Weaker; SVD-based empirical method without theoretical guarantees, less novel problem formulation |
| Sparse Repr (TLBPjECC5D) | 5.25 | R2-middle | Weaker; direct application of DKVB, model-specific, less comprehensive evaluation |
| OUbL (wAemQcyWqq) | 5.67 | R2-middle | Weaker on core contribution; addresses privacy-preserving unlearning (different problem), significant practicality concerns |
| SLUG (3p4raemLAH) | 5.75 | R2-middle | Comparable on paper quality but TARF has more novel problem formulation and stronger evaluation |
| **This paper (OHOmpkGiYK)** | **5.75** | R2-middle | **Own human reviews [6,6,3,8]; 3-score reviewer biased by page-length frustration** |
| Label-Agnostic (SIZWiya7FE) | 6.00 | R2-middle | Comparable; novel supervision-free approach but TARF has stronger empirical validation and theoretical foundation |

**Round 1 Bracket:** 5.5 – 7.0

**Round 2 Narrowing:** The paper is clearly stronger than the 5.0–5.25 anchors (Sparse Representations, Deep Unlearning) which lack theoretical foundations or have model-specific limitations. It is comparable to or stronger than the 5.67–6.00 anchors (OUbL, SLUG, Label-Agnostic Forgetting) in terms of problem novelty, evaluation comprehensiveness, and empirical decisiveness. The paper's own human reviews average 5.75 but were influenced by a 3-score reviewer penalizing page length; the remaining scores [6,6,8] average 6.67.

**Final score: 6.0** — The paper has a genuinely novel problem formulation (decoupling class labels from target concepts), a solid theoretical foundation (Theorem 3.2, representation gravity), and compelling empirical results (order-of-magnitude improvements in target/data mismatch). The weaknesses are fixable — framing clarity, presentation issues, and underdeveloped case studies — and do not undermine the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>