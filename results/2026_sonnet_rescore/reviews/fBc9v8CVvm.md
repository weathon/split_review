## Summary

TWINFLOW proposes a training framework for 1-step/few-step generative models by extending the flow-matching time interval from [0,1] to [-1,1], creating "twin trajectories" where the positive branch maps noise to real data and the negative branch maps noise to model-generated "fake" data. A velocity-matching (rectification) loss minimizes the KL divergence between the fake and real trajectory distributions, internalizing an adversarial signal without external GAN discriminators or frozen teacher models. The flagship result is full-parameter training of Qwen-Image-20B (where competing methods OOM) to achieve GenEval 0.86/DPG-Bench 86.52 at 1-NFE, matching the original 100-NFE performance.

---

## Strengths

- **Memory efficiency at 20B scale verified in Fig. 2b:** DMD2 and SANA-Sprint both exceed 80 GB at batch size 1, while TWINFLOW runs Qwen-Image-20B at batch size 24 in 76 GB. This is not a cherry-picked claim — it follows directly from needing zero auxiliary model copies.

- **Leading 1-NFE benchmark performance across architectures:** Table 4 shows TWINFLOW-0.6B achieves GenEval 0.83 at 1-NFE, ahead of SANA-Sprint-0.6B (0.72), RCGM-0.6B (0.80), and all LCM/PCM/DMD variants. Table 2 shows Qwen-Image-TWINFLOW at 1-NFE (GenEval 0.86) nearly matches the 100-NFE baseline (0.87), a concrete and measurable 100× compute reduction.

- **Genuine scalability result:** Table 3 demonstrates full-parameter TWINFLOW training on Qwen-Image-20B achieving GenEval 0.89/0.90 (1/2-NFE with longer training), outperforming every compared baseline on the same architecture. Competing approaches (VSD, DMD, SiD in raw form) are OOM, and the JVP-requiring methods (sCM, MeanFlow) yield substantially lower scores even with finite-difference approximation.

- **Ablation across three distinct architectures (Fig. 4b):** The contribution of $\mathcal{L}_{\text{TwinFlow}}$ is validated on OpenUni, SANA, and Qwen-Image independently, with the largest gain on Qwen-Image (DPG-Bench: 59.50 → 86.52 at 1-NFE). This cross-architecture consistency is meaningful evidence for the method's generality.

---

## Weaknesses

### Fatal
None.

### Major

- **JVP approximation handicaps sCM and MeanFlow in Table 3 without adequate justification.** The paper notes "For sCM and MeanFlow, the JVP is approximated via finite difference" but does not explain why exact JVP was not computed. sCM and MeanFlow's performance advantage partially rests on exact JVP computation; their numbers in Table 3 (sCM: GenEval 0.55–0.64; MeanFlow: 0.49–0.57) are substantially below TWINFLOW (0.85–0.86), but an unknown fraction of that gap is attributable to approximation degradation rather than the methods themselves. The paper's implicit argument — that TWINFLOW is preferable precisely because it avoids JVP computation altogether — is reasonable, but this framing should be made explicit. The current presentation implies a methodological head-to-head when it is partly a comparison of methods under their feasible operating conditions.

- **Ablation does not isolate $\mathcal{L}_{\text{adv}}$ and $\mathcal{L}_{\text{rectify}}$ individually.** Fig. 4b ablates $\mathcal{L}_{\text{TwinFlow}} = \mathcal{L}_{\text{adv}} + \mathcal{L}_{\text{rectify}}$ as a unit (on vs. off) but does not test each loss individually. Whether the core gain comes from the fake-trajectory learning ($\mathcal{L}_{\text{adv}}$, which is the claimed "self-adversarial" mechanism) or from the velocity rectification ($\mathcal{L}_{\text{rectify}}$, which resembles flow-straightening regularization) is unknown. If the rectification loss does most of the work, the method is better understood as self-distilled flow straightening rather than an adversarial mechanism. This matters for interpreting the contribution's novelty.

### Minor

