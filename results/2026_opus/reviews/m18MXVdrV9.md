Now I have enough information to write the meta-review. The closest anchors are MINDE (6.5, accepted) — the direct continuous-data predecessor — and F-DIME (5.6, rejected) — which shares the same baselines.

## Summary
This paper introduces INFO-SEDD, a method for estimating KL divergence, mutual information, and entropy for high-dimensional discrete data using Continuous Time Markov Chains and discrete diffusion score models. The method combines Dynkin's formula (to express KL as a time-integral of score-ratio terms) with the absorbing-state local rate matrix from SEDD/MDLM (so that one score model trained on the joint distribution also yields the marginals), wrapped into joint and conditional MI estimators plus an entropy estimator with an explicit consistency bound. Experiments cover a synthetic high-MI benchmark, text summarization (SUMMEVAL), genomics (HUMAN-vs-WORM classification and TATA-box motif discovery), and Ising entropy estimation.

## Strengths
- **Strong synthetic results in a regime where competitors fail.** Table 1 shows INFO-SEDD producing MI estimates within ~0.2–2.2 nats of ground truth from MI=10 to MI=50 with std < 1.2, while every competing method (GAN-DIME, MINDE, MINE, NWJ, SMILE, KL-DIME, HD-DIME) deviates by several nats — and at MI=50 most degrade to single-digit values. This is direct evidence that embedding-trick estimators break down in high-MI, high-dimensional discrete regimes while INFO-SEDD does not.
- **A single trained model serves both joint and marginal queries.** Eq. (6) and the absorbing-rate-matrix construction in Section 3 mean only one score network needs to be trained, with marginals recovered by querying absorbed positions. This is a concrete architectural saving over standard "train two estimators" recipes.
- **Composes with pretrained discrete-diffusion backbones (MDLM-SMALL, CADUCEUS).** This is what enables the motif-discovery use case in Section 4.3, Figure 5: one fine-tuning run over the joint distribution gives MI estimates for arbitrary sliding windows, where standard estimators would require a separate training run per window.
- **Explicit error decomposition (Eq. 7).** The bound cleanly separates estimation error (linear in score error) from truncation bias (exponentially decaying in T). This is exactly the right structural argument for "consistent without the exponential-variance pathology of variational lower bounds."
- **Useful downstream demonstration in genomics (Figure 5).** Recovering the TATA-box motif at the known position −35 in *Arabidopsis thaliana* promoters is a genuine application of accurate-enough discrete MI that the embedding-trick alternatives cannot easily reach.

## Weaknesses

### Fatal
None.

### Major
- **INFO-SEDD-J shows a substantial non-zero offset at ρ=0 in the text consistency test (Figure 1), and the paper underplays this.** From the figure description, INFO-SEDD-J sits near 10² nats at ρ=0 — i.e., the estimator returns roughly 100 nats even when summary and source are independent. The paper acknowledges this in passing ("INFO-SEDD-C obtains MI estimates closer to zero than the joint variant, when ρ = 0.0"), but Table 2's downstream model-selection analysis uses absolute INFO-SEDD-J MI as a regression signal against human metrics. A quantitative measurement of this truncation/finite-T bias as a function of T (on a synthetic problem with known MI, where this can be done cleanly) is the natural fix and is missing.
- **The "reference" curves in both real-data consistency tests are themselves approximations, not ground truth, and the writing oversells the comparison.** In Section 4.2 the 256–303 nat band is derived by multiplying a literature English entropy rate by the average summary length and by ρ — an order-of-magnitude proxy. In Section 4.3 the "Classifier-Based MI" reference treats H(Y|X) as H_b(Acc.), which is an upper bound on H(Y|X) and so a lower bound on true MI; INFO-SEDD-C tracking this curve is consistent with either correctness or overestimation. The paper presents matching these curves as evidence of accuracy ("INFO-SEDD-C outperforms competitors, closely matches reference MI"); the framing should be softened to "tracks an order-of-magnitude proxy that competitors fail to reach," which is the actual claim the evidence supports.
- **The synthetic benchmark (Table 1) is structurally well-aligned with the method's assumptions, and no benchmark with non-token-factorizable dependency is shown.** MI grows linearly with D (MI=10 at D=10, ..., MI=50 at D=50), implying each token contributes ~1 nat independently. This is the best case for a sparse rate matrix that perturbs one component at a time (Section 3). Embedding-based baselines, in contrast, have to learn through a continuous bottleneck that destroys this structure. Appendix C.1.6 ablates |χ|, not the dependency structure. The right addition is one synthetic setting where MI is concentrated in long-range or non-decomposable dependencies; whether INFO-SEDD still dominates there is a real open question that determines how broadly Table 1 generalizes.

