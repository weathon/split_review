Based on my reading and calibration, I'll now write the final review.

## Summary
CausalNovo proposes a model-agnostic training framework for *de novo* peptide sequencing that formalizes the task as a Structural Causal Model with causal (signal) and non-causal (noise) factors, introduces a Causality Extraction Module to mask latent representations into causal/non-causal streams, and trains with three objectives (contrastive independence under replacement-based intervention, sufficiency CE on z_c, and a "purification" CE on z_s). Experiments wrap three baselines (CasaNovo, AdaNovo, π-HelixNovo) on three NovoBench datasets, with vulnerability, NSR, and cross-species analyses.

## Strengths
- **Consistent and sizeable empirical gains across baselines and datasets**: Tables 1 and 2 show CausalNovo improves all three baselines on all three datasets — e.g., AdaNovo HC-PT amino acid precision 0.492→0.634 (+14.2%), π-HelixNovo Seven-species PTM precision 0.362→0.513 (+15.1%), CasaNovo Nine-species peptide precision 0.529→0.564 (+3.5%). The fact that gains hold across three architectures and three datasets is meaningful.
- **Vulnerability evidence aligned with the claim**: Figures 1, 3 and Table 6 show baselines degrade substantially as non-causal peaks are perturbed, while CausalNovo variants degrade much less (e.g., +28.5% RI at threshold 1 on HC-PT in Table 6).
- **Cross-species leave-one-out generalization** (Table 3) shows the gains are not concentrated in a single species and survive distribution shifts across organisms.
- **Mechanistic interpretability evidence**: Table 7 shows the fraction of predictions whose top-3 attended peaks are all causal rises from 19.26% to 32.87%, providing some independent evidence for the attention-shift story.

## Weaknesses

### Fatal
None — the concerns below are serious but do not, individually or together, invalidate that the empirical gains exist.

### Major
- **Label-derived peaks are injected at the input via the "Causality Enhancement" step, with no matched-augmentation control** — Section 3.4.1 defines `x_intervene = x_replace ∪ x_theory`, where `x_theory` is the *complete theoretical b/y/a ion spectrum computed from the ground-truth peptide*. The encoder is therefore trained on inputs that carry ground-truth-derived signal. Table 5 attributes roughly half the intervention gain (+0.6 of ~1.2 AA precision points) to the "Enhance" component alone. The only control offered is a random-drop operation, which adds no information. Without a baseline that adds `x_theory` (or any non-trivial augmentation) *without* the CEM and the independence/purification losses, the experiments cannot separate "causal disentanglement" from "the encoder sees clean signal peaks during training." This bears directly on the central framing that the gains come from causality rather than augmentation.
- **The vulnerability test is on the same perturbation family used in training** — Figures 1 and 3 and Table 6 measure "vulnerability" by replacing non-causal peaks identified via the theoretical spectrum, which is exactly the construction used at training (Section 3.4.1, "Replace-based Perturbation"). The baselines have no exposure to that perturbation at training time; CausalNovo does. The curves therefore show robustness to the augmentation distribution, which is partially circular as evidence of "causal grounding." A test using perturbations outside the training family (random noise injection not tied to the theoretical b/y/a split, intensity reweighting, or held-out perturbation types) would close this gap.
- **No direct validation that the learned mask M aligns with causal peak positions** — M is the actual implementation of "causal vs. non-causal" (Eq. 3), yet the paper only evaluates attention matrices (Table 7), not M itself. An obvious experiment — using M as a classifier over signal vs. non-signal peaks on held-out spectra and reporting AUC — is absent. Given M is the linchpin of the disentanglement story, this is an unforced evidentiary gap.

### Minor
- **The "purification" derivation is at least under-explained**. Section 3.3 says maximizing I(z_s; Y) "indirectly leads to the purification of z_c," citing Chen et al. 2022. The full combined loss is never written out explicitly, and the reader is left to reconcile "z_s should not carry label information" with an objective that maximizes its label-predictive power. The framing is defensible (the cited prior work does something similar with shared masks creating competition for label information), but the paper would benefit from spelling out the mechanism. Not fatal, but worth tightening.
- **No seeds / no error bars on any main table**. With several gains in the 1–3 AA precision-point range (e.g., +0.4 in the "Symmetric" row of Table 4, +0.6 in the "Replace" row of Table 5), the lack of even a small variance characterization makes the smaller ablation-level claims hard to weight. Multi-seed reporting is not universal in this field but is increasingly expected.
- **Reproduction gaps versus NovoBench's published numbers deserve acknowledgment**. The †-retrained baselines differ from NovoBench by up to ~4 points (CasaNovo Nine-species AA precision: 0.697 → 0.741; AdaNovo: 0.698 → 0.681; π-HelixNovo HC-PT peptide precision: 0.356 → 0.301). The "+CausalNovo" comparisons are fair against †, but the comparisons against non-retrained SOTA (e.g., SearchNovo) inherit this asymmetry and should be qualified.
- **"Up to 10%" in the abstract is a max, not a typical**. Typical gains over † baselines are ~2–6 points; the largest gains concentrate on weaker baselines on harder datasets. A more representative phrasing would be more accurate.
- **The conclusion concedes that the more realistic large-corpus OOD protocol used by ContraNovo/RankNovo would be a better test of the robustness claim**. The acknowledgment is honest, but since robustness is the central pitch, evaluating only under NovoBench's setup limits the strength of the headline claim.

