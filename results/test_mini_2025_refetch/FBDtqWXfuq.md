Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper introduces **Modality-Collaborated Federated Learning (MCFL)**, a new FL setting where each client holds data from only one modality (e.g., vision or language), and the goal is cross-modality collaboration to improve per-modality performance. The authors propose **FedCola**, built on a modality-agnostic transformer, and systematically investigate three design axes: which transformer parameters to share across modalities (attention sharing), how to aggregate models (modality compensation), and how to schedule modality participation over rounds (modality warm-up). Experiments across 8 FL scenarios on two dataset pairs show FedCola consistently outperforms both a uni-modal baseline (Uni-FedAVG) and an adapted state-of-the-art FMML method (CreamFL), often with no additional computation or communication costs.

## Strengths

- **Clearly motivated new setting (MCFL):** The paper identifies and formalizes a practical gap — existing FMML requires multi-modal clients and focuses on multi-modal tasks, whereas real-world deployments often have uni-modal clients that could still benefit from cross-modality knowledge. Figure 1 and Section 2 draw a clean contrast between the two paradigms. The problem definition (Equation 1) and three design axes (parameter-sharing, aggregation, temporal arrangement) provide a structured framework for study.

- **Systematic exploration of the three design axes (Section 5):** The paper poses three specific research questions and answers each with empirical evidence. For RQ1, Table 1 shows Attention Sharing (72.92% avg) massively outperforms All Sharing (45.99%) and None Sharing (69.76%), with controlled ablations (Vision/Language Attention Only) confirming the mechanism. For RQ2, Figure 5 and the modality compensation scheme are motivated by a generalization bound argument. For RQ3, Table 3 evaluates four warm-up strategies across two dataset pairs.

- **Consistent empirical improvements across diverse FL scenarios (Table 4):** FedCola achieves the highest average accuracy in all 8 evaluated settings, with gains over the best baseline ranging from +0.56% (CIFAR-100+AGNEWS, N=16, α=0.1) to +10.98% (OrganAMNIST+MTSamples, N=4, α=0.5). The medical-domain improvements are particularly substantial, and the resource analysis (Figure 6) shows these gains come without extra computation or communication compared to the simple Uni-FedAVG baseline.

- **Clean ablation study (Table 5) and cross-modal verification (Figure 7):** Table 5 isolates the contribution of each component — Attention Sharing recovers the collapsed vision accuracy from 3.58% to 56.17%, establishing it as the critical enabler, while Modality Compensation and Warm-up provide incremental improvements. Figure 7's correlation experiment (varying patch size affects text accuracy and vice versa) provides direct evidence of genuine cross-modal knowledge transfer.

## Weaknesses

### Major

- **No statistical uncertainty reported for any result:** All accuracies throughout the paper are reported as point estimates without variance, confidence intervals, or multiple-seed runs. Given that federated learning involves stochastic client sampling (r=0.5 or 0.25), Dirichlet-based data partitioning (α=0.1 or 0.5), and random initialization, single-run results may not be representative. This is directly observable from every table — no error bars are present. The claims that FedCola "significantly outperforms" baselines (abstract, Section 6.2) are therefore unsubstantiated in the statistical sense. While the *consistency* of improvements across 8 settings is suggestive, without variance estimates the reader cannot assess whether margins of <1% (e.g., Table 4, N_c=16, α=0.1, r=0.5, CIFAR+AGNEWS: FedCola 49.17 vs Uni-FedAVG 47.41; text: 49.29 vs 49.05) reflect systematic gains or noise. This is a structural weakness for an empirical FL paper where the core claim is about outperforming baselines.

- **Overclaimed language relative to measured margins:** The abstract and conclusion state that FedCola "significantly outperforms existing solutions" and "marks a substantial advancement." However, several configurations show small absolute improvements (e.g., many text accuracy gains are <1%). The paper's primary contribution is the systematic methodology and the MCFL framing itself, not dramatic performance breakthroughs. The language should be calibrated to match the evidence.

### Minor

- **Modality warm-up benefit is context-dependent but presented as generally beneficial:** Table 3 shows that the heat-distribution stage only helps when modalities have "higher correlation" (medical datasets) and actually slightly hurts on the low-correlation pair (CIFAR+AGNEWS: VW achieves 73.73 vs VWH 73.34). The paper briefly acknowledges this but still presents warm-up as a general component of FedCola. More explicit guidance on when to use which warm-up strategy would be valuable.

- **Missing detail on CreamFL adaptation for MCFL:** The paper adapts CreamFL (designed for modality-aligned FMML) to the MCFL setting, and notes that all methods use the same model architecture. However, the adaptation details are deferred to the appendix (stripped). Since CreamFL's original mechanism involves multi-modal feature alignment via a public dataset, and the paper's Table 4 shows CreamFL sometimes underperforms even the simple Uni-FedAVG baseline, a more self-contained explanation of the adaptation in the main text would improve confidence in the comparison fairness.

