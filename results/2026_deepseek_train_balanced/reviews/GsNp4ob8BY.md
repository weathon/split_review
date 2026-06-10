Now let me produce the final formatted review.

## Summary

This paper proposes "ability tokens" — learnable continuous embeddings appended to an LLM's embedding matrix — as a parameter-efficient method for adapting frozen pretrained LMs to specialized domains. Two token types are introduced: domain markers (delimit specialized input spans) and functional tokens (encode tasks). A three-stage hierarchical training protocol uses unlabeled data for markers and labeled data for functional tokens. The method achieves a state-of-the-art result on the TDC Drug Combination benchmark and shows competitive performance on molecular property prediction and binding affinity tasks using LLaMA-7B.

## Strengths

- **Task-specific output heads solve a real, diagnosed limitation** of using autoregressive LMs for regression. Section 3.2.3 (lines 119–120) identifies that cross-entropy loss is order-agnostic for numerical outputs, making text-generation a poor proxy for scalar prediction. The ablation in Figure 3 (right) validates this: replacing the regression head causes the largest performance degradation among all ablated components.

- **State-of-the-art on a real-world drug-discovery benchmark.** Section 4.2.2 (line 170) reports MAE=8.20 on the TDC DrugComb CSS benchmark, outperforming not only all LM-based baselines but also the domain-specific expert model (Xia et al., 2018, MAE=10.07). This is a genuine, practically meaningful result.

- **Systematic ablation of design choices.** Figure 3 separately ablates token length (p ∈ {1,5,10,20,50}), each component type (domain markers, functional tokens, regression heads), and marker enrichment. The non-monotonic relationship between token length and error provides empirical grounding for the method's parameter-efficiency claims.

- **Extreme parameter efficiency.** Each ability token uses only 40,960 parameters for LLaMA-7B (p=10, d=4096). Table 2 shows the method outperforms LoRA (which modifies orders of magnitude more parameters) on both protein descriptor prediction and SMILES QED prediction.

## Weaknesses

### Fatal

None.

### Major

1. **The headline claim of compositionality / zero-shot generalization has no supporting evidence in the reviewed text.** Section 4.1 is the designated experiment for this claim — it describes training 8 language markers and a single ⟨Translate⟩ functional token on 5 language pairs, with the explicit goal of verifying modularity and compositionality (line 135: "Our goal is to verify (i) if the markers can correctly extract the domain information from the data (modularity); and (ii) the learned functional token can generalize to unseen domains and translation pairs (compositionality)"). However, the section ends at line 137 with "format each example as follows:" and no results, tables, or analysis follow. The terms "zero-shot generalization" and "compositionality" appear only in the abstract (line 4) and introduction (line 30) but receive no experimental support in the reviewed paper. Since this claim is one of two headline contributions in the abstract, the gap between promise and evidence is substantial.

2. **The claim that the method "preserves the model's original capabilities" is asserted without any experimental validation.** The paper repeatedly states that because pretrained weights remain intact, general capabilities are retained (abstract, line 14: "preserving the pretrained weights and the model's original capabilities"; Section 3.1). However, adding new embeddings to the input layer changes the model's input distribution and can affect behavior on standard text inputs. The paper provides zero experimental validation of this claim: no perplexity on a general-domain corpus, no performance on standard NLP benchmarks (e.g., MMLU, HellaSwag), no comparison of LLaMA-7B outputs with and without ability tokens on non-specialized inputs. A benefit that the paper uses to distinguish itself from fine-tuning is entirely unverified.

### Minor

3. **No statistical variance or significance is reported for any experiment.** All results (Tables 2, 3; Figure 3) are presented as point estimates without standard deviations, confidence intervals, or multiple random seeds. Given that each ability token uses only ~40K learnable parameters and the dataset sizes in these scientific domains are modest, variance across initializations or data splits could be material. This makes it impossible to assess the reliability of the reported improvements.

4. **The comparison between ability tokens and prompt tuning is confounded by unablated differences in token placement.** Standard prompt tuning places all learnable tokens as a prefix, while the proposed method places domain markers before specialized spans and functional tokens at the end. The ablation (Figure 3, right) removes entire token types but does not control for position. It is plausible that placing prompt-tuning tokens at these same strategic positions would yield comparable improvements, independent of the domain/function distinction. The paper needs an ablation that isolates whether the *type* of token matters or just the *placement*.

