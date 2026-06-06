## Summary

ScaPre is a closed-form framework for large-scale multi-concept unlearning in text-to-image diffusion models. It combines a *conflict-aware stable design* (spectral trace regularizer + Bures geometry alignment) with an *Informax Decoupler* (MI-based channel reweighting) to simultaneously achieve scalability, precision, and efficiency. The system is evaluated on object unlearning at scale (ImageNet-Diversi50: 50 concepts), fine-grained precision (ImageNet-Confuse5), and artistic style unlearning, where it consistently outperforms existing methods across all settings.

---

## Strengths

- **Scalable unlearning with quality retention (Table 3):** On ImageNet-Diversi50 (50 diverse object classes), ScaPre reduces average classifier accuracy to 3.9% while maintaining a CLIP score of 29.41 and UQ of 65.30 — compared to the nearest competitor ESD at 19.6% accuracy / 28.21 CLIP / 56.35 UQ. UCE and RECE achieve near-zero accuracy but with catastrophic CLIP collapse (~22), placing them in a qualitatively different failure regime. Figure 4 shows that ScaPre's accuracy and UQ remain stable as concepts scale from 10 to 50, while all other methods degrade.

- **Precision with fine-grained concept disentanglement (Table 4):** On ImageNet-Confuse5, ScaPre achieves 5.8% unlearn accuracy and 76.3% preserve accuracy (overall: 84.3%), more than 1.7× higher than the next best method (ESD/SP at ~50%). This directly demonstrates that the Informax Decoupler confines updates to the target subspace without collateral damage to visually similar non-target concepts — a qualitative gap, not a marginal improvement.

- **Lightweight closed-form design:** Section 5.5 reports low peak memory (~5 GB), with no auxiliary sub-models or additional training data required, and a principled derivation via Sylvester equation (Eq. 9) with a proximal Bures geodesic refinement for the non-quadratic geometry alignment term. The derivation is rigorous and the solution is reproducible.

- **Strong style unlearning (Table 2):** ScaPre achieves the lowest residual style similarity (CLIP_art = 26.51), highest CLIP_x = 3.44 (balance score), competitive FID (14.37 vs. base 13.60), and highest CLIP_coco among the best unlearning methods — establishing a consistently favorable trade-off.

---

## Weaknesses

### Fatal
None.

### Major

- **Timing inconsistency in a headline efficiency claim.** Section 5.5 and the bullet point on page 2 state that ScaPre "complet[es] the unlearning of 50 concepts within only 120 seconds." However, Figure 3 (and its accompanying data table) shows ScaPre at approximately 1.5 hours execution time, tied with RECE and SP — and slower than UCE (~0.5 hours). The most plausible reconciliation is that "120 seconds" refers exclusively to the closed-form optimization step, while "1.5 hours" includes image generation for evaluation. But this distinction is never stated, and no other method's 120-second-equivalent is reported. As written, the comparison is apples-to-oranges: claiming 120 seconds while the table reports 1.5 hours directly contradicts one of the paper's three headline contributions. This requires an explicit clarification: what does each number actually measure, and how does each baseline's evaluation overhead compare?

- **Neutral inputs for MI computation are undefined, creating a reproducibility gap.** Section 4.2 defines MI between a channel's activation state and a binary label $y \in \{0,1\}$, where $y=0$ is assigned to "neutral inputs." These neutral inputs are never defined — not in the main text, not in the caption, and not in the method description. The MI scores ($\text{MI}_i$) directly determine the $\alpha$ weights that govern which parameters are updated and by how much, making the neutral input distribution a load-bearing design choice. The paper elsewhere claims "no additional data" (contribution bullet 3), which appears to conflict with requiring a population of neutral inputs. Without specifying what constitutes a neutral input and how to construct this population, the Informax Decoupler cannot be faithfully reimplemented.

### Minor

- **Gating function description may be imprecise.** Section 4.1 describes $\mathbf{R}$ using the gating rule $\tilde{\sigma}_i = (1 - \text{sigmoid}(\sigma_i))\sigma_i$, claiming it "softly decays large singular values while leaving smaller ones nearly intact." However, as $\sigma_i \to 0$, $\text{sigmoid}(\sigma_i) \to 0.5$, so $\tilde{\sigma}_i \to 0.5 \cdot 0 = 0$. For a small but positive $\sigma_i$ (e.g., 0.1), the factor $(1 - \text{sigmoid}(0.1)) \approx 0.475$, meaning small singular values are also suppressed by ~50% — not "left nearly intact." The formula does suppress large values more aggressively (approaching 0 as $\sigma_i \to \infty$), so the relative effect is in the right direction, but the stated intuition is inaccurate. The empirical results suggest the mechanism functions well in practice, but the description should be corrected.

- **UQ is a distribution-normalized, author-defined metric whose absolute values are comparison-set-dependent.** As defined, $\tilde{A}$ and $\tilde{C}$ are z-score normalized relative to the current pool of methods, so UQ values change when methods are added or removed. UCE and RECE's catastrophic quality collapse (CLIP ~22) shifts the normalization in ScaPre's favor. This does not undermine the paper's conclusions — the individual component metrics (unlearn accuracy and CLIP score) are explicitly reported and tell the same story — but UQ should not be presented as if it were an established community metric. Its sensitivity to the comparison set should be acknowledged.

- **"SP" abbreviation introduced without definition in the main text.** Tables 1–4 include an "SP" column that refers to Sculpting Memory (Li et al., 2025a), but the abbreviation is never explicitly introduced in the main text; it appears first as a table header. Minor readability issue.

### Trivial

- The scalability curves in Figure 4 truncate UCE and RECE without a stated formal criterion for truncation. The paper says "severe generative collapse," but a threshold (e.g., CLIP < 25) would make this a principled and auditable design decision rather than a judgment call.

