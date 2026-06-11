Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper proposes OML, a brain-inspired hierarchical neural network for online multimodal learning with human-in-the-loop interaction. The architecture includes feature neurons, unimodal association neurons, and multimodal association neurons with ascending, descending, and lateral pathways. Key claimed contributions are: (1) online learning without catastrophic forgetting, (2) autonomous reference extraction that identifies which parts of a multimodal signal a word refers to (e.g., distinguishing "red" as a color attribute from "apple" as an object name), (3) conflict detection and human-in-the-loop question-asking, and (4) modal extension to new modalities. Experiments are conducted on small fruit/home-object datasets with Chinese voice data.

## Strengths

- **Autonomous reference extraction for word-concept alignment (Section 3.4):** The coefficient-of-variation-based method for identifying which feature dimensions a word refers to is a genuinely novel and interesting approach to the symbol grounding problem in an online setting. Table 2 provides evidence that OML handles color-referring words better than baselines (e.g., 87.8% V→A on E-Fruits Open vs. 84.1% for the next-best online method AEN), while offline methods all show accuracy drops marked with ↓.

- **Conflict detection and question-asking framework (Section 3.5):** The four-case framework for handling different recognition scenarios (image recognized/not, word recognized/not) with specific question templates and update rules is a principled design for interactive learning. This capability — detecting conflicts and posing questions — is identified in the paper as missing from prior online methods (Xing et al. 2019; 2021; Tan et al. 2019; Shubham et al. 2025), and the paper provides a concrete mechanism for it.

- **Modal extension with cross-modal distinction (Table 3):** OML outperforms AEN across all six recall directions on VAT and VAT-HomeF datasets in both close and open environments. The frequency-based signal routing (λ parameter) for distinguishing which channel a word refers to is architecturally distinctive.

- **Catastrophic forgetting resistance (Table 1, open environment):** OML achieves the highest accuracy among all methods in open environments (e.g., 89.8% V→A on Fruits Open), while offline methods (DAE, DBM, DJSRH, NRCH, FUME) degrade substantially. OML also outperforms the other online methods ART and AEN, demonstrating genuine resistance to catastrophic forgetting in this setting.

- **Differentiated activation modes by modality (Section 3.2):** The distinction between Order Independent Activation Mode (OIAM) for visual concepts and Order Dependent Activation Mode (ODAM) for auditory (syllable-sequence) concepts is a principled architectural choice grounded in the structure of each modality.

## Weaknesses

### Fatal
None.

### Major

1. **Mathematical issue in the feature neuron activation function (Eq. 1, Section 3.1).** The ascending activation function is defined as:

   $$y^{\alpha_k} = \sum_{i=1}^n \sum_{t=1}^T w_{j,i} \cos(\lambda_i^{\alpha_k} 2\pi \tfrac{t-1}{T})$$

   where each $\lambda_i^{\alpha_k}$ is assigned a "unique natural number" and $T=150$. For any integer $\lambda_i$ that is *not* a multiple of $T$, the inner sum $\sum_{t=1}^T \cos(2\pi \lambda_i (t-1)/T) = 0$ by the standard trigonometric identity that the sum of cosines over $T$ equally-spaced points covering full cycles is zero. Since $\lambda_i$ are unique natural numbers, at most one $\lambda_i$ per feature type can equal a multiple of $T=150$ (or any integer multiple thereof). For all other dimensions, the inner sum is identically zero. This means $y^{\alpha_k}$ would be zero regardless of the input features or learned weights, provided the distance threshold condition is met; if the condition is not met the output is also zero. The paper states "its value does not affect the algorithm" about $T$, but mathematically $T$ directly determines whether the sum is zero or non-zero. The feature neuron is the foundational building block of the entire network — every subsequent computation (UANs, MANs, reference extraction, conflict detection) depends on its output. If the implementation differs from the mathematical description, the paper must clarify this explicitly. As presented, the mathematics in Eq. (1) is inconsistent with the claimed results. **The authors must resolve this discrepancy for the method to be assessable.**

