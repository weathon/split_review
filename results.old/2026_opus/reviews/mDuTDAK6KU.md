Based on my reading of the paper and the calibration anchors, I'll now write the consolidated review.

## Summary
KOALA proposes an adversarial-example detector that runs two nearest-prototype classifiers in parallel — one using KL divergence between feature embeddings and class prototypes, one using a thresholded-deviation count called "L0" — and flags inputs as adversarial when the two heads disagree. The paper presents Theorem 1 (a "proof of correctness" under four assumptions), a clean-only fine-tuning recipe, and experiments on ResNet-18/CIFAR-10 and CLIP/Tiny-ImageNet with PGD, CW, and AutoAttack at ε ∈ {2/255, 4/255}.

## Strengths
- **Clean conceptual story**: The geometric intuition that KL is sensitive to dense, low-amplitude shifts while a thresholded-L0 score is sensitive to sparse, high-impact shifts is articulated clearly in Section 3.1 and Figure 1, and is supported by the ResNet ablation in Table 2 where KL+L0 beats L0+Cosine, KL+Cosine, and KL+L0+Cosine on accuracy/precision/recall/F1.
- **Lightweight, clean-only training recipe**: Section 3.3 introduces differentiable surrogates (sim_KL = exp(−KL); a sigmoid-smoothed L0) trained with BCE on clean image-prototype pairs, with no adversarial training. On ResNet/CIFAR-10 (Table 3) the KL+L0-fine-tuned model improves the integrated system's adversarial accuracy under PGD from the 45.5% baseline to 57.32% at ε=2/255, which is concrete evidence that the embedding-alignment objective is doing useful work.
- **Architectural generality**: Demonstration on both a small ResNet-18/CIFAR-10 setup and a CLIP/Tiny-ImageNet setup with text-derived prototypes shows the detector is not tied to one backbone or one source of prototypes.

## Weaknesses

### Fatal
- **No adaptive (detection-aware) attack evaluation.** Section 4.1 specifies the threat model as PGD/CW/AutoAttack at ε ∈ {2/255, 4/255} in L∞, but provides no indication that the attacks are crafted against the KOALA detector. KOALA's deterministic disagreement rule between two prototype-distance functions over the same encoder is exactly the kind of detector that is supposed to be evaluated under a joint loss like max(margin_KL, margin_L0) under the L∞ budget — the regime where Theorem 1's "the energy budget can't satisfy both flip conditions" argument has to be tested. The headline detection numbers in Table 2 therefore measure detection of attacks that were not trying to evade the detector. For a paper whose central claim is a proven detection guarantee, this is load-bearing and missing.

### Major
- **The confusion-matrix definition in Section 4.2 conflates detection with classification accuracy.** Per the definitions, TP := [a=1] ∧ [(â,ŷ) = (1,⊥) ∨ (â,ŷ) = (0, y*)] and FP := [a=0] ∧ [(â,ŷ) = (1,⊥) ∨ (â,ŷ) = (0, ¬y*)]. So an attacked input that happens to be classified correctly without being flagged counts as a true detection-positive, and a clean input that the prototype heads misclassify counts as a false detection-positive. Standard detection accounting treats those as a true negative and a true negative respectively. The paper itself states the reason the "Theorem-compliant" rows are all 1.0: "the theory assumes that clean, compliant examples are correctly classified by both the KL and L0 heads, leading to prediction agreement and preventing false alarms" — i.e., A4 plus this metric definition trivially yields the 1.0s. The detection numbers are not measuring the quantity the abstract advertises.
- **Theorem 1 verification (Table 1) is circular.** Theorem 1's condition (|c_i* − ĉ_i| > Γ_i(ε)) is stated relative to the *predicted adversarial class prototype* ĉ, which is only known after the attack runs. The "Theorem-Compliant" partition therefore conditions on the attack outcome, then reports perfect detection on that subset. A non-circular validation would specify the compliance condition purely from input-side or clean-embedding quantities. As stated, Table 1's perfect-row result is largely a mechanical consequence of the partitioning rule plus the confusion-matrix definition, not empirical evidence of the theorem.
- **Theorem 1's assumptions are not enforced in the experimental setup.** A1 requires *all* feature embeddings and prototypes to lie on the probability simplex (coordinates strictly positive and summing to 1). No part of Section 4 describes applying softmax to ResNet penultimate features or to CLIP image embeddings; on CIFAR-10 prototypes are mean embeddings and on Tiny-ImageNet they are CLIP text embeddings, neither of which lives on the simplex (so KL(c‖p) as written in Eq. 1 is not even well-defined). A2 bounds the perturbation *in feature space* by ε, but the attacks are bounded in *input space* and the paper handwaves the gap as following from "Lipschitz continuity of the backbone encoder" without bounding the constant. A4 requires both heads to agree on clean inputs in the true class — yet the CLIP precision of 0.66 in Table 2 indicates A4 is substantially violated in that setting. The "formal proof of correctness" therefore does not strictly apply to either experimental configuration as set up.
- **No comparison against existing detector baselines.** Section 2 lists Mahalanobis, NIC, LID, MagNet, feature squeezing, CADet, and Feinman et al., but Tables 1–4 only compare KOALA against itself (different metric combinations). For a paper whose contribution is a new detector, absolute numbers like 0.94/0.81 precision/recall on CIFAR-10 are uninterpretable without at least one contemporary detector baseline on the same architecture/attacks.
- **The CLIP results in Table 4 contradict the central thesis.** Under PGD on CLIP, KL+L0 yields 26.50%/25.47% adversarial accuracy while KL alone yields 60.02%/58.87% and L0 alone yields 53.31%/43.42%. If the complementary-metric story were correct, the combination should not be dominated by both singletons. The paper's explanation in Section 4.4 — that L0 is favored on CLIP because contrastive pretraining produces sparsity-aware structure, and that the high CLIP detection rate of KL+L0+Cosine arises because "the model is essentially randomly guessing" — is candid but post-hoc, and acknowledges that on CLIP the detector is being credited for collateral damage from the fine-tuning rather than for the principled disagreement mechanism.

