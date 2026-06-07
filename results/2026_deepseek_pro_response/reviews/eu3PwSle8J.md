Now I have enough calibration data. Let me synthesize the findings and write the final review.

**Round 1 bracket:** 6.0–7.5 (above ISE at 6.0, below Booster at 8.0)

**Round 2 narrows to:** 6.0–7.0 (above ReFAT at 5.75 and GPromptShield at 6.0, comparable to or slightly below Tensor Trust at 7.0)

**Final placement:** AIR is clearly stronger than ISE (6.0) — it addresses ISE's primary limitation, has more thorough evaluation (3 models, 2 training paradigms, 6 attacks, SEP benchmark), and shows consistent improvements. But the logit-based ASR metric mismatch is a genuine concern that prevents it from reaching the 7.0+ level. I place it at **6.5**.

---

## Summary
This paper proposes Augmented Intermediate Representations (AIR), a defense against indirect prompt injection attacks that injects instruction-hierarchy (IH) signals into every decoder layer of an LLM rather than only at the input layer. The authors first diagnose that input-only IH signals (delimiters, ISE) degrade through the decoder — evidenced by rising cosine similarity between representations of tokens at different privilege levels across layers — and then propose per-layer trainable embeddings to preserve the signal. Across three models (3B–8B), two training paradigms (SFT, DPO), six attack types, and two benchmarks (AlpacaFarm, SEP), AIR demonstrates improved robustness while preserving model utility within 2% of the undefended baseline.

## Strengths
- **Quantitative diagnosis of input-only IH signal degradation (Figure 3):** The paper measures cosine similarity between token representations at different privilege levels across all 26 decoder layers of Llama-3.2-3B. For Delimiters, similarity stays at ~1.0 (representations are indistinguishable). For ISE, similarity rises from ~0.55 to ~0.92 by layer 25. AIR maintains meaningfully lower similarity throughout (~0.55 to ~0.88). This directly substantiates the paper's central motivation and is independently informative for the field.

- **Comprehensive evaluation matrix:** The experiments span 3 model architectures (Llama-3.2-3B, Qwen-2.5-7B, Llama-3.1-8B), 3 IH mechanisms (Delimiters, ISE, AIR), 2 adversarial training paradigms (SFT, DPO), 6 attack types (4 static + 2 gradient-based), and 2 benchmarks (AlpacaFarm, SEP). This is unusually thorough and allows readers to assess both within-method and cross-method comparisons.

- **Preserved model utility (Figure 6):** Across all three models and both training methods, AIR's win rates on AlpacaFarm remain within 2% of the non-adversarially trained baseline. For Qwen-2.5-7B with DPO, AIR achieves the highest win rate (91.9%) among all IH mechanisms. This directly supports the claim of robustness gains without utility degradation.

- **Negligible parameter overhead (Section 4):** AIR adds only 0.4M parameters to Llama-3.1-8B (0.005% increase), and the paper explicitly states inference-time compute overhead is negligible. This makes the approach practically adoptable.

- **SEP benchmark corroboration (Figure 8, Table 1):** On the SEP dataset — which uses generation-based evaluation (checking for witness string presence in model output) — AIR achieves the highest separation scores in all six model/training configurations. This provides independent, generation-based evidence that AIR's benefits are not an artifact of the logit-based metric used for gradient attacks.

- **Consistent loss-curve advantage throughout GCG optimization (Figure 7):** The attacker loss curves show AIR maintaining higher loss than baselines across the full optimization trajectory, with non-overlapping standard-deviation bands. This demonstrates the robustness advantage is sustained rather than confined to a single checkpoint.

## Weaknesses

### Fatal
None.

### Major
- **Metric mismatch for gradient-based ASR undermines headline quantitative claims (Section 5.4, Table 1):** The paper measures ASR for gradient-based attacks using "the likelihood (from model's logits) of generating the target phrase `hacked!`" while ASR for static attacks is measured by "determining if the model's response contains the literal phrase `hacked!`." These are fundamentally different metrics. A model that assigns high logit probability to "hacked!" under an adversarial prefix may never actually produce that output under standard decoding. The paper's central quantitative claims — 1.6× to 9.2× ASR reduction — are derived from this logit-based metric and could overstate AIR's practical advantage. That said, the GCG loss curves (Figure 7) and SEP results (generation-based) provide triangulating evidence that AIR genuinely improves robustness. This is a significant evidential gap rather than a fatal error; reporting generation-based ASR would close it.

### Minor
- **Asymmetric GCG optimization budgets without justification (Section 5.4):** The adversarial prefix is optimized for 200 steps for DPO models versus 50 steps for SFT models, with no rationale provided. Figure 7 suggests that for some configurations the attacker loss is still declining when optimization stops. While AIR's advantage is consistent and large enough that convergence effects are unlikely to reverse the ranking, equalizing optimization budgets would strengthen the comparison.

- **DPO vs. SFT comparison confounded by training regime (Section 5.2, Section 6.1):** DPO adversarial training uses LoRA (parameter-efficient fine-tuning) while SFT uses full fine-tuning. The paper's claim that "adversarial training with DPO yields more robust models than SFT" (Section 6.1) is therefore confounded — any DPO/SFT comparison also reflects LoRA vs. full fine-tuning. This does not affect the paper's primary claims about AIR vs. other IH mechanisms (which are within-method comparisons), but it weakens this specific sub-claim.

