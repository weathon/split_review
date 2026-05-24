Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper proposes ARPO, an RL algorithm for training multi-turn LLM-based agents that use external tools. The core idea is an entropy-based adaptive rollout mechanism: after observing that token entropy spikes sharply after tool-call steps, ARPO triggers partial branching at high-entropy points to explore alternative tool-use behaviors. It also employs an advantage attribution scheme (hard/soft) operating over the shared and individual token segments created by branching. Experiments across 13 benchmarks spanning mathematical reasoning, knowledge-intensive QA, and deep search show consistent accuracy improvements over trajectory-level RL methods (GRPO, DAPO, REINFORCE++), with competitive tool-use efficiency.

## Strengths

1. **Well-motivated, grounded algorithmic idea.** The pilot experiment (Figure 2, Ob.1–3) provides direct evidence that LLM token entropy spikes after tool calls — a phenomenon trajectory-level RL ignores. Section 3.1 formalizes this into a branching mechanism (Eq. 2) that adaptively expands sampling at precisely these steps. The motivation is clear, the observation is reproducible, and the algorithm follows naturally from it.

2. **Consistent empirical gains across a broad evaluation.** Table 1 shows ARPO outperforming GRPO, DAPO, and REINFORCE++ on all 10 mathematical and knowledge-intensive reasoning tasks for both Llama3.1-8B and Qwen2.5-7B backbones. The gains are modest (2–6% typically) but consistent — no cherry-picked datasets or models. Table 2 further demonstrates strong deep-search results with only 1k RL training samples, surpassing much larger models (GPT-4o, DeepSeek-R1-671B) on GAIA and HLE.

3. **Rollout diversity analysis provides supporting evidence for the mechanism.** The PCA+DBSCAN analysis (Figure 7b) shows ARPO produces 54 distinct trajectory clusters vs. 48 for GRPO, with greater intra-cluster compactness and inter-cluster separation. This quantitatively confirms that entropy-guided branching actually yields more structured exploration, not just more trajectories.

## Weaknesses

### Major

