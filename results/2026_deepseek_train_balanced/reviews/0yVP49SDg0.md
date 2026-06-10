## Summary

This paper proposes Mamba-HMIL, a hierarchical multiple instance learning method for WSI classification combining three components: (1) hierarchical feature extraction at 10× and 20× magnifications, (2) a Mamba (state space model) block with mixture-of-experts (MoE) for sequence modeling, and (3) an adaptive selection (AS) module to filter disease-negative patches. The method is evaluated on two subtype classification tasks (TCGA-NSCLC, TCGA-RCC) and two survival prediction tasks (TCGA-BRCA and either TCGA-BLCA or TCGA-LUSC — the paper is inconsistent) against several baselines including ABMIL, CLAM, TransMIL, and Mamba-MIL, achieving top results with small margins.

## Strengths

1. **Hierarchical feature extraction yields substantial, well-attributed gains**: The ablation (Table 3, Section 4.4) shows that using both 10× and 20× magnifications improves ACC by 2.7% and AUC by 4.8% on TCGA-NSCLC, and ACC by 3.4% on TCGA-RCC over single-scale features. These are non-trivial absolute improvements that cleanly isolate the benefit of multi-scale features, which prior MIL methods (ABMIL, CLAM, TransMIL, DSMIL) do not incorporate.

2. **Top results across multiple datasets and tasks**: Mamba-HMIL outperforms all 8 competing methods including Mamba-MIL (Yang et al., 2024) on both TCGA-NSCLC and TCGA-RCC classification (Table 1), and achieves competitive or best C-Index on survival prediction (Table 2). The evaluation spans 4 distinct TCGA datasets covering two clinically relevant tasks.

3. **Adaptive selection demonstrably beats fixed token selection**: The AS module with P=0.8 achieves ACC 0.916 and AUC 0.983 on TCGA-RCC, improving 1.7% ACC over CLAM's fixed Top-K baseline (Table 5, Section 4.4). This directly addresses a known limitation — that the number of disease-positive patches varies per WSI — with quantitative evidence.

4. **Systematic MoE variant and expert-count analysis**: The paper evaluates four MoE variants (basic MoE, STMoE, PEER, Sinkhorn) and justifies the choice of STMoE with 16 experts based on both accuracy and computational trade-offs, including sensitivity analysis showing 16 experts outperforming 32 (Section 4.4).

## Weaknesses

### Major

1. **Dataset inconsistency for survival prediction**: The abstract (line 4), Table 2 caption (line 84), and results discussion (line 139) state survival evaluation on *TCGA-BRCA and TCGA-BLCA*. However, Section 4.2 (line 130) states *"TCGA-BRCA (1022 cases) and TCGA-LUSC (373 cases) are used for the evaluation of survival prediction."* TCGA-BLCA (bladder urothelial carcinoma) and TCGA-LUSC (lung squamous cell carcinoma) are entirely different cancer sites with different tissue types, clinical behaviors, and sample sizes. The reader cannot determine which dataset produced the survival results in Table 2. If TCGA-LUSC was used, it also overlaps with the subtype-classification NSCLC task (which already includes TCGA-LUSC within it), raising concerns about data reuse. This ambiguity must be resolved before the survival prediction claims can be assessed.

2. **Method description is substantially underspecified for a methods paper**: Multiple critical components are described too vaguely for reproduction.
   - *Sequence generation* (Figure 2 caption): *"By combining these embeddings in various ways, we generate different sequences Seq 1, Seq 2, ..., Seq N."* The paper never specifies what "various ways" means — permutations, spatial ordering, random shuffling? This is the central input to the Mamba block.
   - *Hierarchical fusion* (Figure 2 caption): The 10× and 20× features *"undergo hierarchical fusion processing to merge multiscale features"* — no equation, algorithm, or description of this operation is provided anywhere in the paper.
   - *SSM branches* (Section 3.3, line 78): The sentence describing the forward, reverse, and nonlinear flows is truncated mid-sentence (*"The forward"*) with no explanation of how these branches relate to the WSI task.
   - *Undefined abbreviation*: Line 120 states *"optimize SSM+SS training"* where "SS" is never defined.

