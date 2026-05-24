Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes LitCab, a lightweight calibration method that adds a single linear layer (<2% extra parameters) on top of an LM's last hidden states to predict logit biases, trained with a contrastive max-margin objective using correct and incorrect generations. The authors construct CaT-Bench, a benchmark spanning eight text-generation tasks at phrase, sentence, and paragraph levels, and introduce a four-step claim-level evaluation procedure for long-form calibration. Experiments on Llama2-7B show average ECE reduction from 0.137 to 0.093 (32% relative) across all tasks, alongside a cross-model analysis of seven open-source LMs yielding several empirical findings about model scaling and instruction tuning.

## Strengths

- **Lightweight and practical design with measurable gains**: LitCab adds a single linear layer (confirmed <2% of original parameters, line 9) and achieves the lowest average ECE (0.093) and Brier score (0.197) across all eight tasks on Llama2-7B in Table 1, outperforming temperature scaling, label smoothing, P(IK), verbalization, and self-consistency on the phrase- and sentence-level tasks where all baselines are compared.

- **Novel evaluation methodology for long-form calibration**: Section 3.2 and Figure 2 introduce a four-step procedure (claim extraction via GPT-3.5-turbo, span mapping via LCS, confidence estimation via token-probability aggregation, correctness verification via GPT-4 with retrieval) that addresses a real gap — existing calibration work focuses on short-answer QA. This methodological contribution goes beyond the method itself.

- **Construction of a dedicated calibration benchmark (CaT-Bench)**: Section 5 assembles eight tasks spanning phrase (NQ, SciQ, TriviaQA), sentence (TruthfulQA, WikiQA), and paragraph (BioGen, WikiGen, QAMPARI) levels, including two new tasks (WikiGen, QAMPARI). This provides a standardized test bed for evaluating LM calibration across response lengths, which the community can reuse.

- **Comprehensive cross-model analysis with non-obvious findings**: Figure 3 evaluates GPT-2 XL, GPT-J, LLaMA (7B/13B/30B), Llama2 (7B/13B), and Vicuna-13B, yielding three empirically supported insights: (i) scaling improves calibration only on short tasks, (ii) GPT-2 XL (1.5B) is better calibrated than much larger models, (iii) Vicuna's instruction tuning degrades calibration relative to LLaMA-13B.

## Weaknesses

### Fatal
None.

### Major

1. **Unsupported claim that LitCab "outperforms all LM confidence estimation methods in phrase- and paragraph-level tasks."**  
   Line 343 states: "*LitCab outperforms all LM confidence estimation methods in phrase- and paragraph-level tasks and attains the lowest average ECE and Brier score.*" However, in Table 1, all three LM confidence estimation methods (P(IK), Verbalization, Self-Consistency) show "--" for every paragraph-level task (BioGen, WikiGen, QAMPARI) — no comparison exists. The paper itself explains (line 266) that these methods "cannot be used to assess calibration at the claim level" and that results are therefore not listed. The paper cannot claim to outperform methods it did not compare against on paragraph-level tasks. This is not a minor phrasing issue; it is a direct overclaim that undermines the paper's central narrative about long-form calibration superiority. At minimum, the claim should be restricted to phrase- and sentence-level tasks (as the paper correctly does on line 345).

2. **Missing baseline comparisons on the paper's most novel setting (paragraph-level tasks).**  
   Three of five baselines — P(IK), Verbalization, and Self-Consistency — are excluded from paragraph-level evaluation with the justification that they produce single-generation scores rather than claim-level scores. While this justification has some merit, it means the paper's headline claim that LitCab outperforms existing methods is only fully tested on phrase/sentence tasks where the long-form motivation is weakest. On paragraph tasks, LitCab is compared only against temperature scaling and label smoothing, and the gains are often modest (BioGen: 0.169→0.166 ECE, WikiGen: 0.045→0.037 ECE). The conclusion that LitCab is superior for long-form responses is not fully established without some attempt to adapt these baselines (e.g., verbalized confidence per extracted claim, or self-consistency over multiple paragraph generations followed by claim extraction).

3. **Unvalidated paragraph-level evaluation pipeline raises reliability concerns.**  
   The four-step procedure for paragraph-level calibration (Figure 2) relies entirely on GPT-3.5-turbo for claim extraction and span mapping, and GPT-4 for correctness verification. The paper provides **no human evaluation** of: (a) claim extraction quality (completeness, fragmentation), (b) span-mapping accuracy (whether LCS on GPT rephrasings reliably identifies the correct span), or (c) agreement between GPT-4 correctness judgments and human judgments. The paper cites prior work for the retrieval component's robustness (line 159), but this does not validate the full pipeline. Since the primary calibration metric (ECE) depends entirely on this pipeline for paragraph-level tasks, the measured improvements could be artifacts of the evaluation procedure rather than genuine calibration gains. This limits the trustworthiness of the paragraph-level results.

### Minor

4. **Training data asymmetry between LitCab and label smoothing.**  
   LitCab is trained with both positive and negative samples via its max-margin objective (lines 194-201), while label smoothing — the only training-based baseline — is fine-tuned using only positive (accurate) samples (line 267: "but only keep the accurate claims"). The paper attributes label smoothing's poor performance to "small size of training data that leads to model overfitting" (line 340), but this speculation conflates two differences: (i) the calibration method itself and (ii) the availability of negative supervision. A fairer comparison would require giving label smoothing access to the same negative samples (e.g., by treating them as incorrect label examples) or training LitCab on positive-only data. The claimed "superior data efficiency" is premature given this asymmetry.

