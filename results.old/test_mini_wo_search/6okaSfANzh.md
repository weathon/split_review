Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

## Summary

The paper proposes LLM cascades for cost-efficient reasoning, where a weaker/cheaper LLM (GPT-3.5-turbo) first answers each question, and a decision maker based on "answer consistency" determines whether to route the question to a stronger/expensive LLM (GPT-4). The key innovation is using a **mixture of thought (MoT) representations** — combining Chain-of-Thought and Program-of-Thought prompts — to obtain more diverse answer samples that better discriminate easy from hard questions. The paper instantiates ten cascade variants (vote-based and verification-based) and evaluates them on six reasoning benchmarks, reporting that MoT-based cascades match GPT-4-CoT-SC accuracy (92.9% vs. 93.1%) at ~40% of the cost.

## Strengths

- **MoT diversity measurably improves difficulty discrimination.** The analysis in Section 4.5 (Figure 4) directly shows that MoT-1D-Vote produces a larger "consistency gap" between easy and hard questions than CoT-1D-Vote or CoT-2D-Vote, especially on the Navigate dataset where the performance gain is largest. This provides a mechanistic explanation for why mixing thought representations helps cascade routing — a finding that goes beyond simply reporting aggregate improvements.

- **Training-free verification outperforms fine-tuned verifier baselines.** Section 4.3 compares verification-based cascades (CoT-2D-Verify, MoT-1D-Verify) against cascades using fine-tuned RoBERTa or GPT-3.5-turbo verifiers. The proposed methods achieve higher accuracy at the same cost (e.g., 0.951 vs. 0.892 on GSM8k), demonstrating that consistency-checking is more effective for reasoning tasks than learned verifiers from prior work (Chen et al., 2023).

- **Cost-aligned experimental design.** The paper explicitly accounts for the fact that different prompting strategies (1D vs. 2D, CoT vs. PoT) consume different numbers of input tokens, and configures sample sizes to make costs approximately comparable across approaches. Actual token costs are reported, strengthening the validity of cost-efficiency comparisons.

- **Robustness across hyperparameters.** Section 4.4 varies temperature (0.4–0.8) and sample size (K=20–40) on three datasets; MoT-1D-Vote consistently outperforms CoT-2D-Vote under all settings, showing the benefit is not fragile.

## Weaknesses

### Fatal
None.

### Major

- **Duplicate and unreconciled method exposition (Sections 2.2–2.3 vs. Section 3).** The paper presents two nearly complete, parallel descriptions of the same cascade decision-making methods using different notation and terminology. Section 2.2–2.3 introduces vote-based and verification-based methods with variables like $A^w$, $K$, $\tau$, Eq. 1–2, while Section 3 re-derives the same methods from scratch under different variable names ($L$, $A_W$, $A_{major}$, Eq. 2–3), with a different figure (Figure 3/4 vs. Figure 2) and no cross-referencing. Section 3 does not reference Section 2, and the notation swap (e.g., Eq. 1 vs. Eq. 2, Eq. 2 vs. Eq. 3) creates confusion about which definitions the experimental sections rely on. This is not a minor formatting issue — it appears two drafts were merged without reconciliation. The paper would be substantially clearer if it retained only one exposition (Section 2.2–2.3 is the more complete one) and dropped or subsumed Section 3.

### Minor

- **Ambiguity about GPT-4 decoding strategy when invoked in the cascade.** The paper states the stronger LLM is "GPT-4 (8k context) with CoT self-consistency [SC]" (line 162), which suggests GPT-4 always uses SC (K=3) when called, whether as a baseline or in the cascade. However, the cost formula (Eq. 1) treats $C^s$ as a single term, and it is not explicitly stated whether a cascade-routed question to GPT-4 uses greedy decoding or SC. If greedy, the comparison to GPT-4-CoT-SC undervalues the cascade's GPT-4 cost; if SC, the paper should clarify that $C^s$ already incorporates K=3 samples. The most natural reading supports SC being used consistently, but the paper should state this explicitly. This does not invalidate the results but demands clarification.

