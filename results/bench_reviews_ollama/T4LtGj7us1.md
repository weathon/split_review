Now I have a thorough understanding of the paper. Let me synthesize the final review.

Key points to verify:

1. **"Breaking the scaling law" claim**: The paper uses this phrase prominently—the abstract says "significantly breaks the scaling law," and Section 4.1 is titled "A KEY TO BEAT THE SCALING LAWS." But experiments only compare against random sampling at the same scale. "Breaking a scaling law" in the standard sense means achieving performance that cannot be achieved by the baseline at any scale (i.e., shifting the scaling law curve), not just being better at each specific scale. The paper does show ZooProbe consistently outperforms random sampling across scales, which is useful, but the claim of "breaking" or "beating" scaling laws is overstated compared to what's demonstrated. This is a legitimate concern.

2. **A* search framing**: The paper explicitly frames its method as A* search (Eq. 1, Section 2, Section 3.2). The harsh critic points out it lacks A* properties. The paper uses Q = r + γh, which is indeed A*-like in structure, but the algorithm uses softmax-weighted sampling (Eq. 6) rather than greedy best-first expansion, and there's no admissibility guarantee. The paper says "Motivated by the A* search framework" and "within the A* framework" - so it claims to be A*-based. The algorithm is more accurately a heuristic-guided iterative re-weighting procedure. The A* framing is a stretch but the paper does say "motivated by" A* in some places, so it's not entirely claiming to be A*. Let me check...

Looking at line 33: "Motivated by the A* search framework, we propose a quality function" and line 126: "the data tree is expanded within the A* framework." The claim is somewhat mixed - "motivated by" at one point but "within the A* framework" at another. This is a fair concern but the paper does provide the actual equations and algorithm description, so a reader can see what's actually being done. I'd classify this as a moderate framing issue rather than a fatal flaw.

3. **No comparison against non-trivial data selection baselines**: This is confirmed - Figure 3 only compares ZooProbe vs random sampling. The ablation in Figure 4(b) adds "fixed diverse" and "opposite" strategies. But no comparison against DSIR, DoReMi, DPP-based methods, or quality filtering. This is a genuine and significant gap.

4. **Evolving component unevaluated in isolation**: Confirmed - Section 3.3 describes data generation but there's no ablation isolating its contribution. Section 4 mentions "When a sampling batch exceeds 1,000 but fails to meet the quality standards, we initiate a data generation process" but doesn't quantify what fraction of the final dataset is generated vs. sampled, nor does it ablate the generation component.

5. **Proxy validation for r(d; M)**: The paper substitutes "log expected empirical prediction" for actual fine-tuning quality (line 124) but never validates this substitution. This is a legitimate concern about the selection mechanism.

6. **"Nearly equivalent" to LLaVA-1.5**: The paper claims (line 189-192) that with ~1/3 of LLaVA-1.5's training data, performance on AI2D is "nearly equivalent." However, ZooProbe uses Llama3.1-Instruct as the base LLM, which is significantly stronger than LLaVA-1.5's Vicuna/LLaMA. This confounds the comparison—it's not apples-to-apples.

7. **No error bars or statistical significance**: Confirmed from reading the experimental section—no error bars or significance tests are reported.

Let me now evaluate the Strength Finder's claims:

- "Principled formalization of data expansion as A* search" - This is claimed but as discussed, the A* framing is a stretch. The formalization as Q = r + γh is reasonable regardless of the A* label. The strength should be reframed.

- "Dynamic quality rule exploration conditioned on model state" - This is genuinely supported by Figure 4(b) showing dynamic rules outperform fixed diverse ones. Keep.

- "Comprehensive multi-dimensional data description" - Valid, 50+ dimensions across visual/textual/multimodal models. Keep.

- "Strong empirical evidence of beating scaling laws" - The "beating scaling laws" framing is misleading as discussed. The evidence shows ZooProbe outperforms random sampling, which is valuable but not the same as "beating scaling laws." Needs qualification.

- MLLM-Scorer as efficient replacement - Supported by Figure 4(a). Keep but minor.

- Efficiency analysis - Supported by Figure 5/Table 5. Keep but minor.

- Graceful degradation under partial dimensions - Supported by Figure 4(c). Keep but minor.

Now let me organize the final review.</think>## Summary

ZooProbe proposes an Evaluating-Exploring-Evolving (E3) loop for curating multimodal LLM training data. It uses a small model zoo to produce 50+ dimensional data description vectors, then dynamically discovers quality selection rules via probe-set-based perturbation and softmax-weighted selection, and optionally generates new targeted data to fill distribution gaps. The system is evaluated by fine-tuning LLaVA and Wings on curated datasets of 20k–260k samples, showing consistent gains over random sampling across six benchmarks.

