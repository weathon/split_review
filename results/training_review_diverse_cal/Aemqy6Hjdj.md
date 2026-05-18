Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper tackles compositional generalization (CG) — the problem of generalizing to unseen domain-class combinations when training data is sparse. The authors propose Compositional Feature Alignment (CFA), a two-stage finetuning method that (1) learns two orthogonal linear heads for class and domain prediction via linear probing, then (2) finetunes the encoder with those heads frozen. They also curate CG-Bench, a CG benchmark from four real-world datasets. The method is supported by a theoretical guarantee (Theorem 4.1) under the unconstrained feature model and by feature visualizations showing the desired compositional structure.

## Strengths

1. **Theory-motivated method design**: Theorem 4.1 provides a formal guarantee that, under the unconstrained feature model, optimizing with two frozen orthogonal heads yields features decomposable into class-dependent and domain-dependent orthogonal components. This goes beyond engineering heuristics and connects to the neural collapse literature.

2. **Empirical validation of the hypothesized feature structure**: Figure 5 directly visualizes that CFA-finetuned CLIP features separate into orthogonal class and domain clusters (right panel), while pretrained features lack this structure. This provides compelling direct evidence for the proposed mechanism.

3. **Practical robustness to incomplete domain labels**: Table 2 shows CFA retains 53.4% OOD accuracy with only 10% of domain labels (vs. 54.3% with 100%) and 52.0% with zero-shot-predicted domain labels, outperforming full finetuning (51.0%) and LP-FT (43.9%). This addresses a realistic deployment constraint.

4. **Consistent OOD improvements on CLIP across datasets**: On CLIP (where WiSE-FT is applied symmetrically to all methods), CFA (WiSE) achieves the best OOD accuracy on all four datasets — OfficeHome (56.9 vs. next best 53.4), DomainNet (9.2 vs. 8.7), iWildCam (OOD Acc 19.7 vs. 18.2, OOD F1 32.5 vs. 30.0), and is within 0.2 of the best on FMoW — demonstrating multi-dataset generality.

5. **Computational efficiency**: The two-stage design avoids minimax adversarial training used in domain-adversarial networks, making CFA simple and lightweight while still outperforming reweighting and LP-FT baselines.

## Weaknesses

### Major

1. **Benchmark construction does not cleanly match the paper's own definition of compositional generalization.** The paper defines CG as generalization to *unseen domain-class combinations* (line 18: "the training data might not cover all the possible combinations... can the model generalize to unseen domain-class combinations?"). However, CG-Bench's DomainNet split selects OOD combinations as the lowest 20% of zero-shot accuracy, not as combinations with zero training examples (line 151). The general "Benchmark Curation Setup" describes a binary-mask approach that would ensure OOD combinations have no training data, but the DomainNet-specific procedure replaces this with a zero-shot-accuracy threshold. The paper does not verify that the selected OOD combinations actually have no training data — Figure 3 (left) shows some combinations with low but non-zero training counts. Additionally, the curation procedure for the other three datasets (OfficeHome, iWildCam, FMoW) is not described (line 140: "elaborate... by taking DomainNet as an example"), so the reader cannot assess whether the same issue applies across the benchmark suite. This mismatch between the paper's definition of CG and the benchmark's construction undermines the central claim that the method improves generalization to unseen domain-class combinations. **To fix**: Either verify that OOD combinations have zero training samples, or explicitly reframe the benchmark as testing "hard" rather than "unseen" combinations and adjust the claims accordingly.

2. **Asymmetric application of WiSE-FT for DINOv2 experiments creates an uneven playing field.** For CLIP, WiSE-FT is applied to all methods (zero-shot head interpolation). For DINOv2, WiSE-FT is applied to CFA and LP-FT but *not* to full finetuning and reweighting baselines (line 206; visible in Table 1 where DINOv2 rows for these baselines have no WiSE variants). The justification — that these baselines lack linear-probed heads for interpolation — is technically true but solvable (one could easily train a linear probe for them). This means the DINOv2 comparison stacks an additional OOD-improving technique on top of CFA that is withheld from multiple baselines, making the DINOv2 results harder to interpret as a clean comparison of the core methods. The CLIP results (where WiSE is applied symmetrically) are cleaner, but the paper also draws conclusions from DINOv2 experiments where this confound exists.

