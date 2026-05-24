Now I have all the information needed to produce the final consolidated review.

---

## Summary

This paper identifies a novel "priming vulnerability" in Masked Diffusion Language Models (MDLMs): affirmative tokens appearing at intermediate denoising steps can steer even safety-aligned models toward harmful outputs. The authors demonstrate this vulnerability through both direct token injection (anchoring attack) and query-level optimization (First-Step GCG, backed by a theoretical lower bound). They then propose Recovery Alignment (RA), which trains MDLMs to recover safe responses from intentionally contaminated intermediate states via an RLHF-style objective. Experiments across three MDLMs, multiple attacks, and eleven utility benchmarks show that RA dramatically reduces attack success rates while preserving general capability, and also improves robustness to conventional conversational jailbreaks.

## Strengths

- **Novel and well-characterized vulnerability.** The priming vulnerability is clearly formalized and empirically validated. The anchoring attack shows that injecting even a single token at the first denoising step raises ASR from 2% to 21% on LLaDA Instruct, and ASR rises sharply with more intervention steps (Figure 2). Theorem 4.1 provides theoretical grounding for why the vulnerability is exploitable from the query alone, and the resulting First-Step GCG attack achieves up to 4× higher ASR than Monte Carlo GCG while being 20× faster (Table 1).

- **Effective and well-motivated defense.** The paper clearly explains why standard alignment fails (Section 5, Equations 5–6): training from fully masked starts does not constrain behavior at contaminated intermediate states. RA directly addresses this gap by training on those states. The results are strong: RA reduces ASR under anchoring attack at step 4 from 44.0% to 1.3% on LLaDA Instruct and from 35.0% to 0.7% on LLaDA 1.5 (Table 2).

- **Comprehensive evaluation.** The method is tested on three different MDLMs (LLaDA Instruct, LLaDA 1.5, MMaDA MixCoT), against four intervention-based attacks and three conversational jailbreaks, with three different safety evaluators. Utility is measured across eleven diverse benchmarks (Table 4), showing average accuracy preserved within 0.5 percentage points. Ablations on max intervention step and scheduling (Figures 3a, 3b) validate the curriculum design choices.

- **Generalization to conventional attacks.** RA also reduces ASR on conversational jailbreaks like PAIR (44.3% → 10.0% on LLaDA Instruct) and Crescendo (81.3% → 45.0%), indicating the recovery mechanism generalizes beyond intervention-based attacks (Table 3).

## Weaknesses

### Fatal
None.

### Major

- **Uncharacterized reward model dependence.** RA is instantiated with RLHF using a pre-trained DeBERTaV3 reward model (He et al., 2021; Köpf et al., 2023), but the paper provides almost no detail about this reward model — its training objective, input format, output range, calibration, or sensitivity to different types of harmful content. The paper also does not study how RA's effectiveness changes if a different reward model is used. The authors themselves note that "reward hacking" occurs when the intervention step is too large, which hints at fragility. Without understanding the reward model's properties, it is unclear whether RA's strong results would transfer to other reward signals. This is a substantive gap because RA's alignment is entirely mediated through this reward signal. This limits certainty in the method's robustness, though it does not invalidate the core contribution.

### Minor

- **Utility evaluation lacks error bars and shows some non-trivial drops.** Table 4 reports single-run accuracy without standard deviations. HumanEval drops notably from 22.0 to 17.1 on LLaDA Instruct (a ~22% relative decrease), and PIQA drops from 74.4 to 71.6. While the paper acknowledges possible "forgetting effects or output style shifts," single-run reporting prevents the reader from judging whether these drops are statistically significant or within noise. The overall average stability is reassuring but does not fully resolve this concern.

- **Incomplete mitigation at late intervention steps.** At t_inter=32, RA's ASR under the anchoring attack remains 50.7% (LLaDA Instruct), 43.0% (LLaDA 1.5), and 79.3% (MMaDA). The paper acknowledges this inherent difficulty — generating safe responses from deeply contaminated states with many anchors is hard. While not a flaw in the method, this bounds the practical guarantees RA can provide.

- **No mechanistic analysis of the recovery behavior.** The paper evaluates RA purely through ASR and utility metrics. Analysis of how RA changes internal representations, refusal mechanisms, or attention patterns would strengthen the understanding of why the method works and when it might fail.

### Trivial

- **Notation inconsistency in Algorithm 1.** Line 5 uses `t_min` for the contamination step, but line 2 computes `t_inter` and Equation 7 uses `t_inter`. Line 5 should use `t_inter` to be consistent. This is a minor bug in the pseudocode.

