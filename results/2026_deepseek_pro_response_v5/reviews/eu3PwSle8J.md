Now I have enough information to calibrate. Let me finalize:

**Round 1 Bracket:** Based on comparison with anchors, AIR sits clearly above PFT (4.25, rejected for weak attacks/baselines) and Baseline Defenses (5.25, rejected for incomplete evaluation), and above ISE (6.00, accepted but with weaker evaluation and less clarity). The upper bound based on initial bracketing is around 6.5-7.0 (papers with higher scores tend to be very polished or have broader impact). **Initial bracket: 5.5–7.0**.

**Round 2 Narrowing:** The ISE paper (6.00) is the most directly comparable — AIR is a clear improvement over ISE in motivation, evaluation breadth, and attack strength. AIR's weaknesses (parameter count confound, minor abstract bound quibble, missing limitations) are less severe than ISE's (limited novelty, no gradient-based attacks, unclear methodology). AIR is better than ISE but shares some limitations. The Durability of Safeguards paper (6.50) has a different focus (evaluation paper vs. method paper). 

**Final score:** 6.0 — clearly above ISE (6.00) in quality but the parameter count confound and missing ablation prevent it from reaching the 6.5–7.0 range.

Now let me write the final review.

Let me also reconsider the weakness list. I should be careful about what I keep. Let me re-examine each:

1. **Parameter count confound**: Verified in paper. AIR: (33) × 3 × 4096 = 0.4M. ISE: 3 × 4096 = 12K. This is a real 33× difference. The paper doesn't address this. KEEP as Major.

2. **Causal link between cosine similarity and robustness**: The paper asserts this link (line 87: "We hypothesize that this limits the effectiveness") but doesn't test it causally. This is a valid point but the paper does use "hypothesize" language. I'll keep as Minor.

3. **1.6× bound slightly optimistic**: Verified. For Llama-3.1-8B DPO GCG: ISE 4.0 vs AIR 2.8 = 1.43×. Below 1.6×. KEEP as Minor.

4. **Astra results not in abstract**: The reviewer notes this should be mentioned. The abstract does mention gradient-based attacks but doesn't name Astra specifically. This is very minor. REMOVE — the abstract already covers gradient-based attacks broadly.

5. **Section 3 claim about "systematically evaluating broader matrix"**: The paper says line 179: "Our work extends these investigations by systematically evaluating a broader matrix of IH injection mechanisms (Delimiters, ISE, AIR) and adversarial training techniques (SFT, DPO), including combinations not explored in prior studies." ISE was paired with SFT, SecAlign with DPO+Delim. The genuinely new combinations are ISE+DPO and AIR with both. But AIR is the contribution, so AIR+SFT and AIR+DPO are the main new combinations. This is a fair claim. REMOVE.

6. **How k_i is propagated**: Implementation detail. REMOVE as trivial.

7. **Attack budget (50 vs 200 steps)**: Figure 7 does show loss curves. For SFT models, the loss appears to be flattening around step 50 for some models but still decreasing for others. This is a legitimate concern. KEEP as Minor.

8. **ASR via logit likelihood**: Standard in field. MOVE to Nice-to-Have.

9. **Single target phrase**: Legitimate but minor concern. KEEP as Nice-to-Have.

10. **No adaptive attack**: The paper does cite Pandya et al. 2025 about architecture-aware attacks. Evaluating AIR-aware attacker is a high bar for a first paper. MOVE to Nice-to-Have.

11. **SEP improvement modest**: The paper shows AIR is best on 5/6 SEP cells. REMOVE.

12. **No limitations section**: Valid. KEEP as Minor.

13. **No threat model discussion**: The paper does define threat model in Section 2. But the inference-time privilege assignment assumption is not discussed. KEEP as Minor (part of missing limitations).

14. **SFT vs DPO confounded**: Valid. SFT uses full fine-tuning, DPO uses LoRA. KEEP as Minor.

15. **No confidence intervals**: Standard for this field. MOVE to Nice-to-Have.

Now let me compose the final review.Now let me compose the final review.

## Summary
This paper proposes Augmented Intermediate Representations (AIR), a defense against indirect prompt injection attacks that injects Instruction Hierarchy (IH) privilege signals into every decoder layer of an LLM, rather than only at the input layer as prior defenses do. The paper diagnoses through cosine similarity measurements that input-layer-only IH signals (Delimiters, ISE) progressively lose their ability to separate privilege levels as they propagate through the network. AIR addresses this by adding per-layer trainable embedding tables indexed by privilege level, adding only 0.4M parameters (0.005%) to an 8B model. Empirical results across three model families (3B–8B), two training paradigms (SFT, DPO), and multiple attack types show 1.6×–9.2× ASR reduction on gradient-based attacks with minimal utility degradation.

