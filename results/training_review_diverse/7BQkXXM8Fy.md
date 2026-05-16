Now I have all the information I need. Let me verify the key claims against the paper and write the consolidated review.

---

## Summary

This paper presents a systematic empirical study of design choices for diffusion planning in offline reinforcement learning, training over 6,000 models to investigate four key components: guided sampling algorithms, network architecture, action generation methods, and planning strategies. It identifies several counterintuitive findings (e.g., unconditional Monte Carlo sampling with selection can outperform guided sampling, Transformer outperforms U-Net as the denoising backbone, jump-step planning is beneficial) and distills them into a simple baseline method (Diffusion Veteran). The paper should be evaluated as an empirical investigation/design-space study, not as a novel-algorithm paper.

## Strengths

1. **Large-scale systematic investigation.** The paper trains and evaluates over 6,000 diffusion models across four key design dimensions — far exceeding the scale of any prior study in diffusion planning. This provides a broad empirical foundation for the conclusions (abstract, Section 4).

2. **Counterintuitive and practically useful findings.** The paper identifies several design choices that contradict common practice: (a) unconditional Monte Carlo sampling with selection (MCSS) can outperform classifier/classifier-free guidance when datasets contain sufficient near-optimal trajectories (Section 4.5, Fig. 7); (b) Transformer outperforms U-Net as the denoising backbone, especially on long-horizon tasks (Section 4.3, Fig. 5a); (c) jump-step planning consistently beats dense-step planning (Section 4.2, Fig. 4). Each finding is backed by controlled experiments with error bars.

3. **Value-distribution analysis providing mechanistic insight.** Beyond raw performance numbers, Figure 7(b) plots the value distribution of data across environments and shows a clear correlation: MCSS works when the dataset contains substantial near-optimal trajectories, while CFG is preferable when most data is suboptimal. This hypothesis-generating analysis gives readers a tool to predict which guidance method suits their setting.

4. **Concrete, actionable takeaways.** Section 4.8 distills the findings into seven specific, non-obvious practical tips (e.g., "use inverse dynamics for action generation," "try jump-step planning," "try Transformer for long-horizon tasks"). These make the results immediately useful for practitioners and future researchers.

5. **Honest discussion of limitations and future work.** Section 5 provides a balanced discussion of the computational cost, the System 1/System 2 framing (appropriately caveated as an analogy), and open problems — showing awareness of the paper's scope and boundaries.

## Weaknesses

### Fatal
None.

### Major

1. **Imprecise state-of-the-art claim that is partially contradicted by the paper's own results.** The abstract claims DV "achieves state-of-the-art results on standard offline RL benchmarks" and Section 4 states DV "outperforms all previous diffusion planning and diffusion policy methods." However, Figure 8 explicitly shows that DQL (a diffusion policy method) outperforms DV on MuJoCo locomotion tasks, and the paper acknowledges this in the caption. While DV may be SOTA on Kitchen/Maze2D/AntMaze collectively, the blanket phrasing in the abstract and Section 4 is inconsistent with the nuanced results presented in Figure 8. This needs to be qualified per task family.

2. **Insufficient reporting of basic experimental methodology for an empirical study.** The paper repeatedly shows "error bars" but never states whether they are standard deviations across random seeds, across rollouts, or something else. The number of random seeds used is not reported anywhere in the visible text. While the paper explicitly says it excludes "common deep learning hyperparameters such as learning rates" (Section 3) and likely places numerical results in the appendix (reference to Table 10), the omission of seed counts and error-bar definitions from the main paper is a significant gap for an empirical study that positions itself as "a solid starting point." For example, how many seeds were used for the key result that Transformer outperforms U-Net in 8/9 subtasks? Without this information, the reader cannot assess the statistical reliability of the findings.

### Minor

1. **Control-variable analysis anchored on a single best configuration limits generalizability.** The paper's three-step procedure (Section 3.2) finds one best model via search, then varies one component at a time from that configuration. This is a standard ablation approach, but the paper does not demonstrate that its key conclusions (e.g., Transformer > U-Net, MCSS > guidance) hold when starting from different base configurations. For instance, the finding that MCSS outperforms CG/CFG (Section 4.5) may depend on properties of the chosen critic function or sampling budget N in the DV configuration. Replicating the main conclusions from 2–3 different base configurations would substantially strengthen confidence in their generality.

2. **Adroit validation (Section 4.7) contains zero quantitative results.** The subsection states findings are "consistent with our findings" but provides no numbers, table, or figure. For a paper that claims generalizability, this is a gap. Even a brief summary table would suffice.

3. **Attention weight analysis is over-interpreted relative to the evidence.** The paper argues that "attention length × stride ≈ constant" from Figure 5(b) and that this shows "invariant correlations across the stride, contributing to the generalization performance." This interpretation is based on visual inspection of attention patterns from a *single* Transformer on a *single* task (Kitchen). The paper acknowledges more study is needed ("In-depth study will be needed to fully understand..."), but the strength of the language in the main text ("invariant correlations contributing to generalization") exceeds what one anecdotal example supports.

