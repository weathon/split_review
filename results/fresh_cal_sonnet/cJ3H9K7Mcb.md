Let me read the full paper sections and then run calibration searches.Now I have enough to write the final review. Let me compile all findings.Now I have everything I need. Let me write the final consolidated review.

---

## Summary

This paper argues that standard OOD benchmarks, which evaluate models at a fixed degree of distribution shift, yield an incomplete and potentially misleading picture of model robustness. The authors construct multi-degree variants of MNIST and CIFAR10 (NoisyMNIST, RotatedMNIST, LowLightCIFAR10) and additional ImageNet-subset datasets, then test over 20 DG algorithms across multiple architectures. Their central findings are: (1) models selected for best performance at one noise level show sharp drops at slightly stronger levels; (2) training on strongly-shifted data does not reliably guarantee robustness at milder degrees, in a task-dependent way; and (3) CLIP, adapted via linear probing, is disproportionately brittle to distribution shifts rarely seen during pre-training.

---

## Strengths

- **Concrete evidence of model-selection brittleness.** Table 1 (Section 4.2) shows that VREx on ResNet-50 achieves 64.6% at $\mathcal{D}_4$ but falls to 32.1% at $\mathcal{D}_5$ (a 50.3% relative drop) and 17.4% at $\mathcal{D}_6$ (73.1% relative drop). The same direction holds across all nine DG algorithms listed. This directly supports the claim that standard single-degree evaluation can be deeply misleading about a model's robustness profile.

- **Non-monotone robustness transfer on RotatedMNIST (Section 4.3).** The finding that training on strongly rotated data (0° & 80°) *harms* performance at mild rotation compared to training on clean data only is the most surprising result in the paper. This cannot be dismissed as a training-distribution mismatch artifact, and it qualitatively differs from the NoisyMNIST result—demonstrating that the direction of failure is task-dependent and not predictable a priori.

- **Scale of evaluation across algorithms and architectures.** The experiments span a 4-layer CNN, ResNet-50, EfficientNet-b0, and ViT-B/32, plus 20+ DG algorithms. The pattern of brittleness is consistent across all choices (Figure 2 right, Table 1), which meaningfully supports the generality of the finding within the tested settings.

- **GradCAM mechanism for brittleness (Figure 5).** The visualization contrasting ERM (local feature reliance) against CAD (global structure reliance) provides a concrete mechanistic account for why performance collapses at a noise threshold: local features are selectively corrupted once noise exceeds a critical level. This connects the empirical observation to a testable feature-attribution hypothesis.

- **CLIP linear-probing brittleness documented with numbers.** Figure 4 shows CLIP (ResNet-50) accuracy dropping by more than 40% from $\mathcal{D}_0$ to $\mathcal{D}_1$ on NoisyMNIST, while a randomly initialized model trained on the same clean data stays above 95%. The contrast against RotatedMNIST (where CLIP is only mildly worse) supports the hypothesis that the effect is tied to shift novelty relative to pre-training.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing algorithms description (Section 4.1, lines 131–133).** The paper contains a `\paragraph{Algorithms.}` header with no body text before the next subsection. The models used in Sections 4.2 and 4.3 are identified only implicitly: architecture details for the CNN appear briefly in a body sentence (line 159), and Table 1 names the DG algorithms, but training protocols, hyperparameter ranges, and the model-selection procedure are entirely absent from the paper body. This makes the central experimental results non-reproducible and is a basic methodological requirement that must be addressed.

- **Suppressed fine-tuning evidence undermines the CLIP sensitivity claim (Section 5, lines 310–313).** The LaTeX source contains a `\comment{}` block—hidden from the rendered PDF—reading: *"Preliminary experiments suggest that fine-tuning significantly outperforms training from scratch and linear probing on NoisyMNIST. This suggests that when the pre-training data does not cover or is not close to covering the OOD data, linear probing can actually lead to much worse downstream OOD performance than fine-tuning."* This is a materially important finding that directly qualifies the paper's headline claim. If full fine-tuning substantially closes the observed gap, then the "sensitivity to novel downstream distribution shifts" is a property of the *linear probing protocol*, not of CLIP's representations. Section 5's title ("Pre-trained representations are sensitive to novel downstream distribution shifts") and the abstract's framing go broader than what the linear-probing experiments actually support. The paper should either present fine-tuning results and revise claims accordingly, or tightly scope all claims to the linear-probing regime with an explicit justification for why that regime is the operationally relevant comparison.

### Minor

- **Inadequate explanation of RotatedMNIST's non-monotone behavior.** This is the paper's most genuinely interesting finding, yet Section 4.3 attributes it only to "the specific task in consideration" (line 229) without deeper analysis. The paper has three datasets showing qualitatively different patterns (NoisyMNIST: roughly monotone transfer; RotatedMNIST: non-monotone; LowLightCIFAR10: threshold-dependent). No principled characterization of what property of the shift or task governs which regime applies is offered. This is a missed opportunity that weakens the paper's central contribution.

