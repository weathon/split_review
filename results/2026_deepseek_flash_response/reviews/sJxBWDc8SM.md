## Summary

This paper investigates whether the performance gap between Transformers and modern recurrent models (SSMs like Mamba, Hyena) on associative recall and copying stems from expressivity limitations or from optimization difficulties. Through ~3,000 runs across multiple architectures, the authors show that (1) SSMs have extremely narrow optimal learning rate windows compared to Transformers, which can confound prior expressivity comparisons; (2) width/depth scaling strategies differ qualitatively between the two families; and (3) the 1-layer Mamba expressivity advantage over 1-layer Transformers on MQAR is mechanistically attributable to its 1D convolution (Table 2). DeltaNet is shown to achieve Transformer-like LR robustness through a Householder-based update rule that avoids vanishing off-diagonal gradient terms.

## Strengths

- **Clear demonstration that LR sensitivity confounds prior SSM vs. Transformer comparisons (Figures 1–2).** The paper convincingly shows that the learning rates used by Arora et al. (2023) fall outside the narrow optimal windows for Mamba and Hyena on MQAR, and that a finer grid search rescues Mamba's performance at long sequence lengths — directly undercutting the prior "hidden size must equal sequence length" memory bottleneck claim. This is the paper's strongest contribution and is well-supported by the evidence.

- **Causal ablation isolating the 1D convolution as the mechanistic source of Mamba's 1-layer expressivity advantage (Table 2).** The double-ablation is clean and informative: removing the 1D convolution from 1-layer Mamba collapses accuracy from 99% to 2% (matching the 1-layer Transformer baseline), while adding a convolution before the QKV projections of the 1-layer Transformer raises it from 2% to 99%. This pinpoints the specific architectural component responsible for the expressivity difference, going beyond correlational analyses.

- **Demonstration that DeltaNet achieves Transformer-like LR robustness where Mamba and Mamba2 do not (Figure 7).** DeltaNet maintains near-constant accuracy across roughly two orders of magnitude of learning rates. The paper connects this to a concrete architectural mechanism — Householder-based updates avoiding the exponential decay of off-diagonal terms in Mamba's Aₖ matrices — providing a constructive path forward.

- **Contrasting scaling behavior documented with parameter-matched controls on the copy task (Table 1).** The finding that a deeper-but-narrower Mamba (24 layers, 150M params) achieves only 16% accuracy on copying while a wider-but-shallower Mamba (12 layers, 1408 width, 150M params) reaches 100% is practically informative for practitioners.

## Weaknesses

### Major

- **The central thesis (line 39) is stated more strongly than the evidence supports.** The paper claims: *"Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics."* However, the paper's own evidence directly shows that architectural components drive large performance differences: (a) Table 2 demonstrates that the 1D convolution is the reason 1-layer Mamba outperforms 1-layer Attention — removing it collapses Mamba to 2%, matching the Transformer. That is an architectural (expressivity) difference, not an optimization one. (b) Figure 7 shows DeltaNet achieves Transformer-level LR robustness while Mamba and Mamba2 do not — again an architecture-driven difference, since all three are "modern recurrent models." The paper's claim that "the main driver of poor performance can be an unsuccessful optimization" (lines 31–39) is defensible; the stronger claim that it is *not* about expressivity but *mainly* about optimization is not. The abstract and discussion use more measured language ("not just in their expressivity but in their fundamental learnability"), which is well-supported. The paper should align its central framing with its own more cautious statements. This is a framing problem rather than an evidential one, but it affects how the contribution should be interpreted.

### Minor

- **Internal contradiction about Mamba's training dynamics (Section 6).** Figure 6's caption states: *"Hyena (1024) (blue line) and Mamba (64) (orange line) show smooth learning dynamics."* However, the main text (line 190) states: *"Like single-layer Attention models, we report a significant loss bump, reinforcing the connection between Mamba and Attention mechanisms."* A "smooth" learning dynamic and a "significant loss bump" are contradictory descriptions. The figure caption and the text cannot both be correct for the same configuration. The text says Mamba's dynamics are "mixed" (line 189) but does not specify which configuration shows the bump vs. smooth dynamics. This needs to be clarified and reconciled.

- **The induction head analysis is speculative and the paper over-claims here.** The observation that a 1-layer Transformer shows a loss bump during training is a genuine empirical finding. However, claiming this "resembles the formation of an induction head circuit" (line 188) without any attention-pattern analysis, head visualization, or probing evidence is unsupported. The paper's own background (lines 71–73) explains that induction heads require a *two-layer circuit*; a single-layer Transformer physically cannot implement this. The paper acknowledges this limitation (line 192: "a single-layer transformer lacks the expressivity needed to effectively leverage this mechanism") but still lists it as a contribution (line 45: "finding that a 1-layer Transformer also exhibits a loss drop reminiscent of induction head formation"). The empirical observation of a loss bump is interesting on its own — the paper should simply report it as a loss plateau/bump without accuracy improvement and drop the induction head framing.

### Trivial

- None.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Missing experimental details (LR grid construction, optimizer hyperparameters, batch size).** The harsh critic noted these as missing from the main text. However, the paper explicitly states "All experimental details for this and subsequent experiments are in Appendix A.2" (line 105), which was stripped by the parser. The main text reports optimizer (Adam), training steps (50,000 for Section 6), model configurations, and LR ranges are visible in figures. Removed per rules about appendix stripping and reproducibility nitpicks.

- **Induction head claim is "purely speculative" / "not supported."** The harsh critic argued this finding lacks mechanistic evidence. However, the paper uses cautious language ("resembles," "reminiscent of") and explicitly acknowledges the limitation. The observation of a loss bump in 1-layer Transformers is a valid empirical finding worth reporting, even if the mechanistic interpretation is tentative. This criticism is over-stated.

