- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5
Now I have a thorough understanding of the paper and both reviews. Let me produce the final consolidated review.

---

## Summary

FedBiOT addresses federated fine-tuning of LLMs while protecting both client data privacy and the LLM owner's intellectual property (model architecture/parameters). The paper identifies that prior offsite-tuning methods (FedOT) suffer when the public distillation dataset differs in distribution from clients' private data. FedBiOT proposes two improvements: (1) using only the last few decoder layers as the trainable adapter (rather than first-two + last-two), and (2) a bi-level optimization framework that repeatedly aligns the compressed emulator with the full model on public data during federated training. Experiments on LLaMA-7B across math reasoning, code generation, and QA tasks show consistent improvements over FedOT and Offsite-tuning baselines.

## Strengths

1. **Problem identification is well-motivated and timely.** The paper clearly identifies the distribution mismatch between the public distillation dataset and clients' private datasets as a genuine limitation of prior offsite-tuning/FedOT (Section 2.2, lines 67-69). The motivating example of differing programming languages across code-generation clients is concrete and grounded. Addressing this gap is both practically relevant and non-trivial.

2. **Consistent empirical improvements across diverse tasks and settings.** FedBiOT shows higher accuracy than baselines on math problem-solving (Table 1), code generation (Tables 2-3), and question answering (Figures 2-3), across both i.i.d. and non-i.i.d. data splits. The gains are often substantial — for instance, on non-i.i.d. code generation with 0.2 dropout, FedBiOT achieves 5.85% Pass@1 with AdapEmu while baselines achieve 0% (Table 2). These patterns are consistent across multiple tasks, dropout rates, and adapter sizes, lending credibility that the overall FedBiOT framework is effective.

3. **Novel adapter selection (only last layers) is well-argued and practically useful.** The proposal to use only the bottom few layers as the adapter (Section 3, Improvement 1) is grounded in known findings about layer specialization (Yosinski et al., 2014) and reduces client-side memory since only activations from the last layers need to be stored. This is a concrete, non-obvious improvement over the prior two-end adapter choice.

## Weaknesses

### Fatal
None.

### Major

1. **Adapter definition differs between FedBiOT and baselines, creating a confound.** The paper states: "Different from (Xiao et al., 2023; Kuang et al., 2023), we regard the last two and the last four decoders as the adapter" (line 131), while baselines use "the first two and the last two decoders as the adapter" (line 135). This means FedBiOT and the baselines fine-tune different subsets of layers — a fundamentally different learning problem. The claimed gains (often >4%) cannot be cleanly attributed to the bi-level optimization (Improvement 2) versus the adapter choice (Improvement 1), because no experiment controls for this: there is no version of FedBiOT using the baselines' adapter, nor a version of FedOT using FedBiOT's adapter. Since the paper presents both as separate contributions, the evaluation must disentangle them. This is the most significant weakness and severely limits what can be concluded from the reported comparisons.

2. **No ablation isolates the effect of the alternating alignment (online emulator refinement).** The core novelty over FedOT is that the emulator is repeatedly aligned *during* federated training, rather than only once before FL begins. Yet there is no experiment that keeps the emulator fixed after initial distillation (like FedOT) while otherwise using FedBiOT's adapter definition and regularization. Without this control, improvements could be driven entirely by the different adapter choice rather than the online alignment. The existing ablation study (Section 4.4) tests λ, ε, and number of emulator updates, but omits this critical comparison.

### Minor

3. **No standard deviations or confidence intervals reported.** The paper states three random seeds were averaged (line 131), but no variance is reported in any table or figure. Since the claims involve comparing methods, the statistical significance of the reported >4% improvements cannot be assessed. This is fixable but undermines confidence in the results.

4. **Ablation study findings are qualitative only.** Section 4.4 reports findings as unsubstantiated bullet points (e.g., "The regularization term benefits the training of AdapEmu and AdapFu") with no tables, figures, or numerical values to support them. Given that the ablation is the primary evidence for the contribution of individual components, this lack of quantitative support is a significant gap.

