Now I have a solid bracket. Let me finalize by comparing CausalNovo against these anchors and then write the consolidated review.

My bracket: CausalNovo lands between RankNovo (5.50, modest improvements, rejected) and ReNovo (6.50, novel RAG application, accepted). It's clearly above RankNovo — CausalNovo has much larger and more consistent gains, more comprehensive experiments, and a principled (if imperfect) framework. Compared to ReNovo, CausalNovo has broader model-agnostic validation (3 architectures vs 1), richer ablations, and stronger robustness analysis, but weaker theoretical coherence between the causal framing and the implementation. I'd place it at approximately 6.0.

Now let me write the consolidated review.

---

## Summary
This paper proposes CausalNovo, a model-agnostic framework for de novo peptide sequencing that aims to learn representations robust to spectral noise by disentangling causal signal ions from spurious noise peaks. Grounded in a Structural Causal Model, the framework introduces a Causality Extraction Module that separates representations into causal and non-causal components, trained with contrastive learning (independence) and cross-entropy (sufficiency/purification) objectives, plus a label-guided spectrum perturbation as a causal intervention. Experiments across three benchmark datasets and three transformer-based architectures show consistent and often substantial gains in amino acid, peptide, and PTM-level metrics.

## Strengths
- **Model-agnostic effectiveness with consistent gains:** CausalNovo improves three distinct architectures (CasaNovo, AdaNovo, π-HelixNovo) across three datasets (Nine-species, Seven-species, HC-PT), with amino acid precision improvements up to ~14% on HC-PT and consistent peptide-level and PTM-level gains (Tables 1–2). This breadth of validation is a genuine strength.
- **Well-designed vulnerability analysis that directly supports the core claim:** Figures 1 and 3 show that systematically replacing noise peaks degrades baseline models while CausalNovo-augmented models maintain substantially higher precision, directly demonstrating reduced reliance on spurious non-causal peaks.
- **Thorough ablation studies that isolate each component's contribution:** Table 4 decomposes the independence, purification, and symmetric training contributions; Table 5 ablates the replace and enhance steps of the causal intervention. Each component is shown to add incremental value.
- **Robustness demonstrated across noise levels and species:** Figure 4 shows CausalNovo maintains higher precision than baselines across a wide range of Noise Signal Ratios; Table 3 shows consistent cross-species improvements (average +2.6% peptide precision).
- **Reproducible implementation:** Architecture details, hyperparameters, and training protocol are clearly specified; code is provided.

## Weaknesses

### Fatal
None.

### Major
- **The purification objective lacks a coherent causal justification.** The paper states that maximizing \(I(z_s; Y)\) — i.e., encouraging the *non-causal* representation to predict the label — "indirectly leads to the purification of \(z_c\)." Given the SCM posits that \(Y = g(C)\) with \(C \perp S\), forcing the non-causal stream to predict \(Y\) is in tension with the stated goal. The paper does not explain the competition mechanism by which this produces purification. While the ablation (Table 4) shows the auxiliary loss helps empirically (+0.8% amino acid precision), the theoretical rationale is unconvincing as written. This weakens the paper's claim to a principled causal framework.

- **The causal intervention is not a clean intervention on non-causal factors.** The intervened spectrum is defined as \(x_{\text{intervene}} = x_{\text{replace}} \cup x_{\text{theory}}\), where \(x_{\text{theory}}\) is the full theoretical spectrum derived from the ground-truth label \(Y\). Adding the theoretical spectrum injects label-derived causal signal into the augmented view, meaning the "intervention" alters \(C\) as well as \(S\). The paper frames this as "preserving the causal relationship," but it is better described as label-guided data augmentation. The empirical benefits are real (Table 5), but the gap between the do-calculus framing and the implementation should be acknowledged rather than papered over.

### Minor
- **The contrastive loss (Eq. 5) does not condition on \(Y\) in practice.** The stated objective is maximizing \(I(z_c; z_c' | Y)\), but negatives are drawn from the full training batch regardless of label. While peptide diversity makes same-label collisions rare in practice, the approximation is to \(I(z_c; z_c')\) rather than the conditional form. This is a technical imprecision rather than a practical flaw.
- **Missing "Enhance-only" ablation.** Table 5 shows Replace, Replace+Enhance, and Replace+Enhance+Drop, but does not isolate the effect of adding the theoretical spectrum *without* the replacement step. This makes it impossible to determine whether the theoretical spectrum alone (as pure data augmentation) accounts for part of the gain.
- **No variance estimates or statistical testing.** Some reported improvements are small (e.g., +0.4% from symmetric training in Table 4), and without variance it is unclear whether these differences are reliable. This is standard for the field but would strengthen the paper.
- **Retrained baseline discrepancies are not discussed.** CasaNovo's original reported HC-PT precision (0.442) differs substantially from the retrained version (0.525, Table 1). While the comparison to the retrained baseline is the fair one (since CausalNovo uses the same training recipe), the large discrepancy warrants a brief explanation.

