- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 8, 3
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper tackles the important problem that LLMs for molecular generation tend to produce structurally similar molecules even when prompted for diversity. The authors propose Div-SFT+RL, a two-stage fine-tuning approach: (1) supervised fine-tuning to repurpose LLMs to autoregressively generate sequences of multiple molecules conditioned on previously generated ones, and (2) multi-stage reinforcement learning that directly optimizes a structural diversity reward (complement of maximum Tanimoto similarity) along with a description-matching reward. Experiments on ChEBI-20 and property-based prompts across multiple base models (BioT5⁺, MolT5, DrugAssist) show that the method achieves higher structural diversity than decoding-scheme baselines and other LLMs.

## Strengths

1. **Two-stage fine-tuning demonstrably outperforms decoding schemes for structural diversity.** The paper shows that Div-SFT+RL produces substantially higher NCircles and internal diversity than diverse beam search, contrastive beam search, and other decoding baselines on both BioT5⁺ and MolT5 (Section 5.1, Figures 2–3). This is strong evidence that fine-tuning—not decoding modifications—is the effective route for molecular structural diversity, which is the paper's central claim.

2. **Multi-stage RL successfully resolves the credit-assignment problem.** The ablation study (Section 5.4, Table 4) directly compares single-stage (sequence-wise) vs. multi-stage (molecule-wise) RL and shows a clear advantage for multi-stage on NCircles. This validates the paper's motivated claim that conventional sequence-wise RL struggles to attribute rewards to specific molecules responsible for increasing diversity.

3. **The method generalizes to generalist LLMs and unseen property prompts.** Results on DrugAssist (Llama-based) in Section 5.3 (Figure 5) show consistent improvement across all four property prompts, including QED which was explicitly held out from training. This demonstrates robustness beyond chemical-specialist models and some generalization to unseen properties.

4. **The approach does not require external datasets of diverse molecules.** Both SFT and RL stages rely entirely on self-generated samples from the base model (Section 4). This is a practical advantage for settings where curated diverse molecular sets are unavailable.

5. **Computational efficiency advantage over decoding alternatives.** The time-cost analysis (Section 5.4, Table 5) shows Div-SFT+RL on a single GPU matches or exceeds beam search variants that require four GPUs at large beam sizes, while also discovering more diverse molecules per total generated.

## Weaknesses

### Fatal
None.

### Major

1. **The "description satisfaction" criterion relies on BLEU > 0.7 against a single ground-truth SMILES, which is a weak proxy for whether a molecule actually satisfies the described property.** The paper notes (line 125, footnote) that this follows prior work (Edwards et al., 2022), but the limitation is significant for the paper's own claims. BLEU measures textual overlap in SMILES strings against one example molecule, not chemical property satisfaction. Two molecules with very different SMILES can both satisfy a description, and high BLEU does not guarantee property satisfaction. Since the "accepted & unique" count and all downstream diversity metrics (NCircles, IntDiv) are computed only on molecules passing this BLEU threshold, the headline results may partly reflect diversity among SMILES that are textually similar to the reference rather than molecules that are chemically fit-for-purpose. The property-based experiments (Section 5.3) avoid this issue via exact computation, which is reassuring, but those are supplementary experiments; the main ChEBI-20 results depend on the BLEU filter.

2. **The description-matching reward used during RL training is the same BLEU metric used for evaluation acceptance.** The RL reward (line 134) includes a BLEU-based description-matching term, and evaluation filters by BLEU > 0.7. This means the RL method is explicitly trained to produce SMILES strings with high BLEU to the reference, while the decoding baselines are not. Consequently, the RL method may have an advantage in passing the acceptance filter, potentially inflating its "accepted & unique" counts and the diversity metrics computed on the accepted set. A more independent validation (e.g., property predictors, or a held-out set with different acceptance criteria) would strengthen confidence that the diversity gains are not artifacts of this alignment.

### Minor

