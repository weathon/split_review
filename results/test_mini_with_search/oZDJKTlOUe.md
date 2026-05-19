Now I have strong calibration. Let me write the final review.

## Summary

This paper proposes LURE, a post-hoc hallucination revisor for LVLMs. It first identifies three causal factors of object hallucination (co-occurrence, uncertainty, object position) through empirical analysis, then constructs a synthetic hallucination dataset using GPT-3.5 that explicitly models these factors (inserting co-occurring objects, masking uncertain/late-position objects with "[IDK]"). A lightweight revisor model (a fine-tuned LVLM) is trained to reconstruct correct descriptions from these corrupted inputs. Experiments across six open-source LVLMs show consistent and often substantial improvements in CHAIR scores, human evaluation rankings, and GPT evaluation rankings.

## Strengths

- **Consistent and substantial gains across all six evaluated LVLMs on CHAIR metrics (Table 1).** LURE achieves the lowest CHAIR_S and CHAIR_I scores on every single model — e.g., MiniGPT-4 CHAIR_S drops from 26.8 (Original) to 19.7, mPLUG-Owl from 71.2 to 18.8 — often halving the hallucination rate of the original model. The improvement is not cherry-picked on one model but holds across architectures ranging from 7B to 13B scales.

- **Top rankings in both human and GPT evaluations (Table 2).** LURE receives the best (lowest) average ranking in both evaluations across all six LVLMs (e.g., MiniGPT-4: 1.67 GPT / 1.96 Human vs. next-best CoT at 2.44/2.83). This confirms that the CHAIR improvements translate to perceptibly less hallucinated descriptions as judged by both human annotators and an automated judge.

- **Ablation confirms all three factors contribute (Table 4).** Removing any one of the three factors (co-occurrence, uncertainty, object position) degrades CHAIR_S from 19.7 to 21.2–22.6, showing each factor plays a measurable role. The revisor also works across different backbone LVLMs (Table 5: CHAIR_S 19.7–22.1), not just a single architecture.

## Weaknesses

### Fatal

None.

### Major

- **The "additional data" control experiment (Table 3) is a strawman that does not support the intended claim.** The paper fine-tunes the *original LVLM* on the same hallucinatory (corrupted) dataset used to train the revisor. Unsurprisingly, CHAIR_S degrades from 26.8 to 31.0. The paper presents this as evidence that "our method indeed reduces object hallucination by post-hoc rectifying potential hallucinatory descriptions rather than using additional data." This does not follow — fine-tuning on deliberately corrupted data will naturally harm performance. A meaningful control would be: (a) fine-tune the base model on the *clean* target captions used as training targets for the revisor (same data scale), or (b) train the revisor and compare to a single-stage fine-tuning baseline on equal footing. As currently constructed, this experiment provides no evidence about whether the revisor framework is beneficial compared to simply having more training data.

### Minor

- **The theoretical analysis (Section 2.4) does not connect to the specific design choices of LURE.** The theorems demonstrate that reducing co-occurrence and sampling more certain objects can reduce test error in a simplified linear-Gaussian classification model. This is a generic observation that could motivate almost any hallucination mitigation method. It does not justify the specific algorithm design of LURE: using GPT-3.5 to insert co-occurring objects, masking with "[IDK]" placeholder tokens, or training a separate revisor model rather than, say, modifying the base LVLM's decoding. The claims in the abstract and conclusion of providing "rigorous statistical analysis" overstate what the theory delivers for the actual method.

- **The GPT-3.5 data construction pipeline is underspecified.** The paper repeatedly states that it "leverages GPT-3.5 to deduce and incorporate objects" and "prompt GPT-3.5" but provides no prompts, no examples of input-output format, no analysis of GPT-3.5's reliability or agreement rates, and no indication of the number of API calls or cost. The thresholds γ and η are said to be selected via cross-validation but their specific values are never reported, even in the ablation. These omissions hinder reproducibility of the core data generation procedure.

- **Ablation shows identical CHAIR_I (4.9) for "w/o Co-occurrence" and the full model (Table 4).** The paper claims all three factors contribute, but at the object-instance level (CHAIR_I), removing co-occurrence produces *no change* versus the full model. The paper does not discuss this result, which suggests co-occurrence may not help on this specific axis. The reported CHAIR_S differences (19.7 vs. 22.6) are modest and no statistical significance is reported, making it unclear whether the observed differences are reliable.

- **Algorithm 1 has clarity issues.** The variable `H_old` is used in the loop (line 146) but never initialized. Line 143 reads "Use GPT-3" and is truncated, which appears to be an incomplete step description. The algorithm mixes what should be a one-time data generation preprocessing step into the iterative training loop, creating confusion about the pipeline.

- **The revisor's visual access is unclear.** Algorithm 2 shows the revisor takes only the masked text description `s_t` as input and returns a corrected description. The paper never explicitly states whether the revisor also accesses the image during inference. If the revisor is purely text-based (which the algorithms suggest), this is a noteworthy design point that deserves discussion — how does a text-only model correct visual hallucinations reliably without seeing the image? If it does see the image, Algorithm 2 is missing this input.

- **Human evaluation details are vague.** The paper states "several native speakers" were involved but does not report the number of annotators, inter-annotator agreement, or whether annotators were blinded to method identity.

