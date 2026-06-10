Now I have all the information I need. Let me produce the final review.

## Summary
This paper develops a Sequential Monte Carlo (SMC) framework for controlled LLM generation under heterogeneous syntactic and semantic constraints. The key methodological innovation is partitioning constraints into "efficient potentials" (used in the proposal distribution via local product-of-experts) and "semantic potentials" (evaluated only during importance weighting and resampling), enabling integration of constraints that cannot be encoded as per-token logit masks. Experiments across four domains — Python code generation (DS-1000), text-to-SQL (Spider), goal inference (Planetarium), and molecule synthesis (GDB-17) — with systematic 7-method ablations show that the full SMC approach outperforms ablated baselines, and that performance ordering correlates with how closely each method approximates the global product-of-experts posterior.

## Strengths

- **Principled separation of efficient vs. semantic potentials, validated by systematic 7-method ablation across four domains.** The paper formally distinguishes Φ_eff (used in proposals, e.g., CFG constraints with tractable per-token normalization) from Φ\Φ_eff (evaluated only during weighting). The cumulative ablation (LM → Grammar-only → Grammar-only IS → Grammar-only SMC → Sample-Rerank → Full IS → Full SMC, lines 117–135) isolates the contribution of each component. Table 2 shows each added component produces measurable gains in at least some domains, and Full SMC ranks best or tied-best everywhere. This is a clean experimental design that directly tests the paper's central algorithmic claims.

- **Weight correction empirically reduces the distribution distortion of locally constrained decoding.** The paper goes beyond stating the well-known theoretical gap between local and global product-of-experts and directly measures it. Figure 2 shows that methods with weight corrections (Full IS, Full SMC) have significantly lower estimated KL divergence to the global posterior than Sample-Rerank (which applies semantic potentials post-hoc without correcting for the local proposal). Table 3 shows positive Pearson correlations between particle weights and accuracy, confirming higher-weight particles are better-calibrated — a non-trivial empirical validation of the probabilistic framing.

- **Resampling provides accuracy gains beyond importance sampling alone.** Full SMC vs. Full IS (Table 2) shows that adding adaptive resampling improves accuracy in three of four domains (all except text-to-SQL, where it does not hurt). This confirms that the sequential reallocation of computation to promising partial sequences has practical value beyond the weight correction already present in importance sampling.

- **Statement-level SMC steps for code generation.** The paper extends SMC beyond token-level steps to operate over semantically meaningful increments (Python statements), which improves particle alignment (lines 109–110). This is exploited in the DS-1000 experiments and represents a practical extension that addresses a real limitation of token-level SMC.

## Weaknesses

### Fatal
None.

### Major

- **DS-1000 uses a fundamentally different setup (70B model, different compute, trivial CFG potential), weakening the cross-domain narrative.** DS-1000 uses Llama 3 70B with 4 H100 GPUs + 64 vCPUs, while the other three domains use Llama 3.1 8B with 1 A100 + 12 vCPUs (lines 136–137, 148). Furthermore, φ_CFG = 1 for DS-1000 — there is no grammar constraint — so the method here reduces to "sample from the base LM, then execute partial programs on test cases." The within-DS-1000 method comparisons are valid (all methods use the same 70B model), and the paper is transparent about the asymmetry. But the abstract and introduction frame results as a unified cross-domain demonstration, and the DS-1000 results are not directly comparable to the other domains in model scale, compute budget, or algorithm structure. A reader cannot tell how much of the DS-1000 gain comes from SMC vs. the 70B model's greater raw capability or the aggressive test-case validation signal. Running DS-1000 with Llama 3.1 8B (even with lower absolute scores) would substantially strengthen the cross-domain narrative.

### Minor

- **The KL divergence analysis (Figure 2) rests on one instance per domain — too thin to support the central interpretive claim.** The paper selects "the instance with the median unique accuracy as a representative example" per domain (line 179). The claim that "generation quality is correlated with how well each method approximates the global product of experts" (line 199) and the method ordering in Figure 2 are supported by only 4 data points (one per domain), each with within-run error bars but no across-instance variability. Table 3 provides complementary evidence (correlations across all instances within a method), but the between-method comparison in Figure 2 needs more instances per domain to be convincing.

