## Summary

This paper addresses the problem of locating the \(k\) largest/smallest elements in a tensor given in CP (CANDECOMP/PARAFAC) format. It proposes a continuous optimization model (Theorem 1) that reformulates element location as a spherical constrained optimization over the factor matrices, avoiding the CP-rank growth that plagues prior eigenvector-based approaches. On top of this model, the paper develops an alternating iterative method with a maximal block improvement (MBI) strategy (Algorithm 1) that guarantees convergence, and a block-search variant (Algorithm 2) that searches multiple fibers per iteration for improved accuracy. Experiments on synthetic and real-world tensors demonstrate order-of-magnitude speedups over power iteration, star sampling, and MinCPD baselines.

## Strengths

1. **The continuous optimization model avoids the rank-growth bottleneck of prior methods.** Theorem 1 (lines 51–59) converts the extreme-element location problem into a spherical constrained optimization over factor matrices, where objective evaluation costs only \(O(\sum_n I_n R)\) vector-vector multiplications. This cleanly eliminates the Hadamard-product-induced rank growth that forces prior eigenvector approaches (Espig et al., 2013) to perform expensive recompression. This is the paper's central methodological contribution and is well-articulated.

2. **Convergence-guaranteed alternating algorithm with explicit theory.** Algorithm 1's MBI selection rule (updating the variable with the largest Rayleigh quotient) avoids the known failure of predetermined-order alternating iteration (Chen et al., 2012; Higham & Relton, 2016). Theorem 2 proves global convergence to a stationary point from any initialization, and Theorem 3 establishes local R-linear convergence. This is a provably stronger guarantee than the existing PGD-based approach (Sidiropoulos et al., 2022), whose accuracy depends on step-size tuning.

3. **Order-of-magnitude speedups on large-scale tensors.** On tensors from multivariate functions (dimension 10, grid size 4096), the proposed algorithms achieve \(41.9\times\)–\(176.0\times\) speedups over power iteration, \(7.4\times\)–\(27.7\times\) over star sampling, and \(11.02\times\)–\(778.52\times\) over MinCPD (Table 2/line 189). These speedups are substantial and arise from the per-iteration cost of \(O(\sum_n I_n R)\) versus power iteration's recompression overhead.

4. **Simultaneous handling of both largest and smallest elements.** The continuous optimization model naturally handles both minimization and maximization (line 59), whereas power iteration and star sampling can only find the maximum. The experiments confirm this advantage (Tables 1–2), with Algorithm 2 achieving up to 266.7% improvement in locating the smallest element over MinCPD.

5. **Block-search strategy delivers consistent accuracy improvements across settings.** The block-search variant (Algorithm 2) improves accuracy by 14.3%–266.7% over MinCPD and star sampling on random and real-world tensors (Tables 1, 4), and the paper demonstrates insensitivity to the block size parameter \(b\) (line 170).

## Weaknesses

### Major
None.

### Minor

1. **No ablation isolating the plain alternating baseline.** The paper describes a "plain alternating iterative method" (line 67) and states it can fail with predetermined update order (line 82, citing Chen et al., 2012), but never implements or tests it as a standalone baseline. Algorithm 1 (MBI) is compared only against external baselines (power iteration, star sampling, MinCPD), never against the plain alternating method. This means we cannot attribute the reported accuracy gains to the MBI strategy specifically versus the alternating structure itself. While the paper's main claim is superiority over *existing* methods rather than over its own stripped version, this omission makes the narrative about MBI's role partially unsubstantiated. *Effect: moderate experimental gap.*

2. **Overclaimed generality to Tucker/TT/QTT formats.** The abstract (line 18), contributions paragraph (line 22), and conclusion (line 220) state or imply that the proposed methods "could naturally apply" or are "more general" and can be "naturally applied" to Tucker, tensor-train, and tensor ring formats. However, every derivation and experiment is on CP-format tensors only. The paper explicitly says "We leave them for future work" (line 59), which undercuts the generality claim as a current contribution. The language in lines 18 and 22 should be tempered to match what is actually delivered. *Effect: scope mismatch between advertised contributions and experimental content.*

