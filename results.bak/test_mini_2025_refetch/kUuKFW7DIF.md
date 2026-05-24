Now I have all the information I need. Let me write the authoritative final review.

---

## Summary

This paper proposes MR-HuBERT, a self-supervised speech representation learning model that extends HuBERT to process speech at multiple temporal resolutions (20ms and 40ms) within a single hierarchical Transformer architecture. The model uses separate masked unit prediction objectives per resolution and an Hourglass-like encoder structure. Evaluated on LibriSpeech ASR (1h/10h/100h), SUPERB, and ML-SUPERB benchmarks, MR-HuBERT shows consistent improvements over HuBERT baselines, with particularly dramatic gains in low-resource ASR (40–50% relative WER reduction on 1-hour subsets for the large model). The model also achieves 9–13% MACs reduction during inference.

## Strengths

1. **Substantial low-resource ASR gains (Table 1):** The mono-large model achieves 6.44/10.94 WER on dev-clean/dev-other with only 1 hour of labeled data, versus HuBERT-large's 14.42/18.80. This ~55% relative improvement on the 1-hour setting is a clear and large-margin result that directly supports the paper's central claim.

2. **First unified multi-resolution SSL pre-training framework:** Prior work (Shi et al., 2023d) required training three separate SSL models and combining them, which is computationally expensive. MR-HuBERT integrates multi-resolution into a single pre-training stage with a single hierarchical model. This is explicitly contrasted with the prior approach and represents a genuine architectural contribution.

3. **Consistent gains across diverse benchmarks:** Beyond ASR, MR-HuBERT achieves the best SUPERB composite scores across Understanding (949.7), Enhancement (609.5), and General (864.6) categories (Tables 2–3), and the multi-base model achieves the top ML-SUPERB score (957.2/986.8) among all baselines (Table 4). This breadth demonstrates robustness beyond a single task configuration.

4. **Computational efficiency alongside quality gains:** The large MR-HuBERT reduces MACs from 1116G to 971G (13% reduction) while matching or outperforming HuBERT-large. This efficiency arises naturally from the reduced sequence length in the low-resolution path.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Slightly overstated claim about "always matching or outperforming" (Section 4.2, Table 1):** The paper states that with LM joint decoding, MR-HuBERT "still maintains a performance edge, always matching or outperforming the baseline HuBERT models." However, on the 100-hour dev-other setting with LM, HuBERT-large (WER 4.22) outperforms mono-large (WER 4.54). Without LM, the same cell also favors HuBERT-large (6.01 vs 6.04). This is a single counterexample among many positive results, but the "always" claim is technically inaccurate.

2. **Variable naming inconsistency in Section 3.3:** The description of the downsampling module says it "first rescale $\tilde{H}_4^q$ into a higher resolution," but Equation (4) and the architecture flow in Section 3.2 indicate the downsampling module's input should be $\tilde{H}_1^q$ (the output of the high-resolution encoder), not $\tilde{H}_4^q$ (which is the output of the upsampling module later in the pipeline). This appears to be a copy-paste error in the variable name. The core design is still understandable from Figure 2 and Equation (2)–(3), but the text needs correction for reproducibility.

3. **Low-resolution targets are subsampled high-resolution units, not independently clustered (Section 4.1):** The paper acknowledges that low-resolution units are obtained by skipping every second high-resolution unit, rather than running k-means at the low-resolution frame rate independently. As noted briefly in the paper and explored in Appendix B.7 (stripped), this may limit the extent to which the model captures genuinely resolution-specific structure. This is a reasonable design choice for simplicity, but its implications are underexplored in the main text.

### Trivial

- The 100-hour dev-other result (mono-large 6.04 vs HuBERT-large 6.01) also mildly contradicts the claim that MR-HuBERT "consistently surpasses" baselines in Table 1's discussion, though this is a single cell.

## Nice-to-Haves

- Reporting variance, confidence intervals, or multiple-seed runs would strengthen the evidence, especially for the base model where improvements are modest (1–2% absolute WER). This is standard practice in the field.
- Wall-clock timing measurements would complement the MACs analysis for the inference speed claim.
- Analysis showing what the low-resolution encoder actually captures differently from the high-resolution encoder would strengthen the "multi-resolution" claim beyond just reporting aggregate benchmark numbers.

## Removed Points

These points from the input reviews are removed with justification:

1. **"Uncontrolled model size / double parameter count for large model"** (Harsh Critic, Critical Issue 1): REMOVED because it is factually wrong. The critic claims MR-HuBERT-large uses 24 layers vs HuBERT-large's 12 layers. In reality, HuBERT-large (Hsu et al., 2021a) has 24 Transformer layers, and MR-HuBERT-large also has 24 Transformer layers (3 encoders × 8 layers). The paper explicitly states it "adhere[s] to the configurations used in the original HuBERT model" for both base and large (Section 4.1). Both models have the same total Transformer layers, so the comparison is not confounded by model size. This was the critic's central structural objection and it is based on a factual misunderstanding.

