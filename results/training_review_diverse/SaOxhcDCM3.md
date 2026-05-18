Now I have all the information needed to synthesize the final review. Let me carefully construct it.

## Summary

This paper studies the self-consuming training loop — where successive generations of language models are trained on data that includes outputs from prior models — for language models trained from scratch. Using a GPT-style model (10.6M parameters) and a controlled logic-expression dataset that allows unambiguous evaluation of syntactic/semantic correctness and token-level Levenshtein diversity, the authors test four data cycles (full synthetic, balanced, incremental, expanding). They find that while the proportion of semantically correct outputs increases across generations, diversity consistently declines, eventually collapsing to a single point in the full synthetic cycle, and that fresh real data slows but does not halt the decline.

## Strengths

1. **First empirical study of the self-consuming training loop for language models trained from scratch.** Prior work (Shumailov et al., Guo et al.) focused on iterative fine-tuning, while real-world LLMs like GPT are typically trained from scratch on web-scale data. This paper fills that gap with a controlled longitudinal study. (Lines 85-87, Section 2)

2. **Novel evaluation methodology using logic expressions.** The paper designs a logic-expression dataset where correctness is unambiguously verifiable via `eval()` and diversity is measured via token-level Levenshtein distance. This sidesteps the well-known limitations of proxy metrics like BLEU/ROUGE for evaluating generative models. (Section 3.1–3.2)

3. **Systematic exploration of four data cycles with varying proportions of synthetic/real data.** The paper tests full synthetic, balanced, incremental (varying λ), and expanding (varying fresh-data proportion) cycles, showing consistent diversity decline across all configurations. The incremental and expanding cycle experiments with λ variations (Figures 3 and 4) provide a parametric understanding of how data composition affects the rate of decline. (Section 3.3, Figures 2–4)

4. **Qualitative claim about the relationship between fresh data and diversity preservation.** The expanding-cycle experiments quantify that 25% fresh data per generation reduces the diversity decline to only ~11% over 50 generations (vs. ~36% with no fresh data), providing a concrete empirical anchor for discussions about mitigation. (Lines 232–234, Figure 4)

## Weaknesses

### Fatal
None.

### Major

1. **Title, abstract, and contribution claims overreach the experiments.** The paper is titled "Large Language Models Suffer From Their Own Output" and every contribution statement refers to "LLMs," yet the experiments are conducted on a 10.6-million-parameter GPT-style model trained on logic expressions with a 7-token vocabulary (6 logic tokens + `<eos>`). This is not an LLM by any contemporary standard — it is a small transformer language model on a synthetic grammar. While the Limitations section (lines 270–271) acknowledges the model is smaller than GPT-4, the paper does not recalibrate its title, abstract, or bullet-point contributions accordingly. A study of this kind contributes valuable insights about self-consuming training dynamics in small LMs on controlled data, but presenting it as a study of "LLMs" is a significant overclaim that misrepresents the scope of evidence. The authors should either re-scope the paper around "neural language models" or "small language models" or provide an argument for why the findings are expected to transfer to billion-parameter, open-vocabulary models.

2. **Single-run experiments without measures of variance.** The paper states (lines 272–273) that "the main results of this work consist of only one run per experimental configuration" and defends this by saying "As all our experiments point towards the same direction, however, we do not believe that this limitation is crucial." This defense is insufficient. Without multiple random seeds (for initialization, data sampling, training order), we cannot assess the stability of the quantitative results — the specific generation where collapse occurs, the exact shape of diversity curves, or the numerical percentages reported (e.g., "68% decrease," "22% decrease"). The consistency across different data cycles provides some qualitative reassurance, but it does not establish the reliability of the specific quantitative patterns. This is a significant methodological gap that weakens confidence in the paper's numerical claims.

3. **The "increase in correctness" is presented without analysis of what the correct expressions actually are.** The paper states (line 188) that "the self-consuming training loop seems to help with generating more semantically correct expressions" and treats this as a finding alongside the diversity decline. However, the paper does not analyze whether the correct expressions are meaningfully diverse or simply trivial variants of the single token `True` or expressions like `True and True`. Given that the full synthetic cycle collapses to a single point by generation 39 (line 222), the "correctness increase" is very likely just the other side of the diversity collapse — the model converges to producing only the simplest correct expression(s). Without examining the structure/complexity of the generated correct expressions across generations, the paper's framing of this as a potentially positive effect is misleading. The authors should either show that correct expressions retain nontrivial structure as diversity declines, or explicitly acknowledge that the correctness increase is a direct artifact of collapse.

### Minor

