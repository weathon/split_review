Now let me run the calibration search alongside a few anchor reads:Now I have everything I need. Let me write the final consolidated review.

---

## Summary

Interactive Speculative Planning (ISP) adapts speculative decoding — a technique for accelerating LLM token generation — to the coarser level of agent plan steps. A fast approximation agent 𝒜 generates steps sequentially while a slower, more capable target agent 𝒯 verifies each step asynchronously; mismatches trigger a rollback. The paper augments this backend with a UI rescheduling algorithm that serializes out-of-order 𝒯 outputs for users and supports active user interruption. Empirical results on OpenAGI and TravelPlanner show 20–42% latency reduction across four settings.

---

## Strengths

- **Genuinely novel adaptation of speculative decoding.** Lifting speculative execution from token granularity to agent-step granularity is a non-trivial conceptual move. Algorithm 1 correctly handles the stateful nature of agent planning (side-effects of executed steps) by re-executing 𝒯's step on mismatch (line 18) and truncating the trajectory (line 19), which is fundamentally different from lossless token-level speculative decoding.

- **Sound worst-case latency guarantee.** Section 4.1 proves that when all 𝒜 steps are rejected, speculative planning degenerates to exactly normal planning time (Equation 3). This bound prevents ISP from ever being strictly worse than a baseline in expectation, which is a meaningful safety property.

- **Practical UI rescheduling mechanism.** Algorithm 2 addresses a real engineering problem: asynchronous 𝒯 calls produce misordered outputs that would confuse users. The sequential presentation design (showing 𝒜 output only after preceding steps are confirmed, and 𝒯 output only in order) is a thoughtful co-design contribution.

- **Multi-setting empirical breadth.** Four settings varying agent architecture complexity (Direct Generation, ReAct, CoT, Multi-Agent Debate) and backbone models (GPT-3.5, GPT-4) on two benchmarks with different action spaces (tool selection vs. free-form travel planning) provide meaningful generality for the latency results.

- **Unusually candid limitations section.** The paper explicitly flags the Spectre-analogy security concern, the aggressiveness of exact match, the cost overhead, and the UI's lack of backtracking — real issues named rather than hidden.

---

## Weaknesses

### Fatal
*None.*

### Major

- **Missing quality metrics for TravelPlanner.** The paper explicitly acknowledges (Section 4.2) that soft Levenshtein matching (distance < 0.3) "is not guaranteed that the result from speculative planning remains the same as the result from normal agent planning." Having broken the quality-equivalence guarantee, the paper is obligated to measure what quality is actually achieved. TravelPlanner has established evaluation metrics — final plan delivery rate, commonsense constraint satisfaction, hard constraint satisfaction — and Table 2 reports none of them. The paper instead reports only latency and token counts. Claiming that ISP achieves "performance that is at least equivalent to…the target agent alone" is unverified for TravelPlanner, which is the benchmark where the claim is most at risk.

- **The "Interactive" contribution is entirely unevaluated with real users.** The paper's title and abstract center on human-in-the-loop interaction as a first-class contribution. Section 4.4 and Figure 12–14 study "potential user interruptions" — but this is entirely simulation-based: users are modeled by a patience threshold that triggers interruptions at oracle-quality (perfectly correct, instantaneous) inputs. No actual users were studied. Real users may provide incorrect answers, miss interruption windows, face cognitive load from frequent decision prompts (5–15 per task), or introduce their own latency. The simulation shows ISP creates more interruption *opportunities*, but whether those opportunities are utilized beneficially by actual users is entirely unverified. The "Interactive" framing in the title is thus a design intent, not a validated finding.

### Minor

- **Cost overhead left unframed as a tradeoff.** Table 1 shows that ISP costs 38–71% more than normal planning in three of four OpenAGI settings (Setting 1: $0.122 vs. $0.071; Setting 2: $0.074 vs. $0.044; Setting 3: $0.297 vs. $0.216). Only Setting 4 (same backbone) shows cost parity. The paper lists cost as metric #11 and acknowledges in the Limitations that "balancing time and cost efficiency becomes a critical topic," but the main results section never discusses the cost–latency tradeoff or characterizes when the savings are worth the premium. A user paying ~2× API cost for a ~25% latency improvement is making a meaningful tradeoff that deserves explicit analysis.

