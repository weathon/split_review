## Summary

The paper proposes **Augmented Intermediate Representations (AIR)**, a defense mechanism against indirect prompt injection attacks on LLMs. Existing defenses enforce instruction hierarchy (IH) by injecting privilege-level signals only at the input layer (via delimiter tokens or input-level segment embeddings). The authors demonstrate that these input-level signals degrade through decoder layers—evidenced by cosine similarity analysis—and address this by adding learnable privilege embeddings at every decoder layer with negligible parameter overhead (~0.005%). Evaluated across three LLMs (3B–8B), two training regimes (SFT, DPO), static and gradient-based attacks, AIR achieves 1.6×–9.2× reductions in attack success rate on gradient-based attacks compared to prior methods with minimal utility cost.

## Strengths

- **Well-motivated hypothesis with empirical support**: The cosine similarity analysis (Figure 3) provides direct evidence that existing input-level IH signals become increasingly indistinguishable across deeper decoder layers, validating the core motivation. The analogy to RoPE—which improved LLMs by distributing positional signals across layers rather than injecting only at input—is conceptually compelling and grounded in precedent.

- **Simple, low-overhead mechanism**: AIR adds only K × (L+1) learnable embedding vectors, amounting to 0.005% parameter overhead for Llama-3.1-8B. The design is drop-in compatible with existing SFT and DPO training pipelines, making it easy to adopt.

- **Comprehensive evaluation**: Tests span three models (Llama-3.2-3B, Qwen-2.5-7B, Llama-3.1-8B), two training strategies (SFT, DPO), four static attacks, two gradient-based attacks (momentum-enhanced GCG and Astra), and two benchmark datasets (AlpacaFarm, SEP). The same training protocol is used for all baselines, ensuring fair comparison.

- **Strong gradient-based attack results**: AIR consistently achieves the lowest GCG ASR across all model-training combinations in Table 1. The gains are particularly striking: e.g., Llama-3.2-3B SFT drops from 38% (Delim) to 4.1% (AIR); Qwen-2.5-7B DPO drops from 7.7% (ISE) to 1.6% (AIR). These are genuine full white-box results, as the attacker computes gradients through AIR's embedding tables.

- **Maintained utility**: Figure 6 shows win rates for AIR-trained models are nearly identical to non-adversarially trained baselines across all settings, with at most 2% degradation.

## Weaknesses

### Fatal
None.

### Major

1. **Shallow attack budget for SFT models**: GCG/Astra optimization is capped at only 50 steps for SFT models and 200 for DPO models. Standard GCG evaluations typically run 500+ steps. While Figure 7's loss curves suggest AIR's loss stays high across steps, 50-step SFT evaluations may not reflect the true attack ceiling. The asymmetry between SFT (50) and DPO (200) also makes direct comparison of training regimes harder.

2. **ASR proxy for gradient-based attacks**: The gradient-based ASR is measured via the model's log-likelihood of generating "hacked!" rather than actual generation and string-matching. This is a proxy that can diverge from true behavioral success rate, particularly for defended models where calibration may change post-finetuning.

3. **No mechanistic explanation for *why* the gain is so large**: While the cosine similarity argument is suggestive, it is not causally connected to robustness. Low similarity between privilege-level representations does not mechanistically guarantee resistance to adversarial optimization. Understanding whether AIR works by making the loss landscape harder to optimize, by inducing higher gradient variance, or by genuinely preventing token-level conflation would strengthen the contribution.

### Minor

1. **Cosine similarity analysis is only shown for Llama-3.2-3B** (Figure 3). It is unclear whether the pattern generalizes to Qwen-2.5-7B and Llama-3.1-8B, which have different architectures.

2. **Inconsistent relative ordering across settings**: ISE-DPO outperforms AIR-DPO on the Astra attack for Qwen-2.5-7B (2.3% vs 0.9% is actually AIR winning—but the ordering inverts for ISE in GCG). The gains vary widely (1.6× to 9.2×), and the paper provides limited analysis of when and why the improvement is larger or smaller.

3. **Single adversarial target**: All robustness evaluations use one adversarial instruction ("print exactly 'hacked!'"). Broader coverage of adversarial objectives would improve generalizability claims.

### Trivial

- The connection to RoPE, while elegant, is qualitative; unlike RoPE which injects information into attention, AIR adds a constant additive bias per-layer—a simpler mechanism.

## Nice-to-Haves

- Ablation on which layers to apply AIR (e.g., every layer vs. every other layer) to understand where the benefit comes from.
- Evaluation under stronger attacks run to convergence (500+ steps) to show AIR's floor.
- Cosine similarity analysis extended to all three evaluated models.
- An analysis of how gradient norms or loss landscape curvature differ for AIR vs. ISE vs. Delim, to better mechanistically explain the robustness gain.

## Novel Insights

The key novel insight is that privilege-level signals, like positional signals, benefit from being distributed across all Transformer layers rather than injected only at the input. The empirical observation that existing IH signals become increasingly indistinguishable across layers—visible in the cosine similarity convergence—provides a concrete and previously unreported mechanism for why input-level defenses plateau in effectiveness against gradient-based attacks. The interaction between training regime (DPO vs. SFT) and IH injection method is also informative: DPO consistently boosts robustness regardless of injection mechanism, but the AIR+DPO combination yields the best joint utility-separation performance, suggesting the injection mechanism and optimization objective have complementary effects.

## Suggestions

- Run gradient-based attacks to convergence (500 steps minimum) and report both proxy ASR (likelihood) and behavioral ASR (string matching on actual generation) for a more rigorous evaluation.
- Extend the cosine similarity analysis across all evaluated models and report results for AIR after fine-tuning (not just a pre-training baseline).
- Consider reporting accuracy separately on instruction-only instances (no data segment) to detect any edge case utility degradation.
- Examine whether attacking the IH embedding tables specifically (e.g., gradient-based perturbations designed to confuse AIR's privilege lookup) constitutes a more powerful adaptive threat.

## Score and Decision

AIR is a clean, well-motivated contribution to LLM prompt injection defenses. The idea is intuitive, the implementation is minimal, and the experimental results across three models and two training strategies consistently support the claims. The analogy to RoPE provides a principled conceptual framing. The primary concerns—modest attack budget, proxy ASR metric, and lack of mechanistic depth—are real limitations but do not invalidate the core finding. The paper sits comfortably above the ICLR 2026 mean quality and merits acceptance.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>