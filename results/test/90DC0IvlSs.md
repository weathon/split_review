Now I have a thorough understanding of the paper and can verify each claim against the actual content. Let me construct the final review.

---

## Summary

This paper proves the existence of a "universal set" $U$ of keys (size independent of context length $n$) that contains all large attention scores ($\ge \varepsilon$) for any query $Q$, for attention mechanisms of the form $A_{ij} = f(\langle Q_i, K_j \rangle) / \sum_\ell f(\langle Q_i, K_\ell \rangle)$ with $f$ in a broad class including $f(x)=|x|^p$. The set $U$ consists of rows with $f$-sensitivity $\ge \varepsilon$, and its size is bounded by $\Psi^f / \varepsilon$ (e.g., $d/\varepsilon$ for $f(x)=x^2$). The paper provides efficient algorithms to find $U$ in $\text{nnz}(K) + \text{poly}(d/\varepsilon)$ time, per-query computation of large attention scores in $\text{poly}(d/\varepsilon)$ time, and streaming/distributed extensions. Empirical evaluations on ViT models (both pretrained and trained from scratch) test leverage-score-based key selection on softmax attention as a heuristic motivated by the theory.

## Strengths

**1. Elegant and novel theoretical guarantee (universal set).**  
Theorem 1.1 proves a clean, non-trivial result: for any key matrix $K$ and any non-negative $f$, there exists $U \subseteq [n]$ of size $\Psi^f / \varepsilon$ (independent of $n$) such that for any query $Q$, all entries of $A$ exceeding $\varepsilon$ involve only keys in $U$. The proof via $f$-sensitivities is simple yet powerful. For $f(x)=x^2$ this gives $|U| \le d/\varepsilon$; for $f(x)=|x|^p$ with $p\le 2$, $|U| \le d/\varepsilon$; for $p>2$, $|U| \le d^{p/2}/\varepsilon$ (Section 2, Theorem 1.1, and Section 3, Theorem 3). These bounds depend only on $d$ and $p$, not on $n$, making the result fundamentally different from standard sparsity heuristics.

**2. Provably efficient algorithms with clear complexity guarantees.**  
The paper gives a concrete recipe: (a) compute $U$ in $\text{nnz}(K) + \text{poly}(d/\varepsilon)$ time via Lewis weights, (b) for any query $q$, compute all heavy attention scores in only $\text{poly}(d/\varepsilon)$ time (since only keys in $U$ need to be examined). For even $p$, the exact normalization term can be computed in $\text{poly}(d/\varepsilon)$ after SVD-based preprocessing (Section 3). Streaming (2-pass $O(d^2)$ memory, 1-pass $O(d^3\log n)$ memory) and distributed extensions are provided with rigorous bounds.

**3. Pretrained-model experiments show clear superiority of leverage scores over row norms.**  
On pretrained ViT models (softmax attention), selecting top-32 keys by leverage score dramatically outperforms row-norm selection (L/16: 48.58% vs. 8.9%; S/16: 13.3% vs. 3.3%). This is a genuine and practically meaningful empirical finding — it demonstrates that leverage scores capture key importance far better than the naive $\ell_2$ norm heuristic, even when applied to a different attention mechanism (softmax) than the one for which they are theoretically justified.

**4. Streaming and distributed extensions with rigorous memory bounds.**  
The 2-pass streaming algorithm requires only $O(d^2)$ memory, and the 1-pass variant (via online leverage scores) achieves $\text{poly}(d\log n)$ memory. These are non-trivial adaptations that maintain the guarantee of finding $U$ without storing all $n$ keys.

## Weaknesses

### Fatal
None.

### Major

**1. Experiments test softmax attention — a heuristic extension not covered by the theory.**  
The paper's theoretical results hold for $f(x)=|x|^p$ attention (and the GAP formulation with squared inner products). The experiments, however, use *softmax* attention ($f(x)=e^{x/\sqrt{d}}$). Remark 1 notes that softmax can be *approximated* by the GAP framework with finite $D$, but the experiments do not use this approximation — they apply leverage scores (the $f$-sensitivities for $f(x)=x^2$) as a selection heuristic for exact softmax attention. The paper never establishes a theoretical bridge between leverage scores of $K$ and the behavior of softmax attention. This means the experiments validate a heuristic motivated by the theory rather than the theory itself. A direct test of the universal set property (e.g., verifying that on polynomial attention, the $\varepsilon$-heavy positions are contained in the $f$-sensitivity set) would substantially strengthen the paper. *However, the paper is transparent about what it tests: it evaluates "the effectiveness of leverage score selection for the downstream task of image classification using the pretrained softmax model" — this is presented as an empirical investigation, not as a direct proof of the theory.*

**2. Training-from-scratch experiments fail to demonstrate a practical advantage over simple baselines.**  
When models are trained from scratch with selection-aware attention, leverage score selection, row-norm selection, and even random key selection all achieve similar accuracies (e.g., all around 68–75% depending on model size and $k$). The paper honestly reports this and calls it an open question. Nevertheless, it substantially limits the practical contribution: the proposed method does not yield better models than trivial baselines under training-aware conditions. The theoretical guarantees do not translate into a training advantage in the tested regime.

