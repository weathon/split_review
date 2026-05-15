## Summary

This paper proposes TC-Bench, a benchmark for evaluating **temporal compositionality** in conditional video generation — specifically whether models can handle transitions in object attributes, object relations, and backgrounds over time. The benchmark consists of 150 T2V prompts and 120 I2V prompt-video pairs with ground-truth videos. The authors also propose assertion-based evaluation metrics (TCR and TC-Score) that use GPT-4 to generate frame-level assertions and VLMs to verify them, showing substantially higher correlation with human ratings than existing metrics (e.g., Spearman 0.416 vs. 0.046 for ViCLIP). An evaluation of 14 models reveals that T2V models achieve less than ~20% TCR, while I2V models (which take start/end frames as input) reach 42–50% TCR.

## Strengths

- **Novel and well-motivated problem formalization.** The paper identifies temporal compositionality as a distinct, under-addressed evaluation dimension and formalizes it via three clear categories (attribute transition, object relation change, background shifts) with scene-graph representations (Section 3.1). This cleanly differentiates the work from static compositionality benchmarks.

- **Metrics with substantially stronger human correlation.** The proposed TCR and TC-Score achieve much higher Kendall/Spearman correlations with human ratings than CLIP, ViCLIP, UMTScore, and EvalCrafter (Table 3: Spearman 0.416 vs. 0.046 for ViCLIP). This directly validates that assertion-based evaluation better captures temporal compositionality for human observers.

- **Comprehensive evaluation that reveals a real capability gap.** Testing 14 models across three categories (Table 1) shows T2V models achieve 0–18% TCR, with open-source models often near 0%. The evaluation spans open-source (VideoCrafter2, CogVideoX-5B), proprietary (Kling, Gen-3 Alpha), multi-stage (Free-Bloom, LVD), and I2V models (SEINE, DynamiCrafter), providing a grounded picture of current limitations.

- **Insightful diagnostic analysis.** Figure 5's CLIP similarity curves over frame indices decompose *why* models fail: T2V models produce flat curves (no attribute transition), while I2V models track ground-truth attribute trends but suffer from frame-consistency drops. This goes beyond aggregate scores to pinpoint specific failure modes.

## Weaknesses

### Fatal
None.

### Major

- **Consistency term for I2V models (Eq. 4) is introduced without specifying weights or ablating its impact.** The paper adds a CLIP-based consistency term weighted by $w_1$, $w_2$ to TC-Score for I2V models, stating it penalizes adversarial intermediate frames. However: (1) the values of $w_1$ and $w_2$ are never reported, (2) no ablation compares TC-Score *with* vs. *without* the consistency term, and (3) the term is only applied to TC-Score (not TCR) without explanation. Since I2V models achieve much higher TCR and the metric's validity for I2V depends on this term, the reader cannot assess whether the improvement is genuine or an artifact of the weighting. This is the single most consequential methodological gap in the paper.

- **No variance estimates across seeds.** Tables 1 and 2 report only single TCR/TC-Score values per model. Video generation models are stochastic; single-generation evaluation per prompt could yield misleading rankings. While many video generation papers share this limitation, the paper's core claim that "most models achieve less than ~20%" would be strengthened by variance estimates or multi-seed reporting.

### Minor

- **Human evaluation protocol is sparsely described in the main text.** The paper reports correlation coefficients (Table 3) as the central validation of its metrics, but the main text omits: the number of videos rated, the number of annotators per video, the exact rating question (was it about transition completion specifically or overall quality?), and inter-annotator agreement beyond a single "Avg." number. The Ethics Statement (Sec. 9) provides payment details (AMT, $0.3/HIT) and the table caption explains that "Avg." is annotator-annotator correlation. However, the core claim that the metrics "align with human judgments" rests on this evaluation, and the main text lacks sufficient detail for a reader to judge robustness without consulting supplementary materials.

- **Abstract's "~20%" claim could be more precisely scoped.** The abstract states "most video generators achieve less than ~20% of the compositional changes," which is true for T2V models (all 12 tested achieve <20%) and for 12/14 total models. However, the two I2V models (SEINE, DynamiCrafter) achieve 42–50% TCR. Since these models solve a different task (generative frame interpolation from given start/end frames), the claim would be more accurate as "most T2V models" or "most direct video generators." This is a small presentational imprecision rather than a factual error, but it could mislead casual readers.

### Trivial

- The paper states small dataset sizes (150 T2V prompts, 120 I2V videos) as acceptable for a first benchmark, but prompt diversity (number of unique objects, attributes, actions) is not analyzed.
- CLIP is acknowledged to be insensitive to fine-grained changes (used in Figure 5's diagnostic analysis), but the paper could more explicitly note that flat curves in Fig. 5(a)-(b) reflect both model failures and CLIP's limitations.

## Nice-to-Haves

- An ablation of the consistency term in TC-Score for I2V models (with vs. without, at different $w_1:w_2$ ratios) would significantly strengthen the metric validation.
- A breakdown of assertion failures by dimension (start-state vs. end-state vs. consistency) would help diagnose *why* models fail specific transitions.
- Multi-seed reporting or confidence intervals would make the model ranking more robust.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Critic's Issue 4 (orphaned method section):** Removed because the paper explicitly frames SDXL+SEINE as a *baseline* evaluated alongside others (Sec. 5: "a simple and effective baseline"), and the listed contributions do not claim it as a separate contribution. The method section is part of the experimental setup, not a claimed fourth contribution.
- **Critic's claim that the abstract is structurally misleading by conflating T2V/I2V:** Weakened to a minor presentation note above, because "most" (12/14 models <20%) is factually correct. The paper later cleanly separates T2V and I2V analyses. The critic's characterization of this as a "structural" issue overstates the problem.
- **Critic's claim that Sec. 2's "drawbacks" lacks evidence:** The paper provides concrete examples (Fig. 1 left vs. right). This criticism misreads the section.
- **Strength Finder's supporting strength about SDXL+SEINE baseline being "practically useful":** Removed because the baseline is straightforward (shared noise + attention injection + off-the-shelf SEINE) and underperforms on object-relation changes — its usefulness as a reference point for future work is minimal.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a key methodological gap (unablated consistency term) and a presentation imprecision (abstract's scoping), but do not generate novel observations about temporal compositionality beyond what the paper already provides.

## Suggestions

1. **Specify $w_1$, $w_2$ and provide an ablation** comparing TC-Score for I2V with vs. without the consistency term. Without this, the metric's validity for I2V models is not fully established.
2. **Expand the human evaluation description** in the main text: number of videos, annotators per video, the exact rating question, and inter-annotator agreement statistics. This is the empirical foundation for claiming the metrics align with human judgment.
3. **Add variance estimates** (e.g., 3 seeds per model) or at minimum acknowledge that single-generation evaluation is a limitation.
4. **Clarify the abstract** to say "most T2V models" rather than "most video generators" given that I2V models perform substantially better (42–50% TCR).

## Score and Decision

The paper addresses a genuine and under-explored problem with a clean benchmark design, well-motivated metrics, and a comprehensive evaluation that convincingly shows T2V models struggle with temporal compositionality. The core contribution is solid. The main weaknesses — the unablated consistency term weights and the underdescribed human evaluation protocol — are fixable. No fatal issues undermine the paper's claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>