## Summary

The paper proposes Wyckoff Transformer (WyFormer), a generative model for crystals that operates directly on Wyckoff positions—a discrete, symmetry-structured representation—rather than continuous atomic coordinates. The core idea is that the vast majority of stable crystals have unique Wyckoff representations, so generation can be reframed as an autoregressive problem over a compact token set using a Transformer. The model achieves state-of-the-art symmetry reproduction (space group distribution, novel symmetric templates) and is competitive on property prediction while using only discrete Wyckoff information. The key novelty lies in the tokenization scheme (site symmetry + enumeration rather than Wyckoff letters) and the permutation-invariant autoregressive design.

## Strengths

1. **Novel symmetry-aware tokenization that avoids data fragmentation**: By encoding Wyckoff positions as (site symmetry, enumeration) tuples rather than space-group-dependent Wyckoff letter labels, the representation is universal across all 230 space groups (Section 2.1, Figure 2b). This directly addresses a limitation of prior Wyckoff-position-based models (Zhu et al., 2024; Cao et al., 2024).

2. **State-of-the-art reproduction of space group distributions**: WyFormer achieves Space Group χ² of 0.223 and P1% of 3.24% (Table 2), dramatically lower than diffusion baselines such as DiffCSP (χ²=7.989, P1=36.57%) and FlowMM (χ²=12.423, P1=44.27%). The 180 novel unique templates (element-agnostic Wyckoff representations) far exceed DiffCSP's 76 and FlowMM's 51. This provides strong evidence that the model generates crystals with realistic symmetry.

3. **Property prediction competitive with full-structure models using only discrete Wyckoff information**: On MP-20, WyFormer achieves energy MAE of 25 meV and band gap MAE of 247 meV (Table 4)—within striking distance of the best models using full atomic coordinates. On AFLOW, it achieves the best thermal conductivity MAE (2.20) among six methods (Table 5). This directly supports the claim that Wyckoff representations alone capture substantial structure-property information.

4. **Principled permutation-invariant design**: The Transformer encoder intentionally omits positional encodings (Section 2.2), and training with shuffling augmentation (Section 2.3) achieves formal permutation invariance over the set of Wyckoff tokens—a requirement for set-structured crystal representations.

5. **Training augmentation resolves normalizer ambiguity without architectural complexity**: By randomly picking an equivalent representation at each epoch (Section 2.3), the model learns invariance to the arbitrary coset representative choice of the Euclidean normalizer. This is viable because 96% of structures have fewer than 10 variants.

6. **Efficient representation enabling full-dataset gradient computation**: The average Wyckoff representation uses only 3.0 tokens per structure (Section 2.3), allowing the entire MP-20 dataset to fit in GPU memory for full-dataset SGD training without batching—a practical advantage over coordinate-based models.

## Weaknesses

### Fatal
None.

### Major

1. **The abstract and conclusion overclaim stability performance**. The abstract states "best performance in generating novel diverse stable structures conditioned on the symmetry space group," and the conclusion claims the model "achieves a higher degree of structure diversity while maintaining stability." However, the evidence for stability superiority is mixed: on CHGNet-based metrics, WyFormer's S.U.N. (39.2%) is well below DiffCSP (57.4%) and FlowMM (49.2%) (Table 1). On DFT, WyFormer's S.U.N. (7.5%) is below DiffCSP (20.8%), and S.S.U.N. values are essentially tied (T-test p=0.8). The paper itself notes "it is likely that on a larger DFT sample it will surpass WyFormer" (line 251). The paper's honest limitations section contrasts with these overstated claims. The contribution stands firmly on symmetry control, not a stability edge, and the presentation should reflect this.

2. **Limited DFT evaluation scale**. Only ~82–96 DFT calculations per method are available, and several key baselines (CrystalFormer, WyCryst, FlowMM) were entirely omitted from DFT evaluation. This means the DFT column in Table 1 cannot establish a clear relative ordering among all methods. While resource constraints are understandable, the paper should more prominently caveat stability conclusions as provisional.

### Minor

