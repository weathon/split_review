- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 6, 3
Here is my consolidated review:

---

## Summary

This paper proposes a contextual biasing method for ASR based on the Knuth-Morris-Pratt (KMP) string matching algorithm. The key idea is to use KMP failure functions to maintain matching state across biasing phrases during beam search, computing score bonuses as the difference of a potential function. The method is designed to be TPU-friendly by replacing sparse WFST operations with dense vectorized tensor operations. Experimental results on large-scale voice search data show substantial WER reductions (50–77% relative on biasing test sets) over a strong RNN-T baseline, and additive gains when combined with a model-based biasing method (NAM).

---

## Strengths

1. **Large WER reductions without additional model parameters.** Table 1 shows relative WER reductions of 50–77% on biasing test sets (e.g., With-Prefix B=150: 9.6% → 2.4% with shallow fusion F=4096; Without-Prefix B=150: 20.9% → 4.8%) while degrading Anti-Biasing by at most 0.6 points absolute even at B=3000. These are large, clean improvements that demonstrate the method works on its own terms.

2. **Additive gains when combined with model-based biasing (NAM).** Table 2 shows that KMP biasing provides an additional 20–40% relative WER improvement over NAM alone across With-Prefix and Without-Prefix sets (e.g., With-Prefix B=150: 1.5% NAM alone → 0.9% with KMP fusion). This demonstrates orthogonality to model-based approaches and practical value for systems already using NAM.

3. **Principled design with clean theoretical grounding.** The paper derives the biasing method from the KMP algorithm, establishing an explicit equivalence between the biasing FST and a deterministic epsilon-free finite state automaton defined by the forward function (Section 2.2, citing [Algintro]). The failure function approach is theoretically justified as a space-efficient (O(m) per phrase) alternative to storing full transition tables.

4. **Two integration variants with clear trade-off analysis.** Section 2.3 presents both shallow fusion (biasing before pruning, O(γ̄KFB) per step) and on-the-fly rescoring (biasing after pruning, O(γ̄KB) per step), with empirical validation (Table 1) that larger F consistently improves accuracy at the expected computational cost.

5. **Efficient prefix boosting extension.** Section 2.4 proposes a method to boost biasing strength when prefix phrases (e.g., "call", "open", "play") are detected, with minimal added state (O(C+B) overhead). Table 2 shows further gains on Contact-Tag (3.4% → 3.0%) and With-Prefix without degrading Anti-Biasing.

---

## Weaknesses

### Fatal

None.

### Major

1. **No comparison against WFST-based biasing, despite the paper's central framing.** The abstract states that the method "simulates the classical approaches often implemented in the WFST framework" and the introduction motivates the work by arguing that "FST-based biasing poses significant challenges for an efficient TPU-based implementation." This framing directly invites comparison to WFST biasing. Yet the experiments contain zero comparisons against any WFST-based biasing method — neither on accuracy, latency, nor memory. Without this, the reader cannot verify whether KMP biasing achieves accuracy comparable to the classical approach it claims to simulate/replace. This is not a missing ablation; it is the primary baseline implied by the paper's own contribution statement. The paper should include at least one accuracy comparison against a WFST shallow fusion baseline (e.g., Zhao et al. 2019) on the same evaluation sets, even if the WFST runs on CPU and KMP on TPU.

2. **No empirical efficiency measurements despite heavy emphasis on TPU-friendliness.** The paper repeatedly emphasizes "memory footprint and efficiency on TPUs," "vectorization," and being "TPU-friendly," but provides **no wall-clock latency, throughput, or memory usage data whatsoever**. The complexity analysis is purely symbolic (O(γ̄KB), etc.). The reader cannot determine whether the method adds 1 ms or 100 ms per utterance, how it scales with B up to 3000, what the actual overhead of the determinization loop is, or what TPU memory the state arrays require. Since efficiency on TPU is a core part of the contribution, this omission makes the central practical claim untestable. The paper should at minimum report (a) per-step or per-utterance latency overhead relative to baseline beam search, (b) scaling with B and F, and (c) memory overhead of failure function tables and state vectors.

### Minor

1. **No empirical characterization of the determinization loop overhead.** The paper bounds the worst-case determinization iterations as γ ≤ 3 (for the example pattern) and notes it is bounded by O(m), but provides no empirical distribution of γ across actual biasing phrases. Since this loop is the core computation of the forward function and determines practical runtime, reporting the average/max γ over the phrase sets used in experiments would substantiate the complexity analysis.

