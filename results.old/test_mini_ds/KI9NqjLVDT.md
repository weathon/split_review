## Summary

ReMasker extends masked autoencoding (MAE) to tabular data imputation by introducing a "re-masking" strategy: during training, in addition to the naturally missing values, a random subset of observed values is also masked, and the autoencoder reconstructs this re-masked set. This forces the model to learn missingness-invariant representations. The method uses a Transformer backbone with an asymmetric encoder-decoder design and is evaluated on 12 UCI benchmark datasets against 13 baselines under MCAR, MAR, and MNAR missingness mechanisms. The core idea is simple, well-motivated, and the experimental scope is broad.

## Strengths

1. **Clean, well-motivated core idea**: The re-masking approach is a natural and elegant extension of masked autoencoding to the tabular domain, where data is already partially missing. Unlike vision MAE where masking is an artificial training device, here masking accounts for the inherent incompleteness of real tabular data. This conceptual clarity is a genuine strength.

2. **Extensive and rigorous experimental evaluation**: The paper evaluates on 12 real-world datasets from UCI (size 308–20,060, features 7–57) against 13 baselines spanning discriminative (MissForest, MICE, MIRACLE), generative (GAIN, MIWAE, Sinkhorn), and hybrid (HyperImpute) approaches under three missingness mechanisms (MCAR, MAR, MNAR) with fidelity (RMSE, WD) and utility (AUROC) metrics. This breadth is substantial and follows community-standard evaluation protocols.

3. **Systematic ablation studies isolating design choices**: Tables 1a–c and 2 (encoder depth, decoder depth, embedding width, reconstruction loss variants, backbone comparison) provide clear evidence that the design choices matter. The finding that including unmasked values in the loss helps (unlike vision MAE where it hurts) is a non-trivial insight supported by empirical evidence on two datasets.

4. **Honest discussion of limitations**: The Limitations subsection candidly acknowledges that ReMasker performs better under MCAR than MAR/MNAR due to distributional bias, and identifies the RMSE-WD tradeoff (climate dataset) where RMSE wins but WD does not. This transparency is commendable and atypical for papers at this stage.

5. **Practical guidance**: The experiments on masking ratio (Table 4), training regime (Figure 5), and ensemble integration within HyperImpute (Table 5) provide actionable advice for practitioners deploying the method.

## Weaknesses

### Fatal
None.

### Major

- **Overclaimed main result contradicts the paper's own evidence**. Section 4.1 (line 180) states: "ReMasker consistently outperforms all the baselines in terms of **both fidelity** (measured by RMSE and WD) **and utility** (measured by AUROC) **across all the datasets**." However, the Figure 1 caption (line 164) makes a weaker claim: "ReMasker outperforms all the baseline imputers **under at least one metric** across all the datasets." The Limitations section (line 412) further acknowledges that on the climate dataset, ReMasker "outperforms alternative methods in terms of RMSE but underperforms in terms of WD." The strong claim in Section 4.1 is therefore false as written — the paper's own data contradicts it. This must be corrected: the claims in the abstract, introduction, Section 4.1, and conclusion should be harmonized with the "at least one metric" phrasing or otherwise precisely qualified. This is not a minor wording issue; it misrepresents what the evidence supports.

- **Algorithm–text discrepancy on the reconstruction loss**. The paper's method section (line 109) defines the reconstruction loss as MSE on **both** the re-masked set $\mathcal{I}_\text{remask}$ **and** the unmasked set $\mathcal{I}_\text{unmask}$, and Table 4b shows that the "both" variant achieves the best results. However, Algorithm 1 (line 125) only passes the re-masked values as targets to the loss function: $\nabla \ell(d_\vartheta(\{\rvz\}), \{\tilde{\rvx}_{\rvm \wedge \overline{\rvm'}}\})$. The unmasked values' ground truth is not provided as an argument to $\ell$. If the best results rely on the "both" setting (as ablations indicate), the pseudocode does not reflect the actual training procedure. This undermines reproducibility. The paper must either update Algorithm 1 to include the unmasked loss or clarify that the algorithm is a simplified sketch and specify where the full loss specification lives.

### Minor

- **The theoretical justification (Section 5) is presented as a formal derivation but is in fact an intuitive sketch**. The argument assumes (line 382) that "it is possible to make the autoencoder lossless" and posits the existence of an optimal decoder $\vartheta^*$ that exactly reconstructs the unmasked subset — an assumption that is not justified and unlikely to hold in practice, especially early in training. The CKA experiment (Figure 4) is limited to one dataset (letter) with no non-re-masking baseline for comparison, making it hard to attribute the observed invariance specifically to re-masking. The section would be stronger if reframed as an intuitive explanation rather than a formal proof, consistent with the paper's own framing ("provide theoretical justification," "we show that").

- **Sensitivity analysis (Figure 2) is conducted on only one dataset (letter)**. The findings about dataset size, number of features, and missingness ratio would be more convincing if replicated on at least one additional dataset (e.g., california) to assess generalizability.