- **Negative latency improvement cases are acknowledged but unquantified.** Section 4.3 notes that "in almost all settings for both datasets, there are data points exhibiting negative latency improvement." The variance in Table 1 is telling: Setting 3 MAD = 182.70 ± 421.49 where the standard deviation more than doubles the mean. The paper offers two qualitative explanations (speed variability, API slowdown under concurrency) but never reports what fraction of tasks are actually slower with ISP, or by how much. This breakdown is necessary to assess ISP's reliability in practice.

- **The "first system for agent latency efficiency and management of human interactions" claim is asserted but not carefully substantiated.** EcoAssistant and System-1.x Planner are discussed in related work and both address agent efficiency. The paper argues ISP is differentiated (training-free, any agent combination, human-in-the-loop), but the "first" label is stronger than the argument warrants.

### Trivial

- Simulation parameters in Section 4.1.4 use confusingly formatted notation that makes it unclear which values apply to 𝒜 vs. 𝒯 — though this is likely a parser extraction artifact rather than an error in the original submission.

---

## Nice-to-Haves

- A relaxed acceptance criterion beyond exact match (e.g., LLM-judge or embedding-based similarity) would directly address the core acknowledged limitation and could validate TravelPlanner quality simultaneously. The paper identifies this but defers it to future work; given that exact match is characterized as "overly aggressive," this direction is worth prioritizing.
- A Pareto analysis of time saved per dollar spent across settings would make the cost-latency tradeoff actionable for practitioners.
- Even a small-scale user study (10–15 participants on a subset of OpenAGI tasks) would meaningfully validate the "Interactive" component and distinguish the paper from a pure systems/latency paper.
- An end-to-end task trace showing what 𝒜 proposed, which steps 𝒯 accepted or rejected, and how the total time compared would ground the algorithm's behavior better than timing histograms.

---

## Removed Points

*These points were flagged for removal — treat with caution.*

- **Harsh Critic §1 (Algorithm 1 pseudocode typo / parser artifact):** Removed per hard rule on formatting artifacts. The notation confusion in line 319 (three separate values assigned to $time(\mathcal{T}, s)$) is a PDF extraction artifact, not an author error.

- **Harsh Critic §3.1 (no probabilistic grounding for acceptance criterion):** Partially removed / weakened. The paper does not claim to replicate the probabilistic acceptance criterion of speculative decoding — it explicitly positions ISP as a design adaptation, not a theoretically equivalent transfer. Demanding a probabilistic grounding exceeds the paper's stated scope. Kept as Nice-to-Have.

- **Harsh Critic (comparison against EcoAssistant and System-1.x on a shared benchmark):** Removed per hard rule on missing related works. While these are cited in the paper, requiring their reimplementation on the same benchmarks is a significant ask, and the paper's differentiation (training-free, architecture-agnostic) is distinct enough that direct numeric comparison is not essential.

- **Harsh Critic (simulation results are tautological):** Weakened to trivial/not included. The simulation confirms monotonic relationships expected from the theory, but also reveals non-obvious interactions (e.g., the non-monotone effect of 𝒜 accuracy on total tokens when 𝒜 is slow, §4.1.2) that provide practical guidance for hyperparameter selection.

- **Strength Finder — "Quantification of user interaction benefit" as a supporting strength:** Dropped. The simulation of user interruptions (Section 5.5) is presented as a strength of the interactive component, but since user inputs are modeled as oracle-quality and simulation-only, this is contradicted by the verified weakness regarding missing user validation. The weakness wins.

- **Strength Finder — "Versatile experimental design":** Kept but not listed separately; merged into the multi-setting empirical breadth strength above.

---

## Novel Insights

The analogy between hardware speculative execution and agent planning is tighter than it first appears: just as CPUs execute instructions ahead of a branch prediction and roll back on misprediction, ISP executes agent actions ahead of target-agent verification and rolls back the trajectory on mismatch. The paper's Spectre parallel (Section 5) is genuinely illuminating — the security vulnerability arising from executing unverified 𝒜 steps is structurally analogous to Spectre-class side-channel attacks, where speculatively executed instructions leave observable traces before being discarded. This suggests that safe speculative planning in high-stakes domains will require formal notions of "speculation isolation," parallel to hardware mitigations like retpoline, rather than just Docker containers.