2. **No ablation studies, sensitivity analysis, or variance reporting.** The method involves at least three hand-tuned thresholds ($\theta$, $\vartheta$, $r$), the choice of $T$ in Eq. (1), the lateral connection criterion $d(w_i, w_j) \leq 2\theta$, the Fourier transform in Eq. (6), and the reference extraction threshold. None of these are ablated or analyzed for sensitivity. Every result is reported as a single point with no standard deviation, confidence interval, or indication of how many runs were performed. For a paper advancing a new architecture with many design decisions and tunable parameters, this is a serious evidential gap that prevents assessment of robustness.

3. **Thin online baseline comparison and limited benchmarks.** Only two online methods (ART and AEN) are compared against. While these are the most directly relevant online multimodal methods, this narrow comparison limits the strength of the empirical evidence. No standard continual learning baselines (e.g., experience replay, EWC, or prompt-based methods adapted to the multimodal setting) are included. Additionally, all experiments use only small fruit/home-object datasets; no evaluation is conducted on standard multimodal benchmarks (e.g., MSCOCO, Flickr30K) or standard continual learning benchmarks (e.g., Split CIFAR, Seq-MNIST), which limits the generalizability of the claims.

### Minor

1. **Reference extraction threshold $r$ not analyzed (Section 3.4).** The method for distinguishing name words from attribute words relies on a threshold $r$ to decide which feature types a word refers to. The paper does not analyze how this threshold interacts with the feature distribution of different object categories — e.g., if shape variance happens to be low for a particular object category, the algorithm might incorrectly decide a name word refers only to color. No sensitivity analysis for $r$ is provided.

2. **The offline method comparison in Tables 1 & 2 is framed somewhat adversarially.** The paper compares offline methods (DAE, DBM, DJSRH, NRCH, FUME) in settings where they cannot be updated. This is legitimate for demonstrating the limitations of offline approaches and motivating online learning. However, the core evidence for OML's effectiveness should rest primarily on comparisons with the online methods ART and AEN. The degradation of offline methods when encountering new class splits or new words is expected and does not by itself strengthen the case for OML over other online approaches.

3. **The human-in-the-loop component has limited verification.** The paper reports that with 10% mismatched data pairs, "OML is able to detect all conflicts and raise appropriate questions," but this claim is stated qualitatively with no dedicated experimental table, ablation, or controlled study. The unanswered questions defaulting to positive (Section 4, final paragraph) further weakens the claim of genuine interactive learning.

### Trivial
None.

## Nice-to-Haves

- A dedicated experiment for reference extraction (e.g., precision/recall for feature-type attribution) would strengthen the core claim independently from the retrieval accuracy numbers.
- Ablation of the human-in-the-loop component (comparing OML with and without conflict detection/question-asking).
- The frequency-based routing mechanism (Fourier transform in Eq. 6) could be better motivated. It is currently unclear why a Fourier transform is applied to the UAN's output and how the $\lambda$ matching for descending pathways works in detail.
- Statistical significance testing across multiple random seeds/runs.

## Removed Points

*These points were raised by the reviewers but are removed from the main weaknesses for the reasons stated below:*

- **"Evaluation metric is undefined"** — Removed. The paper states "use one channel input to get outputs from other channels on the testing dataset" and describes the counting rule explicitly (returning all relevant features counted as correct for baselines, which is generous to baselines, not unfair). The metric is sufficiently clear.
- **"Unfair offline baseline comparison (Table 2 is staged)"** — Removed. The paper marks accuracy drops with ↓ and frames this as showing limitations of offline methods in a setting they weren't designed for. The comparison is informative about the need for online learning, not unfair. The surviving concern about thin online baselines is kept in Major.
- **"Open environment does not convincingly demonstrate catastrophic forgetting"** — Demoted to the Minor weakness about limited benchmarks. The open environment protocol (class-disjoint sequential splits) is a valid test of catastrophic forgetting on the chosen datasets; the concern is about the scale and diversity of datasets, not a flaw in the experimental design.
- **"Missing related works"** — Removed. Cannot verify external knowledge about what should have been cited.
- **"Anthropomorphic framing claims unsupported"** — Removed. Brain-inspired framing is a common motivational device in neural network papers and not a substantive weakness.
- **"Under-specified Fourier transform motivation"** — Moved to Nice-to-Haves. The mechanism is described; deeper motivation would strengthen the paper but its absence is not a flaw.
- **"Reproducibility concerns about implementation details"** — Removed. The paper provides the core algorithmic description; complete implementation details are impractical for a conference submission.
- **"Pure formatting and style nitpicks"** — Removed. These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel perspective on the work that the paper itself does not already articulate.

