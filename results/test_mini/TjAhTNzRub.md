## Summary

MoRE proposes a training-free framework for feature-level machine unlearning that combines **(i)** prototype-orthogonal (PO) projection to decorrelate forget and remain prototypes before erasure, **(ii)** a mixture-of-experts remapping mechanism that scatters forget features across multiple remain prototypes to prevent recovery via linear probing, and **(iii)** activation-mean prototypes for efficiency. The method is tested on CIFAR-10, CIFAR-100, Tiny-ImageNet for classification and also extended to diffusion model concept unlearning. The core technical idea—prototype orthogonalization for disentangled feature editing—is elegant and genuinely novel within the unlearning literature.

## Strengths

- **Prototype-orthogonal projection is a well-motivated and effective mechanism for preserving remain utility.** The paper demonstrates empirically (Table 3) that without PO projection, erasing forget prototypes degrades remain accuracy substantially (e.g., D_r drops from 99.94% to 89.52% on CIFAR-10). With PO, both erasing and remapping achieve D_r above 99.8%. Figure 6 corroborates this: remain prototypes retain near-perfect autocorrelation after PO-based unlearning, whereas ESC (Figure 3) collapses remain prototype autocorrelation from 1.0 to 0.52. This is a clean, principled improvement over ESC and related subspace-erasure methods.

- **Remapping with multiple experts achieves very low HM_f under KR evaluation across all datasets.** Under the Knowledge Retention (KR) metric, MoRE achieves HM_f = 0.07 (CIFAR-100) and 0.50 (Tiny-ImageNet), compared to ESC-T's 96.07 and 95.47 respectively (Table 1). This large gap indicates that MoRE's feature scattering is effective at preventing linear-probe recovery, which is the paper's central technical claim. The t-SNE visualizations (Figure 1) support this: ESC leaves a distinct forget cluster, while MoRE disperses forget features across the latent space.

- **Comprehensive ablation study validates each design component.** The paper systematically ablates PO projection, erasing vs. remapping, number of experts (Figure 7), target remapping class (Table 5), and router type (Table 6). The ablation of PO (Table 3) is particularly clean, showing that PO is the critical enabler for both erasing and remapping to work without utility degradation.

- **Linear-time, constant-memory complexity is a practical advantage.** Section 3.4 correctly identifies that MoRE's O(Nd) time and O(dk) memory scaling avoid the O(N_f d) memory bottleneck of ESC, which can cause OOM failures on large forget sets. MoRE completes unlearning in ~9.5s (CIFAR-10), which is faster than ESC (21.5s) and training-based methods (80-100s), while being training-free.

## Weaknesses

### Fatal

None.

### Major

- **The "irreversibility" claim is not qualified for larger-scale datasets, and the paper contains a factual error in its efficiency reporting.**  

  **(a)** On Tiny-ImageNet under the KR setting, MoRE's D_f (forget accuracy as measured by a linear probe on frozen features) is 90.01%—nearly identical to ESC-T (90.57%) and Remap (90.13%). While MoRE's HM_f = 0.50 is dramatically lower than baselines (ESC-T: 95.47), the paper does not acknowledge this tension or explain it. The conclusion states that "MoRE maintains accuracy near random-guess levels," which is simply not supported by the KR D_f values on Tiny-ImageNet (90%, vs. random guess of ~0.5% for 200 classes).  

  **(b)** The main text claims that on CIFAR-10/100, MoRE "consumes less than 200 MB of GPU memory" (line 298). However, Figure 5 reports **540 MB** for MoRE on CIFAR-10. This is a 2.7× discrepancy. All methods in the figure fall in the 447–566 MB range, so "less than 200 MB" appears to be a factual error.

  Since "irreversible" is the paper's headline claim and "efficient/scalable" is a central advertised advantage, these issues are significant.

### Minor

- **Key evaluation metric (HM/HM_f) is defined only in the stripped appendix.** The paper states "Following prior work, we also employ the Harmonic Mean (HM) to measure balanced utility (details in §B.3)" without providing the formula in the main text. While HM can be reverse-engineered from the numbers (HM = harmonic mean of (100−D_f) and D_r), and the metric is standard in the literature, reproducibility demands a self-contained definition. The same applies to the KR metric.

- **MIA results for random data forgetting are overstated.** Table 4 shows that "Remap" achieves MIA = 79.31, while RL achieves 27.99 (lower is better for MIA). The paper claims "comparable or superior performance to existing methods," which is misleading for the MIA metric. While Remap/MoRE does achieve better remain accuracy (D_r: 95.53 vs. 93.66), the MIA gap (79.31 vs. 27.99) is substantial and should be discussed candidly.

