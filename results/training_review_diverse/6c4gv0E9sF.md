Now I have all the information I need. Let me compile the final review.

---

## Summary

This paper proposes SpikeBERT, a spiking neural network (SNN) for language tasks built by adapting Spikformer (a vision spiking transformer) for text processing. The core contribution is a two-stage knowledge distillation method from BERT: Stage 1 aligns embeddings and hidden features on unlabeled text, Stage 2 fine-tunes on task-specific data using logits and feature alignment losses. Experiments on six text classification datasets (English and Chinese) show SpikeBERT outperforms existing SNN baselines (SNN-TextCNN and direct-trained Spikformer) by ~3.5% absolute accuracy on average, while achieving theoretical energy savings of ~70% relative to BERT.

## Strengths

- **Substantial accuracy improvement over prior SNN approaches for language**: SpikeBERT achieves 80.20% average accuracy across six benchmarks, outperforming SNN-TextCNN (76.71%) and the directly-trained Spikformer (77.36%) by more than 3 percentage points on average, with up to 5.42% improvement on individual datasets (Table 1, Section 4.3). This is a meaningful advance for deep SNNs in NLP.

- **Two-stage distillation method validated by thorough ablation**: Removing Stage 1 or Stage 2 each causes ~3.2% average accuracy drop (Table 3, Section 4.5). The ablation further decomposes Stage 2 loss components, showing logits loss has the largest impact (3.03% drop) while cross-entropy loss contributes little (0.17% drop). This provides clear evidence that both stages are necessary and identifies which knowledge transfer mechanism matters most.

- **Energy efficiency demonstrated with concrete estimates**: SpikeBERT consumes only ~27.82% of BERT's theoretical energy on average across six datasets (Table 2, Section 4.4), with the largest per-dataset reduction reaching 73.63% (Subj). The paper correctly notes that this energy advantage is distinct from model compression methods and depends on neuromorphic hardware.

- **Cross-lingual validation**: Evaluation spans English (MR, SST-2, SST-5, Subj) and Chinese (ChnSenti, Waimai) datasets, demonstrating the method generalizes beyond a single language (Table 1, Section 4.1).

- **Architectural adaptation is clearly described**: The paper explains the modifications from Spikformer — replacing SPS with word embeddings, convolution+BN with linear+LN, and changing attention from D×D to N×N — with a clear motivation for each change (Section 3.2, Fig. 1).

## Weaknesses

### Fatal
None.

### Major
None. The core claims are supported by evidence; no weakness invalidates the paper's central contribution.

### Minor

1. **"Comparable to BERT" claim is somewhat overstated.** The abstract and conclusion frame SpikeBERT as achieving "comparable results to BERTs," but Table 1 shows a systematic accuracy gap averaging 4.13% (84.33 vs. 80.20), with individual gaps as large as 6.94% on MR (87.63 vs. 80.69). To the paper's credit, Section 4.3 does quantify the exact 4.13% gap ("a small drop..."). However, the abstract/conclusion language glosses over this difference. "Competitive" or "narrowing the gap" would be more precise. This does not undermine the paper's value — the contribution is still clear — but the framing should be aligned with the evidence.

2. **Energy consumption methodology is underspecified.** Table 2 reports FLOPs for BERT and SOPs for SpikeBERT, then derives energy using Horowitz (2014) numbers. However, the paper does not explain: (a) how SOPs are counted — whether they account for actual spike rates (which depend on threshold, input, and time steps) or assume maximum spike activity; (b) whether the SOP numbers already include the time step dimension (T=4); (c) the specific energy-per-operation values used for FLOPs and SOPs. SpikeBERT's SOP count (e.g., 28.47 G for ChnSenti) is larger than BERT's FLOP count (22.46 G), yet the energy is much lower — this is plausible given the per-operation cost difference but deserves explicit explanation. The general approach is standard in SNN literature, but the lack of detail weakens the rigor of the energy claim.

3. **Token-wise (N×N) vs. dimension-wise (D×D) attention choice is heuristic without ablation.** The paper states: "we think that the features shared with words in different positions by attention mechanism are more important than those in different dimensions" (Section 3.2), then changes the SSA attention map from D×D to N×N. No analysis or ablation is provided to support this claim. Given that the binary nature of Q_s, K_s, V_s makes N×N attention compute a fundamentally different quantity (coincidence counts of spikes) than softmax attention, this design choice is non-trivial. The paper should either ablate both variants or acknowledge the choice as heuristic.

