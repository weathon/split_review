Now I have a thorough understanding of the paper and can verify claims against the actual content. Let me produce the consolidated review.

## Summary

This paper proposes IRIS (Intrinsic Reward Image Synthesis), the first RL-based fine-tuning framework for autoregressive text-to-image models that uses negative self-certainty (NSC = -KL(U∥π_θ)) as an intrinsic reward, requiring neither human labels nor external verifier models. The authors observe that self-certainty behaves differently in text reasoning (increases with training) vs. T2I generation (decreases), and leverage this by minimizing self-certainty during RL fine-tuning with GRPO. Evaluated on Janus-Pro (1B and 7B) across GenEval, T2I-CompBench, and WISE, IRIS achieves results competitive with the external-reward baseline T2I-R1 without using any external supervision.

## Strengths

1. **First intrinsic-reward framework for autoregressive T2I without external supervision.** IRIS shows that an RL-based intrinsic signal (negative self-certainty) can meaningfully improve T2I generation quality. Table 1 demonstrates that on GenEval, T2I-CompBench, and WISE, IRIS with no external rewards achieves performance within 1–4% of T2I-R1 (which uses HPSv2, DINO, GIT, and ORM rewards). This is a genuinely novel and potentially impactful result — showing that token-level uncertainty alone can substitute for complex external verifier ensembles.

2. **Systematic ablation study covering key design dimensions.** The paper ablates direction of self-certainty optimization (minimize vs. maximize for text and image tokens separately, Figures 6–7), forward vs. backward KL formulation (Figure 8), and RL vs. direct gradient optimization (Figure 9). These ablations consistently confirm that minimizing self-certainty on both text and image tokens with forward KL and GRPO yields the best performance, providing empirical grounding for the method's design choices.

3. **Honest correction of a baseline implementation issue.** Section 4.1 identifies and corrects a chat-template mismatch in the official T2I-R1 codebase (using Janus templates for Janus-Pro models), ensuring fair comparison.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaiming: the paper asserts results are "superior to" external rewards, but the data consistently show IRIS is slightly worse across all three benchmarks.** In the abstract and contributions, the paper states performance is "competitive with or superior to external rewards." However, Table 1 shows IRIS is numerically *lower* on every overall benchmark metric:
   - GenEval: 0.72 vs. 0.75 (1B), 0.77 vs. 0.78 (7B)
   - T2I-CompBench: 0.3793 vs. 0.3820 (1B), 0.3916 vs. 0.3992 (7B)
   - WISE: 0.37 vs. 0.38 (1B), 0.48 vs. 0.50 (7B)
   
   Several of these gaps exceed or overlap with one standard deviation — but the *direction* is consistent: T2I-R1 is higher in every case. The paper also claims IRIS "surpasses" T2I-R1 on WISE natural-science categories (biology, physics, chemistry), but the data show: Biology 0.36 vs. 0.36 (tie), Physics 0.45 vs. 0.43 (margin of +0.02, within 1σ), Chemistry 0.22 vs. 0.22 (tie). The headline claim should be "competitive with" — "superior to" is unsupported.

2. **The central motivating observation (Figure 2) lacks statistical rigor.** Figure 2 compares self-certainty trajectories across two different models (Qwen2.5-1.5B-Instruct on math reasoning vs. Janus-Pro-1B on T2I), on different tasks, with different token types, and different external reward definitions. The plot is a single run with no error bars, no multiple seeds, and no statistical test. While the paper's main contribution (IRIS) is validated through independent ablation studies that confirm minimizing SC works, the strong contrastive narrative in the abstract and introduction ("contrary to recent findings...") rests on this single weak comparison. At minimum, multiple seeds and error bars are needed to support the claim that self-certainty trends are fundamentally task-dependent rather than an artifact of model, task, or token-type differences.

3. **Ablation studies are evaluated only on proxy reward models (HPSv2, GIT, GDino, ORM), not on the main benchmarks.** The ablation decisions (forward vs. backward KL, RL vs. direct optimization, CoT usage) are validated using the four external reward models that compose the T2I-R1 training reward. While the paper notes these are used only as evaluation metrics, the proxy metrics are not independent of the baseline's training objective. The key design choices are never verified on GenEval, T2I-CompBench, or WISE overall scores, so it is unclear whether the ablation conclusions transfer to the target evaluation setting.

### Minor