- **"Self-adversarial" framing is imprecise.** The paper describes in Sec. 3.1 that the objective is "discriminator-free" and achieves an "internal self-adversarial signal." Inspecting the mechanism: the same network processes both positive-time (real) and negative-time (fake) inputs; there is no min-max game or generator-discriminator competition. The method is more accurately described as self-supervised velocity consistency or flow-straightening with a self-generated target. The "adversarial" terminology is not wrong — there is an implicit competition between real and fake velocity fields — but it overstates the resemblance to GAN-style training and repeatedly contrasts TWINFLOW against GAN methods (DMD, SANA-Sprint) in a way that may mislead readers. A more precise framing would reduce this gap.

- **Mode collapse claim for Qwen-Image-Lightning (Sec. 4.2) is asserted with only visual evidence.** The paper states Qwen-Image-Lightning "suffers from severe mode collapse: when given the same prompt but different noise inputs, the generated images remain nearly identical," pointing to App. E.1 for visual comparisons. No diversity metric (e.g., LPIPS variance across seeds) is reported. The mode collapse claim, if true, is an important empirical finding that strengthens TWINFLOW's narrative; it deserves a quantitative metric rather than a visual demonstration alone.

- **RCGM's 1-NFE collapse on Qwen-Image reflects a deployment challenge, not RCGM's ceiling.** RCGM achieves 0.80 on SANA-0.6B (Table 4) at 1-NFE but collapses to 0.52 on Qwen-Image-20B (Table 2). The paper presents the Qwen-Image result as a methodological comparison, but the failure is likely architecture-specific. TWINFLOW's win of 0.86 vs. 0.52 is real and practically important, but the paper should clarify that this reflects RCGM's difficulty on this architecture rather than its inherent limitations as a method.

- **Circular dependency in the real score estimate (Sec. 3.2).** The KL gradient derivation uses $\mathbf{F}_\theta(\mathbf{x}_t, t)$ as the real score estimate (Eq. 5–6), but this is the same model being optimized. DMD avoids this by using a separate fixed pretrained model for the real score. The paper does not discuss whether this circular dependency introduces training instability or bias — particularly relevant given that the paper's motivation is partly to avoid GAN training instability.

### Trivial
None that are not formatting artifacts.

---

## Nice-to-Haves

- **Perceptual quality metrics (FID or equivalent):** GenEval, DPG-Bench, and WISE all primarily measure prompt-following and compositional fidelity. The abstract claims "minor quality degradation" vs. 100-NFE models, but perceptual quality or image fidelity is not directly evaluated. Even on SANA-0.6B, a FID score would strengthen this claim.

- **Explicit justification that JVP infeasibility at 20B scale is why finite differences were used for sCM/MeanFlow.** If the argument is that TWINFLOW's advantage is precisely that it is JVP-free and therefore scales where JVP-requiring methods cannot, stating this explicitly in the Table 3 discussion converts a potential fairness concern into a feature demonstration.

- **Lambda ($\lambda$) sensitivity across architectures.** The ablation in Fig. 4a is conducted on Qwen-Image; it is unclear whether $\lambda = 1/3$ is robust for SANA-0.6B/1.6B. A brief confirmation or discussion would strengthen the hyperparameter simplicity claim.

- **Training stability curves.** The paper claims a stability advantage over GAN-based methods but demonstrates it only via memory footprint. Training loss curves or output diversity over training on smaller models would make the stability claim concrete.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"0 frozen teacher models" claim is misleading (stop-gradient as frozen copy):** The harsh critic argues that using `sg(·)` in Eq. 9 is "functionally a frozen copy of the current network at each iteration." This conflates two different mechanisms. The stop-gradient operator is a standard technique in self-supervised learning (BYOL, SimSiam, consistency models) that prevents gradient flow through a specific computation; it does not require storing a separate model checkpoint, loading an EMA teacher, or maintaining a distinct model state. A "frozen teacher model" in the sense of Table 1 refers to a separately initialized or stored model that is not being updated (e.g., the teacher in DDIM distillation). The sg() in TWINFLOW is simply a gradient-stopping device within the same forward pass. The Table 1 claim is substantively correct. Removing this criticism as a misread.