1. **Marginal contribution of the token predictor vs. downstream pipeline is not fully isolated**. The paper presents both WyFormer (tokens → pyXtal+CHGNet) and WyFormerDiffCSP++ (tokens → DiffCSP++ coordinates). The latter often outperforms on metrics. The paper separates them in tables, which is good, but an explicit ablation measuring how much the token predictor degrades an oracle (true Wyckoff representation → same downstream pipeline) would clarify the token predictor's actual headroom.

2. **No statistical significance reported for symmetry metrics (Table 2)**. T-tests are reported for DFT stability comparisons but not for the core symmetry metrics (Space Group χ², Novel Unique Templates). Confidence intervals or significance tests would strengthen the symmetry claims against sampling noise.

3. **Property prediction aggregation choice is empirically unmotivated**. The property prediction head uses a weighted average of token outputs with WP multiplicities as weights (Section 2.2). No ablation (e.g., max pooling, CLS token, learned attention) is provided to justify this design.

4. **Unusual training protocol raises mild reproducibility concerns**. Training uses SGD without batching for 9×10⁵ epochs (Section 2.3). While explained by the compact representation, details such as learning rate schedule and wall-clock time per epoch are not reported, and the protocol deviates significantly from standard practice without ablation justification.

5. **No analysis of failure cases by space group or stoichiometry**. A breakdown of which space groups or stoichiometries WyFormer systematically generates invalid/unstable tokens would help users understand the model's reliability envelope.

### Trivial
None that warrant mention beyond the minor points above.

---

## Nice-to-Haves

- Ablation studies on key design choices: (a) positional encoding vs. none, (b) site-symmetry encoding vs. Wyckoff letter encoding, (c) spherical-harmonic enumeration descriptor vs. simpler embedding.
- Including stoichiometry as a generation condition (mentioned as future work but is a natural extension).
- A plot of S.S.U.N. vs. number of templates per model to quantify the diversity–stability tradeoff.
- Providing training details (learning rate schedule, batch size equivalent, hardware, wall-clock time) for reproducibility.

## Removed Points

These points from the inputs were removed after verification against the paper:

- **CHGNet/MP-20 overlap not mentioned**: The paper explicitly states "The MP-20 test set is a part of CHGNet training set" (Table 4 caption). The paper already addresses this. **Removed** (strawman).
- **Conflating method-level and pipeline-level results**: The paper clearly separates WyFormer and WyFormerDiffCSP++ in all tables (Tables 1, 2). The separation is present. **Removed** (factually incorrect as a criticism of the data presentation; kept as a minor point about clarifying headroom).
- **Claim about Cao et al. normalizer limitation stated without evidence**: This is standard academic discourse distinguishing approaches. Not a weakness of the current paper. **Removed**.
- **"Strengthening the Paper on Its Own Terms" items 4, 5 about plots and statistical significance**: Merged into Minor/Nice-to-Have rather than treated as standalone weaknesses.
- **Generic strengths from Strength Finder about "important problem"**: Removed as they lack concrete evidentiary anchor.

## Novel Insights

A genuinely novel insight emerges from the cross-review synthesis: the paper's honest but appropriately hedged in-text discussion (Section 4, line 251) acknowledges the stability evidence is inconclusive, yet the abstract and conclusions make an unqualified claim of superiority. This tension between the careful empirical discussion (which notes DiffCSP "will likely surpass WyFormer" with more DFT data) and the bold front-end claims is a structural issue in the paper's framing rather than a methodological flaw. The *actual* contribution—that Wyckoff tokenization enables dramatic improvements in symmetry reproduction while maintaining stability comparable to diffusion models—is well-supported and valuable. Neither reviewer fully captured this framing mismatch as the core issue.

## Suggestions