- **Ablation differences are small and lack statistical significance**. The gaps between configurations in the ablation study (e.g., RMSE 0.0611 vs 0.0616 across encoder depths, RMSE 0.0616 vs 0.0629 for loss variants) are extremely small. Without confidence intervals or statistical tests, these differences could fall within noise. The basis for selecting the "optimal" configuration (encoder depth 8, decoder depth 8, embedding width 64) is therefore not robustly supported.

- **No computational cost analysis**. Training and inference time for ReMasker versus baselines are not reported. For a deep Transformer model, this is relevant information for practitioners.

### Trivial

- The statement "the work is also related to that models missing data by adapting existing model architectures" (line 44) appears garbled (almost certainly a PDF parsing artifact in the extracted text — ignore).

## Nice-to-Haves

- Expand the CKA experiment (Figure 4) to additional datasets and include a comparison against a model without re-masking to isolate the effect of re-masking on representation invariance.
- Report confidence intervals or bootstrapped standard errors for the main RMSE/WD/AUROC comparisons to demonstrate statistical significance.
- Clarify how categorical features are handled (one-hot encoding? embeddings?) — this is unspecified but important for tabular data practitioners.
- Add a brief discussion or table comparing computational cost (training/inference time) of ReMasker against the most competitive baselines.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Missing recent baselines (TabDDPM, TabDiff)**: Removed per hard rule — the paper cannot be penalized for not comparing against methods that may postdate its submission, and the instruction prohibits mentioning missing related works.
- **"Grammatically garbled" sentence about related work**: This is a PDF parser artifact, not an author error.
- **Reproducibility concern about code release link not being in main text**: The abstract states code is publicly available; the link is in the (stripped) appendix. Removed per hard rules about appendix-stripped content.
- **Generic criticisms about missing appendix/proofs**: Removed per hard rules about appendix stripping.
- **Claim that the paper's response "overclaims" based on abstract vs. Section 4.1 inconsistency**: This is merged into the Major weakness above, not removed.
- **Strength Finder's claim about "consistent outperformance across diverse benchmarks"**: The strength is genuine when read with the "at least one metric" qualification; however, the unqualified version of this strength conflicts with the verified overclaiming weakness and is thus dropped. The qualified version is retained in Strengths.
- **Strength Finder's claim that CKA similarity "directly supports the paper's central theoretical claim"**: Overstated given the CKA experiment is on one dataset with no baseline. The CKA evidence is mentioned in limitations discussion but not as a core strength.

## Novel Insights

None beyond the paper's own contributions. The two reviewers largely agree on the paper's substance — the re-masking idea is sound, the evaluation is broad, the limitations are honestly discussed — and the main novel insight from the review process is that the paper's central claim in Section 4.1 overstates what the data actually shows, and the paper would benefit from aligning its claims with the more modest (and more accurate) "at least one metric" framing from the figure caption.

## Suggestions

1. **Fix the overclaiming**: Revise Section 4.1 (line 180) to match the Figure 1 caption's accurate statement ("outperforms under at least one metric across all datasets"). Also adjust the abstract, introduction, and conclusion claims to be precise about what the evidence supports. The limitations section already correctly identifies cases where ReMasker wins on RMSE but not WD — the main text should be consistent with this.

2. **Align Algorithm 1 with the text**: Either update Algorithm 1 to show the full loss computation on both re-masked and unmasked sets (if "both" was used for main experiments), or state clearly that the algorithm is a simplified sketch and refer the reader to the text for the complete training loss specification.

3. **Reframe the theoretical justification (Section 5)**: Remove the pretense of formal proof and present the derivation as an intuitive explanation or plausible reasoning for why re-masking encourages missingness-invariant representations. The CKA experiment is a reasonable empirical sanity check but should be expanded or clearly caveated as preliminary.

4. **Add statistical rigor**: Report confidence intervals (e.g., 95% bootstrapped) for the main RMSE/WD/AUROC comparisons, particularly for the ablation study where differences are small. This would greatly strengthen confidence in the findings.

## Score and Decision

**Round 1 bracket**: 5.0–6.5 (between weak anchors at ∼3 and middle anchors at 4–5.75, below strong anchors at 7.5+).

**Round 2 anchors used for narrowing**:
- Diffusion Models for Tabular Data (5.75, Reject): ReMasker has a cleaner core idea and more thorough evaluation → ReMasker is stronger.
- GITD (4.80, Reject): ReMasker is methodologically clearer with broader evaluation → ReMasker is clearly stronger.
- MCM (6.67, Accept): Similar methodology but MCM has fewer critical weaknesses (no overclaiming issue, no algorithm-text discrepancy) → ReMasker is slightly weaker.
- UniTabE (6.33, Accept): Different scope but similar evaluation caliber. UniTabE's weaknesses are comparable in severity → roughly similar.

**Final position**: The paper's core contribution is solid and the experiments are extensive, but the overclaiming issue and algorithm-text discrepancy are genuine problems that prevent unconditional acceptance. Placing it relative to the anchors: above the Rejected diffusion paper at 5.75, below the Accepted MCM paper at 6.67.

**Final Score: 6.0**

The paper has a well-motivated core idea and thorough empirical evaluation. The two main weaknesses — overclaimed results that contradict the paper's own evidence, and an algorithm-text discrepancy — are fixable but need to be addressed. With these corrections, the paper would be a solid contribution to the field.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>