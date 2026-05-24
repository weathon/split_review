## Summary
The paper re-evaluates three benchmarks (TORCS/NDPS, Karel/LEAPS, Parking/PSM) used to claim programmatic policies generalize better than neural policies in RL, arguing that the reported gaps largely arise from experimental confounds (reward shaping, observation/architecture choices). It then proposes an *expressivity*/*discoverability* decomposition and identifies tasks requiring instance-scaling memory (pathfinding, nested subproblems) as the regime where programmatic representations have a genuine advantage, illustrated by a proof-of-concept where FUNSEARCH synthesizes BFS for a wall-sparse Karel maze.

## Strengths
- **KAREL re-evaluation (Table 2)** is the strongest piece of evidence: a feedforward PPO agent augmented with the last action achieves 1.00 average return on Stairclimber/Maze/TopOff/FourCorner at 100×100, matching LEAPS while LSTM baselines collapse to 0.00–0.37. This is a concrete, quantitative reversal of a previously reported gap.
- **TORCS re-evaluation (Table 1)** identifies a clean, mechanistic explanation for the prior gap (the speed-emphasizing reward β=1.0). Reducing β to 0.5 lets DRL agents generalize to OOD tracks (e.g., 76% on G-TRACK-2, 69% on E-ROAD), supporting the claim that the original DRL failure was reward-induced over-optimization rather than a representational limit.
- **Expressivity/Discoverability framework + memory-scaling argument (Section 5)** provides a useful conceptual lens that goes beyond the empirics: identifying pathfinding (Ω(log|V|) bits to index vertices, Θ(|V|) frontier memory for BFS) as a problem class where fixed-capacity neural policies are formally inexpressive cleanly separates "neural couldn't be trained to do it" from "neural cannot represent it."
- **Honest reporting of PARKING (Table 3)**: the paper presents both metrics and notes the ambiguity ("PSM policies generalize better… However, looking at the test 'Success Rate' alone suggests that DQN is the winner"), rather than cherry-picking.

## Weaknesses

### Fatal
None.

### Major
- **Asymmetric seed conditioning in Table 1.** The DRL (β=0.5) OOD numbers are computed only over the 13/30 (G-TRACK-1) and 4/15 (AALBORG) seeds that learned to complete the *training* track, while NDPS (3 seeds) is reported without analogous filtering. The headline that "neural matches programmatic OOD generalization once we relax β" rests on this conditioning. The caption is transparent about the filtering, but the comparison as presented understates the cost of the fix — 57% (G-TRACK-1) and 73% (AALBORG) of cautious-reward seeds never reach OOD evaluation at all. A symmetric report (unconditional OOD success, or NDPS conditioned identically) would let the reader make the comparison directly.
- **The KAREL story conflates "remove spurious features" with "match the algorithmic structure of the optimal solution."** Section 4.4 attributes PPO+a_{t-1}'s success to "removing features that could generate spurious correlations." But Section 5's own argument is that partial observation + last action is exactly the state representation a constant-memory wall-following algorithm needs. These are not the same explanation, and Table 2 alone cannot distinguish them. The paper would be sharper if Section 4.4 acknowledged that the architecture/observation pair was chosen to *fit* the algorithmic structure of the optimal solution (already implicit in Section 5), rather than presenting sparsification as a general remedy.
- **The proof-of-concept BFS experiment is too thin to anchor Section 5's empirical claim.** A single sentence — "Three runs of FUNSEARCH returned a correct implementation of breadth-first search" — is asked to demonstrate that programmatic representations *in practice* deliver the asymptotic advantage Section 5 argues for in principle. There is no FUNSEARCH variance analysis, no controlled comparison against a memory-augmented neural baseline (e.g., LSTM with larger hidden state, transformer with CoT, stack RNN) on SparseMaze, and no assessment of how much the result depends on Qwen 3-Coder already containing BFS in pretraining. The conceptual claim survives ("Python can encode BFS, which provably generalizes"), but the empirical demonstration is one paragraph deep.

### Minor
- **PARKING is acknowledged ambivalently but the framing softens what it actually shows.** By the paper's own numbers, PSM solves all 100 test states in 2/30 seeds vs 0/15 for DQN, with a train→test drop of 0.10 vs 0.68. By most reasonable definitions of OOD generalization, this is a case where the programmatic advantage is *not* a confound — and the paper's own Section 5 theory does not explain why (PARKING's solution arguably fits in constant memory). Using PARKING as the bridge case ("even when expressivity is matched, discoverability seems to favor programmatic here") would be more honest than the current hedged framing.
- **Section 5's universal claims are stronger than the experiments warrant.** Statements about what "the neural policies we evaluated" cannot do are well-supported, but the framing slips toward claims about neural representations broadly. The paper does add a paragraph noting that LLMs and memory-augmented networks "can in principle approximate the structures needed... However, they do so imperfectly," which partially addresses this — but the empirical evidence for the "imperfect approximation" claim is only the cited Weiss et al. counting experiment, not the SparseMaze setting at hand.
- **Section 4.4's "fewer features → less spurious correlation" claim is not directly tested.** A 2×2 ablation over {full obs, partial obs} × {with/without last action} on MAZE would settle whether the win comes from sparsification, from the last-action signal, or from their interaction.
- **Section 6 extends the framework speculatively** to Cui et al. (2024), Guo et al. (2023), and Qiu & Zhu (2022) without running experiments. The paper does flag this ("Although a careful investigation is needed…"), so this is a minor framing concern rather than a substantive overreach.

### Trivial
- The contrast between PPO+LSTM (0.04 on 100×100 MAZE) and PPO+a_{t-1} (1.00) is striking and would benefit from at least one diagnostic experiment to identify whether the LSTM failure is representational (cannot encode wall-following) or optimization (PPO cannot train it to).
- The "intrinsic reward" terminology in Section 4.1 is technically correct but understates that the training objective is being changed in a way that biases discoverability — that is precisely the point being made, so it should be stated as such.

## Nice-to-Haves
- A 2×2 ablation on KAREL/MAZE separating the effects of partial observability and last-action augmentation.
- At least one negative result for a memory-augmented neural baseline on SparseMaze, plus FUNSEARCH variance / LLM-sensitivity analysis. This is the single change that would most strengthen the second half.
- Re-presenting Table 1 with comparable conditioning across rows (e.g., adding "fraction of seeds completing training" as a top-level column for both NDPS and DRL variants).
- Either extending the Section 5 framework to explain PARKING, or explicitly noting it as a discoverability puzzle the paper does not yet account for.

## Removed Points
These points are flagged to be removed, treat them with caution:
- *Harsh critic's missing-related-work concern* (transformers/looped transformers/length generalization literature): the paper does engage briefly with memory-augmented models and LLMs (Section 5, last paragraph) and cites Joulin & Mikolov, Graves et al., Yang et al., and Delétang et al. We do not police missing-citations.
- *Critique of "PARKING is buried"*: the paper actually reports both metrics and explicitly states "PSM's policies generalize better… However, looking at the test 'Success Rate' alone suggests that DQN is the winner." This is not burial; demoted from major to minor framing concern.
- *Speculative reproducibility / scaling concerns about FUNSEARCH runs and LLM dependence*: kept the substantive part (PoC too thin) and dropped the speculation about pretraining contamination, since the paper cannot disprove the negative.
- *Strength Finder's framing of the PARKING result as a strength* ("the paper does not overclaim"): the absence of overclaim is virtuous, but it is not evidence supporting the paper's central thesis; in fact PARKING partially contradicts it. Demoted from strength to a Minor weakness.
- *Generic strengths about Section 6 generalization to other works*: the extension is speculative and acknowledged as such; not a substantive strength.

## Novel Insights
None beyond the paper's own contributions. The expressivity/discoverability split is a useful pedagogical reframing (the paper's contribution), but the underlying representation-vs-optimization distinction is standard. The most genuinely informative observation is the magnitude of the KAREL gap closure (LSTM 0.04 → feedforward+a_{t-1} 1.00) when the observation/architecture is chosen to match the algorithm class.

## Suggestions
- Re-present Table 1 with a "fraction of seeds completing training" column shown alongside, for both NDPS and DRL configurations, so the OOD comparison is symmetric.
- Run the 2×2 KAREL ablation on {full/partial obs} × {with/without last action} to disentangle sparsification from algorithmic-structure matching.
- Extend the SparseMaze experiment with (i) a recurrent or transformer baseline that fails the prediction of Section 5, (ii) FUNSEARCH variance over more runs / different underlying LLMs.
- Use PARKING explicitly as the case where the confound argument *does not* explain the gap, and either extend the theory or acknowledge the open question.
- Trim Section 5's claims to the policies actually evaluated, while keeping the in-principle argument about fixed-capacity inexpressivity for instance-scaling memory.

## Axis Assessment
- **Originality**: Moderate. The re-evaluation is a genuine and valuable contribution. The expressivity/discoverability decomposition is a useful exposition but echoes the standard representation/optimization distinction.
- **Importance**: The question is well-motivated — multiple high-profile programmatic-policy papers rest on the OOD comparisons being challenged, so settling whether the gap is confounded matters.
- **Support for claims**: Uneven. KAREL and TORCS support the confound thesis (TORCS with caveats about seed conditioning). PARKING partially contradicts it. The Section 5 thesis is supported in principle but only minimally in practice (one-paragraph FUNSEARCH PoC).
- **Soundness of experiments**: TORCS table conditioning is asymmetric; FUNSEARCH PoC is under-instrumented; missing the natural KAREL ablations. Otherwise the comparisons are reasonable and follow the original benchmarks faithfully.
- **Clarity**: Clean writing and well-scoped background.
- **Value to community**: Real — re-evaluation papers in RL are scarce and the KAREL/TORCS results will influence how future programmatic-policy work is framed.

## Score and Decision

### Calibration anchors retrieved
- `Pjkes5MdKI.md` — avg 2.50 (Round 1, weak band): program synthesis with neural feedback — much weaker contribution and presentation than this paper.
- `hCfhfwSfCg.md` — avg 2.00 (Round 1, weak): LLM-guided exploration RL — far weaker than the paper.
- `N18Z2MkMEa.md` — avg 3.00 (Round 1, weak): code generation paper — not topically close.
- `MpA6HMD7Wq.md` — avg 3.00 (Round 1, weak): "Do Symbolic or Black-Box Representations Generalise Better In Learned Optimisation?" — closest in spirit (symbolic vs black-box re-evaluation); reviewers cited limited baselines, weak presentation. The paper under review is more polished and has a sharper conceptual contribution.
- `NGVljI6HkR.md` — avg 3.67 (Round 1, middle): "Reclaiming the Source of Programmatic Policies" — directly comparable re-evaluation paper; reviewers raised scope/novelty/detail concerns. The current paper is broader (3 benchmarks + framework + PoC) but inherits similar attack surface (empirical detail gaps).
- `lUWf41nR4v.md` — avg 4.50 (Round 1, middle): programmatic + state machine policies — broadly related.
- `QiUitwJDKI.md` — avg 5.75 (Round 1, middle): InnateCoder programmatic options with foundation models — reviewers liked the direction, criticized novelty/scope. Current paper has comparable polish and a more original re-evaluation angle, but weaker empirical anchoring for its Section 5 thesis.
- `JlSyXwCEIQ.md` — avg 5.75 (Round 1, middle): CodeIt abstract reasoning via program synthesis — less directly comparable.
- `OI3RoHoWAN.md`, `9pW2J49flQ.md`, `or8mMhmyRV.md`, `pISLZG7ktL.md` — avg 7.75–8.00 (Round 1, strong): all substantively stronger executions (cleaner empirical case, larger contributions) than this paper.
- `tuEP424UQ5.md` — avg 5.75 (Round 2): MORL generalization benchmark — well-defined contribution, reviewers raised soundness 2/contribution 2. Comparable polish and similar pattern of "useful framing, real but limited empirics."
- `X1p0eNzTGH.md` — avg 5.67 (Round 2): zero-shot generalization in deep RL with sampling strategies — comparable empirical RL paper at the 5–6 band.
- `xTFgpfIMOt.md` — avg 5.67 (Round 2): single-life robot deployment — adjacent.
- `iMI4HRpZFc.md` — avg 5.25 (Round 2): target-directed RL delusions paper.
- `a8VETFwcVR.md` — avg 6.00 (Round 2): "Unveiling Options with Neural Network Decomposition" — closest topical match in the 6 band.
- `PR6RMsxuW7.md` — avg 6.25 (Round 2): planning + DRL integration via task substructure induction.

### Bracketing logic
Round 1 placed the paper between ~3.67 (NGVljI6HkR, the closest topical anchor) and ~5.75–6.0 (QiUitwJDKI, tuEP424UQ5). NGVljI6HkR is narrower in scope but cleaner empirically; QiUitwJDKI/tuEP424UQ5 are similarly scoped contributions in adjacent areas. Round 2 anchors (5.25–6.25) — particularly tuEP424UQ5 and a8VETFwcVR — share the pattern of "useful conceptual contribution + real but limited empirical case + reviewers flagging soundness/scope." The paper under review is comparable to that band: broader and more polished than NGVljI6HkR (which was accepted at 3.67), but with the Section 5 thesis only weakly anchored empirically, and the TORCS table conditioning being a real (not speculative) issue. It is not as cleanly executed as a8VETFwcVR (6.00) or PR6RMsxuW7 (6.25), which present complete experimental loops without the kind of asymmetric reporting flagged here.

Final placement: just below the 5.75 cluster, above NGVljI6HkR (3.67) but not at the 6.0 level — the empirical case is genuinely uneven where the comparable acceptances at 6 are tighter.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>