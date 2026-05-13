## Summary
The paper introduces DeTrans, a post-hoc protection framework for pre-trained DNNs that aims to simultaneously prevent unauthorized inference (source-domain accuracy degradation) and cross-domain transfer (transferability reduction). It generates WAE-based auxiliary domains, selects one highly transferable filter per convolutional layer, and uses a bi-level optimization to perturb those weights; the original values are stored in TEE for authorized inference. Reported results show ~10% source accuracy and up to 81.23% transferability drop on digit/CIFAR pairs for VGG-11/ResNet-18 (and a single ResNet-50 case).

## Strengths
- **Clean problem framing of a real gap.** The paper exhibits a concrete asymmetry in the SOTA: NNSplitter cuts source accuracy but drops transferability by only 0.46%/0.39% (Tab. 2), while NTL/CUTI cut transferability but keep source accuracy high (Tab. 1). Targeting both jointly for *pre-trained* models (post-hoc, not from-scratch) is a defensible contribution.
- **Bi-level formulation that explicitly models the attacker step.** The lower level (Eq. 5) simulates an attacker fine-tune, the upper level (Eq. 6) degrades transferability conditioned on that simulated adaptation. The ablation against naive alternating defense/attack (>80% drop vs. 1.3%, Tab. 3) gives a meaningful, non-trivial argument that the bi-level structure matters.
- **Deployment-grounded budget.** Modifying only 0.07–0.18% of weights (79KB / 122KB) is anchored in TrustZone's 3–5MB secure memory limit, not picked for convenience.
- **Honest scoping.** Authors explicitly state DeTrans targets target domains *close to* the source (Sec. 2.1), aligned with the single-domain-generalization premise it borrows from.

## Weaknesses

### Fatal
None.

### Major
- **No adaptive attacker.** The threat model (Sec. 2.1) grants the attacker full architecture + weights and assumes the protection mechanism is in unsecured memory, yet evaluation restricts the attacker to naïve fine-tuning (last layer or whole model). Since DeTrans concentrates *the entire* perturbation in one filter per layer (the most-transferable filter, by construction), and stores the originals in TEE because they're small (Sec. 2.3 says "small enough to be stored in TEE"), the perturbed weights are likely magnitude/statistical outliers and detectable. An attacker who knows DeTrans is in use can plausibly localize and reinitialize/re-train those filters from a small fraction of target data. The paper does not test this attack, yet it is the natural adversary against an IP-protection scheme (Kerckhoffs's principle). This is the single biggest gap in the security argument.
- **Auxiliary-domain → target-domain link is asserted, not demonstrated.** The bi-level objective is optimized exclusively against WAE-generated auxiliary domains derived from the source, but evaluation transfers to MN↔US/SV and CF10↔STL10. There is no distributional analysis (e.g., feature-distance or coverage statistics) showing that the auxiliary set spans or even resembles the real targets. The "close target distribution" assumption (Sec. 2.1) is doing essentially all the generalization work and is never tested.
- **Filter-selection contribution is weakly supported.** Fig. 3 shows random filter selection achieves most of the transferability reduction; DeTrans's transferability-ranked selection adds only ~14.95% on average, on VGG-11. Given one filter per layer, this suggests the bi-level optimization, not the ranking metric (Eq. 2–3), is the dominant ingredient — yet the ranking metric is presented as a core contribution.
- **Authorized-user accuracy with the TEE-restoration path is never measured.** The whole usability claim hinges on TEE returning the original weights at inference so legitimate users recover near-baseline accuracy. No table reports authorized accuracy of the full pipeline; the paper defers to "the effectiveness of TEE has been previously established" (Sec. 2.3). Security isolation is well-established; *functional correctness* of partial-weight restoration in this specific setting is not, and is a load-bearing claim.

### Minor
- **No sensitivity to attacker data budget.** Attackers are fixed at 5% target data. Transferability defenses typically degrade as attacker data grows; without a sweep (1%/10%/25%/...) the robustness curve is unknown.
- **No sensitivity to the number of perturbed filters per layer.** Sec. 5.1 only ablates *first layer (p1)* vs. *one-per-layer (p2)*, not *k>1 per layer*. This is the most natural ablation for a method whose central design choice is "one filter per layer."
- **Scalability evidence is thin.** Sec. 5.2's ResNet-50 result is a single source→target on CIFAR-10 in one small table. Calling this "applicability beyond smaller models" overstates the evidence.
- **No variance/std reported on Tab. 1, 2, 4.** Many headline drops are ~80%; standard deviation across seeds would help interpret the gaps to NTL/CUTI ("within 4%").
- **Strawman in the optimization ablation.** The "naive alternating defense/attack" baseline trivially loses because the attacker moves last. This shows naïve alternation is bad, not that *bi-level* is uniquely necessary; a stronger naïve baseline (e.g., regularizing against a frozen surrogate attacker) would be more convincing.

### Trivial
None retained (per parser-artifact rule).

## Nice-to-Haves
- Feature-map or representation-similarity visualizations showing the perturbed filters actually disrupt shared features, which is the mechanistic story.
- A composed baseline: NNSplitter + a transferability-reduction module post-hoc, to verify the "cannot be combined" claim (Sec. 1) empirically rather than rhetorically.
- Distributional analysis (e.g., MMD or A-distance) linking generated auxiliary domains to evaluated target domains.

