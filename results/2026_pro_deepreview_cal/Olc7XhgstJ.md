Now I have sufficient calibration data. Let me compile the final consolidated review.

---

## Summary

This paper introduces **Steady Thought (ST)**, a thought-level preference optimization framework that mitigates "under-thinking" in Large Reasoning Models — the tendency of models to prematurely abandon promising reasoning trajectories by switching thoughts too frequently. ST operates in three stages: (1) entropy-based thought segmentation to split responses into thought units, (2) thought completion via logit suppression to generate coherent completions from each thought, and (3) fine-grained preference optimization (STPO, a length-normalized SimPO variant) that treats the correct completion as chosen and the original wasteful switching as rejected. Experiments across three model scales and four benchmarks show consistent accuracy improvements (up to +5.3%) with substantial token reductions (17–39%), including on out-of-distribution code tasks.

## Strengths

- **Dual-axis improvement validated across diverse settings**: Table 1 demonstrates that ST simultaneously improves accuracy and reduces token counts across three model families (1.5B, 8B, 14B) and four benchmarks. For example, ST boosts Qwen3-8B's overall accuracy by 3.12% while cutting token usage by 25.5%, and generalizes to the OOD LiveCode benchmark (+5.3% accuracy, −19.0% tokens). This consistent pattern across architectures and task difficulties is convincing evidence of the method's robustness.

- **STPO is necessary — simpler training methods fall short**: The ablation in Table 4 is instructive: SFT on the chosen responses achieves length reduction but sacrifices accuracy (80.4% vs 82.2% base on MATH-500), while standard DPO barely improves over the base model (82.6%, 4273 tokens). STPO achieves both higher accuracy (84.4%) and lower token count (2809), demonstrating that thought-level, length-normalized preference optimization is essential to the gains, not an incidental design choice.

- **Multi-metric behavioral evidence that reasoning patterns change**: Figure 2 shows that ST consistently reduces average response length and average number of thoughts while increasing the proportion of the final thought (e.g., from 58.8% to 70.0% for Qwen3-8B on MATH-500). Table 2 shows a substantial drop in the proportion of correct intermediate thoughts (PCT) after ST training. Together with the accuracy gains, these metrics converge on the interpretation that the model commits more deeply to promising thoughts rather than switching prematurely.

- **Well-tuned pipeline with empirical grounding**: The entropy threshold sensitivity analysis (Table 3) shows that segmentation granularity meaningfully affects downstream performance, and the authors select an optimal threshold (3.0) based on cross-validation rather than an arbitrary default. This attention to a critical hyperparameter strengthens confidence in the pipeline design.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The PCT metric conflates natural progressive reasoning with wasteful switching**: Section 4.4.2 defines an "Invalid Switch" as any correct intermediate thought that is subsequently abandoned, then equates the number of correct intermediate thoughts with the number of Invalid Switches. By this definition the equation is tautological, but the interpretation is overclaimed: a coherent multi-step chain that naturally builds through several correct intermediate steps would register a high PCT even if no wasteful switching occurred. The metric therefore does not cleanly isolate under-thinking from ordinary progressive reasoning. The paper's convergence of multiple other metrics (token reduction, fewer thoughts, higher last-thought proportion) partially mitigates this concern, but the claim in the text that decreasing PCT "precisely demonstrates that the model's decision-making has become more precise" is too strong. A more direct measure — such as counting switches that occur *after* a thought sufficient to reach the correct answer has already been generated — would provide cleaner evidence.

- **Baseline comparison is limited to inference-time interventions**: The paper compares against NoThink, NOWAIT, and SEAL, which are all test-time suppression methods for under-thinking. This is defensible since the paper explicitly positions these as the existing approaches for under-thinking (Section 5.1 distinguishes training methods for *over-thinking* from these inference-time methods for *under-thinking*). However, the paper would be strengthened by including at least one training-based competitor that targets reasoning efficiency — e.g., an RL variant with length penalties or a supervised method for concise reasoning — to contextualize ST's gains more broadly within the training-based landscape.

### Trivial

- The thought segmentation relies on the delimiter `.\n\n` as a "common logical delimiter" (Section 3.1), but no justification is given for its reliability across the evaluated models (Qwen3-8B vs. DeepSeek-distilled models may format reasoning differently). A brief sensitivity note would improve reproducibility.

- Section 3.2 mentions suppressing logits of trigger words like "wait" and "alternatively" but does not provide the complete list, which matters for reproducing the thought completion stage.

- The NOWAIT baseline exhibits catastrophic behavior on Qwen3-8B (MATH-500 accuracy drops from 91.4% to 61.0% while tokens more than double). The paper reports this result without discussion, leaving readers to wonder whether the baseline is misconfigured or whether this reflects a fundamental brittleness of token-level suppression that ST avoids — either way, the silence is a missed opportunity to strengthen the narrative.

## Nice-to-Haves