5. **No measurement of client-side computation or communication cost.** The paper claims "friendliness for computation-limited clients" (abstract, line 22; Section 3, line 82) and motivates FedBiOT based on resource efficiency, but reports no GPU memory, FLOPs, wall-clock time, or communication volume per round. A simple table of these metrics would substantiate the claim.

6. **0% Pass@1 for baselines with AdapEmu in code generation.** Tables 2 and 3 show baselines achieve 0% Pass@1 with AdapEmu across many settings for a 7B model after 1000 FL rounds. While this could reflect genuine difficulty, it warrants explanation — it suggests the compressed emulator + baseline adapter combination may not produce usable outputs, raising questions about whether baseline hyperparameters were adequately tuned for this setting.

7. **"Bi-level" framing overstates the algorithm.** The paper formulates a bi-level optimization problem (Equations 1-2) and claims the algorithm "can optimize the bi-level problems... to an equilibrium point" (line 107). However, the implemented algorithm is alternating minimization (server updates emulator on public data, then clients update adapter locally) with no implicit differentiation, no gradient through the lower-level solution, and no convergence analysis. This is a reasonable practical heuristic, but framing it as solving a bi-level problem without qualification is imprecise.

### Trivial

8. **Ambiguous phrasing: "bottom few layers."** In Section 3 (line 82), the paper says "choosing the bottom few layers of transformers as the adapter," which could be read as the initial (bottom/early) layers. From Figure 1 and the implementation (line 131: "the last two and the last four decoders"), it is clear this means the *last* layers. The phrasing should be clarified to avoid confusion.

## Nice-to-Haves

- Reporting the divergence (e.g., perplexity gap or embedding cosine distance) between public Alpaca data and the private client datasets would quantitatively support the motivating claim that distribution mismatch exists and is meaningful.
- A sensitivity analysis on the number of emulator updates per round (the paper uses 10 but acknowledges "it is hard to say how many... can bring the best performance," line 185) would strengthen the practical guidance.

## Removed Points

- **"Overall assessment" recommending rejection based on speculation.** The harsh critic's claim that the confound makes the "contribution... not convincingly demonstrated" overstates the issue. The paper demonstrates FedBiOT (as a package) outperforms prior methods; the missing control limits attribution but does not invalidate the results entirely.
- **Strength Finder's claim that "ablation study validates the contribution of the proposed components."** The ablation is qualitative and does not include the key controlled comparison needed to validate the novel contributions. This strength is removed as overclaimed.
- **Strength Finder's claim about "computation and communication efficiency."** No measurements are provided in the paper to support this claimed strength; it reflects the paper's stated goals rather than demonstrated evidence. Removed as unsubstantiated.
- **Criticism about missing appendix content or absent references.** These are parser-stripped sections; they exist in the original submission. Removed per hard rules.
- **Criticism about formatting issues in tables (garbled).** Parser artifact from PDF extraction, not author error. Removed per hard rules.
- **Criticism about missing related works.** The system cannot verify existence of such works. Removed per hard rules.
- **Criticism about "not yet released" systems or unverifiable citations.** All cited works are assumed to exist. Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely react to the paper as written without surfacing new connections or observations not already present in the work itself. The key point worth elevating — that the combination of a different adapter definition with a different optimization scheme creates a confound in the evaluation — is a standard methodological concern rather than a novel discovery.

## Suggestions

1. **Run controlled ablations.** Specifically: (a) compare FedBiOT and FedOT using the *same* adapter definition (either both use last-two-layers, or both use first-two-and-last-two), and (b) compare FedBiOT to a variant where the emulator is fixed after initial distillation (mimicking FedOT) while keeping FedBiOT's adapter and regularization identical. This would directly test whether the alternating alignment provides benefit beyond the adapter choice.
2. **Report standard deviations** for all main results.
3. **Quantify the ablation study.** Provide tables/figures showing accuracy vs. λ, ε, and number of emulator updates, rather than qualitative bullet points.
4. **Add a table of client-side resource costs** (GPU memory, per-round time) and communication volume to substantiate the efficiency claims.
5. **Acknowledge the alternating nature** of the optimization more precisely, and either provide a convergence analysis or reframe as alternating minimization with empirical justification.
