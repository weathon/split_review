---
job_id: e5b5da37-796d-419d-92d2-cc00989edc5e
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: JjJzbMDGsx.pdf
paper: Language Confusion Gate: Language-Aware Decoding Through Model Self-Distillation
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies a decoding-time intervention for multilingual LLM generation, touching representation use, inference-time control, and safety/reliability in language models.

## Minimum Quality
Pass ✅. The submission contains the required scientific components, including Abstract, Introduction, Related Work, Method, Experiments, quantitative results, and Discussion/Conclusion, and it presents a coherent empirical study with enough detail to support review, even though several methodological clarifications are still needed.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-directed instructions, or other signs of manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies language confusion in multilingual LLM decoding, meaning unintended switching into the wrong script or language family during generation, and proposes the Language Confusion Gate (LCG), a lightweight decoding-time module that predicts allowed language families from the model hidden state and masks disallowed tokens only when intervention is deemed necessary. The gate is trained using self-distillation from the frozen base model, with a norm-adjusted variant motivated by an analysis of output embedding norm imbalance across language families. Experiments on several open models and some commercial systems suggest that LCG substantially reduces Chinese/Japanese and Latin-script confusion while largely preserving task performance and some legitimate code-switching behavior.

## Strengths
The paper tackles a real and under-discussed failure mode of multilingual LLMs. The practical motivation is easy to appreciate, and the proposed solution is deployment-friendly because it does not require modifying or retraining the base LLM. This matters, since many practitioners can realistically add a small decoding-time module but cannot afford model-level finetuning.

The core intervention is simple and reasonably well aligned with the empirical observations in Section 3. In particular, the claim in Section 3.1 that correct-language tokens are often still near the top of the distribution makes a masking-based decoding intervention plausible rather than arbitrary.

I found the mechanistic angle in Section 3.2 interesting and potentially useful. The decomposition
\[
\text{logit}_i = h \cdot e_i = \|h\|\,\|e_i\|\,\cos(h,e_i)
\]
is elementary, but the paper uses it effectively to motivate a debiasing view of high-norm output embeddings. The adjusted logit
\[
\text{logit}_{\text{adj},i} = \frac{h\cdot e_i}{\|e_i\|}
\]
is also easy to implement and gives an intuitive training signal for the gate. This is not a deep theorem, but it is a neat bridge between analysis and method.

**Figure 2** is one of the stronger pieces of evidence in the paper. It concretely shows that after norm adjustment, several high-ranked confusion tokens drop out of the top candidates and same-language tokens move up. Even though this is just a case study, it supports the paper’s training intuition better than the text alone.

The empirical section is broad in terms of model coverage. **Table 3** includes multiple families, Qwen, Llama, and Gemma, and the confusion reductions are large enough to be hard to dismiss as noise. For example, Qwen3-8B Latin confusion drops from 12.1% to 2.0%, and Qwen3-30B CJ confusion goes from 1.0% to 0.0%, while BLEU is essentially flat. That is the kind of tradeoff that makes a decoding-time method interesting.

The paper also does a useful ablation between LCG-unadjusted and LCG-adjusted in **Table 3**. The adjusted version is consistently better on confusion metrics and usually neutral on task metrics, which gives some support to the norm-adjustment story instead of treating it as decorative analysis.

I also appreciate that the authors did not only evaluate on translation. The inclusion of INCLUDE and Humaneval-XL broadens the case that the effect is not confined to one benchmark type. In **Table 4**, the method reduces CJ confusion on reasoning/code-generation setups while only mildly affecting pass rates. This is important because a lot of decoding interventions look good on translation and then quietly damage more open-ended reasoning behavior.

The paper is generally readable, and **Figure 1** does a good job summarizing the pipeline. The left-right comparison makes the intended behavior of the gate immediately clear, and the diagram is more helpful than many architecture figures in this space.

## Weaknesses
1. **The central notion of “language confusion” is only partially operationalized, and the evaluation is narrower than the paper’s broader claims.**  
   The method predicts only four broad token families, CJ, Latin, Symbols, and Low-Res, as described in Section 4.1 on Pages 5 to 6. The paper itself acknowledges in Section 6 that this script-level granularity cannot resolve confusion within the same script, such as English vs Spanish. That limitation is not cosmetic, it cuts directly into the scope of the claimed problem. A method that cannot distinguish same-script language confusion addresses only a subset of multilingual confusion, mostly cross-script intrusions. This should be framed more explicitly throughout the paper, including in the Introduction and Abstract, rather than only at the end as a limitation.

