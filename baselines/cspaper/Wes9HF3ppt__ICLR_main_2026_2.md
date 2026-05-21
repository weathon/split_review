---
job_id: 23d9758e-e765-4aa6-a0b7-39fde6b56cff
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Wes9HF3ppt.pdf
paper: Insertion Language Models: Sequence Generation with Arbitrary-Position Insertions
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies generative modeling and sequence modeling for language and planning, with a new insertion-based formulation compared against autoregressive and masked diffusion models.

## Minimum Quality
Pass ✅. The paper contains the essential components expected of a research submission, including abstract, introduction, method, related work, experiments/results, and discussion, and it presents a concrete algorithm with quantitative evaluation, even though several methodological and presentation issues remain.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, concealed instructions, or other manipulative content targeting automated reviewers in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes Insertion Language Models (ILMs), a sequence generation framework that inserts one token at an arbitrary position at each step, allowing variable-length generation in non-left-to-right order. The method is trained with a denoising-style objective based on dropping tokens and predicting a joint distribution over insertion position and token, together with a stopping classifier. Empirically, the paper evaluates ILMs on synthetic planning tasks, Zebra puzzles, unconditional text generation, and arbitrary-length infilling, comparing primarily against autoregressive models (ARMs), masked diffusion models (MDMs), and a variant of the Insertion Transformer.

## Strengths
The paper addresses a real and important limitation of both ARMs and standard MDMs, namely the tension between flexible generation order and variable-length infilling. The motivating examples in the introduction are intuitive, and **Figure 1** does a good job of illustrating the high-level distinction: ARMs support variable length but fixed left-to-right order, MDMs support flexible order but are tied to a fixed number of mask slots, and ILMs aim to combine both. This is a useful framing for the problem.

The core modeling idea is simple and fairly elegant. Predicting a joint distribution over insertion position and token, plus a separate stopping decision, is conceptually cleaner than forcing insertion through a fixed mask layout. The use of a single transformer backbone instead of a more specialized insertion architecture is also practically appealing.

On the synthetic planning side, the empirical results are striking. In **Table 1**, ILM reaches 100.0/100.0/99.1 exact-match accuracy on the three star-graph variants, whereas MDM drops sharply to 36.5 and 21.0 on the variable-length settings, and the standard ARM also fails badly on the hardest case. If these results hold, they support the paper’s central claim that relative-position insertion can be materially better than absolute-position masked denoising for tasks where output structure is not naturally left-to-right and lengths vary.

The paper also includes at least some qualitative evidence for how the model behaves. **Figure 2** is helpful because it concretely shows how the target insertion distribution is constructed from dropped tokens between surviving anchors. This figure makes the intended loss much easier to understand than the surrounding prose alone. Similarly, **Figure 3** is a useful task illustration for the star-graph setup, and **Figure 4** gives a compact but informative example of the zebra-puzzle representation.

The comparison against a decoder-only Insertion Transformer variant is also a useful addition. The paper’s claim that a dedicated stopping classifier matters is at least somewhat supported by the poor IT numbers in **Table 1**.

For unconditional language generation, the paper does not oversell the results against ARMs. In **Table 2**, ILM is generally worse than ARM in Llama-evaluated NLL, but better than MDM, which is a more measured and credible claim than pretending to beat ARMs outright. The same is true in **Figure 5**, where ILM appears consistently stronger than MDM across coherence/consistency/fluency/grammar/redundancy. That comparison supports the paper’s more modest claim that ILMs are competitive and more flexible, not dominant.

The paper also makes an effort to analyze generation quality versus speed. **Figure 6** is one of the more informative experimental figures in the paper, because it moves beyond static benchmark numbers and shows a tradeoff between per-token generation time and NLL for MDM versus ILM. Even though this analysis is incomplete, it is directionally useful.

Finally, the paper is reasonably reproducible at a high level. It provides model sizes, datasets, basic training budgets, and a code link.

## Weaknesses
1. **The training objective is only loosely justified, and the bias introduced by the approximation is not analyzed in a way that supports the main paper’s claims.**  
   The paper explicitly states on **Page 3** that the proposed objective is a “biased training objective” introduced to avoid the high variance of the naive denoising estimator. That is a major methodological move, not a minor engineering detail. However, the main text never really quantifies what distribution is being learned under this approximation, nor when the approximation is expected to be faithful. In **Equation (2)**, the target is not the next-token insertion distribution under a particular reverse process, but a normalized count distribution over all dropped tokens lying between two surviving anchors. This is a quite different object. In other words, if two dropped tokens between anchors must be generated in a particular order for consistency, the loss still treats them as an unordered bag through counts. That may work empirically, but the paper does not explain why this should recover a good sequential insertion policy rather than merely a heuristic. This matters because the paper’s central contribution is precisely the learning objective, and without a clearer account of what is optimized, it is hard to judge the scientific contribution beyond “this heuristic seems to help on a few tasks.”

