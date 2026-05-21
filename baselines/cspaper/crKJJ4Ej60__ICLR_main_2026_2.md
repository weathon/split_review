---
job_id: 37cd4dd8-70f7-4a0b-b9a9-f9dd25af55e4
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: crKJJ4Ej60.pdf
paper: Copy-Paste to Mitigate Large Language Model Hallucinations
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, focusing on LAG/RAG faithfulness, preference optimization, decoding behavior, and interpretability for large language models.

## Minimum Quality
Pass ✅ The paper contains the expected scientific structure, including Abstract, Introduction, Methodology, Experiments, quantitative results, Related Work, and Conclusion. While there are several technical and presentation issues, the submission clears the minimum bar for a full review rather than a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find evidence of hidden prompts, reviewer-targeted instructions, or other manipulative content in the paper text.

# Expected Review Outcome:
## Summary
The paper studies contextual faithfulness in retrieval-augmented generation and argues that higher lexical copying from the provided context is associated with fewer hallucinations. Based on this observation, the authors propose a two-stage framework: first generating high-copying responses with several prompting strategies, then training a model called CopyPasteLLM via preference optimization on automatically constructed preference pairs. The paper also introduces a token-level analysis tool, Context-Parameter Copying Capturing, to probe contextual versus parametric knowledge usage during generation.

## Strengths
The main strength is that the paper pushes a very simple idea to its logical extreme and tests it seriously rather than treating it as a throwaway heuristic. The framing is memorable and operationally clear: if contextual faithfulness is the goal, then forcing stronger reuse of the context is a plausible lever.

The empirical headline results are strong. In **Table 1** on counterfactual settings, CopyPasteLLM substantially outperforms the listed baselines on FaithEval for all three reported base models, despite using far fewer training examples. Even allowing for some caveats about supervision richness, the gain magnitude is large enough that it is hard to dismiss as noise. **Table 3** also shows that the method does not collapse in non-counterfactual settings, which is important because a faithfulness method that only works on synthetic conflict settings would be much less convincing.

I found the overall pipeline easy to follow from **Figure 2**. The stage decomposition, high-copying candidate generation followed by preference construction and DPO training, is one of the clearer parts of the paper. The figure helps explain how the authors move from prompting to training, and why the training data are not just raw QA pairs but filtered and ranked behavioral trajectories.

The motivating observation in **Figure 1** is useful. It does not prove the central claim, but it gives a concrete empirical reason for exploring the copy-paste hypothesis. I also appreciate that the figure is not merely decorative; it directly motivates the method.

The paper is broad in evaluation. It covers prompt-only behavior, trained models, counterfactual and non-counterfactual settings, and some interpretability analysis. Even though I have reservations about several details, the authors clearly made a real effort to examine the phenomenon from multiple angles.

The interpretability section is imperfect, but the attempt is valuable. In particular, **Figure 3** goes beyond final-answer evaluation and tries to study positional changes in contextual versus parametric preference during generation. That is a more interesting direction than yet another aggregate faithfulness score.

## Weaknesses
1. **The central claim is built on correlation, but the paper often writes as if it had established causation.**  
   The key motivation comes from **Figure 1** on **Page 2**, where higher copy coverage/density is associated with lower hallucination density on RAGTruth. This is suggestive, not causal. Models that copy more may differ in many other ways, including prompt following, answer length, verbosity, or baseline faithfulness. The paper then elevates this observation into a much stronger claim that high-copying behavior "fosters genuine contextual belief" and that lexical copying is an "operational proxy" for contextual faithfulness. That is a much bigger leap than the evidence supports. A stronger paper would isolate copying as the variable, for example by controlling answer length, model family, or retrieval quality, or by comparing copy-heavy and copy-light responses matched on faithfulness metrics. As written, the paper's main conceptual bridge is shakier than the confident prose suggests.

2. **The paper overstates what lexical copying can guarantee, and the task formulation is too optimistic.**  
   In **Section 2.1, Page 3**, the task is framed as maximizing lexical reuse from context to "ensure" high contextual faithfulness and minimize hallucination. That is too strong. Copying can still produce irrelevant answers, omit necessary synthesis, or select the wrong evidence span. Exact copying is neither necessary nor sufficient for faithfulness in many QA settings. This matters because the method is sold not just as a useful bias, but almost as a principled solution to attribution and faithfulness. The "Balance" paragraph acknowledges query relevance and fluency, but those factors are not tightly integrated into the actual training objective. They mainly enter via filtering heuristics, not via a clearly defined optimization criterion.

