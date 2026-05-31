Now let me start the calibration search process to anchor my score.**Round 1 bracket: 6.5 – 8.0.** The paper is stronger than TPO (6.33) in evaluation breadth and clearly addresses a new, well-motivated problem. It is comparable to Backtracking (8.0), which is closely related in spirit and received high scores for methodological clarity and experimental strength. The 30-prompt analytical foundation and Figure 6 questions pull the paper slightly below the 8.0 anchor.

Now let me narrow within this bracket.Now I have sufficient anchors. Let me write the full review.

**Comparative positioning:**
- **Backtracking (Bo62NeU6VF, 8.0):** Novel concept for correcting unsafe generations via [RESET] tokens on general LLMs. Simple, well-executed, similar spirit to IPO. IPO is more comprehensive in evaluation but has the 30-prompt analytical limitation.
- **Booster (tTPHgb0EtV, 8.0):** Regularizer for harmful fine-tuning, simple/effective with broad evaluation. Comparable depth to IPO.
- **DPO Likelihood Displacement (uaMSBJDnRv, 7.0):** Theoretical/empirical paper about DPO failure modes. IPO is broader in scope and evaluation.
- **TPO (O0sQ9CPzai, 6.33):** DPO for reasoning (math), limited to one task type. IPO clearly superior in evaluation breadth.

**Round-1 bracket: 6.5–8.0. Round-2 narrowing places IPO at 7.5:** stronger than the 7.0 anchors in novelty, problem focus, and empirical scope; comparable to but slightly below the 8.0 anchors due to the small-sample analytical section.

---

## Summary

This paper identifies reasoning-level safety as a distinct and underaddressed problem in Large Reasoning Models (LRMs): existing safety-aligned LRMs show high harmful reasoning rates even when final responses appear safe. The paper proposes **Intervened Preference Optimization (IPO)**, which systematically identifies "compliance cues" in unsafe reasoning traces, replaces them with mined "safety triggers," and trains on the resulting preference pairs via partial DPO focused only on the divergence segment. Experiments on three LRMs and three adversarial benchmarks show consistent reductions in reasoning harmfulness, outperforming SFT-based and RL-based baselines by over 30% relative reduction while preserving or improving reasoning capabilities.

---

## Strengths

- **Concrete motivation from a new evaluation angle:** Figure 2 / Table quantitatively demonstrates that RealSafe and STAR models—considered strong LRM safety baselines—still produce harmful reasoning at high rates (e.g., 52.2–85.0% on WildJailbreak for STAR-7B). This is not a rhetorical point; it is backed by GPT-4o-scored evaluations on 100–250 benchmark prompts per dataset, establishing a clear gap that IPO targets.

- **Systematic discovery of safety-critical structure in reasoning traces:** The CSR (Continuation Safety Ratio) formalism in Section 3.1 and the identification of "safety triggers" as sharp CSR inflection points provide a principled, automatically applicable lens on reasoning safety dynamics, going beyond prior qualitative observations of such sentences (Zhou et al., 2025b). The Pearson correlation R=0.85 between compliance cue index and CSR turning point in Figure 5(b) illustrates that the onset of unsafe continuation is predictable and localizable.

- **Strong, consistent empirical performance:** Table 2 shows IPO achieves the lowest average reasoning harmfulness across all three models (DS-8B: 15.3%, DS-7B: 18.4%, Qwen3-8B: 13.9%), while maintaining competitive or best-in-class reasoning capability scores across AIME, MATH, GPQA, and HumanEval. The simultaneous improvement in safety and preservation of capability is non-trivial and clearly demonstrated.

- **Ablation that validates core design choices:** Table 3 confirms partial DPO on the divergence segment (10.9%) substantially outperforms full-trajectory DPO (19.0%) and SFT (42.3%), directly supporting the localized supervision design. Figure 7 further shows IPO's KL divergence peaks at compliance cue positions, mechanistically confirming targeted training.

- **Detector robustness enabling self-improvement:** Table 3 shows IPO with DS-8B as its own compliance cue detector (19.4%) remains effective relative to GPT-4o (13.7%) and DeepSeek-R1 (13.6%), providing a path toward teacher-free deployment.

---

## Weaknesses

### Fatal
None.

### Major

- **Small-sample analytical foundation for key quantitative claims.** Sections 3.1–3.3 — which establish the entire motivating empirical basis for IPO — are built on **30 prompts** sampled from JailbreakBench. The paper reports that "over 90% of sampled safe trajectories contain such turning points" and a Pearson correlation of R=0.85 from this same pool. At n=30, the confidence interval on R=0.85 is wide enough to encompass substantially smaller values, and the 90% coverage rate has high variance. The paper notes an extension to Qwen3-8B exists in Figure 10 (appendix) but the core quantitative claims — especially the correlation and coverage rate — rest on 30 prompts. This is the intellectual foundation of the method; the design may be correct, but the evidential standard should be higher for central claims. Expanding the analysis to the full JailbreakBench set (100 prompts) or a held-out sample from WildJailbreak would substantially strengthen these claims.

