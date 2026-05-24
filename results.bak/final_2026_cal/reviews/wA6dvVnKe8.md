Here is the consolidated review.

## Summary

This paper studies adversarial patch attacks on Vision-Language-Action (VLA) models. The authors propose EDPA (Embedding Disruption Patch Attack), a model-agnostic attack that requires only access to the visual encoder parameters (no knowledge of the action space, robot platform, or full model), and a complementary adversarial fine-tuning defense that strengthens the encoder against such patches. EDPA achieves 100% failure rate on OpenVLA across all four LIBERO task suites and transfers to multi-camera models (OpenVLA-OFT and π₀) with lower but still substantial effectiveness. The defense reduces EDPA-induced failures by 34.2% on average on OpenVLA while degrading clean performance by only 1.6%.

## Strengths

- **Model-agnostic attack design with genuinely reduced prior knowledge.** EDPA requires only the visual encoder parameters — unlike prior attacks (UADA, UPA) that need knowledge of the action space or robotic manipulator (Table 1, Figure 1). This makes it more broadly applicable across different VLA architectures and is a clean conceptual advance over prior work.

- **Very high attack effectiveness on the primary testbed.** EDPA achieves 100% failure rate on all four LIBERO suites for OpenVLA (Table 2), matching or exceeding prior attacks that demand far more system knowledge. The attack also produces large failure-rate increases on OpenVLA-OFT (+62.0%) and π₀ (+31.4% average, Table 3), demonstrating transfer beyond its design target.

- **Defense shows cross-attack transferability with minimal clean-performance loss.** The adversarial fine-tuning not only reduces EDPA failures (from 100% to 39.4–91.2% depending on task suite) but also improves robustness against the unrelated UADA and UPA attacks (Table 2), while clean FR increases only 1.6% on average. This indicates the defense is not narrowly overfitted to one attack pattern.

- **Novel defense training procedure.** Algorithm 1's use of intermediate adversarial patches (not just the final optimized patch) combined with periodic patch reset (φ=1000) is a well-motivated design that prevents overfitting to a specific patch pattern.

## Weaknesses

### Major

- **No ablation of the two loss components in EDPA.** The attack combines a patch contrastive loss (Eq. 2) and an image-instruction alignment loss (Eq. 3) with α₁=0.8. The paper provides no experiment isolating what each component contributes. This is a significant gap because it leaves the design rationale unsubstantiated — the reader cannot tell whether both losses are necessary or whether a simpler single-objective attack would perform similarly. Given that prior work (UADA, UPA) achieves comparable 99%+ FR on OpenVLA with entirely different loss formulations, this ablation is essential for understanding EDPA's methodological claim.

- **Defense evaluation lacks adaptive attacks and is tested on only one model.** The adversarial fine-tuning is evaluated only on OpenVLA and only against the *same* attack methods used in the paper (EDPA, UADA, UPA). An attacker aware of the fine-tuned encoder could craft patches specifically optimized against it. Without this evaluation, the reported robustness numbers may be artificially inflated. Since the defense is presented as a core contribution alongside the attack, this gap precludes assessing whether the defense provides meaningful security or only cosmetic resistance. The paper itself acknowledges the defense was tested only on OpenVLA because it showed the weakest robustness, but this does not address the adaptive-attack concern.

- **Attack effectiveness on multi-camera models is substantially lower without validated explanation.** On π₀, EDPA increases average FR by 31.4 percentage points (Table 3), compared to ~75 points on single-camera OpenVLA. The paper attributes this to training data diversity but offers this as a hypothesis, not a tested explanation. Separate patches are applied per camera view without testing whether alternative patch strategies (e.g., a single consistent patch appearing in both views) would be more effective. This limits the claimed model-agnostic practicality — the attack works much less well on models closer to real-world deployment.

- **High variance in defense effectiveness across task suites is not discussed.** After defense under EDPA attack, FR ranges from 39.4% (Spatial) to 91.2% (Long) — a 50-point spread (Table 2). The paper reports only the average improvement, leaving unexplained why the defense is far less effective on some task suites (especially Long, where FR remains above 90%). This undermines confidence in the defense's reliability.

### Minor

- **No sensitivity analysis of patch placement.** The paper evaluates patches at a fixed 50×50 size but does not examine sensitivity to patch location within the camera view, size, or occlusion of task-relevant objects. These factors are important for understanding real-world applicability.

- **Patch visualization hypothesis is presented without causal evidence.** Section 5 proposes that visual encoders overfit to the robot arm's appearance, supported by post-hoc patch visualization. This is an interesting insight but no causal experiment (e.g., fine-tuning on images with the arm masked out, or analyzing encoder attention) supports it.

- **The use of K=1 inner attack iteration is not justified.** Algorithm 1 uses a single gradient step per minibatch during patch generation, which is atypical for adversarial patches. Given that the attack achieves 100% FR, this seems to suffice, but the design choice merits discussion.

### Trivial

- None beyond what is noted above.

## Nice-to-Haves

- An ablation of α₁ (controlling the two loss components) would strengthen understanding of the attack design.
- An adaptive attack against the fine-tuned encoder would substantially strengthen the defense claims.
- The limitation section could explicitly note that the defense was tested on one model without adaptive attacks, adding appropriate caution.

