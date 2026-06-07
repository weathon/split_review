Now I have a clear calibration picture. Let me synthesize everything into the final review.

**Round 1 Bracket:** 6.5–8.0 (clearly above Turner et al. ActAdd at 5.0 and Personality Alignment at 6.0)

**Round 2 Narrowing:** 
- SADI (6.40) — our paper is clearly stronger (more applications, more novel)
- Instruction-Following Steering (7.00) — our paper is stronger (broader scope, preventative steering)
- CAST (7.33) — comparable in quality; our paper has more breadth and similarly novel contributions, but CAST has cleaner execution
- Uncovering Gaps (7.50) — topical adjacency, comparable quality tier

**Final Score:** 7.5 — the paper's strengths (automated pipeline, preventative steering, data screening, multi-model evaluation) place it solidly above the 7.0 tier, comparable to 7.33–7.50 anchors, but presentation gaps (LLM judge validation not surfaced, no variance estimates) prevent it from reaching the 8.0 level.

---

## Summary
This paper introduces "persona vectors" — linear directions in LLM activation space corresponding to personality traits — extracted via a fully automated pipeline requiring only a natural-language trait description. The authors validate these vectors for monitoring and controlling traits in deployment, demonstrate that finetuning-induced persona shifts are mediated by activation changes along persona vectors, and introduce two novel applications: (1) preventative steering, which adds the persona vector *toward* an undesired trait during training to prevent its emergence at inference while preserving capabilities, and (2) pre-finetuning data screening using a projection difference metric to flag problematic training data before expensive finetuning runs.

## Strengths
- **Fully automated pipeline with practical scalability**: The pipeline (Section 2) takes only a trait name and description, uses Claude 3.7 Sonnet to auto-generate contrastive system prompts, evaluation questions, and scoring rubrics, and produces a persona vector without any manual curation. This is a meaningful advance over prior work requiring hand-crafted contrastive prompts.
- **Preventative steering is a genuinely novel and counterintuitive intervention**: Steering *toward* an undesired trait during training to prevent its emergence is non-obvious. The fact-acquisition case study (Figure 6) provides compelling evidence: both inference-time and preventative steering reduce hallucinations, but inference-time steering catastrophically degrades MMLU and new-fact accuracy while preventative steering largely preserves both. This capability-preservation advantage has clear practical significance.
- **Pre-finetuning data screening with strong predictive power**: The projection difference metric (Section 6) predicts post-finetuning trait expression from training data alone, with correlations of r = 0.88–0.95 (p < 0.001) across models and traits (Figure 7). The sample-level separability results (Figure 8) and the finding that persona-vector filtering catches samples LLM-judge filtering misses (Appendix M) demonstrate practical utility.
- **Systematic demonstration that finetuning-induced persona changes are mediated by linear activation shifts**: Section 4 shows strong correlations (r = 0.76–0.97) between finetuning shift (activation change along persona vectors) and post-finetuning trait expression, with within-trait correlations exceeding cross-trait baselines, providing evidence for trait-specific signal.
- **Multi-model, multi-trait, multi-dataset evaluation**: All main claims are validated across two model families (Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct) and three traits (evil, sycophancy, hallucination) with 8 dataset types × 3 severity levels in finetuning experiments. The paper also reports comparisons with CAFT and notes where it fails (hallucination), adding credibility.
- **Honest about limitations**: The paper explicitly acknowledges that monitoring correlations are modest when controlling for prompt type (line 112), that negative traits tend to shift together (footnote 6), and that computing projection difference is expensive (line 253).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **LLM judge validation is deferred entirely to Appendix D**: Every quantitative result depends on trait expression scores from GPT-4.1-mini. The main text states that human-agreement validation and external-benchmark comparisons were performed (line 67: "we validate it by checking agreement between our LLM judge and human evaluators... see Appendix D"), but does not surface any resulting metrics (e.g., inter-rater agreement, correlation with human scores). Surfacing even one or two key numbers in the main text would substantially increase reader confidence. This is a presentation gap, not a methodological one — the validation exists.
- **No uncertainty quantification on key results**: The paper reports point estimates exclusively (correlation coefficients with p-values, MMLU accuracies). Finetuning experiments appear to use single runs per dataset configuration. While this is common in the field, confidence intervals on correlation coefficients and variance estimates for MMLU comparisons would help readers assess the robustness of claimed differences between methods (e.g., the ordering of interventions in Figure 5).
- **Preventative steering mechanism not mechanistically investigated**: The explanation (lines 176–188) is that the intervention "counteracts the finetuning objective's tendency to push the model along that direction." While plausible, the paper provides no analysis of whether the model's *unsteered* internal representations after preventative training remain at baseline levels. Measuring the finetuning shift (as in Section 4) for preventatively steered models would confirm whether the intervention genuinely prevented internal drift or merely counterbalanced it, and would help delineate boundary conditions.
- **Model scale gap between motivation and experiments**: The paper motivates itself with incidents involving very large deployed models (GPT-4o, Grok, Bing), but all experiments use 7B–8B open-weight models. The main text would benefit from acknowledging this gap explicitly.