**3. Experiments test top-$k$ selection, not the $\varepsilon$-threshold universal set.**  
The theoretical result is threshold-based: $U$ contains all keys with $f$-sensitivity $\ge \varepsilon$, and its size is bounded by $\Psi^f / \varepsilon$. The experiments instead always select a fixed number of top-$k$ keys (32, 64, 128) by leverage score, with no analysis of what $\varepsilon$ these $k$ values correspond to or whether the universal set property holds at that threshold. This makes it harder to connect the empirical results to the theoretical claim.

### Minor

**1. Planted model section is loosely integrated.**  
Section 4 introduces a separate set of assumptions (noisy linear combinations, correlation constraints, row-norm-based selection criteria) and a different algorithm using Johnson-Lindenstrauss sketches. While it does leverage the connection to leverage scores (it identifies keys with large leverage scores as "relevant"), the section reads as a standalone contribution rather than building naturally on the universal set result. The paper would benefit from explicitly tying the planted model back to the $f$-sensitivity framework (e.g., showing that under the planted assumptions, the relevant keys are precisely those in the universal set).

**2. Frequency of leverage score recomputation during training is underspecified.**  
The paper says "we compute the keys with the 32 largest $\ell_2$ leverage scores at each attention head" when training from scratch, but does not state whether this is done at every training step, every few steps, or only once. Since the key matrix $K$ changes during training, the frequency affects both the computational cost and the validity of the selection.

**3. Warm-start overhead is not quantified.**  
For L/8 and L/16, the first ~15% of training steps use full attention. The paper reports that selection is used for the remaining 85% of steps, but never reports the total training time or FLOPs to account for the overhead of the warm-start phase.

**4. Streaming algorithm memory-bound description could be sharper.**  
The 1-pass algorithm is described as using "$\text{poly}(d/\varepsilon)$" memory, but this is unpacked later into $O(d^3 \log n)$ words (depending on the online condition number bound). The phrasing "$\text{poly}(d/\varepsilon)$" is technically correct but hides dependence on $\log n$ that is non-trivial for practitioners.

### Trivial

None.

## Nice-to-Haves

- A small-scale experiment on polynomial attention (e.g., $f(x)=x^2$ or $f(x)=x^4$ in a simplified transformer) would directly validate the universal set theorem and complement the softmax heuristic experiments.
- Using $\varepsilon$-threshold selection (rather than top-$k$) and reporting what $\varepsilon$ values emerge from choosing $k=32,64,128$ would strengthen the empirical-theoretical connection.
- A brief discussion of *why* training-aware selection might not exploit the universal set property (e.g., the universal set is about threshold-based heavy scores, while top-$k$ selection is a different knapsack-style constraint) would turn the negative training result into a clearer research direction.

## Removed Points

- **"The paper does not make any assumptions on the data, but the streaming 1-pass bound assumes integer entries with bounded precision."** — This is a standard assumption in streaming literature to obtain meaningful memory bounds; the paper states it explicitly. Not a weakness.
- **"The Huber/Tukey remark feels tangential."** — This remark (line 162) cites Musco et al. (2022) to show that the framework generalizes beyond $|x|^p$ to other functions. It is a concise pointer to related work, which is standard. Move to Nice-to-Haves at most.
- **"[The paper] should have a direct experimental test of the universal set property itself"** — This is subsumed by Major weakness #1 and is listed as a suggestion in Nice-to-Haves. Not a distinct weakness.
- **Strength Finder's claim that experiments "confirm that the theoretical superiority of leverage scores... translates to real-world gains"** — Overstated given Major weakness #2 (training experiments match baselines) and #1 (softmax vs. polynomial attention). The strength is kept but qualified: the pretrained-model comparison *does* show a clear advantage over row-norm, and this is a genuine contribution.

## Novel Insights

The key insight — that for attention functions where the output is a normalized non-negative combination of $f$-transformed inner products, the $f$-sensitivities of the key matrix alone (independent of any query) bound all possible large attention entries through a universal set — is genuinely novel and elegantly connects tools from randomized numerical linear algebra (leverage scores, Lewis weights) to transformer efficiency. The observation that the universal set can be computed in a streaming or distributed setting with memory independent of $n$ is a non-obvious algorithmic consequence.

## Suggestions

1. Add a paragraph explicitly acknowledging that the experiments test a heuristic (leverage scores for softmax attention) rather than a direct consequence of the theory, and explain why leverage scores might still be a reasonable heuristic (e.g., because attention matrices in ViTs often have sub-structure captured by row-space properties of $K$).
2. Specify the frequency of leverage score recomputation during training (every step? every $t$ steps? once per epoch?) to improve reproducibility.
3. Report the total training FLOPs or wall-clock time for the warm-start procedure to quantify the actual efficiency gain.
4. Consider adding a small-scale experiment on $f(x)=x^2$ attention (even on a synthetic task) to directly demonstrate the universal set property.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>