3. **The answer-stamping design is a major confound, and the paper's own ablation suggests that much of the gain may come from this label injection rather than from copy-paste behavior itself.**  
   In **Section 3.2, Page 5**, when gold answers are available, the authors append the correct answer to the top candidate and append incorrect answers to other candidates. This is an unusually strong intervention. It is not just preference learning over better reasoning traces; it directly manufactures chosen and rejected completions with explicit correct versus wrong endings. Then in **Figure 12** and **Appendix G, Pages 24-25**, the authors show that removing answer stamping causes a drastic drop. That is informative, but it also weakens the paper's central story. If stamping is essential, then the gains may reflect conclusion supervision much more than internalization of contextual trust. I would have liked a much more careful separation of: (i) copying signal, (ii) preference ranking signal, and (iii) explicit answer-label signal.

4. **The comparison around data efficiency is not apples-to-apples.**  
   The paper repeatedly emphasizes that CopyPasteLLM uses only **365 training samples**, versus much larger counts for Context-DPO, Canoe, and ParamMute, especially in **Table 1** and the surrounding discussion on **Pages 6-7**. But each of these 365 samples is expanded into multiple generated candidates, filtered with several metrics, judged in tournaments, and in many cases stamped with gold or wrong answers. That is a rich supervision pipeline. So the "50x smaller" message is directionally interesting but methodologically slippery. A fairer comparison would normalize not only the number of raw QA instances but the amount of supervision derived per instance, or at least report the total number of preference pairs and the amount of teacher-model inference used to produce them.

5. **Several tables are difficult to trust because of formatting or metric inconsistencies, especially Table 2.**  
   **Table 2 on Page 6** is the weakest part of the empirical presentation. First, the method names are inconsistent: the text discusses CP-Link and CP-Refine, but the table shows "C-Point" and "CP-Reline", which looks like either formatting corruption or naming mistakes. More seriously, the metric layout is confusing enough that some values appear implausible. For example, numbers such as 1513.7 or 330.8 appear under headers that seem to correspond to faithfulness subcolumns or adjacent metrics, and the table-text explanation does not fully resolve what those numbers mean. The main text then makes detailed claims like "best in 3/4 models, 14/24 top scores", but given the table's formatting issues it is hard to verify these statements. This matters because Stage 1 is a foundational part of the method, and right now the evidence for that stage is much less readable than it should be.

6. **There are multiple algorithmic and mathematical inconsistencies that hurt confidence in the technical rigor.**  
   A few examples:
   - In **Algorithm 1, Page 18**, the loop condition for CP-Refine is `while t < T_max or sigma^{(t)} < theta_sigma`. With an `or`, the loop continues whenever either condition holds, which is not the usual stopping logic for bounded iterative refinement. I suspect the intended condition is `and`, or an equivalent break-based formulation. As written, the logic is wrong or at least misleading.
   - In **Algorithm 2, Page 19**, notation is inconsistent: \(r_i^{\mathrm{descr}}\) is defined on line 11, but line 13 uses \(r_i^{\mathrm{down}}\), which is undefined. The DPO tuple notation also shifts between \((x, y_x, y_t)\) and \(y_w, y_t\). These are not fatal alone, but they indicate the algorithm was not carefully checked.
   - In **Algorithm 3, Page 26**, the variable naming appears broken. The loop uses `for m in M`, but the context length was already denoted by \(m\), and the condition on line 6, `m + ell < m`, is clearly invalid under that reuse. This is more than a typo because it makes the pseudocode nonsensical.
   - In **Equation (8), Page 27**, the "logits power" definition,  
     \[
     \operatorname{logits\_power}=\left(\sum_{i=1}^n \ell_i^2\right)\sqrt{n},
     \]
     is introduced without real justification. Why square logits, then multiply by \(\sqrt{n}\)? Why is this a meaningful measure of contextual or parametric reliance rather than simply a scale-dependent aggregation? The interpretability claims depend on this quantity, so the arbitrariness matters.

7. **The interpretability claims are overinterpreted relative to what the probing method actually identifies.**  
   In **Section 3.3, Page 5**, contextual knowledge is approximated by tokens appearing in the context, and parametric knowledge by tokens preferred in a no-context run. This is a very coarse proxy. Common tokens, discourse markers, and overlap between context and general language priors make this categorization noisy. Yet the later analysis on **Pages 8-9**, especially the interpretation of **Figure 4**, draws strong conclusions such as "selective parametric knowledge suppression" and "recalibrating internal confidence in parametric knowledge." I do not think **Figure 4** supports that level of mechanistic interpretation. UMAP separation is at best suggestive. It is useful as exploratory analysis, but the prose presents it too confidently as evidence of the underlying mechanism.