## Nice-to-Haves

- Characterize the reward model's behavior: show RA results with at least one alternative reward model, and report correlation between reward scores and actual safety judgments on a held-out set.
- Report multiple-run statistics (mean ± std) for utility benchmarks to establish whether observed drops are within noise.
- Discuss the practical relevance of the t_inter=32 threat model — what level of attacker access would be needed to intervene that late in a real deployment.
- Test a reverse curriculum (hard-to-easy scheduling) as an ablation to fully isolate the learning dynamics.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"LLaMA" in table headers (harsh critic).** The parsed text renders "LLaDA" as "LLaMA" in some table headers (Tables 2 and 3). This is clearly a parser/OCR artifact; the body text consistently uses "LLaDA." The original submission does not have this issue. Removed.

- **"Harmful responses for injection — model-generated or fixed set?" (harsh critic).** The paper states that harmful responses are generated by a non-safety-aligned model and references Appendix D for details. The appendix is stripped by the parser, so this detail is not verifiable from the provided text. However, the paper does address this — the criticism about the attack being "influenced by the specific style of the unaligned model" is speculative and not anchored in any concrete problem with the paper's results. Removed as speculative.

- **"Missing GRPO hyperparameters" (harsh critic).** This falls under the rule: "REMOVE nitpicks about reproducibility such as undisclosed hyperparameters, trivial implementation details." The paper references Appendix D.4 for detailed implementations. Removed.

- **Strength finder: "Analysis of why standard alignment fails (Eq 5-6)" —** This is already captured under the defense motivation strength. The equations are a restatement of the core insight, not an independent strength. Merged into existing strength.

## Novel Insights

The paper's key insight — that MDLM safety alignment fails because training from fully masked starts creates no pressure to recover from contaminated intermediate states — is genuinely novel and well-articulated. The connection between Theorem 4.1 (lower bound on full denoising likelihood via first-step predictor) and the practical success of First-Step GCG is an elegant example of theory guiding attack design. The observation that training on contaminated states also improves robustness to conventional conversational jailbreaks (via a plausible "re-detection at later steps" mechanism) is an interesting and somewhat unexpected finding that may generalize beyond MDLMs.

## Suggestions

- The paper would benefit from a short discussion (or experiment) on reward model sensitivity. Even a single alternative reward model comparison would substantially strengthen confidence in RA's generality.
- Consider reporting greedy decoding results for the utility benchmarks alongside sampling results, to isolate whether drops come from output distribution shifts vs. capability loss.
- The linear scheduling ablation is convincing, but adding a short discussion of why a curriculum helps (beyond "harder states are harder") would add depth — e.g., is the benefit from avoiding reward hacking early in training, or from gradually expanding the model's recovery horizon?

## Score and Decision

**Calibration anchors used:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| NEMESIS Jailbreaking | 5kMwiMnUip | 1.40 | R1 | Far below — trivial attack paper with minimal evaluation |
| Playing Language Game | BeOEmnmyFu | 2.50 | R1 | Below — jailbreak method only, weak evaluation |
| Baseline Defenses (Jain et al.) | 0VZP2Dr9KX | 5.25 | R1 | Below — limited to one attack, incomplete analysis |
| RA-LLM Defense | V01FPV3SNY | 5.33 | R1 | Below — limited experiments (1 dataset, 2 models), weaker contribution |
| Cross-Modal Safety Transfer | 45rvZkJbuX | 6.50 | R2 | Below — related safety transfer but narrower scope |
| AutoDAN | 7Jwpw4qKkb | 7.00 | R2 | Below — strong attack paper but narrower evaluation |
| Catastrophic Jailbreak | r42tSSCHPh | 7.00 | R2 | Below — attack-focused, less comprehensive |
| Backtracking | Bo62NeU6VF | 8.00 | R1 | Slightly above — similar recovery-based defense paradigm, but this paper has more comprehensive evaluation; Backtracking has slightly higher conceptual novelty |
| Shallow Safety Alignment | 6Mxhg9PtDE | 9.50 | R1 | Above — more transformative contribution unifying multiple attack types, though less thorough experiments |

**Round 1 bracket:** 6.5–8.5. **Round 2 narrowed:** The paper is stronger than the 6.5–7.0 attack/defense papers in evaluation comprehensiveness and novelty, but not as transformative as the 9.50 "Shallow Safety Alignment" paper. It is comparable to "Backtracking" (8.00) in contribution level but has slightly more experimental breadth at the cost of slightly lower conceptual novelty. **Final score: 7.5.**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>