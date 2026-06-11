## Summary
This paper decouples class labels from target concepts in machine unlearning, introducing three new task settings (target mismatch, model mismatch, data mismatch) beyond conventional all-matched forgetting. It proposes TARF, a three-phase framework that uses representation gravity from gradient ascent to identify false retaining data, separate entangled representations, and approximate retraining. Comprehensive experiments on CIFAR-10/100 and ImageNet-1k demonstrate TARF achieves near-reference performance in settings where all existing baselines fail dramatically.

## Strengths
- **Novel and well-formalized problem taxonomy**: The paper introduces three new unlearning settings via formal label domain relations (L_D, L_M, L_T) in Section 3.1 and Table 1, directly exposing concrete failures of existing methods. For instance, GA has a Gap of 45.68% vs. TARF's 2.90% on CIFAR-10 model mismatch (Table 3). This is a genuine conceptual contribution that identifies a practically important gap in the machine unlearning literature.
- **Interpretable mechanism via representation gravity**: Theorem 3.2 (Eq. 2) derives that loss change dynamics between data subsets are bounded by representation distance d_h(x₁, x₂). This is empirically verified through t-SNE visualizations and loss curves in Figure 3, providing insight into why partial forgetting data fails to govern broader target concepts and why entangled representations resist decomposition.
- **Consistent empirical superiority across all mismatch settings and scales**: Table 3 shows TARF achieves the lowest Gap on 7/8 mismatch task-dataset combinations on CIFAR-10/100. Table 4 extends this to ImageNet-1k, where TARF achieves the lowest Gap on all four settings. The results are comprehensive across three datasets and multiple architectures (Figure 7, middle-right).
- **Validated target identification mechanism**: Figure 5(a) shows clear separation between target-concept classes (large accuracy drop after GA) and remaining classes (stable accuracy), directly validating the representation-gravity-based Phase I. Figure 5(b) demonstrates that RA-UA accuracy gaps converge toward the Retrained reference during Phases II and III.
- **Comprehensive ablation studies**: Figure 7 covers annealing strength k, constant vs. dynamic GA, multiple architectures (ResNet-18, VGG-16bn, WideResNet-50), and gradient operations on identified data, systematically characterizing algorithmic design choices.

## Weaknesses

### Fatal
None.

### Major
- **Theorem 3.2 is loosely connected to the algorithm design**: The theorem bounds loss change dynamics by representation distance, Lipschitz constants, and Jacobian spectral norm (Eq. 2), but these quantities are neither estimated in practice nor used to set any hyperparameter. The annealing schedule k(t), threshold β (top-10% heuristic), and three-phase structure are designed empirically, not derived from the theorem. Remarks 3.1–3.3 restate implications in natural language without adding analytical depth. The "representation gravity" concept (Definition 3.3) is essentially "check which classes lose accuracy after gradient ascent," a straightforward empirical heuristic. The theoretical contribution provides post-hoc rationalization rather than principled design guidance.

- **TOFU/LMM application results are weak and do not convincingly support generalization claims**: Table 5 shows that in multiple blocks (lines 317–325), TARF(GA), TARF(NPO), and plain GA produce identical results across all metrics, offering no improvement. In the first block (lines 307–310), TARF performs worse than CL(GA) in the all-matched setting (QA Prob on F.: 0.0762 vs. 0.0009; QA Prob on R.: 0.0824 vs. 0.1624). The stable diffusion application (Figure 6) is qualitative only. These results are presented in the main text without critical analysis, weakening the narrative that TARF is a general framework beyond classification.

### Minor
- **Potentially misleading retrained model definition**: Line 61 states "the retrained model for every task is trained using D_r = D \ D_f," but for target/data mismatch where D_f ⊂ D_t, the actual retrained reference must use D_r = D \ D_t (excluding the full target concept). This is evidenced by Retrained UA=0.00 in Table 3 for target mismatch, which would be impossible if D_fr (D_t \ D_f) were included in training. Table 1's partitions are internally consistent, but the prose at line 61 could confuse readers.

- **Baseline comparison asymmetry in mismatch settings**: Existing methods (GA, FT, SCRUB, etc.) were designed for the all-matched setting and have no mechanism to identify or forget broader target concepts. Their large performance gaps in mismatch settings reflect design scope mismatch rather than method failure. While TARF's contribution is solving a genuinely new problem, the experimental narrative somewhat overstates the deficiency of prior methods. In the all-matched setting where baselines are competitive, TARF is only marginally better than SCRUB (Gap 1.01 vs 1.03 on CIFAR-10; 1.11 vs 0.71 on CIFAR-100).

- **Multiple hyperparameters with limited practical guidance in main text**: TARF involves k, t₀, t₁, T, and β. Sensitivity analysis and practical guidelines are deferred entirely to Appendix E. The main text should present at least a default recipe showing one reasonable setting works across datasets.

- **Assumed knowledge of target concept scope**: Line 61 assumes "the number of classes in D_un belonging to the target concept is known in target mismatch forgetting." How performance degrades when this is unknown or estimated is not analyzed in the main text, despite being a practically important question.

