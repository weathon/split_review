Now I have enough understanding of the paper. Let me run calibration searches.Round 1 bracket: roughly **4.5 to 6.5**. Now narrowing within this bracket.Now I have enough calibration. Let me write the final review.

## Summary
The paper introduces IRIS, an RL fine-tuning recipe for autoregressive text-to-image (T2I) models (Janus-Pro 1B/7B) that uses *negative self-certainty* (NSC), i.e., the forward KL from the uniform distribution to the model's output distribution, as the sole intrinsic reward — no reward model, human labels, or verifiers. The authors observe that during external-reward RL, image-token self-certainty decreases (opposite of math-reasoning LLMs), and use this as motivation to directly minimize self-certainty. On GenEval, T2I-CompBench, and WISE, IRIS roughly matches the four-reward T2I-R1 baseline despite using no external signal, and shows complementary strengths on knowledge-heavy categories (biology/physics/chemistry on WISE).

## Strengths
- **Concrete and novel empirical observation (Fig. 2).** RL fine-tuning of an LLM (Qwen2.5-1.5B) on math increases text-token self-certainty, while RL fine-tuning of a multimodal LLM (Janus-Pro-1B) on T2I decreases image-token self-certainty. This is a clean, specific, and quantitatively documented contrast between modalities.
- **A purely intrinsic, label-free reward is shown to be roughly competitive with an external four-reward stack.** Table 1 and Fig. 3 show that IRIS reaches scores within one std of T2I-R1 on multiple cells (e.g., 1B GenEval 0.72±0.01 vs 0.75±0.01; T2I-CompBench-Complex 0.3793 vs 0.3820; WISE 0.37 vs 0.38). Given no reward model is used, this is a genuine result.
- **Complementary category-level pattern (Sec. 4.2, Table 1c).** On WISE natural-science (biology/physics/chemistry), where external rewards (HPSv2/DINO/GIT/ORM) have no direct signal, IRIS matches or beats T2I-R1; T2I-R1 leads on categories aligned to its rewards (counting, color attribution, spatial). This is the paper's strongest evidence that intrinsic-reward RL avoids domain-specific blind spots.
- **Reasonable ablation coverage (Figs. 5–9).** CoT vs. no-CoT, min vs. max image SC, min vs. max text SC, forward vs. backward KL, and RL vs. direct gradient optimization each test a specific design choice.
- **Baseline correction (Sec. 4.1).** The authors identify and fix a chat-template mismatch in the official T2I-R1 implementation (Janus vs Janus-Pro keys) before comparing — this is a careful detail.

## Weaknesses

### Fatal
None. The core empirical contribution is intact.

### Major
- **Headline framing overstates Table 1.** The abstract/intro repeatedly state IRIS is "competitive with or superior to external rewards," but every one of the six benchmark × model-size cells in Table 1 has T2I-R1 strictly ahead in the best-checkpoint number (GenEval 1B 0.75 vs 0.72; 7B 0.78 vs 0.77; T2I-CompBench-Complex 1B 0.3820 vs 0.3793; 7B 0.3992 vs 0.3916; WISE 1B 0.38 vs 0.37; 7B 0.50 vs 0.48). The 1B GenEval gap of 0.03 sits well outside the reported ±0.01 std. The "9.1% / 13.3% / 28.8%" numbers in Sec. 4.2 are improvements *over base*, not over T2I-R1, but they appear in a sentence about the comparison to external rewards. Fig. 3 (curves) and Table 1 (best checkpoints) also disagree in direction without reconciliation. The intrinsic-rewards-get-close-to-external-rewards story is genuinely interesting; the current framing oversells it.
- **The headline conceptual claim ("minimize SC for images, maximize for language") is not what IRIS implements.** Sec. 3.2 and Fig. 7 are explicit: IRIS minimizes SC for *both* text and image tokens, and minimizing text SC outperforms maximizing it — directly contradicting the modality-asymmetry message featured in the introduction (and Fig. 2). The paper acknowledges this and offers a post-hoc speculation about "descriptive and explorative text" differing from math reasoning, but the central conceptual claim and the operating recipe remain inconsistent. The honest framing — generative/exploratory tasks (captioning + image gen) want low SC; verifier-grounded reasoning wants high SC — is barely surfaced.
- **NSC is not isolated from standard entropy-style regularization.** Mathematically NSC = (1/|V|) Σ_v −log π(v|·), i.e., a per-token penalty on placing mass on any single bin — a vocabulary-spread / smoothness signal. The forward-vs-backward-KL ablation (Fig. 8) is closely related but narrow; a GRPO + constant reward + entropy bonus, or GRPO + external reward + entropy bonus, would isolate whether NSC carries information beyond standard entropy regularization. Without that, the paper cannot rule out that the contribution is "entropy regularization with forward-KL flavor helps T2I." This bears directly on the central claim.