## Strengths
- **Concrete, quantitative motivation (Figure 3):** The paper measures average cosine similarity between hidden representations of tokens with different privilege levels across decoder layers. ISE similarity rises from ~0.55 to ~0.92 by layer 25, while AIR maintains lower similarity (~0.55 to ~0.88). This directly motivates the per-layer injection design and is a substantial improvement over prior work that asserted degradation without measuring it.
- **Strong, consistent empirical results on gradient-based attacks (Table 1, Figure 7):** AIR delivers substantial ASR reductions — on Llama-3.2-3B SFT, GCG ASR drops from 38% (Delim) / 48.1% (ISE) to 4.1% with AIR; Astra ASR drops to 0.1% vs. 14.5% (Delim). Figure 7 shows AIR consistently incurs higher attacker loss throughout GCG optimization, with the gap growing over steps.
- **Comprehensive evaluation matrix:** Results span 3 model families (Llama-3.2-3B, Qwen-2.5-7B, Llama-3.1-8B), 2 training paradigms (SFT, DPO), and 2 evaluation benchmarks (AlpacaFarm, SEP). AIR is best or tied in nearly every gradient-based attack cell. This breadth substantially strengthens the claim of generality.
- **Negligible overhead with principled design:** AIR adds only 0.4M parameters (0.005%) to an 8B model. The design — per-layer trainable embedding tables indexed by privilege level, added to intermediate representations via a simple additive operation — is compatible with any decoder-only transformer.
- **Utility preservation (Figure 6, Figure 8):** AlpacaEval win rates remain within ~2% of the non-adversarially trained baseline. On SEP, AIR with DPO achieves the best utility×separation point for all three models. This directly addresses the concern that robustness gains come at the cost of general capability.
- **Insightful RoPE analogy (Section 4, lines 105–106):** The paper connects per-layer IH injection to RoPE's per-layer injection of positional information, grounding what could appear as an ad-hoc trick in a well-established architectural design principle.

## Weaknesses

### Fatal
None.

### Major
- **Parameter count confounds the mechanistic claim (Section 5.3, parameter counts in Section 4):** AIR adds (L+1)×K×d ≈ 0.4M IH-dedicated parameters for Llama-3.1-8B, while ISE adds only K×d ≈ 12K. This ~33× difference means the observed robustness improvements could arise from increased capacity devoted to encoding privilege information rather than from per-layer injection per se. The paper cannot currently distinguish "per-layer injection is better" from "more parameters are better." This matters because the paper's central contribution is specifically about the architectural choice of per-layer injection. The empirical results demonstrating AIR's superiority over baselines remain valid, but the mechanistic interpretation they support is underdetermined. A controlled ablation — e.g., giving ISE per-layer segment embeddings with comparable parameter budget, or reducing AIR's embedding dimensionality to match ISE — would isolate the architectural contribution.

### Minor
- **The 1.6× lower bound in the abstract is slightly optimistic (Abstract, Table 1):** For Llama-3.1-8B DPO, GCG ASR is 2.8% (AIR) vs. 4.0% (ISE), giving a 1.43× improvement that falls below the stated 1.6× bound. The abstract range should be corrected.
- **SFT attack budget may not be converged (Section 5.4, line 190):** The gradient-based attack uses 50 steps for SFT models versus 200 for DPO. Figure 7 shows attack loss is still decreasing for some SFT models at step 50. The paper should justify these step counts or show convergence.
- **No limitations section (Section 7):** The paper would benefit from discussing what it does not establish: whether per-layer injection is the mechanism (vs. capacity), scaling to larger models, and assumptions about correct privilege-level assignment at inference time.
- **SFT vs. DPO comparison is confounded (Section 5.2, line 164):** SFT uses full fine-tuning while DPO uses LoRA. The observation that "DPO yields more robust models than SFT" (line 242) could stem from the training objective, the parameter-efficient regime, or an interaction. This deserves explicit caveating.

### Trivial
None.