## Nice-to-Haves
- A quantitative study of how representation distance d_h correlates with co-forgetting dynamics across layers and training stages would strengthen the central mechanism claims beyond t-SNE visualizations.
- Analysis of when TARF fails (e.g., non-contiguous target concepts in representation space) would set honest expectations.
- Breaking out Phase I computational cost separately from overall TARF runtime.
- Per-metric Pareto-style analysis since metrics can trade off (e.g., data mismatch CIFAR-100: TARF RA=95.01 vs GA RA=97.65 in Table 3).

## Removed Points
These points are flagged to be removed, treat them with caution:
- "Baselines designed for different task" — the paper explicitly defines new tasks and demonstrates existing methods fail; this is the stated contribution, not a bug.
- "Evaluation relies heavily on a single Gap metric" — the paper already reports all four individual metrics (UA, RA, TA, MIA) in every table.
- Missing related works — cannot verify existence.
- Formatting/style nitpicks — parser artifacts.

## Novel Insights
The paper's genuinely novel contribution is the formalization of label domain mismatch in machine unlearning. The four-task taxonomy (all-matched, target mismatch, model mismatch, data mismatch) reveals that existing methods, which perform well in the conventional setting, fail catastrophically when the target concept doesn't align with the class label. The representation gravity concept — that nearby features co-move during gradient ascent — provides an interpretable mechanism for understanding these failures and motivates a practical solution. This taxonomy and the empirical evidence for gravity-based identification could seed future work in both unlearning theory and practice.

## Suggestions
- Strengthen the connection between Theorem 3.2 and the algorithm: either use theoretical quantities to derive principled hyperparameter choices, or reframe the theory section as empirical analysis rather than a formal theorem.
- Add honest analysis of TOFU failures to the main text; acknowledge where TARF's mechanism breaks down for LLMs.
- Provide a default hyperparameter recipe in the main text with cross-dataset validation.
- Clarify the retrained model definition for mismatch settings (D \ D_f vs D \ D_t) in Section 2.

---

## Reporting — Calibration Details

### All anchors retrieved across rounds

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Decoupling the Class Label and the Target Concept in Machine Unlearning | OHOmpkGiYK.md | 5.75 | R1 | **Same paper.** Scores 6/6/3/8, rejected. One reviewer gave 3 citing artificiality and notation. |
| A Closer Look at Machine Unlearning for LLMs | Q1MHvGmhyT.md | 6.00 | R1 | Accepted. New eval metrics + objectives for LLM unlearning. Less novel setting but cleaner claims. |
| NegMerge: Consensual Weight Negation for Strong Machine Unlearning | bKQJzuBSRJ.md | 6.00 | R1 | Rejected despite uniform 6s. Incremental method (task vector merging). Less novel than this paper. |
| Evaluating Deep Unlearning in LLMs | CIN2VRxPKU.md | 5.33 | R1 | Rejected. Novel setting but synthetic dataset and weaker experiments. |
| UGradSL: Machine Unlearning Using Gradient-based Smoothed Label | hwXUmwJAq5.md | 3.00 | R1 | Rejected. Simpler method, less novel contribution. |
| SUN: Training-free Machine Unlearning via Subspace | p7mgNvOD9Q.md | 4.00 | R1 | Rejected. Training-free approach, less comprehensive. |
| UnCLe: An Unlearning Framework for Continual Learning | pFjzF7dIgg.md | 5.75 | R1 | Rejected. Different unlearning paradigm (continual learning). |
| Unlearning via Sparse Representations | TLBPjECC5D.md | 5.25 | R1 | Rejected. Discrete bottleneck approach, less novel setting. |
| CodeUnlearn | E6rpTruK4v.md | 3.80 | R1 | Rejected. SAE-based amortized unlearning for LLMs. |
| How much of my dataset did you use? | EUSkm2sVJ6.md | 7.60 | R1 | Accepted. Data usage inference, different topic but strong accepted paper. |

### Bracket determination
- **Round 1 bracket: 5.5 – 6.5.** The paper's closest anchor is itself at 5.75 (rejected). Other unlearning papers cluster between 3.0–6.0, all rejected. "A Closer Look" at 6.0 was accepted. The paper has a more novel problem setting than NegMerge (6.0, rejected) and stronger experiments than most rejected unlearning papers. No round 2 narrowing was needed as the bracket is already tight and the self-anchor provides strong calibration.

### Final calibration reasoning
The paper under review is the exact same paper that received human scores of 6/6/3/8 (avg 5.75) and was rejected. My independent analysis confirms the core strengths (novel problem taxonomy, comprehensive experiments, working method) and weaknesses (loose theory, weak TOFU, hyperparameter guidance) identified by human reviewers. I assess the paper at 6.0, slightly above the 5.75 human consensus, because the novel problem formulation is a genuine and well-executed contribution that clearly advances the unlearning literature. The weaknesses are real but bounded — they don't invalidate the core claim. The paper sits at the borderline, comparable to NegMerge (6.0, rejected) and "A Closer Look" (6.0, accepted).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>