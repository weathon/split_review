- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 5, 3, 1, 3
I have thoroughly read the paper and verified all key claims against the actual text. Let me now construct the consolidated review.

---

## Summary

The paper proposes CVX-DPO, a method for preference fine-tuning of small language models that stacks a convex two-layer ReLU network on top of a frozen pretrained model, then fine-tunes only the convex network's last linear layer (θ₂) via a modified DPO objective. The authors claim the approach eliminates the reference model, guarantees global optimality via convexity, and enables training on a single RTX-4090 GPU. Experiments are conducted on three datasets (IMDb, custom Educational Tutor, Stanford-SHP) with evaluation via training loss curves and a human survey of 25 volunteers on 12 prompts.

## Strengths

- **Genuinely lightweight compute profile.** The paper demonstrates that all experiments run on a single RTX-4090 (line 165), with training times as low as ~2 minutes for SFT on the Educational Tutor dataset. This is a meaningful practical contribution, especially given the paper's stated goal of democratizing access to alignment fine-tuning.

- **Robustness to hyperparameter tuning is empirically supported.** Figures 1–2 and the text (lines 213–214) report that the DPO-Convex model "shows the most stable training performance" and "consistently" decreases loss "without any tuning of hyperparameters." This is a concrete, falsifiable observation that strengthens the paper.

- **Novel data-construction strategy for preference pairs.** The "alternating preference" strategy (line 152) constructs chosen/rejected pairs from natural multi-turn conversation by using the immediate next response as "chosen" and a later response as "rejected," without requiring an external LLM prompt. This is a practical, reusable contribution.

- **Prediction that DPO-Convex generates longer responses (line 227).** While not rigorously quantified, the paper identifies an interesting empirical pattern that could motivate future analysis of the relationship between convex-trained models and response length.

## Weaknesses

### Fatal
None.

### Major

- **Mathematical gap in the loss derivation (Proposition 1).** Equation 6 (line 120–122) contains the term $\pi_{\text{ref}}$ in the log-ratio: $\log(\pi_{\theta_2}^{\text{cvx}}(y_w|x)/\pi_{\text{ref}}(y_w|x))$. Proposition 1 (Equation 7, line 128–130) replaces this with $-\beta y_w \theta_2^T(\Theta_1 f_{\theta_{\text{pre}}}(x))_+ - \gamma$, **eliminating the $\pi_{\text{ref}}$ term entirely without any derivation or justification.** The paper claims to "eliminate the dependence on copying the reference model" (abstract, line 7–8), yet the stated loss function contradicts this unless a non-trivial algebraic step is missing. Since the reference model log-probability $\log \pi_{\text{ref}}(y_w|x)$ is input-dependent, it cannot be absorbed into the scalar $\gamma$ without further justification. This is a genuine mathematical gap in the paper's core technical claim. Either Equation 6 is incorrect (it should not contain $\pi_{\text{ref}}$) or Proposition 1 is incomplete. Either way, the paper does not provide a valid derivation.

- **Evaluation is far too weak to support the claimed contributions.** The human evaluation uses only 12 prompts and 25 volunteers on a single custom dataset (lines 184–188), with no statistical significance measures. No quantitative evaluation metrics (reward accuracy, generation quality scores, or automated evaluation like GPT-4-as-judge) are reported for **any** dataset — not IMDb, not Stanford-SHP, not the Educational Tutor set. The paper only presents training loss curves (Figures 1–2) and qualitative statements. The paper explicitly says Stanford-SHP is used "to stress test the memory and speed performance" (line 158) but provides no wall-clock time or memory numbers for CVX-DPO on that dataset (only "2.15 hours on the Stanford-SHP with the DPO loss," line 165, which appears to be for the DPO baseline, not CVX-DPO). These omissions leave the paper's central claims (superior alignment, compute efficiency) without adequate quantitative backing.

- **Unfair comparison due to mismatched parameter counts / missing baselines.** CVX-DPO fine-tunes only a linear layer (θ₂) on top of a frozen pretrained model and frozen convex first layer (lines 118–119). DPO fine-tunes the full model. The claimed speed and memory advantages of CVX-DPO are therefore largely attributable to freezing almost all parameters, not to the convex optimization formulation. The paper does not control for this by comparing against parameter-matched baselines such as LoRA-tuned DPO, linear probing with standard cross-entropy, or other lightweight alignment methods. SimPO is introduced as a baseline (Section 5.3) but is **never evaluated** — it appears nowhere in the results.

- **Framing is substantially overstated relative to the actual method.** The paper presents itself as introducing a convex optimization breakthrough for preference learning (title, abstract, Sections 3–4), complete with the full theoretical machinery of convex reformulations, activation patterns, cones, and ADMM. However, the actual fine-tuning step (fine-tuning θ₂ via logistic regression on frozen features) is a textbook convex problem solvable by any gradient-based optimizer. The elaborate convex network machinery in Section 3 is used only to train the first layer (Θ₁) in a pre-processing step; the DPO fine-tuning itself never invokes ADMM or the cone constraints. This disconnect between framing and substance is significant.

