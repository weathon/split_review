- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6
Now I have all the evidence I need. Let me produce the final consolidated review.

---

## Summary

AutoAgents proposes a framework that dynamically generates a team of specialized LLM agents through a multi-agent drafting-stage discussion (Planner, Agent Observer, Plan Observer), then executes tasks via self-refinement and collaborative refinement actions. The core idea — using multi-agent dialogue to *generate* the agent team itself rather than relying on handcrafted role assignments — is novel and well-motivated. However, the experimental evidence is insufficient to support the paper's central claims of superiority over existing multi-agent frameworks, primarily due to missing baselines, an undersized ablation study, and unsupported overclaims in the text.

## Strengths

- **Novel dynamic agent generation via multi-agent discussion.** AutoAgents is the only framework in Table 1 that generates agents through "Multi-agent Discussion" rather than a single LLM call or no dynamic generation at all. The drafting stage (Planner + Agent Observer + Plan Observer) is a genuine architectural innovation over prior work like SSP and AgentVerse, which generate agents through a single model. This is concretely supported by Table 1 and the detailed description in Section 3.1.

- **Clear improvement over standard prompting and SSP on Trivia Creative Writing (N=5).** For N=5, AutoAgents achieves 82.0% vs SSP's 79.9% (+2.1% absolute) and vs Standard Prompting's 74.6% (+9.9%). These gains are verified in Table 3 and show the framework's capability on knowledge-intensive creative writing.

- **Systematic ablation providing directional evidence for each component.** Table 5 shows that removing observers, self-refinement, collaborative refinement, or dynamic memory each reduces performance relative to the full system (90.0% → 87.0%, 87.0%, 88.0%, 89.0% respectively). While the sample size (20 instances) is too small for statistical confidence, the ablation structure is sensible and the qualitative case study in Figure 5 (Planner comparison with/without observers) provides complementary illustration.

- **Well-structured method description.** The two-stage design (Drafting + Execution) is clearly explained, the three memory types (short-term, long-term, dynamic) are sensible mechanisms for addressing token limits, and Algorithm 1 provides a complete procedural specification.

## Weaknesses

### Fatal
None.

### Major

- **Missing multi-agent baselines on both benchmarks, despite explicit claims of superiority.** The paper's central claim is that AutoAgents "outperforms other generated-agent frameworks" (Section 1, line 41) and "generates more coherent and accurate solutions than the existing multi-agent methods" (Abstract). Yet:
  - On **Open-ended QA** (Table 2), AutoAgents is compared only against *individual* LLMs (ChatGPT, Vicuna-13B, GPT-4). No multi-agent framework (SSP, AgentVerse, AutoGen, etc.) is evaluated. This means the reader cannot tell whether the reported win rates stem from AutoAgents' dynamic agent generation or simply from the overhead of multi-turn LLM calls.
  - On **Trivia Creative Writing** (Table 3), only SSP is compared. AgentVerse — which the paper itself categorizes as a "generated-agent framework" (Table 1) and explicitly references as a "counterpart" — is **not evaluated**.
  - Critically, the paper states: "The empirical data presented in Table 2 and 3 further accentuate the superiority of AutoAgents when juxtaposed against counterparts like AgentVerse and SPP" (Section 4.3, line 337). This is a **verifiable overclaim**: Table 2 contains no AgentVerse comparison whatsoever, and Table 3 compares only SPP. The paper asserts a conclusion that its own data cannot support.

- **Ablation study on only 20 instances lacks statistical credibility.** The ablation (Table 5) uses "the last 20 samples from a dataset of 100 samples" (Section 4.3, line 307). No confidence intervals, variance, or significance tests are reported. The scores on this 20-instance subset are notably different from the full 100-instance results (e.g., SPP scores 84.4% on the subset vs 79.9% on the full set for N=5), confirming that the subset is not representative. Observed differences of 1–3% between ablated variants could easily be artifacts of random variation on such a small sample.

### Minor

