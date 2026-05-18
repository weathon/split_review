Now I have a complete picture. Let me write the final consolidated review.

## Summary

This paper introduces a Shapley value-based framework to quantify the contribution of individual frequency components to model predictions in out-of-distribution (OoD) generalization. The analysis reveals class-wise patterns of positive and negative frequency components and provides interpretations for why different OoD algorithms (e.g., RSC vs. IRM) succeed on different shift types. Building on these insights, the authors propose Class-wise Frequency Augmentation (CFA), a data-level method that enhances positive frequency components and suppresses negative ones. The method is model-agnostic and consistently improves five baseline OoD algorithms across seven datasets, with a standout result on ColoredMNIST lifting accuracy from 60.2% to 73.0%.

## Strengths

- **Novel Shapley-value quantification of frequency contributions to OoD generalization.** The paper introduces a principled game-theoretic measure (Shapley value) to attribute the influence of individual frequency components on model predictions. This yields interpretable class-wise frequency patterns (Figure 1) that are consistent across domains, providing a new analytical tool for studying OoD behavior.

- **Plausible and visually grounded explanations of algorithm behavior on different shift types.** Using the Shapley-value distributions, the paper offers frequency-domain explanations for algorithm performance: RSC filters harmful low-frequency components on diversity-shifted PACS (Section 3.2), while IRM emphasizes middle-frequency components that avoid spurious color correlations on ColoredMNIST (Section 3.3). These interpretations are supported by Figures 3–5 and provide intuitive reasoning tied to the frequency domain.

- **Consistent and substantial empirical improvements via CFA.** The proposed CFA method improves five baseline algorithms (ERM, IRM, RSC, CORAL, W2D) across all seven evaluated datasets (Tables 1–3), including both diversity shift (PACS, OfficeHome, Terra Incognita, DomainNet) and correlation shift (ColoredMNIST, CelebA, NICO) benchmarks. The largest gain—IRM on ColoredMNIST from 58.9% to 74.3% (ablation) and from 60.2% to 73.0% (state-of-the-art comparison)—is striking given the 75% ceiling. The method is model-agnostic and operates on the data, not the architecture.

- **Comprehensive evaluation covering both shift types and large-scale datasets.** The experiments span seven datasets and five baseline algorithms, including DomainNet at scale. The state-of-the-art comparison (Table 2) reports means and standard errors over three runs, and CFA achieves the best results on six datasets.

## Weaknesses

### Major

- **The Shapley value computation on partial frequency reconstructions rests on an unvalidated and potentially problematic assumption.** The value function *V* (Equation 6) evaluates the model's output on images reconstructed from only a subset of frequency components. An input that retains, say, 10% of Fourier coefficients typically produces a highly degraded reconstruction with ringing artifacts or blur that differs substantially from natural images. It is a well-documented challenge in feature attribution that model behavior on off-manifold inputs can be erratic and may not reflect genuine feature importance. The paper neither acknowledges this issue nor provides any validation—for example, by comparing Shapley-based attributions with simpler frequency ablation (measuring accuracy drops when frequency bands are removed) or with gradient-based attribution methods in the frequency domain. Because the entire analysis in Sections 3.2–3.3 and the design of CFA rest on these attributions, this is a structural concern. The empirical success of CFA provides some indirect support, but a direct validation is needed to distinguish whether the improvements come from principled attribution-driven augmentation or from a generic frequency-space augmentation that would work with randomly selected bands. A control experiment randomizing the selection of augmented frequency components (while keeping the augmentation pipeline otherwise identical) is the minimal experiment needed to substantiate the central claim.

### Minor

- **Inconsistent experimental reporting: single-run ablation vs. three-run main comparison.** The ablation study (Section 5.1) reports single runs with fixed random seed (Table 3), while the state-of-the-art comparison (Section 5.2) averages three runs with standard error (Table 2). This inconsistency makes it impossible to assess whether the large improvements in the ablation—notably the IRM jump from 58.9% to 74.3% on ColoredMNIST—are statistically significant or reflect a single lucky seed. The ablation results should report means and standard deviations over multiple seeds for comparability.

- **Missing hyperparameter values critical for reproducibility.** The number of Shapley sampling permutations *m* (Equation 2, Algorithm 1) is never given a concrete numerical value. Similarly, the augmentation hyperparameters α and β (Equation 8, Algorithm 1) are introduced but their values and sensitivity are not reported. Without these, the experiments cannot be reproduced faithfully.

- **The empty-set baseline *f*(∅) is not specified.** In Equation (6), the value function subtracts *f*(∅). The paper states that the Shapley value property *V*(∅)=0 holds, but does not clarify what input ∅ corresponds to in practice: a zero-frequency image? A mean image? Different choices yield different Shapley values, and this should be justified.

