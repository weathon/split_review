Now I have a thorough understanding of the paper and the calibration landscape. Let me write the consolidated review.

**Round 1 bracket**: I found anchors at 2-3 (rejected/withdrawn papers with fundamental flaws), 4-5 (borderline papers with mixed reviews), and 8 (strong accept oral/poster). DefNTaxS is clearly not in the very weak or very strong bands. Initial bracket: **4–6**.

**Round 2 narrowing**: I examined papers at 4.67, 5.0, 5.33, 5.6, and 6.0. The closest analogues are DualPrompt (5.0, accepted poster) — a training-free CLIP prompt method with good ideas but limited scope — and BayesVLM (6.0, accepted poster) — a well-supported method with clean theory. DefNTaxS has broader evaluation than DualPrompt but more significant claim-overreach issues. It is weaker than BayesVLM. **Final placement: 5.0**.

Here is the consolidated review:

---

## Summary

DefNTaxS proposes a training-free framework that uses an LLM (GPT-4o-mini) to cluster dataset classes into meaningful subcategories, then integrates both class-level descriptors (following D-CLIP) and this taxonomic context into CLIP text prompts. The method is evaluated across seven standard zero-shot benchmarks (ImageNet, CUB, Pets, DTD, Food101, Places365, EuroSAT) using a ViT-B/32 backbone, achieving average gains of +5.5% over vanilla CLIP and +2.4% over D-CLIP at a total LLM API cost of $0.38.

## Strengths

1. **Broad and consistent empirical improvement.** DefNTaxS achieves the highest accuracy on 5 of 7 standard benchmarks (Table 1), with a particularly large gain on EuroSAT (+13.0% over CLIP, +9.86% over D-CLIP). The average improvement over D-CLIP (+2.44%) is meaningful across diverse domains including fine-grained birds, textures, pets, and satellite imagery.

2. **Extremely low cost and full automation.** The entire LLM text generation pipeline costs $0.38 (Section 4.2), the method requires no manual prompt engineering, no model retraining, and no additional data. This is a concrete practical advantage over manual-template methods like E-CLIP.

3. **Systematic ablation study.** Section 6 provides controlled ablations that probe the contributions of different components. Table 4 reports results over 5 runs with standard errors (commendable relative to the field standard). The comparison against k-means clustering (Table 5) cleanly validates the design choice of using LLMs for taxonomy generation.

## Weaknesses

### Major

1. **Incorrect factual claim about "six of seven" benchmarks.** The paper states "DefNTaxS achieving the highest accuracy across six of seven benchmarks" (Section 5), but Table 1 shows CHiLS achieves higher accuracy on Food101 (83.53 vs. 81.48) and Places365 (40.45 vs. 40.00). The correct count is 5 of 7. While the exceptions are visible in the table, the text misstates the results. This is a reporting integrity issue that must be corrected.

2. **Central claim ("taxonomic context is essential") is not fully supported by the evidence.** Table 4 shows that WaffleTaxS (which replaces subcategory labels with random characters while keeping descriptors) achieves comparable or slightly higher accuracy on ImageNet (63.24 vs. 62.96), CUB (53.65 vs. 53.59), and Places (40.05 vs. 39.34). On ImageNet and CUB the margins are within ~1 standard error, but the Places gap (~2.7 SEs) favors the random-token variant. The paper acknowledges this ("differentiation without semantic content can also improve performance") but the title and abstract frame taxonomic context as "inevitable" and "essential," which overstates what the evidence supports. The data show that additional differentiating tokens help — sometimes the semantically meaningful ones help more, sometimes random ones do. This weakens the headline claim.

3. **No confidence intervals for the main results (Table 1).** While the ablation section (Table 4) responsibly reports standard errors over 5 runs, the primary comparison table reports only point estimates. On datasets where the improvement over D-CLIP is small (ImageNet +0.48%, CUB +0.79%, Places +0.16%), it is unclear whether the gains are reliable. The presence of standard errors in the ablation section makes their absence in the flagship results conspicuous.

### Minor

1. **Single VLM backbone (ViT-B/32) and single LLM (GPT-4o-mini).** The paper claims DefNTaxS is a general principle, but all experiments use one CLIP variant and one LLM. Evaluation with larger CLIP models (e.g., ViT-L/14) or alternative VLMs (SigLIP, OpenCLIP) would strengthen the generality claim. The comparisons against baselines use the same backbone, so the numbers are internally fair, but the scope of the generality claim is limited.

2. **The ~20-class-per-subcategory heuristic (Section 3.3) is justified by an appendix that is not present.** The rule is central to Step 3 of the method and is described as based on "empirical analysis," but the full analysis is in the (stripped) appendix. As presented, it appears somewhat arbitrary.

3. **No analysis of LLM output quality or failure modes.** The paper treats the LLM as a black box and does not report how often it produces coherent vs. unusable subcategories, whether the refinement loop (splitting large groups) succeeds reliably, or what happens when the LLM generates poor groupings.

### Trivial

- The bold formatting in Table 1 is inconsistent: on Food, CHiLS (83.53) is correctly bolded as the highest value but DefNTaxS (81.48) is below it; on Places, neither CHiLS (40.45) nor WaffleCLIP+Conc. (40.22) is bolded but DefNTaxS (40.00) is bolded despite not being the highest. This appears to be a formatting error.