## Strengths

- **Comprehensive, multi-dimensional data description framework:** ZooProbe assembles a model zoo covering 50+ intrinsic and meta dimensions (object counts, depth, topic distributions, annotation quality, scene complexity, etc.) using established models (CLIP, SAM, Depth-Anything-V2, GTE-Qwen2). This is a concrete engineering contribution that goes beyond single-difficulty scorers or perplexity-based filtering.

- **Dynamic quality rule exploration validated against meaningful ablations:** Figure 4(b) shows that the dynamic rule discovered by ZooProbe outperforms both a fixed diverse strategy and an "opposite" rule, providing direct evidence that data quality requirements shift during training and the probe-based mechanism captures this shift. This ablation makes a pointed case for the value of the dynamic component.

- **Practical efficiency and graceful degradation:** The overhead analysis (Figure 5) shows evaluation cost ~1/50 and rule exploration cost ~1/20 of training, and Figure 4(c) demonstrates that even with half or a quarter of evaluation dimensions, ZooProbe still outperforms random sampling—making it viable under resource constraints.

- **Consistent gains over random sampling across scales and architectures:** Figure 3 shows ZooProbe outperforming random sampling across all six benchmarks, two architectures (LLaVA and Wings), and all tested scales (20k–260k), which establishes that the overall pipeline produces real, systematic improvements.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed "breaking/scaling laws" framing lacking the critical comparison:** The paper's central claim—both in the abstract ("significantly breaks the scaling law") and in Section 4.1 ("A KEY TO BEAT THE SCALING LAWS")—is that ZooProbe breaks scaling laws. However, all experiments compare only against **random sampling at the same data scale**. To genuinely claim "breaking" a scaling law, one must show that ZooProbe at scale N achieves performance **unattainable by random sampling at any larger scale within the experimental range** (i.e., that the scaling curve itself shifts). The paper does not present this comparison. What the experiments actually show is that curated data selection outperforms random sampling at each fixed scale—a well-established finding in data curation. This mischaracterization inflates what the experiments support and pervades the paper's framing.

- **No experimental comparison against existing data curation/selection methods:** The paper cites multiple established methods (DoReMi, DoGE, DSIR, quality filtering) but compares exclusively against random sampling. Without showing that ZooProbe outperforms these baselines—or even comparable simple quality filters—the contribution is limited to demonstrating that curation helps, rather than that this particular curation method is preferable. The ablation against "fixed diverse" and "opposite" rules is valuable but does not substitute for comparison with prior published approaches.

- **The evolving (data generation) component is unevaluated in isolation:** Section 3.3 describes data generation triggered when sampling "fails to meet quality standards"—arguably the most novel element of the E3 loop. Yet no ablation isolates the contribution of generated data versus sampling alone. The paper does not report what fraction of the final training set comes from generation versus selection, making it impossible to assess whether the "evolving" step actually helps.

### Minor

- **A* search framing is imprecise:** The paper repeatedly frames its method as A* search (e.g., "within the A* framework," Eq. 1 structured as Q = r + γh), but the actual algorithm uses softmax-weighted sampling over probe-set rewards (Eq. 6), has no admissibility guarantee on h, and does not maintain open/closed lists. The method is a well-motivated heuristic iterative re-weighting procedure; calling it "A* search" misleads readers about its theoretical properties. The paper does say "motivated by" A* in one passage, but "within the A* framework" in another—which sends a mixed signal.

- **The proxy for reward-so-far (log expected empirical prediction) is unvalidated:** Eq. 4 defines r(d; M) using model performance and convergence speed after fine-tuning, which is prohibitively expensive to compute per candidate batch. The paper substitutes a proxy (Nguyen et al., 2020) but provides no empirical validation that this proxy correlates with actual fine-tuning quality. If the proxy is a poor approximation, the entire selection mechanism's effectiveness would be compromised.

- **Apples-to-oranges comparison with LLaVA-1.5:** The paper claims "nearly equivalent" AI2D performance with "one-third of the data" vs. LLaVA-1.5 (line 189–192), but ZooProbe uses the much stronger Llama3.1-Instruct base LLM rather than LLaVA-1.5's Vicuna. This confounds data quality with base model capability, making the comparison misleading as evidence for data curation effectiveness.

- **No error bars or statistical significance reported:** All experimental results are presented as single-run figures without uncertainty quantification, which limits confidence in the magnitude of reported gains.

### Trivial
None.

## Nice-to-Haves