### Minor
- **The model-selection interpretation in Section 4.2 is over-read.** Table 2 shows INFO-SEDD-C correlating 0.740 with consistency but also 0.679 with fluency. The paper rescues this by noting fluency correlates with consistency, but the abstract's "semantic-aware model selection in text summarization" claim would be much sharper if the paper actually compared model rankings induced by INFO-SEDD's MI to those induced by ROUGE/BERTScore on a held-out preference task. As presented, this is a correlation observation, not a model-selection contribution.
- **The training-strategy modification used to learn marginal/conditional scores is mentioned in passing in Section 4.2 and deferred entirely to Appendix C.2.** Since the method's core selling point is "one model serves joint and marginal queries," the precise modification is methodologically central and warrants a sentence or two in the main text alongside the high-level claim.
- **Eq. (7)'s bound scales with D|χ|, which is enormous for SUMMEVAL-scale vocabularies and sequence lengths.** The bound therefore does not numerically constrain the empirical accuracy on the real-data experiments. The paper's tone around Eq. (7) ("consistent estimator … without the exponential variance") slightly overstates what the bound buys you in practice. Stating consistency holds asymptotically while the empirical accuracy comes from score-model quality would be more honest.
- **Section 2.2 notation around which terminal of the chain holds data versus noise was hard to follow.** The boundary handling between Eq. (2) and Eq. (4) (omitting the t=0 vs t=T term) reads ambiguously; a half-sentence clarifying which endpoint is data would help.
- **Section 3's claim that the model can be queried at the "fully absorbed in Y, observed X" states.** These are low-density during training; the construction empirically works because MDLM-style training visits enough mixed-mask configurations, but a brief note on when this trade-off (controlled by σ(t)) breaks would aid reproducibility.

### Trivial
None worth listing.

## Nice-to-Haves
- A direct comparison against a classical discrete MI estimator (e.g., histogram or k-NN style) on the synthetic benchmark would demonstrate, rather than just assert, that classical estimators "rapidly decrease in accuracy with dimensionality."
- Wall-clock or FLOPs cost relative to baselines in the main text. The paper notes competitors are slower to converge (Appendix C.1.3) but does not compare total training cost, which is relevant given INFO-SEDD requires training a discrete diffusion model.
- A fully synthetic discrete (text, summary) channel with computable MI would give Figure 1 actual ground truth instead of a 256–303 nat band, and would also let the ρ=0 bias be measured directly.
- Plotting Eq. (7)'s numerical value alongside empirical error on the synthetic benchmark — either it tightens the connection or shows the bound is decorative; either outcome is more informative than the current phrasing.
- A head-to-head model-ranking comparison against ROUGE/BERTScore/BARTScore on SUMMEVAL would convert the correlation observation in Table 2 into an actual model-selection claim.

## Removed Points
*These points are flagged to be removed; treat them with caution — they were raised by the harsh critic but do not survive verification against the paper.*

- *"Eq. (7) is decorative because the bound is loose."* — The paper does not present Eq. (7) as a tight numerical bound; it presents it as a consistency argument explaining why INFO-SEDD avoids the exponential-variance pathology of variational lower bounds. That is a legitimate use of an asymptotic result and is not overclaimed in the body. Kept as a softer Minor point about tone, not as a separate flaw.
- *"Section 4.3 motif discovery only verifies relative MI, not absolute accuracy."* — Section 4.3 is upfront about this; using MI as a *signal* across windows is the contribution, not a claim of absolute correctness. The original criticism was not substantive enough to keep.
- *"Classifier-Based MI reference recovers the noise schedule, not the true MI."* — Partially valid technically, but already captured by the broader "reference curves are approximations" Major point. Merged rather than counted twice.
- *Strength: "Entropy estimation in Ising models (Section 4)."* — Detail is deferred to Appendix D and the main text only mentions it in one sentence; not enough concrete evidence in the body to count this as a separately-supported strength.
- *Strength: "Low sample complexity (Appendix C.1.5)."* — Real but deferred to appendix, and the headline claim "accurate at 10³ samples" is asserted in the main text without showing the curve. Reasonable to mention but not a top-tier strength.

## Novel Insights
None beyond the paper's own contributions. The genuinely interesting observation is the paper's own: by working natively in the discrete domain via CTMC time-reversal plus the absorbing-state trick, one can obtain an MI/entropy estimator that (a) avoids the embedding-trick continuous detour, (b) reuses a single trained score model for both joint and marginal queries, and (c) composes with pretrained discrete-diffusion backbones for downstream tasks like motif discovery. The applications-side observation that accurate-enough discrete MI unlocks single-model sliding-window analyses (Figure 5) is mildly novel — embedding-trick estimators cannot do this without per-window retraining.

## Suggestions
- Add a quantitative measurement of truncation/finite-T bias as a function of T on a known-MI synthetic discrete problem. Plot it alongside the INFO-SEDD-J curve to make Figure 1's ρ=0 behavior interpretable.
- Add at least one synthetic regime where the MI dependency is *not* token-factorizable (e.g., a global-mode mixture or a pairwise-coupled distribution with long-range correlations). This is the single most valuable addition for generalizing Table 1's claim.
- Soften framing around the "reference" curves in Sections 4.2 and 4.3 to "tracks an order-of-magnitude proxy that competitors fail to reach," rather than implying ground-truth recovery.
- Move the description of the training-strategy modification for marginal/conditional scores into Section 4.2 main text — at least a sentence specifying what was changed.
- Convert the model-selection correlation analysis into an actual model-ranking head-to-head against ROUGE / BERTScore on a held-out preference split.
- Add a wall-clock or FLOPs comparison to baselines in the main text.