- Positioning STPO more explicitly against existing step-level DPO variants (Lu et al., 2024; Lai et al., 2024) would help readers understand the specific novelty in data construction and conditioning relative to prior fine-grained preference optimization work.
- Acknowledging the computational overhead of the thought-completion stage (generating completions for every segmented thought) and its scalability to larger models — currently deferred to Appendix E — would benefit the main paper's self-containedness.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Insufficient baseline comparisons — training-based approaches like RL with length penalties should be included."* → **Removed.** The training methods cited by the harsh critic (L1, fine-tuning on concise CoT, dynamic switching) are explicitly discussed in Section 5.1 as addressing *over-thinking*, not *under-thinking*. The paper's baselines (NoThink, NOWAIT, SEAL) are correctly identified as the state-of-the-art for under-thinking. This is a scope mismatch. I retained a weakened version as a minor point since one training-based efficiency baseline would still add value.

- *"Bradley-Terry framing is not carried through to the actual optimization."* → **Removed.** The paper uses Bradley-Terry to motivate the preference formulation conceptually; deriving the actual loss from SimPO with length normalization is standard practice in the preference optimization literature and does not constitute a weakness.

- *"Abstract phrasing 'up to 39.3% output length reduction' may give an inflated impression."* → **Removed.** "Up to" is standard and accurate phrasing for reporting the maximum observed gain; no reader would reasonably mistake this for an average.

- *"Figure 1 y-axis meaning could be clarified."* → **Removed.** The figure caption explains the axis adequately; this is a presentation nitpick without substantive relevance.

- *"Figure 2 sweeping claim about final-thought proportion contradicted by anomaly."* → **Removed.** The paper explicitly acknowledges and discusses the AIME2024 anomaly for DeepSeek-R1-Distill-Qwen-1.5B in the same paragraph, noting that smaller models on high-difficulty problems may increase thought frequency to find optimal solutions. The claim is appropriately qualified.

- *"The method's sensitivity to entropy threshold and heuristic segmentation should be acknowledged as limitations."* → **Removed.** The paper devotes an entire subsection (4.4.3) to analyzing entropy threshold sensitivity and an ablation table (Table 3) to the segmentation parameter; this is far more than typical for such a design choice. Similarly, the thought completion overhead is acknowledged via a pointer to Appendix E. Demanding a "limitations" section is a generic one-size-fits-all criticism.

- *"Missing related work on step-level DPO variants."* → **Removed from weaknesses; moved to Nice-to-Haves.** The paper does cite and discuss these methods (Lu et al., 2024; Lai et al., 2024) in Section 5.2. A sharper positioning would be nice but is not a genuine gap.

- *"NOWAIT erratic behavior is a sign of fundamental brittleness" as a fatal claim.* → **Removed as a strong claim.** The paper reports the numbers honestly. The harsh critic's implication that this might indicate data issues is speculative. I retained only a minor note that discussing the behavior would improve the paper.

## Novel Insights

The idea of treating under-thinking as a *local* preference problem — teaching the model to commit at the specific decision point where a promising thought has been identified, rather than applying global suppression — is genuinely insightful. The thought-completion stage is an elegant data-construction trick: by forcing the model to complete from each intermediate thought without switching, the framework automatically generates "what could have been" chosen trajectories without human annotation. This self-supervised construction of preference pairs at thought boundaries is a practical approach that could generalize to other reasoning pathologies beyond under-thinking.

## Suggestions

- Replace or supplement the PCT metric with a more direct measure: count how many times the model generates a thought that *could* lead to the correct answer (verified by completion) and then switches away from it. This would directly quantify the phenomenon ST aims to suppress without the conflation with natural progressive reasoning.
- Add a discussion of the NOWAIT catastrophic failure on Qwen3-8B — even a brief paragraph explaining the likely cause (e.g., token-level suppression interacts poorly with the model's training distribution) would turn a puzzling data point into supporting evidence for ST's thought-level approach.
- Provide the full list of trigger words used in thought completion and briefly justify the delimiter choice across models, ideally with a one-sentence note on observed sensitivity.

---

## Anchor Comparison Summary

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| IUPO (`bGGMLWAGMc`) | 5.50 | R1 | ST has stronger motivation, broader evaluation, and dual-axis (accuracy+efficiency) gains vs. IUPO's incremental DPO variant |
| Skeleton-of-Thought (`mqVgBbNCm9`) | 5.67 | R2 | ST has more principled methodology, stronger empirical results, and addresses a more fundamental problem |
| TPO (`O0sQ9CPzai`) | 6.33 | R1/R2 | Closest comparator — both are fine-grained preference optimization for reasoning. ST has broader eval (3 model families, 4 datasets, OOD test) and dual-axis gains; TPO has more novel loss formulation |
| Overthinking the Truth (`Tigr1kMDZy`) | 7.33 | R2 | Strong mechanistic analysis paper with clear novelty. ST is a training method with a different contribution type; ST is slightly below in novelty but comparable in execution quality |
| SPA (`BPgK5XW1Nb`) | 8.67 | R1 | Top-tier alignment paper with exceptional results and presentation. ST is clearly below this level |

**Round-1 bracket:** 5.5–7.5. **Round-2 narrowing:** anchors at 5.67, 6.33, and 7.33 place ST between TPO (6.33) and Overthinking the Truth (7.33). ST is clearly stronger than TPO (broader evaluation, dual-axis gains, better problem motivation) but lacks the mechanistic novelty of Overthinking the Truth. Final placement: **6.5**, a solid accept with addressable minor concerns.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>