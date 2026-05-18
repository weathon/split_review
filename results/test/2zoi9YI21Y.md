Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes ZeroPur, a zero-shot (no-training) adversarial purification method that operates in two stages: coarse shifting (pulling adversarial example embeddings toward their blurred counterparts' embeddings) and fine alignment (refining via intermediate-level feature discrepancies). The key appeal is that it requires no generative model training and no classifier retraining, yet achieves competitive robust accuracy on standard benchmarks.

## Strengths

- **Novel coarse-to-fine purification framework without generative models**: The observation that blurring restores classifier attention on adversarial examples (Figure 2, Table 1) is empirically grounded and leads to a practical two-stage method. The steady increase in cosine similarity during coarse shifting (Figure 3, solid lines) and the clear improvement from coarse to fine (e.g., ZeroPur-V-C 62.08% → ZeroPur-V-C-F 77.82% on PGD-20 in Table 2) directly support the approach.

- **Strong performance on standard benchmarks against other purification methods**: On CIFAR-10 with WideResNet-28-10 under AutoAttack (ℓ∞, ε=8/255), ZeroPur achieves 52.23% robust accuracy, outperforming prior purification methods that require generative models (e.g., DiffPure 45.00%, GDMP 51.00%) — and it does so without training any generative model or retraining the classifier.

- **Competitive on ImageNet-scale without expensive generative models**: On ImageNet with ResNet-50 against PGD-200 (ℓ∞, ε=4/255), ZeroPur achieves 47.58% robust accuracy, nearly matching methods relying on diffusion-based purification (DiffPure 48.12%, GDMP 47.62%).

- **Flexible framework not tied to a specific operator**: The paper demonstrates that the blurring operator can be replaced with TV Minimization (Table 7), improving PGD robustness from 72.62% to 77.03%, showing the framework generalizes beyond the specific design choice.

## Weaknesses

### Fatal
None. The paper's core empirical results are reported and no single error invalidates all claims.

### Major

- **Sign error in the fine alignment objective (Equation 8)**: The paper writes the objective as $\max_{\mathbf{x}''} -\Delta\mathbf{u}_l''\cdot\Delta\mathbf{u}_l'$ and states this "is equivalent to maximizing the projection of $\mathbf{u}_l''$ on $\mathbf{u}_l'$." But maximizing $-\Delta\mathbf{u}_l''\cdot\Delta\mathbf{u}_l'$ makes the dot product more negative — i.e., it drives $\Delta\mathbf{u}_l''$ and $\Delta\mathbf{u}_l'$ in opposite directions, which is the opposite of the intended behavior (continuing movement from adversarial toward the natural manifold). Since the authors report strong empirical results, this is almost certainly a presentation error (the negative sign should not be there, or "max" should be "min"). Nevertheless, as written, the math and the prose contradict each other. This must be resolved: either correct the equation to match the intended algorithm, or clarify why the current formulation is correct and the reviewer's reading is wrong. This is a verifiable inconsistency — see lines 132–142 where the equation, its prose description, and the physical intuition are at odds.

- **Overclaimed "state-of-the-art" robustness given adaptive attack results**: The abstract claims "state-of-the-art robust performance" without qualification, and the conclusion claims "largely outperforms previous state-of-the-art adversarial training and adversarial purification methods." However, under the strongest adaptive attacks (BPDA+EOT), Table 6 shows ZeroPur achieves only 48.3%–53.7% robust accuracy, while DiffPure (66.0%) and Hill et al. (2021) (67.8%) substantially outperform it. The paper acknowledges this but then argues "the direct use of strong adaptive attacks underestimates the robustness of ZeroPur" — which is not a valid defense, as adaptive attacks are the relevant threat model for purification methods. The contribution should be honestly scoped as "competitive on standard benchmarks" and "lightweight alternative," not as "state-of-the-art."

- **No systematic clean accuracy degradation reporting on CIFAR-10/CIFAR-100**: The paper acknowledges qualitatively that "our method suffers when applied to clean natural images because the blurring operator corrupts the clean image" (Section 5), and ImageNet results (Table 5) do report natural accuracy (Clean: 76.13% → ZeroPur-V-S-C-F: 71.72%). However, the CIFAR-10 and CIFAR-100 tables (Tables 2–4) omit clean accuracy entirely. For any practical defense, the clean-vs-robust accuracy trade-off is a critical performance dimension, and it is missing from the main evaluation.

### Minor

- **The paper's defense against the adaptive-attack criticism is weak**: The claim that adaptive attacks "underestimate" ZeroPur's robustness because "these attacks start from clean natural examples" is not convincing. Adaptive attacks are designed to evaluate the full pipeline, and other purification methods (DiffPure, Hill et al.) do not receive the same caveat. The paper would benefit from honestly acknowledging that ZeroPur's gradient path can be exploited through the purification pipeline, as evidenced by robustness decreasing with more purification steps under BPDA+EOT (Figure 5).

- **No computational cost analysis**: The paper claims the method is "lightweight" but provides no per-image runtime comparison against DiffPure, SOAP, or other purification methods. Since ZeroPur performs iterative optimization per image, this claim requires empirical support.

- **"Zero-shot" terminology could be clarified**: The method requires gradient backpropagation through the classifier and access to its intermediate layers. This is standard for self-supervised approaches but differs from "zero-shot" in the sense of zero model access. A brief clarification would help readers understand the usage.

### Trivial
- Equation 8 uses "max" but the cited ILA (Huang et al., 2019) uses a similar sign convention for attacks yet achieves the opposite geometric effect for defense — the paper should reconcile this notation.

## Nice-to-Haves
- Ablation showing coarse-only vs. fine-only vs. coarse+fine performance to quantify each stage's contribution.
- Evaluation on architectures beyond ResNet/WideResNet (e.g., ViT) to test generality.
- Discussion of failure cases where coarse shifting provides an incorrect direction (the paper notes this can happen but does not analyze when).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"AutoAttack comparison is unfair because it's non-adaptive for ZeroPur but adaptive for adversarial training methods"** — Removed because this is factually incorrect. AutoAttack is the same standardized attack (including Square Attack, a gradient-free component) applied identically to all methods. It does not "know" any defense. The comparison in Tables 2–5 is standard RobustBench practice. The relevant concern (that AutoAttack may be weaker against purification methods) is already covered by the adaptive-attack section.

2. **"Coarse shifting relies on a heuristic without theoretical justification"** — Removed because the paper provides extensive empirical justification (Figure 2, Table 1, Section 3.1). For an empirical paper, empirical justification is sufficient for a design choice. The method is explicitly presented as motivated by an observed phenomenon.

3. **"MILD borrowed from ILA without discussing why it doesn't overshoot"** — Removed because the paper does discuss this: it notes that fine alignment "backfires if coarse shifting does not give an approximately correct direction as a reference" (line 152), and the constraint $\|\mathbf{x}'' - \mathbf{x}_{\text{adv}}\| \leq \epsilon_{\text{pfy}}$ prevents unbounded movement.

4. **"Tables lack experimental details"** — Removed because the tables are parsed from images; the original submission likely contains details (number of steps, budgets) in captions or the main text that the parser stripped. The paper states in Section 4.1 that $\alpha_c = \alpha$, $\epsilon_c = 1.25\epsilon$, and Algorithm 2 specifies per-step details.

5. **"No evaluation against ℓ₂ or ℓ∞ attacks on ImageNet with adaptive attacks"** — Removed because: (a) Table 5 does report both ℓ∞ (ε=4/255) results, (b) requesting adaptive attacks on ImageNet for all threat models is practically infeasible for an academic submission and goes beyond the paper's stated scope. The core concern (adaptive attack vulnerability) is already covered by CIFAR-10 results.

6. **"No discussion of different classifier architectures beyond ResNet and WideResNet"** — Removed because the paper evaluates ResNet-18, WideResNet-28-10 on CIFAR-10/100, and ResNet-50 on ImageNet. Three architectures across two families is a reasonable evaluation. Requesting ViT or DenseNet is scope creep.

## Novel Insights

The most interesting observation emerging from these reviews is that ZeroPur's decreasing robustness with more purification steps under BPDA+EOT (Figure 5) reveals a fundamental tension in purification-by-optimization: more iterative refinement creates a more differentiable path that stronger adversaries can exploit. This suggests an inherent trade-off between purification quality and gradient obfuscation that the paper does not explore. The sign-error question also raises a deeper point: if the fine alignment objective in ILA-style attacks was originally designed to *amplify* adversarial perturbation (making features deviate further), repurposing it for defense requires care to ensure the optimization direction is properly inverted — a subtle but critical detail that the paper's current formulation obscures.

## Suggestions

1. Fix the sign in Equation 8 (remove the negative sign or change max to min to match the intended behavior) and verify that the implementation matches the corrected equation.
2. Tone down the "state-of-the-art" claim in the abstract and conclusion to accurately reflect performance under adaptive attacks. Position ZeroPur as "competitive with purification methods on standard benchmarks while being training-free" rather than global SOTA.
3. Report clean accuracy on CIFAR-10 and CIFAR-100 for all ZeroPur configurations so readers can assess the clean-vs-robust trade-off.
4. Add a runtime comparison table showing per-image purification time vs. DiffPure, SOAP, and other lightweight methods to support the "lightweight" claim.

## Score and Decision

The paper presents a genuinely novel idea (training-free coarse-to-fine purification via blurring + feature-space refinement) with strong results on standard benchmarks. However, it is undermined by: (1) a sign inconsistency in the core equation that, if present in the implementation, would invert the method's intended behavior and that, even as a typo, prevents verification of the algorithm from the paper; (2) overclaimed "state-of-the-art" status contradicted by the paper's own adaptive-attack results; and (3) missing clean-accuracy degradation data on the primary datasets. These issues are fixable but are too significant to overlook in the current form.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>