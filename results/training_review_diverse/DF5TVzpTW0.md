Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

This paper introduces DPPN (Defense through Perturbing Privacy Neurons), a method that identifies a small subset of embedding dimensions ("privacy neurons") correlated with a sensitive token and perturbs only those dimensions using directional noise, rather than perturbing all dimensions uniformly. The approach uses a differentiable HardConcrete-based mask learning framework to detect privacy neurons in a black-box setting, and a neuron-suppressing perturbation function that pushes embeddings toward the negative direction to increase indistinguishability. Experiments across multiple datasets, attack models, and embedding architectures show that DPPN achieves substantially lower privacy leakage than baselines (LapMech, PurMech) while maintaining higher downstream task utility.

## Strengths

- **Targeted perturbation of privacy neurons, supported by clear evidence**: The core idea — identifying and selectively perturbing only privacy-sensitive dimensions rather than all dimensions — is well-motivated and validated. On STS12 at ε=2, DPPN reduces leakage from 60% (unprotected) to 13%, while LapMech and PurMech only achieve 22% (Section 4.2). The preliminary analysis (Figure 2) confirms that top privacy neurons have significantly higher sensitivity than tail neurons (p=1.30e−21).

- **Black-box neuron detection approaches white-box performance**: The differentiable mask learning framework (Section 3.2) enables privacy neuron detection without access to the attack model. At ε=2, DPPN shows only 3–6% absolute difference in leakage and <5% relative difference in downstream performance compared to the white-box DPPN-Oracle (Figure 4), and identifies 32–51% of the same top neurons as the white-box method (Figure 5).

- **Neuron-suppressing directional perturbation vs. isotropic noise**: The suppress function (Eq. 6) injects one-sided noise in the negative direction, making data points more indistinguishable than isotropic perturbations (Figure 3). At r=10%, suppress reduces leakage by 15.44% and improves downstream performance by 45.12% relative to full-dimension perturbation, while isotropic methods applied to the same neurons show negligible change (Table 2, Section 5.2).

- **Comprehensive evaluation across attacks, models, and real-world data**: DPPN is tested against three attack models (Vec2text, GEIA, MLC), three embedding models (GTR-base, Sentence-T5, SBERT), and two real-world privacy datasets (PII-Masking300K, MIMIC-III). On MIMIC-III, DPPN reduces sex information leakage to 17% vs. 43% for baselines (Table 4). A case study (Table 6) shows DPPN preserves 62% semantic similarity when baselines degrade to 11%.

- **Interpretable and semantically meaningful neuron selection**: Qualitative analysis (Figure 6) shows that semantically similar words (e.g., weekdays, countries) cluster on the same top-5 neuron indices, and DPPN provides implicit protection to related tokens with 36–46% leakage mitigation (Section 5.3).

## Weaknesses

### Major
None.

### Minor
- **Downstream utility metric is not explicitly defined**: The paper states it reports "dataset-specific downstream performance" (line 139) but never specifies what metric is used for STS12 or FIQA (e.g., Spearman correlation? accuracy on a derived task?). While a reader familiar with STS benchmarks may infer the metric, the omission makes the utility numbers harder to interpret and the experiments harder to reproduce. This is the most significant clarity gap in the paper.

- **Leakage metric protocol for sentence-level attacks is underspecified**: The paper defines "Leakage" as "the attack model's accuracy in predicting sensitive tokens" (line 139). For sentence-level attacks like Vec2text that generate free text, it is unclear whether accuracy is computed by scanning the generated text for the token, using a separate classifier head, or some other method. The same concern applies to "Confidence." This is a reproducibility issue.

- **Noise variance scaling has a ≈√2 discrepancy**: The paper states that scaling ε by √(k/d) "ensures consistent noise variance with full-dimension methods" (line 137). However, the suppress perturbation (Eq. 6) uses one-sided (half-Laplace) noise whose per-dimension variance is b², while the symmetric Laplace used by LapMech has variance 2b². Matching total noise variance would require scaling by √(k/(2d)) rather than √(k/d). This does not invalidate the overall comparison (DPPN still adds less noise to non-sensitive dimensions) but the formal claim about variance matching is imprecise.

- **Full-perturbation baseline values not shown in Table 2**: Table 2 reports "relative improvement compared to the full perturbation" as percentages, but the absolute values for the r=100% case are not displayed. The reader cannot verify the claimed relative improvements.