4. **Unsupported extrapolation about inevitable collapse to zero diversity.** The paper states (line 225): "While not all data cycles fully collapse in diversity by generation 50, ultimately, we expect all of them to eventually reach zero diversity if the self-consuming training loop is run for enough generations." For the balanced and expanding cycles, diversity appears to be decelerating (30% and 22% decreases respectively over 50 generations). The paper provides no theoretical argument or longer-run experiments to support the claim that these curves will hit zero rather than plateau at a non-zero value. This claim should either be supported by longer experiments or tempered to acknowledge the possibility of a plateau.

5. **Validation data composition is unspecified.** The paper splits data 90% training / 10% validation and uses validation error for early stopping (line 163), but it does not clarify whether the validation split follows the same data-cycle construction as the training set (i.e., contains a mix of real and synthetic data) or is always drawn from the original real distribution. If the validation set includes synthetic data, the validation error measures fit to a changing distribution, which could affect which checkpoint is selected each generation and bias the comparison across generations. The authors should clarify this design choice.

6. **Missing analysis of what the model actually produces at collapse.** For the full synthetic cycle, the paper notes that diversity collapses to zero and the number of unique expressions drops to "very few" (line 227), but it does not report what those expressions are. This would provide critical interpretability: are there just a handful of distinct expressions, or is it a single string repeated? Is it `True`, or something more structured? This is trivially analyzable and would significantly strengthen the interpretability of the results.

### Trivial
None beyond those already listed above.

## Nice-to-Haves

- The expanding cycle with 25% fresh data shows only an ~11% diversity decline over 50 generations (line 234). The paper could usefully contextualize whether this decline accumulates to a practical problem at realistic timescales (e.g., hundreds of generations), or whether it would likely plateau.
- The token-level Levenshtein distance is a reasonable design choice given the multi-character tokens, but the paper could briefly discuss whether this choice affects the sensitivity of the metric to meaning-changing vs. meaning-preserving edits.

## Removed Points

- The harsh critic's suggestion that the model does not qualify as studying "LLMs" was kept as a Major weakness (point 1 above) since it is factually correct and substantive. However, the critic's characterization that this "undermines the paper's central contribution claim" and that the paper "should not be accepted" on this basis alone is softened: the paper acknowledges the limitation and the core phenomenon (diversity collapse) is still a valid finding even if the paper should be re-scoped.
- The critic's framing of the single-run issue as fatal was downgraded from Fatal to Major: the consistency across multiple data cycle configurations and λ values provides some cross-validation, though the concern about quantitative precision remains valid.
- The critic's concern about the Levenshtein distance being computed on tokens rather than characters is moved to Nice-to-Haves — the authors already acknowledge the choice (line 125–126) and it is unlikely to affect the overall trends.

## Novel Insights

The reviewer raises a genuinely novel insight that the harsh critic missed: the self-consuming training loop's "increase in correctness" and "decrease in diversity" are very likely the same phenomenon described from two different angles. As the learned distribution collapses, it converges to the simplest correct expression(s), which mechanically causes both correctness to approach 100% and diversity to approach zero. This means that correctness cannot be treated as a separate, independent finding — it is a side-effect of collapse, not a distinct beneficial outcome. The paper would be strengthened by treating correctness and diversity as two views of the same underlying distributional collapse, rather than as separate "quality" and "diversity" dimensions.

## Suggestions

1. **Re-scope the paper.** Change the title from "Large Language Models Suffer From Their Own Output" to something like "A Study of Self-Consuming Training Loops for Neural Language Models on a Controlled Task" or similar. Adjust the abstract and contributions to match the actual scope of evidence.

2. **Add multiple runs.** Even 3–5 random seeds per configuration would provide much-needed variance estimates for the reported percentages and help establish the reliability of the findings.

3. **Analyze the actual generated expressions.** Report what the model generates at key points: the collapsed state (what is that single point?), the expressions during the correctness increase phase (are they trivial or complex?), and how expression length/distribution changes across generations.

4. **Clarify or correct the inevitable-collapse claim.** Either run longer experiments (200+ generations) for the balanced and expanding cycles to determine whether diversity plateaus, or temper the claim to acknowledge that a non-zero plateau is possible.

5. **Clarify validation data composition.** State explicitly whether the 10% validation split uses the same data-cycle distribution as the training set or is always sourced from the original real data.

## Score and Decision

The paper tackles an important and timely problem with a clever experimental design. However, the significant overclaiming in the title/abstract (claiming to study "LLMs" while using a 10.6M-parameter model on a 7-token synthetic grammar), the lack of multiple runs for statistical reliability, and the unanalyzed nature of the "correctness increase" finding collectively weaken the contribution below the acceptance threshold. The paper shows promise and the direction is valuable, but in its current form the claims outpace the evidence.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>