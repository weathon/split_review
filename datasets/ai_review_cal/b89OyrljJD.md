- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces an LLM-powered framework for multi-step retrosynthesis that generates a complete route in a single pass using molecular-similarity-based retrieval-augmented generation (RAG), then iteratively refines it via expert model feedback (MolecularTransformer, LocalRetro, etc.). The framework is evaluated with GPT-4-turbo, Claude-3.5-haiku, and Deepseek-V2.5 on a subset of the retro* dataset, achieving 79.5% route validity (GPT-4) compared to 83.0% for the Retro* baseline, and provides useful analyses of LLM cheating behaviors, the importance of RAG quality, and design trade-offs between domain knowledge and general instruction-following.

## Strengths

1. **Demonstrated value of molecular-similarity-based RAG**: The ablation (Table 2) shows that replacing representative routes with RAG from similar molecules improves initial reaction round-trip validity from 24.42% to 51.64% — a clean, well-controlled comparison that directly supports the paper's central design choice.

2. **Iterative refinement is shown to drive substantial improvements**: Table 3 reports reaction-level top-5 round-trip validity rising from 51.64% (first iteration) to 89.81% (final iteration) for GPT-4-turbo, and Figure 4b shows that many valid routes emerge only after multiple refinement rounds, not just from the initial generation.

3. **Competitive overall route validity with traditional planners**: The GPT-4-turbo variant achieves 79.5% route validity versus Retro* at 83.0% (Table 1), and the paper further demonstrates (Section A.6) that the framework discovers valid routes Retro* cannot find. This supports the claim that LLM-driven holistic route generation is a viable direction.

