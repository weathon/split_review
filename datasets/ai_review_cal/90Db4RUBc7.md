- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 8, 6, 8
Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes Cross-Architecture Layerwise Distillation (CALD), a framework to jointly convert a pretrained transformer into a linear-complexity model (Linformer, Mamba, Mamba2) and fine-tune it on a downstream task. The approach combines parameter transfer with layerwise hidden-state distillation and introduces several guidance modes (target, trajectory, waypoint, hybrid) that differ in how they leverage the teacher model during conversion. Experiments cover RoBERTa→Linformer (NLP classification), Pythia→Mamba (language modeling), and Wav2Vec2→Mamba2 (speech tasks), demonstrating that CALD substantially closes the gap between naive parameter transfer and the original transformer's performance.

## Strengths

1. **Broad experimental validation across diverse domains and architectures.** The paper evaluates CALD on three distinct settings (NLP classification, language modeling, and speech tasks including ASR, SLU, SID) using three different target architectures (Linformer, Mamba, Mamba2). Table 1 shows trajectory-guided CALD achieves 92.5% average accuracy on NLP benchmarks — recovering nearly all of the gap from the naive unguided baseline (72.9%) to the standard RoBERTa (93.8%). Table 3 shows hybrid CALD on speech tasks obtains 6.41% WER (vs. Std. Wav2Vec2's 6.24%), 91.23% IC accuracy (vs. 91.70%), and 96.41% SID accuracy (vs. 96.09%). These results directly support the claim that CALD effectively converts transformers to linear-complexity models with minimal performance loss.

2. **Novel trajectory and waypoint guidance strategies that demonstrably improve upon standard target-guided distillation.** Trajectory-guided CALD (92.5%) outperforms target-guided (91.6%) on NLP tasks (Table 1), and the hybrid approach consistently beats target-guided on language modeling across all data fractions (Table 2: e.g., 2% Pile: hybrid 0.525 vs. target-guided 0.520). These results support the claim that the choice of guidance strategy contributes to the outcome.

3. **Extension of conversion methodology to speech tasks with a principled bidirectional adaptation.** The paper converts the bidirectional Wav2Vec2 to Mamba2 by replacing each attention layer with forward and backward Mamba2 mixers (Section 4.1, Figure 1), extending prior NLP-only conversion work to the less-explored speech domain.

4. **Analysis of hidden-state shift provides a principled explanation for when trajectory guidance is effective.** Figure 2 (feature shift figure) measures cosine distance between initial and fine-tuned hidden states: speech models show a much larger shift (0.372 after only 2,000 steps) than NLP models, correlating with the observation that trajectory/waypoint guidance helps in NLP but not in speech. This provides a predictive insight beyond a simple ablation report.

## Weaknesses

### Fatal

None.

### Major

- **The headline comparison against the pretrained Linformer is cross-paper and not fully controlled.** The paper reports that trajectory-guided CALD "can even reach better results (+0.2% on average)" compared to the pretrained Linformer (Table 1), but these Linformer numbers are taken from the original Linformer paper, which used a different pretraining corpus and procedure. The authors transparently note this ("the fully re-pretrained Linformer, which is not publicly available," line 119, and the table caption says "reported results"), but the claim is broader than what the evidence supports. The gap between trajectory-guided CALD (92.5%) and the authors' own fine-tuned RoBERTa (93.8%) is 1.3%, which is a more controlled comparison. The authors should either reproduce the pretrained Linformer under their own pipeline or explicitly soften the claim about "matching/exceeding" the pretrained model.

### Minor

- **Language modeling experiments provide limited evidence.** The conversion from Pythia to Mamba is conducted only on the 1B model using a tiny fraction of the pretraining corpus (0.5–2% of Pile, 1.5–6B tokens). The improvements from CALD over unguided are modest (e.g., 0.525 vs. 0.514 average at 2% Pile). The paper acknowledges this is "not our focus" (lines 100, 173), and the consistent positive trend across data fractions is encouraging, but single-model-size results with no run-to-run variance reported constitute thin evidence for the claimed generality.

- **No error bars or variance estimates for any experiment.** All tables report point estimates. Given that CALD involves several hyperparameters (distillation weights α, temperature β, update frequency, etc.), single runs leave uncertainty about the stability and statistical significance of the reported gains. This is standard in parts of the field but would meaningfully strengthen the paper.

- **The trajectory-guided condition is not tested on speech tasks.** Waypoint guidance (the coarser approximation) underperforms target-guided on speech, and the authors provide a reasonable hypothesis backed by hidden-state shift analysis (Figure 2). However, trajectory guidance is a core contribution and the most precise form of the method. While the paper's reasoning is sound — if the coarse approximation fails, the finer-grained version would likely also fail — empirical confirmation on at least one speech task would make the analysis conclusive rather than post-hoc.

### Trivial

- The paper does not explicitly state the total number of fine-tuning steps or the learning rate schedule for the speech experiments (only the waypoint frequency of 10,000 steps is given). These details are likely in the (stripped) appendix.

## Nice-to-Haves

- **Inference efficiency measurements.** The paper is motivated by achieving linear complexity, but never reports wall-clock speed or memory usage for the converted models (e.g., on a long sequence of 16k tokens). A brief efficiency table would substantiate the practical motivation and make the contribution more compelling for practitioners.

## Removed Points

These points were considered but removed from the main evaluation for the reasons stated:

- **"The bidirectional Mamba construction doubles parameters, contradicting claims."** The paper explicitly addresses this: each Mamba2 mixer uses "expand factor = 1" (line 106). In Mamba2 the default expand factor is 2, so two mixers at expand=1 have roughly the same parameters as one standard attention layer. The criticism does not hold given the paper is transparent about this design choice.

- **"KL divergence notation could be confusing."** The notation `log((y_i^(t)/β) / (y_i^(s)/β))` is standard for KL divergence with temperature scaling. This is a correct formulation and not a weakness.

- **"Language modeling results are weak" framed as a structural flaw rather than acknowledged scope limitation.** The paper explicitly states twice (lines 100, 173) that language modeling conversion during re-pretraining is not its focus. The results are presented as supplementary evidence. The weakness is real but the severity in the original critic's framing overstates it.

- **"Results are weak compared to Pythia" without noting the very limited training data.** The paper trains on only 0.5–2% of the pretraining corpus, and the gap to the original Pythia is expectedly small (0.544 vs. 0.525 at 2% Pile). The comparison is reasonable given the experimental constraints.

## Novel Insights

The individual reviews did not surface any insight about the paper that goes beyond the paper's own contributions. The hidden-state shift analysis (Figure 2) as a predictor of trajectory guidance effectiveness is the paper's own insight, well-supported by the evidence presented.

## Suggestions

1. **Clarify the Linformer comparison.** Either reproduce the pretrained Linformer under controlled conditions, or explicitly remove the "better results (+0.2%)" framing and recast the comparison solely against the authors' fine-tuned RoBERTa, noting the pretrained-Linformer numbers are provided for reference only.

2. **Add run-to-run variance.** Report results from at least 2–3 seeds for a representative subset of experiments (e.g., the NLP benchmarks) to demonstrate statistical reliability of the reported trends.

3. **Include a single speech experiment with trajectory guidance** to empirically validate the hidden-state shift hypothesis, even if only on one task (e.g., ASR on TED-LIUM). This would make the analysis predictive rather than post-hoc.

4. **Add a brief efficiency table** showing inference time and/or memory for the original transformer vs. the converted model on a long input sequence, to substantiate the practical motivation.

5. **Explicitly state the total training steps and learning rate for the speech experiments** in the main paper body.
