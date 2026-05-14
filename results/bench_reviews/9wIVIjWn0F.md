## Summary
The paper proposes RTA (Regression-based Test-Time Adaptation) for CLIP-based image classification. The idea is to train a lightweight LightGBM regression tree once, offline, on a set of pseudo-labeled images, to predict the cross-entropy loss of an augmented view from its logits, and then at test time select the top-k views with the lowest predicted loss for ensembling. Experiments are reported on ImageNet (and variants), 10 cross-domain datasets, and three multi-label datasets.

## Strengths
- The "Ceiling TTA" observation (Tables 1–2) is genuinely striking: selecting views by ground-truth cross-entropy loss reaches 90.2%/94.4% on ImageNet-A/R with ViT-B/16 (64 views), versus 64.3%/80.4% for entropy-based selection at the same view count. This is an interesting empirical phenomenon worth reporting even if the proposed estimator cannot reach this oracle.
- The proposed pipeline is genuinely lightweight: a single one-time training of a depth-5 LightGBM tree on 1k samples, with no test-time optimization, prompt tuning, or memory updates.
- Empirically, RTA reports gains over Zero/BCA on the ImageNet OOD average (e.g., +0.81 OOD avg over Zero on ViT-B/16 in Table 3) and beats ML-TTA across all three multi-label datasets (e.g., +1.67/+1.58/+2.99 mAP on RN50 in Table 5; +1.43/+1.47/+1.88 in Table 6), where the multi-label gains are the most substantive of the headline numbers.

## Weaknesses

### Fatal
None — the contributions are not invalidated outright, but the central conceptual claim has a serious gap (see Major).

### Major
- **Pseudo-label cross-entropy is, by construction, a near-deterministic function of the regressor's input.** Pseudo-labels are obtained by thresholding CLIP confidence at ≥0.8 (Sec. 5.1). Under this rule the pseudo-label is essentially always l = argmax_k softmax(s^reg)_k, so the regression target Eq. 4 simplifies to -log max_k softmax(s^reg)_k — a closed-form function of the same logits s^reg that constitute the tree's input. A regressor with sufficient capacity to fit this can do no more than learn a monotone transform of max-softmax probability. At test time, the tree only sees logits (no pseudo-label is computed per-view), so "ranking views by predicted loss" reduces to "ranking views by max-softmax." This makes the paper's headline framing — "view-loss mapping as a fundamentally new information source different from entropy" — incorrect as stated. The paper never runs the obvious sanity-check baseline: pick views by max-softmax (or -log max softmax) inside the same Zero-style ensembling pipeline. Without that baseline, all single-label gains are consistent with a renamed confidence selector. Why it matters: the central methodological contribution may be a re-parameterization, not a new mechanism.
- **The "Ceiling TTA" motivation does not bridge to the proposed method.** Tables 1–2 use ground-truth labels to compute LCE; the regressor never sees ground truth. Given the issue above, the gap between Ceiling LCE (e.g., 90.2% on IN-A) and what an input-deterministic regressor can attain is structural, not a tractability gap. The paper presents the ceiling as if the proposed method inherits its headroom; in Table 3 the actual gain over Zero on IN-A is +1.62%. Why it matters: the motivating narrative is much stronger than the achievable mechanism.
- **Cross-domain protocol is methodologically underspecified.** The tree is trained on ImageVal-12k as L=1000-dim ImageNet logits (Eq. 3) but applied to Flowers (102), Aircraft (100), DTD (47), EuroSAT (10), MSCOCO (80), VOC (20), NUSWIDE (81). Splits like "is coordinate 437 > τ?" have no shared semantics across these spaces. The paper does not describe any feature-mapping, padding, normalization, or per-dataset retraining. Either the "train once" claim is violated, or the same tree is applied to inputs whose dimensionality and feature semantics differ — making Table 4 currently uninterpretable. Why it matters: the cross-domain experiments are a major part of the empirical contribution.
- **Multi-label formulation is not specified.** Eq. 4 defines LCE via a single softmax index l, which is ill-posed when an instance has multiple positive labels. How the pseudo-label and target are constructed for multi-label training, and how the tree is queried at test time for multi-label prediction, is not described — yet the largest claimed gains are in this setting (Tables 5–6).

