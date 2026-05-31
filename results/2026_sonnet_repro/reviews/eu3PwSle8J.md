Now let me run calibration searches to determine the appropriate score range.Now I have enough information to write the final consolidated review. Let me verify one specific claim about Figure 3 before proceeding.Now I have sufficient information to write the full review. Let me compile everything.

---

## Summary
This paper proposes Augmented Intermediate Representations (AIR), a defense against indirect prompt injection attacks on LLMs. Unlike prior methods (Delimiters, ISE) that inject Instruction Hierarchy (IH) signals only at the input layer, AIR injects trainable privilege-level embeddings into every decoder layer at negligible parameter cost (0.005% increase for Llama-3.1-8B). Evaluated across three model architectures (3B, 7B, 8B) and two training paradigms (SFT, DPO), AIR achieves 1.6×–9.2× lower attack success rate on gradient-based attacks compared to the next-best defense, with minimal utility degradation.

---

## Strengths

- **Principled, well-motivated design.** The paper anchors its design intuition in the analogy to positional embeddings: input-only sinusoidal/learnable PE → layer-wise RoPE (Section 4). Figure 3 directly measures cosine similarity of privilege-differentiated token representations across decoder layers in trained models for all three methods (Delim, ISE, AIR), showing that AIR achieves consistently lower inter-privilege similarity at all depths (e.g., layer 25: Delim ≈ 1.0, ISE ≈ 0.92, AIR ≈ 0.88). This motivates the design empirically.

- **Consistent, multi-configuration empirical results.** Table 1 and Figure 7 demonstrate that AIR reduces GCG ASR across all six configurations (3 models × 2 training methods): e.g., Llama-3.2-3B SFT GCG drops from 38% (Delim) to 4.1% (AIR); Qwen-2.5-7B DPO GCG drops from 32% (Delim) to 1.6% (AIR). The consistency across architecturally diverse models (3B, 7B, 8B) and training regimes argues against the improvement being an artifact of a single model's quirks.

- **Utility preservation.** Figure 6 shows at most ~2% degradation in AlpacaEval win rate (Qwen-2.5-7B DPO). Figure 8 shows AIR+DPO achieves the best utility × separation tradeoff on the SEP benchmark across all model sizes. The utility cost is minimal.

- **Lightweight and practical architecture.** Only 0.4M extra parameters for an 8B model (Equation 1); negligible inference overhead. The extension is a simple additive table lookup per layer, cleanly described and straightforwardly reproducible.

- **Rigorous experimental protocol.** All three IH injection mechanisms are re-implemented under the same two-stage training pipeline (Section 5.2), eliminating confounds from training recipe differences and enabling a fair comparison of the injection mechanism alone.

---

## Weaknesses

### Fatal
None.

### Major

- **Severely truncated gradient-based attack budget without gradient-masking check.** Section 5.4 states: "we optimize a 100-token random prefix for 200 (DPO models) or 50 (SFT models) steps." The original GCG paper and most downstream defense work use 500+ steps; 50 steps is an unusually small budget. The headline claim—"1.6× to 9.2× reduction in ASR"—comes entirely from this evaluation regime. A model that simply obfuscates the gradient landscape (rather than being structurally more robust) would present a high attacker loss at 50–200 steps but would eventually be compromised at 500+ steps. The paper provides no evidence to distinguish genuine structural robustness from gradient obfuscation: it does not (a) extend the evaluation to 500+ steps, (b) run a transfer attack (optimize against an undefended surrogate, evaluate on AIR), or (c) discuss this limitation explicitly. The pattern that AIR's large advantage materializes only on gradient-based attacks—not static attacks or SEP—is consistent with, though not proof of, gradient masking.

- **Asymmetric attack budget for DPO vs. SFT models is unexplained and may confound the SFT–DPO comparison.** DPO models receive 200 steps and SFT models 50 steps. The paper claims in Section 6 that "adversarial training with DPO yields more robust models than SFT" (corroborating SecAlign). But if DPO models receive 4× more attack budget, and the conclusion is that DPO is more robust, the differential might partly reflect a harder attack against DPO models rather than genuinely different structural robustness. The paper offers no justification for the asymmetry.

### Minor

- **Cosine similarity motivation (Figure 3) establishes correlation, not a causal mechanism.** The paper states (Section 3): "We hypothesize that this limits the effectiveness of the IH signals." High inter-privilege cosine similarity is not the same as IH enforcement failure—a model could have converged representations and still respect privilege boundaries through its attention heads and residual stream. The paper's design rationale is plausible but is not ruled-in by Figure 3 alone. Since the paper correctly uses "hypothesize," this is an appropriate epistemic framing; it would be strengthened by a layer-depth ablation (inject at only top half of layers, bottom half, etc.) to test whether the benefit is monotone in injection depth.

