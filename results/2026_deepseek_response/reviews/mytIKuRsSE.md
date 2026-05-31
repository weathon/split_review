## Summary

This paper identifies and formalizes Dual-level Noisy Correspondence (DNC) — noise in both intra-entity (entity-attribute) and inter-graph (entity-entity and attribute-attribute) correspondences — for Multi-Modal Entity Alignment (MMEA). The authors propose RULE, a framework that estimates correspondence reliability via uncertainty (Dempster-Shafer/Dirichlet) and consensus principles, uses robust loss functions and weighted fusion to mitigate noise during training, and incorporates a test-time MLLM-based reasoning module. Experiments on five benchmarks show consistent improvements over seven MMEA baselines across multiple noise levels.

## Strengths

1. **Novel problem framing with empirical backing**: DNC is a practically relevant but under-explored issue in MMEA. The paper provides evidence that real-world benchmarks contain substantial noisy correspondences and demonstrates that existing methods degrade significantly under such noise (Fig. 1b), establishing clear motivation.

2. **Two-fold reliability estimation that empirically works**: The combination of uncertainty (Dirichlet-based) and consensus (similarity-based) principles is conceptually sound. Figure 4 empirically validates that the three subsets (S_U, S_I, S_C) form distinct clusters, supporting the pair-division design. The reliability distributions (Fig. 3b) show clean vs. noisy pairs are separable.

3. **Dually Robust Loss ablation evidence**: Table 3 shows that removing DRL drops H@1 from 58.2 to 31.6 (Non-name, 50% DNC) — a 26.6 point gap. This demonstrates that the tailored loss functions, not just the MLLM module, drive the core performance.

4. **Comprehensive evaluation**: Compared against seven SOTA MMEA methods on five benchmarks under three noise levels (inherent, 20%, 50%) with two protocols (Non-name and All-attributes). RULE achieves the highest average H@1 in every setting.

## Weaknesses

### Fatal
None.

### Major

1. **Test-time MLLM confounds the main comparison**: RULE uses Qwen2.5-VL-72B-Instruct at inference time (TTR module), while none of the seven baselines use any MLLM. Although the ablation shows TTR contributes only 1.7 H@1 (56.5 → 58.2), the main comparison tables include TTR for RULE while baselines have no equivalent. This asymmetry means the headline results in Tables 1-2 partially reflect the MLLM's reasoning capability, not purely the proposed training-time method. The paper should present non-TTR results alongside baselines in the main tables, or apply the same MLLM re-ranker to all baselines.

2. **Circular dependency in consensus estimation is unexamined**: The greedy attribute selection (Eq. 6-7) estimates correspondence labels using cross-graph attribute similarities computed from the *same encoders being trained*. This creates a self-training/bootstrap loop that the paper does not analyze or theoretically characterize. The paper provides no evidence — e.g., precision/recall of the identified clean vs. noisy pairs, or analysis under random initialization — that this bootstrap works rather than amplifying initial biases. This is a genuine methodological gap even if the empirical results suggest it works in practice.

### Minor

1. **Noise types conflated in aggregate experiments**: The 20%/50% DNC settings simultaneously inject entity-entity, entity-attribute, and attribute-attribute noise. This makes it impossible to determine which noise type drives the method's gains or whether the full "dual-level" machinery is necessary. Isolated experiments (intra-entity noise only, inter-graph noise only, both) would directly validate the dual-level framing.

2. **TTR module is underspecified**: Equation 16 defines ŝ_i^m = Softmax(⊕_{j∈T_i^m}(CoT[x_i^m, x̃_j^m, s_i^m])) but does not specify what CoT[·] returns (a scalar? a vector?), provides no prompt template, no example outputs, and no reasoning quality analysis. This hinders reproducibility and assessment of what the MLLM contributes.

3. **No accuracy analysis of consensus estimation**: The paper does not report precision or recall of the greedy strategy's identification of clean vs. noisy pairs. Since the pair-division thresholds (Eq. 8) depend entirely on this estimation, understanding its accuracy is critical to evaluating the method's soundness.

4. **Missing comparison with adapted noisy-learning baselines**: The seven baselines are standard MMEA methods, none designed for noise. Adapting simpler robust strategies (label smoothing, temperature scaling, loss clipping, or DECL-style methods) to MMEA would better isolate whether the specific uncertainty-consensus-Dirichlet machinery is necessary.

5. **Hyperparameter β sensitivity**: The self-adaptive thresholds that divide all pairs into S_U, S_I, S_C depend on β=0.3 (fixed for all experiments). Only one sensitivity analysis is deferred to Appendix G.10. Since the pair division quality directly controls the robust loss behavior, the main text should discuss sensitivity to this parameter.

### Trivial

1. "HMC Ratio" on the y-axis of Fig. 3(a) is not defined in the main text.
2. The numerical values behind the Fig. 1(b) bar charts are not reported in the main text.

## Nice-to-Haves

- **Statistical significance**: Standard deviations over multiple random seeds would strengthen confidence, especially for the noise injection experiments.
- **Runtime/cost analysis of the TTR module**: A 72B MLLM at inference time on datasets with 15k+ entities is expensive. Reporting average inference time per entity would contextualize the practicality.
- **Compare against noisy-label learning methods**: Adapting DivideMix, JoCoR, or Noise Contrastive Estimation to the MMEA setting would strengthen the comparison.

## Removed Points

*(Points flagged by reviewers but removed from the main review with justification)*

