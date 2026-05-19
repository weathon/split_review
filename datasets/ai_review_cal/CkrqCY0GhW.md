- Decision: Reject
- Avg Score: 6.50
- Scores: 6, 8, 6, 6
Now I have all the information needed to verify the reviewer claims against the actual paper. Let me produce the final consolidated review.

## Summary
This paper introduces CompWoB, a benchmark of 50 compositional web automation tasks derived from MiniWoB primitives, and studies how language model agents (LMAs) generalize to task combinations. The main finding is that prompted LMAs (e.g., GPT-3.5/4 with RCI, AdaPlanner, Synapse) drop from 94.0% on base tasks to 24.9% on compositional tasks, while finetuned/transferred LMAs (WebGUM, HTML-T5++) drop less (85.4% → 54.8%). The paper also proposes HTML-T5++, a finetuned model trained with data-rebalancing, and analyzes factors affecting compositional difficulty (instruction length, HTML depth).

## Strengths
1. **Controlled benchmark design for compositional web automation**: CompWoB provides 50 systematically constructed compositional tasks across five subtypes (two-way, three-way, n-way, transition, easy-medium), with explicit page transitions and reverse-order instruction variants. This enables tractable analysis of compositional generalization beyond single-task evaluation (Section 5, Figure 1).

2. **Clear and non-obvious performance reversal**: The paper demonstrates that prompted LMAs (strong on base tasks at 94.0%) degrade to 24.9% on compositional tasks, while transferred LMAs (weaker on base tasks at 85.4%) degrade to only 54.8%. This inversion — prompted agents being stronger on base tasks but much weaker on composition — is a concrete, empirically-supported finding (Figure 2, Section 6.1).

3. **Data-rebalancing yields best compositional performance**: By collecting 77K additional demonstrations and reducing easy-task episodes by 50%, HTML-T5++ achieves 95.2% on MiniWoB (best among finetuned LMAs) and 61.5% zero-shot on CompWoB — the best among all compared LMAs (Table 1, Figure 2, Section 4.5).

4. **Quantified sensitivity to instruction order**: The reverse-order instruction experiment shows that both prompted and transferred LMAs degrade significantly, with transferred LMAs dropping from 54.8% to 31.0% and prompted from 24.9% to 18.0%, supported by failure examples (Figure 3, Section 6.2, Table 3).

5. **Correlation analysis of compositional difficulty factors**: The paper identifies three statistically significant predictors of CompWoB performance — synthesized base-task success rate (R=0.691, p<0.01), instruction token count (R=-0.579, p<0.01), and HTML subtree depth (R=-0.433, p<0.01) — linking compositional difficulty to observable task features (Figure 5, Section 6.4).

## Weaknesses

### Fatal
None.

### Major
- **Unsubstantiated human-level performance claim**: The abstract and text (lines 9, 28, 34, 103) repeatedly claim that HTML-T5++ "surpasses human-level performance (95.2%)" or achieves "super-human performance" on MiniWoB, yet the paper never states the actual human baseline number or provides a citation for it. Table 1's caption mentions "competitive performance to... humans" but does not report the human success rate. This claim is both central (used to establish HTML-T5++'s credibility as a baseline) and empty without supporting evidence. The authors must either provide and cite the human baseline or retract the claim.

### Minor
- **AdaPlanner evaluated with suboptimal backbone in main comparison**: The paper states that AdaPlanner "has been reported that LLMs more capable of code generation perform better, such as text-davinci-003 than gpt-3.5-turbo" (Section 4.2, line 79). Yet the main experiments (Figures 2 and 3) use gpt-3.5-turbo for all prompted LMAs, including AdaPlanner. Section 6.3/Figure 4 separately tests AdaPlanner with text-davinci-003 and shows substantial improvement (from ~18% to ~40% on CompWoB). While the paper is transparent about this choice and the core finding (prompted < transferred on composition) is robust even with the correct backbone, the internal ranking among prompted methods (RCI > AdaPlanner) is based on conditions known to disadvantage AdaPlanner. The paper should acknowledge this more explicitly or use consistent backbones.

