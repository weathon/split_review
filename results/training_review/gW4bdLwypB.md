Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper investigates three multi-objective optimization (MOO) formulations — single-level (VS-ASR), bilevel/constrained (VC-ASR), and multilevel (VM-ASR) — for training multilingual multi-task ASR models that jointly perform ASR and speech-to-text translation. The core finding is that separating highly conflicting objectives (self-supervised, ASR, S2TT) into hierarchical optimization levels (VM-ASR) outperforms single-level and bilevel approaches, with average improvements of 5.6% WER reduction and 5.9% BLEU gain over VC-ASR on the CoVoST 2 dataset.

## Strengths

1. **The paper addresses a genuine and practically important problem**: conflicting gradients in multilingual multi-task ASR training are a known obstacle, and studying which MOO formulation is most suitable is a well-motivated research question. The experimental design covers two model sizes (100M and 58M) and multiple languages (5 for ASR, 4 for S2TT) on CoVoST 2.

2. **VM-ASR consistently shows the best or tied-best performance across nearly all language/task combinations in the main tables.** For the 100M model, VM-ASR (USA) achieves the lowest WER on all five ASR languages and the highest BLEU on all four S2TT language pairs, with "up to" 22.3% WER improvement and 27.9% BLEU improvement over baselines at the best individual cell. The average improvements over the Joint PT+FT W/O MOO baseline (3.8% WER, 4.8% BLEU for VC-ASR; 5.6% WER, 5.9% BLEU for VM-ASR over VC-ASR) suggest a consistent directional benefit.

3. **Transparent reporting of computational overhead.** The paper quantifies the additional cost of MOO methods (11.6 GB vs 8.7 GB GPU memory; ~2.8 vs ~2.25 hours per epoch), which helps practitioners assess the trade-off.

4. **Penalty parameter analysis provides a practical insight.** The comparison of two penalty increase rates (0.002 vs 0.02 per epoch) in Tables 3 and 4 shows that slower increase benefits performance, an actionable finding for practitioners using penalty-based multilevel optimization.

## Weaknesses

### Fatal
None.

### Major

1. **The three "formulations" reduce to nearly the same algorithmic procedure, and the connection between the theoretical formulations and implemented updates is not explained.** The paper presents VS-ASR (single-level vector optimization), VC-ASR (constrained optimization with threshold ε), and VM-ASR (nested hierarchical optimization) as distinct methods. However, the update rules (Eqs. 6–8) are all weighted-sum gradient descents differing only in which terms receive fixed penalty coefficients vs. dynamic MoDo weights. The constraint threshold ε from VC-ASR (Eq. 2) never appears in the algorithm (Eq. 7); instead, a penalty parameter η is used. Similarly, VM-ASR's nested hierarchical structure (Eq. 3) is implemented as a single weighted combination with two scalar penalty parameters (Eq. 8). The paper does not explain how the penalty method approximates the constrained/nested formulation, nor does it justify that the specific weight assignments (which loss gets which λ/η) are theoretically grounded rather than heuristic. This gap between the claimed theoretical formulations and the actual algorithms undermines the paper's framing of a "structural" methodological contribution — the novelty lies more in the empirical comparison of weighting schemes than in distinct optimization frameworks.

2. **The MoDo algorithm (Chen et al., 2023), which provides the dynamic λ weights central to all three methods, is never described.** The paper states only that λ weights are "computed using the MoDo algorithm" (line 122) and provides no explanation of how MoDo works, what objective it optimizes, or how it relates to standard MOO approaches (e.g., MGDA, PCGrad, uncertainty weighting). Since dynamic weighting is the key differentiator between the proposed methods and the "Joint PT+FT W/O MOO" baseline, the method is critically underspecified. A reader cannot understand, replicate, or assess the core algorithmic contribution without consulting an external paper.

3. **Finding F3 ("Task-based hierarchy outperforms language-based hierarchy") is claimed without any supporting quantitative comparison.** The paper mentions language-based MLO involving English (LibriSpeech) and Chinese (AISHELL) in Remark 1 (line 112), but no results are shown — no table, no figure, no numbers. F3 is a central finding that directly supports the paper's recommendation for task-based VM-ASR. Making this claim without evidence is a significant gap.

4. **No direct measurement of gradient conflict is provided to support Finding F1.** The paper claims "MOO methods mitigate gradient conflicts in PT and FT" (F1), and references Figure 3 as an "illustration of gradient conflicts" (F3). But no quantitative gradient conflict metric is reported (e.g., cosine similarity between task gradients, gradient magnitude ratios, or number of conflicting gradient pairs). The claim rests entirely on downstream task performance, which conflates gradient conflict mitigation with other possible explanations for improvement.

5. **Baselines are insufficiently specified.** "Static Weight" (Gong et al., 2022) — what weight value(s) were used, and how were they selected? "PEFT" — which parameter-efficient fine-tuning method (adapters, LoRA, prefix tuning)? "Joint PT+FT W/O MOO" (Saif et al., 2024) — what static weighting does it use? Without these details, the comparison cannot be properly interpreted or reproduced, and the claimed superiority over "static weighting" is ambiguous.

6. **No measures of variance or statistical significance are reported for any result.** Tables 1–4 present single numbers per condition. Given that many differences between methods are small (0.1–0.5 WER/BLEU) and results likely vary across random seeds, it is impossible to assess whether the observed improvements are statistically reliable. For a paper whose central claims rest on performance comparisons, this is a serious omission.

### Minor

