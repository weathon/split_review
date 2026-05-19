- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 5, 6
Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper proposes Self-Alignment for Safety (SAS), a test-time adaptation method for transformer-based offline safe RL. The core idea is to use a learned density model (the Lyapunov condition) to select a "safe" trajectory from the transformer's own imagination, then use that trajectory as a prompt to condition safer action selection — without retraining or fine-tuning. The method is evaluated on Safety Gymnasium (cost-based safety) and MuJoCo (failure-rate-based safety).

## Strengths

- **Novel application of self-alignment to safe RL**: The idea of using a transformer's own imagined trajectories, filtered through a Lyapunov density condition, to generate a safety-inducing prompt at test time is creative and underexplored. The paper connects in-context learning from LLMs (self-alignment) to the offline RL setting, which is a genuine conceptual contribution.

- **Ablation study validates the prompt selection mechanism**: Table 1 directly compares DT+SAS (Lyapunov-conditioned prompt) against DT+rand (random prompt) and DT+maxmax (max-energy prompt). DT+SAS consistently achieves lower cost than both alternatives, providing concrete evidence that the specific Lyapunov-based trajectory selection — not just any prompt — drives the safety improvement.

- **Works with multiple base architectures**: Table 2 shows that SAS reduces cost when applied to both DT (Decision Transformer) and CDT (Constrained Decision Transformer), demonstrating that the method is architecture-agnostic and composable with existing offline safe RL bases.

- **Improves performance on MuJoCo without cost supervision**: In Table 3, DT+SAS improves both reward (+8.9% average return on Walker2d medium vs. DT) and failure rate on Humanoid and Walker2d without requiring cost labels during training, showing generalization beyond cost-annotated environments.

## Weaknesses

### Major

- **Missing comparison to LDM, the direct predecessor**: The paper builds extensively on LDM (Kang et al., 2022) — the Lyapunov density method for offline safe RL — as its theoretical foundation. LDM is discussed in Sections 2, 3, and 4 as the core framework that SAS extends. Yet LDM is absent from all experimental comparisons (Table 2). Since the paper claims to "outperform prior safe RL methods" and SAS is essentially a test-time adaptation layer over a density-based Lyapunov approach, a direct comparison to LDM is critical to establishing whether SAS adds meaningful benefit beyond the base Lyapunov framework.

- **Gap between cost-constrained MDP motivation and density-only algorithm**: The paper derives a safety criterion from a cost-constrained MDP (Equations 2–4) involving cost thresholds \(d\) and \(C_{max}\). However, Algorithm 1 selects prompts based purely on density/energy \(E = -\log\hat{\rho}_{\text{data}}\), with no direct use of cost information. The control invariant set \(\mathcal{R}_G^{\text{SAS}}\) (Equation 7) that encodes cost parameters is never computed or checked by the algorithm. This disconnect undermines the claim that the method addresses *cost-based* safety specifically — it inherits the assumption from LDM that high-density regions are safe, but this assumption is not validated (see PB1 where cost and reward both rise simultaneously). The paper acknowledges this in passing ("cost also increase by the absence of enough cost information") but treats it as an exception rather than a fundamental limitation of the density-only approach.

### Minor

- **No measures of variance reported**: The paper states that results are averaged over "three random seeds" (Table 2 caption) and "100 episodes" (Table 3), but never reports standard deviations, confidence intervals, or any variance measure. Without this, it is impossible to assess whether the reported differences (e.g., CDT+SAS vs. CDT) are statistically significant or within noise.

- **Section 5.1 (hierarchical RL interpretation) is disconnected from the algorithm**: Equations 10–13 and the graphical model in Figure 2 present a theoretical framing of the transformer as performing implicit Bayesian inference over high-level policies. This section has no operational consequence — Algorithm 1 does not perform inference over \(\theta\), does not use the optimality variable \(O_t\) as defined, and the derivation from Equation 11 to Equation 13 assumes access to \(\theta^*\) (the safe high-level policy) which the algorithm never computes. The section reads as a post-hoc overlay that neither motivated nor explains the algorithm's design.

- **Proposition 4.2 assumption conflicts with the setting**: Proposition 4.2 assumes i.i.d. state-action pairs to bound the probability of out-of-distribution trajectories. This is violated by the trajectory structure of the data (autocorrelated sequential samples), and the proposition is not empirically verified (e.g., by computing the bound on real data and checking whether it holds).

