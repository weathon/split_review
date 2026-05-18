I have a thorough understanding of the paper and all the reviewer inputs. Let me now compose the consolidated review.

---

## Summary

This paper proposes PASLE (Progressive Adaptation with Selective Label Enhancement), a test-time adaptation framework that partitions test samples into confident and uncertain subsets, assigns one-hot pseudo-labels to confident samples and candidate pseudo-label sets (partial labels) to uncertain ones, then progressively trains the model while dynamically refining the candidate sets as the model improves. The paper reports strong empirical results on six benchmark datasets (PACS, VLCS, OfficeHome, DomainNet, CIFAR-10-C, CIFAR-100-C), outperforming nine existing TTA methods.

## Strengths

1. **Consistent state-of-the-art empirical performance.** Tables 1 and 2 show PASLE achieving the highest classification accuracy across all benchmarks and network architectures, with average improvements of 5.63% (ResNet-18) and 4.19% (ResNet-50) on domain generalization tasks and meaningful gains on corruption benchmarks. The improvement is particularly notable on DomainNet, a large-scale dataset with 345 classes.

2. **Novel and well-motivated idea.** The core idea — representing uncertainty through candidate pseudo-label sets rather than committing to definite (and potentially false) pseudo-labels — is intuitively sound and addresses a genuine limitation of existing TTA pseudo-labeling approaches. The connection to partial-label learning (Feng et al., 2020) is appropriate and gives the method a principled loss function (classifier-consistent loss) for candidate-labeled samples.

3. **Ablation confirms candidate labels contribute positively.** The comparison PASLE vs. PASLE-NC (Table 3) shows that including candidate-labeled samples consistently improves performance across all target domains of OfficeHome, demonstrating that the candidate-set component is not superfluous.

4. **Robustness to hyperparameters and batch sizes demonstrated.** Figure 2a shows PASLE's performance is relatively stable across a broad range of τ_start and τ_end values, and Figure 2b shows consistent advantage over baselines under varying batch sizes — both practically relevant properties for deployment.

## Weaknesses

### Major

1. **Theoretical analysis is generic and disconnected from the method.** The paper lists "theoretically establishing a generalization bound for TTA" as a bullet-point contribution, but neither theorem specifically validates PASLE's mechanisms. Theorem 1 is a standard domain adaptation bound (derived from Ben-David et al., 2010) showing that adding more target-domain samples tightens the bound — a generic observation that applies to any TTA method that uses more target samples. Theorem 2 is a general PAC-style bound relating the gap between empirical and expected risk to the distance between the provided label distribution and the Bayes class-probability distribution. The paper asserts that PASLE's actions make the label distribution "closer" to the Bayes distribution, but provides no formal derivation showing how — no argument that candidate-set construction reduces $\mathbb{E}[\|q-p\|_2]$ compared to one-hot pseudo-labels from the same model, nor any quantification. The theory section reads as appended after the method was designed rather than as analysis that is specific to PASLE. This overclaiming of the theory's role weakens the paper's framing of its contributions.

### Minor

2. **Missing comparisons with recent uncertainty-aware TTA methods.** The baselines (TENT, PL, SHOT-IM, T3A, TAST, TSD, etc.) are reasonable but omit several strong recent methods that also handle uncertainty through other mechanisms — most notably SAR (Niu et al., 2023), which the paper cites in the related work (line 23) but does not compare against. EATA (Niu et al., 2022) is also relevant. Without these comparisons, it is unclear whether PASLE's candidate-set approach genuinely outperforms simpler selective adaptation schemes (gradient filtering, confidence-based sample selection) or whether the gains primarily come from progressive self-training components that many methods already use. The existing 9 baselines already demonstrate broad superiority, so this is not fatal, but it is a gap that would substantially strengthen the empirical validation.

3. **Limited ablation of interacting components.** The ablation (Table 3) compares PASLE only against PASLE-NC (excluding candidate-labeled samples). Since the method has multiple components that interact — the confident/uncertain partition rule, the buffer management (Eq. 8), the linear threshold schedule (Eq. 9), and the choice of classifier-consistent loss for candidate labels — the paper does not isolate which components drive the improvement. For instance, the buffer selection rule prefers samples with larger margins, but this choice is not compared against alternatives (e.g., storing high-entropy samples, random selection). The linear decay of τ(r) is compared against no alternative schedule. This makes it difficult to assess whether the gains come from the candidate-set representation itself or from auxiliary design choices.

4. **Proposition 1 rests on an unverifiable assumption.** Proposition 1 assumes $|f_j(\mathbf{x};\Theta^r) - f_j(\mathbf{x};\Theta^*)| \le \frac{1}{2}\tau(r)$ for all $j$ — i.e., a known uniform bound on the error of the current model relative to the Bayes-optimal model. In practice, τ(r) is set manually (τ_start, τ_end, τ_des tuned per dataset) and decreased linearly with no mechanism to estimate the actual bound. The proposition therefore motivates the *form* of the selection rule but does not justify the specific threshold values used. The paper somewhat overstates the role of Proposition 1 as a theoretical justification; it is more accurately described as a heuristic motivation.