- **Causal mechanism not rigorously established (Section 4, Figure 3):** The paper's motivating narrative — that input-only IH signals "degrade" and that per-layer re-injection is the *reason* AIR works better — is supported by correlation (cosine similarity trends in Figure 3) but not by causal ablation. AIR adds per-layer learnable parameters that are directly optimized during adversarial training. While the parameter increase is negligible (0.4M out of 8B, or 0.005%), an ablation giving ISE or Delimiters an equivalent parameter budget (e.g., expanded ISE embeddings) would strengthen the mechanism claim.

- **P2 (response-level privilege) usage during inference unclear (Section 5.3):** The IH assigns P2 to model response tokens, but during autoregressive inference the response has not been generated yet. The paper does not explain how P2 embeddings are used during training (presumably via teacher-forcing) vs. inference, or whether they contribute to robustness or are merely a formalism for training symmetry.

### Trivial
- **Ambiguity in the injection point within the decoder block (Section 4, Figure 4):** Equation 1 defines $\tilde{x}'_{ij} = \tilde{x}_{ij} + s_j^k$ where $\tilde{x}_{ij}$ is the "intermediate token representation of the i-th input token in the j-th decoder block." The text and figure together suggest the IH signal is added at the block input, but the phrasing could be read as either block input or output. Clarifying this would aid reproducibility.

## Nice-to-Haves
- Reporting generation-based ASR for gradient attacks would close the primary evaluation gap and substantially strengthen the paper.
- An ablation showing which layers matter most for IH injection (e.g., first N layers only, every other layer) would illuminate the mechanism and potentially reduce the already-small parameter count.
- Running GCG to convergence (or equalizing step budgets across SFT/DPO) would eliminate the optimization-budget confound.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic:** "The paper does not discuss whether there exist other defenses that already inject signals into intermediate layers" — REMOVED as speculative; we cannot verify the existence of such defenses, and the paper's literature review appears adequate for its scope.

- **Harsh Critic:** "The paper does not discuss perplexity-based detection methods (e.g., Alon & Kamfonas, 2023)" — REMOVED as scope creep; the paper focuses on IH injection mechanisms, not orthogonal detection strategies.

- **Harsh Critic:** "Adversarial training data details are absent from the main text… The reader cannot assess what attacks or conflict patterns the models were trained on" — REMOVED per rules: appendix content is stripped by the parser and exists in the original submission.

- **Harsh Critic:** "No evaluation against adaptive attacks" / "the IH embeddings themselves could be targeted by an attacker" — REMOVED as partially addressed: the GCG evaluation already uses white-box gradient access through the IH embeddings, which is the adaptive threat the critic demands.

- **Strength Finder:** "Conceptual grounding in a well-established design principle (RoPE analogy)" — REMOVED from strengths. While the analogy with RoPE is clever and well-articulated, it is a presentation flourish rather than a substantive contribution. The paper's contributions stand on their own without this analogy.

## Novel Insights
The paper's finding that input-only IH signals become increasingly indistinguishable in deeper layers (cosine similarity → 1.0 for Delimiters, → 0.92 for ISE by layer 25) is a genuinely informative diagnostic with implications beyond this paper. It suggests that any defense relying solely on input-layer modifications may face a fundamental limitation in decoder-only architectures, where representations naturally converge as depth increases. This diagnostic methodology — measuring representation separability by privilege level across layers — could become a standard tool for evaluating future IH injection mechanisms.

## Suggestions
- The strongest single improvement would be to report generation-based ASR for GCG and Astra attacks, even if only on a subset of models. This would directly address the metric-mismatch concern.
- Equalize the GCG optimization budget across SFT and DPO, or provide a clear justification for the asymmetry (e.g., showing that SFT models converge faster).
- Add a brief clarification in Section 5.3 about how P2 embeddings are used during inference.

### Calibration anchors

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| ISE (sjWG7B8dvt) | 6.00 | R1 (mid) | AIR's direct predecessor. AIR addresses ISE's key limitation (input-only injection), has more thorough evaluation (3 models, 6 attacks, SEP), and shows consistent improvements. AIR > ISE. |
| PFT (l3bUmPn6u5) | 4.25 | R1 (mid) | Prompt injection defense with narrower scope. AIR has far more comprehensive evaluation including gradient-based attacks. AIR >> PFT. |
| Booster (tTPHgb0EtV) | 8.00 | R1 (high) | Strong theoretical framing (harmful perturbation, minimax loss). AIR's evaluation is more comprehensive but its theoretical contribution is simpler. AIR < Booster. |
| ReFAT (s5orchdb33) | 5.75 | R2 (low) | LLM safety via refusal feature adversarial training. AIR has clearer presentation and more comprehensive evaluation. AIR > ReFAT. |
| Tensor Trust (fsW7wJGLBd) | 7.00 | R2 (high) | Dataset paper with novel game-based collection. Different contribution type; AIR has a simpler method but strong evaluation. AIR ≈ slightly below. |
| GPromptShield (yCN4yI6zhH) | 6.00 | R2 (low) | Graph prompt defense, different domain. AIR appears stronger in evaluation thoroughness and clarity. AIR > GPromptShield. |

**Round 1 bracket:** 6.0–7.5. **Round 2 narrowed to:** 6.0–7.0. AIR is clearly stronger than ISE (6.0) and ReFAT (5.75), but the logit-based ASR metric mismatch prevents it from reaching the 7.0+ level occupied by contributions like Tensor Trust (dataset) or Booster (stronger theory). **Final score: 6.5.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>