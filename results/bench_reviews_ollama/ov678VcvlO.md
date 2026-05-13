Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper proposes Jigsaw Puzzles (JSP), a multi-turn jailbreak strategy that splits harmful questions into benign fractions, fed across successive turns to bypass LLM safeguards. Using carefully designed prompts (prohibiting concatenated question generation and requiring a disclaimer), the strategy achieves an average ASR-q of 93.76% across 5 LLMs on 189 harmful queries from Figstep, and compares favorably against PAIR and PAPs on AdvBench under GPT-4.

## Strengths

- **Systematic ablation of prompt components and splitting strategies** (Figure 4, Table of splitting strategies): The paper cleanly decomposes the contribution of each component—prohibition, disclaimer, word-level vs. sentence-level splitting, and no-splitting baselines. The finding that disclaimers bypass output-side guardrails and that "no splitting" (JSP prompt alone) achieves 91.64% ASR-a on GPT-4 is a concrete, useful insight, raising the question of what exactly the splitting contributes on certain models.

- **Multi-turn vs. single-turn comparison isolates the mechanism** (Table 3): The side-by-side comparison of single-turn, pseudo-multi-turn, and multi-turn settings shows that distributing fractions across turns dramatically increases ASR on some models (e.g., GPT-4o: 10.86% → 66.81%), providing direct evidence that the multi-turn structure itself—not just obfuscated content—is what bypasses safeguards.