- **Diffusion model claims exceed what the quantitative results support.** The paper states that MoRE "outperforms SOTA diffusion model unlearning methods both quantitatively and qualitatively." Quantitatively, MoRE achieves the best LPIPS_d tradeoff (0.25 vs. UCE's 0.20 for Van Gogh), but UCE achieves better LPIPS_r (0.05 vs. 0.08—lower is better for remain distortion). The qualitative claim about "faithfully adhering to the input prompt" is not substantiated by any quantitative metric (e.g., CLIP score or FID). The paper should present these results as "competitive with a favorable tradeoff" rather than categorical outperformance.

- **Efficiency comparison to ESC-T is not discussed fairly.** MoRE takes 9.5s and 540 MB vs. ESC-T's 1.7s and 447 MB on CIFAR-10. While MoRE is training-free and ESC-T requires training, a reader would benefit from an explanation of why a training-free method is slower than a training-based baseline, and whether this matters for practical deployment.

### Trivial

- The stochastic router's input-independence means the same forget image can be routed to different experts across forward passes. The paper does not discuss whether this introduces variance in unlearning outcomes or whether a fixed seed is used at inference time.

## Nice-to-Haves

- Adding CLIP score or FID to the diffusion experiment would substantiate the qualitative claim about prompt faithfulness.
- Analyzing why Tiny-ImageNet resists irreversibility by the D_f metric (e.g., prototype matrix rank deficiency, or insufficient alignment between activation means and forget feature directions) would strengthen the paper's contribution.
- Including a comparison to a wider set of training-free baselines (e.g., SCRUB, BadTeacher variants) would improve coverage.

## Removed Points

- **Criticism about LPIPS_f being worse for MoRE (Harsh Critic #4):** Removed because it is factually wrong. The paper states LPIPS_f: "higher is better." MoRE achieves 0.33 vs. UCE's 0.25, meaning MoRE forgets *more* aggressively. The critic reversed the metric direction.

- **Criticism about MoRE being 5.6× slower and 21% more memory than ESC-T, "undermining the efficiency argument":** Demoted from the severity implied by the critic. MoRE is training-free while ESC-T requires training; the appropriate baseline for a training-free method is ESC (21.5s, 491 MB), against which MoRE is 2.3× faster. The ESC-T comparison is informative but not disqualifying.

- **Criticism about HM being "opaque" and potentially "biased":** Softened. HM = 2·(100−D_f)·D_r / ((100−D_f)+D_r) is the standard harmonic mean formulation used in prior KD literature. It is reverse-engineerable from the numbers. The real issue is it should be in the main text.

- **Strength Finder's claim about zero-shot diffusion achieving "SOTA tradeoff":** Kept in spirit but qualified. MoRE achieves the best LPIPS_d but not the best individual scores. The phrasing "SOTA" in the original strength is removed as too strong.

- **Strength Finder's claim about "linear time and constant memory":** Kept. Verified from Section 3.4.

- **Criticism about Table 4 showing "MoRE" with MIA=79.31: The table actually shows "Remap" (single expert), not MoRE.** However, the paper text claims MoRE, so this is a discrepancy. Incorporated into the Minor weakness about MIA being overstated.

- **Criticism about missing related works, typos/formatting, and stripped appendix content:** Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not produce a synthetic insight that transcends what the paper already states.

## Suggestions

1. **Qualify the irreversibility claim.** Add a sentence in the abstract and conclusion explicitly noting that while MoRE achieves near-perfect HM_f across all datasets (including Tiny-ImageNet), the KR D_f on Tiny-ImageNet remains ~90%, and the method's irreversibility guarantees are strongest on datasets with modest class counts.

2. **Fix the efficiency numbers.** The text says "<200 MB" but Figure 5 shows 540 MB. Reconcile this discrepancy. If the 540 MB includes the base model's memory footprint, clarify and provide the incremental cost separately.

3. **Define HM and KR in the main text.** Even a one-line formula (e.g., HM = 2·(100−D_f)·D_r / ((100−D_f)+D_r)) in §4 would make the paper self-contained.

4. **Tone down the diffusion claims.** Replace "outperforms SOTA diffusion model unlearning methods" with "achieves a competitive utility-forget tradeoff (highest LPIPS_d) while being applied out-of-the-box without diffusion-specific adaptation."

5. **Be candid about the MIA results.** Acknowledge that on the MIA metric, RL outperforms MoRE, and explain why this tradeoff (better utility vs. weaker MIA) is acceptable in the KD task formulation.

6. **Discuss the stochastic router's determinism.** Clarify whether the router uses a fixed seed at inference and whether unlearning outcomes are reproducible.

## Score and Decision

**Calibration anchors used:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Learning to Unlearn (L2UL) | WNUDOLYlbh.md | 3.00 | R1 bracketing | Weaker: no novel method, complex training required |
| Rethinking Unlearning Definition | hvTFoDsgCe.md | 2.50 | R1 bracketing | Weaker: withdrawn, definitional paper only |
| Forget Vectors at Play | m3FOf6nKnU.md | 4.50 | R1 bracketing | Weaker: limited scope, degraded utility |
| Unlearning Isn't Deletion | 7cEMkTu7Lf.md | 4.00 | R1 bracketing | Weaker: evaluation framework without new method |
| REM: Redirection for Erasing Memory | xG0mQ4Xsfm.md | 5.00 | R1 bracketing | Similar: novel redirection mechanism, but MoRE has stronger feature-level theory |
| Memorize to Forget | iKqQGEOeej.md | 5.50 | R2 narrowing | Comparable novelty, but MoRE's PO projection is more technically distinctive |
| Distributional Machine Unlearning | IPqUBL4R9x.md | 6.00 | R2 narrowing | Stronger theory, comparable experimental breadth. MoRE has stronger algorithmic novelty |

**Round 1 bracket:** 4.5 – 6.5 (above weak unlearning papers, below strong papers on unrelated topics).

**Round 2 narrowing:** Compared against Memorize to Forget (5.5) and Distributional Machine Unlearning (6.0). MoRE has stronger algorithmic novelty than Memorize to Forget (criticized for similarity to Task Vectors) and comparable experimental breadth to Distributional Machine Unlearning. The main drags on score are the overclaiming of irreversibility at scale, the efficiency factual error, and presentation issues.

**Final score:** 6.0. The paper makes a genuinely novel technical contribution with a well-motivated method and strong empirical validation on small-to-medium benchmarks. However, the overclaiming on irreversibility and the factual error in efficiency reporting prevent a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>