Now I have all the information needed to produce the consolidated review.

## Summary

The paper proposes LoLoRA, which replaces the frozen LoRA-FA A matrix with a Hebbian-style (HPCA) online update during the forward pass. This avoids storing A's input activations for backprop (same memory savings as LoRA-FA) while learning the PCA subspace of the inputs on the fly — removing the need for an offline PCA pass. Theorem 4.4 proves that, under an isotropic random-target assumption, the optimal A initializations are nonsingular transforms of the top-r input eigenvectors, providing theoretical grounding for both EVA initialization and HPCA updates.

## Strengths

1. **Clean theoretical characterization of optimal A (Theorem 4.4).** The paper proves that under a random regression model with i.i.d. Gaussian ΔW₀, optimal A matrices are any nonsingular linear transformation of the first r eigenvectors of the input covariance. This is the first rigorous justification I am aware of for why PCA-based A initializations (EVA) are principled, and it also explains why HPCA — which converges to the same subspace — is a sensible online substitute. The proof connects a line of empirical observations (PiSSA, EVA) to a formal statement.

2. **Systematic ablation of initializations and local update rules (Tables 5, 6).** The paper compares four A initializations (Uniform, Orthogonal, PiSSA, EVA) and five local update rules (HPCA with/without centering, Autoencoder, SoftHebb, SVD-first) on TinyLlama-1.1B. The ablation cleanly shows that (a) EVA initialization dominates other frozen-A initializations, and (b) HPCA and autoencoder — both converging to the PCA subspace — perform best among local rules, consistent with the theory. This is a useful empirical map for anyone working on non-backprop updates in LoRA.