---

## Suggestions

1. **Report TravelPlanner quality metrics.** Add plan delivery rate and constraint satisfaction (commonsense + hard) for both ISP and normal planning. If quality degrades under soft match, quantify it honestly — this is more credible than omitting the metrics.
2. **Quantify negative-latency-improvement cases.** For each setting, report the fraction of tasks where ISP is slower and the mean slowdown for those tasks. This converts a vague acknowledgment into actionable data.
3. **Re-title or reframe the "Interactive" contribution.** Consider presenting the UI and user interaction component as a system design contribution with a simulated characterization, rather than a validated empirical finding. Alternatively, run even a small pilot user study and report it.
4. **Add a cost–latency efficiency analysis.** A simple table of "% latency saved per % cost increase" across settings would help practitioners decide when ISP is beneficial.

---

## Score and Decision

**Anchor comparison:**

| Path | Avg Score | Decision | Relation to this paper |
|---|---|---|---|
| xOtOfdbBqK (On-the-fly Speculative Decoding) | 5.75 | Reject | Most similar topic; adapts speculative decoding with theoretical + empirical work, but has marginal improvements and limited benchmark coverage. ISP has stronger latency gains but deeper experimental gaps. |
| xgQfWbV6Ey (Speculative RAG) | 5.50 | Accept | Directly analogous: extends speculative concept to a new domain (RAG vs. agent planning). Speculative RAG provides proper quality evaluation; ISP does not for TravelPlanner. |
| sLKDbuyq99 (Dynamic Multi-Agent Workflow) | 6.25 | Accept | High-quality multi-agent efficiency paper with comprehensive evaluation. ISP's core idea is comparably novel but evaluation is weaker. |
| cJd1BgZ9CS (DSI, distributed speculative inference) | 5.00 | Accept | Speculative inference paper with theoretical guarantees; accepted at a weak score. ISP has similar theoretical depth but with more experimental limitations. |
| lXwhR7uci1 (TestAgent) | 4.75 | Reject | Agent system with HCI component, rejected for limited novelty and evaluation gaps. ISP has stronger core novelty. |
| n7s9EwG6hW (LLM4Floorplan) | 4.00 | Reject | Low-scoring agent planning paper with limited evaluation. ISP is substantially stronger in core contribution. |
| n7iwmPacDt (Polybasic Speculative Decoding) | 3.00 | Reject | Weak speculative decoding extension, largely theoretical, low empirical contribution. ISP is much stronger. |
| WVWZ6SnM4t (RoundTable multi-agent) | 4.75 | Reject | Multi-agent system with evaluation gaps; similar positioning to ISP's interactive component. |

**Assessment:** ISP's speculative planning core is a genuine contribution — the idea is novel, the theoretical framework is sound, and the latency improvements are real. However, it falls short of Speculative RAG (5.5, accepted) primarily because it lacks quality evaluation on TravelPlanner (the benchmark where quality equivalence is not guaranteed) and lacks any user validation for the "Interactive" component that defines the paper's framing. It is stronger than the 4.0–4.75 rejected papers due to its stronger core idea and more comprehensive system design. The missing quality metrics on TravelPlanner are a concrete, fixable experimental gap; the missing user study is a more fundamental framing issue. Positioned between the 4.75 rejected papers and the 5.0–5.5 accepted speculative-adaptation papers.

**Originality:** Strong — step-level speculative planning is a clean and non-trivial adaptation.
**Importance of research question:** High — agent latency is a real bottleneck.
**Claims supported by evidence:** Partially — latency claims are well-supported; quality-equivalence claims are not verified for TravelPlanner; interactive claims are simulation-only.
**Soundness of experiments:** Mixed — OpenAGI is solid; TravelPlanner is incomplete.
**Clarity of writing:** Good — the algorithms and theory are presented clearly.
**Value to research community:** Moderate-to-high for the speculative planning concept; uncertain for the interactive component without user evaluation.

**Final Score: 4.5 — Weak Reject**

The speculative planning contribution could justify acceptance if the TravelPlanner quality gap is resolved; the interactive framing without user evidence is a more persistent concern that a revision alone may not fully address.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>