- Decision: Reject
- Avg Score: 2.50
- Scores: 1, 3, 3, 3
Now I have a thorough understanding of the paper and the reviews. Let me produce the consolidated review.

## Summary

The paper proposes jailbreak attacks on LLMs using "language games" — both natural (Ubbi Dubbi, Leetspeak, Aigy Paigy, Alfa Balfa) and custom rule-based transformations (inserting characters between letters, reversing internal letters, cyclically replacing vowels, etc.). The key idea is that these transformed queries bypass safety alignment because the model fails to recognize the harmful intent when the surface form deviates from its safety training distribution. Experiments on GPT-4o, GPT-4o-mini, and Claude-3.5-Sonnet report success rates up to 93%. A fine-tuning experiment on Llama-3.1-70B then demonstrates that supervised fine-tuning on one transformation (e.g., inserting "-a-") does not generalize to even closely related variants, revealing brittleness in safety alignment.

## Strengths

1. **Novel attack surface grounded in real linguistic phenomena.** The use of natural language games (Ubbi Dubbi, Aigy Paigy, etc.) is genuinely different from prior encoding-based methods (Base64, ciphers, Morse code). These are not ad-hoc perturbations but well-defined linguistic manipulations with cultural history, and they produce outputs that remain interpretable to humans who know the rules (Section 3.1, Table lgs). The custom language games (Section 3.2, 8 rules) further extend this into an open-ended family of transformations.

2. **High observed attack success rates across multiple commercial models.** The paper reports 93% SR on GPT-4o (Leetspeak, Aigy Paigy), 89% on GPT-4o-mini (Self 7), and 83% on Claude-3.5-Sonnet (Self 7, Aigy Paigy) in Tables exp1 and exp2. These numbers are striking and suggest a genuine vulnerability, not a marginal effect.

3. **Fine-tuning generalization experiment reveals a meaningful finding about the brittleness of SFT-based safety alignment.** Table exp3.1 shows that fine-tuning Llama-3.1-70B on each of the 8 custom games yields near-zero success rates on the trained game (0–3%) but high success rates on the other 7 games (23–75%). Table exp3.2 further shows that even trivial variants of the trained transformation (e.g., changing the inserted string from "-a-" to "@p@" or "*z*") yield 75–98% success rates. This provides concrete evidence that supervised fine-tuning produces pattern-matched defenses rather than a generalizable understanding of harm.

4. **Systematic multi-domain evaluation.** The 300 test questions span 6 domains from SALAD-Bench (Representation & Toxicity, Misinformation Harms, Socioeconomic Harms, Information & Safety, Malicious Use, Human Autonomy & Integrity), and domain-level breakdowns in Figure overall show that the attacks are broadly effective, not limited to one category.

## Weaknesses

### Fatal
None.

### Major

1. **No baseline comparisons against existing encoding-based jailbreak methods.** The introduction motivates the work by claiming that prior encoding methods (Base64, ciphers, Morse code) suffer from "unreadability" and are "easily blocked" by targeted alignment, yet the paper never tests these claims empirically. Without a side-by-side comparison — same benchmark questions, same models — against, e.g., a Base64 attack, a simple substitution cipher, or AutoDAN, it is impossible to know whether the language-game methods are actually *more* effective, *more* readable, or *harder* to defend against. The paper's contribution is presented as an improvement over prior encoding approaches, but the evidence for this improvement is entirely missing. This is the single largest gap in the paper.

2. **Evaluation procedure for labeling SR/UR/FR is critically under-specified.** The paper defines success rate (SR), unclear rate (UR), and failure rate (FR) (Section 4.1) but never describes the process by which responses are assigned to these categories. Are responses judged by human annotators? If so, how many, what was the inter-annotator agreement, and what guidelines were provided? Were judges blind to condition? If an automated classifier was used, which one, and was it validated against human judgment? The paper states that "the decoding process … allows us to clearly assess the content" (Section 3.1), but this only describes reversing the transformation — it does not describe how the decoded content is classified as harmful, unclear, or blocked. Without this transparency, the headline success rates (93%, 89%, 83%) rest on an unverifiable foundation.

### Minor

1. **Inconsistent y-axis scaling in Figure overall.** The subfigures use different y-axis ranges (some go to 50, others to 200), making cross-domain visual comparison difficult. This should be standardized.

2. **Unclear rate (UR) is reported but not adequately interpreted.** UR is high in several conditions (e.g., 70% for GPT-4o-mini on Self 2, 38% on Aigy Paigy). The paper notes this briefly (Section 4.2: "GPT-4o and GPT-4o-mini frequently provide unclear responses, often addressing questions while framing their answers in a positive manner") but does not analyze whether these unclear responses still constitute a useful attack. If a model responds with harmless-sounding content that avoids the harmful request, the attack has not really succeeded despite not being a "failure." A breakdown of what "unclear" means in practice would strengthen the analysis.

3. **No human evaluation of readability.** A core claimed advantage of language games over encoding methods is "high readability," but this is asserted without any human study, readability metric, or even a systematic comparison. The examples in the paper are somewhat readable, but a quantitative or human-evaluated assessment would substantiate the claim.

