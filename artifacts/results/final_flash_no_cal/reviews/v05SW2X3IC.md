## Summary

This paper proposes a learnable instantiation of the Gray-Wyner network for multi-task compression, combining one common channel and two private channels to separate shared and task-specific information. The authors derive new information-theoretic bounds on lossy common information (Theorem 1), a simplified optimization objective with a single Lagrangian parameter \(\beta\) controlling the transmit-receive rate tradeoff (Theorem 2, Eq. 12), and a neural architecture that implements this framework via a matching mechanism on the common channel. Experiments on synthetic data, colored MNIST, Cityscapes, and COCO validate that the approach isolates common information and substantially reduces transmit rate relative to independent coding baselines.

## Strengths

1. **Novel theoretical bounds for lossy common information (Theorem 1).**  
   The paper extends Wyner's lossless result to the lossy setting, bounding Gács-Körner and Wyner's lossy common information via interaction information (Eqs. 6–7). This provides a principled information-theoretic foundation for the transmit-receive tradeoff that the rest of the paper exploits.

2. **Clean optimization objective with a single tradeoff parameter (Theorem 2, Eq. 12).**  
   Under deterministic encoders, the Gray-Wyner objective simplifies to entropy terms (Eq. 10). The Lagrangian relaxation (Eq. 12) introduces a single hyper-parameter \(\beta\) that spans transmit-rate optimization (\(\beta=1\)), receive-rate optimization (\(\beta=2\)), or a mixture (\(\beta=3/2\)). This is elegant and directly tunable in practice.

3. **Architecture design that demonstrably separates common and private information.**  
   The matching mechanism (Eq. 14) plus auxiliary MSE loss (Eq. 15) forces the two encoder branches to agree on the common channel elements. Figure 3a confirms that the proposed Shared architecture produces common-channel rates that track the empirical mutual information, unlike the Separated and Combined ablations.

4. **Controlled edge-case validation via colored MNIST (Section 4.2).**  
   The three PMFs with known mutual information (zero, full, partial) provide a clean sanity check: the codec correctly places information on the common channel according to the true dependency structure, confirming that the \(\beta\) formulation behaves as theory predicts.

5. **Consistent transmit-rate advantage over independent coding.**  
   Across the Cityscapes and COCO experiments, the proposed method substantially outperforms the Independent baseline and approaches the Joint upper bound (Figure 5). The average \(-81.58\%\) BD-rate advantage in transmit rate (against single-task codecs) is a meaningful efficiency gain, though the baseline specification could be clearer (discussed below).

## Weaknesses

### Fatal
None.

### Major

1. **No experimental comparison against related multi-task codec methods.**  
   The Related Work section surveys two relevant families: *coding for humans and machines* (Choi & Bajic 2022, Foroutan et al. 2023, de Andrade & Bajic 2024) and *multitask learnable codecs* (Chamain et al. 2021, Feng et al. 2022, Guo et al. 2024). While the paper's framing (three-channel split with private channels) differs from these works (two-channel or common-channel-only designs), the experiments compare exclusively against trivial baselines (Joint and Independent). The practical advantage of the Gray-Wyner formulation relative to existing practical codecs is therefore unsubstantiated. Including at least one representative from these families would significantly strengthen the claim that the proposed approach is practically valuable.  The paper's claims are scoped honestly (it claims only to beat *independent* coding), but the disconnect between the Related Work and the experimental evaluation undermines the paper's stated goal of "bridging classic information theory with task-driven representation learning."

2. **No statistical rigor (confidence intervals, standard deviations, or multiple-seed averages).**  
   No error bars or variance information is reported for any BD-rate number or rate-distortion curve. Given the well-known training variance in learned compression, single-curve comparisons are insufficient to establish reliability. The oscillations in the Cityscapes curves (Section 4.3) are attributed informally to regularization effects, but this observation would be more convincing backed by variance estimates.  This concern is moderately serious because the paper's headline quantitative claims (e.g., \(-81.58\%\) BD-rate) could shift substantially across runs.

### Minor

