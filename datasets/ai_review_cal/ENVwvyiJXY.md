- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary
This paper proposes a new task, Dataset Distillation for Domain Generalization (DD for DG), studying how models trained on distilled synthetic datasets generalize to unseen domains. The authors evaluate two natural baselines (DD across domains and DD per domain) and identify a trade-off between performance and efficiency. They then introduce a method that constructs a single synthetic dataset with a domain transfer module (Domain Transfer Learning / Domain Style Mixing), drawing a formal connection between dataset distillation losses and style transfer losses. Experiments on DomainBed benchmarks show the method outperforms across-domains baselines.

---

## Strengths

- **Formal connection between DD loss and style transfer loss (Sec. 3.2).** The paper explicitly derives the equivalence between batch-norm statistic matching used in SRe²L and the channel-wise mean/variance style matching used in style transfer (Dumoulin et al., 2017). This provides a principled lens for applying style-transfer techniques to dataset distillation, and it is supported by equations showing how the running mean/variance of synthetic and original datasets correspond to style representations.

- **Ablation study disentangles contributions of each component (Table 4, Sec. 4.4).** The ablation compares style loss, normalized style loss, normalized average style loss, the full DTL process, and DSM. The row-by-row breakdown allows isolating the effect of each design choice. The results show that the normalized style loss per domain (row 2) is better than raw style loss (row 1), that the DTL process (row 4) restores performance from the averaged-style baseline (row 3), and that DSM (row 5) provides a marginal additional gain. This decomposition is informative and supports the method's design rationale.

- **Problem framing is well-motivated and the task is clearly defined (Sec. 3.1).** The paper systematically identifies that existing DD methods have not been evaluated for cross-domain robustness, and the two-baseline analysis (DD across domains vs. DD per domain) cleanly exposes the trade-off. The formal definition of DD for DG in Eq. (4) and the extension from standard DD are precise.

---

## Weaknesses

### Fatal
None.

### Major

1. **Overclaim relative to comparison transparency.** The paper states "our approach consistently outperforms the SRe²L and G-VBSM baselines by a large margin" (line 146) and "outperforms state-of-the-art DD methods" (line 25). However, Table 2 — the paper's main results table — does not explicitly state whether the baselines use the *across-domains* or *per-domain* configuration. The experimental setup (line 139) implies baselines use the across-domains configuration (BN frozen unless per-domain). Table 1 shows that per-domain baselines achieve higher accuracy than the proposed method in some settings (the critic reports e.g., per-domain SRe²L at 56.02% vs. the proposed method at 54.37% on R-18). Because the per-domain approach stores multiple synthetic datasets (one per domain), it is not a strictly apples-to-apples comparison, and the across-domains comparison is the correct primary benchmark. However, the paper's broad "outperforming" claims should be qualified to specify the comparison setting, and the per-domain numbers should be co-located in Table 2 for the reader to assess the trade-off directly. As written, the claims outrun the evidence.

2. **Efficiency advantage is stated but never quantified.** The entire motivation for the method rests on the trade-off between performance and efficiency: DD per domain performs better but costs more in storage and training. The proposed method is supposed to approximate per-domain performance with a single dataset. Yet no storage costs (MB per synthetic dataset), training time, or compute comparisons are reported anywhere. Without these numbers, the efficiency argument is purely rhetorical. The paper would be substantially stronger by reporting, e.g., the total synthetic dataset size for across-domains vs. per-domain vs. the proposed method, and training time for each.

### Minor

1. **The DTL loss function $\mathcal{L}_{\mathrm{DTL}}$ is never explicitly defined.** Algorithm 1 references $\mathcal{L}_{\mathrm{DTL}}(S_{k,m},\psi)$ but the paper never writes an equation for this loss. From the surrounding text (line 98 and Sec. 3.2), one can infer it combines the averaged-domain style matching loss (MSE on channel means/variances) and cross-entropy, but a formal equation would remove ambiguity. This is an addressable gap.

