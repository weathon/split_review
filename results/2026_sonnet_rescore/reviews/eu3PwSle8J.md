Now I have everything I need to write the final consolidated review. Let me synthesize the inputs against the paper.

---

## Summary
This paper proposes Augmented Intermediate Representations (AIR), a defense against indirect prompt injection attacks in LLMs. Rather than injecting instruction-hierarchy (IH) signals only at the input layer (as in prior work—Delimiters and ISE), AIR injects layer-specific trainable embeddings at every decoder layer, adding only ~0.4M parameters (0.005% overhead). Evaluated across three models (Llama-3.2-3B, Qwen-2.5-7B, Llama-3.1-8B) and two training paradigms (SFT and DPO), AIR reduces GCG/Astra attack success rates by 1.6×–9.2× over prior methods with minimal utility degradation.

---

## Strengths

- **Consistent, large-margin gains on gradient-based attacks across all models and training paradigms.** Table 1 shows GCG ASR on Llama-3.2-3B (SFT) drops from 38% (Delim) to 4.1% (AIR), a 9.2× reduction; on Llama-3.1-8B (DPO) from 4.0% (ISE) to 2.8% (AIR). Figure 7 confirms that the attacker loss under AIR remains consistently higher throughout the optimization trajectory, not just at the endpoint.