5. **The "matching and outperforming expert models" framing (abstract) is narrower than the evidence supports.** The method convincingly outperforms the expert model on Drug Combination (Table 3). However: (a) on Binding Affinity (Table 3) the method ranks 3rd behind two specialized methods, and the paper acknowledges the gap; (b) on the molecular property prediction tasks (Table 2), no domain-specific expert models are included as baselines at all — only PEFT methods, hard prompting, and nearest-neighbor. The claim is accurately supported only for the Drug Combination task.

6. **The three-stage training protocol's Stage 3 is described but not experimentally validated.** The paper presents a three-stage protocol (Section 3.2) where Stage 3 trains multi-domain functional tokens with frozen markers. The binding affinity task (Section 4.2.3) uses two markers (⟨Protein⟩, ⟨SMILES⟩) but it is not explicitly tested whether freezing markers during multi-domain training is beneficial compared to joint training or allowing updates. No experiment compares the three-stage protocol against simpler alternatives.

### Trivial

None.

## Nice-to-Haves

- A position-controlled ablation comparing ability tokens against prompt-tuning tokens placed at the same positions (before specialized spans + at end) would clarify whether the domain/function distinction drives improvements or the placement alone.
- An explicit validation of Stage 3 (multi-domain training with frozen vs. unfrozen markers) would complete the empirical support for the proposed training scheme.
- Reporting the dataset size and coverage of the unlabeled data used for Stage 1 pre-training (cited as "extracted from Blanchard et al. (2021)") would improve reproducibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength Finder's claimed compositionality results (original Strength #2):** The Strength Finder claims that Section 4.1 "shows" the system "generalizes to unseen translation pairs (EN–ES, EN–PT) without any additional training, directly demonstrating the claimed compositionality and modularity." This information does **not** appear in the paper — Section 4.1 ends at line 137 with the setup description and contains no results. This strength is hallucinated and is removed.
- **"Apples to oranges" comparison sub-point (Harsh Critic Issue 5, sub-bullet #4):** The critic frames comparing the 7B LLaMA against small specialized models as "comparing apples to oranges." This is a valid experimental design — the paper shows that a general-purpose LLM with ability tokens can compete with specialized models. The criticism mischaracterizes a legitimate comparison and is removed.
- **Minor reproducibility nitpicks** about undisclosed hyperparameters, initialization alternatives, and inference cost: These are reasonable suggestions but do not constitute core weaknesses of the paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Complete Section 4.1.** If the compositionality results are positive, present them clearly with a table and analysis. This section is the designated evidence for a headline claim and its absence is the paper's most serious gap. If the results do not support strong claims, remove the compositionality/zero-shot generalization language from the abstract and introduction.
2. **Validate the "preserved general capabilities" claim directly.** A single experiment measuring LLaMA-7B's perplexity on WikiText-2 or performance on a subset of MMLU with and without ability tokens would either support or undermine a central advertised advantage over fine-tuning.
3. **Add variance estimates** (standard deviations across at least 3 random seeds) to all reported results.
4. **Calibrate the abstract's claims.** The phrasing "matching and outperforming expert models" applies convincingly only to Drug Combination. Scope this claim to the tasks where it is demonstrated.

## Score and Decision

The paper introduces a conceptually clean and interesting idea (ability tokens with domain/function separation) and delivers a genuine SOTA result on the TDC Drug Combination benchmark with thorough ablations. However, the paper suffers from two major evidence gaps: the headline compositionality/zero-shot generalization claim (prominently featured in the abstract and introduction) receives no experimental support in the reviewed text, and the "preserved general capabilities" claim is asserted without any validation. These gaps create a significant mismatch between the paper's advertised contributions and the evidence provided. At the ICLR level, where claims must be backed by rigorous evidence, these issues are substantial enough to weigh against acceptance in the current form. The core idea and the Drug Combination result are solid and could form the basis of a strong paper after the evidence gaps are addressed.

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**