### Minor

- **Section 4.2 ("Convex DPO Algorithm") is empty** — just a section header (line 138) followed immediately by Section 5 (Experiments). No pseudo-code, no training loop, no convergence criteria, and no description of how ADMM interacts with the DPO fine-tuning step are provided. This impairs reproducibility.

- **The human evaluation metric ("average preference") is ambiguously defined.** The paper states (line 215): "The average preference is calculated as the percentage of each model's win rate divided by the number of times it won." This definition combines "win rate" and "number of times it won" in a way that is not clearly interpretable. The 83.3% figure for DPO-Convex is presented without confidence intervals or clarification of the exact calculation.

- **The "alternating preference" data construction is not validated or ablated.** The paper proposes a novel preference pair construction strategy (Section 5.1) but never evaluates whether it produces higher-quality preference pairs than alternatives (e.g., random sampling, human annotation, or external LLM prompts). Its effect on results is confounded with the method itself.

- **No analysis of the γ hyperparameter.** Equation 6 introduces a hyperparameter γ that replaces the second log-ratio term from standard DPO. The paper does not analyze its effect, range of effective values, or sensitivity.

- **Textual inconsistencies.** The paper refers to "Educational Tutor" (line 156) but the analysis section discusses a "Hotel-Concierge setting" (line 227), suggesting the text may be inconsistent between the dataset description and the discussion. Section 5.5 refers to a "baseline FST model" (line 215) that was not previously defined (the baseline in Section 5.3 is "DistilGPT2 with supervised fine-tuning loss").

### Trivial

- The paper refers to "Table 5.5" as a results summary (lines 200, 215) but the only numbered table is "Table 1" (line 196). The actual table is embedded as an image, making the numerical values inaccessible for independent verification.

## Nice-to-Haves

- Adding LoRA-fine-tuned DPO as a baseline would help isolate whether the benefits come from convexity or from parameter freezing.
- Reporting confidence intervals for the human evaluation (e.g., via bootstrap resampling) would substantially strengthen the empirical claims.
- Wall-clock and peak-memory comparisons between CVX-DPO and DPO under the same hardware would directly support the efficiency claims.
- Automated evaluation (e.g., AlpacaEval, reward model scoring) would complement the human study with replicable, low-variance metrics.

## Removed Points

These points were flagged by reviewers but are removed or demoted for the reasons described:

- **"The method is a trivial convex problem / ADMM is irrelevant"** (from harsh critic): Kept as a framing issue (Major) but the critic's stronger claim that this is a "structural flaw that cannot be fixed" is removed. The convex network training (stage 1) does use ADMM; the critic's framing ignores this. The disconnect is real but potentially fixable with honest reframing.

- **"The critic claims the 'Table 1 is a placeholder image'"**: Removed. The table IS an embedded image in the PDF — this is a parsing artifact common in PDF extraction, not a paper flaw. The table exists.

- **"The critic's point about missing visualizations from omitted appendix"**: Removed. The reviewer is not supposed to penalize papers for missing appendix content that may have been stripped during parsing.

- **"The average preference calculation contradiction"** (equal win rate but 83.3% preference): Removed. A model can have equal win rate but stronger preference when it wins (larger margins). This is not a contradiction.

- **Strength Finder's generic strengths** ("addresses an important problem," "targets an interesting question"): Removed as generic/superficial. Only concrete, paper-specific strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the paper's weaknesses (insufficient evaluation, overclaimed framing, mathematical gaps) but provide different granularities. An unappreciated subtlety is that the "alternating preference" data construction strategy — while presented as a minor implementation detail — may actually be the most novel and reusable contribution of the paper, as it enables constructing preference pairs from natural conversation logs without human annotation or LLM prompting. This deserves more attention and validation than the paper gives it.

## Suggestions

1. **Fix the loss function derivation.** Either remove π_ref from Equation 6 (if the reference model is truly not used) and show the closed-form reduction to logistic regression, or provide the full derivation accounting for π_ref if it is used. This is the paper's most critical fix.

2. **Reframe the contribution honestly.** The paper's actual contribution — studying whether linear probing with a DPO-style loss on frozen LLM representations yields competitive alignment — is a perfectly valid research question. Present it as such rather than overclaiming a convex optimization breakthrough.

3. **Add at least one quantitative evaluation on a standard benchmark.** Even a single automated metric (e.g., reward model score on the test set, or GPT-4 evaluation on AlpacaEval prompts) would substantially strengthen the empirical support.

4. **Add parameter-matched baselines.** Compare against LoRA-tuned DPO (with comparable trainable parameters) and against simple logistic regression with cross-entropy loss to isolate the effect of the DPO-style loss.

5. **Provide concrete training time and memory numbers for CVX-DPO** on each dataset, comparable to the "2.15 hours" given for DPO on Stanford-SHP.