4. **SNN baseline comparison is narrow.** The paper compares against only one prior SNN approach (SNN-TextCNN) plus a direct-trained version of its own architecture. While SpikeGPT is cited in related work as a spiking language model, it is not included as a baseline. The paper's claim of outperforming "state-of-the-art SNNs" would be strengthened by a broader comparison. (Note: SpikeGPT is a generative model, so direct comparison on classification is not straightforward — but the general point about narrow baselines stands.)

### Trivial
None.

## Nice-to-Haves

- The paper mentions attempting direct MLM/NSP pretraining and failing (Section 3.3) but provides no details about the setup (depth, learning rate, time steps). Including these details would strengthen the motivation for distillation and serve as a useful negative result for the community.
- The hyperparameter choices for neuron threshold (0.25 in SSA vs. 1.0 elsewhere) and the scaling factor τ=0.125 are not explained or ablated. A brief sensitivity analysis (even on one dataset) would help assess how robust the method is to these spiking-specific parameters.
- The paper focuses on text classification. Adding a sentence scoping future work to other NLP tasks (e.g., sequence labeling, QA) would align the title's "language" framing with the actual evaluation scope.

## Removed Points

- **Demand for SpikeGPT comparison (from Harsh Critic Point 2)**: Removed because SpikeGPT is a generative spiking language model, not a classifier. Adapting it for text classification with a task head is not a standard or trivial baseline, and the ask constitutes scope creep. The underlying concern about narrow baselines is kept (Minor Weakness #4), but the specific SpikeGPT demand is removed.
- **Criticism about "state-out-of-art" typo**: Removed per instructions — typographical nitpicks are not author errors (they are likely parser artifacts).
- **Criticism that the paper lacks justification for D×D vs. N×N being "necessary"**: Kept in softened form (Minor Weakness #3) — the point that no ablation supports this choice is valid, but the claim that the paper asserts it as "necessary" overstates the paper's language. The paper says "we think" and "most importantly," which is heuristic, not a formal necessity claim.

## Novel Insights

The reviews surface a recurring tension: the paper's results are genuinely solid (clear improvement over SNN baselines, well-structured ablation, plausible energy savings), but the framing consistently reaches one step beyond what the evidence supports. The "comparable to BERT" language, the underspecified energy methodology, and the heuristic architectural choice all share this character — the paper has real contributions but would benefit from more measured presentation. The most interesting insight from the reviews is that the logits loss dominates the Stage 2 contribution (3.03% drop when removed), far exceeding feature loss (1.90%) and embedding loss (1.74%). This suggests that for SNN distillation, task-specific output distribution matters more than hidden feature alignment, which could inform future SNN training strategies beyond this specific architecture.

## Suggestions

1. **Revise the abstract and conclusion** to replace "comparable results to BERTs" with language like "competitive with BERTs while narrowing the gap from prior SNN approaches" or "achieves results within 4% of BERT with ~70% less energy." The data is already in the paper — align the narrative claims with it.
2. **Specify the SOP computation methodology**: Report whether SOPs account for actual spike rates or assume maximum activity, clarify that the time step dimension T=4 is factored in, and state the per-operation energy values used (e.g., E_FLOP = X pJ, E_SOP = Y pJ on 45nm CMOS from Horowitz 2014).
3. **Add an ablation comparing N×N vs. D×D attention** on at least one dataset. If the results are similar, acknowledge both variants are viable; if N×N is better, this becomes a non-trivial architectural finding.
4. **Expand the SNN baseline discussion**: While adding SpikeGPT is not straightforward due to task differences, the paper could discuss how SpikeBERT's performance compares roughly to other spiking approaches for language (e.g., noting that SpikeGPT targets generation, not classification, so direct comparison is left for future work).
5. **Add a brief sensitivity analysis** for the threshold (0.25 vs. 1.0) and τ=0.125 hyperparameters, or at minimum note that these values were chosen based on a small validation set.

## Score and Decision

The paper makes a genuine contribution: it demonstrates that a deep spiking transformer can be trained for text classification via two-stage distillation, achieves meaningful accuracy gains over prior SNN methods, and quantifies substantial theoretical energy savings. The weaknesses are all addressable — none threaten the core findings. The ablations are well-executed and informative. The paper is clearly written and the method is reproducible.

**Originality**: Good — adapting Spikformer for language and the two-stage distillation from BERT to SNN is a novel combination.  
**Importance**: Good — energy-efficient NLP is an increasingly relevant problem.  
**Claims support**: Adequate — main claims are supported, but some framing (comparable to BERT) and methodology (energy computation) need tightening.  
**Soundness**: Good — ablation study is strong; main experimental results are clear.  
**Clarity**: Good — well-structured, clear figures, method is explained in sufficient detail.  
**Value to community**: Good — provides a practical recipe for training deep SNNs for language and a useful negative result about direct MLM/NSP pretraining.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>