## Nice-to-Haves
- Report binomial confidence intervals for ASR in Table 1 to help readers assess whether small differences (e.g., 2.7 vs. 3.1 SEP scores for Llama-3.2-3B) are statistically meaningful given only 208 test instances.
- Evaluate against an AIR-aware adaptive attacker that specifically targets the per-layer embedding tables, which would strengthen the security claims.
- Use more diverse adversarial target phrases beyond "hacked!" to strengthen generality.
- Measure ASR via actual generation rather than logit likelihood for robustness evaluations.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *"How k_i is propagated to each layer is ambiguous"* — This is an implementation detail, not a conceptual gap, and does not affect reproducibility of the core idea.
- *"The claim about systematically evaluating a broader matrix is undercut since ISE+DPO is the only new combination"* — AIR with both SFT and DPO are the main new contributions; AIR+DPO and AIR+SFT are new combinations.
- *"Astra results should be in the abstract headline"* — The abstract already covers gradient-based attacks broadly; naming a specific attack is unnecessary.
- *"SEP improvement is modest"* — AIR is best on 5/6 SEP model×training combinations. This is consistent improvement, not a weakness.
- *"ASR measured via logit likelihood rather than generation"* — This is standard practice in the field for gradient-based attack evaluation.

## Novel Insights
The analogy between per-layer IH injection and RoPE's per-layer injection of positional information (Section 4) is genuinely insightful. It reframes what could appear as an ad-hoc architectural trick as an application of a broader design principle — that token-level metadata critical to downstream processing benefits from being reinforced at every processing stage. Beyond this paper, the insight suggests a general design pattern: any token-level signal that must survive deep transformer processing may benefit from recurrent injection rather than one-shot input-layer encoding.

## Suggestions
- Add a controlled ablation that equalizes parameter count between AIR and ISE (e.g., give ISE per-layer segment embeddings with comparable budget, or downsample AIR's embedding dimensionality to match ISE's parameter count). This would directly test whether per-layer injection provides benefits beyond increased capacity and substantially strengthen the mechanistic claim.
- Add a limitations section explicitly discussing the parameter-count confound, threat model assumptions about correct privilege assignment at inference time, and scaling to larger models.
- Justify or equalize the SFT attack budget by showing convergence curves at 50 steps or extending to a consistent budget.
- Add a caveat that SFT uses full fine-tuning while DPO uses LoRA, complicating direct comparison of training objectives.

## Calibration Notes

**Round 1 bracket:** 5.5–7.0 based on broad anchor comparison.

Anchors considered across all rounds:

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| NEMESIS (5kMwiMnUip) | 1.40 | R1 | Far below — unserious jailbreak paper |
| MV5j4Qpq7N | 2.33 | R1 | Far below — weak defense with poor evaluation |
| PFT (l3bUmPn6u5) | 4.25 | R1 | Below — similar topic but weak attacks/baselines, narrow scope |
| Certifying LLM Safety (wNere1lelo) | 3.50 | R1 | Below — certified defense but limited practicality |
| Baseline Defenses (0VZP2Dr9KX) | 5.25 | R1 | Below — incomplete, inconsistent evaluation |
| RA-LLM (V01FPV3SNY) | 5.33 | R1/R2 | Below — alignment-breaking defense with less evaluation breadth |
| Deciphering Chaos (iKgQOAtvsD) | 5.75 | R2 | Below — attack paper, different focus |
| **ISE (sjWG7B8dvt)** | **6.00** | **R2** | **AIR is a direct improvement: stronger evaluation (GCG/Astra), better motivation (Figure 3), principled extension to per-layer** |
| Durability of Safeguards (fXJCqdUSVG) | 6.50 | R2 | Slightly above — more polished critical analysis |
| Robustness Over Time (eC4WlSZc4H) | 6.75 | R2 | Above — broader longitudinal study |
| ArrAttack (sULAwlAWc1) | 7.00 | R1 | Above — strong attack paper with novel method |
| Backtracking (Bo62NeU6VF) | 8.00 | R1 | Far above — very polished, novel paradigm |

**Round 2 narrowing:** The ISE paper (6.00) is the most directly comparable anchor. AIR is a clear improvement over ISE in evaluation breadth (gradient-based attacks), diagnostic motivation (Figure 3), and conceptual depth (RoPE analogy). However, AIR introduces a parameter-count confound that ISE does not have, preventing it from reaching 6.5+. The paper sits at **6.0** — a solid accept with a clear, well-motivated contribution that is marred by an unresolved confound in its mechanistic interpretation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>