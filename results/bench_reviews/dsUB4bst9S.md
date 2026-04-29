## Summary

This paper studies how small decoder-only transformers trained from scratch learn arithmetic under a next-token objective, with emphasis on data formatting, sampling, scratchpad/CoT-style supervision, text–arithmetic mixtures, scaling, pretraining, and length generalization. Its main empirical message is that ordinary left-to-right arithmetic strings are a poor training format, while reversed outputs and scratchpad-style decompositions can dramatically improve in-distribution arithmetic accuracy and reduce the number of distinct examples needed. The paper is broad and useful, but several headline interpretations are stronger than what the experiments cleanly establish.

## Strengths

- **The paper provides a broad, controlled empirical study of arithmetic data formats in small transformers.** The setup is clearly specified: NanoGPT with 10.6M parameters, decoder-only architecture, character-level tokenization unless otherwise stated, and next-token prediction from random initialization (lines 68–75). The paper compares plain, reverse, simplified scratchpad, and detailed scratchpad formats with concrete examples (lines 81–136), which makes the experimental factors unusually transparent.

- **The format comparisons reveal strong and practically relevant effects.** For 3-digit addition, the paper reports that plain formatting plateaus around 85% while reverse formatting reaches near/perfect accuracy after a sharp transition (lines 162–190). Even though the reverse comparison is confounded by delimiters, the empirical observation that output format strongly affects learnability is still valuable.

- **The scratchpad experiments are informative, especially because they show that intermediate-step design matters.** The paper reports that simplified scratchpad reaches 100% accuracy with about 2,000 addition samples and detailed scratchpad with about 1,000 samples (lines 279–289). The subtraction comparison between two detailed scratchpad designs is particularly useful: Version 2 performs worse because it requires an operand-comparison step, and the authors analyze that many errors come from misidentifying which operand is larger (lines 382–390).

- **The paper goes beyond headline accuracy with several diagnostic experiments.** These include hiding operands and digit positions (lines 216–268), noisy intermediate scratchpads (lines 393–408), perturbing autoregressive output prefixes (lines 410–440), mixing Shakespeare text with arithmetic (lines 685–722), GPT-2/GPT-3 scaling and tokenization experiments (lines 727–818), and token-cost analysis (lines 822–849).

- **The length-generalization section is a major strength.** The paper directly tests whether high in-distribution arithmetic accuracy implies algorithmic generalization, and finds that it does not: models trained on 1- and 3-digit additions fail on 2- and 4-digit additions, and models trained up to 7 digits fail on 8 digits (lines 853–869). The detailed failure cases in Figure 18/lines 870–1015 are especially valuable because they show failures even when much of the scratchpad is supplied.

- **The limitations and conclusion are more candid than many papers in this area.** The authors explicitly state that the model “learn[s] arithmetic not as a flexible algorithm, but more as a mapping function constrained to trained digit lengths” (line 34), and the conclusion acknowledges that scratchpad methods are not necessarily token-efficient and that length generalization remains difficult (lines 1029–1033).

## Weaknesses

### Fatal

None.

### Major

- **The central “reverse vs. plain” result is confounded by multiple formatting changes, not just output reversal.** The paper explicitly states that reverse examples are wrapped with `$` delimiters, while the plain baseline is kept in the original unpadded, undelimited format: “we wrap each data sample in the reverse format with the `$` symbol … We originally observed improved performance in both the plain and reverse formats when the operands and outputs were zero-padded … While we maintain the original plain format without padding as a baseline … we incorporate the `$`-encapsulation in our modified reverse format” (line 136). This means the headline comparison changes output order, boundary signaling, and possibly output-length ambiguity at the same time. The evidence still supports that formatting matters, but it does not cleanly isolate reversal as the cause of the phase transition.

- **The paper repeatedly frames scratchpad/CoT as improving “sample complexity” without sufficiently foregrounding the much larger token budget.** The authors do acknowledge this later: Table 10 reports 13 tokens for plain, 15 for reverse, 64 for simplified scratchpad, and 281 for detailed scratchpad per 3-digit addition example (lines 831–849), and the text states that detailed scratchpad is not necessarily token-efficient (lines 289 and 831–833). However, the abstract and earlier sections still claim that CoT-style data “significantly and simultaneously improves accuracy, sample complexity, and convergence speed” (lines 4–6, 24–26), and Figure 1/Section 6 emphasize fewer examples. A more precise claim would be that scratchpads reduce the number of distinct problem instances needed, while often increasing supervised token exposure and inference/training cost substantially.

