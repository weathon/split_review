Now I have a comprehensive set of anchors. Let me synthesize the review.

**Anchor comparison summary:**

**Round 1:**
- Topic low-band (avg <3.5): 4 anchors scored 2.50–3.20 — weak papers, paper under review is clearly stronger
- Topic mid-band (3.5–7.5): 4 anchors scored 5.25–6.75 — most relevant comparators. "Scaling Law with Learning Rate Annealing" (6.75, reject), "A Multi-Power Law for Loss Curve Prediction" (6.00, accept), "Scaling Optimal LR Across Token Horizons" (6.00, accept), "Time Transfer" (5.25, reject)
- Topic high-band (>7.5): 4 anchors scored 7.60–8.00 — strong established papers
- Weakness queries: varied relevance, the early-stopping-HPO paper scored 4.67

**Round 2:**
- Anchors within 5.0–6.5: "NanoLM" (5.50, reject), "Hitchhiker's Guide to Scaling Law" (5.20, reject), "Stagewise Development" (5.50, reject)

**Round-1 bracket explicit:** [5.0, 6.5]

**What did the low-band anchors fail at?** Papers scoring ≤3.5 typically had vague methods, no clear empirical validation, poor experimental design, or unsubstantiated claims. The paper under review shares NONE of these failures — its experiments are carefully designed, the core claim is well-supported, and the methodology is sound. The low-band anchors are not informative here.

**What did the weakness-anchored queries show?** The early-stopping-HPO query returned a paper scoring 4.67 where the method had limited validation across settings. The paper under review partially shares this weakness (early stopping only on λ) but this is a secondary contribution, not the core claim.

**Final anchoring:** Topic-mid anchors are the right reference class. The paper is comparable to "Scaling Optimal LR Across Token Horizons" (6.00, accept) and "A Multi-Power Law" (6.00, accept) in substantive quality and validation depth. It is weaker than the 8.00 anchor "Small-scale proxies" which had cleaner, more thorough empirical work. It is stronger than the 5.25–5.50 anchors, which had more limited contributions. The weaknesses identified (abstract overclaim, single diagnostic anecdote, narrow early-stopping validation) are real but minor and do not threaten the core contribution.

**Final score: 6.0, Decision: Accept**

Now let me produce the final review.

---

Let me structure the output carefully.

For the Weaknesses section, I need to be clear about what I'm keeping vs. removing.

**Kept Weaknesses:**
1. Abstract overclaims about optimality (Minor) - The abstract says collapse happens "precisely when" hyperparameters are "set optimally." The body shows collapse occurs when τ, TPP, and LR schedule are *fixed*. The link to optimality is indirect (optimal τ depends on TPP, so training at optimal τ with fixed TPP produces collapse). The paper doesn't test whether suboptimal τ with fixed TPP also produces collapse, and Fig. 4 right suggests it might. This is a wording issue confined mainly to the abstract.

2. Diagnostic claim rests on a single case study (Minor) - The paper claims collapse residuals provide "a sensitive, early diagnostic" but the evidence is one anecdotal case. No controlled experiments with injected anomalies, no false-positive analysis. This doesn't undermine the core contribution but limits the diagnostic application's strength.

3. Early stopping validated only for λ sweeps (Minor) - The method is presented as general, but the empirical validation covers only weight decay sweeps. The method is conceptually general (it works for any HP that affects τ/TPP/ schedule), but this isn't demonstrated. 

4. No quantitative collapse metric (Minor) - Collapse is asserted visually. A metric (max deviation, variance explained) would strengthen the analysis.

**Removed Points (moved from harsh critic or strength finder):**
- Harsh critic's "strengthening" suggestions about systematic diagnostic evaluation, broader early-stopping validation, quantifying collapse → These are suggestions, not weaknesses. Moved to Suggestions/Nice-to-Haves.
- Harsh critic's section-by-section note about "discussion of the parametric model's limitations" → This is acknowledged in the paper. It's a nice-to-have.
- Harsh critic's note about "uncertainty in the compute-efficiency frontier" → Valid but very minor. The paper acknowledges data mixture favors Celerity.
- Harsh critic's note about "impact of data mixture on collapse" → The paper already mentions data mixture choices. Minor suggestion.
- Strength Finder claim 3 about "collapse residuals provide early-warning diagnostic" → This conflicts with weakness 2. But the strength is still a genuine strength (the paper does demonstrate this in one case) - it's just limited in scope. I'll keep it but note the limitation.
- Strength Finder supporting strength 1 about "systematic isolation of three controls" → Verified against paper. Keep.
- Strength Finder supporting strength 2 about "Celerity at compute frontier" → Verified. Keep.
- Strength Finder supporting strength 3 about "parametric surrogate model" → Verified. Keep.