- **Pre-trained models experimental setup is a single undescribed sentence (Section 5.1, line 277).** The paper states only "They are adapted to downstream tasks through linear probing, following [Radford et al., 2021]," with no specification of which CLIP variants (e.g., RN50, ViT-B/32) are compared, which ImageNet-pretrained architectures serve as the baseline, or what linear probe training procedure is used. Given that Figure 4 is central to Section 5's claims, this absence makes the results difficult to interpret or reproduce.

- **Limited scope—entirely synthetic and toy-scale datasets.** All Section 4 results are on MNIST variants; Section 5 adds a 15-category ImageNet subset. The brittleness phenomena could behave quite differently on natural distribution shifts (e.g., domain shifts arising from different camera equipment, geographic bias, or semantic co-occurrence shifts) that do not decompose into controllable scalar-degree perturbations. The generalizability of the findings to real-world OOD benchmarks is asserted but not demonstrated.

### Trivial

- The claim that training on $\mathcal{D}_0$ and $\mathcal{D}_1$ only and then selecting models at $\mathcal{D}_4$ makes the brittleness finding somewhat expected—these models were never exposed to shift degrees beyond 1. The finding is still practically relevant (it shows model selection at a specific evaluation degree is unreliable as a proxy for nearby degrees), but the paper would benefit from acknowledging this design explicitly, rather than presenting the magnitude of drop as uniformly surprising.

---

## Nice-to-Haves

- A rank-correlation analysis across shift degrees (e.g., does a model ranked first at $\mathcal{D}_4$ tend to rank first at $\mathcal{D}_5$?) would more directly answer the benchmark-design question, and is a more informative quantity than the performance of the single best model at each degree.

- A principled (even informal) characterization of *when* monotone vs. non-monotone robustness transfer applies would substantially elevate the paper's contribution. The NoisyMNIST vs. RotatedMNIST contrast is suggestive but unexplained.

- Engaging more directly with ImageNet-C's five-severity-level structure (cited in line 63) as a prior instance of multi-degree evaluation: either showing why the paper's setting is importantly different, or using ImageNet-C as a concrete validation vehicle for the recommended evaluation practice.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **[REMOVED – Factual error] Harsh critic's claim about VREx/ERM table inconsistency.** The critic states "VREx stands out—97.4% at $\mathcal{D}_4$ for ResNet-50 but then 64.6% at $\mathcal{D}_4$." This is a misread: the 97.4% entry belongs to ERM (line 175), not VREx. VREx on ResNet-50 shows 64.6% at $\mathcal{D}_4$ (line 176), which is perfectly consistent with the 50.3% and 73.1% drops cited in line 208.

- **[REMOVED – Appendix reference] Missing proofs / appendix material.** Multiple complaints about missing details may be resolved in stripped appendices.

- **[REMOVED – Scope creep] Demand for confidence intervals across large-scale sweeps.** The paper runs 20 models per algorithm and reports averages with standard deviations; this is community-standard for DomainBed-style evaluations.

- **[REMOVED – Strawman] "Brittleness is guaranteed by the experimental design."** While training on D0/D1 does limit how well models can generalize to D5/D6, the model-selection-at-D4 finding is the practical point: a practitioner who evaluates on D4 and selects the best model has no guarantee about D5. The design is appropriate for the question being asked.

- **[REMOVED – Strength Finder: generic/ungrounded] "Datasets are released for future work."** The paper does not explicitly announce dataset release as a contribution; this is unsupported by the text.

- **[REMOVED – Strength Finder: generic importance claim] "The paper addresses an important problem."** Generic; lacks specific content.

---

## Novel Insights

The sharpest genuinely novel observation in this paper is the task-dependence of robustness transfer direction: the same training protocol (exposing the model to strongly shifted data) monotonically improves robustness across degrees on NoisyMNIST but *actively harms* mild-shift performance on RotatedMNIST. This asymmetry suggests that the geometry of the shift in feature space—not merely its magnitude—governs whether a model interpolates or extrapolates when exposed to strong perturbations. The LowLightCIFAR10 intermediate case further suggests a threshold effect tied to how much of the task-relevant feature space the strong perturbation destroys. While the paper does not theorize about this, the three-dataset contrast is the most scientifically interesting component of the work and deserves a substantially deeper investigation.

---

## Evaluation on Primary Axes

- **Originality:** The core framing—multi-degree evaluation as a richer diagnostic—is a novel and practically useful reframing of existing benchmark design. The non-monotone RotatedMNIST finding is original. The CLIP linear-probing brittleness finding is novel in the degree-wise framing, though qualified by the suppressed fine-tuning evidence.