3. **Clear algorithm (Algorithm 1) for memory-efficient forward-pass updates.** The procedure specifies: compute z→Az, apply local gradient to A and step immediately, then free z before the backward pass (retaining only u=Az for B's gradient). This is a concrete, implementable recipe that makes the memory-accounting transparent.

4. **Demonstrates that online HPCA can match EVA initialization without offline PCA.** On TinyLlama ablation (r=2: 2.557 vs 2.558), MetaMathQA (both 82.9%), and LLaVA (2.93 vs 2.92), LoLoRA matches EVA-initialized LoRA-FA within standard deviation. For practitioners who prefer to avoid a separate PCA pre-computation, this is a legitimate convenience.

## Weaknesses

### Major

1. **Central claims are overstated relative to the evidence.** The abstract states LoLoRA "further reduc[es] the memory required for fine-tuning," but LoLoRA uses the same memory as LoRA-FA (26 GB in Table 3) or slightly more (24.1 GB vs 23.9 GB in Table 4). The conclusion claims HPCA "consistently outperforms standard LoRA-FA in two out of three experimental setups," but on GLUE (the first setup), LoLoRA is actually *worse* than LoRA-FA (uniform) on 5 of 8 tasks (CoLA, RTE, MNLI, QQP, SST-2), and the two tasks where LoLoRA leads (MRPC, QNLI) are within standard deviation. The performance story is one of approximate parity with the best static baseline (EVA), not consistent improvement. These overstatements undermine reader trust. The paper should reframe its contribution as achieving LoRA-FA (EVA) performance while avoiding an offline PCA pass — a practical convenience — rather than claiming performance or memory advantages over LoRA-FA.

2. **No experiment tests the stated motivation for online updates.** The paper motivates local updates by saying they "allow it to adapt to input distribution shifts" (abstract). Yet every experiment uses standard static datasets with no distribution shift. The core thesis — that online adaptation matters when the input distribution changes during fine-tuning — is never tested. Without such an experiment, the reader cannot distinguish LoLoRA from "EVA but computed incrementally," which reduces the novelty to an implementation detail. A distribution-shift experiment (mixed-domain curriculum, multi-task switching, or eval under covariate shift) would directly test this.

3. **Statistical significance is unaddressed for very small effect sizes.** Across all experiments, the differences between LoLoRA and LoRA-FA (EVA) are tiny: 0.001 in perplexity (Table 5 vs 6), 0.0% in accuracy (Table 3), 0.01 in Matthews (Table 1). Standard deviations overlap. No statistical test is performed. Given the small magnitudes, many of the reported "advantages" are indistinguishable from noise. This matters because the paper's entire case for the method's value (versus EVA initialization + freeze) rests on these marginal differences.

### Minor

1. **Memory framing conflates LoLoRA's contribution with LoRA-FA's.** The memory reduction relative to standard LoRA (13–20%) comes from freezing A's backward pass — which LoRA-FA already does. LoLoRA's novel component (the forward-pass update) adds a small optimizer state for A (hence 24.1 GB vs 23.9 GB for LoRA-FA in Table 4). The paper should explicitly separate the two: the memory saving is inherited from LoRA-FA; the local update is an alternative to the offline PCA pass, not a further memory reduction.

2. **Missing baselines.** VeRA, AdaLoRA, or gradient checkpointing are not compared. Since the claim is about efficiency, comparing to other memory-reducing PEFT methods would strengthen the positioning. VeRA in particular uses fewer parameters than LoRA and is highly relevant.

3. **Theorem 4.4 assumes i.i.d. Gaussian ΔW₀, which is unrealistic.** The authors acknowledge this in the limitations, but the assumption is very strong — real fine-tuning weight changes are structured and task-dependent. Under this assumption, the optimal A depends only on the input covariance, not on the task targets. In practice, targets matter, and the theorem's direct applicability to real settings is unclear. The result is best viewed as a theoretical complement to empirical observations, not as a practical guarantee.

4. **Table 6 (local rules ablation) does not include the most directly relevant baseline — LoRA-FA (EVA).** The reader has to cross-reference Table 5 to see that LoRA-FA (EVA) gives 2.558 at r=2, while LoLoRA HPCA gives 2.557. Including LoRA-FA (EVA) in the same table would make the comparison immediate and honest.

### Trivial

None.

## Nice-to-Haves

- An experiment with deliberate input distribution shift (e.g., training on interleaved domains, or curriculum from easy to hard) that directly tests whether the online HPCA adaptation outperforms a static EVA subspace.
- A breakdown of "Extra Memory" showing activation memory vs. optimizer state vs. local-update overhead.
- A paired significance test (e.g., bootstrap or t-test) for the comparisons with the strongest baselines.

## Removed Points

- **Criticism that the paper lacks comparison to LoRA-FA (EVA) in ablations (Table 6):** The critic claimed Table 6 does not include LoRA-FA (EVA) results. This is correct — Table 6 only shows local update rules. However, Table 5 (separate table on the same page) provides LoRA-FA (EVA) results, so the comparison is available to a careful reader. Kept as a minor weakness because including them in the same table would be better, but the reviewer's framing as a major gap was too strong.
- **Criticism about missing related works (VeRA, AdaLoRA):** The paper does cite some related works on parameter sharing (Kopiczko et al., 2024 — VeRA's authors) and adaptive ranking (Zhang et al., 2023a;c; Renduchintala et al., 2024 — AdaLoRA-style). The scope is acknowledged as limited. Moved to Minor as a missing-baseline concern rather than removed entirely.
- **Criticism about the paper's font/formatting:** Not present in this submission; parser artifacts are not author errors.
- **Strength Finder's generic strength about "the paper addressed an important problem":** Removed as generic/insubstantial.
- **Strength Finder's claim about Algorithm 1 as a separate strength:** The algorithm is clear but is a standard part of describing any method, not a standalone contribution. Merged its content into the strengths summary.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Re-frame the contribution** as "a method that matches EVA-initialized LoRA-FA performance while learning the PCA subspace online, avoiding a separate pre-processing pass." Remove or qualify claims of "further reducing memory" and "consistently outperforming" where unsupported.
2. **Add a distribution-shift experiment** to directly test the online adaptation rationale. For example, train on mixed-domain instructions (Alpaca → Math → Code) and compare HPCA's trajectory to a static EVA subspace.
3. **Include LoRA-FA (EVA) directly in Table 6** so readers can see the frozen-vs-local comparison without cross-referencing.
4. **Report statistical significance** (e.g., paired bootstrap) for the main comparisons, especially given the small effect sizes.
5. **Add memory-component breakdown** as a supplementary table showing activation, optimizer, and local-update contributions for each method.

## Score and Decision

**Round 1 bracket:** I queried three bands of human-review anchors on LoRA/PEFT topics. Weak anchors (avg ≤3.5): papers at 3.0–3.33, generally rejected for fundamental flaws. Middle anchors (3.5–7.5): LoRA-FA paper at 5.33 (rejected), EVA paper at 4.75 (rejected), ReLoRA at 5.75 (accepted), FLoRA at 5.75 (accepted), ROSA at 6.0 (rejected). Strong anchors (≥7.5): VeRA at 7.25 (accepted), HiRA at 8.0 (accepted). LoLoRA is clearly above the weak band and clearly below the strong band. Initial bracket: 4.5–6.5.

**Round 2 narrowing:** I pulled anchors inside (4.0–6.5) and (5.0–7.0) on topics closely related to the paper's contributions. Direct comparison:
- **LoRA-FA paper (5.33, rejected):** Proposes freezing A for memory savings. LoLoRA improves on this by replacing the frozen random A with online HPCA and adding theoretical justification. LoLoRA is a clear step up → scores above 5.33.
- **EVA paper (4.75, rejected):** Proposes data-driven PCA initialization without theory and without online updates. LoLoRA provides the theory and the online update — a substantial improvement → scores well above 4.75.
- **ReLoRA (5.75, accepted):** Memory savings with comparable quality via cyclic merge/reinitialize. ReLoRA's experiments more convincingly demonstrate its efficiency advantage, while LoLoRA's claimed advantages over the strongest baseline (EVA) are marginal. LoLoRA is slightly weaker → scores below 5.75.
- **FLoRA (5.75, accepted):** Generalizes LoRA to higher-dimensional parameter spaces with strong multi-domain experiments. LoLoRA's GLUE results and missing baselines are less compelling. → scores below 5.75.
- **ROSA (6.0, rejected):** Strong theory but practicality concerns. LoLoRA has similar issues (incremental over baselines) → comparable range.

The narrowing places the paper between 5.33 (LoRA-FA) and 5.75 (ReLoRA/FLoRA). The paper's real contributions — the theoretical result, the systematic ablation, and matching EVA without offline computation — are solid. However, the overclaiming of memory and performance advantages, the lack of a distribution-shift experiment to validate the online rationale, and unaddressed statistical significance pull the score toward the lower end of this range.

**Final score: 5.0** — a paper with genuine theoretical and empirical contributions that is held back by narrative overreach and a mismatch between claimed advantages and demonstrated evidence. The method is comparably performant to a simpler baseline with a clever initialization, and the paper would benefit from honest reframing and targeted additional experiments.

**Calibration anchors consulted:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| HoLoRA | igGeaxOiFM | 3.00 | 1 | Far weaker — fundamental method flaws |
| ALLoRA | 7X65yoKl3Y | 3.33 | 1 | Far weaker — identified fatal flaws |
| UnoLoRA | 49ti6LOUw5 | 3.00 | 1 | Far weaker |
| L-MSA | xi3sDtf8A0 | 3.00 | 1 | Far weaker |
| FLoRA (Struct. Integrity) | OALIb8oNfl | 5.75 | 1 | Stronger — more convincing multi-domain experiments |
| ReLoRA | DLJznSp6X3 | 5.75 | 1 | Stronger — clearer efficiency demonstration |
| VeRA | NjNfLdxr3A | 7.25 | 1 | Stronger — clear parameter reduction with matched performance |
| ULoRA | bYsieh8LE2 | 3.67 | 1 | Weaker — limited applicability |
| EVA init. paper | DM6Q45HWSk | 4.75 | 2 | Weaker — no theory, no online updates, smaller experiments |
| PaCA | iYkhxre0In | 6.00 | 2 | Stronger — addresses latency, better experiments |
| GLoRA | NXnNiT0fdp | 4.75 | 2 | Comparable — similar overclaiming issues |
| ROSA | cgCKm5DOnu | 6.00 | 2 | Comparable range but different approach |
| LoRA-FA paper | RbKThNNFxr | 5.33 | 2 | Weaker — no theory, no local updates, smaller scope |
| SGD fine-tuning | ZTssMmhC2X | 6.40 | 2 | Stronger — more rigorous experiments |
| Conv filter tuning | E5YmIBvOqV | 6.00 | 2 | Stronger — clearer contribution |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>