## Suggestions

1. **Clarify or correct Eq. (1).** This is the most critical issue. If the implementation computes something different from what Eq. (1) states (e.g., if the sum over $t$ is not taken, or if the cosine encoding is used differently), the paper must provide the correct mathematical description. If Eq. (1) is what is actually computed, explain how the output is non-zero given the trigonometric identity discussed above.

2. **Add ablation studies** for the key thresholds ($\theta$, $\vartheta$, $r$) and report standard deviations across multiple runs with different random seeds.

3. **Include at least one standard continual learning baseline** (e.g., experience replay applied to a multimodal model) and evaluate on a benchmark dataset to improve generalizability.

4. **Design a dedicated reference extraction experiment** with precision/recall metrics for feature-type attribution, decoupled from the overall retrieval accuracy.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Initial search placed the paper against three score bands. Low band queries (<3.5) returned papers with avg scores 1.5–3.0 (e.g., CAN at 1.50, HDC at 3.00) — the OML paper is clearly stronger than these. Middle band queries (3.5–7.5) returned papers with avg scores 3.80–5.00. High band queries (>7.5) returned papers with avg scores 8.00 — the OML paper is clearly weaker than these. **Initial bracket: 3.5–6.0.**

**Round 2 (Narrowing):** Searched inside the bracket (3.5–6.0 and 4.0–6.5). Anchors consulted in full:
- Pa6SiS66p0 (4.33, Reject) — Multimodal continual learning benchmark/study. OML has more architectural novelty but also has a mathematical flaw this paper lacks.
- UhKkWHkvfg (5.00, Reject) — MM-CTTA with analytic learning. Similar evaluation scope; OML has a more novel architecture but a more serious core weakness.
- CagdoUkvvl (4.50, Reject) — Multi-modal continual learning with dual-learner. Similar ablation issues; OML's contribution is more novel but has the Eq. (1) problem.
- JAnyCnK5In (4.75, Reject) — SNN online training. Comparable novelty concerns; OML has a more novel contribution but a more serious mathematical issue.
- DCpukR83sw (5.75, Accept) — Interactive trajectory prediction. Stronger evaluation, no mathematical flaw; OML is weaker.
- BSBZCa6N3E (5.00, Reject) — Retrospective learning from interactions. More thorough evaluation but different domain.
- Vy5aRVSbNo (4.25, Reject) — Object permanence from video. Comparable score.

**Calibrated position:** OML is in the range of the 4.33–5.00 anchors. It has more architectural novelty than most, but the mathematical issue in Eq. (1) is a more serious weakness than any single weakness in those comparison papers. It is clearly weaker than the 5.75 accepted paper (DCpukR83sw) which has a sound core mechanism and more rigorous evaluation. Score of 4.5 reflects a paper with genuinely novel ideas that is substantially undermined by a verifiable mathematical concern and insufficient evaluation rigor.

**All anchor papers retrieved:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| SI6zocV2SS.md | 1.50 | R1 | Much weaker |
| NYPJz0CL5X.md | 3.00 | R1 | Weaker |
| fnO5h1CFyh.md | 3.00 | R1 | Weaker |
| WM5G2NWSYC.md | 2.00 | R1 | Much weaker |
| Pa6SiS66p0.md | 4.33 | R1/R2 | Comparable, less novelty but no math flaw |
| G9Ea7mlqGO.md | 3.80 | R1 | Weaker |
| CagdoUkvvl.md | 4.50 | R1/R2 | Comparable |
| UhKkWHkvfg.md | 5.00 | R1/R2 | Slightly stronger evaluation |
| TPZRq4FALB.md | 8.00 | R1 | Much stronger |
| kbjJ9ZOakb.md | 8.00 | R1 | Much stronger |
| RWJX5F5I9g.md | 8.00 | R1 | Much stronger |
| agPpmEgf8C.md | 8.00 | R1 | Much stronger |
| DCpukR83sw.md | 5.75 | R2 | Stronger (accepted, no math flaw) |
| JAnyCnK5In.md | 4.75 | R2 | Comparable |
| BSBZCa6N3E.md | 5.00 | R2 | Different domain, comparable rigor |
| Vy5aRVSbNo.md | 4.25 | R2 | Comparable |

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>