- **Importance of research question:** High. If model selection at one shift degree poorly predicts performance at nearby degrees, many benchmark leaderboards are conveying substantially less information than implied.

- **Claims supported by evidence:** Partially. The central brittleness claim (Section 4.2) is supported by Table 1 and Figure 2, but is also partially expected from the experimental setup. The CLIP sensitivity claim (Section 5) is supported only under linear probing, and preliminary evidence for fine-tuning substantially changes the picture is suppressed. The RotatedMNIST result is well-supported but unexplained.

- **Soundness of experiments:** Compromised by the missing algorithms section. 20+ DG algorithms are run but the setup is not fully described, making replication impossible from the paper body.

- **Clarity of writing:** The paper is readable and well-motivated, but the missing section and suppressed comment block are serious presentation/integrity lapses.

- **Value to research community:** The motivation is valuable, and the datasets could be useful. However, the paper falls short of providing either a rigorous characterization of *when* multi-degree evaluation changes conclusions or a principled guidance on how to construct such evaluations.

---

## Suggestions

1. Fill in the missing `\paragraph{Algorithms.}` section with complete training details, hyperparameter ranges, and model selection criteria.
2. Either include fine-tuning experiments in Section 5 and revise the headline claims accordingly, or explicitly scope all CLIP claims to the linear-probing regime with a rigorous justification for that scope.
3. Devote significantly more analysis to explaining the NoisyMNIST vs. RotatedMNIST contrast—this is the most interesting finding in the paper and currently receives less than half a paragraph.
4. Move the brittleness framing to rest primarily on the RotatedMNIST non-monotone result (Section 4.3), which is the finding least explainable by obvious prior causes, rather than the Section 4.2 result.
5. Add one experiment on a real-world OOD benchmark (e.g., WILDS or DomainBed) with a known degree-varying structure to demonstrate that findings generalize beyond controlled synthetic perturbations.

---

## Score Calibration

**Round 1 (Bracketing):**
- Low anchors (≤3): KK29oh8jZs (3.0), l5ouuojPGe (3.0) — clearly weaker papers; our paper is more organized and more novel.
- Mid anchors (4–7): VTYg5ykEGS (6.5, accepted ImageNet-OOD paper with extensive curation), w0jk3L3IjV (5.67), oKglS1cFdb (5.67), hlijRgXTDK (4.75). Initial bracket: **4–6**.
- High anchors (≥8): All CLIP interpretation/representation papers — substantially more technically sophisticated; our paper is clearly below.

**Round 2 (Narrowing):**
- qHAblIFenP (4.75, Reject): ImageNet-RIB benchmark. Has limited novelty, limited experimental support for claims, no causal explanation of findings. Similar structural weakness to our paper (incomplete methodology, claims broader than evidence). The missing algorithms section in our paper is comparably serious.
- tnBaiidobu (5.75, Accept): CLIP train-test similarity paper. Stronger experimental rigor (retrains CLIP on pruned LAION), clearer hypothesis, more defensible claims. Our paper is weaker than this anchor because of the missing methodology, suppressed fine-tuning, and toy-level scope.
- wCOJpXm0Me (6.25, Accept): Large-scale pretraining DG paper with the Alignment Hypothesis and DomainBed validation. Clearly stronger experimental design, better theoretical grounding. Our paper is clearly below this anchor.

**Final determination:** The paper is closer to qHAblIFenP (4.75) than tnBaiidobu (5.75). The missing algorithms section is a more serious gap than anything in the 5.75 anchor, and the suppressed fine-tuning evidence directly undermines a core claim. The RotatedMNIST non-monotone finding is genuinely interesting but underexplored. Score: **4.5**.

| Anchor | Score | Round | Comparison |
|---|---|---|---|
| KK29oh8jZs | 3.0 | R1 | Weaker; our paper is more organized and more novel |
| l5ouuojPGe | 3.0 | R1 | Weaker; different domain |
| hlijRgXTDK | 4.75 | R1 | Comparable—both have limited rigor but valid observations |
| oKglS1cFdb | 5.67 | R1 | Stronger—has theoretical component |
| w0jk3L3IjV | 5.67 | R1 | Stronger—has a method component |
| VTYg5ykEGS | 6.50 | R1 | Stronger—curated real dataset, extensive experiments |
| WyEdX2R4er | 8.0 | R1 | Much stronger—large-scale VLM evaluation |
| qHAblIFenP | 4.75 | R2 | Most similar—benchmark/empirical study with methodology gaps |
| tnBaiidobu | 5.75 | R2 | Stronger—more rigorous, broader experimental scope |
| wCOJpXm0Me | 6.25 | R2 | Stronger—principled hypothesis, DomainBed validation |

**Round 1 bracket: 4–6. Round 2 narrowing places paper at ~4.5, closer to the lower end of the bracket.**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>