Now I have all the information needed to produce the consolidated review.

---

## Summary

This paper identifies harmful perturbation (a gradient step on harmful data) as a cause of alignment breakdown during LLM fine-tuning, and proposes Booster, an alignment-stage regularizer that penalizes the reduction in harmful loss after a simulated harmful gradient step. Combined with standard alignment loss, Booster is evaluated across four downstream tasks, multiple attack settings (harmful ratio, sample count), and three model families (Llama2-7B, Gemma2-9B, Qwen2-7B), consistently achieving lower Harmful Score (HS) than SFT, Lisa, RepNoise, and Vaccine while maintaining or improving fine-tune accuracy.

## Strengths

1. **Consistent and large empirical improvements across diverse settings.** Booster substantially reduces Harmful Score compared to all baselines. Under varying harmful ratios (Table 1), Booster's average HS is 10.94% vs. the next best (Lisa, 21.88%). Across four fine-tuning datasets (Table 4), Booster averages 14.63% HS vs. Lisa's 14.98% and Vaccine's 25.15%. Across three model architectures (Table 5), Booster averages 7.03% HS vs. Lisa's 21.33%. These gains are large and consistent, strongly supporting the method's effectiveness.

2. **Principled and well-motivated defense design.** The regularizer (Eq. 1) directly targets the identified cause: it simulates a normalized harmful gradient step and minimizes the resulting reduction in harmful loss. Unlike prior alignment-stage defenses (Vaccine uses only alignment data; RepNoise uses an MMD-based embedding perturbation), Booster's loss explicitly operationalizes the perturbation concept. The connection between the causal analysis (Figure 1, motivation section) and the method is clean.

3. **Thorough ablation and hyperparameter analysis.** The paper systematically studies regularizer intensity λ (Table 7), inner step size α (Table 8), and number of harmful alignment samples (Table 9), providing practical tuning guidance. The ablation with λ=0 confirms that the gains come from the regularizer, not merely from having the harmful dataset present during alignment in some unspecified way.

4. **Demonstrated generality across models and tasks.** Results on Llama2-7B, Gemma2-9B, and Qwen2-7B, as well as SST2, AGNEWS, GSM8K, and AlpacaEval, show the method is not brittle to a particular architecture or task type. The especially strong result on Qwen2-7B (HS=1.6%, FA=95.64%) is notable.

## Weaknesses

### Major

1. **Missing baseline: simpler use of harmful data during alignment.** The paper does not compare against a direct alternative where the harmful dataset is used during alignment in a straightforward way — e.g., pairing harmful prompts with safe responses and adding them to the alignment dataset (i.e., augmenting the alignment data) via standard SFT, or adding a term `γ·h_safe(w)` that directly minimizes the loss on harmful-prompts-with-safe-answers. The λ=0 ablation shows that removing the regularizer (i.e., pure SFT on alignment data only) gives HS=27.00, while Booster with λ=5 gives HS=8.30. But λ=0 uses no harmful data at all during alignment; it does not isolate whether the benefit comes from the meta-regularizer's specific mechanism or simply from exposing the model to harmful prompts during alignment (even with safe answers). Without this baseline, the reader cannot determine whether the meta-regularizer's extra complexity (three forward/backward passes per step) is justified over a simpler multi-task objective that also uses the harmful dataset. This is the most significant gap because it directly affects attribution of the paper's core algorithmic contribution.

2. **No variance or statistical significance reported.** All results are single-run point estimates without error bars. Given well-known variability in LLM fine-tuning (random seed, LoRA initialization, batch order), it is impossible to assess whether the reported improvements (e.g., 17.26% / 20.08% HS reductions) are statistically meaningful or could shrink with different seeds. This is a critical gap for a paper making quantitative comparative claims. While single-run evaluation is somewhat standard in this specific literature (Vaccine, RepNoise), the community should expect basic reliability reporting, and its absence weakens confidence in the results.