## Axis Evaluation
- **Originality**: high. The CTMC + Dynkin + absorbing-state construction is a genuine new derivation for discrete MI estimation, not a discrete port of MINDE.
- **Importance of research question**: high. Discrete high-dimensional MI estimation is a real gap; existing work mostly does the embedding trick.
- **Whether claims are well supported**: mixed. The synthetic claims are well supported within a regime favorable to the method. The "consistency" claims on real data are supported relative to weak references; the model-selection claim is over-read.
- **Soundness of experiments**: solid. Same backbone across methods, reasonable seeds, multiple application domains. The remaining gap is the absence of a non-factorizable synthetic regime.
- **Clarity of writing**: adequate. Section 2.2's notation is dense; Section 3 is clean.
- **Value to the research community**: meaningful. The motif-discovery and SUMMEVAL applications are the kind of downstream use that justifies a new estimator paper.

## Calibration

Anchors retrieved:

**Round 1 (bracketing):**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4u0ruVk749.md` (avg 3.00, R1 weak) — diffusion for ITE; rejected, weakly related — paper under review is much stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/46tjvA75h6.md` (avg 3.00, R1 weak) — EBM + diffusion synergy; weakly related.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rAZ3yCpc3K.md` (avg 3.00, R1 weak) — information-theoretic critique of diffusion; weakly related.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/kKXIYUi8ff.md` (avg 3.00, R1 weak) — molecular-dynamics diffusion; weakly related.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0kWd8SJq8d.md` (avg 6.50, R1 middle) — **MINDE**: direct continuous-data predecessor; paper under review is essentially the discrete counterpart. Read in full.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pq1WUegkza.md` (avg 7.00, R1 middle) — convergence of discrete diffusion; orthogonal theory paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/peNgxpbdxB.md` (avg 6.00, R1 middle) — discrete diffusion samplers; orthogonal applications.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Ombm8S40zN.md` (avg 6.25, R1 middle) — steering MDMs; orthogonal applications.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EO8xpnW7aX.md` (avg 8.00, R1 strong) — permutation discrete diffusion; strong consensus accept, more polished than paper under review.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/tyEyYT267x.md` (avg 8.00, R1 strong) — semi-AR diffusion language models; strong accept, broader empirical impact.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/CxXGvKRDnL.md` (avg 8.00, R1 strong) — progressive compression diffusion; strong accept.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zMPHKOmQNb.md` (avg 8.00, R1 strong) — discrete walk-jump sampling for proteins; strong accept.

Round 1 bracket: between 5.5 and 7.5. The paper is clearly above the weak (3.0) tier (real contribution, real experiments) and below the strong-accept (8.0) tier (the application sections are useful but not field-shifting). The nearest topical anchor in the middle band, MINDE, sits at 6.5.

**Round 2 (narrowing):**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Piod76RSrx.md` (avg 5.50, R2) — slicing MI generalization bounds; rejected, more theoretical-only.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KC2MViQASx.md` (avg 5.60, R2) — **F-DIME**: same baselines (GAN-DIME, KL-DIME, HD-DIME) as paper under review; rejected. Read in full. Reviewers criticized inconsistent winners across estimators, weak bias-variance story, and shaky experimental claims. The paper under review has clearer wins (Table 1 dominance) but shares some risk of over-reading correlation results.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/PyHRUMxKbT.md` (avg 5.75, R2) — InfoNet: feed-forward MI estimator; rejected, weaker theoretical grounding.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/71mqtQdKB9.md` (avg 6.60, R2) — SEDD (the discrete-diffusion ratio-matching paper INFO-SEDD builds on); reviewers split but generally positive.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/sL2F9YCMXf.md` (avg 6.75, R2) — energy-based diffusion language models; accepted.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Mri9WIfxSm.md` (avg 6.75, R2) — efficient perplexity bound for CTMC discrete diffusion; accepted.

Round-2 comparison: the paper under review is **stronger than F-DIME** (KC2MViQASx, 5.6) — clearer winning margin on the synthetic benchmark, more diverse applications (text + genomics + Ising), and a cleaner theoretical motivation. It is **comparable to MINDE** (6.5) — extends MINDE's idea to a different (discrete) data regime with a method specifically tailored for that regime, has applications MINDE does not, but inherits MINDE-style issues (reference curves are not ground truth, some over-interpretation of correlation analyses). It is **weaker than SEDD-line follow-ups at 6.75–7.0** — those have either stronger language-modeling empirical wins or full convergence theory; INFO-SEDD's downstream applications are nice but not killer.

The paper sits closest to MINDE (6.5) with a slight discount for the ρ=0 offset issue, the favorable synthetic structure, and the over-interpretation of Table 2. I land at **6.0** — accept, sitting just below the MINDE anchor.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>