- **"Dual-level framing conflates two different problems"** (Harsh Critic, para 1): The paper explicitly treats intra-entity noise with DRF (weighted fusion) and inter-graph noise with DRL (uncertainty-consensus machinery). Acknowledging they operate at different granularities is not a flaw — it's a correct characterization. The critic's claim that prior work on "missing modalities" already addresses this conflates missing data with noisy correspondences. **Removed.**
- **"The method's advantage shrinks dramatically on All-attributes"** (Harsh Critic): This is expected behavior — names are universally the strongest signal in MMEA. The Non-name protocol is the harder and more revealing setting. **Removed.**
- **"Consensus definition is misleading"** (Harsh Critic): Terminology preference, not a substantive weakness. **Removed.**
- **"No theoretical grounding for Dirichlet framework necessity"** (Harsh Critic): The paper explains *why* uncertainty alone is insufficient (Theorem 1). The reviewer's preference for simpler alternatives is fair as a question but not a demonstrated weakness. **Removed.**
- **"Over 50% noise statistic unverifiable"** (Harsh Critic): The paper references Appendix B; removed appendix content should not be treated as a flaw. **Removed.**
- **"w/o DRL baseline is particularly weak"** (Harsh Critic): The w/o DRL baseline uses standard MSE loss without any noise handling — its 31.6 H@1 is expected under 50% noise. This is not an implementation artifact. **Removed.**
- **"Regularization loss closed form not given"** (Harsh Critic): The KL divergence between Dirichlet distributions has a standard closed form involving gamma/digamma functions, which the paper references. **Removed.**
- **Various presentation nitpicks** (parser artifacts): **Removed per hard rules.**
- **Strength: "TTR module's effectiveness"** (Strength Finder): Partially conflicts with the TTR confound weakness. Kept as a separate claim but the weakness overrides.
- **Strength: "Comprehensive and fair evaluation"** (Strength Finder): "Fair" is undermined by the TTR asymmetry. Changed to "comprehensive evaluation."

## Novel Insights

None beyond the paper's own contributions. The reviews corroborate the paper's framing and highlight specific methodological gaps (circular dependency, noise-type isolation) that the authors should address but do not reveal fundamentally new interpretations of the work.

## Suggestions

1. Report results **without the TTR module** in the main comparison tables, or equivalently apply the same MLLM re-ranker to all baselines, to isolate the contribution of the training-time method.
2. Add ablation experiments **isolating each noise type** (intra-entity only, inter-graph only, both) to validate the dual-level claim directly.
3. Analyze the accuracy of the greedy consensus estimation: report precision/recall of identified clean vs. noisy pairs, and test with randomly initialized encoders to characterize the bootstrap behavior.
4. Provide the prompt template and example outputs for the TTR CoT reasoning, and clarify what Eq. 16 returns.

---

## Score and Decision

**Calibration anchors** (from human review corpus):

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `a4O528mek9.md` | 3.00 | 1 (low) | Fundamentally flawed paper; RULE is substantially stronger |
| `YrxhSkfHh0.md` | 3.33 | 1 (low) | Methodologically weak; RULE is substantially stronger |
| `rwdeKOdAwY.md` | 3.00 | 1 (low) | Limited contribution; RULE is substantially stronger |
| `AAZ3vwyQ4X.md` | 2.50 | 1 (low) | Very weak; RULE is much stronger |
| `z3dfuRcGAK.md` | 6.67 | 1 (mid) | Strong theoretical grounding for entity alignment; RULE comparable but less theoretical depth |
| `NNUiUwQWx6.md` | 5.75 | 1 (mid) | Neuro-symbolic EA with complexity concerns; RULE more comprehensive eval |
| `ue1Tt3h1VC.md` | 6.60 | 1 (mid) | Well-executed MMKG framework; RULE comparable |
| `QQYpgReSRk.md` | 6.25 | 1 (mid) | Noisy entity annotation; RULE addresses different problem |
| `uAFHCZRmXk.md` | 8.00 | 1 (high) | Strong analysis paper; RULE is less exceptional |
| `TPZRq4FALB.md` | 8.00 | 1 (high) | Strong TTA method; RULE is less exceptional |
| `z3dfuRcGAK.md` | 6.67 | 2 (narrow) | RULE ≈ GEEA, comparable quality |
| `NNUiUwQWx6.md` | 5.75 | 2 (narrow) | RULE > NeuSymEA (more comprehensive eval) |
| `CbfsKHiWEn.md` | 6.20 | 2 (narrow) | Robust DPO; different domain, comparable rigor |
| `Pz9zFea4MQ.md` | 6.50 | 2 (narrow) | Robust learning; different domain |
| `DKgAFfCs5F.md` | 6.00 | 2 (narrow) | Uncertainty-aware fusion; RULE ≈ Cocoon |
| `ftGnpZrW7P.md` | 7.00 | 2 (narrow) | Strong multimodal alignment paper; RULE slightly below |
| `jJCeMiwHdH.md` | 7.00 | 2 (narrow) | KG-bridged multimodal; different task |

**Bracket (Round 1):** [5.75, 7.0]

**Narrowing (Round 2):** The most directly analogous anchors are GEEA (6.67), MoMoK (6.60), NeuSymEA (5.75), and Cocoon (6.00). RULE is clearly stronger than NeuSymEA (5.75) — more comprehensive evaluation and clearer problem framing. RULE is comparable to GEEA (6.67) and MoMoK (6.60) in scope and rigor, though it has less theoretical depth than GEEA. The TTR confound and the unexamined circular dependency in consensus estimation prevent it from reaching the 6.5+ range. RULE is slightly above Cocoon (6.00), a solid accepted paper with minor concerns.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>