- **Correlation analysis lacks controls for confounding**: Section 6.4 reports three separate pairwise correlations (synthesized success rate, instruction token count, HTML depth) but does not test whether these factors are independently predictive (e.g., through partial correlations or regression). The claim that "depth rather than length matters" is suggestive but not rigorously established without controlling for the other variables (Section 6.4, line 171).

- **Failure modes not systematically quantified**: Tables 2 and 3 provide illustrative failure examples (missing steps, incorrect XPath, wrong action types), but the paper does not report the frequency distribution of these failure types across the 5,000 episodes. A systematic categorization would strengthen the analysis (Sections 6.1, 6.2).

- **Data collection protocol for 77K additional demonstrations underspecified**: Section 4.5 describes collecting 77K demonstrations via Synapse across 16 tasks, but does not specify whether the demonstrations were filtered by task success, how many episodes per task were collected, or whether Synapse was run with any modifications (lines 103-105).

### Trivial
None.

## Nice-to-Haves
- Report per-model CompWoB success rates for all transferred LMAs explicitly in the text (the abstract and Section 6.1 give the average of 54.8% and HTML-T5++ at 61.5%, but individual WebGUM/HTML-T5 numbers are only available in Table 4, an embedded image).
- Include a table or figure showing per-task success rates across methods to understand variance across compositional tasks.
- Add partial correlations or a regression analysis to disentangle the effects of instruction length, HTML depth, and base-task difficulty on compositional performance.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **Figure-text inconsistency (Critic's #1)**: The critic claims Figure 2 shows WebGUM at ~40% contradicting the 54.8% average. However, 54.8% is the **average across multiple transferred LMAs**, not WebGUM's individual score. The text never claims WebGUM individually achieves 54.8%. Without being able to verify the precise figure bars (embedded image), and given that the paper's stated numbers (average=54.8%, HTML-T5++=61.5%) are internally consistent, this criticism is not verifiable from text and may be based on misreading the figure.

2. **"Optimal exemplar retriever" overclaim (Critic's #4)**: The paper says "We assume the optimal exemplar retriever throughout experiments" (line 124) but actually tests multiple fixed exemplar strategies (first-task, second-task, combination) and reports the best. For Synapse, this is explicit: "best exemplars (i.e. maximum score between (1) and (2))." This is a reasonable proxy for optimal retrieval. The claim is slightly imprecise but not misleading — the paper fully describes what was done.

3. **Missing task list table**: The 50-task list (categories, combinations) is in the appendix, which the parser stripped. Per hard rules, this is not a valid criticism.

4. **AdaPlanner comparison "misleading"**: Despite the suboptimal backbone concern (retained as Minor above), the critic's stronger framing — that the paper's conclusion is misleading — is unwarranted. The paper is transparent about using gpt-3.5-turbo (stated in every figure caption and the methodology section), separately tests the intended backbone in Section 6.3, and the core finding (transferred > prompted on composition) holds even with the correct backbone.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Provide the human baseline**: Either cite the source of human-level performance on MiniWoB (e.g., from Shi et al., 2017 or the original RCI paper) or retract the "surpasses human-level" claim. A simple statement like "human performance on MiniWoB is X% (source)" would suffice.
2. **Run AdaPlanner with text-davinci-003 in the main comparison or add an explicit caveat** that the main results under-represent AdaPlanner's capability, and avoid drawing strong comparative conclusions among prompted LMAs based on the gpt-3.5-turbo-only setup.
3. **Add partial correlations or regression** to the correlation analysis to establish whether HTML depth independently predicts difficulty after controlling for instruction length and base-task success rate.
4. **Quantify failure mode frequencies** across all 5,000 episodes so readers can see the prevalence of each error type.
