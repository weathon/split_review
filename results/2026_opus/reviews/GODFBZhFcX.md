Now I have enough calibration. Let me verify one more detail about the Composer prompts and figure 4 issue.## Summary
The paper proposes PCE, a Planner–Composer–Evaluator pipeline that converts the implicit assumptions latent in an LLM's chain-of-thought into an explicit decision tree whose root-to-leaf paths are scored as `U(S, a) = L(S)·G(a) − λ·C(a)`. PCE is evaluated on C-WAH (10 episodes) and TDW-MAT (24 episodes) across three LLM backbones (GPT-4o mini, GPT-OSS:20B, Gemma3:4B) against four communication-centric baselines (CoELA, REVECA, CaPo, CoTS), with module ablations, an LLM-scaling ablation, and a 12-participant user study.

## Strengths
- **Consistent task-performance wins across two benchmarks and three backbones.** In C-WAH (Table 1), PCE attains the lowest *Total Steps* on every backbone (42.76 / 49.60 / 59.20 vs. next-best 46.80 / 53.86 / 62.56). In TDW-MAT (Table 2), PCE attains the highest *Total* on every backbone (87.50 / 81.25 / 70.83 vs. next-best 81.25 / 73.33 / 67.50). The wins are not driven by a single backbone or benchmark.
- **Structured uncertainty handling complements scaling.** Figure 3 shows PCE keeps a consistent gap over a "Planner only" variant as Gemma3 scales 4B→12B→27B and as GPT-OSS:20B reasoning depth scales Low→Medium→High; "Planner only" improves only marginally. This is a substantive ablation result supporting the paper's framing that PCE is additive to scaling rather than a substitute.
- **Each module of the pipeline is shown to matter.** Table 3 (GPT-4o mini, C-WAH) reports that removing Planner / Composer / Evaluator increases Total Steps from 42.76 to 56.46 / 46.82 / 47.34 respectively, and removing the Planner blows up token usage from ~44k to ~140k.
- **Communication treated as an atomic action rather than the search mechanism (Sec. 2, 4.3).** This is a clean conceptual choice that differentiates PCE from CoTS-style methods where dialogue is intrinsic to plan exploration. The Composer can insert `[send message]` as a leaf when E[gain] − λC favors it, which is a coherent gating mechanism.
- **User study shows human preference across four Likert dimensions (Figure 4).** PCE beats both `w/o Com` and `Com always` on Appropriateness, Usefulness, Efficiency, and Trust, with qualitative interview evidence supporting the "selective communication" interpretation.

## Weaknesses

### Fatal
None.

### Major
- **"Comparable token usage" headline overclaim vs. Table 2.** The abstract and conclusion both assert PCE achieves "comparable token usage" while outperforming baselines. On TDW-MAT this is not supported against CoELA: GPT-4o mini PCE 197,807 vs. CoELA 113,059 (~1.75×); Gemma3:4B PCE 184,809 vs. CoELA 98,350 (~1.88×); GPT-OSS:20B PCE 337,225 vs. CoELA 237,499. PCE wins on tokens only against debate/MCTS-style baselines (CaPo, CoTS) and against CoELA in C-WAH. The Sec. 5.1 narrative that the three-LLM overhead is "offset by shorter episodes" holds for C-WAH but not TDW-MAT against CoELA. The headline framing should be tightened to "comparable or favorable against communication-heavy baselines; higher than CoELA on TDW-MAT, where shorter episodes do not offset the per-step overhead."
- **Very small samples with no variance/significance reporting.** C-WAH has 10 episodes and TDW-MAT 24, yet results are reported to two decimals (e.g., PCE 42.76 vs. REVECA 46.80 Total Steps) without standard deviations, per-episode breakdowns, seed-level variance for the LLM modules, or any significance test. With three LLM calls per step and a 250- or 3000-step horizon, episode-to-episode variance from LLM sampling alone is likely non-trivial, and several "wins" by 2–4 steps may be within noise. The 12-participant user study (Figure 4) similarly reports only means and lacks error bars or statistical tests. For a paper whose central claim is *consistent* outperformance, this is a real evidential gap.

