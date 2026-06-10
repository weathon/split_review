Now I have all the information needed to write the final review. Let me synthesize everything.

## Summary

The paper proposes Entity Interaction Transformer (EIT), a Transformer-based architecture for goal-conditioned multi-object manipulation from pixels. Combined with Deep Latent Particles (DLP) as an object-centric image representation, the method is evaluated on simulated robotic pushing tasks. The main empirical finding — that EIT outperforms the prior work SMORL on tasks requiring object interactions (Ordered-Push, Adjacent-Goals, Small-Table) — is well-supported. However, two claimed contributions lack supporting evidence in the paper: the Chamfer reward has zero quantitative evaluation, and the Cube Sorting generalization claim (3→12 objects) is purely qualitative.

## Strengths

1. **EIT explicitly models entity interactions, enabling tasks SMORL cannot solve.** SMORL's per-object independence assumption is fundamentally limited on interaction-heavy tasks. The paper provides clear quantitative evidence: on Ordered-Push, EIT with state achieves ~0.94 success rate vs. SMORL with state at ~0.45 (Fig. 2d); on Adjacent-Goals, EIT with state achieves 0.963 vs. SMORL with state at 0.716 (Table 1). These results directly support the paper's central claim.

2. **Image-based EIT matches or exceeds state-based SMORL on interaction tasks.** On Adjacent-Goals, the image-based EIT achieves 0.710 success rate vs. SMORL with perfect ground-truth state at 0.716 — nearly matching it despite operating from pixels. On Ordered-Push, image-based EIT significantly exceeds state-based SMORL (Fig. 2d). This is a non-trivial demonstration that interaction modeling can compensate for imperfect perceptual input.

3. **Compositional generalization from 3 to 6 cubes with quantitative evidence.** The paper shows an approximately linear decay in average return as the number of cubes increases from 1 to 6 for an agent trained on 3 cubes (Fig. 5, right), with quantitative metrics over 400 episodes per seed. This provides credible empirical support for the method's generalization capability.

4. **Multi-view processing without explicit entity alignment.** The EIT architecture processes particles from multiple viewpoints without requiring alignment between particles across views or between state and goal particles. This is a clean and practical design advantage over methods that need explicit correspondence matching.

## Weaknesses

### Major

1. **Chamfer reward — claimed as a contribution — has zero quantitative evaluation.** The paper states (line 67): "We additionally propose a novel image-based reward... it enables learning entirely from pixels." The experiment outline (lines 183–186) promises "in the third part we evaluate our method using the Chamfer reward." This third part is entirely absent from the main paper. The only mention of results is in the limitations (line 303): "Our results with Chamfer rewards show worse performance than with ground truth reward" — but no figures, tables, or summary statistics are provided. A claimed contribution with no supporting evidence is a significant omission.

2. **Cube Sorting generalization claim is purely qualitative.** The paper describes an agent trained on 3 cubes generalizing to sort 12 cubes by color (lines 282–293), calling the results "exceptional." Yet only rollout images are presented (Fig. 6). No success rate, failure analysis, or any quantitative metric is reported. For a generalization claim of this magnitude, qualitative images alone are insufficient to establish reliability.

### Minor

3. **Theoretical result (Theorem 1) is substantially weaker than presented.** Assumption 1 essentially assumes the optimal Q-function already takes the form of a self-attention function with attention weights α* and value function v*. The theorem then proves that approximating such a function on ≤M objects yields error that grows at most linearly in k on M+k objects. The assumption itself does all the work — it says nothing about whether real manipulation tasks have optimal Q-functions of this form. The bound 3ε + ((3(M+k)+2)/(1-γ))·δ is also very weak for γ close to 1. The paper frames this as providing "a sound basis" (line 27) for the architecture, which overstates its contribution. The empirical results stand on their own; removing or honestly reframing this theorem would not harm the paper.

