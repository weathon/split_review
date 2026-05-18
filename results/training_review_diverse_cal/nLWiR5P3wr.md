I have the paper content from my earlier successful read. Let me now synthesize the final review.

---

## Summary

This paper proposes FoRDE (First-order Repulsive Deep Ensemble), a particle-based variational inference method that repels ensemble members in *input-gradient space* rather than weight space or function space. The core idea — that diversifying input gradients encourages each network to learn different features — is well-motivated and addresses a known limitation of existing repulsive ensemble methods. The authors further design a data-dependent PCA kernel that sets lengthscales inversely proportional to data eigenvalues, producing strong gains under covariate shift (e.g., +2.4% cA on CIFAR-10-C, +1.3% on CIFAR-100-C over the second-best baseline). Experiments span three datasets with seven baselines and include transfer learning and EmpCov prior comparisons.

## Strengths

1. **Well-motivated and novel repulsion space.** The paper identifies concrete limitations of weight-space repulsion (overparameterization, weight symmetries) and function-space repulsion (underfitting), and proposes input-gradient space as a principled alternative. The claim that input gradients characterize a function up to translation provides a clean theoretical grounding. The toy experiments (Figs. 1–3) visually confirm that FoRDE produces higher predictive uncertainty in regions without training data compared to plain DE, weight-RDE, and function-RDE — directly demonstrating improved functional diversity.

2. **PCA kernel design yields substantial and consistent robustness gains.** The data-dependent kernel (Section 3.3) is an elegant way to embed data geometry into the repulsion mechanism. FoRDE-PCA consistently achieves the best corruption robustness across CIFAR-10-C (+2.4% cA), CIFAR-100-C (+1.3% cA), and in the EmpCov ablation (Table 3: 80.5% vs 78.7–78.9% cA). The connection to the EmpCov prior is insightful and places the design in a theoretical context.

3. **Strong transfer learning results.** FoRDE outperforms all baselines on transfer learning with Vision Transformer features (Fig. 4), improving NLL, ECE, and accuracy on both in-distribution and shifted test sets. This demonstrates practical applicability beyond standard benchmarks.

4. **Comprehensive experimental setup.** The paper compares against seven diverse baselines (DE, three RDE variants, LIT, node-BNNs, SWAG) on three datasets, with 5 random seeds each. The EmpCov prior comparison (Table 3) specifically addresses the connection to related work.

## Weaknesses

### Fatal
None.

### Major

1. **Missing uncertainty quantification on the paper's central empirical claim.** Tables 1–3 report standard errors for clean-data metrics (NLL, accuracy, ECE) but not for the corruption-averaged metrics (cA, cNLL, cECE). The paper's headline empirical claim is that FoRDE-PCA outperforms DEs *under covariate shift*, with reported gains of +1.3% cA on CIFAR-100-C and +2.4% on CIFAR-10-C. Without standard errors (or confidence intervals across seeds and/or corruption types), the reader cannot assess whether these improvements are statistically reliable or fall within evaluation noise. This is the most important quantitative result in the paper, and omitting error bars on it is a significant gap. The fact that clean-data metrics show non-trivial variance (e.g., ±0.2–0.3% accuracy) suggests the corruption metrics could also have meaningful variance. The authors should report standard errors or confidence intervals for all corruption metrics, ideally with per-corruption-type breakdowns.

### Minor

2. **No direct measurement of input-gradient diversity in the main experiments.** The paper argues that FoRDE improves functional diversity via gradient repulsion, and provides strong indirect evidence (epistemic uncertainty in transfer learning, toy experiment uncertainty plots). However, for the main image-classification claims, the paper does not directly verify that the repulsion term actually *diversifies* ensemble members' input gradients relative to a plain DE or LIT. A simple pairwise cosine similarity (or angular distance) of normalized input gradients between ensemble members would directly test whether the mechanism is working as intended. While not fatal — the performance gains and toy evidence are suggestive — this gap weakens the causal attribution between the repulsion mechanism and the observed improvements.

3. **The PCA kernel's effect is not fully disentangled from the repulsion effect.** The paper shows that FoRDE-Identity (isotropic repulsion) does *not* improve corruption robustness over DE (e.g., 54.1 vs 54.3 cA on CIFAR-100-C), meaning the entire gain comes from the PCA kernel. The PCA kernel, however, changes both the driving force (via the kernelized density estimate) and the repulsion force. The paper attributes improvement to the PCA kernel's "prior-like" effect (via the EmpCov connection) and its interaction with repulsion, but does not cleanly isolate whether the gains would persist with the PCA kernel but *without* the repulsion term. The EmpCov comparison (Table 3) partially addresses this, but a direct ablation — e.g., FoRDE-PCA vs. a version using the PCA lengthscales in the driving force only, with identity repulsion — would clarify the mechanism.