- **Representational analysis supporting the design choice.** Figure 3 shows that with Delim/ISE, cosine similarity between different-privilege-level representations rises to ~0.92 by layer 25 (for ISE) or 1.00 throughout (for Delim), while AIR reaches only ~0.88—maintaining better privilege-level separation at every layer. This is measured on trained models (since AIR's trainable embeddings are included and show strictly lower values than ISE), directly supporting the motivation.

- **Utility preserved under adversarial training.** Figure 6 shows AlpacaEval win rates for AIR-equipped models within 2% of the non-adversarially-trained None baseline; Figure 8 shows AIR+DPO achieves the best utility × separation trade-off on the SEP benchmark across all model sizes.

- **Lightweight and practically deployable.** Section 4 quantifies the overhead precisely: (32+1)×3×4096 = 0.4M parameters for Llama-3.1-8B, with negligible inference overhead.

- **Fair comparative protocol.** Section 5.2 documents that all methods (Delim, ISE, AIR) undergo the exact same two-stage training pipeline, eliminating confounds from training recipe differences.

- **Conceptual grounding via positional embedding analogy.** Section 4 draws a principled parallel to RoPE—both distribute a critical signal (positional or privilege) across all layers rather than injecting it only at input—providing a well-motivated design rationale.

---

## Weaknesses

### Fatal
None.

### Major

- **Attack budget (50–200 steps) is far below the community standard for GCG evaluations, and the asymmetric budget between DPO (200 steps) and SFT (50 steps) is unexplained.** Section 5.4 states these budgets without justification. Standard GCG work uses 500–1000+ steps; running fewer steps is precisely the condition under which gradient obfuscation and genuine robustness are hardest to distinguish. The headline result (1.6×–9.2× reduction in ASR) is derived exclusively from this setting. The concern is sharpened by the observation that on static attacks and SEP (Table 1), all three methods are essentially tied (0.0–0.5% ASR on static attacks; 2.2–5.3% SEP scores). The only meaningful differentiation between AIR and prior methods appears in gradient-based attacks at short budgets—the precise regime where gradient obfuscation is hardest to rule out. The asymmetry between DPO (200 steps) and SFT (50 steps) additionally complicates interpreting the claim (Section 6.1) that "DPO yields more robust models," since the DPO models are evaluated under a 4× stronger attack. A transfer attack or extended-budget evaluation (e.g., 500+ steps) would decisively address this.

- **Single adversarial target and narrow ASR measurement.** Section 5.4 fixes the adversarial instruction I′ as the literal string "hacked!" and measures ASR by exact-string match across all 208 test instances and all gradient-based attack evaluations. The threat model in Section 2 encompasses diverse harms (data exfiltration, behavioral redirection, harmful outputs), but the entire gradient-based robustness evaluation rests on a single-phrase target. It is unclear whether the reported 1.6×–9.2× improvement would replicate across diverse adversarial goals (e.g., different target strings, multi-step instructions, data exfiltration). This limits the generalizability of the headline numbers.

### Minor

- **Privilege assignment (P0 = system + user) is not discussed.** Section 5.3 maps both system and user tokens to P0 and only data-segment tokens to P1. The threat model (Section 2) is specifically about data-segment injections overriding user instructions, so within this scope the assignment is defensible. However, the paper does not discuss whether AIR would extend to user-level prompt injection (where malicious tokens appear in the user segment), and whether the current hierarchy design limits AIR's scope of protection.

- **No layer-depth ablation to verify the "signal degradation through depth" hypothesis.** AIR injects embeddings at every layer, but the paper never tests injecting at only a subset of layers (e.g., bottom half, top half, every other layer). Such an ablation would directly test whether the benefit is monotone in injection coverage depth, which would validate the core design hypothesis. Without it, it is unclear whether most of the gain comes from a few critical layers.

- **The cosine-similarity metric does not directly demonstrate privilege-level confusion.** Figure 3 is presented as evidence of "signal degradation," but high cosine similarity between representations is not equivalent to the model failing to use those representations to track privilege—the model could still route decisions correctly through attention heads or residual subspaces not captured by cosine similarity. The analysis is consistent with the hypothesis but does not establish it causally.

### Trivial
None that survive verification.

---

## Nice-to-Haves

- **Extended attack evaluation at 500+ steps.** Repeating the GCG evaluation at standard budgets would resolve the gradient-obfuscation concern definitively and significantly strengthen the paper's central claim.
- **Transfer-attack sanity check.** Optimizing adversarial prefixes against a surrogate model (without AIR) and then evaluating success on an AIR-defended model would verify that the robustness is structural rather than due to gradient masking.
- **Diverse adversarial targets.** Testing with a range of adversarial instructions (not just "hacked!") would improve the credibility and generalizability of the ASR results.
- **Defense-aware white-box analysis.** Since AIR's privilege embedding tables are fixed and deterministic at deployment, a sophisticated white-box attacker could incorporate them into the optimization. A brief discussion of this known limitation would be valuable.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Figure 3 is shown only for the base (pre-trained) model"** (Harsh Critic, Section 3 / Figure 3 note). — REMOVED. The paper's Figure 3 explicitly includes AIR in the comparison. Since AIR's embedding tables are trainable (not present in a base model), this figure must be generated from trained models. The critic's claim that the pre-training-only analysis is deceptive appears factually incorrect given the paper content.

2. **Criticism that the motivation for AIR is unfounded because "Figure 3 shows only a correlation"** — DEMOTED to Minor. The causal mechanism is not directly proven, but the motivation is clearly stated as a hypothesis, not a theorem, and it is empirically consistent with the results.

3. **Asymmetric attack budget biases the DPO-vs-SFT comparison** — Merged into the Major weakness above rather than listed separately.

4. **Missing appendix discussion of Astra (Section 6.1)** — REMOVED per hard rule on stripped appendix content.

5. **Strength Finder claim "Rigorous and fair experimental protocol"** — Retained but not listed as a standalone strength (merged into main strengths above), since the attack budget shortfall is a real methodological limitation that partially undermines this framing.

---

## Novel Insights

The paper's most genuinely novel observation is the representational-degradation diagnosis: Figure 3 quantitatively demonstrates that input-only IH injection (ISE, Delim) fails to maintain privilege-level separation in deep layers, with cosine similarity rising to 0.92+ by layer 25 even after training. AIR's recurrent injection—analogous to how RoPE injects positional information at every attention layer rather than once at input—verifiably maintains better separation (0.88 vs. 0.92 at layer 25) and translates this representational advantage into consistent large-margin gains against gradient-based attacks across all three model families tested. The connection between "signal persistence through depth" and "attack resistance under gradient-based optimization" is empirically supported, even if not causally isolated.

---

## Suggestions

1. Re-run GCG and Astra evaluations at 500 steps (minimum) for at least one model to confirm the ASR gap is not a short-budget artifact; report loss curves through the full budget.
2. Add at least 3–5 diverse adversarial target strings in the AlpacaFarm robustness sweep; report mean and variance of ASR across targets.
3. Include a layer-depth ablation (inject AIR at bottom 50% of layers, top 50%, every other layer) to isolate which layers contribute most to the robustness gain.
4. Clarify the privilege mapping choice (P0 = system + user) and explicitly state whether the defense is designed to cover user-level injection or only data-level injection.
5. Add a transfer-attack control to rule out gradient obfuscation.

---

**Evaluation along key axes:**
- **Originality:** Incremental but non-trivial extension of an active research direction; the analogy to RoPE is insightful.
- **Importance:** Prompt injection defense for agentic LLMs is a pressing practical problem; a method with negligible overhead and consistent gains is valuable.
- **Claims supported:** Core claims are empirically supported across multiple models and training paradigms, but the attack budget concern introduces meaningful uncertainty around the headline numbers.
- **Soundness:** Methodology is clean and the fair-comparison protocol is carefully designed; the attack evaluation regime is the primary soundness concern.
- **Clarity:** Well-written; the method description is precise and the experimental setup is clearly documented.
- **Community value:** High—simple, reproducible, practical defense mechanism.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>