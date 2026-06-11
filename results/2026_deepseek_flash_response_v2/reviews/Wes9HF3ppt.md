## Summary

This paper introduces Insertion Language Models (ILMs), which generate sequences by inserting tokens one at a time at arbitrary positions using a transformer encoder and a denoising objective. To avoid high variance in the naive marginalization training objective, the authors propose a biased approximation that predicts normalized counts of dropped tokens. The method is evaluated on planning tasks (star graph path generation, zebra puzzles) and text generation/infilling (LM1B, TinyStories). The strongest results are on star graphs, where ILM achieves 99.1–100% exact-match accuracy on variants where both ARMs (23–75%) and MDMs (21–36.5%) collapse dramatically.

## Strengths

1. **Star graph results are compelling and demonstrate a genuine structural advantage.** On Star_hard, ILM scores 99.1% exact-match accuracy versus MDM's 21.0% and ARM's 23.0% (Table 1). On Star_medium, ILM achieves 100% versus MDM's 36.5%. These are large, unambiguous improvements that directly validate the paper's core claim that insertion-based generation overcomes structural limitations of both left-to-right generation and simultaneous unmasking on tasks with variable-length dependencies. The gap is not incremental — it suggests a fundamentally better fit for this class of problems.

2. **Zebra puzzle results provide complementary evidence.** ILM scores 90.0% vs ARM's 81.2% and MDM's 82.6%, and comes close to ARMO (oracle-order ARM, 91.2%), showing the benefit extends beyond the star graph setting.

