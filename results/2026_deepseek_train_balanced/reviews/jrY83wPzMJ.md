## Summary

This paper proposes a synchronous (jointly trained) architecture for Scene Text Image Machine Translation (Scene TIMT) that simultaneously detects text regions, recognizes source text, and translates it into a target language. The key architectural contribution is a Bridge & Fusion (BAF) module that fuses visual and textual features for translation, with position embeddings that enable the model to recover correct translations even when recognition is partially wrong. The paper also introduces the STST800K dataset with paragraph-level annotations for both Chinese→English and English→Chinese translation. The strongest experimental evidence—Table 4, which shows the proposed method outperforming the best pipeline baseline (MCTIT) even when both receive perfect ground-truth OCR input—supports the claim that synchronous training and multi-modal fusion provide genuine benefits beyond simply reducing error propagation.

## Strengths

- **Controlled experiment isolating the benefit of synchronous training (Table 4)**: The paper tests its method against MCTIT using ground-truth coordinates AND ground-truth recognition as input, stripping away all OCR and detection errors. The synchronous method still outperforms the pipeline, especially on ReCTS (complex layouts), directly demonstrating that joint learning provides benefits beyond reducing OCR error propagation — it improves handling of layout and reading order.

- **Position-robust BAF module design (Section 3.4)**: The BAF module concatenates the textual feature with *two* distinct position embeddings — a 2D global position from the visual feature map and a 1D local position from the text sequence — before feeding it as query into cross-attention. The paper explicitly states that "even if the recognition result is wrong, BAF module is still able to guide cross-attention layer to collect visual information for translation according to position-related part in the query." This is a specific, well-motivated architectural innovation.

- **STST800K dataset contribution (Section 4.1)**: The paper creates a dataset with paragraph-level coordinates, matched bilingual sentence pairs, and semantic reading order for both Chinese→English and English→Chinese. The synthesis pipeline is clearly described, and real data from multiple sources are relabeled with reading order via LLM API and human proofreading. This fills a genuine gap: prior TIMT datasets lacked paragraph-level layout annotations or focused on a single translation direction.

## Weaknesses

### Major

- **Ablation study confounds two variables (Table 7)**: The "Remove BAF" condition simultaneously (i) removes the BAF module and (ii) switches from joint training to separate training of spotting and translation. This confound makes it impossible to attribute the observed performance drop to removal of BAF vs. removal of joint training. The paper claims this "proves the effectiveness of BAF module and multi-modal feature fusion," but the experimental design does not support isolating the contribution of BAF alone. A proper set of ablations would include at least "joint training without BAF" and "separate training with BAF" as additional conditions. (The "Visual Only" and "Textual Only" conditions are cleaner — they test the components of multi-modal fusion while keeping joint training fixed — so the fusion benefit is supported. The confound specifically affects the Remove BAF vs. Best comparison.)

### Minor

- **α hyperparameter value not reported (Section 3.6)**: The paper states that α "could be set as 0.1, 0.5 or 0.9" but never reports which value was actually used in the main experiments. Since this weight controls the balance between detection/recognition loss and translation loss, the actual value matters for reproducibility.

- **"SOTA" framing overstates the end-to-end comparison (Section 4.4.1)**: The paper acknowledges that "a comprehensive end-to-end model for synchronous detecting and translating remains elusive in existing methods" and therefore creates end-to-end baselines by repurposing text spotters trained for translation instead of recognition. These are not genuine TIMT competitors. The claim of "state-of-the-art" is fairly earned against pipeline methods (especially given Table 4), but the framing of beating "end-to-end baselines" inflates the apparent margin. The paper would be more precise to frame its contribution as improving over pipeline methods with a novel synchronous architecture.

### Trivial

- **Minor inconsistency in where bins B are generated (Section 3.3 vs. 3.4)**: Section 3.3 states that discrete bins B are generated in the Detection & Recognition module, while Section 3.4 says bins B are "generated in Bridge & Fusion Module." This appears to be a description error (the bins flow from D&R through BAF) and does not affect the method's correctness, but it should be corrected for clarity.

## Nice-to-Haves

- Report confidence intervals or statistical significance for the main comparisons (Table 2, 3, 4), especially given the modest size of some test sets (ReCTS, CTW1500).
- Add an analysis of how realistically the synthetic data approximates real scene text, or quantify any domain shift between synthetic and real splits.
- Report inference speed, FLOPs, or parameter count to contextualize the "small model" claim.

## Removed Points

- *Metrics inconsistency for AnyTrans comparison*: The paper explicitly justifies using BLEU-1 and wmt-22-comet-da "to keep the same configuration as AnyTrans." This is standard practice for fair comparison against a published baseline that used different metrics. The paper is not requiring cross-comparison between Table 6 and Tables 2–5.
- *VLM comparison is tangential*: This is a secondary experiment, not a core claim. The paper frames it as an additional comparison to show the advantages of specialized small-model training, which is a reasonable secondary point.
- *No confidence intervals*: Not standard for this type of evaluation in this community; single-run benchmark evaluation is the norm.
- *Sequence format not fully specified*: The method builds on UNITS, which is cited; the coordinate-text-mixed sequence format follows that prior work.
- *Synthetic data realism concern*: Speculative, and the paper uses real data (OCRMT30K, ReCTS, HierText, CTW1500) alongside synthetic data, mitigating this concern.
- *Strength Finder's claim that the ablation "cleanly separates" benefits*: This is incorrect — the ablation is confounded as noted above. This claim is dropped.
- *Generic strengths about problem importance*: Dropped per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Disentangle the ablation study by adding conditions for (a) joint training without BAF and (b) separate training with BAF. This would cleanly isolate whether the benefit comes from the BAF module, joint training, or their interaction.
2. Report the actual α value used in experiments, and ideally include a sensitivity analysis.
3. Reframe the "SOTA" claim to more precisely describe what the method achieves — e.g., "state-of-the-art among pipeline and synchronous methods for Scene TIMT" — rather than implying dominance over well-engineered end-to-end competitors that do not exist for this task.
4. Resolve the minor inconsistency about where bins B are generated (Section 3.3 vs. 3.4).

## Score and Decision

The paper makes a genuine contribution to an under-studied problem. The core idea — synchronous training with a position-aware multi-modal fusion module — is well-motivated, and the strongest experimental evidence (Table 4) convincingly shows that the approach delivers real improvements over pipeline methods. The STST800K dataset is a useful resource. The main weakness is the confounded ablation study, which prevents isolating the contribution of BAF from joint training. This is a clean-up issue rather than a fatal flaw; the method and contribution remain sound. The paper would benefit from revision but is ready for acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>