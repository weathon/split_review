Now I have a thorough understanding of both the paper and the reviews. Let me produce the final consolidated review.

## Summary

This paper proposes ResearchTown, a multi-agent LLM framework that models a research community as an "agent-data graph" where researchers are agent nodes (with LLM functions) and papers are data nodes (with text attributes). The authors introduce TextGNN, a text-based message-passing formalism that casts paper reading, writing, and review writing as inference layers on this graph. For evaluation, they present ResearchBench, a benchmark of 2,737 paper-writing and 1,452 review-writing tasks using masked node prediction, where a paper's content is predicted from its authors and references. The main findings are that ResearchTown can reconstruct papers with similarity scores around 0.66, that simulating only first+last authors outperforms using all authors (mirroring real-world contribution patterns), and that it can generate interdisciplinary paper ideas.

## Strengths

- **Novel graph abstraction (agent-data graph) that formally distinguishes agent and data nodes with distinct semantics.** The paper defines a heterogeneous graph where agent nodes carry functions (LLMs with profile prompts) and data nodes carry text attributes, enabling a unified representation of both agents and artifacts. This goes beyond prior multi-agent frameworks that treat data only as external context, and it directly structures the simulation of research activities as message-passing processes (Sections 3-5).

- **TextGNN provides a principled formalism for unifying diverse research activities under a common inference structure.** The paper adapts standard GNN aggregation equations to operate entirely in text space, and instantiates them for paper reading (Eq. 5), paper writing (Eq. 6), and review writing (Eq. 7) as distinct TextGNN layers. This provides a mathematically grounded way to describe the research lifecycle, which prior works (single-agent idea generation, isolated paper writing) lack.

- **The ablative finding that simulating only first+last authors outperforms using all authors is an empirically interesting insight.** Table 2 shows that using the first and last author yields higher similarity (64.8/66.0) than using all authors (64.7/65.5), which aligns with real-world observations about unequal author contributions. This result would be genuinely informative if it were statistically reliable.

## Weaknesses

### Major

- **Incomplete experiments undermine the quantitative claims.** The paper announces ResearchBench as a 2,737-paper benchmark but runs experiments on only 100 papers (3.7%). Worse, it describes a review-writing evaluation methodology (1,452 tasks) and then reports zero review-writing results. The paper's own caveat — "Due to limited time and cost budget, a more comprehensive result on RESEARCHBENCH will be available in the later version" (line 161) — is an explicit acknowledgment of incompleteness. For a paper whose main evidence is quantitative, this is a severe limitation: the reader cannot assess whether the reported patterns hold at scale or are artifacts of a small, potentially biased sample.

- **No uncertainty quantification on any reported number.** Every score in Tables 1 and 2 is reported as a point estimate without standard deviations, confidence intervals, or significance tests. The differences between conditions are small (e.g., 0.648 vs. 0.616 at k=1; 0.647 vs. 0.648 in the ablation). Without error bars, the reader cannot distinguish signal from noise. This is particularly problematic in the ablation study (Table 2), where the paper draws a substantive conclusion about author contributions from differences of 0.1–0.5 points.

- **The experimental "community" is a single-paper local neighborhood, not a community.** Each evaluation constructs a graph from only one target paper's authors and its references. There are no non-author researchers, no other papers from those authors, and no broader citation network. This reduces the task to a constrained generation problem (predict a paper given its known authors and references) rather than a simulation of genuine community dynamics (e.g., how researchers from different subfields combine expertise to produce new ideas). The paper's framing — "simulating research communities," "understanding the process behind research idea generation" (line 10) — implies capabilities that this setup does not test.

### Minor

- **The "TextGNN" framing overclaims relative to the actual implementation.** The formal equations (3–7) present a message-passing framework, but the practical implementation reduces to prompting an LLM with concatenated text from neighboring nodes. There are no learned message functions, no trainable aggregation, and no backpropagation. The "graph" does two fixed layers (reading → writing/reviewing). The paper would be better received if it presented the work as a structured prompt-engineering framework inspired by GNNs, rather than claiming a new class of graph neural network, which invites expectations about expressivity and theoretical guarantees that are not met.

- **The claim of "objective" evaluation is overstated.** The paper states that masked node prediction is "scalable and objective" and "does not rely on high-quality human annotations" (line 21). However, the evaluation still requires (a) an LLM-based 5-question summarization prompt, (b) an LLM-based bullet-point extraction prompt for reviews, (c) a chosen embedding model (text-embedding-3-large or voyage-3), and (d) a weighted combination of similarity scores. Each of these is a human design choice that introduces subjectivity and potential bias. The metric is more reproducible than human evaluation, but it is not truly objective.