1. **The "up to XX%" claims emphasize best-case language/task pairs, while average improvements are substantially smaller.** The paper reports "up to 22.3%/27.9%" improvements, but the average gains over Joint PT+FT W/O MOO are 3.8% (WER) and 4.8% (BLEU) for VC-ASR, and the improvements of VM-ASR over VC-ASR average 5.6%/5.9%. The headline numbers are not representative of typical gains.

2. **The penalty parameter study (Tables 3, 4) tests only two increase rates (0.002 and 0.02 per epoch).** Most differences are within 0.1–0.3 WER / 0.1–0.5 BLEU. The claim that "well-calibrated penalty parameters improve overall ASR and S2TT performance by 8.3% and 2.2%" uses relative percentages on specific entries, and a broader sweep would be needed to establish robustness.

3. **The gap between the theoretical formulations and the implemented algorithms (Major point #1) also affects clarity of contribution.** The paper's title and framing use "Objective Soups" and "recipes," but this terminology appears only in the title and abstract and is never connected to the technical content or to "rewarded soups" (Rame et al., 2024) beyond a brief mention. The terminology adds little.

### Trivial
None.

## Nice-to-Haves

- A direct comparison of MoDo-based dynamic weighting to simpler alternatives (e.g., uncertainty weighting, MGDA, or random scheduling) would help isolate the source of improvement.
- Including gradient conflict measurements (cosine similarity between task gradients during training) would strengthen the support for Finding F1.
- Reporting results with standard deviations across multiple seeds would address the statistical reliability concern.
- A comparison to larger systems (Whisper, Mu²SLAM) for context on absolute performance levels would be informative but is outside the paper's stated scope.

## Removed Points

These points were flagged by reviewers but removed or weakened after verification against the paper:

- **"Missing LibriSpeech and AISHELL results"** — The paper states experiments were performed with these datasets, but results may reside in the appendix, which is stripped by the parser. Removed per rule about missing appendix content.
- **"Reproducibility statement is empty"** — Section 8 appears empty in the parsed text, but this could be a parsing artifact. Removed.
- **"No architecture details provided"** — Architecture details ARE provided (line 164: Conformer blocks, hidden dimensions, attention heads, kernel size). Factually incorrect criticism — removed.
- **"No comparison to prior MOO-ASR work (MGDA, PCGrad, uncertainty weighting)"** — Missing related works critique. Removed per rules.
- **"The comparison is dynamic vs static scalarization, not MOO vs no MOO"** — While baselines are underspecified, the paper does compare multiple dynamic-weighting variants (VS-ASR, VC-ASR, VM-ASR) against each other, and all baselines are cited to prior work. The framing is acceptable for a systems paper. Weakened.
- **"Objective soup terminology not carried through"** — A presentational nitpick, not a substantive weakness. Removed.
- **"PDF parsing artifacts in Definition 1"** — Known parser issue, not a paper error. Removed.
- **"Comparing to Whisper/Mu²SLAM would contextualize absolute performance"** — Outside the paper's stated scope. Moved to Nice-to-Haves.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a notable tension: the paper claims three distinct MOO formulations (single-level, bilevel/constrained, multilevel) as a structural contribution, but the algorithmic implementation collapses them into variants of a single scalarization scheme (weighted gradient descent with two types of coefficients — MoDo dynamic λs and fixed/predictably increasing penalty ηs). This gap between claimed and actual methodological novelty is the paper's most fundamental weakness and is unlikely to be resolved within a rebuttal — it would require either (a) reformulating the theory to match the algorithm or (b) redesigning the algorithms to faithfully implement the claimed formulations. Neither is a small fix. The reviews also collectively reveal that the paper's strongest evidence is comparative (VM-ASR > VC-ASR > VS-ASR empirically) while its weakest is explanatory (why this hierarchy works, whether gradient conflict is actually the mechanism).

## Suggestions

1. Clarify how the penalty-based update rules (Eqs. 7, 8) relate to the constrained/nested formulations (Eqs. 2, 3). If the threshold ε from VC-ASR is eliminated via penalty methods, state this explicitly and cite the standard penalty-method or augmented-Lagrangian justification. If VM-ASR's nested structure is approximated by a weighted sum, explain what conditions make this approximation valid.

2. Describe the MoDo algorithm (Chen et al., 2023) at a level sufficient for a reader to understand how λ weights are computed and what objective they optimize. MoDo is the engine of all three methods and cannot remain a black box.

3. Either provide the quantitative comparison for task-based vs. language-based hierarchy (F3) or downgrade F3 from a "finding" to a hypothesis for future work. A central claim made without evidence weakens the paper's credibility.

4. Add variance estimates (standard deviations or confidence intervals) to all main result tables. Even if single-run evaluation is the norm in the field, the small magnitude of many differences makes this essential.

5. Report the specific configurations of all baselines: the weight value used for "Static Weight," the PEFT method employed, and the weighting scheme used by "Joint PT+FT W/O MOO."

6. Reconsider the "up to XX%" framing. Present average improvements as the primary result and "up to" values as supplementary, so readers are not misled.

## Score and Decision

This paper addresses a relevant problem and provides a reasonably extensive empirical comparison on CoVoST 2. The consistent advantage of VM-ASR over alternatives is noteworthy. However, the paper has substantial weaknesses that limit its contribution: the algorithmic core (MoDo) is a black box, the connection between formulations and implementations is unstated, a central finding (F3) lacks supporting evidence, baselines are underspecified, and no statistical significance is reported. These issues collectively mean the paper's core claims are not adequately supported in its current form. The paper would need major revisions (clarifying the algorithm-formulation relationship, describing MoDo, providing evidence for F3, and adding statistical rigor) before it meets the threshold for acceptance at a competitive venue.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>