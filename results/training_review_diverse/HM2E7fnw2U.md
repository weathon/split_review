Here is the final consolidated review.

## Summary

This paper proposes a novel approach to unsupervised sequential disentanglement that mitigates mode collapse through an architectural bias rather than through mutual information loss terms or dimension reduction. The key ideas are (1) conditioning the static posterior on a single element of the sequence (e.g., \(x_1\)) rather than the full sequence, and (2) subtracting the static representation from the LSTM hidden states that produce the dynamic codes. The resulting variational model has only two hyper-parameters and achieves state-of-the-art results across video (Sprites, MUG), time series (PhysioNet, ETTh1, Air Quality), and audio (Timit) benchmarks on both generation quality and downstream prediction/classification tasks.

## Strengths

- **Clean architectural bias that directly addresses mode collapse.** The paper's core design—conditioning the static posterior on a single sample and explicitly subtracting its representation from the dynamic encoder's hidden states (Eq. 8)—is elegantly motivated and avoids the complexity of mutual information estimation or ad‑hoc dimension reduction. The ablation study (Table 4) confirms that removing the subtraction causes a ~40% accuracy drop on MUG and substantial degradation on time‑series tasks, showing that this architectural choice is directly responsible for the method's performance.

- **State-of-the-art results across multiple modalities.** On MUG facial expression generation, the method achieves 87.53% accuracy, IS = 5.598, and \(H(y|x)=0.049\), substantially outperforming prior methods including SPYL (Table 1). On PhysioNet in‑hospital mortality prediction, it achieves AUROC = 0.901 and AUPRC = 0.720, beating both raw‑feature baselines and all prior disentanglement methods (Table 2). These results are consistent across video, time series, and audio benchmarks, demonstrating the method's generality.

- **Robustness to the choice of anchor sample is experimentally validated.** The ablation in Table 4 (bottom) shows that using the first, middle, or last element as the static anchor yields nearly identical performance across datasets. This addresses an obvious practical concern about the method's dependence on a specific index.

- **Transparent failure‑case analysis.** The paper analyzes confusion patterns on MUG (Fig. 4), showing that most errors occur between visually similar expressions (fear vs. surprise) that are also confusable for human observers. This honest assessment helps characterize the method's limitations and suggests a concrete future direction (hierarchical disentanglement).

## Weaknesses

### Fatal

None.

### Major

1. **The central claim—mitigation of mode collapse—lacks a direct quantitative measure.** The paper claims its architecture prevents dynamic codes from encoding static information (the definition of mode collapse in this setting), yet the primary quantitative metrics (classification accuracy of generated videos, downstream prediction/classification) measure overall representation quality rather than the *separation* of static and dynamic factors. The t‑SNE visualizations and swap experiments provide qualitative evidence, but these are not sufficient: t‑SNE can create false separation structure, and swap experiments can succeed even under partial information leakage. A more direct test would be to freeze the dynamic encoder and measure how much static information can be decoded from \(d_{1:T}\) (e.g., train a classifier on dynamic codes to predict subject identity on MUG or ICU unit on PhysioNet). The paper does not report such a test for the proposed method or any baseline. Given that the paper's key differentiator is mitigating mode collapse *without* additional loss terms, the absence of a direct quantitative measure of that phenomenon is a significant evidential gap. The ablation study (Table 4) provides indirect support, but does not fully close this gap.

2. **The single-sample assumption is tested for index robustness but not for whether a single sample is sufficient to capture all static information.** The paper's core assumption is that the static posterior can be conditioned on a single element because static features are time-invariant. The ablation in Table 4 (bottom) tests whether the *choice* of index matters (first vs. middle vs. last), which is a useful check, but it does not test the stronger scenario where a single frame is genuinely insufficient to infer the static factor (e.g., partial occlusion in the anchor frame, high noise in the first measurement of a clinical time series, or static attributes that are only disambiguated by dynamics). The paper would be stronger with a diagnostic experiment comparing the static code learned from a single sample against one learned from the full sequence (e.g., by measuring how much static information is preserved under each condition). Without this, the claimed justification for the assumption is plausible but not fully verified, and the scope of settings where the method will succeed is unclear.

### Minor