- **The tension between reconstruction and generation is acknowledged but not resolved.** The quantitative evaluation rewards similarity to ground truth, while Section 10 celebrates divergence ("RESEARCHTOWN can discover valuable ideas that differ from the ground truth"). If the goal is simulation fidelity, divergence is a bug; if the goal is novel idea generation, the similarity metric is the wrong measure. The paper does not clarify which standard applies when, or how to reconcile the two.

- **Profile initialization and prompt templates are underspecified for reproducibility.** The paper describes researcher profiles as being formed by aggregating authored papers via an LLM (Eq. 5), but provides no details on the prompt structure, how many papers are used per researcher, or whether the profile is constructed per-target-paper or globally. This is the core mechanism for injecting expertise into the simulation, and the current level of detail makes reproduction difficult.

### Trivial

- Ethical concerns (research fabrication, plagiarism) are mentioned in the introduction but not revisited in the discussion or conclusion.

## Nice-to-Haves

- A human evaluation study (even small-scale) would help calibrate what a similarity score of 0.66 actually means in terms of paper quality, coherence, and novelty. However, the paper's goal of an automated, scalable evaluation is a defensible design choice, so its absence is not a flaw.
- Releasing code, prompts, and agent profile templates would improve reproducibility and community adoption, but this is not a requirement for evaluation.
- A deeper qualitative comparison with AI Scientist on axes like novelty, coherence, and soundness would help position the contribution.

## Removed Points

These points were flagged by reviewers but are removed for the following reasons:

- **"Section 2 (related work) is missing from the provided text."** — This is a parser artifact. The original submission contains a related work section; the PDF extractor stripped it. Not a valid criticism.
- **"No human evaluation is reported."** — The paper intentionally proposes an automated evaluation paradigm as an alternative to costly human evaluation. Whether this is sufficient is a design judgment, not a factual gap. Moved to Nice-to-Haves.
- **"The paper should release code and prompts."** — A suggestion for future work, not a weakness of the current submission. Moved to Nice-to-Haves.
- **"The comparison to AI Scientist is not detailed."** — The paper uses AI Scientist as one of four baselines with adapted prompts. This is an adequate baseline comparison for a paper focused on introducing a new framework.
- **"The ethical concerns mentioned are not revisited."** — A single-sentence acknowledgment of ethical concerns followed by a brief discussion would be nice, but this is a trivial omission.

## Novel Insights

None beyond the paper's own contributions. The reviews largely react to what the paper claims rather than offering new perspectives that the authors missed.

## Suggestions

1. **Complete the experiments.** Run the full 2,737-paper benchmark or (if truly infeasible) reduce the scope of ResearchBench to a size that can be fully executed, and clearly state the reduced scope upfront. Report review-writing results if the evaluation methodology is described.
2. **Add uncertainty estimates.** Report standard deviations over multiple runs, or at minimum bootstrap the similarity scores over the test set. Without this, small differences between methods are uninterpretable.
3. **Run a genuine community-level experiment.** Select a set of researchers from different subfields and ask them to generate a paper idea not already in the training set. This would directly test the interdisciplinary synthesis the paper claims as a key finding.
4. **Tone down the GNN framing.** Rename "TextGNN" to something like "structured text-based message passing" or acknowledge explicitly that this is a prompt pipeline inspired by GNNs, not a trainable neural network.
5. **Acknowledge the evaluation tension directly.** State clearly that similarity to ground truth measures whether the simulation captures known collaboration patterns, while qualitative assessment measures novelty. These are complementary, not competing, but the paper should make this explicit.
6. **Provide prompt templates** for researcher profile construction and paper generation in an appendix or supplementary material.

## Score and Decision

The paper introduces an interesting conceptual framework (agent-data graphs, TextGNN formalism) and a thoughtfully designed benchmark. However, the experimental validation is severely incomplete: only 3.7% of the claimed benchmark is evaluated, review-writing results are entirely absent, no uncertainty quantification is provided for any reported number, and the experimental "community" is a single-paper local neighborhood that does not test the community-level dynamics the paper promises. The core ideas have merit, but the paper in its current form does not present sufficient evidence to support its claims. A resubmission with complete experiments and proper statistical reporting could be competitive.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>