2. **The self-distillation target is heuristic and may encode the base model’s own mistakes in a way that is not fully justified.**  
   In Section 4.2, the pseudo-label is
   \[
   y_{t,i}^{*}=\mathbf{1}\big[S_{k,p}(\mathbf{logits}_{\text{adjust}})\cap\mathcal{F}_i\neq\emptyset\big].
   \]
   This means a family is labeled “allowed” if any token from that family survives top-\(k\)/top-\(p\) filtering after norm adjustment. There are at least two issues here. First, the target depends strongly on the arbitrary choice of \(k\) and \(p\), but the paper does not explain what values are used during training, whether they match inference, or how sensitive training is to them. Second, “presence in candidate set” is a very weak criterion. A single marginal token from a family makes the whole family positive, which seems especially loose for a 4-label classifier. This matters because it can produce high-recall/low-precision supervision and may be one reason the rules in Section 4.3 are needed to rescue behavior. I would have liked a stronger justification or an ablation on alternative targets, for example using cumulative family probability, thresholded family mass, or top-rank constraints.

3. **The mathematical formulation of norm adjustment is intuitive but not fully cleanly specified, and the paper overstates what it explains.**  
   Section 3.2 says that dividing logits by embedding norm “removes the embedding norm bias,” but this is only true relative to the multiplicative decomposition in a per-token ranking sense. It does not mean the resulting adjusted logits are calibrated probabilities, and the transformation changes the geometry of the decoder scoring in a nontrivial way. Also, on Page 4 the notation is inconsistent, with \(\cos_{-}\mathrm{sim}(h,e_i)\) seemingly a typo for cosine similarity. More importantly, the paper says norm bias “creates a systemic bias” and “sometimes causes language confusion,” but the evidence in **Table 1** is only correlational. The percentages of top-5%-norm tokens by family are suggestive, not causal. The discussion would be more convincing if the paper were more careful in separating “consistent with” from “explains.”

4. **The intervention rules are doing a fair amount of work, but their effects are not isolated clearly enough in the main paper.**  
   Section 4.3 contains three nontrivial rules: never mask Symbols/Low-Res, defer when gate prediction is contradicted by high-confidence model output, and always allow persistence of the previous non-symbol token’s language. These are not minor implementation details, they shape the semantics of the method. In fact, the persistence rule seems especially powerful for preventing catastrophic disruption. Yet the main paper gives only a passing sentence near the end of Section 5.3 that “No Rule” was ablated in Figure 3, without enough detail. **Figure 3** visually suggests the rules matter, but the exact numbers, the full setup, and whether the gain comes from the gate itself or the hand-crafted rules are not made explicit. If the method’s effectiveness relies substantially on these rules, that should be quantified more directly in a table.

5. **The code-switching evaluation is informative but still weak relative to the paper’s claims about preserving natural multilingual behavior.**  
   The paper repeatedly emphasizes the distinction between harmful confusion and legitimate code-switching, which is a key selling point. However, the evidence in Section 5.3 is mixed. On one hand, the token-level permission result of 86.7% sounds encouraging. On the other hand, **Table 5** shows substantial drops in observed code-switch rate after LCG, for example Qwen3-8B from 46.34% to 25.90%. The paper interprets this as acceptable because the rate is still above Claude Sonnet 4 and not much lower than the answer rate, but this is a fairly indirect argument. Higher or lower code-switch rate is not itself a quality metric. The stronger test would be judged adequacy of responses in contexts where code-switching is necessary. As written, the paper demonstrates that the method does not eliminate all code-switching, but it does not convincingly establish that it preserves it well.

6. **Some result reporting lacks uncertainty estimates or significance analysis, making it hard to judge whether small changes in task performance are meaningful.**  
   This is especially relevant in **Table 3** and **Table 4**, where the performance differences are often small. For example, INCLUDE accuracy moves from 71.12 to 70.83 for Qwen3-30B, and Humaneval Pass@1 for GPT-Oss drops from 85.88 to 84.56. These could be noise, or they could reflect a real cost. The paper often interprets such changes as “maintaining” performance, but without confidence intervals, repeated seeds, or at least per-benchmark variance, that conclusion is softer than the text suggests.

7. **The baseline comparison is useful but not entirely satisfying, especially for the training-based baseline.**  
   Section 5.3 compares against ICL, greedy decoding, and ORPO. This is a sensible start, but the ORPO baseline is described only briefly: “we prepare a multilingual dataset, and synthesize samples with language confusion as rejected samples similar as Lee et al. (2025).” That leaves many degrees of freedom unspecified, and it is difficult to assess whether ORPO was tuned competitively. Since one of the paper’s claims is practical superiority to retraining-based methods, a stronger and more transparent baseline section would help.

8. **The evaluation of commercial LLMs in Table 2 is interesting context, but it is not fully integrated into the scientific argument.**  
   **Table 2** demonstrates that confusion exists in strong proprietary systems, which helps motivate the problem. However, the BLEU scores vary widely across systems, and the table is used mostly rhetorically. It does not inform the effectiveness of LCG directly, since the method is not applied to these models. This is not a fatal issue, but some of the Introduction framing leans on it more heavily than the paper’s actual contribution warrants.

