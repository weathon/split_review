Now I have a clear picture of the paper and its calibration anchors. Let me synthesize the final review.

---

## Summary

The paper introduces the Open Proof Corpus (OPC), a human-validated dataset of over 5,000 LLM-generated mathematical proofs across 1,010 competition problems (IMO, USAMO, Putnam, etc.). Using this dataset, the authors address three open questions: the gap between final-answer accuracy and proof correctness, the gap between informal and formal proof generation, and the effectiveness of best-of-*n* selection strategies. They also fine-tune an 8B-parameter proof judge model that matches frontier models.

## Strengths

- **Rigorous dataset construction with measured reliability**: 5,062 proofs across 1,010 problems, with 10% double-grading yielding 90.4% inter-annotator agreement (estimated 5% judge error rate). The methodology includes a pilot phase, coordinator oversight, LLM-generated issue summaries with bias checking, and explicit abstention/uncertainty mechanisms (§3). This level of care is uncommon and provides a solid foundation for all downstream analyses.

- **Demonstration that final-answer accuracy does not reliably indicate proof correctness**: Figure 5 (§5.4) shows that while o3, o4-mini, and Gemini-2.5-Pro all achieve ~85–88% final-answer accuracy on MathArena problems, o3's proof correctness drops to 59.5% — a gap of nearly 30 percentage points. This is a concrete, well-measured finding that substantiates a claim often made but rarely quantified with human-validated proofs.

- **LLM judges reach human-level accuracy, and the dataset enables training a strong open judge**: Table 2 shows GPT-5 at 89.3% pass@1 and 90.8% maj@5, approaching the 90.4% human agreement baseline. The fine-tuned OPC-R1-8B achieves 88.1% maj@5, matching Gemini-2.5-Pro, demonstrating practical dataset utility. Table 3 further reveals that models judge their own proofs more harshly than others' — a finding with implications for self-improvement strategies.

- **Controlled best-of-*n* analysis showing ranking strategies outperform discrete/continuous selection**: On a subset where all 8 generations per problem are human-validated (§5.5, Figure 6a), Rank (Swiss) improves accuracy from 26% to 47% and continues to scale with *n*, while discrete and continuous methods plateau. This is a clean, well-controlled experiment with direct practical implications.

- **Thorough contamination analysis**: §5.6 and Table 4 demonstrate that providing ground-truth solutions yields at most 3–4% improvement in judging accuracy for smaller models and essentially no gain for top models (GPT-5 actually drops 0.3%). This credibly limits concerns that memorized solutions drive the judging comparisons.

## Weaknesses

### Fatal

None.

### Major

- **The claim that informal proof generation outperforms formal by 4× rests on a cross-study comparison on mismatched problem sets.** The abstract and §5.3 state that Gemini-2.5-Pro solves "4 times more problems" than Goedel-Prover-V2. However, Gemini-2.5-Pro is evaluated on the OPC's 114-problem PutnamBench *subset* (82.7% accuracy), while Goedel-Prover-V2's <19% figure comes from the *full* PutnamBench as reported by Lin et al. (2025b). The paper acknowledges the difficulty mismatch implicitly by later noting that an agentic formal system (Seed-Prover) reaches 50% on the full PutnamBench, but this does not correct the core comparison. The paper's own methodology (§3.1) states that informal answers were appended to "mirror the setup for formal models, allowing direct comparison" — yet the formal model was never evaluated on this identical subset. The direction of the finding is plausible, but the "4×" multiplier cannot be taken as reliable evidence without evaluating the formal system on the same problems. This does not undermine the paper's other contributions, but the claim is prominent (abstract, Fig. 1b) and should either be supported by a proper head-to-head evaluation or explicitly qualified as preliminary/cross-study.

### Minor

- **Model generation rankings in Fig. 3 may be partially confounded by data contamination, as the paper acknowledges.** §5.6 concedes that "the small gap in performance between GEMINI-2.5-PRO and O4-MINI in §5.1 cannot be conclusively attributed to genuine performance differences." While the paper does address contamination (and most conclusions are robust to it), the presentation of Fig. 3 as firm model rankings would benefit from a more prominent caveat in the figure caption or nearby text.

- **The abstract claims the OPC is "the first large dataset of LLM-generated solutions to problems from prestigious mathematics competitions such as the USAMO and IMO."** Mahdavi et al. (2025) evaluated a larger set of IMO Shortlist problems (though without releasing proofs). A qualifier such as "first open-source" or "first publicly available" would be more precise. This is a minor framing issue that does not diminish the dataset's actual value.

### Trivial

- The statement "LLMs are human level judges" in §5.2's heading slightly overstates: the human baseline of 90.4% is estimated from double-annotator agreement, not from a direct human-vs-ground-truth accuracy measurement. The claim is defensible and the paper handles it carefully in the body text, but the heading could be more precise.

