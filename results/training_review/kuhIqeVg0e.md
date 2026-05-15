Now I have a thorough understanding of the paper and can verify the reviewer claims directly. Let me write the consolidated review.

---

## Summary

This paper presents ChemAgent, a framework that augments LLMs with a structured library of three memory types (planning, execution, knowledge) for chemical reasoning. The library is initially constructed from a development set by decomposing problems into atomic sub-tasks with solutions, then used during inference via retrieval-augmented generation. The paper reports strong accuracy gains over direct reasoning (up to 46% on CHEMMC) and over the prior state-of-the-art StructChem (9.5% average), across four SciBench chemistry datasets and three LLM backbones.

## Strengths

- **Consistent and substantial accuracy improvements across diverse settings**: ChemAgent outperforms StructChem by an average of 9.50% absolute and up to 15% on individual datasets, and achieves up to 46% improvement over direct reasoning (Table 1). These gains hold across four chemistry datasets and three LLM backbones (GPT-3.5, GPT-4, Llama3), demonstrating that the overall framework reliably enhances chemical reasoning.

- **Well-motivated three-memory architecture with ablation support**: The decomposition into planning memory (high-level strategies), execution memory (specific sub-task solutions), and knowledge memory (fundamental principles) is conceptually grounded. The ablation study (Table 2) confirms that removing any component degrades performance, and the memory quality analysis (Table 3) shows a meaningful 8% gap between GPT-4-generated and GPT-3.5-generated memory, validating the design choices empirically.

- **Honest error analysis identifying a nuanced retrieval limitation**: Section 3.5 provides a concrete failure case where retrieved memory is semantically similar but critically different (adiabatic vs. isothermal), a genuinely insightful observation about the limits of embedding-based retrieval for domain-specific reasoning. The paper acknowledges this limitation rather than glossing over it.

- **Multi-model and cost analysis**: The framework is evaluated on three LLM backbones showing consistent trends, and the cost analysis (Section 3.4, ~$0.09–$0.17 per example) provides practical transparency about deployment viability.

## Weaknesses

### Fatal

None. The paper's core results are real and reproducible in principle; the weaknesses lie in framing and experimental design rather than methodological invalidation.

### Major

- **Mismatch between headline contribution ("self-updating memories") and primary evidence**: The title, abstract, and introduction frame dynamic self-updating as the central contribution. However, the main experimental results (Table 1) evaluate a static library constructed once from the development set — the "memory" toggle in Table 1 refers to enabling/disabling this static library (Section 2.4), not to runtime self-updating. The only experiment that tests dynamic updating is Section 3.3, which is (a) restricted to a single dataset (MATTER), (b) removes the evaluation & refinement module for simplification, making it not directly comparable to the full method, and (c) converges to performance that does not clearly exceed the static library's results on that dataset. The paper's framing implies that self-updating drives the reported gains, but the evidence does not support this — the large improvements come from the overall architecture (structured memory + decomposition + evaluation & refinement), not specifically from dynamic updates. This is a consequential framing error that would require either reframing the contribution or providing evidence of self-updating's benefits across all datasets.

- **Missing critical baseline: retrieval-augmented generation (RAG) with full problem–solution pairs**: The baselines include direct reasoning (zero-shot), few-shot+Python with *fixed* examples, and StructChem. There is no comparison against a method that retrieves complete problem–solution pairs from the same development set based on embedding similarity and conditions the LLM with them. Since the "memory" in ChemAgent retrieves decomposed sub-task units rather than whole problems, the observed gains over StructChem cannot be attributed to the structured decomposition vs. simple retrieval of full examples. This gap prevents isolating the contribution of the sub-task decomposition and three-memory design from the well-known benefit of having relevant examples at inference time. A RAG baseline retrieving full pairs is the minimum needed to establish that the structured, decomposed memory adds value beyond standard retrieval.

- **Core hyperparameter unspecified**: The similarity threshold \(\theta\) for retrieving memory units (Equation in Section 2.5) is defined but never given a value. Since retrieval quality depends critically on this threshold, and the paper makes claims about memory quality and selection, omitting \(\theta\) impairs reproducibility and makes it impossible to assess whether the retrieval mechanism is well-calibrated or trivially tuned.

### Minor

- **Inconsistency in headline numbers**: The abstract reports "performance gains of up to 46% (GPT-4)," and the results section (line 161) confirms "46% increase (28.21 vs. 74.36)." However, the conclusion states "achieving up to a 36% improvement." This inconsistency — likely a copy-editing error — is confusing and undermines the paper's polish.