### Minor

- **Unexplained reward function in Table 1.** The GRPO reward function $\mathbb{I}[z \text{ is safe}] - \mathbb{I}[y \text{ is safe}]$ rewards a trajectory where reasoning is safe and the response is unsafe (+1), gives zero reward when both are safe or both are unsafe, and penalizes a trajectory where reasoning is unsafe but the response is safe (-1). While the paper says this formulation is designed to "emphasize reasoning," the reward signal as written explicitly penalizes safe responses, which is counterintuitive and could have unintended training consequences. The motivation for subtracting the response safety term is not explained in the text.

- **Efficiency comparison conflates training paradigms.** Section 4.3 compares IPO's ≤14 model generations to GRPO's ≥40 and presents this as a sampling efficiency advantage. However, GRPO is an online RL method that continuously updates its policy during generation, while IPO constructs a fixed offline dataset and applies DPO. The paper notes GRPO was given "at least twice the sampled trajectories of IPO," but a controlled comparison (GRPO at equal generation budget) is absent. The efficiency advantage is plausible in spirit and directionally supported by wall-clock times (~40 min vs. >2 hours), but the generation-count comparison is not a clean apples-to-apples measure.

- **Qwen3-8B partially dilutes the motivating analysis.** Figure 3 data shows Qwen3-8B has only 3.7% in the "unsafe reasoning + safe response" category—an order of magnitude less than DS-8B (40.5%) and DS-7B (51.3%). While Qwen3-8B still has 28.2% "unsafe reasoning + unsafe response," the framing in Section 2.2 that unsafe reasoning leads to safe responses and thus is a hidden risk is weaker for this model. The discussion could acknowledge this heterogeneity more explicitly.

### Trivial

- **Figure 3 caption inconsistency.** The caption reads "Distribution of reasoning and response safety in outputs from DS-8B," but the underlying table clearly shows data for DS-8B, DS-7B, and Qwen3-8B. The caption was likely not updated when the scope was broadened.

---

## Nice-to-Haves

- **Characterize the diversity of the trigger pool and show robustness to trigger selection.** The paper uses 6 triggers sampled from a pool (Section 4.1). It is not described how these 6 were selected or how sensitive results are to random trigger selection. A brief ablation over random 6-trigger subsets would significantly strengthen the generalization claim.

- **Brief main-text characterization of the adaptive attack experiment.** Appendix B.2 reportedly evaluates robustness to adaptive attacks; since IPO's aligned models may develop systematic reasoning patterns tied to the trigger vocabulary, the extent of adversarial robustness is an important property worth briefly summarizing in the main text.

- **The compliance-cue detector robustness deserves more prominence.** The result that DS-8B can serve as its own detector (Table 3) is a practically important finding — it suggests IPO can work without teacher model access — but it is described briefly in the ablation section. Highlighting this in the conclusion or abstract would improve the paper's practical framing.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **Harsh critic: Figure 6 shows identical values for all three triggers (potentially a data error).** The extracted table shows all three trigger lines identical to the average at every step. However, the figure description explicitly names three distinct visual lines and describes them with distinct colors (red, green, blue). This is most parsimoniously explained as an integer-rounding artifact in the extracted table (e.g., 60.1%, 59.7%, 60.2% all round to 60%). The figure in the actual submission very likely shows visually distinct (but close) trajectories. **Removed** as a likely PDF extraction artifact per the hard rule on formatting/parser artifacts.

- **Harsh critic: Equation 4 DPO objective notation error (π_θ in both terms of first log-ratio).** The critic flagged that the first log-ratio uses π_θ in both numerator and denominator for the chosen trajectory. This is noted as "very likely a PDF-parsing artifact" even by the critic. **Removed** under the hard rule on parser/formatting artifacts.

- **Harsh critic: "Exactly the value function" overstates the formal claim.** The paper writes "CSR S_t(x,z) is exactly the value function V^π(s_t)." The critic notes this conflates the empirical estimate (32 sampled continuations over 30 prompts) with the population quantity. This is a minor precision issue in an explicitly analogical remark (the sentence begins "if we treat…"). **Removed** as an overreading of an intentionally analogical framing; the paper does not present this as a formal theorem.

- **Harsh critic / strength finder: Figure 6 as a validated strength.** Given that Figure 6's identical trigger values raise ambiguity (likely rounding, but not verifiable from the extracted text alone), the specific strength claim "Figure 6 demonstrates safety triggers reliably steer reasoning" is partially retained as a directional result but the precise numerical comparison across triggers is not confirmed. The overall decline from 100% to ~15% harmful ratio after 5 iterations IS clearly shown for the average.

