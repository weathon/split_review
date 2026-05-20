Now I have a complete picture. Let me compile the final review.

---

## Summary

Critique-RL proposes a two-stage RL method for training critic language models without requiring a stronger supervisor. Stage I optimizes the critic's discriminability (ability to judge response correctness) via a direct rule-based reward, and Stage II optimizes helpfulness (providing useful refinement feedback) while regularizing toward the Stage I model to preserve discriminability. The paper identifies through training-dynamics analysis that standard indirect-reward RL (relying solely on actor refinement outcomes) leads to mode collapse into overly conservative or aggressive critics, and shows that the proposed two-stage approach resolves this. Experiments on math reasoning tasks (MATH, GSM8K, AQuA) with Qwen2.5-3B and Qwen2.5-7B demonstrate consistent improvements over SFT, STaR, Retroformer, and CTRL baselines, along with iterative improvement and OOD generalization to SVAMP and TheoremQA.

## Strengths

- **Compelling empirical diagnosis of RL failure modes for critics.** Figure 3 and Section 4.1 provide a clear, quantitative analysis of why indirect reward signals alone fail: discriminability collapses while helpfulness optimizes only one-sidedly (overly conservative with \(r_{\text{refine}}\)/\(r_\Delta\), overly aggressive with \(r_{\text{correction}}\)). This analysis goes beyond prior work (Retroformer, CTRL) that did not study or address this specific conflict between discriminability and helpfulness.

- **Well-motivated two-stage design with supporting ablations.** The decoupling of discriminability (Stage I) and helpfulness (Stage II) directly addresses the conflict identified in the motivation. The ablation in Table 3 confirms that removing either stage degrades performance, and that removing the discriminability-preserving terms from Stage II causes a substantial drop in discrimination accuracy (e.g., Acc@Dis falls from 82.8 to 77.7 on MATH).

- **Consistent and substantial improvements across models and tasks.** Table 1 shows Critique-RL outperforms all baselines on every in-domain dataset for both Qwen2.5-3B and Qwen2.5-7B. On Qwen2.5-7B, it achieves a 9.02% average gain on in-domain tasks and 5.70% on out-of-domain tasks, with discrimination accuracy reaching 85.2% vs. 68–71% for the best baselines.

- **Demonstrated iterative capability.** Both iterative critique-refinement (Figure 4) and iterative training (Table 2) show consistent gains, with a second training iteration improving Acc@Dis from 82.8 to 86.5 on MATH, suggesting the method stacks effectively.

- **Scalable oversight without stronger supervisors.** The method bootstraps critic training using SFT data generated from the same-size instruct model and online RL, avoiding expensive annotations from larger commercial models — a practically important property for scalable oversight.

## Weaknesses

### Major

- **Ambiguous ablation of two-stage necessity.** The "w/o Stage I" ablation (Table 3) is the key experiment for establishing that the two-stage structure is necessary, but its precise implementation is unclear. The Stage II objective (Eq. 9) uses a KL penalty to \(\pi_\phi^{\text{Stage-I}}\); if Stage I is skipped, what reference model replaces it? If the SFT model is used instead, then "w/o Stage I" is essentially a single-stage combined objective (\(r_{\text{refine}} + \beta_1 r_{\text{dis}}\) with KL to SFT), which would be the right ablation — but the paper does not specify this. Without clarity on what "w/o Stage I" means, the central claim that two-stage training is necessary (rather than merely including \(r_{\text{dis}}\) somewhere) is not conclusively established. This is an evidential gap in an otherwise well-ablated paper.

### Minor

- **Narrow task scope limits generality claims.** All experiments are on mathematical reasoning tasks. Even the "out-of-domain" evaluation (SVAMP, TheoremQA) remains within math. The paper mentions summarization experiments in Appendix G (stripped from the manuscript), but the main text's claims about generalization to "unseen tasks" are overstated given that all evaluated tasks share the same fundamental structure (math word problems with verifiable answers). The reliance on a rule-based correctness verifier \(f(x,y,c)\) whose extraction mechanism and failure modes are not characterized further narrows the method's current applicability.

- **No sensitivity analysis for key hyperparameters.** The Stage II discriminability weight \(\beta_1 = 0.2\) is stated without justification or ablation. Since \(\beta_1\) controls the trade-off between discriminability preservation and helpfulness optimization, its sensitivity is important for understanding the method's robustness. Similarly, the KL coefficients \(\beta\) and \(\beta_2\) receive no exploration.

- **No variance estimates for main results.** Given test sets of 3,000–7,000 examples, the observed differences are likely significant, but reporting confidence intervals or standard deviations (especially for the smaller AQuA test set) would add rigor to the comparisons.

### Trivial