- **Improvement over SSP on N=10 is marginal and unreliably measured.** For the harder setting (N=10), AutoAgents scores 85.3% vs SSP's 84.7% — a 0.6% absolute difference. The metric is string matching against answer variants (Section 4.2, line 300), which has known limitations with synonyms and paraphrases. No statistical significance is reported. The paper's framing as a decisive improvement is overstated given this narrow margin.

- **Open-ended QA evaluation is underspecified and lacks baselines.** Only win rates are reported (Table 2), with no absolute quality scores. The human evaluation ("several volunteers," line 269) provides no information on number of raters, rating instructions, or inter-rater agreement. Without multi-agent baselines, it is unclear whether the reported win rates reflect the value of dynamic agent generation or just the added compute from multiple GPT-4 calls.

- **The paper claims superiority over AgentVerse without evaluating it.** As detailed above, AgentVerse is listed as a "counterpart" and the text claims the data shows superiority over it (line 337), but no experimental comparison appears anywhere in the paper. This goes beyond a missing baseline — it is an explicit claim that the data do not support.

### Trivial
None.

## Nice-to-Haves

- **Cost/overhead analysis.** AutoAgents makes many GPT-4 calls (drafting-stage discussions, observer loops, self-refinement and collaborative refinement iterations). An analysis of token cost vs. performance gain — especially given the +0.6% improvement on N=10 — would help practitioners assess the practical trade-off.
- **Failure case analysis.** The paper reports only successful examples. Understanding when dynamic agent generation fails (e.g., drafting-stage convergence to a poor agent team) would strengthen the contribution.

## Removed Points

- **"Table 1 classification conflates single-profile generation with single-agent system."** The column "Dynamic Agent Generation Method" describes *how* agents are generated, not how many exist. Systems with "Single Agent" generation (e.g., Social Simulacra with 25 agents, AgentVerse with unlimited agents) generate many agents through a single LLM call; AutoAgents uses multi-agent discussion. The distinction is valid and the table is correctly labeled. **Removed as a misunderstanding.**

- **"Reliance on a single underlying LLM is a limitation."** Nearly all LLM-based multi-agent systems (MetaGPT, AutoGen, AgentVerse, etc.) use the same underlying model with different prompts for different roles. This is a field-wide characteristic, not a weakness specific to this paper. **Removed as not a valid weakness.**

- **"No failure analysis" / "No cost analysis."** Moved to Nice-to-Haves. These are suggestions for enrichment, not core weaknesses.

- **"Prompts not provided."** The appendix is stripped by the parser; prompts would be in the original submission. **Removed per instructions.**

- **"The overall evaluation lacks rigor" (generic framing).** The harsh critic's sweeping concerns about "evaluation validity" and "comparison fairness" are anchored to specific points (missing baselines, small ablation, etc.) which are retained above. The generic framing is removed; the specific criticisms are kept in the Major/Minor sections.

- **Strength Finder's generic/superficial strengths.** Claims like "this paper addressed an important problem" are removed. The concrete strengths (novel method via Table 1, quantitative improvement in Table 3, ablation structure, memory mechanism) are retained.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between a genuinely novel method design and a substantially undersupported experimental evaluation, but this is a standard observation for papers in this state.

## Suggestions

1. **Add at least two multi-agent baselines** — SSP and AgentVerse are the most natural — to the Open-ended QA task. Report both win rates and absolute quality scores.
2. **Run ablations on the full 100-instance Trivia set** (or a properly powered random sample) with confidence intervals or bootstrap estimates. The current 20-instance ablation is not trustworthy.
3. **Remove or qualify the claim of superiority over AgentVerse** unless AgentVerse is actually evaluated. The current text (line 337) makes an explicit claim that the reported data do not support.
4. **Report variance or significance** for all main results. Even a simple bootstrap confidence interval would substantially improve credibility.
5. **Describe the human evaluation protocol** (number of raters, instructions, inter-rater agreement). Currently it is underspecified to the point of being unreproducible.