2. **There are mathematical and notational issues in the core formulation that make the method harder to verify than it should be.**  
   Several equations and definitions are underspecified or inconsistent. In **Equation (2)** on **Page 4**, the summation is written as
   \[
   \frac{1}{n}\sum_{k \in [L-n]} c_{i_k,i_{k+1}}(v;\mathbf{x}) \log p_{\theta,\mathrm{tok}}^{\mathrm{ilm}}(k,v\mid \mathbf{x}[\mathbf{b}]),
   \]
   but the variable \(v\) is free, not summed over. From the surrounding text, it seems the authors intend a sum over both slots \(k\) and vocabulary items \(v\), weighted by counts \(c_{i_k,i_{k+1}}(v;\mathbf{x})\), but that is not what is written. Also, the indexing around the boundaries is unclear: if there are \(L-n\) visible tokens, there are usually \(L-n+1\) insertion slots if one includes both ends, yet the formula and prose fluctuate between “between positions \(k\) and \(k+1\)” and sums over \([L-n]\). This ambiguity matters because end insertions are essential for variable-length generation. The definition
   \[
   c_{i_k,i_{k+1}}(v;\mathbf{x}) = \sum_{j=i_k}^{i_{k+1}-1}\delta(\mathbf{x}^j,v)
   \]
   also appears to include the left anchor token \(i_k\), which seems wrong if the goal is to count tokens strictly between anchors. At minimum, one would expect something like \(j=i_k+1,\dots,i_{k+1}-1\), unless the indexing convention is different and explicitly defined, which it is not.

3. **The MDM baseline description contains what looks like an error, which weakens confidence in the precision of the technical exposition.**  
   On **Page 3**, in the “Limitations of MDMs” paragraph, the unmasking probability is written as
   \[
   P(i) \propto \frac{\alpha_t - \alpha_t}{1-\alpha_t}\delta(x_t^i,m),
   \]
   which simplifies to zero. This is almost certainly a typo, presumably meant to involve two different time indices, but it is not a harmless cosmetic issue because it appears exactly where the paper explains the baseline inference mechanism it is criticizing. If the authors want readers to trust their comparison to MDMs, these details need to be correct and checked carefully.

4. **The relationship between the training objective and repeated tokens is a serious unresolved issue in the main paper, not just an appendix footnote.**  
   In Appendix D, the paper states that when sequences do not repeat tokens, the reverse conditional can match the target insertion distribution \(d(k,v;\mathbf{x}_0,\mathbf{b})\), but when repeated tokens exist, a dynamic-programming alignment is needed to get a closed form. The main method in the paper, however, is applied to natural language where repeated tokens are pervasive. Yet the main text does not explain how this issue is handled in practice, nor whether the loss in **Equation (2)** is exact, approximate, or inconsistent in this regime. This is not a niche corner case. Repeated tokens are ubiquitous in text, and if the training target is only cleanly defined in the no-repeat setting, the paper needs to state much more clearly what is actually implemented and what approximation is used. Right now, the derivational story is incomplete at exactly the point where the paper moves from synthetic tasks to language modeling.

5. **The experimental positioning is too narrow relative to the paper’s claims about general language modeling.**  
   The title and abstract frame ILMs as a fairly general sequence-generation alternative, but the language experiments are limited to medium-sized models and relatively small-scale datasets, LM1B and TinyStories/ROCStories. That is acceptable for an initial study, but then the claims should be scoped more carefully. As written, the paper suggests a broader conclusion about language modeling, while the evidence is really “this works reasonably at 85M scale on two corpora.” There is no comparison to stronger any-order or insertion-style baselines beyond a very limited IT ablation on synthetic tasks. The related work mentions older insertion approaches, but the experiments do not meaningfully test whether the proposed training loss is better than modern insertion-based generation strategies, only that it beats one simplified IT-style implementation and standard MDM/ARM baselines.