- **No tabular results at the claimed operating point.** The headline claim (~92.9% accuracy at 40% cost across six datasets) is supported only by curves in figures. A table reporting accuracy and relative cost for each of the ten approaches on each dataset at the operating point(s) achieving 40% cost is essential for independent verification and per-dataset analysis.

- **K=3 for GPT-4 not justified.** The paper uses K=3 for GPT-4 self-consistency while noting that self-consistency "typically uses 5–20 samples." The choice is not arbitrary (it affects the cost baseline), but no justification is given for why 3 is sufficient for GPT-4 in this setting.

- **No discussion of tie-breaking in the vote-based method.** Eq. 1 defines the agreement score $s$ based on the most-consistent (majority) answer, but the paper does not state how ties for the majority answer are resolved, or whether ties trigger routing to GPT-4. This matters for reproducibility.

- **L=2 not explored.** The paper fixes the number of prompts at $L=2$ for the verification-based and 2D approaches but does not explore L=1 (single prompt, purely in-distribution sampling) or L>2. While L=2 is a reasonable default, the paper would be stronger with a brief ablation or at least a justification for this choice.

### Trivial
None.

## Nice-to-Haves

- A brief discussion of why $L=2$ is chosen versus $L=1$ or $L>2$, even if only to explain that the cost grows linearly with $L$ and two sources provide sufficient diversity.
- Explicit statement of tie-breaking rules for majority voting.

## Removed Points

The following points from the reviewers are removed with justification:

- **"40% of which cost?"** — Removed. The paper clearly states on line 162 that relative cost is "compared with the cost of GPT-4 with CoT SC (denoted as GPT-4-CoT-SC)." The baseline is unambiguous.
- **"Truncated section on factual-based tasks"** — Removed per instructions (parser artifact, not an author error). The original submission is complete.
- **"Cost of decision maker $C^d$ not empirically accounted"** — Downgraded to Trivial and moved here. The paper acknowledges cost simplifications (line 100) and explicitly reports actual token costs. $C^d$ is negligible relative to LLM API calls.
- **"Figure 5 vs. Figure 1 confusion"** — Removed. The paper does not reference a "Figure 5" in the text; the reviewer's specific figure-number complaints do not match the paper as written. The broader point about duplicate exposition is already included as a Major weakness.
- **"Missing appendix content / proofs"** — Removed per instructions (parser strips appendix sections).
- **Strength Finder's generic framed strengths ("important problem", "timely")** — Removed. Dropped generic/superficial framings; only concrete, evidence-grounded strengths retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Unify Sections 2 and 3.** Retain the tighter, more complete exposition from Section 2.2–2.3 and either delete Section 3 or subsume its cost-alignment details (Section 3.3) as a short subsection of Section 2. Unify notation throughout.
2. **Add a table** reporting accuracy and relative cost for each method on each dataset at the operating point corresponding to the 40% cost claim. This would replace sole reliance on figures and allow per-dataset verification.
3. **Explicitly state** whether GPT-4 uses greedy decoding or SC (K=3) when invoked by the cascade. If SC is used, clarify that $C^s$ in Eq. 1 represents the cost of K=3 GPT-4 calls.
4. **Add a brief note** on how ties are resolved in the vote-based method, and justify the choice of K=3 for GPT-4.

**Evaluation on standard axes:**
- *Originality:* Good — using answer consistency as a routing signal and MoT for better difficulty discrimination is a novel combination.
- *Importance of research question:* High — cost-efficient LLM usage is practically valuable.
- *Claims supported:* Mostly yes, but the duplicate exposition and missing tabular results weaken the presentation of evidence.
- *Soundness of experiments:* Sound overall, with cost-aware design and robustness checks.
- *Clarity of writing:* Clouded by the structural duplication but otherwise clear.
- *Value to community:* Solid — the approach is training-free and easy to implement.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>