- **Harsh critic: Missing human evaluation of intervened trajectories.** The critic suggests human evaluation on intervened trajectories to confirm quality beyond GPT-4o evaluation. While a useful suggestion, human evaluation is not standard practice in this field setting and requesting it as a weakness is scope creep. **Moved to Nice-to-Have.**

---

## Novel Insights

The paper's most novel contribution is framing LRM reasoning safety as a *localized, predictable* problem rather than a diffuse one. The identification that safe reasoning is often "secured" at a single early sentence (safety trigger), and that unsafe trajectory divergence is equally concentrated at the first compliance cue, reframes safety alignment from a full-sequence supervision problem to a **step-level intervention problem**. This concentration of safety-critical signal at specific positions motivates partial DPO — training only on the divergent suffix — which the ablation confirms is significantly more effective than full-trajectory approaches. This insight connects to reward-shaping theory (Section 3.4) in a way that generalizes beyond safety: anytime safety-critical decisions are concentrated in localized steps, partial preference optimization on those steps should be superior to outcome-only supervision. This principle could extend to multi-turn dialogue safety, agentic planning, and other settings where trajectory-level safety signals are sparse.

---

## Suggestions

1. **Scale the Section 3 analysis from 30 to ≥100 prompts**, ideally including held-out prompts from WildJailbreak, and report confidence intervals on R and the 90% coverage rate. This would lift the analytical foundation to match the strength of the empirical results.

2. **Clarify the reward function** $\mathbb{I}[z \text{ is safe}] - \mathbb{I}[y \text{ is safe}]$ in Table 1 with one sentence explaining why subtracting response safety (rather than just rewarding reasoning safety) produces better alignment signals.

3. **Add a trigger-selection ablation** in Table 3: report results for two or three randomly selected 6-trigger subsets from the full pool to show the method is not sensitive to the specific triggers chosen.

4. **Add a 2-sentence summary of the adaptive attack results** from Appendix B.2 in Section 4.3, so readers can evaluate robustness without navigating appendices.

---

## Score and Decision

**Anchor comparison:**

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Multi-Objective ORPO | aYYZBPoSHb.md | 3.40 | R1 | Much weaker: incremental method, limited novelty |
| Soft Alignment SPO | 28TLorTMnP.md | 2.50 | R1 | Much weaker: narrow contribution |
| POROver | 5EuAMDMPRK.md | 5.75 | R1 | Weaker: safety-utility tradeoff without novel analysis |
| DPO Margin Issues | YaBiGjuDiC.md | 6.00 | R1 | Weaker: analysis paper without comparable empirical scope |
| TPO | O0sQ9CPzai.md | 6.33 | R1 | Weaker: limited to math reasoning, less evaluation breadth |
| Backtracking | Bo62NeU6VF.md | 8.00 | R1 | Comparable: novel safety mechanism, simpler method, strong evaluation |
| Booster | tTPHgb0EtV.md | 8.00 | R1 | Comparable: effective safety method, good ablations |
| Logicbreaks | pljYMCYDWJ.md | 6.20 | R2 | Weaker: theoretical analysis without proposed method |
| Jailbreaking LLMs | hXA8wqRdyV.md | 6.14 | R2 | Weaker: attack paper, no defense/alignment contribution |
| CoT Info Theory | ouRX6A8RQJ.md | 6.40 | R2 | Weaker: analysis tool without alignment method |
| DPO Likelihood Displacement | uaMSBJDnRv.md | 7.00 | R2 | Slightly weaker: insightful theoretical paper, limited evaluation scope |
| Catastrophic Jailbreak | r42tSSCHPh.md | 7.00 | R2 | Different problem; comparable empirical scope |
| RLHF Trustworthiness | FpiCLJrSW8.md | 7.00 | R2 | Weaker: analysis without proposed method |
| f-DPO | 2cRzmWXK9N.md | 7.25 | R2 | Comparable theoretical rigor, narrower scope |

**Bracketing:** Round 1 placed the paper between 6.5 and 8.0. Round 2 confirmed the paper is clearly above the 6.2–7.25 cluster and comparable to the 8.0 anchors.

**Final position:** The paper is stronger than the 7.0–7.25 anchors in novelty (specifically targets LRM reasoning safety, a genuinely new angle), evaluation breadth (3 models × 3 benchmarks × 4 reasoning tasks), and practical impact. It is slightly below the cleanest 8.0 anchors (Backtracking, Booster) due to the small-sample analytical section (30 prompts for the central quantitative claims). The method design is sound and the results are convincing; the analytical limitation is a real but resolvable weakness that does not undermine the core contribution.

**Score: 7.5 — Accept**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>