6. **The empirical comparison to ARMs and MDMs is not fully balanced, especially on text generation.**  
   On **Pages 7–8**, the paper states that all models are trained for the same number of gradient steps and roughly similar parameter counts, but that does not imply equal compute, equal effective tokens processed, or equal optimization maturity across fundamentally different objectives. The authors themselves acknowledge possible token-efficiency differences. This becomes important in **Table 2**, where ILM trails ARM in NLL on both datasets, and where MDM generates much longer outputs than the training data. If one baseline is operating under a poor stopping regime and another is known to have different scaling properties, the comparison may say as much about hyperparameter maturity as about the underlying model class. The paper needed a stronger tuning-effort statement, more extensive ablations on stopping thresholds and samplers in the main text, or at least multiple compute-normalized comparisons. **Figure 6** is useful, but it is only on Stories, only for MDM vs ILM, and still does not fully close the fairness question.

7. **The language evaluation methodology is weaker than the paper seems to acknowledge.**  
   The primary text-generation metric is per-token NLL under an external Llama model in **Equation (5)** and **Table 2**, complemented by an LLM judge in **Figure 5**. This is not invalid, but it is indirect and brittle. Llama-NLL is not the same as log-likelihood under the data distribution, and it can strongly privilege stylistic similarity to the evaluator. The entropy metric is also quite crude; high or low entropy can reflect many things, including trivial length effects. The paper partly notices this, especially when discussing MDM length inflation, but then still uses these metrics as central evidence. The qualitative examples in the appendix actually reveal substantial failure cases for all models, including ILM. For a paper claiming competitive open-ended generation, the evaluation should be stronger, for example with more direct human evaluation, task-specific quality measures, or at least broader automatic metrics and better controls for generation length.

8. **Some of the paper’s strongest claims are supported mainly by synthetic tasks whose interpretation is still debatable.**  
   The star-graph results in **Table 1** are impressive, but the paper leans heavily on them to argue a broader advantage of insertion over left-to-right and masked denoising. These tasks are indeed diagnostic, but they are also highly structured and can reward the inductive biases the method is designed around. Similarly, the zebra-puzzle result is encouraging, but the gap over ARM is not huge, 90.0 vs 81.2, while ARM with oracle order reaches 91.2. So the picture is more nuanced than “ILM solves planning better.” The synthetic experiments support a targeted claim about order flexibility, not yet a broad conclusion about planning or reasoning writ large.

9. **The parameterization section leaves important implementation details unclear.**  
   In **Section 3.1**, the model is described via a transformer backbone \(f_\theta^{\mathrm{dec}}\) and insertion logits \(s_\theta(k,v\mid \mathbf{x}[\mathbf{b}])\), but the exact representation of insertion slots is not cleanly specified. **Equation (3)** appears to produce insertion logits from token representation \(k\), but insertion happens between tokens, not at token positions. The text says the special `<stp>` token is prepended and the input in **Figure 2** looks like `<stp><s>A C`, yet the boundary conventions, positional encodings for gaps, and mapping from token states to insertion-slot scores remain underexplained. This matters for reproducibility and also for understanding whether the model is truly using relative-position structure in a principled way or simply relying on implicit conventions.

10. **The comparison to the Insertion Transformer is potentially underdeveloped and therefore not entirely persuasive.**  
    The paper uses the IT result in **Table 1** to argue that the dedicated stopping classifier is important. That may be true. But the baseline is a custom “single transformer version of the Insertion Transformer,” and the key differences from the original method are only relegated to the appendix. Since IT is one of the most directly relevant prior families, a clearer and more faithful comparison would be important. Otherwise, it is hard to know whether the poor IT numbers reflect a genuine weakness of the older approach or a mismatch in implementation/training setup.

11. **The paper’s figures are helpful, but some of them also expose unresolved issues.**  
    **Figure 5** shows ILM outperforming MDM on LLM-judge criteria, but it does not include variance bars, sample counts, or statistical uncertainty, so it is impossible to judge whether some apparent gaps are robust or just noise from judge/model sampling. **Figure 6** is directionally interesting, but the axes and legend make it clear that the time comparison is only partial; it omits ARM and does not tell the reader whether wall-clock includes different sequence lengths, stopping behavior, or batching effects. **Figure 7** in the appendix is visually interesting because it suggests ILM often grows the sequence from both ends and leaves the hard junction token for later, but this interpretability nugget is not quantified in the main paper. Right now, the figures are more suggestive than conclusive.