**Strengths to keep (after aggressive filtering):**
1. Demonstrates loss-curve collapse at LLM scale (300M-3.9B) under practical scaling recipes (Figs. 1, 6) — Verified, specific evidence.
2. Identifies τ as the essential control for collapse with bias-variance explanation (Sec. 3, Fig. 3, Eq. 3, Appendix B.3) — Verified.
3. Celerity family lands on compute-efficiency frontier while operating in collapse regime (Fig. 2, Table 10) — Verified.
4. Collapse enables early stopping that selects optimal λ after 10-30% of training (Sec. 5, Fig. 9) — Verified for λ.

Strength Finder's "collapse residuals" strength: I'll keep it but qualify it properly. It does demonstrate one case, which is a genuine demonstration.

Let me draft the full review now.## Summary

This paper demonstrates that normalized training loss curves (TLCs) from LLMs of different sizes (300M–3.9B parameters) *collapse* onto a single trajectory when three controls are matched across scales: the AdamW timescale τ, the tokens-per-parameter ratio (TPP), and the learning-rate schedule. The authors introduce the Celerity model family trained under these conditions, show that residuals from collapse can serve as an early diagnostic for training issues (one case study), and propose an early-stopping method for hyperparameter tuning based on a parametric model of the normalized loss curve. The core empirical finding—that collapse at scale requires fixed τ, TPP, and LR schedule—is well-supported and extends prior small-scale µP results to practical LLM training.

## Strengths

- **Demonstrates loss-curve collapse at LLM scale under practical scaling recipes.** Prior work (Qiu et al., 2025) validated collapse only for small models with vanilla Adam and no weight decay. This paper shows collapse across 300M–3.9B parameters using AdamW, weight decay, co-scaled depth and batch size, directly answering the call for tests at larger scale. The visual evidence in Fig. 1 (middle) and Fig. 6 is clear and compelling.

- **Identifies the normalized AdamW timescale τ as the essential control for collapse and explains its effect via a bias–variance model.** Sweeping η, λ, or B while keeping τ fixed yields identical normalized TLCs (Fig. 3); a noisy-quadratic model (Eq. 3, Appendix B.3) rationalizes why τ governs the trade-off between early bias reduction and late-stage variance suppression. This is a clean, mechanistically grounded finding.

- **The Celerity family lands on the compute-efficiency frontier while operating in the collapse regime.** Celerity models achieve comparable accuracy to BTLm with 75% fewer training FLOPs and sit at the upper-left frontier of average accuracy vs. compute (Fig. 2). This is the first LLM family deliberately trained at fixed TPP with optimally transferred τ.

- **Collapse enables principled early stopping that selects optimal λ after only 10–30% of training.** By fitting a parametric surrogate for the normalized TLC at 111M scale and aligning partial large-scale curves to it, the predicted-best setting incurs a negligible loss gap (<0.1%) across λ sweeps at 1.7B and 3.3B, while "current best" and random baselines fail (Fig. 9). The method is clearly demonstrated for weight decay tuning.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Abstract overclaims about optimality.** The abstract states that "loss curves collapse across scales precisely when optimization hyperparameters are set optimally for the given data budget." The body establishes collapse when τ, TPP, and the LR schedule are *fixed* across scales, not necessarily that they are *optimal*. The paper does not test whether a fixed but suboptimal τ also yields collapse (Fig. 4 right suggests it might), and the connection to optimality is indirect (optimal τ depends on TPP via prior work, so training at optimal τ with fixed TPP produces collapse). The claim conflates a sufficient condition (matched controls) with a property of the controls (optimality). The body text is more precise, but the abstract should be corrected to reflect the actual finding: collapse occurs when τ, TPP, and LR schedule are matched across scales, with optimal τ as a natural regime where this matching holds.

- **Diagnostic use of collapse residuals is supported only by a single case study.** The paper claims that "deviation-from-collapse provides a sensitive, early diagnostic of training pathologies" (abstract) and presents the 1.8B numerical kernel bug as evidence (Fig. 1 right, Sec. 4). While this example is illustrative, it is a single observation without systematic evaluation (e.g., controlled injection of anomalies, false-positive rate, comparison to alternative detection methods). The diagnostic claim as stated implies a validated tool, but the evidence is preliminary. The contribution here is an interesting observation rather than a rigorously validated technique. Moderating the claim (e.g., "a case study suggesting diagnostic potential") would better match the evidence.

- **Early-stopping method validated only for λ sweeps.** The early-stopping experiments (Sec. 5) exclusively tune weight decay λ. The paper presents this as a general method for hyperparameter tuning but does not test on learning rate or batch size sweeps, where the interplay with τ differs. While the method is conceptually general (the parametric surrogate depends on τ and TPP, not λ directly), the empirical validation is narrow. Showing that it works for at least one more hyperparameter type would substantially strengthen the claim.

- **No quantitative collapse metric.** The paper asserts collapse but relies on visual inspection. A simple metric (e.g., maximum absolute deviation between normalized curves, or variance explained by a shared trajectory) would make comparisons across conditions (different TPP values in Fig. 4, different model bands in Fig. 6) more precise and allow readers to assess collapse tightness objectively.

