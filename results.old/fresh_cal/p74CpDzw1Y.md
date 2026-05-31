Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper proposes "wrong-over-wrong alignment": a pipeline for (1) eliciting preferences among *incorrect* LLM answers using consistency, logits, pairwise comparison, and score-based methods, and (2) aligning models via DPO using only those wrong-over-wrong preferences. Experiments with seven LLMs across eight datasets show that LLMs can distinguish "shades of wrong" with up to 70.9% accuracy (substantially above random), and that alignment with these wrong-only preferences yields models that are less wrong (9.0% improvement in proxy wrongness), more correct (up to 7.0% accuracy increase), and better calibrated (ECE reduction up to 9.4%) compared to the original model.

## Strengths

1. **Novel and well-motivated research question.** The idea of leveraging preferences among wrong answers—where correct answers are unavailable—is genuinely novel and has practical relevance for tasks like theorem proving or low-resource-language reasoning where ground-truth answers are scarce. The paper's framing distinguishes it clearly from standard right-over-wrong alignment.

2. **Comprehensive preference elicitation study (RQ1).** The paper systematically compares five elicitation methods (heuristic, consistency, logits, pairwise comparison, score-based) across three generators and three evaluators on four datasets. The finding that score-based LLM-as-a-judge with a 10th-percentile margin outperforms all other methods by at least 9.4% (Table 1) is solid and well-supported. The observation that self-evaluation degrades accuracy by ~21% (Section 4, line 166) while weak models can evaluate strong ones is a practically useful finding.

3. **Wrong-over-wrong alignment consistently improves over the original model (RQ2, Table 2).** Across all four datasets and both generator settings, every alignment method yields improvements in at least some metrics over the original LLaMA3-8B. The average gains (Δp_wrong = +0.074, ΔAcc = +0.045, −ΔECE = 0.044) are modest but consistent, and the surprising result that training only on wrong answers increases accuracy (up to +7.0% on NLGraph) is interesting and non-obvious.

4. **Mixing wrong-over-wrong with right-over-wrong preferences yields best calibration (Table 3).** The paper shows that a 50:50 mix of wrong-over-wrong and right-over-wrong data achieves better ECE than either alone (e.g., oracle r+w on KC: ECE 0.025 vs. r-only 0.079). This directly addresses the known issue that alignment can hurt calibration, and positions wrong-over-wrong alignment as a practical complement to existing methods.

5. **Generalization to unseen tasks in the same domain (Table 4).** Fine-tuning on COM² and shortest-path data improves proxy wrongness scores on HellaSwag and maximum-flow tasks (avg Δp_wrong = +0.118), suggesting the method captures transferable notions of answer quality. (Accuracy transfer is negligible at ΔAcc = +0.002, which the paper honestly reports.)

6. **Honest reporting of limitations.** The paper explicitly notes that wrongness proxies are imperfect (footnote 1, line 16), that self-evaluation is subpar (line 166), and that the weak correlation between preference accuracy and alignment improvement (Figure 2) makes the mechanism less clear than desired (line 217). This transparency strengthens the paper.

## Weaknesses

### Fatal
None.

### Major

1. **Missing negative control for alignment experiments.** The core alignment experiments (Table 2) compare wrong-over-wrong aligned models to the *original* LLaMA3-8B, but do not include a control condition where DPO is trained on the same wrong answers with *random* preference directions. Without this control, the improvements cannot be causally attributed to the *wrong-over-wrong direction* of the preferences rather than to any DPO training on paired wrong answers (e.g., regularization effects or continued training). The paper's RQ2 asks "Is alignment with wrong-over-wrong preferences helpful?"—but the comparison only shows the pipeline *as a whole* improves over no alignment, not that the *specific preference direction* drives the gains. The weak correlation between preference accuracy and alignment improvement (Figure 2, line 217) further underscores the need for this control: if even oracle-quality preferences don't strongly correlate with improvement, the preference direction may not be the operative factor. This does not invalidate the paper's findings, but it weakens the causal interpretation of the headline results. *Evidence location: Table 2; Section 4 (lines 196–202); Section 5 (lines 217–223).*

### Minor

1. **The "less wrong" metric shares the same proxy function as the evaluation of preference accuracy.** The metric p_wrong (average proxy score of wrong answers; Eq. on line 110) uses the same proxy function p(a|q) that defines the silver standard for wrong-over-wrong preferences (f̂ = sgn(p(a₁|q) − p(a₂|q)); line 93). Consequently, improvements in p_wrong partially measure how well the model aligns with the proxy itself, not an independent measure of "intrinsic wrongness." The paper partly mitigates this by also reporting accuracy (Acc) and calibration (ECE), which are independent metrics, but the "less wrong" objective lacks independence. *Location: Section 3 (lines 91–94), Section 3 (line 110), Section 4 (lines 196–200).*