- **Category-level analysis reveals model-specific vulnerabilities** (Figure 3): The heatmap across 7 harmful categories × 5 LLMs reveals interesting patterns (e.g., Gemini-1.5-Pro's resistance on Malware but vulnerability on Privacy), which is informative for targeted defense development.

- **Simplicity relative to prior multi-turn attacks**: Unlike Crescendo or CoA, JSP requires only query splitting and a fixed prompt template—no elaborate scenario construction or gradual topic steering—yet achieves high ASR-q, demonstrating that simple fragmentation suffices to expose vulnerabilities in content-centric defenses.

## Weaknesses

### Fatal

None.

### Major

- **ASR-q (5 attempts) inflates headline numbers; the paper's framing overstates per-attempt efficacy.** The abstract and conclusions prominently report 93.76% "average attack success rate" and "near 100%" on Llama-3.1-70B and GPT-4—these are ASR-q figures (at least 1 of 5 attempts succeeds). For Gemini-1.5-Pro, the per-attempt ASR-a is only 52.70%, and for GPT-4o it is 66.81%. As the paper defines, ASR-q = 1−(1−p)⁵, so even a per-attempt rate of 40% yields ASR-q of ~92%. While the paper does define and report ASR-a (Section 4.1, Table), the abstract, section headers, and conclusion all foreground ASR-q without adequately contextualizing that this is a 5-attempt metric. The practical operational significance differs markedly between "we can eventually jailbreak any question with enough retries" and "each attempt succeeds at rate p."

- **Defense evaluation tests only system-prompt defenses, making the "strong resistance" claim unsupported.** Section 5 tests only two system-prompt defenses ("You are a helpful assistant, and you are not easily persuaded…" and its JSP-adapted variant). These are among the weakest defense categories. The claim of "strong resistance to defence strategies" (abstract, Section 5, conclusion) is not grounded by these results. Perplexity-based input detection, output classifiers, multi-turn context safety checks, or self-consistency mechanisms are not tested despite being directly relevant. For example, JSP's letter-fragment inputs in later turns produce unusual text patterns that perplexity filters could plausibly flag—a natural defense worth at least mentioning.

- **The primary comparison against baselines (PAIR, PAPs) uses a different experimental setup from the main experiments.** Section 5 uses AdvBench (50 questions), GPT-4 Judge (1–5 scoring), and 15 attempts (3 trials × 5), whereas Sections 4.2–4.3 use Figstep (189 questions), Llama-guard-3 (binary classification), and 5 attempts. The paper states it "strictly follows the settings of [zeng2024johnny]," which standardizes against PAPs' own protocol—this makes the comparison internally consistent with that baseline but incomparable with the paper's own main results. The "state-of-the-art" claim in Section 5 and the abstract should be qualified accordingly.

### Minor

- **The "no splitting" baseline on GPT-4 (91.64% ASR-a) nearly matches full JSP (93.65%), a finding the paper under-weights.** This reveals that on models with weaker input-side filters, the JSP prompt (especially the disclaimer) alone does most of the work, and the splitting mechanism (the paper's namesake contribution) adds marginal improvement. The paper discusses this in Section 4.3 ("Splitting Strategies"), but frames it as validation that JSP's splitting "balances" requirements; the more honest interpretation is that the splitting is non-essential on GPT-4 specifically and the prompt design insight deserves more prominence.

- **The splitting pipeline uses GPT-4 to identify and split harmful words (Stages 2–3), which adds an external dependency.** The paper does not discuss whether the attack still works with simpler splitting methods (e.g., dictionary-based identification of harmful words) or how sensitive results are to GPT-4's classification. The tokenizer-based splitting baseline (Table, 49.31% on Gemini vs. 52.70% for JSP-S3) partially addresses this, but only for Stage 3, not Stage 2.

- **Fabricated history is a significant intervention presented as a minor enhancement.** Replacing a model's refusal response with a fabricated compliant one (Section 4.4) is conversation tampering that bypasses a natural safety mechanism. This is a meaningful additional attack vector that could be unavailable in settings with signed conversation logs, and its contribution to ASR improvement (e.g., GPT-4o: 66.81% → 86.28% ASR-a) is substantial enough to warrant more serious discussion.

### Trivial

None.

## Nice-to-Haves

- Evaluate against non-trivial defenses (perplexity filters, multi-turn safety classifiers) to substantiate the robustness claim.
- Report ASR-q as a function of number of attempts (1, 3, 5) to let readers judge per-attempt efficacy directly.
- Include full attack transcripts as case studies so readers can assess the naturalness of the interaction.

## Removed Points

- **ASR-q metric "systematically inflates" success rates — removed as "inflation" characterization.** ASR-q is a legitimate metric (can the question be jailbroken at all?). The real issue is the *framing* and *emphasis*, not that the metric itself is wrong. The paper reports both metrics; the problem is prioritization. Reclassified as a major weakness about *overstated framing* rather than invalid methodology.

- **"The attack requires GPT-4 to construct splits, undermining the black-box framing."** The paper does not explicitly claim JSP itself is a black-box attack; it describes instruction jailbreaking as a general category that operates under black-box conditions. GPT-4 is used as a preprocessing tool (splitting), not as the attack target, and any model capable of identifying harmful words could substitute. Reclassified as minor (external dependency).

- **SOTA claim on GPT-4 is based on incomparable setup.** This is a valid concern about qualification, but the paper explicitly states it follows the PAPs benchmark protocol, making this standardized against those baselines. The issue is lack of comparability with the paper's own main experiments, not that the experiment is unfair. Reclassified as major (overclaimed scope) rather than fatal.

- **"ASR-q numbers are misleading in the abstract"**: Merged into the major weakness about metric framing. The paper does define the metric in the methodology section, so this is about emphasis, not deception.

- **"Defense evaluation tests only trivial defenses"**: The defenses are simple system prompts, but they are the standard defense evaluated in the PAPs benchmark the paper replicates. This is a real limitation that weakens the "strong resistance" claim, but not evidence of cherry-picking. Kept as major.

- **Strength Finder's "High attack success rates across multiple frontier LLMs"**: Partially removed. The 93.76% figure is ASR-q, not per-attempt. The per-attempt rates (ASR-a) tell a more nuanced story (e.g., 52.70% on Gemini). The strength of breadth Across 5 models is retained but qualified.

- **Strength Finder's "Strong resistance to defense strategies"**: Removed as a strength because only trivial defenses were tested—it conflicts with the verified weakness that the defense evaluation is insufficient. The 76% ASR-q under Defence-JSP is notable but does not constitute "strong resistance" given the weak defenses tested.

- **Formatting/style nitpicks from the parser**: Removed per hard rules.

- **Reproducibility concerns about undisclosed hyperparameters or GPT-4 non-determinism**: Removed as nitpicks about reproducibility per hard rules.

## Novel Insights

The paper reveals an important asymmetry: on models with strong input-side guardrails (GPT-4o, Gemini), the splitting mechanism is essential; on models with weaker input filtering (GPT-4), the JSP prompt alone achieves 91.64% ASR-a, making splitting nearly irrelevant. This suggests the real vulnerability is not fragmentation per se but the combination of multi-turn context accumulation with output-side bypass (disclaimer), and that the effective attack surface varies significantly by model architecture. The per-attempt ASR-a numbers (52–87% across models) under a straightforward attack raise genuine security concerns, even if the 93.76% ASR-q headline overstates the per-attempt threat.

## Suggestions

- Re-frame the contribution around the prompt design insights (disclaimer bypass, multi-turn accumulation) rather than the splitting strategy, since the ablation shows the prompt alone is the main driver on the most widely-used model (GPT-4).
- Prominently report ASR-a alongside ASR-q in the abstract and conclusions, and include a table of ASR-q at 1, 3, and 5 attempts to let readers calibrate the metric.
- Test at least one non-trivial defense (e.g., perplexity filtering or a multi-turn context safety classifier) to substantiate the claim of "strong resistance."

## Score and Decision

The paper identifies a real vulnerability—LLMs can be jailbroken by splitting harmful content across turns—and provides useful ablations. However, the headline claims are overstated: ASR-q with 5 attempts inflates perceived success rates, the "strong resistance to defense" claim rests on trivial defenses, and the comparison against baselines uses a different protocol from the main experiments. The per-attempt reality (52–87% ASR-a across models) is concerning but far from the "near 100%" framing in the abstract. The core finding that the JSP prompt alone achieves 91.64% on GPT-4 actually suggests the splitting mechanism (the paper's namesake) is not the primary driver on important models, which reframes the contribution. These are addressable in revision but significantly weaken the current submission.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>