- **Inconsistent safety improvement across tasks**: While CDT+SAS reduces cost vs. CDT overall, in PG1, PP1, and PB2 (Table 2), CDT+SAS has *higher* cost than CDT. In PB1, applying SAS to DT *increases* all metrics (reward, cost, failure rate) simultaneously. These exceptions are acknowledged but not explained mechanistically, weakening the claim that SAS provides reliable safety improvement.

### Trivial

- Algorithm 1, lines 10–12: "Compute \(E_t\) of each time-step" — it is ambiguous which model produces \(E_t\) (the VAE density estimate? the autoregressive policy?). This should be specified for reproducibility.
- Equation 1 (LDM operator) and the LDM Bellman operator are presented in preliminaries but never referenced again, which may confuse readers about their role in the paper.

## Nice-to-Haves

- **Incorporate cost into prompt selection**: A natural extension would be to weight or filter imagined trajectories by learned cost estimates, closing the gap between the cost-constrained framing and the density-only algorithm.
- **Ablation of density vs. cost**: A simple ablation using cost-weighted energy would clarify whether density alone is sufficient for safety or whether cost information is needed in low-density-but-high-cost regions.
- **Analysis of prompt quality**: The paper does not analyze how often the selected prompt actually leads to lower cost in execution, or how prompt quality degrades when the density–cost correlation is weak (e.g., PB1).

## Removed Points

These are flagged for removal — treat with caution:

1. **Criticism about Z not being defined or used**: The reviewer claimed the latent skill space \(\mathcal{Z}\) "never appears" or is "never clearly defined." It *is* defined in Section 3 and used theoretically in Section 5.1. The algorithm does not use it, but that is a separate point already covered above. The "never clearly defined" claim is incorrect.

2. **Criticism that LDM operator is presented but never used**: The LDM operator is presented in the Preliminaries as background (Definition 3.1, Equation 1). This is standard practice — related work is presented for context, not because the paper claims to use it. This is a misunderstanding of what a preliminaries section is for.

3. **Criticism about "SAC is included despite being an online method"**: Including SAC as a reference point (showing what an online, non-safe method achieves) is standard in safe RL evaluations to calibrate the safety-performance tradeoff. The table clearly labels unsafe agents in gray. Not a genuine weakness.

4. **Criticism about APE-V comparison being irrelevant**: APE-V is presented as a test-time adaptation method, not a safety method. The comparison is about reward improvement under test-time adaptation, which is within scope. The paper does not claim APE-V is a safe RL baseline.

5. **Criticism that the abstract's "outperforms by up to 2 times" is unsubstantiated**: This is a quantitative claim supported by the reported numbers in Tables 2 and 3 (e.g., cost reductions and failure rate improvements). Whether the baselines are appropriate is addressed in the Major weaknesses above; the claim itself is numerically substantiated.

6. **Section-by-section notes about Equation 3→4 assumptions**: These are presented as "confusing" rather than as a specific identifiable error. The core point about the gap between theory and practice is already covered in the Major weaknesses section.

7. **Criticism about the claim that "cost decreases in all three environments" for Figure 4 not being visible**: The paper states this claim in text alongside the figure. The figure image is not available in the text extraction, so the reviewer cannot verify whether it is visible or not. Remove this speculative criticism.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the reviews is the tension between the method's theoretical framing (cost-constrained MDP) and its practical implementation (density-only prompt selection). This highlights a broader question for the density-based safe RL literature (LDM, DCRL, and this work): when does density correlate with safety, and when does it break down? The PB1 case in this paper — where applying SAS increases *both* reward and cost — provides a concrete counterexample that could be a starting point for studying when density-based safety proxies fail. The self-alignment framing itself is also a useful conceptual bridge between LLM alignment techniques and RL safety, independent of the specific density-based instantiation.

## Suggestions

1. **Add LDM and at least one other safe offline RL baseline** (e.g., BC-Safe or CPQ if available on Safety Gymnasium) to Table 2. Without this, the claim of outperforming "prior safe RL methods" rests entirely on comparison to CDT.
2. **Report standard deviations** across seeds for all metrics in Tables 1–3.
3. **Either integrate cost into the prompt selection** (e.g., by filtering out imagined states with high predicted cost) **or explicitly scope the paper** as a density-based safety method and drop the cost-constrained MDP framing from the theoretical motivation.
4. **Streamline or remove Section 5.1** and replace it with a clear explanation of why minimizing maximum energy corresponds to staying in high-probability (and therefore safer) regions. A concise operational explanation would serve the paper better than the current theoretical derivation.
5. **Explain the PB1 anomaly**: why does SAS increase all metrics simultaneously, and under what conditions should users expect similar behavior?