3. **Ambiguous accuracy definition for the \(k\)-largest experiments.** Line 203 defines accuracy as \(\#\text{hit}/k\), where \(\#\text{hit}\) is "the number of values found by each algorithm that are smaller than the \(k\)-th largest element." For a top-\(k\) location task, counting values *smaller than* the \(k\)-th largest counts misses, not hits, making the definition as rendered logically inverted. This is very likely a parser artifact (the original submission almost certainly uses a correct definition), but as presented the reader cannot interpret the real-world accuracy numbers in Table 4 with confidence. The authors should clarify the intended definition. *Effect: a portion of the experimental results is unverifiable from the text.*

4. **No variance or confidence-interval reporting.** The synthetic experiments (Section 5.1) report accuracy over 50 random tensors but provide no standard deviation, variance, or confidence intervals. The real-world experiments (Section 5.3) report single point estimates per tensor. Without variance information, the reported improvements (e.g., "up to 48.2% and 266.7%") cannot be assessed for statistical reliability. This is especially important given the use of random restarts and random tensor instances. *Effect: limits the evidentiary strength of the quantitative claims.*

5. **Missing explanation of how CP representations are derived for multivariate functions.** Section 5.2 (line 187) states that the CP representation of 10-dimensional Rastrigin/Schwefel tensors on a 4096-point grid "can be derived from Eq. 5.1" but provides no derivation or reference. It is not obvious how a 10-dimensional function sampled on a \(4096^{10}\) grid yields an exact CP representation, and whether this representation is exact or approximate matters for the validity of the comparison. *Effect: reproducibility concern for the large-scale experiments.*

6. **No discussion of CP-ALS approximation error in real-world tensors.** The real-world tensors (Section 5.3) are converted to CP format via CP-ALS, which introduces approximation error. The paper does not discuss how this approximation error could affect the accuracy of extreme-element localization or whether it interacts differently with the tested algorithms. *Effect: completeness gap in experimental methodology.*

### Trivial

- Theorem 1's equation (lines 53–55) states the optimization problem without showing the spherical constraints \(\|\mathbf{x}^{(n)}\|_2 = 1\) in the equation itself; they are mentioned only in the surrounding text. The constraint should appear explicitly in the theorem display.
- Algorithm 2's pseudocode (line 106) contains garbled indexing, making it difficult to parse the logic of multi-fiber candidate tracking across modes.

## Nice-to-Haves

- The greedy extension for \(k > 1\) comes with the acknowledged limitation that CP-rank grows with each shift transformation (line 137), restricting it to small \(k\). This is an honest limitation rather than a weakness of the paper, but the authors could discuss whether alternative strategies (e.g., orthogonalization constraints solved approximately) could extend the range.
- A sensitivity analysis for the block size \(b\) beyond the three values tested \((3,5,7)\) on a single experimental setting would strengthen Algorithm 2's characterization.

## Removed Points

These points were considered and removed because they are either not supported by the paper as written, misunderstanding the content, or fall under explicit removal rules:

- *The greedy extension is a fundamental limitation because real applications need large k.* — The paper explicitly acknowledges this limitation (line 137). The criticism restates a known scope boundary; it does not identify a flaw in what the paper claims.
- *Algorithm 1's hard one-hot update is a weakness* — The paper explains this is equivalent to "searching for the largest element from the fibers" (line 91) and explicitly cites Higham & Relton (2016) showing that this can miss global optima. This is a stated characteristic of the algorithm, not an unacknowledged flaw.
- *The convergence theorems are "standard" and provide no insight* — All convergence analyses for coordinate-type methods build on established frameworks. The paper's theorems are appropriate for its scope and more than what most applied-method papers provide.
- *"At time of writing, the models cited may not exist" or similar reproducibility concerns* — All cited models, baselines, datasets, and references are assumed to exist per the review instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected concerns about ablation completeness and scope overclaim but do not identify any structural flaw or unnoticed synthesis that the paper itself misses.

## Suggestions

1. **Add an ablation experiment.** Implement the plain alternating method (predetermined cyclic order) and report its accuracy and runtime alongside Algorithm 1 (MBI) and Algorithm 2 (MBI + block-search) on the same synthetic tensors from Section 5.1. This would isolate the contribution of the MBI ordering strategy.
2. **Temper the generality claims.** Replace statements like "could naturally apply to other tensor formats" in the abstract/contributions with language that accurately reflects what is currently demonstrated (CP format), while retaining the formats as future work.
3. **Clarify the \(k\)-largest accuracy definition** in Section 5.3. Ensure the definition unambiguously counts elements that belong to the true top-\(k\) set.
4. **Add standard deviation or quartile reporting** to the synthetic experiment results across the 50 random tensors.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>