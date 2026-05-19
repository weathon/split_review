- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 6, 6, 5
Here is my consolidated review.

---

## Summary

This paper introduces SEPIT (Structure-Enhanced Protein Instruction Tuning), a framework that integrates a structure-aware protein encoder with a large language model via a two-stage instruction tuning pipeline. The structure-aware module (Gaussian basis kernel → attention bias + positional encoding) is plugged into a pre-trained pLM to enable it to perceive 3D structural information. A linear projector connects the encoder to the LLM, and MoE modules (initialized by upcycling from Stage 1 FFNs) replace the LLM's feed-forward layers. The authors also construct a protein instruction dataset of ~10M instructions covering 12 property/function types from Swiss-Prot. Results show SEPIT-Llama outperforming baselines (GPT-4, Claude-3, InstructProtein, BioT5+, PIT) across BLEU, ROUGE, METEOR, BERTScore, and Accuracy on both open-ended generation and closed-set answer tasks.

## Strengths

- **Structure-aware module demonstrably improves performance and generalizes to sequence-only inputs.** The ablation study (Table 2) confirms that removing the structure-aware module degrades performance on both task types. More notably, Table 4 shows SEPIT using only sequence input outperforms the sequence-only PIT baseline, confirming structural knowledge learned during training transfers to proteins without available structures — a practically important property.

- **Largest and most comprehensive protein instruction dataset to date.** The dataset comprises over 10 million instructions covering 12 property/function categories from Swiss-Prot (plus ~5M supplementary from TrEMBL). Section 3 explicitly compares scope against prior datasets (ProtST, Mol-Instructions, InstructProtein, ProteinChat), showing advantages in instruction diversity, volume, and structural information. The honest reporting of the negative result with TrEMBL data (adding it hurts performance) strengthens credibility.

- **MoE achieves strong performance without increasing activated parameters.** The upcycling-based MoE design (Stage 2) enables SEPIT-TinyLlama-MoEs to match SEPIT-Llama's performance with only 1/6 of the activated parameters (Table 1). Figure 3 provides the interesting, non-obvious finding that protein and text tokens follow different expert pathways — unlike vision-language MoEs where image and text tokens follow near-identical routes — validating the choice to use complete protein representation sequences rather than compressed tokens.

- **Comprehensive evaluation across diverse metrics and task types.** The paper reports five metrics (BLEU, ROUGE, METEOR, BERTScore with PubMedBERT, Accuracy) spanning both open-ended generation and closed-set answer tasks. The comparison set includes strong baselines: closed-source general LLMs (GPT-4, Claude-3, GPT-3.5), open-source biomedical LLMs (Galactica, BioMedGPT), protein-specific models (InstructProtein, BioT5+, Mol-Instructions), and instruction-tuned LLMs with protein sequence input (TinyLlama-Chat, Llama2-Chat, OpenLlama-v2, PIT).

## Weaknesses

### Major

- **The full SEPIT model is evaluated exclusively on the authors' own test set.** The paper states (Sec. 5.2, line 202): "We evaluate the capability of SEPIT for general-purpose protein understanding on the test set of the protein instruction dataset we proposed." While the Stage 0 encoder is validated on external EC/GO benchmarks (Table on F_max), the complete SEPIT model (with LLM) is never tested on independently established protein property prediction tasks. The claim of "general-purpose protein understanding" is thus supported primarily by in-distribution evaluation. All baselines face the same test set, so the relative comparisons are fair, but the absolute claim about general-purpose capability would be strengthened by at least one external evaluation.

### Minor

- **The "w/o Stage 0" ablation is unavailable, and the replacement evidence is indirect.** The paper honestly acknowledges (line 215) that removing Stage 0 warm-up causes FP16 gradient overflow, preventing a direct comparison. The authors supplement with EC/GO encoder validation, which is reasonable but only evaluates the encoder in isolation, not the full instruction-tuned model. This does not invalidate the core claims (the remaining ablations clearly support the other design choices), but the Stage 0 evidence is weaker than it could be.

- **Results are reported from single runs without error bars or standard deviations.** No multiple seeds are mentioned. Given the stochasticity of instruction tuning and MoE routing, confidence intervals would help assess whether reported performance differences (especially between SEPIT variants and baselines) are statistically significant.

