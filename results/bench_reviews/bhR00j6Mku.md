Now I have all the evidence needed for a thorough cross-check. Let me synthesize the final review.

---

## Summary

This paper presents the first systematic study of benchmark contamination detection failures in Large Reasoning Models (LRMs). It identifies two vulnerability scenarios: (I) when contamination introduced during SFT of a base model is concealed by subsequent RL training (specifically GRPO), and (II) when chain-of-thought contamination applied to advanced LRMs as a final SFT step leaves detection methods performing near random. The paper provides theoretical analysis attributing the concealment in Stage I to PPO-style importance sampling and clipping, supported by clean ablations contrasting RAFT (no clipping, no concealment) with RAFT++/GRPO (clipping, strong concealment). Evaluation spans 10 detection methods, 6 benchmarks, and multiple model families across both stages.

## Strengths

- **Clean identification of the clipping/importance-sampling mechanism.** The ablation comparing RAFT (AUROC 77.51% after training) vs. RAFT++ (57.58%) vs. GRPO (61.26%) in Table 3, with and without clipping, provides compelling causal evidence that PPO-style clipping drives concealment — not simply additional training. This is the paper's most specific and well-supported claim.

- **Comprehensive and well-controlled experimental design.** Stage I systematically controls for multiple confounds: the paper shows further SFT does not conceal contamination, training on clean+member RL data still conceals it (ruling out "forgetting" explanations), and the effect is monotonic across 156 GRPO steps. Evaluation across 10 detection methods, 2 base models (Qwen2.5-7B, Llama-3.1-8B), 6 benchmarks, with extensions to 3B/14B models and non-math domains (Appendix E.11) provides reasonable breadth.

- **Theoretical analysis connecting objective design to detection vulnerability.** Theorem 3.1 derives the NLL drift for PPO-style objectives and explains why the covariance term from importance-sampling/clipping reverses the gap contraction direction relative to plain rejection sampling. While idealized (tabular setting, binary rewards), the theory correctly predicts the empirical pattern across RAFT/RAFT++/GRPO.

- **Stage II finding about LRM generalization is novel and well-motivated.** Figure 4 shows that after SFT contamination with CoT, the log-prob distributions of both members and non-members shift together — the model generalizes to distributionally similar unseen samples. This challenges the memorization assumption underlying most existing detection methods and is a genuinely new observation specific to LRMs.

## Weaknesses

### Major

- **Stage I: Insufficient RL training horizon to establish permanence of concealment.** The maximum is 156 GRPO steps (one epoch on 10K questions). The paper states "we expect that extensive GRPO training would render all existing detection methods to near-random performance eventually" (line 245-246), but this extrapolation is speculative. The extension to 280 steps on Qwen-3B (Appendix E.7) partially addresses this, but the core claim about "extensive" training remains unsupported. The theory itself is a first-order expansion (O(η²)), which only rigorously holds for small step sizes — the trend could reverse at longer horizons. The paper would benefit from either longer training runs or moderating this claim.

- **The theoretical analysis is not directly connected to the AUROC evaluation metric.** Theorem 3.1 analyzes the mean NLL gap G_k, but all detection experiments report AUROC, which depends on the *ranking* of individual question scores, not just the mean gap. A contraction in mean separability could in principle coexist with maintained AUROC if variance also shifts. The paper provides empirical evidence that AUROC does drop (Tables 2, 12), which partly addresses this, but the theory is presented as explaining "why detection fails" when it actually explains why the mean NLL gap contracts. This gap is acknowledged by the paper's own framing ("many contamination detection methods rely on separability in this space") but the logical chain from gap contraction → AUROC drop is never formalized. Additionally, the empirical support in Section 3.2.1 tests only the Loss detector — the paper should show more directly that the theory's predictions extend to Min-K%, Max-K%, and LiRA.

### Minor

- **Stage II experiments test only member-only contamination.** The paper's Stage II applies SFT exclusively on member data (see Section 4). While Table 24 shows that clean+member mixtures sometimes dilute performance gains, a practical contamination scenario could involve mixing benchmark data with other training data. The AUROC for clean+member mixtures in Stage II is never reported. This does not invalidate the finding, but the paper's claim that "contamination with CoT on advanced LRMs barely leaves evidence" is bounded by this setup. Acknowledging this scope limitation more prominently would strengthen the paper.

- **Some Stage II detection results are not uniformly "near random."** LiRA on DeepSeek-R1-Distill-Qwen-14B achieves 65.55% average AUROC, and several individual entries reach 70-80% (e.g., Max-K% on AIME24 for DS Qwen-7B: 73.33%; Loss on AIME24 for DS Qwen-14B: 77.56%). These are substantially above 50% random guessing. The paper's framing ("performing near random guess") is accurate as an average statement but oversimplifies a more nuanced picture where certain method/model/benchmark combinations retain meaningful detection power.

- **The Stage I RL training produced marginal performance gains.** Table 1 shows that the RL-on-top-of-SFT rows produce pass@1 improvements of only 1-3% over SFT alone, and RL-only (no SFT) is essentially at base-model level. This weakens the practical threat model: a developer would need RL long enough to inflate benchmark scores for contamination to be worthwhile. The paper addresses this in Appendix E.7 with longer runs on Qwen-3B, but this tension between the short training used for the main experiments and the practical scenario is not fully resolved in the main text.

- **The theory relies on several idealizations not discussed.** The analysis assumes a tabular setting, binary rewards, only correct trajectories (r=1), no KL penalty, and small step sizes. While these are standard simplifications, the paper does not discuss whether or how they affect the conclusions when violated (e.g., GRPO uses group-normalized advantages, not raw rewards; the DAPO implementation removes the KL term as noted, but this is a deviation from standard PPO/GRPO). The connection between the idealized setting and the actual experiments could be more explicit.

