## Summary
PLAGUE is a plug-and-play multi-turn jailbreaking framework that structures attacks into three sequential phases: a **Planner** that retrieves semantically similar successful strategies from a lifelong-learning memory bank, a **Primer** that builds adversarial context through progressively escalating benign-appearing queries, and a **Finisher** that delivers the final harmful query on a frozen context. Evaluated on HarmBench across five frontier models (OpenAI o3/o1, Deepseek-R1, Llama 3.3-70B, Claude Opus 4.1), PLAGUE achieves state-of-the-art ASR of 81.4% on o3 and 67.3% on Opus 4.1, substantially outperforming prior multi-turn baselines (GOAT, Crescendo, ActorBreaker).

---

## Strengths

- **Significant empirical results on frontier safety-resistant models.** PLAGUE improves over the strongest prior baseline by 32.1% on o3 (SRE 0.814 vs. GOAT's 0.587) and 40.2% on Opus 4.1 (SRE 0.673 vs. Crescendo's 0.48, Table 4). These are not marginal gains; they represent meaningful advances against models explicitly designed to resist jailbreaks.

- **Thorough, incremental ablation study.** Tables 3 and 4 decompose PLAGUE's gains component by component (GOAT → +BT → +R → +P → +RSS), cleanly attributing ~8.5% of the total 22.7% SRE improvement on o3 to the retrieval-augmented memory and showing similar trends on Opus 4.1. This level of rigor is rare in the jailbreaking literature.

- **Genuine plug-and-play modularity with demonstrated interchange.** The paper validates the modular claim empirically: substituting Crescendo for GOAT as the Finisher on Opus 4.1 gains +20.8% SRE (Table 4), and plugging ActorBreaker's planner improves diversity (Figure 3) at negligible ASR cost. This modular design offers concrete utility to red-teamers.

- **Model-specific vulnerability insights.** The paper identifies that different PLAGUE components are differentially important across models (backtracking dominates on Opus 4.1; reflection dominates on o3). This is a practically useful empirical insight that goes beyond headline ASR numbers.

- **Controlled budget evaluation.** All experiments enforce a 6-turn budget with K=2 (ASR@2), and baselines are re-run in the same environment, making cross-method comparison substantially fairer than what is common in the literature.

---

## Weaknesses

### Fatal
None.

### Major

1. **Attacker model confound for baselines.** The paper states that Deepseek-R1 is used as the attacker for PLAGUE, but it is unclear whether the re-run baselines (GOAT, Crescendo, ActorBreaker) also use Deepseek-R1 as their attacker LLM. If baselines were run with their original, weaker attacker models while PLAGUE benefits from the highly capable Deepseek-R1 reasoning model, then a substantial portion of the observed improvements may be attributable to attacker model strength rather than the PLAGUE framework architecture. The paper does not explicitly confirm that all baselines share the same attacker backbone, and this gap directly undermines the core comparative claim.

2. **Diversity metric underexplored in the main paper.** The abstract and introduction identify diversity as a primary goal of PLAGUE and cite its importance for comprehensive red-teaming. However, the main paper provides no concrete diversity measurements in Tables 2–5. Figure 3 (referenced in-text for diversity improvements) appears to be in an appendix not accessible in this review. Without quantitative diversity results in the main body, one of the framework's three stated design goals is inadequately supported.

3. **Memory bank contribution is marginal and poorly characterized.** Table 3 shows the retrieval of successful strategies (RSS) contributes only ~4.1% SRE improvement on o3 and ~3.4% on Opus 4.1, making it the smallest individual contributor. More importantly, the memory bank is seeded with only two Crescendo-derived strategies at initialization. The paper does not isolate how much improvement comes from the initial seed vs. strategies learned during the 200-goal evaluation run. This is crucial for evaluating the lifelong-learning claim: if seed strategies drive most of the gain, the lifelong-learning novelty is overstated.

### Minor

1. **StrongReject evaluation modification is underdescribed.** The paper uses a "slightly modified version" of the StrongReject evaluation prompt and a different evaluator model (Qwen3-235B instead of the original LLM used in StrongReject). The modifications and their impact on score calibration relative to published StrongReject scores are not explained.

2. **X-Teaming comparison is potentially unfair.** The paper attributes X-Teaming's poor performance to "fewer TextGrad steps" but does not report what step count was used or whether this was the configuration recommended by X-Teaming's authors. This raises the possibility that X-Teaming was undertuned while PLAGUE was fully optimized.

3. **Self-attack dynamic on Deepseek-R1.** Using Deepseek-R1 both as attacker and as one of the targets creates a setting where the attacker has possible implicit familiarity with the target's failure modes. While this may be unavoidable in practice, it deserves explicit acknowledgment.

### Trivial

- The abstract quotes "67.3% on Claude's Opus 4.1" but the main Table 2 shows 0.465 SRE for the default Opus 4.1 configuration; the 0.673 figure requires reading Table 4's footnote, which is a presentation choice that may confuse readers.

---

## Nice-to-Haves

- Include a confirmed statement that all baselines use Deepseek-R1 as attacker (or run an attacker-controlled ablation using the same attacker for all methods).
- Add a quantitative diversity metric (e.g., semantic diversity of generated attack plans across goals) to the main results table.
- Report how many strategies are learned during a single 200-goal run vs. used from the initial seed, to characterize the lifelong learning component's contribution more precisely.
- Provide an analysis of how ASR@1 compares to ASR@2 across methods to better characterize variance in multi-turn attacks.

---

## Novel Insights

PLAGUE offers two genuinely novel observations beyond its engineering contribution. First, strategy retrieval by **goal semantic similarity** outperforms AutoDAN-Turbo's **response similarity** approach, with the intuition that semantically related harmful goals share structural attack patterns regardless of response diversity. Second, the **Primer-Finisher separation** with a frozen context boundary addresses a known failure mode of end-to-end multi-turn methods (semantic drift), by decoupling context escalation from goal-directed querying. Together these suggest that multi-turn jailbreaking success depends less on adversarial prompt cleverness and more on **structured context engineering** — a framing that could influence how future defenses are designed, especially contextual monitoring mechanisms.

---

## Suggestions

- **Clarify attacker backbone for all baselines** in the experimental setup section (confirm or deny that GOAT, Crescendo, ActorBreaker, and X-Teaming all use Deepseek-R1 as attacker in the reported results).
- **Run an ablation with a weaker attacker** (e.g., GPT-4o or Llama 3.3-70B) to disentangle PLAGUE's framework gains from the Deepseek-R1 attacker's raw capability.
- **Add a diversity table** to the main paper, reporting intra-run semantic diversity of attack paths for each method.
- **Characterize memory growth**: report, for the 200-goal run, how many unique strategies were discovered and added to the library, and a learning curve showing ASR vs. number of completed goals.

---

## Score and Decision

PLAGUE is a well-executed paper on a high-impact safety topic. The three-phase architecture is well-motivated, the ablation is rigorous by the standards of the field, and the empirical results on o3 and Opus 4.1 are impressive. The main concern — whether baselines are run with comparable attacker models — is a real methodological gap that could substantially change the interpretation of the results. The lifelong-learning contribution, while novel in framing, is empirically modest and insufficiently characterized. These concerns warrant major revisions but do not invalidate the core contribution. The paper sits above the borderline.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>