4. **Comparison limited to a single diffusion policy method.** The comparison in Section 4.6 contrasts DV (diffusion planning) only with DQL as a representative of diffusion policy. While this is defensible given the paper's focus on planning, the claim that DQL is "the representative" of diffusion policy methods is not justified — methods such as IDQL, Diffusion-QL, and others exist. This does not invalidate the paper's findings, but the reader should interpret the diffusion-planning-vs.-diffusion-policy comparison as a preliminary observation rather than a comprehensive analysis.

### Trivial
None.

## Nice-to-Haves

- **Multi-factorial validation:** Verifying the main conclusions from 2–3 alternative base configurations would significantly strengthen the paper's claims of generalizability.
- **Full Adroit results in the main text:** Even a brief table would address the current omission.
- **Seed/statistics disclosure in the main text:** Stating the number of seeds and the meaning of error bars would address the reproducibility concern efficiently.

## Removed Points

- **"6,000 models claim not substantiated":** The paper clearly states this figure and describes the search procedure (comprehensive search via grid search + manual tuning). The control-variable analysis from a single best config is a legitimate ablation methodology concern (kept as a minor weakness above), but the claim that the 6,000 figure itself is unsubstantiated is not supported by the paper text.
- **"DQL outperforms DV on MuJoCo undermines SOTA claim":** This specific sub-point misreads the paper — the paper *acknowledges* this in Figure 8's caption and discusses the task-dependent trade-off in detail. The broader issue of an imprecise SOTA claim in the abstract is retained above.
- **"Missing related works":** Cannot be verified without external sources (per instructions).
- **"More diffusion policy baselines needed":** The paper is about diffusion *planning*; comparing with one representative diffusion policy method is a defensible scope choice for a design-space study. This is a wishlist item, moved to Nice-to-Haves.
- **"Table 1 missing from parsed text":** The parser strips tables/appendices from all papers; the table exists in the original submission. Numerical results are likely in the appendix (reference to Table 10).
- **"Missing hyperparameters (learning rates, batch size, etc.)":** The paper explicitly scopes out "common deep learning hyperparameters such as learning rates" (Section 3), which is a reasonable choice for a design-space paper. The more fundamental omission (seeds, error-bar definitions) is retained above.
- **Strength Finder's claim about "Adroit validation as a strength":** Removed because the subsection lacks quantitative results — it is a weakness, not a strength.

## Novel Insights

The most genuinely novel observation emerging from the review process is the **value-distribution conditional recommendation** (Fig. 7b): the paper shows that the optimal guided sampling algorithm depends on the concentration of near-optimal trajectories in the dataset, providing a testable hypothesis for when to use MCSS vs. CFG/CG. This is more specific and actionable than the typical "guidance is good" heuristic and deserves more emphasis. The attention-weight "stride × attention-length ≈ constant" observation is intriguing but too preliminary to count as a robust insight.

## Suggestions

1. **Qualify the SOTA claim per task family.** The abstract and Section 4 should say something like "DV achieves state-of-the-art results on long-horizon planning tasks (Kitchen, Maze2D, AntMaze) and is competitive with diffusion policy methods on locomotion tasks" — this accurately reflects Figure 8.

2. **Add a brief table in the main text** reporting DV's performance with standard deviations and number of seeds for each task. This single addition would address the most serious reproducibility concern.

3. **State the number of random seeds and what the error bars represent** explicitly in the experimental setup (Section 3) — e.g., "All results are averaged over 5 random seeds; error bars show ±1 standard deviation."

4. **Include the Adroit results** — even a short paragraph with a few numbers would transform Section 4.7 from a placeholder into evidence.

5. **Tone down the attention analysis language.** Replace "invariant correlations contributing to generalization" with "suggestive evidence that warrants further investigation" — the current phrasing oversells one visual example.

## Score and Decision

**Originality:** Good — the paper tackles a timely question with a scale of experimentation that exceeds prior work. **Importance:** High — diffusion planning is an active area with inconsistent design choices; systematic guidance is valuable. **Claims support:** Moderate — the control-variable analysis is reasonable but the blanket SOTA claim is imprecise, and experimental methodology details (seeds, error-bar definitions) are insufficiently reported. **Soundness:** Moderate — the core experiments appear well-designed, but incomplete reporting undermines verifiability. **Clarity:** Good — the paper is well-structured and the takeaways are clearly presented. **Value to community:** High — the practical tips and baseline will likely be used by other researchers.

The paper makes a genuine contribution through its large-scale empirical investigation and counterintuitive findings. However, the imprecise SOTA claim and gaps in experimental reporting (seeds, error-bar definitions, missing Adroit numbers) reduce confidence in the results. These issues are addressable with moderate revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>