4. **Attack cost and overhead are not reported.** The paper does not discuss how many additional tokens the transformations add (e.g., Self 1's "-a-" insertion roughly doubles length; other transformations may add less), nor the time cost of the encoding/decoding process. These are relevant for practical deployment of the attack and for comparison to alternatives.

5. **Only one decoding/annotation reproducibility detail is missing.** The paper does not specify the exact decoding algorithms for the natural language games (e.g., how Ubbi Dubbi output is reverse-transformed), which is important for reproducibility.

### Trivial
- Figure overall uses jailbreak "counts" rather than rates, and the y-axis ranges are inconsistent across subfigures.
- The caption for Table exp3.1 uses the phrase "the model successfully defends against Self 1" in the caption, but the row clearly shows it fine-tunes on all 8 games, not just Self 1. The caption could be clearer.

## Nice-to-Haves
- **Baseline comparison** (addressed under Major — this is the most important improvement).
- **Ablation on the 2.7:1 general-to-jailbreak data ratio** in the fine-tuning experiment. The paper does not justify this ratio or test its sensitivity.
- **Testing on open-source models** (e.g., Llama-3-8B/70B, Mistral) for the main attack, not just for the fine-tuning experiment.
- **Testing whether broader safety fine-tuning** (RLHF/DPO on multiple adversarial patterns) also fails, to see if the generalization failure is specific to SFT-LoRA or more general.

## Removed Points

- **"The paper fine-tunes on only one custom language game (Self 1)"** — REMOVED as factually incorrect. Table exp3.1 (rows Self 1 through Self 8) shows fine-tuning on ALL 8 games separately, with each row reporting a separate fine-tuning run. The critic appears to have misread the table.
- **"The criticism of prior encoding methods being 'completely indecipherable' is an overstatement"** — REMOVED. The paper's claim is specifically about outputs *containing errors* in Base64/ciphers, which is a reasonable observation (a few garbled characters in Base64 indeed make decoding difficult). Not a substantive weakness.
- **"Custom games are more akin to character-level perturbations, the label 'language games' feels inflated"** — REMOVED as a subjective framing preference that does not constitute a weakness. The transformations are rule-based manipulations of natural language text, which fits the authors' definition.
- **"The readability claim is questionable because example '-1-Ho-1-w...' is not easily readable"** — REMOVED. This example IS readable to an English speaker (it spells "How to make a bomb?" with "-1-" before odd-position letters). The critic's personal readability assessment does not override the paper's characterization.
- **"No open-source model is evaluated for the main attack"** — REMOVED. Three commercial models (GPT-4o, GPT-4o-mini, Claude-3.5-Sonnet) are tested, which is a reasonable starting point. Llama-3.1-70B is additionally used for fine-tuning. This is not a gap.
- **"Only 300 questions is a small sample"** — REMOVED. The critic's own calculation shows ±3% CI for the aggregate, which is standard. 50 per domain is reasonable for a category-level analysis.
- **"The paper should release annotation guidelines and judgment data"** — REDUCED from Major to the evaluation-protocol Major weakness. The core issue is that the protocol is under-described, not that data isn't released.

## Novel Insights

None beyond the paper's own contributions. The core observation — that LLMs fail to recognize harmful intent when input is transformed through simple, rule-based linguistic manipulations — is well-validated by the experiments. The most striking finding is from the fine-tuning experiments (Tables exp3.1 and exp3.2): changing a single string in a transformation rule (from "-a-" to "@p@") collapses defense rates from 98% failure to 2% failure, showing that SFT-based safety alignment learns extremely narrow, pattern-matched behaviors rather than any generalizable understanding of harm.

## Suggestions

1. **Add baseline comparisons as the top priority.** Test Base64, a simple substitution cipher (e.g., ROT13 or a Caesar cipher), and an AutoDAN-style attack on the same 300 SALAD-Bench questions against the same models. Report SR/UR/FR side-by-side with the language game methods. This would directly validate (or refute) the claimed advantages over encoding-based methods.

2. **Describe the labeling protocol in detail.** Specify whether SR/UR/FR were assigned by human annotators or automated classifiers. If automated, name the classifier, report its accuracy against human judgments on a sample, and release the judgment data. If human, report the number of annotators, inter-annotator agreement (Cohen's κ), and the annotation guidelines.

3. **Disaggregate "unclear rate."** Separate UR into at least two categories: (a) responses that are off-topic or nonsensical, and (b) responses that reframe the harmful request in a harmless way. This would clarify whether UR represents a failed attack or a partial defense.

4. **Standardize the y-axis in Figure overall** to use the same scale across all subfigures, or at minimum note the scale difference clearly.

5. **Add a supplement with the decoding algorithms** for each natural language game so the method is fully reproducible.

6. **Temper the generalization claims slightly.** The fine-tuning experiment convincingly shows that SFT-LoRA on one transformation does not generalize, but the paper's conclusion that "safety alignments fail to generalize" could be read as a broader claim about all safety fine-tuning methods. Clarify the scope (SFT, LoRA, one base model, one training setup).