### Minor
- **Calibration evidence for L(S) and G(a) is relegated to the appendix.** The Evaluator's central rule `E[gain] = L(S)·G(a)` (Sec. 4.4) treats LLM-estimated quantities as probabilities and utilities on [0,1]. Sec. 5.2 acknowledges the human-expert correlation studies are in appendices A.10–A.11, but given that every comparative result rests on these scores producing a meaningful *ranking* of leaves, at least a small reliability/correlation snapshot belongs in the main paper. A randomized-scoring control (hold the tree fixed; replace L, G with random or uniform values) would also be more diagnostic than the current `w/o Evaluator` ablation, which removes scoring entirely.
- **Composer's local ranking policy is described in one sentence.** Sec. 4.3 says the policy "prioritizes [assumptions] that most reduce uncertainty and most strongly influence subsequent action choice" but the main text gives no concrete scoring procedure, no statement of whether expansion is one-shot or iterative, and no discussion of variance under LLM stochasticity. Depth `D=3` with binary splits also caps the tree at 8 leaves, which is small for a claim of "systematic" assumption reconciliation; the main text should explain why this depth is adequate.
- **Cost-function constants `α = β = λ = 1` set by default without justification (Sec. 4.4).** `α d(a)` is in path-length units and `β ℓ(a)` is in message-length units (presumably tokens/words). Combining quantities with no natural common scale at equal weight directly determines when communication beats movement; a brief sensitivity snapshot in the main paper would be appropriate. The paper does say sensitivity is deferred to the appendix.
- **DEC-POMDP formalism (Sec. 3) is mostly decorative.** The Composer/Evaluator do not estimate a belief `b(s)`; they produce LLM-scored heuristics. Either tie `L(S)` back to the belief or move the formalism to the appendix — the current writeup risks suggesting more theoretical grounding than the method delivers.
- **The two "empirical observations" motivating PCE (Sec. 1) are stated without supporting data.** A small structured study (e.g., counting assumptions per CoT trace, measuring how often they are referenced more than once) would make the foundational claim that LLM reasoning produces locally-referenced, never-globally-aggregated assumptions empirically grounded rather than asserted.

### Trivial
- The cost function's mutually-exclusive structure (`1{move(a)} + 1{comm(a)} = 1`) implicitly assumes no other action types; a one-line comment in Sec. 4.4 would clarify.

## Nice-to-Haves
- **Analysis of *when* PCE communicates.** Since the contribution is fundamentally a gating mechanism over communication, a conditional distribution of `[send message]` selection across belief states or scenario types would convert the quantitative wins into an interpretable mechanism story and directly support the user-study claim of "selective" communication.
- **Reporting Usages and Comm alongside Total Steps in the scaling ablation (Figure 3).** Currently only Total Steps is plotted; tracking whether token usage and communication counts also stay flat or shrink with model size would clarify whether PCE's benefit shrinks or grows with model capacity.
- **A fairer-backbone control.** A restricted comparison limited to the strongest backbone (GPT-4o mini) would clarify how much of "PCE consistently outperforms across diverse backbones" reflects PCE's robustness vs. baselines (esp. CoTS / CaPo) breaking down on small backbones.

