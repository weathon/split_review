Now I have a thorough understanding of the paper and can verify each claim directly against the text.

Let me compose the final review.

## Summary

This paper introduces the first method for label unlearning in Vertical Federated Learning (VFL), addressing a gap where existing VFU works focus on passive-party removal rather than class-level label unlearning. The method uses manifold mixup to augment few-shot labeled data (e.g., 40 samples) and then applies gradient ascent on the augmented embeddings to erase label influence from both active and passive models. Experiments on MNIST, CIFAR10, CIFAR100, and ModelNet show strong utility/unlearning trade-offs and low runtime.

## Strengths

- **First work on label unlearning in VFL.** The paper correctly identifies and fills a gap: existing VFU literature (3 prior works cited) addresses passive-party removal, not class/label unlearning. This is a genuine novel contribution to a relatively underexplored problem.

- **Concrete demonstration of label leakage risk in traditional VFU methods.** Section 3.2 provides a systematic analysis showing that Boundary unlearning gradients can be clustered to infer labels (e.g., 62.45% clustering accuracy on CIFAR-100 with 4 classes). This motivates the need for the proposed approach and is valuable in its own right.

- **Manifold mixup enables effective unlearning with very few labeled samples.** The ablation (Figure 5, Section 4.4.2) shows that gradient ascent with 40 raw samples (GA-s) achieves only 40.48% on D_u, while the proposed method with the same 40 samples plus mixup achieves 0% — matching the 5000-sample result. This is the paper's strongest empirical finding and clearly demonstrates the value of the mixup component.

- **Consistent utility/unlearning balance across diverse settings.** In Tables 1–3 and the multi-party ablation, the proposed method achieves D_u accuracy near 0% while retaining the highest D_r accuracy among all non-retrain baselines in most configurations (e.g., 89.11% on CIFAR10/ResNet18 vs. 88.16% for FT, 54.4% for Fisher). The method also completes unlearning in seconds.

- **Robustness under DP and Gradient Compression.** Figures 7–8 show the method retains near-0% D_u accuracy under varying differential privacy noise and gradient compression ratios, demonstrating practical viability for real VFL deployments.

## Weaknesses

### Fatal
None.

### Major

- **The central claim of mitigating label leakage is not empirically verified for the proposed method.** Section 3.2 convincingly demonstrates that traditional unlearning gradients can be clustered to infer labels. However, no analogous experiment is conducted on the gradients transmitted by the proposed method (the mixed embeddings' partial derivatives sent back to passive parties). The paper argues *in prose* that using few-shot data and manifold mixup reduces risk, but provides no quantitative privacy evaluation (e.g., clustering accuracy on the mixed gradients, membership inference on the few shared labels). Since "mitigating the risk of label privacy leakage" is stated as a key advantage in the abstract, introduction, and conclusion, this evidential gap is significant — the paper's primary claimed benefit is unsubstantiated by direct measurement.

### Minor

- **Ambiguity in the mixup design for gradient ascent.** The paper applies manifold mixup to the forward embeddings, then performs gradient ascent on the mixed labels y'. It is not clearly specified whether mixup is performed (a) only within the forgetting class (so y' is always a forgetting-class mixture, which is sensible) or (b) across classes (which would cause gradient ascent on retain-class mixtures and potentially degrade utility). The paper refers to D_p as "representative unlearned data" (Section 4.2) but never formally states whether D_p is drawn exclusively from D_u. The experimental results (strong D_r retention) suggest case (a), but the paper should state this explicitly. This ambiguity affects reproducibility.

- **Runtime comparison shown for a single configuration.** Figure 7 shows runtime for only one setting (ResNet18, CIFAR10, 2 passive parties), yet the paper claims "lowest execution time on all experiments." Runtime depends on the number of passive parties, model depth, and dataset size; a single bar chart is insufficient to support this general claim.

- **The MIA figures (Figures 5–6) plot results for CIFAR10 and CIFAR100 aggregated in a shared subplot.** The caption says "CIFAR10 and CIFAR100" but the x-axis lists method names without visually separating datasets, making it difficult to distinguish which bars correspond to which dataset. This is a presentation issue that reduces readability.