- **DPG-Bench gap attributed to proprietary data (Sec. 4.3):** The critic notes the paper asserts "the gap is primarily data-driven" without demonstration. However, this is the natural explanation for a gap when training data volume and provenance differ — it is a reasonable working hypothesis stated modestly. Not a verifiable flaw; keeping as a note but not a scored weakness.

- **Requesting missing related works:** Not applicable — per rules, missing related work is not raised.

---

## Novel Insights

The paper's most genuinely novel observation is that time-symmetry (extending t ∈ [0,1] to t ∈ [-1,1]) provides a principled way to incorporate a distribution-matching signal entirely within the pretrained model's parameterization. Prior work on distribution matching (DMD, SiD) achieves the same conceptual goal — aligning generated and real distributions at every noise level — but requires separate model components. TWINFLOW shows that if the same network can model velocity fields for both real-data trajectories (positive time) and fake-data trajectories (negative time), the divergence between these velocity fields is a tractable proxy for distribution alignment, and minimizing it is achievable with ordinary gradient descent on a single model. The practical payoff — training at 20B parameters where architecturally heavier methods OOM — validates that the simplicity is not just elegant but necessary at scale.

---

## Suggestions

1. **Report sCM/MeanFlow performance with exact JVP on SANA-0.6B or smaller model.** Even if exact JVP is infeasible at 20B, a calibration experiment at smaller scale would let readers understand how much of the Table 3 gap is due to approximation vs. fundamental method differences.

2. **Add a per-component ablation: $\mathcal{L}_{\text{adv}}$ alone, $\mathcal{L}_{\text{rectify}}$ alone, and both combined.** This directly addresses the novelty question and would likely be the most cited result from the ablation section.

3. **Quantify diversity for the Qwen-Image-Lightning mode collapse claim** (e.g., mean pairwise LPIPS over multiple seeds per prompt). The claim is central to the narrative and deserves quantitative backing.

4. **Explicitly reframe the JVP-free comparison in Table 3** as a demonstration that sCM/MeanFlow are not deployable at 20B with exact JVP, and finite differences are what makes them feasible — thereby showing TWINFLOW excels in the actual deployment-feasible setting. This converts a fairness concern into a clearer argument.

5. **Clarify the circular dependency in the real-score estimate** in Sec. 3.2. A brief note on whether training dynamics are observed to be stable (e.g., gradient norms don't explode) would address this concern concisely.

---

## Score and Decision

**Originality:** The time-symmetry trick for twin trajectories is novel and cleanly motivated. The method draws on DMD's KL-gradient insight and flow-matching, but the integration is original. **3/5**

**Importance of research question:** Enabling 1-step generation on 20B-scale models is highly practical. The memory bottleneck they solve is real and limits the broader adoption of fast generation on frontier models. **4/5**

**Claims well-supported:** Core claims (1-NFE performance, memory efficiency, scalability) are well-supported by multiple tables and architectures. The JVP approximation issue slightly weakens the Table 3 comparative claim, and the mode collapse claim for Lightning needs quantification. **4/5**

**Soundness of experiments:** Multi-architecture evaluation is thorough. The ablation of the combined loss is meaningful. Missing component-level ablation is the notable gap. **4/5**

**Clarity:** Well-written with a clear derivation. The "self-adversarial" framing is slightly misleading but the mechanism is formally defined. **4/5**

**Value to the research community:** High — memory-efficient, no-auxiliary-model 1-step training is directly usable by practitioners working on large generative models. **4/5**

The paper makes a genuine, practically significant contribution. The flagship result — matching 100-NFE performance at 1-NFE on a 20B model, where prior methods OOM or collapse — is clean and compelling. The identified weaknesses (JVP comparison, component ablation) are real but do not undermine the core claim and are addressable in revision.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>