### Trivial
- The parametric surrogate model (Eq. 4) uses fixed constants (m=0.05, ε₁=0.001, ε₂=0.1) tied to linear decay. The paper could more prominently state that these may need recalibration for other schedules or architectures.
- The compute-efficiency frontier analysis (Fig. 2) relies on power-law fits over a small number of Celerity points (three). Including variance information across the seven evaluation tasks would be helpful.

## Nice-to-Haves

- A controlled study injecting synthetic anomalies into training runs to validate the diagnostic approach beyond a single anecdote.
- Early-stopping validation on at least one additional hyperparameter type (e.g., learning rate or batch size sweep).
- A formal metric for collapse tightness (e.g., max inter-curve deviation) to replace visual assessment.

## Removed Points

These points were identified by the reviewers but are removed from the main weakness list with justification:

- **"Missing related works"** → The paper adequately cites relevant scaling law, loss-curve prediction, and early-stopping literature. I cannot verify claims about missing references without external knowledge.
- **"Formatting / style nitpicks"** → Removed per hard rules. Parser artifacts are not author errors.
- **"Reproducibility concerns about undisclosed hyperparameters"** → The paper provides extensive experimental details in the main text and appendix. Requesting complete training logs or trivial implementation details is outside standard expectations.
- **"The paper already addresses..."** → Some suggested improvements (e.g., data mixture effects, limitations of the parametric model) are partially acknowledged by the authors. These are kept in recognition but not treated as omissions.
- **"Factually wrong criticisms about optimality requiring more evidence"** → The core point (abstract overclaim) is kept as a minor weakness, but the harsh critic's framing that this is a "critical issue" is inflated. The overclaim is limited to the abstract and does not undermine the paper's findings.

## Novel Insights

The core insight—that the normalized AdamW timescale τ, rather than any of its constituent hyperparameters individually, governs TLC shape, and that collapse at scale requires τ, TPP, and LR schedule to be jointly fixed—is a genuine conceptual advance over prior work. The noisy-quadratic model (Eq. 3) providing a mechanistic rationale for τ's effect on the bias-variance trade-off is a nice theoretical touch that connects an empirical observation to optimization theory. The idea that collapse residuals can serve as a debugging tool (even if only validated anecdotally) and that the parametric surrogate enables early stopping are useful applications derived from the core insight.

## Suggestions

1. **Reword the abstract and introduction** to state that collapse requires matched τ, TPP, and LR schedule across scales, and that optimal τ (from prior scaling laws) is a natural regime where this matching occurs—rather than implying collapse occurs "precisely when" hyperparameters are optimal.
2. **Add a quantitative collapse metric** (e.g., mean absolute deviation between normalized curves across model sizes) to Figs. 4 and 6 to replace visual assessment.
3. **Moderate the diagnostic claim** from "sensitive, early diagnostic" to "a case study suggesting diagnostic potential" unless additional controlled experiments are added.
4. **Add one more hyperparameter type** (e.g., learning rate or batch size) to the early-stopping validation to demonstrate generality.

## Score and Decision

**Round-1 bracket:** [5.0, 6.5]

**Calibration anchors consulted:**
| Anchor | Avg Score | Source | Comparison |
|--------|-----------|--------|------------|
| Scaling Law with LR Annealing | 6.75 | round1-topic-mid | Similar topic (loss curve prediction); slightly stronger validation but was rejected; comparable quality |
| A Multi-Power Law for Loss Curve Prediction | 6.00 | round1-topic-mid/r2 | Similar scope; the paper under review is comparable in substance with a broader contribution |
| Scaling Optimal LR Across Token Horizons | 6.00 | round1-topic-mid | Closest comparator: solid empirical scaling study; comparable quality |
| Time Transfer | 5.25 | round1-topic-mid | Narrower scope with similar methodology; the paper under review is stronger |
| Small-scale proxies for large-scale instabilities | 8.00 | round1-topic-high | Stronger experimental design; the paper under review is not at this level |
| NanoLM | 5.50 | round2 | Similar methodology but limited novelty; paper under review is stronger |
| Hitchhiker's Guide to Scaling Law | 5.20 | round2 | Methodological study; less directly comparable; paper under review has more substantive empirical findings |
| Methods of Improving LLM Training Stability | 3.50 | round3 | Weak paper; paper under review is far stronger |

**What the low-band and weakness-anchored queries reveal:** Papers scoring ≤3.5 typically have vague methods or unsubstantiated claims. The paper under review shares none of these failures—its experiments are carefully designed and its core claim is well-supported. The weakness-anchored early-stopping paper (4.67) shares the characteristic of limited validation scope, but the paper under review's early-stopping contribution is secondary to its main finding about collapse conditions. The round-2 narrowed anchors (5.2–5.5) are less substantive overall. The most informative comparators are the round-1 topic-mid anchors (5.25–6.75), where the paper under review sits comfortably in the upper half of the range.

The paper has a clear, well-supported core contribution (identifying conditions for LLM-scale TLC collapse) with several minor but genuine weaknesses in the secondary contributions (abstract wording, thin diagnostic evidence, narrow early-stopping validation). These weaknesses do not threaten the central claim and are addressable.

**Score:** 6.0  
**Decision:** Accept

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>