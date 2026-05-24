Now I have a clear picture. Let me compile the final review.

**Round 1 Bracket:** TNT sits between approximately 5.0 and 6.5. Below it: "Were RNNs All We Needed" (5.00, rejected — limited novelty, small-scale evaluation). Above it: "Beyond Auto-Regression" (7.00, accepted — polished, well-validated speed claims).

**Round 2 Narrowing:** MELODI (6.25, accepted) is the closest thematic match — hierarchical memory for long contexts. TNT is comparable in architectural novelty but weaker in evaluation rigor (training-loss-based speedup, config mismatch). CNL2bku4ra (5.25, accepted) has a simpler idea with evaluation gaps; TNT is stronger. UltraMem (6.00, accepted) is comparable.

**Final placement:** 5.5 — between CNL2bku4ra (5.25) and MELODI (6.25), closer to the lower end due to the speedup evaluation gap. This is a borderline paper with genuine contributions but non-trivial evaluation weaknesses.

---

## Summary

TNT introduces a two-stage training paradigm for deep (non-linear) test-time memorization models that decouples training throughput from inference performance. The core contribution is a hierarchical memory architecture: a global module processes large, hardware-efficient chunks to capture long-range context, while multiple local modules with periodic state resets handle fine-grained details and enable context parallelism. A Q-K projection mechanism resolves the train-test domain mismatch in memory retrieval, and a brief Stage 2 fine-tuning phase adapts the model to high-resolution small-chunk inference with minimal overhead. Experiments on Titans show up to 17× training speedup and improved perplexity and reasoning accuracy.

## Strengths

- **Hierarchical memory with periodic resets is a genuinely novel architectural contribution.** The idea of resetting local memory states to a shared learned initialization every S_L tokens (Eq. 6) breaks sequential dependencies and enables context parallelism for non-linear deep memory modules — a long-standing challenge that prior work largely avoided by sticking to linear recurrences. This is clearly motivated by the three challenges in Section 3 and well-illustrated in Figure 3.

- **The Q-K projection mechanism (Section 4.1.2, Eq. 7) is simple, well-motivated, and empirically validated.** The insight that memory compression trains on keys but retrieval queries with queries creates a domain mismatch is sharp, and the projection onto the key subspace elegantly resolves it. The ablation (Table 3) shows its removal increases perplexity from 21.04 to 22.01 and drops reasoning accuracy from 40.6% to 36.4%, confirming it is not a marginal tweak.

- **Componential ablation (Table 3) systematically validates each design choice.** Incrementally adding local memory modules reduces perplexity from 23.53 (base Titans) to 20.15 (4 local modules). Removing global memory degrades perplexity to 25.60. The ablation provides a clean decomposition of where the gains come from.

- **The two-stage training paradigm is practical and well-justified.** The observation that a brief fine-tuning phase with smaller chunk sizes can overcome train-test chunk-size mismatch (Challenge 3, Figure 2) is valuable. The reported 5% overhead makes this a genuinely lightweight solution rather than a post-hoc fix.

- **The problem is important and well-motivated.** Deep memory modules are a promising alternative to Transformers for long-context modeling, but their training inefficiency (sub-10% FLOPs utilization) is a real barrier. TNT addresses a genuine bottleneck that, if resolved, could accelerate research in this subfield.

## Weaknesses

### Fatal

None.

### Major

- **The headline speedup claim (17×) uses training loss as a target, not validation perplexity or any downstream quality metric.** Table 1 measures wall-clock time to reach training loss 3.20. While the paper separately reports validation perplexity in Table 2, no link is established between these two tables — there is no evidence that reaching training loss 3.20 faster corresponds to reaching a given validation perplexity faster. Training loss can diverge from model quality across architectures with different chunk sizes (the very hyperparameter being varied in Table 1). This weakens the paper's central narrative that TNT "simultaneously improves efficiency and accuracy," because the efficiency measurement and accuracy measurement are disconnected. The paper would be strengthened substantially by plotting validation perplexity vs. wall-clock time for TNT and baselines.

- **The fastest-training and best-quality TNT configurations are different, and the speed of the best-quality configuration is not reported.** The top speedup (17.37×) in Table 1 uses a single local memory with C_L = {64}. The best-quality model in Table 2 uses four local memories with C_L = {4,8,16,32} (avg ppl 23.13). The training time of the multi-local-memory configurations is absent, so the paper does not demonstrate that a single TNT model is simultaneously 17× faster and more accurate than Titans. These two properties are demonstrated on incompatible setups.

### Minor

- **The generality claim ("Evaluated on Titans and TTT models" in the abstract) is not supported by the experiments.** The abstract states TNT was evaluated on both Titans and TTT, but the experiments only instantiate TNT on Titans. TTT appears only as a baseline in Table 2, not as a backbone for TNT. The claim that TNT is a "general training paradigm applicable to any deep memory module" (Section 1) is reasonable but remains empirically untested beyond a single architecture.

- **The base Titans configuration in Table 3 is not fully specified.** The ablation's "Base Model (Titans)" reports 23.53 perplexity without indicating its chunk size C. Cross-referencing Table 2 (where Titans C=256 has C4=23.53), this appears to be Titans with C=256 evaluated on C4, but this should be explicit for interpretability.

