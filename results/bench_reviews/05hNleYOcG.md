Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

PLAGUE proposes a modular three-phase framework (Planner, Primer, Finisher) for constructing multi-turn jailbreak attacks, augmented by a strategy-retrieval memory bank the authors call "lifelong learning." The framework is designed to be plug-and-play: existing attacks like GOAT, Crescendo, and ActorBreaker can substitute into different phases. The paper evaluates against five frontier models (o3, o1, Claude Opus 4.1, DeepSeek-R1, Llama 3.3 70B), shows systematic component-wise ablations, and reports strong attack success rates under an ASR@K (K=2) protocol.

## Strengths

- **Clean framework decomposition with systematic ablation**: The Planner/Primer/Finisher decomposition is well-motivated (Section 3), and Table 3 provides a genuinely informative ablation: adding backtracking, reflection, planning, and strategy retrieval to GOAT lifts SRE on o3 from 0.587 → 0.612 → 0.761 → 0.773 → 0.814. Each component addition yields a non-trivial gain, and the pattern holds on Claude Opus 4.1 (0.222 → 0.396 → 0.402 → 0.431 → 0.465). This controlled experiment is the strongest evidence in the paper.

- **Plug-and-play modularity demonstrated in practice**: Table 4 shows that substituting Crescendo as the Finisher (instead of GOAT) for Claude Opus 4.1 lifts SRE from 0.48 (base Crescendo) to 0.673 (PLAGUE with Crescendo Finisher), a 40.2% relative improvement. This directly validates the framework's modularity claim and shows practical value beyond a single fixed configuration.

- **Broad model coverage on contemporary frontier models**: Evaluation spans o3, o1, Claude Opus 4.1, DeepSeek-R1, and Llama 3.3 70B — a strong, up-to-date set that includes the most safety-aligned models available. The paper also evaluates against six baseline methods (ActorBreaker, GOAT, Crescendo, AutoDAN-Turbo, X-Teaming, FITD), making this one of the more comprehensive multi-turn jailbreak comparisons.

- **Efficiency analysis under controlled budgets**: Table 5 shows PLAGUE uses comparable or fewer total LLM calls than Crescendo (e.g., 6.53 vs. 5.28 on o3) despite much higher ASR. Figure 2 shows SRE scales with turns up to 6 and plateaus at 8, justifying the budget choice. The cost analysis is a genuine strength that many competing papers omit.

## Weaknesses

### Fatal
None.

### Major

- **ASR@K (K=2) is not the standard metric in jailbreak evaluation, and ASR@1 is not reported.** The paper explicitly states (line 164) that it reports ASR@2, selecting the better of two attempts per objective using the internal rubric scorer. While this is transparently disclosed and uniformly applied to all baselines (e.g., ActorBreaker is limited to K=2 actors, line 168), the headline numbers (81.4% on o3, 97.8% on DeepSeek-R1) cannot be directly compared to prior work that reports standard single-attempt ASR. The paper claims state-of-the-art without providing the numbers that would enable readers to verify this against published results. Reporting ASR@1 alongside ASR@2 would let readers assess the extent of inflation and enable fair cross-paper comparison. This is not fatal — the internal comparisons are valid and the paper is transparent — but it weakens the central SOTA claim.

- **The "lifelong learning" claim is overstated relative to the evidence.** The paper's key conceptual framing is that PLAGUE is a "lifelong-learning agent" that "learns from past attacks, evolves, and discovers novel vulnerabilities" (line 85). The only supporting evidence is the RSS ablation in Table 3, which shows that retrieving successful strategies from a memory bank improves SRE (o3: 0.773 → 0.814). This demonstrates that a retrieval memory is useful, but it does not demonstrate lifelong learning: there is no experiment showing performance improves as the strategy library grows over time, no plot of cumulative ASR against number of stored strategies, and no comparison against a static-memory condition. The mechanism is a one-shot retrieval from a memory bank — a useful component, but calling it "lifelong learning" is an overclaim that the experiments do not substantiate. The contribution would be stronger if reframed as "strategy retrieval memory" without the lifelong framing, or if actual learning-over-time experiments were included.

### Minor

- **Factual error in baseline identification.** Line 209 states "we outperform the previous best - GOAT by a factor of 32.14%." However, in Table 2, on o3 SRE, ActorBreaker scores 0.616 while GOAT scores 0.587 — so ActorBreaker is actually the best prior method by SRE. The 32.14% figure itself matches (0.814 − 0.616)/0.616 = 32.14%, which is the improvement over ActorBreaker, not GOAT. The paper misidentifies which baseline the improvement is relative to. This is a presentation error but it muddies the framing of the paper's advantage.

