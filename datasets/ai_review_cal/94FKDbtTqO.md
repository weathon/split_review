- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 3, 6, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary
This paper studies BERT-like pretraining for DNA sequences, focusing on the interaction between K-mer tokenization (overlapping vs. non-overlapping) and masking strategy. Through exploratory experiments, the authors observe that (1) overlapping tokenization consistently improves fine-tuning regardless of pretraining tokenization, (2) overlapping tokenization causes fast convergence and low loss during pretraining, and (3) it leads to under-trained intermediate attention layers. To address this, they propose RandomMask, a curriculum-learning approach that gradually expands the masked span during pretraining. The method is evaluated on 28 datasets across 7 downstream tasks and achieves strong results, including 65.83% MCC on epigenetic mark prediction.

## Strengths
- **Demonstration that overlapping tokenization consistently improves fine-tuning regardless of pretraining tokenization** — Table 2 shows that fine-tuning with overlapping tokenization outperforms non-overlapping on all 7 task groups for both DNABERT (average +10.25% MCC/PCC) and Nucleotide Transformer (average +10.01%). This contradicts the conventional expectation that tokenization mismatch between pretraining and fine-tuning would hurt performance, making it a genuinely useful empirical finding.
- **Empirical evidence that overlapping tokenization leads to fast convergence and undertrained intermediate layers** — Loss curves, t-SNE embeddings (Figure 2), and attention analysis (Section 3.2.2, Figure 4) provide multi-faceted evidence that overlapping tokenization causes the model to converge too quickly, with intermediate layers focusing on too few tokens.
- **Strong downstream results across a large benchmark** — RandomMask achieves SOTA on 26 out of 28 datasets spanning 7 tasks (Table 3). The 65.83% MCC on Epigenetic Marks Prediction (vs. 51.81% for DNABERT baseline and ~61.01% for HyenaDNA) is a large and practically meaningful improvement.
- **Clear algorithmic specification** — Algorithm 1 provides a reproducible step-by-step procedure for RandomMask, specifying the five-phase schedule, mask boundary expansion logic, and masking probability (P = 2.5%).

## Weaknesses

### Fatal
None.

### Major
- **Missing ablation: fixed large mask vs. progressive expansion.** The paper attributes RandomMask's gains to its curriculum-style progressive expansion. However, there is no comparison against a simple baseline that uses a fixed, larger mask span (e.g., always masking 12 contiguous tokens) from the start of pretraining. Without this control, the observed improvement could come from masking more tokens (longer spans) at all steps rather than from the curriculum schedule specifically. This gap directly weakens the paper's central causal claim about RandomMask's mechanism. *(Verified: no such ablation appears in the paper.)*
- **No statistical significance or variance reported.** No confidence intervals, standard deviations, or number of runs are reported for any downstream result (Tables 2 and 3). Many reported improvements are small (0.5–2% on some datasets), and without variance estimates it is impossible to assess whether these differences are reliable. This is especially problematic for the headline claim of "top-tier performance across 26 out of 28 datasets." *(Verified: grep for "standard deviation", "variance", "confidence" returns no matches.)*

### Minor
- **Overclaimed interpretation of overlapping tokenization's "intrinsic superiority."** The paper states (line 93) that the performance gap "stems from the intrinsic superiority of overlapping tokenization for DNA downstream tasks." However, overlapping tokenization produces roughly 6× more tokens than non-overlapping for a given sequence, giving the model more capacity, more parameters in the embedding and classification layers, and finer positional resolution. The paper does not control for these confounds. The observation that overlapping fine-tuning works better is real, but attributing it to an "intrinsic" property is not sufficiently supported.
- **No sensitivity analysis for the mask boundary schedule.** The five-phase schedule [30k, 60k, 100k, 150k, 480k] with mask increments of +2 per phase is presented without any justification or ablation. Sensitivity to these hyperparameters is important since the schedule is a core component of RandomMask. *(Verified: line 125 gives the schedule with no justification.)*
- **Dataset count inconsistency between abstract and body.** The abstract (line 5) says "achieving top-tier performance across 26 datasets spanning 7 downstream tasks," which reads as if there are 26 total datasets. The body consistently states there are 28 total datasets, with SOTA on 26 of them (lines 32, 157, 168, 177). The abstract should say "28 datasets" to match the body. *(Verified via grep.)*
- **"Identical settings" may not be optimal across different architectures.** The paper states all models are fine-tuned with "identical settings" (lines 157, 170). However, different tokenization methods (6-mer overlapping, 6-mer non-overlapping, single-nucleotide for HyenaDNA) produce very different sequence lengths (up to 6× difference). Identical batch sizes, learning rates, and optimization settings may systematically disadvantage some models. This should at least be acknowledged as a limitation.
- **Missing discussion of computational cost.** Overlapping tokenization increases the token count by approximately 6× compared to non-overlapping, dramatically increasing memory and FLOPs in both pretraining and fine-tuning. The paper does not mention this trade-off, which is relevant for practitioners deciding whether to adopt overlapping tokenization.