5. **No statistical significance or variance reported for any metric.**  
   All metrics (ECE, Brier, acc@q, cov@p) in Table 1 are point estimates with no standard deviations, confidence intervals, or multi-seed experiments. Given small task sizes (e.g., TruthfulQA ~800 samples), some reported improvements could be within noise. A minimal improvement would be reporting bootstrapped intervals or results over multiple random seeds.

6. **LitCab is only applied to Llama2-7B for the main comparison.**  
   The cross-model analysis (Figure 3) evaluates calibration of seven LMs but does not test whether LitCab's benefits generalize beyond Llama2-7B. Since Section 6.3 finds large calibration differences across model families (GPT-2 XL vs. LLaMA vs. Vicuna), it would strengthen the contribution to show that LitCab works on at least one other model. This limits the generality claims about the method.

7. **Inconsistent model reference for claim extraction.**  
   The figure caption (line 133) correctly states "GPT-3.5-turbo" is used for claim extraction, but the procedure text (line 149) says "We prompt GPT-3." — an inconsistency that matters for reproducibility, as GPT-3 (text-davinci-002/003) and GPT-3.5-turbo are different model classes.

8. **No sensitivity analysis of key hyperparameters.**  
   The max-margin objective uses a fixed margin of 1 (line 199), and the number of negative samples is 3 for short tasks but unspecified for paragraph tasks ("all generated positive and negative samples," line 201). The paper does not ablate these choices or discuss sensitivity, leaving questions about robustness.

### Trivial

- Line 152 contains a stray closing brace ("}") after "span." — a LaTeX artifact from the original formatting.
- The QAMPARI extraction method is described only as "can be easily extracted" (line 220) but the actual extraction procedure is not specified, leaving a minor documentation gap.

## Nice-to-Haves

- A small human-annotation study (e.g., 50-100 claims per paragraph task) validating the claim-level evaluation pipeline would substantially increase confidence in the paragraph-level results.
- Testing whether LitCab trained on one model (e.g., Llama2-7B) transfers to other model families, or whether its benefits hold across model sizes, would significantly raise the contribution's impact.
- Ablations on the margin value and number of negative samples would help understand when and why LitCab works.

## Removed Points

These points were identified by reviewers but excluded from the main evaluation under the filtering rules:

- **"30% claim is misleading" (Harsh Critic Section-by-Section)**: The paper states "reducing the average ECE score by as large as 30%" (line 11). The average ECE drops from 0.137 to 0.093 (32% relative), making the claim factually accurate. Removed as the criticism misreads the qualified wording.
- **"Vicuna finding ignores training distribution difference" (Harsh Critic, conclusion note)**: The paper explicitly notes Vicuna "is fine-tuned from LLaMA-13B on user-shared conversations" (line 375), acknowledging the distribution difference. The finding is stated as an observation, not a universal claim. Removed as the paper already addresses this.
- **"Missing appendix content" (Harsh Critic, various references)**: The paper references appendices for prompts and details, which were stripped by the PDF parser. Per the hard rule, these absences are not author errors. Removed.
- **"Verbalization per claim dismissed without justification" (Harsh Critic, §6.2 note)**: The paper provides a justification: these methods produce single-generation scores not suitable for claim-level calibration (line 266). While the adaptation is possible, the paper's justification is not unreasonable for a first presentation. Demoted to a nice-to-have consideration rather than a weakness.
- **"Cross-model evaluation of LitCab would be natural" (Harsh Critic, Strengthening section)**: Agreed this would strengthen the paper, but it is outside the paper's stated scope (focus on Llama2-7B). Moved to Nice-to-Haves.
- **Generic strength about "addressing an important problem"**: The Strength Finder's implicit framing that "the problem is important" is a generic observation not specific to this paper. Removed as too generic.

## Novel Insights

The reviews collectively surface a tension between the paper's methodological ambition and its evidential strength. The paper identifies a genuine gap — long-form LM calibration — and proposes a sensible lightweight solution plus a benchmark. However, the claim about paragraph-level superiority (line 343) is an overreach that is directly contradicted by the paper's own table, where no comparison data exists for paragraph-level tasks against the most relevant LM-specific baselines. This overclaim, combined with the unvalidated GPT-based evaluation pipeline, means the paper's most distinctive contribution (long-form calibration) rests on the weakest evidence. The irony is that the method's effectiveness is well-supported on short-form tasks — the setting the paper treats as less novel — while the long-form claims are unsupported by the evidence as presented.

## Suggestions

1. **Correct the overclaim on line 343**: Restrict the claim to "phrase- and sentence-level tasks" or acknowledge that the paragraph-level comparison is only against traditional methods (temperature scaling, label smoothing).
2. **Add a small human-annotation study** validating the claim-level pipeline (even 50 claims per paragraph task), or at minimum report agreement statistics between GPT-4 and human judgments for the correctness step.
3. **Add variance estimates**: Report ECE/Brier scores over multiple random seeds or bootstrapped confidence intervals.
4. **Ablate the margin hyperparameter** and the number of negative samples to demonstrate robustness.
5. **Test LitCab on at least one additional model** (e.g., Llama2-13B or GPT-J) to show generality beyond Llama2-7B.
6. **Fix the GPT-3/GPT-3.5-turbo inconsistency** (lines 133 vs. 149).

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>