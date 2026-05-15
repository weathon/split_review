Now I have a thorough understanding of the paper and have verified each claim. Let me produce the final consolidated review.

## Summary

This paper proposes Context Steering (CoS), a training-free inference-time method that modulates the influence of contextual information on LLM generation by computing the logit difference between a model with and without context, scaled by a parameter λ. The method is applied to three settings: personalization (amplifying context), bias mitigation (attenuating or redirecting context via an equalizing prompt), and hate speech quantification (inverting the forward model to infer the "hate level" λ of a tweet). CoS is related to contrastive decoding but reframes the logit difference as "contextual influence" and adds a Bayesian inversion procedure.

## Strengths

- **Training-free, broadly applicable method**: CoS requires only log-probability access (not model weights) and works with API-gated models. It can be applied at inference time without fine-tuning, which is a practical advantage over debiasing or personalization methods that require dataset collection and retraining. The paper demonstrates this across T0pp, Mistral-7B-instruct, and Llama2-7B-Chat.

- **Interpretable single-parameter control**: The λ parameter provides a straightforward, continuous knob that qualitatively shifts generation tone — from scholarly and generic (low λ) to highly contextualized and empathetic (high λ) — as shown convincingly in Table 1's Newton's second law examples spanning λ ∈ {−3, −1, 0, 1, 3}. The qualitative examples are illustrative and build intuition for how λ affects generation.

- **Effective hate speech quantification**: On the Implicit Hate dataset, CoS-based hate ratings align better with expert human judgments (p = 0.0295) than a direct LLM-based rating baseline, and CoS outperforms the LLM baseline on implicit hate classification for 2 out of 3 target groups (82% vs. 50% on Black, 47% vs. 37% on Immigrant). This is a genuinely non-obvious application of the inverse framework.

- **Bayesian inversion provides a novel analytical tool**: The inverse inference procedure (Eq. 4–5) enables probing what context the model "thinks" it is responding to given a generation. The STEM proficiency example (Figure 2) showing that generations from "I am familiar with STEM" are inferred to have higher λ under "college student" than under "middle schooler" is a clean demonstration of probing latent associations in LLMs.

## Weaknesses

### Fatal

None.

### Major

- **User study only tests two λ values, failing to demonstrate fine-grained continuous control.** The personalization experiment uses only λ ∈ {−1, 3} with 8 participants. The claim that CoS provides "fine-grained control" (as stated in the Introduction) or that "higher λ increases personalization" in a graded sense is not supported — the binary comparison merely shows that λ = 3 produces more personalized-sounding text than λ = −1, which is a different (and far weaker) claim. The Spearman correlation of ρ = 0.67 is driven by a two-group contrast and does not demonstrate a monotonic trend across the λ continuum. Without testing at least 3–5 values across the range (e.g., −1, 0, 1, 2, 3), the central claim of *continuous* controllable generation is unsubstantiated by this experiment.

- **The Bayesian "inference" framing overstates what is actually done.** Equations (4) and (5) present Bayes' rule with integrals over continuous C and λ, but the paper immediately acknowledges the normalizing constant is intractable and resorts to computing the maximum likelihood over a *discrete candidate set* (line 116: "In practice, we can instead compute the maximum likelihood of candidate set Λ or C"). This is likelihood-based ranking, not Bayesian inference over a latent variable. The abstract's claim that CoS "can be combined with Bayesian Inference to quantify the extent of hate speech" implies a richer probabilistic framework than is realized. The method is still useful, but the framing promises more than it delivers.

- **The relationship to contrastive decoding / DExperts is acknowledged but the distinct contribution is not clearly articulated.** The paper states in the Related Work section (line 61) that the approach is "similar to" contrastive logit modification, but upon reading the method section one finds that CoS_λ(x_i|C,P) = (1+λ)LLM(x_i|C,P) − λ·LLM(x_i|∅,P) — which is mathematically the same functional form as contrastive decoding with the amateur model replaced by the same model without context. The paper does not explain why reinterpreting this operation as "contextual influence" rather than "contrastive quality improvement" constitutes a distinct methodological contribution beyond the application domain. This is not fatal (the Bayesian inversion is genuinely novel), but it limits the paper's technical novelty.

- **The IAT bias experiments are presented without sufficient rigor.** The IAT section (lines 179–180) contains a single brief paragraph with no numerical results, no statistical tests, and no clear evaluation protocol. The figure referenced (Figure 4, labeled `fig:exp-decision-bias`) is accompanied only by the vague caption "Decision bias on IAT test with different models, plotted under increasing λ values." The text describing the results appears truncated ("i.e. In \textit{decision tasks}..."). As presented, this experiment does not provide any meaningful evidence for bias mitigation.

### Minor

