Now I have all the evidence I need. Let me write the consolidated review.

## Summary

This paper proposes and compares three multi-objective optimization (MOO) frameworks—VS-ASR (single-level vector), VC-ASR (bilevel with self-supervised constraint), and VM-ASR (multilevel with hierarchical objectives)—for multilingual multi-task ASR and speech-to-text translation. The central claim is that a multilevel optimization structure separating highly conflicting objectives into different optimization levels consistently outperforms both single-level and bilevel formulations. Empirical results on CoVoST 2 with two model sizes (100M and 58M) show VM-ASR achieving up to ~23% relative improvement in ASR WER and ~28% improvement in S2TT BLEU over two-stage PT+FT baselines.

## Strengths

1. **Clear formulation and systematic comparison of three MOO architectures.** The paper explicitly defines VS-ASR (Section 4.2), VC-ASR (Section 4.3), and VM-ASR (Section 4.4) with concrete update rules (Equations 5, 7, 8) and algorithm summaries. All three use the same underlying MOO solver (MoDo), which allows attribution of performance differences to the optimization structure rather than the weighting scheme. This clean experimental design is the paper's strongest methodological feature.

2. **Consistent and substantial performance gains from VM-ASR across languages.** Tables 1 and 2 (present in the parsed text as images) report that VM-ASR (USA) improves ASR WER by up to 22.3% (100M model) and S2TT BLEU by up to 27.9% over two-stage PT+FT, with gains holding across multiple languages (En, Fr, De, Es, Ca for ASR; Fr, De, Es, Ca for S2TT) and two model sizes. Gains for the 58M model are also consistent (up to 14.6% ASR, 20.5% S2TT).

3. **Training cost trade-off is explicitly quantified.** The paper reports that MOO methods require ~11.6 GB GPU memory and ~2.8 hours/epoch versus ~8.7 GB and ~2.25 hours/epoch for standard PT+FT (line 166). Acknowledging the higher training cost while noting that deployment efficiency of a single model justifies it adds practical credibility.

## Weaknesses

### Major

1. **Missing content prevents full evaluation of core claims.** Section 5.2 ("Conflicting ASR and S2TT Objectives") consists of a heading with no text. **Figure 3**, referenced as the key evidence for F3 (task-based hierarchy outperforms language-based hierarchy), does not appear in the parsed manuscript. **Table 4**, referenced in F4 (penalty parameter impact), is entirely absent—the string "Table 4" does not appear anywhere in the provided text. While Tables 1–3 and Figures 1–2 are present as images, the complete absence of Figure 3 and Table 4 means that claims F3 and parts of F4 rest on evidence the reviewer cannot inspect. This is not an appendix/parser issue—the missing content belongs to the main body's empirical analysis.

2. **Promised LibriSpeech and AISHELL results are absent.** The abstract and findings (lines 4, 21) claim experiments on LibriSpeech and AISHELL v1 alongside CoVoST 2. Remark 1 (line 112) describes language-based MLO involving English (LibriSpeech) and Chinese (AISHELL). However, all visible results in Tables 1–3 are exclusively from CoVoST 2. The paper's empirical scope is substantially narrower than advertised. A paper that promises experiments on three datasets but delivers results for only one has a significant credibility gap.

3. **VC-ASR constraint (Equation 4) is ill-defined and disconnected from the algorithm.** The constraint is written as \(l_u(\theta) - \min_{\theta} l_u(\theta) \leq \epsilon\) (line 84). The term \(\min_{\theta} l_u(\theta)\) denotes the global minimum of the self-supervised loss, which is an unknown quantity that depends on \(\theta\) itself—it is not a standard optimization constraint. The paper never explains how this quantity is computed or approximated, nor how \(\epsilon\) is chosen. The actual update rule (Equation 7, line 135) uses a penalty term \(\eta \nabla_\theta l_u\) with no explanation of how the constrained formulation maps to the penalty method. There is no discussion of how \(\epsilon\) relates to \(\eta\) or the penalty schedule. This conceptual gap undermines confidence in the algorithm's theoretical grounding.

