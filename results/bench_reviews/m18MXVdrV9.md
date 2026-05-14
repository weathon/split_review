## Summary
INFO-SEDD extends the SEDD/CTMC framework to estimate KL divergence (and hence MI, entropy) between discrete distributions by combining Dynkin's formula with discrete-diffusion score parameterization. A key trick uses an absorbing-state rate matrix so that a single joint score model yields both joint and marginal scores. Experiments cover synthetic MI, SUMMEVAL text-summary MI, HUMAN-vs-WORM genomics, and TATA-box motif discovery.

## Strengths
- Clean mathematical derivation: combining Dynkin's formula (Eq. 3) with the SEDD score parameterization yields a tractable KL estimator (Eqs. 4–5) with an explicit error decomposition (Eq. 7) into estimation error and exponentially decaying truncation bias.
- The absorbing-state trick in Eq. (6) is a genuine engineering simplification — it lets one model trained on the joint give both joint and marginal scores, enabling MI between arbitrary subsets of a sequence without retraining (used naturally in the motif scan, Fig. 5).
- Strong synthetic results in a regime where lower-bound variational estimators are mathematically inadmissible: INFO-SEDD-J recovers 47.77 nats at MI=50, D=50 with low variance (±1.18) where most baselines collapse (Table 1).
- Practical demonstration of integration with pretrained discrete-diffusion backbones (MDLM-SMALL, CADUCEUS), not just a synthetic-only proposal.
- Motif-discovery application (Fig. 5) is a refreshing real-world use case that exploits the single-model property and qualitatively localizes the TATA-box to its known position window.

## Weaknesses

### Fatal
None — the core derivation is sound and synthetic ground-truth results support the central claim that INFO-SEDD is admissible in the high-MI/high-D discrete regime where competitors are not.

### Major
- **2× internal disagreement between INFO-SEDD-J and INFO-SEDD-C on SUMMEVAL is unexplained.** Figure 2 shows INFO-SEDD-C MI in ~400–800 nats; Figure 3 shows INFO-SEDD-J MI in ~250–425 nats — same population quantity, factor-of-two gap. The paper attributes the J/C gap on genomics (Sec. 4.3) to optimization difficulty when one side is low-dimensional, but in SUMMEVAL both variables are high-dimensional text and the discrepancy is not analyzed. This matters because the downstream qualitative claim (which human metric MI correlates with) shifts depending on which variant is used — INFO-SEDD-C gives r=0.740 with consistency and r=0.679 with fluency (nearly tied), while INFO-SEDD-J gives r=0.550 with consistency. Without diagnosing the gap, the reader cannot decide which estimate to trust.
- **The SUMMEVAL "consistency test" reference target is an entropy upper bound, not MI ground truth.** The 256–303 nats line in Fig. 1 is `H(summary)` derived from English entropy rates × summary length, which upper-bounds I(text;summary), not equals it. The linear-in-ρ argument is also conditional on MI ≫ log 2. Together this means landing near 256–303 with linear slope is consistent with both an accurate estimator and an estimator that effectively reports H(summary). A trivial baseline that returns H(summary) would pass this test, so it does not distinguish accuracy from order-of-magnitude correctness — exactly the regime where the J/C 2× gap lives.

### Minor
- **No description of a train/eval data split for real-data MI.** Neural KL/MI estimators are known to over-estimate when the score model is evaluated on its training set. For SUMMEVAL and especially the motif scan (where MI ≈ 0.02–0.12 nats and overfitting-driven inflation would dominate signal), the paper does not say whether MI is reported on held-out data. Eq. (7) bounds error in terms of true-score approximation but says nothing about generalization gap.
- **The genomics "ground truth" in Fig. 4 is itself an approximation.** Sec. 4.3 substitutes `H(Y|X) ≈ H_b(Acc.)` of a trained classifier — a Fano-style bound, not an information-theoretic ground truth. Treating INFO-SEDD-C matching the dashed line as evidence of *accuracy* (rather than agreement-with-a-proxy) is weaker than the text suggests. The paper would benefit from acknowledging this more explicitly.
- **Table 1 benchmark configuration handicaps the lower-bound baselines.** With batch size 1024, log(1024) ≈ 6.93 nats caps NWJ/MINE/SMILE/KL-DIME by construction at MI ≥ 10. The paper cites this limitation and the comparison is informative about which estimators are *admissible* at high MI — but framing Table 1 as a head-to-head accuracy comparison overstates what it shows. The directly comparable baseline (MINDE) is included, which mitigates this, but a panel at MI ≤ log(batch size) would round out the picture.
- **Eq. (7) is overclaimed as a consistency result in Sec. 3.** The bound is in terms of population approximation errors (ε_p, ε_q) → 0; Monte-Carlo variance over t and X_t and finite-sample generalization are not in the bound. "INFO-SEDD is a consistent estimator up to this exponentially decaying bias" is true under strong assumptions that are not validated.

### Trivial
- Section 2.2 drops `E[log p₀/q₀(X₀)]` on the grounds that both p₀ and q₀ converge to π, but Eq. (7) treats it as a truncation bias term. Reconciling these two framings explicitly in the main text would help.
- The synthetic data-generating process is fully deferred to the appendix; a one-line statement of the construction and MI/D ratio in the main text would aid interpretation.

