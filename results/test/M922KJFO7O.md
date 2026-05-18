Now I have all the information I need. Let me carefully construct the final consolidated review, verifying each claim against the paper.

---

## Summary

This paper proposes ClusterGen, a KV-cache compression method that clusters key embeddings online and uses reservoir sampling on values to approximate attention output with sublinear memory and time. The paper provides theoretical error bounds (Theorem 2.4) and validates the clusterability premise qualitatively. However, the empirical evaluation tests an offline k-center clustering method rather than the claimed streaming algorithm, and no runtime or memory measurements are provided to support the central efficiency claims.

## Strengths

1. **Novel algorithmic insight exploiting key embedding structure.** The paper identifies and provides evidence (t-SNE visualizations, Fig. 1; query norm measurements, Table 1) that key embeddings in high-performing LLMs (especially those with RoPE) are clusterable, while values are not. This geometric observation is leveraged to design a compression approach that is conceptually distinct from prior attention-score-based or position-based eviction heuristics.

2. **Theoretical analysis with provable error bounds.** Theorem 2.4 and Corollary 2.5 provide formal guarantees that under $(m,\delta)$-clusterability and bounded query norms, ClusterGen achieves a spectral error bound (Eq. 3) with $O(\varepsilon^{-2} d n^{1-\Omega(1)})$ memory and runtime. This is a non-trivial theoretical contribution that goes beyond the heuristic guarantees of prior KV-cache compression methods (H2O, AttentionSink).

3. **Empirical outperformance over baselines under equal cache budgets.** On line retrieval (Table 2), the clustering-based approach achieves substantially higher accuracy than H2O and AttentionSink across sequence lengths of 5k–9k (e.g., 44% vs. ~34% at 9k). On LongBench tasks (Table 3), it shows advantages on single-document QA and code completion.

## Weaknesses

### Fatal

None.

### Major

1. **The experiments test an offline algorithm, not the claimed streaming method.** The paper's central algorithmic contribution is Algorithm 1 — a streaming clustering procedure that processes tokens one at a time with sublinear update cost. Yet Section 4.1 explicitly states: *"We apply the greedy k-center clustering algorithm **once** to compress the entire KV caches"* (emphasis added). This is an offline pass over all keys, not the streaming reservoir-based method described in Algorithm 1. The online algorithm is never implemented, its runtime or memory usage is never measured, and its claimed sublinear scaling is never demonstrated. The empirical results validate a different (non-streaming) method. This is the most serious weakness: the paper's headline claim is about a streaming algorithm that is not evaluated.

2. **No runtime or memory measurements anywhere in the paper.** Despite the title claiming "Sublinear Time and Memory," the experiments report only task accuracy. No wall-clock time, memory usage, or scaling behavior is measured for any method. The sole hardware statement (line 279: "single NVIDIA A100 GPU with 80 GB VRAM") simply describes the compute setup. The theoretical complexity analysis provides an upper bound, but whether the algorithm actually achieves sublinear performance in practice — and how it compares to baselines in efficiency — is entirely unknown empirically. Given that the central contribution is a complexity improvement, this is a severe omission.

3. **The key theoretical parameter $\delta$ is never quantified empirically.** Theorem 2.4 requires that the keys be $(m,\delta)$-clusterable and that $\delta r = o(\log n)$ for sublinear guarantees. The paper provides qualitative t-SNE evidence of clusterability and reports query $l_2$ norms $r$ (Table 1, roughly 5–20), but it never measures $\delta$ (maximum cluster diameter) for any real model, layer, or head. For typical $n$ where $\log n \approx 8$–10, the condition $\delta r = o(\log n)$ with $r \approx 10$ requires $\delta \ll 1$, but key embeddings have norms on the order of 1–10 — a diameter under 1 is not obviously true. The empirical evidence for clusterability (t-SNE, k-center with $k=16$) shows qualitative structure but does not quantify diameters, leaving the central theoretical condition unverified. Furthermore, the offline k-center experiments use a fixed number of centers $k$, not a fixed radius $\delta$, creating a disconnect between the theoretical framing and empirical setup.

### Minor

4. **No full-cache (uncompressed) baseline is reported.** The paper compares only against other compression methods (H2O, AttentionSink) under equal cache budgets. Without knowing the uncompressed attention's accuracy on the same tasks, it is impossible to assess how much quality is sacrificed by compression. A reader cannot tell, for instance, whether 44% accuracy at 9k (Table 2) represents a small or large degradation relative to no compression.

5. **The theoretical error bound (Eq. 3) is not empirically evaluated.** The bound uses the operator norm of the value matrix $\|V_n\|_{\text{op}}$ and the spectral norm of the softmax vector. The paper never computes this bound or any proxy approximation error (e.g., L2 difference from exact attention) in the experiments. The theory and experiments are effectively disconnected on this dimension.