## Removed Points
*These points are flagged as removed; treat them with caution.*
- **Eq. 2 missing the square in σ² (parser artifact).** Removed under the formatting/parser rule — the original LaTeX likely renders correctly.
- **"NTL/CUTI could be configured to also degrade source-domain accuracy" composed-baseline framing as a fairness complaint.** Asymmetry favors the baselines (they are trained from scratch with full source data, vs. DeTrans's post-hoc setting); the paper's intentional asymmetry is to demonstrate a different problem regime. Kept as a *nice-to-have* (composed baseline) rather than a weakness.
- **Strength: "Robustness to attacker fine-tuning strategies" (Tab. 4).** Partially conflicts with the verified Major weakness on adaptive attackers — Tab. 4 only covers a1/a2 naïve fine-tunes, so it does not support a general robustness claim.
- **Strength: "Scalability to ResNet-50".** Kept downgraded — a single number is suggestive, not conclusive (see Minor).
- **Strength: "Applicability to pre-trained models as post-processing".** Kept as part of the framing strength.

## Novel Insights
None beyond the paper's own contributions. The principal insight — that source-accuracy degradation and transferability reduction are orthogonal protection axes for pre-trained models, and can be tackled jointly via a bi-level objective over filter-level perturbations confined to TEE memory — is the paper's own.

## Suggestions
- Run the adaptive-attacker experiment: detect the perturbed filters via magnitude/activation anomalies, reinitialize and retrain them from a 1–50% sweep of target data. Report transfer accuracy as a function of attacker data budget.
- Quantify auxiliary-vs-target distributional alignment (MMD, FID, or simple feature-space distance) and correlate that alignment with DeTrans's transferability-reduction effectiveness.
- Add an authorized-inference end-to-end measurement: accuracy and per-batch latency for the TEE-restoration pipeline (even simulated TEE access) on the same source-domain test set.
- Sweep k (filters per layer) in {1, 2, 4, 8} and report Pareto curves of (TEE storage, source drop, target drop).
- Report mean ± std over ≥3 seeds for all main tables.

## Evaluation
- **Originality:** Moderate. Combines single-domain generalization, filter masking, and bi-level optimization — all imported — into a new joint-protection framing for post-hoc pre-trained models. The framing is the most novel piece.
- **Importance:** Reasonable. On-device DNN IP is a real concern and the joint-protection gap is genuine.
- **Soundness of claims:** Partially supported. Source-degradation and transferability-reduction numbers are believable, but the security claim is undermined by no adaptive attacker, and the generalization claim by no link from auxiliary to target distributions.
- **Soundness of experiments:** Limited. Tiny datasets/models, single attacker budget, no variance, scalability section is one paragraph.
- **Clarity:** Mostly clear; equations and the framework figure are readable. Some prose imprecision around what TEE measures.
- **Value to community:** A useful framing and a reusable bi-level formulation; the empirical evidence is not yet strong enough to be load-bearing.

## Score and Decision

**Anchors returned by `calibration_search` (one batch):**
- `e2YOVTenU9.md` — ArchLock (avg **5.67**, Accept). Closest neighbor: same authors' line on transferability defense; here at parameter level instead of architecture level. Comparable contribution magnitude, slightly weaker empirics (Fig. 3 random-selection issue, no adaptive attacker). **Most direct anchor.**
- `029hDSVoXK.md` — Dynamic Neural Fortresses (avg **6.80**, Accept). Higher band; stronger model-extraction defense story with adaptive evaluation — this paper is clearly below.
- `0tMcsHsHgQ.md` — Undistillable Models via CMI (avg **5.50**, Reject). Comparable IP-protection framing; similar borderline.
- `PCm1oT8pZI.md` — Safe & Robust Watermark (avg **5.75**, Accept). Same IP-protection space, more thorough threat-model evaluation; this paper sits slightly below.
- `gjFgBfbP2C.md` — NeuralMark white-box watermarking (avg **5.25**, Reject). Comparable IP-protection paper, borderline reject.
- `wE5xp3zBaQ.md` — Watermarks/Transferable Attacks (avg **5.00**, Reject). Theoretical framing in same neighborhood.
- `KRMSH1GxUK.md` — LLM IP infringement watermarks (avg **5.80**, Accept). Medium-high band.
- `WNSjteBJd9.md` — Tracking IP infringers in FL (avg **5.33**, Reject). Borderline reject; comparable scope.
- `sruGNQHd7t.md` — Privacy via Domain Shifting (avg **3.00**, Reject). Low-band; weaker threat-model and methodology than this paper.
- `tqYx8DgL0u.md` — Homomorphic Adversarial Nets (avg **3.67**, Reject). Low band; not closely related.
- `i8ynYkfoRg.md` — Model Entanglement FL (avg **3.00**, Reject). Low band.
- `BRDqmYU8A0.md` — Model Developmental Safety (avg **5.50**, Reject). Different topic; similar borderline.
- `tiJzOop4u6.md` — Adv. attacks vs. diffusion mimicry (avg **6.25**, Reject). Higher score despite reject; less related.
- `qbw861vueP.md` — BiDST sparse training (avg **4.33**, Reject). Different topic.
- `9vZ8UjP2Mz.md` — AID bi-level generalization (avg **5.00**, Reject). Different topic.
- `oxjeePpgSP.md` — Backdoor CL via bi-level (avg **5.75**, Accept). Different topic; bi-level method paper that landed accept on tighter empirics.
- `VRTCXYvPxc.md` — VideoGuard (avg **4.50**, Reject). Same protection-via-perturbation flavor with similar empirical thinness.

DeTrans is comparable to ArchLock in framing/contribution but weaker on two fronts (adaptive attacker missing; random-filter ablation eats most of the gain). It sits a touch below ArchLock (5.67) and around NeuralMark/Tracking-IP (5.25–5.33). I place it at 5.0.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>