4. **Toy experiments use 16 ensemble members vs. 10 in main experiments.** The paper does not explain this discrepancy. While this does not invalidate the main results, it makes the toy illustrations not directly comparable to the main experiments.

### Trivial
None.

## Nice-to-Haves

- A per-corruption-type breakdown (e.g., a bar chart or table) showing whether FoRDE-PCA's gains are systematic across all corruption types or concentrated on a few, to strengthen the robustness claim.
- A brief statement in the main text about what the "tuned" lengthscale procedure entails (currently deferred to the appendix), to help readers interpret FoRDE-Tuned results.
- A more detailed discussion of the cost-benefit tradeoff (the paper already reports 3× training time with concrete numbers, but could add commentary on when the improvement justifies the cost).

## Removed Points

- **"Computational cost not contextualized"** — Removed as factually inaccurate. The paper explicitly reports concrete training times (31s vs 101s per epoch) in Section 3.5 and discusses complexity reduction strategies in the Discussion. The paper does contextualize the cost.
- **"PCA lengthscale choice lacks theoretical grounding"** — Downgraded from a standalone weakness to a nice-to-have. The paper is transparent about the PCA heuristic being a design choice (not an optimal prescription), reports FoRDE-Tuned with intermediate settings, and connects it to the EmpCov prior literature. The critic's concern about robustness of the choice is valid as a research direction but not a weakness of the current paper.
- **"Brief LIT comparison in related work"** — Removed as scope-normal. The paper devotes a paragraph to LIT, correctly identifying the key difference (orthogonalization vs. kernelized repulsion) and explaining the advantage of the ParVI framework for flexible kernel design. This is an appropriate level of discussion for a related work section.
- **"Input gradients uniquely characterize functions claim could mislead"** — Removed. The paper correctly states "up to translation," which is the mathematically precise qualification. Comparing gradients on training data is standard practice and does not constitute a misleading claim.
- **Some generic strengths from Strength Finder** — Filtered out; only concrete, evidence-backed strengths are retained above.

## Novel Insights

The harsh critic makes an insightful observation that cuts across the paper's framing: the PCA kernel does the heavy lifting for corruption robustness (FoRDE-Identity shows no improvement over DE), but the repulsion mechanism is what justifies the method's name and framing. This tension is partially resolved by the EmpCov comparison (Table 3), which shows FoRDE-PCA outperforms baselines *with* the EmpCov prior — suggesting synergy between the PCA-induced bias and gradient repulsion. However, a cleaner ablation that isolates these two effects remains an important open question for the paper's narrative.

## Suggestions

1. **Add standard errors (or confidence intervals) to all corruption metrics in Tables 1–3.** This is the most impactful improvement: it directly supports the paper's central claim and costs no additional experiments (simply compute across the 5 seeds already run).
2. **Measure and report pairwise input-gradient cosine similarity** between ensemble members for FoRDE variants and top baselines (DE, LIT) on CIFAR-10 or CIFAR-100. This would directly test whether the repulsion mechanism produces the intended diversity in the main setting.
3. **Run an ablation comparing FoRDE-PCA to a version with PCA lengthscales in the driving force only + identity repulsion**, to disentangle the PCA kernel's prior-like effect from the repulsion effect.
4. **Include a per-corruption-type breakdown figure** (e.g., 19 corruption types × 5 severity levels) in the appendix and show standard errors across seeds, to demonstrate that FoRDE-PCA's gains are systematic rather than driven by a few corruptions.
5. **Briefly note why toy experiments use 16 members vs. 10 in the main experiments**, to avoid confusion.

## Score and Decision

The paper makes a genuine contribution — input-gradient space repulsion is a novel and well-motivated idea, the PCA kernel design is elegant, and the empirical validation spans extensive baselines. The main weakness (missing error bars on the key corruption metrics) is significant but readily addressable. No fatally flawed reasoning or unsupported claims remain after filtering. With the addition of uncertainty quantification and the suggested diversity measurement, the paper would be clearly ready for acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>