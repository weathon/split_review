**Summary**

This paper proposes using the bias part (constant term in the piecewise-linear representation) of a ReLU DNN as a classifier, motivated by the claim that the bias part is piecewise constant with zero gradient and therefore immune to direct gradient-based attacks. The authors prove an existence theorem for bias classifiers, propose a training method combining cross-entropy losses on both the bias part and full network, and introduce the concept of an "information-theoretically safe" classifier by adding a random first-degree matrix to randomize attack directions. Experiments on MNIST and CIFAR-10 compare the bias classifier against standard networks and several defense baselines.

---

## Strengths

1. **Non-trivial existence theorem (Theorem 1).** The paper formally proves that for any classification problem with disjoint open sets, there exists a ReLU DNN whose bias part gives the correct label with arbitrarily high probability (i.e., on all but an arbitrarily small-volume set). This establishes the bias classifier as a theoretically viable concept, not just an empirical heuristic.

2. **Training method demonstrably shifts classification to the bias part (Table 1).** The paper shows that adversarial training on the combined loss (Eq. HT1) increases B_F accuracy from 15.62% (normal training) to 99.09% while driving the first-degree part's accuracy down to 0.28%. This is a striking empirical result, even if the mechanism needs clarification (see Weaknesses).

3. **Novel concept of randomizing the first-degree part for safety (Theorems 2–5).** Adding a random matrix \(W_R\) to a trained bias classifier makes the gradient-based attack direction provably random (under the secrecy condition and the bound \(|\nabla F/\nabla x|_\infty<\lambda/2\)). For MNIST, this drives adversary creation rates down to 1–4%, matching the random-sample baseline. The idea of achieving safety by making the gradient random (rather than zero) is creative and distinct from gradient obfuscation.

4. **Empirical robustness across multiple attack types is suggestive.** Tables 4–5 show that \(B_{F^{(2)}}\) consistently achieves lower adversary creation rates than several baselines (\(F^{(1)}\), \(F^{(3)}\), \(F^{(4)}\)) under both \(l_\infty\) and \(l_0\) attacks on MNIST and CIFAR-10. The black-box attack results (Tables 9–10) also show the bias classifier performing competitively.

---

## Weaknesses

### Major

1. **Algorithm 1 (BCTrain) has a structural discrepancy with the paper's own mathematical claims — the PGD loop cannot generate perturbations as described.**  

   The paper's core claim is that \(B_F\) has zero gradient almost everywhere (lines 67–68, 341–342). Algorithm 1 (lines 301–306) performs an inner PGD-style maximization using  
   \[
   x_{i+1} = x_i - M_b\,\frac{\partial L(x_i, y, \Theta_k)}{\partial x_i}
   \]
   where \(L(x, y, \Theta) = L_{\text{CE}}(B_{F_\Theta}(x), y)\). If \(B_F\) truly has zero gradient w.r.t. \(x\) (as the paper asserts), then \(\partial L/\partial x = 0\) pointwise almost everywhere, the PGD loop produces no perturbation, and the inner maximization degenerates.  

   Meanwhile, the training objective Eq. HT1 suggests a joint inner maximization over both the B_F and F losses. Algorithm 1 uses only the B_F term for the inner loop and incorporates the F term only in the outer parameter update (line 309). The paper does not explain this discrepancy. Since Table 1 shows that Eq. HT1 dramatically boosts B_F accuracy (15.62% → 99.09%), the algorithm *as written* cannot account for the reported results.  

   This is a **major** weakness: the core training procedure needs a corrected description or a justification for how the PGD loop functions despite the zero-gradient claim. The underlying approach may still be salvageable (e.g., by using the combined loss for PGD), but in its current form the paper's central experimental results rest on an unexplained mechanism.

2. **Key theoretical condition \(|\nabla F(x)/\nabla x|_\infty < \lambda/2\) is never verified.**  

   This condition is the bedrock of Theorems 2–6. The paper does not measure \(|\nabla F/\nabla x|_\infty\) for any trained network, does not explain how to enforce it during training, and does not discuss what happens when it is violated. Without any empirical evidence that this bound holds, the information-theoretic safety guarantees float disconnected from the experiments.  

   Moreover, the condition in Theorem 6 (line 585),
   \[
   (\lambda - \mu)\,e^{-2\beta - n\mu + \sqrt{\lambda}} > (2m\lambda + \mu)m,
   \]
   contains an exponential term \(e^{-n\mu}\) that, for CIFAR-10 (\(n=3072\)), renders the condition practically impossible to satisfy unless \(\lambda\) is astronomically large. The paper acknowledges this gap only indirectly ("the estimations in Theorems 5–6 are not optimal," line 1082) but does not discuss whether the general-\(m\) guarantees are meaningful for realistic input dimensions.