### Minor

3. **No error bars or confidence intervals on main results (Table 1).** The paper reports single numbers for each method/dataset combination. Given well-known variability in finetuning experiments — especially when OOD accuracies are in single digits (e.g., 5–9%) — it is impossible to assess whether observed differences are statistically meaningful. The partial-label experiments do report 3-seed averages, so the authors are aware of this practice. Adding variance estimates to Table 1 would significantly strengthen the empirical claims.

4. **Improvements are modest and sometimes inconsistent.** On DomainNet CLIP, CFA without WiSE (7.3) actually underperforms full finetuning (7.5). On FMoW CLIP, Reweight-E (41.8) ties or slightly exceeds CFA (41.6). These cases show the method does not dominate across all settings, and the best results often require WiSE-FT as a co-requisite. The paper uses a 0.2% bold-tolerance to claim parity, which is reasonable but further underscores the modest effect sizes.

### Trivial

5. **The paper could state more clearly that the benchmark curation procedure differs across datasets** — only DomainNet's procedure is described. The current language ("elaborate... by taking DomainNet as an example") leaves ambiguity about how the other three datasets' OOD splits were constructed.

## Nice-to-Haves

- **Compare to a domain-adversarial finetuning baseline** (e.g., DANN or a lightweight variant adapted for finetuning). The paper explicitly distinguishes CFA from adversarial methods in §2.1, noting its computational advantage, but never empirically demonstrates that CFA matches or exceeds that family of methods. Such a comparison would strengthen the paper's positioning.
- **The theoretical guarantee (Theorem 4.1)** concerns convergence of training-set feature optima under the UFM, as the paper acknowledges (line 68: "no guarantee that features from unseen domain-class combinations will still conform to this structure"). A broader discussion of what guarantees the finetuned encoder might provide for out-of-sample inputs would be a useful addition, though not required.

## Removed Points

- **"Theoretical guarantee does not speak to generalization to unseen combinations"** — The paper already acknowledges this limitation explicitly at line 68. The critic's suggestion that the paper "would benefit from acknowledging this gap" is based on a misreading; the gap is already self-acknowledged.
- **"Missing related works"** — Not verifiable without external sources. Removed per instructions.
- **"Pure formatting/style nitpicks"** — None present in the critic's output.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated claims and their evaluation, without offering a novel reframing or synthesis that goes beyond what the paper itself provides.

## Suggestions

1. Reframe CG-Bench to ensure OOD combinations genuinely have zero training samples (using the binary-mask approach described in the "Benchmark Curation Setup" section), or explicitly acknowledge that the benchmark tests "hard" rather than strictly "unseen" combinations and temper the claims accordingly.
2. Apply WiSE-FT symmetrically to all DINOv2 baselines (train a linear probe for full finetuning and reweighting baselines to serve as the interpolation target), or restrict the main claims to the CLIP results where the comparison is cleaner.
3. Add standard deviations (over at least 3 seeds) to Table 1 for all methods and datasets.
4. Include a DANN-based finetuning baseline to substantiate the claimed advantage over adversarial methods.
5. Clarify in the main text how the OOD splits for OfficeHome, iWildCam, and FMoW were constructed (briefly, even in a short paragraph).

## Score and Decision

This paper tackles a genuinely important and understudied problem (compositional generalization in the multi-domain multi-class setting), and the core idea — orthogonal two-head feature alignment via frozen heads — is theoretically motivated and conceptually clean. The feature visualizations and partial-label experiments are compelling evidence that the method works as intended.

However, the experimental evaluation has two substantive flaws that collectively undermine the paper's central comparative claims: (1) the benchmark's OOD construction (lowest 20% zero-shot accuracy) does not clearly match the paper's own definition of compositional generalization (unseen domain-class combinations with zero training data), and (2) the DINOv2 experiments apply WiSE-FT asymmetrically, giving CFA an advantage withheld from several baselines. The lack of error bars further weakens confidence in what are often modest improvements (sometimes a fraction of a percent). These issues are fixable, but in their current form they prevent a clean assessment of whether CFA truly outperforms standard methods for the claimed problem.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>