1. **The "half the tool-call budget" efficiency claim is overstated and not properly controlled.** This claim appears in the abstract (line 19), contribution list (lines 57, 62), body (line 290), and conclusion (line 312), yet the evidence does not fully support it. Figure 7a compares tool-call counts during training for ARPO (~250–300) vs. GRPO (~400–450) on a single model (Qwen2.5-7B). This is roughly a 35–40% reduction, not 50%, and the comparison is only against one baseline, with no controlled experiment matching computational budgets (e.g., does GRPO with ARPO's tool-call budget perform worse?). Moreover, the main results tables (Tables 1–2) report only accuracy, not tool-call counts, so readers cannot verify the efficiency claim against other methods or models. This overclaiming weakens a central advertised contribution.

### Minor

2. **The "Advantage Attribution Estimation" framing overstates novelty.** Section 3.2 presents both hard and soft advantage settings, but the default (soft) *retains the original GRPO loss formulation* (line 154: "While we retain the original GRPO loss formulation"). The paper correctly notes that GRPO's importance sampling ratio automatically distinguishes shared vs. individual tokens in branched trajectories (Eq. 4), so the distinction is a natural consequence of the partial rollout — not a new credit assignment method. The hard variant is a genuine modification but performs worse (Figure 5) and is not used. The paper would be better served by presenting the core contribution as *entropy-guided partial rollout applied to GRPO* rather than as a separate advantage estimation contribution.

3. **No statistical significance or variance reporting.** All tables report point estimates without standard deviations, confidence intervals, or significance tests. Given that improvements over GRPO are often 2–4%, it is unclear whether these gains are reliable or within the noise of a single run. This is a standard expectation for experimental RL papers.

4. **Several key hyperparameters receive no sensitivity analysis in the main paper.** The branching mechanism introduces α, β, τ, Z, k, M, and N (Section 3.1), whose values could significantly affect behavior. The paper references Appendix A.2 for "more ablation and scaling analyses," but the main paper offers no summary of which parameters matter most or how robust the method is to their settings.

### Trivial

5. **The computational complexity claim (line 128) is questionable.** The paper states ARPO reduces complexity from O(n²) to between O(n log n) and O(n²) — but this analysis neglects the branching factor Z, which could increase the effective n in practice. This claim is unnecessary and distracting.

## Nice-to-Haves

- A controlled efficiency experiment comparing ARPO and GRPO at matched tool-call budgets would make the efficiency claim credible.
- An analysis of the branching distribution (how often does the entropy threshold fire? how many branches per trajectory?) would help readers understand method behavior.
- The theoretical section (Section 3.3, GPG theorem) is a standard extension of the policy gradient theorem to macro-actions and does not specifically justify the entropy-based selection of branching points. Consider either removing it or connecting it explicitly to why entropy peaks are the right branching criterion.

## Removed Points

The following points from the inputs were removed with justification:

- **"The deep search comparison includes large models not RL-trained"** (harsh critic): The paper clearly separates these in Table 2 (gray rows for "Direct Reasoning (≥32B)" vs. "RL-based Method"), so this is not an unfair comparison — it is a demonstration that smaller RL-trained models can surpass larger ones. A strength, not a weakness.
- **"The comparison against fixed-trajectory baselines is unfair unless total computational budget is matched"** (harsh critic): Table 1 reports *accuracy* at comparable training steps; the efficiency claim is separate and addressed in Weakness #1. The main accuracy comparison in Table 1 is not about budget matching.
- **"Complexity claim not justified and neglects branching factor"** (harsh critic): Retained as Trivial #5 but demoted — this is a minor side-claim, not a core issue.
- **"Pioneeringly quantify is overstated"** (harsh critic): A wording choice in the contribution list, not a substantive weakness. The paper correctly cites prior entropy-based work it follows.
- **Strength: "50% reduction in tool-call budget"** (strength finder): Merged into Weakness #1 — the evidence does not support 50%.
- **Strength: "Advantage attribution estimation"** (strength finder): Overclaimed; downgraded via Weakness #2.
- **Strength: "Theoretical grounding via GPG"** (strength finder): This is a standard extension; not a distinct strength.
- **Strength: "Only 1k RL samples on deep search"** (strength finder): Retained as part of Strength #2 (consistent gains) but framed more carefully — this is about sample efficiency, not a standalone contribution.
- **Generic strengths** (strength finder): Removed any that were superficial or not specific to this paper's actual evidence.

## Novel Insights

None beyond the paper's own contributions. The key observation — that entropy spikes after tool calls and can be used to guide branching — is the paper's core insight, and the reviews did not surface additional novel angles.

## Suggestions

1. Tone down the efficiency claim: replace "only half the tool-call budget" with "substantially fewer tool calls" or "~35–40% fewer tool calls" unless a controlled experiment at matched budgets confirms 50%.
2. Reframe the contributions around the entropy-based adaptive rollout as the primary novelty, with the advantage attribution as an observation about how GRPO's loss interacts with partial rollout — not as a separate contribution.
3. Add statistical significance (e.g., standard deviations across seeds) to the main results tables.
4. Include a brief hyperparameter sensitivity summary (α, β, τ, Z) for at least one dataset in the main paper.
5. Remove or tighten the computational complexity claim.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Searched for papers on RL for LLM agents with tool use. Weak anchors (avg 2.0–3.0) were rejected/withdrawn papers with fundamental flaws — ARPO is clearly stronger. Middle anchors (avg 4.2–7.0) included Retroformer (5.67, accepted spotlight), LAM Simulator (6.0, rejected), Creative Robot Tool Use (5.0, rejected), and ToolLLM (7.0, accepted spotlight). Strong anchors (avg 7.75–8.67) were clear oral/poster accepts with stronger claims and fuller validation. **Initial bracket: 5.0–7.0.**

**Round 2 (Narrowing):** Retrieved anchors in (4.5, 6.0) and (6.0, 7.5). Key comparisons:
- **Retroformer** (avg 5.67): Methodologically similar (RL for LLM agents) but has weaker empirical results (mixed task improvements) and no entropy-based mechanism. ARPO is stronger empirically and has a clearer algorithmic contribution. ARPO ≥ Retroformer.
- **LAM Simulator** (avg 6.0, rejected): Focuses on data synthesis for agent training rather than RL algorithm design; weaker on novelty and ablation. ARPO has a sharper contribution and more extensive evaluation. ARPO > LAM Simulator.
- **Eureka** (avg 6.25, accepted poster): LLM-based reward design for RL; technically different domain but comparable rigor. ARPO's evaluation breadth is similar; both have some overclaiming issues. ARPO ≈ Eureka.
- **ToolLLM** (avg 7.0, accepted spotlight): Comprehensive tool-use framework; strong empirical work but low technical novelty (mostly applying existing techniques at scale). ARPO has higher algorithmic novelty but less comprehensive infrastructure contribution. ARPO ≤ ToolLLM.

**Final position:** ARPO sits above Retroformer and LAM Simulator, comparable to Eureka, and slightly below ToolLLM. The core entropy-based branching idea is genuinely novel, the evaluation is broad, and the empirical results are consistent. However, the overstated efficiency claim and overframed advantage attribution contribution pull the score down from the top of the bracket.

**Score: 6.0** — Marginally above acceptance threshold. The paper has a sound core contribution, broad evaluation, and real empirical value. The main issues (overclaiming on efficiency and contribution framing) are addressable in revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>