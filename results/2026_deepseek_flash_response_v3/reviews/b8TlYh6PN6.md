## Summary

This paper tackles a genuinely open problem: characterizing distributional equivalence for linear non-Gaussian causal models with **both** arbitrary latent variables **and** cycles. It introduces "edge rank" constraints as a new local tool (dual to the well-known path ranks), derives a graphical criterion (Theorem 2) that reduces equivalence checking to comparing children bases for the latent set and each observed singleton independently, provides a transformational characterization (Theorem 3 — cycle reversals + edge additions/deletions) akin to the Meek conjecture, and develops the glvLiNG algorithm as a proof-of-concept structural-assumption-free discovery method. The theoretical framework is coherent, novel, and well-motivated.

## Strengths

1. **First distributional equivalence characterization handling both arbitrary latent structure and cycles (Theorem 2).** Prior work handled cycles without latents (Lacerda et al., 2008) or gave only unique-identifiability conditions (Adams et al., 2021). This paper provides a necessary and sufficient graphical criterion that is both principled and tractable — reducing exponentially many checks to |X|+1. The connection to the classical causally-sufficient case (L=∅) is clearly shown.

2. **Edge rank constraints and the duality theorem (Definition 4, Theorem 1).** Edge ranks are a genuinely new local tool that complements path ranks. Theorem 1 establishes a clean duality between the two, and Lemma 4 connects edge ranks to matching ranks of binary support matrices. This contribution extends beyond the paper's specific setting and enriches the rank-based toolbox for causal discovery.

3. **Clean transformational characterization (Theorem 3) with "at most one cycle reversal."** The result that equivalence is fully characterized by admissible cycle reversals and edge additions/deletions is non-trivial given the complexity illustrated in Example 1, and directly enables equivalence class traversal. The pillar/coloop intuition for edge additions is well-explained.

4. **Clean irreducibility characterization and reduction procedure (Propositions 1, 2).** The paper cleanly separates inherent non-identifiability (trivial additions of redundant latents) from structural equivalence, using a simple graphical condition and an explicit reduction procedure. This is done without imposing structural assumptions.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The critical Lemma 5 → Theorem 2 reduction lacks a proof sketch in the main text.** The paper states that edge ranks allow "instead of checking all subsets $x \subseteq X$, it suffices to check each singleton $X_i \in X$ independently" and declares "Fortunately, this time, the answer is yes" (line 248), but offers no intuition for why this non-trivial combinatorial compression holds. Since this is the linchpin of the entire graphical criterion, a brief sketch (even 3–5 sentences) in the main text would greatly increase reader confidence. The full proof is deferred to the appendix (standard practice), but the gap between "check all subsets" and "check singletons" is large enough that some intermediate reasoning would benefit readers.

2. **No quantitative results appear in the main text.** All tables, error bars, and comparisons (runtime, baseline comparisons under oracle inputs, finite-sample performance) are deferred to the appendix. While the paper honestly frames glvLiNG as a "proof of concept" (line 328) and the main contribution is theoretical, the abstract's claim of "the first structural-assumption-free discovery method" implies practical viability. Moving even one summary table (e.g., F1 vs. sample size) into the main text would substantially strengthen the applied claim.

3. **Transition from Lemma 3 (path ranks) to Lemma 5 (edge ranks) is not shown.** The paper says "let us rephrase Lemma 3 using edge ranks below" (line 232) but simply states Lemma 5 without showing how the duality theorem converts the path-rank conditions to edge-rank conditions with the $L \subseteq Y$ restriction. A brief derivation or even a note about which substitution is needed would improve transparency.

### Trivial
None.

## Nice-to-Haves
- A richer limitations discussion covering (a) what happens when OICA returns a wrong number of latents (a known failure mode), (b) how glvLiNG degrades with increasing dimensionality beyond n=10, and (c) whether equivalence classes can be so large as to be diagnostically uninformative.
- A discussion of whether the characterization can recover Adams et al.'s (2021) uniqueness conditions as a special case.

