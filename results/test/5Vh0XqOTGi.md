Now I have all the information needed. Let me write the consolidated review after thoroughly cross-checking every claim.

---

## Summary

This paper proposes GAFM (Generative Adversarial Federated Model), a method that integrates a Wasserstein GAN with split learning to protect against Label Leakage from Gradients (LLG) in binary classification for vertical federated learning. GAFM replaces the standard logit function with a GAN generator to learn the label distribution indirectly, and adds a cross-entropy loss with randomized response labels to maintain utility. The key mechanism is that the GAN loss gradient and the CE loss gradient point in opposite directions, creating mutual perturbation that mixes gradients and obscures label information. Experiments on four datasets (Spambase, IMDB, Criteo, ISIC) show GAFM achieves near-0.5 leak AUC while maintaining classification AUC comparable to vanilla splitNN.

## Strengths

- **Novel and well-motivated approach**: GAFM is the first method to combine GANs with split learning specifically for label protection in VFL binary classification. The design is principled — the GAN learns the label distribution without direct label usage, while the CE loss with randomized response provides utility guidance. The mutual perturbation mechanism (GAN and CE gradients pointing in opposite directions) is intuitively appealing and supported by visual evidence.

- **Strong empirical privacy-utility trade-off**: Table 2 demonstrates that GAFM achieves leak AUC close to 0.5 (e.g., 0.581 on Spambase under norm attack) compared to vanilla splitNN (0.781) and Max Norm (0.673), while maintaining comparable classification AUC (0.925 vs. 0.928). GAFM also exhibits lower variance across random seeds than Marvell, indicating more stable performance — a practically important advantage.

- **Ablation study cleanly validates the design**: Figure 3 and Table 3 show that neither the GAN-only variant (low utility, e.g., ~0.7 classification AUC on IMDB) nor the CE-only variant (high leak AUC, e.g., >0.7 on IMDB and ISIC) achieves the balance that GAFM does, confirming that the synergy of both components is essential.

- **Contribution of more effective label-stealing attacks**: The proposed mean and median attacks (Section 3.5) consistently achieve higher leak AUC than the existing norm attack across all four datasets (Table 2). This advances the evaluation methodology for LLG defenses, providing stronger benchmarks for future work.

- **Robust performance on imbalanced, real-world data**: GAFM performs well on severely imbalanced datasets Criteo (~35% positive rate) and ISIC (~14%), demonstrating practical applicability in domains like advertising and healthcare where label leakage is a critical concern.

## Weaknesses

### Fatal
None.

### Major

- **Evaluation limited to two-party setting despite general VFL framing**: The problem setup (Section 3.1) and Figure 1 present the method with *P* non-label parties, consistent with the VFL framing. However, all experiments (Section 4.1: "We consider the two-party split learning setting used by Marvell") use exactly one non-label party. While this follows the convention of prior work (Marvell also evaluates on two-party), the paper neither acknowledges this as a scope limitation nor provides theoretical justification that results from *P*=1 generalize to *P*>1. The aggregation of intermediate features from multiple parties could affect gradient statistics, GAN dynamics, and the degree of gradient mixing. This creates a gap between the claimed scope (multi-party VFL) and the evidence provided. The paper should either add multi-party experiments (even a three-party setting with two non-label parties and one label party would help) or explicitly scope its claims to the two-party setting and adjust the framing accordingly.

### Minor

- **Privacy mechanism lacks quantitative backing tied to its own theory**: Section 3.4 invokes Proposition 3.1 (which bounds worst-case leak AUC by the sum of KL divergences between class gradient distributions) to motivate the gradient mixing argument, but then supports the claim that GAFM "has more mixed intermediate gradients" only with a qualitative visual comparison (Figure 2). The paper does not compute the empirical sum of KL divergences — the very quantity that Proposition 3.1 identifies as the relevant metric. This is not a fatal gap because Table 2 provides downstream quantitative evidence via actual leak AUC, but computing the KL divergence would directly connect the empirical results to the theoretical bound and make the privacy argument more rigorous.