- **The low-rank matrix completion explanation is overclaimed relative to the actual autoregressive digit-generation task.** The paper states that “learning an addition map on \(n\) digits from random samples can be considered as completing a rank-2 matrix” and that this “offers a compelling explanation” for the observed phase transition (lines 200–215). But the LRMC formulation is a scalar table \(M_{ij}=i+j\), while the trained model emits token sequences autoregressively, with reversed or unreversed digits, delimiters, variable lengths, carries, and next-token loss. The paper itself later shows that NanoGPT behaves differently from LRMC when rows/columns or digits are excluded (lines 216–268), which is interesting but also weakens LRMC as a mechanistic explanation. The LRMC section is best viewed as an analogy or suggestive comparison, not an equivalence or explanation of the transformer mechanism.

- **The strongest “perfect learning” and “phase transition” claims would be more convincing with exhaustive or replicated evaluation.** The paper often uses randomly sampled test sets, e.g. the test dataset is “randomly sampling pairs of operands not included in” training (line 74), hiding-number experiments evaluate over 10,000 random examples (line 218), and length-generalization tests use 100 random samples (line 856). For 2-digit and 3-digit addition/subtraction, exhaustive evaluation is feasible, and phase-transition curves would benefit from multiple seeds and uncertainty bands. This does not invalidate the broad trends, but it weakens near-absolute wording such as “learns addition perfectly” and “transition from 0 to 100%.”

### Minor

- **Some broader arithmetic claims are less mature than the addition results.** The paper extends to subtraction, multiplication, sine, and square root (lines 533–651), but multiplication is only up to 2 digits (line 549), and sine/square-root results are evaluated on truncated decimal strings with tolerance thresholds (lines 551–555). The paper itself notes that sine/square-root scratchpads involve exponentiation or division that may not be simpler than the original operation (lines 551–560), so claims about “arithmetic operations beyond addition” should be framed more cautiously.

- **The square-root scratchpad example appears internally inconsistent.** For `sqrt(2.7174)`, the scratchpad converges to \(x_4=1.6484\), but the final answer shown is `0.6484` (lines 616–629). Since the defined square-root output format is a full decimal value (lines 553–555), this example needs correction or explanation.

- **There is an inconsistency between the Figure 11 caption and main-text interpretation for multiplication.** The caption says “reverse always produces improved sample complexity and performance for all operations” (lines 637–646), while the main text says “reverse is not particularly effective in multiplication” (lines 650–651). This should be reconciled.

- **Some few-shot prompting effects may be better interpreted as distribution matching rather than task induction.** In the joint arithmetic experiments, the model is trained on randomized concatenations of different tasks, and the paper itself hypothesizes that few-shot prompting works because training often contains one task directly following another (lines 656–660). This is a valid phenomenon, but the framing should distinguish in-context task induction from matching the training stream format.

- **The GPT-2/GPT-3 scaling and pretraining comparisons are suggestive but not clean scaling evidence.** The paper changes architecture scale, tokenizer, pretraining status, and loss setup across settings (lines 727–751). The authors note some of these differences, especially for GPT-3 where only completions generate loss and only 1,000 examples are used (lines 749–751), but conclusions about pretraining/scale should remain cautious.

- **The token-efficiency section contains a cost-model overstatement.** The paper says “the cost of a single forward pass is cubic in the number of tokens” (line 833). For standard transformer attention, the dominant sequence-length dependence is typically quadratic per layer, not cubic. This matters because the section is specifically about training and inference cost.

- **Generated scratchpads are not analyzed enough.** For noisy intermediate steps, the paper concludes that with enough data the model may “disregard” noisy intermediate steps (line 408). That is plausible, but the paper mostly evaluates final answers; analyzing whether generated scratchpads are themselves correct or causally used would strengthen the claim.

### Trivial