## Removed Points
These points are flagged to be removed; treat them with caution.
- *"Method vs. motivation mismatch on 'without heavy communication.'"* The paper explicitly says (Sec. 2) "PCE treats communication not as the search mechanism itself, but as an atomic action within the search space to be evaluated against physical actions" and uses the phrase "without heavy communication" rather than "without communication." This is not a contradiction; the harsh critic's framing somewhat overstates it. Demoted from major to a presentation note already covered by the "comparable token usage" major point.
- *"Baseline fairness — running CoTS on Gemma3:4B handicaps it."* This asymmetry would, if real, *hurt* the baselines and make PCE's wins look stronger than they are. Per the rubric, criticisms about unfair comparisons that *favor the baseline* are kept, but here the asymmetry favors the author's method, which is the opposite case. Demoted.
- *"Figure 4 lists PCE twice."* This is a parser artifact, not a paper problem.
- *Generic strength about "explicit modeling of environmental assumptions as a decision tree with principled scoring"* (Strength Finder) — this is essentially restating the paper's pitch; kept only as supporting context for the "each module matters" ablation strength.

## Novel Insights
The conceptually interesting move is making *implicit assumptions in an LLM's CoT* into first-class decision variables and structuring them into an explicit tree that can be jointly scored — rather than either (a) papering over uncertainty with more dialogue, or (b) doing tree search over actions/plans directly. The corollary empirical insight, surfaced by Figure 3, is that this structured-uncertainty handling is complementary to model scaling rather than redundant with it: a larger backbone alone does not learn to aggregate its own local assumptions into a coherent global decision. Both observations are genuinely useful framings; whether they survive at scale and on harder benchmarks is the natural follow-up question.

## Suggestions
- Rewrite the abstract's "comparable token usage" sentence to honestly reflect that PCE matches or beats baselines on tokens in C-WAH but is ~1.75–1.88× CoELA on TDW-MAT (while still beating CaPo / CoTS / REVECA on tokens on TDW-MAT). Be explicit about which trade.
- Add per-episode breakdowns and standard deviations to Tables 1–2; add error bars and a paired significance test (e.g., Wilcoxon) to Figure 4.
- Surface a 1–2 sentence calibration result for `L(S)` and `G(a)` (e.g., Spearman correlation against human ratings) in the main paper, even if full details remain in the appendix.
- Run a randomized-scoring control (fix the tree; randomize L, G) as a sharper ablation than `w/o Evaluator`.
- Add a 1-paragraph description of the Composer's local ranking policy with the concrete prompt or scoring procedure.
- Add a sensitivity snapshot for `α, β, λ` (e.g., ±50%) in the main paper.
- Add a short analysis of *when* PCE chooses communication — at minimum, the per-state rate of `[send message]` selection vs. baseline.

## Axes
- **Originality:** Moderate. The decision-tree-over-assumptions framing is a meaningful conceptual reshape of existing PCE-style modular pipelines (CoELA, REVECA, CaPo, CoTS); it is not a paradigm shift but it is a non-trivial refinement.
- **Importance of research question:** Reasonable. Communication overhead in LLM embodied multi-agent cooperation is an active and relevant problem.
- **Whether claims are well-supported:** Partially. Task-performance gains are well-supported across three backbones and two benchmarks, but the "comparable token usage" headline is loose on TDW-MAT vs. CoELA, and the lack of variance reporting weakens the "consistent" framing.
- **Soundness of experiments:** Acceptable but thin. Sample sizes are small (10 and 24 episodes), no variance is reported, calibration of central quantities is deferred. The scaling ablation and component ablation are well-designed.
- **Clarity of writing:** Generally clear. The Composer's ranking policy and the cost-constant choices are under-described.
- **Value to the community:** Real. The mechanism (turn implicit CoT assumptions into a tree, score paths by L·G − λC) is reusable, and the empirical observation that PCE complements scaling is worth surfacing.

