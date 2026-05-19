- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 1, 3, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper identifies a practical but unaddressed problem setting: cross-domain recommendation where both source and target domains contain implicit feedback (CDRIF), rather than explicit ratings. It observes that existing CDR algorithms fail catastrophically on implicit-only data, and proposes NARF, a noise-aware reweighting framework with two stages: (1) Implicit Feedback Calibration (IFC) which weights user-item pairs by how reliably they reflect true preferences, and (2) Dynamic Noise Reduction (DNR) which discards high-loss instances during training. Experiments on two synthetic Amazon tasks and one real-world PubMed-to-DBLP task show large improvements over CDR baselines.

## Strengths

1. **First systematic treatment of CDRIF as a distinct problem.** The paper clearly articulates why implicit feedback in CDR introduces two specific challenges (absence of negative signals, confidence-vs-preference ambiguity) that existing CDR methods are not designed to handle. Table 1 demonstrates that a standard CDR algorithm (PTUPCDR) catastrophically fails on implicit data, with relative improvements of 1650%–3130% from the proposed approach — directly validating that the problem is real, severe, and previously unaddressed.

2. **Consistent and large improvements across multiple tasks and noise levels.** In Tables 2 and 3, NARF variants (especially P-NARF-IC and E-NARF-IC) achieve approximately 200% relative improvement in Recall@k and NDCG@k over the best baseline across both synthetic tasks (with varying noise levels ε=10%, 15%, 20%) and the real-world task. These gains are not marginal — they reflect fundamentally better handling of noisy implicit signals.

3. **Modular, model-agnostic framework.** NARF wraps existing CDR algorithms (EMCDR, PTUPCDR) with its IFC and DNR components. Six NARF-based variants are evaluated, showing consistent gains regardless of the underlying CDR method. Section 4 and Remark 2 explicitly describe this plug-and-play design, which is a practical advantage.

4. **Ablation and analysis confirm both components contribute.** Table 4 shows that removing either IFC or DNR degrades performance (e.g., P-NARF w/o IFC drops Recall@100 from 0.0210 to 0.0098 on the real-world task). Figure 4 shows that denoising methods prevent the performance collapse that occurs without denoising, and Figure 5 demonstrates that denoising both positive and negative pairs is the most effective strategy.

## Weaknesses

### Fatal
None.

### Major

1. **AD and CTD are never defined, making the experimental results uninterpretable at a critical level.** The paper repeatedly refers to "AD" and "CTD" as denoising methods in the method names (E-NARF-IA, E-NARF-IC), in Table captions, in Figure 4's discussion ("Both denoising methods, AD and CTD, consistently exhibit increasing performance outcomes"), and in the ablation study (Table 4). Yet neither acronym is ever expanded, described, or cited. The paper states "Eq. (10) can be realized by existing denoising algorithms" (Section 4), suggesting AD/CTD are implementations of Eq. (10), but provides no reference, description, or attribution. Since the DNR component — and specifically the comparison between NARF-IC and NARF-IA — is central to the experimental evaluation, this omission prevents the reader from understanding what was actually evaluated, comparing against the literature, or reproducing the results. The paper also promises to "introduce the proper calibration function c, Eq. (10), and the mapping function ρ at the end of this section" (Section 4, after Eq. 10), but this introduction never appears in the extracted text.

2. **The real-world dataset (PubMed→DBLP) is described only minimally.** The paper mentions collecting "two larger real-world datasets from PubMed and DBLP" for Task 3 and references "Table 5.2" for statistics, but the table is not visible in the extracted text. There is no description of what constitutes an interaction (citations? co-authorship? reads?), how data was collected or filtered, what the user/item overlap counts are, or the sparsity level. Without this information, the "real-world" evaluation cannot be properly assessed.

### Minor

3. **DNR implementation details are underspecified beyond the AD/CTD gap.** Even setting aside the undefined AD/CTD, key design choices for DNR are left unspecified: how R(T) (the retention rate) evolves over training epochs, whether the selection in Eq. (10) is per-epoch or per-iteration, and how the loss threshold is computed. These details matter for reproducibility.

