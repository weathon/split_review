Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper proposes FedDFQ, a personalized federated learning method that uses a parameter-free Data Identity Extraction Module (DIEM) to generate metric proxies quantifying data heterogeneity across clients. These proxies are intended to re-weight global parameter aggregation (FELPA) and to regularize personalized classifiers via an Automatic Gradient Accumulation Module (AGAM). The paper claims state-of-the-art performance on CIFAR-10 and FashionMNIST under non-IID settings with 50 and 100 clients.

## Strengths

- **Parameter-free data heterogeneity quantification via DIEM.** Unlike existing methods that rely on learnable feature extractors (e.g., FedRep, FedPAC) which can introduce training-induced biases, DIEM uses a no-parameter algorithm of channel-wise and spatial averaging to generate data identifiers. This design avoids bias from model initialization and training while still capturing local data distribution characteristics (Section 3.1). This is the paper's most distinctive idea.

- **Scalability advantage with increasing client count.** Figure 3 shows that the accuracy gap between FedDFQ and local-only training grows as the number of clients increases from 50 to 100, suggesting the method leverages complementary information from a larger pool of heterogeneous clients.

- **Robustness to diverse non-IID distribution types.** The paper evaluates FedDFQ under three different heterogeneous distribution setups (Dirichlet, pathological, and unbalanced coverage) and reports consistent outperformance over baselines (Figure 4), demonstrating practical robustness without per-distribution tuning.

## Weaknesses

### Fatal

- **Two of the three claimed core modules (FELPA and AGAM) are not algorithmically described.** Section 3.3.1 ("Global parameters aggregation") cuts off mid-sentence after "Here is the introduction to the algorithm process:" and jumps directly to Section 4 — no aggregation formula, no weighting rule, no procedure is given. The AGAM module, listed as a main contribution in the abstract and introduction, receives **no equations, no algorithmic description, and no dedicated subsection at all**. It is only mentioned at a high level (e.g., "regularizes personalized classification layers with re-balanced gradients") with no specification of how this regularization works. Without these descriptions, the paper's central claimed contribution — a novel method for weighted aggregation and gradient regularization — cannot be evaluated for correctness, novelty, or reproducibility. This is not a minor omission; it is the absence of the method itself.

### Major

- **The theoretical justification for metric proxies is insufficient and the claim is overstated.** Section 3.2 attempts to prove that the similarity of DIEM outputs (S(𝐱ᵢ, 𝐱ⱼ)) is a reliable proxy for the similarity of class predictions (S(𝐳ᵢ, 𝐳ⱼ)). The argument invokes an unspecified "matrix A" via "the theory of matrix" (line 89), then expands the cosine similarity of a linear function 𝐳 = 𝐖ᵀ𝐱 + 𝐛 into an expression involving 𝐱, 𝐖, and 𝐛 (Eq. 6). This is algebra — it expresses S(𝐳ᵢ, 𝐳ⱼ) in terms of 𝐱, 𝐖, 𝐛, but does **not** show that S(𝐱ᵢ, 𝐱ⱼ) is a reliable or information-preserving proxy for S(𝐳ᵢ, 𝐳ⱼ) under realistic conditions. The special case 𝐖=𝐈, 𝐛=𝟎 (Appendix A.1) is trivial and irrelevant to the actual setting. The empirical Pearson correlation of r=0.728 (Table 3) suggests a moderate correlation, but the paper does not discuss how proxy errors affect the downstream tasks (weighted aggregation and gradient regularization) or why this correlation level is sufficient. The claim "We theoretically prove that the similarity of data identifiers can represent the data heterogeneity" (line 107) is substantially overstated relative to what is actually shown.

### Minor

- **The DIEM is only weakly validated as a meaningful descriptor for federated learning.** The DIEM reduces each image to a vector of length W (e.g., 32 for CIFAR-10) by averaging channels then averaging rows. The paper offers no analysis — beyond the single Pearson correlation against prediction similarity — of whether such a coarse descriptor captures label distribution, domain shift, or other forms of heterogeneity that matter for FL. Synthetic examples, t-SNE visualizations, or ablation on the descriptor dimensionality would strengthen the case but are absent.

