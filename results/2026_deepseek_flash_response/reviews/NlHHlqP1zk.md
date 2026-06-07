Now I have enough information to finalize. Let me compile the final review with calibrated score.

**Round 1 Bracket:** Based on the anchors, the paper clearly sits in the middle band (between the weak 3.0-3.4 anchors and the strong 7.6-8.0 anchors), in the range of approximately 4.0-5.75.

**Round 2 Narrowing:** I read several anchors within this bracket. The paper is stronger than the 3.40 concept-bank generation paper (more novel methodology, broader experiments) but weaker than the 5.75 V-IP paper (which has cleaner experiments without a major confound). Comparing to the 4.83 zero-shot CBM paper (which had mixed reviews about novelty) and the 5.33 KT annotation paper (domain-specific but clean execution), our paper has a genuine methodological contribution but a structural confound that weakens its central claim.

**Final Score:** 5.0 — The paper has a genuine contribution (FSE framework, CRI metric, utility-as-proxy critique) but the main empirical finding conflates annotation insufficiency with LLM reasoning limitations, substantially weakening the headline conclusions. With major revisions this could be a stronger paper, but in its current form the evidence does not fully support the claims.

---

## Summary

This paper proposes the Fast and Slow Effect (FSE) framework for automatically evaluating the sufficiency of LLM/VLM-generated concept annotations for XAI without human supervision. The framework introduces a five-stage hierarchical concept gathering process and a Class Representation Index (CRI) metric that measures whether accumulated concepts enable correct classification against semantically similar distractors. Experiments across six models and five datasets reveal that on fine-grained datasets, concept-only ("slow mode") classification underperforms direct visual ("fast mode") classification by ~25%, and that high fused-mode accuracy does not imply annotation sufficiency, challenging the utility-as-proxy validation paradigm.

## Strengths

1. **Quantitative challenge to the utility-as-proxy assumption (Table 4):** The paper directly compares fast (visual only), slow (concepts only), and fused (visual + concepts) modes, showing fused mode achieves ~83–96% CRI while slow mode alone achieves only ~42–68% on fine-grained datasets. This is a well-controlled experiment demonstrating that high downstream performance does not imply annotation sufficiency, directly contradicting a core assumption in prior work (Hu et al. 2024a,b; He et al. 2025).

2. **Cross-dataset contrast that delimits the problem scope (Table 3):** The paper shows that on general datasets (CIFAR-100, Caltech-101) the slow mode achieves >90% CRI and outperforms the fast mode, while on fine-grained datasets the same models drop to ~50–60% CRI. This controlled comparison isolates the failure to fine-grained discrimination, showing the limitation is domain-specific — a nuance that strengthens rather than weakens the paper's contribution.

3. **Multi-family, multi-scale model evaluation (Section 5.2):** Experiments cover six models from three families (GPT-4o, Llama-3.2-vision, QwenVL2) at two scales each. Tables 2–3 show the CRI-Gap is consistently negative across all six models on fine-grained datasets, demonstrating the finding is not an artifact of a single architecture or scale.

4. **Empirically grounded distractor selection (Section 5.3, Table 1):** The paper validates distractor construction through a contradiction test comparing random distractors (14–20% contradiction rate) against semantically related distractors (34–45% contradiction rate), providing quantitative justification for the experimental design.

## Weaknesses

### Major

1. **The experimental design conflates annotation insufficiency with LLM reasoning failure.** The slow mode requires the LLM to (a) generate concepts and then (b) reason from textual concepts to a classification. A failure in slow mode could mean the concepts are insufficient *or* that the LLM is poor at concept-based reasoning. The paper provides no control condition (e.g., human-written gold-standard concepts evaluated in the same way) to separate these possibilities. Without knowing whether *any* set of textual concepts would allow the LLM to succeed at this task, the attribution of failure to annotation quality specifically is unsupported. The CRI measures a joint distribution of (concept quality × reasoning ability), and the paper attributes all failures to the first factor. This is the most significant limitation of the paper.

2. **The "Slow Mode Superiority" hypothesis is theoretically unmotivated, and its failure is not a diagnostic finding.** The paper hypothesizes that slow mode (concepts only) should outperform fast mode (full image), citing dual-process theory. However, no information-theoretic rationale supports the claim that textual concepts should encode *more* discriminative signal than the full pixel-level image. The observed negative gap (fast mode outperforms slow mode) is neither surprising nor diagnostic of annotation insufficiency — it is a predictable consequence of the lower information bandwidth of textual descriptions. The paper would be stronger if it dropped this hypothesis and instead treated the slow mode as an intrinsically hard diagnostic task, focusing on *which* concepts and stages contribute most to recovery.

3. **The CRI formula (Equation 2) contains a notational error.** As written, CRI = 100% × (1/t) Σ_{i=1}^{t} 𝟙[y_i^t = y_i], where t is the annotation step index (1 to 5). The test set has l instances (i = 1, ..., l, as defined on line 115). The formula should use l, not t, in the summation bounds and denominator. This is a typesetting error (confusing the symbol t with l) that likely does not affect the implementation, but it creates confusion in the paper's formal definition and should be corrected.

### Minor