### Minor
- Sub-1% deltas (e.g., +0.24 on IN-1k for ViT-B/16; cross-domain average ViT-B/16 RTA 68.70 vs. BCA 68.59) are presented without seeds, variance, or significance, and on several cross-domain datasets RTA is below BCA (DTD 50.45 vs. 53.49; EuroSAT 53.65 vs. 56.63). The narrative bolds RTA cells without acknowledging these losses.
- Algorithm 2 Step 13 ("Average the predictions") leaves ambiguous whether averaging is over logits or probabilities; given the magnitude of the gains, this matters.
- Train/test distribution mismatch on regressor inputs is not analyzed: the tree is trained on logits of the *original* image (Sec. 4.2) but applied to logits of *heavily augmented* views at test time.
- The Spearman analysis (Sec. 4.1) examines the "top 10 features" pre-selected for highest correlation with the target; this is a selection-induced bias and does not establish that logits in general predict LCE.

### Trivial
- The decision-tree leaf count (16 leaves on 1000 samples) is at the low end for any claim that the regressor is exploiting nontrivial structure beyond max-softmax. This is borne out by Figure 5, where accuracy saturates with 1k–5k training samples.

## Nice-to-Haves
- A scatter plot of predicted LCE vs. true LCE on labeled test data (colored by whether the pseudo-label was correct) would directly visualize how close the regressor approaches the ceiling.
- Feeding the regressor with features the logits alone cannot recover (image embeddings, cross-view statistics, augmentation parameters) would be the natural way to actually transcend max-softmax confidence.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Strength claims like "the regression mapping is learned without ground-truth labels" and "extends naturally to multi-label" — these restate paper claims rather than evidence them, and the multi-label claim conflicts with the formulation gap noted in Major.
- Strength claim "ablations confirm robustness of design choices" — the ablations (Figures 4–5) vary view count and regression-set size only; they do not isolate the regressor's contribution against a max-softmax-ranked baseline.

## Novel Insights
None beyond the paper's own contributions. The main novel empirical observation — that ground-truth-LCE-based view selection nearly saturates accuracy — is already in the paper. The critical follow-up question the reviewers surface (whether the pseudo-label-trained regressor is functionally equivalent to max-softmax ranking) is a diagnosis of the paper's framing rather than a new insight.

## Suggestions
- Add the decisive control: same augmentations, same top-k, same ensembling as Zero, but rank views by max-softmax probability or by -log max softmax. Report rank correlation between the tree's predicted loss and max-softmax across views; if it is ~1.0, reframe the contribution.
- Specify and ablate the cross-domain protocol: is the tree retrained per dataset, or applied to differently-shaped logit vectors? If retrained, the "train once, deploy anywhere" claim should be removed.
- Define the multi-label target precisely (per-class binary CE? Sum over positives? Per-label tree?) and adjust Eq. 4 accordingly.
- Report seeds/variance on the headline tables; many cross-domain deltas are well within noise.
- Honestly discuss the rows where RTA underperforms BCA (DTD, EuroSAT on ViT-B/16).

## Evaluation Axes
- Originality: The Ceiling-TTA framing is novel; the proposed estimator's design fails to deliver a genuinely new signal beyond confidence.
- Importance: The problem (training-free TTA for CLIP) is established and active.
- Support for claims: Weak. The "view-loss mapping is new information beyond single-instance probability" claim is not supported once the pseudo-label collapse is taken into account, and the strongest motivating numbers (Tables 1–2) require oracle labels.
- Soundness of experiments: Mixed. Coverage is broad, but missing the max-softmax baseline, undescribed cross-domain feature mapping, and absent variance estimates undercut interpretability.
- Clarity: Acceptable at the surface but multi-label and cross-domain protocols are missing.
- Value to the community: The Ceiling observation is shareable; the proposed estimator as currently designed adds limited value.