- **Copy task section is under-developed.** The harsh critic noted this section is thin compared to MQAR analysis. This is a fair observation, but the copy task results (Table 1, Figure 5) support the paper's main claims about LR sensitivity and scaling behavior. The section is adequate for its supporting role. The criticism is a scope issue, not a substantive weakness.

- **Criticisms about unfair comparison (parameter mismatch in Table 1).** The harsh critic noted that the 12-layer Mamba at 80M params vs. 12-layer Attention at 150M params is not parameter-matched. However, Table 1's main comparisons are between parameter-matched models (24-layer Mamba at 150M vs. 12-layer Attention at 150M; 12-layer Mamba at 1408 width at 150M vs. 12-layer Attention at 150M). The paper's stated point is that parameter-count matching through depth is misguided. This criticism misunderstands the design.

- **Copy task analysis is "thin" / deserves more analysis.** This is a scope judgment. The paper's copy task results support the main claims; expanding the analysis would strengthen the paper but its current depth is adequate for a supporting section.

## Novel Insights

Beyond the paper's own contributions, the most notable insight from the review process is that the paper's strongest finding — the convolution ablation (Table 2) — actually undermines its own headline claim. The paper's most convincing causal evidence isolates an *architectural* component (convolution) as the decisive factor for 1-layer expressivity, not an optimization property. This tension between the paper's framing and its own best experiment is a genuine intellectual tension worth exploring: the convolution ablation suggests that the expressivity debate and the learnability debate are not competing explanations but deeply entangled — architectural choices (convolution, update-rule structure) determine both what a model *can* express and how stably it *can* be optimized. The paper would be strengthened by leaning into this entanglement rather than framing it as a dichotomy.

## Suggestions

1. **Reframe the central thesis** to align with the more measured language of the abstract and discussion. Replace line 39 ("not in terms of expressive power but mainly because of their optimization dynamics") with something like: "a crucial differentiator between these architectures lies not just in their expressivity but in their fundamental learnability properties — and critically, these two factors interact through specific architectural components (convolutions, update-rule structure) in ways that prior comparisons have not disentangled." This is more defensible and more useful to the community.

2. **Resolve the Section 6 contradiction.** Clarify whether Mamba shows a loss bump (and at what width/LR configuration) or smooth dynamics (as Figure 6 shows). If different configurations show different behavior, state this explicitly.

3. **Drop the induction head framing** for the 1-layer Transformer loss bump. Simply report the empirical finding (a loss plateau/bump without accuracy improvement) and note that this pattern differs from the accuracy-correlated phase transitions observed in multi-layer Transformers. This observation is interesting enough on its own.

4. **Acknowledge the architectural nature of key findings more explicitly** in the Discussion. The convolution ablation and the DeltaNet result show that both architecture and optimization matter, and that they interact in important ways.

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| fnO5h1CFyh.md (Learning Successor Representations...) | 3.00 | R1, low | Much weaker — unserious proposal, no clear contribution |
| NSBP7HzA5Z.md (Inductive Transformers...) | 3.00 | R1, low | Much weaker — conceptually confused |
| It4KL6XnPq.md (Foundation Policies with Memory) | 3.00 | R1, low | Much weaker — narrow RL application |
| OW5Gf4cse1.md (Task Complexity in Emergent Abilities) | 3.00 | R1, low | Much weaker — less thorough, weaker analysis |
| cSgEW7EZ9h.md (Meta-BBO with Mamba) | 4.75 | R1, mid | Weaker — niche application, limited architecture analysis |
| 1TXDtnDIsV.md (Learning Mamba as a Continual Learner) | 4.67 | R1, mid | Weaker — limited novelty, straightforward model substitution |
| mkNVPGpEPm.md (Associative memory and dead neurons) | 6.67 | R1, mid | Stronger — has theoretical contribution, rigorous proofs |
| i9RTCC6whL.md (Mamba SSMs are Lyapunov-Stable...) | 4.67 | R1, mid | Weaker — narrower contribution, less extensive experiments |
| GRMfXcAAFh.md (Oscillatory State-Space Models) | 8.00 | R1, high | Much stronger — new model with theory and experiments |
| PdaPky8MUn.md (Never Train from Scratch) | 8.00 | R1, high | Much stronger — compelling experimental reframing with practical recommendations |
| 8zJRon6k5v.md (Amortized Control of Continuous SSM...) | 8.00 | R1, high | Much stronger — novel method with strong empirical results |
| STUGfUz8ob.md (When can transformers reason with abstract symbols?) | 7.60 | R1, high | Much stronger — theoretical proofs with empirical validation |
| h3wbI8Uk1Z.md (RNNs are not Transformers (Yet)) | 5.50 | R2 | Comparable — same topic (RNN vs Transformer on associative recall), has theoretical proofs but split reviews (3,6,8,5); our paper has more thorough empirical investigation |
| b5lXUwZiD3.md (On Limitation of Transformer for Learning HMMs) | 5.25 | R2 | Slightly weaker — similar genre (empirical comparison on synthetic tasks), but our paper has more architectures, cleaner ablations |
| xrXci5YGm7.md (Emergent properties with repeated examples) | 5.50 | R2 | Comparable journal — different topic but similar score; our paper has more direct practical implications |
| pXPIQsV1St.md (Dynamical Similarity Analysis...) | 5.25 | R2 | Weaker — narrow methodology paper, less direct contribution |

**Round-1 bracket**: 4–6. **Round-2 narrowing**: Compared against anchors at 5.25 (rejected) and 5.50 (accepted). Our paper is stronger than the rejected 5.25 paper and comparable to the accepted 5.50 paper but lacks that paper's theoretical contribution while having stronger empirical depth. The framing issue and Section 6 contradiction weigh against it.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>