### Minor
- **CoT confound not fully isolated.** Fig. 5 establishes that CoT helps IRIS, and T2I-R1 also uses CoT, so the IRIS-vs-T2I-R1 comparison itself does control for CoT. But the paper never runs GRPO with the same CoT pipeline and a *constant* reward (or pure KL-to-reference regularization), which would quantify how much of the 1B gains come from the CoT + GRPO scaffolding versus the NSC signal specifically. The "RL vs direct optimization" ablation (Fig. 9) shows that *gradient-direct* NSC collapses, but does not address the constant-reward baseline.
- **7B gains are modest.** On Janus-Pro-7B, IRIS gains +0.01 (GenEval), +0.007 (T2I-CompBench-Complex), and +0.02 (WISE) over base, compared to +0.02/+0.015/+0.04 for T2I-R1. The paper notes this and attributes it to the stronger base, which is reasonable, but it does mean the case for intrinsic-reward RL is largely a 1B-scale phenomenon in this paper.
- **Ablation metrics are the same four reward models used to train T2I-R1.** Sec. 4.3 uses HPSv2/GIT/DINO/ORM as ablation evaluators. For IRIS-vs-IRIS variant comparisons this is fine, but it does mean "minimizing both SCs is best" is measured against signals that are precisely what the external-reward baseline optimizes — which constrains the interpretation of how much these ablations speak to "general image quality" vs. "alignment with these four scorers."

### Trivial
None worth weighing in the decision.

