- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6
Now I have verified the paper claims. Let me compile the authoritative review.

## Summary

The paper addresses data scarcity in protein inter-chain contact prediction by introducing Split and Merge Proxy (SMP), a pre-training method that converts abundant monomer data into pseudo-multimer training examples by splitting a single chain into two fragments and training the model to predict their intra-chain contacts as if they were inter-chain. The pre-trained model is then fine-tuned on real multimer data. Experiments on DIPS-Plus, CASP-CAPRI, and DB5 show SMP improves over the GeoTrans baseline by 11.40%, 2.97%, and ~1.5× respectively, and generalizes to protein docking and interaction site prediction.

## Strengths

1. **Novel and practical pre-training paradigm.** The core idea of splitting monomers into pseudo-multimers and aligning the proxy task with the final contact-prediction objective is elegant and technically well-motivated. The paper is, to my knowledge, the first to use monomer data in this way for pre-training inter-chain contact prediction. (Section 3.2, Figure 2)

2. **Consistent improvements across multiple benchmarks.** SMP combined with GeoTrans achieves clear gains on DIPS-Plus (+11.40% P@L/10), CASP-CAPRI (+2.97% P@L/10), and roughly 1.5× the performance of GeoTrans on the difficult unbounded DB5 benchmark. Improvements hold for both homodimers and heterodimers. (Tables 1, 2, 3)

3. **Generalizability to other multimer-related tasks.** SMP pre-training improves results on protein interaction site prediction (GraphBind, GraphPPIS) and protein docking (EQUIDOCK) without requiring any framework modification, demonstrating the method's potential as a general pre-training strategy. (Section 4.6, Tables 7, 8)

4. **Informative ablation studies.** The paper compares SMP against alternative pre-training paradigms (mask modeling, PHD) and shows SMP outperforms them by clear margins (e.g., 5.89% on P@L/2). Partial pre-training experiments confirm monotonic improvement with more monomer data. (Table 4, Table 5)

## Weaknesses

### Fatal
None.

### Major

1. **Potential data leakage via sequence homology is not addressed.** The paper asserts no overlap between pre-training and test data because "the ID numbers of monomer and multimer in PDB being different" (line 117). However, PDB IDs identify *structures*, not sequences. A chain that appears in a test complex could have been deposited earlier as an independent monomer under a different PDB ID. The paper reports no sequence-level redundancy reduction (e.g., clustering at any sequence identity threshold) between pre-training monomers and test-set chains. If pre-training data inadvertently includes chains homologous to test complex chains, the model may have seen the structure of one side of the interface, inflating performance — particularly concerning for the dramatic gains on DB5 (unbound, where interfaces are diverse). The authors should either demonstrate minimal sequence overlap or report results on a held-out non-homologous subset.

### Minor

2. **Overstated claim of "no task gap."** The paper repeatedly states there is "no task gap" between SMP and the target task because both are contact prediction (lines 19, 86). In reality, SMP involves predicting *intra-*chain contacts (dense contacts within a single folded chain after splitting) while the final task involves *inter-*chain contacts (sparse contacts between independently folded chains at an interface). These are different distributions — a point implicitly acknowledged by the fact that zero-shot SMP (line 180, Table 5) is far below SOTA, requiring fine-tuning. The paper would be stronger by honestly characterizing this distributional shift and explaining *why* intra-chain pre-training still benefits inter-chain prediction (e.g., learning residue-pair representations). This is a framing issue, not a technical flaw.

3. **Lack of statistical significance reporting.** Test sets are small: 32 (DIPS-Plus), 19 (CASP-CAPRI), and 55 (DB5) complexes. The paper reports no standard deviations, confidence intervals, or results from multiple independent runs. Single-run percentage differences on sets this small could be within noise. While single-run evaluation is standard practice in many structural biology benchmarks, a paper claiming new SOTA would benefit substantially from reporting variance over at least 3 runs or bootstrapped confidence intervals.

4. **Data efficiency claim lacks proper control.** The partial fine-tuning experiment (Table 5) compares SMP-pretrained models trained on (e.g.) 1/4 of real data against GeoTrans trained on full real data, concluding "comparable results … only with 1/4 training data." This conflates the benefit of pre-training with the benefit of additional data. A cleaner demonstration would compare SMP-pretrained and non-pretrained (GeoTrans) models at *equivalent* data volumes (1/4, 1/2, full). Without this control, the claim that SMP "reduces dependence on real data" is supported but not as rigorously as it could be.

### Trivial

None.

## Nice-to-Haves

- **Analyze what the pre-trained model learns.** An attention or feature analysis showing that SMP captures interface-relevant patterns (e.g., surface complementarity, conserved patches) shared between intra- and inter-chain contacts would strengthen the motivation and help explain the method's success.
- **Discuss failure cases.** For instance, why does SMP improve homodimer performance more than heterodimer performance on DIPS-Plus (+14.81% vs +2.44% P@L/10)? A brief analysis would help set expectations.
- **Report training cost** (GPU hours) so practitioners can assess the trade-off.
- **Multiple cut points per monomer** could be explored to create more diverse pseudo-multimers, though this may be computationally expensive.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Criticism that zero-fine-tune results are "worse than BIPSPI"** (from Harsh Critic #1). Removed: factually incorrect. The paper explicitly states (line 180) "SMP surpasses the traditional method BIPSPI without any fine-tuning."
- **"The model has effectively seen the structure of one side of the interface"** — this is a speculative extrapolation of the data leakage concern. The concern about sequence-level homology is valid (kept as Major #1), but the claim that leakage *has* occurred is unverified.
- **Criticism that MSA quality on fragments may degrade pre-training.** Removed: speculative with no evidence presented that this actually harms results. The paper's empirical results suggest whatever degradation exists does not prevent effective transfer.
- **Suggestion of non-contiguous splits / multiple cuts.** Removed: this is a design variant, not a flaw in the current design.
- **Generic "Strengthening the Paper on Its Own Terms" section.** Moved: these are suggested future analyses, not weaknesses of the current work.

## Novel Insights

None beyond the paper's own contributions. The novel observation is that splitting monomers into two contiguous fragments and training on intra-chain contacts (treated as pseudo inter-chain contacts) transfers effectively to real inter-chain contact prediction. This is non-trivial because the two contact types differ in distribution (dense vs sparse, intra-domain vs inter-interface), yet the pre-training consistently improves a strong baseline. The finding that SMP also aids docking and interaction site prediction suggests the learned residue-pair representations capture broadly useful structural information, not just task-specific contact patterns.

## Suggestions

1. **Address the data leakage concern directly:** Perform sequence-level clustering (e.g., at 30% sequence identity) between the set of all chains in pre-training monomers and all chains in the test sets (DIPS-Plus test, CASP-CAPRI, DB5). Report the fraction of test chains with a homologous monomer in pre-training. If the fraction is small, state this explicitly. If it is non-trivial, rerun experiments on a clean non-homologous split.
2. **Add variance reporting:** Run the main experiments (Tables 1–3) with at least 3 different random seeds and report means and standard deviations.
3. **Tone down the "no task gap" framing** and instead describe the relationship as "aligned objective with a distributional shift that fine-tuning resolves." This is more accurate and does not weaken the contribution.
4. **Add the missing control for data efficiency:** Fine-tune a non-pretrained GeoTrans on 1/4, 1/3, 1/2 of the real data and show that SMP-pretrained outperforms it at each volume. This turns an already suggestive table into a rigorous one.