### Minor
- **Assumption A3 is unsupported.** A3 stipulates |δ_i| ≤ (3/2)|p_i*| and labels this as "mild and practical." The constant 3/2 is not justified and no empirical measurement is given showing that real PGD/CW/AutoAttack perturbations in the feature space satisfy it. A direct measurement of the fraction of attack samples satisfying A3 (and what happens on those that do not) would either back up the theorem's relevance or contradict it.
- **The "adversarial accuracy" in Tables 3–4 is computed on inputs *not* flagged by KOALA**, which couples it to the detector's flag rate and makes cross-method comparison awkward. A standard reporting practice (accuracy under attack with and without abstention; ROC over the disagreement criterion) would let readers separate the detector from the classifier.
- **The disagreement criterion is binary**: any disagreement → attack. No threshold/operating-point sweep or ROC/AUC is reported, so the trade-off between precision and recall cannot be inspected. For a detection paper this is a meaningful omission.

### Trivial
- **The "L0" terminology is non-standard.** In the adversarial-robustness literature L0 is the count of non-zero coordinates of the perturbation; Eq. 2 defines a thresholded-deviation count relative to the mean absolute difference. Calling this "L0" is misleading; a name like "thresholded-deviation count" or "soft-L0" would prevent confusion.

## Nice-to-Haves
- Restate Theorem 1's compliance condition in terms of input-side or clean-embedding quantities so the partition in Table 1 can be defined before running an attack.
- Either softmax-normalize features so A1 holds (and KL is well-defined), or restate the theory in terms of a divergence that does not require simplex inputs.
- Add ROC/AUC over a sweep of the disagreement threshold (e.g., abstain when min_k L0(c_k,p) − second-smallest exceeds a margin).
- Empirically measure what fraction of attacks fall in the "compliant" subset, and how that fraction varies with ε — if it shrinks rapidly, the theorem's practical reach is narrow.
- Add at least one or two detector baselines (e.g., Mahalanobis, LID, CADet) on the same backbones and attacks to anchor the absolute detection numbers.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Strength: "Formal detection guarantee with empirical validation" yielding 1.0/1.0/1.0/1.0 on the theorem-compliant subset.** Removed: directly contradicted by the verified weakness that the compliance partition uses the post-attack class ĉ and the confusion matrix mechanically yields 1.0s under A4. The strength is a restatement of the metric definition, not independent evidence.
- **Strength: "Lightweight training without adversarial examples" yielding 57.32% PGD adversarial accuracy on ResNet-18 vs. 45.5% baseline.** Demoted/removed: while the number itself is in Table 3, attributing it to a robustness gain is premature because the adversarial accuracy is computed only on inputs not flagged by KOALA (Section 4.4), making cross-method comparison ill-posed. Keeping it as a strength would conflict with the Minor weakness on the same accounting.
- **Strength: "Semantic-free and plug-and-play."** Removed: this is descriptive rather than evidential.
- **Strength: "Thoughtful analysis of metric interference" in Section 4.4.** Demoted: the analysis is post-hoc and undercuts (rather than supports) the central thesis on CLIP.

## Novel Insights
None beyond the paper's own contributions. The "two-head disagreement as a detector" idea is a clean instantiation of well-known ensemble-disagreement reasoning, but no insight surfaced in the reviews that goes beyond what the paper itself states.

## Suggestions
- Implement an adaptive attack with white-box access to the encoder and both prototype heads, optimizing a joint loss such as max(margin_KL, margin_L0) under the L∞ budget; report detection metrics under this attack as the headline experiment.
- Replace the current TP/FP definitions with standard detection accounting: attacked ↔ positive, clean ↔ negative, with classification accuracy reported separately and an ROC over the disagreement threshold.
- Either softmax-normalize the features (so A1 holds for KL) or restate the theory using a divergence that does not require simplex inputs; then directly measure A2 and A3 on the PGD/CW/AutoAttack samples used.
- Recast Theorem 1's compliance test in input-side or clean-embedding terms; otherwise present the theorem as a feasibility result rather than an empirically-verified one.
- Add at least one contemporary detector baseline (e.g., Mahalanobis, NIC, CADet) on identical backbones and attacks.