### Trivial

- The case study (Figure 5) only shows successful corrections. Including failure cases (where LURE introduces new hallucinations or removes correct objects) would provide a more balanced picture.

## Nice-to-Haves

- Make the GPT-3.5 prompts available with the code release to fully enable reproducibility of the data construction pipeline.
- Report threshold values (γ, η) and show sensitivity to them, since the method's masking behavior depends entirely on these two hyperparameters.
- Include GPT-Ensemble in the human/GPT evaluation tables for completeness, or explicitly state the cost rationale more clearly.
- Report statistical significance (e.g., confidence intervals via bootstrapping) for the CHAIR scores across the 5000 test samples, especially for the ablation study.

## Removed Points

These points were raised in the input reviews but are removed with justification:

- **"Unfair comparison with GPT-based baselines (LURE uses GPT-3.5 during training)"** — Removed. This is a standard knowledge-distillation setup: LURE uses GPT-3.5 only at training time to generate synthetic data, while GPT-Teacher/Ensemble use GPT-3.5 at inference time. LURE outperforming these baselines *without needing GPT-3.5 at test time* is a feature, not a flaw. The critic's framing misunderstands the design goal.
- **"Figures described only by captions / no quantitative summary statistics for the empirical analysis"** — Removed. The figures are embedded in the original PDF; this is a parser artifact.
- **"Missing related works"** — Removed per policy (cannot verify existence of missing references without external sources).
- **"GPT-Ensemble excluded from human/GPT eval"** — Removed. The paper explains this is due to cost, which is reasonable, and the four selected methods (Original, Teacher, CoT, GPT-Teacher) are appropriate.
- **"No statistical significance reported"** — Removed. CHAIR evaluation in this field does not routinely report significance tests; this is a community-standard choice.
- **"Missing appendix content / proofs"** — Removed per policy (appendix sections are stripped by the parser).
- **"Typos/formatting issues"** — Removed per policy (parser artifacts).
- **"General evaluation lacks rigor / baselines may not be fair"** — Removed as a generic area sweep without specific anchor in the paper text.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the central tension: LURE has strong and consistent empirical results across a wide range of models and metrics, but its weakest supporting experiments (the Table 3 control) and its most hyped section (the theoretical analysis) do not hold up to scrutiny. The honest strength of the paper is the empirical evaluation; the weak spots are the attempts to go beyond that into theory and controls.

## Suggestions

- Replace the Table 3 control with a meaningful baseline: fine-tune the base LVLM on the *clean* target captions (same size as the revisor's training data) and compare. This would actually test whether the revisor framework adds value over straightforward supervised fine-tuning on the same data.
- Either substantially shorten the theoretical section or replace it with analysis that connects to the actual method (e.g., when can a text-only revisor correct hallucinations that depend on visual grounding?).
- Release the GPT-3.5 prompts and report the threshold values (γ, η) and their sensitivity. These are essential for reproducibility of the data generation pipeline.
- Explicitly state whether the revisor takes the image as input during inference. If it is text-only, discuss the implications and limitations of this design choice.

## Score and Decision

**Calibration Report:**

*Round 1 (Bracketing):* Three queries found papers in [0–3] (weak: avg 2.67–3.0, rejected — e.g., attention calibration papers with outdated models and weak evaluations), [4–7] (middle: avg 4.0–5.5 — HIRE at 5.0 accepted poster, HalCap-Bench at 5.5, SHIELD at 5.5 accepted poster), and [8–10] (strong: avg 8.0 — oral-level papers on different topics). I bracketed LURE in [4.0, 7.0].

*Round 2 (Narrowing):* Searched inside [4.5, 6.5] and [5.5, 7.5]. Compared against:
- **HIRE** (5.0, Accept Poster, scores 6/6/2/6) — representation editing method with unfair baseline concerns. LURE has broader evaluation (6 models, human eval) and is somewhat stronger but shares similar evaluation-design concerns.
- **CAI** (5.0, Reject, scores 6/2/6/6) — attention intervention on outdated models. LURE is clearly stronger in evaluation breadth and result consistency.
- **DSCR** (6.0, Accept Poster, scores 6/4/6/8) — training-free KV refinement with depth cues. Cleaner evaluation, fewer methodological concerns than LURE. LURE's strawman control holds it back relative to DSCR.
- **SHIELD** (5.5, Accept Poster, scores 8/6/6/2) — training-free encoder-level mitigation with computational cost concerns. Comparable to LURE in having solid results paired with a notable methodological weakness.

*Final Score Determination:* LURE sits between SHIELD (5.5) and DSCR (6.0). It has stronger evaluation breadth than SHIELD (human eval, 6 models) but a more significant evaluation-design flaw (the strawman control). The disconnected theory section and missing reproducibility details are additional minor concerns. **5.5** is the appropriate score — LURE would benefit from major revisions to its control experiment and should release prompts/thresholds, but its core empirical contribution (consistent gains across 6 LVLMs validated by CHAIR, human, and GPT evaluations) is solid and supports the main claim.

**MY FINAL SCORE: <score>5.5</score>**
**MY FINAL DECISION: <decision>Accept</decision>**