### Trivial

- Table 3 formatting has minor readability issues (merged cells, clipped column headers).
- Figure 2 and Figure 5 would benefit from error bars or confidence intervals across rollouts.

## Nice-to-Haves

- **Variance analysis of detection scores.** Since AUROC depends on ranking (not just mean gap), reporting the variance of per-question detection scores before/after RL would strengthen the connection between the theoretical mean-gap analysis and the empirical AUROC results.
- **Testing the theory's prediction on more RL algorithms.** The paper claims that "a broad class of RL methods may inherently exhibit similar concealment capability," but only tests GRPO, RAFT, and RAFT++. Testing PPO or REINFORCE would provide stronger support for this generalization claim.
- **Clean+member AUROC for Stage II.** Reporting AUROC for the clean+member mixture condition in Table 24 would directly address the most natural practical concern about the Stage II setup.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Stage II experiments do not evaluate the scenario that would actually occur in practice"** — The paper explicitly justifies the member-only choice (Table 24 shows clean+member sometimes dilutes performance) and scopes its claim to this setting. The paper does test the clean+member mixture for pass@1. This is a reasonable design choice, not a flaw. Moved because the paper acknowledges and justifies the scope.

- **"The paper claims contamination is undetectable but conflates 'training improves the model' with 'contamination is undetectable'"** — Figure 4 directly shows that both member and non-member distributions shift together, which is not what you'd expect from general improvement alone (which could preserve or even widen the gap). The paper's explanation (generalization to distributionally similar samples) is distinct from "training improves everything."

- **"The number of RL training steps is insufficient... the RL-only and clean-RL rows show no meaningful learning"** — The paper's core claim is about concealment, not performance improvement. The short training is a limitation that the paper acknowledges (Appendix E.7), but it does not invalidate the concealment finding within that regime. The claim about "extensive... near-random eventually" is hedged ("we expect").

## Novel Insights

The reviews collectively surface one observation that goes beyond the paper's own framing: the paper provides strong evidence that **the very mechanism that makes GRPO stable (clipping/importance sampling) is what makes it dangerous from a contamination-detection perspective.** This creates an inherent tension — stabilizing RL training undermines the statistical signals detectors rely on. This tension is not exploitable by modifying detectors alone; it suggests that robust contamination detection for LRMs may require fundamentally different assumptions (e.g., behavioral or functional testing rather than statistical probing of log-probabilities). The paper hints at this in its conclusion but does not fully develop the implication.

## Suggestions

1. Add longer RL training runs (500-1000+ steps) for at least one model/benchmark to test whether the monotonic trend in Figure 2 continues or plateaus/reverses.
2. Report AUROC for the clean+member mixture condition in Stage II (alongside the member-only results already shown).
3. Add a variance analysis (e.g., per-question score distributions before/after RL) to bridge the theoretical mean-gap analysis with the AUROC evaluation metric.
4. Moderate the claim about "extensive GRPO training would render all existing detection methods to near-random performance eventually" — replace with a statement about the observed trend over the training horizon tested.
5. Test the theoretical prediction on at least one additional RL algorithm without clipping (e.g., REINFORCE) to strengthen the claim that "a broad class of RL methods" exhibits this behavior.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|---|---|---|
| /home/wg25r/review_agent/human_reviews_2026/GFDSGlEks2.md | 4.67 | Lower quality — related topic (post-training × contamination) but uses much smaller models (0.5B-4B), less comprehensive detection evaluation, no theoretical analysis. Current paper is stronger. |
| /home/wg25r/review_agent/human_reviews_2026/EjiJmiA6ea.md | 5.33 | Comparable quality — both study contamination in RL context. That paper proposes a new detection method (Self-Critique) while this paper diagnoses detection failure. Both have similar experimental breadth. |
| /home/wg25r/review_agent/human_reviews_2026/WFGxFzFDmQ.md | 5.00 | Lower quality — watermarked detection is a different framing (proactive rather than diagnostic). More narrow scope (only pre-training contamination). Current paper is broader in phenomena studied. |
| /home/wg25r/review_agent/human_reviews_2026/WERLf030OU.md | 3.00 | Much lower quality — limited experiments, weak novelty. Current paper is far stronger. |
| /home/wg25r/review_agent/human_reviews_2026/omg9K6lI93.md | 1.00 | Much lower quality — flawed experimental design, missing controls. Current paper is in a different league. |
| /home/wg25r/review_agent/human_reviews_2026/jNiEMDsRgc.md | 7.33 | Higher quality — evaluation robustness study with clean theoretical contribution and impactful findings. Current paper has similar rigor but narrower immediate impact. |
| /home/wg25r/review_agent/human_reviews_2026/StshuNpuaO.md | 5.00 | Lower quality — scaling law paper with mixed reviews. Current paper has stronger experimental methodology. |

**Reasoning:** The paper makes a solid empirical contribution with good experimental controls, a theoretical analysis that correctly predicts empirical outcomes, and identifies a genuinely new phenomenon (LRM generalization undermining memorization-based detection). The weaknesses are real but addressable — the core mechanism identification (clipping drives concealment) is well-supported. The paper compares favorably to the ~5.0-5.3 anchor papers in the contamination detection space, being stronger in experimental breadth and theoretical depth than GFDSGlEks2 (4.67) and WFGxFzFDmQ (5.00), and roughly on par with EjiJmiA6ea (5.33). It does not reach the level of the strongest papers (avg 7+) which typically offer either a deployable solution or a more definitive empirical finding. The primary limitations — short RL training horizon and the theory-AUROC gap — are standard for a first study opening a new area.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>