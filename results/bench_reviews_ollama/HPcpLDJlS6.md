## Summary
The paper proposes Stated Causal Language Modeling (stated-CLM), a training-free, architecture-preserving method that compresses adjacent token pairs in KV-cache space (rather than evicting tokens) to extend the effective memory of LLMs. The compression target is derived via a second-order (Fisher-diagonal) Taylor approximation of the CLM loss, paired with an attention re-weighting trick using a per-token count `cnt_i`. Experiments on LongBench and TopicRet across LLaMA/Mistral/Gemma report consistent gains over StreamingLLM and LongCache.

## Strengths
- **Clean conceptual unit.** Adjacent atomic compression in KV space, applied iteratively without any fine-tuning, is genuinely different from sink/eviction-style methods (StreamingLLM, LongCache), and the framing in §3 is concrete.
- **`cnt_i` bookkeeping.** Using a per-slot count to fold duplicate KVs back into a single entry is a sensible engineering trick that keeps cache size bounded under repeated compression.
- **TopicRet result is qualitatively striking (Table 2).** Eviction baselines collapse to ~0 (e.g., StreamingLLM 0.006 on LLaMA2-7B) while stated-CLM matches full-context (0.383 vs 0.383 on LLaMA2-7B). This directly targets the failure mode the method should address, which is a well-chosen evaluation.
- **LongBench gains are consistent across model families** (LLaMA2/3/3.1, Mistral, Gemma), suggesting the method is not tied to a single backbone (Table 1, +6.12% / +5.97% averages).

## Weaknesses

### Fatal
None — but two of the Major points, taken together, come close to undermining the paper's headline derivation.

### Major
- **Eq. 17 is missing `cnt_j` in the denominator.** As written, output(q) = Σ cnt_i · exp(q·K'_i) / Σ_j exp(q·K'_j) · V'_i. For this to equal the original attention when K_m=K_{m+1}=K*, the denominator must be Σ cnt_j · exp(q·K'_j) (the "duplicated K*" appears twice in the original normalizer). I verified this against the manuscript; the printed formula does not reproduce the original softmax. Either it's a pervasive typo or the implementation is in fact lossy — and the central claim that "step 2 is lossless, so optimization reduces to step 1" (just below Eq. 9) rests on this being correct. The authors must clarify and re-state Eq. 17, and indicate which version was implemented in the experiments.
- **Internal tension in §3.2.1.** The Hessian is approximated by H_ii ≈ (∇L)_i² (Fisher diagonal, Eq. 14), and immediately afterwards the gradient terms are dropped on the grounds that g_m, g_{m+1} ≈ 0. But if the gradients are negligible, then by Eq. 14 so is the Hessian, and the quadratic objective in Eq. 13 is degenerate — the "optimal e*" becomes ill-posed. At minimum this needs a quantitative justification (e.g., empirical magnitudes of g vs g²·Δ at the relevant scale of Δ). Additionally, the displayed expansion in Eq. 11 contains only (e − e_{m+1}) terms after expansion around (e_m, e_{m+1}), so the dependence on e_m has dropped out — this looks like an algebraic error in the displayed equation, not just notation.
- **Section 4.4 does not deliver the analysis it promises.** The text describes a compression-rate vs. accuracy study on HotpotQA, but Figure 3 is captioned "Inference efficiency of different models" and the prose discusses linear-vs-quadratic latency scaling. The information-loss-vs-compression-rate curve — the most direct evidence for the paper's "lower information loss per token" claim — is not actually presented. This is the core experiment for the central contribution.
- **Baselines are too narrow to support a "state-of-the-art compression" claim.** Only StreamingLLM and LongCache (both eviction methods) are compared. Several method-class peers in the same training-free KV-compression space are absent (e.g., H2O, SnapKV, FastGen). The 6.12%/5.97% gains are calibrated against the two most directly-attacked baselines; the headline claim of advantage over "context-compression methods" needs at least one non-eviction baseline to be defensible.
- **No ablations of the four moving parts.** (a) Hessian-based e*, (b) `cnt_i` re-weighting, (c) attention-score position selection, (d) positional normalization with σ=4096 + sink length 32. A trivial baseline — replace (K_m, K_{m+1}) by their mean and keep `cnt_i` — would directly show whether the second-order machinery is doing real work. Without this, the attribution of gains to the second-order derivation is unverified.