- **The theoretical analysis (Section 4.2) is too informal to carry weight.** Theorems 1 and 2 are stated with no assumptions, no proof outline (images referenced in the text are missing from the parsed version; the original submission may have proofs, but the theorems as stated do not connect to the actual CFA algorithm's design), and no formal specification of how α, β, or the class-wise aggregation relate to the causal/non-causal decomposition. The paper would be better served by either removing this section or replacing it with clear intuitive motivation rather than presenting what purports to be a theorem but lacks the standard components of one.

### Trivial

- **The weighting scheme for aggregating *p<sub>r</sub>* (Algorithm 1, line 4)** uses the cardinality of positive components as weights, divided by *d<sub>1</sub>d<sub>2</sub>*, without motivation. A simple explanation of why this form is chosen over alternatives (e.g., a mean) would improve clarity.

## Nice-to-Haves

- A discussion of computational cost (number of Shapley permutation *m*, wall-clock overhead relative to ERM) would help readers assess practicality, especially for larger images (224×224 DomainNet).
- A brief limitations section acknowledging the off-manifold attribution concern and the potential scalability issues would strengthen the paper's rigor.

## Removed Points

- **Criticism about comparing with only five algorithms / insufficient baselines.** The paper tests on five algorithms across seven datasets, which is a thorough evaluation for an augmentation method of this type. Claims of "seamless integration" are appropriately scoped to the tested algorithms.
- **Criticism about the "state-of-the-art" claim lacking comprehensive leaderboard comparisons.** The provided comparisons—including DFF and other recent baselines—are sufficient for the paper's claims. Exhaustive leaderboard coverage is beyond reasonable expectations for a single paper.
- **Criticism about the computational cost being "enormous" implied as a fatal flaw.** This is a legitimate consideration but not a fatal weakness; it belongs as a reproducibility and practicality note (now in Minor and Nice-to-Haves).

## Novel Insights

The most interesting observation from the reviews is that the paper's interpretability claims (contributions 1 and 2) and its algorithmic contribution (contribution 3, CFA) may be partially decoupled. The CFA method could potentially work as a generic frequency-domain data augmentation even if the Shapley-based attribution is imperfect—the class-wise frequency patterns may be capturing coarse signal that suffices for augmentation even if individual frequency attributions are noisy. This means the paper has a stronger floor (CFA empirically works) even if the ceiling (exact attribution interpretation) requires more validation. Conversely, if the authors can validate the attributions (e.g., via the randomized augmentation control), the paper becomes stronger than the sum of its parts.

## Suggestions

1. **Validate the Shapley attribution.** Add a control experiment where CFA uses randomly selected frequency components of the same sparsity as the Shapley-selected ones. If Shapley-selected patterns yield significantly better OoD accuracy, the attribution is doing useful work. Also consider comparing with a simpler attribution method (e.g., measuring accuracy drop when removing frequency bands) to show that Shapley values correlate with a meaningful measure of frequency importance.

2. **Report uncertainty for all experiments.** Run the ablation study (Table 3) over at least three seeds and report means with standard deviations, consistent with the main comparison.

3. **Report concrete hyperparameters.** Specify the numerical value of *m* (number of Shapley permutations), the values of α and β used in experiments, and perform a sensitivity analysis for these parameters.

4. **Clarify the empty-set baseline.** State explicitly what image/input ∅ corresponds to in the Shapley value computation and discuss why this choice is reasonable.

5. **Either formalize or remove the theoretical section.** The informal theorem statements do not add scientific value as presented. If rigorous analysis is not possible, replace with prose intuition and remove the theorem labels to avoid misleading claims of provable guarantees.

## Score and Decision

**Originality:** 7/10 — Shapley values in the frequency domain for OoD is a genuinely novel combination.
**Importance of research question:** 8/10 — OoD generalization is an important problem, and understanding frequency-domain patterns is timely.
**Soundness of experiments:** 6/10 — The empirical results are extensive and positive, but the single-run ablation and missing hyperparameters reduce confidence. The core concern about attribution validity is unaddressed.
**Claims support:** 5/10 — The CFA effectiveness is well-supported, but the interpretability claims (contributions 1–2) rest on an unvalidated attribution assumption.
**Clarity of writing:** 6/10 — The overall structure is clear, but some methodological details are missing and the theoretical section is vague.
**Value to community:** 7/10 — CFA is a simple, effective, and model-agnostic method that could be widely adopted. The frequency-domain analysis perspective may inspire future work.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>