- **Single adversarial target across all gradient-based evaluations.** Section 5.4 specifies: "the adversarial instruction I′ is set to print exactly 'hacked!'" and ASR is measured by exact string match. All 208 × 2 attack instances target this single phrase. It is not demonstrated whether the 9.2× reduction holds for diverse adversarial targets (data exfiltration strings, behavioral redirection) that are more representative of the threat model described in Section 2.

- **Privilege hierarchy design choice (P0 = system ∪ user) is unexplained.** Section 5.3 assigns P0 to both system and user instruction tokens, P1 to data tokens, and P2 to model responses. This means the defense does not address user-level prompt injection (a user instruction overriding a system instruction)—an important subclass of the threat model. The paper does not discuss this design choice or its scope implications.

### Trivial
- The Astra headline result ("up to 145× lower ASR for SFT") is stated in Section 6.1 but its detailed discussion is deferred to Appendix C. At least a brief summary of the pattern in the main text would strengthen the discussion.

---

## Nice-to-Haves

- **Layer-depth ablation.** Inject IH embeddings into only the top/bottom/random half of decoder layers. This would directly test whether the benefit is monotone in injection depth, supporting (or complicating) the "signal degradation" hypothesis.
- **Longer GCG run (500 steps) or transfer attack.** Either extension would decisively address the gradient masking concern and substantially raise confidence in the 9.2× headline figure.
- **Multiple adversarial target strings.** Including 2–3 diverse targets (not just "hacked!") would strengthen the generalizability claim.
- **Defense-aware attacker discussion.** Because the embedding tables S_j are fixed and deterministic, a white-box attacker with knowledge of AIR could incorporate them into the attack objective. This known limitation should be acknowledged.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "Figure 3 is shown only for the base (pre-trained) model."** This is factually incorrect. Figure 3 explicitly shows three separate lines for Delim, ISE, and AIR—all of which are trained models with each respective mechanism applied. If it were the base model, AIR would not appear. The caption reads "Comparison of average cosine similarity between hidden representations of tokens encoded with different privilege level using different instruction hierarchy injection mechanisms (Delim, ISE, AIR)." REMOVED as a factual error.

- **Strength finder: "Rigorous and fair experimental protocol eliminates all confounds."** Partially accurate (identical training pipeline), but the asymmetric attack budget (50 SFT / 200 DPO steps) introduces a confound in the DPO vs. SFT comparison. REMOVED as stated; the fair protocol strength is retained with narrower scope.

- **Harsh critic: "Defense-aware attacker can cancel out privilege embeddings."** Valid in principle, but this is speculation about a possible future attack, not a verified flaw in the current paper. Moved to Nice-to-Have.

- **Harsh critic's concern that Astra results are discussed only in appendix.** This is a deferred-to-appendix complaint; appendix is stripped by the parser and exists in the submission. REMOVED as a formatting-artifact criticism. (The related substantive point—that the Astra summary in the main text is thin—is retained as a Trivial item.)

- **Harsh critic: "Static attacks are in-distribution for training and thus uninformative."** This is accurately noted in the paper itself (Section 6.1) and does not constitute a novel criticism. The paper acknowledges it and does not overclaim on this dimension. REMOVED as a strawman (paper already addresses it).

---

## Novel Insights

The most analytically interesting observation across both reviewers is the distinction between *structural robustness* and *gradient obfuscation*: AIR's improvements are concentrated exclusively on short-budget white-box attacks. On every other axis—static attacks, SEP separation score, AlpacaEval utility—the gains are marginal (≤0.5% SEP improvement, near-tied on static attacks). This concentration is meaningful: it suggests that AIR's primary effect may be to make the gradient loss landscape harder to descend quickly, rather than to fundamentally alter the model's representational structure. If true, an attacker with a larger budget or a transfer-based strategy might close the gap substantially. The paper would benefit greatly from empirically distinguishing these two hypotheses.

---

## Suggestions