5. **Sample utilization analysis could be more probative.** Figure 1 shows PASLE uses more "effectively labeled" samples over time than PASLE-NC. However, this metric inherently favors PASLE because candidate-labeled samples are counted as "effectively labeled" in PASLE but excluded entirely from PASLE-NC. A more informative comparison would be to plot the number of *correctly* assigned labels (or the accuracy of the candidate sets) over time, to demonstrate that the adaptive refinement genuinely improves label quality rather than merely counting more samples.

### Trivial

None that survive filtering (formatting issues are parser artifacts).

## Nice-to-Haves

- **Compare candidate sets against alternative treatments of uncertain samples.** The most informative experiment would be: for the same set of uncertain samples (those not meeting the confident threshold), compare self-training with (a) one-hot pseudo-labels, (b) soft labels (raw softmax), and (c) candidate sets (Eq. 7). This would isolate whether the candidate-set representation itself provides a benefit over simpler approaches.
- **Report candidate set size evolution.** The paper says uncertainty is "manifested through cardinality of the candidate pseudo-label set" but never shows the distribution of set sizes during adaptation — does the average number of candidates shrink as the model improves? Are most uncertain samples assigned small (2–3 class) or large candidate sets? This would give insight into how the method actually behaves.
- **Runtime or latency comparison.** Online TTA cares about per-step wall-clock time. PASLE adds overhead from candidate set construction, buffer management, and the classifier-consistent loss. A runtime comparison against simpler baselines (e.g., T3A, BN calibration) would help assess the practical tradeoff between accuracy gain and computational cost.

## Removed Points

- **Criticisms about formatting, garbled notation, and parser artifacts in Algorithm 1.** These are PDF-extraction artifacts, not author errors. Removed per hard rules.
- **Criticism that the paper should "acknowledge that τ_start is dataset-dependent."** The paper already does this explicitly on line 288, which describes how hyperparameters are selected per dataset based on validation performance following Gulrajani & Lopez-Paz (2021). Removed as the paper already addresses this.
- **Strength Finder's claim that "Theoretical analysis supports the approach."** This conflicts with the verified weakness that the theory is generic and disconnected from PASLE's specific mechanisms. Per the rule that when a strength and weakness disagree the weakness wins, this strength is removed.
- **Strength Finder's claim about "Clear theoretical motivation for data partitioning" from Proposition 1.** Proposition 1 provides motivation for the *form* of the selection rule, but the verified weakness (unverifiable assumption, heuristic threshold values) significantly undermines the strength of this claim. Removed as the weakness partially invalidates the claimed strength.

## Novel Insights

The most interesting observation that emerges from the reviews is that the paper's core idea — representing label uncertainty through candidate sets in TTA — occupies a middle ground between two well-studied extremes: one-hot pseudo-labels (hard assignment, high risk of confirmation bias) and soft-label/probability-based training (continuous weighting, no explicit uncertainty representation). The candidate-set approach has a natural connection to partial-label learning that gives it a principled loss function, and the progressive refinement of candidate sets as the model improves is a clean way to monotonically increase the effective supervision. However, this conceptual novelty is partially undercut by the lack of direct comparisons with the intermediate alternatives (confidence-weighted entropy minimization, soft-label self-training), making it difficult to pinpoint exactly where the benefit lies. The paper makes a stronger empirical case than a theoretical one.

## Suggestions

1. **Either tighten the theory to be PASLE-specific or remove it from the claimed contributions.** If Proposition 1's assumption held, the candidate set in Eq. (7) would guarantee containment of the true label — this property could be used to bound $\mathbb{E}[\|q-p\|_2]$ in terms of model error and candidate-set size, making Theorem 2 method-specific. Alternatively, reframe the theory section as informal motivation to avoid overclaiming.

2. **Add comparisons with SAR, EATA, and a soft-label variant** to position PASLE against other uncertainty-handling approaches in TTA and demonstrate that the candidate-set representation specifically is beneficial, not just progressive self-training generally.

3. **Ablate additional components:** the buffer selection rule (margin-based vs. entropy-based vs. random), the threshold schedule (linear vs. constant vs. exponential decay), and the loss function for uncertain samples (classifier-consistent vs. cross-entropy with soft labels).

## Score and Decision

**Score: 6.0**

**Decision: Accept**

The paper presents a novel and well-motivated approach to test-time adaptation with consistently strong empirical results across diverse benchmarks. The main weaknesses are (a) the theoretical analysis is overstated as a contribution and does not specifically validate the method, (b) the baseline set omits some recent uncertainty-aware TTA methods, and (c) the ablation study is too limited given the number of interacting components. None of these issues invalidate the core empirical contribution — the method clearly works well and the idea is novel — but they prevent the paper from being a stronger submission. The theory should be either substantively connected to the method or downgraded from a claimed contribution, and the empirical positioning against alternative uncertainty-handling approaches should be strengthened. With these revisions, the paper would be a solid contribution to the TTA literature.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>