8. **The empirical comparison set is selective in ways that favor the paper's narrative.**  
   For Stage 1, the baselines in **Table 2** are mainly Attributed and Citations, which are fairly weak prompt-based comparators. Yet the paper's claims are broader, positioning Copy-Paste against prompting, decoding, and fine-tuning families. Stronger faithfulness-oriented prompting or decoding baselines are mostly deferred to Stage 2 or not included in that specific analysis. Similarly, because the method is explicitly copy-driven, I would have expected more direct comparisons with stronger constrained-decoding or retrieval-head-based methods in the prompt-only setting. The present setup makes the Stage 1 win look cleaner than it may actually be.

9. **Heavy reliance on LLM-as-judge enters at multiple critical points, but its reliability is not convincingly established in the main paper.**  
   The pipeline uses model-based judging for filtering and Elo-style ranking in **Section 3.2, Page 5**, and hallucination evaluation in **Appendix B, Page 16**. That is a lot of delegated supervision. The paper cites prior work on judging, but there is little in the main paper to show that the judge is stable or aligned for this specific task. Since the method's preference labels depend heavily on this ranking, judge noise could directly shape the learned policy.

10. **The presentation quality is uneven, with several avoidable errors that make a careful read harder than necessary.**  
    There are many typos and naming inconsistencies, for example "CP-Reline" versus CP-Refine, "ParamMute" versus "ParamMate" in different places, and formatting corruption in **Appendix L.3, Page 32** where the judge output template is partially unreadable. The references around **Pages 11-15** also contain some corrupted entries. None of this invalidates the experiments, but it does lower confidence because the paper asks the reader to trust a fairly intricate pipeline while presenting several parts sloppily.

## Questions
1. The biggest issue for me is the role of answer stamping. Can the authors provide a cleaner experiment that separates the effect of high-copying preference data from the effect of appending gold versus wrong answers? For example, what happens if the chosen/rejected responses differ only in reasoning trace quality and copying degree, with no explicit answer stamping at all?

2. Can the authors clarify the exact logic of **Algorithm 1**? As written, the loop condition uses `or`, which seems incorrect. Please specify the intended stopping condition and whether the implementation matches the pseudocode.

3. Please clean up and re-present **Table 2**. At the moment the metric columns, method names, and several values are difficult to interpret. In particular, what exactly are the large numbers around 1400-1600 measuring, and where is CP-Link in the table if the text later discusses its performance extensively?

4. For the data-efficiency claim, could the authors report the total number of final preference pairs, the number of teacher-generated candidates per raw sample, and the total amount of answer supervision injected through stamping? That would make the comparison to methods trained on 10k-30k raw examples more transparent.

5. The contextual versus parametric probing in **Section 3.3** seems heuristic. Can the authors provide robustness checks showing that the conclusions in **Figures 3 and 4** do not materially change under alternative token-source definitions, different \(K\), or stronger filtering of common tokens?

6. Since **Figure 1** is central to the motivation, can the authors provide a controlled analysis showing whether the copy-faithfulness relationship still holds after controlling for answer length, model family, and prompt type? That would make the causal story much more convincing.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper discusses deployment in medical and other high-stakes domains, and the ethics statement appropriately notes that copying can also reproduce biased or incorrect source content. These are important considerations, but they are already acknowledged and do not rise, in my view, to the level requiring a separate ethics review.

## Soundness Rating
2: fair. The empirical results are promising and likely reflect a real effect, but several methodological confounds, unclear tables, and algorithmic inconsistencies weaken confidence in the strength of the central claims.

## Presentation Rating
2: fair. The core idea is understandable and some figures, especially **Figure 2**, communicate well, but multiple typos, notation issues, broken pseudocode, and the hard-to-parse **Table 2** materially hurt the presentation.

## Contribution Rating
3: good. Despite my reservations, the paper advances an interesting and useful direction for contextual faithfulness, and the results are strong enough that the broader idea is worth sharing with the community.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The empirical gains and the clarity of the high-level idea push this above the line for me, but only narrowly. The paper would be substantially stronger with cleaner evidence isolating the effect of copying, a much more careful treatment of answer stamping, and a pass to fix the mathematical and presentation issues.

## Reviewer Confidence
4: confident. I am familiar with the contextual faithfulness / RAG hallucination literature and checked the main claims, tables, figures, and equations carefully, though some empirical implementation details remain difficult to verify from the paper alone.