- **No dedicated limitations discussion.** The paper omits a limitations section. A brief paragraph on the reliance on AlphaFold-predicted structures (which may be less reliable for some proteins), potential biases from ChatGPT-designed templates, and the computational cost of the three-stage pipeline would be appropriate for a paper making strong claims about general-purpose understanding.

### Trivial

- None.

## Nice-to-Haves

- **External evaluation of the full SEPIT model.** The single most impactful addition would be to evaluate the instruction-tuned model on 2–3 well-established protein property prediction benchmarks (e.g., EC number prediction, GO term prediction, subcellular localization) using the model's generation format. This would directly substantiate the "general-purpose" claim beyond the in-distribution test set.
- **Human evaluation of open-ended outputs.** Given the known weaknesses of BLEU/ROUGE for scientific text, a small human evaluation (e.g., 50 samples judged for correctness and fluency) would strengthen the open-ended generation results beyond the two case studies shown.
- **More dataset statistics.** Reporting the number of unique protein sequences covered, distinct question templates, and distribution across the 12 property types would make the dataset contribution more concretely reproducible.

## Removed Points

These points are flagged to be removed; they are kept here for reference but should be treated with caution:

- **"Missing hyperparameter details (learning rates, batch sizes, GPU hours)"** — Removed per hard rule: criticisms about undisclosed hyperparameters and training budget details (e.g., learning rates, batch sizes, GPU hours) are classified as nitpicks about reproducibility and should be removed. While this information would be helpful, the rule explicitly identifies such criticisms as removals.
- **"Missing noise scaling factor α and β values"** — Removed per hard rule: these are hyperparameter values that fall under the same reproducibility-nitpick classification.
- **"Text encoder architecture not specified (which BERT variant?)"** — Removed per hard rule: trivial implementation detail.
- **"Typo: 'noval' should be 'novel'"** — Removed per hard rule: the rule states to remove criticisms about typos/spelling as parser errors, not author errors.
- **"Dataset may contain many templates/duplicates"** — Removed as speculative. The paper provides counts (10M+ instructions, 5.47M core + 5.25M supplement) and the construction methodology is clearly described; there is no evidence of problematic duplication.
- **"Missing related works (ProLLaMA, ProteinChat)"** — Removed per hard rule: do not mention missing related works as you cannot confirm their existence or relevance from external knowledge.
- **"Requesting human evaluation"** — Moved to Nice-to-Haves as a suggestion, not a weakness.
- **Strengths removed:** Generic/superficial strengths about "addressing an important problem" and "comprehensive evaluation confirms general-purpose capability" were removed because the in-distribution evaluation limitation partially conflicts with the latter claim and the former is generic. The concrete, evidence-backed strengths are retained in the main section.

## Novel Insights

The most novel insight emerging from the reviews — beyond the paper's own contributions — is the observation that in SEPIT's MoE, protein tokens and text tokens follow substantially different expert pathways, unlike vision-language MoEs (e.g., MoE-LLaVa) where image and text tokens share near-identical routing. The paper (Figure 3) documents this and attributes it to a fundamental difference: individual protein tokens (amino acids) do not independently convey protein-level meaning, whereas image patches contain independently meaningful information. This finding both validates the paper's design choice (using complete protein representation sequences rather than compressed tokens) and provides guidance for future multimodal protein-language architectures. The honest reporting of the TrEMBL negative result is also notable — adding 5.25M supplementary instructions from lower-quality annotations *decreased* performance, a non-obvious result that the paper attributes to noise from low-quality data, supporting a quality-over-quantity conclusion for protein instruction data.

## Suggestions

1. **Add at least one external evaluation of the full SEPIT model** on a standardized protein property prediction benchmark (e.g., EC/GO prediction, subcellular localization). Even a limited evaluation with a few hundred examples would substantially strengthen the "general-purpose" claim.
2. **Acknowledge the in-distribution evaluation limitation explicitly** in the paper, noting that the full model's absolute performance on external benchmarks remains to be verified, while the relative improvements over baselines on the held-out test set are robust.
3. **Add statistical significance reporting** (standard deviations over at least 3 seeds) for the main results to help readers gauge the reliability of the reported improvements.
4. **Include a brief limitations paragraph** discussing reliance on AlphaFold-predicted structures, potential biases from ChatGPT-designed templates, and computational requirements.