## Score and Decision

Anchors retrieved:
- /home/wg25r/.../75PhjtbBdr.md (ML-TTA, avg 6.25, Accept) — directly comparable method on multi-label TTA; better methodological framing and clearer mechanism than RTA.
- /home/wg25r/.../kIP0duasBb.md (RLCF, avg 6.67, Accept) — clear conceptual contribution (CLIP reward), better-motivated than RTA.
- /home/wg25r/.../9w3iw8wDuE.md (DeYO, avg 7.00, Accept) — shares the "entropy is insufficient" thesis but builds a principled alternative confidence signal; RTA's alternative collapses to a confidence transform.
- /home/wg25r/.../yD2JMeKumt.md (DOTA, avg 6.00, Reject) — solid CLIP TTA with distributional modeling; tighter methodology than RTA.
- /home/wg25r/.../KNtcoAM5Gy.md (BaFTA, avg 5.50, Reject) — backprop-free CLIP TTA; comparable practicality to RTA but with clearer mechanism.
- /home/wg25r/.../z7PhIgVmZU.md (BAT-CLIP, avg 5.50, Reject) — bimodal CLIP TTA; comparable scope, similar score range.
- /home/wg25r/.../KZZbdJ4wff.md (PRO, avg 3.75, Reject) — pseudo-label CLIP adaptation with unclear pseudo-label dynamics; close analog in terms of pseudo-label-driven mechanism concerns; RTA has clearer empirical wins but a similar conceptual fragility.
- /home/wg25r/.../ezzmWTm8r6.md (Noisy-pseudo-labels TTA, avg 4.00, Reject) — pseudo-label TTA with confirmation-bias concerns; comparable to RTA's concerns.
- /home/wg25r/.../7iuFxx9Ccx.md (SlimTTT, avg 6.00, Reject) — broader TTT scope, more thorough experiments than RTA.
- /home/wg25r/.../PxL35zAxvT.md (TTA with Auxiliary Tasks, avg 4.67, Reject) — comparable in empirical scope but with a clearer mechanism than RTA.
- /home/wg25r/.../9bMZ29SPVx.md (CLIP-powered Data Selection, avg 7.50, Accept) — different domain but high quality; clearly above RTA.
- /home/wg25r/.../yINucFNbcZ.md (Conformal w/ TTA, avg 4.83, Reject) — different focus; comparable execution quality.
- /home/wg25r/.../XMlj8W8o0Y.md (HoughST VLMA, avg 4.00, Reject) — comparable concept-level concerns with weaker mechanism than RTA.
- /home/wg25r/.../EKfcngSxwD.md (Task Codebook VLM, avg 4.67, Reject) — different scope; similar marginal-novelty concerns.
- /home/wg25r/.../t84UBRhhvp.md (Text Descriptions, avg 4.75, Reject) — different angle.
- /home/wg25r/.../lCqNxBGPp5.md (vVLM benchmark, avg 5.00, Reject) — different scope.

RTA's empirical breadth (10 cross-domain + 3 multi-label) is comparable to mid-range CLIP-TTA submissions like BaFTA (5.5) and BAT-CLIP (5.5). However, the central conceptual collapse — pseudo-label CE reducing to a closed-form function of the regressor's input, making the method potentially equivalent to a max-softmax baseline never compared against — is more severe than the issues that pushed DOTA (6.0, Reject) and BaFTA (5.5, Reject) below the bar, and the cross-domain feature-mapping omission is a documented methodological gap. It sits closer to PRO (3.75) and the noisy-pseudo-label TTA paper (4.0) than to mid-range papers, though RTA's stronger empirical numbers and cleaner presentation lift it a notch above those.

MY FINAL SCORE: <pineapple>4</pineapple>
MY FINAL DECISION: <orange>Reject</orange>