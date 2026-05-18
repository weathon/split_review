## Summary

This paper proposes a "chat vector" approach: subtracting LLaMA2 weights from LLaMA2-chat weights yields a vector that, when added to a continually pre-trained model on a non-English language (Traditional Chinese, Korean, Simplified Chinese), imparts instruction-following and alignment capabilities without the need for RLHF. The method is computationally efficient — replacing the CP→SFT→RLHF pipeline with CP + vector addition. The main evidence comes from GPT-4 scoring on the Vicuna benchmark, supported by toxicity and safety evaluations.

## Strengths

- **Computational efficiency.** The paper clearly demonstrates that the chat vector replaces the expensive RLHF phase with a single vector addition after continual pre-training, drastically lowering the barrier for non-English alignment. Section 1 explicitly contrasts the traditional pipeline with the proposed approach and notes it is "substantially more efficient than reimplementing RLHF."

- **Effectiveness across multiple languages.** Table 1 reports GPT-4 scores on the Vicuna benchmark for Traditional Chinese, Korean, and Simplified Chinese, showing that CP + chat vector achieves competitive or better instruction-following compared to CP→FT baselines. The effect holds across three different language-specific models.

- **Complementary effect with fine-tuning.** Table 1 consistently shows that the combination FT + chat vector outperforms either component alone, even when the fine-tuned model uses a different prompt template (Korean case). This directly supports the claim that the chat vector can synergize with existing fine-tuned knowledge.

- **Honest treatment of a limitation.** Section 5.5 identifies that the full chat vector can cause English responses for Chinese-LLaMA, and shows that scaling by 0.5 mitigates this (Table 4). The paper openly states that finding the optimal coefficient "requires further research" — this transparency strengthens the practical contribution.

## Weaknesses

### Fatal
None.

### Major

1. **Multi-turn dialogue claim is supported only by a single case study, contradicting the claim of "comprehensive evaluation."**  
   The paper lists "multi-turn dialogue" as one of three evaluation perspectives in its stated contributions (Section 1, bullet 3), yet Section 5.4 presents exactly one anecdotal example (Figure 2) as evidence. No systematic metric (e.g., MT-Bench, turn-level accuracy, dialogue length, coherence scoring) is reported. The fine-tuning dataset explicitly contains no multi-turn data (Section 4.1), so the claim that the chat vector alone imparts multi-turn ability rests entirely on a single cherry-pickable example. Describing this as a "case study" does not reconcile with the paper's contribution framing of a "comprehensive evaluation" across three perspectives.

2. **Missing training details prevent reproducibility assessment.**  
   No hyperparameters are reported for either continual pre-training (3.1B tokens) or fine-tuning (80k pairs): learning rate, batch size, optimizer, scheduler, number of steps/epochs, or warmup are entirely absent. The fine-tuning dataset generation via GPT-4 with self-instruct (Section 4.1) lacks parameters (temperature, top-p), filtering criteria, prompt templates, and any manual verification protocol. The continual pre-training corpus is described only by coarse domain labels. These omissions make it impossible for other researchers to replicate the baselines or to verify that comparisons were conducted under fair/optimal conditions. While the chat vector method itself is simple, the baselines against which it is compared are opaque.

### Minor