### Trivial
- The number of system prompt pairs (5), evaluation questions (40), and the 50/50 extraction/evaluation split are stated without justification in the main text.

## Nice-to-Haves
- Cross-model transfer experiments (e.g., Qwen-extracted vector applied to Llama) would clarify whether the pipeline needs to be re-run per model or whether persona vectors generalize across model families.
- Testing on at least one larger model (30B–70B range) would increase confidence that findings scale to the model sizes where the problem is most acute.
- A deeper analysis of *why* preventative steering works — e.g., measuring unsteered activation drift after preventative training — would strengthen the mechanistic contribution.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "The evaluation framework rests entirely on an LLM judge whose reliability is not established" (claimed as fatal)** — REMOVED as a fatal claim. The paper explicitly acknowledges this reliance and states validation was performed (line 67). The validation exists in Appendix D; the issue is presentation (surfacing metrics in main text), not absence of validation. Retained as Minor above.
- **Harsh Critic: "The analysis conflates two sources of variation... creating a potential for circularity" (Section 4)** — REMOVED as factually incorrect. The finetuning shift is computed from activation differences and trait expression is from an LLM judge — these are different measurement instruments. Using the same evaluation prompts for both is standard practice to test whether activation-space changes predict behavioral changes, which is the point.
- **Harsh Critic: "The pipeline is self-referential... LLM-generated artifacts as ground truth"** — REMOVED as a distinct weakness. The paper acknowledges the LLM judge dependency and validates against humans. The concern about shared LLM biases is speculative and would apply equally to human annotators.
- **Harsh Critic: "The 'evil' construct... likely conflates multiple distinct behavioral dimensions"** — REMOVED. This is a philosophical concern about construct validity that does not threaten the empirical results. The paper defines evil clearly for its purposes and the results validate the construct operationally.
- **Harsh Critic: cross-model transfer and larger models as "Missing Parts"** — MOVED to Nice-to-Haves. These are scope expansions, not weaknesses of what the paper does.
- **Harsh Critic: Dataset construction transparency concern** — REMOVED. The paper states dataset construction details are in Appendix F (line 132: "Further details are provided in Appendix F"). Appendices are stripped by the parser but exist in the original submission.
- **Strength Finder: "This paper addressed an important problem" / "targeted an interesting question"** — REMOVED as generic and superficial praise without concrete grounding.

## Novel Insights
The paper's most interesting finding is the asymmetry between inference-time and preventative steering for capability preservation (Figure 6). The fact that adding a hallucination vector *during* training prevents hallucinatory behavior *after* training, while subtracting it at inference destroys the knowledge the model was trained to acquire, suggests that the training-time intervention changes *what the model learns* rather than merely masking outputs. This hints at a general principle for training-time interventions that preserve capabilities while shaping behavior — a direction with implications beyond persona control.