- The paper claims discriminability and helpfulness are "jointly optimized" in Stage II, but only discriminability receives a direct reward; helpfulness is optimized purely through the refinement outcome. The phrasing could be more precise.
- "Helpfulness" is implicitly defined via refinement outcome, which conflates feedback quality with the actor's ability to use it — a known confound in refinement-based training that could be acknowledged.

## Nice-to-Haves

- A direct helpfulness reward (e.g., via an LLM judge evaluating critique quality independent of refinement success) could further strengthen Stage II, though this is genuinely a direction for future work.
- A single non-math task (e.g., a science QA or short-form generation task where correctness can be operationalized) would substantially strengthen the generalization claims.
- Reporting the precision of the discriminability extraction function \(f(x,y,c)\) on a held-out set would address concerns about noise in the Stage I reward signal.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Baselines originally designed for decision-making and coding tasks"** — REMOVED. The paper fairly reimplements Retroformer and CTRL for math reasoning; domain mismatch is not a valid criticism when the reimplementation is done properly.
- **"Inference compute comparison may be unfair"** — REMOVED. The baseline uses \(3K\) parallel samples vs. \(K\) critique-refinement cycles. Since each refinement cycle requires three generations (response + critique + refinement), the comparison is reasonable and the paper is transparent about it.
- **"Helpfulness conflates feedback quality with actor ability"** — DEMOTED to Trivial. This is a conceptual observation about terminology, not a substantive flaw in the method.
- **"Could a larger or smaller \(\beta_1\) degrade performance?" (from section-by-section notes)** — MERGED into the Minor weakness about missing sensitivity analysis.
- **General concern about appendix-deferred experiments** — REMOVED per hard rules (parser strips appendix, but it exists in the original submission).
- **Formatting/style nitpicks** — REMOVED per hard rules.

## Novel Insights

The training-dynamics analysis (Figure 3) provides a genuinely novel characterization that goes beyond the paper's own methodological contribution: it shows that different indirect reward formulations (\(r_{\text{refine}}\), \(r_\Delta\), \(r_{\text{correction}}\)) produce qualitatively different failure modes (conservative vs. aggressive collapse), and that these failures share a common root cause — discriminability degrades for one class of responses (correct or incorrect) while the indirect reward optimizes only the other. This systematic decomposition of why indirect-reward RL fails for critic training, supported by per-class discrimination accuracy curves, is an insight that generalizes beyond the specific method proposed and may inform future work on critic and reward model training.

## Suggestions

- Clarify exactly what "w/o Stage I" implements: what reference model replaces \(\pi_\phi^{\text{Stage-I}}\) in the KL term? If it uses the SFT model, state this and frame it as the single-stage combined baseline. If the implementation is different, add the genuine single-stage baseline (\(r_{\text{refine}} + \beta_1 r_{\text{dis}}\) with KL to SFT, starting from SFT).
- Characterize the discriminability extraction function \(f(x,y,c)\): report its precision on a held-out set and discuss the required output format, which will clarify the method's scope and robustness.
- Tone down claims about generalization to "unseen tasks" — SVAMP and TheoremQA are still mathematical reasoning. Acknowledge this as a limitation explicitly, or broaden the OOD evaluation.
- Add a brief sensitivity analysis for \(\beta_1\) (the discriminability weight in Stage II) to help practitioners understand the trade-off.

---

## Score Calibration

Round 1 bracket: based on the three bands, the paper sits between Critic-CoT (5.75, a critic-training paper with distillation from stronger models and weaker results) and WizardMath (8.00, a strong math-reasoning training paper). Initial bracket: **5.5–7.5**.

Round 2 narrowing anchors within the bracket:
- **Critic-CoT** (5.75) — Critique-RL is clearly stronger: no distillation from stronger models, better failure-mode analysis, more comprehensive experiments, larger gains.
- **SRC** (6.00) — Self-improvement via RL contemplation, limited to 780M model, modest gains, mixed novelty. Critique-RL is clearly stronger.
- **CRITIC** (6.50) — Tool-use framework for self-correction, broad task coverage (QA, code, toxicity), strong results. Critique-RL is comparable in contribution quality: trains models rather than relying on prompts + external tools, has better failure-mode analysis, but narrower task scope (math only).
- **Progress or Regress** (6.50) — Analysis of self-improvement reversal in post-training. Comparable contribution quality.
- **Q-SFT** (7.00) — Q-learning for LLMs, broader applicability. Slightly stronger due to generality.
- **OCEAN** (6.80) — Offline CoT evaluation, knowledge-graph feedback. Slightly stronger scope.

Critique-RL is comparable to the 6.50 cluster (CRITIC, Progress or Regress) — solid contribution, good experiments, some scope and evidential limitations. It is clearly stronger than the 5.75–6.00 papers but not at the 7.00+ level where contributions have broader applicability or more thoroughly validated claims.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>