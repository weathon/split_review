Now I have all the information I need. Let me finalize my review.

**Round 1 Bracket:** Based on the bracketing search, this paper sits between the weak anchors (2.33–3.0) and the exceptional anchors (8.0+), placing it in the 4.5–6.5 range.

**Round 2 Narrowing:** The most directly comparable anchor is the ISE paper (6.0, accepted) — the exact baseline this paper improves upon. That paper was criticized for limited novelty but accepted. The current paper has stronger diagnosis, broader evaluation, but an unresolved confound. The "Can LLMs Separate Instructions?" paper (6.67, accepted) is a different contribution type (benchmark/analysis). The PFT paper (4.25, rejected) and Baseline Defenses paper (5.25, rejected) are weaker — the current paper substantially exceeds both in evaluation breadth and methodological grounding.

**Final Score: 5.5** — The paper is above the ICLR acceptance threshold but the confound weakness (multi-layer injection vs. parameter count) prevents it from being a stronger paper. Comparable to the ISE paper (6.0) but slightly lower due to the unresolved methodological confound.

Here is the final consolidated review:

## Summary
This paper proposes Augmented Intermediate Representations (AIR), a defense against indirect prompt injection attacks for LLMs. Instead of injecting instruction hierarchy (IH) signals only at the input layer (as in prior work with delimiters or Instructional Segment Embedding), AIR injects trainable, layer-specific IH embeddings at every decoder layer. Evaluated across 3 models, 2 training methods (SFT/DPO), and multiple attack types, AIR achieves 1.6× to 9.2× reduction in GCG attack success rate compared to prior IH methods, with minimal utility degradation.

## Strengths
- **Diagnostic evidence for multi-layer injection (Figure 3):** The paper measures cosine similarity between representations of tokens at different privilege levels across decoder layers, showing that input-only methods (Delim, ISE) lose separation in deeper layers while AIR maintains better separation. This provides concrete empirical grounding for the paper's core hypothesis that input-level IH signals degrade through the network — something no prior IH defense paper provides.

- **Consistent and substantial ASR reductions on gradient-based attacks (Table 1):** Across all 3 models and both training methods, AIR achieves the lowest ASR on GCG and Astra attacks by substantial margins. On Llama-3.2-3B with SFT, AIR=4.1% GCG ASR vs Delim=38% and ISE=48.1%. On Astra for Qwen-2.5-7B SFT, AIR achieves 2.4% vs ISE=39.2% and Delim=69.0%. The improvement is not cherry-picked but holds across all configurations.

- **Thorough evaluation scope:** The paper evaluates across 3 model families (3B, 7B, 8B), 2 training paradigms (SFT, DPO), 5 attack types (4 static, 2 gradient-based), and 2 evaluation frameworks (AlpacaFarm, SEP) — substantially more comprehensive than typical IH defense papers.

- **Precisely quantified overhead and honest framing:** Specific parameter counts (0.4M extra, 0.005% increase) and explicit acknowledgment of the architectural similarity to RoPE and positional embeddings. The paper frames its contribution honestly rather than overselling.

## Weaknesses

### Fatal
None.

### Major
- **Confounded comparison: multi-layer injection vs. additional parameters.** AIR adds ~0.4M IH-dedicated parameters (32 layers × 3 privilege levels × 4096 hidden size), while ISE adds only ~12K (at the input layer only) and Delimiters add even fewer (two new token embeddings). The paper attributes AIR's improvement to injecting IH signals at every layer, but the experiment does not isolate whether the improvement comes from multi-layer injection or simply from having more IH-dedicated parameters. A controlled ablation — e.g., adding the same total parameter count at the input layer only, or injecting AIR-like embeddings at a subset of layers — is needed to validate the central architectural claim. This does not invalidate the method (AIR clearly works better), but it weakens the paper's specific claim about *why* it works better.

### Minor
- **Asymmetric GCG optimization budgets:** SFT models use 50 GCG steps while DPO models use 200 steps, with no justification for this asymmetry. Since SFT models generally have higher ASR than DPO models, longer optimization for SFT models could change relative comparisons. This does not invalidate the headline results but warrants clarification.
- **SEP results show AIR-SFT sometimes underperforms "None" on utility (Figure 8):** The paper acknowledges this briefly but does not discuss why multi-layer injection might hurt utility in the SFT setting while helping in DPO. This asymmetry is interesting and merits analysis.

### Trivial
None.

## Nice-to-Haves
- Reporting statistical significance or variance for ASR numbers (Table 1 reports single values over 208 test instances — a few percentage points could be noise).
- Evaluating on multiple target phrases beyond the single "hacked!" string, which the defense is specifically trained to suppress.
- Testing transfer attacks from surrogate models (the threat model is white-box, but transfer robustness would strengthen claims about practical security).

## Removed Points
These points from the reviewers are flagged to be removed; treat with caution.

1. **"Figure 3 motivation is circular"** — The figure compares all three trained methods post-hoc, showing that input-only methods lose separation (Delim near-1.0 throughout, ISE rising from 0.55 to 0.92) while AIR maintains better separation (0.55 to 0.88). This is a valid diagnostic that supports the hypothesis, not circular reasoning. The criticism is too strict.