---

## Nice-to-Haves

- An ablation summary in the main text comparing ScaPre-without-R (no inter-concept suppression), ScaPre-without-S (no conflict detection), and ScaPre-without-α (no Informax Decoupler) would clarify which component drives the precision gain (Table 4) versus the scalability gain (Table 3). The paper indicates these ablations are in Appendix C.5–C.7, but given the Informax Decoupler's novelty, a headline summary of component contributions would strengthen the narrative.

- An experiment varying the neutral input distribution in MI computation (e.g., random embeddings vs. semantically adjacent embeddings vs. null-text embedding) would demonstrate robustness of the Informax Decoupler — particularly useful given the current underspecification.

- A short analysis of *why* UCE and RECE fail at scale (e.g., showing the optimization landscape becomes ill-conditioned at 50 concepts without the spectral components) would provide causal evidence for the design choices rather than purely correlational comparison.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"×5 more concepts" exact threshold not stated.** The harsh critic notes this number depends on an undefined "acceptable quality" threshold. This is a very minor presentation concern, and the scalability trend in Figure 4 visually supports the claim even without a formal threshold. Not sufficient to constitute a weakness — removed.

- **Computational complexity of Sylvester solve.** The concern about inverting a $(d_{in} \cdot d_{out}) \times (d_{in} \cdot d_{out})$ Kronecker matrix is valid in principle, but the paper explicitly says it uses "standard Sylvester solvers" that avoid the explicit Kronecker product (Eq. 10 is presented for reference, not as the computational path). The 120-second (or 1.5-hour, depending on clarification) runtime and 5 GB memory footprint empirically demonstrate the solver is tractable. Removed as speculative concern.

- **ESD achieves 19.6% accuracy on ImageNet-Diversi50, so "universally encounter" framing is slightly overstated.** This is a valid rhetorical note (the paper uses strong language), but it does not weaken any experimental claim. The paper itself says "none has been able to *fully* overcome these challenges" — ESD partially addresses scale but fails at precise disentanglement (Table 4: 57.7% preserve acc). Removed as a nitpick.

- **CLIP_art / style selection bias.** The concern that CLIP_art and human perception might diverge if both respond to the same surface features is plausible but purely speculative — no evidence in the paper supports this concern as an actual problem with the results. Removed as unanchored.

- **Missing related works** — removed per hard rules.

- **Ablation studies deferred to appendix** — removed per hard rules (appendix is stripped from parsed version; these exist in the original).

---

## Novel Insights

The paper's most genuinely novel contribution is the combination of the Informax Decoupler with a Bures geodesic proximal refinement for geometry alignment in a closed-form unlearning framework. Prior closed-form unlearning methods (UCE, RECE) fail at scale because their quadratic objectives cannot suppress inter-concept conflicts. ScaPre's insight is that the problem has two distinct failure modes — optimization instability (addressed by spectral regularization and geometry alignment) and parameter non-specificity (addressed by MI-based channel reweighting) — and that both need simultaneous treatment. The particularly striking evidence for the Informax Decoupler's necessity comes from Table 4: the preserve accuracy gap between ScaPre (76.3%) and all methods that achieve comparable unlearn accuracy (UCE: 5.6%, RECE: 5.5%) is not incremental — it is qualitative, suggesting the Decoupler provides a structural separation of concept-relevant from concept-adjacent parameters that purely closed-form methods without channel gating cannot achieve.

---

## Suggestions

1. **Clarify what the 120-second figure actually measures** — specifically, whether it covers only the closed-form optimization step or the full pipeline including evaluation. Report the optimization-only time for all closed-form baselines (UCE, RECE) on equal footing. This is the single highest-priority fix.

2. **Specify the neutral input distribution for MI computation** — at minimum, state concretely in the main text what inputs are used for $y=0$, and whether these count as "additional data" in the efficiency comparison or not.

3. **Correct the gating function description** — either adjust the formula (e.g., add a shift $\kappa$ so $(1-\text{sigmoid}(\sigma_i - \kappa))$ is near 1 for small $\sigma_i$) or revise the stated intuition to match the actual behavior of the formula.

4. **Add a formal truncation criterion for the scalability curves** (e.g., CLIP < X or generative collapse defined by FID > Y) so the decision to truncate UCE and RECE curves is auditable.

---

## Evaluation on Core Axes

**Originality:** Moderate-to-good. The combination of spectral trace regularization (with SVD-based gating on inter-concept subspace), Bures geodesic geometry alignment, and MI-based channel decoupling is novel as a system. Each component adapts known tools (SVD, Bures distance, mutual information) to a new problem setting.

**Importance:** High. Scalable and precise concept unlearning in deployed diffusion models is a pressing practical problem with direct implications for copyright, safety, and content moderation. Demonstrating 50-concept removal without generation quality collapse addresses a real bottleneck.

**Claims supported:** Mostly. The precision and scalability claims are robustly supported by Tables 3 and 4 with multiple metrics. The efficiency claim is undermined by the 120-second vs. 1.5-hour inconsistency.

**Soundness of experiments:** Good. Comprehensive benchmarks (Imagenette, ImageNet-Diversi50, ImageNet-Confuse5, 50-artist styles, I2P), multiple metrics, and comparison against 7+ baselines. The UQ metric's distribution-dependence is a minor flaw; the component metrics tell the same story.

**Clarity of writing:** Adequate but with notable gaps — the timing discrepancy and the undefined neutral inputs are clarity failures in sections central to the paper's contribution.

**Value to research community:** High. New benchmarks (ImageNet-Diversi50, ImageNet-Confuse5) and a clearly superior operating point on the unlearning/quality/efficiency frontier will be useful to the community. The closed-form design with publicly reproducible baselines is a practical contribution.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>