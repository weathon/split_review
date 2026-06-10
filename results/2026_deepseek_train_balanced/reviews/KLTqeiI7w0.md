## Summary

AnyBimanual proposes a plug-and-play framework to transfer pre-trained unimanual manipulation policies to multi-task bimanual manipulation with few bimanual demonstrations. It introduces two modules: (1) a *skill manager* that composes unimanual skill primitives (initialized from the unimanual policy's task embeddings) via sparse linear combination with a task-oriented compensation term, and (2) a *visual aligner* that learns mutually-exclusive spatial soft masks to decompose the bimanual voxel observation into per-arm views resembling the unimanual pretraining distribution. Experiments on 12 RLBench2 tasks and 9 real-world tasks show improvements over several baselines.

## Strengths

- **Ablation cleanly validates both components.** Table 2 (Section 4.3) decomposes the total gain: the skill manager alone contributes +4.67%, the visual aligner alone +4.34%, and the combination reaches +12.67% over direct finetuning. This is concrete evidence that both modules carry independent weight and are not cosmetic additions.

- **Model-agnostic design demonstrated across multiple backbones.** The method is evaluated on PerAct-LF, RVT-LF, and standalone PerAct (Table 1), and improves each one (relative boosts of 25.87%, 116.65%, and +12.67pp respectively). This shows the framework does not depend on a single architecture.

- **Works with limited data (20 demos per task).** At 1/5 the standard data budget, the method still outperforms baselines by 8.00% (Table 1, columns labeled "20"), directly supporting the paper's central motivation that bimanual data is expensive.

- **Real-world validation on 9 diverse tasks.** A single multi-task model achieves 84.62% average success across 65 real-world episodes (Table 4, Section 4.6), including tasks requiring synchronous/asynchronous coordination, long-horizon execution, and object variation.

## Weaknesses

### Major

- **No real-world baselines are reported.** Table 4 (Section 4.6) presents AnyBimanual's real-world performance alone—84.62% across 9 tasks—without any comparison to PerAct-LF, PerAct², direct finetuning, or any other method on the same hardware and tasks. The paper's central claim is that AnyBimanual *outperforms* existing methods; the real-world section provides no evidence for this comparative claim. It only shows that the method *works* in real-world settings, which is not the same as demonstrating superiority.

- **No variance or confidence intervals on any experimental result.** All simulation results (Table 1) are point estimates from 25 episodes per task. For a binary metric at ~20% success rate, the standard error is approximately 8 percentage points—comparable to or larger than many reported differences between methods. Without variance estimates, multiple runs, or statistical tests, it is impossible to determine which of the reported improvements are reliable vs. noise. The paper's strongest claims rest on this unquantified evidence.

### Minor

- **The abstract's headline improvement number is imprecisely stated.** The abstract claims "a sizable 12.67% improvement in success rate over previous methods." This 12.67% is the gap between AnyBimanual (21.67%) and vanilla PerAct² (9.00%). However, Table 1 also reports "PerAct² + Pretraining" (14.67%), against which the improvement is 7.00%—roughly half the advertised number. Section 4.2 correctly attributes the 12.67% to PerAct² specifically, but the abstract's phrasing "over previous methods" is over-broad. The paper would be more transparent if it explicitly discussed both comparisons.

- **The "skill discovery" framing overstates what the method actually does.** The paper claims "automatic skill discovery in an unsupervised manner" (Section 3.2) and that the skill manager "discovers skill representations" from offline bimanual data. In practice, the skill primitives are initialized from the 18 task embeddings of the pre-trained PerAct policy (Section 4.5, line 353: "we use 18 task embeddings from PerAct as the initial skill set"), and the only learning is training a transformer to predict sparse linear combinations of these fixed embeddings plus a compensation term. The method learns *how to compose* pre-existing unimanual skill representations, not *which skills to discover* from bimanual data. This should be characterized more honestly.

- **Key architectural details of the skill manager are unspecified.** The skill manager is described as a "multi-model transformer" (line 140) that takes visual, language, and proprioception inputs and outputs weights and compensation terms for both arms. No further details are provided: number of layers, hidden dimensions, cross-attention structure, or how the three input modalities are fused. This makes the method difficult to reproduce or compare against.

- **No sensitivity analysis on the number of skill primitives K.** K=18 is chosen (mentioned only in Section 4.5) with no ablation for different values (e.g., K=10, K=30). The choice is potentially consequential—too few primitives may underfit, too many may harm sparsity—and the paper provides no evidence that performance is robust to this hyperparameter.

- **Absolute success rates are low (~21.67% on simulation).** While the paper acknowledges this as a property of multi-task bimanual training, the absolute numbers are weak, and many individual tasks remain below 10% (e.g., 4% on sweep_to_dustpan and take_out_tray with 100 demos). The claim of "state-of-the-art" rests entirely on relative gains against an already-low baseline.

### Trivial

- The "JS divergence" in Eq. 4 is technically the symmetrized KL divergence (average of KL(left||right) and KL(right||left)), not the standard JS divergence (which uses the midpoint distribution). This is a minor mathematical imprecision that does not affect the method.

- Key hyperparameters (K, λ_ε, λ_skill, λ_voxel) are not given numerical values in the paper.

## Nice-to-Haves

- The L₂,₁ regularization on the compensation term ε is described as a "denoising term" (line 150) but the paper does not justify why column-wise sparsity is the right structural prior for embodiment-specific knowledge. A brief motivation would help.
- Testing on a fundamentally different backbone architecture (e.g., a diffusion policy like 3D-DiffuserActor or Octo) would strengthen the "plug-and-play" claim, which is currently demonstrated only on transformer-based voxel/multi-view methods.
- A failure analysis for the simulation tasks with <10% success (e.g., sweep_to_dustpan, put_in_fridge) would sharpen the contribution and guide future work.

## Removed Points

These points were flagged during review synthesis but removed for the reasons stated below. Treat them with caution.

1. **"PerAct² + Pretraining is never explained."** — The paper explicitly states at line 294: "To exclude the influence of model parameters, we also implement a counterpart that directly combines two pre-trained PerAct policies." This explanation is brief but present and adequate. **Reason for removal: factually wrong.**

2. **"The 12.67% improvement is framed against the weakest baseline."** — PerAct² (9.0%) is actually the strongest of the vanilla baselines, outperforming PerAct-LF (7.0%) and RVT-LF (4.0%). The critic's assertion that this is the "weakest" is incorrect. **Reason for removal: factually wrong.**

3. **"Pure formatting/style nitpicks / typos / grammar issues"** — Various alleged formatting criticisms were considered. The paper's formatting is standard; any artifacts are from PDF extraction. **Reason for removal: parser artifacts, not author errors.**

4. **Strength Finder claim: "Empirical superiority over prior SOTA across both simulation and real-world"** (real-world part). — The real-world section contains no baselines, so "superiority" in real-world is unsubstantiated. The simulation claim is fine, but the real-world portion is removed from the strength claim. **Reason for removal: unsupported by evidence.**

5. **Strength Finder claim: "Principled sparse-representation learning"** — While the L₁+L₂,₁ regularization is standard and reasonable, calling it "principled" as a distinctive strength is generic. **Reason for removal: generic/superficial praise.**

## Novel Insights

None beyond the paper's own contributions. The reviews surface two important tensions: (1) the method's strongest claim (superiority) is evaluated least rigorously where it matters most (real-world, no baselines); and (2) the "discovery" framing masks a more modest but still interesting contribution—learning to compose pre-existing unimanual skill representations for bimanual tasks, which is a form of skill *scheduling* rather than skill *discovery*.

## Suggestions

1. **Add real-world baselines.** The single most impactful improvement would be to run PerAct² or PerAct-LF on the same 9 real-world tasks and report side-by-side comparisons. Without this, the central comparative claim is untested in the practically relevant setting.

2. **Report variance or confidence intervals.** Run each simulation experiment over multiple seeds (at least 3) and report standard deviations, or compute binomial confidence intervals for the per-task success rates. This is essential for judging which differences are meaningful given 25-episode evaluations.

3. **Clarify the abstract's improvement claim.** Specify that the 12.67% is vs. PerAct², and explicitly discuss the 7.0% improvement over the "PerAct² + Pretraining" baseline as the more controlled comparison.

4. **Provide architecture details for the skill manager.** Add a short paragraph describing the transformer layers, hidden dimensions, input fusion mechanism, and output heads.

5. **Report hyperparameter values** (K, λ_ε, λ_skill, λ_voxel) and include a sensitivity analysis for K.

## Score and Decision

The paper addresses a well-motivated problem and proposes a structurally plausible solution with clean ablations. However, the evidence is not commensurate with the strength of the claims. The absence of real-world baselines and variance reporting are significant gaps that prevent the paper from meeting the standard required for acceptance at a top venue. The method is promising and the core ideas are sound, but the experimental validation has critical holes.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>