### Trivial
- **Abstract uses "26 datasets" where it should refer to 28 total datasets** (the body correctly reports 28 total with SOTA on 26). This is a small writing inconsistency.

## Nice-to-Haves
- **Non-overlapping pretraining + overlapping fine-tuning baseline:** Testing whether one can simply use cheaper non-overlapping pretraining (which is harder) and then fine-tune with overlapping tokenization would sharpen the evidence that the problem is specific to overlapping pretraining.
- **Comparison with SpanBERT-style masking:** A brief experiment on one or two tasks contextualizing RandomMask against per-span masking would strengthen the novelty claim.
- **Quantitative characterization of undertraining:** Computing attention entropy per layer, head diversity, or probing classifier accuracy would strengthen the qualitative t-SNE/attention analysis.

## Removed Points
*These points are flagged for removal — treat with caution if referencing them.*

1. **"DNABERT masking strategy incompletely specified"** — The paper states (line 20–21) that DNABERT masks "k consecutive tokens at the chosen point" where k = 6 (the K-mer size). The distinction with RandomMask (which starts at 6 and progressively expands to larger spans) is clear from Algorithm 1 and the surrounding text. The exact masking percentage for DNABERT is not specified, but this is a minor detail that does not affect the validity of the comparison. *(Reason: partially misunderstands what is specified.)*
2. **"Qualitative analysis is insufficient"** — The exploratory experiments (Section 3) are explicitly observational. The paper's main claims rest on the quantitative downstream results in Table 3, not on the qualitative analysis alone. *(Reason: scope creep; the analysis is appropriate for exploratory observations.)*
3. **"Limited baselines (missing LOGO, Enformer)"** — The paper compares against DNABERT, Nucleotide Transformer, and HyenaDNA, which are the three most relevant BERT-like DNA models. Missing every possible baseline is not a weakness. *(Reason: scope is clearly stated.)*

## Novel Insights
The most interesting insight to emerge from synthesizing these reviews is that the paper's central thesis — "overlapping tokenization makes pretraining too easy, so we make it harder via curriculum masking" — would be substantially strengthened by a specific ablation that neither review fully articulated: comparing RandomMask against a *fixed large mask* and also against a *randomly varying mask size* (non-curriculum). If both baselines match RandomMask's performance, the curriculum aspect is superfluous. If neither does, the case for curriculum learning is strong. This is a clean experimental design point that the reviews collectively surface but do not consolidate.

## Suggestions
1. **Add the fixed-large-mask ablation** as the primary control — compare pretraining with (a) fixed mask of 6 tokens (DNABERT's default), (b) fixed mask of 12+ tokens, (c) RandomMask (progressive), and (d) randomly varying mask size. Report downstream results for at least the 3–4 most important tasks.
2. **Report variance** — provide standard deviations over at least 3 random seeds for all main results (Tables 2 and 3).
3. **Fix the dataset count in the abstract** (28 total datasets, SOTA on 26).
4. **Acknowledge the increased sequence length and computational cost** of overlapping tokenization, and discuss how input lengths were handled during pretraining and fine-tuning.
5. **Add a brief sensitivity analysis** for the mask schedule (e.g., compare different step boundaries or growth rates on one representative task).