1. **Revise the abstract and conclusion** to present WyFormer as a method that *controls and reproduces symmetries* while achieving *comparable* stability to diffusion baselines, not outright superior stability. This aligns the claims with the evidence.
2. **Add an oracle ablation**: report metrics for structures generated by taking tokens from the true dataset Wyckoff representation and running the same downstream pipeline, to bound the token predictor's degradation.
3. **Report statistical significance for symmetry metrics** in Table 2 (confidence intervals or bootstrapped p-values for χ² and template counts).
4. **Release training details**: learning rate schedule, effective batch size, hardware, wall-clock time per epoch, and number of parameters.

## Score and Decision

**Calibration process**: 
- **Round 1 (Bracketing, 3 queries → score bands <3.5, 3.5–7.5, >7.5)**: Retrieved 12 anchors. The most relevant upper-middle anchor was "Space Group Constrained Crystal Generation" (DiffCSP++, avg 7.33, accepted poster) and "Crystalformer" (avg 7.25, accepted poster). Low-scoring anchors were ~3–3.25. The paper clearly sits in the middle band.
- **Round 2 (Narrowing, 2 queries → scores 4.5–7.5 and 3.0–6.0)**: Retrieved anchors including TGDMat (avg 6.5, accepted poster), Symphony (avg 6.5, accepted poster), PDDFormer (avg 5.0, withdrawn/rejected), and "Towards continuous machine learning..." (avg 4.5, rejected). Read TGDMat and Symphony in full.
- **Bracket**: Round 1 placed the paper between 3.5 and 7.5. Narrowing in Round 2 placed it above the ~4.5–5.0 anchors (which had more fundamental flaws) and below DiffCSP++ (7.33, which had cleaner stability evidence).
- **Final position**: The paper sits below DiffCSP++ (7.33) because that paper's stability evidence is stronger and claims better-calibrated. It is comparable to TGDMat (6.5) and Symphony (6.5) in overall quality—similar levels of genuine novelty combined with some evidence gaps. The paper's symmetry results are stronger than either of those anchors, but the stability overclaim and limited DFT evaluation pull it slightly down. Final score: **6.0**.

**Anchors retrieved (all rounds)**:
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| jkvZ7v4OmP (DiffCSP++) | 7.33 | 1, 2 | Stronger stability evidence, similar topic. Current paper weaker. |
| fxQiecl9HB (Crystalformer) | 7.25 | 1 | Property prediction, not generation. Not directly comparable. |
| AkBrb7yQ0G (TGDMat) | 6.50 | 1, 2 | Comparable quality; less novelty but stronger stability eval. |
| MIEnYtlGyv (Symphony) | 6.50 | 2 | Comparable; molecule generation, different domain. |
| ewjN1MAnJi (PDDFormer) | 5.00 | 1, 2 | Withdrawn/rejected; property prediction only. Current paper stronger. |
| NVKwjCIAAX (SMOACS) | 4.75 | 2 | Rejected; more fundamental issues. Current paper stronger. |
| rcdR97P2Mp (Continuous ML) | 4.50 | 2 | Rejected; different topic (invariant theory). |
| zUDbPgskDS (CrysToGraph) | 3.25 | 1, 2 | Rejected; serious reproducibility issues. Current paper much stronger. |
| g0fHn95m3D (Text-To-Energy) | 3.25 | 1 | Rejected; fundamentally different domain. |
| rEQ8OiBxbZ (LEGO) | 3.00 | 1 | Rejected; molecular pretraining, different domain. |
| m9zWBn1Y2j (PsiDiff) | 3.00 | 1 | Rejected; molecular conformations. |
| 0VBsoluxR2 (MOFDiff) | 8.00 | 1 | Stronger paper overall; more comprehensive evaluation. |
| KSLkFYHlYg (ShEPhERD) | 8.00 | 1 | Drug design; different domain. |
| EO8xpnW7aX (SymmetricDiffusers) | 8.00 | 1 | Discrete diffusion on symmetric groups; different domain. |

**Decision rationale**: The paper's core contribution—operating a Transformer on Wyckoff positions for symmetry-controlled crystal generation—is novel, well-motivated, and convincingly demonstrated for symmetry reproduction. The primary weakness is overclaiming on stability, which is fixable with revisions. No fatal flaws were identified. The paper merits acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>