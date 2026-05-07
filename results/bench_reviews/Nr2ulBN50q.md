Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final review.

## Summary

The paper argues that synthetic experiments are essential—not merely a necessary evil—for rigorously evaluating causal ML methods, and that the real problem is *how* synthetic data is currently used (biased, simplistic, non-transparent), not *that* it is used. It identifies three problems with current evaluation (scarce ground truth, unintentional bias in semi-synthetic data, insufficient complexity), demonstrates these problems empirically (RealCause instability, CausalNF failures beyond its identification domain), and proposes four principles for reform: synthetic data is necessary; design choices must be transparent (operationalized via a five-element classification); evaluation must go beyond aggregation and the identification domain; and standardized evaluation frameworks should be developed.

## Strengths

- **The three-problem diagnosis (Section 2) clearly articulates real and important methodological failures.** Problem 2's analysis of how researcher design choices introduce implicit biases into semi-synthetic benchmarks—including the discussion of non-identifiability issues in CATE-estimator benchmarks—is a particularly valuable synthesis that the community needs to hear. This is not a straw-man diagnosis; it documents concrete, cited failures.

- **The five-element classification for specifying experimental design choices (Section 4.2) is a novel, concrete, and actionable contribution.** Breaking down any synthetic experiment into (i) set of causal models, (ii) set of queries, (iii) set of training data, (iv) generation algorithm, and (v) induced distribution goes well beyond generic calls for "better evaluation" and provides a specification framework that researchers could immediately adopt. The worked CausalNF example in Section 4.2 demonstrates feasibility of the framework.

- **The RealCause instability demonstration (Section 3.1) provides striking quantitative evidence that a widely-used semi-synthetic benchmarking tool produces unreliable method rankings.** The finding that varying the seed across a single realization yields ATE errors from 0.17 to 1.77, and varying realizations yields errors up to 9.45 (against a true ATE of 4.02), is concrete and important. This is not just a theoretical concern—it documents that current practice is producing misleading results.

- **The paper correctly reframes the community discourse.** Rather than accepting the common criticism that "causal ML relies too much on synthetic data," the paper redirects the critique: the problem is not synthetic data itself but its careless use. This is a productive reorientation that invites engagement on evaluation *practice* rather than evaluation *necessity*.

## Weaknesses

### Fatal
None.

### Major

