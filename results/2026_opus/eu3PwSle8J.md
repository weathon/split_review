Now let me check for calibration anchors.I have enough calibration data. The paper sits next to the ISE paper (the very baseline it improves on, scored 6.0) and the PFT paper (similar architectural defense, scored 4.25). AIR has more rigorous gradient-attack evaluation than either, but shares the "missing isolating ablation" weakness as ISE. My bracket is 5.0–6.0. Writing the final review now.

## Summary
The paper introduces Augmented Intermediate Representations (AIR), a defense against indirect prompt-injection that injects Instruction Hierarchy (IH) signals at every decoder layer via per-layer trainable embedding tables indexed by privilege level, rather than only at the input layer as in Delimiters or ISE. Evaluated on Llama-3.2-3B, Qwen-2.5-7B, and Llama-3.1-8B with both SFT and DPO, AIR reports a 1.6×–9.2× reduction in ASR on gradient-based attacks (Momentum-GCG, Astra) against Delim/ISE, with <2% utility degradation on AlpacaFarm and the best utility–separation trade-off on SEP under DPO.

## Strengths
- **Large, consistent gradient-attack robustness gains.** Table 1 shows AIR achieves 1.6×–9.2× lower GCG ASR than the next-best defense across all three model sizes and both training regimes (e.g., 99.5% → 11.3% on Llama-3.1-8B SFT; 38% → 4.1% on Llama-3.2-3B SFT). Astra ASRs collapse to near-zero (0.1%, 0.9%, 1.0%) in several settings. These are concrete, large-magnitude wins on the headline metric.
- **Negligible parameter overhead.** Section 4 calculates 0.4M extra parameters (~0.005% increase) for Llama-3.1-8B, which is genuinely cheap relative to the robustness improvement.
- **Best utility–separation trade-off on SEP under DPO.** Figure 8 shows AIR-DPO Pareto-dominates Delim and ISE on the SEP benchmark for all three models, indicating the robustness gains transfer to a second, independently designed evaluation.
- **Controlled, apples-to-apples training pipeline.** All injection mechanisms (Delim, ISE, AIR) share the identical two-stage training procedure, datasets, optimizer, and epoch counts (§5.2), so observed differences are attributable to the architectural change rather than training confounds.

## Weaknesses

### Fatal
None.

### Major
- **Missing ablation isolating "per-layer injection" from "per-layer trainable parameters."** AIR conflates two changes: (a) making the IH signal available at every layer, and (b) using independently-trained embedding tables S_j per layer. The natural intermediate baselines (ISE-style segment embedding applied at every layer with shared/tied weights; AIR with tied S across layers) are absent. Without these, Table 1 supports the empirical claim "AIR > ISE/Delim" but does not test the paper's actual thesis ("inject IH at every layer is what matters"); the gains may stem largely from the added layer-conditional capacity rather than from the conceptual claim the paper makes. This is the most substantive scientific gap.
- **Asymmetric attack budget across training regimes.** §5.4 reports 50 GCG steps for SFT but 200 for DPO models, with no convergence sanity check that the SFT attack has plateaued. Several SFT loss curves in Fig. 7 appear still trending downward at the cutoff; the SFT robustness claim is more sensitive to this than the DPO one. A consistent (or per-model converged) budget would tighten the headline number.
- **Single fixed attack target weakens the generality claim.** All gradient-based and static robustness numbers use the literal target "hacked!" (§5.4), and ASR is measured by likelihood of that exact phrase. The 1.6×–9.2× number is therefore for one synthetic objective; the broader threat model in §1 (exfiltration, agentic hijacking) is not directly probed. Reporting GCG/Astra against a small set of varied targets would substantially strengthen the contribution.