12. **Presentation quality is uneven, with many small but cumulative issues.**  
    There are numerous typos and inconsistencies: “empirical valuation” instead of “evaluation” in the abstract, “The are many variants” on **Page 7**, “join distribution” instead of “joint distribution” on **Page 5**, inconsistent naming between ILM and IFM in Algorithm 2, and dataset/task naming inconsistencies such as `Star_easy`/`Star_small`/`Stareasy`. None of these alone is fatal, but together they make the paper feel insufficiently polished for a top-tier venue and they exacerbate the deeper ambiguities in the equations.

## Questions
1. **Please clarify and correct the exact token loss in Equation (2).**  
   Is the intended objective
   \[
   -\mathbb{E}_{n,\mathbf{b}}\sum_k\sum_v d(k,v;\mathbf{x},\mathbf{b})\log p_\theta(k,v\mid \mathbf{x}[\mathbf{b}])?
   \]
   If so, please state it explicitly and clarify the boundary-slot indexing, including insertions at the beginning and end of the sequence. A precise corrected formula would substantially increase my confidence.

2. **How is the repeated-token issue handled in practice for natural language?**  
   Appendix D suggests the exact reverse conditional is simple only when tokens are unique, and otherwise dynamic programming is needed. Did the implemented language-model objective actually use such a DP alignment, or did it directly use count-based targets as in Equation (2)? If the latter, what exactly is the probabilistic interpretation? This is a central question for soundness.

3. **Can the authors provide a clearer derivational connection between the approximate objective and the intended reverse process?**  
   Even a proposition describing when the approximation is exact, when it is biased, and what kind of sequential insertion policy it encourages would help a lot. Right now the paper jumps rather quickly from “naive estimator has high variance” to “we use normalized counts,” which feels too abrupt.

4. **How sensitive are the text-generation results to the stopping threshold \(\tau\), top-\(k\) for position sampling, and nucleus settings for token sampling?**  
   The appendix has some sampling analysis, but the main-text conclusions about ILM being competitive with ARM and stronger than MDM depend quite a bit on generation hyperparameters. A more systematic summary in the rebuttal would be helpful.

5. **Can the authors better justify the fairness of the ARM/MDM/ILM comparison in terms of compute and tuning effort?**  
   For example, how many hyperparameter sweeps were run for each model family, and were stopping/length-control hyperparameters optimized on a validation set equivalently? Clarifying this could change my view of how much to read into Table 2 and Table 3.

6. **Why is the IT baseline only evaluated on the synthetic tasks and not on text generation or infilling?**  
   Since insertion-based generation is one of the closest prior directions, even a small-scale text comparison would strengthen the paper’s positioning.

7. **For Figure 5 and Table 2, please report the number of generated samples and some measure of uncertainty.**  
   Confidence intervals, bootstrap intervals, or repeated generations with different seeds would make the claims more convincing.

8. **Can the authors quantify the qualitative generation-order behavior suggested by Figure 7?**  
   The figure indicates that ILM may learn a nontrivial strategy, often inserting easier endpoint tokens first and harder linking tokens later. If that pattern can be summarized statistically, it would strengthen the central argument that the model benefits from arbitrary insertion order rather than merely from a different parameterization.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work studies generic sequence generation and planning-style tasks, uses standard language datasets, and does not introduce an obviously high-risk deployment setting in the main submission.

## Soundness Rating
2: fair. The empirical results are interesting and some claims are supported, especially on the synthetic tasks, but the central training objective is not specified or justified cleanly enough, and the treatment of repeated tokens and insertion-slot indexing leaves important technical gaps.

## Presentation Rating
2: fair. The paper is readable at a high level and several figures are helpful, but the exposition has too many notation issues, typos, and underspecified equations for a paper whose main contribution is methodological.

## Contribution Rating
2: fair. The problem is worthwhile and the insertion-based perspective is potentially useful, but the novelty is somewhat constrained by prior insertion-generation literature, and the evidence for broad language-modeling impact is not yet strong enough for a higher score.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a good idea and some strong synthetic-task results, but for the main ICLR track I think the current version falls short because the key objective is not specified and justified rigorously enough, the experimental positioning in language modeling is narrower than the framing suggests, and there are too many unresolved technical details in the main text. With a cleaner formulation, stronger baseline coverage, and better analysis of the approximation and repeated-token setting, this could become a much stronger submission.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I am familiar with the surrounding literature on sequence generation, diffusion-style text models, and insertion-based methods, and I checked the main equations and experimental claims carefully, but some implementation details remain unclear from the paper.