- **The bold framing ("on the contrary, synthetic experiments are essential and necessary") is misaligned with the paper's actual substantive contribution.** Given the fundamental problem of causal inference (Holland, 1986), counterfactual ground truth is unobservable in real data, so synthetic data is *trivially* necessary for evaluating counterfactual estimation methods—the paper itself acknowledges this (Section 2, Problem 1). The genuinely debatable and interesting claim is not about *whether* but about *how*: that synthetic evaluation needs fundamental reform in design, transparency, and scope. This inner position is substantive and well-argued, but framing it as contrarian against a "synthetic data is bad" camp obscures the genuine contribution. Nobody in the causal ML community seriously argues for abandoning synthetic evaluation entirely; they argue for improving it. The paper's actual contribution aligns with this goal but its stated position argues against a straw man. **This matters because the provocative framing creates a rhetorical mismatch:** readers expecting a genuine debate about whether synthetic data is needed will find the real contribution elsewhere, while the readers who would benefit most from the principles (those who already accept synthetic data's necessity) may miss the reformist message buried under the contrarian framing.

- **The paper lacks a compelling argument that its proposed principles would bridge from rigorous synthetic evaluation to real-world trustworthiness.** The abstract claims the principles "will enable comprehensive evaluations that build trust in causal machine learning methods, driving their broader adoption," but this bridge is asserted rather than argued. The paper shows current synthetic evaluation is unreliable (Section 3) and proposes principles for better synthetic evaluation (Section 4), but never reasons through why following these principles would produce evaluations whose conclusions transfer to real-world deployment. The "unknown unknowns" problem (acknowledged in Sections 5–6) is the core challenge here: even perfectly designed synthetic experiments cannot capture phenomena outside their DGP. More rigorous synthetic evaluation could create *false confidence* if practitioners treat synthetic success as evidence of real-world reliability. The paper acknowledges this briefly but treats it as a minor caveat rather than a fundamental challenge to its central promise. **This gap between synthetic rigor and real-world trustworthiness is the central challenge the paper must address, and it does not do so adequately.**

### Minor

- **The principles in Sections 4.3–4.4 are reasonable but partly restate insights from prior work.** The recommendations to go "beyond aggregation" and "beyond the identification domain" echo Herrmann et al. (2024) and Karl et al. (2024) for general ML. The progressive complexity approach (Section 4.3) is practical but underspecified: it says to add one complexity at a time but gives no guidance on which complexities to prioritize or how to decide what counts as a meaningful increment. This is a useful direction but needs more specificity to be truly actionable.

- **The empirical demonstrations diagnose problems but don't connect back to the principles.** Section 3.1 shows RealCause is unstable; Section 3.2 shows testing beyond the identification domain reveals failure modes. These are valuable demonstrations, but the paper never shows how applying its principles (especially the five-element classification) to RealCause would fix—or even mitigate—the instability. A brief worked example applying Principles 2–3 to redesign a known benchmark would significantly strengthen the argument.

### Trivial
None.

## Nice-to-Haves

- A worked example applying the five-element classification to redesign a specific benchmark (e.g., RealCause) would demonstrate the framework's practical value and close the gap between problem diagnosis and proposed solution.
- Deeper engagement with the false-confidence objection—perhaps a dedicated subsection in Sections 5–6—would make the paper's position more robust and invite productive disagreement on the hardest challenge.
- More specificity in the progressive complexity approach (Section 4.3): a decision procedure or taxonomy of complexity types would help practitioners implement this principle.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Empirical demonstrations undermine the position."** The harsh critic argues that showing RealCause is unreliable undermines the pro-synthetic stance. This misreads the paper's logic: the argument is "current synthetic evaluation is bad → we need *better* synthetic evaluation → here are principles for it." Showing current tools are unreliable is consistent with this argument and does not undermine it.

- **"The position is tautological and therefore the paper is fundamentally flawed."** While the outer framing ("synthetic experiments are necessary") borders on tautological, the inner position ("how synthetic data is used matters more than whether") is substantive. The paper's real contributions (the problem diagnosis, five-element framework, empirical demonstrations) do not depend on the tautological outer shell. The framing is a rhetorical weakness, not a fatal one.

- **"Lack of empirical validation of the principles."** This is a position paper; it is not required to empirically validate that its proposed principles solve the problems. Empirical validation would strengthen the paper but is a Nice-to-Have for a position paper, not a Major weakness.

- **"Overclaiming / too strong framing."** Position papers are expected to make strong, provocative claims. The paper's bold framing is intentional. The issue is not that the claim is too strong but that the bold claim and the actual contribution are misaligned.

- **"Missing related works."** Cannot verify external references; removed per instructions.

- **"The resource-cost objection."** The paper acknowledges this in Section 5. While the acknowledgment is brief, it is reasonable for a position paper to flag this without fully resolving it.

## Novel Insights

The five-element classification (set of causal models, set of queries, set of training data, generation algorithm, induced distribution) is a genuinely novel formal framework that could become a standard specification tool for causal ML experiments. Its emphasis on explicitly characterizing the *induced distribution* over synthetic examples—rather than just the set of parameters—is an underappreciated insight. Most experimental papers specify their DGPs but completely ignore what distribution their sampling/exploration strategy induces over the experiment space, even though this distribution determines aggregated results. This is a concrete gap that the paper identifies and proposes a solution for.

## Suggestions

- Reframe the title and abstract to highlight the *reform* position ("synthetic experiments must be redesigned along these principles") rather than the *necessity* position ("synthetic experiments are essential"), which is trivially true and thus less productive as a central claim.
- Add a brief subsection or extended paragraph explicitly arguing why principled synthetic evaluation, despite unknown unknowns, can produce *more trustworthy* (not *fully trustworthy*) conclusions than current practice. Even a few paragraphs of reasoning here would significantly strengthen the bridge claim.
- Consider providing a short worked example showing how applying the five-element classification to RealCause would change or improve the experimental design, closing the loop between problem diagnosis and proposed solution.

## Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| dVKcLgcCLZ (causality for benchmark evaluation) | 6.67 | Similar topic (causal ML evaluation reform), similar structure (position + case studies). This paper is somewhat weaker due to its framing issue and the gap between problems and solutions, but has a more concrete framework (five-element classification). |
| j0h4glzL2F (LLM causal discovery benchmarks need reform) | 7.0 | Similar evaluation-reform position with empirical evidence. That paper had a clearer, more specific two-part position. This paper's position is muddier but the five-element framework is more actionable. |
| vFae5rRman (benchmarking is broken) | 6.0 | Similar "evaluation is broken, here's how to fix it" structure. That paper had a more concrete proposed solution (PeerBench). This paper's principles are less concrete but the empirical demonstrations are more rigorous. |
| 816gaVGHgP (RL hyperparameter tuning distorts evaluation) | 5.33 | Similar structure (position + theory + empirical demonstration + proposed fix). That paper had a formal proof supporting its position; this paper has the five-element framework. Both have a gap between problem and solution. |
| FJF1sa6elQ (five-tiered model evaluation framework) | 3.33 | Largely tautological claim ("current evaluation is insufficient") with limited novelty. This paper is clearly stronger: it has genuine empirical evidence and an actionable framework, not just a taxonomy. |
| tMJvb9JDsd (MAD evaluation is broken) | 7.0 | Similar structure with stronger empirical evidence (9 benchmarks, 4 models). This paper has less empirical breadth but more novel conceptual contributions (the five-element framework). |

This paper sits between the medium and medium-high anchors. It is clearly stronger than the truly weak position papers (3–4 range) that have tautological claims with no concrete contributions. It is somewhat weaker than the top evaluation-reform papers (7+ range) because of the framing misalignment and the gap between diagnosed problems and proposed solutions. The five-element classification is the paper's most distinctive and novel contribution, but it is underdeveloped relative to the problems it needs to solve. I place this paper at approximately **5.5**—a solid position paper with real contributions held back by framing issues and insufficient argumentation on its hardest challenge.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>