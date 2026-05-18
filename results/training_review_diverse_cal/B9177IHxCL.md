Now I have a thorough understanding of the paper and all the reviewer claims. Let me compose the final consolidated review.

---

## Summary

This paper identifies a genuine gap in LLM-based molecular generation: existing models produce structurally similar molecules despite the need for diversity in drug discovery. It proposes a two-stage fine-tuning approach—supervised fine-tuning (SFT) to adapt LLMs to autoregressively output multiple molecules, followed by multi-stage reinforcement learning (RL) to maximize structural diversity—without requiring external diverse datasets. Experiments on BioT5$^{+}$, MolT5, and DrugAssist show consistent improvements in NCircles and internal diversity over decoding schemes (diverse beam search, contrastive beam search) and over other LLMs including GPT-4o and o1-preview.

## Strengths

- **Empirical identification of a real diversity gap in LLM-based molecular generation.** The paper provides concrete evidence (Section 1, Figure 1) that even state-of-the-art models like ChatGPT-4o generate structurally identical or near-identical molecules from the same prompt, and that diverse decoding schemes fail to improve molecular structural diversity (Figure 2). This clearly motivates the fine-tuning approach.

- **Novel two-stage fine-tuning with multi-stage RL to solve credit assignment.** The core methodological contribution is repurposing LLMs to autoregressively generate a set of molecules and applying molecule-wise (multi-stage) RL rather than sequence-wise RL. The ablation (Table 4, Section 5.4) validates that multi-stage RL significantly outperforms single-stage RL, confirming that the credit assignment problem is real and that the proposed solution works.

- **Consistent and substantial empirical outperformance across multiple settings.** Div-SFT+RL achieves higher NCircles and internal diversity than all baselines—including diverse decoding schemes applied to BioT5$^{+}$ and MolT5 (Figure 2, Section 5.1), other specialist and generalist LLMs (Table 2, Section 5.2), and generalizes to unseen properties (QED) when fine-tuned on DrugAssist (Section 5.3, Figure 3). The self-improvement paradigm (no external diverse datasets) makes the approach data-efficient.

- **Generalizability across model families.** The method is successfully applied to domain-specialist models (BioT5$^{+}$, MolT5) and a generalist model (DrugAssist), demonstrating versatility beyond a single architecture.

- **Comprehensive ablation analysis.** The paper ablates design choices including hard-filtering vs. RL, single-stage vs. multi-stage RL, and runtime-performance trade-offs (Section 5.4), confirming that the RL fine-tuning and multi-stage setup are critical.

## Weaknesses

### Fatal
None.

### Major

- **BLEU-based property-matching reward is a semantic proxy, not a genuine property validator.** The description-matching reward $r_{\text{match}}$ (and the evaluation filter for "accepted" molecules) relies on BLEU score between the generated SMILES and a ground-truth example (line 125, 134). BLEU measures surface-level string overlap, not whether the molecule actually possesses the described chemical property. A molecule could pass the BLEU > 0.7 threshold while being structurally different from the described property, or fail it while genuinely satisfying the description. This limitation is acknowledged by the paper as following prior work (Edwards et al., Pei et al.), and importantly the *diversity* reward $r_{\text{div}}$ correctly uses Tanimoto similarity on true molecular structures. However, the core task requires generating molecules that *actually satisfy* the described property, so the reliance on BLEU weakens the claim that diversity gains are among truly property-satisfying molecules. The DrugAssist experiments (Section 5.3) partially mitigate this concern by using genuine property validators. The authors should validate a subset of generated molecules with a structural property predictor or RDKit descriptor matching.

### Minor

- **No multiple runs or statistical significance reported.** All experimental results appear to come from a single training run. The stochasticity of RL fine-tuning means that reported numbers could vary across seeds. While the evaluation spans 3,300 test descriptions (decoding comparison) and 500 (LLM comparison)—which provides aggregate stability—the lack of reported error bars or multiple-seed statistics makes it difficult to assess whether performance gaps are reliable. Running 3–5 independent seeds and reporting means/standard deviations would strengthen the conclusions.

- **Ordering and composition of the SFT training data not specified.** The SFT stage concatenates filtered molecules into a sequence $\mathcal{M}_{1:K}$ (line 81), but the ordering criterion (random? sorted by likelihood? by similarity?) is not stated. Since the RL stage conditions on previously generated molecules, the ordering matters for the conditional generation task. Additionally, reporting the average pairwise Tanimoto similarity of SFT-collected molecules would help gauge how much diversity the RL stage must introduce.