2. **Alignment experiments use only one base model (LLaMA3-8B).** While the preference elicitation study spans three generators and three evaluators, the alignment fine-tuning (RQ2) is conducted only on LLaMA3-8B. Showing results on at least one additional model (e.g., a different 7B–8B-scale model) would strengthen generalizability claims. *Location: Section 3 (line 89–90).*

3. **Insufficient discussion of proxy noise on results.** The paper acknowledges that proxies (FActScore, Vera) are imperfect (footnote 1, line 16), but does not discuss how noise in these metrics might bias the reported preference accuracy (making the 70.9% an over- or underestimate relative to human judgment) or affect the alignment evaluation. A brief analysis of proxy reliability would strengthen the paper's evidence. *Location: Section 3 (lines 91–100), Section 4 (line 162).*

4. **Weak correlation between preference accuracy and alignment improvement undermines the assumed mechanism.** The paper's own analysis (Figure 2, line 217) shows no significant correlation between Acc_WoW and ΔAcc or −ΔECE, and only a weak correlation with Δp_wrong. This pattern is consistent with the missing-control concern (Major weakness #1): it suggests the preference direction may not be the primary driver of the observed improvements. The paper notes this honestly but does not sufficiently discuss why the mechanism it hypothesizes might be wrong or incomplete.

### Trivial
None.

## Nice-to-Haves
- **Random-preference control** (for the reason stated in Major #1). This is the single most impactful addition.
- **SFT baseline on the same wrong answers** without any pairwise preferences, to separate continued-training effects from preference optimization effects.
- **Variance or confidence intervals** for the alignment results (Table 2), since the absolute gains are modest (~0.045 average ΔAcc).
- **Additional qualitative examples** spanning multiple datasets (currently only NLGraph is shown in Table 5).

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **"No significance tests or variance estimates are reported for the alignment improvements."** — Removed. Single-run DPO fine-tuning evaluations without significance tests are standard practice in the LLM alignment literature. Requesting confidence intervals for every entry in Table 2 is above the norm for papers at this venue. Moved to Nice-to-Haves.
2. **"The single qualitative example (Table 5) is helpful but not sufficient."** — Removed. This is a preference, not a flaw. Moved to Nice-to-Haves.
3. **"SFT baseline on wrong answers"** — Removed as it is fully subsumed under the negative-control concern (Major #1) and does not add independent diagnostic value.
4. **From Strength Finder: "Identifies and solves the self-evaluation failure mode."** — Removed the "solves" characterization. The paper identifies the failure mode (line 166) and makes the interesting observation that weak models can evaluate strong ones, but does not claim to have "solved" it. The strength is retained with adjusted wording (see Strengths #2).

## Novel Insights
The most interesting finding that goes beyond what the paper itself emphasizes is the *decoupling* between preference accuracy and alignment improvement shown in Figure 2 and discussed in the correlation analysis (line 217). The paper finds that the quality of wrong-over-wrong preferences (Acc_WoW) does not strongly predict downstream alignment gains—even the oracle condition (perfect preferences) does not consistently outperform elicited preferences on all metrics, and the overall correlation is weak. This suggests that (a) the benefit of wrong-over-wrong alignment may come less from the specific preference *direction* and more from exposing the model to a diverse set of paired wrong answers during continued training, or (b) the proxy-based evaluation is too noisy to reveal the true relationship. Either interpretation is important for future work and warrants deeper investigation than the paper currently provides.

## Suggestions

1. **Add a random-preference DPO control** to the alignment experiments (Major #1). Use the same set of wrong-answer pairs but randomly assign chosen/rejected labels. If this control yields substantially smaller improvements than wrong-over-wrong preferences, the paper's central causal claim is confirmed. If improvements are similar, reframe the contribution around the pipeline's overall effectiveness rather than the preference direction.
2. **Add an SFT-only baseline** on the wrong answers (without pairwise preferences) to help disentangle continued-training effects from preference optimization.
3. **Discuss how proxy noise might affect both Acc_WoW and p_wrong.** For example, FActScore's moderate correlation with human factuality judgments means the 70.9% figure is noisy relative to hypothetical human judgments of wrongness.
4. **Report alignment results on at least one additional base model** (e.g., Mistral-7B or LLaMA3-70B via QLoRA) to strengthen generalizability claims for RQ2.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>