9. **The paper would benefit from sharper positioning relative to evaluation work on language confusion.**  
   The related work cites Marchisio et al. (2024) and several mitigation papers, but the evaluation discussion in Section 5.2 mainly justifies not using LCB. There is less engagement with alternative confusion metrics or broader typological analyses of language confusion. Since the paper’s main empirical claim is mitigation quality, stronger positioning against existing evaluation methodology would improve confidence that the chosen metrics are not overly favorable to this specific intervention.

10. **There are several presentation and notation issues that are not catastrophic, but they do reduce precision.**  
   A few examples: “Related Works” should be “Related Work”; “Language Confusion V.S. Natural Language Mix” is awkwardly phrased; the caption of **Table 4** says “No-Think” models although the text says Humaneval-XL is used for thinking models; Page 6 says “we refer the gate” where “refer to the gate” is intended; Section 3.2 includes notational glitches. None of this kills the paper, but the method is simple enough that sloppiness in the formal description stands out more.

11. **Some claims are stronger than the evidence in the main paper supports.**  
   For example, the Abstract says the method decreases confusion “without negatively impacting task performance.” That is too categorical given **Table 4**, where Pass@1 drops modestly for all three thinking models, and given some small degradations elsewhere. A more accurate statement would be that performance is usually preserved or only mildly affected. This may sound pedantic, but for a decoding-time constraint method, the cost-benefit tradeoff is the whole game.

## Questions
1. In Section 4.2, what exact \(k\) and \(p\) values are used to construct \(S_{k,p}(\mathbf{logits}_{\text{adjust}})\) during training? Are they fixed across all models and tasks, and how sensitive are the results to this choice? A small ablation here could materially increase my confidence.

2. Could the authors report a more explicit ablation separating:  
   (a) gate only,  
   (b) rules only, and  
   (c) gate + rules,  
   with exact numbers in a table for at least one representative model? The current presentation, especially around **Figure 3**, suggests both matter, but it is hard to tell how much each contributes.

3. For the pseudo-label construction, did the authors try stronger targets than family presence in the norm-adjusted candidate set, such as thresholding by family probability mass or using the top-1/top-3 family after adjustment? If not, can they explain why the current binary construction is preferred?

4. For **Table 3** and **Table 4**, can the authors provide variance estimates, repeated runs, or confidence intervals for the task metrics? This is particularly important for small changes in BLEU, accuracy, and Pass@1.

5. The code-switching results in **Table 5** are somewhat ambiguous. Can the authors provide a human evaluation, even on a modest sample, of adequacy in contexts where code-switching is genuinely required? That would strengthen the claim that LCG preserves useful code-switching rather than merely leaving some Latin tokens unmasked.

6. The persistence rule in Section 4.3 seems important. Can the authors clarify whether it theoretically guarantees only that LCG does not suppress continuation in the same family, or whether it also prevents some classes of false interventions? The claim in Appendix J that LCG cannot increase confusion is strong and would benefit from a crisper formal argument in the main paper.

7. Since the method only uses four language families, how much of the observed residual Latin confusion on FLORES-NO-LATIN is due to same-family ambiguity versus gate misses? A short error analysis would help clarify the headroom and limitations.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond standard considerations for multilingual LLM deployment. The work is primarily about reducing unintended language mixing and improving reliability. I do not see a paper-specific ethics issue that requires escalation based on the presented content.

## Soundness Rating
3: good. The method is technically plausible, the experiments are substantial, and the main empirical claims are mostly supported, but several parts of the training target, rule interactions, and performance tradeoff analysis need tighter justification.

## Presentation Rating
3: good. The paper is generally readable and the main idea is communicated clearly, with helpful figures such as **Figure 1** and **Figure 2**, but there are notable imprecisions in notation, some overstated claims, and a few inconsistencies in tables/captions.

## Contribution Rating
3: good. This is a useful and practically relevant decoding-time intervention for an important multilingual failure mode, with broad empirical evidence. The contribution is meaningful, though somewhat limited by the coarse script-family formulation and incomplete validation of the code-switching claims.

## Overall Rating
8: Accept, good paper (poster). The paper presents a practical and empirically effective intervention for a real multilingual generation problem, and the improvements in confusion rates across models are substantial enough to matter. I do have meaningful reservations, especially about the coarse family granularity, the heuristic supervision target, and the still-limited evidence on preserving legitimate code-switching, but overall the strengths clearly outweigh the weaknesses and the work is worth sharing with the ICLR community.

## Reviewer Confidence
4: confident. I am familiar with multilingual LLM evaluation and decoding-time interventions, and I checked the main technical details and empirical claims carefully, though some implementation specifics would still benefit from author clarification.