6. **Limited comparison scope.** Only two baselines (H2O and AttentionSink) from early 2023 are compared. H2O could not be evaluated on the LongBench tasks at all due to memory overflow. The experimental picture would be strengthened by comparisons with methods operating on a similar principle (e.g., clustering-based approaches) or more recent eviction strategies.

### Trivial

- The paper notes that the proofs of Lemma 2.2 and Theorem 2.3 are deferred to an appendix; the appendix content was not visible in the reviewed manuscript.
- The pseudocode contains minor formatting inconsistencies (e.g., line 11 initializes $\mathcal{D}$ within the procedure, which is syntactically odd for an update routine).

## Nice-to-Haves

- Measure the actual approximation error (L2 difference) between ClusterGen and exact attention for varying cache budgets, connecting theory to experiments.
- Ablate the components: compare online streaming clustering vs. offline k-center vs. random subsampling, and vary $s$ and $t$ to show their effect on accuracy and efficiency.
- Quantify $\delta$ empirically across layers and models (distribution of within-cluster key distances) to verify $\delta r = o(\log n)$.
- Include error bars or confidence intervals for main experimental results (Tables 2–3).

## Removed Points

These points were flagged by reviewers but are removed or downgraded per the review rules:

- *Criticism that the sampling schemes (UPDATEMATRIXPRODUCT and UPDATESOFTMAXNORMALIZER) are flawed or incorrect.* **Removed.** The procedures are correct: each of the $s$/$t$ slots independently maintains a reservoir sample. For UPDATEMATRIXPRODUCT, the probability $p = \|v\|_2^2/(\mu + \|v\|_2^2)$ correctly implements weighted reservoir sampling per slot. For UPDATESOFTMAXNORMALIZER, the probability $p = 1/n_{i^*}$ correctly maintains $t$ independent uniform reservoir samples — each item has probability $1/n$ of being in any given slot after $n$ items, contra the critic's claim of "oversampling earlier elements." The critic's mathematical analysis of these procedures is incorrect.

- *Criticism about missing related works (SnapKV, KIVI, KVQuant, Keyformer).* **Removed.** Per review rules, missing related works cannot be confirmed without external sources.

- *Criticism about missing proofs or appendix content.* **Removed.** The parser strips appendix content; these proofs exist in the original submission.

- *Criticism about parser-truncated lemma statements (Lemma 2.2).* **Removed.** This is a parser artifact, not an author error.

- *Claim that the error bound is "not tied to the implementation" (downgraded from major to minor).* The paper could usefully measure approximation error, but end-task accuracy is a standard and defensible evaluation proxy. This is a missed opportunity, not a structural flaw.

## Novel Insights

The harsh critic's observation that the offline empirical evaluation tests a fundamentally different procedure from the claimed streaming algorithm is the most striking insight from the review process — it reveals a core disconnect between the paper's theoretical framing and its experimental validation that is not acknowledged in the paper itself. The strength finder's identification of the clusterability analysis as a genuinely novel empirical finding is correct and partially mitigates this gap, but it does not resolve it. A striking pattern is that both the theoretical and empirical contributions are individually interesting, but they operate on different levels: the theory concerns a streaming complexity guarantee, while the experiments test a batch k-center heuristic. The paper would be strengthened by honestly confronting this gap.

## Suggestions

1. **Implement and benchmark the streaming algorithm (Algorithm 1).** Measure its runtime and memory growth as a function of sequence length to empirically verify sublinear scaling. Without this, the paper's title claim is unsupported.

2. **Quantify $\delta$ empirically** across layers and heads for the models studied. Report the distribution of pairwise distances within clusters from the k-center algorithm to verify whether $\delta r = o(\log n)$ holds in practice.

3. **Add a full-cache baseline** to all experiments so readers can assess absolute quality loss.

4. **Include runtime and peak memory measurements** for all methods compared. Even wall-clock time per token and cache size in MB would substantially strengthen the empirical case.

5. **Either reframe the paper** to acknowledge that the experiments evaluate batch k-center (not streaming) and clarify that the streaming algorithm's efficiency is a theoretical result, or replace the offline experiments with the actual streaming implementation.

## Score and Decision

**Overall assessment:** The paper identifies a genuinely interesting geometric property of LLM key embeddings and provides non-trivial theoretical analysis. However, the empirical evaluation does not test the claimed streaming algorithm, and the central efficiency claims (sublinear time and memory) are not empirically supported by any measurement. The theoretical conditions are also not quantitatively verified for real models. While the core ideas have merit, the paper in its current form makes claims that its evidence does not support.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>