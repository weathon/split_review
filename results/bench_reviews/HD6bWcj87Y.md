## Summary
The paper introduces **In-Run Data Shapley**, a data attribution method that computes Shapley values along a single training trajectory by defining a per-iteration local utility (loss change over a single gradient update) and aggregating across steps via linearity. Closed-form expressions are derived under first- and second-order Taylor approximations of the local utility (reducing to per-step gradient dot-products and gradient-Hessian-gradient products), and "ghost dot-product" / ghost gradient-Hessian-gradient techniques allow all pairwise quantities to be computed inside 1–2 backpropagations without ever instantiating per-sample gradients. The result is the first Shapley-style attribution demonstrated at GPT-2-pretraining scale (~10B tokens of the Pile).

## Strengths
- **Ghost dot-product / ghost vHv derivation (Eq. 5, Section 4.2)** is a concrete engineering contribution: pairwise per-sample gradient inner products with no per-sample gradient materialization, by reusing activations and output-gradients already computed in backprop. This is portable to influence-function and DP work.
- **Empirical efficiency claim is well-substantiated (Figure on runtime, Section 5.1)**: first-order In-Run Shapley matches regular-training wall clock and is >30× faster than naive per-sample-gradient computation, putting Shapley-based attribution into the same compute envelope as ordinary pretraining for the first time.
- **Theoretical grounding of TracIN**: Theorem 4.1 / discussion after Theorem 1 makes explicit that the first-order quantity equals TracIN-Ideal, recasting a previously heuristic per-step gradient-alignment score as a Shapley value under an additive local utility — a clean theoretical observation rather than a re-derivation that pretends to be novel.
- **Second-order interaction term** has a principled, interpretable role (Theorem 4.2, term ②): it down-weights duplicates and near-duplicates via a Hessian-modulated interaction with the rest of the batch, which is conceptually what distinguishes Shapley from per-sample influence.
- **Stage-dependent attribution finding (Section 5.2.2)**: capturing the rise-then-fall trajectory of Pile-CC's contribution to math validation data is genuinely something final-model influence cannot expose.

## Weaknesses

### Fatal
None.

### Major
- **Data-curation evaluation has an in-distribution confound (Section 5.3, Figure 5).** The Pile validation set is used both to compute Shapley values and (implicitly, through the Pile test set) to evaluate convergence. Removing the 16% of training corpora whose gradients align negatively with the validation distribution will, almost by construction, accelerate loss on the same distribution — independent of whether those corpora are actually "low quality." Without a held-out out-of-Pile evaluation, or a comparison against cheap proxies (random 16% removal at matched compute, perplexity filtering, embedding-distance-to-validation), the "well-curated datasets still contain bad data" claim is weaker than presented. The paper does acknowledge "significant domain shift" might explain some negative values but does not isolate this from genuine quality detection.
- **Copyright/royalty conclusion overreaches what the method shows (Section 5.2.1).** The result is that a paraphrase/"similar topic" rewrite ranks the source corpus at 32–146 out of ~320k — i.e., topic-level gradient alignment exists. The paper extrapolates from this to a normative claim that "data owners should receive a royalty share for generated content, even if the output does not closely resemble the copyrighted material." The chosen Shapley utility is loss-change on a fixed validation point along one trajectory, not causal contribution to a particular generation; topic-level alignment may exist for thousands of training corpora simultaneously. The empirical observation is fine; the policy framing is a leap the gradient-dot-product cannot support and should be softened.
- **Adam vs SGD gap for a "foundation-model pretraining" framing.** The ghost derivations are SGD-specific and all case studies are run with SGD on GPT-2-small, while real pretraining uses Adam/AdamW. The paper does flag this in its limitations and argues SGD acts as a proxy, but the per-coordinate adaptive scaling of Adam changes the Taylor-expansion validity argument materially. The contribution as stated (data attribution for the foundation-model pretraining stage) is currently demonstrated only under the surrogate optimizer.