2. **"Significant" is used without statistical quantification.** The paper uses "significant WER reduction" (abstract, Section 4.1, conclusion) informally. While the large test set sizes (7.6K–10K utterances) make the differences likely reliable, reporting confidence intervals or performing a simple significance test would strengthen the claims.

3. **No analysis of false triggering or anti-biasing degradation.** The Anti-Biasing WER rises from 1.7% (no biasing) to 2.3% at B=3000 with shallow fusion (Table 1), and up to 2.5% with NAM+KMP+prefix boost (Table 2). The paper notes this briefly but provides no analysis of the types of errors introduced (e.g., substitution of non-biasing words with acoustically confusable biasing phrases). A brief error analysis (even qualitative) would help practitioners understand the trade-off.

### Trivial

None.

---

## Nice-to-Haves

- **Clarify the interaction between the max potential function and prefix boosting.** The potential function µ uses a max over phrase scores. When prefix boosting applies a multiplier λ to a specific phrase's score, the boost only affects the bonus if that phrase is the one achieving the max. If another phrase has a higher partial match score, the boost has no effect. The paper could benefit from noting this interaction or considering an additive alternative.

- **Ablation of the max operation in the potential function.** Using max means that at any step, only the best-matched phrase contributes to the bonus; other concurrently-matching phrases are ignored. An ablation comparing max vs. sum vs. top-k pooling would illuminate the design choice.

- **Empirical validation of the "no backtracking in T" property.** The paper claims the algorithm avoids backtracking in the input sequence. While this is a standard property of KMP, measuring the average determinization loop iterations per token across phrases would directly verify this in the biasing context.

---

## Removed Points

These points are flagged to be removed — treat them with caution:

- **No citation of prior work on string matching for biasing.** The harsh critic asks about missing prior work using string matching for biasing. Per policy: "DO NOT mention missing related works, as you do not have external sources to confirm their existence." Removed.

- **Reproducibility concerns about proprietary data.** The harsh critic notes the data is proprietary and the setting is non-reproducible, but then acknowledges "for an industrial paper this is acceptable." This is a self-cancelling point; removed.

- **Missing comparison to simpler algorithms (prefix-tree, Aho-Corasick).** The critic suggests comparing to "simpler baselines like a prefix-tree-based approach." This is scope creep — the paper's contribution is specifically KMP-based with FSA equivalence. Removed.

- **δ hyperparameter analysis across NAM vs. no-NAM settings.** The critic notes δ differs between Table 1 and Table 2 experiments. The paper already addresses this explicitly: "now the optimal δ is much smaller than those used in Section 4.1, as the output of NAM already contains strong biasing information" (lines 388–389). Removed as already addressed.

- **Limitation discussion about linear scoring.** The critic says the paper should discuss limitations of the linear scoring function. The paper already states "It is future work to explore more sophisticated scoring functions for biasing phrases" (line 169). Removed as already acknowledged.

- **"Missing" analysis in the Strengthening section that would require a different paper.** Several "Strengthening the Paper on Its Own Terms" points (statistical significance, confidence intervals for large-scale benchmarks) prescribe methodological practices not standard for industrial-scale ASR papers. These are moved here as they do not constitute genuine weaknesses.

---

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any observation that the paper itself does not already articulate or imply.

---

## Suggestions

1. **Add a WFST accuracy comparison.** Include even one evaluation set comparing KMP shallow fusion against a WFST shallow fusion baseline (e.g., Zhao et al. 2019) on the same test data. This is the single most important addition to substantiate the paper's framing.

2. **Report empirical latency and memory measurements.** Measure (a) per-utterance latency overhead of KMP biasing vs. baseline beam search on TPU, (b) scaling with B (150, 600, 3000) and F (10, 50, 4096), and (c) memory footprint of failure function tables and state vectors. Even a single table with these numbers would transform the paper from a method proposal into a practically useful reference.

3. **Report the average and maximum determinization loop iterations (γ) across the biasing phrase sets used.** This is cheap to compute and directly validates the complexity analysis.

4. **Add a brief error analysis of Anti-Biasing degradation.** Show one or two example utterances where biasing incorrectly boosted a non-present phrase, to help practitioners understand the failure mode.

---