3. **The methodological motivation is clear and the design principles are sound.** The paper correctly identifies that MDMs cannot do variable-length infilling because the number of masks is fixed (Section 2), and that simultaneous unmasking can violate token dependencies. The ILM framework of iterative single-token insertion at arbitrary positions is a principled response to both problems. The dedicated stopping classifier (vs IT's EOS approach) is shown empirically to solve the variable-length generation failure (35.2% → 100% on Star_easy, Table 1).

## Weaknesses

### Major

1. **Overclaimed text generation results contradict the paper's own data.** The abstract and conclusion state ILMs "perform on par with ARMs" in unconditional text generation. On Stories this is roughly true (ILM 2.14 vs ARM 2.11 NLL). But on LM1B, ILM's NLL is **4.67 vs ARM's 3.94** — a 19% relative gap. This is not "on par." The paper acknowledges the gap only in passing (attributed to "training token efficiency and scaling laws") and does not resolve the tension with the paper's framing. This overclaim needs to be corrected, either by qualifying the claim to the Stories dataset or by providing analysis that closes the gap.

2. **No empirical comparison between the proposed biased objective and the naive marginalization objective.** A core methodological claim (Section 3, lines 18–19, 79) is that the naive objective has "extremely high variance" that "can make training infeasible." Yet no experiment demonstrates this. Without this ablation, it is unclear whether the approximation is actually necessary or whether the model would work equally well with the simpler objective. This weakens the empirical support for the paper's central technical innovation.

3. **The explanation for why MDMs fail on variable-length star graphs is architecturally imprecise.** The paper states MDMs "work with absolute token positions" (line 147), but the MDM architecture used (DDiT) employs RoPE (relative positions), like the ILM. The more likely explanation — that MDMs solve the path in one parallel pass while ILMs decompose it into sequential steps — is more accurate but not clearly stated. This undermines a key claimed mechanistic insight.

### Minor

4. **The notation `α_Duo` appears in Table 3 without any definition in the main paper body** (confirmed via grep — zero matches outside Table 3). This makes the infilling evaluation results partially uninterpretable.

5. **No statistical uncertainty reported for any result.** None of the tables include standard deviations, confidence intervals, or replication runs. For the planning tasks, effect sizes are large enough that this likely does not change qualitative conclusions, but for text generation (Tables 2, 3) where differences are smaller, the absence of variance estimates is a structural weakness.

6. **The length confound in text evaluation is not addressed for ILM.** On Stories, ILM generates sequences averaging 119 tokens versus the training data's 205 (a 42% reduction). For the Prometheus LLM judge evaluation (Figure 5), shorter sequences naturally have fewer opportunities for inconsistency, which could inflate coherence/consistency scores. The paper acknowledges this issue for MDM ("the main reason for the high entropy...of sequences produced by the MDM") but not for its own model. (For per-token NLL, which is length-normalized, this concern is less severe.)

7. **The Insertion Transformer baseline is only compared on star graphs** (Table 1 shows "–" for Zebra and no results for text tasks). This limits assessment of whether ILM's improvements come from the specific training objective versus the insertion framework itself.

### Trivial

8. **ARM's performance on Star_medium (75.0%) being higher than Star_easy (32.3%) is unexplained.** If these are ordered by difficulty, this pattern requires clarification.

## Nice-to-Haves

- An ablation comparing the proposed biased objective against the naive marginalization objective would significantly strengthen the core methodological claim.
- Reporting results over multiple random seeds for text experiments.
- Providing likelihood estimates for the ILM itself (not just NLL under an external LLM).
- Analysis of the stopping classifier's behavior (accuracy, learned threshold, typical stopping point).

## Removed Points

The following points from reviewer inputs were removed or downgraded:

- *"The theoretical analysis is relegated to Appendix D, which is not available"* — The parser strips appendices; this cannot be evaluated from the available text. The core point (missing ablation) is retained in Major Weakness #2, but the appendix reference is removed.
- *"Shorter sequences are inherently easier for an evaluator LLM to predict because they contain fewer tokens whose likelihood compounds"* — For per-token NLL (which is length-normalized), this argument about compounding probability does not straightforwardly apply. Retained only for the Prometheus (holistic) evaluation, where it is a valid concern (Minor Weakness #6).
- *"The mismatch between training (all dropped tokens simultaneously) and inference (one token at a time) is not discussed"* — The paper explicitly describes this as a tractable approximation (lines 79–80). The reviewer did not identify a concrete failure mode beyond speculation.
- *"MDMs have known mitigation strategies not acknowledged"* — The related work section (lines 125–126) does acknowledge greedy/top-k sampling and flow-based strategies.

## Novel Insights

The strongest signal from this review is the star graph result: the dramatic gap between ILM (99.1%) and both ARMs (23%) and MDMs (21%) on Star_hard is not incremental — it suggests a genuine structural advantage of iterative single-token insertion for tasks where token dependencies do not follow sequential order and lengths vary. This is the paper's true contribution and is well-supported. The text generation results are more mixed and the paper would benefit from reframing around this strength.

## Suggestions

1. Correct the text generation claim in the abstract/intro to accurately reflect the LM1B results (e.g., "competitive with ARMs on short-story generation, with a gap on denser text like LM1B").
2. Add an ablation comparing the proposed biased objective against the naive marginalization objective — this is the most impactful single improvement.
3. Clarify or correct the explanation of why MDMs fail on variable-length star graphs (the "absolute positions" claim is architecturally imprecise).
4. Define α_Duo in the main text and add a brief description of the sampling variant it refers to.
5. Add error bars or replication results for the text generation experiments.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Beyond Autoregression: Discrete Diffusion for Complex Reasoning (NRYgUzSPZz) | 6.25 | R1 | Similar scope (diffusion for planning); my paper has comparable planning results but weaker text eval and missing ablation |
| Think while You Generate (MJNywBdSDy) | 5.75 | R1/R2 | Both propose novel generation frameworks; my star graph results are more dramatic but evaluation is less clean |
| Scaling up Masked Diffusion Models on Text (WNvvwK0tut) | 6.50 | R1 | More thorough evaluation and methodology; my paper is weaker methodologically but more novel in paradigm |
| COrAL: Order-Agnostic Language Modeling (0JjsZC0w8x) | 5.75 | R2 | Similar theme (order-agnostic generation); my paper has stronger planning results |
| A Branching Decoder for Set Generation (riNuqYiD66) | 7.00 | R2 | Cleaner evaluation; my paper tackles harder problems but with more evaluation gaps |
| Integrating Planning into Single-Turn Long-Form Text (YONCcPQJoC) | 4.75 | R2 | My paper has stronger core contribution and empirical results |
| Interpolating AR and Discrete Denoising Diffusion Language Models (tyEyYT267x) | 8.00 | R1 | Strong methodology and clean results; my paper is clearly weaker |
| Diffusion Language Models Can Perform Many Tasks (Qn4HEhezKW) | 5.00 | R1 | Rejected with mixed results; my paper has stronger planning evidence |

**Bracketing:** Round 1 placed the paper between approximately 5.0 and 6.5 (stronger than the 3.0–3.25 weak anchors and the 5.00 rejected paper, but weaker than the 6.50+ papers). Round 2 narrowed the bracket: the paper is comparable to "Think while You Generate" (5.75) and "Beyond Autoregression" (6.25), but its evaluation weaknesses (missing ablation, overclaimed text results, no error bars) pull it toward the lower end of that range.

**Final score:** 5.75 — The paper has a genuine and well-demonstrated contribution on planning tasks, but the overclaimed text generation results, missing ablation for the core methodological claim, and several evaluation gaps prevent a higher score.

**Decision:** Accept — The star graph results alone are a strong enough contribution to merit acceptance, and the core idea is novel and well-motivated. However, the authors should address the overclaiming and ideally add the missing ablation before publication.

MY FINAL SCORE: <score>5.75</score>
MY FINAL DECISION: <decision>Accept</decision>