1. **The mechanism linking per-token uniformity (NSC) to semantic image quality is not well explained.** The paper offers a qualitative intuition ("low-uncertainty models generate uniform and simplistic images") supported by Figure 1 and Figure 2's correlation, but does not provide a deeper analysis (e.g., measuring image entropy, lexical diversity of CoTs, or visualizing per-token reward distributions over training). The claim that token-level KL-to-uniform should produce semantically better images remains a plausible-but-undersupported intuition.

2. **Evaluation is limited to a single model family (Janus-Pro).** The paper acknowledges this in Section 4.4 — T2I architectures are diverse (diffusion, masked modeling, MAE-style) and autoregressive T2I models are only one branch. Without results on at least one other model (e.g., Show-o, Emu3), the generality claims are untested.

3. **The paper speculates about why T2I-R1 excels on certain categories (aesthetics/spatial) and IRIS on others (natural science) without supporting evidence.** The attribution that T2I-R1's external rewards (HPSv2, DINO, GIT, ORM) favor aesthetic/spatial tasks while being "irrelevant to natural science" is reasonable but unverified — no analysis is provided to confirm that these reward models are systematically worse on natural-science prompts.

### Trivial

None.

## Nice-to-Haves

- Report the original (buggy-chat-template) T2I-R1 numbers alongside the corrected ones, so readers can assess the impact of the fix.
- Evaluate ablation checkpoints on at least one main benchmark (e.g., GenEval overall) to confirm that proxy-metric conclusions transfer.
- Add multiple seeds and error bars to Figure 2 to strengthen the core motivation.

## Removed Points

These points were identified by the reviewers but are removed from the main assessment for the reasons given below:

- **Missing original T2I-R1 numbers (chat template issue):** The critic argues the baseline comparison is compromised because original (buggy) numbers aren't provided. However, the comparison between IRIS and the *corrected* T2I-R1 is internally valid and fair — both use the same fixed template. Reporting the old numbers would be informative but is not required to assess the comparison presented.
- **Group size G=8 too small:** The paper follows the same protocol as T2I-R1 (Jiang et al., 2025), and image generation is computationally expensive. A sensitivity analysis would be a nice addition, but the existing choice is standard for this setting and yields meaningful results.
- **Reward definition is "circular":** The critic claims the reward definition is not justified, but the paper provides qualitative (Figure 1), correlational (Figure 2), and ablative (Figures 6–9) evidence linking lower self-certainty to better image quality. The mechanism could be explained more deeply, but the claim is not circular — it is empirically grounded.
- **Factorial ablation design criticism:** The critic notes the ablation in Figure 6 does not include a condition where image is minimized and text is held constant. However, the "Minimize Text SC Only" condition in Figure 6 already represents minimizing text with no image reward applied, which tests the relevant boundary. The ablations adequately support the design choices.
- **Strengths removed from Strength Finder:** The claim that "empirical discovery of task-dependent self-certainty" is a clean strength conflicts with the verified weakness about Figure 2's weak evidence, so it is downgraded. Generic/superficial phrasings (e.g., "the paper tackles the important challenge") were also removed as lacking specific evidentiary anchor.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one cross-cutting observation: the tension between the paper's strong contrastive framing ("contrary to findings in text generation") and the modest evidence base for that contrast. The harsh critic correctly identifies that Figure 2's cross-model, cross-task, single-run comparison cannot bear the weight the abstract places on it. Meanwhile, the actual algorithmic contribution — that minimizing token-level self-certainty via RL improves T2I — is independently validated by the ablation studies and does not depend on the contrastive framing. This suggests the paper would be better served by foregrounding the empirical finding that NSC-as-reward works for T2I (which is well-supported) and de-emphasizing the comparative narrative about text vs. image (which is under-supported).

## Suggestions

1. **Adjust the claims to match the data.** Replace "superior to external rewards" and "surpasses" with "competitive with" — the overall numbers consistently show slight deficits to T2I-R1, and the sub-score advantages are within error bars. The contribution is strong enough (first intrinsic-reward T2I method) that honest framing will not diminish it.
2. **Add multiple seeds and error bars to Figure 2**, or reframe the observation as a suggestive finding rather than a definitive discovery.
3. **Report at least one main-benchmark score (e.g., GenEval overall) for the best checkpoint of each ablation condition** (forward vs. backward KL, RL vs. direct, CoT vs. no CoT) to confirm that proxy-metric ablations transfer.
4. **Include a brief analysis of the mechanism** — e.g., measure image diversity (entropy, color histogram variance) or CoT lexical diversity across training to make the "uniform vs. rich images" intuition more concrete.
5. **Test on a second autoregressive T2I model** (e.g., Show-o or Emu3) to support the generality claim.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>