4. **Practical insights from cross-model analysis**: The separation of Deepseek (generator) + GPT-4-turbo (formatter) in Table 4, with molecule validity rising from 86.76% to 93.45%, provides a concrete actionable finding about balancing domain knowledge (Deepseek's stronger initial chemistry output) against general instruction-following ability. The documentation of LLM "cheating" behaviors (Figure 5) is also informative for future system design.

5. **Comprehensive multi-metric evaluation**: The paper reports not just route validity but also ROUGE, BLEU, exact match, molecular validity, and route length, giving a rounded picture of what the framework does well and where it falls short (e.g., longer average route length than Retro*).

## Weaknesses

### Fatal

None.

### Major

- **Overlap between feedback models and evaluation models creates an interpretability concern for the refinement improvement.** The expert models used for feedback (MolecularTransformer, LocalTransform, LocalRetro, MLP, lines 133–137) are the same *categories* of models (template-free forward predictors, template-based retrosynthesis predictors) as those used in the round-trip validity evaluation ensemble ("an ensemble approach combining database, template-free, and template-based models," line 157). The paper does not specify whether the same model *instances/checkpoints* are used for both roles, nor does it discuss the potential circularity. The improvement from 51.64% to 89.81% reaction-level RT validity through iterative refinement could partly reflect the LLM learning to satisfy the same models that evaluate it, rather than reflecting genuinely more feasible chemistry. This concern is partially mitigated by: (a) the RT validity metric includes a database look-up (reactions from all splits), which is an independent signal; (b) the paper acknowledges that RT validation "remains flawed without experimental verification" (line 157); and (c) the comparison to Retro* uses the same metric. However, the paper would be substantially strengthened by explicitly naming the evaluation models and, ideally, validating a subset against an independent source (e.g., human expert review, or a held-out reaction database not used in training any of the feedback models).

- **The comparison to traditional planners is not controlled for the expert models used.** The Retro* and EG-MCTS baselines employ their own single-step retrosynthesis models (different from those in the proposed framework). Since the proposed framework's route validity heavily depends on the quality of the expert models (MolecularTransformer, LocalRetro, etc.) for feedback, it is unclear how much of the 79.5% vs. 83.0% comparison reflects the LLM framework versus the underlying expert models. A controlled ablation — running Retro* using the *same* forward/retrosynthesis models as the proposed framework — would cleanly isolate the LLM's contribution.

### Minor

- **The LLM's contribution to the final result is not fully isolated via ablation.** While the paper reports initial-generation reaction validity (51.64%, Table 3) and the final refined result (89.81%), there is no explicit condition showing what the pipeline produces *without* the expert feedback loop beyond the initial generation. The data to infer this exists (first iteration results), but a direct comparison of final route validity with vs. without feedback would strengthen attribution of success to the LLM versus the expert models.

- **The fine-tuning baseline (ChemDFM-8B) is confounded by model scale.** Comparing an 8B fine-tuned model directly to GPT-4-turbo (orders of magnitude larger) to conclude that "fine-tuned LLMs fail to generate as many valid retrosynthesis routes" conflates scale with approach. A controlled comparison fine-tuning a similarly sized base model (e.g., LLaMA-8B) within the same RAG+feedback framework would provide a cleaner test of fine-tuning versus in-context learning.

- **The "slightly harder subset" of retro* is not described in the main text** (only referenced as Table A1 in the appendix, which is stripped by the parser). While this is partially an artifact of the PDF extraction, the main paper is self-contained enough for evaluation; still, the size and selection criteria would help readers assess the generality of results. This is a minor presentation issue.

### Trivial

- The retrosynthesis tree format described in Figure 3d (JSON) would benefit from a concrete inline example in the main text rather than only in the figure.
- Table 2 (RAG ablation) reports only the initial generation; labeling it more explicitly as "initial generation (iteration 0)" would avoid any confusion with the final results in Table 1.

## Nice-to-Haves

- **External validation**: Validating a representative subset of generated routes against a reaction database not used by any component, or via human expert review, would directly address the circularity concern and significantly strengthen the absolute claims.
- **Computational cost analysis**: The framework requires multiple LLM API calls and expert model inferences per iteration. Reporting cost (dollars per route) and wall-clock time versus traditional planners (which are cheaper) would contextualize the practical trade-offs.
- **Failure mode analysis of expert models**: The paper notes that expert models "often fail to cope with out-of-distribution datasets" (citing Yu et al., 2024b, line 139–140) but does not analyze whether the refinement loop ever goes astray due to incorrect expert feedback.

## Removed Points

These points were surfaced by reviewers but are not included as weaknesses in the main review, for the reasons given:

- **"No error bars or statistical significance"**: The paper sets LLM sampling temperature to 0 during route generation (line 243), making the main pipeline deterministic. Error bars are not applicable for a deterministic procedure.
- **"Ground Truth row not explained"**: The "Ground Truth" row in Table 1 is self-explanatory as the reference route metric values.
- **"Average route length not discussed as a limitation"**: The paper explicitly discusses longer routes at lines 174–175: "Retro* consistently produces shorter routes, with an average valid route length of 2.58, compared to the longer average of 3.30 steps."
- **"Reproducibility: model checkpoints not specified"**: The reproducibility statement (line 242) states weights are from official repositories, which is standard practice.
- **Missing related work**: Cannot be verified externally.
- **Formatting/style nitpicks and parser-artifact complaints**: Stripped as parser issues, not author errors.
- **"Dataset statistics should be in main text"**: Referenced to Table A1 in the appendix (stripped by parser). This is an extraction artifact.
- **"Feedback mechanism details only in appendix"**: Table A2 referenced for rule-based integration is in the appendix (stripped). The main text still provides a clear high-level description of the feedback process.

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced no genuinely novel observation that the paper itself does not already articulate.

## Suggestions

1. **Explicitly name the evaluation models for RT validity** in the main text, and confirm whether they are the same checkpoints used for feedback. If they differ, state this clearly; if they overlap, discuss the circularity and consider adding an independent evaluation component (e.g., human expert review of a held-out subset).
2. **Add an ablation comparing final route validity with and without the expert feedback loop** — i.e., report what the "LLM + RAG + formatter" pipeline achieves as its final output without accessing the expert models. This would isolate the LLM's direct planning contribution.
3. **Run Retro* with the same single-step models** used by the proposed framework's feedback module, and report the resulting route validity. This would control for expert model quality and clarify whether the LLM framework adds value beyond what those models can already provide to a traditional planner.
4. **Replace or supplement the ChemDFM baseline** with a fine-tuned model of comparable scale to the tested LLMs (e.g., LLaMA-8B or Deepseek-7B), evaluated within the same RAG+feedback framework, to make the fine-tuning comparison fair.
5. **Describe the "slightly harder subset"** (size, selection criteria) in the main text so readers can assess result generality without consulting the appendix.