## Calibration Trace
Anchors retrieved (path, avg human score, round, comparison):
- `EnXJfQqy0K.md` CoELA — 6.50, Round 1 — Same benchmarks (C-WAH, TDW-MAT), introduces the framework PCE refines; PCE is narrower in conceptual scope but with stronger multi-backbone evidence.
- `KRv9NubipP.md` CaPo — 6.00, Round 1+2 — Same benchmarks, extension of CoELA with a meta-plan module; comparable contribution scope to PCE but PCE has more diagnostic ablations and broader backbone sweep.
- `YXRyYkb1im.md` COMBO — 6.67, Round 1+2 — Same problem area with a heavier world-model contribution; stronger conceptual novelty than PCE.
- `7gUrYE50Rb.md` EQA-MX — 8.00, Round 1 — Different sub-area; not used for narrowing.
- `or8mMhmyRV.md` MaestroMotif — 7.75, Round 1 — Skill design; not directly comparable.
- `Q6a9W6kzv5.md` PhysBench — 8.00, Round 1 — Benchmark paper; not directly comparable.
- `OI3RoHoWAN.md` GenSim — 8.00, Round 1 — Simulation task generation; not directly comparable.
- `BW8O4wHgbo.md` LLM-MAPF — 3.00, Round 1 — Negative-result paper; weaker than PCE.
- `P0eEalHM5h.md` LLMs Synergy — 3.40, Round 1 — Weaker contribution than PCE.
- `E2CR6hmV1I.md` CollabUIAgents — 3.00, Round 1 — Different domain.
- `ByLO7p0oCF.md` DebUnc — 3.00, Round 1 — Different domain (debate); weaker than PCE.
- `Glcsog6zOe.md` Tree-Planner — 5.25, Round 2 — Tree-based LLM planning, single-agent; comparable structural idea but narrower problem; PCE has stronger multi-agent + multi-backbone story.
- `kpL66Mvd2a.md` Tree Search for LM Agents — 5.50, Round 2 — Web automation tree search; comparable empirical depth.
- `pRIPRDALBV.md` Open-World Planning via Lifted Regression — 5.50, Round 2 — Affordance planning; comparable methodological scope, weaker empirical breadth than PCE.
- `OPdmIxdkPb.md` Query-Efficient Planning — 4.75, Round 2 — Weaker contribution than PCE.
- `GBIUbwW9D8.md` R-MCTS — 5.75, Round 2 — Reflective tree search for VLM agents; comparable empirical depth, somewhat better-instrumented.
- `JDd46WodYf.md` Active Procedure Planning — 5.67, Round 2 — Different domain (instructional videos).
- `Acvo2RGSCy.md` DeLLMa — 7.33, Round 2 — Stronger decision-theoretic framing with cleaner calibration story; clearly above PCE.
- `MqL2e85ZTp.md` Uncertainty-Guided LLM Search Trees — 6.40, Round 2 — Cleaner probabilistic framing with proper priors; somewhat tighter than PCE.
- `EqcLAU6gyU.md` Agent-Oriented Planning — 5.60, Round 1 — Different problem; not used for narrowing.
- `1Euu8FPr3d.md` Wasserstein MARL — 5.25, Round 2 — Different domain.

**Round-1 bracket:** Given direct competitors CoELA (6.5), CaPo (6.0), and COMBO (6.67) all sit in [6.0, 6.7], with rejected weaker LLM-agent papers in [3.0, 3.4], the initial bracket was 5.0–6.5.

**Round-2 narrowing:** Tree-Planner (5.25), Tree Search for LM Agents (5.5), and R-MCTS (5.75) are tree-search-style LLM planning papers with comparable empirical depth to PCE; CaPo (6.0) is a near-direct comparator with a similarly-modular extension story. PCE has more breadth than the round-2 cluster at ~5.5 (three backbones, scaling ablation, user study), but is weaker on rigor (no variance, calibration deferred, headline token claim overclaimed) than CaPo (6.0). It does not reach DeLLMa (7.33), which has a tighter formal/calibration story. PCE lands between R-MCTS (5.75) and CaPo (6.0).

Final position: 5.5 — closer to R-MCTS (5.75) than to CaPo (6.0). Real contribution, real empirical wins, but the "comparable token usage" overclaim and the absence of variance reporting keep it from clearing the bar set by the closest accepted anchor.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>