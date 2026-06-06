Now I have everything I need to write the final review. Let me verify the key quantitative claims before proceeding.

**Verifying the "80%" recovery claim (Critic's major concern):**
From Figure 3 / Table (lines 110–117):
- Claude Haiku 3.5: Interaction=26.80, Full=33.80 → 26.80/33.80 = 79.3% ≈ 80% ✓
- Claude Sonnet 3.5: Interaction=39.60, Full=49.40 → 39.60/49.40 = 80.2% ≈ 80% ✓
- Claude Sonnet 4: Interaction=61.40, Full=68.00 → 61.40/68.00 = 90.3% ≈ 89% ✓

The critic computed gap-closure formula but the paper clearly uses Interaction/Full ratio. The numbers are consistent. **Critic's claim here is wrong — REMOVE that weakness.**

**Verifying compulsory interaction in RQ1 (lines 104, 129):**
Confirmed: "we modify the prompt to make interaction with the user compulsory in the Interaction setting" (footnote 3) while the research question asks "Can LLMs *appropriately* leverage interaction?" — real tension.

**Verifying detection metric issue (Table 2, lines 181–182):**
Confirmed: Llama 3.1 70B under Moderate prompting shows FPR=0.95, FNR=0.09 — essentially interacting with everything indiscriminately, not demonstrating genuine detection.

**Verifying triple GPT-4o role:** Confirmed in §2.1 (generator), §2.2 (user proxy), §5.1 (judge).

**Verifying navigational info finding (Table 1, lines 143–151):**
Qwen 3 Coder: w/o nav=55.43%, w/ nav=52.38% — ~3 pp difference with no CIs.

---

## Summary

Ambig-SWE introduces an underspecified variant of SWE-Bench Verified and an interactive evaluation framework for measuring three distinct capabilities of LLM agents: detecting underspecificity, asking targeted clarifying questions, and leveraging interaction to improve task completion. The paper evaluates six proprietary and open-weight models across three controlled settings (Full, Hidden, Interaction) and finds that interaction substantially recovers performance lost to underspecificity, but most models fail to initiate interaction spontaneously and struggle to reliably detect incomplete specifications.

---

## Strengths

- **Multi-faceted evaluation decomposing three key capabilities (§§3–5):** The three-RQ structure (detection, question quality, task completion) provides targeted diagnostics rather than a single holistic metric. Each capacity has dedicated experiments and appropriate metrics, enabling finer-grained analysis of where models succeed or fail.
- **Statistically validated performance recovery (Figure 3, Table 4):** The resolve-rate improvement from Hidden to Interaction is significant for all six evaluated models via Wilcoxon Signed-Rank tests. Interaction scores reach 79–80% of fully specified performance for Claude Sonnet 3.5 and Haiku 3.5 (39.60/49.40 and 26.80/33.80), and 90% for Claude Sonnet 4 (61.40/68.00).
- **Striking detection failure findings (Table 2, §4.3):** The detection experiment reveals severe model limitations — Qwen 3 Coder exhibits 100% FNR across all three prompt conditions, and Claude Sonnet 3.5's detection accuracy swings from 60% to 84% depending solely on prompt framing, demonstrating brittleness rather than robust understanding.
- **Granular question-asking strategy analysis (§5, Figure 4, Table 1):** The paper shows Claude Sonnet 4 achieves comparable information gain to Qwen 3 Coder (cosine distance 0.171 vs. 0.179) with ~50% fewer questions (4.03 vs. 6.02 on average), and reveals that Qwen's performance actually worsens with navigational information due to rigid protocol-following — a concrete and non-obvious finding.
- **Navigational vs. informational information breakdown (Table 1):** The finding that smaller models request file locations more often but underperform without them, while stronger models can infer navigation independently, provides actionable guidance for agent design and user-burden optimization.
- **Diverse model coverage:** Evaluation across six models spanning proprietary (Claude family) and open-weight (Llama, Deepseek, Qwen) with varying capability tiers enables comparative insights that would not emerge from single-family studies.

---

## Weaknesses

### Fatal
None.

### Major

- **RQ1 conflates "appropriate leveraging" with "leveraging when forced":** The central research question for RQ1 asks "Can LLMs *appropriately* leverage interaction to improve performance?" yet footnote 3 explicitly states that interaction is made **compulsory** because "the model defaults to non-interactive behavior for most issues." The experiment thus measures conditional performance — *given that interaction is triggered externally, can models use it?* — rather than whether models would autonomously choose and execute interaction appropriately. This framing gap is meaningful because RQ2 then demonstrates that autonomous triggering fails almost entirely; the combination means the RQ1 result describes a capability that current agents largely cannot exercise in deployment without external scaffolding. The paper should explicitly reframe RQ1 as measuring the upper bound of interactive capability under forced interaction, rather than as evidence of appropriate use.

- **Triple use of GPT-4o introduces a coherent evaluation loop (§2.1, §2.2, §5.1):** GPT-4o generates the underspecified issues, serves as the user proxy that answers agent questions, and judges question quality. This creates a closed feedback loop: GPT-4o removes information in a particular stylistic register, then fields questions about what it removed, then evaluates those questions. Models with similar training lineages or alignment conventions to GPT-4o may be systematically advantaged across all three roles. The paper's distributional defense — that "the other differences may not directly impact agent performance" — is asserted rather than demonstrated. Notably, the Claude family (consistently top performers) is the most likely beneficiary of such alignment coherence. This does not invalidate the findings, but the paper should acknowledge the limitation more prominently and consider whether open-weight models trained on substantially different pipelines show coherent differences that cannot be explained by task capability alone.

### Minor

- **Detection metric conflates interaction propensity with genuine discrimination (Table 2, §4.2–4.3):** The experiment operationalizes "detection" as interaction rate across Full versus Hidden inputs. A model that interacts with everything scores a low FNR at the cost of a high FPR — which is not evidence of detection capability. Llama 3.1 70B under Moderate prompting (FPR=0.95, FNR=0.09) is essentially interacting indiscriminately, yet it appears in the same metric space as models that genuinely discriminate. The paper acknowledges this as "excessive interaction" but does not explicitly caveat that the metric cannot distinguish detection skill from interaction propensity. The practical implication is that reported "detection accuracy" scores for high-FPR models overstate genuine detection capability.

- **No confidence intervals for borderline comparisons in Table 1 and Table 2:** The claim that Qwen 3 Coder's performance worsens with navigational information (55.43% → 52.38%, 3.05 pp) and the comparison of Deepseek-v2 across prompt conditions involve differences small enough that statistical significance is unclear. The paper reports significance for the main Hidden vs. Interaction comparisons (Wilcoxon tests, Table 4) but not for these secondary analyses. At n=500 binary outcomes, a 3 pp difference approaches but may not cross conventional thresholds.

- **Claude Sonnet 4 Hidden evaluation on 100/500 instances creates a silent comparability issue (Footnote 4):** The paper evaluates Claude Sonnet 4's Hidden performance on a 100-instance subset due to cost, then reports 40.00% alongside 500-instance results for all other models in Figure 3. While statistical significance is confirmed for this subset, the 40% figure drives the gap calculations (76% recovery for Sonnet 4) and the characterization of Sonnet 4's "substantially different" codebase-exploration behavior. Whether the 100-instance subset is representative of the full 500 for this uniquely high-exploration model is not established. The main figure caption should note this limitation explicitly rather than relegating it to a footnote.

### Trivial
None.

---

## Nice-to-Haves

- **A non-compulsory interaction condition in RQ1** (Full specification + interaction enabled but not required) would quantify the cost of false-positive interactions in the ideal case, making the Interaction gains more interpretable in practice.
- **A small-scale validation on human-curated naturally underspecified issues** (even 20–30 examples) would test whether patterns observed on synthetic issues generalize — specifically, whether the relative model rankings in interaction benefit replicate on organically incomplete specifications.
- **Explicit binary classification probe for detection (RQ2):** Asking models to classify issues as "sufficiently specified" or "underspecified" before acting would cleanly separate detection judgment from behavioral propensity, enabling stronger claims about what models genuinely perceive.
- **Analysis of the efficiency gap:** The finding that "interaction yields no efficiency gains" (action steps do not decrease in the Interaction vs. Hidden setting) is stated but unexplained. A brief trajectory-level analysis of why information acquisition does not reduce exploration steps would be practically informative.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **Critic's "80% figure unverifiable from Figure 3" (§3.2):** REMOVED. The critic computed gap-closure ((Interaction−Hidden)/(Full−Hidden)) but the paper uses Interaction/Full ratio. Haiku: 26.80/33.80=79.3%, Sonnet 3.5: 39.60/49.40=80.2%, Sonnet 4: 61.40/68.00=90.3%. All figures are numerically consistent with the stated claims. Critic's arithmetic was based on the wrong formula.

- **Critic: "asymmetric comparison favors the Interaction setting because the user proxy knows file locations":** PARTIALLY REMOVED. The paper explicitly discloses this in §2.3 and §3.3, then studies it as a separate factor (Table 1). The design choice is justified and analyzed, not hidden. It is mildly worth noting that Interaction and Hidden settings differ in total available information, but this is acknowledged and used as a study variable, not a confound.

- **Critic: "small-scale human study to validate synthetic distribution":** Moved to Nice-to-Haves. This is a methodological improvement suggestion, not a flaw that undermines current claims.

- **Critic: "Deepseek counterintuitive behavior unanalyzed":** REMOVED as a weakness. The paper calls it "counterintuitive" and provides the relevant data (Table 2). Requesting deeper trajectory analysis is a nice-to-have, not a substantive flaw.

- **Strength Finder claim that interaction "recovers up to ~80% performance gap":** CLARIFIED. The 80% is a ratio metric (Interaction/Full), not gap-closure. The numeric recovery of the gap is lower (61–66% for Sonnet 3.5 / Haiku, 76% for Sonnet 4). The strength is real but the specific framing matters.

- **Critic concern about Claude models being "most likely to share training data with GPT-4o":** DEMOTED from the triple-GPT-4o weakness. The training data overlap claim is speculative and unverifiable. The structural concern about the feedback loop is kept on its own merits without this specific claim.

---

## Novel Insights

The most genuinely non-obvious insight emerging from the review synthesis is the **decoupling between information extraction volume and integration quality**: Qwen 3 Coder extracts more information per trajectory (cosine distance 0.179) and asks more questions (6.02 avg.) than Claude Sonnet 4 (0.171, 4.03 avg.), yet achieves similar or lower resolve rates — and its performance *worsens* with navigational information that other models benefit from. This suggests a qualitative distinction between "information extraction" as a search behavior and "information integration" as a planning and execution behavior, and that current benchmarks and training pipelines may conflate the two. The paper's observation that "interaction improves effectiveness but not efficiency" across models reinforces this: models appear to add interaction turns on top of existing exploration rather than substituting informed planning for blind search. This has direct implications for training objectives — rewarding successful trajectories that happen to include interaction may not be sufficient to train genuinely adaptive agents.

---

## Suggestions

1. **Rename RQ1 or add a clarifying qualifier**: Amend the research question from "Can LLMs *appropriately* leverage interaction?" to "Can LLMs leverage interaction to improve task completion when interaction is provided?" and add a sentence in §3.1 explaining that compulsory interaction is used because voluntary interaction is studied in RQ2.
2. **Report effect sizes and CIs for Table 1 comparisons**: Add bootstrap confidence intervals or binomial proportion CIs to the navigational vs. non-navigational resolve rates, especially for Qwen 3 Coder's paradoxical decrease.
3. **Promote footnote 4 to a main-text caveat**: Add a sentence in §3.1 noting that Claude Sonnet 4's Hidden result is a 100-instance estimate, and discuss the potential direction of bias.
4. **Acknowledge the GPT-4o loop more directly in limitations (§7)**: Add a sentence noting that GPT-4o's role as generator, proxy, and judge creates coherence that may not generalize to evaluations using alternative judge or proxy models.
5. **Add an "efficiency" analysis**: Explain mechanistically why interaction does not reduce action steps — whether question turns count against the 30/100-step budget, and whether models that obtain navigational information still proceed to re-explore the codebase (as observed for Qwen 3 Coder).

---

**Evaluation on core axes:**

- **Originality:** The three-way decomposition of interactive SWE performance and the controlled underspecification benchmark are novel contributions, though grounded in existing infrastructure (SWE-Bench, OpenHands). Moderate-high originality.
- **Importance:** Interactive handling of underspecified instructions is increasingly critical as agents are deployed on real-world tasks; the gap between forced and voluntary interaction is a practically important finding.
- **Claims supported:** The main empirical claims (interaction improves resolve rates; models fail to detect underspecificity; question strategies vary meaningfully) are well-supported by data and statistical tests. The framing of RQ1 is the primary weakness in claim support.
- **Soundness:** Methodology is generally sound; the Wilcoxon tests, cosine-distance + LLM-judge dual evaluation, and three-condition design are appropriate. Detection metric design is the most significant soundness concern.
- **Clarity:** Well-written, structured logically, findings clearly stated, limitations partially acknowledged in §7.
- **Community value:** Provides a reproducible benchmark, actionable findings for agent designers, and a diagnostic framework extensible beyond SWE to other agentic domains.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>