2. **"Utility contradiction"** — The critic claims AIR's win rates (85.4%, 91.9%, 87.1%) exceeding "None" (~80%) contradicts the "no significant degradation" claim. But the claim is conservative — AIR does not degrade utility significantly, and the worst case is a <2% drop for one configuration. That AIR sometimes surpasses None does not contradict the claim at all.

3. **"Marginal advantage on static attacks"** — The paper explicitly states that all three IH methods achieve "near-perfect protection" on static attacks. The paper's claimed improvement is specifically on gradient-based attacks (1.6×–9.2×), which is accurately framed throughout.

4. **Pure formatting/style nitpicks and parser artifacts** — The PDF parser introduced formatting issues that do not reflect the authors' submission.

5. **"Missing related work"** — Cannot be verified without external sources.

## Novel Insights
None beyond the paper's own contributions. The core insight — that IH signals should be injected at every layer, not just the input — is the paper's own novel contribution, and the reviews do not surface additional novel observations about it. The connection between multi-layer IH injection and the RoPE trajectory in positional embeddings is an observation the paper itself draws.

## Suggestions
1. **Add a controlled ablation** isolating the effect of multi-layer injection from parameter count: compare AIR (multi-layer, 0.4M params) against a version with a single large embedding table at the input layer matched to AIR's parameter count. If AIR still wins, the multi-layer thesis is strongly supported. If the high-capacity single-layer version matches AIR, the contribution reduces to "more parameters for IH helps."
2. **Add a partial-layer ablation:** inject AIR at varying numbers of layers (e.g., only first 8, only last 8, every other layer) to understand how many injection sites are sufficient and whether later-layer injection matters more than early.
3. **Clarify the "None" baselines:** Table 1's column headers are ambiguous — "None" appears under both model-level and method-level headers. Specify whether "None" means no adversarial training, no IH mechanism, or both. Figure 6's "None" also needs explicit definition.
4. **Justify or equalize the GCG optimization budget** between SFT (50 steps) and DPO (200 steps) models.
5. **Discuss the SFT vs. DPO utility asymmetry on SEP:** Why does multi-layer injection sometimes hurt SFT utility but never DPO utility? This could reveal interesting properties of the training paradigms.

## Calibration Anchors

| Path | Avg Human Score | Round | Comparison |
|------|----------------|-------|------------|
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/3MDmM0rMPQ.md | 3.00 | 1 | Weaker: limited-scope task-specific safety, rejected |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/MV5j4Qpq7N.md | 2.33 | 1 | Weaker: novel attack patterns defense, rejected |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/KyKTjRtyNG.md | 3.00 | 1 | Weaker: multi-round conversational jailbreaking, rejected |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/6Mxhg9PtDE.md | 9.50 | 1 | Much stronger: foundational insight about shallow alignment, accepted |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/5kMwiMnUip.md | 1.40 | 1 | Weaker: basic jailbreaking exploration, rejected |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/sjWG7B8dvt.md | 6.00 | 1 | **Directly comparable**: ISE paper (same topic, exact baseline). Accepted at 6.0 with concerns about novelty. Current paper has stronger diagnosis/broader evaluation but unresolved confound issue. Current paper slightly weaker overall. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/l3bUmPn6u5.md | 4.25 | 1 | Weaker: PFT paper, rejected. Narrower evaluation, less convincing results. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/2VmB01D9Ef.md | 4.25 | 1 | Weaker: AutoHijacker attack paper, rejected. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/iKgQOAtvsD.md | 5.75 | 1 | **Comparable but different domain**: jailbreak attack translation paper, rejected. Similar quality but different contribution type. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/0VZP2Dr9KX.md | 5.25 | 2 | Weaker: baseline defenses survey, rejected. Narrower evaluation, less novel contribution. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/V01FPV3SNY.md | 5.33 | 2 | Weaker: RA-LLM defense, rejected. Less comprehensive evaluation. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/yVVzaRE8Pi.md | 5.50 | 2 | **Comparable in score**: implicit reference jailbreak attack, rejected. Different contribution (attack vs defense). |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ikqcUzUogm.md | 4.75 | 2 | Weaker: rule-following benchmark, rejected. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/hXA8wqRdyV.md | 6.14 | 2 | Stronger: adaptive jailbreak attack paper, accepted. Very strong results across many models. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/e9yfCY7Q3U.md | 6.25 | 2 | Stronger: improved GCG techniques paper, accepted. More mature analysis of attack methods. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/sULAwlAWc1.md | 7.00 | 2 | Stronger: robust jailbreak prompt generation, accepted. More comprehensive attack evaluation. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/8EtSBX41mt.md | 6.67 | 2 | Stronger: SEP benchmark paper, accepted. More rigorous formalization. Different contribution type (benchmark vs defense). |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Y4aWwRh25b.md | 6.75 | 2 | Stronger: RAG data extraction paper, accepted. Stronger evaluation methodology. |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>