## Nice-to-Haves

- Run-to-run variance for the main Table 1 results (following the protocol already established in Table 4) would allow readers to assess statistical reliability of the small-margin gains.
- A control that replaces subcategory labels with semantically *incorrect* words (not just random characters) would more directly test whether the *semantic content* of the subcategory matters, beyond the WaffleTaxS comparison.
- A focused experiment on datasets or subsets with genuinely ambiguous class labels (matching the "boxer" / "crane" / "mouse" motivation) would bridge the gap between the motivating examples and the evaluation.

## Removed Points

These points were raised by the reviewers but are removed from the main assessment with justification:

- *Criticism about WaffleTaxS "replicating the improvement" being fatal* — Retained as Major #2 but downgraded from "the claim is invalidated" to "the claim is overstated." WaffleTaxS does not replicate the improvement on all datasets (DefNTaxS wins on 4/7 with meaningful margins on DTD and ESAT), so the core method still shows value; the issue is the framing, not the method itself.

- *Criticism about "small margins" on several datasets being within noise* — Retained as Major #3 about missing confidence intervals, but removed the implication that the gains are "unreliable." Without standard errors we simply cannot know; the paper should provide them. This is a missing-evidence concern, not a proven flaw.

- *Criticism about the paper not measuring how many ambiguous class labels exist in the benchmarks* — Removed. The paper motivates the problem with ambiguity examples but does not claim to count ambiguous labels. The evaluation demonstrates real improvements; the motivation simply frames why the problem matters. This is standard practice.

- *Criticism about comparison with D-CLIP being "fair in principle" but then raising concerns about noise* — Merged into Major #3 (missing confidence intervals). Kept the substance, removed the framing that implies unfairness.

- *Criticism about Table 1 "Mean" column including ImageNetV2 giving "double weight" to ImageNet* — Removed. This is a standard reporting choice; INV2 is a robustness check, and averaging it with the main benchmarks is not unusual.

- *Criticism about the method not analyzing whether improvement is "additive or synergistic" with D-CLIP* — Removed as scope creep. The paper compares against D-CLIP; a 2×2 ablation would be interesting future work but is not required.

- *Criticism about Step 3 refinement heuristic being "arbitrary"* — Retained as Minor #2, noting the missing appendix, not as a weakness about the heuristic itself being wrong.

- *Criticism about cost variance and non-determinism* — Removed. $0.38 total is trivially low; non-determinism of LLM calls is handled by the loop structure described in the method.

- *Strength Finder claim about "SOTA across six of seven"* — Repaired to "highest accuracy on 5 of 7 standard benchmarks" in Strengths.

- *Strength Finder strength about "ablation isolating the contribution of taxonomic context from descriptors"* — Retained but weakened: the ablation does isolate components, but the WaffleTaxS results partially undermine the interpretation. The strength is that the authors ran the control, not that the control validates their claim.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between the paper's strong framing ("essential", "inevitable") and the more nuanced evidence (random tokens help too, the "six of seven" claim is off by one). This tension is the central issue the authors need to address.

## Suggestions

1. **Fix the factual error**: change "six of seven" to "five of seven" (or "six of seven, with DefNTaxS first or second on all") and explicitly discuss where CHiLS outperforms.
2. **Tone down the central claim**: Frame DefNTaxS as a method that *benefits* from taxonomic context rather than one for which context is *essential* or *inevitable*. The data support the former, not the latter.
3. **Add standard errors to Table 1** following the protocol already established for Table 4.
4. **Add at least one additional VLM backbone** (e.g., ViT-L/14 or SigLIP) to demonstrate generality.
5. **Consider an additional control** replacing the subcategory label with a semantically *unrelated* word to test whether the *semantic relevance* of the subcategory matters beyond mere differentiation tokens.

## Score and Decision

Round 1 bracket: The paper clearly does not belong with the 2-3 anchors (papers with fundamental flaws and reject decisions) or the 8.0 anchors (strong accept oral/poster). Initial bracket: **4.0–6.0**.

Round 2 narrowing: Compared against five anchors from the 4.5–6.0 range:
- **DualPrompt (5.0, accepted poster)**: Training-free CLIP method with a simpler evaluation (2 datasets). DefNTaxS has stronger evaluation breadth but more significant overclaiming. **Comparable overall.**
- **Free-Grained Hierarchical Recognition (5.0, withdrawn)**: Strongly split reviews (2,4,8,6). DefNTaxS has clearer contributions and better evidence. **Slightly stronger.**
- **CDantiHalP (5.33, rejected)**: Good method but rejected due to scope and methodology concerns. DefNTaxS has similar patterns. **Comparable.**
- **LVLM Annotation (4.67, rejected)**: Weaker empirical story. **DefNTaxS is stronger.**
- **BayesVLM (6.0, accepted poster)**: Clean mathematical contribution and solid evaluation. DefNTaxS has weaker claim support. **DefNTaxS is weaker.**

The paper has clear merit (clean method, broad evaluation, low cost) but its central claim is overreaching and it contains a factual reporting error. Positioned relative to the anchors, the appropriate score is **5.0** — borderline accept territory where the authors can address the concerns through major revision.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>