- Analysis of which specific evaluation dimensions (or dimension groups) drive quality improvements, rather than only showing that random halves/quarters of dimensions still work.
- Visualization of how the discovered quality rules (π*) evolve across training iterations, which would substantiate the "dynamic" claim.
- Examples of generated data from the evolving component alongside the macro task prompts used, to provide qualitative evidence for the generation mechanism's value.
- Scaling experiments beyond 260k to test whether gains persist at modern MLLM training scales (1M+).

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Claim that experiments are not "large-scale":** The harsh critic notes experiments only go up to 260k. While smaller than some contemporary MLLM training runs, 260k is a reasonable scale for an ablation-focused study. This is a nice-to-have suggestion, not a weakness.

- **Notation issues with δπ:** The critic flags inconsistent use of δπ across sections. Upon review, δπ refers to the concatenated description vector consistently—it appears in Section 3.1 (Eq. 2–3 context) and Section 3.2, and is defined in the equations. Any confusion is a minor presentation issue, not a substantive problem.

- **Claim that the perturbation scheme for h is under-specified:** The paper states it conducts r random perturbations of the uniform distribution U (Section 3.2). While more detail on the perturbation mechanism would be helpful, the high-level description is sufficient for understanding the algorithm; this falls under reproducibility details rather than a fundamental gap.

- **Strength Finder claim that "breaking scaling laws" is a strength:** This is a mischaracterization—the evidence shows improvement over random sampling, not a genuine shift in scaling behavior. Removed as a strength and elevated to a major weakness above.

- **Strength Finder claim about "principled formalization as A* search":** Downgraded because the A* framing is imprecise (see Minor weakness). The formalization Q = r + γh is a reasonable decomposition regardless of the A* label, but calling it A* search is misleading.

- **Demands for comparison with specific unreleased baselines:** Removed per hard rules—cited methods (DoReMi, DSIR, etc.) are treated as existing. The legitimate concern is their absence from experiments, not their existence.

## Novel Insights

The most insightful finding from the reviews is the tension between what ZooProbe actually demonstrates and what it claims. The system's genuine contribution is a well-engineered, multi-dimensional, dynamically adaptive data curation pipeline that consistently outperforms random sampling. The dynamic rule exploration (validated in Figure 4b) showing that "opposite" rules degrade performance while fixed diverse rules underperform adaptive ones is a concrete and useful finding. However, the paper's repeated claim to "break scaling laws" conflates "data curation beats random sampling at the same scale" with "data curation shifts the performance-vs-scale curve"—a fundamentally different (and unproven) proposition. The gap matters because the former is well-established, while the latter would be genuinely novel if demonstrated with proper comparisons against both larger-scale random data and existing curation methods.

## Suggestions

- Retitle Section 4.1 and revise the abstract/conclusion to accurately reflect the finding: ZooProbe improves data efficiency versus random sampling, not that it "breaks" scaling laws. At minimum, add a comparison showing ZooProbe at scale N vs. random sampling at the smallest scale where random matches ZooProbe's performance—that would substantiate a "data efficiency" claim rather than a scaling-law claim.
- Add at least 2–3 comparisons against established data selection baselines (DoReMi, DSIR, or simple quality filtering) to show that ZooProbe's specific pipeline adds value beyond what already exists.
- Run an ablation that disables the evolving/generation component (sampling only) and report the performance gap, as well as the fraction of the final training set that comes from generation vs. selection.

## Score and Decision

The paper makes a genuine engineering contribution—a multi-dimensional, dynamically adaptive data curation pipeline with consistent empirical improvements over random sampling. However, the "breaking scaling laws" claim significantly overstates what the experiments establish, the absence of comparisons against any non-trivial data selection baselines leaves the incremental value over prior art unverified, and the most novel component (data evolution) is unabluted. These are substantive issues that weaken confidence in the paper's central claims.

**Originality:** Moderate. The components (model zoo evaluation, KL-based diversity, probe-set selection) draw from known ideas, but the specific E3 loop integration is novel. The A* framing adds rhetorical rather than technical value.

**Importance of research question:** High. Data curation for MLLMs is a timely and important problem.

**Claims supported by experiments:** Partially. ZooProbe beats random sampling, but the stronger claims (breaking scaling laws, superiority over existing curation methods) are not supported.

**Soundness of experiments:** Moderate. Adequate scales, multiple benchmarks, two architectures, and good ablations—but missing critical baselines and ablution of the generation component.

**Clarity:** Moderate. The A* framing obscures rather than clarifies; the evolving component is under-specified; the paper is dense but mostly readable.

**Value to community:** Moderate. The model zoo and dynamic rule exploration ideas could be useful, but without baseline comparisons, it is hard to know whether they outperform simpler alternatives.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>