### Trivial
None worth flagging.

## Nice-to-Haves
- A matched-augmentation baseline: train the baseline encoder on the same `x_replace ∪ x_theory` inputs with the same compute budget but without the CEM, independence, or purification losses. This is the single most informative additional experiment.
- A direct M-alignment metric (e.g., AUC of M against b/y/a peak positions on held-out spectra).
- A robustness evaluation using perturbations outside the training-time family (random Gaussian peaks, intensity jitter, cross-instrument variation).
- Multi-seed runs with reported variance on the main tables.
- An evaluation under the ContraNovo/RankNovo large-corpus OOD protocol.
- A training-time vs. accuracy curve given the disclosed 2.3× training cost.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"The purification objective is internally inconsistent with the stated goal" — fatal claim by the harsh critic.* Demoted to Minor. The paper's framing is admittedly under-explained, but the design follows Chen et al. 2022's logic where the auxiliary stream creates competition for label information via the shared mask. Calling it "internally inconsistent" overstates the case without seeing the full combined loss; it is more accurately a clarity/derivation gap.
- *Generic strengths about "principled SCM formalization" being a clear theoretical departure.* Kept only insofar as it grounds the contrastive/sufficiency objectives; the SCM diagram itself is light and does not, on its own, constitute a contribution.
- *"Up to 14.2% relative improvement" framed as a top-line strength.* Kept the underlying numbers as evidence, but flagged the abstract's framing in Minor — the typical improvement is several points lower.
- *Ablation in Table 4 / Table 5 "all-checkmarks" presentation.* Parser artifact, ignored.

## Novel Insights
None beyond the paper's own contributions. The most useful synthesizing observation from the reviews is the structural one: when a "causal" framework's intervention injects label-derived signal at the input and is evaluated under perturbations drawn from its own augmentation distribution, the burden of evidence for "causality, not augmentation" requires a matched-augmentation control and a direct mask-alignment check — neither of which the paper provides.

## Suggestions
- Add the matched-augmentation baseline (same `x_replace ∪ x_theory` inputs, no CEM/independence/purification losses) and re-report Tables 1–2 against it. If CausalNovo's margin survives, the causal framing is substantially more credible.
- Add a direct AUC-style evaluation of mask M as a causal-peak classifier on held-out spectra.
- Add an out-of-family vulnerability test (e.g., Gaussian noise injection not constrained to the theoretical spectrum split).
- Write out the combined loss explicitly and reconcile the maximize-I(z_s; Y) step with the "purification" claim.
- Add at least three seeds with variance bars on the main tables and ablations.
- Soften the abstract's "up to 10%" to a more typical figure, and acknowledge the reproduction gaps in the † baselines.

## Evaluation by axis
- **Originality**: Moderate. The SCM-style causal disentanglement framework is well-trodden in computer vision and graph learning; the contribution is applying and adapting it to spectral peak inputs.
- **Importance of research question**: High. *De novo* peptide sequencing under noisy spectra is a real, active problem.
- **Are claims well-supported?**: Partially. The "consistent empirical improvements" claim is well-supported; the "causal disentanglement, not augmentation, drives the gains" claim is undersupported.
- **Soundness of experiments**: Mixed. Breadth across three baselines and three datasets is good; the missing matched-augmentation control, the in-distribution vulnerability test, and the absent direct M-alignment evaluation are real soundness gaps. No seeds.
- **Clarity of writing**: Reasonable overall; the purification derivation is the weakest part.
- **Value to research community**: Real — the empirical improvements are large enough that practitioners may want to try the framework even if the causal framing is overstated. But the methodology, as currently evidenced, will leave open whether it's the "causal" piece or the augmentation piece that helps.

