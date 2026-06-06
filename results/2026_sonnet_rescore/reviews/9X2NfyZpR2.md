Now I have a thorough understanding of the paper and can write the meta-review. Let me verify the key claims from the reviewers against the actual paper content.

**Key verifications from the paper:**

1. **Stochastic vs. deterministic comparison (Table 1, lines 202–221):** The table caption explicitly states: *"The highest accuracy under a deterministic framework is indicated in bold… The highest accuracy under a probabilistic framework is indicated in gray. * means stochastic protocol."* Stochastic and deterministic results are visually distinguished. The paper does not make the false claim that stochastic TbLTA beats deterministic supervised methods. The paper says it is "competitive with, and occasionally superior to, fully supervised approaches" — which is primarily supported by the deterministic Breakfast numbers (29.03% avg vs. ActFusion 28.45%).

2. **50Salads vs. Breakfast gap:** On 50Salads, TbLTA deterministic lags significantly (20.92% avg vs. ActFusion 28.39%). On Breakfast, TbLTA outperforms (29.03% vs. 28.45%). The paper explains this in Section 4.2: *"long videos, denser action distributions, and frequent transitions yield weaker temporal regularities, amplifying the impact of imprecise temporal alignment."* This is a plausible and reasonable explanation rooted in dataset properties (50Salads has ~20 dense actions per video).

3. **Duplicate Tables 3 and 4 (lines 247–271):** Both tables are byte-for-byte identical in the extracted text. The paper text refers to "Table 3 (IAS)" and "Table 4 (LTA)" as separate ablations targeting segmentation and anticipation quality respectively, but both contain identical numbers. This is a confirmed, concrete, and significant presentation problem: the ablation cannot independently support the design claim that better segmentation propagates to better anticipation.

4. **Duration loss effect:** Paper states at line 283: "Table 4 shows that removing the duration loss reduces accuracy (~0.2 on 50Salads, ~3.3 on Breakfast)." This matches the tables (28.5 vs. 26.3 on 50Salads; 37.2 vs. 33.9 on Breakfast average — differences of ~2.2 and ~3.3). The harsh critic's claim that the drop on 50Salads is only ~0.2 does not match the tables (it's ~2.2), but the tables are the stochastic Top-1 results, so this is a minor discrepancy in framing.

5. **ATBA module is borrowed (Section 3.1):** The paper explicitly acknowledges this: *"we adopt the ATBA module proposed in (Xu & Zheng, 2024)."* The contribution is the extension to anticipation — this is clearly stated.

---

## Summary

TbLTA is the first weakly-supervised framework for dense long-term action anticipation (LTA), trained exclusively with ordered action transcripts — without frame-level annotations, boundaries, or durations. The architecture combines a borrowed temporal alignment module (ATBA) for pseudo-label generation, a novel local cross-modal attention mechanism, a CTC-regularized segmentation head, a CRF-based anticipation decoder, and a momentum-based duration head. On the Breakfast benchmark, the deterministic model surpasses all fully supervised baselines under weak supervision; on 50Salads and EGTEA, results are competitive but inferior overall, with a notable advantage on rare classes.

---

## Strengths

- **First transcript-only dense LTA framework with genuine competitive results.** The deterministic TbLTA achieves 29.03% average MoC on Breakfast, exceeding ActFusion (28.45%) and all other supervised baselines. This is a meaningful result for a method that uses no frame-level annotations.

- **Novel cross-modal attention design with pseudo-label-driven masking.** The local masking mechanism (Eq. 1–2) restricts each transcript embedding to its temporally aligned video neighborhood, then injects it via a gated residual. Ablation shows removing this mechanism drops average accuracy by ~5.7 points on Breakfast and ~1.3 on 50Salads, confirming concrete value.

- **Rare-class performance on EGTEA is genuinely interesting.** TbLTA outperforms the supervised Anticipatr on rare action classes (60.11% vs. 55.10% mAP), suggesting that high-level semantic supervision from transcripts mitigates data imbalance in ways that dense supervision does not. This receives insufficient attention in the paper and deserves more analysis.

- **Ablation study covers all key design components.** CTC, CRF, cross-attention, and duration head are each individually ablated with full metric tables. The CRF in particular has a large effect on long-horizon stability (~5.3 points on 50Salads, ~4.1 on Breakfast at 50% anticipation horizon), confirming it is not cosmetic.

---

## Weaknesses

### Fatal
None.

### Major

- **Duplicate ablation Tables 3 and 4 (verified, lines 247–271).** Both tables contain byte-for-byte identical numbers, yet Section 4.3 cites them as separate results for "IAS" (segmentation quality) and "LTA" (anticipation quality), making distinct claims about each. This is a concrete internal inconsistency: if the same numbers are presented under two different labels, either the segmentation metric was conflated with the anticipation metric, or one table's data is missing. This directly undermines the paper's architectural claim that better temporal alignment propagates to better anticipation — the claim cannot be independently verified from the ablations as printed. *The paper must provide separately computed segmentation-quality numbers (e.g., frame accuracy on the observed interval) alongside the anticipation numbers to support this specific design claim.*

### Minor