- **Modality collaboration verification (Figure 7) lacks a negative control:** The experiment shows that changing patch size for vision affects language accuracy, and vice versa. This is a clever sanity check, but it would be significantly strengthened by including a control under Uni-FedAVG (where no cross-modal parameters are shared) — the absence of a cross-modal effect in that control would provide much stronger evidence that the observed correlation is due to FedCola's parameter sharing rather than a spurious artifact. As presented, the effect sizes are modest (a few percent).

### Trivial

- None beyond standard formatting artifacts (which are parser issues, not author errors).

## Nice-to-Haves

- **Discussion of negative transfer conditions:** When might cross-modal parameter sharing harm performance? Testing a scenario with conflicting semantics (e.g., image classification of natural scenes + text classification of technical documents) would bound the method's applicability. Currently the paper only shows improvement scenarios.
- **Error bars / multiple seeds** are listed as a major weakness above, not a nice-to-have.
- **Negative control for Figure 7** is listed as minor above.

## Removed Points

The following points from the reviewers were removed:

1. **"No experiments on more than two modalities"** — Removed as scope creep. The paper explicitly acknowledges this as future work, and adding a third modality (audio) would be a substantial engineering undertaking beyond the paper's stated scope.
2. **"Hyperparameter table missing"** — Removed. The paper references Appendix F/G for detailed algorithms and implementation. The appendix is stripped by the parsing process, not absent from the original submission.
3. **"CreamFL adaptation may be suboptimal, undermining fair comparison"** — Downgraded from major concern to minor. The paper explicitly acknowledges that CreamFL was designed for a different setting and explains why it sometimes underperforms Uni-FedAVG ("with the absence of multi-modal clients for direct feature alignment, CreamFL cannot always outperform Uni-FedAVG"). This is a reasonable explanation, not a hidden weakness. The adaptation concern remains minor because details are in the stripped appendix.
4. **Generic area-of-concern sweeps** from the harsh critic about evaluation validity and comparison fairness that lacked specific textual anchors have been removed.

## Novel Insights

The reviews converge on a key observation that is not explicitly developed in the paper: the success of attention sharing (over FFN sharing) for cross-modal collaboration provides an interesting data point for understanding what makes transformer architectures effective for multi-modal learning. The finding that self-attention layers — which compute pairwise interactions between tokens — are the primary vehicle for cross-modal knowledge transfer, while FFN layers (which operate per-token) are better kept modality-specific, aligns with the intuition that cross-modal learning requires modeling inter-token relationships across modalities. This insight could inform architecture design for federated settings beyond the specific MCFL framework.

## Suggestions

1. **Add error bars (std over 3–5 seeds)** to all main result tables (Tables 1, 3, 4, 5). Without these, the quantitative claims of outperformance are unverifiable. This is the single highest-priority fix.
2. **Calibrate the language** in the abstract and conclusion — replace "significantly outperforms" with "consistently outperforms" or "achieves higher average accuracy across diverse settings." The contribution is genuinely the systematic methodology and the MCFL framing, not dramatic margins.
3. **Add a negative control to Figure 7:** Show that changing patch size (or token length) under Uni-FedAVG does not produce a cross-modal effect. This would substantially strengthen the modality collaboration verification.
4. **Provide more explicit guidance** on when the modality warm-up heat-distribution stage is beneficial vs. detrimental, given the mixed results in Table 3.

## Score and Decision

**Round 1 — Bracketing:** Three queries anchored the weak (<3.5), middle (3.5–7.5), and strong (>7.5) bands. The weak anchors (scores 2.33–3.00) were clearly inferior papers with basic methodological flaws. The strong anchors (scores 7.60–8.00) were top-tier papers with extensive experiments and strong theoretical grounding. This paper sits firmly in the middle band.

**Round 2 — Narrowing:** Two queries targeting (4.5, 6.5) and (5.5, 7.5) yielded anchors including:
- **Equ277PBN0** (5.75, Accept Poster) — DP-FPL for multimodal FL. Similar structure, shared weakness of no statistical significance testing. This paper has clearer novelty (new MCFL setting vs. incremental DP addition).
- **TKDwsJmrDJ** (6.00, Reject) — ATC for heterogeneous NLP tasks. Similar profile: novel framework, consistent but sometimes small improvements, no significance tests, overclaimed language. Rejected despite high avg score.
- **zPDpdk3V8L** (6.33, Accept Poster) — HCFL for clustered FL. Stronger theoretical grounding and more comprehensive experiments.
- **LGzTtvisL3** (4.75, Reject) — FLea feature augmentation. Limited to one dataset and model.
- **U0P622bfUN** (5.25, Reject) — Federated Generative Learning. Decent scores but rejected.

The paper under review is stronger than LGzTtvisL3 and U0P622bfUN, comparable to Equ277PBN0 but with clearer novelty, and somewhat weaker than zPDpdk3V8L in terms of experimental rigor. Compared to TKDwsJmrDJ (rejected despite 6.00 avg), this paper has a more clearly defined new setting and more comprehensive experiments, but shares the same core weakness of absent error bars. After cross-referencing all anchors, the paper is best placed at the lower end of the 5.5–6.0 range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>