3. **The common-channel construction is a heuristic with limited theoretical grounding.**  
   The matching mechanism (Eq. 14)—averaging matching elements and zeroing non-matching ones, plus an MSE auxiliary loss—is an engineering choice. The paper does not explain how this procedure guarantees representations satisfying the Markov conditions of Theorem 1 (Eqs. 3, 5). An architecture that directly optimizes a variational bound on the relevant mutual informations would be a more principled instantiation. The ablation study (Section 4.1) shows the Shared architecture outperforms Separated and Combined alternatives, but it does not ablate the mask mechanism itself (e.g., comparing against simple addition or learned gating). This limits insight into which component of the design is responsible for the improvement.

4. **The headline \(-81.58\%\) BD-rate claim needs clarification.**  
   The conclusion states this is "against single-task codecs," which refers to the Independent baseline. However, the BD-rates in Figure 5 are computed *with respect to the Joint method*, not directly against Independent. The exact computation behind the \(-81.58\%\) number and which specific experiments it averages over should be stated explicitly to avoid confusion.

5. **Role of \(\beta\) in the architecture is not fully validated.**  
   Section 4.1 shows that \(\beta=3/2\) works well for the synthetic task, but the main computer-vision experiments (Section 4.3) only report results for \(\beta=1\) (Transmit) and \(\beta=2\) (Receive)—the mixed \(\beta=3/2\) is not included in Figure 5. Since the ability to navigate the transmit-receive tradeoff is a core contribution, evaluating \(\beta=3/2\) on real benchmarks would strengthen the paper.

### Trivial
None.

## Nice-to-Haves

- **Ablation of the mask mechanism:** Comparing Eq. 14 against alternatives (simple addition, learned gating) would clarify whether the hard-zero masking or the MSE loss is responsible for the observed behavior.
- **Limitation discussion:** A brief paragraph acknowledging the fragility of the \(Y_0\) construction (sensitivity to \(\gamma\)) and noting that Theorem 2 assumes the existence of optimal models in the function families would help readers gauge the generality of the method.
- **\(\beta=3/2\) on Cityscapes/COCO:** Including the mixed tradeoff in Figure 5 would complete the empirical picture of the transmit-receive tradeoff on real tasks.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Training-detail criticism (hyper-parameter ranges, optimizer, training steps).** The paper points to Appendix D for these details; the parser strips all appendix content. Per the hard rules, criticisms about information deferred to a (now-absent) appendix are removed.
- **"The \(-81.58\%\) claim is misleading without specifying the baseline."** The paper does state "against single-task codecs," which identifies the Independent baseline. While the phrasing could be more precise, this is not misleading to the extent the harsh critic asserts.
- **"Strong assumptions of Theorem 2 should be acknowledged, not only the appendix."** The assumptions (deterministic functions, existence of optimal models) are stated in the theorem statement itself (Section 3.2), so this criticism is factually incorrect.
- **"Architecture is a heuristic loosely moored to the theory."** This is kept in the Minor section above but the harsh critic's stronger characterization as an "engineering patch" is moderated. The architecture is a reasonable instantiation given the practical difficulties of directly optimizing mutual-information bounds.

## Novel Insights

The single most insightful observation from the cross-review is that the paper's empirical contribution is stronger as a validation of the theoretical framework (the \(\beta\) tradeoff, the common-information bounds) than as a practical codec demonstration. The harsh critic correctly identifies the missing baselines as a gap, but the strength finder correctly identifies that the paper's claims are appropriately scoped to outperform *independent* coding. The synthesis suggests that the paper would benefit from repositioning: it is primarily a theory-to-algorithm contribution validated on simple and moderately complex tasks, not a SOTA codec. The colored MNIST experiment is particularly effective at bridging theory and practice and deserves more emphasis.

## Suggestions

1. **Add at least one comparison to a related multi-task codec** (e.g., the split-encoder design in Foroutan et al. 2023) on the Cityscapes or COCO benchmarks. Even if the settings are not identical, a carefully matched comparison would give readers a concrete sense of practical advantage.
2. **Report BD-rate intervals or standard deviations** over 3–5 seeds for all main experiments.
3. **Include \(\beta=3/2\) results** in the Cityscapes/COCO figure to complete the tradeoff picture.
4. **Clarify the \(-81.58\%\) calculation** by stating the reference baseline and the experiments averaged.
5. **Add a simple ablation of the mask** (e.g., replace Eq. 14 with element-wise addition or learned gating) to isolate the effect of the hard-zero mechanism.

## Score and Decision

**MY FINAL SCORE: <score>6.5</score>**  
**MY FINAL DECISION: <decision>Accept</decision>**