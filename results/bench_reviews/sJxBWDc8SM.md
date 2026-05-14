Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper conducts a large-scale empirical study (>3,000 runs) comparing Transformers and modern SSMs (Mamba, Hyena, H3, RWKV) on two synthetic benchmarks — multi-query associative recall (MQAR) and copying. The central findings are: (1) SSM performance on these tasks is acutely sensitive to learning rate choice, and finer LR grids reveal that Mamba can solve MQAR even when hidden size ≪ sequence length, contradicting prior expressivity-based conclusions; (2) SSMs benefit from width scaling while Transformers require depth (1-layer attention cannot solve MQAR regardless of width, while 1-layer Mamba can); (3) a 1D convolution is the critical component enabling single-layer performance for both architectures; and (4) newer architectures like DeltaNet exhibit more stable optimization.

## Strengths

- **Re-contextualization of prior expressivity results through optimization tuning:** Figures 1-2 demonstrate that Mamba, previously reported to fail on MQAR when hidden size ≪ sequence length, reaches near-perfect accuracy under a finer LR grid. This directly challenges the "memory bottleneck" conclusion of prior work and shows that optimization, not expressivity, was the confound. The paper provides concrete evidence that the LR grid used by Arora et al. (2023) was too coarse to capture Mamba's viable range.

- **Mechanistic identification of 1D convolution as the critical expressivity enabler:** Table 2 and Appendix Table 3 show that removing the convolution from 1-layer Mamba drops accuracy from 99% to 2% (matching the 1-layer Transformer), while adding a convolution to the Transformer's QKV projections raises its accuracy from 2% to 99%. The fine-grained result that convolution on K or V alone suffices (while on Q alone does not) is particularly insightful.

- **Contrasting width-vs-depth scaling with practical guidance:** Figures 3-4 and Table 1 demonstrate that matching total parameters by increasing depth harms Mamba while matching by increasing width succeeds. The paper provides a concrete, actionable guideline: scale SSMs by width and Transformers by depth when comparing architectures.

- **Large-scale empirical validation:** The study encompasses >3,000 runs and ~20,000 GPU-hours, with 5-seed averaging across multiple sequence lengths, widths, depths, and architectures, lending statistical weight to the findings.

- **Comparison with modern SSM variants:** The evaluation of Mamba2 and DeltaNet (Figure 7) shows that DeltaNet achieves more stable optimization, attributed to its Householder-matrix-based mixing that avoids exponential decay — a hypothesis with practical implications for future architecture design.

## Weaknesses

### Fatal

None.

### Major

- **Central thesis overstated relative to evidence:** The paper states "Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics" (line 105-106). This claim is considerably broader than what the experiments — restricted to two synthetic tasks (MQAR and copying) and primarily to Mamba — can support. While the paper does hedge elsewhere (acknowledging expressivity differences exist at line 94, and noting the limitation to synthetic benchmarks in the conclusion at line 561), the headline framing invites a reading that the authors have resolved the expressivity-vs-optimization debate in general, which they have not. The gap between the sweeping thesis statement and the synthetic-task evidence base weakens the paper's impact.

- **Induction head interpretation is speculative and unsupported by mechanistic evidence:** Section 6 interprets a loss bump in 1-layer Transformers as "an attempt to form induction heads" and infers "severe mismatches in the landscape geometry" of SSMs vs. Transformers. The paper provides no attention-map analysis, no probing of induction-circuit formation, and no gradient analysis — only learning curves. The paper does use hedged language ("resembles," "we hypothesize"), but the claim is nonetheless presented as a finding rather than as speculation. This weakens an entire section of the paper. The landscape-geometry conclusion (line 126) is particularly under-supported.

### Minor

- **Optimization instability claim would benefit from optimizer ablations:** The narrow LR window is demonstrated using a single optimizer setup (AdamW, weight decay 0.1, linear warmup, 10% warmup duration, 50 epochs). While the finding that Mamba is sensitive under a standard setup (the same setup used by prior work) is valid, the paper presents this as a fundamental property of SSMs. Ablations on weight decay, warmup duration, or gradient clipping would strengthen the generality claim. This does not invalidate the finding but limits how broadly it can be interpreted.

- **Scaling-behavior conclusions primarily based on 1-vs-2 layer comparison:** The claim of "opposing scaling behaviors" in width vs. depth is supported by comparing 1-layer and 2-layer configurations. The paper argues that the MQAR task saturates at 2 layers (stated in text and Appendix A.6 with 12-layer results), which partially addresses this concern. However, the conclusion that SSMs generally prefer width and Transformers generally prefer depth is drawn from a limited depth range for a task where depth beyond 2 layers provides no benefit.

### Trivial

- **No quantitative measure of LR window width:** The paper relies on visual inspection of Figure 1 to convey the narrowness of Mamba's viable LR window. A quantitative measure (e.g., the LR interval over which accuracy exceeds 90%) would make the "narrow window" claim more precise and comparable across architectures.

## Nice-to-Haves

- Validation of optimization instability and LR sensitivity on a small-scale language modeling task (the authors themselves note this as future work).
- Attention-map analysis for the 1-layer Transformer's loss bump to ground the induction-head speculation.
- More diverse optimizer configurations to test the generality of the instability claim.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic Point 2 (full version demanding optimizer ablations to validate instability):** The claim that the narrow LR window "may be an artefact of the chosen training recipe" is too strong. The paper's setup matches what prior work used, so the finding that prior conclusions were confounded is valid regardless. The criticism is reclassified as minor (nice-to-have ablations) rather than a threat to the core finding.