### Trivial

- The paper never defines the notation D_r (retain set), D_u (unlearn set), and D_p (few-shot labeled set) in one centralized place. A summary table would help.
- The number of unlearning epochs N and learning rate η are omitted from the baseline descriptions, making reproduction harder than necessary.

## Nice-to-Haves

- **Ablation on intermediate values of n_p.** The ablation compares 40 vs. 5000 samples but does not explore intermediate values (e.g., 100, 500). Understanding how unlearning effectiveness degrades as n_p shrinks further would strengthen the "few-shot" framing.
- **Discussion of the case where the active party does not own labels for any unlearn samples.** The paper currently assumes D_p is available; acknowledging this limitation would improve rigor.
- **Subsampling discussion for the n_p² mixup loss.** With 40 samples, the loss requires 1600 pairs. The paper does not discuss whether all pairs are used or a subsample is drawn.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Baselines not evaluated under same privacy constraints."** The asymmetry here favors the baselines (they have full data access) while the proposed method operates under stricter constraints (few-shot). This asymmetry is intentional and standard — it shows that the proposed method achieves competitive results despite harder operating conditions. Not a valid weakness.
- **"7.63, 0.13" and "0.90, 0.00" formatting issues in tables.** These are formatting artifacts (likely missing \pm in LaTeX rendering); removed per instruction as parser-level presentation issues.
- **"Equation for manifold mixup loss uses n_p² terms — computationally expensive."** This is a computational concern about the method itself, not a weakness in the evaluation. The 40-sample setting makes 1600 pairs entirely tractable, as the runtime results confirm.
- **"ASR graphs aggregate datasets"** clarification requests and other presentation-level nitpicks that do not affect the paper's contribution evaluation.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's novel positioning (first label unlearning in VFL) and surface the central tension: the method clearly works well for few-shot unlearning, but the privacy claim — which is central to the paper's framing — lacks direct empirical support. This is a well-known pattern in privacy papers where a method is motivated by a threat but tested only on utility metrics.

## Suggestions

1. **Run the gradient-clustering attack (Section 3.2) on the mixed gradients ∂ℓ/∂H_k' transmitted during the proposed method.** If clustering accuracy drops near random chance, the privacy claim is validated. If it remains high, the paper should acknowledge this limitation honestly. Either outcome would make the paper significantly stronger than the current state where the claim is asserted but untested.
2. **State explicitly whether mixup is within-class or across-class**, and clarify whether D_p is drawn exclusively from D_u or includes retain-class samples. If within-class, a brief justification would resolve the current ambiguity.
3. **Add intermediate values of n_p** (e.g., 80, 200, 1000) in the ablation study to characterize how the privacy-utility trade-off scales.
4. **Acknowledge the asymmetric comparison explicitly** by noting that baselines operate without the few-shot constraint, and that the comparison demonstrates the proposed method achieves competitive utility despite operating under stricter assumptions.

## Score and Decision

The paper makes a genuine contribution — it is the first to formulate and address label unlearning in VFL, and the manifold mixup + gradient ascent approach is empirically effective at few-shot unlearning. However, the paper's central claim of mitigating label leakage is asserted without direct empirical verification, and a key design choice (mixup scope) is ambiguously specified. These issues are addressable but require revision.

**Originality:** 7/10 — first to address label unlearning in VFL; the mixup+gradient ascent combination is technically straightforward but well-motivated.  
**Importance of question:** 8/10 — label privacy in VFL is a timely and practically relevant problem.  
**Claims supported:** 5/10 — privacy claim is unverified; utility claims are well-supported.  
**Soundness:** 6/10 — experiments are generally sound but the missing privacy evaluation is a significant gap.  
**Clarity:** 6/10 — generally readable but ambiguous on key design choices.  
**Value to community:** 6/10 — the few-shot unlearning technique is useful; the paper would benefit substantially from a privacy evaluation.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>