---

## Summary

TNT is a two-stage training paradigm for deep memory modules (e.g., Titans, TTT) that decouples training efficiency from inference quality. Stage 1 introduces a hierarchical memory architecture—one global module with a large chunk size and *N* parallel local modules with periodic state resets—enabling context parallelism for non-linear recurrences. Stage 2 applies brief fine-tuning at smaller chunk sizes to adapt the model for fine-grained inference. The framework achieves up to 17.37× faster training-to-quality over the most accurate Titans baseline while simultaneously improving perplexity and reasoning accuracy over all tested RNN architectures.

---

## Strengths

- **Substantial, well-documented training acceleration**: Table 1 shows TNT reaches target loss 3.20 up to 17.37× faster than Titans (C=8), and Figure 4 confirms linear runtime scaling with sequence length vs. quadratic for attention and super-linear for standard Titans. At equal chunk size (C=C_L=8), the speedup is 7.68×, still impressive and clearly the result of the periodic-reset context-parallelism mechanism alone.
- **Improved language modeling quality over all RNN baselines**: Table 2 demonstrates TNT Stage 1 (4 local modules, {4,8,16,32}) achieves 23.13 avg ppl—lower than the best Titans at 25.07 and vanilla Transformer at 23.58—while taking a fraction of training time. The improvement over Titans is large (25.07 → 23.13).
- **Component ablation validates each design choice**: Table 3 provides a clear decomposition: removing global memory raises PPL from 21.04 to 25.60 (+4.56), removing Q-K projection raises it to 22.01 (+0.97), and each additional local module yields incremental gains. The ablations are structured and interpretable.
- **Empirically identifies the chunk-size sensitivity problem**: Figure 2 compellingly documents that a 550M Titans model pre-trained at C=64 degrades sharply for both smaller and larger inference chunk sizes (perplexity rising from 13.78 at C=64 to 36.45 at C=8), directly motivating the two-stage design.
- **Stage 2 is computationally inexpensive**: The paper reports Stage 2 requires ~5% of pre-training compute (referenced to Table 4), which makes the fine-tuning stage practical even if its PPL gains are modest.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing long-context quality evaluation despite long-context motivation**: The entire abstract, introduction, and conclusion are framed around enabling "truly long sequences." Runtime experiments reach 32K tokens (Figure 4), but all language-model quality evaluations in Table 2 use 16K context and standard benchmarks (C4, FineWeb, PG19, PIQA, HellaSwag, ARC-e, CSQA) that do not probe long-range information retrieval. No passkey retrieval, RULER, SCROLLS, or any needle-in-a-haystack experiment is present. The core claim—that TNT's hierarchical global memory enables *better* long-context understanding, not just faster runtime—is never directly validated. The efficiency contribution stands on its own, but the paper cannot currently support its motivating premise on quality grounds.

- **Attribution ambiguity: architectural change vs. training paradigm**: TNT is framed as a *training paradigm*, yet it modifies the model architecture by adding a global memory module and N local modules. The quality gains (e.g., 23.53 → 21.04 PPL on C4 with 1 local module in Table 3) reflect the combined effect of: (a) the periodic-reset parallelism mechanism, (b) the added global memory capacity, and (c) the Q-K projection. Table 3 ablates (b) and (c) individually, but there is no comparison that isolates (a) from (b)—i.e., no experiment trains a Titans model augmented with the same global+local architectural setup *without* periodic resets and at the same total parameter budget. Without this, the paper cannot cleanly attribute quality gains to the "training paradigm" as claimed, versus simply "adding more memory modules."

### Minor

- **Stage 2's contribution is marginal and its framing is overstated**: In Table 2, Stage 2 reduces the best 4-module average perplexity from 23.13 → 23.09 (0.04 PPL) and accuracy from 40.6% → 40.9%. For N=1, the gain is 24.10 → 23.99 PPL and 40.6% → 40.9% acc. These are consistent but very small. Calling this a "stage" that "resolves Challenge 3" misrepresents its magnitude; a more accurate description would be "a cheap calibration step that marginally improves inference-resolution alignment." This mismatch between the narrative and the data is likely to mislead readers about Stage 2's practical value.

- **Ablation baseline is a weaker Titans configuration**: Table 3 uses Titans C=256 (C4 PPL = 23.53) as the "Base Model," while Table 2 also reports Titans C=8 (C4 PPL = 22.25), which is the better-performing but slower Titans configuration. Using the weaker baseline inflates the apparent magnitude of each incremental TNT improvement in the ablation. The ablation should ideally compare against Titans C=8 as the challenging baseline.

- **Inference behavior beyond S_L is underspecified**: Section 4.2 states that Stage 2 aligns the model with "the standard prefill-and-decode paradigm," with global memory handling prefill and local memory handling decoding. However, when generating sequences longer than S_L = 4096 tokens, the behavior of the local memory (which was trained to reset every S_L tokens) during auto-regressive generation is not described. This gap affects the paper's claims about deployment in long-sequence settings.

- **Figure 2 uses a 550M model while all quality experiments use 150M**: The chunk-size sensitivity demonstration (Figure 2) is compelling but uses a 550M model, while the main results use 150M. The qualitative phenomenon likely transfers, but there is no confirmation it holds at the experimental scale.

### Trivial

- The paper concedes TNT does not yet match the Gated Transformer in perplexity (23.09 vs. 22.39) but claims superiority in reasoning accuracy (41.0% vs. 39.7%). A 1.3% accuracy difference across four benchmarks without variance statistics cannot robustly support a superiority claim. The paper itself acknowledges perplexity is "a more stable metric" — it should be more cautious about the accuracy comparison.