## Anchor calibration

Round 1 anchors retrieved:
- /home/wg25r/.../AvXrppAS2o.md — avg 3.00 (R1, weak): causal structure learning for outcome prediction; weaker scope and execution than CausalNovo.
- /home/wg25r/.../JzFLBOFMZ2.md — avg 3.20 (R1, weak): LLM-supervised CSL; less empirically thorough than this paper.
- /home/wg25r/.../yIRtu2FJvY.md — avg 3.00 (R1, weak): VEP with VAE; topical-adjacent biology paper, weaker than this.
- /home/wg25r/.../UO6JmbwVkC.md — avg 3.00 (R1, weak): adsorption-energy causal perspective; weaker.
- /home/wg25r/.../uQnvYP7yX9.md — **avg 6.50 (R1, mid, READ)**: ReNovo, direct de novo peptide sequencing competitor; cleaner contribution and broader cross-reviewer agreement than CausalNovo.
- /home/wg25r/.../I2ZYngkRW6.md — avg 4.25 (R1, mid): NAT distillation for de novo; weaker than CausalNovo on empirical breadth.
- /home/wg25r/.../87B3zDRMjv.md — **avg 5.50 (R1, mid, READ)**: RankNovo, direct competitor with similar robustness pitch and methodology concerns; reviewers flagged modest gains and missing analyses.
- /home/wg25r/.../jqmptcSNVG.md — avg 6.20 (R1, mid): peptide design, less directly comparable.
- /home/wg25r/.../zMPHKOmQNb.md — avg 8.00 (R1, strong): protein discrete walk-jump; well above this paper's contribution.
- /home/wg25r/.../KSLkFYHlYg.md — avg 8.00 (R1, strong): ShEPhERD; above.
- /home/wg25r/.../0ctvBgKFgc.md — avg 8.00 (R1, strong): ProtComposer; above.
- /home/wg25r/.../kJFIH23hXb.md — avg 8.00 (R1, strong): SE(3) flow matching; above.

Round-1 bracket: **between 4.5 and 6.5**, anchored on RankNovo (5.5) below and ReNovo (6.5) above.

Round 2 anchors retrieved:
- /home/wg25r/.../22ywev7zMt.md — avg 5.67 (R2): SSL OOD via SCM; similar causal-framing methodology with similar evidentiary gaps.
- /home/wg25r/.../tlH4vDii0E.md — avg 5.60 (R2): Robust Causal Representation Learning for PLMs; similar disentanglement pitch.
- /home/wg25r/.../vmkpk0ed1F.md — avg 5.40 (R2): Spuriousness via PID; methodologically more principled.
- /home/wg25r/.../q07DDpu8Xb.md — avg 5.25 (R2): Identifiability in causal rep learning; more theoretical.
- /home/wg25r/.../2uQBSa2X4R.md — avg 6.50 (R2): Robust Gymnasium benchmark; not comparable.
- /home/wg25r/.../1STZCCI8mn.md — avg 6.00 (R2): CNS-Bench; not comparable.
- /home/wg25r/.../icTZCUbtD6.md — avg 6.20 (R2): hardness analysis; not comparable.
- /home/wg25r/.../W0zgCR6FIE.md — avg 5.75 (R2): Spawrious benchmark; not comparable.
- /home/wg25r/.../ZXs3pkmrRG.md — avg 5.50 (R2): Test-time learning of causal structure; similar in methodology, less empirically strong.
- /home/wg25r/.../lQYi2zeDyh.md — avg 5.00 (R2): amortized causal discovery; weaker on empirics.

Placement: CausalNovo's empirical breadth (3 baselines × 3 datasets + cross-species + NSR + vulnerability) is stronger than the cluster of causal-rep-learning rejects in the 5.25–5.67 band, but its causal-framing concerns mirror theirs almost exactly (label-derived signal injected, in-distribution robustness test, no direct mechanism validation). The direct competitor RankNovo (5.5) is the closest single anchor: similar empirical-improvement story, similar reviewer pushback on what's actually driving the gains. ReNovo (6.5) is a cleaner contribution with a more crisp methodological story and stronger reviewer consensus. The empirical breadth pushes CausalNovo above the 5.25–5.5 cluster slightly, but the structural concerns about whether causality (vs. augmentation) is doing the work keep it below ReNovo.

Final position: between RankNovo (5.5) and ReNovo (6.5), closer to RankNovo because of the structural critiques on causality framing — around **5.0–5.5**. The methodological concerns are non-trivial enough that I lean 5.0.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>