### Minor

3. **Small margins on main results without variance estimates**: The improvement over the best baseline on the two classification tasks is 0.9% ACC / 0.5% AUC (NSCLC) and 0.6% ACC / 0.4% AUC (RCC) — reported without confidence intervals, standard deviations, or significance tests. These margins are within the range that random seed variation can produce, making the "state of the art" claim unsubstantiated without variance information. (Ablation results do report std. dev. for some settings, e.g., line 162-163, but the main comparison does not.)

4. **Terminology error in ablation (line 150)**: The ablation section refers to *"two Self-Supervised Masking (SSM) blocks"* when clearly discussing the Mamba/state space model block (defined as "State Space Model" in Section 3.3). While the intended meaning is discernible from context, this is a substantive editing error that undermines confidence in manuscript polish.

5. **Ambiguous architecture selection protocol** (Section 4.4, line 148): *"We use one fold of the dataset to determine the optimal number of blocks for our model."* The paper does not clarify whether this fold is a held-out validation set or whether the same data later appears in the reported evaluation, introducing potential data leakage.

6. **Overstated conclusions**: The conclusion claims Mamba-HMIL *"can dramatically improve the performance of WSI-level classification"* (line 180), which is inconsistent with the 0.4–0.9% margins on the main results vs. the strongest baselines.

7. **Survival prediction endpoint unspecified**: The paper never defines whether the endpoint is overall survival, disease-specific survival, or progression-free interval — different endpoints have different clinical interpretations and censoring patterns.

### Trivial

8. **5× magnification patches are extracted (line 124) but never used** — the method only uses 10× and 20×, with no justification for discarding 5×.
9. **Inconsistent ablation baselines**: The AS ablation uses CLAM as baseline, while the Mamba block ablation uses ABMIL, making cross-component contribution comparison difficult.

## Nice-to-Haves

- Report computational cost (inference time, memory, parameter counts) for the full model vs. baselines. The MoE with 16 experts and multi-scale encoding add overhead that should be quantified.
- The paper could more explicitly discuss architectural differences from Mamba-MIL (Yang et al., 2024), which is the most directly related prior work, beyond listing the additional components.

## Removed Points

*The following points from the input reviews were removed as noise, speculation, or violations of filtering rules:*

- **Criticism about "scales not corresponding to clinical practice"**: The paper's clinical motivation is reasonable and the HFE ablation empirically validates multi-scale benefit; demanding exact correspondence with pathologist practice is scope creep.
- **Criticism about multi-modality comparison being unfair**: The paper explicitly distinguishes uni-modal vs. multi-modal comparisons (line 139: *"when compared to MIL-based methods that rely solely on pathological image data, Mamba-HMIL outperforms... when compared to multi-modality methods... competitive results"*), which is adequate contextualization.
- **Claim that Mamba-MIL is excluded from comparison**: Mamba-MIL is included as a baseline in Table 1 (line 137 lists it among 8 compared methods).
- **Claim that SSM terminology error suggests fundamental misunderstanding**: The paper correctly describes Mamba/SSM in Section 3.3; the "Self-Supervised Masking" phrasing is an editing error in one sentence, not evidence of conceptual confusion.
- **Generic formatting/presentation nitpicks** and speculation about "what if the normalization were X."

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine dataset inconsistency and method underspecification that are not resolved by the paper itself.

## Suggestions

1. **Resolve the dataset inconsistency**: Confirm whether survival evaluation used TCGA-BLCA or TCGA-LUSC and correct all inconsistent occurrences throughout the paper.
2. **Fully specify the method**: Provide explicit algorithms or equations for sequence generation and hierarchical fusion; complete the truncated SSM section; define all abbreviations including "SS."
3. **Report variance on all main results**: Add standard deviations, confidence intervals, or statistical significance tests to Tables 1 and 2.
4. **Clarify the architecture selection protocol**: Specify which fold is used for hyperparameter selection and confirm test data independence.
5. **Tone down claims**: Replace "dramatically improve" with wording proportional to the observed margins.
6. **Either use or justify discarding the 5× magnification data** collected during preprocessing.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>