- **Harsh Critic Point about "other SSMs (Hyena, H3) still fail to match Transformers":** The paper explicitly acknowledges this at line 327-329: "we confirm that a sizable gap with Transformers can still be observed at low widths (e.g. Hyena)." The critic presents this as if the paper claims all SSMs are saved by tuning, which it does not.

- **Criticism that "no evidence is presented that optimization is the dominant differentiator in real language tasks":** The paper explicitly acknowledges this limitation in the conclusion (line 561). Criticizing a paper for not doing something it scopes out is scope creep.

- **Strength Finder's "divergent single-layer training dynamics and induction-head phenomenology":** The induction-head interpretation strength is contradicted by its corresponding weakness (speculative, unsupported). The underlying training-dynamics observation is interesting, but the induction-head framing is not well-supported enough to count as a strength.

- **Harsh Critic's formatting nitpicks (typos, "Transofrmer" at line 558):** These are parser artifacts or trivial presentation issues. Removed.

## Novel Insights

Beyond the paper's own contributions, a genuinely novel insight emerging from the cross-review analysis is that **convolution serves as a mechanistic bridge between architectures**: the paper shows that convolution on K or V alone (not Q) suffices to enable single-layer recall in Transformers (Appendix Table 3), and that removing convolution from Mamba degrades it to Transformer-level performance. This suggests a unified picture where the critical function is local information mixing in the key/value pathways, independently of whether the global mixing is attention-based or recurrence-based. This is a sharper and more actionable finding than the paper's own framing of "Mamba is mechanistically similar to a Transformer" and could guide hybrid architecture design.

## Suggestions

- **Narrow the central thesis.** Replace the absolute-sounding "Transformers differ from SSMs not in terms of expressive power but mainly because of their optimization dynamics" with a statement scoped to the tasks studied: e.g., "On MQAR and copying, prior conclusions about SSM expressivity limitations were substantially confounded by optimization; learnability is thus a first-class concern alongside expressivity."
- **Either ground or remove the induction-head speculation.** The loss-bump observation is interesting on its own as a training-dynamics phenomenon. Either inspect attention patterns to support the induction-head interpretation, or present the bump as an unexplained phenomenon worth further study.
- **Quantify the LR window.** Report the LR interval where accuracy exceeds a threshold (e.g., 90%) for each architecture, making the "narrow window" claim numerically precise.
- **Add optimizer ablations** for at least one architecture (Mamba) to strengthen the claim that the instability is a property of the model rather than a particular optimizer configuration.

## Score and Decision

**Anchor calibration:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/zj2mI9TSF7.md` | 4.00 (Reject) | Also studies SSMs on AR with mechanistic evaluation. Our paper has substantially more experiments, cleaner contributions (convolution role, LR sensitivity), and better-supported claims. Clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/8cDoHzqDXP.md` | 3.33 (Reject) | Mamba recall theory + empirics. Concerns about novelty overlap with prior work. Our paper has more novel findings and broader empirical scope. |
| `/home/wg25r/review_agent/human_reviews_2026/KaGhyeUCgO.md` | 4.50 (Reject) | Mechanistic study of primacy/recency in Mamba. Interesting but limited significance. Our paper has broader scope and clearer practical implications. |
| `/home/wg25r/review_agent/human_reviews_2026/hvpKqEYJjj.md` | 5.00 (Accept Poster) | Theoretical analysis of Mamba training dynamics. Strong theory but limited scope. Our paper lacks theory but provides broader empirical insights. Comparable in contribution level but different in approach. |
| `/home/wg25r/review_agent/human_reviews_2026/CfFj68C9Cn.md` | 6.50 (Accept Poster) | Theoretical + empirical on transformer recall. More rigorous but limited to a simpler model. Our paper is less rigorous theoretically but provides insights across multiple architectures. |
| `/home/wg25r/review_agent/human_reviews_2026/VCjlm003WL.md` | 7.00 (Accept Poster) | Formalization + empirical study of pattern matching in Transformer and Mamba. Stronger formal contribution and cleaner story. Our paper addresses a different, important question but with less conceptual depth. |
| `/home/wg25r/review_agent/human_reviews_2026/3u5Ti1CfzE.md` | 2.00 (Reject) | Benchmarking architectures in RL. Much weaker contribution. Our paper is clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/clCsSQ5rKg.md` | 2.00 (Reject) | NeuMa architecture proposal. Much weaker. |
| `/home/wg25r/review_agent/human_reviews_2026/AbcU33aTLx.md` | 2.50 (Reject) | Theoretical study of attention simulation. Much weaker. |

The paper under review has genuine empirical contributions (LR sensitivity re-contextualization, convolution role, width-vs-depth scaling) backed by large-scale experimentation. These are stronger than the 4.0-4.5 anchors but lack the theoretical depth and formal rigor of the 6.5-7.0 anchors. The overclaiming of the central thesis and the unsupported induction-head speculation are material weaknesses that prevent a higher score but do not invalidate the core contributions. Positioned between the 5.0 and 6.5 anchors but closer to 5.0 due to the claim-evidence gap and speculative interpretation in Section 6.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>