2. **Domain transfer network $\psi$ architecture is underspecified.** The paper mentions a "style transfer network" with "conditional instance normalization layers" (Figure 1 caption) but does not specify its depth, architecture family (e.g., small CNN following Dumoulin et al. 2017), capacity, or initialization. While the general approach is clear, reproducibility would benefit from a brief architectural summary.

3. **Ablation study (Table 4) is missing the IPC setting.** The text states the models (R-18/50) but does not state the IPC (images-per-class) used for the ablation. The reader cannot assess whether the ablation results correspond to IPC 10, 50, or 200. This should be stated explicitly, either in the caption or the surrounding text.

4. **Minor typos and inconsistencies.** (a) Line 24: "Domain Transfer Learning (DSM)" — should be "DTL". (b) Table 4 caption: "DST" — likely a typo for "DTL". These don't affect scientific validity but suggest the paper could benefit from a final proofread.

### Trivial
None.

---

## Nice-to-Haves

- **Add per-domain baseline results to Table 2.** Including per-domain numbers (even as a separate row or note) would let the reader directly see how the proposed method compares against both single-dataset and multi-dataset baselines.
- **Report standard deviations or multiple seeds.** The results appear to be single-run; given the noise in DG evaluation, error bars would strengthen confidence.
- **Include cross-architecture results for baseline methods in Table 3.** Currently only the proposed method's cross-architecture numbers are shown, making it hard to assess whether the method is better or worse at cross-architecture transfer relative to baselines.

---

## Removed Points

These points were flagged by reviewers but removed after verification against the paper:

- **"Method is under-specified to the point of non-reproducibility"** — Too harsh. Algorithm 1, Figure 1, and Sec. 3.2–3.4 together give a clear conceptual description. While more detail on $\psi$'s architecture and the exact loss equation would improve reproducibility, the core mechanism is understandable and the paper provides training hyperparameters (learning rate, batch size, optimizer, epochs). Removing citation of "non-reproducibility" as a fatal issue.

- **"The per-domain baseline is the natural upper bound" and comparison gap is a structural flaw** — The per-domain approach stores multiple datasets, so it is not a like-for-like baseline. The fair comparison is against across-domains (same data budget). The paper's motivation is to approximate per-domain performance with a single dataset. The issue is one of presentation clarity, not a fatal methodological flaw. Demoted to Major weakness #1 above.

- **"Cross-architecture results only for Ours, so not specific to the proposed method"** — Generic DD methods also pursue cross-architecture generalization; however, showing that the distilled dataset transfers across architectures is still useful supporting evidence. The strength is genuine but the paper does not claim cross-architecture superiority.

- **"The connection between DD and style transfer is not entirely novel"** — Even if previously hinted at in the literature, the paper formalizes the connection explicitly with equations (Sec. 3.2) and builds a method on top of it, which is a valid contribution.

- **"DSM is a straightforward application"** — The application of mixing to the learned style parameters in the transfer network, as opposed to mixing feature statistics in the classifier, is a specific design choice that the paper tests in ablation.

- **Missing related works, missing appendix, typo/formatting criticisms** — Removed per hard rules.

---

## Novel Insights
None beyond the paper's own contributions. The two reviews do not surface a perspective that the paper itself does not already articulate or imply. The core tension (single-dataset vs. multi-dataset distillation for domain generalization) is present in the paper's own framing; the reviewers highlight it as a weakness, which the paper could address with better presentation rather than missing it entirely.

---

## Suggestions

1. **Clarify the comparison explicitly in Table 2.** Add a footnote or column specifying that baselines use the across-domains configuration, and include per-domain results for direct reference.
2. **Quantify the efficiency gain.** Report storage size (MB) of the synthetic dataset for across-domains vs. per-domain vs. the proposed method, and optionally training time. This grounds the central trade-off claim.
3. **Write the DTL loss function explicitly.** Add an equation combining the averaged-domain style loss (MSE on BN statistics) with cross-entropy, and specify the role of $\mathcal{L}_{\mathrm{DTL}}$ in Algorithm 1.
4. **State the IPC setting in the ablation study** (Table 4).
5. **Fix minor typos:** "Domain Transfer Learning (DSM)" → "DTL" in line 24; "DST" → "DTL" in Table 4 caption.

---
