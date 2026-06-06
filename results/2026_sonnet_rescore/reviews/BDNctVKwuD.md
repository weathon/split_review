---

## Summary

This paper identifies a theoretical limitation of HiResCAM: the explanations admit an arbitrary common spatial shift $M$ (derived from softmax's shift invariance) while producing identical probability predictions. The authors propose **ContrastiveCAMs** — class-difference activation maps that cancel $M$ by construction — and leverage them in **Core-Focused Cross-Entropy (CFCE)**, a training objective that penalizes predictions relying on non-core image regions. Experiments on Hard-ImageNet, Oxford-IIIT Pets, and PASCAL VOC demonstrate substantial improvements in core-region alignment metrics, and downstream segmentation benefits are also shown.

---

## Strengths

1. **Formally characterizes a real HiResCAM limitation**: Theorem 3.2 rigorously proves that HiResCAMs admit an arbitrary $M$-shift while preserving softmax predictions, formalizing a concrete failure mode. Table 1 quantifies the practical magnitude ($\gamma = 0.201$–$0.367$ across datasets), showing the redundant component represents 20–37% of total CAM mass — non-negligible.

2. **ContrastiveCAMs are provably $M$-invariant (Theorem 3.5)**: The invariance proof is direct and complete given the construction in Definitions 3.3–3.4. Figure 2 illustrates genuine qualitative value: ContrastiveCAMs expose region distinctions across class pairs that HiResCAMs conflate into a single map.

3. **Proposition 4.2 provides principled motivation for CFCE**: By decomposing cross-entropy into core and non-core contributions (Eq. 12–13), the paper establishes a theoretical basis for why standard CE does not inherently discourage non-core region usage — a clean theoretical argument that motivates the loss modification.

4. **Theorem 4.6 establishes classification calibration**: The convergence of CFCE risk minimization to the Bayes-optimal Core-Constrained Risk Minimization solution provides a principled connection between the proposed training objective and the alignment goal.

5. **Large, credible improvements on Hard-ImageNet (Table 2)**: CFCE reduces gray-mask ablation accuracy from 75.94% to 41.78% and raises ContrastiveCAM IoU to 89.22%, while the standard CE baseline achieves only 18.44% GradCAM IoU. The magnitude of the improvement is unambiguous.

6. **Practical applicability with weak supervision**: Table 3 demonstrates that CFCE using SAM-generated or bounding-box masks achieves alignment competitive with ground-truth masks (e.g., SAM CFCE binary IoU: 83.54% vs GT CFCE: 82.92%), substantially widening the method's applicability.

7. **Downstream segmentation benefits transfer**: Figure 4 consistently shows that CFCE+KL-pretrained backbones outperform CE-pretrained ones in per-class segmentation IoU across 20 VOC classes in the end-to-end setting.

---

## Weaknesses

### Fatal
None.

### Major

- **ContrastiveCAM faithfulness as a standalone explanation method is asserted but not independently validated.** The paper claims ContrastiveCAMs provide "more faithful attention maps" (Abstract, Section 3) for *any* model, but the only faithfulness evidence is qualitative (Figure 2) and the Table 2 ContrastiveCAM IoU column — which is reported exclusively for CFCE-trained models ("—" for all baselines). This conflates the quality of the explanation method with the quality of the training objective. There is no experiment applying ContrastiveCAM vs. HiResCAM to a fixed, CE-trained model on any faithfulness benchmark (pointing game, insertion/deletion, ROAR-style perturbations), so the claim that ContrastiveCAMs are strictly better explanators for a given model is under-supported.

- **The accuracy–alignment trade-off is consistently present but never analyzed.** Table 2 shows CFCE drops classification accuracy from 94.25% (CE) to 90.53% (~3.7 pp decline). Table 3 confirms the pattern: CFCE multiclass accuracy is 92.96% and CFCE+KL is 90.08%, both below CE (94.41%) and CE w/ Arch (95.5%). This tradeoff is a systematic finding across datasets but the Discussion section does not address it, leaving unanswered the practical question of when CFCE is preferable to CE.

### Minor

- **The "CE w/ Arch" binary IoU anomaly (Table 3) is unexplained.** Adding interpretability-motivated architectural modifications drops binary IoU from 78.37% (CE) to 39.07% (CE w/ Arch), a ~50% relative decline. This counterintuitive result — that architectural modifications intended to aid interpretability *hurt* alignment — is not addressed in the main text. Readers cannot assess whether this reflects a known limitation or a bug.

- **The "pareto improvement" claim in Section 5.3 is imprecise.** The text states "We report a pareto improvement with increased Average Precision (AP) and Intersection-over-Union (IoU) scores when using core-focused loss formulations." This holds for CFBCE (88.39% AP, 82.07% IoU) vs. CE (87.32% AP, 44.50% IoU), but CFBCE+KL (87.19% AP, 85.39% IoU) does not strictly improve AP over CE (87.32%) and trails CE w/ Arch (88.85%) on AP. The claim should be scoped to the CFBCE variant or the specific CE baseline being compared.

- **The zero-bias constraint (Proposition 4.2) lacks an ablation.** Setting $\mathbf{b} := \mathbf{0}$ in $h$ is a non-trivial architectural modification required for the clean core/non-core decomposition. The paper mentions it in passing ("b := 0 for h only") but provides no evidence on what happens when this constraint is not enforced — is the method degraded or is the decomposition merely an approximation?

### Trivial

- The PASCAL VOC segmentation bar chart (Figure 4) reports no numeric means per class or per condition; only the description table accompanies it. Explicit numerical summaries would improve readability.

---

## Nice-to-Haves

- An out-of-distribution evaluation (e.g., background-swapped or corrupted Hard-ImageNet variants) would provide direct evidence that CFCE-trained models generalize better, not just localize differently — the strongest possible argument for the paper's thesis.
- At least one quantitative faithfulness experiment (pointing game accuracy or ROAR/ROAD-style perturbation test) comparing HiResCAM vs. ContrastiveCAM on a frozen CE-trained model would cleanly decouple explanation method quality from training objective quality.
- A brief hyperparameter sensitivity ablation for the three $\lambda$ values in Eq. (18) (CFCE+KL) would establish robustness of the improved IoU results.
- Computing ContrastiveCAM IoU for the CE baseline in Table 2 would directly test whether ContrastiveCAMs expose better alignment than GradCAM *for standard models*, a key claim currently untested.

---

## Removed Points

*These points are flagged as removed; treat with caution.*

- **"M-shift limitation is overstated as a practical threat" (Harsh Critic)**: Partially valid as a nuance but does not undermine the contribution. For a fixed trained network, the weights are deterministic, so there is one concrete CAM value at inference — but the non-uniqueness is a genuine interpretive limitation: any other network achieving the same predictions via a different $M$ would produce a different absolute CAM. Figure 1 illustrates a concrete misleading case. The criticism is a legitimate nuance but not a weakness in the paper's contribution, so it is demoted to the novel insights section rather than a weakness.

- **"Comparison with CORM and DFR is asymmetric" (Harsh Critic)**: Removed per hard rule — the asymmetry favors the baselines, not the proposed method, making it intentionally conservative. CORM and DFR do not optimize for core-region alignment, so their higher accuracy at lower IoU is expected. The authors are proving a stronger point, not cherry-picking a favorable comparison.

- **Demand for OOD generalization evaluation**: Moved to Nice-to-Haves; evaluating OOD performance is outside the stated scope of the paper, which focuses on core-region alignment via interpretability.

- **Missing related works (Strength Finder)**: Removed per hard rule — no external sources available to verify existence.

- **Hyperparameter sensitivity as a major weakness**: Downgraded to Nice-to-Have; sensitivity analysis for regularization hyperparameters is standard but not required by the paper's community norms.

---

## Novel Insights

The paper's most interesting conceptual move is not the M-invariance theorem itself (which follows nearly trivially from softmax shift invariance) but the pipeline it enables: using the closed-form decomposition of cross-entropy into core and non-core ContrastiveCAM contributions (Eq. 12–13) as a direct training signal, rather than as a post-hoc interpretability tool. This reframes post-hoc explanation methods as gradient-amenable loss components, a direction with broader implications for interpretability-guided training beyond the specific CAM family. The observation in Table 1 that non-core regions dominate contributions in Hard-ImageNet (Core/Total = 0.26) while models still achieve 95.73% accuracy also concretely quantifies how much margin exists to re-route predictive information to core regions — a direct numerical motivation for the work.

---

## Suggestions

1. Compute ContrastiveCAM IoU for CE-trained baselines in Table 2; this single experiment would resolve the key ambiguity about whether ContrastiveCAMs are better explanators for *any* model vs. only CFCE-trained ones.
2. Add a one-paragraph discussion in Section 5 or the Discussion acknowledging the accuracy–alignment trade-off and its practical implications (when is 3–4% accuracy worth the alignment gain?).
3. Explain the CE w/ Arch binary IoU drop in Table 3 — even a footnote identifying the cause would prevent reader confusion.
4. Scope or clarify the "pareto improvement" claim in Section 5.3 to correctly describe which variants and which baseline the comparison holds against.
5. Add a small ablation (one row in Table 3 or an appendix table) showing performance with and without the zero-bias constraint to establish whether the method degrades gracefully.

---

## Score and Decision

**Originality**: The combination of a formal CAM limitation, a provably-invariant contrastive variant, and a training loss derived directly from that variant is a coherent and original contribution. The M-invariance theorem itself is thin, but the full pipeline is novel.

**Importance**: Feature alignment and interpretability-guided training are active, high-impact problems; the paper makes a concrete, usable contribution to both.

**Claims Supported**: The primary claim (CFCE improves feature alignment) is well-supported by large empirical gains in Table 2. The secondary claim (ContrastiveCAMs are better explanations independently of training) is asserted more than demonstrated.

**Soundness**: Theorems are stated correctly; experiments use standard benchmarks with error bars; the architecture details are referenced in the appendix. The main gap is the missing standalone validation of ContrastiveCAM faithfulness.

**Clarity**: Well-organized with clear notation; the decomposition in Eqs. 12–13 is presented cleanly. The accuracy trade-off and CE w/ Arch anomaly are not discussed.

**Community Value**: Directly applicable to anyone using HiResCAMs or seeking to improve feature alignment in ConvNets; the weak-supervision results (SAM/BBOX masks) lower the barrier to adoption.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>