- **Ablation substitutes human-written examples when removing \(\mathcal{M}_e\)**: In Section 4.1, when removing execution memory, the paper replaces it with "two fixed human-written few-shot examples." These human-written examples may be of higher quality than the automatically generated memory units, potentially masking the true impact of removing \(\mathcal{M}_e\). A cleaner ablation would remove \(\mathcal{M}_e\) without substitution or substitute with randomly selected sub-tasks.

- **Self-evolution experiment not directly comparable to main results**: The dynamic updating experiment (Section 3.3) removes the evaluation & refinement module, uses a different evaluation protocol (iteration-based with target-leakage prevention), and is only run on MATTER. It is not a controlled comparison against the static-library version of ChemAgent with the same setup, so the claim that "self-evolution improves performance" is not rigorously benchmarked against the alternative (just using the static library).

- **Cost analysis lacks baseline comparison**: The token cost analysis (Section 3.4) reports absolute costs but does not compare token consumption of baselines (e.g., StructChem, few-shot+Python). Without this context, the reader cannot assess the cost-performance trade-off relative to alternatives.

### Trivial

- Typo on line 150: "accucacy" → "accuracy".

## Nice-to-Haves

- Running the self-evolution experiment on all four datasets (not just MATTER) with a controlled comparison against the static library version (with the same modules enabled/disabled) would substantially strengthen the self-updating claim.
- A failure analysis quantifying how often high-similarity retrieval is misleading (beyond the one qualitative example in Figure 7) would add depth.
- Testing on an unseen chemistry benchmark (not from SciBench) would address potential dataset-specific fitting concerns.

## Removed Points

- **"Evaluation metric not defined / Section 4.3 missing"**: The paper defines the metric as "relative tolerance of 0.01" (line 150). The reference to "Section 4.3" is likely an appendix section stripped by the parser. Per instructions, criticisms about missing appendix content are removed.
- **"Algorithm 1 referenced but missing"**: Likely in the appendix. Removed per hard rule about parser-stripped content.
- **"46% is ambiguous (absolute vs. relative)"**: The paper provides actual numbers (28.21 vs. 74.36), making the meaning clear. This is standard practice for reporting percentage-point improvements in this literature. Removed as not a genuine weakness.
- **"Method for self-created chemistry problems described in one sentence"**: The paper describes the approach (lines 106-108) at an appropriate level for a framework paper; this is a presentation preference, not a flaw.
- **"Confidence threshold for discarding memory units not specified"**: This is a minor implementation detail; per hard rules, such hyperparameter nitpicks are removed unless core to the contribution.

## Novel Insights

The most interesting observation emerging from the reviews — beyond the paper's own contributions — is the tension between the paper's self-updating framing and its experimental design. The self-updating claim requires evidence that the *process of updating* (not just the *content of the library*) causes improvement over time. The paper's attempt at this (Section 3.3) is too weak to carry the weight the framing places on it, while the main results are better interpreted as evidence for a well-designed structured retrieval system. This suggests a broader lesson for the field: papers should be cautious about claiming "learning" or "self-improvement" when the gains could equally come from a carefully constructed static retrieval index.

## Suggestions

1. **Reframe the contribution** to honestly reflect what is demonstrated: a structured memory-augmented reasoning framework with a static library (initially constructed from a dev set) and an evaluation & refinement module. The self-updating can be presented as an additional finding with appropriate caveats about its limited evaluation, or it needs to be demonstrated convincingly across all datasets with proper controls.
2. **Add a RAG baseline** that retrieves full problem–solution pairs from the development set using the same embedding similarity (Llama3) and feeds them as few-shot examples. This is the minimal control needed to isolate the benefit of the structured, decomposed memory design.
3. **Report the similarity threshold \(\theta\)** and any other hyperparameters that affect retrieval quality.
4. **Fix the inconsistency** between the abstract's "46%" and the conclusion's "36%."
5. **Run the self-evolution experiment** with the evaluation & refinement module included, and compare against the static-library baseline under the same conditions.

## Score and Decision

The paper presents a genuinely useful framework with strong empirical results, and the three-memory architecture is well-motivated. However, the fundamental mismatch between the **self-updating framing** and the **static-library evidence** is a substantial issue that cannot be dismissed. The missing RAG baseline further weakens the ability to assess what the structured decomposition specifically contributes. These problems are addressable with major revision, but in the current form the paper's claims outrun its evidence.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>