---

## Evaluation Axes (in words)

- **Originality**: The KL+L0 disagreement framing is a modest variation of ensemble-disagreement detection rather than a genuinely new idea.
- **Importance of question**: Provably-correct adversarial detection is an important, long-standing problem.
- **Whether claims are well supported**: Several central claims are not well supported as written — the proof's assumptions are not enforced in the experiments; the "verification" is circular; the headline metrics use a non-standard confusion matrix; and the CLIP result actively contradicts the complementary-metrics narrative.
- **Soundness of experiments**: Falls short of community standards for detection papers (no adaptive attack, no detector baselines, single-run, non-standard confusion matrix).
- **Clarity of writing**: Generally clear and well-organized.
- **Value to the research community**: Limited in current form; could be sharpened substantially by the changes listed above.

---

## Calibration Anchors

Round 1 (bracketing):
- `KAWlH5pfQu.md` — avg 3.00, Reject. "Detecting Adversarial Examples" by layer regression with claimed theoretical theorem; explicitly criticized for no adaptive-attack evaluation, weak baselines, and a theorem with shaky assumptions. **Very close match to KOALA's structural problems.**
- `kz78RIVL7G.md` — avg 2.60, Reject. Statistical attack-agnostic detector claiming near-perfect detection — flagged as too good to be true.
- `lEsNGN1SjG.md` — avg 2.00, Reject. Information-theoretic bias classifier — much weaker than KOALA.
- `dIK7GpOwNY.md` — avg 3.00, Reject. Effective-dimensionality as a robustness metric — only loosely related.
- `r5d8zkYizS.md` — avg 5.33, Reject. Mercer-eigenvalue framework — primarily theoretical.
- `RzdtpxL0H5.md` — avg 6.20, Reject. DDAD with distributional-discrepancy detection — more thorough than KOALA.
- `YmQyEdLIkU.md` — avg 5.50, Reject. Same Mercer-eigenvalue paper reseen.
- `kwCHcaeHrf.md` — avg 5.50, Accept. SPADE with provable OOD/adversarial detection via EVT — stronger experiments (ResNet/VGG/ViT on CIFAR-10/100/ImageNet) but still criticized for weak attacks and strong Lipschitz assumption.
- `IGzaH538fz.md` — avg 8.00, Accept. GNNCert — deterministic certification on graph data; not topically aligned.
- `P7KIGdgW8S.md` — avg 8.00, Accept. Hölder stability of GNNs; off-topic.
- `I5lcjmFmlc.md` — avg 8.00, Reject. Diffusion-based robust classifier; out of scope.
- `cJs4oE4m9Q.md` — avg 8.00, Accept. Hypersphere anomaly detection; tangential.

Round-1 bracket: **3.0 – 5.5** (similar in spirit to KAWlH5pfQu at the bottom and SPADE at the top).

Round 2 (narrowing):
- `J2we1sVd9m.md` — avg 4.60, Reject. Prototype-based OT for OOD detection — uses prototypes like KOALA; more thorough OOD evaluation.
- `4BYzyGKIcb.md` — avg 4.00, Reject. Sharpness-aware geometric defense for OOD; methodologically more careful than KOALA.
- `Vi6p2TeujL.md` — avg 4.25, Reject. Prototype-oriented tabular anomaly detection; tangential.
- `28U5Olm32r.md` — avg 5.75, Reject. Model ensemble transferable attacks — primarily theoretical.
- `R1crLHQ4kf.md` — avg 5.00, Reject. KL/JS divergence over ASR output distributions for adversarial detection — very thematically close; gets uniform 5s.

Round-2 comparison: KOALA is closer to `KAWlH5pfQu` (3.0) than to `R1crLHQ4kf` (5.0) because of the structural metric-definition problem and the circular Theorem-1 verification, which the score-5 ASR-detection paper does not share. KOALA does test against stronger attacks (PGD/CW/AutoAttack) than `KAWlH5pfQu` (which was largely transferability-only) and presents a more developed theoretical narrative, so it should sit *above* KAWlH5pfQu but clearly below the 5.0 anchor. It is methodologically weaker than `J2we1sVd9m` (4.60) and `4BYzyGKIcb` (4.00), both of which use stronger evaluation protocols.

Final placement: ~3.5 — slightly above the 3.0 anchor (better attacks tested, cleaner theoretical exposition) but below the 4.0–4.6 prototype/OOD anchors (which have more rigorous evaluations and do not have a circular "verification") and well below the 5.0 ASR-detector and 5.5 SPADE anchors.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>