### Minor
- **The cosine-similarity motivation (Fig. 3) is a correlate, not a mechanism.** All three methods show the same monotonic increase in privilege-token similarity with depth; AIR is only modestly damped (0.55 → 0.88 vs. ISE's 0.55 → 0.92). It is reasonable to use this as a suggestive observation, but the paper occasionally implies it mechanistically explains why AIR is robust — which a >10× ASR gap is unlikely to follow from such a modest similarity gap. The framing in §3.2/§1 could be softened to an empirical observation, or replaced/supplemented by a probe-based diagnostic (e.g., privilege-classification accuracy from layer-l hidden states, or layer-wise attention mass on high- vs. low-privilege tokens).
- **Single-seed numbers with no variance estimates over training runs.** Several Table 1 cells differ by <1 percentage point between methods on static attacks, and Astra ASR moves dramatically (e.g., 25.8 → 0.1) between adjacent configurations. The Fig. 7 shaded regions are over test instances, not training runs. Even a small number of seeded re-runs on the gradient-attack column would help readers calibrate which gaps are real.
- **AIR-aware attack not clearly evaluated.** Astra is cited as "architecture-aware" but the paper does not explicitly state whether the optimization backpropagates through the per-layer S_j additions or treats AIR as a black box. For a new architectural defense, the most informative attack is one that knows the defense.
- **SEP gap is small.** On SEP, AIR's separation scores are close to ISE under SFT (e.g., 3.1 vs. 3.1 on Llama-3.1-8B). The paper does not over-claim here, but readers should be aware the headline framing rests on the gradient-attack column.
- **Utility below the None baseline for AIR-SFT on some models** (Fig. 8, Qwen-2.5-7B, Llama-3.1-8B). The body acknowledges this; the abstract does not.

### Trivial
- The "Similarity to Positional Embeddings" analogy in §4 is rhetorical rather than structural — RoPE injects positional information into attention rotations, not as a residual addition to the hidden state, so the structural parallel is loose.

## Nice-to-Haves
- Report whether the learned per-layer S_j actually develop layer-distinct structure (e.g., pairwise similarity / norm-by-layer of the learned tables). If they collapse to near-identical vectors, the layer-specific design is redundant; if they are distinct, the choice is empirically justified.
- Run a probe-based diagnostic across layers (privilege classifier on hidden states, attention mass on different privilege segments) — these would either substantiate or replace the cosine-similarity motivation.
- Vary the adversarial target across a small set of objectives and report variance.
- Add the isolating ablation (tied-S AIR; ISE-applied-per-layer) — this is the single most informative experiment for the paper.

## Removed Points
These points are flagged to be removed — treat them with caution.

- **"AIR re-injects a privilege offset before each layer, mechanically lowering similarity by construction; Fig. 3 is decorative."** This is partially speculative — the figure does plot a meaningful quantity, and the paper does not over-claim mechanism in the formal contributions. I retained the substance as a Minor weakness (motivation is correlative, not mechanistic) but dropped the "decorative" framing.
- **"The empirical gains may be coming from a privilege-gating mechanism inside attention/FFN rather than from preserving an input signal."** This is exactly the kind of speculation the harsh-critic protocol asks to demote — it depends on information not in the paper. The constructive form (run the tied-S ablation) is already kept as a Major weakness.
- **"AIR-SFT utility falls below None baseline — abstract should mention it."** The body explicitly discusses this; calling it a deficiency of the abstract is a presentation nitpick, not a substantive weakness.
- Strength: "Empirical evidence of signal degradation in input-only methods (Fig. 3)" — Conflicts with the verified Minor weakness that the figure is a correlate rather than mechanistic evidence. Demoted/removed in favor of the weakness.
- Strength: "Consistent evaluation across diverse settings" — Real but generic; better captured implicitly by the headline-ASR strength.

## Novel Insights
None beyond the paper's own contributions. The core idea — distributing privilege-level signals across all decoder layers rather than only at the input — is the paper's contribution, and the empirical evidence supports that this is worth doing. No additional insight emerges from the reviews.

## Suggestions
- Run the **tied-S AIR ablation** (single shared S across layers) and **ISE-applied-per-layer** to isolate "where to inject" from "how many parameters." This is the single experiment that would most strengthen the paper's central thesis.
- Equalize the GCG budget across SFT and DPO (or show convergence), and report seed variance on the gradient-attack column.
- Run a small **target-diversification sweep** for GCG/Astra (several distinct adversarial instructions) to broaden the robustness claim beyond "hacked!".
- Either soften the "signal degradation" framing in §3.2 to an empirical observation, or replace Fig. 3 with a probe-based diagnostic that more directly tests the hypothesis (e.g., layerwise privilege-classification probe).
- State explicitly in §5.4 whether Astra/GCG optimization routes gradients through the per-layer S_j tables, and if not, run an AIR-aware adaptive attack.

---

**Axis evaluation.** *Originality:* moderate — a natural and well-motivated incremental extension of ISE/Delim. *Importance of the question:* high — indirect prompt injection is a central safety concern. *Whether the claims are well supported:* mixed — the empirical headline (1.6×–9.2× ASR reduction) is supported, but the mechanistic framing is not isolated by experiments. *Soundness of experiments:* solid setup, but missing the key ablation and an explicitly AIR-aware adaptive attack, and using one fixed adversarial target. *Clarity of writing:* clear, well-organized, easy to follow. *Value to the research community:* moderate — a useful, cheap architectural lever that practitioners can adopt; needs the disentangling ablation to be convincing about *why* it works.

## Score and Decision

**Anchors used:**

- `sjWG7B8dvt.md` — ISE paper (avg score **6.00**, Accept). Round 1 + Round 2. This is the immediate predecessor and a direct comparable. ISE introduced segment embeddings at the input layer; reviewers accepted at 6.0 despite "merely adds an embedding layer" novelty concerns, missing-ablation concerns (e.g., concatenation vs. addition, capacity ablation), and questions about evaluation. AIR is a strictly more rigorous evaluation (three models, two training regimes, both static and gradient-based attacks, two benchmarks) of a similar-grain architectural change, but shares the central methodological gap (no ablation isolating the conceptual change from the parameter increase). Roughly comparable contribution scale; AIR slightly better-evaluated.

- `l3bUmPn6u5.md` — PFT paper (avg score **4.25**, Reject). Round 1 + Round 2. Position-based prompt-injection defense. Rejected for narrow problem framing, weak attack diversity (no GCG), unclear comparison to baselines, and questionable real-world relevance. AIR is clearly stronger: it includes gradient-based attacks (GCG, Astra), compares against the right baselines (Delim, ISE), and frames the threat model in line with the standard community formulation. AIR is well above PFT.

- `kUH1yPMAn7.md` — Safety Layers (avg score **6.00**, Accept). Round 2. Analyzes which internal layers maintain safety; methodologically adjacent in spirit (layer-level mechanisms in alignment). Different problem but similar contribution flavor (architectural-mechanism insight + empirical validation). AIR is comparable on rigor and scope.

**Comparative placement.** AIR is broadly comparable to ISE (6.0) — same problem area, same kind of architectural delta, similar caliber of missing-ablation issue — but AIR has notably more rigorous gradient-attack evaluation (this is a real plus over ISE), offset by a weaker motivating analysis (cosine similarity figure) and the missing tied-S ablation. Net: very slightly below ISE in my judgment, because the central thesis ("layer-wise injection is the key") is not actually isolated, and because the single-target evaluation bounds the generality claim. Clearly well above PFT (4.25).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>