- **The bias metric for the BBQ experiment is never defined.** The paper reports "accuracy and bias" across λ values (Section 4.2, Figure 5) and claims that "bias also decreases for increasing λ," but never specifies how bias is calculated. The BBQ benchmark defines standard bias metrics (e.g., the difference in accuracy on stereotypical vs. anti-stereotypical ambiguous pairs), but the paper does not state which one is used or how the reported quantity relates to established definitions. Readers cannot independently verify the bias reduction claim.

- **The hate quantification result relies on a single borderline p-value (0.0295) without correction, and the baseline comparison is limited.** A p-value of 0.0295 does not survive a Bonferroni correction for even a small number of tests. Moreover, the only baseline is a direct LLM-based rating — no comparison to existing hate speech quantification methods (e.g., toxicity classifiers, lexicon-based approaches) is provided. The classification results (Table in Figure 6) are on only 3 target groups with 2–3 classes each, and CoS is comparable to (not clearly superior to) the LLM baseline.

- **The 2× inference cost of CoS (two forward passes per token) is never mentioned.** The method requires one forward pass with context and one without for every generated token, doubling inference cost. For a method presented as practical and deployable, this overhead should be acknowledged.

### Trivial

None.

## Nice-to-Haves

- Test at least 3–5 λ values in the personalization user study to credibly demonstrate graded, continuous control.
- Add a standard prompting baseline (λ = 0 with the equalizing context) explicitly highlighted in the BBQ results.
- Define the BBQ bias metric clearly and report it alongside accuracy.
- Compare to existing debiasing methods (e.g., self-debiasing, fairness prompting) for context.
- Add per-tweet correlation (e.g., Spearman's ρ) between CoS λ estimates and human ratings in the hate quantification experiment, with confidence intervals.

## Removed Points

These points were flagged for removal — treat with caution:

- **"The method is a trivial instance of well-known contrastive techniques"**: The paper explicitly acknowledges the connection to contrastive decoding in the Related Work section (line 61) and the contribution includes the Bayesian inversion framework, which is not present in prior work. The criticism is accurate about the limited technical novelty of the forward direction but overstated in calling it "trivial."

- **"BBQ never compares to λ=0"**: The paper explicitly states λ=0 corresponds to prepending the context without modulation (line 91), and the figures show results across λ values. The reviewer likely missed that λ=0 *is* the standard prompting baseline.

- **"The notation LLM(·) is ambiguous"**: The paper clearly defines LLM(·) as outputting logits (line 73: "this step outputs logits, which can be converted into the probability of the next token being generated under the softmax operation").

- **"The improvement from CoS may be specific to models that already respond to context well"**: Removing models at floor performance (Llama2-7b, GPT-J on BBQ) is standard experimental design to avoid floor effects. This does not undermine the results.

- **"CoS classification results are comparable to a weak baseline"**: CoS outperforms the LLM baseline on 2 of 3 groups (82% vs. 50%, 47% vs. 37%) and is competitive on the third (60.5% vs. 62%). This supports rather than undermines the claim.

- **Pure formatting nitpicks and complaints about missing appendix content**: These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper's core idea — that logit-level contrast between context-conditioned and context-free distributions enables controllable generation — is simple and intuitive, and the qualitative demonstrations are compelling. But the paper consistently claims *more* than the experiments support (fine-grained continuous control from 2 λ values; Bayesian inference from discrete MAP; bias reduction without defining the bias metric). The reviews collectively suggest that the paper's strength is in the conceptual framework and qualitative demonstrations, while the quantitative evidence is a clear step below what would be needed for acceptance at a top venue.

## Suggestions

1. **Acknowledge the limited novelty of the forward direction more directly** in the main text, and position the paper's contribution squarely on the Bayesian inversion framework (which *is* novel) rather than on the logit-difference operation.
2. **Run the personalization study with at least 4 λ values** (−1, 0, 1, 3) and more participants to support the continuous-control claim.
3. **Define the BBQ bias metric explicitly** and include a direct comparison to λ = 0 (standard prompting) as a highlighted row or annotation.
4. **Provide numerical results and statistical tests for the IAT experiments**, or remove them if they cannot be rigorously defended.
5. **Tone down the Bayesian language** (e.g., "likelihood-based context inference" instead of "Bayesian Inference") or implement actual Bayesian inference with proper marginalization.

## Score and Decision

The paper presents a clean, intuitive idea with broad applicability, and the Bayesian inversion framework is a genuinely novel contribution. However, the experimental validation is substantially weaker than what the claims require: the user study uses only 2 λ values, the bias metric is undefined, the IAT experiments lack all numerical rigor, and the Bayesian framing is overclaimed. The technical novelty of the forward model (logit-level contrast) is limited and explicitly connected to prior work. These issues are addressable in revision, but in its current form the paper does not meet the evidential bar for its claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>