---

## Nice-to-Haves

- A controlled experiment isolating periodic resets from the architectural change: train a Titans model augmented with global+local modules at the same parameter budget but without periodic resets, and compare against TNT. This would firmly establish whether the training paradigm or the memory hierarchy is responsible for quality gains.
- Even a simple passkey retrieval or length-extrapolation experiment at 32K–64K would close the motivational gap and directly validate the long-context claim.
- An ablation testing a learned gating (instead of uniform addition) between global and local memory outputs in Eq. 7, to determine whether the equal-weight combination is a principled choice or a simplification.
- Statistical significance testing or multiple runs for the small accuracy differences in Table 2 (which are in the 1–2% range).

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Projection matrix is not idempotent / not a true orthogonal projection" (Section 4.1.2)**: The paper describes Eq. 7 as projecting $q_t$ onto the "subspace spanned by previously observed keys." Technically, $\sum_\tau k_\tau k_\tau^\top / \|k_\tau\|^2$ is only idempotent if keys are orthonormal, so "projection" is informal. However, the paper uses this term in an engineering context and validates the operation empirically (+0.97 PPL in Table 3). This is a theoretical imprecision but not a flaw that invalidates the method. Demoted from weakness; does not belong in the main review.

- **Harsh Critic: "17× headline is misleading because it compares different chunk sizes"**: The paper is transparent in Table 1 and Section 5.2: "17.37× faster than the original Titans baseline" refers to Titans C=8 (most accurate configuration). The paper explicitly states the same-chunk-size comparison (7.68× at C=8) in Section 5.2. No framing issue exists given this transparency.

- **Harsh Critic: "No variance/error bars on accuracy numbers" as a major issue**: Single-run evaluation is standard practice for these reasoning benchmarks at this scale in the field. This is a minor point, addressed in Trivial section.

- **Strength Finder: "Stage 2 fine-tuning adapts to small inference chunks with minimal overhead" framed as a core strength**: Stage 2 is real and costs only 5% extra compute, but the PPL/accuracy gains are minimal (0.04 ppl, 0.3% acc for the 4-module case). This conflicts with the paper's framing of Stage 2 as a major contribution, so the strength is downgraded and Stage 2's overstated role is moved to Minor weakness instead.

---

## Novel Insights

The Q-K projection (Eq. 7) is a lightweight, running-sum approximation to aligning retrieval queries with the compression key-domain, and its ablation shows a meaningful +0.97 PPL impact — suggesting that domain mismatch between compression and retrieval in test-time memory modules is a genuinely underappreciated degradation source. The periodic-reset mechanism enabling context parallelism for *non-linear* recurrences (which cannot use linear parallel scans) is the paper's most technically novel observation: it essentially converts a non-linear RNN into a block-independent computation graph at the cost of lost cross-shard continuity, compensated by the global memory. The tradeoff analysis of when this approximation is worthwhile (how much global memory coverage is needed) is left implicit but is an interesting design question for future work.

---

## Suggestions

1. Add a long-context quality experiment (e.g., passkey retrieval at 32K or RULER) to validate the central motivation — even a single controlled comparison showing TNT retains information better than the best-comparable Titans at long context would be highly impactful.
2. Add an ablation experiment: Titans + global+local architecture but *without* periodic resets, at the same parameter and FLOP budget. This directly establishes whether the quality improvement comes from the training paradigm or the architecture.
3. Specify the inference behavior of the local memory during autoregressive generation of sequences longer than S_L — this is a practical deployment question the paper leaves unanswered.
4. Use Titans C=8 (the better-performing baseline) as the ablation starting point in Table 3, or provide both for completeness.
5. Reframe Stage 2 as a lightweight calibration step; its 0.04 ppl improvement for the best configuration is real but should not be framed as resolving a "fundamental challenge."

---

## Score and Decision

**Originality**: The periodic-reset approach for non-linear RNN parallelization is a novel practical contribution. The hierarchical memory design builds on prior work (e.g., log-linear attention) but applies it to the deep memory module setting in a new way. The Q-K projection is simple and novel. *Score: 3/5*

**Importance of research question**: Training efficiency for deep memory modules is a genuine bottleneck and a timely problem. Resolving it could unlock a broader experimental ecosystem. *Score: 4/5*

**Claims supported**: The training efficiency claims (Table 1, Figure 4) are strongly and transparently supported. The quality claims are supported for standard benchmarks but not at long context, and attribution of quality gains to the training paradigm is incomplete. *Score: 3/5*

**Soundness of experiments**: Ablations are clear and useful. Core experiments are well-designed. The chunk-size experiments and runtime comparisons are credible. Missing: long-context quality evaluation; attribution isolation experiment. *Score: 3/5*

**Clarity of writing**: The paper is well-organized, the three challenges are clearly stated, and the solutions map cleanly onto them. Figures and tables are informative. *Score: 4/5*

**Value to community**: Removes a practical training bottleneck for a growing class of architectures. The training paradigm is model-agnostic. Directly useful for practitioners working with Titans and TTT variants. *Score: 4/5*

The paper makes a clear, well-executed contribution to training efficiency for deep memory modules. The 7–17× speedup is real and significant. Quality improvements over RNN baselines are verified. The major shortcomings — missing long-context quality evaluation and incomplete attribution of quality gains — are gaps the authors should address but do not invalidate the core efficiency contribution, which stands independently. This is a weak accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>