### Trivial
- The attention analysis (Table 7) relies on an external interpretability tool (π-xNovo) and should be presented as suggestive rather than conclusive evidence.

## Nice-to-Haves
- Comparing against simpler invariance-enhancing baselines (e.g., standard contrastive pretraining, random peak dropout, or adversarial noise training) would help clarify whether the elaborate causal intervention machinery is necessary or whether simpler robustness methods achieve similar gains.
- The paper notes a ~2.3× training time overhead; a brief runtime comparison against baselines would help practitioners assess the cost-benefit tradeoff.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *Harsh Critic claim that the purification objective is a "structural issue that undermines the theoretical backbone"*: While the purification justification is indeed confusing (kept as Major), it is an auxiliary objective, not the core theoretical claim. The core principles of independence and sufficiency are reasonably motivated. Calling it "structural" and "fatal" overstates the problem.

- *Harsh Critic claim that the vulnerability analysis is "confounded" because replacing noise peaks can remove weak information-carrying features*: The analysis uses well-established domain knowledge (theoretical spectra based on b/y/a ions) to distinguish signal from noise. The paper acknowledges this is an approximation (m/z tolerance thresholds). The analysis remains informative and the conclusion that baselines rely on non-causal peaks is supported.

- *Harsh Critic claim that the attention analysis "should be regarded as anecdotal rather than conclusive"*: Kept as Trivial; the paper itself does not overclaim this analysis.

- *Harsh Critic claim that the SCM assumption that C and S can be cleanly separated is "never empirically verified"*: This is not a verifiable claim — latent factor separation is inherently unobservable. The paper validates the framework's effectiveness through downstream performance, which is the appropriate standard.

- *Strength Finder: "Theoretical grounding in a well-defined causal model"*: Qualified and kept, but the SCM is described at a high level and the step from RCCP to structural equations is terse.

- *Strength Finder generic claims about "important problem" or "interesting question"*: Removed — these are generic and not specific to this paper.

## Novel Insights
None beyond the paper's own contributions. The vulnerability analysis methodology (systematic noise-peak perturbation with varying m/z thresholds) is a useful evaluation protocol that could be adopted by future work in de novo sequencing, though it is not entirely novel (it builds on practices from Zhou et al., 2024).

## Suggestions
- Reframe the purification objective transparently — e.g., as a competitive self-supervision signal that encourages the CEM to assign Y-relevant information to \(z_c\) rather than \(z_s\) — rather than asserting it follows from causal principles.
- Add the missing Enhance-only ablation (theoretical spectrum added as pure augmentation without replacement) to clarify what drives the gains.
- Acknowledge explicitly that the theoretical-spectrum addition in the intervention is a form of label-informed augmentation rather than a pure do-operation on S, and discuss whether this creates any train-test mismatch.
- Report standard deviations or confidence intervals for at least the key results.

## Score and Decision

**Anchor comparison:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| RankNovo (87B3zDRMjv) | 5.50 | R1 | CausalNovo clearly stronger: larger gains, model-agnostic, richer analysis |
| CrossNovo/Distillation (I2ZYngkRW6) | 4.25 | R1 | CausalNovo substantially stronger: broader experiments, principled framework |
| ReNovo (uQnvYP7yX9) | 6.50 | R1 | Comparable empirical strength; ReNovo has cleaner story, CausalNovo has broader validation but weaker theoretical coherence |
| CL-MFAP (fv9XU7CyN2) | 5.75 | R2 | CausalNovo stronger: more comprehensive experiments, larger gains |
| CausalIB (qac43AwuL9) | 6.00 | R2 | CausalNovo has weaker theory but much stronger empirical validation on real application |
| Multimodal Causal Bio (hjROBHstZ3) | 5.80 | R2 | CausalNovo has stronger and more complete empirical results |

**Bracket:** Round 1 placed CausalNovo between 5.50 (RankNovo) and 6.50 (ReNovo). Round 2 narrowed this: CausalNovo is clearly above the 5.50–5.80 range and sits near ReNovo at 6.50 but slightly below due to the theoretical gaps between causal framing and implementation. CausalNovo's empirical contribution (model-agnostic, well-ablated, consistent gains across architectures and datasets) is genuinely strong; the theoretical narrative is somewhat overclaimed but the method works and the ablation studies substantiate each design choice. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>