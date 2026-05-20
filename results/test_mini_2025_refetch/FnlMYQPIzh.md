Now let me write the final consolidated review.

---

## Summary

This paper proposes ConvINT, a semi-structured intention framework that decomposes user utterances into four aspects (situation, emotion, action, knowledge), and a Weakly-supervised Reinforced Generation (WeRG) method that combines coarse (mapped from existing intents), mid (LLM-annotated), and fine (human-annotated) supervision signals with a tiered quadruple reward to generate ConvINT annotations at scale. Experiments on DuRecDial and ESConv evaluate annotation quality (automatic and human metrics) and downstream response generation.

## Strengths

1. **Sensible framework design with clear operationalization.** The ConvINT framework's four-aspect decomposition (situation, emotion, action, knowledge) is grounded in cognitive intention theories (Schröder et al., 2014; semantic pointers) and provides a concrete annotation schema that is more flexible than rigid slot-value ontologies but more structured than free-text summaries. The framework is clearly defined and easy to apply.

2. **WeRG consistently outperforms prompting baselines on annotation quality.** On both datasets, WeRG achieves the highest scores across F1, BLEU-1/2, BERTScore, and BARTScore (Table 1). For example, on DuRecDial, F1 improves from 0.5519 (CoT few-shot) to 0.5814, and BARTScore improves from -2.7762 to -2.3652. Human evaluation (Table 2) corroborates the trend, with WeRG ranking first on Informativeness, Understanding, and Conciseness on both datasets, with Fleiss' Kappa (0.39–0.49) indicating moderate inter-annotator agreement.

3. **Ablation studies isolate the contribution of each supervision tier.** Removing mid annotations collapses F1 from 0.5814 to 0.2355, while removing the tiered reward (w/o r_c) drops it to 0.5347 (Table 3). This differential degradation shows that the mid-level LLM annotations provide the bulk of training signal and that the reward hierarchy adds meaningful value beyond simply training on all data.

4. **Downstream task demonstrates practical value.** Incorporating ConvINT annotations into a response generation model (DuRecDial, Table 4) raises Success Rate from 0.7952 (CoT Prompt) to 0.8537 and reduces average turns from 3.86 to 3.37. This shows that the ConvINT annotations carry actionable signal for steering conversations.

5. **Component-level analysis validates each ConvINT aspect.** Removing the [EMOTION] aspect on ESConv causes the largest performance degradation (SR drops from 0.8445 to 0.7692, Table 5), confirming that the emotion dimension carries unique value for emotional-support dialogues and that the multi-aspect design is not cosmetic.

## Weaknesses

### Major

1. **Missing implementation details for the RL component.** The WeRG method is described via Equations (3)–(5) as a KL-regularized RL objective, but the paper does not specify: (i) which base LLM is fine-tuned (model name, size, checkpoint), (ii) which RL algorithm is used (PPO? DPO? REINFORCE? The formulation in Eq 5 resembles a DPO-style minimization, but this is not stated), (iii) the actual numerical reward values (the paper only says r_coarse < r_mid < r_fine, not the scalars or whether they are per-aspect), and (iv) training details (batch size, learning rate, convergence criteria). Figure 2 mentions LoRA but the text does not discuss it. These omissions make the method difficult to reproduce or assess. The "w/o r_c" ablation in Table 3 helps, but the gap between "w/o r_c" (0.5347 F1) and "Ours" (0.5814 F1) is modest, and without knowing what training procedure "w/o r_c" exactly corresponds to, readers cannot assess whether the RL objective is genuinely being optimized.

2. **Baselines for annotation quality evaluation are too weak.** The only baselines (Direct Prompt, CoT Prompt) are zero-shot/few-shot prompting methods that do no fine-tuning. Comparing a fine-tuned RL model against prompt-only methods conflates the effect of fine-tuning with the effect of the RL objective. The "w/o r_c" ablation in Table 3 partially addresses this by removing the reward signal, but there is no *supervised fine-tuning* baseline trained *separately* on each data source (e.g., SFT on D_fine only, SFT on D_mid only, SFT on all data without any RL framing). Such baselines would be needed to isolate whether WeRG's reward hierarchy provides a benefit beyond simply training on more data. The w/o D_mid ablation shows that removing mid data hurts, but this is expected (mid data is the largest source) and does not validate synergy.

