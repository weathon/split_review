Now I have a thorough understanding of the paper and the calibration landscape. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
// Most papers have none. Leave empty if none apply.

### Major
- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
These points are flagged to be removed, treat them with caution

## Novel Insights
One paragraph synthesizing genuinely novel observations.

## Suggestions
- specific actionable suggestion

## Score and Decision

Let me now write this up carefully.

For the Removed Points, let me think about what to remove from the harsh critic:

1. **Insufficient baseline comparison** - Keep as Major. This is verified: the paper compares against inference-time methods (NoThink, NOWAIT, SEAL) and trains STPO/SFT/DPO all on thought-level data. But there's no comparison against a training-time method that uses response-level preference construction without thought segmentation. This is a real gap.

2. **Logit suppression confound** - Keep as Minor (downgraded from Major). The paper explicitly states the suppression is used only during data generation (Section 3.2), and the trained model doesn't use suppression at inference. The concern that the model might learn to mimic suppression patterns is valid but speculative. The thought-level conditioning should teach the model which thoughts to commit to, not just to avoid tokens. However, the paper doesn't discuss or ablate this.

3. **Lack of statistical reporting** - Keep as Minor. The paper averages 8 runs for AIME (30 problems) and 2 for LiveCode but doesn't report variance. This is a real omission but common in the field.

4. **Steadiness Score not operationalized** - Move to Minor. The formalism in Section 2.1 introduces a latent score but STPO directly uses SimPO's objective. It's a framing issue, not a fatal flaw.

5. **Trigger words and threshold not fully specified** - Move to Trivial/Nice-to-have. The paper gives examples ("wait", "alternatively") and the threshold for the 1.5B model (3.0). More detail would help reproducibility but this is standard for a conference paper.

6. **PCT metric circularity** - Keep as Minor. Valid point that the same segmentation procedure is used for both training and evaluation of PCT.

7. **β and γ hyperparameters not reported** - Move to Trivial. These are standard SimPO hyperparameters and are mentioned in the equations.

Now let me evaluate the Strength Finder's claims:

1. **Thought-level preference optimization (Table 4)** - Valid, keep. The paper shows STPO > SFT > DPO.

2. **Consistent accuracy gains with token reductions** - Valid, keep. The results in Table 1 are impressive and consistent.

3. **Direct evidence of reduced invalid switching (PCT)** - Valid, keep. Table 2 shows PCT decreases.

4. **Principled formalization** - Somewhat valid but the critic notes it's not operationalized. I'll soften this.

5. **Entropy-based thought segmentation** - Valid, keep. Table 3 shows the tuning.

6. **Comparison against SFT and DPO** - Valid, keep, but note the limitation that all use thought-level data.

Now let me write the full review.Here is my final consolidated review.

---

## Summary

This paper proposes **Steady Thought (ST)**, a three-stage training-time framework to mitigate "under-thinking" in large reasoning models (LRMs). ST first segments model responses into thought-level units via entropy spike detection, then generates preferred completions of each thought (with forced switching suppression), and finally performs *thought-level* preference optimization (STPO) using SimPO's length-normalized objective on pairs of (thought completion, subsequent wasteful thoughts). Experiments across three model scales (1.5B, 8B, 14B) and four benchmarks (MATH500, AIME 2024, GSM8K, LiveCode) show consistent accuracy improvements (up to +5.3%) alongside substantial token reductions (up to 39.3%), with gains also observed on an out-of-distribution coding benchmark.

## Strengths

- **Novel and well-motivated framework for mitigating under-thinking.** The paper correctly identifies that prior suppression-based methods (NoThink, NOWAIT, SEAL) apply suppression globally and may discard valuable exploration. ST's approach of *training* the model to selectively commit to promising thoughts while preserving the ability to explore is a principled and practically important direction. The three-stage pipeline (segmentation → completion → preference optimization) is cleanly structured.