- **"First" claim is slightly overbroad.** Line 37 states "We are the first to explore the use of LLMs for generating diverse molecules." Prior work on LLM-based molecular generation (MolT5, BioT5$^{+}$) has evaluated diversity as a secondary metric, and diverse decoding schemes exist. The paper's genuine novelty is *fine-tuning LLMs to explicitly optimize structural diversity via RL*, which stands without the superlative. The claim should be qualified (e.g., "first to fine-tune LLMs explicitly for structural diversity in molecules").

- **Time-cost analysis compares across different GPU counts.** The comparison in Section 5.4 uses a single GPU for the proposed method but four GPUs for beam search baselines (line 167), making the wall-clock comparison less clean. The cost advantage is still evident, but normalizing by GPU-hours would be fairer.

- **500-test-subset for LLM comparison.** The LLM comparison (Section 5.2) uses the first 500 test descriptions due to API costs. While the paper is transparent, it reduces sample size relative to the full 3,300. The authors should note whether the subset was randomly drawn and whether baseline performance on the subset is consistent with full-set results (when known from prior work).

### Trivial

- **"K" (number of molecules per prompt) is fixed at 50 in experiments** but the paper does not clarify whether the model can stop early or always generates exactly K molecules, which affects the RL formulation. This is a minor clarity issue.

## Nice-to-Haves

- Validating a subset of BLEU-filtered molecules with a structural property predictor (e.g., RDKit descriptors matching logP, molecular weight, ring counts) would substantially strengthen the credibility of the property-satisfaction claim.
- Reporting the average pairwise Tanimoto similarity of SFT training data would clarify the difficulty the RL stage must overcome.
- Including a non-LLM diverse generation baseline (e.g., a genetic algorithm on SMILES or a VAE with diversity objective) would further situate the LLM-based approach.
- More hyperparameter details (learning rate, KL coefficient, number of RL steps) in the main text would aid reproducibility.

## Removed Points

- **"AutoRegressive" formatting artifact in title:** Parser artifact, not an author error → removed.
- **Criticism that BLEU makes diversity gains "unclear":** The diversity reward $r_{\text{div}}$ and the NCircles/IntDiv metrics use Tanimoto similarity on actual molecular fingerprints, so diversity gains are measured structurally, not via BLEU. The BLEU concern applies only to property filtering, not diversity measurement → downgraded from the reviewer's "fatal" characterization to Major.
- **Complaint about missing appendix content:** Parser strips appendix sections from all papers; they exist in the original submission → removed.
- **Criticism about missing hyperparameter details in main text:** Addressed by the paper's reference to the appendix, which is standard practice → removed, moved to Nice-to-Haves.

## Novel Insights

The most interesting observation across reviews is the tension between using BLEU (a surface string metric) for property matching versus Tanimoto similarity (a structural fingerprint metric) for diversity. The paper's contribution is genuinely about structural diversity, and the diversity reward correctly uses Tanimoto similarity—yet the property filter uses BLEU, creating an asymmetry that future work should resolve. The multi-stage RL framing of the credit assignment problem (each molecule generation is a separate stage with its own reward) is a clean formulation that could transfer to other "set generation" tasks beyond molecules, such as code generation or protein design.

## Suggestions

1. **Validate property satisfaction structurally.** For a subset of generated molecules, check that they satisfy the described property using RDKit descriptor matching or a pre-trained property predictor. Show that BLEU-filtered molecules actually possess the described properties.
2. **Report means and standard deviations over 3–5 independent training seeds** for all key experiments to establish statistical reliability.
3. **Clarify the ordering of molecules in SFT sequences** and report the average pairwise Tanimoto similarity of the SFT training data.
4. **Qualify the "first" claim** to avoid unnecessary scrutiny—the contribution stands on its technical merits.

## Score and Decision

The paper identifies a genuine gap, proposes a well-motivated solution (two-stage SFT + multi-stage RL), and provides consistent empirical evidence across multiple models and tasks. The most significant weakness (BLEU-based property matching) is a standard practice in the field, partially mitigated by the DrugAssist experiments using genuine property validators, and does not affect the structural diversity measurements (which use Tanimoto similarity). The remaining weaknesses (no multiple runs, SFT data ordering, scope of claims) are addressable and do not undermine the core contribution. The paper represents a solid contribution to LLM-based molecular generation.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>