3. **Experimental comparisons are confounded.**  

   - **Architecture mismatch (Table 11).** The main comparison table (tab-com1) compares \(B_{F^{(2)}}\) (LeNet-5 / VGG-19 variants) with ADV, TRADES, SOAR, etc. that use ResNet-10. The paper acknowledges this (lines 1026–1028: "the DNN models and the attacks are not the same") but draws conclusions anyway. This makes the quantitative comparisons uninformative — the observed differences could easily be driven by architecture rather than the bias classifier idea.
   - **No variance or statistical significance.** No experiment reports standard deviations, confidence intervals, or results over multiple random seeds. Many comparisons differ by just a few percentage points (e.g., \(B_{F^{(2)}}\) vs. \(F^{(2)}\) for 2-80 on MNIST: 79% vs. 90%), making it impossible to assess whether differences are meaningful.
   - **CIFAR-10 "near optimal" claim is unsupported (Table 6).** The paper claims that \(B_{F^{(6)}}\) achieves "near optimal" results for CIFAR-10 (line 904), but the adversary creation rates are 19–24%, far above the random-sample baseline of 1.67–4.28% (Table 7). The paper's defense (lines 907–910, adjusting for accuracy) is convoluted and does not convincingly bridge this gap.

### Minor

4. **"Information-theoretically safe" terminology is misleading.** The paper defines its own notion (random attack direction) and credits cryptography for the term (lines 95–98). However, in cryptography, information-theoretic security holds *even when the algorithm is fully known* (Kerckhoffs's principle), whereas Theorem 1 explicitly requires that "the structure and parameters of \(F\) are kept secret" (line 513). This dependence on secrecy is a meaningful departure from the cryptographic concept and should be flagged more prominently — ideally by renaming the concept or clarifying the gap.

5. **Inference cost of computing \(B_F\) is not discussed.** Computing \(B_F(x) = F(x) - (\nabla F(x)/\nabla x)\cdot x\) requires the Jacobian-vector product \(J(x)\cdot x\) at every inference. The paper does not mention this cost, let alone discuss whether a cheaper decomposition exists (e.g., extracting the bias term analytically from each linear region). For any deployment scenario, the added latency matters.

6. **Correlation attack motivation is stated without quantitative support.** The paper asserts that \(W_F\) and \(B_F\) are anti-correlated "with high probability" (lines 374–378) but provides no empirical measurement of this correlation. Given that this observation motivates an entire attack algorithm, some quantitative evidence should be provided.

7. **Theorem 3's "approximate safety" bound is dimension-dependent.** Theorem 3 gives \(\Ca(B_{\tilde F},\A_3,\U) \le \Ca(F,\rho) + \mu n/\lambda\). For CIFAR-10 (\(n=3072\)), making \(\mu n/\lambda\) small requires \(\lambda\) to be impractically large unless \(\mu\) is very small — but \(\mu\) is never measured. The practical relevance of this bound is unclear.

### Trivial

- The "SA" metric for strong adversaries is referenced to [netb] without a brief descriptive footnote, though this is acceptable practice.
- Minor notation inconsistency: the paper uses \(\gamma\) (Eq. HT1) and \(M_n\) (Algorithm 1) for the weight on the F loss without explicitly connecting them.

---

## Nice-to-Haves

- Verify the condition \(|\nabla F/\nabla x|_\infty < \lambda/2\) empirically on the trained networks to connect theory with experiments.
- Run controlled comparisons using the same base architecture for all methods, or clearly state the limitation more prominently.
- Discuss adaptive attacks beyond the three proposed, even if only to argue why they are unlikely to succeed.

---

## Removed Points

These points from the reviewers are removed with justification:

- **"SA metric is undefined"** — Removed. The paper explicitly cites [netb] for the definition. This is standard practice.
- **"Table 41 compares the wrong model"** — Removed (moved from weakness proper). Table 41 compares \(F^{(1)}\) (not the bias classifier) with ResNet18/VGG19 to show the base network is competitive. This is a supporting experiment, not the paper's main claim. It is not "wrong," merely supplementary.
- **"No discussion of gradient obfuscation failures"** — Removed. The paper *does* address this (lines 148–149): "Our network does not deliberately hide the gradient like the method in [not]. Our network does not have gradient, so the white box attack method for the gradient hiding method in [not] does not work for our model."
- **"No code release" and "undisclosed hyperparameters"** — Removed per hard rules. These are reproducibility nitpicks not required for evaluation.
- **"Missing adaptive attacks"** — Removed. The paper proposes and evaluates three concrete attack methods. Demanding more is scope creep without specific justification.
- **Several generic area-of-concern sweeps from the harsh critic** (e.g., "could the metric be measuring a proxy?", "confounders not controlled") — Removed as speculative rather than identified problems.
- **Strength Finder strengths that are generic or conflict with verified weaknesses** — Removed. Some strengths (e.g., "the paper addresses an important problem") are generic. Others (e.g., strong claims about Table 11 comparison) conflict with the verified architecture-mismatch weakness and are removed.

---

## Novel Insights

None beyond the paper's own contributions. The reviewer analyses do not surface a synthesis that the paper itself does not already contain or imply.

---

## Suggestions

1. **Correct Algorithm 1.** Describe how adversarial perturbations are actually generated during training. If the implementation uses the full combined loss (including the \(F\) term) for the inner maximization, state this clearly and reconcile the pseudocode with Eq. HT1.
2. **Verify the Jacobian bound.** Measure \(\|\nabla F/\nabla x\|_\infty\) for the trained networks to demonstrate that the key theoretical condition is satisfiable.
3. **Run matched-architecture comparisons.** Compare \(B_F\) against baselines using the same base architecture, attack, and evaluation protocol. Report variance.
4. **Tone down the "near optimal" characterization for CIFAR-10.** The gap between 19–24% adversary rates and the 1.67–4.28% random baseline is substantial and should be discussed honestly.

---

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>