3. **Overclaimed novelty that mispositions the contribution.** The paper states: "To the best of our knowledge, we are the first to identify harmful perturbation as the cause of alignment broken" (line 57). The formalization and empirical demonstration (Figure 1) are useful, but the core observation — that gradient steps on harmful data reduce harmful loss and cause the model to respond harmfully — is a straightforward consequence of gradient-based optimization on harmful samples. Prior work (e.g., Vaccine's "harmful embedding drift") implicitly recognizes the same phenomenon. The paper would be better served by positioning its contribution as a *practical defense method* (a novel regularizer) rather than claiming to have discovered a new cause. This overclaim does not invalidate the results but mischaracterizes the contribution's nature and may alienate informed readers.

### Minor

4. **No validation of the first-order gradient approximation.** The derivation from Eq. (2) to Eq. (3) drops the Hessian term, approximating it as constant — a common practice in first-order MAML. The paper cites Finn et al. and Rajeswaran et al. in justification, but does not analyze whether this approximation preserves the regularizer's intended effect in this specific setting (where the outer objective is itself a difference of harmful losses). An experiment comparing with a full second-order update on a small model, or at least a theoretical justification conditioned on the normalized gradient step, would substantially strengthen the work.

5. **RepNoise baseline performance appears unusually weak.** In Table 1 (p=0.1), RepNoise achieves HS=32.10 vs. SFT's 33.70 — barely better than no defense. This is inconsistent with published RepNoise results, suggesting either suboptimal hyperparameter tuning or a mismatch in the experimental setup. The paper should report the hyperparameters used for each baseline (e.g., regularizer weight, learning rate) and whether they were independently tuned. Without this, the comparison may be unfairly favorable to Booster.

6. **Experiments are LoRA-only (rank=32).** All experiments use LoRA for both alignment and fine-tuning. The "harmful perturbation" is therefore defined and countered in a low-rank subspace of parameters. The paper would benefit from at least one full-parameter fine-tuning setting (e.g., LoRA with rank=64, or full FT on a smaller model) to demonstrate that the concept and defense transfer beyond the low-rank regime. This is acknowledged in the paper's setup but not discussed as a limitation.

7. **No dedicated limitations section.** The paper does not discuss its own limitations: the defense weakens as the number of fine-tuning samples or harmful ratio grows (evident in Tables 1 and 2), the method requires access to a harmful dataset representative of future attacks, and the LoRA-only scope limits generality. Adding a limitations paragraph would strengthen the paper's scholarly integrity.

### Trivial

8. **Minor notational issues.** The paper alternates between "harmful score" and "HS" without always defining the abbreviation at first use in each section. The caption for Table 1 references "tab:my_table" rather than a meaningful label.

## Nice-to-Haves

- An analysis relating the inner step size α to the typical learning rate used in fine-tuning (1e-5) — if α matches the effective per-step perturbation, the simulation is faithful; if not, α may be simulating unrealistically large or small perturbations.
- Results on a more recent model such as Llama3-8B or Mistral-7B to strengthen the generality claim.
- A discussion of how the service provider would obtain a representative harmful dataset that matches the distribution of future user attacks (a practical deployment constraint).

## Removed Points

- **Criticism about "harmful dataset availability" being an unrealistic assumption.** The paper explicitly cites BeaverTails as an existing open dataset (line 66-67), and the assumption is standard in prior defense work (RepNoise, TAR). This is not a weakness of the paper — it is a stated and reasonable assumption shared by the field.
- **Complaints about computational overhead not being justified.** The paper already provides a system evaluation (Table 6) showing Booster is faster and uses less memory than RepNoise, and correctly argues that alignment-stage overhead is a one-time cost amortized over many fine-tuning requests. The reviewer's concern about "simpler alternatives" is subsumed by the missing baseline point (Major #1), but as stated it ignores the paper's existing justification.
- **The suggestion that the paper does not discuss how the harmful dataset matches future attacks.** Line 66-67 already states this assumption and cites the relevant dataset. The paper is not a deployment guide; this level of practical detail is beyond scope.
- **Formatting/style nitpicks and complaints about missing appendix content.** The parser strips appendices; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful methodological gaps (missing baseline, no variance reporting) but do not contribute novel insights the paper itself does not already articulate.

## Suggestions

1. **Add the critical missing baseline** — a variant where harmful prompts are paired with safe responses and added to the alignment dataset via standard SFT (i.e., `f(w) + γ·h_safe(w)`). Use the same harmful dataset, same compute budget, and show that Booster's meta-regularizer yields better HS/FA trade-off. If it does, the meta-learning framing is justified. If not, the simpler method should be preferred.
2. **Report mean ± std over at least 3 seeds** for the main results (Tables 1, 2, 4, 5). This is table-stakes for any paper making comparative empirical claims.
3. **Validate the first-order approximation** on a smaller model (e.g., Llama-1B) by comparing against a full second-order update or finite-difference Hessian approximation.
4. **Tone down the novelty claim.** Acknowledge that the basic observation (gradients from harmful data reduce harmful loss) is not new, and reframe the contribution as a *method* that exploits this via a specific meta-regularizer.
5. **Tune all baselines more carefully for the specific setting** (Llama2-7B, LoRA, 20 epochs) and report the hyperparameters searched. The near-SFT performance of RepNoise (Table 1) is a red flag.
6. **Add a limitations paragraph** explicitly discussing the HS degradation with larger harmful ratios/sample sizes, the LoRA-only scope, and the reliance on a representative harmful dataset.

## Score and Decision

**MY FINAL SCORE:** <pineapple>5.0</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>