## Nice-to-Haves
- A direct head-to-head of INFO-SEDD-J vs. INFO-SEDD-C on a synthetic discrete distribution with known MI at SUMMEVAL-comparable dimensionality, to characterize the J/C gap.
- A baseline in Fig. 1 that simply reports `H(summary)` to show the consistency test discriminates a real MI estimator from a trivial entropy proxy.
- Training/validation loss diagnostics alongside MI estimates over training to expose any overfit-inflation.
- For motif discovery, a comparison to position weight matrices or the original Umarov & Solovyev randomization on the same sequences would strengthen the application claim beyond "the peak lands in the right window."

## Removed Points
*These points were flagged for removal — treat them with caution.*

- *"Synthetic benchmark at MI > log batch size is unfair."* Kept as a minor point above rather than removed, because the framing concern is real; but the Hard Rule on asymmetric comparisons would otherwise discount this, since the asymmetry favors the proposed method by exposing a baseline limitation the paper explicitly cites. Not a fatal flaw.
- *Strength: "addresses an important problem of MI estimation on discrete data."* Generic — removed.
- *Strength: "seamless integration with pretrained models."* Kept (concrete: MDLM-SMALL, CADUCEUS demonstrated).
- *"Missing comparison to Darrin et al. (2024) pipeline directly."* Removed — adjacent-method-comparison request that may stray into "missing related work" territory and the paper does compare against estimators in that family.

## Novel Insights
None beyond the paper's own contributions. The methodological novelty (Dynkin's formula + absorbing-state single-model trick for discrete KL) is genuinely new relative to MINDE's continuous-domain analogue, but no reviewer-side insight goes beyond what the paper itself argues.

## Suggestions
- Add a direct diagnosis of the J vs. C 2× gap on SUMMEVAL — either via a controlled synthetic at matched dimensionality or via a budget-matched compute analysis.
- Report SUMMEVAL/motif MI on held-out data and state the train/eval protocol in the main text.
- Add an `H(summary)`-only baseline to Fig. 1 to demonstrate the consistency test discriminates accuracy, not just order of magnitude.
- Soften "consistent estimator" in Sec. 3 to "consistent under bounded score-approximation error in expectation" and acknowledge Monte-Carlo and generalization error separately.
- Reframe Fig. 4 reference as "classifier-based proxy" rather than ground truth.

## Axis-by-axis assessment
- **Originality:** Strong — first principled CTMC/Dynkin-based KL estimator for high-dim discrete data; absorbing-state single-model trick is novel.
- **Importance of question:** High — discrete high-D MI estimation is genuinely under-served and the embedding-trick alternative is unsatisfying.
- **Are claims well supported?** Partially. Synthetic claims (Table 1) are well supported relative to admissible baselines; real-data accuracy claims rest on a proxy reference and an upper-bound target, and the J/C disagreement is unaddressed.
- **Soundness of experiments:** Mixed. Synthetic protocol is solid; real-data protocol lacks train/eval split disclosure and ground-truth substitutes are weaker than the text suggests.
- **Clarity of writing:** Generally clear; the gap between "consistent estimator" claim and what Eq. (7) actually proves should be tightened.
- **Value to the community:** Real — the absorbing-state single-model design and the pretrained-backbone integration are tools the discrete-MI community can use immediately.

## Score and Decision

Anchors:
- `0kWd8SJq8d.md` (MINDE) — avg 6.50, Accept. Most similar; this paper is the discrete-domain analogue with comparable rigor but weaker real-data validation (no train/test split, upper-bound reference, J/C gap). I rate INFO-SEDD slightly below MINDE.
- `KC2MViQASx.md` (f-DIME) — avg 5.60, Reject. Similar empirical-benchmark MI paper; INFO-SEDD's mathematical contribution is more distinctive than f-DIME's reweighting tweak.
- `PyHRUMxKbT.md` (InfoNet) — avg 5.75, Reject. Comparable: real method, real benchmarks, but real-data validation has gaps.
- `vgQmK5HHfz.md` (NF-DoE MI) — avg 4.83, Reject. Less mature than INFO-SEDD; INFO-SEDD is clearly stronger.
- `peNgxpbdxB.md` (Discrete diffusion samplers) — avg 6.00, Accept. Comparable level of methodological novelty in the discrete-diffusion space.
- `Wi74fYCX2f.md` — avg 5.00, Reject. Different topic.
- `h8GeqOxtd4.md` — avg 6.25, Accept. Different topic.
- `qOgLmcJxxF.md` — avg 5.75, Reject. Different topic.
- `kBLnxjuKd3.md` — avg 5.75, Reject. Different topic.
- `4SrzKsJocx.md` — avg 3.80, Reject. Substantially weaker than this paper.
- `WnqD3EiylC.md` — avg 5.00, Reject. Less impactful.
- `rdE9MCcNCz.md` — avg 4.50, Reject. Weaker than this paper.
- `MNGMpHxi1I.md` — avg 3.00, Reject. Substantially weaker than this paper.
- `PYQmaU4RwI.md` — avg 4.00, Reject. Far weaker.
- `orEX9GKQAD.md`, `1yJ3IDpb1D.md` — avg 4.00, Reject. Different topic, weaker.

Positioned just below MINDE (6.5) and roughly at f-DIME/InfoNet (5.6–5.75) but with stronger methodological novelty and a real engineering contribution (single-model absorbing-state design). The real-data evaluation issues keep it from MINDE's level.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>