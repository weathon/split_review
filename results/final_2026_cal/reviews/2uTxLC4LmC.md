Now I have all the calibration I need. Let me write the final review.

**Round 1 bracket**: The paper is clearly stronger than the 3.0-3.5 anchors (CoT monitoring, LoRA safety alignment) and clearly less fundamental/transformative than the 8.0 anchors. Its closest topical matches sit at 4.5-6.5. Initial bracket: 5.0-7.5.

**Round 2 narrowing**: The most comparable papers are RECAP (6.5 avg, Reject) and SafeDPO (6.5 avg, Oral). Our paper has stronger empirical analysis of safety dynamics than RECAP, better cross-model evaluation than SafeDPO, and the weaknesses are manageable (evaluation validity concern is common in this field; the trigger pool concern is overstated by the reviewer). The paper is slightly stronger than the 5.0-5.3 anchors (ReasoningShield, SaFeR-VLM). Final score: **6.5**.

Here is the consolidated review:

---

## Summary

This paper identifies that chain-of-thought reasoning in Large Reasoning Models (LRMs) often contains harmful content even when final responses appear safe, and proposes **Intervened Preference Optimization (IPO)** to align reasoning-level safety. IPO first empirically characterizes safety dynamics in reasoning — discovering *safety triggers* (steps where safe continuation probability jumps to ~100%) and *compliance cues* (steps that strongly correlate with unsafe continuation, Pearson R=0.853). It then replaces compliance cues with safety triggers in unsafe trajectories to construct preference pairs, and applies DPO only from the divergence point. Experiments across DS-8B, DS-7B, and Qwen3-8B on JailbreakBench, StrongReject, and WildJailbreak show IPO achieves the lowest reasoning harmfulness across all three models (e.g., DS-8B 15.3% vs. best baseline 18.5%) while preserving or enhancing reasoning capability.

## Strengths

1. **Novel and well-supported empirical characterization of reasoning safety dynamics.** The paper systematically identifies safety triggers (Section 3.1, over 90% of safe trajectories contain CSR turning points at μ=0.9, K=15) and compliance cues (Section 3.2, Pearson R=0.853 with unsafe turning points), and demonstrates that replacing compliance cues with triggers corrects unsafe reasoning from 100% to ~15% harmful continuation (Figure 6). This goes beyond prior qualitative observations to provide a reproducible, automatic identification procedure.

2. **IPO is well-motivated by the analysis and demonstrably more efficient than RL-based process supervision.** The paper shows GRPO suffers from low rollout diversity (36.2% of prompts yield zero safe reasoning trajectories, Figure 4), while IPO's intervention-based approach requires at most 14 generations (~40 min training) versus GRPO's 40+ generations (~2 hr), yet achieves better reasoning safety (DS-8B reasoning avg: IPO 15.3% vs. GRPO 18.5%, Table 2).

3. **Consistent improvement across three LRMs and three safety benchmarks with preserved reasoning capability.** IPO achieves the lowest reasoning harmfulness on DS-8B (15.3%), DS-7B (18.4%), and Qwen3-8B (13.9%) while achieving the highest or tied-highest average reasoning capability (DS-8B 68.5%, DS-7B 71.5%). The method also generalizes across detectors (GPT-4o, DeepSeek-R1, DS-8B itself — Table 3), showing practical deployability.

4. **Targeted DPO from divergence point is clearly better than alternatives.** Ablation (Table 3) shows DPO on partial trajectories (divergence point onward) yields 10.9% harmfulness on StrongReject, substantially outperforming SFT (42.3%) and full-trajectory DPO (19.0%). The KL divergence plot (Figure 7) visually confirms concentration of supervision at safety-critical tokens.

## Weaknesses

### Major

1. **Reasoning safety evaluation lacks human validation.** The paper uses GPT-4o to assess both reasoning traces and responses for safety (Section 2.1), but does not validate that the evaluator correctly distinguishes between *genuinely unsafe reasoning* (endorsing harmful actions) and *safe reasoning that merely mentions harmful concepts in the process of rejecting them*. This is critical because the paper's core claim is that "reasoning safety is overlooked" and IPO fixes it — if the evaluator systematically over-flags benign references to harm as unsafe, both the problem statement and the reported gains could be inflated. The paper should provide human annotation subset, error analysis, or at minimum representative examples showing flagged reasoning traces with GPT-4o scores alongside human judgment. *(Verification: The paper states "assess both using GPT-4o as an automatic evaluator with established safety guidelines" on p.2 and defers details to Appendix A.1, which is stripped. No human validation is reported in the main text.)*

### Minor

2. **Trigger pool construction is from a narrow sample without systematic validation of generality.** The safety triggers and compliance cues are identified from only 30 JailbreakBench prompts (Section 3.1), and only six representative triggers are used for training (Section 4.1). While these triggers serve as template sentences for intervention rather than training data per se, the paper does not demonstrate that this small set covers the range of harmful intent categories or generalizes across attack styles. The concern is mitigated by the strong empirical results across multiple benchmarks (including WildJailbreak, which is more diverse), but a systematic analysis of trigger coverage would strengthen confidence.