4. **No confidence intervals or statistical significance reported.** All results are reported as single numbers without variance estimates (e.g., standard deviation over multiple runs). Given the synthetic tasks only have two tasks (three including the real-world one), confidence intervals would help assess the reliability of the claimed improvements.

### Trivial
None.

## Nice-to-Haves

- The paper would be strengthened by including additional baselines that incorporate established implicit-feedback handling techniques (e.g., adapting weighted matrix factorization approaches from Hu et al. (2008) to the CDR setting, or incorporating sample reweighting schemes from the single-domain implicit recommendation literature). The current baselines (EMCDR, PTUPCDR, and their LID variants) are standard CDR methods, but they do not include methods designed to handle noise in implicit feedback.
- A more detailed description of the synthetic data generation process (how label noise is introduced, whether it preserves the confidence structure of implicit feedback) would help readers assess how well the synthetic tasks model real CDRIF challenges.
- An explicit discussion of limitations and failure cases (e.g., sensitivity to the retention schedule R(T), scalability concerns) would improve the paper's scholarly depth.

## Removed Points

These points were flagged by reviewers but are removed here with justification:

- **"The baselines are too weak to support the claimed improvements; no baseline uses any established denoising method from the implicit recommendation literature."** — Partially removed. The paper compares against state-of-the-art CDR methods (EMCDR, PTUPCDR) and their implicit-adapted variants (LID). For a first work on a new problem setting, these are reasonable baselines. The criticism implicitly demands that the paper contribute new CDR baselines (adapting single-domain methods to CDR), which is itself a non-trivial task and beyond the stated scope. However, the suggestion to include weighted MF baselines is retained as a Nice-to-Have.

- **"Synthetic data generation may not capture the essential challenge of CDRIF."** — Removed. This is speculative ("may not capture") rather than a specific identified flaw. The paper includes a real-world task (Task 3) to validate findings, and Remark 1 explicitly scopes the work to initial exploration of CDRIF.

- **"The paper does not discuss limitations."** — Removed. This is an area-of-concern sweep rather than a specific identified problem. While discussing limitations would improve the paper, it is not a weakness of the experimental evidence or methodology.

- **"The inference procedure section says Algorithm 1 is mentioned but not shown (stripped by parser)."** — Removed per rule about parser-stripped content.

- **"The paper does not describe the evaluation metric computation in enough detail."** — Removed. The paper states it follows the all-ranking protocol from Wang et al. (2019) and He et al. (2020), which is standard practice.

- **"DNR is underspecified beyond the mention of AD/CTD"** and **"The paper does not describe how negatives are sampled"** — These are merged into the weaknesses above where concrete gaps exist. Pure implementation-level nitpicks about unspecified hyperparameters are removed per the hard rules.

- **Strengths removed from Strength Finder:** The strength about "dramatic and consistent performance advantage" is kept. The generic framing of strengths is tightened to avoid overclaiming. Removed the superfluous strength about the "single most important piece of evidence" being the 200%+ improvement — this is redundant with the strength already listed.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface any perspective on the paper's approach that the authors themselves do not articulate.

## Suggestions

1. **Define AD and CTD explicitly.** If they are existing algorithms, provide expansions, citations, and a brief description. If they are variants designed by the authors, describe them in full detail (as thoroughly as IFC is described) — including any hyperparameters specific to each method.
2. **Describe the real-world dataset in detail** — what constitutes an interaction in PubMed/DBLP, collection procedure, filtering criteria, overlap statistics, sparsity, and number of users/items per domain. Provide the promised statistics table.
3. **Clarify the DNR schedule** — specify how R(T) evolves over training (is it a fixed ratio? a decay schedule?), and whether mini-batch selection is applied per-epoch or per-iteration.
4. **Add error bars or confidence intervals** to at least the main results (Tables 2–3) to demonstrate that improvements are statistically reliable.
5. **Provide the full Algorithm 1** in the main text or appendix, including the specific denoising procedures.