- **Terminology in the token analysis should be cleaned up.** The paper calls the multiplied token count “unique tokens” while explicitly acknowledging that this is not uniqueness across samples (lines 824–831). This is not a major issue, but renaming it to “token instances” or “total training tokens” would avoid confusion.

## Nice-to-Haves

- Add delimiter/padding-controlled ablations: plain with delimiters, plain with padding, reverse without delimiters, fixed-length outputs, and matched tokenization.
- Add token- and compute-matched scratchpad comparisons, e.g. train plain/reverse on enough independently sampled examples to match total token budget or FLOPs.
- Report exhaustive evaluation for 2- and 3-digit arithmetic, and multiple random seeds for phase-transition curves.
- Plot error rates by output position, carry pattern, operand length, and digit position to better distinguish local digit-wise learning from memorization or coverage.
- Analyze generated scratchpads directly: intermediate-step correctness, whether final answers are correct when scratchpads are wrong, and whether forcing correct scratchpads changes final accuracy.
- Replace or substantially weaken the LRMC framing with a token-level analysis of digit functions, carries, boundary tokens, and autoregressive dependence.
- Clarify when the paper is studying in-distribution scaling to longer trained lengths versus true length extrapolation to unseen lengths.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Removed/qualified strength: “reversing only the output order produces the phase transition.”** The paper does not only reverse the output: it also adds `$` delimiters to the reverse format while leaving the plain baseline undelimited and unpadded (line 136). The valid strength is that formatting strongly affects performance, not that reversal alone has been isolated.

- **Removed/qualified strength: “the LRMC section gives a useful mechanistic/theoretical explanation.”** The rank-2 scalar table observation is mathematically correct, but it does not model the autoregressive token-level learning problem. It should be treated as an analogy rather than a strong mechanistic explanation.

- **Removed generic strengths about the problem being important.** The importance of arithmetic learning and CoT-style supervision is broadly true, but generic importance claims do not by themselves support the paper’s contribution. The retained strengths focus on concrete experiments and findings.

- **Removed pure formatting/style concerns.** Any issues arising from extracted-PDF artifacts, line breaks, minor punctuation, or parser oddities should not affect evaluation.

- **Removed requests for missing appendix/proofs/references.** The review should not penalize missing appendix material or references, since those may be absent due to extraction.

## Novel Insights

The most useful synthesis is that the paper’s best contribution is empirical rather than theoretical: it convincingly shows that next-token arithmetic learning is highly sensitive to target format, intermediate supervision, and training-stream structure, but it does not yet cleanly identify the causal mechanism behind the strongest effects. In particular, the same evidence that makes the paper interesting—delimiters, reversal, scratchpad verbosity, structured sampling, concatenated task streams—also makes causal interpretation difficult. The negative length-generalization results are especially important because they prevent the in-distribution accuracy gains from being mistaken for learning a general arithmetic algorithm.

## Suggestions

- Re-run the core addition experiment with a full factorial formatting ablation: output order × delimiters × padding/fixed length × balanced sampling.
- Report both example efficiency and token/FLOP efficiency in every headline scratchpad result, not only in a late separate section.
- Replace “learns perfectly” with “achieves 100% on the sampled/exhaustive test set,” and use exhaustive evaluation where feasible.
- Recast the LRMC section as a motivating analogy unless a token-level model of carries and autoregressive generation is developed.
- For scratchpad methods, evaluate intermediate-step correctness and causal dependence on the scratchpad, not just final-answer accuracy.
- Tighten claims for sine/square root and other non-integer tasks, where the decompositions are not necessarily simpler than the original function.
- Correct the square-root example and reconcile the multiplication caption/text inconsistency.

## Score and Decision

**Overall assessment:** This is a useful and ambitious empirical paper with substantial experiments and several genuinely informative diagnostics. Its originality is moderate-to-good: many ingredients are known, but the systematic controlled study in small randomly initialized transformers is valuable. The research question is important, and the empirical contribution has community value. However, the main claims are not as cleanly supported as the paper suggests: the reverse-format result is confounded by delimiters/padding, scratchpad sample-efficiency claims are not consistently token/compute-normalized, and the LRMC explanation overreaches. The writing is generally clear, and the limitations are unusually candid, but the causal interpretation needs tightening.