- **Sparsity regularization constants (γ, ξ) are not specified numerically**: Equations 3 and 5 use γ and ξ without giving their values or a reference to standard defaults in the HardConcrete literature. This makes the sparsity behavior of the learned mask partly unspecified.

- **Multi-token scenario not discussed**: The paper evaluates on one sensitive token at a time. Real deployments would need to protect multiple sensitive tokens that may co-occur (e.g., a name and a disease in the same sentence). The paper does not discuss how masks would combine or interact when multiple tokens are protected simultaneously. This is noted as a practical limitation; the paper does scope its method to protecting a "set of sensitive tokens" (Goal 1, line 42), so this is a limitation rather than a flaw.

### Trivial
None

## Nice-to-Haves
- An ablation experiment that applies isotropic noise solely to selected privacy neurons (not all dimensions) would more clearly isolate whether the benefit of DPPN comes from the directional perturbation, the neuron selection, or both. (Table 2 partially addresses this but the "relative improvement" framing without absolute baselines makes comparison difficult.)
- Reporting the number of sentences needed per token (|D⁺|) to learn a stable mask would help practitioners assess feasibility.
- A brief discussion of how to handle sentences containing multiple sensitive tokens with potentially overlapping privacy neurons.

## Removed Points

The following points from the harsh critic are removed with justifications:

1. **Criticism that Eq. 4 pushes optimization in the wrong direction**: REMOVED — the reviewer's algebraic interpretation is incorrect. Minimizing ℒ = −Σ log P(x⁺) − Σ(1 − log P(x⁻)) correctly pushes P(x⁺) → 1 (token present) and P(x⁻) → 0 (token absent). The reviewer's derivation conflates the direction of optimization.

2. **Claim that "DPPN achieves higher downstream performance than the non-protected baseline" as a red flag**: The paper's text explicitly says DPPN "maintains or enhances the downstream performance relative to **baseline methods**" (LapMech, PurMech), not relative to the no-defense baseline (line 152). The specific numerical comparison cited by the reviewer (84.21% vs. 65.47%) does not appear in the extracted text and cannot be verified. The paper's central comparison is against LapMech/PurMech, and DPPN's advantage over those methods is clearly established. The downstream metric definition is indeed underspecified (kept in Minor above), but the specific claim about "exceeding no-defense" is a reviewer misreading.

3. **"Title overclaims generality"**: REMOVED — the paper clearly scopes its approach within Section 2.2 (Goal 1: "the data owner defines a set of sensitive tokens T"), and the title accurately reflects the paper's content.

4. **Criticism that the method is "concept-specific" rather than a general defense**: REMOVED — the paper's stated goals explicitly define the defense as protecting a predefined set of sensitive tokens. Evaluating it against the wrong class of expectations (a general, all-purpose defense) is out of scope.

5. **Perturbation scaling critique framed as fatal apples-to-oranges comparison**: DOWNGRADED from fatal to minor. The reviewer correctly identifies that the one-sided noise has different variance (b² vs. 2b²), creating a √2 factor discrepancy in the claimed variance matching. However, this is an imprecision in the formal claim, not a fatal flaw. The paper's core comparison — showing DPPN outperforms LapMech/PurMech at the same ε — remains valid since the discrepancy equally applies across all DPPN experiments and doesn't affect the relative ranking.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Explicitly state the downstream metric for each dataset (e.g., "Spearman correlation for STS12, NDCG@k for FIQA"). This is the most important fix for the camera-ready version.
2. Describe the exact protocol for computing Leakage and Confidence from free-text attack outputs like Vec2text.
3. Correct the noise variance scaling claim to reflect the one-sided vs. symmetric Laplace difference.
4. Add the absolute r=100% baseline values to Table 2 alongside the relative improvements.
5. Provide the numerical values or literature defaults for γ and ξ in the sparsity regularization.
6. Add a brief discussion of the multi-token scenario — even a paragraph acknowledging the challenge and sketching a solution (e.g., union of masks) would strengthen the practical framing.

## Score and Decision

The paper proposes a genuinely novel and well-motivated approach (targeted privacy neuron perturbation instead of uniform noise injection), validates it across a comprehensive set of experiments, and achieves convincing results. The main weaknesses are presentation/definition issues rather than flaws in the methodology or evidence. The paper makes a clear contribution to the privacy-preserving embedding literature.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>