1. **Toxicity evaluation via Perspective API does not address language limitations.**  
   The paper evaluates toxicity on Chinese model outputs using Perspective API (Table 2) without discussing whether the API was configured for the target language or acknowledging known variability in toxicity detection quality across languages. While Perspective API does support multiple languages (the reviewer's claim that it "was trained on English text and is not designed for Chinese or Korean" is factually incorrect — Perspective API has had Chinese and Korean support since 2020), the quality of cross-lingual toxicity detection is an established concern in the literature, and the paper cites no validation for its use in Traditional Chinese. This weakens but does not invalidate the safety-related claims, since the paper's primary demonstration (instruction following via GPT-4 scoring on Vicuna) does not depend on this evaluation.

2. **Language detection is not reported for the toxicity evaluation.**  
   Table 4 shows that the chat vector can trigger English responses for some models (e.g., Chinese-LLaMA), and scaling mitigates this. However, language purity is only monitored for Vicuna and Safety Prompts evaluations, not for the Real Toxicity Prompts evaluation (Table 2). If a non-trivial fraction of toxicity-evaluation outputs are in English, the Perspective API scores could be confounded. The paper should report language detection results for all evaluation sets or explain why this is not needed.

### Trivial
None.

## Nice-to-Haves

- A systematic multi-turn evaluation benchmark (e.g., MT-Bench translated to the target language, or a custom multi-turn Chinese dialogue task with quantitative metrics) would substantiate the multi-turn claim.
- An ablation on continual pre-training data size would strengthen the efficiency argument — does the chat vector work equally well when CP data is scarce?
- An RLHF baseline (even at small scale, e.g., PPO on the same 80k dataset) would help contextualize how much of RLHF's benefit the chat vector actually captures. However, this is a substantial engineering undertaking and not a standard expectation for this type of paper.
- The scaling coefficient (full vs. half vector) is noted as important but explored only at {1.0, 0.5}. A finer-grained sweep across evaluation dimensions would provide practical guidance.

## Removed Points

These points were flagged by reviewers but are removed or downgraded upon verification against the paper:

- **"Perspective API was trained on English text and is not designed for Chinese or Korean"** — Removed as factually incorrect. Perspective API has supported Chinese and Korean since 2020. The underlying concern about cross-lingual reliability is retained in Minor Weakness 1 with corrected framing.
- **"GPT-4 as a judge has known biases"** — Removed as generic and not specific to this paper. The paper transparently describes its evaluation protocol (Section 4.3) and this is a widely accepted practice in the literature despite known limitations.
- **"Scaling factor not systematically studied"** — Moved to Nice-to-Haves. The paper explicitly acknowledges this as future work ("requires further research," line 186). The criticism amounts to asking for additional experiments, not identifying a flaw.
- **"No error bars or statistical tests"** — Removed as a nitpick. Greedy decoding is deterministic, and multi-seed training of 13B models is prohibitively expensive. Single-run evaluation with greedy decoding is standard practice in this setting.
- **"The comparison to traditional CP→SFT→RLHF is conceptually central but no RLHF baseline is attempted"** — Moved to Nice-to-Haves. Implementing RLHF is a major undertaking described by the paper itself as "intricate" and "computationally demanding." Its absence is not a flaw given the paper's stated goal of offering an efficient alternative.
- **"Training hyperparameters for baselines"** — Kept as Major Weakness 2 (not a nitpick), since the complete absence of any training configuration goes beyond a trivial omission and affects the verifiability of all baseline comparisons.
- **Strength "Multi-turn dialogue acquisition"** — Dropped from Strengths because it conflicts with a verified weakness (insufficient evidence). The case study exists but does not constitute strong evidence; the weakness wins.

## Novel Insights

None beyond the paper's own contributions. The core observation — that the difference between a pretrained model and its chat-aligned counterpart can be treated as a vector and transferred to a language-adapted version of the same base model — is the paper's main insight, and the reviews do not add a deeper synthesis beyond what the authors already present.

## Suggestions

1. **For the multi-turn claim:** Either provide a systematic evaluation (translated MT-Bench, automated metrics on dialogue state tracking, or human evaluation) or explicitly scale back the claim to a qualitative observation rather than listing it as one of three core evaluation perspectives.

2. **For the toxicity evaluation:** At minimum, document whether the Perspective API was configured with language-specific settings, report language detection on toxicity outputs, and add a citation discussing the reliability of cross-lingual toxicity detection. Better yet, complement with a Chinese-specific safety classifier or a small-scale human annotation.

3. **Disclose training hyperparameters** for both continual pre-training and fine-tuning (learning rate, batch size, optimizer, scheduler, steps/epochs) and provide details on the self-instruct data generation process (prompt templates, temperature, filtering criteria).

4. **Report language detection for all evaluation sets**, not just Vicuna and Safety Prompts, to rule out confounding from English responses in the toxicity and instruction-following evaluations.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>