- **Consistent and practically meaningful gains across diverse models and benchmarks (Table 1).** The results are impressive: accuracy improvements of 1.9% (1.5B), 3.12% (8B), and 2.52% (14B) on average across four datasets, paired with token reductions of 17.3%–25.5%. The gains on LiveCode (an OOD coding benchmark) — +5.3% for Qwen3-8B and +4.2% for 14B — provide evidence that the method learns generalizable switching behavior rather than overfitting to math data.

- **Direct evidence of reduced invalid switching via the PCT metric (Table 2).** The paper introduces percentage of correct thoughts (PCT) to quantify how often the model abandons a correct intermediate thought. Reductions from 54.9%→40.4% (1.5B on MATH500) and 73.2%→67.7% (8B on MATH500) provide a concrete behavioral link between the training objective and the claimed effect.

- **Ablation isolating preference objective (Table 4).** The comparison of STPO against SFT and DPO within the same thought-level data pipeline confirms that the preference optimization component is the driver of the accuracy-length tradeoff, not merely supervised learning on shorter completions.

## Weaknesses

### Major

1. **Missing training-time baseline that isolates the thought-level conditioning.** The paper compares ST against inference-time methods (NoThink, NOWAIT, SEAL) and ablates STPO against SFT/DPO — but all of these baselines operate on data constructed through the thought-level pipeline. There is no experiment where a preference optimization method (e.g., SimPO or DPO) is trained at the *response level* on the same training set, without thought-level conditioning. Without such a comparison, the reader cannot determine whether the observed gains come from the thought-level design or simply from training on the automatically generated preference data (i.e., any training-time alignment on the dataset would yield similar benefits). This is the single clearest gap in the evaluation — it directly prevents isolating the paper's core claimed contribution.