1. **No reported standard deviation values.** The paper states "standard deviations are negligible" (line 211) and shows shaded error bars in Figure 3, but does not report actual numerical values. Given stochastic LLM outputs across three seeds, explicit reporting (e.g., a supplementary table) would strengthen claims of consistency.

2. **The design choice T=5 is not empirically justified.** The paper cites prior hierarchical extraction work as motivation but does not ablate this choice or show whether CRI saturates earlier or would improve with more stages.

3. **The description of fast mode as "without any conceptual reasoning" (abstract, line 9) is imprecise for VLMs.** VLMs may internally use conceptual reasoning even without explicit textual prompting. This phrasing overstates the difference between the two modes.

4. **The ResNet-18-based semantic similarity for distractor selection is not externally validated.** The paper uses ResNet-18 confusion to define "semantically related" distractors, but does not validate whether these align with human judgments of semantic similarity or with other similarity metrics.

### Trivial

- The reproducibility statement says "We have provided the code and data at here" — a placeholder with no URL.

## Nice-to-Haves

1. Adding a human-written gold-standard concept control (e.g., from CUB's attribute annotations) to disentangle annotation quality from reasoning ability would substantially strengthen the paper's central claim.
2. An ablation study varying the number of annotation stages (T).
3. Manual analysis of failure modes — categorizing whether failures arise from missing concepts, incorrect concept weighting, or reasoning errors.
4. Reporting numerical standard deviation values alongside the claim of negligible variance.

## Removed Points

Points from the Harsh Critic that were removed after verification:

1. **"Results on general datasets contradict the central narrative"** — Removed. The paper explicitly presents the general-dataset results as evidence that annotations *can* be sufficient for coarse-grained tasks, which is consistent with and actually *delimits* the scope of the paper's claims. This does not contradict the narrative.

2. **"The fast/slow comparison is structurally confounded by information bandwidth"** — Partially subsumed by Weakness #2 above. The critic's framing that the gap is "uninformative" is too strong; the paper's core contribution (FSE + CRI) can still be informative if the reasoning confound is addressed. The information-theoretic framing is a restatement of Weakness #2 rather than a separate concern.

3. **"CIFAR-100/Caltech-101 results are explained away post-hoc"** — Removed. The paper's explanation (coarse-grained vs. fine-grained discrimination) is the natural reading of the data, not an ad-hoc rationalization. This finding supports the paper's scope delimitation.

4. **"Definition 3.1 is operationally vague"** — Removed. This is a generic critique applicable to many conceptual definitions in ML papers; "expressive, clear, and precise enough" is an intentionally high-level definition that is then operationalized through the CRI metric.

5. **"Reproducibility — no code URL"** — Removed per instruction: reproducibility concerns about placeholder URLs in a double-blind submission are treated as formatting artifacts rather than substantive weaknesses.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a control experiment with human-written gold-standard concepts (e.g., CUB attribute annotations) to isolate the effect of annotation quality from LLM reasoning ability. This is the single most important improvement and would directly address the central confound.
2. Drop or substantially soften the "Slow Mode Superiority" hypothesis, as it is not theoretically grounded. Reframe the slow mode purely as a diagnostic tool rather than an expected improvement.
3. Fix the notational error in Equation 2 (t → l in summation bounds and denominator).
4. Report numerical standard deviation values from the three-seed runs, and provide a brief justification for T=5 (or show that CRI saturates).

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| KLUDshUx2V.md (Automating Concept Banks) | 3.40 | 1 | **Weaker** — less novel methodology, fewer experiments. Our paper is clearly stronger. |
| wZiH43e5Ah.md (Conceptualize Any Network) | 3.00 | 1 | **Weaker** — different topic (post-hoc explanation framework rather than evaluation). |
| kTjEPEy96Q.md (Evaluating Unsupervised CBMs) | 3.00 | 1 | **Slightly weaker** — similar goal (evaluating CBMs) but less comprehensive experiments. |
| 0qrTH5AZVt.md (ConLUX) | 4.67 | 1 | **Comparable** — concept-based explanation framework with similar scope. |
| ZSvOIT5Ai2.md (Interpretable Concept Discovery) | 4.33 | 1 | **Comparable** — addresses concept quality but with different methodology. |
| 9bmTbVaA2A.md (Bootstrapping V-IP) | 5.75 | 1 | **Stronger** — cleaner experimental design without major confounds, well-written. |
| 5Aem9XFZ0t.md (Zero-shot CBMs) | 4.83 | 2 | **Comparable** — both have significant limitations; ours has more novelty but a confound issue. |
| M4fhjfGAsZ.md (Automated Knowledge Concept Annotation) | 5.33 | 2 | **Slightly stronger** — domain-specific but clean execution without confound issues. |
| L9U5MJJleF.md (CB Generative Models) | 6.00 | 2 | **Stronger** — novel idea, broader applicability, well-received by reviewers. |

**Round 1 Bracket:** 4.0 – 5.75  
**Round 2 Narrowing:** The paper is above the 3.0-3.4 anchor papers (more novel methodology, broader experiments) but below the 5.75-6.0 anchor papers (which have cleaner experimental designs without the confound issue). Compared to the 4.83-5.33 anchors, the paper has comparable quality — genuine contribution but a structural confound that limits the strength of its central claim.

### Final Score

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>