3. **Abstract's "over 30% relative reduction" claim is ambiguously anchored.** The claim "outperforming SFT-based and RL-based baselines with a relative reduction of over 30% in harmfulness" (Abstract, p.1) is strictly true only for some baselines (e.g., 32% vs. STAR at 22.6% → IPO 15.3% on DS-8B reasoning avg) but not others (17% vs. GRPO at 18.5%). The phrasing could be read as claiming 30%+ reduction against the best baseline overall, which is unsupported. The conclusion (p.9) states this more carefully as "relative to leading baselines" but the abstract should be precise.

4. **RealSafe achieves lower response harmfulness on DS-8B and DS-7B, but this comparison is asymmetrically favorable to RealSafe.** RealSafe achieves 2.7% vs. IPO 6.9% response harm on DS-8B (Table 2), but at the cost of massive over-refusal (47.5% compliance vs. IPO's 80.0%). The paper acknowledges this ("over-conservative") but the claim that "prioritizing reasoning-level alignment naturally develops into safer responses" is weakly supported for these two models. On Qwen3-8B, IPO achieves the best response safety (8.4%), so this is a model-dependent claim.

### Trivial

5. The GRPO reward function `I[z is safe] - I[y is safe]` (Table 1) is presented without clear justification of its design rationale. While the results confirm it works, the reviewer's confusion about it penalizing safe responses is understandable — a brief explanation in the text would help.

## Nice-to-Haves

- Human validation of the reasoning safety evaluation metric (critical for trust in the core claim).
- Analysis of IPO failure cases: when does it still produce unsafe reasoning (e.g., DS-8B 23.4% on WildJailbreak), and are these due to trigger pool limitations, missed compliance cues, or distributional shift?
- Scalability demonstration on a larger model (e.g., 14B or 32B) in the main paper rather than deferred to appendix.

## Removed Points

- *Criticism about GPT-4o circularity (trigger pool identification via GPT-4o)*: The paper already addresses this with a thorough ablation (Section 4.3, Table 3) showing IPO is robust when GPT-4o is replaced by DeepSeek-R1 or DS-8B itself. The concern is valid in principle but the paper provided empirical evidence against it. Moved here to acknowledge the reviewer's valid point while noting it is addressed.

- *Criticism about "IPO only achieves best reasoning safety on DS-8B and DS-7B, but not Qwen3-8B"*: This is factually incorrect — IPO achieves 13.9% vs. GRPO 23.3% on Qwen3-8B reasoning average (Table 2), making it the best. The reviewer's text corrects itself mid-paragraph, indicating confusion. Removed as factually wrong.

- *Criticism about missing related works or appendix content*: Parser strips appendices; related work coverage in Section 5 is adequate for the main body.

## Novel Insights

None beyond the paper's own contributions. The key insight — that safety evolves through identifiable critical steps (safety triggers and compliance cues) which can be systematically intervened upon — is the paper's own novel contribution, not synthesized from reviewers.

## Suggestions

1. Provide a human-annotated subset (e.g., 100 samples per benchmark) of reasoning trace safety judgments to validate GPT-4o's evaluation accuracy, or at minimum show representative examples with scores from both GPT-4o and human annotators.
2. Precisely qualify the "over 30%" claim in the abstract to specify the baseline comparison (e.g., "over 30% relative reduction compared to SFT-based baselines").
3. Extend the trigger pool analysis to show coverage across harm categories (e.g., using a taxonomy) or demonstrate that the method's effectiveness is robust to which triggers are sampled.

## Score and Decision

**Round-1 bracket**: Based on comparison with weak anchors (CtvnVtWZvN: 3.0, kboK7ad4Cn: 3.33, ssbwLWPeSy: 3.33) and strong anchors (DM0Y0oL33T: 8.0, kkBOIsrCXh: 8.0), the paper sits well above weak and well below top-tier. Bracket: 5.0–7.5.

**Round-2 narrowing**: Compared to topical peers: RECAP (TSk3cIdIQK: 6.50 avg, Reject) addresses a related LRM safety problem with similar evaluation concerns but weaker theoretical grounding; SafeDPO (PJdw4VBsXD: 6.50 avg, Oral) has cleaner theory but does not address reasoning-level safety specifically; ReasoningShield (IAuGwtwuYX: 5.00 avg, Reject) tackles CoT moderation but is a different task; LCPO (8xSU8Oscvg: 5.00 avg, Poster) addresses length reduction rather than safety. Our paper is stronger than the 4.5–5.3 anchors and comparable to the 6.5 anchors, with a clear advantage in empirical analysis depth and task importance.

**Final score**: 6.5. The paper makes a genuine contribution — the empirical characterization of safety dynamics in LRM reasoning is novel, the IPO method is well-motivated and effective, and the evaluation is comprehensive across models and benchmarks. The main limitation (lack of human validation for the reasoning safety evaluator) is real but common in this fast-moving field and addressable. The paper deserves acceptance.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>