- **Stochastic Top-1 comparison lacks a symmetric supervised baseline (Table 1).** The stochastic TbLTA* Top-1 (37.15% Breakfast, 28.51% 50Salads) substantially exceeds the deterministic supervised baselines and is shown in the same table. While the paper appropriately distinguishes stochastic from deterministic with different typographic treatment (gray vs. bold) and clearly labels `*` as "stochastic protocol," no stochastic baseline is provided for supervised methods. Without this, one cannot determine whether the Top-1 advantage reflects a genuinely better predictive distribution or simply that sampling helps weakly-supervised models more because the base distribution is noisier. This is worth noting, though the paper's core "competitive with full supervision" claim rests primarily on the deterministic Breakfast numbers.

- **The paper describes an unexplained performance gap on 50Salads.** The deterministic TbLTA trails ActFusion by ~7.5 points average on 50Salads, while outperforming it on Breakfast. The paper attributes this to "longer videos, denser action distributions, and frequent transitions," which is a reasonable and contextually grounded explanation, but it is qualitative. No analysis of pseudo-label quality or alignment accuracy on 50Salads is provided to substantiate why transcript alignment is harder there. This weakens the generalization claims. The honest discussion in Section 4.2 mitigates this somewhat, but a quantitative analysis (even a simple pseudo-label accuracy estimate) would significantly strengthen the paper's understanding of its own failure mode.

### Trivial

- The section abstract claim "transcript-based supervision offers a *very robust* and less costly alternative" is slightly overstated given the 50Salads results. "Competitive" is more accurate for the general case.

---

## Nice-to-Haves

- Report pseudo-label accuracy (frame-level precision against held-out ground-truth boundaries) as a function of dataset. This single diagnostic metric would explain the Breakfast/50Salads asymmetry mechanistically and make the paper's practical guidance much clearer.

- If stochastic superiority is to be claimed in future work, applying the same Top-K sampling protocol to at least one supervised baseline (e.g., diffusion-based ActFusion) would make the comparison interpretable.

- The rare-class advantage on EGTEA (Section 4.2, Table 2) is the paper's most surprising finding and currently receives one sentence. A deeper analysis of why transcript supervision mitigates class imbalance would make a strong secondary contribution.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Comparison as designed cannot tell us whether stochastic TbLTA is genuinely better" (harsh critic framing it as "structural").** The paper's table caption explicitly separates deterministic and stochastic results using bold/gray encoding, and the text describes them as "dual views." The paper does not claim stochastic TbLTA beats deterministic supervised methods. The concern about a missing stochastic supervised baseline is retained as a minor issue, but the "structural" severity label is unwarranted.

- **"ATBA is adopted wholesale" as lack of novelty.** The paper explicitly acknowledges adopting ATBA from Xu & Zheng (2024) and clearly articulates the new contribution: extending pseudo-label generation to anticipation, adding the cross-modal attention, CTC supervision, CRF decoder, and duration head. Adopting an existing alignment module as a component while contributing the full framework around it is standard practice.

- **"Performance on 50Salads suggests the approach fails on denser datasets."** The paper provides a reasonable dataset-level explanation, and "failure" is too strong. The method still outperforms WS-DA on 50Salads and achieves 20.92% average vs. 21.30% for that method at one operating point. The limitation is real but the paper acknowledges it explicitly.

- **"Headline claim of 'very robust alternative' is not supported."** This is a trivial wording critique, retained at the Trivial level, not as a structural concern.

---

## Novel Insights

The paper's most underexplored finding is the rare-class advantage on EGTEA: a weakly supervised method trained only on ordered action lists outperforms a densely supervised model specifically on underrepresented classes (60.11% vs. 55.10% mAP). This suggests a novel hypothesis — transcript-level semantic supervision provides a regularization effect that prevents overfitting to majority classes, an effect that dense frame-by-frame supervision cannot easily replicate. If this hypothesis were substantiated with an analysis correlating class frequency with transcript-supervision benefit, it could constitute a distinct contribution beyond the core engineering novelty of the TbLTA framework. The current paper raises this result but does not investigate it.

---

## Suggestions

1. **Fix Tables 3 and 4:** Provide genuinely separate ablation numbers for segmentation quality (e.g., F1 or frame accuracy on the observed interval) and anticipation quality (MoC). This is the highest-priority fix.

2. **Add a pseudo-label quality analysis:** Even a simple frame accuracy comparison between pseudo-labels and ground-truth annotations on both datasets would anchor the discussion of why Breakfast and 50Salads differ so dramatically in method performance.

3. **Expand the EGTEA rare-class discussion:** The rare-class result (Table 2) is the paper's most intriguing finding. Analyze whether this holds as a function of class frequency and tie it to the nature of transcript supervision.

4. **Clarify stochastic evaluation scope in Table 1:** Either add a stochastic supervised baseline or add an explicit note that the stochastic rows are shown for completeness and not claimed to be directly comparable with deterministic supervised results.

---

## Assessment on Key Axes

- **Originality:** High. This is the first transcript-only dense LTA framework. The local cross-modal attention with pseudo-label masking is a novel design.
- **Importance:** High. Reducing annotation requirements for LTA is practically significant; the problem is well-motivated.
- **Claims supported:** Moderate. The Breakfast results are well-supported; the 50Salads gap and duplicate tables weaken broader claims about component contributions.
- **Soundness of experiments:** Moderate. The experimental protocol follows established benchmarks; the duplicate table issue and missing stochastic supervised baseline are the main gaps.
- **Clarity of writing:** Good overall, with the notable exception of the duplicate/mislabeled ablation tables.
- **Value to research community:** Good. Establishing the first transcript-supervised baseline for dense LTA opens a new research direction.

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>