### Minor
- **No run-to-run stability analysis.** The conceptual selling point is "targeted attribution to the specific trained model." Without showing rank correlations across SGD seeds / batch orders, it is unknown whether per-point Shapley values are stable enough to support the data-curation and copyright applications, or whether they reflect mostly trajectory noise. A basic seed-variation study would directly test the central claim.
- **Limited evidence that the 2nd-order term is decisive.** Section 5.3 reports ~equivalent curation improvements from 1st- and 2nd-order Shapley. The interaction term has a clear theoretical role (near-duplicate down-weighting), but the paper does not show a setting (e.g., a controlled k-duplicate insertion test) where 2nd-order changes a decision. Without that, the 2× cost is hard to motivate beyond the conceptual justification.
- **Error-rate numbers for the Taylor approximation ("<10% first-order, <4% second-order," Section 4.1) are asserted without a stated protocol** — model scale, training stage, batch size, validation point. These carry real weight in justifying the approximation and should be backed by an explicit measurement.
- **Local utility is computed only over players that happened to land in the realized batch** (Section 4.1 and the augmentation argument), and the global Shapley is just the sum across $T$ steps. This sidesteps the Shapley combinatorial blow-up, but it also means the "Shapley axioms" hold for a sequence of local per-batch games rather than for a global retraining-style utility. The framing is honest in the technical statements but the introduction sells a stronger flavor of "axiomatic uniqueness" than the construction delivers.
- **Memory cost of ghost dot-product (storage of per-layer activations and output-gradients for the validation batch alongside the training batch) is not quantified.** The conclusion mentions gradient accumulation as a fallback but does not characterize scaling with $|D_{val}|$ or model size — relevant if the technique is to migrate to larger models.

### Trivial
- The "rank out of ~320k" framing makes top-145 look extreme, but absolute ranks of unrelated topic-level corpora are not measured, so the reader has no null distribution to compare against.
- Test-loss-vs-wall-clock (rather than vs iterations) for the curation experiment would be more honest given the 2× cost of 2nd-order Shapley computation during the original run.

## Nice-to-Haves
- Replicate one case study under Adam (even approximately) and report rank correlation with the SGD attributions, to substantiate the "SGD-as-proxy" claim empirically.
- A controlled near-duplicate stress test ($k$ copies of a corpus inserted into the training set) showing 2nd-order Shapley distributes the credit correctly while 1st-order/TracIN-Ideal does not — this would crisply demonstrate the value of the second-order term.
- Out-of-Pile evaluation in the curation experiment to rule out the in-distribution confound.
- A simple seed-variation table for the per-corpus rankings used in the copyright study.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Harsh critic's framing that "the first-order method is just TracIN-Ideal repackaged as Shapley."** This is technically correct but the paper explicitly states the equivalence in Section 4.1 and presents the contribution as (a) supplying a Shapley-axiomatic interpretation of an existing heuristic, (b) deriving the genuinely new 2nd-order term, and (c) providing the efficient ghost computation. Treating the equivalence as a "structural" flaw rather than an acknowledged framing decision is unfair.
- **Strength claim "first Shapley-value-based data attribution at pretraining scale"** as phrased is supported by the experiments, but the strength finder's broader "GPT-2 pretraining = foundation model pretraining" framing conflicts with the Adam-vs-SGD gap noted above; kept only as supporting evidence.

## Novel Insights
The cleanest novel observation is that **TracIN-Ideal is exactly the first-order Shapley value of an additive single-step local utility** — this is a small but real theoretical reframing that retroactively axiomatizes an existing heuristic and makes the route to a 2nd-order (interaction-aware) refinement obvious. The ghost dot-product extension from DP "ghost clipping" to pairwise inner products is a transferable technique that goes beyond the paper's own application. Beyond these, no insights emerge from the reviews that exceed the paper's own contributions.

## Suggestions
- Reframe the copyright discussion as: "gradient alignment persists under paraphrasing, which is suggestive for the copyright debate," and drop the explicit royalty-share normative claim, or move it explicitly to a discussion of implications.
- Add an out-of-distribution evaluation for the curation experiment (e.g., one external benchmark not derived from Pile).
- Report seed-to-seed rank correlation for the per-corpus attributions.
- Add a controlled duplicate-insertion experiment that 1st-order cannot solve but 2nd-order can; this would justify the extra backprop.
- Spell out the experimental protocol behind the "<10% / <4%" Taylor-error numbers.

