- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 6, 5, 3
Now I have a thorough understanding of the paper and can verify all reviewer claims directly. Let me synthesize the final review.

## Summary

This paper proposes Parrot, a framework that trains a dedicated "ask model" (Parrot-Ask) on real user-ChatGPT logs to generate human-like multi-turn instructions. Parrot-Ask then converses with ChatGPT to collect 40K high-quality multi-turn dialogues (Parrot-40K), which are used to fine-tune a chat model (Parrot-Chat). The paper demonstrates that Parrot-40K has substantially better properties than existing datasets (longer turns, more topic shifts, more human-like) and that Parrot-Chat achieves strong performance on instruction-following benchmarks, particularly on multi-turn evaluations.

## Strengths

1. **Novel ask-model methodology.** Training a model to predict *question* tokens conditioned on assistant responses (Section 3.1, Eq. 1) is a genuinely clever inversion of standard chat model training. This addresses a real gap — existing automatic data generation methods produce non-human-like instructions — and the approach is well-motivated by direct analysis of real user logs.

2. **Parrot-40K dataset is clearly superior to existing alternatives.** Table 1 and Figure 3 show Parrot-40K achieves the highest average turns (8.7 vs. 2.1–3.1), longest average sequence length (751 tokens vs. 196–355), highest topic shifts (8.0 vs. 0.6–3.7), and highest context-dependent reference count (5.0 vs. 1.0–1.7). These differences are large and consistently favor Parrot-40K across every metric.

3. **Clean ablation studies that isolate the method's effect.** Table 4 controls for base model (all LLaMA-2-13B) and shows that replacing original ShareGPT/UltraChat questions with Parrot-Ask-generated questions yields consistent improvements across Alpaca-Eval, MT-Bench, and MT-Bench++ (e.g., +10.57pp on Alpaca-Eval for the UltraChat subset). Figure 5 further shows that longer training sessions (full turns) produce stable multi-turn performance while truncated sessions degrade — causally linking the data properties to the performance gains.

4. **Data efficiency.** Parrot-Chat achieves strong results with only 40K training dialogues, while Vicuna uses 200K and UltraLM uses 1.5M. This is a meaningful practical advantage.

## Weaknesses

### Fatal
None.

### Major

1. **Base model confound in the main comparison table (Table 3).** The paper compares Parrot-Chat (LLaMA-2-13B) against Baize and UltraLM, which use LLaMA-1-13B, while only Vicuna also uses LLaMA-2-13B. The paper acknowledges "Baize, UltraLM, and Vicuna are all based on the LLaMA series model, including LLaMA-1 and LLaMA-2" (Section 4.4) but presents the comparison as "Among the open-source models, Parrot-Chat exhibits the best performance" without controlling for the base model. The ablations in Table 4 use LLaMA-2-13B for all variants and are internally clean, but the headline result in Table 3 conflates two variables (base architecture and training data). The claim of superiority over other open-source models would be stronger if either (a) Baize and UltraLM were retrained on LLaMA-2-13B, or (b) an additional Parrot-Chat baseline on LLaMA-1-13B were provided.

2. **MT-Bench++ validation gap.** The central multi-turn evaluation benchmark (MT-Bench++) is constructed by manually adding six follow-up questions to each MT-Bench dialogue (Section 4.3). The main text provides no information about: the number of annotators, inter-annotator agreement, whether annotators were blind to the method, or any validation of the added questions' quality (beyond requiring they be "articulated and fluent"). The paper references "comprehensive instructions for annotators" in supplementary materials, but the key details about reliability and potential bias belong in the main text since the paper's strongest multi-turn claims (stable performance across 8 turns, Figure 4) rest on this benchmark.

3. **Human-likeness annotation lacks methodological detail.** The claim that "81.1% of the questions generated using our parrot method resembled real user inquiries, while only 36.8% did so when using iterative self-chatting" (Section 4.2) is a strong quantitative claim, but the main text provides no details about who the annotators were, how many, whether they were blind to question source, what instructions they received, or what the inter-annotator agreement was. This weakens what would otherwise be a compelling direct validation of the method's core premise.

### Minor

1. **No variance or confidence intervals reported.** All evaluation results (Tables 3, 4; Figures 4, 5) are point estimates with no indication of whether evaluations were repeated or how much GPT-4 judgments vary. While single-run GPT-4 evaluation is standard practice in this area, the paper's strongest visual evidence (Figure 4 showing stable performance vs. competitor degradation) would be more convincing with some measure of uncertainty, especially since differences between models at individual turns are on the order of ~0.5 points. This is a minor concern given community norms, but worth noting.

2. **Limited failure case analysis.** The paper acknowledges that Parrot-Ask "may generate repetitive or non-meaningful questions" but describes these as "only a small proportion" (Section 4.2) without providing concrete examples. A few illustrative failure cases would help readers understand the method's limitations.

### Trivial
None.

## Nice-to-Haves

- **Retrain Baize/UltraLM on LLaMA-2-13B** to clean up the base-model confound in the main results table, or provide a Parrot-Chat variant trained on LLaMA-1-13B for a fairer comparison.
- **Run a small human evaluation** on MT-Bench++ model responses (e.g., pairwise comparisons between Parrot-Chat and Vicuna) to validate that GPT-4 judgments align with human preference in the multi-turn setting.
- **Report GPT-4 evaluation variance** (e.g., 3 runs with different temperatures or bootstrap resampling) for the key comparisons.
- **Provide a cost estimate** for generating Parrot-40K (API calls, time) to help readers assess scalability.

## Removed Points

Points flagged for removal — treat with caution:

1. **"The paper should note that the system instruction is included in the sequence and masked"** (Harsh Critic, Section 3.3 note): This is a minor presentation clarification about standard practice. The paper describes the masking already: "With the system instruction and user question tokens masked, we compute the loss on the response tokens" (Section 3.3). The critic's point about the training objective is addressed.

2. **"Ablation on the choice of base model for Parrot-Ask"** (Harsh Critic): Asking whether a smaller model (e.g., 7B) would suffice for Parrot-Ask is a reasonable extension but goes beyond the paper's stated scope. The paper trains on LLaMA-2-13B and achieves good results; exploring smaller backends is future work.

3. **Strength from Strength Finder about Parrot-Chat "outperforms existing 13B open-source models"**: Kept as a strength but with caveat (the base model confound is noted in weaknesses). Not removed — just qualified.

4. **Strength from Strength Finder about MT-Bench++ providing "a more rigorous multi-turn evaluation"**: Kept but qualified by the validation gap weakness.

5. **Strength about "Parrot-Chat maintains stable performance across all 8 turns while competitor models drop after turn 6"**: This is a directly supported claim from Figure 4. Kept but qualified by MT-Bench++ validation concerns.

## Novel Insights

None beyond the paper's own contributions. The core insight — training a dedicated ask model by inverting the standard chat model loss to predict questions rather than answers — is the paper's contribution itself.

## Suggestions

1. For the main results table (Table 3): either retrain Baize and UltraLM on LLaMA-2-13B, or train a Parrot-Chat variant on LLaMA-1-13B. This would cleanly separate the effect of the data generation method from the effect of the base model architecture.

2. Provide basic annotation metadata in the main text for the human-likeness evaluation: annotator count, blinding procedure, and inter-annotator agreement (even if computed on a small subset). This would substantially strengthen the 81.1% vs 36.8% claim.

3. Report whether GPT-4 evaluations on MT-Bench++ were repeated and provide some measure of agreement (e.g., correlation between runs, or a note on the temperature setting used).