- **The context parallelism claim is architectural, not demonstrated through distributed experiments.** The periodic reset mechanism is motivated as enabling massive context parallelism (Section 4.1.1), but all experiments use a single TPUv4 pod with model parallelism 2. No multi-device scaling results are shown. The linear runtime scaling in Figure 4 can be explained by algorithmic complexity alone and does not validate the context parallelism claim specifically.

### Trivial

- None significant. The paper is generally well-written.

## Nice-to-Haves

- Reporting wall-clock time for the best-performing multi-local-memory configurations ({4,8,16,32}) would close the gap between Tables 1 and 2 and provide a complete picture of the speed-quality trade-off.
- Testing TNT on at least one additional deep memory module (e.g., TTT as the abstract suggests) would substantiate the generality claim.
- Reporting variance or confidence intervals for perplexity and accuracy numbers would strengthen reliability, though this is not standard in this subfield at this scale.
- An end-to-end measurement that includes Stage 2 fine-tuning overhead in the total training time would help practitioners assess overall cost.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing Appendix E and Table 4 (harsh critic):** Removed. The parser strips appendices and supplementary material from all papers; these exist in the original submission. The 5% Stage 2 overhead claim references Table 4, which is a parser artifact, not an author omission.

- **"Fatal" label on training-loss speedup (harsh critic):** Demoted to Major. Training loss is a reasonable, if imperfect, proxy for convergence. The paper separately validates model quality. This is an evaluation gap, not a fatal flaw.

- **Pure formatting/grammar complaints:** Not present in any substantive form in the reviews.

- **"No results for TTT" framed as missing experiments (harsh critic):** Incorporated as Minor, but the harsh critic's framing of generality failure is overstated. The paper's claim that TNT is a general paradigm is a conceptual claim; the lack of TTT experiments limits empirical support but does not invalidate the framework.

- **Strength Finder — "Enables context parallelism for non-linear deep memory modules through periodic state resets" (strength):** Kept but with the caveat that this is an architectural claim, not a distributed-systems demonstration. Moved the gap in distributed validation to Minor weaknesses.

- **Strength Finder — "Decouples training efficiency from inference performance with massive measured speedups":** Partially retained. The speedup numbers are real (Table 1) but the disconnect from model quality is flagged as a Major weakness.

## Novel Insights

The paper's observation that deep memory modules suffer from a compression-retrieval domain mismatch — the memory is trained on keys but queried with queries — and that a simple Q-K projection onto the key subspace resolves this, is genuinely insightful and likely applies beyond TNT to any architecture using test-time memorization with asymmetric encoding/retrieval pathways. This insight is more broadly applicable than the specific training framework and deserves attention from the wider recurrent architecture community.

## Suggestions

- Replace or supplement the training-loss-based speedup in Table 1 with validation-perplexity-vs-wall-clock-time curves. This is the single most important change to make the paper's central claim credible.
- Report training time for the best-quality multi-local-memory configurations, even if the speedup is smaller than 17×. A 5× speedup with better accuracy is still a strong result and would be more honest.
- Either demonstrate TNT on a second deep memory module (e.g., TTT) or soften the generality language in the abstract to reflect that empirical validation is currently limited to Titans.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison to TNT |
|--------|-----------|-------|-------------------|
| 4ymHtDAlBv (FSFC RNN) | 2.33 | R1 | Clearly weaker — narrow contribution, limited evaluation |
| I1484gDBr4 (Linear RNNs) | 2.50 | R1 | Clearly weaker — limited novelty, small-scale |
| It4KL6XnPq (Foundation Policies) | 3.00 | R1 | Different domain, weaker contribution |
| GrmFFxGnOR (Were RNNs All We Needed) | 5.00 | R1 | TNT is stronger — more novel architecture, better evaluation |
| CNL2bku4ra (Test-Time Training NN) | 5.25 | R2 | TNT is moderately stronger — more architectural depth |
| Hjk1tWIdvL (Hierarchy-Aided Sparse Attn) | 5.00 | R2 | Different approach, TNT has better empirical validation |
| DfTWrTwLzD (Multi-Grained Self-Injection) | 5.00 | R2 | TNT is comparable or slightly stronger |
| UU9Icwbhin (Retentive Network) | 4.75 | R2 | TNT is stronger — more thorough evaluation |
| UltraMem (zjeHLSiNv1) | 6.00 | R2 | Comparable — TNT has similar contribution level |
| MELODI (TvGPP8i18S) | 6.25 | R1/R2 | TNT is slightly weaker — MELODI has cleaner evaluation |
| Memory Mosaics (IiagjrJNwF) | 6.25 | R1 | TNT is comparable or slightly weaker |
| Beyond Auto-Regression (uZ5K4HeNwd) | 7.00 | R2 | TNT is clearly weaker — more polished, better-validated claims |

**Round 1 bracket:** 5.0–6.5. **Round 2 narrowed to:** 5.25–6.25. TNT is stronger than CNL2bku4ra (5.25) but weaker than MELODI (6.25) due to the training-loss speedup gap and config mismatch. Final placement: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>