## Nice-to-Haves
- Reframe the contribution around portability (label-free RL reaches an external-reward stack's neighborhood, with complementary strengths on knowledge-heavy prompts) rather than modality asymmetry. The paper's own ablations support the portability story better than the asymmetry story.
- Add a GRPO + constant-reward + entropy bonus baseline (and ideally a CoT-only baseline under a constant reward) to isolate NSC's contribution from entropy regularization and the CoT pipeline.
- Reconcile the apparent disagreement between Fig. 3 (curves favoring IRIS) and Table 1 (best-checkpoint numbers favoring T2I-R1) explicitly — e.g., are these different training regimes, different stopping criteria, different seeds?
- Per-category training trajectories on WISE natural-science prompts would strengthen the strongest argument the paper has (the complementarity finding in Sec. 4.2).

## Removed Points
These points were flagged in the harsh review but trimmed; treat with caution.

- *"7B gains weaken the broader claim entirely."* — Demoted to Minor. The 7B numbers are smaller but still positive, and the paper discusses this; framing this as a structural threat overstates it.
- *"Mechanism story is hand-wavy"* (as a separate critique) — merged into the "NSC vs entropy regularization" weakness; keeping it standalone would inflate the count.
- *"Ablation metrics use the same four reward models, making conclusions circular as a measure of overall image quality."* — kept as a Minor; the harsh critic's stronger phrasing ("circular") goes further than the evidence supports for IRIS-vs-IRIS comparisons.

## Novel Insights
None beyond the paper's own contributions. The most interesting framing the reviewers surfaced is that IRIS's contribution is better understood as a *portability / label-free RL* result than a *modality-asymmetry* result — but this is a reframing of the paper's own evidence, not an external insight.

## Suggestions
- Rewrite the abstract and intro so that gains are described against the right comparator. Reserve "9.1% / 13.3% / 28.8%" for "over base," and use "within ~3 points / within ~1 std of T2I-R1" when discussing the external-reward comparison.
- Drop, or substantially soften, the modality-asymmetry headline; lead instead with "label-free RL gets close to a four-component external-reward stack and is complementary in domains the external rewards don't cover."
- Add the entropy-regularization baseline. This is the single experiment most likely to either (a) sharpen the contribution into "NSC carries real information beyond entropy regularization" or (b) reposition it honestly as "forward-KL entropy regularization is enough for T2I."
- Report ablation variance (multiple seeds) on Figs. 6–8, where current conclusions about which SC direction or KL direction is "better" rest on single trajectories.

---

## Axis-level assessment
- **Originality:** Above average. The image-token-SC-decreases-under-RL observation (Fig. 2) and the label-free intrinsic-only RL recipe for autoregressive T2I are genuinely fresh.
- **Importance of question:** Solid. Label-free RL for T2I is a real bottleneck given how expensive multi-reward stacks are.
- **Support for claims:** Mixed. The portability claim is supported; the modality-asymmetry claim is undercut by the paper's own ablations; the "competitive with or superior to" claim is mildly overstated relative to Table 1.
- **Soundness of experiments:** Reasonable for the scope — three benchmarks at two model sizes, ablations on the major design choices. Missing: an entropy-regularization control and a constant-reward + CoT control.
- **Clarity of writing:** Mostly clear, but the framing-versus-recipe inconsistency in Sec. 3.2 and the gain-attribution confusion in Sec. 4.2 cost meaningful clarity.
- **Value to the community:** Real. Even if the mechanism turns out to be a flavor of entropy regularization, demonstrating that a label-free signal closes most of the gap with a four-component reward stack is a useful empirical result.

---

## Calibration anchors used

Round 1 (bracketing):
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/oOa3ZCtMjJ.md — avg 3.00 — weak T2I work; IRIS is clearly stronger.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/TJHB4ySVZM.md — avg 3.40 — weak T2I data augmentation; IRIS is clearly stronger.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/ZVOGMy8Sd8.md — avg 3.00 — weak image captioning; IRIS is clearly stronger.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/RFJGFrMvYj.md — avg 1.50 — clearly weaker than IRIS.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/bO31lfEdos.md — avg 5.00 — human-free RL for VLM captioning, similar spirit but narrower; IRIS slightly stronger.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/fXkoROek1M.md — avg 4.00 — diffusion + RL mode-collapse; IRIS stronger.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/Let8OMe20n.md — avg 6.00 (Accept) — confidence-aware reward optimization, comparable scope; comparable to IRIS.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/cJQ1K2fjpD.md — avg 6.20 (Accept) — token-level intrinsic rewards for VLM alignment; comparable to IRIS in spirit and scope.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/DJSZGGZYVi.md — avg 9.00 — representation-alignment landmark work; clearly above IRIS.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/u1cQYxRI1H.md — avg 10.00 — clearly above IRIS.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/uAFHCZRmXk.md — avg 8.00 — clearly above IRIS.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/NN6QHwgRrQ.md — avg 8.00 — clearly above IRIS.

Round-1 bracket: **4.5–6.5**.

Round 2 (narrowing):
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/ewIfVxCzbo.md — avg 5.00 (Reject) — DPO-Diff prompt optimization; IRIS is comparable or slightly stronger in scope.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/5CHcmVzbAz.md — avg 5.00 (Reject) — SePPO; IRIS is comparable but with a more surprising finding.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/w0lhe9prqH.md — avg 4.75 (Reject) — DCPO; IRIS is stronger.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/9fMNxWDZsP.md — avg 5.50 (Reject) — Explainable Concept Generation, RL-based preference; comparable.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/pzUhfQ74c5.md — avg 6.25 (Accept) — Conformal LM; different topic, comparable rigor.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/iamWnRpMuQ.md — avg 7.00 (Accept) — Policy-aware Reward Modeling; cleaner and more theoretically grounded than IRIS.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/tmBKIecDE9.md — avg 7.25 (Accept) — Motif (intrinsic motivation from LLM feedback); a tighter, more compelling intrinsic-reward story than IRIS.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/MeGDmZjUXy.md — avg 6.33 (Accept) — Moral alignment; less directly comparable.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/jQP5o1VAVc.md — avg 5.75 (Reject) — Scaling AR T2I; comparable.
- /home/wg25r/split_review/datasets/deepreview_13k_calibration/tjn2YZSHUv.md — avg 6.75 (Accept) — Social Reward; comparable.

After reading TIA2 (Let8OMe20n, 6.0 Accept) and Fine-Grained Verifiers (cJQ1K2fjpD, 6.2 Accept) in full: both papers introduce a clean idea with adequate but unspectacular empirical support; both have visible weaknesses (limited evaluation depth, partial benchmark coverage) without being fatally compromised. IRIS sits in the same neighborhood — interesting central observation, decent empirical work, but with a noticeable framing inconsistency and a missing entropy-regularization control that the accepted anchors don't have analogous flaws of. IRIS is comparable to or slightly weaker than these 6.0–6.2 accept anchors due to (a) the headline-vs-Table-1 discrepancy and (b) the unreconciled framing-vs-recipe inconsistency in Sec. 3.2; it is clearly stronger than the 5.0 reject anchors (DPO-Diff, SePPO). I land at **5.5** — just below the accept anchors, above the cluster of 5.0 rejects.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>