2. **"Internal incoherence in method description" as a structural flaw** (Harsh Critic, Critical Issue 2): The critic claims the downsampling module description is "internally incoherent" and "appears to contain factual errors." While there is a real variable naming issue (discussed in Minor Weakness #2 above — the text says $\tilde{H}_4^q$ when it should say $\tilde{H}_1^q$), calling this a "structural flaw" or fatal error is excessive. The architecture is clearly described in the figure (Figure 2) and the equations (2)–(4). The downsampling module's design (upsample → fuse → downsample, a standard Hourglass pattern) is understandable from the figure and the equation even if one variable name in the text is wrong. This is a presentation issue, not an incoherent method.

3. **"Inference speedup comparison is between 12-layer and 24-layer model"** (Harsh Critic, Critical Issue 3): Same factual error as #1. Both models have 24 Transformer layers. The MACs comparison is between models with the same layer count but different architectures. The criticism is invalid.

4. **Generic reproducibility nitpicks** (Harsh Critic, various): Demands about "undisclosed hyperparameters," "variance bars," "wall-clock time" fall into the nice-to-have category. The paper provides significant experimental detail including ablation studies (in appendix). These are not core flaws.

5. **Generic strengths** (Strength Finder): Claims about the problem being "important" or the paper having "reproducibility through open-source release" are generic and not specific evidence of quality. The concrete strengths (ASR gains, first unified framework, consistent benchmark improvements) are retained. The ablation study and open-source strengths are dropped from the strength list but are noted where relevant.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's most serious claim (model size confound) turns out to be factually wrong upon verification against the paper, and the remaining issues are minor presentation concerns. The paper's actual contribution — multi-resolution SSL pre-training in a single hierarchical model — stands largely as claimed.

## Suggestions

1. Fix the variable naming error in Section 3.3: replace $\tilde{H}_4^q$ with $\tilde{H}_1^q$ in the downsampling module description, or clarify the flow more carefully.
2. Tone down the "always" language about matching/outperforming baselines — qualify it as "in most settings" or remove the absolute claim.
3. Consider adding a brief analysis (possibly 2–3 sentences or a small figure) comparing what the low-resolution and high-resolution encoders learn, to substantiate the "multi-resolution" framing beyond benchmark numbers.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak anchors (<3.5): W4yLHZGqdp (2.75, unrelated speaker ID), 73EDGbG6mB (3.00, spoken dialogue), xJ5CF1aOOX (2.50, time series classification), QjrC77Nyu6 (2.50, ECG). All are on different topics with major flaws. Paper is clearly above this band.
- Middle anchors (3.5–7.5): UT5B7fktaw (4.75, variational inference for SSL speech — rejected for limited gains), Id2JMVSQHZ (4.80, privacy-preserving speech — rejected for missing baselines), bRa4JLPzii (6.25, multi-resolution time series — accepted poster), TtKN1TpvUu (6.25, unified ASR/TTS — accepted poster). The MR-HuBERT paper has stronger evidence than the 4.75–4.80 papers and is comparable to the 6.25 papers.
- Strong anchors (>7.5): PdaPky8MUn (8.00, long-sequence models), vf5aUZT0Fz (8.00, language model pre-training), MO5PiKHELW (7.75, MLM syntax acquisition), Yen1lGns2o (7.60, image SSL from video). These papers have deeper analytical insights or broader contributions than MR-HuBERT. Paper is below this band.

**Initial bracket: 4.5–6.5**

**Round 2 (Narrowing):**
- M8J0b9gNfG (6.20, multilingual visual speech recognition — rejected despite good scores; reviewers noted limited novelty and incremental extension of existing work). Similar profile to MR-HuBERT (extension of HuBERT family). Slightly weaker evidence than MR-HuBERT.
- OW332Wh9S5 (4.75, speech tokenizer — rejected).
- PsRL00864k (6.00, accent reduction — rejected).
- izrOLJov5y (6.75, Spectron — accepted poster). Spectron had a more novel framing (spoken QA via LLM) but MR-HuBERT has more thorough benchmark coverage.
- U42TkrEDzb (6.75, audio LLM for quality eval — accepted poster).
- 86NGO8qeWs (6.50, CompA — accepted poster).
- XRtyVELwr6 (6.25, synthetic audio contrastive learning — accepted poster).

**Final Score:** 6.0. The paper sits near the upper end of the 4.5–6.5 bracket. Its contribution is solid: the first unified multi-resolution SSL pre-training for speech, backed by comprehensive evaluations and strong empirical gains, especially in low-resource ASR. The main weakness from the harsh critic is based on a factual error (misunderstanding HuBERT-large's layer count). The remaining real issues (one variable naming error, a slightly overstated "always" claim) are minor and do not undermine the core contribution. Compared to accepted mid-6 anchors (T2V2, Spectron, Contrastive Learning from Synthetic Audio), MR-HuBERT provides comparable evidence breadth with somewhat less analytical depth but a clear and well-motivated contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>