## Evaluation by axis
- **Originality**: medium-high. The Shapley reframing of TracIN is a small but real theoretical step; the ghost dot-product/vHv for pairwise inner products is genuinely new in this context.
- **Importance**: high. Per-example attribution at pretraining scale is a problem with real legal and curation stakes.
- **Soundness of claims**: mixed. The efficiency claim is well-supported. The "targeted to a specific model" claim lacks stability evidence. The data-quality claim is confounded by in-distribution evaluation. The copyright/royalty claim outruns the method.
- **Experiments**: case studies are evocative and well-chosen but methodologically thin (single baseline, in-distribution evaluation, SGD only, no seed variation).
- **Clarity**: good. Theorems, ghost derivations, and limitations are stated cleanly.
- **Community value**: high — the ghost techniques and the per-iteration decomposition will be reused regardless of whether the case-study conclusions stand.

## Score and Decision

Anchors retrieved (all queries; subset read in full):
- `qk6AxjhFVR.md` — NESTLE (LLM data valuation), avg 5.25, Reject. Comparable framing but weaker theoretical novelty than this paper.
- `EDoD3DgivF.md` — Linear Representations & pretraining frequency, avg 6.00, Accept. Different topic; similar "first principled study at scale" flavor.
- `9EqQC2ct4H.md` — Crediting Data Contributors of Diffusion Models (Shapley for diffusion), avg 6.00, Accept. Closest match — Shapley scaling story with policy framing; this paper has stronger efficiency results.
- `zWqr3MQuNs.md` — Detecting Pretraining Data from LLMs, avg 6.25, Accept. Different problem; comparable maturity.
- `p85TNN62KD.md` — Versatile Influence Functions, avg 5.50, Reject. Similar gradient-based attribution; this paper has more striking efficiency wins.
- `esYrEndGsr.md` — Influence Functions for Diffusion, avg 8.00, Accept. Stronger theoretical-empirical integration than the paper under review.
- `jZw0CWXuDc.md` — LoGra / large-scale influence, avg 5.50, Reject. Very close analog (efficient gradient-projected attribution at scale); split reviews mirror likely fate here.
- `HE9eUQlAvo.md` — Influence-based data selection, avg 6.40, Accept. Comparable applied flavor.
- `PKqHT0xZhI.md` — Efficient Ensembles for TDA, avg 5.40, Reject. Less novel.
- `OLtD2vDF5X.md` — HyperINF, avg 4.88, Reject. Narrower contribution than the paper here.
- `9m02ib92Wz.md` — DataInf, avg 6.00, Accept. Same "closed-form efficient attribution" template; the paper here is more ambitious in scale.
- `kuutidLf6R.md` — Diffusion Attribution Score, avg 7.50, Accept. Stronger evaluation rigor than this paper's case studies.
- `WncnpvJk83.md` — GMValuator, avg 6.50, Accept. Comparable.
- `77zLqGGowO.md` — Data Attribution for Multitask Learning, avg 5.50, Reject. Less impactful contribution.
- `qUVP6IDc5J.md` — Eliciting Attributions from LLMs, avg 3.50, Reject. Much weaker.
- `BQgAToASdX.md` — Generalized Group Data Attribution, avg 4.00, Reject. Notably less novel.
- `fdvSCcB7i8.md` — Feature-Level Instance Attribution, avg 3.00, Reject. Far weaker.

Relative to the cluster, this paper sits **above** DataInf / NESTLE / LoGra (closer technical analogs) because of (a) the genuinely new ghost vHv derivation, (b) the cleaner theoretical bridge to TracIN, and (c) the demonstrated pretraining-scale runtime parity — but **below** the diffusion-attribution accepts (kuutidLf6R/esYrEndGsr) because the case studies have real methodological gaps (in-distribution curation eval, copyright overreach, no stability analysis, SGD-only). That puts it around the diffusion-Shapley accept (9EqQC2ct4H, 6.00) and slightly above DataInf, with a half-step bonus for the efficiency story.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>