1. **No variance or statistical significance reported.** The paper reports single-point results without confidence intervals, standard deviations, or multiple seeds (Sections 5.1–5.4). Given that LLM sampling is stochastic and baselines involve varied hyperparameters, we cannot assess whether the reported improvements are robust or within the noise of the method.

2. **Comparison with existing LLMs uses only the first 500 of 3,300 test descriptions without justification.** Line 144 states that the comparison (Table: "sota") uses the first 500 descriptions, but provides no analysis showing this subset is representative of the full test set. While API cost for GPT models is a practical constraint, the paper should at minimum report how the subset's characteristics (e.g., description length, property distribution) compare to the full set.

3. **The SFT data collection pipeline is underspecified.** The paper collects 100 molecules per prompt via beam search, then filters (line 80, line 134). It does not report the fraction of prompts that yield sufficient valid/accepted molecules after filtering, nor the distribution of retained molecule counts. If many prompts yield few valid molecules, the SFT supervision signal may be weak or uneven. These statistics may appear in the stripped appendix, but the main text would benefit from a summary.

4. **Fingerprint parameters for Tanimoto similarity are not specified.** The diversity reward and evaluation metrics (NCircles, IntDiv) rely on Tanimoto similarity computed from molecular fingerprints, but the paper does not specify the fingerprint type, radius, or bit length (line 123–127). This affects reproducibility of the diversity computation.

### Trivial
None.

## Nice-to-Haves

- Report validity rates for all baselines, especially GPT models, for context on the "accepted & unique" counts.
- Include an analysis of drug-likeness or synthesizability of generated molecules to address whether diversity comes at the cost of quality.
- Compare against additional decoding or sampling strategies on the property-based prompts (Section 5.3) beyond random sampling and contrastive beam search.

## Removed Points

The following points raised by the reviewers are removed with justification:

- *"The comparison feels staged to show a clear win."* — Subjective assertion without specific evidence; the paper transparently reports its experimental choices.
- *"No code availability mentioned."* — Code release is a nice-to-have, not a weakness. The hard rule removes reproducibility nitpicks about artifacts impractical for submission.
- *"Validity rates of generated SMILES are not reported for LLM baselines."* — These details may appear in the stripped appendix.
- *"SFT dataset statistics not reported."* — Same as above; likely in appendix.
- *"Adding a second description-based dataset would strengthen claims."* — Scope creep; the paper evaluates on the standard benchmark.
- *"The decoding schemes discussion could more explicitly note that these methods operate at the sequence level."* — Presentation suggestion, not a weakness; the paper already makes this point.
- *"Missing related works."* — Cannot be verified without external sources.

## Novel Insights

Beyond the paper's own contributions, the most informative cross-cutting observation from the reviews is that the BLEU-based evaluation reliance creates a tension: the paper convincingly demonstrates that RL-based fine-tuning produces structurally more diverse molecule sets, but the strength of this conclusion is tempered by the fact that the description-satisfaction filter (BLEU) is both weak and aligned with the training objective. The multi-stage RL credit-assignment solution is well-supported by the ablation, making it the most robust contribution. The gap between the property-based experiments (which use exact computation) and the description-based experiments (which use BLEU) suggests a natural path for strengthening: validating the description-based results with property predictors.

## Suggestions

1. **Address the BLEU dependency in evaluation.** At minimum, provide a supplementary analysis using a molecular property predictor or a cheminformatic oracle to validate that the "accepted" molecules genuinely satisfy the descriptions. Show that the diversity trends hold when a stricter or independent acceptance criterion is applied.

2. **Report results with statistical significance.** Run each experiment with 3–5 random seeds and report means and standard deviations. This is essential given the stochasticity of LLM sampling and RL training.

3. **Justify or expand the LLM comparison subset.** Either provide evidence that the first 500 ChEBI-20 descriptions are representative, or expand to a larger random sample. Also report per-model performance on basic quality metrics (validity, uniqueness).

4. **Specify the fingerprint parameters** (type, radius, bit length) used for all Tanimoto-based computations.