1. **The subtraction operation's role is empirically validated but not analytically characterized.** The paper motivates subtraction as an architectural bias that "removes" static features from the LSTM hidden states, and the ablation confirms its importance. However, the analysis does not examine settings where dynamics naturally correlate with static factors (e.g., a person's gait depending on their identity, or speaking style depending on the speaker). In such cases, subtraction could suppress legitimate dynamic information, potentially degrading the dynamic representation. The paper's strong results suggest this is not a problem on the tested benchmarks, but the absence of analysis means the method may fail on datasets where statics and dynamics are more entangled. An ablation comparing subtraction against alternatives (e.g., concatenation, gating, learned residual) would help clarify whether the subtraction is a critical inductive bias or simply a working heuristic for these particular benchmarks.

2. **The evaluation does not control for the possibility that baselines are at a methodological disadvantage on time-series tasks.** The paper states that "for a fair comparison, we use the same encoder and decoder modules for all baseline methods" (Sec 5.3.2), which controls for architecture. However, several baselines (FHVAE, DSVAE, C-DSVAE, SPYL) were originally designed and tuned for video, not general time series. Their comparatively weaker performance on PhysioNet and ETTh1 may partly reflect a mismatch between their design assumptions (e.g., contrastive estimation with domain‑dependent augmentation) and the time‑series modality, rather than a fundamental superiority of the proposed method. The paper does not discuss this confound.

### Trivial

None.

## Nice-to-Haves

- A sensitivity analysis for the hyperparameter \(\alpha\) (the reconstruction weight on the anchor sample in Eq. 5) showing performance across a range of values.
- A brief discussion in the Limitations section about when the single-sample assumption is most likely to hold (e.g., when the first sample is representative of the sequence's static content) and when it is likely to fail (e.g., heavily corrupted initial measurements).

## Removed Points

- The critic's observation that "audio results (Timit) are mentioned in Sec. 5.1 but no audio results appear in the provided text" is removed per the hard rule about missing appendix content. The parser strips appendix sections from the submission text; these results exist in the original submission.
- The critic's point that "baseline results on time series... the paper does not discuss this" is downgraded from its original framing to the Minor weakness above (item 2), since the paper does state it uses the same encoder/decoder for all methods.
- The Strength Finder's general claim that the paper "addressed an important problem" is too generic to include as a standalone strength; it is subsumed by the more specific strengths listed above.

## Novel Insights

The most interesting observation from the reviews is the tension between the paper's central claim (mitigation of mode collapse) and the absence of a direct metric for that claim. The paper operationalizes mode collapse as a downstream effect (poor generation quality when the dynamic code captures everything), but the community would benefit from a standardized, direct measurement protocol—such as decoding static attributes from frozen dynamic codes—that allows different methods to be compared on the *mechanism* rather than just the *consequences* of mode collapse. The reviewer's suggestion of this metric is genuinely useful beyond this specific paper.

## Suggestions

1. **Add a direct mode‑collapse metric.** After training, freeze the dynamic encoder on a held‑out test set and train a simple classifier to predict static attributes (e.g., subject identity on MUG, ICU unit on PhysioNet) from the dynamic codes \(d_{1:T}\). Report this for the proposed method and all baselines. This would directly test whether the dynamic codes have been purged of static information.
2. **Add a diagnostic experiment comparing single‑sample vs. full‑sequence static encoding.** Train a variant where the static encoder sees the full sequence and compare the information content of the resulting static codes (e.g., by measuring classification accuracy on a static attribute). This would verify the core assumption rather than only its index‑robustness.
3. **Characterize the subtraction operation more thoroughly.** Replace subtraction with concatenation, a gated mechanism, or a learned residual in the ablation and compare both the variational lower bound and the direct mode‑collapse metric.
4. **Acknowledge the modality‑origin confound in the time‑series evaluation** and discuss whether baselines designed for video may be at a systematic disadvantage.

## Score and Decision

The paper presents a clean, well‑motivated method with strong empirical results across multiple modalities. The core weaknesses—the lack of a direct mode‑collapse metric and incomplete validation of the single‑sample assumption—are real but addressable in a revision and do not invalidate the contribution. The method is original, the experiments are otherwise rigorous, and the results are convincing on their own terms. The paper makes a solid contribution to sequential disentanglement.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>