## Nice-to-Haves

- Running Goedel-Prover-V2 (or another current formal system) on the identical 114-problem PutnamBench subset would convert the informal-formal comparison from a cross-study estimate into direct evidence. The paper's methodology already sets up the needed infrastructure (§3.1).
- A brief discussion in the main text of the OPC-R1-8B out-of-distribution robustness results (currently in §C, the stripped appendix) would address the natural concern about distribution-matched training inflating the judge model's reported performance.
- Adding a small-scale experiment using a stronger, disjoint judge model (e.g., GPT-5) in the best-of-*n* selection would help disentangle whether the gains come from the ranking strategy itself versus the competence of the judge.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic: "Absence of a clear mitigation for contamination in generation rankings" framed as a separate weakness.** REMOVED — the paper already discusses this in §5.6 with explicit caveats; the reviewers' framing would duplicate what the paper already does. Retained above as a minor presentation point (more prominent caveat).

- **Harsh Critic: "The paper does not include a formal datasheet or a discussion of ethical considerations."** REMOVED — this is a community-norm preference, not a weakness of the work. Moved to Nice-to-Haves implicitly.

- **Harsh Critic: concerns about stripped appendices (§C, §E).** REMOVED per hard rules — the parser strips appendices; the original submission includes them. Demanding appendix content in the main text is a presentation preference, not a weakness.

- **Harsh Critic: "The lack of GPT-5 or Grok-4 as proof generators is acknowledged" and suggesting more models.** REMOVED — the paper already acknowledges this in §6 (Limitations). The current model zoo is adequate for the paper's claims.

- **Strength Finder: "Quantitative comparison of informal vs. formal proof generation" as a clean strength.** DEMOTED — this comparison has the methodological issue described in the Major weakness. The finding is directionally correct but not cleanly supported as presented.

- **Strength Finder: generic framing about "the problem is important."** REMOVED — this is not a concrete, evidence-backed strength.

## Novel Insights

Beyond the paper's own contributions, the synthesis of reviews reveals an important methodological tension: the paper sets up a comparison infrastructure (appending informal answers to PutnamBench problems to mirror formal model setups) but then relies on cross-study numbers rather than executing the head-to-head evaluation this infrastructure was built for. This pattern — building the right scaffolding but not completing the measurement — is a common pitfall in benchmark papers and worth flagging for future dataset efforts. The paper otherwise exemplifies how a carefully constructed human-annotated resource can unlock multiple lines of empirical inquiry simultaneously (judge training, best-of-*n* analysis, self-evaluation bias, contamination robustness), demonstrating a high "insight-per-annotation-dollar" ratio that other dataset efforts could emulate.

## Suggestions

- Either run a formal prover (Goedel-Prover-V2 or similar) on the 114-problem PutnamBench subset to make the "4×" comparison direct and defensible, or qualify the claim as a cross-study estimate with appropriate caveats in the abstract and Fig. 1(b). The rest of the paper does not depend on this specific number.
- Add a one-sentence caveat to the Fig. 3 caption noting that the narrow gaps between top models cannot be conclusively attributed to genuine performance differences due to possible contamination.
- Move the OPC-R1-8B out-of-distribution robustness summary from appendix §C into the main text (even one sentence in §5.2) to preempt concerns about distribution-matched evaluation inflating the fine-tuned judge's numbers.

## Score and Decision

**Round 1 bracket:** The paper is stronger than Putnam-AXIOM (5.80, a smaller Putnam benchmark without proof evaluation) and Omni-MATH (6.75, a larger but final-answer-only Olympiad benchmark). Both lack the human-validated proof evaluation that distinguishes OPC. Initial bracket: 7.0–8.5.

**Round 2 narrowing:** Compared against MathGAP (7.00, synthetic arithmetic proof evaluation) and MUSTARD (7.33, synthetic theorem-proof data generation), OPC has stronger methodology (real competition problems, human validation, inter-annotator agreement) and more diverse empirical contributions. The "4×" claim weakness prevents it from reaching the clean 8.0 tier (MMQA, miniCTX). Final placement: **7.5**.

**Anchor summary:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| StepProof | 3.25 | R1 | Different focus; OPC is far stronger |
| Putnam-AXIOM | 5.80 | R1 | Smaller, final-answer-only; OPC clearly superior |
| Omni-MATH | 6.75 | R1/R2 | Larger but no proof evaluation; OPC stronger |
| MathGAP | 7.00 | R2 | Synthetic, constrained proofs; OPC more real-world valuable |
| MUSTARD | 7.33 | R2 | Synthetic data, no human validation; OPC stronger |
| LEGO-Prover | 7.50 | R2 | Different focus (formal method); OPC comparable |
| MMQA | 8.00 | R1 | Different domain; OPC slightly below this tier due to the "4×" weakness |

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>