4. **No direct evidence that MOO mitigates gradient conflicts (Claim F1's mechanism).** The paper's central motivation is that MOO avoids conflicting gradient directions (F1, line 23), yet no gradient-level diagnostics are presented—no cosine similarity measurements, conflict ratios, or any direct analysis of gradient alignment. The only evidence is that final ASR/S2TT metrics improve. Improved metrics could result from hyperparameter tuning, different learning schedules, or the dynamic weighting itself rather than from conflict mitigation specifically. For a paper whose entire framing rests on gradient conflict, the absence of gradient-level analysis is a significant gap.

### Minor

1. **No comparison against other MOO solvers.** The paper only uses the MoDo algorithm for dynamic weighting and does not compare against widely used MOO alternatives such as MGDA, PCGrad, or CAGrad. While the comparison of VS-ASR vs. VC-ASR vs. VM-ASR (all using MoDo) does successfully isolate the hierarchy effect, the broader claim that "MOO methods help" would be strengthened by demonstrating robustness across different MOO solvers.

2. **Choice of CPC loss is not motivated.** The paper uses Contrastive Predictive Coding (CPC) as the self-supervised objective, which is less common in modern ASR pre-training (where wav2vec 2.0 or HuBERT are more standard, line 106). No justification is given for this choice, and it is unclear whether findings would transfer to other SSL methods.

3. **No confidence intervals or variance estimates.** Tables 1–3 report point estimates without standard deviations. Multi-task training is known to be sensitive to hyperparameters and initialization; some measure of variability would be needed to assess the statistical reliability of the claimed improvements.

4. **Reproducibility statement is empty.** Section 8 (line 201) is a heading with no content, making reproducibility non-assessable from the paper itself.

### Trivial

- None beyond what is already noted in Minor.

## Nice-to-Haves

- The paper would benefit from gradient-conflict diagnostics (cosine similarity, conflict ratios) to directly support the mechanism claimed in F1.
- A controlled ablation comparing VM-ASR against a version with the same hierarchy but static weighting (without MoDo) would further disentangle hierarchy benefits from dynamic weighting.
- Results on LibriSpeech and AISHELL should be added to fulfill the scope promised in the abstract.
- The VC-ASR formulation should be rewritten as a proper penalty method or the constraint should be redefined using empirically accessible quantities.

## Removed Points

These points were flagged by reviewers but are removed for the reasons noted below; they are recorded here for transparency:

- **"Objective soup terminology is confusing / never clearly tied to methodology."** — The paper explicitly defines "objective soup" as the methodology of combining multiple objectives (line 12). Whether the name is felicitous is a matter of taste, not a technical weakness. *Removed as a style nitpick.*

- **"The 3.8% and 4.8% improvement claim is asserted rather than derived from a table."** — The paper directly references Tables 1 and 2 for these numbers (line 23). The tables are present as images in the parsed manuscript (lines 160, 174). *Removed because this is a parser limitation, not an author error.*

- **"The experiment does not isolate the contribution of the hierarchy."** — This is incorrect: VS-ASR, VC-ASR, and VM-ASR all use MoDo as the MOO solver. The comparison VM-ASR vs. VS-ASR therefore does isolate the hierarchy effect. (The separate concern about missing comparisons to other MOO solvers is retained in Minor.) *Removed as factually incorrect.*

- **"The paper should cover more languages / tasks / domains."** — The paper evaluates 5 languages for ASR and 4 for S2TT on CoVoST 2, plus claims LibriSpeech and AISHELL experiments (whose results are absent). Scope creep beyond this would turn the paper into a different, broader paper. *Removed as scope creep.*

- **"Large-scale multi-seed runs" and "full-scale evaluation on every benchmark" asks.** — The experiments described are already substantial for an academic submission. *Removed as infeasible asks.*

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel interpretation or insight that the paper itself does not already contain or imply.

## Suggestions

1. **Complete the missing empirical content.** Add the text for Section 5.2 (gradient conflict analysis), include Figure 3, provide Table 4, and report the promised LibriSpeech and AISHELL results. Without these, the paper's claims F3 and F4 cannot be fully evaluated.

2. **Reformulate the VC-ASR constraint.** Replace the ambiguous \(l_u(\theta) - \min_\theta l_u(\theta) \leq \epsilon\) with a proper penalty or barrier formulation, and explain the relationship between \(\epsilon\) and the penalty schedule \(\eta\).

3. **Add gradient-level diagnostics.** Report mean pairwise gradient cosine similarity and/or conflict ratios across objectives under each formulation to directly support the gradient-conflict mitigation claim.

4. **Add variance estimates.** Report results over multiple seeds (at least 3) for the main comparisons to establish statistical reliability.

5. **Motivate the choice of CPC or include a second SSL method** (e.g., wav2vec 2.0) as a robustness check.

## Score and Decision

**Overall assessment:** The paper tackles a relevant problem (multilingual multi-task ASR with conflicting objectives) and presents a clean comparison of three MOO formulations using a consistent solver, with promising results on CoVoST 2. However, the submission in its current form has significant structural gaps: Section 5.2 is empty, Figure 3 and Table 4 are absent, and results for LibriSpeech and AISHELL are promised but not delivered. These gaps affect 3 of the paper's 4 claimed findings (F1's mechanism, F3, F4). Additionally, the VC-ASR constraint is ill-defined, and no gradient-level diagnostics support the core conflict-mitigation narrative. The paper requires substantial revisions before it can be accepted.

**Score: 4.5/10** — Reject. The core idea has merit and the CoVoST 2 empirical comparison is well-structured, but the incomplete empirical content, absent promised results, ambiguous algorithmic formulation, and lack of mechanism-level evidence collectively prevent acceptance in the current form. A substantially revised and completed manuscript could be competitive.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>