4. **Limited baseline set for a state-of-the-art claim.** The paper systematically compares against only SMORL and an unstructured VAE baseline. Several other object-centric pixel-based RL methods are cited in related work (COBRA, STOVE, NCS, FOCUS, DAFT-RL, OCRL) but not compared. While some of these are model-based (and the paper scopes itself as model-free), the absence of comparison against at least one modern model-free slot-based method (e.g., OCRL) limits calibration of the method's relative merit.

5. **Push-2T results are preliminary and lack baselines.** The Push-2T experiment (line 250) is labeled "preliminary" and presented without any comparison baseline. The evidence is a rollout visualization and a distribution of angle differences. This is at best a demonstration, not an evaluation.

### Trivial

None.

## Nice-to-Haves

- Quantitative evaluation of the Chamfer reward (even if worse than GT reward) would complete the paper's stated experiment plan and honestly calibrate expectations.
- Success rates and episode-level statistics for the Cube Sorting experiment would turn an impressive-looking demo into a substantiated result.
- A single-vs-multi-view ablation (mentioned as "crucial" for sample efficiency but not empirically supported in the main text).
- Broader baseline comparisons against at least one slot-based pixel method (e.g., OCRL).

## Removed Points

These points were surfaced by reviewers but removed after verification against the paper:

- **Missing ablations of architectural choices (SA→CA→SA→AA sequence, single vs multi-view, DLP vs other OCRs, richer OCR vs simpler MLP):** The paper references an ablation study in the appendix (line 94: "see ablation study in~\ref{apndx:ablation}"). The appendix is stripped by the parser, so whether these ablations exist cannot be verified from the available text. Per the removal rules, weaknesses about missing appendix content are removed.

- **"No statistical significance testing":** Reporting means and standard deviations across 3 seeds is the standard practice in this sub-field. This criticism does not reflect a meaningful standard violation.

- **"Hyperparameter sensitivity not discussed":** A generic point that applies to most RL papers and does not specifically threaten this paper's claims.

- **"No comparison with COBRA, STOVE, NCS, FOCUS, DAFT-RL, OCRL":** The paper explicitly scopes itself as model-free (line 49: "our method is trained in a model-free setting"), and most of these cited methods are model-based. The one comparable model-free slot-based method (OCRL) would be a useful addition, but the criticism as framed is overbroad scope creep.

- **Theoretical section should be "removed entirely":** The theorem is weak but not vacuous; it states a formal condition under which self-attention Q-functions admit compositional generalization. The overclaiming is noted in Weakness #3; removal is unnecessary.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between what the paper claims (Chamfer reward as contribution, Cube Sorting as exceptional generalization) and what is actually evidenced. These are omissions by the authors, not novel insights from the reviewers.

## Suggestions

1. **Add the missing Chamfer reward evaluation.** Even if results are poorer than GT reward, this is important information. Show success rate vs. timesteps for at least one environment (e.g., 3-Cubes) with Chamfer reward, compared against GT reward as an upper bound.

2. **Quantify the Cube Sorting experiment.** Report success rate over multiple random seeds and goal configurations. If the agent truly achieves non-trivial sorting with 12 cubes (4 per color), this would be a genuinely strong result worth rigorous documentation.

3. **Reframe or replace the theoretical section.** Either acknowledge the limited scope of the theorem explicitly (the assumption is that Q* is already a self-attention function), or replace it with a more meaningful analysis (e.g., a bound that does not assume the optimal Q-function's structure).

4. **Add at least one additional pixel-based baseline.** OCRL (model-free, slot-based) would be the most informative comparison to establish whether the observed improvements come from the EIT architecture or from the DLP representation itself.

## Score and Decision

The paper has a solid core: the EIT architecture convincingly outperforms SMORL on interaction-heavy manipulation tasks, the main quantitative experiments are well-designed, and the compositional generalization results on N-Cubes (3→6) are credible. However, two significant gaps prevent full acceptance: the Chamfer reward — explicitly listed as a contribution — has zero experimental validation anywhere in the paper, and the Cube Sorting generalization claim (from the abstract: "generalize to similar tasks with over 10 objects") rests on purely qualitative rollout images. These are not cosmetic issues; they are central claims that are not substantiated.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>