**Calibration anchors retrieved and comparison:**

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eIgGesYKLG.md` — Avg 6.50, Accept. Stronger than this paper on length generalization because it achieves 2–3× extrapolation and includes targeted scratchpad/position-coupling methods; the current paper is broader but less conclusive mechanistically.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZMuPAOY8Oz.md` — Avg 4.00, Reject. Similar topic on arithmetic formatting/positional effects, but reviewers found cohesion and mechanism weaker; the current paper is more comprehensive and better substantiated, so it should score higher.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zpENPcQSj1.md` — Avg 6.33, Accept. Stronger theoretical angle on CoT and length generalization; current paper has broader experiments but weaker theory.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NjNGlPh8Wh.md` — Avg 7.50, Accept. A stronger theoretical scratchpad/CoT paper; current paper does not reach this level of formal contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/30oIfmrcFO.md` — Avg 6.25, Accept. Comparable in transformer arithmetic/CoT motivation, but current paper has more breadth and more confounds.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/v3DwQlyGbv.md` — Avg 2.33, Reject. Much weaker evidence and ablation structure than the current paper; current paper is far above this low anchor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LojXXo2xaf.md` — Avg 6.00, Reject. Similar synthetic arithmetic-training theme; current paper is more diagnostic but still has overclaiming issues.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/OW5Gf4cse1.md` — Avg 3.00, Reject. Lower-quality small-transformer math/task-complexity work; current paper is clearly stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/R6klub5OXr.md` — Avg 5.25, Reject. Similar quality pattern: extensive empirical work but confounded comparisons and broad claims; current paper is close but somewhat more valuable topically.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/55EO8gSCBT.md` — Avg 5.50, Reject. Similar broad empirical design paper with useful diagnostics but inconclusive conclusions; this is one of the closest calibration anchors.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Ok7ZH2Cyd7.md` — Avg 4.20, Reject. Similar concerns about controlled comparisons, but current paper’s experiments and diagnostics are stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GqI4fTVUXC.md` — Avg 6.00, Reject. Similar theory–practice disconnect: useful empirical probing but theory not fully explanatory; current paper is around this range but with more central confounds.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/icTZCUbtD6.md` — Avg 6.20, Accept. Broad empirical toolkit with limited conclusions; current paper is somewhat below due to confounded headline results.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/4hp2bVdaHU.md` — Avg 3.50, Reject. Weaker validation/utility than the current paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/2edigk8yoU.md` — Avg 6.50, Accept. Stronger because it addresses length generalization constructively; current paper mostly documents failure.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/qYb0CANLGC.md` — Avg 6.00, Reject. Theoretical CoT work with mixed reception; current paper has stronger experiments but weaker formalism.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0sbIEkIutN.md` — Avg 5.50, Reject. Similar arithmetic/length-generalization area and borderline quality; current paper is comparable.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/oTl1ABwM4n.md` — Avg 4.25, Reject. Weaker than current paper in evidence and contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1Xg4JPPxJ0.md` — Avg 6.00, Accept. Related compositional reasoning/CoT work; current paper is below due to causal confounds.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/tYVmxoRps3.md` — Avg 4.00, Reject. Similar concerns about input/output formatting controls; current paper is stronger but shares this central issue.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/38hLpTVpe7.md` — Avg 4.00, Reject. Less compelling motivation/interpretation than the current paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/wabp68RoSP.md` — Avg 3.75, Reject. Weaker evidence and cost analysis than the current paper.

Relative to these anchors, the paper is clearly above the low-scoring arithmetic/CoT papers because it has many concrete experiments and useful diagnostics. It is below the stronger accepted arithmetic/CoT/length-generalization papers because its headline causal claims are confounded and its theory is not well matched to the actual task. The closest anchors are the 5.25–5.50 empirical papers with useful breadth but overclaiming and confounded conclusions. I therefore assign a **5.5**: borderline, leaning reject unless the authors substantially narrow claims or add the key controls.

MY FINAL SCORE: <pineapple>5.5</pineapple>  
MY FINAL DECISION: <orange>Reject</orange>