2. **Logit suppression during chosen-response generation introduces a confound (Section 3.2).** The preferred trajectories are generated by "sharply decreasing the logits" of switch-trigger words ("wait", "alternatively") during decoding, driving their probability "close to zero." The model is then trained to increase the likelihood of these artificially constrained completions over the original unconstrained ones. This creates a risk: the model may learn to avoid trigger words themselves rather than to autonomously identify and commit to promising thoughts. The paper does not discuss this confound or provide an ablation where chosen responses are generated without suppression (e.g., using the base model's natural distribution). While the confound does not necessarily invalidate the results, it weakens the mechanistic interpretation that the paper advances.

### Minor

3. **No variance or confidence intervals on main results (Table 1).** The paper reports averaging "eight test runs for AIME 2024 and two runs for LiveCode" but provides no standard deviations, per-run ranges, or confidence intervals. Given that AIME 2024 has only 30 problems and some accuracy differences are small (e.g., +0.6% on MATH500 for 14B), the absence of variance information makes it difficult to assess whether improvements are statistically reliable. This weakens the evidence, particularly on smaller test sets.

4. **The PCT metric relies on the same segmentation procedure used in training, introducing potential circularity (Section 4.4.2).** The paper uses entropy-based segmentation both to construct training data and to compute the percentage of correct thoughts (PCT) as evidence of reduced invalid switching. An independent measure of thought validity or a human-annotated evaluation would strengthen this analysis.

5. **The Steadiness Score formalism (Section 2.1) is not operationalized.** The paper introduces a latent "Steadiness Score" and connects it to DPO/SimPO via Bradley-Terry, but STPO directly inherits the SimPO objective without instantiating this score. The formalism motivates the approach but is not used in the actual algorithm, creating a mild disconnect between the conceptual framing and the implementation.

### Trivial

6. The specific trigger words used for logit suppression are only partially listed ("e.g., 'wait' and 'alternatively'"), and the suppression strength (magnitude of logit decrease) is not quantified. The entropy thresholds for models other than DeepSeek-R1-Distill-Qwen-1.5B are referenced as in the appendix (stripped).

## Nice-to-Haves

- **Ablation of the logit suppression confound**: Generating chosen responses with and without suppression and comparing downstream performance would cleanly address Concern #2.
- **Response-level training baseline**: Training SimPO on the same preference data but at the full-response level (conditioning only on the question, not on the intermediate thought) would directly isolate whether thought-level conditioning provides additional benefit over response-level alignment.
- **Reporting standard deviations or bootstrapped error bars** on the main accuracy and token-count metrics, especially for AIME 2024 and LiveCode.

## Removed Points

These points from the reviewers were evaluated against the paper and removed with justification:

- **"The paper does not specify the set of trigger words used"**: The paper gives examples ("wait", "alternatively") in Sections 3.2 and Figure 1c. While a complete list would aid reproducibility, this level of detail is typical for the main text. Removed as overblown.
- **"The threshold tuning results for other models are only in the stripped appendix"**: Per the meta-reviewer rules, I cannot penalize the paper for appendix content removed by the PDF parser. Removed as a parser artifact complaint.
- **"The paper's claim about 'average of eight test runs for AIME 2024' suggests the authors performed multiple runs but didn't report variance"**: Retained as Minor (#3 above), not removed. The issue is real but the severity was inflated by the critic.
- **Various style/formatting nitpicks from the harsh critic**: Removed per hard rules.
- **Strength Finder strengths that were generic or not specific**: Removed superficial strengths such as "This paper addressed an important problem" — kept only evidence-anchored strengths.

## Novel Insights

None beyond the paper's own contributions. The observation that thought-level preference optimization can simultaneously improve accuracy and reduce token count — and that the mechanism works through reduced abandonment of correct intermediate thoughts (quantified via PCT) — is the paper's core novel claim.

## Suggestions

1. **Add a response-level preference optimization baseline.** Train SimPO (or DPO) on the same training set but constructing preference pairs at the full-trajectory level (chosen = full correct response, rejected = full incorrect response, conditioned only on the question). This is the cleanest way to isolate whether the thought-level conditioning in STPO provides additional benefit beyond any training-time alignment.

2. **Ablate the logit suppression in data generation.** Generate chosen completions for Stage 2 without suppression (e.g., using the base model's natural decoding or a trained model) and compare final performance. If the method still works, the confound concern is mitigated.

3. **Report standard deviations or bootstrapped confidence intervals** for the main metrics in Table 1, particularly for AIME 2024 (30 problems, 8 runs) and LiveCode (400 problems, 2 runs).

4. **Discuss the logit suppression confound explicitly** in the main paper, noting both the risk and why the thought-level conditioning likely mitigates it.

## Score and Decision

I compared this paper against human-reviewed anchors across three calibration rounds.

**Round 1 (bracketing):** Three queries anchored the weak (<3.5), middle (3.5–7.5), and strong (>7.5) bands. Weak anchors (avg 2.5–3.0) were clearly below this paper. Strong anchors (avg 8.0–9.0) were theoretical or safety papers with fundamentally different contribution types. Middle-band anchors were most relevant.

**Round 2 (narrowing):** I read four middle-band anchors in full: TPO (6.33, accept), IUPO (5.50, reject), SuperCorrect (6.50, accept), and Rational Metareasoning (5.00, reject).

**Comparison to anchors:**
- **TPO (6.33, accept):** Similar scope — preference optimization for complex reasoning. TPO has a cleaner evaluation (compares against DPO fairly) and a more rigorous mathematical formulation, but evaluates on fewer model architectures. The ST paper has broader model/benchmark coverage and more impressive token reductions. Roughly comparable; ST is slightly weaker due to the missing baseline gap.
- **SuperCorrect (6.50, accept):** Stronger results (SOTA on MATH/GSM8K for 7B models) and a cleaner experimental design (no logit suppression confound). ST is weaker on rigor but addresses a different problem (under-thinking vs. error correction).
- **IUPO (5.50, reject):** ST is clearly stronger — more novel framework, better results, cleaner ablation. IUPO was rejected primarily due to limited novelty and heuristic formulation, neither of which applies to ST.
- **Rational Metareasoning (5.00, reject):** Similar goal (reduce unnecessary reasoning tokens) but weaker results and less novel approach. ST is superior.

**Final placement:** The paper sits between the IUPO (5.50) and TPO (6.33) anchors, closer to TPO. The contribution is genuine and the results are consistent, but the evaluation gaps (missing training-time baseline, logit suppression confound) prevent it from reaching the same level of evidentiary support as TPO or SuperCorrect. I place it at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>