1. **Run GCG to 500 steps** (or match the original GCG paper's budget) on at least one model and report the ASR. If the gap persists, the headline claim is strongly supported. If it narrows significantly, revise the claims accordingly.
2. **Add a transfer attack baseline**: optimize GCG against an undefended (None) model, then evaluate the resulting adversarial prefixes against AIR, ISE, and Delim. A defense that fails transfer attacks provides weak guarantees.
3. **Justify the DPO/SFT step asymmetry**, or equalize the budgets (both at 200 steps) and re-report the results to enable a clean DPO-vs-SFT comparison.
4. **Add 2–3 adversarial targets** beyond "hacked!" (e.g., a URL, a multi-word behavioral instruction) to establish generalizability of the ASR metric.
5. **Add a layer-depth ablation**: inject into only the first half, second half, or every other layer. This is a small experiment that directly validates the paper's central mechanistic claim.

---

## Score and Decision

**Axes:**
- *Originality*: Moderate. The idea (extend input-level IH injection to all layers) is simple and natural, analogous to RoPE for positional encodings. It is not a deep conceptual advance but is a clear, principled architectural improvement over prior work.
- *Importance of research question*: High. Prompt injection in agentic LLM systems is an active, practically significant security problem.
- *Claims well supported*: Partially. Consistent across 6 configurations, but the headline metric (GCG ASR reduction) rests on a truncated attack budget without gradient-masking safeguards.
- *Soundness of experiments*: Moderate. The evaluation protocol is fair and multi-dimensional (AlpacaFarm + SEP, SFT + DPO, 3 models), but the GCG step count is substantially below community norm and the single target limits scope.
- *Clarity of writing*: Good. The paper is clearly organized, the method is straightforwardly described, and the experiments are well-reported.
- *Value to research community*: Moderate-high. The method is practical, lightweight, and consistently improves over state-of-the-art, making it likely to be adopted if the gradient-masking concern is addressed.

**Calibration:**
- **Round 1 bracket**: 5.0–7.0.
  - Weak anchors (≤3.5): LLM jailbreak papers averaging 3.0 — clearly above.
  - Middle anchors (3.5–7.5): ISE paper (avg 6.0, Accept — the primary baseline AIR improves upon); PFT (avg 4.25, Reject); RA-LLM (avg 5.33, Reject).
  - Strong anchors (≥7.5): unrelated or broader-scope papers at 8.0.

- **Round 2 narrowing (5.0–7.0)**: Baseline defenses for adversarial attacks (5.25, Reject); ReFAT refusal feature adversarial training (5.75, Accept); TAR tamper-resistant safeguards (5.83, Accept); Scaling laws for adversarial attacks on activations (6.50, Accept).

  AIR is stronger than the baseline defenses paper (5.25) — cleaner method, more consistent results across multiple architectures. Comparable in scope to ReFAT (5.75) and TAR (5.83). Below ISE (6.0) in confidence because ISE's core method was adopted with full attack budgets, whereas AIR's headline improvement rests on a truncated evaluation. Clearly below the scaling laws paper (6.50) which has more comprehensive theoretical and empirical coverage.

  The paper sits between 5.25 and 5.75, closer to 5.5. The short GCG budget is a genuine methodological gap that prevents full trust in the 9.2× headline number. However, the multi-model, multi-paradigm consistency and the continuous loss curves in Figure 7 provide partial reassurance.

**Final score: 5.5 — Weak Reject.**

The paper has a real, simple, and well-motivated contribution, but the core empirical result (gradient-based ASR reduction) cannot be fully trusted until evaluated at community-standard attack budgets or with a gradient-masking sanity check. This is fixable in a revision.

| Anchor | Score | Round | Comparison |
|---|---|---|---|
| `3MDmM0rMPQ` (Inverse Prompt Engineering) | 3.0 | R1 (weak) | Clearly below AIR in scope and rigor |
| `sjWG7B8dvt` (ISE) | 6.0 | R1 (mid) | AIR's primary baseline; AIR shows consistent improvement but with truncated attack budget |
| `l3bUmPn6u5` (PFT) | 4.25 | R1 (mid) | AIR is stronger: more comprehensive evaluation, clearer method |
| `V01FPV3SNY` (RA-LLM) | 5.33 | R1 (mid) | Comparable scope; AIR has more systematic evaluation |
| `tTPHgb0EtV` (Booster) | 8.0 | R1 (strong) | Broader problem scope, stronger theory — AIR below this |
| `0VZP2Dr9KX` (Baseline defenses) | 5.25 | R2 | AIR is stronger: cleaner method, better evaluation |
| `s5orchdb33` (ReFAT) | 5.75 | R2 | Comparable scope; ReFAT has better theoretical grounding, AIR has better empirical breadth |
| `4FIjRodbW6` (TAR) | 5.83 | R2 | Comparable; TAR has stronger theoretical and empirical coverage |
| `YzxMu1asQi` (Scaling Laws) | 6.50 | R2 | AIR is below; scaling laws paper has stronger analysis and broader coverage |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>