- **No discussion of computational overhead**: GAFM introduces a GAN (generator + discriminator) into the training pipeline, which adds non-trivial training cost compared to vanilla splitNN, Max Norm, and Marvell. The paper does not report training time, memory usage, or convergence speed. Practitioners need this information to assess the practical trade-off.

- **No explicit analysis of GAN training stability**: Wasserstein GANs with weight clipping can suffer from gradient vanishing or mode collapse. The paper reports results across 10 random seeds without discussing whether any runs were discarded or whether training was stable across all seeds. Since the method's performance depends on GAN training quality, a brief discussion of stability would strengthen confidence.

### Trivial

- The description of mean and median attacks (Section 3.5) states "Assuming that attackers know the gradient centers/medians" but does not specify how the attacker would obtain this knowledge (e.g., from a held-out labeled set, or by observing the training process). This is a minor clarity issue since the paper already acknowledges these are stronger attack assumptions.

## Nice-to-Haves

- Computing the empirical sum of KL divergences between class gradient distributions (as in Proposition 3.1) would directly tie the theoretical bound to the empirical results.
- A discussion of how the method could extend to multi-class settings (mentioned briefly in limitations, but more detail would help).
- A sensitivity analysis for the 10% subset used to select the Δ hyperparameter.
- Reporting wall-clock training time and memory footprint of GAFM vs. baselines.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Δ selection on 10% subset could leak label information"**: Hyperparameter selection on a held-out subset is standard ML practice. The concern about label leakage through tuning a single scalar (Δ) is marginal and does not constitute a meaningful weakness.

- **"Method only demonstrated on binary classification"**: The paper explicitly and repeatedly scopes its contribution to binary classification ("..."to mitigate LLG in binary classification...", "critical to address how splitNN can resist LLG in binary classification tasks"). The limitations section even mentions multi-class as future work. Criticizing the absence of multi-class experiments evaluates the paper against the wrong class of expectations.

- **"Missing DP baseline with gradient clipping"**: The paper explains why differential privacy is not considered as a leakage measure ("not applicable to example-specific and example-aware settings like VFL"). Demanding a DP baseline evaluates against a different methodological class.

- **"Multi-class extension not discussed"**: Already acknowledged as future work in the limitations section; this is scope creep.

## Novel Insights

The observation that the GAN loss gradient and the CE loss gradient have class centers that "differ in opposite directions" (Section 3.4), leading to mutual cancellation in the final gradient, provides a concrete mechanistic explanation for *why* GAFM achieves gradient mixing — beyond simply adding noise. This two-loss design principle (adversarial loss + utility loss with intentionally opposing gradient directions) is potentially transferable to other privacy-preserving learning settings beyond VFL.

## Suggestions

1. **Add at least one multi-party experiment** — even a three-party setting (two non-label parties, one label party) would substantially strengthen the generality of the claims. If not feasible, explicitly scope the paper to the two-party setting and adjust the VFL framing accordingly.

2. **Compute the empirical sum of KL divergences** between class gradient distributions for all methods. This would directly connect the results to Proposition 3.1, providing a quantitative counterpart to Figure 2 and making the privacy analysis more rigorous.

3. **Report training time and memory overhead** to help practitioners assess the practical cost of adding a GAN to the splitNN pipeline.

4. **Add a brief discussion of GAN training stability** across the 10 random seeds, noting whether any convergence issues were observed.

## Score and Decision

Based on my assessment: the paper has a novel contribution, sound experimental design (within its 2-party scope), and convincing empirical results. The main weakness — the gap between the general VFL framing and the 2-party-only evaluation — is real but fixable and does not invalidate the core contribution. The remaining issues are minor. I recommend acceptance with a request to address the scope-evidence gap.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>