## Suggestions
- Surface the key LLM-judge validation metrics (e.g., human-judge correlation, Cohen's κ) in Section 2.1. This is the single highest-leverage improvement — it would anchor reader confidence in every subsequent result.
- Add confidence intervals to the headline correlation coefficients (Figures 3, 4, 7) and variance estimates to the MMLU comparisons (Figures 5–6). Even simple ±1 SD error bars from bootstrap resampling would suffice.
- Measure the finetuning shift for preventatively steered models. If the shift is near zero, this mechanistically confirms that preventative steering prevents internal drift; if the shift is large, it reveals a more complex mechanism and would help delineate boundary conditions.

## Calibration Summary (All Retrieved Anchors)

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| What Makes Your Model a Low-empathy... | DXaUC7lBq1 | 3.00 | R1 (weak) | Significantly weaker; thin empirical contribution |
| Measuring Effects of Steered Representation | z1yI8uoVU3 | 3.00 | R1 (weak) | Much weaker; evaluation-focused, no novel applications |
| pSAE-chiatry | LQdaXixB0g | 2.50 | R1 (weak) | Much weaker; narrow mental-health focus, limited validation |
| Generative Modeling of Individual Behavior | R9OHszNtpA | 3.40 | R1 (weak) | Weaker; different domain, narrower scope |
| Steering Language Models with Activation Engineering (Turner et al.) | 2XBPdPIcFK | 5.00 | R1 (middle) | Our paper substantially stronger: automated pipeline, more applications, broader evaluation |
| Entropic Activation Steering | YCu7H0kFS3 | 4.75 | R1 (middle) | Our paper stronger; EAST is narrower in scope |
| Personality Alignment of LLMs | 0DZEs8NpUH | 6.00 | R1 (middle) | Our paper stronger: more novel method, broader evaluation, more applications |
| From Steering Vectors to Conceptors | 9wjGUN65tY | 5.00 | R1 (middle) | Our paper stronger; more empirical, more applications |
| MAP: Multi-Human-Value Alignment Palette | NN6QHwgRrQ | 8.00 | R1 (strong) | Our paper slightly below; MAP has stronger theoretical framing |
| Booster: Tackling Harmful Fine-tuning | tTPHgb0EtV | 8.00 | R1 (strong) | Our paper slightly below; Booster has more rigorous defense evaluation |
| Sparse Feature Circuits | I4e82CIDxv | 8.00 | R1 (strong) | Our paper comparable novelty but less polished execution |
| HiRA | TwJrTz9cRS | 8.00 | R1 (strong) | Different domain; not directly comparable |
| Semantics-Adaptive Activation Intervention (SADI) | 8WQ7VTfPTl | 6.40 | R2 (narrow) | Our paper clearly stronger: more novel applications, broader evaluation, honest about limitations |
| Improving Instruction-Following via Activation Steering | wozhdnRCtw | 7.00 | R2 (narrow) | Our paper stronger: broader scope, preventative steering adds novelty beyond inference-time control |
| Programming Refusal with CAST | Oi47wc10sm | 7.33 | R2 (narrow) | **Comparable**: CAST has cleaner execution; our paper has more breadth and similarly novel contributions |
| Identifying and Tuning Safety Neurons | yR47RmND1m | 6.20 | R2 (narrow) | Our paper stronger: more applications, more automated |
| Linearity of Relation Decoding | w7LU2s14kE | 7.33 | R2 (narrow) | Comparable tier; our paper more applied, theirs more analytical |
| First-Person Fairness in Chatbots | TlAdgeoDTo | 7.25 | R2 (narrow) | Different domain; comparable quality tier |
| Uncovering Gaps in How Humans and LLMs Interpret Subjective Language | gye2U9uNXx | 7.50 | R2 (narrow) | **Comparable**: similar quality; our paper has broader practical contributions |
| Overthinking the Truth | Tigr1kMDZy | 7.33 | R2 (narrow) | Comparable tier; different focus (mechanistic vs. applied) |

**Round 1 Bracket:** 6.5–8.0. **Round 2 narrowed to:** 7.0–7.5. The paper is clearly above SADI (6.40) and Instruction-Following Steering (7.00), comparable to CAST (7.33) and Uncovering Gaps (7.50), and below the 8.0 tier (MAP, Booster, Sparse Feature Circuits). Final score: **7.5**.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>