## Removed Points

The following points from the input reviews were removed per the filtering rules:

- *"Defense is evaluated only on OpenVLA"* — This is kept as a Major weakness above (combined with the adaptive-attack point, since it's part of the same concern about defense evaluation completeness).
- *"Source code not provided"* — The paper states code will be released upon acceptance. This is standard practice and removed per hard rules on reproducibility nitpicks.
- *"Baseline attack is too weak (random noise)"* — The random noise baseline follows prior work (Wang et al., 2024) and is standard for this setting. The suggestion for a stronger baseline (e.g., classification-like objective) is a nice-to-have.
- *"Missing limitation about defense only tested on one model"* — Addressed in the evaluation; not a missing limitation per se since the paper already states "OpenVLA exhibited the weakest robustness against EDPA, it was chosen as the primary model for defense evaluation."
- Various formatting/style nitpicks from the reviewer inputs.
- Some Strength Finder items that were generic or sycophantic ("this paper addressed an important problem").

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Ablate the two loss components.** Run EDPA with only the patch contrastive loss (α₁=1.0), only the alignment loss (α₁=0.0), and the default (α₁=0.8) on OpenVLA. This would directly validate whether the combined objective is necessary or whether a simpler attack works equally well.

2. **Evaluate the defense under an adaptive attack.** Craft patches optimized against the fine-tuned encoder using the same EDPA procedure. If the defense still holds, it is substantially stronger. If not, the paper should honestly characterize the defense as limited to known attacks.

3. **Test alternative patch strategies for multi-camera models.** Evaluate whether a single patch placed to appear in both camera views (if possible in the simulator) yields higher attack success on π₀.

4. **Provide patch placement sensitivity analysis.** Report how attack success varies with patch location, size, and overlap with task-relevant objects.

5. **Discuss the variance in defense effectiveness across task suites.** Provide analysis or additional experiments to explain why some suites (Long) remain above 90% FR even after fine-tuning.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Queried the human-review corpus for papers on adversarial robustness of VLA models. Weak band (score <3.5): FreezeVLA (avg 3.00), VLA-Risk (avg 2.50), GoBA (avg 3.00) — all rejected/withdrawn, with issues including contrived threat models, insufficient novelty, simulation-only evaluation. Strong band (score >7.5): mostly unrelated papers (embodied navigation, multimodal reasoning) with avg scores of 8.00 — clearly out of this paper's range. Middle band (3.5–7.5): RobustVLA Multi-Modal (avg 6.00, Accept Poster), VLM4VLA (avg 7.00, Accept Poster), InstructVLA (avg 5.50, Accept Poster), RobustVLA RL (avg 4.50, Reject). Initial bracket: between 3.0 and 6.0.

**Round 2 (Narrowing):** Queried 4.0–5.5 and 5.5–7.0 bands for adversarial attack/defense papers. Key anchors: AdvMask (avg 4.50, Accept Poster), PSI Attack (avg 5.00, Accept Poster), RobustVLA Multi-Modal (avg 6.00, Accept Poster). Reading AdvMask (4.50): had extensive experiments but was criticized for weak attack strength and no adaptive attacks — similar limitations to our paper. PSI Attack (5.00): stronger attacks across multiple models with ablations, but was still accepted. RobustVLA (6.00): substantially stronger evaluation (17 perturbations, real-world tests). **Comparison:** The paper under review is clearly stronger than FreezeVLA (3.00) due to a more practical threat model and inclusion of a defense. It is comparable to AdvMask (4.50) — both have genuine contributions but suffer from incomplete evaluation (no adaptive attacks, limited attack strength validation). It is weaker than PSI Attack (5.00) which had careful ablations, and substantially weaker than RobustVLA (6.00) which had comprehensive evaluation including real-world experiments.

**Final score:** 4.5. The paper has a solid core contribution (model-agnostic attack + defense) but the evaluation is incomplete in ways that prevent the evidence from matching the breadth of the claims.

### Anchors Retrieved

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| zdvlLxRWSn (FreezeVLA) | 3.00 | 1 | Weaker threat model, no defense; our paper is clearly stronger |
| 31EjDFwFEe (VLA-Risk) | 2.50 | 1 | Reject; our paper's practical attack is more novel |
| j9k3Oamba8 (GoBA) | 3.00 | 1 | Reject; different setting (backdoor), less relevant |
| cS6xizdYD5 (RobustVLA MM) | 6.00 | 1,2 | Stronger evaluation with 17 perturbations + real-world; our paper is weaker |
| 9g7UXLqD4B (RobustVLA RL) | 4.50 | 1 | Reject; comparable quality, simulation-only with evaluation gaps |
| kzGkXpW4FT (AdvMask) | 4.50 | 2 | Accept Poster; similar level — good core idea, incomplete evaluation |
| liQueBuFXi (PSI Attack) | 5.00 | 2 | Accept Poster; stronger evaluation with ablations |
| 4ihxXIakoY (Token Robustness) | 4.67 | 2 | Reject; first work on tokenizer robustness |

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>