### Minor
- **Position selection uses attention from later queries (Eq. 19), but during autoregressive generation those queries do not exist yet at the moment of compression.** §3.3 does not specify whether scoring is retrospective, on the prompt only, or rolling — and what the implied compute cost is.
- **§3.4 chunk-wise compression "single forward and backward"** — the loss being back-propagated is not specified. Cross-entropy on the just-generated token? On a held-out target? This matters for reproducibility and for understanding what "second-order" actually means in deployment.
- **Cache sizes per model/baseline are not enumerated.** §4.1 says different limits are used for different models; both StreamingLLM and LongCache are sensitive to this. Without per-row reporting, Table 1 numbers are not directly interpretable.
- **TopicRet sometimes exceeds full context** (e.g., per Strength Finder summary, Mistral row). Either compression genuinely improves accuracy (surprising; deserves an explanation) or the full-context baseline runs under unfavorable settings (truncation, alignment). Worth discussing.
- **No variance / multi-seed reporting on per-task LongBench scores**, where task-level variance is typically appreciable.

### Trivial
- The "Alice / library / It was quiet" example illustrates anaphora, while the actual method compresses pairs picked by attention scores rather than co-referent pronouns. The intuition pump and the algorithm are not the same operation; a small note would help.

## Nice-to-Haves
- A qualitative analysis of *which* token pairs get compressed in practice, to test whether the intuition (semantically redundant adjacent tokens) actually obtains.
- Sweep of σ and sink-length in §3.3.
- A simple mean-pool ablation as a sanity baseline for Eq. 13.

## Removed Points
*These points are flagged as removed; treat them with caution.*

- "AutoCompressor / ICAE / gist tokens / LLMLingua are missing baselines." Removed per house rule about missing related work — I cannot independently verify these or whether they are direct competitors in the same training-free, no-fine-tuning regime the paper scopes itself to. The non-eviction-baseline concern is retained in a generic form under Major.
- "Cache-size sweep required" — kept as Minor (per-row reporting) rather than as a blocking objection; sweeps are nice-to-have.
- Strength Finder's "principled second-order optimization" framing is dropped as a standalone strength because the verified Major weakness about the Fisher/gradient contradiction directly conflicts with it.
- Strength Finder's "exact output consistency under identical embeddings" is partially retained (the `cnt_i` idea is sound) but downgraded because Eq. 17 as printed does not in fact preserve the softmax denominator.

## Novel Insights
None beyond the paper's own contributions. The atomic-pair compression with `cnt_i` re-weighting is the genuinely new conceptual move; the rest of the machinery is a straightforward port of OBD/OBS-style second-order pruning to KV-cache entries.

## Suggestions
- **Fix and re-state Eq. 17** with `cnt_j` in the denominator, and confirm the implementation matches.
- **Reconcile §3.2.1.** Show empirically that ‖g‖·Δ is small relative to ½·g²·Δ² at the operating Δ, or replace the Fisher-diagonal step with a derivation that doesn't collapse when both terms are small.
- **Replace Figure 3 in §4.4** (or add a second figure) with an actual compression-rate vs. task-accuracy curve on HotpotQA — this is the headline experiment for the paper's framing and is currently missing.
- **Add at least one non-eviction KV-compression baseline** to Table 1.
- **Ablate the second-order solution** against (i) mean of K_m, K_{m+1}, (ii) the higher-attention member, (iii) random pick.
- **Report per-baseline cache sizes** in Table 1, and add seed variance for at least the LongBench averages.
- **Specify the loss used in the §3.4 chunked backward pass** during inference.

## Score and Decision
The paper's idea (KV-pair compression with `cnt_i` reweighting, training-free) is interesting and the TopicRet result is a real signal that something useful is happening. But two technical issues — the printed Eq. 17 is non-equivalent to the original attention, and the §3.2.1 derivation simultaneously approximates H by g² and sets g≈0 — undermine the paper's central "principled, lossless" framing. Compounded with the missing compression-rate-vs-accuracy plot in §4.4 (which the text promises but Figure 3 does not deliver) and the absence of any ablation of the second-order machinery, the manuscript does not currently establish that the proposed mechanism is what is driving the gains. These are fixable in a revision, but as written the technical core and the headline empirical analysis are both under-supported.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>