- **Diversity claims are not quantitatively evaluated.** The paper claims that PLAGUE improves tactical diversity (line 49), that incorporating ActorBreaker's planner improves diversity by 15% (referencing Figure 3), and that existing attacks "suffer from limited tactical diversity" (line 65). However, no diversity metric is defined or tabulated anywhere in the paper text. The diversity claim is essentially unbacked.

- **No ablation isolating embedding-based retrieval from random retrieval.** The RSS component retrieves strategies via cosine similarity (threshold 0.6, max 2 examples). Without a control condition that retrieves random strategies from the same pool, it is impossible to tell whether the semantic-similarity retrieval specifically adds value beyond mere exposure to diverse past strategies. This is a straightforward ablation that would strengthen the RSS claim.

- **Rubric scorer fidelity not analyzed.** The internal rubric scorer R is used for two critical decisions: (1) triggering backtracking during the Primer and Finisher phases, and (2) selecting the best of K=2 attempts for final evaluation. If R's scores correlate poorly with the external evaluator judge J, both mechanisms could be misleading. Reporting the correlation between R and J would add confidence in the framework's internal decision-making.

### Trivial

- **SRE/ASR interchangeability is confusing.** Line 164 states "We use SRE and ASR interchangeably in our work." But SRE is a continuous harmfulness score (0–1) while ASR is introduced as a binary metric in the same paragraph. Using them interchangeably invites misinterpretation, especially when the paper reports both Bin-ASR and SRE in tables.

- **The 32.14% improvement claim in the introduction (line 47) does not name which baseline it refers to**, making it impossible for the reader to verify without reaching Table 2.

## Nice-to-Haves

- **Evaluation with a weaker attacker LLM.** The paper uses DeepSeek-R1 as the attacker — a strong reasoning model. Showing results with a less capable attacker (e.g., Llama-3.1-8B) would test whether PLAGUE's gains come from the framework design or from the raw capability of the attacking model. This is not a weakness (using a strong attacker is a valid design choice), but it would strengthen the framework contribution claim.

- **Qualitative attack traces.** A full multi-turn conversation example on a hard model (e.g., o3) showing Planner → Primer → Finisher in action would make the framework more concrete and persuasive. The paper currently describes the phases abstractly without showing them in operation.

- **Sensitivity analysis on Primer/Finisher scoring thresholds.** The 7/10 Primer bar and 3/10 (backtrack) / 8/10 (success) Finisher bars appear reasonable but are presented without ablation. A brief sensitivity study would strengthen internal validity.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic claimed Figure 3 is "absent from the PDF rendering."** The figure is referenced in the paper text (line 49: "diversity improves by 15% (Figure 3)"). Whether it renders correctly is a parser artifact, not an author error. However, the substantive point — that no diversity metric is defined or tabulated — stands and is included in Minor weaknesses above.

- **Harsh critic claimed the budget analysis in Table 5 does not account for K=2 runs.** The paper states the budget is capped at 6 target LLM calls per run, and Table 5 reports average calls per single run. An ASR@2 evaluation runs the attack twice and picks the best; each individual run is budget-capped at 6 turns. The Table 5 numbers reflect per-run averages, not per-ASR@2-evaluation totals. This is consistent with the paper's methodology — the K=2 protocol means two independent runs, each under the budget, not one run with double the budget. The harsh critic's concern about "doubling" is a misunderstanding of how ASR@K works when each attempt is independently budgeted.

- **Harsh critic claimed the constant interchange of SRE and ASR "invites misinterpretation."** The paper explicitly defines both metrics and states the interchangeability convention upfront (line 164). While confusing (see Trivial weakness), the paper is not hiding anything — this is a presentation choice, not a deception.

- **Strength Finder claimed "Performance scales with conversation turns up to a well-defined budget" as a supporting strength.** This is included in the Efficiency analysis but is a relatively minor and expected observation. It remains in the Strengths section only as part of the broader efficiency point.

- **Strength Finder claimed "Lifelong strategy retrieval directly boosts success" as a core strength.** This conflates "strategy retrieval helps" with "lifelong learning is demonstrated." The retrieval benefit is real and is captured under the ablation strength. The lifelong framing is addressed as a Major weakness.

