## Summary
This paper investigates "Context Length Generalizability" (CoLeG) — the ability of LLMs to solve math word problems embedded in lengthy narrative contexts. It introduces GSM-Ext, an extension of GSM8K with iteratively lengthened problem descriptions; two metrics (CoLeG-E for efficacy, CoLeG-R for robustness); a Condition-Retrieving (CoRe) prompting method for proprietary LLMs; and an extension-based data augmentation strategy for fine-tuning open-source LLMs. The paper evaluates 7 proprietary and 20 open-source LLMs.

## Strengths
1. **Rigorous causal separation of context length from problem difficulty**: Section 2 uses a one-sided Mann-Whitney test (U=141565, P<0.0001) showing incorrect answers correspond to longer descriptions, followed by a contrast test controlling for reasoning-step count (F=1.9158, P=0.1476). This goes beyond descriptive correlational analysis found in most prior work on LLM distractibility.

2. **Quality-controlled benchmark construction**: GSM-Ext is created via iterative extension with two heuristic filters (entailment scoring + multi-LLM solvability) calibrated against human evaluation (185/200 excellent, only 11 poor). The dataset provides a unique testbed for studying context-length effects.

3. **CoRe prompting shows consistent gains across multiple proprietary LLMs**: In Table 1, CoRe improves 0-CoT, PS, and PS+ across Claude-3-opus, Gemini-pro, and GPT-3.5-turbo (typically +1–5 pp on Acc₄ and CoLeG-E). A worked example (Figure 2) illustrates the mechanism — recovering conditions missed by standard prompting.

4. **Broad model coverage**: Experiments span 7 proprietary and 20 open-source LLMs including general pre-trained (LLaMA-2), specialized math models (MetaMath, WizardMath, MAmmoTH, DeepSeek-Math), and multiple scales (7B–70B).

5. **Generalization to out-of-distribution benchmarks**: Both CoRe and SFT transfer to MAWPS, SVAMP, and GSM-IC without further adaptation — e.g., CoRe+PS+ improves GSM-IC accuracy from 87.48% to 91.63% (GPT-3.5-turbo), and SFT lifts LLaMA-2-7B on GSM-IC from 33.55% to 66.48%.

## Weaknesses

### Major
1. **Missing D₀-only ablation for the SFT experiments**: The paper fine-tunes on D = D₀ ∪ D₁ (64,929 CoT paths from standard GSM8K + extended questions) and attributes the gains to the "extension" component. There is no control experiment fine-tuning on D₀ alone (38,507 paths). Since D is ~1.7× the size of D₀, the improvements in Table 2 (e.g., LLaMA-2-7B: 4.31% → 28.09% CoLeG-E) could partially or entirely stem from simply adding more CoT training data rather than from the extension-specific data. This directly undermines the central SFT claim that "extension as an auxiliary task" drives the improvement. The Figure 7 analysis on MetaMath provides partial supporting evidence but is on GSM8K, not GSM-Ext, and uses a different model. Without the D₀-only control, the paper's main SFT results cannot be interpreted as evidence for the extension hypothesis.

### Minor
2. **CoRe lacks comparison to the most similar zero-shot methods**: The paper's zero-shot focus (Section 7, line 1011) means the primary baselines (0-CoT, PS, PS+) are reasonable choices. However, Re-Reading (RE2) and Stepback prompting — both of which can operate zero-shot and share the idea of re-engaging with problem context — are mentioned only in Related Work without empirical comparison. An experimental comparison would strengthen the novelty claim for CoRe and is a straightforward addition.

3. **CoLeG-R metric mechanically favors low-accuracy models**: CoLeG-R = Acc₄/Acc₀ is a ratio measure. A model with Acc₀=50%, Acc₄=49% scores 98%, while a stronger model with Acc₀=95%, Acc₄=80% scores 84%. The metric conflates absolute headroom for degradation with robustness. The paper reports Acc₀ and Acc₄ alongside CoLeG-R, partially mitigating this, but the metric's interpretation in cross-model comparisons is unreliable.

4. **Initial diagnostic analysis is narrow**: The statistical test in Section 2.1 uses only GPT-3.5-turbo on GSM8K. While sufficient as motivation, the paper's broader claims about "LLMs" struggling with long contexts generalize from a single model. (The subsequent GSM-Ext experiments on many models largely fill this gap, but the initial framing overstates the breadth of evidence.)

### Trivial
5. **No variance or confidence intervals for main results**: Tables 1–4 report only point estimates without statistical significance or variance measures.

## Nice-to-Haves
- Clarify how GSM-Ext's multi-round iterative extension (preserving conditions and order) differs from the single-sentence distractors of GSM-IC.
- Report whether the GPT-3.5-turbo-based answer extraction could systematically favor more structured CoRe outputs.
- Consider reporting an absolute degradation metric (e.g., Acc₀−Acc₄) alongside CoLeG-R.

## Removed Points
These points were raised by reviewers but removed after verification:

- **"CoLeG-E requires Q₀ through Q₄ to be all correct"** — The formula (line 206) sums over ∧_{r=1}^{R}, i.e., Q₁–Q_R only. Q₀ is not included. The critic misread the metric.
- **"Paper does not report round-by-round Accᵣ"** — Figure 6 explicitly shows per-round accuracy (Acc_i) for LLaMA-2 and MetaMath families. Incorrect claim.
- **"Data contamination concerns about generated data"** — Speculative; cannot be verified from paper content.
- **"Long context framing not distinguished from distractibility"** — The paper cites and evaluates on GSM-IC, and GSM-Ext's iterative narrative extension is structurally different from inserting distracting sentences, as described in Section 3.
- **"SFT comparison to MetaMath is apples-to-oranges"** — The paper explicitly notes the data efficiency comparison (65K vs 400K), which is a legitimate observation about training efficiency, not a flaw.
- **"CoRe hurts performance on GPT-3.5-instruct with PS and PS+"** — True for 2 of 12 comparisons but does not independently constitute a weakness given the overall positive pattern; subsumed under general CoRe evaluation.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add a D₀-only ablation** for the SFT experiments — this single experiment determines whether extension data provides benefit beyond simply adding more CoT training data and is essential to support the paper's central SFT claim.
2. **Compare CoRe empirically** to Re-Reading and Stepback prompting on GSM-Ext to establish whether CoRe provides marginal benefit over similar zero-shot approaches.
3. **Report confidence intervals** for main experimental results.
4. **Consider recalibrating CoLeG-R** — report an absolute measure like Acc₀−Acc₄ alongside the ratio.

## Score and Decision
This paper makes genuine contributions: a carefully constructed benchmark with rigorous quality control, a well-motivated prompting method (CoRe) with consistent if modest gains, and extensive evaluation across many models. However, the SFT claim for open-source LLMs lacks a D₀-only ablation, so the paper cannot distinguish the effect of "extension data" from simply "more CoT data." This is a structural experimental gap that directly affects a core claimed contribution. The CoRe prompting is better supported but would benefit from comparison to related zero-shot methods. The paper has real value — particularly the benchmark, the initial diagnosis, and the broad evaluation — but in its current form, experimental support for two of its four claimed contributions is incomplete.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>