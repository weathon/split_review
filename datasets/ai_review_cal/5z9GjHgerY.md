- Decision: Accept
- Avg Score: 6.33
- Scores: 3, 8, 8
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

DPLM-2 extends the discrete diffusion protein language model (DPLM) to jointly model both protein sequences and 3D backbone structures. It tokenizes structures via a lookup-free quantization (LFQ) encoder-decoder, enabling discrete-token representation of coordinates, and fine-tunes the pre-trained DPLM on experimental and synthetic structures using an efficient warm-up strategy with LoRA. The model simultaneously generates compatible sequence-structure pairs, achieving strong results on unconditional co-generation, folding, inverse folding, and motif-scaffolding, while also providing structure-aware representations for predictive tasks.

## Strengths

- **High-quality multimodal co-generation with clear evidence.** DPLM-2 simultaneously generates sequences and structures with sc-TM scores exceeding 0.9 across lengths 100–500 (Fig. 2A/B), outperforming Multiflow retrained on the same data (Table 3, "co-gen" row). The co-generation setting outperforms cascaded generation from the same model, directly supporting the claim that joint modeling is beneficial.

- **Warm-up from pre-trained DPLM is shown to be essential via ablation.** The ablation study (Table 4) demonstrates that sequence pre-training (warm-up from DPLM) more than doubles designability at lengths >300 (sc-TM 0.25→0.84 for 300–500) and substantially improves diversity. Data augmentation alone provides a smaller gain. This gives direct, quantitative evidence for a key design claim.

- **LFQ-based structure tokenizer is a concrete technical advance.** The tokenizer evaluation (Fig. 3, §3.3) shows LFQ achieves lower FAPE reconstruction error than VQ-VAE while training in 2 days vs. 15 days, and the 8192-codebook choice delivers the best compression–reconstruction trade-off. Strong correlation between structure tokens and secondary structure (Fig. 3B) validates the representation.

- **Competitive performance on conditional tasks without task-specific architecture changes.** On folding (Table 5), DPLM-2 in zero-shot mode achieves RMSD 4.02 / TM 0.67 on CAMEO, and after supervised fine-tuning reaches RMSD 1.97 / TM 0.86, matching ESMFold. On inverse folding (Table 6), it matches or outperforms Multiflow and ESM3-Open. On motif-scaffolding (Fig. 6), it solves more problems than most baselines and is competitive with RFDiffusion.

- **Generated proteins have secondary-structure distributions closest to natural proteins.** Figure 4A shows DPLM-2's helix/sheet/loop proportions nearly match PDB, while RFDiffusion and Multiflow are helix-biased and ESM3 generates more loops. This is a distinctive advantage over structure-based generative models.

- **Length extrapolation beyond the training cutoff (512→1000).** Figure 2F shows DPLM-2 maintains pLDDT scores close to DPLM for lengths up to 1000, indicating it retains sequence generation capability from pre-training.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Self-mixup strategy is claimed but not experimentally validated.** The paper lists self-mixup as one of three "key recipes" (line 63) and claims it addresses exposure bias to improve generation quality and diversity (line 229). However, the ablation study (Table 4, lines 381–388) only evaluates sequence pre-training and data augmentation; there is no controlled comparison (with vs. without self-mixup) that isolates its effect. While the overall system works well, the claimed benefit of this specific component is unsubstantiated.

- **LoRA for warm-up is not compared to alternatives.** The efficient warm-up uses LoRA to prevent catastrophic forgetting (line 239), which is sensible, but no ablation compares it to full fine-tuning or other parameter-efficient methods. The reader cannot tell whether the warm-up benefit comes from the pre-training itself or from the specific choice of LoRA. This is a minor methodological gap.

- **Catastrophic forgetting analysis in representation learning is limited to one task.** The paper identifies that DPLM-2 underperforms SaProt/DPLM on predictive tasks due to catastrophic forgetting from limited structure data. Table 8 provides supporting evidence on DeepLoc, but this is only one task. A broader demonstration across multiple tasks would strengthen this conclusion (though the analysis is transparent and honest as presented).

### Trivial
None.

## Nice-to-Haves

- The trade-off between structure codebook size (e.g., 8192 vs. other values) and downstream generation diversity/capability could be analyzed. Currently only reconstruction quality is studied.
- Motif-scaffolding evaluation could be strengthened by reporting continuous metrics (e.g., mean motif-RMSD, mean scTM) alongside binary success rates.
- Confidence intervals or standard errors on main benchmark results would be informative, though single-run evaluation is standard practice in this field.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Missing description of self-mixup strategy"** — The paper references §self-mixup (line 229) which was stripped by the PDF parser; the hard rules instruct to remove criticisms about missing sections caused by parser truncation.
- **"No comparison of structure tokenizer on backbone-only vs. full-atom reconstruction"** — The paper explicitly scopes to backbone atoms only (line 151); this is scope creep.
- **"Statistical significance not reported"** — Single-run evaluation on large-scale generative benchmarks is standard practice in this field; this is not a meaningful weakness.
- **Formatting/style nitpicks** — Parser artifacts, not author errors.

## Novel Insights

The strength finder identifies that the real innovations cluster around the *combination* of pre-trained evolutionary knowledge (from DPLM) plus tokenized structure (via LFQ) within a single discrete diffusion framework. The harsh critic's close reading surfaces that the self-mixup component, while mentioned, is the least substantiated element. An interesting cross-cut not explicitly stated by either reviewer: the paper's strongest evidence comes from tasks where multimodal conditioning is a natural fit (co-generation, motif-scaffolding with multimodal inputs), while its weakest evidence is on tasks where structure is merely an auxiliary signal (representation learning). This suggests the main value proposition — joint sequence-structure understanding — is well-supported exactly where you would expect it to shine.

## Suggestions

1. Include an ablation experiment for the self-mixup strategy (sc-TM, pLDDT, diversity with vs. without self-mixup under identical settings) to substantiate the claimed improvement in generation quality and diversity.
2. Add a comparison of LoRA vs. full fine-tuning (or another PEFT method) in the warm-up ablation to clarify the source of benefit.
3. For the representation learning analysis, extend the catastrophic forgetting investigation to at least 2–3 additional predictive tasks beyond DeepLoc to strengthen the conclusion.