## Removed Points
- **"Structural-assumption-free label may be misleading":** The paper explicitly defines "structural assumptions" on lines 19–23 (measurement models, hierarchy, acyclicity, etc.) and distinguishes them from parametric assumptions (linearity, non-Gaussianity). The claim is technically precise and the paper is transparent about its remaining assumptions. This criticism reflects a potential reader misinterpretation, not an author error.
- **"Proof of Theorem 2 is in the appendix":** The parser strips appendix content from all papers; the proof exists in the original submission. The hard rule mandates removing weaknesses about missing appendix contents.
- **Strength Finder's generic statements** about problem importance and motivation: These lack specific content tied to the paper and could apply to many papers in the area.

## Novel Insights

The reviews surface an interesting meta-point about how to evaluate theoretical papers with algorithmic components. The harsh critic correctly identifies that the paper's main contribution is the equivalence characterization, not the algorithm, and evaluates against that standard. However, the critic then applies applied-evidence standards to the algorithm's claim. The strength finder correctly identifies the theoretical contributions but overstates the algorithmic evidence. The real insight is that the paper sits in an awkward middle zone: it is primarily theoretical but makes applied claims in the abstract, leaving it vulnerable to criticism from both directions. The authors would benefit from either leaning fully into the theory framing (and toning down applied claims) or investing in stronger empirical support for the algorithm.

## Suggestions

1. **Add a brief proof sketch for Theorem 2's local decomposition in §4.** A paragraph explaining why edge ranks enable the reduction from checking all subsets $Y \supseteq L$ to checking only $L$ and $L\cup\{X_i\}$ — perhaps showing how the constraints for arbitrary subsets factor through singleton constraints — would dramatically increase reader confidence in the paper's centerpiece result.

2. **Move one representative empirical result into the main text.** Even a single table (e.g., F1 vs. sample size for glvLiNG and one baseline) would provide concrete evidence for the abstract's applied claim without requiring more experiments.

3. **Show the derivation of Lemma 5 from Lemma 3.** Add a short derivation showing how the duality theorem (Theorem 1) transforms the path-rank condition $\rho_\mathcal{G}(Z,Y) = \rho_\mathcal{H}(Z,\pi(Y))$ into the edge-rank condition $r_\mathcal{G}(Z,Y) = r_\mathcal{H}(\pi(Z),Y)$ with $L\subseteq Y$.

## Score and Decision

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/nHkMm0ywWm.md | 6.50 | R1+R2 | PO-LiNGAM paper — extends LiNGAM to latents but requires acyclicity + pure children. Our paper tackles harder problem (cycles, no structural assumptions). Comparable theoretical depth but our paper's main text has weaker empirical presentation. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/fGhr39bqZa.md | 6.00 | R1+R2 | Homologous surrogates — relaxes pure children but still has structural assumptions. Our paper is more novel and more general. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/BZYIEw4mcY.md | 6.00 | R1+R2 | Efficient causal discovery with latents — has assumptions about latents leaving footprints. Our paper is stronger theoretically. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Bp0HBaMNRl.md | 6.75 | R1+R2 | Differentiable latent hierarchy — different approach, combines theory with practical algorithm. Comparable novelty but our paper lacks the differentiable/scale angle. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Lxst78Rrwj.md | 5.00 | R1 | Distributional invariance — different approach, less ambitious. Our paper is stronger. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/7oT1X8xjIk.md | 5.80 | R1+R2 | Nonlinear representation learning identifiability — different focus, reject despite some good scores. Our paper is stronger. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/k03mB41vyM.md | 6.50 | R2 | Exchangeable mechanisms — different focus (representation learning). Our paper is comparable in quality. |

**Round-1 bracket:** 5.5–7.5 (paper clearly above 2–4 range, comparable to anchors in 5.5–7.5)

**Round-2 narrowing:** Placed at 6.5 — comparable to topically similar accepted papers (PO-LiNGAM at 6.50), slightly above papers with more significant limitations (Homologous Surrogates at 6.00, Efficient Causal Discovery at 6.00). The paper's theoretical novelty (first equivalence characterization with latents + cycles) is genuinely significant, but the presentation gaps (no proof sketch for Theorem 2, no quantitative results in main text) prevent it from reaching the 7+ tier.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>