3. **No error bars or statistical significance in any table.** Every table reports point estimates without standard deviations, confidence intervals, or pairwise significance tests. Given the modest margins (e.g., +0.03 F1 on DuRecDial vs. CoT few-shot), it is unclear whether the reported advantages are reliable. This is particularly important for the human evaluation where differences are ~0.2–0.4 on a 0–5 scale.

### Minor

4. **Downstream experiment (Table 4) could more directly validate WeRG.** Section 4.5.3 states that "ConvINT data generated by the WeRG method" is used, and the caption says "CoT ConvINT denotes the CoT Prompt enhanced by the proposed ConvINT framework." The experiment shows that adding ConvINT annotations to the response generator improves results, which validates the framework. However, it does not compare WeRG-generated annotations against an alternative set of ConvINT annotations (e.g., from a prompt-only method or from SFT). A cleaner comparison would pit WeRG-generated annotations against prompt-generated annotations in the downstream task, which would directly test the claim that WeRG's specific quality matters for downstream utility.

5. **Dataset statistics and annotation counts are missing.** The paper gives overall dataset sizes (16.5K dialogues for DuRecDial, 1,300 cases for ESConv) but does not report: how many instances per train/dev/test split, how many coarse/mid/fine annotations were created, what proportion of the data each tier constitutes, or how many human annotators produced the fine data and what their agreement was (beyond the Fleiss' Kappa for the evaluation task). These numbers are essential for understanding the experimental scale and the weak supervision setup.

6. **Moderate novelty of the four-aspect decomposition.** The ConvINT framework organizes user intentions into situation, emotion, action, and knowledge. While the citation of psychological theory provides a principled framing, many dialogue systems already track these dimensions (context, emotion, user actions, entities) in practice. The paper does not demonstrate that specific design choices flowed from the cited theory in a way that diverges from a commonsense or ad-hoc decomposition.

### Trivial

7. **Ambiguity in the Table 4 caption.** The caption "CoT ConvINT denotes the CoT Prompt enhanced by the proposed ConvINT framework" could be read as using the framework *concept* as a prompt structure rather than using WeRG-generated annotations. The main text resolves this ("ConvINT data generated by the WeRG method"), but the caption should be aligned for clarity.

8. **Table 3 reports proportion vs. BARTScore in Figure 3's table but the relationship is unclear.** In the Figure 3 table, BARTScore becomes *more negative* as proportion increases (e.g., -2.3652 at 10% → -2.75 at 30%), which means the score is getting *worse* (BARTScore is negative and lower is better). But the text says "model performance improves with stable gains." If BARTScore is getting more negative, that's actually improvement (more negative is better). This is correct but the table layout is confusing.

## Nice-to-Haves

- **SFT baselines on individual data sources** would strengthen the claim that WeRG's tiered reward provides a specific advantage over simply fine-tuning on all available data.
- **Qualitative examples** of generated ConvINT labels from each method would help readers understand what quality differences look like in practice.
- **Error analysis** of where WeRG succeeds and fails (e.g., which aspects are hardest to generate) would add depth.

## Removed Points

- **"The downstream evaluation does not test the method's core claim"**: The harsh critic claimed that WeRG annotations are "never used" in the downstream experiment. This is factually incorrect — Section 4.5.3 explicitly states: "We further validate the effectiveness of applying the **ConvINT data generated by the WeRG method** to downstream conversational applications." The critic appears to have misread the caption. Removed.
- **"Automatic metrics are poorly suited for free-form annotations"**: This is a generic concern applicable to most text generation tasks. The paper already includes human evaluation and BERTScore/BARTScore as complementary semantic metrics. The concern is not specific enough to constitute a genuine paper weakness (it does not invalidate the comparison since all methods are evaluated on the same metrics). Removed.
- **Reproducibility nitpicks about trivial details (hyperparameters, training logs)**: Removed per formatting rules.
- **Missing related works**: Removed per rules — I cannot confirm what related works exist.
- **The harsh critic's "Section-by-Section Notes" section**: These are general observations, not structured weaknesses. Most are already subsumed by the weaknesses above.
- **"framework's four aspects ... are not particularly novel" claim from harsh critic**: While I note this as a minor weakness above, the critic's stronger characterization ("not particularly novel — many dialogue systems already track context, emotion...") overstates the case. Cited psychological theory provides grounding, and the paper is the first to formalize this specific four-aspect decomposition as a unified annotation frame. Retained as a minor point rather than major.
- **Strength Finder's claim about "principle-grounded multidimensional decomposition"**: Overstated. The paper cites semantic pointers and Schröder et al. but does not show how the theory uniquely determined the four aspects. I kept a diluted version and moved the original strong claim here.
- **Strength Finder's strength #3 about "Clear downstream utility"**: Merged with strength #4 in my list.

## Novel Insights

None beyond the paper's own contributions. Both reviewers identified the core strengths and weaknesses accurately; no unexpected finding emerged from the synthesis.

## Suggestions

1. Add an SFT baseline trained on the combined coarse+mid+fine data without the RL reward to directly isolate WeRG's specific advantage.
2. Specify the base LLM, RL algorithm, and exact reward values used. If the optimization reduces to a weighted supervised loss (as the DPO-style formulation in Eq 5 suggests), state this explicitly.
3. Report standard deviations or bootstrap confidence intervals for all main results.
4. Provide dataset statistics (split sizes, annotation counts per tier).
5. Clarify the Table 4 caption to explicitly state that WeRG-generated annotations are used.
6. Include qualitative examples of generated ConvINT labels.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing (all on conversational/intent/RL topics):**
- Weak band (<3.5): Papers at avg 2.33–3.00 (clear rejects, weak relevance). ConvINT is substantially stronger.
- Middle band (3.5–7.5): IntentGPT (4.40, Reject), GROOT-2 (5.50, Accept Poster), Modeling Future Turns (6.00, Accept Poster), ACT (6.25, Accept Poster). ConvINT is weaker than ACT (6.25) and Modeling Future Turns (6.00) but stronger or comparable to IntentGPT (4.40).
- Strong band (>7.5): Oral-level papers (7.75–8.00). ConvINT does not approach this level.

**Round 2 — Narrowing (4.5–7.0):**
- Supervised Knowledge (5.00, Accept Poster): Similar level of methodological contribution. Both papers propose a framework with moderate novelty, have some baseline concerns, and were accepted/rejected at the borderline. ConvINT has more experiment dimensions (human eval, ablation, downstream) but similar depth issues. Comparable.
- IDEAL (6.00, Accept Poster): Stronger — has theoretical analysis, more rigorous evaluation. ConvINT does not reach this level.
- Zero-Shot Goal-Directed Dialogue (5.33, Reject): Similar approach (RL for dialogue) but was rejected. ConvINT has more comprehensive experiments. Slightly stronger.
- X-SHOT (4.75, Withdrawn/Reject): Weaker contribution. ConvINT is clearly stronger.

**Round-1 bracket**: [4.5, 6.5]
**Round-2 narrowing**: ConvINT sits at ~5.0 — comparable to Supervised Knowledge (5.00, poster accepted) and stronger than IntentGPT (4.40, rejected), but clearly weaker than IDEAL (6.00, poster accepted) and ACT (6.25, poster accepted). The missing implementation details, weak baselines (no SFT comparison), and absent error bars prevent the paper from reaching the 5.5+ range, but the framework and WeRG method provide a substantive enough contribution to sit above clear-reject territory.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>