- **Strength Finder's claim about "Efficiency comparable to or better than baselines despite higher ASR."** This is valid but the numbers cited (3.85 target calls on o3 vs Crescendo's 3.14) are from Table 5. I include this under the efficiency strength above.

## Novel Insights

The paper's most valuable insight — somewhat buried in the ablation — is that different models are vulnerable to different attack components. Table 3 shows that for o3, the largest gain comes from adding reflection (+0.149 SRE), while for Claude Opus 4.1, the largest gain comes from backtracking (+0.174 SRE). Furthermore, on Claude Opus 4.1, GOAT as a Finisher performs poorly (0.222 SRE) while Crescendo as a Finisher works much better (0.48 base, 0.673 with PLAGUE). This model-specific vulnerability pattern — that no single attack configuration is optimal across all targets — is a genuinely useful observation that supports the plug-and-play design and offers practical guidance for red-teamers. The paper could have highlighted this finding more prominently rather than focusing on the aggregate SOTA claim.

## Suggestions

1. **Report ASR@1 alongside ASR@2** for both PLAGUE and all baselines. This is the single most important addition — it would let readers calibrate the numbers against prior work and assess the inflation from best-of-2 selection. The data already exists; it just needs to be reported.

2. **Either provide a learning-over-time experiment or reframe "lifelong learning" as "strategy retrieval memory."** If the authors want to keep the lifelong claim, they should run a sequential campaign (e.g., 200 objectives) and plot cumulative ASR against the number of stored strategies, comparing against a fixed initial strategy set. If not, renaming RSS to something like "adaptive strategy retrieval" would be more accurate and still capture the contribution.

3. **Define and report a concrete diversity metric.** Even a simple metric (e.g., pairwise semantic dissimilarity of generated attack plans, or number of unique strategy types used) would back the diversity claims that currently lack evidence.

4. **Fix the baseline identification error** on line 209 — either correctly identify ActorBreaker as the best prior method by SRE, or recalculate the improvement percentage relative to GOAT.

5. **Add a random-retrieval control** for the RSS component to isolate the value of embedding-based similarity retrieval.

## Score and Decision

### Anchor Comparison

| Anchor | Avg Score | Decision | Comparison to PLAGUE |
|--------|-----------|----------|----------------------|
| SEMA (`6eSNG1VNkl`) | 5.00 | Accept (Poster) | Similar quality. SEMA has cleaner methodology (RL training, ASR@1) but weaker model coverage (no frontier models). PLAGUE has broader empirical scope and better ablation but the ASR@K and lifelong-learning overclaims pull it down. Comparable overall. |
| GRAF (`f9BuANYtJf`) | 4.40 | Reject | PLAGUE is stronger. GRAF had a fundamental methodological issue (fabricating model responses = attacking an illusional model). PLAGUE has no comparable fatal flaw. |
| CoaxChain (`6yCZEruFu9`) | 3.50 | Reject | PLAGUE is clearly stronger. CoaxChain had limited novelty and surrogate-model dependency issues. PLAGUE's modular framework and systematic ablation represent a more substantial contribution. |
| The Attacker Moves Second (`7B9mTg7z25`) | 6.00 | Reject | PLAGUE is weaker. This paper had exceptional empirical scope (breaking 12 defenses, large-scale human study) and a clear meta-contribution. PLAGUE's contribution is narrower. |
| UltraBreak (`T5hD0as3jb`) | 6.00 | Accept (Poster) | PLAGUE is weaker. UltraBreak addresses a different problem (VLM jailbreak) with strong transfer results. |
| ACCEPT (`B7oQWswV7y`) | 6.50 | Reject | PLAGUE is clearly weaker. ACCEPT had a more novel optimization method (genetic updating with textual gradients) and stronger results. |
| AJF (`bQQkWXYjuy`) | 2.50 | Reject | PLAGUE is clearly stronger. |
| MAPA (`h0lOaeDwF2`) | 2.50 | Reject | PLAGUE is clearly stronger. |

**Positioning:** PLAGUE sits between GRAF (4.40, Reject) and SEMA (5.00, Accept Poster). It is stronger than GRAF (no fatal methodological flaw) and broadly comparable to SEMA — trading off cleaner evaluation (SEMA reports ASR@1) against broader empirical scope (PLAGUE evaluates frontier reasoning models like o3/o1). The overclaimed "lifelong learning" and ASR@K metric are real weaknesses, but the core contribution — the modular three-phase framework with systematic component ablation — is solid and the plug-and-play demonstration is convincing. Score: **5.0**.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>