- **FELPA is never defined as an acronym.** The term "FELPA" appears in the ablation study (Section 4.3) and conclusion (Section 5) without ever being spelled out. From context it refers to the weighted global parameter aggregation, but the paper should state this explicitly.

- **Limited evaluation scope.** The experiments only use CIFAR-10 and FashionMNIST. Many recent personalized FL papers additionally evaluate on CIFAR-100, TinyImageNet, or domain-realignment benchmarks. While this is not a fatal flaw, the claim of general applicability would be strengthened by broader evaluation.

### Trivial

- The conclusion (Section 5) refers to "IDEM" rather than "DIEM," an inconsistency worth fixing.

## Nice-to-Haves

- A visualization (e.g., t-SNE or heatmap of pairwise similarities) showing that DIEM vectors from clients with similar label distributions cluster together would ground the entire proxy mechanism.
- Adding CIFAR-100 or a federated NLP task would broaden the empirical contribution.

## Removed Points

The following points from the reviews were removed for the reasons stated:

- **"Tables 1 and 2 are placeholder images so results cannot be verified"** — The tables are embedded as images in the original submission (a formatting choice, not a parser error). The images are the tables, not placeholders. However, since the tables are image-based, the specific numbers are not extractable here. This point is removed as it conflates a format preference with a substantive criticism of the author's content.
- **Strength: "Plug-and-play AGAM design"** — This strength claims AGAM is a usable plug-and-play component, but this directly conflicts with the verified fatal weakness that AGAM is not algorithmically described. Per instructions, when strength and verified weakness conflict, the weakness prevails.
- **Strength: "Theoretical and empirical validation for metric proxies"** — This describes the derivation and Pearson correlation as strengths, but the verified Major weakness establishes this theory is insufficient and the claim is overstated. The empirical correlation is genuine but the strength as framed ("principled basis") conflicts with the finding that the theory is incomplete. Relegated here; the empirical part (r=0.728) is acknowledged in the Weaknesses section.
- **Criticism about missing related works differentiation** — Partially addressed by the paper's discussion of limitations of existing methods in Sections 2.1–2.2; the differentiation is present, if not sharp. Removed as insufficiently specific.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Complete the algorithmic specification.** Provide the full aggregation rule for FELPA (how metric proxies produce per-client weights, the exact weighted averaging formula) and a full algorithmic description of AGAM (what gradients are modified, how re-balancing works, the update rule). Without these, the paper is a proposal sketch, not a complete research contribution.
2. **Replace the vague matrix argument** with a clear statement of conditions under which S(𝐱ᵢ, 𝐱ⱼ) approximates S(𝐳ᵢ, 𝐳ⱼ), or replace the theoretical claim with an honest empirical characterization of the proxy's limitations.
3. **Validate DIEM directly** by showing that the distance/similarity between DIEM vectors correlates with known ground-truth heterogeneity (e.g., label skew measured by the Dirichlet parameter α).
4. **Define all acronyms** (FELPA) at first use.

## Score and Decision

**Originality:** The core idea — parameter-free data identifiers for quantifying FL heterogeneity — is moderately novel. However, the novelty cannot be properly assessed without knowing how the identifiers are actually used in aggregation and gradient regularization.

**Importance:** Heterogeneity-aware personalized FL is an important and active area.

**Claims support:** The paper's central claims are not supported because the methods that would support them (FELPA, AGAM) are not described. The experimental results are reported but cannot be connected to a specific, replicable algorithm.

**Soundness:** Cannot be evaluated due to missing method descriptions.

**Clarity:** The DIEM and metric proxies sections are reasonably clear; the paper becomes opaque exactly where it matters most — the actual aggregation and gradient modules.

**Value to community:** The paper's idea has potential value, but in its current form it cannot serve as a reproducible reference for other researchers.

The paper is fundamentally incomplete: two of its three claimed modules have no algorithmic description. No amount of positive experimental results can compensate for the absence of the method itself. The strongest revision path requires rewriting the core methodology sections from scratch, after which the theoretical and empirical validation can be properly assessed.

MY FINAL SCORE: <pineapple>2.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>