- **No empirical comparison to the prior SMC-for-LM methods that the paper distinguishes itself from.** The paper builds on Lew et al. (2023) and contrasts with Zhao et al. (2024) (lines 190–191). Grammar-only SMC is described as a "straightforward application of Lew et al. (2023)" (line 128), which partially addresses this. But the key innovation — Full SMC with semantic potentials and resampling — is not empirically compared to any variant of Zhao et al. (2024)'s learned-twist approach, nor to any published controlled generation system for Spider or DS-1000. The introduction claims the method offers a superior approach, but this is positionally asserted, not tested.

- **The main metric is posterior-weighted accuracy, which conflates generation quality with weight calibration.** Weighted accuracy is the right metric for evaluating posterior approximation quality. But it is not the metric practitioners typically care about (best-of-N, majority-vote, or single-sample accuracy). A method could have good weighted accuracy because the weights are well-calibrated even if no individual particle solves the task. Reporting unweighted accuracy alongside weighted accuracy would strengthen practical relevance.

### Trivial

- **The "Further extensions" paragraph (lines 109–110) mentions stochastic approximations to expensive Φ_eff potentials, but this idea is never evaluated or used.** The statement-level SMC extension is used, but the stochastic approximation remains a dangling loose end.

## Nice-to-Haves

- Report wall-clock time or token-generation cost for each method, especially for DS-1000 where partial program execution on test cases is expensive.
- Track effective sample size trajectories or particle diversity (unique ancestors after resampling) to show how well the N=10 particle budget is used.
- Move the N-ablation results (currently in Appendix A.2) into the main paper, or at minimum show that the key findings (e.g., "resampling improves performance") hold across different N values.

## Removed Points

These were filtered from the inputs for the following reasons:

- **"Convergence with respect to N is not demonstrated"** — The paper explicitly says "see App. A.2 for downstream accuracy results for a varying number of particles" (line 136). The parser strips appendices, which exist in the original submission. Speculating about absent appendix content is not valid criticism.
- **"Semantic potential in molecular synthesis is actually syntactic/chemical validity"** — The paper's φ_sem for molecular synthesis checks SMILES validity, valences, and kekulization — these are domain-specific signals the paper categorizes as "semantic" in the sense they cannot be encoded as CFG constraints. This is a labeling preference, not a flaw.
- **"Goal inference semantic potential only gives negative signal"** — This describes the domain's signal structure, not a weakness of the method. The paper transparently states what the potential does.
- **Formatting/style nitpicks (figure placement, garbled characters, whitespace)** — These are parser artifacts from the PDF extraction, not present in the original submission.
- **Strengths that were generic or unsupported** (e.g., "avoids costly contrastive fine-tuning" — claimed but not empirically demonstrated against the cited approach; "addressed an important problem" — generic).

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface a genuinely novel perspective that the paper itself does not articulate.

## Suggestions

1. **Run DS-1000 with Llama 3.1 8B** to provide an apples-to-apples comparison across domains. If infeasible, clearly qualify the cross-domain narrative to acknowledge the asymmetry in model scale, compute, and algorithm structure.
2. **Expand the KL divergence analysis** to cover at least 5–10 instances per domain with error bars across instances, not just across runs on one instance.
3. **Report unweighted accuracy (best-of-N, top-weighted-particle)** alongside posterior-weighted accuracy in Table 2.
4. **Add an empirical comparison to Zhao et al. (2024)** on at least one domain, or explicitly reframe the paper's positioning from "superior approach" to "complementary approach using static/dynamic analysis instead of learned twists."
5. **Remove or operationalize** the dangling stochastic approximation mention in "Further extensions."

## Score and Decision
Score: 7.0  
Decision: Accept

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>